---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1262-admin-guide-cfin-b-1262-cis-df40660964
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1262/admin/guide/cfin_b_1262_cisco-finesse-administration-guide/cfin_m_1261-manage-workflows.html
retrieved_at: 2026-08-21T15:55:42.355109+00:00
---

Cisco Finesse Administration Guide, Release 12.6(2)

# Cisco Finesse Administration Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Manage Workflows

## Chapter: Manage Workflows

# Manage Workflows

## Workflows and Workflow Actions

You can use workflows to automate common repetitive agent tasks. A workflow has a unique name and a helpful description. Use
                              the Manage Workflows and Manage Workflow Actions gadgets to view, add, edit, or delete workflows and workflow actions.

All workflows are team-level workflows. You cannot create a global workflow. If you need a global workflow, create a team
                              workflow and assign it to all teams.

Cisco Finesse supports the following number of workflows and workflow actions:

100 workflows per Cisco Finesse system

100 actions per Cisco Finesse system

20 workflows per team

Five conditions per workflow

Five actions per workflow

Five variables per action

The following fields can be used to configure workflows:

queueNumber

queueName

callKeyCallId

callKeyPrefix

callKeySequenceNum

wrapUpReason

For Voice - Call variables, Outbound Option variables, queue details, wrap-up reasons, agent details, or team details.

For Email - Queue name and email attributes like From, To, Cc, Bcc, or Subject.

For Chat - Queue name, chat type, or system defined customer details as available from the web chat form.

Click the column headers to sort workflows and workflow actions in ascending or descending order.

The following table describes the fields on the Manage Workflows gadget:

Field

Explanation

Name

The name of the workflow must be unique and can have a maximum length of 40 characters.

Description

The description of the workflow can have a maximum length of 128 characters.

Media

The media of the workflow. You can configure the media to Voice and any preferred Digital Channel.

The following table describes the fields on the Manage Workflow Actions gadget:

Field

Name

The name of the workflow action must be unique and can have a maximum length of 64 characters.

Type

The type of workflow. Possible values are Browser Pop and HTTP Request.

Actions on the Manage Workflows and Manage Workflow Actions gadgets:

New: Add a new workflow or workflow action

Edit: Edit a workflow or workflow action

Delete: Delete a workflow or workflow action

Refresh: Reload the list of workflows or workflow actions from the server.

You can configure workflow actions to be handled by the Cisco Finesse desktop or in a third-party gadget. A third-party gadget
                              can be designed to handle the action differently than Cisco Finesse does.

Each workflow must contain only one trigger. Triggers are based on Cisco Finesse dialog events.

Voice dialog events include the following:

When a Call arrives

When a Call is answered

When a Call ends

When making a Call

The call variable workflow responds as expected only when you add both the conditions Is not equal and Is not empty .

While previewing an Outbound Option call.

Digital Channels dialog events include the following:

When a task is offered

When a task is accepted

Some solutions such as ECE don’t provide a separate accept task functionality. Therefore, the tasks that are offered are auto
                                                      accepted, which simultaneously generate the task is accepted event along with the task is offered event. In such scenarios, use only one event ( task is accepted or task is offered ) for configuring workflows because there is no difference between these two events.

When a task is active

When a task is paused

When a task is interrupted

When a task is closed

The workflow engine uses the following simple logic to determine whether to run a workflow:

The workflow logic and examples are similar for all media.

Its trigger set and conditions are evaluated against each dialog event received.

The workflow engine processes workflow events for the first call that matches any configured workflow's trigger set and conditions.
                                    No other workflows run until this call has ended. If the agent accepts a second call while still on the first call, workflows
                                    do not run on the second call even after the first call has ended.

After a workflow for a particular trigger type (for example, Call Arrives) runs, it never triggers again for the same dialog
                                    ID.

The workflow engine caches workflows for an agent when the agent signs in. Workflows do not change for the agent until the
                              agent signs out and signs in again or refreshes the browser.

Whenever the browser is refreshed, the workflows that trigger the following events run:

when a call arrives

when a call is answered

when making a call

When an agent refreshes the browser, the workflow engine considers the call as newly arrived or newly made. If an HTTP request
                                          action is part of the workflow, the HTTP request is sent when the agent refreshes the browser. Applications that receive the
                                          HTTP requests must account for this scenario.

An example of a workflow is a Call Arrival event that triggers an action that collects information from the dialog event (for
                              example, the ANI or customer information) and displays a web page containing customer information.

You can filter trigger events by the value of the data that comes in the event. You can configure a workflow to run if any
                              of the conditions are met or if all the conditions are met.

Individual conditions comprise of the following:

A piece of event data to be examined. For example, DNIS or call variables.

A comparison between the event data and the values entered (for example contains , is equal to , is not equal to , begins with , ends with , is empty , is not empty , and is in list ).

When the trigger and its conditions are satisfied, a list of actions assigned to the workflow are run. The actions are run
                              in the listed order.

Workflows run only for agents and supervisors who are Cisco Finesse users. The Workflow Engine is a JavaScript library that
                              runs client-side on a per-user basis within the Cisco Finesse desktop application. The desktop retrieves the workflows that
                              are to be run for a user from the server when the user signs in or when the browser is refreshed.

Changes made to a workflow or its actions while a user is signed in are not automatically pushed to that user.

It is possible to set workflows, conditions, and actions that are contradictory so that a workflow or action cannot function.
                              Workflows are not validated.

If multiple workflows are configured for a team, the Workflow Engine evaluates them in the configured order. The Workflow
                              Engine ignores workflows with no actions. When the Workflow Engine finds a workflow with a matching trigger for an event and
                              the workflow conditions evaluate to true, that workflow is used, and the subsequent workflows in the list are not evaluated.
                              Workflows with no conditions evaluate to true if the event matches the workflow trigger. All workflows are enabled by default.
                              Only one workflow for a specific user can run at a time.

The Workflow Engine retrieves dialog-based variables that are used in workflow conditions from the dialog that triggered the
                              workflow. If a variable is not found in the dialog, it's value is considered to be empty.

The Workflow Engine runs the actions that are associated with the matched workflow in the order in which they are listed.
                              The Workflow Engine runs actions in a workflow even if the previously run action fails. Failed actions are logged.

The Cisco Finesse server controls the calls that are displayed to the Cisco Finesse user. If the user has multiple calls,
                              the workflow applies only to the first call that matches a trigger. If the first call displayed does not match any triggers
                              but the second call does match a trigger, the Workflow Engine evaluates and processes the triggers for the second call.

A call is considered to be the first displayed call if it is the only call on the Cisco Finesse desktop when it appears.
                              If two calls on a phone are merged (as they are in a conference call), then the first displayed call flag value of the surviving
                              call is used.

If a user has a call and the user refreshes the browser, the Workflow Engine evaluates the call as it is. If the dialog data
                              (call variable values) change, the data may not match the trigger and conditions of the original workflow. The data may match
                              a different workflow or no workflows at all.

If a user has multiple calls and the user refreshes the browser, the Workflow Engine treats the first dialog received from
                              the Cisco Finesse server as the first displayed call. This call may not be the same call that was first displayed before the
                              refreshing the browser. Dialogs received for any other call are ignored because they are not considered as first displayed
                              calls. After refreshing the browser, if dialogs for more than one call are received before the Workflow Engine is loaded,
                              none of the dialogs are evaluated because they are not considered as first displayed calls.

Workflows that are run for both Cisco Finesse agents and supervisors. The team to which the supervisor belongs (as distinguished
                              from the team that the supervisor manages) determines which workflows run for the supervisor. Put the supervisors in their
                              own team to keep agent workflows from being run for them.

### Workflow Triggers and Outbound Calls

When you create a workflow specifically for Outbound Option calls, add a condition of BAStatus is not empty (except for the
                                             Workflow Trigger 'When a call arrives' as BAStatus will be empty at that point of time). This condition ensures that the workflow
                                             can distinguish Outbound Option calls from agent-initiated outbound calls.

The following table illustrates when workflows trigger in outbound call scenarios:

Workflow Trigger

Direct Preview Outbound Call

Preview Outbound Call

Progressive/Predictive Outbound Call

While previewing a call

When the agent previews the call (before accepting or rejecting it)

When the agent previews the call (before accepting or rejecting it)

Does not trigger

When a call arrives

Does not trigger

When the agent accepts the call

When the call arrives on the agent desktop

When a call is answered

When the customer answers the call and during failover

When the customer answers the call and during failover

When the customer answers the call

When a call is made

When the customer call is initiated

When the customer call is initiated

When the customer call is initiated, and during failover

When a call ends

When the customer call ends

When the customer call ends

When the customer call ends

## Add Browser Pop Workflow Action

The Browser Pop workflow action opens a browser window or tab on the user's desktop when workflow conditions are met.

Whether the action opens a new window or tab on the desktop depends on the target user's browser settings.

Step 1

In the Manage Workflow Actions gadget, click New .

Step 2

In the Name box, enter a name for the action.

Workflow action names are limited to 64 characters.

Step 3

From the Type drop-down list, choose Browser Pop .

Step 4

From the Handled By drop-down list, choose what will run the action, either the Finesse Desktop or Other (a third-party gadget).

Step 5

In the Window Name box, enter the ID name of the window that is opened. Any action that uses this window name reuses that
                                       specific window.

Window names are limited to 40 characters, and can be blank. If you leave the window name blank, a new window opens every
                                                      time the action runs.

Step 6

Enter the URL of the browser window and click the tag icon at the right of the box and select one or more variables from the
                                       drop-down list to add tags.

### Example:

For every variable you select, you can enter test data in the Sample Data box. A sample URL is automatically built in the
                                          Browser URL box below the Sample Data area. To test the URL, click Open to open the URL in your browser.

Finesse does not validate the URL you enter.

Step 7

Click Save .

## Add HTTP Request Workflow Action

The HTTP Request workflow action makes an HTTP request to an API on behalf of the desktop user.

Step 1

In the Manage Workflow Actions area, click New .

Step 2

In the Name box, enter a name for the action.

A workflow action name can contain a maximum of 64 characters.

Step 3

From the Type drop-down list, select HTTP Request .

Step 4

From the Handled By drop-down list, select what will run the action, the Finesse desktop or Other (a third-party gadget).

Step 5

From the Method drop-down list, select the method to use.

You can select either PUT or POST.

Step 6

From the Location drop-down list, select the location.

If you are making the HTTP request to a Finesse API, select Finesse . If you are making a request to any other API, select Other .

Step 7

In the Content Type box, enter the content type.

The default content type is application/xml, which is the content type for Finesse APIs. If you are using a different API,
                                          enter the content types for that API (for example, application/JSON).

Step 8

In the URL box, enter the URL to which to make the request. To add variables to the URL, click the tag icon at the right of
                                       the box and select one or more variables from the drop-down list.

The drop-down list contains variables from all the configured media channels.

### Example:

When the location is FINESSE, do not specify the protocol, host, and port information. Finesse automatically fetches these
                                                      details when the REST request is run.

If you want to make a request to another API, you must enter the entire URL (for example, http://googleapis.com).

You can click the tag icon at the right of the box and select one or more variables from the drop-down list to add tags to
                                          the URL. In the preceding example, to add the dialogId, click the tag icon and select dialogId from the list.

Step 9

In the Body box, enter the text for the request. The body must match the content type (for example, if the content types is
                                       application/xml, the body must contain XML). To add variables to the body, click the tag icon at the right of the box and
                                       select one or more variables from the drop-down list.

### Example:

To make an HTTP request to the Dialog - Start a recording API, enter the following into the Body box:

To add the extension, click the tag icon and select extension.

For every variable you add, you can enter test data in the Sample Data box.

Step 10

Click Save .

## Edit Workflow Action

Step 1

In the Manage Workflow Actions gadget, select the action that you want to edit.

Step 2

Click Edit .

Step 3

Edit the fields that you want to change.

Step 4

Click Save .

## Delete Workflow Action

Step 1

In the Workflow Actions gadget, select the action that you want to delete.

Step 2

Click Delete .

Step 3

Click Yes to confirm the deletion of the selected action.

## Add Workflow

Step 1

In the Manage Workflows gadget, click New .

Step 2

From the Choose Media drop-down, select the media.

In case of a voice only configuration, the Choose Media drop-down will display only Voice.

Step 3

In the Name box, enter the name of the workflow.

The name is limited to 40 characters.

Step 4

In the Description box, enter a description of the workflow.

The description is limited to 128 characters.

Step 5

In the When to perform Actions drop-down list, select the event that triggers the workflow.

The drop-down actions change depending on the selected media.

Step 6

In the How to apply Conditions box, select if all conditions are met, or if any conditions are met, and then click Add Condition to add up to five conditions.

Variables in the drop-down for conditions are grouped depending on the selected media.

### Example:

Step 7

In the Ordered List of Actions area, click Add to open the Add Actions area. Click an action in this area to add it to the Ordered List of Actions.

Step 8

Use the up and down arrows next to the Ordered List of Actions to move actions into the performance order.

Step 9

Click Save .

Step 10

Assign the workflow to one or more teams.

A workflow does not run until it is assigned to a team.

## Edit Workflow

Step 1

In the Manage Workflows gadget, select the workflow you want to edit.

Step 2

Click Edit .

The media for an existing workflow can be changed by editing the workflow.

Step 3

Edit the fields that you want to change.

Step 4

Click Save .

## Delete Workflow

Step 1

In the Manage Workflows gadget, select the workflow that you want to delete.

Step 2

Click Delete .

Step 3

Click Yes to confirm the deletion of the selected workflow.

| Field | Explanation |
|---|---|
| Name | The name of the workflow must be unique and can have a maximum length of 40 characters. |
| Description | The description of the workflow can have a maximum length of 128 characters. |
| Media | The media of the workflow. You can configure the media to Voice and any preferred Digital Channel. |

| Field | Explanation |
|---|---|
| Name | The name of the workflow action must be unique and can have a maximum length of 64 characters. |
| Type | The type of workflow. Possible values are Browser Pop and HTTP Request. |

| Note | You can configure the trigger only after you select the media. |
|---|---|

| Note | The call variable workflow responds as expected only when you add both the conditions Is not equal and Is not empty . |
|---|---|

| Note | Some solutions such as ECE don’t provide a separate accept task functionality. Therefore, the tasks that are offered are auto
                                                      accepted, which simultaneously generate the task is accepted event along with the task is offered event. In such scenarios, use only one event ( task is accepted or task is offered ) for configuring workflows because there is no difference between these two events. |
|---|---|

| Note | The workflow logic and examples are similar for all media. |
|---|---|

| Note | Whenever the browser is refreshed, the workflows that trigger the following events run: when a call arrives when a call is answered when making a call When an agent refreshes the browser, the workflow engine considers the call as newly arrived or newly made. If an HTTP request
                                          action is part of the workflow, the HTTP request is sent when the agent refreshes the browser. Applications that receive the
                                          HTTP requests must account for this scenario. |
|---|---|

| Note | Changes made to a workflow or its actions while a user is signed in are not automatically pushed to that user. |
|---|---|

| Note | When you create a workflow specifically for Outbound Option calls, add a condition of BAStatus is not empty (except for the
                                             Workflow Trigger 'When a call arrives' as BAStatus will be empty at that point of time). This condition ensures that the workflow
                                             can distinguish Outbound Option calls from agent-initiated outbound calls. |
|---|---|

| Workflow Trigger | Direct Preview Outbound Call | Preview Outbound Call | Progressive/Predictive Outbound Call |
|---|---|---|---|
| While previewing a call | When the agent previews the call (before accepting or rejecting it) | When the agent previews the call (before accepting or rejecting it) | Does not trigger |
| When a call arrives | Does not trigger | When the agent accepts the call | When the call arrives on the agent desktop |
| When a call is answered | When the customer answers the call and during failover | When the customer answers the call and during failover | When the customer answers the call |
| When a call is made | When the customer call is initiated | When the customer call is initiated | When the customer call is initiated, and during failover |
| When a call ends | When the customer call ends | When the customer call ends | When the customer call ends |

| Note | Whether the action opens a new window or tab on the desktop depends on the target user's browser settings. |
|---|---|

| Step 1 | In the Manage Workflow Actions gadget, click New . |
|---|---|
| Step 2 | In the Name box, enter a name for the action. Note Workflow action names are limited to 64 characters. | Note | Workflow action names are limited to 64 characters. |
| Note | Workflow action names are limited to 64 characters. |
| Step 3 | From the Type drop-down list, choose Browser Pop . |
| Step 4 | From the Handled By drop-down list, choose what will run the action, either the Finesse Desktop or Other (a third-party gadget). |
| Step 5 | In the Window Name box, enter the ID name of the window that is opened. Any action that uses this window name reuses that
                                       specific window. Note Window names are limited to 40 characters, and can be blank. If you leave the window name blank, a new window opens every
                                                      time the action runs. | Note | Window names are limited to 40 characters, and can be blank. If you leave the window name blank, a new window opens every
                                                      time the action runs. |
| Note | Window names are limited to 40 characters, and can be blank. If you leave the window name blank, a new window opens every
                                                      time the action runs. |
| Step 6 | Enter the URL of the browser window and click the tag icon at the right of the box and select one or more variables from the
                                       drop-down list to add tags. Example: For every variable you select, you can enter test data in the Sample Data box. A sample URL is automatically built in the
                                          Browser URL box below the Sample Data area. To test the URL, click Open to open the URL in your browser. Note Finesse does not validate the URL you enter. | Note | Finesse does not validate the URL you enter. |
| Note | Finesse does not validate the URL you enter. |
| Step 7 | Click Save . |

| Note | Workflow action names are limited to 64 characters. |
|---|---|

| Note | Window names are limited to 40 characters, and can be blank. If you leave the window name blank, a new window opens every
                                                      time the action runs. |
|---|---|

| Note | Finesse does not validate the URL you enter. |
|---|---|

| Step 1 | In the Manage Workflow Actions area, click New . |
|---|---|
| Step 2 | In the Name box, enter a name for the action. A workflow action name can contain a maximum of 64 characters. |
| Step 3 | From the Type drop-down list, select HTTP Request . |
| Step 4 | From the Handled By drop-down list, select what will run the action, the Finesse desktop or Other (a third-party gadget). |
| Step 5 | From the Method drop-down list, select the method to use. You can select either PUT or POST. |
| Step 6 | From the Location drop-down list, select the location. If you are making the HTTP request to a Finesse API, select Finesse . If you are making a request to any other API, select Other . |
| Step 7 | In the Content Type box, enter the content type. The default content type is application/xml, which is the content type for Finesse APIs. If you are using a different API,
                                          enter the content types for that API (for example, application/JSON). |
| Step 8 | In the URL box, enter the URL to which to make the request. To add variables to the URL, click the tag icon at the right of
                                       the box and select one or more variables from the drop-down list. Note The drop-down list contains variables from all the configured media channels. Example: The following is the URL example for a Finesse API: Note When the location is FINESSE, do not specify the protocol, host, and port information. Finesse automatically fetches these
                                                      details when the REST request is run. If you want to make a request to another API, you must enter the entire URL (for example, http://googleapis.com). You can click the tag icon at the right of the box and select one or more variables from the drop-down list to add tags to
                                          the URL. In the preceding example, to add the dialogId, click the tag icon and select dialogId from the list. | Note | The drop-down list contains variables from all the configured media channels. | Note | When the location is FINESSE, do not specify the protocol, host, and port information. Finesse automatically fetches these
                                                      details when the REST request is run. If you want to make a request to another API, you must enter the entire URL (for example, http://googleapis.com). |
| Note | The drop-down list contains variables from all the configured media channels. |
| Note | When the location is FINESSE, do not specify the protocol, host, and port information. Finesse automatically fetches these
                                                      details when the REST request is run. If you want to make a request to another API, you must enter the entire URL (for example, http://googleapis.com). |
| Step 9 | In the Body box, enter the text for the request. The body must match the content type (for example, if the content types is
                                       application/xml, the body must contain XML). To add variables to the body, click the tag icon at the right of the box and
                                       select one or more variables from the drop-down list. Example: To make an HTTP request to the Dialog - Start a recording API, enter the following into the Body box: To add the extension, click the tag icon and select extension. For every variable you add, you can enter test data in the Sample Data box. |
| Step 10 | Click Save . |

| Note | The drop-down list contains variables from all the configured media channels. |
|---|---|

| Note | When the location is FINESSE, do not specify the protocol, host, and port information. Finesse automatically fetches these
                                                      details when the REST request is run. If you want to make a request to another API, you must enter the entire URL (for example, http://googleapis.com). |
|---|---|

| Step 1 | In the Manage Workflow Actions gadget, select the action that you want to edit. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | Edit the fields that you want to change. |
| Step 4 | Click Save . |

| Step 1 | In the Workflow Actions gadget, select the action that you want to delete. |
|---|---|
| Step 2 | Click Delete . |
| Step 3 | Click Yes to confirm the deletion of the selected action. |

| Step 1 | In the Manage Workflows gadget, click New . |
|---|---|
| Step 2 | From the Choose Media drop-down, select the media. Note In case of a voice only configuration, the Choose Media drop-down will display only Voice. | Note | In case of a voice only configuration, the Choose Media drop-down will display only Voice. |
| Note | In case of a voice only configuration, the Choose Media drop-down will display only Voice. |
| Step 3 | In the Name box, enter the name of the workflow. Note The name is limited to 40 characters. | Note | The name is limited to 40 characters. |
| Note | The name is limited to 40 characters. |
| Step 4 | In the Description box, enter a description of the workflow. Note The description is limited to 128 characters. | Note | The description is limited to 128 characters. |
| Note | The description is limited to 128 characters. |
| Step 5 | In the When to perform Actions drop-down list, select the event that triggers the workflow. Note The drop-down actions change depending on the selected media. | Note | The drop-down actions change depending on the selected media. |
| Note | The drop-down actions change depending on the selected media. |
| Step 6 | In the How to apply Conditions box, select if all conditions are met, or if any conditions are met, and then click Add Condition to add up to five conditions. Note Variables in the drop-down for conditions are grouped depending on the selected media. Example: For example, you can specify that the action is taken when CallVariable 1 equals 123 and CallVariable 2 begins with 2. | Note | Variables in the drop-down for conditions are grouped depending on the selected media. |
| Note | Variables in the drop-down for conditions are grouped depending on the selected media. |
| Step 7 | In the Ordered List of Actions area, click Add to open the Add Actions area. Click an action in this area to add it to the Ordered List of Actions. |
| Step 8 | Use the up and down arrows next to the Ordered List of Actions to move actions into the performance order. |
| Step 9 | Click Save . |
| Step 10 | Assign the workflow to one or more teams. Note A workflow does not run until it is assigned to a team. | Note | A workflow does not run until it is assigned to a team. |
| Note | A workflow does not run until it is assigned to a team. |

| Note | In case of a voice only configuration, the Choose Media drop-down will display only Voice. |
|---|---|

| Note | The name is limited to 40 characters. |
|---|---|

| Note | The description is limited to 128 characters. |
|---|---|

| Note | The drop-down actions change depending on the selected media. |
|---|---|

| Note | Variables in the drop-down for conditions are grouped depending on the selected media. |
|---|---|

| Note | A workflow does not run until it is assigned to a team. |
|---|---|

| Step 1 | In the Manage Workflows gadget, select the workflow you want to edit. |
|---|---|
| Step 2 | Click Edit . Note The media for an existing workflow can be changed by editing the workflow. | Note | The media for an existing workflow can be changed by editing the workflow. |
| Note | The media for an existing workflow can be changed by editing the workflow. |
| Step 3 | Edit the fields that you want to change. |
| Step 4 | Click Save . |

| Note | The media for an existing workflow can be changed by editing the workflow. |
|---|---|

| Step 1 | In the Manage Workflows gadget, select the workflow that you want to delete. |
|---|---|
| Step 2 | Click Delete . |
| Step 3 | Click Yes to confirm the deletion of the selected workflow. |