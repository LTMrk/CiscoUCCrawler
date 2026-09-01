---
doc_id: developer-cisco-com-docs-task-routing-creating-script-selector-c6f28226d2
source_url: https://developer.cisco.com/docs/task-routing/creating-script-selector/
retrieved_at: 2026-09-01T17:34:53.419149+00:00
---

# Creating Script
	 Selector

The Script
		  Selector (also called Dialed Numbers) ensures the addressability of the Media
		  Routing Domain. This (Dialed number String) is used by the
		  task-creation/injection API.

For Routing
				  Type , select Customer Collaboration Platform .

For Media
				  Routing Domain , select one of the Task Routing
				  MRDs you created.

For Call
				  Type , select a call type that you created for Task
				  Routing .

Each
						dialed number must be associated with a call type. Default call type is not
						supported for tasks submitted with Task Routing APIs.

You can
				accept the default values.

When you
				configure the Network VRU Script, you specify whether it is interruptible. The
				Interruptible setting for the Network VRU Script controls whether the script
				can be interrupted (for example if an agent becomes available). This setting is
				not related to the Media Routing Domain Interruptible setting, which controls
				whether an agent working on a task in that MRD can be interrupted by a task
				from a non-interruptible MRD.

For more
				information on writing scripts to return estimated wait time, see the Cisco
				  Packaged Contact Center Enterprise Administration and Configuration Guide

## Desk
		Settings

If agents will use a Task Routing gadget in the Finesse desktop,
		leave the Logout Inactivity Time setting for those agents blank or delete the
		existing value. Otherwise, if the agent exceeds the Logout Inactivity Time in
		the voice MRD, the agent is logged out of the Cisco Finesse desktop, even if
		the agent is actively working on tasks from non-voice MRDs. The agent needs to
		log into the desktop again to continue working on the non-voice
		tasks.

## Increasing
		TCDTimeout Value

Complete this procedure only if you are using
		precision queues and routing tasks with potentially long durations, like
		emails. Several precision queue fields in the Termination_Call_Detail record are not completed until the end of
		a task. These precision queue fields are blank for tasks whose durations exceed
		the TCDTimeout registry key value. The default value of the TCDTimeout registry key is 9,000 seconds (2.5 hours).

Next

| Step 1 | Select Dialed
				Numbers from the Call option of the Manage menu. |
|---|---|
| Step 2 | Create dialed
			 numbers for Task Routing. Add
			 the numbers or strings that the third-party multichannel application will use
			 (via API) when submitting task requests. For Routing
				  Type , select Customer Collaboration Platform . For Media
				  Routing Domain , select one of the Task Routing
				  MRDs you created. For Call
				  Type , select a call type that you created for Task
				  Routing . Note Each
						dialed number must be associated with a call type. Default call type is not
						supported for tasks submitted with Task Routing APIs. | Note | Each
						dialed number must be associated with a call type. Default call type is not
						supported for tasks submitted with Task Routing APIs. |
| Note | Each
						dialed number must be associated with a call type. Default call type is not
						supported for tasks submitted with Task Routing APIs. |
| Step 3 | Create a Network VRU
				Script that references the Network VRU (MR_Network_VRU). The
			 Network VRU Script is used to return estimated wait time to customers. You can
				accept the default values. When you
				configure the Network VRU Script, you specify whether it is interruptible. The
				Interruptible setting for the Network VRU Script controls whether the script
				can be interrupted (for example if an agent becomes available). This setting is
				not related to the Media Routing Domain Interruptible setting, which controls
				whether an agent working on a task in that MRD can be interrupted by a task
				from a non-interruptible MRD. For more
				information on writing scripts to return estimated wait time, see the Cisco
				  Packaged Contact Center Enterprise Administration and Configuration Guide |

| Note | Each
						dialed number must be associated with a call type. Default call type is not
						supported for tasks submitted with Task Routing APIs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | If you are
				configuring a system to handle email or other long tasks, you can increase the
				TCDTimeout registry key value to a maximum of 86,400 seconds (24 hours). |  |
| Step 2 | Change the
				registry key on either the Side A or B Unified CCE Rogger. |  |
| Step 3 | Modify the
				following registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\Icm\<instance
				  me>\Router<A/B>\Router\CurrentVersion\Configuration\Global\TCDTimeout . |  |