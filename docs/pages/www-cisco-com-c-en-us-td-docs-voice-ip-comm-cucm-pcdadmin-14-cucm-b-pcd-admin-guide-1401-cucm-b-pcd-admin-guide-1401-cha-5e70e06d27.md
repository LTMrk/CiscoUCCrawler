---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-14-cucm-b-pcd-admin-guide-1401-cucm-b-pcd-admin-guide-1401-cha-5e70e06d27
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/14/cucm_b_pcd-admin-guide-1401/cucm_b_pcd-admin-guide-1401_chapter_0100.html
retrieved_at: 2026-08-17T00:35:43.974822+00:00
---

Prime Collaboration Deployment Administration Guide, Release 14 and SUs

# Prime Collaboration Deployment Administration Guide, Release 14 and SUs

Updated: November 25, 2025

Chapter: Cisco Prime Collaboration Deployment Administrative Interface Elements

## Chapter: Cisco Prime Collaboration Deployment Administrative Interface Elements

# Cisco Prime Collaboration Deployment Administrative Interface Elements

## Common
                        	 Administrative Interface Elements

The
                              			 following elements are common to all views in the Cisco Prime Collaboration
                              			 Deployment administration interface.

Open and
                                          						close navigation button

Provides
                                          						you access to navigate to menus, which appear in a vertical pane. Click this
                                          						button view and hide the menus.

When you sign in to the application for the first time, a
                                                      						  transparent grey screen appears indicating this button. This screen also shows
                                                      						  a pop-up message to turn off the indication.

Search
                                          						and Indexing

Displays
                                          						the search text box to allow search in the application. It also displays the
                                          						options Cisco Prime Collaboration Deployment as index.

To
                                                      						  view the search option, click the open and close navigation button.

About

Provides the version of the Cisco Prime Collaboration Deployment. This setting
                                          						also includes copyright and trademark information.

Logout

Exits
                                          						from the server.

Help

Provides context-sensitive help information.

Information ("i" button)

Provides information about the current page that you are viewing.

Getting
                                          						Started (flag button)

Provides information about getting started to perform system-level tasks on the
                                          						server.

## Monitoring View
                        	 Elements

After a task is scheduled, you can monitor, and control the tasks by using the Monitoring
                              		  page.

Task
                                          						Queue

A list
                                          						of all the tasks contained in Cisco Prime Collaboration Deployment. This list can include any of the following tasks:

Scheduled

Canceled

Started

Paused

Paused due to Error

Successful

Failed

Upgrade Tasks

Switch Version Tasks

Server Restart Tasks

Readdress Tasks

Install Tasks

Migrate Tasks

Click one of the tasks in the Task Queue to open the details for that task in the
                                          						right top panel.

Task
                                          						status

The top
                                          						right portion of the Monitoring page shows the following information for a given task:

Status

Start time

Task
                                                							 data (for example: cluster data)

To see
                                          						details about the task, click on the View Log link.

The
                                          						following are the possible statuses for tasks:

Successful—Indicates that the task has finished without errors.

Started—Indicates that the task is currently running.

Scheduled—Indicates that the task has been scheduled, but has
                                                							 not yet started.

Manual Start—Indicates that the task is waiting to be started (user created the
                                                							 task with the "Start Task Manually" option).

Canceled—Indicates that the user chose not to run the task.

Paused—Indicates that the task is in a paused state waiting
                                                							 for feedback.

Paused due To Error—Indicates that the task is in a paused
                                                							 state due to an error in the system.

Failed—Indicates that the task has stopped because of an error.

Failed to Schedule—Indicates that the task was not
                                                							 scheduled, due to an error that occurred.

Failed to Cancel—Indicates that the user tried unsuccessfully to cancel the task. This typically happens when the task is
                                                in
                                                							 a final state (no actions are left to cancel).

Canceling—Indicates that the user canceled the
                                                							 task, but the task is in a state that will take a long time to cancel. The task
                                                							 may be in this state for an hour or more if the task being canceled is an
                                                							 installation or migration task (during the install-new-server phase).

Possible messages and actions in a Successful Status state:

Task
                                                							 completed successfully

Delete—Deletes the task data permanently

Possible
                                          						actions in a Started state:

Cancel—Cancels the selected task

Delete—Deletes the selected task permanently

Possible actions in a Scheduled state:

Cancel—Cancels the selected task

Delete—Deletes the selected task permanently

Possible
                                          						actions in a Waiting for
                                             						  Manual Start state:

Start—Starts the task (You will see this button only if the
                                                							 Manual Start option was chosen when the task was created)

Delete—Deletes the selected task permanently

Possible
                                          						actions in a Paused state (a task enters this state if  the user
                                          						set up the task to pause at this step):

Resume—Task will continue at the next step

Cancel—Cancels the selected task

Delete—Deletes the selected task permanently

Possible
                                          						actions in a Paused
                                             						  Due To Errors state (a task will enter this state, because the system
                                          						detected an error at this step):

Resume—Task will continue at the next step. (Before resuming, user should look at the error in the view log and correct the
                                                problem that caused the error, or else the task will fail.) If the error message says "Failed due to validation," the task will revalidate and start from the first step when you click Resume. Otherwise, the task will start from the next
                                                step or sub-step.

Retry—Retry the last failed task action (the failed next step or sub-step)

Cancel—Cancels the selected task

Delete—Deletes the selected task permanently

Possible
                                          						action in a Failed
                                             						  Status state:

Delete—Deletes the selected task permanently

Start
                                          						Task button

Starts
                                          						task running for Scheduled tasks

Edit
                                          						button

Opens
                                          						Edit dialog for Scheduled tasks

Pause
                                          						button

Pauses
                                          						Running tasks (at next step)

Resume
                                          						button

Resumes
                                          						task at next step for Paused and Paused (Error) tasks

Retry Button

Retries the last failed task action for Paused (Error) tasks

Cancel
                                          						button

Cancels
                                          						Scheduled, Running, Paused, and Paused (Error) tasks

Delete
                                          						button

Deletes
                                          						Scheduled, Canceled, Successful, and Failed tasks

Task
                                          						Summary

The Task
                                          						Summary section contains the following information for a task:

Source Cluster

Destination Cluster

Unified Communications Manager Upgrade File

Unified Presence Upgrade File

## Tasks View
                        	 Elements

### Upgrade
                           	 View

Scheduled Tasks and History table

Status

Provides information about the upgrade task:

Successful—Indicates that the task has finished without errors

Running—Indicates that the task is currently running

Scheduled—Indicates that the task has not yet started

Canceled—Indicates that the user has chosen not to run task

Paused—Indicates that the task is in a paused state waiting for feedback

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Failed—Indicates that the task has stopped due to error

Start Time

Specifies the start time of the upgrade task

Last Status Report Time

Specifies the time at which the action was completed. The completed action may be a success or failure.

Cluster

Specifies the name of the upgraded cluster

Notes

Note added during the Review portion of the Add Upgrade Task wizard

Actions

Allows you to perform the following for a particular upgrade task

Depending on the state of the task, only some of these actions may be allowed (for example, an upgrade task that is completed
                                                         cannot be canceled).

Scheduled status:

Run Validation Test—Runs a validation test to ensure that all nodes are available and the iso to be used for upgrade is present.

Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task

Cancel Task—Cancels the selected task

Delete—Deletes the selected task permanently

Canceled status:

Delete—Deletes the selected task permanently

Started status:

Cancel Task—Cancels the selected task

Paused status:

Resume—Use this button to restart task at the next step.

View Details—Navigates to the monitoring page showing all the tasks available

Start Task—Start task is present if the task is started manually. Time is not selected for this action.

Start Task is applicable only if you select Start task manually option in the Set Start Time panel.

When you select the task manually, the resume option is unavailable in the monitoring page.

Cancel Task—Cancels the selected task

Paused due to Error:

Retry—This causes the task to restart and retry the last failed task action (the failed step).

Resume—This causes the task to start at the next step (after the failed step).

View Details—Navigates to the monitoring page showing all the tasks available

Cancel Task—Cancels the selected task

Successful status:

View Details—Navigates to the monitoring page showing all the tasks available.

Delete—Deletes the selected task permanently

Failed status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Show

Allows you to filter upgrade tasks by status, by selecting one of the following options from the drop-down list:

Quick Filter—To filter the tasks based on the status

All—To show all the tasks available

Scheduled—To show the tasks that are scheduled

Canceled—To show the tasks that are canceled

Running—To show the tasks that are started

Paused—To show the tasks that are paused

Paused due To Error—To show the tasks that are paused due to an error in the system

Successful—To show the tasks that are successful

Failed—To show the tasks that failed

Filter

Select a status and click Filter to set a search rule at the bottom of the search window.

Delete

Click the checkbox next to the task and click the Delete button at the top of the table. This action is applicable to tasks
                                             in the Failed, Successful, Scheduled and, Paused state.

Add Upgrade Task button

Opens the Add Upgrade Task wizard.

You can also open the Add Upgrade Task wizard selecting Edit in the Actions column for a particular upgrade task.

Add Upgrade Task wizard window

For information about how to Add an Upgrade Task, see "Create an Upgrade Task" .

Choose Cluster page

From the Choose Cluster page, select the cluster and product from the drop-down lists (All products is the default option
                                             for Products). Once you have selected the cluster, the list of nodes appears in the Cluster Nodes table.

Choose Upgrade File page

From the Choose Upgrade File page, select the upgrade file for each product being upgraded. You will have the option of selecting
                                             files only for the product type you selected on the Choose Cluster page.

Set Start Time and Upgrade Options page

From the Set Start Time and Upgrade Options page, select a start time for the task.

You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard.

You also have the option of automatically switching to a new version following a successful upgrade.

Specify Run Sequence page

From the Specify Run Sequence, specify the sequence in which the upgrade will be processed on the servers. You change the
                                             sequence of steps by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit an existing
                                             step.

Select the Use Last Configured Run Sequence box if you want to reuse the previous sequence.

By default, each node is sequenced into its own step.

Review page

The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only—you cannot select them.

You can add notes to the Notes field for future reference.

### Switch Versions
                           	 View

Scheduled Tasks and History table

Status

Provides information about the switch version task:

Successful—Indicates that the task has finished without errors

Running—Indicates that the task is currently running

Scheduled—Indicates that the task has not yet started

Canceled—Indicates that the user has chosen not to run task

Paused—Indicates that the task is in a paused state waiting for feedback

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Failed—Indicates that the task has stopped due to error

Start Time

Specifies the start time of the switch version task

Last Status Report Time

Specifies the time at which the action was completed. The completed action may be a success or failure.

Cluster

Specifies the switch version cluster

Notes

Notes that were added during the Review portion of the Add Switch Version wizard

Actions

The following are the status and the corresponding actions:

Scheduled status:

Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable

Edit—Shows the Edit Switch Version Task window. Allows you to edit the selected task

Cancel Task—Cancels the selected task

Delete—Deletes the selected task permanently

Canceled status:

Delete—Deletes the selected task permanently

Started status:

Cancel Task—Cancels the selected task

Paused status:

Resume—Restarts task at the next step.

View Details—Navigates to the monitoring page showing all the tasks available

Start Task—Start task is present if the task is started manually. Time is not selected for this action

Start Task is applicable only if you select Start task manually option in the Set Start Time panel.

When you select the task manually, the resume option is unavailable in the monitoring page.

Cancel Task—Cancels the selected task

Paused due to Error:

Retry—This causes the task to restart and retry the last failed task action (the failed step)

Resume—This causes the task to start at the next step (after the failed step)

View Details—Navigates to the monitoring page showing all the tasks available

Cancel Task—Cancels the selected task

Successful status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Failed status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Show

Allows you to filter switch version tasks by status, by selecting one of the following options from the drop-down list:

Quick Filter—To filter the tasks based on the status

All—To show all the tasks available

Scheduled—To show the tasks that are scheduled

Canceled—To show the tasks that are canceled

Running—To show the tasks that are started

Paused—To show the tasks that are paused

Paused due To Error—To show the tasks that are paused due to an error in the system

Successful—To show the tasks that are successful

Failed—To show the tasks that failed

Filter

Select a status and click Filter to set a search rule at the bottom of the search window

Delete

Check the check box next to the task and click the Delete button at the top of the table. You can also click Delete under
                                             the Actions column for the task you wish to delete

Add Switch Versions Task button

Opens the Switch Versions Task wizard.

You can also open the Switch Versions Task wizard by selecting Edit in the Actions column for a particular switch version
                                                         task.

Add Switch Versions Task window

For information about how to add a switch version task, see "Create a Switch Versions Task" .

Choose Cluster page

From the Choose Cluster page, select the cluster from the drop-down list. After you select the cluster, you must select the
                                             product versions (installed on the publisher) from the drop-down lists. If there is more than one product in the cluster,
                                             you have the option of not switching versions for one or more products. As long as one valid version is selected, you may
                                             proceed

Set Start Time page

From the Set Start Time page, select a start time for the task.

You have the option of setting the start time for a specific time, starting the task manually, or setting it to begin immediately
                                             upon completion of the wizard.

Set Run Sequence page

From the Specify Run Sequence, specify the sequence in which the version switch is processed on the servers. The sequence
                                             of the steps is changed by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit
                                             an existing step.

Check the Use Last Configured Run Sequence check box if you want to reuse the previous sequence.

By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state.

Review page

The Review page provides a summary of the options you selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them.

You can add notes to the Notes field for future reference.

### Server Restart
                           	 View

Scheduled Tasks and History table

Status

Provides information about the server restart task:

Successful—Indicates that the task is complete without errors

Running—Indicates that the task is currently running

Scheduled—Indicates that the task is not yet started

Canceled—Indicates that the user has chosen not to run task

Paused—Indicates that the task is in a paused state waiting for feedback

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Failed—Indicates that the task has stopped due to error

Start Time

Specifies the start time of the server restart task

Last Status Report Time

Specifies the time at which the action was completed. The completed action may be a success or failure.

Cluster

Specifies the server restart cluster

Notes

Notes that were added during the Review portion of the Add Restart Task wizard

Actions

The following are the status and the corresponding actions:

Scheduled status:

Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable.

Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task

Cancel Task—Cancels the selected task

Delete—Deletes the selected task permanently

Canceled status:

Edit—Shows the Edit Server Restart Task window. Allows you to edit the selected task

Delete—Deletes the selected task permanently

Started status:

Cancel Task—Cancels the selected task

Paused status:

Resume—Restarts task at the next step.

View Details—Navigates to the monitoring page showing all the tasks available

Start Task—Start task is present if the task is started manually. Time is not selected for this action

Start Task is applicable only if you select Start task manually option in the Set Start Time panel.

When you select the task manually, the resume option is unavailable in the monitoring page.

Cancel Task—Cancels the selected task

Paused due to Error:

Retry—This causes the task to restart and retry the last failed task action (the failed step).

Resume—This causes the task to start at the next step (after the failed step).

View Details—Navigates to the monitoring page showing all the tasks available

Cancel Task—Cancels the selected task

Successful status:

View Details—Navigates to the monitoring page showing all the tasks available.

Delete—Deletes the selected task permanently

Failed status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Show

Allows you to filter restart tasks by status, by selecting one of the following options from the drop-down list:

Quick Filter—To filter the tasks based on the status

All—To show all the tasks available

Scheduled—To show the tasks that are scheduled

Canceled—To show the tasks that are canceled

Running—To show the tasks that are started

Paused—To show the tasks that are paused

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Successful—To show the tasks that are successful

Failed—To show the tasks that failed

Filter

Select a status and click Filter to set a search rule at the bottom of the search window.

Delete

Click the checkbox next to the task and click the Delete button at the top of the table. You can also click Delete under the
                                             Actions column for the task you wish to delete.

Add Server Restart Task button

Opens the Add Server Restart Task wizard.

You can also open the Add Server Restart Task wizard by selecting Edit in the Actions column for a particular server restart
                                                         task.

Add Server Restart Task window

For information about how to add a server restart task, see "Create a Restart Task" .

Choose Cluster page

From the Choose Cluster page, select the cluster from the drop-down list. After you select the cluster, you will see that
                                             the nodes listed in the Cluster Nodes table change accordingly. Select the servers to be restarted.

Set Start Time page

From the Set Start Time page, select a start time for the task.

You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard.

Set Run Sequence page

From the Set Run Sequence page, specify the sequence in which the restart is processed on the servers. You can change the
                                             sequence of steps by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit an existing
                                             step.

Check the Use Last Configured Run Sequence check box if you want to reuse the previous sequence.

By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state.

Review page

The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them.

You can add notes to the Notes field for future reference.

### Readdress
                           	 View

Scheduled Tasks and History table

Status

Provides information about the readdress task:

Successful—Indicates that the task has finished without errors

Running—Indicates that the task is currently running

Scheduled—Indicates that the task has not yet started

Canceled—Indicates that the user has chosen not to run task

Paused—Indicates that the task is in a paused state waiting for feedback

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Failed—Indicates that the task has stopped due to error

Start Time

Specifies the start time of the readdress task

Last Status Report Time

Specifies the time at which the action was completed. The completed action may be a success or failure.

Cluster

Specifies the readdress cluster

Notes

Note that were added during the Review portion of the Add Readdress Task wizard

Actions

The following are the status and the corresponding actions:

Scheduled status:

Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable.

Edit—Shows the Edit Readdress Task window. Allows you to edit the selected task

Cancel Task—Cancels the selected task

Delete—Deletes the selected task permanently

Canceled status:

Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task

Delete—Deletes the selected task permanently

Started status:

Cancel Task—Cancels the selected task

Paused status:

Resume—Restarts task at the next step.

View Details—Navigates to the monitoring page showing all the tasks available

Start Task—Start task is present if the task is started manually. Time is not selected for this action

Start Task is applicable only if you select Start task manually option in the Set Start Time panel.

When you select the task manually, the resume option is unavailable in the monitoring page.

Cancel Task—Cancels the selected task

Paused due to Error:

Retry—This causes the task to restart and retry the last failed task action (the failed step or sub-step).

Resume—This causes the task to start at the next step (after the failed step or sub-step).

View Details—Navigates to the monitoring page showing all the tasks available

Cancel Task—Cancels the selected task

Successful status:

View Details—Navigates to the monitoring page showing all the tasks available.

Delete—Deletes the selected task permanently

Failed status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Show

Allows you to filter readdress tasks by status, by selecting one of the following options from the drop-down list:

Quick Filter—To filter the tasks based on the status

All—To show all the tasks available

Scheduled—To show the tasks that are scheduled

Canceled—To show the tasks that are canceled

Running—To show the tasks that are started

Paused—To show the tasks that are paused

Paused due To Error—To show the tasks that are paused due to an error in the system

Successful—To show the tasks that are successful

Failed—To show the tasks that failed

Filter

Select a status and click Filter to set a search rule at the bottom of the search window.

Delete

Check the check box next to the task and click the Delete button at the top of the table. You can also click Delete under
                                             the Actions column for the task you wish to delete.

Add Readdress Task button

Opens the Add Readdress Task wizard.

You can also open the Add Readdress Task wizard by selecting Edit in the Actions column for a particular readress task.

Add Readdress Task window

For information about how to Add a Readdress Task, see "Create a Readdress Task" .

Choose Cluster page

From the Choose Cluster page, select the cluster from the drop-down list. Click View Nodes to the nodes associated with this
                                             cluster. The View UC Cluster Nodes dialog box opens, listing the nodes in a table that identifies the following:

Hostname

IP Address

Product

Role

The View UC Cluster Nodes dialog box is not editable. Click Close to return to the Choose Cluster page.

Enter New Hostnames/IP Addresses page

From the Enter New Hostnames/IP Addresses page, click Edit under the Actions column to open the Edit Hostname/IP Address dialog
                                             box. This dialog box allows you to enter a new hostname or IP address for the cluster nodes to be readdressed. You have the
                                             option of using DHCP or a static IP address.

Set Start Time page

From the Set Start Time page, select a start time for the task.

You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard.

You can use this page to also enable the re-address option. Check the Pause before network verification substeps to allow external changes check box if you wish to introduce a pause between the re-address and the network change verification substeps upon changing
                                             the subnet or gateway. During this pause, you can make the necessary network changes to the virtual machine configuration,
                                             such as VLAN.

After you make the changes, resume the task to complete the verification.

Set Run Sequence page

From the Set Run Sequence page, specify the sequence in which the readdress is processed on the servers. The sequence of the
                                             steps is changed by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit an existing
                                             step.

Check the Use Last Configured Run Sequence check box if you want to reuse the previous sequence.

By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state.

Review page

The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them.

You can add notes to the Notes field for future reference.

### Install
                           	 View

Scheduled Tasks and History table

Status

Provides information about the install task:

Successful—Indicates that the task has finished without errors

Running—Indicates that the task is currently running

Scheduled—Indicates that the task has not yet started

Canceled—Indicates that the user has chosen not to run task

Paused—Indicates that the task is in a paused state waiting for feedback

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Failed—Indicates that the task has stopped due to error

Start Time

Specifies the start time of the install task

Last Status Report Time

Specifies the time at which the action was completed. The completed action may be a success or failure.

Cluster

Specifies the install cluster

Notes

Notes that were added during the Review portion of the Add Install Task wizard

Actions

The following are the status and the corresponding actions:

Scheduled status:

Run Validation Test—Runs a validation test to ensure that all the ESXi host is present, the VMs are in the correct state,
                                                         and the .iso file to be used in the install is present.

Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task

Cancel Task—Cancels the selected task

Delete—Deletes the selected task permanently

Canceled status:

Delete—Deletes the selected task permanently

Started status:

Cancel Task—Cancels the selected task

Paused status:

Resume—Restarts task at the next step.

View Details—Navigates to the monitoring page showing all the tasks available

Start Task—Start task is present if the task is started manually. Time is not selected for this action

Start Task is applicable only if you select Start task manually option in the Set Start Time panel.

When you select the task manually, the resume option is unavailable in the monitoring page.

Cancel Task—Cancels the selected task

Paused due to Error:

Retry—Retry the last failed step. This button causes the task to retry the last step that failed, and restart the task (the
                                                         failed step).

Resume—Resumes the task at the next step (after the failed step). Use this option only if the failed step is non-essential,
                                                         or if you have manually performed that step

View Details—Navigates to the monitoring page showing all the tasks available

Cancel Task—Cancels the selected task

Successful status:

View Details—Navigates to the monitoring page showing all the tasks available.

Delete—Deletes the selected task permanently

Failed status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Show

Allows you to filter install tasks by status, by selecting one of the following options from the drop-down list:

Quick Filter—To filter the tasks based on the status

All—To show all the tasks available

Scheduled—To show the tasks that are scheduled

Canceled—To show the tasks that are canceled

Running—To show the tasks that are started

Paused—To show the tasks that are paused

Paused due To Error—To show the tasks that are paused due to an error in the system

Successful—To show the tasks that are successful

Failed—To show the tasks that failed

Filter

Select a status and click Filter to set a search rule at the bottom of the search window.

Delete

Click the checkbox next to the task and click the Delete button at the top of the table. You can also click Delete under the
                                             Actions column for the task you wish to delete.

Add Install Task button

Opens the Add Installation Task wizard.

You can also open the Add Installation Task wizard by selecting Edit in the Actions column for a particular install task.

Add Installation Task window

For information about how to add an installation task, see "Create an Install Task" .

Choose Installation Cluster page

From the Choose Cluster page, select the cluster from the drop-down list. After you select the cluster, you will see that
                                             the nodes listed in the Installation Cluster Nodes table change accordingly.

Choose Installation Files page

From the Choose Installation Files page, select the installation images to be installed on the staging cluster. The ISO images
                                             must be uploaded to the /install directory on the system sftp server for Cisco Prime Collaboration Deployment.

Set Start Time page

From the Set Start Time page, select a start time for the task.

You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard.

Specify Installation Sequence page

From the Specify Installation Sequence page, specify the sequence in which the installation is processed on the servers. You
                                             can change the sequence of steps by clicking the up and down arrows of a particular step. You can also add or delete a step,
                                             or edit an existing step.

By default, each node is sequenced into its own step.

Review page

The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them.

You can add notes to the Notes field for future reference.

### Migrate
                           	 View

Scheduled Tasks and History table

Status

Provides information about the migrate task:

Successful—Indicates that the task has finished without errors

Running—Indicates that the task is currently running

Scheduled—Indicates that the task has not yet started

Canceled—Indicates that the user has chosen not to run task

Paused—Indicates that the task is in a paused state waiting for feedback

Paused due To Error—Indicates that the task is in a paused state due to an error in the system

Failed—Indicates that the task has stopped due to error

Start Time

Specifies the start time of the migrate task

Last Status Report Time

Specifies the time at which the action was completed. The completed action may be a success or failure.

Cluster

Specifies the cluster being migrated.

Notes

Notes that were added during the Review portion of the Add Migration Task wizard

Actions

The following are the status and the corresponding actions:

Scheduled status:

Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable. It also checks that the ESXi hosts that the VMs reside on are mounted. It also verifies that the iso file to
                                                         be used is present.

Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task

Cancel Task—Cancels the selected task

Delete—Deletes the selected task permanently

Canceled status:

Delete—Deletes the selected task permanently

Started status:

Cancel Task—Cancels the selected task

Paused status:

Resume—Restarts task at the next step.

View Details—Navigates to the monitoring page showing all the tasks available

Start Task—Start task is present if the task is started manually. Time is not selected for this action

Start Task is applicable only if you select Start task manually option in the Set Start Time panel.

When you select the task manually, the resume option is unavailable in the monitoring page.

Cancel Task—Cancels the selected task

Paused due to Error:

Retry—Retry the last failed step (the failed step or sub-step). This button causes the task to retry the last step that failed,
                                                         and restart the task.

Resume—Resumes the task at the next step (after the failed step or sub-step). Use this option only if the failed step is non-essential,
                                                         or if you have manually performed that step.

View Details—Navigates to the monitoring page showing all the tasks available

Cancel Task—Cancels the selected task

Successful status:

View Details—Navigates to the monitoring page showing all the tasks available.

Delete—Deletes the selected task permanently

Failed status:

View Details—Navigates to the monitoring page showing all the tasks available

Delete—Deletes the selected task permanently

Show

Allows you to filter migration tasks by status, by selecting one of the following options from the drop-down list:

Quick Filter—To filter the tasks based on the status

All—To show all the tasks available

Scheduled—To show the tasks that are scheduled

Canceled—To show the tasks that are canceled

Running—To show the tasks that are started

Paused—To show the tasks that are paused

Paused due To Error—To show the tasks that are paused due to an error in the system

Successful—To show the tasks that are successful

Failed—To show the tasks that failed

Filter

Select a status and click Filter to set a search rule at the bottom of the search window.

Delete

Check the check box next to the task and click the Delete button at the top of the table. You can also click Delete under
                                             the Actions column for the task you wish to delete.

Add Migration Task button

Opens the Add Migration Task wizard.

You can also open the Add Migration Task wizard by selecting Edit in the Actions column for a particular migrate task.

Add Migration Task window

For information about how to add a migration task, see "Add Migration Task" .

Choose Source and Destination Clusters page

From the Choose Source and Destination Clusters page, select the source UC cluster from the drop-down list. After you select
                                             the source cluster, you select the destination cluster from the drop-down list and the nodes from the Node Mapping from Source
                                             to Destination Cluster table.

Choose Upgrade Files page

From the Choose Upgrade File page, select the upgrade file for each product being upgraded. You will only have the option
                                             of selecting files for the product type you selected on the Choose Cluster page.

Set Start Time page

From the Set Start Time page, select a start time for the task.

You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard.

Specify Migration Procedure page

From the Specify Migration Procedure page, specify the sequence in which the migration is processed on the servers. You can
                                             change the sequence of the stepsby clicking the up and down arrows of a particular step. You can also add or delete a step,
                                             or edit an existing step.

By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state.

Review page

The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them.

You can add notes to the Notes field for future reference.

## Inventory View Elements

### Clusters

Clusters table

Cluster
                                             						Name

Shows
                                             						the available clusters

Product
                                             						and Version

Shows
                                             						the product for which the cluster is added along with its version

Nodes

Shows
                                             						the number of nodes associated with the cluster

Cluster
                                             						Type

Shows
                                             						the cluster type, such as Discovered, New install, or Migration

Discovery Status

Contacting

Discovering

Successful

Node Unreachable

Timeout

Internal Error

Actions

Edit —Edit an added new node that has not yet been
                                                      							 installed

Delete —Delete an added new node that has not yet
                                                      							 been installed

Show

All—To show all the available clusters

Discovered—To show the clusters that are scheduled

New Install—To show the cluster that newly installed

Migration—To show the clusters that are migrated

Filter

Select a status and click Filter to set a search rule at the bottom of the
                                             						search window.

Discover
                                             						Cluster button

Click
                                             						this button so that Cisco Prime Collaboration Deployment communicates with the
                                             						servers that are already running Unified Communications applications and adds
                                             						that cluster information into the Cisco Prime Collaboration Deployment
                                             						inventory

Define Migration
                                                						  Destination Cluster

For information on how to create a migration cluster, see the Create a Migration Cluster .

Specify Clusters page

Source Cluster —From the drop-down list, select a
                                                      							 source UC cluster.

View Nodes —Click this link to view the available
                                                      							 cluster nodes.

Active Versions —Shows the active versions of the
                                                      							 source UC cluster.

Destination Cluster Nickname —Enter a nickname for
                                                      							 the destination cluster.

Use the source node network settings for all destination
                                                                  									 nodes —Choose this option to retain the default network options.

Enter new network settings for one or more destination
                                                                  									 nodes —Choose this option to modify the default network settings or
                                                               								  enter new network options.

If you select the Use the source node network settings for all destination
                                                                              										nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns on the Assign Destination Cluster Nodes window. If you
                                                                           									 select the Enter new network settings for one or more destination
                                                                              										nodes option, only source hostname appears and not the destination
                                                                           									 hostname on the Assign Destination Cluster Nodes window.

Assign
                                             						Destination Cluster Nodes page

Source Cluster —Displays the name of the source
                                                   							 cluster.

Destination Cluster —Displays the name of the
                                                   							 destination cluster.

Assign Destination Cluster Nodes —Click this button
                                                   							 to associate destination virtual machines with nodes in the source cluster.

If DHCP is in use on your source node, the destination node is
                                                               								also configured to use DHCP, and you will have no option to change your network
                                                               								settings in this wizard.

Configure NTP/SMTP Settings

Enter
                                             						details for the following sections to configure NTP and SMTP to the migration
                                             						nodes when the migration task is run:

NTP Server 1

NTP Server 2

NTP Server 3

NTP Server 4

NTP Server 5

SMTP Server —Enter IP address of the SMTP server.

Define
                                             						DNS Settings

(Optional) From the available hosts added along with the
                                             						functions, check a node to configure DNS setting for the migration cluster
                                             						nodes and click Assign DNS Settings

Discover Cluster window

For
                                             						information on how to Discover a Cluster, see Discover a Cluster .

Cluster
                                             						Access page

Choose a Nickname for this Cluster —Enter a nick name
                                                      							 for the cluster.

Hostname/IP Address of Cluster Publisher —Enter
                                                      							 either the host name or the IP address for the publisher node of the cluster.

OS Admin Username —Enter the OS administrator user
                                                      							 name.

OS Admin Password —Enter the password for the OS
                                                      							 administrator.

Ensure that cluster password is less than 16 characters.

Enable NAT —Check this check box to enable NAT for
                                                      							 the cluster.

When you check the Enable NAT check box, the NAT IP column appears on the Cluster Discovery
                                                                  								Progress page.

Cluster
                                             						Discovery Progress page

Cluster Name —Shows the cluster name along with the
                                                      							 status message of the cluster discovery.

Hostname —Shows the host name.

Contacting

Discovering

Successful

Node Unreachable

Timeout

Internal Error

Product —Shows the product of the cluster.

Active version —Shows the version currently in use.

Inactive version —Shows the version that is currently
                                                      							 not in use.

NAT IP —This column appears only if you check the Enable NAT check box on the Cluster Access page.

Hardware —Shows the hardware associated to the
                                                      							 cluster.

Cluster
                                             						Role Assignment page

Hostname —Shows the host name.

Product —Shows the product of the cluster.

Functions —Shows the different roles that are assigned to a particular node. For example Publisher,Primary TFTP, Secondary TFTP.

SFTP Server —Shows the location of the ISO files.

By default the SFTP server is PCD.

Edit Settings —Allows to assign more  roles or functionality to the node.

Define New UC Cluster
                                                						  window

For information on how to install a new cluster, see the Add New Cluster for Fresh Install .

After
                                             						you click this button, a wizard appears that guides you to the installation
                                             						process of a new UC cluster.

Specify Cluster Name window

Choose the Nickname for this cluster —Enter the
                                             						cluster name

Add
                                             						Virtual Machines window

Add Node —Check one or more functions for adding a
                                                      							 node from the available check boxes.

Notes —(Optional) Add a nodes for the selected
                                                      							 cluster.

The available VMs are sorted by name and by host. The details of
                                                                     								  virtual machines, such as VM Name, ESXi Host, and Power State, appear in this
                                                                     								  window.

Show —Allows you to filter virtual machine by status,
                                                      							 by selecting options from the drop-down list.

Static IP address —Enter the details for hostname, IP
                                                               								  Address, Subnet Mask, Gateway, and NAT IP fields.

Use DHCP with Reservations —Enter the IP address that
                                                               								  you have a reservation for on your DHCP server (associated with the MAC address
                                                               								  for that VM) in addition to the hostname.

Products and Functions —From the drop-down list,
                                                      							 select a product. In the Functions section, check the appropriate function
                                                      							 check boxes for your VM.

Check the Publisher check box for at least one node in the
                                                                        									 cluster that you have defined for each application type.

(Optional) Add a note about the functions that you have assigned
                                                                        									 in the Notes field below the Publisher field.

Virtual Machines section—Choose a VM for the selected node.

Configure Cluster Wide Settings window

Enter
                                             						details for the fields of the following sections:

Username —Enter user name of the OS administrator.

Password —Enter password of the user name.

Confirm Password —Re-enter the same password that you
                                                      							 entered in the Password field.

Username —Enter user name of the application user.

Password —Enter password of the user name.

Confirm Password —Re-enter the same password that you
                                                      							 entered in the Password field.

Password —Enter the security password for the
                                                      							 cluster.

Confirm Password —Re-enter the same password that you
                                                      							 entered in the Password field.

SMTP Server —Enter the IP address of the SMTP server.

Organization —Enter the name of the organization of
                                                      							 which the certificate is being used.

Unit —Enter the number of certificates being used.

Location —Enter the location where the certificate is
                                                      							 being used.

State —Enter the state where the certificate is being
                                                      							 used.

Country —From the drop-down list, select the country
                                                      							 where the certificate is being used.

Configure DNS Settings window

(Optional) From the available hosts added along with the
                                             						functions, check a node to configure DNS setting for a node and click Assign DNS Settings .

Configure NTP Settings

NTP Server 1

NTP Server 2

NTP Server 3

NTP Server 4

NTP Server 5

It
                                                            						  is recommended that you define at least IP addresses of two NTP servers

Configure NIC Settings

Hostname, Functions, and MTU size column—From the available
                                                      							 servers, check the check box for a server.

MTU Size —Enter an MTU size between 552 and 1500 and
                                                      							 click Apply to Selected .

Apply to Selected —Click this button to apply the MTU
                                                      							 size for the selected host.

Apply Default MTU —Click this button to apply the
                                                      							 default value of MTU size for the selected host.

Configure Time Zones window

Region —From the drop-down list, select the region
                                                      							 for the cluster node.

Time Zone —From the drop-down list, select the time
                                                      							 zone of the selected region.

Apply to Selected —Click this button to apply the
                                                      							 time zone changes for each cluster node.

### ESXi Hosts
                           	 View

ESXi Hosts table

Hostname

Shows
                                             						the ESXi host name.

IP
                                             						Address

Shows
                                             						the IP address of the ESXi host.

Description

Shows
                                             						the description, if any, of the ESXi host.

Actions

Edit —Click this link to edit the ESXi host details.

Delete —Click this link to delete the ESXi host from
                                                      							 the database.

Add ESXi
                                             						Host

Click
                                             						this button to add an ESXi host in the database.

Add ESXi Host window

Hostname/IP Address

Enter
                                             						the host name of the IP address of the ESXi host.

Username

Enter
                                             						the user name.

Password

Enter
                                             						the password for the user.

Description

(Optional) Enter the description for the ESXi host.

### SFTP Servers and
                           	 Datastore

Setting

Description

SFTP Servers/Datastore section

The
                                             						Cisco Prime Collaboration Deployment server serves as a local SSH File Transfer
                                             						Protocol or Secure File Transfer Protocol (SFTP) server that stores the ISO and
                                             						COP files to be used by upgrade, fresh, install, and migrate tasks.

For more
                                             						information on SFTP Datastore, see SFTP Servers and Datastore .

Delete

Click
                                             						this button to delete the selected SFTP server from the datastore.

Add
                                             						Server

Click
                                             						this button to add the selected SFTP server to the datastore.

Server
                                             						IP

Shows
                                             						the IP addresses of the available SFTP servers in the datastore.

Server
                                             						Description

Shows
                                             						the description added for the available SFTP servers.

Database
                                             						Directory

Shows
                                             						the directory path of the SFTP servers.

Status

Shows
                                             						the status of the SFTP server. For example, Connected and Local.

Actions

Edit —Click this link to edit the SFTP server
                                                      							 details.

Delete —Click this link to delete the selected SFTP
                                                      							 server from the datastore.

SFTP/Datastore Files section

Delete

Click
                                             						this button to delete the ISO and COP files of the selected SFTP server from
                                             						the datastore.

Filename

Shows
                                             						the available ISO and COP files of the SFTP servers.

Server
                                             						IP

Shows
                                             						the IP address of the SFTP servers.

Server
                                             						Description

Shows
                                             						the description added for the available SFTP servers.

Directory

Shows
                                             						the directory name where the SFTP files of the SFTP servers are stored.

File
                                             						Type

Shows
                                             						the type of file, such as upgrade file and fresh install.

Copied
                                             						On (local)

Shows
                                             						the data, time, and time zone when the SFTP file is copied to the datastore.

## Administration View Elements

### Email Notification
                           	 View

Notification Settings section

For more information, see the Email Notification .

Notifications

Do not send email notification —Choose this option if
                                                      							 you do not wish to receive any email notification for errors or types of tasks.

If
                                                                  								you choose this option, all the fields of this section become non-editable.

Failed to Schedule

Failed

Failed to cancel

Paused on error

Scheduled

Failed to Schedule

Started

Successful

Failed

Canceled

Canceling

Failed to Cancel

Paused on Error

Paused

Paused – Required

Email
                                             						Recipients

Separate multiple email addresses with a comma.

Use TLS

Check
                                             						this check box so that Transport Layer Security (TLS) protocol ensures privacy
                                             						or prevent tampering with the email between the application and the email
                                             						recipients.

Mail server credentials section

Username

Enter
                                             						the user name of the mail server.

Password

Enter
                                             						the password to log in to the mail server.

Server Settings section

SMTP
                                             						Server

Enter
                                             						the IP address of the SMTP server.

Port

Enter
                                             						the number of ports for the SMTP server.

Save

Click
                                             						this button to save the changes you have made in this page.

Reset

Click
                                             						this button to set the default values on this page.

Send
                                             						Test Email

Click
                                             						this button to send a test email to one or more recipients for the errors only
                                             						and standard options.

### NAT
                           	 Settings

Setting

Description

PCD NAT
                                                						  Settings

For more information on network address translation, see the Network Address Translation Support .

Hostname

Shows
                                             						the host name of the server.

Private
                                             						IP

Shows
                                             						the IP address of the server that is in the private network.

NAT IP

Enter
                                             						the NAT IP address.

Save

The NAT
                                             						IP address is saved as an entry in a configuration file on Cisco Prime
                                             						Collaboration Deployment. This entry is used when the application nodes try to
                                             						contact Cisco Prime Collaboration Deployment.

Reset

(Optional) The NAT IP address is reset to the earlier saved NAT
                                             						IP address.

### Disk Space Warning
                           	 Level

Setting

Description

Disk Space Warning Level
                                                						  Configuration

For details, see Disk Space Warning Level .

Total
                                             						Disk Space (GB)

Shows
                                             						the total disk space on the server.

Available Disk Space (GB)

Shows
                                             						the available disk space for use on the server.

Warning
                                             						Level Disk Space (GB)

Enter
                                             						the disk space warning value. After entering this value, click the information
                                             						link to check if the space value you entered is available for use on the
                                             						server.

Save

Save the
                                             						warning disk space value.

Reset

(Optional) Resets the page with the default values.

### Max Nodes Configuration

Setting

Description

Max Nodes

Enter the maximim nodes on the server.

Save

Save the maximum nodes value.

Reset

(Optional) Resets the page with the default values.

### Audit Log
                           	 Configuration

Setting

Description

Audit Level Settings section

Application Audit Event Level

From the drop-down list, choose one of the following options:

Info —To view the audit event level as an information message.

Warning —To view the audit event level as a warning message.

Debug —To view the audit event level as a debug message.

Error —To view the audit event level as an error message.

Remote SysLog Settings section

Remote Syslog Server Name / IP

Enter the name of remote syslog server or the IP address for
                                             						the audit logs to be logged in to this remote server.

Local Audit Log Settings

Enable Local Audit Log

Check or uncheck this check box to enable or disable the
                                             						local audit log.

When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                               not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                               , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID.

When you check this field, the Enable Log Rotation field
                                                               								becomes active.

Enable Log Rotation

Check or uncheck this check box to enable or disable the log
                                             						rotation.

You can configure this field if the Enable Local Audit Log field is
                                                               								enabled.

After you enable this field, you can configure the Maximum No of Files , Maximum File Size(MB) , and Warning Threshold for Approaching Log
                                                                  								  Rotation Overwrite(%) fields. When you uncheck the Enable Local Audit Log field,
                                                               								the default values of these fields are not applicable as they are not active.

Maximum No of Files

Enter an integer value for the Maximum No of Files field to configure
                                             						the maximum number of files that can be created on the server.

After you check the Enable Log Rotation field, you can configure the value for Maximum No of Files field. Once the number of files reaches the configured value, the log rotation process starts. In the log rotation process,
                                             all the log files are deleted and rewritten from the log file number 1.

The value for this field must be in the range of 1 to 5000.

Maximum File Size(MB)

Enter a value for the Maximum File Size (MB) field to
                                             						configure the maximum file size of each log that is created on the server.

The value for this field must be in the range of 1 to 10.

Warning Threshold for Approaching Log Rotation Overwrite(%)

Enter the warning threshold value for the Warning Threshold for Approaching Log Rotation
                                                						  Overwrite(%) field.

After the configured warning threshold value is reached, an
                                             						email notification is sent to users to take back up of the audit log files.
                                             						These files are deleted or overwritten during log rotation.

The value for this field must be in the range of 1 to 100.

For details, see the Email notification topic in the Cisco Prime Collaboration Deployment Administration
                                                						  Guide .

Save

Click this button to save the changes you have made on this
                                             						page.

Reset

Click this button to set the default values on this page.

### Customized Logon
                           	 Message Configuration

Setting

Description

Upload Customized Logon File

Upload File

Click the Browse button to browse to the
                                             						location of file that includes the customized sign-on message.

Require User Acknowledgment

Check or uncheck this check box to enable or disable user
                                             						acknowledgment for the file that the user receives.

If this field is enabled, users get an acknowledgment as an
                                             						alert message on the Cisco Prime Collaboration Deployment sign-in page. This
                                             						message appears after they sign out for the first time from the same web
                                             						browser instance.

Upload File

Click this button to upload the file with the customized
                                             						sign-on message to the server. After you upload the file, a popup appears
                                             						showing the file upload status.

Delete

Click this button to delete the file with the customized
                                             						sign-on message. After you delete the file, popup appears showing the file
                                             						deletion status.

### Supported Release Matrix

This release of Cisco Prime Collaboration Deployment includes the Supported Releases Matrix window in the Administration menu. Use this matrix to view the supported and unsupported releases of the product, task type, and Cisco Prime Collaboration
                                 Deployment release that you choose.

Setting

Description

PCD Releases

From the drop-down list, choose one of the releases of Cisco Prime Collaboration Deployment. The available options are Release
                                             12.6(1) up to the latest release.

Task Type

From the drop-down list, choose one of the following tasks to view the supported releases for a specific task:

All

Migration

Install

Upgrade

Switch Version

Server Restart

Readdress

Product Type

From the drop-down list, choose one of the following products:

CUCM—Implies Cisco Unified Communications Manager.

IM&P—Implies Instant Messaging and Presence services

CUC—Implies Cisco Unity Connection

UCCX—Implies Cisco Unified Contact Center Express

CER—Implies Cisco Emergency Responder

Based on the values you choose for the Supported Release Matrix table, the values in Supported Releases Table appear for the CUCM Task Type column. This table shows the supported and unsupported releases of the product and the task type you choose.

| Setting | Description |
|---|---|
| Open and
                                          						close navigation button | Provides
                                          						you access to navigate to menus, which appear in a vertical pane. Click this
                                          						button view and hide the menus. Note When you sign in to the application for the first time, a
                                                      						  transparent grey screen appears indicating this button. This screen also shows
                                                      						  a pop-up message to turn off the indication. | Note | When you sign in to the application for the first time, a
                                                      						  transparent grey screen appears indicating this button. This screen also shows
                                                      						  a pop-up message to turn off the indication. |
| Note | When you sign in to the application for the first time, a
                                                      						  transparent grey screen appears indicating this button. This screen also shows
                                                      						  a pop-up message to turn off the indication. |
| Search
                                          						and Indexing | Displays
                                          						the search text box to allow search in the application. It also displays the
                                          						options Cisco Prime Collaboration Deployment as index. Note To
                                                      						  view the search option, click the open and close navigation button. | Note | To
                                                      						  view the search option, click the open and close navigation button. |
| Note | To
                                                      						  view the search option, click the open and close navigation button. |
| About | Provides the version of the Cisco Prime Collaboration Deployment. This setting
                                          						also includes copyright and trademark information. |
| Logout | Exits
                                          						from the server. |
| Help | Provides context-sensitive help information. |
| Information ("i" button) | Provides information about the current page that you are viewing. |
| Getting
                                          						Started (flag button) | Provides information about getting started to perform system-level tasks on the
                                          						server. |

| Note | When you sign in to the application for the first time, a
                                                      						  transparent grey screen appears indicating this button. This screen also shows
                                                      						  a pop-up message to turn off the indication. |
|---|---|

| Note | To
                                                      						  view the search option, click the open and close navigation button. |
|---|---|

| Setting | Description |
|---|---|
| Task
                                          						Queue | A list
                                          						of all the tasks contained in Cisco Prime Collaboration Deployment. This list can include any of the following tasks: Scheduled Canceled Started Paused Paused due to Error Successful Failed Upgrade Tasks Switch Version Tasks Server Restart Tasks Readdress Tasks Install Tasks Migrate Tasks Click one of the tasks in the Task Queue to open the details for that task in the
                                          						right top panel. |
| Task
                                          						status | The top
                                          						right portion of the Monitoring page shows the following information for a given task: Status Start time Task
                                                							 data (for example: cluster data) To see
                                          						details about the task, click on the View Log link. The
                                          						following are the possible statuses for tasks: Successful—Indicates that the task has finished without errors. Started—Indicates that the task is currently running. Scheduled—Indicates that the task has been scheduled, but has
                                                							 not yet started. Manual Start—Indicates that the task is waiting to be started (user created the
                                                							 task with the "Start Task Manually" option). Canceled—Indicates that the user chose not to run the task. Paused—Indicates that the task is in a paused state waiting
                                                							 for feedback. Paused due To Error—Indicates that the task is in a paused
                                                							 state due to an error in the system. Failed—Indicates that the task has stopped because of an error. Failed to Schedule—Indicates that the task was not
                                                							 scheduled, due to an error that occurred. Failed to Cancel—Indicates that the user tried unsuccessfully to cancel the task. This typically happens when the task is
                                                in
                                                							 a final state (no actions are left to cancel). Canceling—Indicates that the user canceled the
                                                							 task, but the task is in a state that will take a long time to cancel. The task
                                                							 may be in this state for an hour or more if the task being canceled is an
                                                							 installation or migration task (during the install-new-server phase). Possible messages and actions in a Successful Status state: Task
                                                							 completed successfully Delete—Deletes the task data permanently Possible
                                          						actions in a Started state: Cancel—Cancels the selected task Delete—Deletes the selected task permanently Possible actions in a Scheduled state: Cancel—Cancels the selected task Delete—Deletes the selected task permanently Possible
                                          						actions in a Waiting for
                                             						  Manual Start state: Start—Starts the task (You will see this button only if the
                                                							 Manual Start option was chosen when the task was created) Delete—Deletes the selected task permanently Possible
                                          						actions in a Paused state (a task enters this state if  the user
                                          						set up the task to pause at this step): Resume—Task will continue at the next step Cancel—Cancels the selected task Delete—Deletes the selected task permanently Possible
                                          						actions in a Paused
                                             						  Due To Errors state (a task will enter this state, because the system
                                          						detected an error at this step): Resume—Task will continue at the next step. (Before resuming, user should look at the error in the view log and correct the
                                                problem that caused the error, or else the task will fail.) If the error message says "Failed due to validation," the task will revalidate and start from the first step when you click Resume. Otherwise, the task will start from the next
                                                step or sub-step. Retry—Retry the last failed task action (the failed next step or sub-step) Cancel—Cancels the selected task Delete—Deletes the selected task permanently Possible
                                          						action in a Failed
                                             						  Status state: Delete—Deletes the selected task permanently |
| Start
                                          						Task button | Starts
                                          						task running for Scheduled tasks |
| Edit
                                          						button | Opens
                                          						Edit dialog for Scheduled tasks |
| Pause
                                          						button | Pauses
                                          						Running tasks (at next step) |
| Resume
                                          						button | Resumes
                                          						task at next step for Paused and Paused (Error) tasks |
| Retry Button | Retries the last failed task action for Paused (Error) tasks |
| Cancel
                                          						button | Cancels
                                          						Scheduled, Running, Paused, and Paused (Error) tasks |
| Delete
                                          						button | Deletes
                                          						Scheduled, Canceled, Successful, and Failed tasks |
| Task
                                          						Summary | The Task
                                          						Summary section contains the following information for a task: Source Cluster Destination Cluster Unified Communications Manager Upgrade File Unified Presence Upgrade File |

| Setting | Description |
|---|---|
| Scheduled Tasks and History table |
| Status | Provides information about the upgrade task: Successful—Indicates that the task has finished without errors Running—Indicates that the task is currently running Scheduled—Indicates that the task has not yet started Canceled—Indicates that the user has chosen not to run task Paused—Indicates that the task is in a paused state waiting for feedback Paused due To Error—Indicates that the task is in a paused state due to an error in the system Failed—Indicates that the task has stopped due to error |
| Start Time | Specifies the start time of the upgrade task |
| Last Status Report Time | Specifies the time at which the action was completed. The completed action may be a success or failure. |
| Cluster | Specifies the name of the upgraded cluster |
| Notes | Note added during the Review portion of the Add Upgrade Task wizard |
| Actions | Allows you to perform the following for a particular upgrade task Note Depending on the state of the task, only some of these actions may be allowed (for example, an upgrade task that is completed
                                                         cannot be canceled). Scheduled status: Run Validation Test—Runs a validation test to ensure that all nodes are available and the iso to be used for upgrade is present. Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task Cancel Task—Cancels the selected task Delete—Deletes the selected task permanently Canceled status: Delete—Deletes the selected task permanently Started status: Cancel Task—Cancels the selected task Paused status: Resume—Use this button to restart task at the next step. View Details—Navigates to the monitoring page showing all the tasks available Start Task—Start task is present if the task is started manually. Time is not selected for this action. Note Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. Cancel Task—Cancels the selected task Paused due to Error: Retry—This causes the task to restart and retry the last failed task action (the failed step). Resume—This causes the task to start at the next step (after the failed step). View Details—Navigates to the monitoring page showing all the tasks available Cancel Task—Cancels the selected task Successful status: View Details—Navigates to the monitoring page showing all the tasks available. Delete—Deletes the selected task permanently Failed status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently | Note | Depending on the state of the task, only some of these actions may be allowed (for example, an upgrade task that is completed
                                                         cannot be canceled). | Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Note | Depending on the state of the task, only some of these actions may be allowed (for example, an upgrade task that is completed
                                                         cannot be canceled). |
| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Show | Allows you to filter upgrade tasks by status, by selecting one of the following options from the drop-down list: Quick Filter—To filter the tasks based on the status All—To show all the tasks available Scheduled—To show the tasks that are scheduled Canceled—To show the tasks that are canceled Running—To show the tasks that are started Paused—To show the tasks that are paused Paused due To Error—To show the tasks that are paused due to an error in the system Successful—To show the tasks that are successful Failed—To show the tasks that failed |
| Filter | Select a status and click Filter to set a search rule at the bottom of the search window. |
| Delete | Click the checkbox next to the task and click the Delete button at the top of the table. This action is applicable to tasks
                                             in the Failed, Successful, Scheduled and, Paused state. |
| Add Upgrade Task button | Opens the Add Upgrade Task wizard. Note You can also open the Add Upgrade Task wizard selecting Edit in the Actions column for a particular upgrade task. | Note | You can also open the Add Upgrade Task wizard selecting Edit in the Actions column for a particular upgrade task. |
| Note | You can also open the Add Upgrade Task wizard selecting Edit in the Actions column for a particular upgrade task. |
| Add Upgrade Task wizard window For information about how to Add an Upgrade Task, see "Create an Upgrade Task" . |
| Choose Cluster page | From the Choose Cluster page, select the cluster and product from the drop-down lists (All products is the default option
                                             for Products). Once you have selected the cluster, the list of nodes appears in the Cluster Nodes table. |
| Choose Upgrade File page | From the Choose Upgrade File page, select the upgrade file for each product being upgraded. You will have the option of selecting
                                             files only for the product type you selected on the Choose Cluster page. |
| Set Start Time and Upgrade Options page | From the Set Start Time and Upgrade Options page, select a start time for the task. Note The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard. You also have the option of automatically switching to a new version following a successful upgrade. | Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Specify Run Sequence page | From the Specify Run Sequence, specify the sequence in which the upgrade will be processed on the servers. You change the
                                             sequence of steps by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit an existing
                                             step. Select the Use Last Configured Run Sequence box if you want to reuse the previous sequence. By default, each node is sequenced into its own step. |
| Review page | The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only—you cannot select them. You can add notes to the Notes field for future reference. |

| Note | Depending on the state of the task, only some of these actions may be allowed (for example, an upgrade task that is completed
                                                         cannot be canceled). |
|---|---|

| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
|---|---|

| Note | You can also open the Add Upgrade Task wizard selecting Edit in the Actions column for a particular upgrade task. |
|---|---|

| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
|---|---|

| Setting | Description |
|---|---|
| Scheduled Tasks and History table |
| Status | Provides information about the switch version task: Successful—Indicates that the task has finished without errors Running—Indicates that the task is currently running Scheduled—Indicates that the task has not yet started Canceled—Indicates that the user has chosen not to run task Paused—Indicates that the task is in a paused state waiting for feedback Paused due To Error—Indicates that the task is in a paused state due to an error in the system Failed—Indicates that the task has stopped due to error |
| Start Time | Specifies the start time of the switch version task |
| Last Status Report Time | Specifies the time at which the action was completed. The completed action may be a success or failure. |
| Cluster | Specifies the switch version cluster |
| Notes | Notes that were added during the Review portion of the Add Switch Version wizard |
| Actions | The following are the status and the corresponding actions: Scheduled status: Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable Edit—Shows the Edit Switch Version Task window. Allows you to edit the selected task Cancel Task—Cancels the selected task Delete—Deletes the selected task permanently Canceled status: Delete—Deletes the selected task permanently Started status: Cancel Task—Cancels the selected task Paused status: Resume—Restarts task at the next step. View Details—Navigates to the monitoring page showing all the tasks available Start Task—Start task is present if the task is started manually. Time is not selected for this action Note Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. Cancel Task—Cancels the selected task Paused due to Error: Retry—This causes the task to restart and retry the last failed task action (the failed step) Resume—This causes the task to start at the next step (after the failed step) View Details—Navigates to the monitoring page showing all the tasks available Cancel Task—Cancels the selected task Successful status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently Failed status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently | Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Show | Allows you to filter switch version tasks by status, by selecting one of the following options from the drop-down list: Quick Filter—To filter the tasks based on the status All—To show all the tasks available Scheduled—To show the tasks that are scheduled Canceled—To show the tasks that are canceled Running—To show the tasks that are started Paused—To show the tasks that are paused Paused due To Error—To show the tasks that are paused due to an error in the system Successful—To show the tasks that are successful Failed—To show the tasks that failed |
| Filter | Select a status and click Filter to set a search rule at the bottom of the search window |
| Delete | Check the check box next to the task and click the Delete button at the top of the table. You can also click Delete under
                                             the Actions column for the task you wish to delete |
| Add Switch Versions Task button | Opens the Switch Versions Task wizard. Note You can also open the Switch Versions Task wizard by selecting Edit in the Actions column for a particular switch version
                                                         task. | Note | You can also open the Switch Versions Task wizard by selecting Edit in the Actions column for a particular switch version
                                                         task. |
| Note | You can also open the Switch Versions Task wizard by selecting Edit in the Actions column for a particular switch version
                                                         task. |
| Add Switch Versions Task window For information about how to add a switch version task, see "Create a Switch Versions Task" . |
| Choose Cluster page | From the Choose Cluster page, select the cluster from the drop-down list. After you select the cluster, you must select the
                                             product versions (installed on the publisher) from the drop-down lists. If there is more than one product in the cluster,
                                             you have the option of not switching versions for one or more products. As long as one valid version is selected, you may
                                             proceed |
| Set Start Time page | From the Set Start Time page, select a start time for the task. Note The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. You have the option of setting the start time for a specific time, starting the task manually, or setting it to begin immediately
                                             upon completion of the wizard. | Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Set Run Sequence page | From the Specify Run Sequence, specify the sequence in which the version switch is processed on the servers. The sequence
                                             of the steps is changed by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit
                                             an existing step. Check the Use Last Configured Run Sequence check box if you want to reuse the previous sequence. By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state. |
| Review page | The Review page provides a summary of the options you selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them. You can add notes to the Notes field for future reference. |

| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
|---|---|

| Note | You can also open the Switch Versions Task wizard by selecting Edit in the Actions column for a particular switch version
                                                         task. |
|---|---|

| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
|---|---|

| Setting | Description |
|---|---|
| Scheduled Tasks and History table |
| Status | Provides information about the server restart task: Successful—Indicates that the task is complete without errors Running—Indicates that the task is currently running Scheduled—Indicates that the task is not yet started Canceled—Indicates that the user has chosen not to run task Paused—Indicates that the task is in a paused state waiting for feedback Paused due To Error—Indicates that the task is in a paused state due to an error in the system Failed—Indicates that the task has stopped due to error |
| Start Time | Specifies the start time of the server restart task |
| Last Status Report Time | Specifies the time at which the action was completed. The completed action may be a success or failure. |
| Cluster | Specifies the server restart cluster |
| Notes | Notes that were added during the Review portion of the Add Restart Task wizard |
| Actions | The following are the status and the corresponding actions: Scheduled status: Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable. Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task Cancel Task—Cancels the selected task Delete—Deletes the selected task permanently Canceled status: Edit—Shows the Edit Server Restart Task window. Allows you to edit the selected task Delete—Deletes the selected task permanently Started status: Cancel Task—Cancels the selected task Paused status: Resume—Restarts task at the next step. View Details—Navigates to the monitoring page showing all the tasks available Start Task—Start task is present if the task is started manually. Time is not selected for this action Note Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. Cancel Task—Cancels the selected task Paused due to Error: Retry—This causes the task to restart and retry the last failed task action (the failed step). Resume—This causes the task to start at the next step (after the failed step). View Details—Navigates to the monitoring page showing all the tasks available Cancel Task—Cancels the selected task Successful status: View Details—Navigates to the monitoring page showing all the tasks available. Delete—Deletes the selected task permanently Failed status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently | Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Show | Allows you to filter restart tasks by status, by selecting one of the following options from the drop-down list: Quick Filter—To filter the tasks based on the status All—To show all the tasks available Scheduled—To show the tasks that are scheduled Canceled—To show the tasks that are canceled Running—To show the tasks that are started Paused—To show the tasks that are paused Paused due To Error—Indicates that the task is in a paused state due to an error in the system Successful—To show the tasks that are successful Failed—To show the tasks that failed |
| Filter | Select a status and click Filter to set a search rule at the bottom of the search window. |
| Delete | Click the checkbox next to the task and click the Delete button at the top of the table. You can also click Delete under the
                                             Actions column for the task you wish to delete. |
| Add Server Restart Task button | Opens the Add Server Restart Task wizard. Note You can also open the Add Server Restart Task wizard by selecting Edit in the Actions column for a particular server restart
                                                         task. | Note | You can also open the Add Server Restart Task wizard by selecting Edit in the Actions column for a particular server restart
                                                         task. |
| Note | You can also open the Add Server Restart Task wizard by selecting Edit in the Actions column for a particular server restart
                                                         task. |
| Add Server Restart Task window For information about how to add a server restart task, see "Create a Restart Task" . |
| Choose Cluster page | From the Choose Cluster page, select the cluster from the drop-down list. After you select the cluster, you will see that
                                             the nodes listed in the Cluster Nodes table change accordingly. Select the servers to be restarted. |
| Set Start Time page | From the Set Start Time page, select a start time for the task. Note The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard. | Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Set Run Sequence page | From the Set Run Sequence page, specify the sequence in which the restart is processed on the servers. You can change the
                                             sequence of steps by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit an existing
                                             step. Check the Use Last Configured Run Sequence check box if you want to reuse the previous sequence. By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state. |
| Review page | The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them. You can add notes to the Notes field for future reference. |

| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
|---|---|

| Note | You can also open the Add Server Restart Task wizard by selecting Edit in the Actions column for a particular server restart
                                                         task. |
|---|---|

| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
|---|---|

| Setting | Description |
|---|---|
| Scheduled Tasks and History table |
| Status | Provides information about the readdress task: Successful—Indicates that the task has finished without errors Running—Indicates that the task is currently running Scheduled—Indicates that the task has not yet started Canceled—Indicates that the user has chosen not to run task Paused—Indicates that the task is in a paused state waiting for feedback Paused due To Error—Indicates that the task is in a paused state due to an error in the system Failed—Indicates that the task has stopped due to error |
| Start Time | Specifies the start time of the readdress task |
| Last Status Report Time | Specifies the time at which the action was completed. The completed action may be a success or failure. |
| Cluster | Specifies the readdress cluster |
| Notes | Note that were added during the Review portion of the Add Readdress Task wizard |
| Actions | The following are the status and the corresponding actions: Scheduled status: Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable. Edit—Shows the Edit Readdress Task window. Allows you to edit the selected task Cancel Task—Cancels the selected task Delete—Deletes the selected task permanently Canceled status: Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task Delete—Deletes the selected task permanently Started status: Cancel Task—Cancels the selected task Paused status: Resume—Restarts task at the next step. View Details—Navigates to the monitoring page showing all the tasks available Start Task—Start task is present if the task is started manually. Time is not selected for this action Note Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. Cancel Task—Cancels the selected task Paused due to Error: Retry—This causes the task to restart and retry the last failed task action (the failed step or sub-step). Resume—This causes the task to start at the next step (after the failed step or sub-step). View Details—Navigates to the monitoring page showing all the tasks available Cancel Task—Cancels the selected task Successful status: View Details—Navigates to the monitoring page showing all the tasks available. Delete—Deletes the selected task permanently Failed status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently | Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Show | Allows you to filter readdress tasks by status, by selecting one of the following options from the drop-down list: Quick Filter—To filter the tasks based on the status All—To show all the tasks available Scheduled—To show the tasks that are scheduled Canceled—To show the tasks that are canceled Running—To show the tasks that are started Paused—To show the tasks that are paused Paused due To Error—To show the tasks that are paused due to an error in the system Successful—To show the tasks that are successful Failed—To show the tasks that failed |
| Filter | Select a status and click Filter to set a search rule at the bottom of the search window. |
| Delete | Check the check box next to the task and click the Delete button at the top of the table. You can also click Delete under
                                             the Actions column for the task you wish to delete. |
| Add Readdress Task button | Opens the Add Readdress Task wizard. Note You can also open the Add Readdress Task wizard by selecting Edit in the Actions column for a particular readress task. | Note | You can also open the Add Readdress Task wizard by selecting Edit in the Actions column for a particular readress task. |
| Note | You can also open the Add Readdress Task wizard by selecting Edit in the Actions column for a particular readress task. |
| Add Readdress Task window For information about how to Add a Readdress Task, see "Create a Readdress Task" . |
| Choose Cluster page | From the Choose Cluster page, select the cluster from the drop-down list. Click View Nodes to the nodes associated with this
                                             cluster. The View UC Cluster Nodes dialog box opens, listing the nodes in a table that identifies the following: Hostname IP Address Product Role The View UC Cluster Nodes dialog box is not editable. Click Close to return to the Choose Cluster page. |
| Enter New Hostnames/IP Addresses page | From the Enter New Hostnames/IP Addresses page, click Edit under the Actions column to open the Edit Hostname/IP Address dialog
                                             box. This dialog box allows you to enter a new hostname or IP address for the cluster nodes to be readdressed. You have the
                                             option of using DHCP or a static IP address. |
| Set Start Time page | From the Set Start Time page, select a start time for the task. Note The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard. You can use this page to also enable the re-address option. Check the Pause before network verification substeps to allow external changes check box if you wish to introduce a pause between the re-address and the network change verification substeps upon changing
                                             the subnet or gateway. During this pause, you can make the necessary network changes to the virtual machine configuration,
                                             such as VLAN. Note After you make the changes, resume the task to complete the verification. | Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. | Note | After you make the changes, resume the task to complete the verification. |
| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Note | After you make the changes, resume the task to complete the verification. |
| Set Run Sequence page | From the Set Run Sequence page, specify the sequence in which the readdress is processed on the servers. The sequence of the
                                             steps is changed by clicking the up and down arrows of a particular step. You can also add or delete a step, or edit an existing
                                             step. Check the Use Last Configured Run Sequence check box if you want to reuse the previous sequence. By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state. |
| Review page | The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them. You can add notes to the Notes field for future reference. |

| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
|---|---|

| Note | You can also open the Add Readdress Task wizard by selecting Edit in the Actions column for a particular readress task. |
|---|---|

| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
|---|---|

| Note | After you make the changes, resume the task to complete the verification. |
|---|---|

| Setting | Description |
|---|---|
| Scheduled Tasks and History table |
| Status | Provides information about the install task: Successful—Indicates that the task has finished without errors Running—Indicates that the task is currently running Scheduled—Indicates that the task has not yet started Canceled—Indicates that the user has chosen not to run task Paused—Indicates that the task is in a paused state waiting for feedback Paused due To Error—Indicates that the task is in a paused state due to an error in the system Failed—Indicates that the task has stopped due to error |
| Start Time | Specifies the start time of the install task |
| Last Status Report Time | Specifies the time at which the action was completed. The completed action may be a success or failure. |
| Cluster | Specifies the install cluster |
| Notes | Notes that were added during the Review portion of the Add Install Task wizard |
| Actions | The following are the status and the corresponding actions: Scheduled status: Run Validation Test—Runs a validation test to ensure that all the ESXi host is present, the VMs are in the correct state,
                                                         and the .iso file to be used in the install is present. Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task Cancel Task—Cancels the selected task Delete—Deletes the selected task permanently Canceled status: Delete—Deletes the selected task permanently Started status: Cancel Task—Cancels the selected task Paused status: Resume—Restarts task at the next step. View Details—Navigates to the monitoring page showing all the tasks available Start Task—Start task is present if the task is started manually. Time is not selected for this action Note Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. Cancel Task—Cancels the selected task Paused due to Error: Retry—Retry the last failed step. This button causes the task to retry the last step that failed, and restart the task (the
                                                         failed step). Resume—Resumes the task at the next step (after the failed step). Use this option only if the failed step is non-essential,
                                                         or if you have manually performed that step View Details—Navigates to the monitoring page showing all the tasks available Cancel Task—Cancels the selected task Successful status: View Details—Navigates to the monitoring page showing all the tasks available. Delete—Deletes the selected task permanently Failed status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently | Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Show | Allows you to filter install tasks by status, by selecting one of the following options from the drop-down list: Quick Filter—To filter the tasks based on the status All—To show all the tasks available Scheduled—To show the tasks that are scheduled Canceled—To show the tasks that are canceled Running—To show the tasks that are started Paused—To show the tasks that are paused Paused due To Error—To show the tasks that are paused due to an error in the system Successful—To show the tasks that are successful Failed—To show the tasks that failed |
| Filter | Select a status and click Filter to set a search rule at the bottom of the search window. |
| Delete | Click the checkbox next to the task and click the Delete button at the top of the table. You can also click Delete under the
                                             Actions column for the task you wish to delete. |
| Add Install Task button | Opens the Add Installation Task wizard. Note You can also open the Add Installation Task wizard by selecting Edit in the Actions column for a particular install task. | Note | You can also open the Add Installation Task wizard by selecting Edit in the Actions column for a particular install task. |
| Note | You can also open the Add Installation Task wizard by selecting Edit in the Actions column for a particular install task. |
| Add Installation Task window For information about how to add an installation task, see "Create an Install Task" . |
| Choose Installation Cluster page | From the Choose Cluster page, select the cluster from the drop-down list. After you select the cluster, you will see that
                                             the nodes listed in the Installation Cluster Nodes table change accordingly. |
| Choose Installation Files page | From the Choose Installation Files page, select the installation images to be installed on the staging cluster. The ISO images
                                             must be uploaded to the /install directory on the system sftp server for Cisco Prime Collaboration Deployment. |
| Set Start Time page | From the Set Start Time page, select a start time for the task. Note The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard. | Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Specify Installation Sequence page | From the Specify Installation Sequence page, specify the sequence in which the installation is processed on the servers. You
                                             can change the sequence of steps by clicking the up and down arrows of a particular step. You can also add or delete a step,
                                             or edit an existing step. By default, each node is sequenced into its own step. |
| Review page | The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them. You can add notes to the Notes field for future reference. |

| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
|---|---|

| Note | You can also open the Add Installation Task wizard by selecting Edit in the Actions column for a particular install task. |
|---|---|

| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
|---|---|

| Setting | Description |
|---|---|
| Scheduled Tasks and History table |
| Status | Provides information about the migrate task: Successful—Indicates that the task has finished without errors Running—Indicates that the task is currently running Scheduled—Indicates that the task has not yet started Canceled—Indicates that the user has chosen not to run task Paused—Indicates that the task is in a paused state waiting for feedback Paused due To Error—Indicates that the task is in a paused state due to an error in the system Failed—Indicates that the task has stopped due to error |
| Start Time | Specifies the start time of the migrate task |
| Last Status Report Time | Specifies the time at which the action was completed. The completed action may be a success or failure. |
| Cluster | Specifies the cluster being migrated. |
| Notes | Notes that were added during the Review portion of the Add Migration Task wizard |
| Actions | The following are the status and the corresponding actions: Scheduled status: Run Validation Test—Runs a validation test to ensure that all nodes are available and that none of the specified new addresses
                                                         are reachable. It also checks that the ESXi hosts that the VMs reside on are mounted. It also verifies that the iso file to
                                                         be used is present. Edit—Shows the Edit Upgrade Task window. Allows you to edit the selected task Cancel Task—Cancels the selected task Delete—Deletes the selected task permanently Canceled status: Delete—Deletes the selected task permanently Started status: Cancel Task—Cancels the selected task Paused status: Resume—Restarts task at the next step. View Details—Navigates to the monitoring page showing all the tasks available Start Task—Start task is present if the task is started manually. Time is not selected for this action Note Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. Cancel Task—Cancels the selected task Paused due to Error: Retry—Retry the last failed step (the failed step or sub-step). This button causes the task to retry the last step that failed,
                                                         and restart the task. Resume—Resumes the task at the next step (after the failed step or sub-step). Use this option only if the failed step is non-essential,
                                                         or if you have manually performed that step. View Details—Navigates to the monitoring page showing all the tasks available Cancel Task—Cancels the selected task Successful status: View Details—Navigates to the monitoring page showing all the tasks available. Delete—Deletes the selected task permanently Failed status: View Details—Navigates to the monitoring page showing all the tasks available Delete—Deletes the selected task permanently | Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
| Show | Allows you to filter migration tasks by status, by selecting one of the following options from the drop-down list: Quick Filter—To filter the tasks based on the status All—To show all the tasks available Scheduled—To show the tasks that are scheduled Canceled—To show the tasks that are canceled Running—To show the tasks that are started Paused—To show the tasks that are paused Paused due To Error—To show the tasks that are paused due to an error in the system Successful—To show the tasks that are successful Failed—To show the tasks that failed |
| Filter | Select a status and click Filter to set a search rule at the bottom of the search window. |
| Delete | Check the check box next to the task and click the Delete button at the top of the table. You can also click Delete under
                                             the Actions column for the task you wish to delete. |
| Add Migration Task button | Opens the Add Migration Task wizard. Note You can also open the Add Migration Task wizard by selecting Edit in the Actions column for a particular migrate task. | Note | You can also open the Add Migration Task wizard by selecting Edit in the Actions column for a particular migrate task. |
| Note | You can also open the Add Migration Task wizard by selecting Edit in the Actions column for a particular migrate task. |
| Add Migration Task window For information about how to add a migration task, see "Add Migration Task" . |
| Choose Source and Destination Clusters page | From the Choose Source and Destination Clusters page, select the source UC cluster from the drop-down list. After you select
                                             the source cluster, you select the destination cluster from the drop-down list and the nodes from the Node Mapping from Source
                                             to Destination Cluster table. |
| Choose Upgrade Files page | From the Choose Upgrade File page, select the upgrade file for each product being upgraded. You will only have the option
                                             of selecting files for the product type you selected on the Choose Cluster page. |
| Set Start Time page | From the Set Start Time page, select a start time for the task. Note The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. You have the option of setting the start time for a specific time, starting the task manually, or setting the task to begin
                                             immediately upon completion of the wizard. | Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
| Specify Migration Procedure page | From the Specify Migration Procedure page, specify the sequence in which the migration is processed on the servers. You can
                                             change the sequence of the stepsby clicking the up and down arrows of a particular step. You can also add or delete a step,
                                             or edit an existing step. By default, each node is sequenced into its own step. The Revert to Default button returns the steps to this original state. |
| Review page | The Review page provides a summary of the options you have selected in the previous steps. The nodes listed in the Nodes field
                                             are view-only; you cannot select them. You can add notes to the Notes field for future reference. |

| Note | Start Task is applicable only if you select Start task manually option in the Set Start Time panel. When you select the task manually, the resume option is unavailable in the monitoring page. |
|---|---|

| Note | You can also open the Add Migration Task wizard by selecting Edit in the Actions column for a particular migrate task. |
|---|---|

| Note | The time specified is based on the Cisco Prime Collaboration Deployment server time, not the time zone of the selected cluster. |
|---|---|

| Setting | Description |
|---|---|
| Clusters table |
| Cluster
                                             						Name | Shows
                                             						the available clusters |
| Product
                                             						and Version | Shows
                                             						the product for which the cluster is added along with its version |
| Nodes | Shows
                                             						the number of nodes associated with the cluster |
| Cluster
                                             						Type | Shows
                                             						the cluster type, such as Discovered, New install, or Migration |
| Discovery Status | Shows
                                             						the discovery status of a cluster. This field shows one of the following
                                             						discovery statuses: Contacting Discovering Successful Node Unreachable Timeout Internal Error |
| Actions | Includes
                                             						the following options: Edit —Edit an added new node that has not yet been
                                                      							 installed Delete —Delete an added new node that has not yet
                                                      							 been installed |
| Show | Allows
                                             						you to filter cluster tasks by status, by selecting one of the following
                                             						options from the drop-down list: All—To show all the available clusters Discovered—To show the clusters that are scheduled New Install—To show the cluster that newly installed Migration—To show the clusters that are migrated |
| Filter | Select a status and click Filter to set a search rule at the bottom of the
                                             						search window. |
| Discover
                                             						Cluster button | Click
                                             						this button so that Cisco Prime Collaboration Deployment communicates with the
                                             						servers that are already running Unified Communications applications and adds
                                             						that cluster information into the Cisco Prime Collaboration Deployment
                                             						inventory |
| Define Migration
                                                						  Destination Cluster For information on how to create a migration cluster, see the Create a Migration Cluster . |
| Specify Clusters page | Enter
                                             						details for the following fields to configure a destination cluster for a
                                             						migration task: Source Cluster —From the drop-down list, select a
                                                      							 source UC cluster. View Nodes —Click this link to view the available
                                                      							 cluster nodes. Active Versions —Shows the active versions of the
                                                      							 source UC cluster. Destination Cluster Nickname —Enter a nickname for
                                                      							 the destination cluster. Destination Network Settings —Choose one of the
                                                      							 following options: Use the source node network settings for all destination
                                                                  									 nodes —Choose this option to retain the default network options. Enter new network settings for one or more destination
                                                                  									 nodes —Choose this option to modify the default network settings or
                                                               								  enter new network options. Note If you select the Use the source node network settings for all destination
                                                                              										nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns on the Assign Destination Cluster Nodes window. If you
                                                                           									 select the Enter new network settings for one or more destination
                                                                              										nodes option, only source hostname appears and not the destination
                                                                           									 hostname on the Assign Destination Cluster Nodes window. | Note | If you select the Use the source node network settings for all destination
                                                                              										nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns on the Assign Destination Cluster Nodes window. If you
                                                                           									 select the Enter new network settings for one or more destination
                                                                              										nodes option, only source hostname appears and not the destination
                                                                           									 hostname on the Assign Destination Cluster Nodes window. |
| Note | If you select the Use the source node network settings for all destination
                                                                              										nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns on the Assign Destination Cluster Nodes window. If you
                                                                           									 select the Enter new network settings for one or more destination
                                                                              										nodes option, only source hostname appears and not the destination
                                                                           									 hostname on the Assign Destination Cluster Nodes window. |
| Assign
                                             						Destination Cluster Nodes page | Source Cluster —Displays the name of the source
                                                   							 cluster. Destination Cluster —Displays the name of the
                                                   							 destination cluster. Assign Destination Cluster Nodes —Click this button
                                                   							 to associate destination virtual machines with nodes in the source cluster. Note If DHCP is in use on your source node, the destination node is
                                                               								also configured to use DHCP, and you will have no option to change your network
                                                               								settings in this wizard. | Note | If DHCP is in use on your source node, the destination node is
                                                               								also configured to use DHCP, and you will have no option to change your network
                                                               								settings in this wizard. |
| Note | If DHCP is in use on your source node, the destination node is
                                                               								also configured to use DHCP, and you will have no option to change your network
                                                               								settings in this wizard. |
| Configure NTP/SMTP Settings | Enter
                                             						details for the following sections to configure NTP and SMTP to the migration
                                             						nodes when the migration task is run: Network Time Protocol (NTP) Configuration window—Enter IP address of at least one of the following fields: NTP Server 1 NTP Server 2 NTP Server 3 NTP Server 4 NTP Server 5 (Optional) Simple Mail Transfer Protocol (SMTP) Configuration window SMTP Server —Enter IP address of the SMTP server. |
| Define
                                             						DNS Settings | (Optional) From the available hosts added along with the
                                             						functions, check a node to configure DNS setting for the migration cluster
                                             						nodes and click Assign DNS Settings |
| Discover Cluster window For
                                             						information on how to Discover a Cluster, see Discover a Cluster . |
| Cluster
                                             						Access page | Enter
                                             						details in the following fields: Choose a Nickname for this Cluster —Enter a nick name
                                                      							 for the cluster. Hostname/IP Address of Cluster Publisher —Enter
                                                      							 either the host name or the IP address for the publisher node of the cluster. OS Admin Username —Enter the OS administrator user
                                                      							 name. OS Admin Password —Enter the password for the OS
                                                      							 administrator. Note Ensure that cluster password is less than 16 characters. Enable NAT —Check this check box to enable NAT for
                                                      							 the cluster. Note When you check the Enable NAT check box, the NAT IP column appears on the Cluster Discovery
                                                                  								Progress page. | Note | Ensure that cluster password is less than 16 characters. | Note | When you check the Enable NAT check box, the NAT IP column appears on the Cluster Discovery
                                                                  								Progress page. |
| Note | Ensure that cluster password is less than 16 characters. |
| Note | When you check the Enable NAT check box, the NAT IP column appears on the Cluster Discovery
                                                                  								Progress page. |
| Cluster
                                             						Discovery Progress page | This
                                             						page displays the status of cluster discovery in the following fields: Cluster Name —Shows the cluster name along with the
                                                      							 status message of the cluster discovery. Hostname —Shows the host name. Contact Status —Shows the one of the following
                                                      							 statuses for cluster discovery: Contacting Discovering Successful Node Unreachable Timeout Internal Error Product —Shows the product of the cluster. Active version —Shows the version currently in use. Inactive version —Shows the version that is currently
                                                      							 not in use. NAT IP —This column appears only if you check the Enable NAT check box on the Cluster Access page. Hardware —Shows the hardware associated to the
                                                      							 cluster. |
| Cluster
                                             						Role Assignment page | This page displays the role assignments of cluster in the following fields: Hostname —Shows the host name. Product —Shows the product of the cluster. Functions —Shows the different roles that are assigned to a particular node. For example Publisher,Primary TFTP, Secondary TFTP. SFTP Server —Shows the location of the ISO files. By default the SFTP server is PCD. Edit Settings —Allows to assign more  roles or functionality to the node. |
| Define New UC Cluster
                                                						  window For information on how to install a new cluster, see the Add New Cluster for Fresh Install . After
                                             						you click this button, a wizard appears that guides you to the installation
                                             						process of a new UC cluster. |
| Specify Cluster Name window | Choose the Nickname for this cluster —Enter the
                                             						cluster name |
| Add
                                             						Virtual Machines window | Enter
                                             						details in the following fields: Add Node —Check one or more functions for adding a
                                                      							 node from the available check boxes. Notes —(Optional) Add a nodes for the selected
                                                      							 cluster. Virtual Machines —Add a node from the available
                                                      							 virtual machines. Note The available VMs are sorted by name and by host. The details of
                                                                     								  virtual machines, such as VM Name, ESXi Host, and Power State, appear in this
                                                                     								  window. Show —Allows you to filter virtual machine by status,
                                                      							 by selecting options from the drop-down list. Network —Select one of the following options: Static IP address —Enter the details for hostname, IP
                                                               								  Address, Subnet Mask, Gateway, and NAT IP fields. Use DHCP with Reservations —Enter the IP address that
                                                               								  you have a reservation for on your DHCP server (associated with the MAC address
                                                               								  for that VM) in addition to the hostname. Products and Functions —From the drop-down list,
                                                      							 select a product. In the Functions section, check the appropriate function
                                                      							 check boxes for your VM. Note Check the Publisher check box for at least one node in the
                                                                        									 cluster that you have defined for each application type. (Optional) Add a note about the functions that you have assigned
                                                                        									 in the Notes field below the Publisher field. Virtual Machines section—Choose a VM for the selected node. | Note | The available VMs are sorted by name and by host. The details of
                                                                     								  virtual machines, such as VM Name, ESXi Host, and Power State, appear in this
                                                                     								  window. | Note | Check the Publisher check box for at least one node in the
                                                                        									 cluster that you have defined for each application type. (Optional) Add a note about the functions that you have assigned
                                                                        									 in the Notes field below the Publisher field. |
| Note | The available VMs are sorted by name and by host. The details of
                                                                     								  virtual machines, such as VM Name, ESXi Host, and Power State, appear in this
                                                                     								  window. |
| Note | Check the Publisher check box for at least one node in the
                                                                        									 cluster that you have defined for each application type. (Optional) Add a note about the functions that you have assigned
                                                                        									 in the Notes field below the Publisher field. |
| Configure Cluster Wide Settings window | Enter
                                             						details for the fields of the following sections: OS Administration
                                                						  Credentials Username —Enter user name of the OS administrator. Password —Enter password of the user name. Confirm Password —Re-enter the same password that you
                                                      							 entered in the Password field. Application
                                                						  Credentials Username —Enter user name of the application user. Password —Enter password of the user name. Confirm Password —Re-enter the same password that you
                                                      							 entered in the Password field. Security
                                                						  Password Password —Enter the security password for the
                                                      							 cluster. Confirm Password —Re-enter the same password that you
                                                      							 entered in the Password field. SMTP Settings (Optional) SMTP Server —Enter the IP address of the SMTP server. Certificate
                                                						  Information Organization —Enter the name of the organization of
                                                      							 which the certificate is being used. Unit —Enter the number of certificates being used. Location —Enter the location where the certificate is
                                                      							 being used. State —Enter the state where the certificate is being
                                                      							 used. Country —From the drop-down list, select the country
                                                      							 where the certificate is being used. |
| Configure DNS Settings window | (Optional) From the available hosts added along with the
                                             						functions, check a node to configure DNS setting for a node and click Assign DNS Settings . |
| Configure NTP Settings | To
                                             						configure the Network Time Protocol, enter details of at least one NTP server
                                             						in the following fields. If you are not using DNS, NTP server must be an IP
                                             						address. If you are using DNS, NTP server can be an FQDN. NTP Server 1 NTP Server 2 NTP Server 3 NTP Server 4 NTP Server 5 Note It
                                                            						  is recommended that you define at least IP addresses of two NTP servers | Note | It
                                                            						  is recommended that you define at least IP addresses of two NTP servers |
| Note | It
                                                            						  is recommended that you define at least IP addresses of two NTP servers |
| Configure NIC Settings | (Optional) Enter details for the following fields: Hostname, Functions, and MTU size column—From the available
                                                      							 servers, check the check box for a server. MTU Size —Enter an MTU size between 552 and 1500 and
                                                      							 click Apply to Selected . Apply to Selected —Click this button to apply the MTU
                                                      							 size for the selected host. Apply Default MTU —Click this button to apply the
                                                      							 default value of MTU size for the selected host. |
| Configure Time Zones window | Enter
                                             						details for the following fields to specify the time zone for each cluster
                                             						node: Region —From the drop-down list, select the region
                                                      							 for the cluster node. Time Zone —From the drop-down list, select the time
                                                      							 zone of the selected region. Apply to Selected —Click this button to apply the
                                                      							 time zone changes for each cluster node. |

| Note | If you select the Use the source node network settings for all destination
                                                                              										nodes option, same IP address appears for both the source node NAT IP and Dest NAT IP columns on the Assign Destination Cluster Nodes window. If you
                                                                           									 select the Enter new network settings for one or more destination
                                                                              										nodes option, only source hostname appears and not the destination
                                                                           									 hostname on the Assign Destination Cluster Nodes window. |
|---|---|

| Note | If DHCP is in use on your source node, the destination node is
                                                               								also configured to use DHCP, and you will have no option to change your network
                                                               								settings in this wizard. |
|---|---|

| Note | Ensure that cluster password is less than 16 characters. |
|---|---|

| Note | When you check the Enable NAT check box, the NAT IP column appears on the Cluster Discovery
                                                                  								Progress page. |
|---|---|

| Note | The available VMs are sorted by name and by host. The details of
                                                                     								  virtual machines, such as VM Name, ESXi Host, and Power State, appear in this
                                                                     								  window. |
|---|---|

| Note | Check the Publisher check box for at least one node in the
                                                                        									 cluster that you have defined for each application type. (Optional) Add a note about the functions that you have assigned
                                                                        									 in the Notes field below the Publisher field. |
|---|---|

| Note | It
                                                            						  is recommended that you define at least IP addresses of two NTP servers |
|---|---|

| Setting | Description |
|---|---|
| ESXi Hosts table |
| Hostname | Shows
                                             						the ESXi host name. |
| IP
                                             						Address | Shows
                                             						the IP address of the ESXi host. |
| Description | Shows
                                             						the description, if any, of the ESXi host. |
| Actions | Includes
                                             						the following options: Edit —Click this link to edit the ESXi host details. Delete —Click this link to delete the ESXi host from
                                                      							 the database. |
| Add ESXi
                                             						Host | Click
                                             						this button to add an ESXi host in the database. |
| Add ESXi Host window |
| Hostname/IP Address | Enter
                                             						the host name of the IP address of the ESXi host. |
| Username | Enter
                                             						the user name. |
| Password | Enter
                                             						the password for the user. |
| Description | (Optional) Enter the description for the ESXi host. |

| Setting | Description |
|---|---|
| SFTP Servers/Datastore section The
                                             						Cisco Prime Collaboration Deployment server serves as a local SSH File Transfer
                                             						Protocol or Secure File Transfer Protocol (SFTP) server that stores the ISO and
                                             						COP files to be used by upgrade, fresh, install, and migrate tasks. For more
                                             						information on SFTP Datastore, see SFTP Servers and Datastore . |
| Delete | Click
                                             						this button to delete the selected SFTP server from the datastore. |
| Add
                                             						Server | Click
                                             						this button to add the selected SFTP server to the datastore. |
| Server
                                             						IP | Shows
                                             						the IP addresses of the available SFTP servers in the datastore. |
| Server
                                             						Description | Shows
                                             						the description added for the available SFTP servers. |
| Database
                                             						Directory | Shows
                                             						the directory path of the SFTP servers. |
| Status | Shows
                                             						the status of the SFTP server. For example, Connected and Local. |
| Actions | Includes the following options: Edit —Click this link to edit the SFTP server
                                                      							 details. Delete —Click this link to delete the selected SFTP
                                                      							 server from the datastore. |
| SFTP/Datastore Files section |
| Delete | Click
                                             						this button to delete the ISO and COP files of the selected SFTP server from
                                             						the datastore. |
| Filename | Shows
                                             						the available ISO and COP files of the SFTP servers. |
| Server
                                             						IP | Shows
                                             						the IP address of the SFTP servers. |
| Server
                                             						Description | Shows
                                             						the description added for the available SFTP servers. |
| Directory | Shows
                                             						the directory name where the SFTP files of the SFTP servers are stored. |
| File
                                             						Type | Shows
                                             						the type of file, such as upgrade file and fresh install. |
| Copied
                                             						On (local) | Shows
                                             						the data, time, and time zone when the SFTP file is copied to the datastore. |

| Setting | Description |
|---|---|
| Notification Settings section For more information, see the Email Notification . |
| Notifications | Select
                                             						one of the following options: Do not send email notification —Choose this option if
                                                      							 you do not wish to receive any email notification for errors or types of tasks. Note If
                                                                  								you choose this option, all the fields of this section become non-editable. Errors only - Send email only when there is an
                                                         								error —Choose this option if you wish to receive email notifications
                                                      							 for task event errors in the following states: Failed to Schedule Failed Failed to cancel Paused on error Standard - Send email when tasks start, pause, finish, or when
                                                         								there is an error —Choose this option if you wish to receive email
                                                      							 notifications when a task enters any of the following states: Scheduled Failed to Schedule Started Successful Failed Canceled Canceling Failed to Cancel Paused on Error Paused Paused – Required | Note | If
                                                                  								you choose this option, all the fields of this section become non-editable. |
| Note | If
                                                                  								you choose this option, all the fields of this section become non-editable. |
| Email
                                             						Recipients | Enter
                                             						the email address of one or multiple recipients. Note Separate multiple email addresses with a comma. | Note | Separate multiple email addresses with a comma. |
| Note | Separate multiple email addresses with a comma. |
| Use TLS | Check
                                             						this check box so that Transport Layer Security (TLS) protocol ensures privacy
                                             						or prevent tampering with the email between the application and the email
                                             						recipients. |
| Mail server credentials section |
| Username | Enter
                                             						the user name of the mail server. |
| Password | Enter
                                             						the password to log in to the mail server. |
| Server Settings section |
| SMTP
                                             						Server | Enter
                                             						the IP address of the SMTP server. |
| Port | Enter
                                             						the number of ports for the SMTP server. |
| Save | Click
                                             						this button to save the changes you have made in this page. |
| Reset | Click
                                             						this button to set the default values on this page. |
| Send
                                             						Test Email | Click
                                             						this button to send a test email to one or more recipients for the errors only
                                             						and standard options. |

| Note | If
                                                                  								you choose this option, all the fields of this section become non-editable. |
|---|---|

| Note | Separate multiple email addresses with a comma. |
|---|---|

| Setting | Description |
|---|---|
| PCD NAT
                                                						  Settings For more information on network address translation, see the Network Address Translation Support . |
| Hostname | Shows
                                             						the host name of the server. |
| Private
                                             						IP | Shows
                                             						the IP address of the server that is in the private network. |
| NAT IP | Enter
                                             						the NAT IP address. |
| Save | The NAT
                                             						IP address is saved as an entry in a configuration file on Cisco Prime
                                             						Collaboration Deployment. This entry is used when the application nodes try to
                                             						contact Cisco Prime Collaboration Deployment. |
| Reset | (Optional) The NAT IP address is reset to the earlier saved NAT
                                             						IP address. |

| Setting | Description |
|---|---|
| Disk Space Warning Level
                                                						  Configuration For details, see Disk Space Warning Level . |
| Total
                                             						Disk Space (GB) | Shows
                                             						the total disk space on the server. |
| Available Disk Space (GB) | Shows
                                             						the available disk space for use on the server. |
| Warning
                                             						Level Disk Space (GB) | Enter
                                             						the disk space warning value. After entering this value, click the information
                                             						link to check if the space value you entered is available for use on the
                                             						server. |
| Save | Save the
                                             						warning disk space value. |
| Reset | (Optional) Resets the page with the default values. |

| Setting | Description |
|---|---|
| Max Nodes | Enter the maximim nodes on the server. |
| Save | Save the maximum nodes value. |
| Reset | (Optional) Resets the page with the default values. |

| Setting | Description |
|---|---|
| Audit Level Settings section |
| Application Audit Event Level | From the drop-down list, choose one of the following options: Info —To view the audit event level as an information message. Warning —To view the audit event level as a warning message. Debug —To view the audit event level as a debug message. Error —To view the audit event level as an error message. |
| Remote SysLog Settings section |
| Remote Syslog Server Name / IP | Enter the name of remote syslog server or the IP address for
                                             						the audit logs to be logged in to this remote server. |
| Local Audit Log Settings |
| Enable Local Audit Log | Check or uncheck this check box to enable or disable the
                                             						local audit log. Note When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                               not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                               , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID. When you check this field, the Enable Log Rotation field
                                                               								becomes active. | Note | When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                               not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                               , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID. When you check this field, the Enable Log Rotation field
                                                               								becomes active. |
| Note | When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                               not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                               , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID. When you check this field, the Enable Log Rotation field
                                                               								becomes active. |
| Enable Log Rotation | Check or uncheck this check box to enable or disable the log
                                             						rotation. Note You can configure this field if the Enable Local Audit Log field is
                                                               								enabled. After you enable this field, you can configure the Maximum No of Files , Maximum File Size(MB) , and Warning Threshold for Approaching Log
                                                                  								  Rotation Overwrite(%) fields. When you uncheck the Enable Local Audit Log field,
                                                               								the default values of these fields are not applicable as they are not active. | Note | You can configure this field if the Enable Local Audit Log field is
                                                               								enabled. After you enable this field, you can configure the Maximum No of Files , Maximum File Size(MB) , and Warning Threshold for Approaching Log
                                                                  								  Rotation Overwrite(%) fields. When you uncheck the Enable Local Audit Log field,
                                                               								the default values of these fields are not applicable as they are not active. |
| Note | You can configure this field if the Enable Local Audit Log field is
                                                               								enabled. After you enable this field, you can configure the Maximum No of Files , Maximum File Size(MB) , and Warning Threshold for Approaching Log
                                                                  								  Rotation Overwrite(%) fields. When you uncheck the Enable Local Audit Log field,
                                                               								the default values of these fields are not applicable as they are not active. |
| Maximum No of Files | Enter an integer value for the Maximum No of Files field to configure
                                             						the maximum number of files that can be created on the server. After you check the Enable Log Rotation field, you can configure the value for Maximum No of Files field. Once the number of files reaches the configured value, the log rotation process starts. In the log rotation process,
                                             all the log files are deleted and rewritten from the log file number 1. Note The value for this field must be in the range of 1 to 5000. | Note | The value for this field must be in the range of 1 to 5000. |
| Note | The value for this field must be in the range of 1 to 5000. |
| Maximum File Size(MB) | Enter a value for the Maximum File Size (MB) field to
                                             						configure the maximum file size of each log that is created on the server. Note The value for this field must be in the range of 1 to 10. | Note | The value for this field must be in the range of 1 to 10. |
| Note | The value for this field must be in the range of 1 to 10. |
| Warning Threshold for Approaching Log Rotation Overwrite(%) | Enter the warning threshold value for the Warning Threshold for Approaching Log Rotation
                                                						  Overwrite(%) field. After the configured warning threshold value is reached, an
                                             						email notification is sent to users to take back up of the audit log files.
                                             						These files are deleted or overwritten during log rotation. Note The value for this field must be in the range of 1 to 100. For details, see the Email notification topic in the Cisco Prime Collaboration Deployment Administration
                                                						  Guide . | Note | The value for this field must be in the range of 1 to 100. |
| Note | The value for this field must be in the range of 1 to 100. |
| Save | Click this button to save the changes you have made on this
                                             						page. |
| Reset | Click this button to set the default values on this page. |

| Note | When you check this field, the audit events are logged in the local server. When you uncheck this field, audit events are
                                                               not logged in the local server. The audit events includes User ID, ClientAddress, Severity, EventType, ResourceAccessed, EventuStatus
                                                               , AuditCategory, CompulsoryEvent, ComponentID, CorrelationID and Node ID. When you check this field, the Enable Log Rotation field
                                                               								becomes active. |
|---|---|

| Note | You can configure this field if the Enable Local Audit Log field is
                                                               								enabled. After you enable this field, you can configure the Maximum No of Files , Maximum File Size(MB) , and Warning Threshold for Approaching Log
                                                                  								  Rotation Overwrite(%) fields. When you uncheck the Enable Local Audit Log field,
                                                               								the default values of these fields are not applicable as they are not active. |
|---|---|

| Note | The value for this field must be in the range of 1 to 5000. |
|---|---|

| Note | The value for this field must be in the range of 1 to 10. |
|---|---|

| Note | The value for this field must be in the range of 1 to 100. |
|---|---|

| Setting | Description |
|---|---|
| Upload Customized Logon File |
| Upload File | Click the Browse button to browse to the
                                             						location of file that includes the customized sign-on message. |
| Require User Acknowledgment | Check or uncheck this check box to enable or disable user
                                             						acknowledgment for the file that the user receives. If this field is enabled, users get an acknowledgment as an
                                             						alert message on the Cisco Prime Collaboration Deployment sign-in page. This
                                             						message appears after they sign out for the first time from the same web
                                             						browser instance. |
| Upload File | Click this button to upload the file with the customized
                                             						sign-on message to the server. After you upload the file, a popup appears
                                             						showing the file upload status. |
| Delete | Click this button to delete the file with the customized
                                             						sign-on message. After you delete the file, popup appears showing the file
                                             						deletion status. |

| Setting | Description |
|---|---|
| PCD Releases | From the drop-down list, choose one of the releases of Cisco Prime Collaboration Deployment. The available options are Release
                                             12.6(1) up to the latest release. |
| Task Type | From the drop-down list, choose one of the following tasks to view the supported releases for a specific task: All Migration Install Upgrade Switch Version Server Restart Readdress |
| Product Type | From the drop-down list, choose one of the following products: CUCM—Implies Cisco Unified Communications Manager. IM&P—Implies Instant Messaging and Presence services CUC—Implies Cisco Unity Connection UCCX—Implies Cisco Unified Contact Center Express CER—Implies Cisco Emergency Responder |