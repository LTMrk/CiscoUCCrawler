---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-da078d3dab
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce_m_graceful-shutdown_15_0.html
retrieved_at: 2026-08-21T16:51:11.710573+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Graceful shutdown

## Chapter: Graceful shutdown

# Graceful shutdown

## Graceful Shutdown

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

### Components Enabled for Graceful Shutdown

Before you perform a maintenance activity, you must put the Unified CCE Services that are running on the virtual machine (VM)
                                 into maintenance mode so that its peer can take over processing without impacting contact center operations. Set the following
                                 Unified CCE services to maintenance mode to gracefully shut them down. Stopping these services directly without maintenance
                                 mode impacts the agent and calls in progress.

Unified CCE Enterprise Agent PG

Unified CCE Outbound Option Dialer

Unified CCE Media Routing PG

Unified CCE Router

You can stop the other Unified CCE Services directly using the Unified CCE Service Control Manager tool.

Before you stop the Unified CCE VRU PG service, set the corresponding Unified CVP to maintenance mode. You can stop the Unified
                                             CCE VRU PG only after Unified CVP completes all calls and stops.

#### Unified CCE Enterprise Agent PG Graceful Shutdown

The Unified CCE Enterprise Agent PG supports graceful shutdown. When you invoke graceful shutdown on the active side of the
                                 Unified CCE Enterprise Agent PG, it gracefully migrates all agents and calls to its peer. When you invoke graceful shutdown
                                 on the standby or idle side, it has no migration activities to perform and just stops the services.

To enable graceful shutdown on Unified CCE Agent PG, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B.

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

#### Unified CCE Outbound Option Dialer Graceful Shutdown

The Unified CCE Outbound Options Dialer supports graceful shutdown. When you invoke graceful shutdown on the Dialer, it stops
                                 reserving agents and dialing new calls while transitioning responsibility to the other side of the dialer. The Dialer that
                                 is shutting down waits until the calls in progress are complete before it shuts itself down.

##### Limitations

When the Dialer gracefully shuts down, scenarios can occur where IVR Campaign calls may not connect the customer to Unified
                                    CVP or the IVR. To avoid these scenarios, disable the IVR Campaigns before gracefully shutting down the Dialer.

#### Unified CCE Media Routing PG Graceful Shutdown

The Unified CCE Media Routing (MR) PG supports graceful shutdown. For the MR PG peripheral to support graceful shutdown, the
                                 media routing application connecting to the peripheral must use MR Protocol version 5 or later. When you invoke graceful shutdown
                                 on the MR PG, it gracefully migrates all tasks from the active peripheral to the idle peripheral. The MR PG sends a message
                                 to the router to not clear any tasks in queue for that peripheral.

To enable graceful shutdown on Unified CCE Media Routing PG, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B.

#### Unified CCE VRU PG Graceful Shutdown

The Unified CCE VRU PG does not support graceful shutdown. This PG uses an existing maintenance mode feature from Unified
                                 CVP. Before you stop the Unified CCE VRU PG, put the Unified CVP that the VRU PG connects to into maintenance mode. Unified
                                 CVP stops gracefully after it completes all existing calls. You can then stop the Unified CCE VRU PG from the Unified CCE
                                 Service Control Manager.

To enable graceful shutdown on Unified CCE VRU PG, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B.

#### Unified CCE AW Graceful Shutdown

You can invoke maintenance mode on Unified CCE AW VM using the maintenance mode command to shutdown the Unified CCE distributor
                                 service.

Ensure you stop all the ongoing configuration operations on this Unified CCE AW VM, and then initiate the maintenance mode.
                                 For more information about the maintenance mode command, see the Invoking Maintenance Mode topic.

To enable graceful shutdown on Unified CCE AW, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B.

#### Unified CCE Router Graceful Shutdown

To enable graceful shutdown on Unified CCE Routers, install the 15.0(1) on both Side A and Side B. When you initiate a graceful shutdown, the active Router side verifies that the inactive side
                                 can handle calls and agent states before transferring tasks. Initiating a graceful shutdown on Routers also shuts down all
                                 Logger services on the same box.

For router, maintenance mode can be invoked using CLI command only. For more information, see the Invoking Maintenance Mode section.

The request to gracefully shut down the router is rejected in the following cases:

Either Side A or Side B is running in simplex mode.

When the 15.0(1) version has not been applied to both Side A and Side B. If the 15.0(1) version is missing on either side, the Router node will reject the transition to maintenance mode.

The inactive side lacks device majority after the active side is shut down.

Limitations

If one side of the router service fails, database and application gateway lookups may not work if only accessible from the
                                 affected side.

If you use the Outbound API to perform a bulk import of customer records during a Logger shutdown, the import may not complete.
                                 For overwrite imports, you may need to rerun the import. For append imports, some records may have been imported; you can
                                 either import the remaining records or delete all records and reimport them.

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

## Orchestration Framework and Maintenance Mode

The Orchestration framework integrates with a Unified CCE PG using SSH services that are configured on the Unified CCE virtual
                           machines (VMs). You can put the Agent PG VM into maintenance mode by invoking certain commands from the Orchestration framework. For information about SSH configuration, see the Orchestration chapter of the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

A PowerShell script on the Unified CCE VM internally runs an executable to coordinate maintenance mode activities. PGs can
                           have different types of services (for example, Agent PG, VRU PG, or MR PG). Some PG services do not support maintenance mode.
                           The services that do support maintenance mode can transfer their context to the other side before shutting down. The executable
                           handles which services to put into maintenance mode and which services to shut down.

There are two main ways to invoke the script.

Start maintenance mode on Unified CCE VMs .

Request the status of an ongoing operation or retrieve the final status of the maintenance mode.

The PowerShell script provides the status in the form of a string that contains a high-level code followed by a substatus. For more information about these codes, see the Orchestration chapter of the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

Install the ICM15.0.1_ES202508 patch to initiate the maintenance mode on Router and Rogger from orchestration. However, you cannot initiate Logger and AW
                                       VM from orchestration.

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

## Invoking Maintenance Mode

A PowerShell script on the Unified CCE VM runs an executable to coordinate maintenance mode activities. Use the following
                           command to invoke the maintenance mode:

c:\icm\bin\ExecuteMaintMode.ps1 StartMM InstallType <value>

Only users with administrator role in Powershell can run this script to invoke the maintenance mode.

The possible InstallType values are as follows:

Microsoft Security (MS) patch: 1

Engineering Special (ES) patch: 2

Engineering Special (ES) rollback: 3

Maintenance Release (MR) patch: 4

Maintenance Release (MR) rollback: 5

ISO or Major Release: 6

Use the following command to check the status of maintenance mode:

c:\icm\bin\ExecuteMaintMode.ps1 RequestStatus

When you run the invoke and status of maintenance mode commands on the script, it displays the output as a return code.

For more information about upgrading the Unified CCE VMs, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

### Return Code

The return code contains three parts:

The first part indicates the current system status – normal, in maintenance mode, partially operational, and so on.

The second part indicates which service provides the status.

The third part indicates a service-specific code.

The following table shows the return codes for Unified CCE VMs :

No.

Operation

Return Code

Description

Common Return Codes of Unified CCE VMs : All codes to be prefixed with "MMRequest-".

The return code "500" indicates a proper maintenance mode status achieved through a previous invocation of the script.

Return code "402" indicates that the required services are already shutdown and they're not operational.

Partially in service.

The previous maintenance mode request had left the system in this state as it couldn't successfully move the system fully
                                                into maintenance mode.

Not all services are started properly by an administrator.

PG Specific codes : All codes to be prefixed with "MMRequest-".

Router/Logger Specific codes : All codes to be prefixed with "MMRequest-".

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Note | Before you stop the Unified CCE VRU PG service, set the corresponding Unified CVP to maintenance mode. You can stop the Unified
                                             CCE VRU PG only after Unified CVP completes all calls and stops. |
|---|---|

| Note | To enable graceful shutdown on Unified CCE Agent PG, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B. |
|---|---|

| Note | To enable graceful shutdown on Unified CCE Media Routing PG, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B. |
|---|---|

| Note | To enable graceful shutdown on Unified CCE VRU PG, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B. |
|---|---|

| Note | To enable graceful shutdown on Unified CCE AW, install the ICM 15.0.1_ES202607 or later cumulative installer on both Side A and Side B. |
|---|---|

| Note | For router, maintenance mode can be invoked using CLI command only. For more information, see the Invoking Maintenance Mode section. |
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

| Note | Install the ICM15.0.1_ES202508 patch to initiate the maintenance mode on Router and Rogger from orchestration. However, you cannot initiate Logger and AW
                                       VM from orchestration. |
|---|---|

| Note | Only users with administrator role in Powershell can run this script to invoke the maintenance mode. |
|---|---|

| Note | For more information about upgrading the Unified CCE VMs, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
|---|---|

| No. | Operation | Return Code | Description |
|---|---|---|---|
| Common Return Codes of Unified CCE VMs : All codes to be prefixed with "MMRequest-". |
| 1 | Requesting for maintenance mode | "100" | Accepted. |
| 2 | Requesting for maintenance mode, Querying for status | "500" | System is already in maintenance mode. |
| 3 | Requesting for maintenance mode, Querying for status | "402" | The return code "500" indicates a proper maintenance mode status achieved through a previous invocation of the script. Return code "402" indicates that the required services are already shutdown and they're not operational. |
| 4 | Querying for status | "200" | Normal, System Operational |
| 5 | Querying for status | "300" | Maintenance mode request in-progress |
| 6 | Querying for status | "401" | Partially in service. The previous maintenance mode request had left the system in this state as it couldn't successfully move the system fully
                                                into maintenance mode. Not all services are started properly by an administrator. |
| 7 | Querying for status, Requesting for maintenance mode | "400" | Rejected |
| 8 | Querying for status | "403" | Maintenance mode request has been successfully cancelled by the administrator. |
| PG Specific codes : All codes to be prefixed with "MMRequest-". |
| 1 | Querying status | "300-AGENTPG-101" | Maintenance mode request is in-progress, Agent PG MM attempted. |
| 2 | Querying status | "300-AGENTPG-300" | Maintenance mode request is in-progress, Agent PG MM in-progress. |
| 3 | Querying status | "401-AGENTPG-400" | Maintenance mode request failed at Agent PG because the request was rejected. |
| 4 | Querying status | "300-DIALER-101" | Maintenance mode request is in-progress. Dialer MM attempted. |
| 5 | Querying status | "300-DIALER-300" | Maintenance mode request is in-progress. Dialer MM in-progress. |
| 6 | Querying status | "401-DIALER-400" | Maintenance mode request failed at Dialer because the request was rejected. |
| 7 | Querying status | "300-MRPG-101" | Maintenance mode request is in-progress, MR PG MM attempted. |
| 8 | Querying status | "300-MRPG-300" | Maintenance mode request in-progress, MR PG MM in-progress. |
| 9 | Querying status | "401-MRPG-400" | Maintenance mode request failed at MR PG because the request was rejected. |
| 10 | Querying status | "401-SCERROR-400" | Maintenance mode failed because service control rejected the request. |
| 11 | Querying status | "200" | Normal system operation |
| 12 | Querying status | "500" | System in maintenance mode |
| 13 | Querying status | "400-REGREADERROR-400" | Maintenance mode script is not able to read required registry. |
| 14 | Querying status | 400-NOVALIDCOMP-400 | Maintenance mode scripts are run on a VM which has no PG service installed. |
| 15 | Querying status | 400-NODISCRETECOMP-400 | Maintenance mode scripts are run on a VM which has at least one PG service installed but there are other services that don't
                                       support maintenance mode. |
| Router/Logger Specific codes : All codes to be prefixed with "MMRequest-". |
| 1 | Querying status | "300-ROUTER-101" | Maintenance mode request is in-progress, Router MM attempted. |
| 2 | Querying status | "300-LOGGER-101" | Maintenance mode request is in-progress, Logger MM attempted. |
| 3 | Querying status | "300-ROUTER-300" | Maintenance mode request in-progress, Router MM is in-progress. |
| 4 | Querying status | "300-LOGGER-300" | Maintenance mode request in-progress, Logger MM is in-progress. |
| 5 | Querying status | "401-ROUTER-400" | Maintenance mode request failed at Router because the request was rejected. |
| 6 | Querying status | "401-LOGGER-400" | Maintenance mode request failed at Logger because the request was rejected. |
| 7 | Querying status | "401-SCERROR-400" | Maintenance mode failed because service control rejected the request. |
| 8 | Querying status | "401-SCERROR-401" | Maintenance mode failed because service control rejected the request. |
| 9 | Querying status | "401-ROUTER-402" | Maintenance mode service Router already shut down. |
| 10 | Querying status | "200" | Normal system operation |
| 11 | Querying status | "500" | System in maintenance mode |
| 12 | Querying status | "400-REGREADERROR-400" | Maintenance mode script is not able to read the required registry. |
| 13 | Querying status | 400-NOVALIDCOMP-400 | Maintenance mode scripts are run on a VM which has no Router service installed. |
| 14 | Querying status | 400-NODISCRETECOMP-400 | Maintenance mode scripts are run on a VM which has Router service installed but there are other services that don't support
                                       maintenance mode. |