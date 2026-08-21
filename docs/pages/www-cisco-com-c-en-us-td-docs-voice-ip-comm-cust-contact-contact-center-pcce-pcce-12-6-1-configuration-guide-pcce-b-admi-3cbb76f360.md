---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-configuration-guide-pcce-b-admi-3cbb76f360
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/configuration/guide/pcce_b_admin_configuration_guide_12_6_1/rcct_m_zero-downtime-upgrade.html
retrieved_at: 2026-08-21T16:53:08.824306+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(1)

Updated: August 21, 2023

Chapter: Graceful shutdown

## Chapter: Graceful shutdown

# Graceful shutdown

## Graceful shutdown

The graceful shutdown feature allows you to perform firmware upgrades, apply security patches, and apply engineering specials
                              (ES) without the need for a maintenance window. With this feature, actively used processes can be brought down while the backup
                              processes take over, with minimal impact to the contact center day-to-day (Day 2) operations. Agent and supervisor states,
                              call states, and call context can be maintained. Operations such as reskilling and changing an agent's team membership are
                              not affected.

The Unified CCE core components for managing call and agent states, such as the Unified CCE Router, PGs, CTI Server, and Outbound
                              Option Dialer, are duplexed. The duplex nature of these components means that the peer side can recover call and agent states
                              and continue processing if any process in one side stops. While the peer side recovers call and agent states, it may not recover
                              all information about call context.

The Unified CCE Logger and AW-HDS do not contribute directly to real time call and agent state activities. If one side of
                              the Unified CCE Logger or AW-HDS stops, it can recover its state from its peer when it starts back up.

### Components enabled for graceful shutdown

Before you perform a maintenance activity, you must put the Unified CCE Services that are running on the virtual machine (VM)
                                 into maintenance mode so that its peer can take over processing without impacting contact center operations. Set the following
                                 Unified CCE services to maintenance mode to gracefully shut them down. Stopping these services directly without maintenance
                                 mode impacts the agent and calls in progress.

Unified CCE Enterprise Agent PG

Unified CCE Outbound Option Dialer

Unified CCE Media Routing PG

You can stop the other Unified CCE Services directly using the Unified CCE Service Control Manager tool.

Before you stop the Unified CCE VRU PG service, set the corresponding Unified CVP to maintenance mode. You can stop the Unified
                                             CCE VRU PG only after Unified CVP completes all calls and stops.

#### Unified CCE Enterprise Agent PG graceful shutdown

The Unified CCE Enterprise Agent PG supports graceful shutdown. When you invoke graceful shutdown on the active side of the
                                 Unified CCE Enterprise Agent PG, it gracefully migrates all agents and calls to its peer. When you invoke graceful shutdown
                                 on the standby or idle side, it has no migration activities to perform and just stops the services.

Graceful shutdown on the Unified CCE Enterprise Agent PG also shuts down the corresponding CG Service. A separate request
                                 to gracefully shut down the CG Service is not needed.

The request to gracefully shut down the Unified CCE Enterprise Agent PG is rejected in the following cases:

The PG is running in simplex mode.

Finesse (or another CTI client that supports the Active and Standby CTI Server connection model) does not confirm the maintenance
                                       mode action.

The system is in an overloaded congestion control condition (congestion level is greater than zero).

The PG is Generic, Simplified, or any TDM PG.

##### Limitations

Pending agent state transitions are lost during graceful shutdown. An agent state request made while an agent is handling
                                    a call is considered a pending state. When the call is complete, the agent is moved to the pending state.

If any of the following scenarios occur during the shutdown of the Unified CCE Enterprise Agent PG, the side that has gracefully
                                    shut down stops and its peer restarts in simplex mode. These scenarios impact the calls in progress and agents who are signed
                                    in. Finesse must sign agents back in. Calls and agent states are recovered as during an agent PG failover.

Processes on the side that was set to maintenance mode crash.

Processes on the side that is being activated crash.

There is a network disconnect between the PG and the Central Controller.

There is a network disconnect between the PG and Unified Communications Manager.

There is a private network disconnect between the PG sides.

#### Unified CCE outbound option dialer graceful shutdown

The Unified CCE Outbound Options Dialer supports graceful shutdown. When you invoke graceful shutdown on the Dialer, it stops
                                 reserving agents and dialing new calls while transitioning responsibility to the other side of the dialer. The Dialer that
                                 is shutting down waits until the calls in progress are complete before it shuts itself down.

##### Limitations

When the Dialer gracefully shuts down, scenarios can occur where IVR Campaign calls may not connect the customer to Unified
                                    CVP or the IVR. To avoid these scenarios, disable the IVR Campaigns before gracefully shutting down the Dialer.

#### Unified CCE Media Routing PG graceful shutdown

The Unified CCE Media Routing (MR) PG supports graceful shutdown. For the MR PG peripheral to support graceful shutdown, the
                                 media routing application connecting to the peripheral must use MR Protocol version 5 or later. When you invoke graceful shutdown
                                 on the MR PG, it gracefully migrates all tasks from the active peripheral to the idle peripheral. The MR PG sends a message
                                 to the router to not clear any tasks in queue for that peripheral.

#### Unified CCE VRU PG Graceful Shutdown

The Unified CCE VRU PG does not support graceful shutdown. This PG uses an existing maintenance mode feature from Unified
                                 CVP. Before you stop the Unified CCE VRU PG, put the Unified CVP that the VRU PG connects to into maintenance mode. Unified
                                 CVP stops gracefully after it completes all existing calls. You can then stop the Unified CCE VRU PG from the Unified CCE
                                 Service Control Manager.

### Graceful shutdown caveats

The following caveats apply to Unified CCE graceful shutdown:

Make sure that at least 50 percent plus one of the Unified CCE PGs are connected to the Unified CCE Router. The device majority
                                       feature requires that more than half of the configured Unified CCE PGs are connected to the router for the router to run in
                                       simplex mode. This caveat applies to graceful shutdown of the router, as well as anytime the router must run in simplex mode.

When stopping one side of the router service, database and application gateway lookup may fail. This error condition can be
                                       appropriately handled in the routing script.

If you are using the Outbound API to perform a bulk import of customer records during Logger shutdown, it may not complete.
                                       If you are running overwrite imports, you may need to rerun the import. If you are running append imports, some of the records
                                       may have been imported. You can either import the remaining records or delete the records and reimport them all.

## Graceful Shutdown of Call Server or Reporting Server

As a local administrator, you can use the following procedure to gracefully shut down the Call Server or Reporting Server
                              services from the CLI.

Step 1

Log in to the CVP Call Server box.

Step 2

Go to <CVP-INSTALLED-LOCATION>\Cisco\CVP\bin\ServiceController .

Step 3

Run the service-controller.bat file.

Step 4

Enter the administrator credentials, service name, and IP address details at the prompt:

```
CALLSERVER-IP-ADDRESS: <IP-Address of the Call Server> CALLSERVER-USERNAME: <Username of the Call Server> CALLSERVER-PASSWORD: <Password of the Call Server> SERVICE-NAME: <Choose the Service name which you need to shutdown gracefully(callserver/reportingserver)>
REPORTINGSERVER-IP-ADDRESS: <IP-Address of the REPORTING SERVER>
```

To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running.

If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server.

## Orchestration framework and maintenance mode

The Orchestration framework integrates with a Unified CCE PG using SSH services that are configured on the Unified CCE virtual
                           machines (VMs). You can put the Agent PG VM into maintenance mode by invoking certain commands from the Orchestration framework. For information about SSH configuration, see the Orchestration chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . For information about SSH configuration, see the Orchestration chapter of the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

A PowerShell script on the Unified CCE VM internally runs an executable to coordinate maintenance mode activities on the PG
                           VM. PGs can have different types of services (for example, Agent PG, VRU PG, or MR PG). Some PG services do not support maintenance
                           mode. The services that do support maintenance mode can transfer their context to the other side before shutting down. The
                           executable handles which services to put into maintenance mode and which services to shut down.

There are two main ways to invoke the script from the Orchestration framework.

Start maintenance mode on a PG VM.

Request the status of an ongoing operation or retrieve the final status of the maintenance mode.

The PowerShell script provides the status in the form of a string that contains a high-level code followed by a substatus. For more information about these codes, see the Orchestration chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . For more information about these codes, see the Orchestration chapter of the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

Currently, only Unified CCE PG VMs (VMs that contain only valid PG services) support maintenance mode. If you start maintenance
                                       mode on a VM that is not a PG (such as a router or Rogger) or a VM with a non-PG service installed with the PG services, the
                                       script returns the appropriate error code and does not invoke maintenance mode.

When the executable runs on a PG VM, it follows a default order to shut down the services. This order is based on dependencies
                           that exist between the services. If services must shut down in a different order for a specific customer deployment, you can
                           change the order in the MaintenanceMode.properties file. This file is located in the icm\bin directory.

The following PG services support maintenance mode:

Unified CCE Enterprise Agent PG

Unified CCE Media Routing (MR) PG

Unified CCE Outbound Options Dialer

The script puts the supported services into maintenance mode and then shuts them down.

The following services do not support maintenance mode:

Unified CCE VRU PG

Simplified PG

Generic PG

TDM PG

The script simply shuts down these services.

| Note | Before you stop the Unified CCE VRU PG service, set the corresponding Unified CVP to maintenance mode. You can stop the Unified
                                             CCE VRU PG only after Unified CVP completes all calls and stops. |
|---|---|

| Step 1 | Log in to the CVP Call Server box. |
|---|---|
| Step 2 | Go to <CVP-INSTALLED-LOCATION>\Cisco\CVP\bin\ServiceController . |
| Step 3 | Run the service-controller.bat file. |
| Step 4 | Enter the administrator credentials, service name, and IP address details at the prompt: CALLSERVER-IP-ADDRESS: <IP-Address of the Call Server> CALLSERVER-USERNAME: <Username of the Call Server> CALLSERVER-PASSWORD: <Password of the Call Server> SERVICE-NAME: <Choose the Service name which you need to shutdown gracefully(callserver/reportingserver)>
REPORTINGSERVER-IP-ADDRESS: <IP-Address of the REPORTING SERVER> Note To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. | Note | To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. |
| Note | To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. |

| Note | To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. |
|---|---|

| Note | Currently, only Unified CCE PG VMs (VMs that contain only valid PG services) support maintenance mode. If you start maintenance
                                       mode on a VM that is not a PG (such as a router or Rogger) or a VM with a non-PG service installed with the PG services, the
                                       script returns the appropriate error code and does not invoke maintenance mode. |
|---|---|