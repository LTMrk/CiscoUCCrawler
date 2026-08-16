---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-user-guide-uccx-b-1251su2-9f46b4e874
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/user/guide/uccx_b_1251su2_finesse-agent-supervisor-desktop-user-guide/uccx_m_1251su2_supervisor-tasks.html
retrieved_at: 2026-08-16T21:24:09.319773+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU2

# Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU2

Updated: April 10, 2022

Chapter: Supervisor Tasks

## Chapter: Supervisor Tasks

# Supervisor Tasks

## View Team Performance

Use the Team Performance gadget to view the agents on each of your assigned teams.

In the Team Performance gadget, you can view the details of the team selected by default in the Team Name drop-down.

A list of agents for the selected team with their current state, time in state, extension, and action appears. Click the headers
                                          of the columns to sort by Agent Name, State, Time in State, or Extension.

For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart.

By default, the list will only contain logged in agents for the selected team. To view both, logged in and logged out agents,
                                          check the Include logged out agents check box.

Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session.

Select an agent and in the corresponding row, click under the Actions tab to monitor the agent, change the state to Ready, Not Ready, or Sign Out the agent.

The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0.

To view another team, click the Team Name drop-down and choose a new team.

## View Active Call Details

From the Team Name drop-down, choose the agent's team.

From the displayed list, choose an agent in the Talking state.

In the Actions tab of the selected agent, click the down arrow.

The following call details are displayed:

The popover call variable header and the call variables configured by the administrator.

Active Participants : The phone numbers of the active participants in the call.

Held Participants : The phone numbers of the held participants in the call. The Held Participants information is not available for unmonitored
                                                devices. For example, customer or external devices.

Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call.

Duration : The duration of the call.

Call Status : The current status of the call. Indicates the status of the expanded agent in the call.

Queue Name : The customer service queue to which the call belongs to.

## View Recent Call History

If the Administrator has configured view history for you, use the Team Performance gadget to view the call history of an agent
                              of your assigned team.

From the Team Name drop-down, choose the agent's team.

From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox.

In the Actions tab of the selected agent, click > View History .

The following call details of the selected agent's Recent Call History are displayed:

Start Time : Indicates the start time of the call.

Duration : Indicates the call duration.

Type : Indicates if the call was an Inbound or Outbound.

Number : Indicates the phone number of the call.

Disposition : Indicates the action taken on the call.

Queue : Indicates the name of the queue assigned to the agent.

Wrap-Up Reason : Indicates the Wrap-Up Reason selected by the agent.

You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame.

To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header.

## View Recent State History

If the Administrator has configured view history for you, use the Team Performance gadget to view the state history of an
                              agent of your assigned team.

From the Team Name drop-down, choose the agent's team.

From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox.

In the Actions tab of the selected agent, click > View History .

The following details of the selected agent's Recent State History are displayed:

Start Time : Indicates the start time of the call.

State : Indicates the agent state. In the Team Performance gadget, when an agent state changes to Wrap-Up, the corresponding state
                                                in the Recent State History gadget will display as WORK_READY .

Reason : Indicates the wrap-up reason of the call.

Duration : Indicates the call duration.

You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame.

To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header.

## Change the State of an Agent

Use the Team Performance gadget to change the state of an agent to Ready, Not Ready, or Sign Out.

From the Team Name drop-down list, choose the agent's
                                       team.

From the displayed list, choose the agent whose state you want to change.

In the Actions tab of the selected agent, click and choose:

Ready

To force the agent state to Ready.

Not Ready

To force the agent state to Not Ready.

Sign Out

To sign the agent out.

In the Actions tab, the Ready, Not Ready, and Sign Out options are active only if the action is allowed.

For example, if you select an agent who is in Ready state, you will see only the Not Ready and Sign Out options. If you select
                                          an agent who is in Not Ready state, you will see only the Ready and Sign Out options.

If you sign out an agent on an active call (in Talking state), or has a call
                                          on hold (in Hold state), that agent is immediately signed out of the desktop
                                          but the call is retained.

## Monitor a Call

You must be in Not Ready state to monitor an agent. You can monitor only one agent at
                              a time. To monitor another agent, you must End the silent
                              monitoring call and then select a new agent.

From the Team Name drop-down list, choose the team whose
                                       agents you want to monitor.

From the displayed list, choose an agent to monitor.

In the Actions tab of the selected agent, click > Monitor .

The silent monitor call appears in the call control area of the desktop. The Hold , Barge In , and End buttons are enabled. Click:

To place the call on hold.

To retrieve the call placed on hold.

To barge in to the call.

To end the silent monitor call, click End .

The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption.

## Barge In on a Call

The Barge In feature allows you to join a call between an agent and a caller.

You can only barge in on a call that you are silently monitoring.

For the supervisor to be able to barge in, the agent and supervisor
                                                extensions must have visibility to each other's partition or calling
                                                search space (CSS) without any prefix or steering digit.

From the Team Name drop-down list, choose the agent's
                                       team.

From the displayed list, choose an agent in the Talking state.

In the Actions tab of the selected agent, click > Monitor .

The silent monitor call appears in the call control area of your desktop. The Barge In button appears.

Click Barge In .

The call becomes a conference call between you, the agent, and the caller.

## Intercept a Call

After you barge in to a call between an agent and a caller, you can intercept the call by dropping the agent from the call.
                              You can also drop any participant from a conference call in which you are a participant.

Click the Drop drop-down.

Click the agent to drop from the list of participants.

Even if an agent initiates a conference call, only the supervisor can drop an agent from the call. The Supervisor cannot drop
                                          a CTI Route Point, IVR Port, or a caller.

## Send Team Message

The Team Message feature allows you to create and send a broadcast message to one or multiple teams. The message appears as
                              a banner across the Finesse desktop and agents can view these messages in real-time. Team Message will be available on your
                              Finesse desktop only if the administrator has configured this feature for you.

In the Finesse desktop, click the Team Message icon.

In the Compose Message box, enter the broadcast message (maximum number of characters allowed is 255).

Select the team or teams to send the message by checking the check box next to the team name.

You can send multiple messages to a single team, multiple teams, or all teams.

From the drop-down, you can set an expiry time for the composed messages: starting at 5 minutes and ending at 23:55 hours.
                                       The time is displayed in hours and minutes. However, this time frame can be edited.

Click Send .

You can view the latest messages sent by clicking Show recent messages . If you wish to delete any or all messages, check the check box next to the message. Click Delete and confirm the deletion.

The message is removed from active display and the previous non-expired team message will become the active message for the
                                          agent.

Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message .

The rate at which messages (create/delete) are published to the teams involved, is capped at  per hour and the maximum number
                                          of active messages allowed is . If the limit of active messages is reached, supervisors will not be able to broadcast new
                                          messages until an existing team message is deleted or it expires.

As there are no individual limitations on supervisors, either one or all supervisors can broadcast messages up to the maximum
                                          active messages limit.

## Advanced Capabilities for Supervisor

As a supervisor, you can now manage Queues, Applications, Calendars, and Outbound Campaigns.

Queue Management - Manage resources across the assigned CSQs of your team.

Application Management - Manage working hours, holidays, and prompts.

Calendar Management - Edit the Business Hours, Custom Business Days, and Holidays.

Outbound Campaign Management - Schedule, enable or disable outbound campaigns, and import contacts.

The columns of all the tables available in Advanced Supervisor Capability gadget can be resized except for the tables in Calendar View (available in Application Management ) and Calendar Management page.

When you click the Application Management , Calendar Management , or Outbound Campaign Management tab, the corresponding data is refreshed.

When you try to access Advanced Capabilities for the first time, if you do not have CA signed certificate, you are prompted to accept the Unified CCX certificates. Accept
                                       the certificates to enable all the functionalities.

### Queue Management Summary

Queue Management displays the summary of Voice, Chat, and Email CSQs. Each CSQ summary is displayed based on the condition that at least one
                                 queue is assigned to the logged in supervisor. For example, if a supervisor is assigned to only Voice CSQ, only Voice CSQ
                                 Summary is displayed. The common fields for all the three CSQ summaries are as follows:

Queue Name - Displays the queue names for the CSQ that are managed by the supervisor.

Team Name - Displays the team names that are associated with the CSQ.

Agents Modified (Since Midnight)

Added - Number of agents that are added to the CSQ.

Removed - Number of agents that are removed from the CSQ.

Action - Provides a link to the Manage Queue page.

#### Voice CSQ Summary

Voice CSQ Summary displays statistics of the queues (for the current day, beginning at midnight) managed by the supervisor. It lists only the
                                 CSQs that are skill-based, that is, Resource Skills is selected for Resource Pool Selection Model in the queue configuration. The fields that are specific to Voice CSQ Summary are as follows:

Waiting Calls - Number of calls that are in queue for the CSQ.

Abandoned Calls - Number of calls that are not handled by the agents in the CSQ.

Longest Call in Queue - Longest customer call waiting in the queue.

#### Chat CSQ Summary

Chat CSQ Summary displays statistics of the queues (for the current day, beginning at midnight) managed by the supervisor. The specific fields
                                 are as follows:

Waiting Contacts - Number of contacts that are in queue for the CSQ.

Abandoned Contacts - Number of contacts that are not handled by the agents in the CSQ.

#### Email CSQ Summary

Email CSQ Summary displays statistics of the queues (for the current day, beginning at midnight) managed by the supervisor. The specific fields
                                 are as follows:

Emails in Queue - Number of emails that are in queue for the CSQ.

Emails in Process - Number of emails that are delivered and waiting for response in the CSQ.

#### Manage Queue

Based on the queue that is selected in the Queue Management Summary window, corresponding Manage Queue window is displayed. All the agents, who are assigned to the selected queue are listed. You can click the column headers
                                    to sort information by Agent Name , Agent ID , Team Name , Added by , Added at , or Remove at . By default, the last added agent is listed at the top of the table. You can add and remove agents from the queue. The fields
                                    that are listed in the table are as follows:

Agent Name - Name of the agent who is assigned to the queue.

Agent ID - Login ID of the agent who is assigned to the queue.

Team Name - Name of the agent's team.

Skills (Competency) - Skills and competencies of the agent.

Added by - Role and name of the resources who have added the agent to the queue.

Added at - Date and Time at which the agent is added to the queue.

Remove at - Date and Time at which the agent has to be removed from the queue. You can edit or cancel the schedule. Before saving the
                                          changes, you can revert to the previous scheduled time.

When you save, if the agent is associated with multiple queues, the impact of changes on all the associated queues is verified.
                                          If there is an impact, a confirmation message is displayed. Click Yes to update all the queues else click No to discard the changes.

Remove - Option to remove the agent from the queue. You can remove only the agents who are part of your team.

##### Search

The search criteria is applicable only for Agent Name and Agent ID . To search for an agent, click the search icon. The search field expands in which, you can enter the search criteria to find
                                    the required agent. You can:

Click All to list all the agents who are assigned to the queue.

Click Agents Added (Since Midnight) to list all the agents, who are assigned to the queue since midnight.

##### Adding Agents to the Queue

Click Add/Schedule Agents button to add and schedule agents to the queue.

##### Add and Schedule Agents for a Queue

You can add and schedule (add and remove) agents for the selected queue. Only the agents who are part of your team can be
                                       added and scheduled. When you click the Add/Schedule Agents button in the Manage Queue page, Add Agents page is displayed. The Add Agents page has Agents Available and Agents Scheduled tabs. By default, the Agents Available tab is selected. The fields that are listed in both the tabs are as follows:

Agent Name - Name of the agent.

Agent ID - Login ID of the agent.

Skills (Competency) - Skills and competencies of the agent.

CSQs - Names of the queues to which the agent belongs.

Team Name - Name of the agent's team.

Add at - Date and Time at which the agent has to be added to the queue. You can clear and undo the changes by using the icons that
                                             are available for each agent.

Remove at - Date and Time at which the agent has to be removed from the queue. You can clear and undo the changes by using the icons
                                             that are available for each agent.

###### Agents Available

By default, all the logged in agents, who are not assigned to the queue are listed in the table. The table has two sections, Agents with required skills and less competency and Agents without the required skills . You can click the column headers to sort information by Agent Name or Agent ID . The sorting is within the respective sections in the table. You can click Search to search an agent by Agent Name or Agent ID . The agents can be added to the queue as follows:

Select Include Logged Out Agents to list all the logged out agents. To identify the logged out agents in the list, an asterisk is displayed next to the agent
                                                   name. Based on the skills and competency, agents are appropriately listed in the respective sections of the table.

If Include Logged Out Agents is already selected, all the agents are listed. Clear Include Logged Out Agents so that only the agents who are logged in to Finesse desktop are listed in the table.

Select one or more agents to be added to the queue.

Select Add at to add the agent to the queue as per the schedule. Click the Clear icon to clear the schedule.

If you do not select the date and time, agent is immediately added to the queue.

Select Remove at to remove agent from the queue as per the schedule. Click the Clear icon to clear the schedule.

If you do not select the date and time, agent remains associated with the queue.

Click Save to add and schedule (add and remove) the selected agents for the CSQ.

While adding or removing an agent for a queue, if there are common skills across queues, a confirmation message is displayed.
                                                      Based on the confirmation, the changes impact all the queues that have common skills to which the agent is associated.

If you select No , the action is canceled. If you select Yes , the update is as follows:

Add Impact

If date and time are not selected for Add at , the agent is immediately added to the selected queue and to all the impacted queues.

If date and time are selected for Add at , the agent is scheduled to be added to the selected queue. At the scheduled time, the agent is added to the selected queue
                                                            and to all the impacted queues.

Remove Impact

If date and time are selected for Remove at , the agent is scheduled to be removed from the selected queue.

At the scheduled time, the agent is removed from the selected queue and from all the impacted queues.

###### Status of Agents Added to a Queue

When you add more than one agent to the selected queue, the status of agents being added is displayed in the Status of Agents Added page. The fields that are displayed are as follows:

Agent Name - The name of the selected agent.

Agent ID - The login ID of the selected agent.

Status - Visual indication of the agents being added to the queue.

CSQs - List of all the CSQs that the agent is assigned to. The list is displayed only after the agent is added to the queue.

Remarks/Action - If an agent is not added or scheduled (added and removed) for the queue, the reason for the failure is displayed.

While adding and removing agents for the queue, if there are common skills across impacted queues, a confirmation message
                                                is displayed for each agent.

The Done button is enabled after the task for all the agents is complete.

If you close this page before all the tasks are complete, the page cannot be retrieved. The tasks that need confirmation (for
                                                      adding or scheduling) are aborted.

###### Agents Scheduled

You can view the agents who are scheduled to be added to a queue. All the agents, who are scheduled to be added to the queue
                                          are listed in the table. If Include Logged Out Agents is already selected, all the agents are listed. Clear Include Logged Out Agents so that only the agents who are logged in to Finesse desktop are listed in the table. You can click the column headers to
                                          sort information by Agent Name or Agent ID . You can click Search to search an agent by Agent Name or Agent ID . The agents can be scheduled for the queue as follows:

Select Include Logged Out Agents to list the agents who are logged out of Finesse desktop.

To identify the logged out agents in the list, an asterisk is displayed next to the agent name.

Select Add at to add or modify the date and time of the schedule. Click the Clear icon to clear the schedule. Click the Undo icon to revert to the previous schedule.

When you clear Add at , the Add at schedule is cleared and the Remove at schedule is disabled.

After clearing Add at , click the Undo icon to revert to the previous schedule. The Add at schedule is retrieved and the Remove at schedule is enabled.

Select Remove at to add or modify the date and time of the schedule. Click the Clear icon to clear the schedule. Click the Undo icon to revert to the previous schedule.

When you clear Remove at , only the Remove at schedule of that agent is cleared.

After clearing Remove at , click the Undo icon to revert to the previous schedule.

Click Save to save the modified schedule.

If the Add at schedule of the agents are cleared, the schedules of those agents are canceled and are listed in the Agents Available tab.

The add and remove impact scenarios are same as mentioned in Agents Available .

###### Status of Agents' Schedule Changes

When you modify the schedule of more than one agent for the selected queue, the changes in status are displayed on the Agents Schedule Change Status page. The fields that are displayed are as follows:

Agent Name - The name of the selected agent.

Agent ID - The login ID of the selected agent.

Status - Visual indication of the schedule that is being modified.

Remarks - If rescheduled details are not saved, the reason for failure is displayed.

While saving rescheduled details of the agents, if there are common skills across impacted queues, a confirmation message
                                                is displayed for each agent.

The Done button is enabled after the tasks of all the agents are complete.

If you close this page before all the tasks are complete, the page cannot be retrieved. The tasks that need confirmation (for
                                                      rescheduling) are canceled.

#### Remove Agents from a Queue

You can remove agents from the selected queue. In the Remove column, the remove icon is highlighted only for the agents who are part of your team.

You can remove only one agent at a time.

Click the remove icon of the respective agent.

A confirmation message is displayed.

Click Yes to remove the agent from the queue.

If removing the agent from the selected queue impacts other queues, a confirmation message is displayed.

Click Yes to remove the agent from the selected queue and from all the impacted queues.

If the agent is removed from the queue, a success message is displayed else a failure message is displayed.

Click No to retain the agent in the selected queue and in all the impacted queues.

### Application Management

Application Management displays the list of script-based applications and its details. The applications that are listed are
                                 based on the configuration by the administrator. As a supervisor, you can manage the applications that are assigned to you.
                                 The fields that are displayed are as follows:

Name - Displays the application name that is assigned to the logged in supervisor.

Description - The description of the application that is provided by the administrator.

Enabled - Indicates whether the application is active. You can also manage the disabled applications.

Triggers - The triggers that are associated with the application.

Action - Link to the Manage Application screen.

#### Manage Application

The required prompts and calendars can be associated with the applications that are assigned to you. The prompts and calendars
                                    are available in Script Parameters and Default Script Parameters tab. In the Prompts tab, all the prompts that are associated with the application are displayed. The list contains only the user uploaded prompts.
                                    In the Calendars tab, all the calendars that are configured are listed. By default, Script Parameters tab and Parameters tab are selected.

The Default Script Parameters tab is displayed only when a default script is associated with the application.

When there is an error in execution of the other script that is configured, the Default Script is run.

In the Prompts tab of the Script Parameters tab, select the required prompts from the list. By default, the prompts that are assigned by the administrator are selected.

Select None , if you do not want to assign any prompt.

Click Yes to confirm the selection.

Only the relative path of the prompt is displayed. The absolute path (language specific) is selected based on the system configuration.

If the script selected by the administrator has a default prompt, Default Prompt is selected for the corresponding prompt in the Prompts tab.

Click the Play icon, which is next to the selected prompt to listen to the prompt.

You cannot play a Default Prompt .

If the prompt that you have selected is available in more than one language, you have to select a language to play the prompt.
                                                Based on the language configured by the administrator, corresponding language prompts are played to the customers.

Click Save .

If you try to navigate out of this tab without saving, a confirmation message is displayed to save the changes.

Select the Calendars tab.

In the Calendars tab, select the required calendars from the list.

Select None , if you do not want to assign any calendar.

Click Yes to confirm the selection.

Click the preview icon, which is next to the selected calendar to view the calendar details.

Click Save to associate the selected prompts and calendars with the application.

If you try to navigate out of this tab without saving, a confirmation message is displayed to save the changes.

Select the Default Script Parameters tab.

Based on the default script that is selected by the administrator, the parameters for prompts and calendars are selected.

Modify the required prompts and calendars.

Click Save to make the selected prompts and calendars as part of the default script.

### Calendar Management

Calendar Management displays the list of calendars and its details. The calendars that are listed are based on the configuration
                                 by the administrator. As a supervisor, you can manage the calendars that are assigned to you. The fields that are displayed
                                 are as follows:

Name - Displays the calendar name that is associated with the logged in supervisor.

Description - Describes the calendar that is provided by the administrator.

Time Zone - Displays the configured time zone of the calendar.

Business Hours - Displays Fixed and Flexible hours that are configured for the calendar.

Custom Business Days - Indicates whether custom business days have been configured for the calendar. The indication is displayed even if one custom
                                       business day is configured.

Holidays - Indicates whether holidays have been configured for the calendar. The indication is displayed even if one holiday is configured.

Associated with - Lists the names of chats and IVR applications that are associated with the calendar.

Action - Link to the Manage Calendar page.

#### Manage Calendar

As a supervisor, you can modify the following details (available as tabs) in the calendars that are assigned to you:

Business Hours

Custom Business Days

Holidays

For the calendar that you have selected, the following information is displayed:

Time Zone - Displays the configured time zone of the selected calendar.

Associated with - Displays the associated IVR application and chat for the selected calendar.

Description - Displays the description of the calendar that is configured by the administrator.

The details that are available in each tab are as follows:

Business Hours - Based on the requirement, different working hours can be configured. The following three types of time range are provided.
                                    By default, the Business Hours tab is selected.

24 x 7 days - You can select this option if the contact center works 24 hours and 7 days in a week.

Fixed Hours - You can select this option when the business has fixed working hours for the selected business days of the week. A maximum
                                          of three time ranges can be configured.

Flexible Hours - You can select this option when the business has different working hours for different days of the week. You can also configure
                                          different working hours for each day of the week. You can configure up to three time ranges for each day.

Custom Business Days - The special days when the contact center works apart from the regular business days with different time range. When a different
                                    time range is specified, the Unified CCX engine overrides any previous schedule that was configured in Custom Business Hours for the same day.

Holidays - In addition to the defined holidays, the contact center can declare a holiday or reschedule the defined holidays. You can
                                    either modify the existing holidays or add more holidays by specifying the day and the date.

##### Modify Business Hours

When the Custom (Fixed) or Custom (Flexible) hours are not configured, by default 24 Hours x 7 Days is selected.

Select Fixed Hours . By default, Monday to Friday is selected.

Check or uncheck the days from the Day column.

Select the working hours, From and To from Time Range 1 column. Similarly, select working hours for Time Range 2 and Time Range 3 .

The time range is applicable for all the days that are selected in the Day column. The order of selection is from Time Range 1 to Time Range 3 .

Click Save .

If you have different working hours for different days, configure as follows:

Select Flexible Hours . By default, Monday to Friday is selected.

If you have made some changes in Fixed Hours , a confirmation message is displayed to save the changes. Clicking Yes updates the database.

Check or uncheck the days from the Day column.

Select the working hours, From and To from Time Range 1 column for each day. Similarly, select working hours for Time Range 2 and Time Range 3 .

The time range has to be configured for each selected day.

Click Save .

##### Custom Business Days

If custom business days are configured, the same is displayed, else it is blank.

You can add and delete custom business days.

Enter a name for the custom business day in Name of the Day column.

Select a date in Date column.

Select the working hours, From and To from Time Range 1 column. Similarly, select working hours for Time Range 2 and Time Range 3 .

Click Add Day to add a custom business day.

Click the delete icon to delete the corresponding custom business day.

Click Save .

##### Holidays

You can add, modify and delete holidays. You can also add more holidays to a calendar.

Enter a holiday name in the Name of the Day column.

Select a date in Date column.

Click Add Day to add more holidays.

Click the delete icon to delete a holiday.

Click Save .

### Outbound Campaign Management

Outbound Campaign Management lists the campaigns and its details that are assigned to the logged in supervisor. The fields
                                 that are displayed are as follows:

Campaign Name - Displays the campaign name that is associated with the logged in supervisor.

Campaign Type - There are two types of campaign, Agent and IVR . The type indicates whether the outbound calls are handled by agents or IVR.

Callback option is not available for IVR campaigns.

Dialer Type - There are three types of dialer, Direct Preview , Predictive , and Progressive . Predictive and Progressive dialers are available for both types of campaign. Direct Preview is available only for the Agent type campaign.

Time - Displays the From and To time of the campaign, which can be edited. You can save the edited time or revert. The timing is applicable for every day
                                       as long as the campaign is enabled.

Contacts Remaining - Displays the number of contacts that are yet to be dialed for the campaign. During manual import of contacts, the import
                                       status is also displayed in this column.

Enabled - Displays a toggle button that can be used to enable or disable a campaign.

Action - A link to the Update Contacts page, where you can delete the existing contacts, import new contacts and modify auto import schedule.

#### Update Contacts

Update Contacts window provides information about the number of contacts that are to be dialed out. You can delete the contacts. You can
                                    manually import contacts and schedule the import of contacts for the campaign.

For reference, the server time zone is displayed at the bottom of the window.

Click Update Contacts for the required campaign in the Outbound Campaign Management tab.

The Update Contacts page displays the following:

Field

Description

Contacts Remaining

The number of contacts that are yet to be dialed for the campaign.

Manual Import

To import the contacts that are to be dialed for the campaign. This tab is selected by default.

Schedule Import

To schedule import of contacts that are to be dialed for the campaign.

If you want the option to schedule import of contacts for a campaign, contact your administrator.

Click the Delete icon to delete the contacts from the database. Delete is applicable for contacts that are imported manually and through Schedule Import .

A confirmation message is displayed.

Click Yes to delete the contacts.

The campaign is disabled, contacts are deleted, and the value of Contacts Remaining is updated to 0 .

##### Manual Import of Contacts

You can manually import contacts from a CSV file (in .csv or .txt format) into the Unified CCX database. The Manual Import tab displays the date and time of the last import.

Click Select File , browse, and select the file that you want to import.

Enable Allow Duplicate Contacts if you want to save duplicate contacts in the database.

Select appropriate fields from Column 1 to Column 7 in the same order as they are in the CSV file.

Predective and Progressive Campaigns have six columns and Direct Preview Campaigns have seven columns.

Click Save . The contacts from the selected file are imported into the Unified CCX database.

During manual import, if you go to the Update Contacts page the status is displayed at the top the page and the Delete icon is disabled. After the import of contacts is complete, the Contacts Remaining and Last Import information is updated and the Delete icon is enabled.

##### Schedule Import of Contacts

You can schedule import of contacts into the Unified CCX database that is used for outbound campaigns. A CSV file (in .csv
                                       or .txt format) that is available in the configured path (by administrator) can be scheduled for import of contacts. The Schedule Import tab displays the date and time of the last import.

Enable Allow Duplicate Contacts if you want to save duplicate contacts in the database.

Select appropriate fields from Column 1 to Column 7 in the same order as they are in the CSV file.

Predictive and Progressive Campaigns have six columns and Direct Preview Campaigns have seven columns.

Select appropriate Start Date .

Select appropriate Start Time .

Select Repeat Every Hours , if the contacts are being updated regularly.

Enable Schedule .

Click Save . A confirmation message is displayed.

| Step 1 | In the Team Performance gadget, you can view the details of the team selected by default in the Team Name drop-down. A list of agents for the selected team with their current state, time in state, extension, and action appears. Click the headers
                                          of the columns to sort by Agent Name, State, Time in State, or Extension. Note For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. By default, the list will only contain logged in agents for the selected team. To view both, logged in and logged out agents,
                                          check the Include logged out agents check box. Note Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. Select an agent and in the corresponding row, click under the Actions tab to monitor the agent, change the state to Ready, Not Ready, or Sign Out the agent. Note The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. | Note | For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. | Note | Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. | Note | The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. |
|---|---|---|---|---|---|---|---|
| Note | For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. |
| Note | Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. |
| Note | The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. |
| Step 2 | To view another team, click the Team Name drop-down and choose a new team. |

| Note | For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. |
|---|---|

| Note | Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. |
|---|---|

| Note | The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. |
|---|---|

| Step 1 | From the Team Name drop-down, choose the agent's team. |
|---|---|
| Step 2 | From the displayed list, choose an agent in the Talking state. |
| Step 3 | In the Actions tab of the selected agent, click the down arrow. The following call details are displayed: The popover call variable header and the call variables configured by the administrator. Active Participants : The phone numbers of the active participants in the call. Held Participants : The phone numbers of the held participants in the call. The Held Participants information is not available for unmonitored
                                                devices. For example, customer or external devices. Note Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. Duration : The duration of the call. Call Status : The current status of the call. Indicates the status of the expanded agent in the call. Queue Name : The customer service queue to which the call belongs to. | Note | Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. |
| Note | Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. |

| Note | Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. |
|---|---|

| Step 1 | From the Team Name drop-down, choose the agent's team. |
|---|---|
| Step 2 | From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox. |
| Step 3 | In the Actions tab of the selected agent, click > View History . The following call details of the selected agent's Recent Call History are displayed: Start Time : Indicates the start time of the call. Duration : Indicates the call duration. Type : Indicates if the call was an Inbound or Outbound. Number : Indicates the phone number of the call. Disposition : Indicates the action taken on the call. Queue : Indicates the name of the queue assigned to the agent. Wrap-Up Reason : Indicates the Wrap-Up Reason selected by the agent. Note You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. Note To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. | Note | You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. | Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. |
| Note | You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. |

| Note | You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
|---|---|

| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. |
|---|---|

| Step 1 | From the Team Name drop-down, choose the agent's team. |
|---|---|
| Step 2 | From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox. |
| Step 3 | In the Actions tab of the selected agent, click > View History . The following details of the selected agent's Recent State History are displayed: Start Time : Indicates the start time of the call. State : Indicates the agent state. In the Team Performance gadget, when an agent state changes to Wrap-Up, the corresponding state
                                                in the Recent State History gadget will display as WORK_READY . Reason : Indicates the wrap-up reason of the call. Duration : Indicates the call duration. Note You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. Note To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. | Note | You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. | Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. |
| Note | You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. |

| Note | You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
|---|---|

| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. |
|---|---|

| Step 1 | From the Team Name drop-down list, choose the agent's
                                       team. |
|---|---|
| Step 2 | From the displayed list, choose the agent whose state you want to change. |
| Step 3 | In the Actions tab of the selected agent, click and choose: Ready To force the agent state to Ready. Not Ready To force the agent state to Not Ready. Sign Out To sign the agent out. In the Actions tab, the Ready, Not Ready, and Sign Out options are active only if the action is allowed. For example, if you select an agent who is in Ready state, you will see only the Not Ready and Sign Out options. If you select
                                          an agent who is in Not Ready state, you will see only the Ready and Sign Out options. If you sign out an agent on an active call (in Talking state), or has a call
                                          on hold (in Hold state), that agent is immediately signed out of the desktop
                                          but the call is retained. | Ready | To force the agent state to Ready. | Not Ready | To force the agent state to Not Ready. | Sign Out | To sign the agent out. |
| Ready | To force the agent state to Ready. |
| Not Ready | To force the agent state to Not Ready. |
| Sign Out | To sign the agent out. |

| Ready | To force the agent state to Ready. |
|---|---|
| Not Ready | To force the agent state to Not Ready. |
| Sign Out | To sign the agent out. |

| Step 1 | From the Team Name drop-down list, choose the team whose
                                       agents you want to monitor. |
|---|---|
| Step 2 | From the displayed list, choose an agent to monitor. |
| Step 3 | In the Actions tab of the selected agent, click > Monitor . The silent monitor call appears in the call control area of the desktop. The Hold , Barge In , and End buttons are enabled. Click: Hold To place the call on hold. Retrieve To retrieve the call placed on hold. Barge In To barge in to the call. | Hold | To place the call on hold. | Retrieve | To retrieve the call placed on hold. | Barge In | To barge in to the call. |
| Hold | To place the call on hold. |
| Retrieve | To retrieve the call placed on hold. |
| Barge In | To barge in to the call. |
| Step 4 | To end the silent monitor call, click End . Note The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. | Note | The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. |
| Note | The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. |

| Hold | To place the call on hold. |
|---|---|
| Retrieve | To retrieve the call placed on hold. |
| Barge In | To barge in to the call. |

| Note | The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. |
|---|---|

| Note | You can only barge in on a call that you are silently monitoring. For the supervisor to be able to barge in, the agent and supervisor
                                                extensions must have visibility to each other's partition or calling
                                                search space (CSS) without any prefix or steering digit. |
|---|---|

| Step 1 | From the Team Name drop-down list, choose the agent's
                                       team. |
|---|---|
| Step 2 | From the displayed list, choose an agent in the Talking state. |
| Step 3 | In the Actions tab of the selected agent, click > Monitor . The silent monitor call appears in the call control area of your desktop. The Barge In button appears. |
| Step 4 | Click Barge In . The call becomes a conference call between you, the agent, and the caller. |

| Step 1 | Click the Drop drop-down. |
|---|---|
| Step 2 | Click the agent to drop from the list of participants. |

| Note | Even if an agent initiates a conference call, only the supervisor can drop an agent from the call. The Supervisor cannot drop
                                          a CTI Route Point, IVR Port, or a caller. |
|---|---|

| Step 1 | In the Finesse desktop, click the Team Message icon. |
|---|---|
| Step 2 | In the Compose Message box, enter the broadcast message (maximum number of characters allowed is 255). |
| Step 3 | Select the team or teams to send the message by checking the check box next to the team name. Note You can send multiple messages to a single team, multiple teams, or all teams. | Note | You can send multiple messages to a single team, multiple teams, or all teams. |
| Note | You can send multiple messages to a single team, multiple teams, or all teams. |
| Step 4 | From the drop-down, you can set an expiry time for the composed messages: starting at 5 minutes and ending at 23:55 hours.
                                       The time is displayed in hours and minutes. However, this time frame can be edited. |
| Step 5 | Click Send . You can view the latest messages sent by clicking Show recent messages . If you wish to delete any or all messages, check the check box next to the message. Click Delete and confirm the deletion. The message is removed from active display and the previous non-expired team message will become the active message for the
                                          agent. Note Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . | Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |
| Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |

| Note | You can send multiple messages to a single team, multiple teams, or all teams. |
|---|---|

| Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |
|---|---|

| Note | The rate at which messages (create/delete) are published to the teams involved, is capped at  per hour and the maximum number
                                          of active messages allowed is . If the limit of active messages is reached, supervisors will not be able to broadcast new
                                          messages until an existing team message is deleted or it expires. As there are no individual limitations on supervisors, either one or all supervisors can broadcast messages up to the maximum
                                          active messages limit. |
|---|---|

| Note | The columns of all the tables available in Advanced Supervisor Capability gadget can be resized except for the tables in Calendar View (available in Application Management ) and Calendar Management page. When you click the Application Management , Calendar Management , or Outbound Campaign Management tab, the corresponding data is refreshed. When you try to access Advanced Capabilities for the first time, if you do not have CA signed certificate, you are prompted to accept the Unified CCX certificates. Accept
                                       the certificates to enable all the functionalities. |
|---|---|

| Step 1 | Select Include Logged Out Agents to list all the logged out agents. To identify the logged out agents in the list, an asterisk is displayed next to the agent
                                                   name. Based on the skills and competency, agents are appropriately listed in the respective sections of the table. Note If Include Logged Out Agents is already selected, all the agents are listed. Clear Include Logged Out Agents so that only the agents who are logged in to Finesse desktop are listed in the table. | Note | If Include Logged Out Agents is already selected, all the agents are listed. Clear Include Logged Out Agents so that only the agents who are logged in to Finesse desktop are listed in the table. |
|---|---|---|---|
| Note | If Include Logged Out Agents is already selected, all the agents are listed. Clear Include Logged Out Agents so that only the agents who are logged in to Finesse desktop are listed in the table. |
| Step 2 | Select one or more agents to be added to the queue. |
| Step 3 | Select Add at to add the agent to the queue as per the schedule. Click the Clear icon to clear the schedule. Note If you do not select the date and time, agent is immediately added to the queue. | Note | If you do not select the date and time, agent is immediately added to the queue. |
| Note | If you do not select the date and time, agent is immediately added to the queue. |
| Step 4 | Select Remove at to remove agent from the queue as per the schedule. Click the Clear icon to clear the schedule. Note If you do not select the date and time, agent remains associated with the queue. | Note | If you do not select the date and time, agent remains associated with the queue. |
| Note | If you do not select the date and time, agent remains associated with the queue. |
| Step 5 | Click Save to add and schedule (add and remove) the selected agents for the CSQ. When you select a single agent to be scheduled or added immediately to the queue, you are directed to the Agent Scheduled tab or Manage Queue page respectively. If multiple agents are selected, a Summary page is displayed with the status of the agents who are being added and scheduled. While adding or removing an agent for a queue, if there are common skills across queues, a confirmation message is displayed.
                                                      Based on the confirmation, the changes impact all the queues that have common skills to which the agent is associated. If you select No , the action is canceled. If you select Yes , the update is as follows: Add Impact If date and time are not selected for Add at , the agent is immediately added to the selected queue and to all the impacted queues. If date and time are selected for Add at , the agent is scheduled to be added to the selected queue. At the scheduled time, the agent is added to the selected queue
                                                            and to all the impacted queues. Remove Impact If date and time are selected for Remove at , the agent is scheduled to be removed from the selected queue. At the scheduled time, the agent is removed from the selected queue and from all the impacted queues. |

| Note | If Include Logged Out Agents is already selected, all the agents are listed. Clear Include Logged Out Agents so that only the agents who are logged in to Finesse desktop are listed in the table. |
|---|---|

| Note | If you do not select the date and time, agent is immediately added to the queue. |
|---|---|

| Note | If you do not select the date and time, agent remains associated with the queue. |
|---|---|

| Note | If you close this page before all the tasks are complete, the page cannot be retrieved. The tasks that need confirmation (for
                                                      adding or scheduling) are aborted. |
|---|---|

| Step 1 | Select Include Logged Out Agents to list the agents who are logged out of Finesse desktop. To identify the logged out agents in the list, an asterisk is displayed next to the agent name. |
|---|---|
| Step 2 | Select Add at to add or modify the date and time of the schedule. Click the Clear icon to clear the schedule. Click the Undo icon to revert to the previous schedule. Note When you clear Add at , the Add at schedule is cleared and the Remove at schedule is disabled. After clearing Add at , click the Undo icon to revert to the previous schedule. The Add at schedule is retrieved and the Remove at schedule is enabled. | Note | When you clear Add at , the Add at schedule is cleared and the Remove at schedule is disabled. After clearing Add at , click the Undo icon to revert to the previous schedule. The Add at schedule is retrieved and the Remove at schedule is enabled. |
| Note | When you clear Add at , the Add at schedule is cleared and the Remove at schedule is disabled. After clearing Add at , click the Undo icon to revert to the previous schedule. The Add at schedule is retrieved and the Remove at schedule is enabled. |
| Step 3 | Select Remove at to add or modify the date and time of the schedule. Click the Clear icon to clear the schedule. Click the Undo icon to revert to the previous schedule. Note When you clear Remove at , only the Remove at schedule of that agent is cleared. After clearing Remove at , click the Undo icon to revert to the previous schedule. | Note | When you clear Remove at , only the Remove at schedule of that agent is cleared. After clearing Remove at , click the Undo icon to revert to the previous schedule. |
| Note | When you clear Remove at , only the Remove at schedule of that agent is cleared. After clearing Remove at , click the Undo icon to revert to the previous schedule. |
| Step 4 | Click Save to save the modified schedule. If you modify the schedule of only one agent, you will remain on the same page, where the success or error message is displayed.
                                                   If you have modified the schedule of more than one agent, a Summary page is displayed with the status of the agents who are being rescheduled. Note If the Add at schedule of the agents are cleared, the schedules of those agents are canceled and are listed in the Agents Available tab. The add and remove impact scenarios are same as mentioned in Agents Available . | Note | If the Add at schedule of the agents are cleared, the schedules of those agents are canceled and are listed in the Agents Available tab. The add and remove impact scenarios are same as mentioned in Agents Available . |
| Note | If the Add at schedule of the agents are cleared, the schedules of those agents are canceled and are listed in the Agents Available tab. The add and remove impact scenarios are same as mentioned in Agents Available . |

| Note | When you clear Add at , the Add at schedule is cleared and the Remove at schedule is disabled. After clearing Add at , click the Undo icon to revert to the previous schedule. The Add at schedule is retrieved and the Remove at schedule is enabled. |
|---|---|

| Note | When you clear Remove at , only the Remove at schedule of that agent is cleared. After clearing Remove at , click the Undo icon to revert to the previous schedule. |
|---|---|

| Note | If the Add at schedule of the agents are cleared, the schedules of those agents are canceled and are listed in the Agents Available tab. The add and remove impact scenarios are same as mentioned in Agents Available . |
|---|---|

| Note | If you close this page before all the tasks are complete, the page cannot be retrieved. The tasks that need confirmation (for
                                                      rescheduling) are canceled. |
|---|---|

| Note | You can remove only one agent at a time. |
|---|---|

| Step 1 | Click the remove icon of the respective agent. A confirmation message is displayed. |
|---|---|
| Step 2 | Click Yes to remove the agent from the queue. If removing the agent from the selected queue impacts other queues, a confirmation message is displayed. |
| Step 3 | Click Yes to remove the agent from the selected queue and from all the impacted queues. If the agent is removed from the queue, a success message is displayed else a failure message is displayed. |
| Step 4 | Click No to retain the agent in the selected queue and in all the impacted queues. When you select No , it overrides the earlier selection for delete. |

| Note | The Default Script Parameters tab is displayed only when a default script is associated with the application. When there is an error in execution of the other script that is configured, the Default Script is run. |
|---|---|

| Step 1 | In the Prompts tab of the Script Parameters tab, select the required prompts from the list. By default, the prompts that are assigned by the administrator are selected. Select None , if you do not want to assign any prompt. Click Yes to confirm the selection. Only the relative path of the prompt is displayed. The absolute path (language specific) is selected based on the system configuration. If the script selected by the administrator has a default prompt, Default Prompt is selected for the corresponding prompt in the Prompts tab. |
|---|---|
| Step 2 | Click the Play icon, which is next to the selected prompt to listen to the prompt. You cannot play a Default Prompt . If the prompt that you have selected is available in more than one language, you have to select a language to play the prompt.
                                                Based on the language configured by the administrator, corresponding language prompts are played to the customers. |
| Step 3 | Click Save . If you try to navigate out of this tab without saving, a confirmation message is displayed to save the changes. |
| Step 4 | Select the Calendars tab. |
| Step 5 | In the Calendars tab, select the required calendars from the list. Select None , if you do not want to assign any calendar. Click Yes to confirm the selection. |
| Step 6 | Click the preview icon, which is next to the selected calendar to view the calendar details. |
| Step 7 | Click Save to associate the selected prompts and calendars with the application. If you try to navigate out of this tab without saving, a confirmation message is displayed to save the changes. |
| Step 8 | Select the Default Script Parameters tab. Based on the default script that is selected by the administrator, the parameters for prompts and calendars are selected. |
| Step 9 | Modify the required prompts and calendars. |
| Step 10 | Click Save to make the selected prompts and calendars as part of the default script. |

| Step 1 | Select Fixed Hours . By default, Monday to Friday is selected. |
|---|---|
| Step 2 | Check or uncheck the days from the Day column. |
| Step 3 | Select the working hours, From and To from Time Range 1 column. Similarly, select working hours for Time Range 2 and Time Range 3 . The time range is applicable for all the days that are selected in the Day column. The order of selection is from Time Range 1 to Time Range 3 . |
| Step 4 | Click Save . |

| Step 5 | Select Flexible Hours . By default, Monday to Friday is selected. If you have made some changes in Fixed Hours , a confirmation message is displayed to save the changes. Clicking Yes updates the database. |
|---|---|
| Step 6 | Check or uncheck the days from the Day column. |
| Step 7 | Select the working hours, From and To from Time Range 1 column for each day. Similarly, select working hours for Time Range 2 and Time Range 3 . The time range has to be configured for each selected day. |
| Step 8 | Click Save . |

| Step 1 | Enter a name for the custom business day in Name of the Day column. |
|---|---|
| Step 2 | Select a date in Date column. |
| Step 3 | Select the working hours, From and To from Time Range 1 column. Similarly, select working hours for Time Range 2 and Time Range 3 . |
| Step 4 | Click Add Day to add a custom business day. |
| Step 5 | Click the delete icon to delete the corresponding custom business day. |
| Step 6 | Click Save . |

| Step 1 | Enter a holiday name in the Name of the Day column. |
|---|---|
| Step 2 | Select a date in Date column. |
| Step 3 | Click Add Day to add more holidays. |
| Step 4 | Click the delete icon to delete a holiday. |
| Step 5 | Click Save . |

| Note | Callback option is not available for IVR campaigns. |
|---|---|

| Note | For reference, the server time zone is displayed at the bottom of the window. |
|---|---|

| Step 1 | Click Update Contacts for the required campaign in the Outbound Campaign Management tab. |
|---|---|
| Step 2 | The Update Contacts page displays the following: Field Description Contacts Remaining The number of contacts that are yet to be dialed for the campaign. Manual Import To import the contacts that are to be dialed for the campaign. This tab is selected by default. Schedule Import To schedule import of contacts that are to be dialed for the campaign. Note If you want the option to schedule import of contacts for a campaign, contact your administrator. | Field | Description | Contacts Remaining | The number of contacts that are yet to be dialed for the campaign. | Manual Import | To import the contacts that are to be dialed for the campaign. This tab is selected by default. | Schedule Import | To schedule import of contacts that are to be dialed for the campaign. Note If you want the option to schedule import of contacts for a campaign, contact your administrator. | Note | If you want the option to schedule import of contacts for a campaign, contact your administrator. |
| Field | Description |
| Contacts Remaining | The number of contacts that are yet to be dialed for the campaign. |
| Manual Import | To import the contacts that are to be dialed for the campaign. This tab is selected by default. |
| Schedule Import | To schedule import of contacts that are to be dialed for the campaign. Note If you want the option to schedule import of contacts for a campaign, contact your administrator. | Note | If you want the option to schedule import of contacts for a campaign, contact your administrator. |
| Note | If you want the option to schedule import of contacts for a campaign, contact your administrator. |
| Step 3 | Click the Delete icon to delete the contacts from the database. Delete is applicable for contacts that are imported manually and through Schedule Import . A confirmation message is displayed. |
| Step 4 | Click Yes to delete the contacts. The campaign is disabled, contacts are deleted, and the value of Contacts Remaining is updated to 0 . |

| Field | Description |
|---|---|
| Contacts Remaining | The number of contacts that are yet to be dialed for the campaign. |
| Manual Import | To import the contacts that are to be dialed for the campaign. This tab is selected by default. |
| Schedule Import | To schedule import of contacts that are to be dialed for the campaign. Note If you want the option to schedule import of contacts for a campaign, contact your administrator. | Note | If you want the option to schedule import of contacts for a campaign, contact your administrator. |
| Note | If you want the option to schedule import of contacts for a campaign, contact your administrator. |

| Note | If you want the option to schedule import of contacts for a campaign, contact your administrator. |
|---|---|

| Step 1 | Click Select File , browse, and select the file that you want to import. |
|---|---|
| Step 2 | Enable Allow Duplicate Contacts if you want to save duplicate contacts in the database. |
| Step 3 | Select appropriate fields from Column 1 to Column 7 in the same order as they are in the CSV file. Predective and Progressive Campaigns have six columns and Direct Preview Campaigns have seven columns. |
| Step 4 | Click Save . The contacts from the selected file are imported into the Unified CCX database. The progress of importing contacts is displayed at the top of the page. If you close the page, the progress is displayed in
                                                the Contacts Remaining column of the Outbound Campaign Management page. Note During manual import, if you go to the Update Contacts page the status is displayed at the top the page and the Delete icon is disabled. After the import of contacts is complete, the Contacts Remaining and Last Import information is updated and the Delete icon is enabled. | Note | During manual import, if you go to the Update Contacts page the status is displayed at the top the page and the Delete icon is disabled. After the import of contacts is complete, the Contacts Remaining and Last Import information is updated and the Delete icon is enabled. |
| Note | During manual import, if you go to the Update Contacts page the status is displayed at the top the page and the Delete icon is disabled. After the import of contacts is complete, the Contacts Remaining and Last Import information is updated and the Delete icon is enabled. |

| Note | During manual import, if you go to the Update Contacts page the status is displayed at the top the page and the Delete icon is disabled. After the import of contacts is complete, the Contacts Remaining and Last Import information is updated and the Delete icon is enabled. |
|---|---|

| Step 1 | Enable Allow Duplicate Contacts if you want to save duplicate contacts in the database. |
|---|---|
| Step 2 | Select appropriate fields from Column 1 to Column 7 in the same order as they are in the CSV file. Predictive and Progressive Campaigns have six columns and Direct Preview Campaigns have seven columns. |
| Step 3 | Select appropriate Start Date . |
| Step 4 | Select appropriate Start Time . |
| Step 5 | Select Repeat Every Hours , if the contacts are being updated regularly. |
| Step 6 | Enable Schedule . |
| Step 7 | Click Save . A confirmation message is displayed. The contacts from the predefined file are imported into the Unified CCX database at the scheduled date and time. To view the
                                                status of the scheduled import of contacts, revisit this tab. |