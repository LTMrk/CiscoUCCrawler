---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-webexcc-setupandadministrationguide-2-b-mp-relea-3de98861ec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/webexcc/SetupandAdministrationGuide_2/b_mp-release-2/b_cc-release-2_chapter_0100.html
retrieved_at: 2026-08-16T15:09:30.454214+00:00
---

Cisco Webex Contact Center Setup and Administration Guide

# Cisco Webex Contact Center Setup and Administration Guide

Updated: February 7, 2021

Chapter: Contact Routing

## Chapter: Contact Routing

# Contact Routing

## About Contact Routing

Each contact arrives at an entry point, where a routing strategy applies business logic. Based on the evaluated criteria in
                              the routing strategy, the system selects an appropriate queue to distribute the contact to one of the available teams.

### About Skills-based Routing

Skills-based Routing (SBR) is an optional feature that matches the needs of contacts with agents who have the skills to best
                                 meet those needs. SBR is available for voice contacts as well as digital channel contacts. When calls arrive at an entry point,
                                 SBR classifies the calls into subsets. You can route the calls in each subset to agents who possess a required set of skills,
                                 such as language fluency or product expertise.

SBR assigns skill requirements to calls in a flow. Based on the assigned skill requirements, the calls enter a queue for distribution
                                 to agents who have matching skills. You can configure SBR in a way that removes or reduces the skill requirements of agents
                                 if an agent is not available within a time interval that is specified in the queue. For more information, see Skill Definitions . To remove or reduce the skill requirements, specify the skill relaxations in the Queue Contact activity.

SBR matches all skill requirements of contacts with the skills of agents. If one of the skill requirements of a contact is
                                 invalid because skill values are not properly defined in the flow, SBR cannot find a matching agent. In such cases, the call
                                 is routed to the longest available agent.

SBR provides the following capabilities:

Match skill requirements of contacts with agents who have those specific skills.

Add skill requirements to contacts and route contacts with the same skill requirements to a single queue. For more information,
                                       see Queue Contact activity.

Configure different agent teams with a set of agents to serve a queue. For more information, see Create a Queue and an Outdial Queue .

Map various skills to the profiles of these agents. For more information, see Agent Profiles .

In the preceding example, contact C1 requires skill A and contact C2 requires both skill A and skill B. When C2 enters the
                                 queue, it requires agents with both skill A and skill B. For best customer service, map C2 to the team that has both skill
                                 A and skill B. Do not map C2 to a team that has only skill A or skill B. If you map C2 to a team that has only skill A or
                                 skill B, C2 becomes the longest contact in the parked state.

#### Skills-based Routing Types

SBR routes contacts to agents based on the contact’s skill requirements that are configured in the flow. For more information,
                                    see About Skills-based Routing .

You can enable SBR in the Queue Routing Type settings when creating a queue. For more information, see Create a Queue and an Outdial Queue . SBR routes contacts to agents in one of the following ways when more than one agent with the required skill set is available:

Longest Available Agent

Best Available Agent

Longest Available Agent : SBR routes contacts to the agent who has been available for the longest duration.

Best Available Agent : SBR routes contacts to the agent who has the highest level of proficiency in the skill. To route contacts to the best available
                                    agent:

Configure the contact’s skill requirements with the necessary condition so that the contact is always routed to an agent with
                                          the highest level of proficiency:

If you choose <= condition for the contact’s skill requirements, a lower value indicates a better match with the contact's requirement.

If you choose >= condition for the contact’s skill requirements, a higher value indicates a better match with the contact's requirement.

If you choose IS condition for the contact’s skill requirements, a higher value indicates a better match with the contact's requirement.

For more information, see Skill Requirements in Queue Contact activity.

Assign the proficiency level to an agent when creating Skill Definitions and Agent Profiles .

For example, you can route contacts to agents with English speaking skill as a language proficiency. Consider two agents:
                                    Agent 1 with an English language proficiency level of 3 and Agent 2 with an English language proficiency level of 6. Both
                                    agents are available in the queue.

If you configure the contact’s skill requirement with <= condition in the flow, Agent 1 with an English language proficiency level of 3 is the best available agent in the queue to
                                          connect to the contact.

If you configure the contact’s skill requirement with >= condition in the flow, Agent 2 with an English language proficiency level of 6 is the best available agent in the queue to
                                          connect to the contact.

#### Advanced Queue Information

The Advanced Queue Information feature allows you to assess if the skills of the logged in and available agents in a queue
                                    match the contact's skill requirement without queueing the contacts for a long duration. The GetQueueInfo activity provides the number of agents that are logged on and available. However, this activity doesn't provide information
                                    about any logged in agents who have specific skills that match the requirement of a specific contact. For more information
                                    about the GetQueueInfo activity, see Get Queue Info .

At some time of the day, there may be no agents who are adequately skilled to match the skill requirement of a specific contact.
                                    The administrator needs information about such agents before and after queuing a contact to initiate alternative action such
                                    as playing a message, providing a callback option, or escalating to a different queue.

The administrator can do the following:

If this activity is invoked before queuing the contact, the flow uses the skill requirements that are configured in the Advanced
                                          Queue Information activity and the teams from the last call distribution group. This determines the number of logged in and
                                          available agents and populates the LoggedOnAgentsAll and AvailableAgentsAll output variables. The system sets the output variable CurrentGroup to –1.

A value of -1 for the CurrentGroup indicates that the contact isn't yet queued when the activity is invoked. Flow designers can use the output variable CurrentGroup and determine if the contact isn't queued.

If this activity is invoked after queuing the contact, the system considers the current skills of the contact. The skills
                                          in the current skill relaxation cycle and the teams from the current call distribution group will be used to calculate the
                                          available and logged in agents. These values are populated in the LoggedOnAgentsCurrent and AvailableAgentsCurrent output variables. The system uses skills from the current skill relaxation cycle and the last call distribution group to
                                          calculate logged in and available agents and stores these values in the LoggedOnAgentsAll and AvailableAgentsAll output variables. The system also stores values in the PIQ , CurrentGroup , and TotalGroups output variables.

You can invoke this activity for LAA-based queues. However, skill requirements that are configured for this activity aren't
                                                applicable for LAA-based queues. You can use this activity in a loop. The Flow Designer invokes the Advanced Queue Information
                                                activity when executing the flow.

In the Flow Designer, you can create flows using the Advanced Queue Information activity only if the feature flag is enabled
                                                for this feature. You can't work with flows that have the Advanced Queue Information activity in the Flow Designer, if the
                                                feature flag is disabled. Ensure that the feature flag is enabled for the Advanced Queue Information activity.

As part of the Advanced Queue Information when a contact is parked in a queue and you use the Advanced Queue Information to
                                                query another queue stack, this will not be supported and will result in an error. For more information on the error response
                                                code, see Advanced Queue Information .

#### Escalate Call Distribution Group

The application uses the Escalate Call Distribution Group activity in the post queuing loop to quickly move to the next call distribution group or the last. Typically, administrators
                                    use this activity to identify the contacts that are parked against escalation groups. These escalation groups have at least
                                    one logged in agent who has matching skills or no logged in agents.

The application uses the QueueContact activity and calls the advanced GetQueueInfo activity to determine if there are any
                                    agents logged in to a specific call distribution group. If no agents are logged in to a specific call distribution group,
                                    the flow designer uses the EscalateCallDistribution activity to move ahead to either the next or the last call distribution
                                    group in the series. If an agent is available in the escalated group, Webex Contact Center routes the contact to that agent.
                                    If not, Webex Contact Center parks the contact immediately in that call distribution group.

For more information about the QueueContact activity, see Queue Contact .

A customer use case is a queue that has many call distribution groups. If an agent is not available in the first call distribution
                                    group to answer a call, the flow designer redirects the call to another call distribution group within the queue. At each
                                    level, the number of agents in the call distribution group increases so that there is a greater chance of the call getting
                                    answered. At certain times of the day, agents from this group or other groups might not be available.

For SBR and LAA-based queues, if you invoke the EscalateCallDistribution activity on a contact that is not yet queued, it
                                    results in an error and exits the error path in the flow activity.

Escalate Call Distribution Group is an independent activity. You can use this activity along with the AdvancedQueueInformation and the GetQueueInformation
                                                activities to escalate the call distribution group on a queue. The CheckAgentAvailability parameter in the QueueContact activity results in escalation of call distribution groups. Don't use the EscalateCallDistributionGroup
                                                activity along with the CheckAgentAvailability parameter in the QueueContact activity.

In the Flow Designer, you can create flows using the EscalateCallDistributionGroup activity only if the feature flag is enabled
                                                for this feature. You can't work with flows that have the EscalateCallDistributionGroup activity in the Flow Designer, if
                                                the feature flag is disabled. Ensure that the feature flag is enabled for the EscalateCallDistributionGroup activity.

### Routing of Parked Contacts

SBR parks contacts in a queue until an agent connects with the contacts.

When agents become available, SBR routes contacts by using one of the following selection methods:

Skills-based Contact Selection

First In, First Out (FIFO) based Contact Selection

By default, Skills-based contact selection is enabled for your organization.

#### Skills-based Contact Selection

In skills-based contact selection, contacts are selected based on the exact match between the skill requirements of the contact
                                 and the skills of the agent. Skills-based contact selection does not assign contacts to agents on FIFO basis. If the contact's
                                 skill requirements match exactly with the agent's skill, the contact connects to the agent irrespective of its position in
                                 the queue. If there are many such contacts with the same skill requirements, skills-based contact selection filters contacts
                                 in the queue and assigns them to the agent in the following order:

Priority

Timestamp (oldest to newest)

For example, consider that contact C1 which requires an agent with skill A and contact C2 which requires an agent with skill
                                 B are waiting in the queue to connect to an agent. Contact C3 which requires an agent with skill C also enters the queue.
                                 If an agent with skill C becomes available, C3 does not wait for C1 and C2 to connect to agents, as the skill requirements
                                 of C3 match exactly with the agent who has skill C.

#### First In, First Out (FIFO) based Contact Selection

The first contact that enters the queue has the highest priority to connect to an agent. The first contact connects to an
                                 agent when an agent with matching skills becomes available. If the agent’s skill does not match the skill requirement of the
                                 first contact that is parked in the queue, the agent does not connect to the first contact. Even though the agent’s skill
                                 matches the skill requirements of other contacts in the queue, the contacts remain parked until the first contact finds an
                                 agent.

For example, consider two contacts: C1 is the first contact to enter the queue which requires an agent with skill A and C2
                                 is the second contact to enter the queue which requires an agent with skill B. When an agent with skill B becomes available,
                                 C2 does not connect to skill B. Since C1 is the first contact to enter the queue, SBR waits for an agent with skill A to be
                                 available to connect to C1 first. C2 connects to skill B only after C1 finds an agent.

To enable FIFO-based contact selection for your organization, contact Cisco Support.

### Set Up Skills-Based Routing

Step 1

Define the skills. For more information, see Skill Definitions .

Step 2

Define the skill profiles. For more information, see Skill Profiles .

Step 3

Assign the skill profiles to agents. You can assign a skill profile to an individual agent. Currently, you cannot assign a
                                          skill profile to a team. For more information, see View the Details of a User .

Step 4

Create a queue with a channel type as Telephony and Queue Routing Type as Skills-Based.

Step 5

Create a flow that defines how to treat the call. For more information, see Create and Manage Flows .

Step 6

Add a Queue Contact activity and select the queue for which Skills-Based Routing is configured. For more information, see Queue Contact .

Step 7

Create an entry point routing strategy and select the flow that you created. For more information, see Create a routing strategy .

### Agent-based Routing

Agent-based Routing is an optional feature that routes or queues a contact to the preferred agent directly. An agent lookup
                              with agent's email address or agent's ID routes a contact to the preferred agent. The Queue To Agent activity in the flow
                              helps to achieve Agent-based Routing. For more information, see the section Queue To Agent activity.

A contact can have one or more preferred agents. The mapping between the contacts and their preferred agents is managed in
                              an external application outside Webex Contact Center. The preferred agent lookup for any contact is performed using the HTTP
                              Request activity in the flow. The HTTP Request activity retrieves the mapping from the external application. To route or park
                              the contact against that preferred agent, you can configure the Queue To Agent activity in the flow. The Queue To Agent activity
                              allows you to specify the agent by their Webex Contact Center agent ID or email address. You can also park the contact against
                              a preferred agent if that preferred agent isn't immediately available.

You can consider chaining an activity within the flow to route or queue contacts.

For example, you can chain one Queue To Agent activity to another Queue To Agent activity to queue a contact to multiple preferred
                              agents. You can chain a Queue Contact activity to the Queue To Agent activity to route a contact if none of the preferred agents are available for that contact.

Agent-based Routing is useful in the following scenarios:

Preferred agent routing : The customer can assign contacts to dedicated agents or relationship executives. In such scenarios, the Agent-based Routing
                                    routes the contacts directly to that preferred agent.

Last agent routing : When a contact calls back the contact center multiple times to interact with an agent, Agent-based Routing can route the
                                    contact to the last agent who handled that contact.

In both use cases, the details of the contact and the agent mapping are stored outside the Webex Contact Center. The HTTP
                              activity retrieves the data. The Queue To Agent activity routes the contact to the preferred agent or the last agent.

To set up Agent-based Routing:

Before you begin:

You must export the Webex Contact Center agent ID and agent email address from Webex Contact Center to an external application.
                              Webex Contact Center doesn't store the mapping between the agent and its contacts.

Retrieve the mapping between the agent and the contact from the external application using the HTTP Request activity in the
                                    Flow Designer (From the Management Portal navigation bar, choose Routing Strategy > Flow and click New to create a new flow). For more information, see the section HTTP Request .

Configure the Queue To Agent Activity in the Flow Designer. You can provide the general settings and the contact handling
                                    details to route the contact. For more information, see the section Queue To Agent activity.

## Configure Multimedia Profiles

If your enterprise uses social channels, chat, and email routing in addition to voice, then Multimedia profiles are enabled.
                              You can associate sites and agents with multimedia profiles.

Step 1

Define the multimedia profiles. If your enterprise subscribes to the Multimedia feature, each agent is associated with a multimedia
                                       profile, which specifies how many contacts of each media type the agent can handle concurrently. For more information, see Multimedia Profiles .

Step 2

Assign multimedia profiles to sites, teams, or agents. When Multimedia
                                       is enabled, every site is associated with a multimedia profile. Each agent-based team at a
                                       given site is associated with the profile assigned to that site unless the team is
                                       assigned a different multimedia profile. Similarly, each agent logged in to a team is
                                       associated with the team's profile unless the agent is assigned a different multimedia
                                       profile. For more information, see Sites , Create a team , and Users .

Step 3

Create separate entry points and queues for each media type. For more information, see Create an Entry Point .

Step 4

Work with Webex Contact Center Operations to create routing strategies configured to use a specialized call control script.

Step 5

Work with your specific CRM vendor to configure the multimedia interaction at the agent level.

Alternately you can configure the queue routing strategy to assign multimedia contacts (Chat, Email, Social Channels) to your
                                          agents.

## Working with Resource Files

To view the resources, choose Routing Strategy from the Management Portal navigation bar.

You can choose to see the audio files, predefined emails, or predefined chat responses.

### Upload an Audio Resource File

Webex Contact Center supports uploading .wav audio files with the following specifications:

Channels: 1

Sample Rate: 8000

Sample Encoding: 8-bit u-law

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Audio Files .

Step 3

Click New .

Step 4

On the Upload Resource page, click Browse .

Step 5

Navigate to the file in your system, and click Open .

The File field displays the path and file name of the uploaded file, and the Resource Name field displays the file name.

Step 6

Click Save .

### Edit an Audio Resource File

Do not update resources that are currently used by the system.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Audio Files .

Step 3

Click the Ellipsis button beside the resource name and click Edit .

Step 4

On the Overwrite Resource page, click Browse .

Step 5

Navigate to the file in your system, and click Open .

The File field displays the path and file name of the uploaded file, and the Resource Name field displays the file name.

For audio file specifications, see Upload an Audio Resource File .

Step 6

Click Save .

Step 7

Click Yes to confirm overwriting the audio file.

### Play or Download a .wav File

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Audio Files .

Step 3

Click the ellipsis button beside the file name and click Play .

Step 4

In the dialog box that opens, specify whether you want to open or save the file. When you click Open , the media player installed on your computer opens and plays the file. If a compatible media player is not installed, a dialog
                                          box opens and prompts you to download a player.

### Update a Resource File

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Audio Files .

Step 3

Click the ellipsis button beside the file name and click Edit .

Step 4

Make the necessary changes to the resource.

Step 5

Click Save .

### Copy a Resource File

The copy function enables you to create backup copies of prompts and other resource files. Only files with the .wav extension can be copied.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Audio Files .

Step 3

Click the ellipsis button beside the file name and click Copy .

Step 4

On the page that appears, enter a name for the copied file or leave the default name (Copy_ is prepended to the original name).

Step 5

Click Save .

### Export References to a Media File

You can view or export a list showing the name of each routing strategy that references a specified media file along with
                                 the name of the associated entry point or queue. In the case of a global routing strategy, the list shows 0 instead of the
                                 name of an entry point or queue.

To view or export the references to a media file:

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Audio Files .

Step 3

Click the ellipsis button beside the file name and click Excel or CSV .

Step 4

In the dialog box that opens, specify whether to open or save the file.

### Create a Predefined Email Template

You can predefine the email template that agents use to communicate with customers. An organization can have a single predefined
                                 template for email.

To edit or delete the template, click the ellipsis button beside the template in the Predefined Emails page.

You cannot use the predefined email templates for quick-reply emails.

To create an email template:

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Predefined Emails .

Step 3

Click New .

The New button is disabled if your organization already has a predefined email template.

Step 4

In the New Predefined Email dialog box, do the following:

Enter a name for the email template.

Set the status for the template.

Set the status as Active to use it as a default template for all email communications between agents and customers.

Set the status to Not Active to save it as draft. You can later change the status to Active to use it.

Enter the email body. You can use the formatting tools to draft the email body.

(Optional) Add macros to the email body.

You can use the macro to add variables for Customer Name or Agent Name to the email. You can set a default value for the variable type you choose. You can use the macros multiple times in the
                                                   template as per your requirement.

To add the macro variables, place the cursor where you want the variable. Choose the type of macro you want to add and click
                                                         the Insert to Text Editor button.

To set a default value for a macro, enter the default value in the field Default Value before you insert the macro to the text editor.

Click Save to save the email template.

### Create a Predefined Chat Response

US English

Japanese

Italian

French

German

Spanish

You can configure 50 responses per language, per queue, for a total of 300 responses per queue. Agents can see the responses
                                 in their queue based on the language settings in their local browser. Thus, agents can see only 50 responses at a time.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Predefined Chat Responses .

Step 3

Click New .

Step 4

Enter the following details:

Setting

Description

Response Name

Contains the name of the predefined chat response. You can enter a name of maximum 40 characters.

Status

Contains the status of the predefined chat response. Deactivate the status to hide it from the agents in Agent Desktop.

Language

Choose the language of the predefined chat response from the drop-down list.

You cannot edit the language of the chat reponse.

Queue

Choose the queue for which you want to define the chat response. If you select All from the drop-down list, all agents in
                                                         all the queues in your organization can use the chat response.

However, if any queue has reached the capacity of 50 messages, the system displays an error message with the names of the
                                                         queues that have reached the limit. The system disables the queues that have reached the limit and you cannot choose them.

Content

Contains the text for the chat response. You can enter a maximum of 150 characters.

Step 5

Click Save .

## Configure Routing Strategies

Routing strategies will be obsolete in the future. It is recommended to use flows configured with business hours and outdial
                                       entry points.

If you want to proceed with routing strategies, consider the following aspects. For each entry point and queue, you should
                           create a set of default routing strategies that cover all time intervals. In addition, you can schedule an alternate strategy
                           beyond the default strategy for any time interval. For example, Queue 1 could have a BusyHourStrategy for the normal day shift
                           and an OffHoursStrategy for non-business hours.

Flag the normal daily schedule as the default strategy. You can create a non-default strategy, such as a holiday schedule
                           for a time interval that overlaps the default strategy. A strategy that is not flagged as default overrides a default strategy
                           and is used as an exception to the default schedule. This means that the system first checks for a strategy that is not flagged
                           as default, and if none exists, the system uses the default strategy.

When the default strategy is the current strategy (that is, the strategy that is currently running), the system checks every
                           three minutes for a non-default strategy and if one is found, it becomes the current strategy.

If no strategy is specified for a time interval, and there is no default strategy for the time interval, the last strategy
                           used by the system may continue as the current strategy even though it has expired. In this case, the system checks every
                           minute for a valid strategy and as soon as it finds one, that strategy becomes the current strategy.

### About Team Types

When you create or modify a queue routing strategy, the following options appear:

Agent-Based teams have a known number of agents that are assigned to teams. Authorized users assign an agent profile to one or more teams.
                                    These agents use the Agent Desktop to interface with the Webex Contact Center system.

Capacity-Based teams don’t have specific agents that are assigned to them, and the agents don’t use the Agent Desktop. For example, an outsourcer
                                    could have teams that use a PBX or an ACD to handle calls. You can use a capacity-based team to represent a voicemail box
                                    or an agent group, which Webex Contact Center doesn’t manage.

When you create a routing strategy, you can mix team types. Remember that the accuracy of call routing to capacity-based teams
                              depends on the capacity number specified.

Limitations of Capacity Based Teams

Webex Contact Center assigns calls to the capacity-based team by transferring the call to a Dial Number (DN). After the call
                                 transfers to a DN, Webex Contact Center disconnects from the call. Webex Contact Center isn’t aware of the call status; that
                                 is, whether the capacity-based team answers, handles, or rejects the call.

This limitation causes the following behaviors:

Tracking the contact after the call transfer isn't possible.

Detecting RONA or call failures isn't possible.

Recording the call isn't possible.

Getting the Connect Time and Handled Time values isn't possible. Call report shows the value as zero (0).

Setting the capacity isn't applicable, hence more calls could go to the capacity-based team.

When a static load-balancing strategy includes both agent-based and capacity-based teams, the system doesn't distribute calls
                                          to agent-based teams even if the call volume exceeds the capacity of the capacity-based teams.

### View routing strategies for an entry point or queue

To view all routing strategies for an entry point or queue:

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

Choose an entry point or queue from the Select Entry Point drop-down list to display the routing strategies for that entry point or queue.

For more information on the parameters that display on the Routing Strategy page, see Routing strategy parameters .

The upper section of the list view displays a table that lists all routing strategies available for the selected entry point
                                             or queue.

(Optional) Use the sort button at the end of the table to chronologically sort the strategies.

Step 3

To see details for a strategy, click the ellipsis beside the routing strategy and click Edit .

The lower section of the Routing Strategy page displays the Routing Strategy Mapping Details table, which:

lists destination queues and entry points, which are based on the active routing strategies that you define for the selected
                                                   entry point.

lists the teams to which the system routes calls, chats, or emails, which are based on the active routing strategies that
                                                   you define for the selected queue. Mapping details aren't provided for a queue routing strategy that simply redirects the
                                                   call to another entry point or queue.

Your access privileges determine what you see in the Mapping Details table. For example, if the system routes calls for the
                                                               Sales queue to Teams A and B, and you have access rights only to Team A, the mapping table shows only Team A as the destination
                                                               for incoming calls.

Step 4

Click Save .

#### Routing strategy parameters

The following table describes the parameters that appear on the Routing Strategy page.

Column

Description

Name

Displays the name you assign to the strategy. You can't change the strategy name after you create it.

ID

Displays the system-assigned number of the strategy.

Status

Indicates the status of the strategy.

Current (appears in Red) means this is a snapshot of the currently running strategy. You can't copy the current strategy, but you
                                                      can modify any setting that does not affect execution time or date. Changes to the strategy don't affect the recurring scheduled
                                                      version of the strategy.

You can delete the current strategy, but don't delete it before you create a different strategy for the same time interval.
                                                                  If you delete a strategy without having another one in place, the last strategy used by the system becomes the default strategy
                                                                  although the start and end times and dates have expired. If this occurs, either create a new strategy for the current time
                                                                  period, or copy the default strategy and correct the time settings.

Active means that the strategy is in effect at the specified start time on the specified start date. This is the default status.

Not Active means the strategy isn't in effect regardless of the specified start time and date. This status lets you save a strategy for
                                                      future use or as a draft to continue with later.

Default

Indicates whether the strategy is the default. A strategy not flagged as the default overrides a default strategy and potentially
                                                replaces the default schedule.

Chat Template

Identifies the chat template used for the routing strategy.

Repetition

Specifies whether the strategy repeats daily or only on specific days of the week.

Start Date

Displays the date on which the strategy starts.

End Date

Displays the date on which the strategy ends.

Start Time

Displays the time at which the strategy starts (in 24-hour format) for any given day in the specified date range.

End Time

Displays the time at which the strategy ends (in 24-hour format) for any given day in the specified date range.

Time Zone

Displays the time zone if you enable the Multiple Time Zone feature when you create the entry point or queue.

Flow

Lists the associated call flows when a routing strategy is executing.

### View the current routing strategies

You can view a list of currently deployed routing strategies for multiple entry points or queues.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

From the Routing Strategy page, choose Resources > Current Routing Strategies .

Step 3

Choose All from the drop-down list to view current strategies for all entry points or queues.

Step 4

Click Apply .

table provides details about the current routing strategies for the selected entry points or queues. The Flow column displays the
                                             names of the call flows associated with the listed entry points or queues.

### View routing strategies by time zone

If you enable the Multiple Time Zone feature for your enterprise, you can configure entry points and queues with time zones.
                                 Time values that are used in the routing strategies are based on the time zone you configure for the entry point or queue.
                                 If you don't configure time zones with entry points and queues, the system uses the time zone that you configure for your
                                 enterprise (typically headquarters).

When you click your name button on the upper-right side of the Routing Strategy page, any time zones you configure for entry points or queues appear in a drop-down list.

If you do not enable the Multiple Time Zone feature for your enterprise, time values in routing strategies are based on the
                                 time zone you configure for your enterprise.

If the time zone observes daylight-saving time, the time adjusts automatically when the daylight-saving time changes.

Step 1

On the Management Portal, click the gears icon in the upper-right corner to view the three or four Tab keyed settings panel.

Step 2

Click the gears icon. Select a time zone from the Time Zone drop-down list.

Step 3

Click Apply .

Step 4

From the Management Portal navigation bar, choose Routing Strategy to view the routing strategies based on the selected time zone.

### Create a routing strategy

Use this procedure to create new routing strategies. You can also create a new strategy by editing an existing strategy.

Before you create new strategies:

Always create an active strategy for every time interval. If you don't specify an active strategy for a time interval, the
                                       system uses the default. If there’s no default strategy, the last strategy that the system used may continue as the current
                                       strategy although it has expired.

You can easily create a new strategy from an existing strategy, change some settings, and save it as a new strategy.

You can have only one routing strategy for each email entry point.

You can't save changes to an active strategy when the scheduled dates or times conflict with an existing active strategy.

#### Before you begin

You must Create a Chat Template before you create a Chat Routing Strategy.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

At the Routing Strategy page, choose Routing > Routing Strategies .

Step 3

Choose an entry point from the Select Entry Point drop-down list.

Step 4

Do one of the following in the list view:

Click New Strategy .

Global Routing Overrides only apply to Telephony channel type.

- OR -

Click the ellipsis button beside an existing routing strategy with Active status and click Copy .

Step 5

Enter or modify the settings as described in the following tables.

You can create more than one strategy for a Telephony channel.

Setting

Description

General Settings

Name

Enter a name for the strategy, such as US Holiday or Weekends. You can’t edit this field after you save the strategy.

Enterprise Name

Shows the tenant name.

Status

Click Active if you want the strategy to become effective on the start date that you specify in the Start Date field.

Click Not Active if you want to save the strategy for future use or as a draft to work on later.

The status is always Active for chat and email routing strategies as you can configure only one routing strategy for each entry point or queue.

Setting

Description

Time Settings (These are read-only for proxy queues.)

Start Date

End Date

Click in each of these fields and use the calendar controls to specify the start date (the date that the strategy becomes
                                                         effective) and the end date (the date that the strategy expires).

Start Time

End Time

Enter in 24-hour format (0000–2400) the time of day that you want the strategy to start and end.

Day of Week

From the drop-down list, choose All Days if you want to schedule the strategy for every day or Weekdays if you want to schedule the strategy for Monday through Friday only.

-OR-

Click each icon that represents a day on which you want to schedule the strategy.

Advanced Settings

Music on Hold

Select the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ.

Call Control

Flag as Default Routing Strategy

-or-

Update as Default Routing Strategy

Choose the Routing Strategy. This setting is available only if you create a new strategy or copy an existing one.

Set to Yes if you want this routing strategy to be the default routing strategy for the specified time interval for this entry point
                                                         or queue.

Set to No to create an exception to the default schedule, such as a holiday. This strategy overrides the default strategy. That is,
                                                         the system first checks for a strategy that isn’t flagged as default, and if none exists, the system uses the default strategy.

Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time:

1. Global Routing Overrides

2. Default Global Routing Overrides

3. Routing Strategy

4. Default Routing Strategy

Flow

Select the flow from the drop-down list.

Setting

Description

Email Account

You can add only one email account for each entry point. You can edit or delete the email account using the icons beside the
                                                         email account name.

Add Email Account

Click the Add Email Account button to open the Add Email Account dialog box. Enter the following details:

Incoming Protocol

Incoming Host

Inbound Encryption

Inbound Port Number

SMTP Server

Outbound Encryption

Outbound Port Number

Ensure you use only secure access to mail servers, such as:

SMTP, IMAP, or POP over SSL

SMTP, IMAP, or POP over TLS

Mandatory steps to use a Gmail account for an email channel are as follows:

Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings.

Enable the Less Secure Apps flag in the Gmail account settings.

Disable the captcha by logging into https://g.co/allowaccess .

Update the credentials in the routing strategy and click Save .

Maximum Attachment Size

Number of Attachment Limit

Mail Delay

Maximum Messages/Cycle

Email Routing Rules

You can add up to 20 email routing rules. Use the icon beside the rule to edit or delete the rule.

Routing Rule

Click the Add Routing Rule button to open the Add Routing Rule dialog box. Enter the following details to add a rule:

The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center.

Default Routing Rule

Select an email queue for the default routing rule in case none of the defined rules satisfy the criteria.

### Modify a Routing Strategy

Before you modify a routing strategy, be aware of the following:

Although you cannot copy the current strategy, you can modify any of its settings except those that affect execution time
                                       or date. These changes have no effect on the recurring scheduled version of the strategy.

When you modify the current strategy, your changes take effect immediately for new calls and remain in effect until the current
                                       strategy ends. If there are calls in the queue when the modifications are made, the existing queued calls follow the original
                                       strategy unless you check the Apply changes to current calls in queue check box to the right of the Save button.

Changes made to the current Email or Chat entry point routing strategy are also applied to the corresponding active routing
                                                   strategies.

When you modify a strategy that is not the current strategy, your changes take effect according to the scheduled times specified
                                       in the strategy.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

On the Routing Strategy page, choose an entry point or queue from the Select Entry Point/Queue drop-down list.

Step 3

Click the ellipsis button beside the strategy that you want to modify and choose Edit .

Step 4

Make your changes. For information about each setting, see the setting descriptions table in Create a routing strategy .

Step 5

If you modify the current strategy and want the changes to apply to calls currently in queue, check the Apply changes to current calls in queue check box on the lower right side of the page. If you don't check this check box, the changes only apply to new calls.

Step 6

Click Save to save your changes.

### Routing Strategies Deletion and Restoration

When you delete a routing strategy, the system moves the strategy to the Deleted Routing Strategies or Deleted Global Routing Overrides page where it can be restored or permanently deleted within 30 days. After 30 days, the system permanently deletes the routing
                              strategy.

When you delete a current strategy, the system activates the next strategy scheduled for that time period. Do not delete a
                                          current strategy unless an alternate strategy is available.

#### Delete a Standard Routing Strategy

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

On the Routing Strategy page, choose an entry point or queue from the Select Entry Point/Queue drop-down list.

Step 3

Click the ellipsis button beside the routing strategy that you want to delete and click Delete .

Step 4

Click Yes to confirm.

The system moves the strategy to the Deleted Routing Strategies page where it can be restored or permanently deleted (see Restore or Permanently Delete a Routing Strategy ).

#### Restore or Permanently Delete a Routing Strategy

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

Step 2

On the Routing Strategy page, click Deleted Strategies .

Step 3

Choose an entry point or queue from the Select Entry Point/Queue drop-down list.

Step 4

Click the ellipsis button beside the strategy that you want to either restore or permanently delete and do one of the following:

To permanently delete the strategy, click Delete . Click Yes to confirm.

- OR -

To restore the strategy, click Restore .

Step 5

If you are restoring a strategy, modify the settings as required, and click Restore .

You cannot restore a deleted Chat Entry Point Routing Strategy, if a Routing Strategy is assigned to the Entry Point.

If any settings conflict with an existing routing strategy, a message informs you. In this case, you must modify the settings
                                                before you can restore the strategy.

### Audio on Hold

When a call is queued on the network, an audio file continues to play until the call is distributed to a team with available
                              capacity. If the call is queued for longer than the length of the audio content, the audio file loops back and restarts from
                              the beginning.

We recommend that the audio file include a brief delay message followed by music. The message should announce the name of
                              the associated queue, instruct the caller to hold for the next available agent, and include a warning that calls may be monitored.

You can record one audio file for each strategy, so the message can vary by time of day, day of week, holiday schedule, and
                              other factors.

## Working with Global Routing Overrides

A global routing override is a routing strategy that applies to one or more Telephony entry points. When a call arrives at
                           an entry point, the routing engine checks whether a Global Routing Override exists for that entry point. If a Global Routing
                           Override exists, it becomes the current routing strategy for the entry point, overriding any standard routing strategies associated
                           with that entry point.

Creating a global routing override enables you to change the routing strategies quickly and easily for many entry points simultaneously
                           in urgent situations, rather than changing each routing strategy individually.

Global routing overrides operate in the Tenant time zone.

### View global routing overrides

Use this procedure to view a list of global routing overrides .

#### Before you begin

You require Administrator access privileges to perform this procedure.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

The Routing Strategy page opens.

Step 2

From the menu bar, choose Routing > Global Routing Overrides .

The Global Routing Overrides page opens to display the Global Routing Overrides List . This page displays all existing global routing overrides. You can use the Search function at the top-right of the List area to find your target. See Global routing override parameters for a description of the parameters that are visible on the page.

Step 3

(Optional) To export the list of global routing overrides for data analysis, click the ellipsis button near the top-right side of the page and click Excel or CSV .

Step 4

(Optional) To display the details of a routing override or to edit it, click the ellipsis button at the left of the listed override and then click Edit . See Edit a global routing override for further detail on editing a routing override .

### Create global routing overrides

You can change the contact handling flow for multiple telephony entry points  at the same time, such as for a holiday or emergency
                              situation. Preconfigure one or more flows that you can apply quickly as an override when needed. When it becomes active, the
                              global routing override only applies to new calls, while active calls follow the current entry point  routing strategies.

By default, you create global routing overrides in the Tenant time zone. All the data that are displayed on the Global Routing Overrides page or dashboard are based on the Tenant time zone.

You can choose between two methods to create a global routing override :

#### Create a global routing override

Use this procedure to create a global routing override .

##### Before you begin

You require Administrator access privileges to perform this procedure.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

The Routing Strategy page opens.

Step 2

From the menu bar, choose Routing > Global Routing Overrides .

The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides.

Step 3

From the Global Routing Overrides page, click + New Override .

The Create Global Routing Override page opens.

Step 4

Configure the new global routing override as described in Global routing override parameters .

Step 5

Click Save or Cancel .

#### Create a global routing override from a copy

Use this procedure to create a global routing override from a copy of an existing override .

##### Before you begin

You require Administrator access privileges to perform this procedure.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

The Routing Strategy page opens.

Step 2

From the menu bar, choose Routing > Global Routing Overrides .

The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides.

Step 3

Locate the global routing override you want to copy to create a new override . You can use the Search function at the top-right of the Global Routing Overrides List area to find your target.

Step 4

Click the ellipsis button to the left of a listed override , and then click Copy .

The Copy Global Routing Override page opens.

Step 5

Change the settings as required, and in accordance with instructions provided in Global routing override parameters .

Step 6

Click Save or Cancel .

### Edit a global routing override

Use this procedure to edit an existing global routing override .

#### Before you begin

You require Administrator access privileges to perform this procedure.

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

The Routing Strategy page opens.

Step 2

From the menu bar, choose Routing > Global Routing Overrides .

The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides .

Step 3

Locate the global routing override you want to edit. You can use the Search function at the top-right of the Global Routing Overrides List area to find your target.

Step 4

Click the ellipsis button at the left of the entry point you want to modify, and then click Edit .

The Overwrite Global Routing Override page opens.

Step 5

Edit the routing override parameters in accordance with the information provided in Global routing override parameters .

Step 6

Click Save or Cancel .

### Global routing override parameters

#### Parameters for Global Routing Overrides page

The following table lists and describes the parameters you see in the Global Routing Overrides List area on the Global Routing Overrides page.

Column

Description

Name

Displays the name you assign to the override . You can't change the override name after you create it.

ID

Displays the system-assigned number of the override .

Status

Indicates the status of the override .

Current (appears in Red) means this is a snapshot of the currently running override . You can't copy the current override , but you can modify any setting that doesn't affect execution time or date. Changes to the override don't affect the recurring scheduled version of the override .

You can delete the current override , but don't delete it before you create a different override for the same time interval. If you delete an override without having another one in place, the last override used by the system becomes the default override although the start and end times and dates have expired. If this occurs, either create a new override for the current time period, or copy the default override and correct the time settings.

Active means that the override is in effect at the specified start time on the specified start date. This is the default status.

Not Active means the override isn't in effect regardless of the specified start time and date. This status lets you save an override for future use or as a draft to continue with later.

Default

Indicates whether the global routing override is the default routing strategy ( Yes ) or isn't the default routing strategy ( No ).

Repetition

Specifies whether the override repeats daily or only on specific days of the week.

Start Date

Displays the date on which the override starts.

End Date

Displays the date on which the override ends.

Start Time

Displays the time at which the override starts (in 24-hour format) for any given day in the specified date range.

End Time

Displays the time at which the override ends (in 24-hour format) for any given day in the specified date range.

Time Zone

Displays the Tenant time zone.

Global routing overrides operate in the Tenant time zone.

Flow

Lists the associated call flows when a routing override is executing.

#### Parameters for Create, Overwrite, Copy, and Restore Gobal Routing Override pages

The following table lists and describes the parameters that you see on the:

Create Global Routing Override page

Overwrite Global Routing Override page

Copy Global Routing Override page

Restore Global Routing Override page

Use this information to configure new or copied overrides and edit existing ones.

Description

General Settings

Name

Enter the name for the global routing override . You can't change the name after it's created.

If you copy an override , you can change the name of the copy.

Enterprise Name

Displays the name of the Tenant.

Channel Type

Displays the only valid channel type: Telephony

Entry Points

This field appears only if you are creating or copying a global routing override .

Choose the entry points to which the global routing override applies.

Status

Click the Status toggle button to set the status of the global routing override to either Active or Not Active .

When set to Active , the routing override activates and deactivates on the dates and at the times specified in the related Start and End Date and Start and End  Time
                                             fields.

Time Settings

Time zone

Displays the Tenant time zone.

Global routing overrides operate in the Tenant time zone.

Start Date

End Date

Click in each of these fields and use the calendar controls to specify the start date (the date the global routing override becomes effective) and end date (the date the global routing override expires).

Start Time

End Time

Enter in 24-hour format (0000–2400) the time of day you want the global routing override to start and end.

Day of Week

From the drop-down list:

Choose All Days if you want to schedule the global routing override to run every day.

Choose Weekdays if you want to schedule the global routing override to run from Monday through Friday only.

Choose Specific Days , and click the icons representing weekdays if you want to schedule the global routing override to run on specific days of the week.

Advanced Settings

Music on Hold

From the drop-down list, choose the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music
                                             in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ.

Flag as Default Routing Strategy

This setting is available only if you create a new override or copy an existing one.

Set to Yes if you want this global routing override to be the default global routing override for the specified time interval for this entry point.

Set to No to create an exception to the default schedule, such as a holiday. This override overrides the default override . That is, the system first checks for a override that isn’t flagged as default, and if none exists, the system uses the default override .

You can configure different routing strategies for a given time interval. However, Webex Contact Center prioritizes only one
                                                         routing strategy. Webex Contact Center uses the following order of prioritization to decide the current routing strategy at
                                                         any given time:

1. Global Routing Overrides

2. Default Global Routing Overrides

3. Routing Strategy

4. Default Routing Strategy

Call Control

Flow

Choose a flow to override the contact handling behavior for the selected entry points during the configured time period.

### Delete a global routing override

Use this procedure to delete a global routing strategy.

#### Before you begin

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

The Routing Strategy page opens.

Step 2

From the menu bar, choose Routing > Global Routing Overrides .

The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides. See Global routing override parameters for a description of the elements that are visible on the page.

Step 3

Locate the global routing override you want to edit. You can use the Search function at the top-right of the Global Routing Overrides List area to find your target.

Step 4

Click the ellipsis button to the left of the routing override you want to delete, then click Delete . In the confirmation dialog box that opens, click OK .

The routing override moves to the Deleted Global Routing Overrides page where it awaits restoration or permanent deletion. For more information, see Restore or Permanently Delete a Routing Strategy .

### Restore or permanently delete a global routing override

Use this procedure to restore or permanently delete a global routing override .

#### Before you begin

Step 1

From the Management Portal navigation bar, choose Routing Strategy .

The Routing Strategy page opens.

Step 2

From the menu bar, choose Routing > Global Routing Override .

The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides. See Global routing override parameters for a description of the parameters that are visible on the page.

Step 3

Click the Deleted Global Routing Overrides button at the top-right side of the page.

The Deleted Global Routing Overrides page opens displaying a list of deleted routing overrides , if any exist.

Step 4

In the Deleted Global Routing Overrides List view, locate the routing override you want to either restore or permanently delete. You can use the Search function at the far-right of the page to locate your target.

Step 5

Click the ellipsis button to the left of the routing override you want to either restore or permanently delete and do one of the following:

(Optional) To permanently delete the override , click the Delete icon. Click Yes in the confirmation dialog box to commit.

The Deleted Global Routing Overrides page immediately refreshes, excluding the deleted routing override .

(Optional) To restore the override , click the Restore icon. Click Yes in the confirmation dialog box to commit.

The Restore Global Routing Override page appears, displaying the settings for the routing override .

You can change some of the settings in accordance with the information that is provided in Global routing override parameters .

Click Restore to save changes and confirm reactivation of the override .

If any settings conflict with an existing routing override , a message informs you. In this case, you must modify the settings before the override restores.

The Deleted Global Routing Overrides page immediately refreshes, excluding the restored routing override .

| Note | A value of -1 for the CurrentGroup indicates that the contact isn't yet queued when the activity is invoked. Flow designers can use the output variable CurrentGroup and determine if the contact isn't queued. |
|---|---|

| Note | You can invoke this activity for LAA-based queues. However, skill requirements that are configured for this activity aren't
                                                applicable for LAA-based queues. You can use this activity in a loop. The Flow Designer invokes the Advanced Queue Information
                                                activity when executing the flow. In the Flow Designer, you can create flows using the Advanced Queue Information activity only if the feature flag is enabled
                                                for this feature. You can't work with flows that have the Advanced Queue Information activity in the Flow Designer, if the
                                                feature flag is disabled. Ensure that the feature flag is enabled for the Advanced Queue Information activity. |
|---|---|

| Note | As part of the Advanced Queue Information when a contact is parked in a queue and you use the Advanced Queue Information to
                                                query another queue stack, this will not be supported and will result in an error. For more information on the error response
                                                code, see Advanced Queue Information . |
|---|---|

| Note | Escalate Call Distribution Group is an independent activity. You can use this activity along with the AdvancedQueueInformation and the GetQueueInformation
                                                activities to escalate the call distribution group on a queue. The CheckAgentAvailability parameter in the QueueContact activity results in escalation of call distribution groups. Don't use the EscalateCallDistributionGroup
                                                activity along with the CheckAgentAvailability parameter in the QueueContact activity. In the Flow Designer, you can create flows using the EscalateCallDistributionGroup activity only if the feature flag is enabled
                                                for this feature. You can't work with flows that have the EscalateCallDistributionGroup activity in the Flow Designer, if
                                                the feature flag is disabled. Ensure that the feature flag is enabled for the EscalateCallDistributionGroup activity. |
|---|---|

| Note | By default, Skills-based contact selection is enabled for your organization. |
|---|---|

| Note | To enable FIFO-based contact selection for your organization, contact Cisco Support. |
|---|---|

| Step 1 | Define the skills. For more information, see Skill Definitions . |
|---|---|
| Step 2 | Define the skill profiles. For more information, see Skill Profiles . |
| Step 3 | Assign the skill profiles to agents. You can assign a skill profile to an individual agent. Currently, you cannot assign a
                                          skill profile to a team. For more information, see View the Details of a User . |
| Step 4 | Create a queue with a channel type as Telephony and Queue Routing Type as Skills-Based. |
| Step 5 | Create a flow that defines how to treat the call. For more information, see Create and Manage Flows . |
| Step 6 | Add a Queue Contact activity and select the queue for which Skills-Based Routing is configured. For more information, see Queue Contact . |
| Step 7 | Create an entry point routing strategy and select the flow that you created. For more information, see Create a routing strategy . |

| Step 1 | Define the multimedia profiles. If your enterprise subscribes to the Multimedia feature, each agent is associated with a multimedia
                                       profile, which specifies how many contacts of each media type the agent can handle concurrently. For more information, see Multimedia Profiles . |
|---|---|
| Step 2 | Assign multimedia profiles to sites, teams, or agents. When Multimedia
                                       is enabled, every site is associated with a multimedia profile. Each agent-based team at a
                                       given site is associated with the profile assigned to that site unless the team is
                                       assigned a different multimedia profile. Similarly, each agent logged in to a team is
                                       associated with the team's profile unless the agent is assigned a different multimedia
                                       profile. For more information, see Sites , Create a team , and Users . |
| Step 3 | Create separate entry points and queues for each media type. For more information, see Create an Entry Point . |
| Step 4 | Work with Webex Contact Center Operations to create routing strategies configured to use a specialized call control script. |
| Step 5 | Work with your specific CRM vendor to configure the multimedia interaction at the agent level. Alternately you can configure the queue routing strategy to assign multimedia contacts (Chat, Email, Social Channels) to your
                                          agents. |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Audio Files . |
| Step 3 | Click New . |
| Step 4 | On the Upload Resource page, click Browse . |
| Step 5 | Navigate to the file in your system, and click Open . The File field displays the path and file name of the uploaded file, and the Resource Name field displays the file name. |
| Step 6 | Click Save . |

| Note | Do not update resources that are currently used by the system. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Audio Files . |
| Step 3 | Click the Ellipsis button beside the resource name and click Edit . |
| Step 4 | On the Overwrite Resource page, click Browse . |
| Step 5 | Navigate to the file in your system, and click Open . The File field displays the path and file name of the uploaded file, and the Resource Name field displays the file name. For audio file specifications, see Upload an Audio Resource File . |
| Step 6 | Click Save . |
| Step 7 | Click Yes to confirm overwriting the audio file. |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Audio Files . |
| Step 3 | Click the ellipsis button beside the file name and click Play . |
| Step 4 | In the dialog box that opens, specify whether you want to open or save the file. When you click Open , the media player installed on your computer opens and plays the file. If a compatible media player is not installed, a dialog
                                          box opens and prompts you to download a player. |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Audio Files . |
| Step 3 | Click the ellipsis button beside the file name and click Edit . |
| Step 4 | Make the necessary changes to the resource. |
| Step 5 | Click Save . |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Audio Files . |
| Step 3 | Click the ellipsis button beside the file name and click Copy . |
| Step 4 | On the page that appears, enter a name for the copied file or leave the default name (Copy_ is prepended to the original name). |
| Step 5 | Click Save . |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Audio Files . |
| Step 3 | Click the ellipsis button beside the file name and click Excel or CSV . |
| Step 4 | In the dialog box that opens, specify whether to open or save the file. |

| Note | You cannot use the predefined email templates for quick-reply emails. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Predefined Emails . |
| Step 3 | Click New . Note The New button is disabled if your organization already has a predefined email template. | Note | The New button is disabled if your organization already has a predefined email template. |
| Note | The New button is disabled if your organization already has a predefined email template. |
| Step 4 | In the New Predefined Email dialog box, do the following: Enter a name for the email template. Set the status for the template. Set the status as Active to use it as a default template for all email communications between agents and customers. Set the status to Not Active to save it as draft. You can later change the status to Active to use it. Enter the email body. You can use the formatting tools to draft the email body. (Optional) Add macros to the email body. You can use the macro to add variables for Customer Name or Agent Name to the email. You can set a default value for the variable type you choose. You can use the macros multiple times in the
                                                   template as per your requirement. To add the macro variables, place the cursor where you want the variable. Choose the type of macro you want to add and click
                                                         the Insert to Text Editor button. To set a default value for a macro, enter the default value in the field Default Value before you insert the macro to the text editor. Click Save to save the email template. |

| Note | The New button is disabled if your organization already has a predefined email template. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Predefined Chat Responses . |
| Step 3 | Click New . |
| Step 4 | Enter the following details: Setting Description Response Name Contains the name of the predefined chat response. You can enter a name of maximum 40 characters. Status Contains the status of the predefined chat response. Deactivate the status to hide it from the agents in Agent Desktop. Language Choose the language of the predefined chat response from the drop-down list. You cannot edit the language of the chat reponse. Queue Choose the queue for which you want to define the chat response. If you select All from the drop-down list, all agents in
                                                         all the queues in your organization can use the chat response. However, if any queue has reached the capacity of 50 messages, the system displays an error message with the names of the
                                                         queues that have reached the limit. The system disables the queues that have reached the limit and you cannot choose them. Content Contains the text for the chat response. You can enter a maximum of 150 characters. | Setting | Description | Response Name | Contains the name of the predefined chat response. You can enter a name of maximum 40 characters. | Status | Contains the status of the predefined chat response. Deactivate the status to hide it from the agents in Agent Desktop. | Language | Choose the language of the predefined chat response from the drop-down list. You cannot edit the language of the chat reponse. | Queue | Choose the queue for which you want to define the chat response. If you select All from the drop-down list, all agents in
                                                         all the queues in your organization can use the chat response. However, if any queue has reached the capacity of 50 messages, the system displays an error message with the names of the
                                                         queues that have reached the limit. The system disables the queues that have reached the limit and you cannot choose them. | Content | Contains the text for the chat response. You can enter a maximum of 150 characters. |
| Setting | Description |
| Response Name | Contains the name of the predefined chat response. You can enter a name of maximum 40 characters. |
| Status | Contains the status of the predefined chat response. Deactivate the status to hide it from the agents in Agent Desktop. |
| Language | Choose the language of the predefined chat response from the drop-down list. You cannot edit the language of the chat reponse. |
| Queue | Choose the queue for which you want to define the chat response. If you select All from the drop-down list, all agents in
                                                         all the queues in your organization can use the chat response. However, if any queue has reached the capacity of 50 messages, the system displays an error message with the names of the
                                                         queues that have reached the limit. The system disables the queues that have reached the limit and you cannot choose them. |
| Content | Contains the text for the chat response. You can enter a maximum of 150 characters. |
| Step 5 | Click Save . |

| Setting | Description |
|---|---|
| Response Name | Contains the name of the predefined chat response. You can enter a name of maximum 40 characters. |
| Status | Contains the status of the predefined chat response. Deactivate the status to hide it from the agents in Agent Desktop. |
| Language | Choose the language of the predefined chat response from the drop-down list. You cannot edit the language of the chat reponse. |
| Queue | Choose the queue for which you want to define the chat response. If you select All from the drop-down list, all agents in
                                                         all the queues in your organization can use the chat response. However, if any queue has reached the capacity of 50 messages, the system displays an error message with the names of the
                                                         queues that have reached the limit. The system disables the queues that have reached the limit and you cannot choose them. |
| Content | Contains the text for the chat response. You can enter a maximum of 150 characters. |

| Note | Routing strategies will be obsolete in the future. It is recommended to use flows configured with business hours and outdial
                                       entry points. |
|---|---|

| Note | When a static load-balancing strategy includes both agent-based and capacity-based teams, the system doesn't distribute calls
                                          to agent-based teams even if the call volume exceeds the capacity of the capacity-based teams. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | Choose an entry point or queue from the Select Entry Point drop-down list to display the routing strategies for that entry point or queue. For more information on the parameters that display on the Routing Strategy page, see Routing strategy parameters . The upper section of the list view displays a table that lists all routing strategies available for the selected entry point
                                             or queue. Note (Optional) Use the sort button at the end of the table to chronologically sort the strategies. | Note | (Optional) Use the sort button at the end of the table to chronologically sort the strategies. |
| Note | (Optional) Use the sort button at the end of the table to chronologically sort the strategies. |
| Step 3 | To see details for a strategy, click the ellipsis beside the routing strategy and click Edit . The lower section of the Routing Strategy page displays the Routing Strategy Mapping Details table, which: lists destination queues and entry points, which are based on the active routing strategies that you define for the selected
                                                   entry point. lists the teams to which the system routes calls, chats, or emails, which are based on the active routing strategies that
                                                   you define for the selected queue. Mapping details aren't provided for a queue routing strategy that simply redirects the
                                                   call to another entry point or queue. Note Your access privileges determine what you see in the Mapping Details table. For example, if the system routes calls for the
                                                               Sales queue to Teams A and B, and you have access rights only to Team A, the mapping table shows only Team A as the destination
                                                               for incoming calls. | Note | Your access privileges determine what you see in the Mapping Details table. For example, if the system routes calls for the
                                                               Sales queue to Teams A and B, and you have access rights only to Team A, the mapping table shows only Team A as the destination
                                                               for incoming calls. |
| Note | Your access privileges determine what you see in the Mapping Details table. For example, if the system routes calls for the
                                                               Sales queue to Teams A and B, and you have access rights only to Team A, the mapping table shows only Team A as the destination
                                                               for incoming calls. |
| Step 4 | Click Save . |

| Note | (Optional) Use the sort button at the end of the table to chronologically sort the strategies. |
|---|---|

| Note | Your access privileges determine what you see in the Mapping Details table. For example, if the system routes calls for the
                                                               Sales queue to Teams A and B, and you have access rights only to Team A, the mapping table shows only Team A as the destination
                                                               for incoming calls. |
|---|---|

| Column | Description |
|---|---|
| Name | Displays the name you assign to the strategy. You can't change the strategy name after you create it. |
| ID | Displays the system-assigned number of the strategy. |
| Status | Indicates the status of the strategy. Current (appears in Red) means this is a snapshot of the currently running strategy. You can't copy the current strategy, but you
                                                      can modify any setting that does not affect execution time or date. Changes to the strategy don't affect the recurring scheduled
                                                      version of the strategy. Note You can delete the current strategy, but don't delete it before you create a different strategy for the same time interval.
                                                                  If you delete a strategy without having another one in place, the last strategy used by the system becomes the default strategy
                                                                  although the start and end times and dates have expired. If this occurs, either create a new strategy for the current time
                                                                  period, or copy the default strategy and correct the time settings. Active means that the strategy is in effect at the specified start time on the specified start date. This is the default status. Not Active means the strategy isn't in effect regardless of the specified start time and date. This status lets you save a strategy for
                                                      future use or as a draft to continue with later. | Note | You can delete the current strategy, but don't delete it before you create a different strategy for the same time interval.
                                                                  If you delete a strategy without having another one in place, the last strategy used by the system becomes the default strategy
                                                                  although the start and end times and dates have expired. If this occurs, either create a new strategy for the current time
                                                                  period, or copy the default strategy and correct the time settings. |
| Note | You can delete the current strategy, but don't delete it before you create a different strategy for the same time interval.
                                                                  If you delete a strategy without having another one in place, the last strategy used by the system becomes the default strategy
                                                                  although the start and end times and dates have expired. If this occurs, either create a new strategy for the current time
                                                                  period, or copy the default strategy and correct the time settings. |
| Default | Indicates whether the strategy is the default. A strategy not flagged as the default overrides a default strategy and potentially
                                                replaces the default schedule. |
| Chat Template | Identifies the chat template used for the routing strategy. |
| Repetition | Specifies whether the strategy repeats daily or only on specific days of the week. |
| Start Date | Displays the date on which the strategy starts. |
| End Date | Displays the date on which the strategy ends. |
| Start Time | Displays the time at which the strategy starts (in 24-hour format) for any given day in the specified date range. |
| End Time | Displays the time at which the strategy ends (in 24-hour format) for any given day in the specified date range. |
| Time Zone | Displays the time zone if you enable the Multiple Time Zone feature when you create the entry point or queue. |
| Flow | Lists the associated call flows when a routing strategy is executing. |

| Note | You can delete the current strategy, but don't delete it before you create a different strategy for the same time interval.
                                                                  If you delete a strategy without having another one in place, the last strategy used by the system becomes the default strategy
                                                                  although the start and end times and dates have expired. If this occurs, either create a new strategy for the current time
                                                                  period, or copy the default strategy and correct the time settings. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | From the Routing Strategy page, choose Resources > Current Routing Strategies . |
| Step 3 | Choose All from the drop-down list to view current strategies for all entry points or queues. |
| Step 4 | Click Apply . table provides details about the current routing strategies for the selected entry points or queues. The Flow column displays the
                                             names of the call flows associated with the listed entry points or queues. |

| Step 1 | On the Management Portal, click the gears icon in the upper-right corner to view the three or four Tab keyed settings panel. |
|---|---|
| Step 2 | Click the gears icon. Select a time zone from the Time Zone drop-down list. |
| Step 3 | Click Apply . |
| Step 4 | From the Management Portal navigation bar, choose Routing Strategy to view the routing strategies based on the selected time zone. |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | At the Routing Strategy page, choose Routing > Routing Strategies . |
| Step 3 | Choose an entry point from the Select Entry Point drop-down list. |
| Step 4 | Do one of the following in the list view: Click New Strategy . Note Global Routing Overrides only apply to Telephony channel type. - OR - Click the ellipsis button beside an existing routing strategy with Active status and click Copy . | Note | Global Routing Overrides only apply to Telephony channel type. |
| Note | Global Routing Overrides only apply to Telephony channel type. |
| Step 5 | Enter or modify the settings as described in the following tables. Note You can create more than one strategy for a Telephony channel. Table 1. General settings applicable in routing strategy Setting Description General Settings Name Enter a name for the strategy, such as US Holiday or Weekends. You can’t edit this field after you save the strategy. Enterprise Name Shows the tenant name. Status Click Active if you want the strategy to become effective on the start date that you specify in the Start Date field. Click Not Active if you want to save the strategy for future use or as a draft to work on later. The status is always Active for chat and email routing strategies as you can configure only one routing strategy for each entry point or queue. Table 2. Settings applicable in routing strategy for Telephony Setting Description Time Settings (These are read-only for proxy queues.) Start Date End Date Click in each of these fields and use the calendar controls to specify the start date (the date that the strategy becomes
                                                         effective) and the end date (the date that the strategy expires). Start Time End Time Enter in 24-hour format (0000–2400) the time of day that you want the strategy to start and end. Day of Week From the drop-down list, choose All Days if you want to schedule the strategy for every day or Weekdays if you want to schedule the strategy for Monday through Friday only. -OR- Click each icon that represents a day on which you want to schedule the strategy. Advanced Settings Music on Hold Select the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ. Call Control Flag as Default Routing Strategy -or- Update as Default Routing Strategy Choose the Routing Strategy. This setting is available only if you create a new strategy or copy an existing one. Set to Yes if you want this routing strategy to be the default routing strategy for the specified time interval for this entry point
                                                         or queue. Set to No to create an exception to the default schedule, such as a holiday. This strategy overrides the default strategy. That is,
                                                         the system first checks for a strategy that isn’t flagged as default, and if none exists, the system uses the default strategy. Note Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy Flow Select the flow from the drop-down list. Table 3. Settings applicable in routing strategy for Email Setting Description Email Account You can add only one email account for each entry point. You can edit or delete the email account using the icons beside the
                                                         email account name. Add Email Account Click the Add Email Account button to open the Add Email Account dialog box. Enter the following details: Email Address: Enter the email address to contact your organization. Inbound Server Settings: Enter the following server details for incoming emails: Incoming Protocol Incoming Host Inbound Encryption Inbound Port Number Outbound Server Settings: Enter the following server details for outgoing emails: SMTP Server Outbound Encryption Outbound Port Number Server Authentication: Enter the username and password to connect to the email account. Note Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS Note Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . Advanced Email Account Settings: Enter the following advanced settings for the email account: Maximum Attachment Size Number of Attachment Limit Mail Delay Maximum Messages/Cycle Email Routing Rules You can add up to 20 email routing rules. Use the icon beside the rule to edit or delete the rule. Routing Rule Click the Add Routing Rule button to open the Add Routing Rule dialog box. Enter the following details to add a rule: Routing Rule Name: Enter the name for the rule. IF Email Subject Contains: Enter the text in the email subject to set the condition for the rule. You can add up to 10 conditions using the AND or OR
                                                            operators. However, you can mix the AND and OR operators in a rule. Then: Select the email queue to which the email is queued if it satisfies any condition. Note The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. Default Routing Rule Select an email queue for the default routing rule in case none of the defined rules satisfy the criteria. | Note | You can create more than one strategy for a Telephony channel. | Setting | Description | General Settings | Name | Enter a name for the strategy, such as US Holiday or Weekends. You can’t edit this field after you save the strategy. | Enterprise Name | Shows the tenant name. | Status | Click Active if you want the strategy to become effective on the start date that you specify in the Start Date field. Click Not Active if you want to save the strategy for future use or as a draft to work on later. The status is always Active for chat and email routing strategies as you can configure only one routing strategy for each entry point or queue. | Setting | Description | Time Settings (These are read-only for proxy queues.) | Start Date End Date | Click in each of these fields and use the calendar controls to specify the start date (the date that the strategy becomes
                                                         effective) and the end date (the date that the strategy expires). | Start Time End Time | Enter in 24-hour format (0000–2400) the time of day that you want the strategy to start and end. | Day of Week | From the drop-down list, choose All Days if you want to schedule the strategy for every day or Weekdays if you want to schedule the strategy for Monday through Friday only. -OR- Click each icon that represents a day on which you want to schedule the strategy. | Advanced Settings | Music on Hold | Select the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ. | Call Control | Flag as Default Routing Strategy -or- Update as Default Routing Strategy | Choose the Routing Strategy. This setting is available only if you create a new strategy or copy an existing one. Set to Yes if you want this routing strategy to be the default routing strategy for the specified time interval for this entry point
                                                         or queue. Set to No to create an exception to the default schedule, such as a holiday. This strategy overrides the default strategy. That is,
                                                         the system first checks for a strategy that isn’t flagged as default, and if none exists, the system uses the default strategy. Note Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy | Note | Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy | Flow | Select the flow from the drop-down list. | Setting | Description | Email Account You can add only one email account for each entry point. You can edit or delete the email account using the icons beside the
                                                         email account name. | Add Email Account | Click the Add Email Account button to open the Add Email Account dialog box. Enter the following details: Email Address: Enter the email address to contact your organization. Inbound Server Settings: Enter the following server details for incoming emails: Incoming Protocol Incoming Host Inbound Encryption Inbound Port Number Outbound Server Settings: Enter the following server details for outgoing emails: SMTP Server Outbound Encryption Outbound Port Number Server Authentication: Enter the username and password to connect to the email account. Note Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS Note Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . Advanced Email Account Settings: Enter the following advanced settings for the email account: Maximum Attachment Size Number of Attachment Limit Mail Delay Maximum Messages/Cycle | Note | Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS | Note | Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . | Email Routing Rules You can add up to 20 email routing rules. Use the icon beside the rule to edit or delete the rule. | Routing Rule | Click the Add Routing Rule button to open the Add Routing Rule dialog box. Enter the following details to add a rule: Routing Rule Name: Enter the name for the rule. IF Email Subject Contains: Enter the text in the email subject to set the condition for the rule. You can add up to 10 conditions using the AND or OR
                                                            operators. However, you can mix the AND and OR operators in a rule. Then: Select the email queue to which the email is queued if it satisfies any condition. Note The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. | Note | The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. | Default Routing Rule | Select an email queue for the default routing rule in case none of the defined rules satisfy the criteria. |
| Note | You can create more than one strategy for a Telephony channel. |
| Setting | Description |
| General Settings |
| Name | Enter a name for the strategy, such as US Holiday or Weekends. You can’t edit this field after you save the strategy. |
| Enterprise Name | Shows the tenant name. |
| Status | Click Active if you want the strategy to become effective on the start date that you specify in the Start Date field. Click Not Active if you want to save the strategy for future use or as a draft to work on later. The status is always Active for chat and email routing strategies as you can configure only one routing strategy for each entry point or queue. |
| Setting | Description |
| Time Settings (These are read-only for proxy queues.) |
| Start Date End Date | Click in each of these fields and use the calendar controls to specify the start date (the date that the strategy becomes
                                                         effective) and the end date (the date that the strategy expires). |
| Start Time End Time | Enter in 24-hour format (0000–2400) the time of day that you want the strategy to start and end. |
| Day of Week | From the drop-down list, choose All Days if you want to schedule the strategy for every day or Weekdays if you want to schedule the strategy for Monday through Friday only. -OR- Click each icon that represents a day on which you want to schedule the strategy. |
| Advanced Settings |
| Music on Hold | Select the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ. |
| Call Control |
| Flag as Default Routing Strategy -or- Update as Default Routing Strategy | Choose the Routing Strategy. This setting is available only if you create a new strategy or copy an existing one. Set to Yes if you want this routing strategy to be the default routing strategy for the specified time interval for this entry point
                                                         or queue. Set to No to create an exception to the default schedule, such as a holiday. This strategy overrides the default strategy. That is,
                                                         the system first checks for a strategy that isn’t flagged as default, and if none exists, the system uses the default strategy. Note Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy | Note | Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
| Note | Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
| Flow | Select the flow from the drop-down list. |
| Setting | Description |
| Email Account You can add only one email account for each entry point. You can edit or delete the email account using the icons beside the
                                                         email account name. |
| Add Email Account | Click the Add Email Account button to open the Add Email Account dialog box. Enter the following details: Email Address: Enter the email address to contact your organization. Inbound Server Settings: Enter the following server details for incoming emails: Incoming Protocol Incoming Host Inbound Encryption Inbound Port Number Outbound Server Settings: Enter the following server details for outgoing emails: SMTP Server Outbound Encryption Outbound Port Number Server Authentication: Enter the username and password to connect to the email account. Note Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS Note Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . Advanced Email Account Settings: Enter the following advanced settings for the email account: Maximum Attachment Size Number of Attachment Limit Mail Delay Maximum Messages/Cycle | Note | Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS | Note | Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . |
| Note | Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS |
| Note | Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . |
| Email Routing Rules You can add up to 20 email routing rules. Use the icon beside the rule to edit or delete the rule. |
| Routing Rule | Click the Add Routing Rule button to open the Add Routing Rule dialog box. Enter the following details to add a rule: Routing Rule Name: Enter the name for the rule. IF Email Subject Contains: Enter the text in the email subject to set the condition for the rule. You can add up to 10 conditions using the AND or OR
                                                            operators. However, you can mix the AND and OR operators in a rule. Then: Select the email queue to which the email is queued if it satisfies any condition. Note The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. | Note | The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. |
| Note | The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. |
| Default Routing Rule | Select an email queue for the default routing rule in case none of the defined rules satisfy the criteria. |

| Note | Global Routing Overrides only apply to Telephony channel type. |
|---|---|

| Note | You can create more than one strategy for a Telephony channel. |
|---|---|

| Setting | Description |
|---|---|
| General Settings |
| Name | Enter a name for the strategy, such as US Holiday or Weekends. You can’t edit this field after you save the strategy. |
| Enterprise Name | Shows the tenant name. |
| Status | Click Active if you want the strategy to become effective on the start date that you specify in the Start Date field. Click Not Active if you want to save the strategy for future use or as a draft to work on later. The status is always Active for chat and email routing strategies as you can configure only one routing strategy for each entry point or queue. |

| Setting | Description |
|---|---|
| Time Settings (These are read-only for proxy queues.) |
| Start Date End Date | Click in each of these fields and use the calendar controls to specify the start date (the date that the strategy becomes
                                                         effective) and the end date (the date that the strategy expires). |
| Start Time End Time | Enter in 24-hour format (0000–2400) the time of day that you want the strategy to start and end. |
| Day of Week | From the drop-down list, choose All Days if you want to schedule the strategy for every day or Weekdays if you want to schedule the strategy for Monday through Friday only. -OR- Click each icon that represents a day on which you want to schedule the strategy. |
| Advanced Settings |
| Music on Hold | Select the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ. |
| Call Control |
| Flag as Default Routing Strategy -or- Update as Default Routing Strategy | Choose the Routing Strategy. This setting is available only if you create a new strategy or copy an existing one. Set to Yes if you want this routing strategy to be the default routing strategy for the specified time interval for this entry point
                                                         or queue. Set to No to create an exception to the default schedule, such as a holiday. This strategy overrides the default strategy. That is,
                                                         the system first checks for a strategy that isn’t flagged as default, and if none exists, the system uses the default strategy. Note Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy | Note | Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
| Note | Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
| Flow | Select the flow from the drop-down list. |

| Note | Various routing strategies may be configured for a given time interval, but only one can be considered the current routing
                                                                     strategy. Webex Contact Center uses the following order of preference to decide the current routing strategy at any given
                                                                     time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
|---|---|

| Setting | Description |
|---|---|
| Email Account You can add only one email account for each entry point. You can edit or delete the email account using the icons beside the
                                                         email account name. |
| Add Email Account | Click the Add Email Account button to open the Add Email Account dialog box. Enter the following details: Email Address: Enter the email address to contact your organization. Inbound Server Settings: Enter the following server details for incoming emails: Incoming Protocol Incoming Host Inbound Encryption Inbound Port Number Outbound Server Settings: Enter the following server details for outgoing emails: SMTP Server Outbound Encryption Outbound Port Number Server Authentication: Enter the username and password to connect to the email account. Note Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS Note Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . Advanced Email Account Settings: Enter the following advanced settings for the email account: Maximum Attachment Size Number of Attachment Limit Mail Delay Maximum Messages/Cycle | Note | Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS | Note | Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . |
| Note | Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS |
| Note | Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . |
| Email Routing Rules You can add up to 20 email routing rules. Use the icon beside the rule to edit or delete the rule. |
| Routing Rule | Click the Add Routing Rule button to open the Add Routing Rule dialog box. Enter the following details to add a rule: Routing Rule Name: Enter the name for the rule. IF Email Subject Contains: Enter the text in the email subject to set the condition for the rule. You can add up to 10 conditions using the AND or OR
                                                            operators. However, you can mix the AND and OR operators in a rule. Then: Select the email queue to which the email is queued if it satisfies any condition. Note The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. | Note | The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. |
| Note | The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. |
| Default Routing Rule | Select an email queue for the default routing rule in case none of the defined rules satisfy the criteria. |

| Note | Ensure you use only secure access to mail servers, such as: SMTP, IMAP, or POP over SSL SMTP, IMAP, or POP over TLS |
|---|---|

| Note | Mandatory steps to use a Gmail account for an email channel are as follows: Enable the IMAP option if you provide IMAP server to fetch mails in the server in the Gmail settings. Enable the Less Secure Apps flag in the Gmail account settings. Disable the captcha by logging into https://g.co/allowaccess . Update the credentials in the routing strategy and click Save . |
|---|---|

| Note | The email can remain in a queue for a maximum of 240 days. After 240 days, the system removes the email from Webex Contact
                                                                     Center. |
|---|---|

| Note | Changes made to the current Email or Chat entry point routing strategy are also applied to the corresponding active routing
                                                   strategies. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | On the Routing Strategy page, choose an entry point or queue from the Select Entry Point/Queue drop-down list. |
| Step 3 | Click the ellipsis button beside the strategy that you want to modify and choose Edit . |
| Step 4 | Make your changes. For information about each setting, see the setting descriptions table in Create a routing strategy . |
| Step 5 | If you modify the current strategy and want the changes to apply to calls currently in queue, check the Apply changes to current calls in queue check box on the lower right side of the page. If you don't check this check box, the changes only apply to new calls. |
| Step 6 | Click Save to save your changes. |

| Note | When you delete a current strategy, the system activates the next strategy scheduled for that time period. Do not delete a
                                          current strategy unless an alternate strategy is available. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | On the Routing Strategy page, choose an entry point or queue from the Select Entry Point/Queue drop-down list. |
| Step 3 | Click the ellipsis button beside the routing strategy that you want to delete and click Delete . |
| Step 4 | Click Yes to confirm. The system moves the strategy to the Deleted Routing Strategies page where it can be restored or permanently deleted (see Restore or Permanently Delete a Routing Strategy ). |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . |
|---|---|
| Step 2 | On the Routing Strategy page, click Deleted Strategies . |
| Step 3 | Choose an entry point or queue from the Select Entry Point/Queue drop-down list. |
| Step 4 | Click the ellipsis button beside the strategy that you want to either restore or permanently delete and do one of the following: To permanently delete the strategy, click Delete . Click Yes to confirm. - OR - To restore the strategy, click Restore . |
| Step 5 | If you are restoring a strategy, modify the settings as required, and click Restore . Note You cannot restore a deleted Chat Entry Point Routing Strategy, if a Routing Strategy is assigned to the Entry Point. If any settings conflict with an existing routing strategy, a message informs you. In this case, you must modify the settings
                                                before you can restore the strategy. | Note | You cannot restore a deleted Chat Entry Point Routing Strategy, if a Routing Strategy is assigned to the Entry Point. |
| Note | You cannot restore a deleted Chat Entry Point Routing Strategy, if a Routing Strategy is assigned to the Entry Point. |

| Note | You cannot restore a deleted Chat Entry Point Routing Strategy, if a Routing Strategy is assigned to the Entry Point. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . The Routing Strategy page opens. |
|---|---|
| Step 2 | From the menu bar, choose Routing > Global Routing Overrides . The Global Routing Overrides page opens to display the Global Routing Overrides List . This page displays all existing global routing overrides. You can use the Search function at the top-right of the List area to find your target. See Global routing override parameters for a description of the parameters that are visible on the page. |
| Step 3 | (Optional) To export the list of global routing overrides for data analysis, click the ellipsis button near the top-right side of the page and click Excel or CSV . |
| Step 4 | (Optional) To display the details of a routing override or to edit it, click the ellipsis button at the left of the listed override and then click Edit . See Edit a global routing override for further detail on editing a routing override . |

| Note | By default, you create global routing overrides in the Tenant time zone. All the data that are displayed on the Global Routing Overrides page or dashboard are based on the Tenant time zone. |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . The Routing Strategy page opens. |
|---|---|
| Step 2 | From the menu bar, choose Routing > Global Routing Overrides . The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides. |
| Step 3 | From the Global Routing Overrides page, click + New Override . The Create Global Routing Override page opens. |
| Step 4 | Configure the new global routing override as described in Global routing override parameters . |
| Step 5 | Click Save or Cancel . |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . The Routing Strategy page opens. |
|---|---|
| Step 2 | From the menu bar, choose Routing > Global Routing Overrides . The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides. |
| Step 3 | Locate the global routing override you want to copy to create a new override . You can use the Search function at the top-right of the Global Routing Overrides List area to find your target. |
| Step 4 | Click the ellipsis button to the left of a listed override , and then click Copy . The Copy Global Routing Override page opens. |
| Step 5 | Change the settings as required, and in accordance with instructions provided in Global routing override parameters . |
| Step 6 | Click Save or Cancel . |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . The Routing Strategy page opens. |
|---|---|
| Step 2 | From the menu bar, choose Routing > Global Routing Overrides . The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides . |
| Step 3 | Locate the global routing override you want to edit. You can use the Search function at the top-right of the Global Routing Overrides List area to find your target. |
| Step 4 | Click the ellipsis button at the left of the entry point you want to modify, and then click Edit . The Overwrite Global Routing Override page opens. |
| Step 5 | Edit the routing override parameters in accordance with the information provided in Global routing override parameters . |
| Step 6 | Click Save or Cancel . |

| Column | Description |
|---|---|
| Name | Displays the name you assign to the override . You can't change the override name after you create it. |
| ID | Displays the system-assigned number of the override . |
| Status | Indicates the status of the override . Current (appears in Red) means this is a snapshot of the currently running override . You can't copy the current override , but you can modify any setting that doesn't affect execution time or date. Changes to the override don't affect the recurring scheduled version of the override . Note You can delete the current override , but don't delete it before you create a different override for the same time interval. If you delete an override without having another one in place, the last override used by the system becomes the default override although the start and end times and dates have expired. If this occurs, either create a new override for the current time period, or copy the default override and correct the time settings. Active means that the override is in effect at the specified start time on the specified start date. This is the default status. Not Active means the override isn't in effect regardless of the specified start time and date. This status lets you save an override for future use or as a draft to continue with later. | Note | You can delete the current override , but don't delete it before you create a different override for the same time interval. If you delete an override without having another one in place, the last override used by the system becomes the default override although the start and end times and dates have expired. If this occurs, either create a new override for the current time period, or copy the default override and correct the time settings. |
| Note | You can delete the current override , but don't delete it before you create a different override for the same time interval. If you delete an override without having another one in place, the last override used by the system becomes the default override although the start and end times and dates have expired. If this occurs, either create a new override for the current time period, or copy the default override and correct the time settings. |
| Default | Indicates whether the global routing override is the default routing strategy ( Yes ) or isn't the default routing strategy ( No ). |
| Repetition | Specifies whether the override repeats daily or only on specific days of the week. |
| Start Date | Displays the date on which the override starts. |
| End Date | Displays the date on which the override ends. |
| Start Time | Displays the time at which the override starts (in 24-hour format) for any given day in the specified date range. |
| End Time | Displays the time at which the override ends (in 24-hour format) for any given day in the specified date range. |
| Time Zone | Displays the Tenant time zone. Global routing overrides operate in the Tenant time zone. |
| Flow | Lists the associated call flows when a routing override is executing. |

| Note | You can delete the current override , but don't delete it before you create a different override for the same time interval. If you delete an override without having another one in place, the last override used by the system becomes the default override although the start and end times and dates have expired. If this occurs, either create a new override for the current time period, or copy the default override and correct the time settings. |
|---|---|

| Parameter | Description |
|---|---|
| General Settings |  |
| Name | Enter the name for the global routing override . You can't change the name after it's created. If you copy an override , you can change the name of the copy. |
| Enterprise Name | Displays the name of the Tenant. |
| Channel Type | Displays the only valid channel type: Telephony |
| Entry Points | This field appears only if you are creating or copying a global routing override . Choose the entry points to which the global routing override applies. |
| Status | Click the Status toggle button to set the status of the global routing override to either Active or Not Active . When set to Active , the routing override activates and deactivates on the dates and at the times specified in the related Start and End Date and Start and End  Time
                                             fields. |
| Time Settings |  |
| Time zone | Displays the Tenant time zone. Global routing overrides operate in the Tenant time zone. |
| Start Date End Date | Click in each of these fields and use the calendar controls to specify the start date (the date the global routing override becomes effective) and end date (the date the global routing override expires). |
| Start Time End Time | Enter in 24-hour format (0000–2400) the time of day you want the global routing override to start and end. |
| Day of Week | From the drop-down list: Choose All Days if you want to schedule the global routing override to run every day. Choose Weekdays if you want to schedule the global routing override to run from Monday through Friday only. Choose Specific Days , and click the icons representing weekdays if you want to schedule the global routing override to run on specific days of the week. |
| Advanced Settings |  |
| Music on Hold | From the drop-down list, choose the name of the audio (.wav) file to play for calls when an agent puts a call on hold. Music
                                             in Queue (MIQ) is handled from Flow. When a contact is queued and if no agent is available, the customer is engaged with MIQ. |
| Flag as Default Routing Strategy | This setting is available only if you create a new override or copy an existing one. Set to Yes if you want this global routing override to be the default global routing override for the specified time interval for this entry point. Set to No to create an exception to the default schedule, such as a holiday. This override overrides the default override . That is, the system first checks for a override that isn’t flagged as default, and if none exists, the system uses the default override . Note You can configure different routing strategies for a given time interval. However, Webex Contact Center prioritizes only one
                                                         routing strategy. Webex Contact Center uses the following order of prioritization to decide the current routing strategy at
                                                         any given time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy | Note | You can configure different routing strategies for a given time interval. However, Webex Contact Center prioritizes only one
                                                         routing strategy. Webex Contact Center uses the following order of prioritization to decide the current routing strategy at
                                                         any given time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
| Note | You can configure different routing strategies for a given time interval. However, Webex Contact Center prioritizes only one
                                                         routing strategy. Webex Contact Center uses the following order of prioritization to decide the current routing strategy at
                                                         any given time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
| Call Control |  |
| Flow | Choose a flow to override the contact handling behavior for the selected entry points during the configured time period. |

| Note | You can configure different routing strategies for a given time interval. However, Webex Contact Center prioritizes only one
                                                         routing strategy. Webex Contact Center uses the following order of prioritization to decide the current routing strategy at
                                                         any given time: 1. Global Routing Overrides 2. Default Global Routing Overrides 3. Routing Strategy 4. Default Routing Strategy |
|---|---|

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . The Routing Strategy page opens. |
|---|---|
| Step 2 | From the menu bar, choose Routing > Global Routing Overrides . The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides. See Global routing override parameters for a description of the elements that are visible on the page. |
| Step 3 | Locate the global routing override you want to edit. You can use the Search function at the top-right of the Global Routing Overrides List area to find your target. |
| Step 4 | Click the ellipsis button to the left of the routing override you want to delete, then click Delete . In the confirmation dialog box that opens, click OK . The routing override moves to the Deleted Global Routing Overrides page where it awaits restoration or permanent deletion. For more information, see Restore or Permanently Delete a Routing Strategy . |

| Step 1 | From the Management Portal navigation bar, choose Routing Strategy . The Routing Strategy page opens. |
|---|---|
| Step 2 | From the menu bar, choose Routing > Global Routing Override . The Global Routing Overrides page opens to display the Global Routing Overrides List . This page shows all existing global routing overrides. See Global routing override parameters for a description of the parameters that are visible on the page. |
| Step 3 | Click the Deleted Global Routing Overrides button at the top-right side of the page. The Deleted Global Routing Overrides page opens displaying a list of deleted routing overrides , if any exist. |
| Step 4 | In the Deleted Global Routing Overrides List view, locate the routing override you want to either restore or permanently delete. You can use the Search function at the far-right of the page to locate your target. |
| Step 5 | Click the ellipsis button to the left of the routing override you want to either restore or permanently delete and do one of the following: (Optional) To permanently delete the override , click the Delete icon. Click Yes in the confirmation dialog box to commit. The Deleted Global Routing Overrides page immediately refreshes, excluding the deleted routing override . (Optional) To restore the override , click the Restore icon. Click Yes in the confirmation dialog box to commit. The Restore Global Routing Override page appears, displaying the settings for the routing override . You can change some of the settings in accordance with the information that is provided in Global routing override parameters . Click Restore to save changes and confirm reactivation of the override . Note If any settings conflict with an existing routing override , a message informs you. In this case, you must modify the settings before the override restores. The Deleted Global Routing Overrides page immediately refreshes, excluding the restored routing override . | Note | If any settings conflict with an existing routing override , a message informs you. In this case, you must modify the settings before the override restores. |
| Note | If any settings conflict with an existing routing override , a message informs you. In this case, you must modify the settings before the override restores. |

| Note | If any settings conflict with an existing routing override , a message informs you. In this case, you must modify the settings before the override restores. |
|---|---|