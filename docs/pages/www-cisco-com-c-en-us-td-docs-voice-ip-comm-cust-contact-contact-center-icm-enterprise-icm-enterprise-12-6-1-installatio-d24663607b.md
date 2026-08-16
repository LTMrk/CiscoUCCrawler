---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-d24663607b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_cti-os-system-manager-guide12-6-1/ucce_b_cti-os-system-manager-guide12-5_chapter_01000.html
retrieved_at: 2026-08-16T20:04:29.610869+00:00
---

CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

# CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

Updated: May 12, 2021

Chapter: CTI OS Configuration

## Chapter: CTI OS Configuration

# CTI OS Configuration

## Use Windows Registry Editor

CTI OS
                              		  configuration is handled through the Windows Registry Editor. Using the Editor,
                              		  you can add or change registry values.

Except where
                                          			 otherwise indicated, the CTI OS registry keys discussed in this chapter are
                                          			 local and start at the [ HKEY_LOCAL_MACHINE\SOFTWARE\ Cisco Systems,
                                             				Inc.\CTIOS\< CTIOS_CTIOSInstanceName >\< CTIOSServerName > ] path.

CTI OS Server installation initializes a configuration that is stored in the Windows
                              				System Registry database. You can access and edit this configuration is through the
                              				Windows Registry Editor (regedit.exe).

To add a
                              		  key or registry value under an existing key, perform the following steps.

Step 1

Highlight the
                                       			 existing key in the left panel.

Step 2

Position the
                                       			 cursor in the right panel and click.

A popup menu
                                          				appears.

Step 3

From the popup
                                       			 menu, select Key , String
                                          				Value , Binary
                                          				Value , or DWORD value.

If you select Key , a placeholder for the key you want to add
                                          				appears highlighted in the left panel. For other items, a placeholder for the
                                          				item you want to add appears highlighted in the right panel.

Step 4

Right-click the
                                       			 highlighted item. A popup menu appears.

To name the
                                             				  item, select Rename from the popup menu; then type the new name
                                             				  for the item.

To set the
                                             				  value data for String , Binary , and DWORD values, select Modify . A dialog box appears. Enter the value data
                                             				  following the Value Data prompt.

To edit an existing
                              		  key or registry value, highlight the key or value and right-click it. Select Modify , Delete , or Rename from the popup menu and proceed.

After you change the registry, restart the CTI OS processes before the new
                                          			 setting can take effect.

### Silent Monitor Type
                           	 Configuration for CTI OS

You can
                                 		  configure the CTI OS can be configured to use either the Unified CM-based
                                 		  silent monitor or the CTI OS-based silent monitor. You accomplish this by
                                 		  setting the following field in the CTI OS registry:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems
                                    			 Inc.\CTIOS\< CTIOS
                                       				InstanceName >\< CTIOSServerName >\EnterpriseDesktopSettings\All
                                    			 Desktops\IPCCSilentMonitor\Name\Settings\CCMBasedSilentMonitor

This field
                                 		  is a DWORD and if present and set to "1" , Unified
                                 		  CM-based silent monitor is used.

CTI
                                 		  OS-based silent monitor is used if this field is not present or if it is
                                 		  present and set to "0" .

You can also run
                                             			 the setup program to reconfigure the CTI OS-based silent monitor.

If the server
                                             			 setup program is not run, the CCMBasedSilentMonitor field is not present. As a
                                             			 result, CTI OS-based silent monitor is used.

## Virtual Desktop Infrastructure

Virtual Desktop Infrastructure (VDI) is a server-centric computing model. It is designed to help you to host and centrally
                              manage desktop virtual machines in the data center, while providing a full PC desktop experience.

The VMware View portfolio of products VDI lets IT run virtual desktops in the data center while giving you a single view of
                              all your applications and data in a familiar, personalized environment on any device at any location. VDI provides greater
                              flexibility, reliability, efficiency, and security managing desktops and applications from the datacenter.

### CTI OS Desktop Installations on VDI Agent Desktops

#### Prerequisites

Complete functional VDI deployment as per the VDI requirements. For more information, see http://www.vmware.com/products/view/.

#### Install CTI OS Desktop on VDI Agent

Step 1

On any VDI agent desktop, run the CTI OS client installer and
                                             			 configure the desktop.  For more information on the
                                             			 deployment, limitations, and supported features of CTI OS desktops on VDI, see CTI OS System Manager Guide for Cisco Unified ICM .

Step 2

When the installation is complete, launch the CTI OS desktop and
                                             			 verify basic functionality by logging in an agent, changing agent states, or
                                             			 making calls.

Step 3

After you complete the testing, follow the same steps on the other
                                             			 VDI agent desktops.

#### Notes and Restrictions

##### Silent Monitoring

CTI OS-based silent monitoring is not supported due to physical limitations. For CTI OS-based silent monitoring, you must
                                       connect the agent machine to the network via the phone hard-set. This cannot be achieved with a Virtual Machine, such as when
                                       using VDI.

##### ThinApp

For
                                    		more information about ThinApp, see http://www.vmware.com/products/thinapp .

## CTI Driver Key

The CTI Driver key includes registry settings required for
                              		  CTI Server connection. The CTI Driver key contains one key, the Config key. The
                              		  following table describes the CtiDriver/Config key registry values.

Registry Value Name

Value Type

Description

Default

ClientID

String Value

The identifier of the CTI Client. This appears in the CTI
                                          					 Server log file to help identify which session the CTI OS Server is connected
                                          					 on.

CTIOSServer

ClientPassword

String Value

The password of the CTI Client. This appears in the CTI
                                          					 Server log file to help identify which session the CTI OS Server is connected
                                          					 on.

CTIOSServer

ClientSignature

String Value

The signature of the CTI Client. This appears in the CTI
                                          					 Server log file to help identify which session the CTI OS Server is connected
                                          					 on.

CTIOSServer

SideAHost

String Value

The CTI Server (sideA) IP address or hostname to which the CTI
                                          					 OS Server connects.

Host specified during CTI Server installation.

SideAPort

DWORD Value

The CTI Server (sideA) IP port to which the CTI OS Server
                                          					 connects.

Port specified during CTI Server installation.

SideBHost

String Value

The CTI Server (sideB) IP address or hostname to which the CTI
                                          					 OS Server connects.

Host specified during CTI Server installation.

SideBPort

DWORD Value

The CTI Server (sideB) IP port to which the CTI OS Server
                                          					 connects.

Port specified during CTI Server installation.

Heartbeat Interval

DWORD Value

The interval (in seconds) at which HEARTBEAT_REQ messages are
                                          					 sent to the CTI Server.

5

ServicesMask

DWORD Value

The services requested from the CTI Server and provides the
                                          					 functionality that the MinimizeAgentStateEvents registry value used to provide.

To suppress multiple state events add the
                                          					 bit:CTI_SERVICE_IGNORE _DUPLICATE_AGENT _STATES = 0x00100000

to the following registry key:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\Ctios\
                                          					 CTIOS_<ctios_instance>\CTIOS1\ CtiDriver\Config

Example:

Change

"ServicesMask" =dword:000c0016

to:

"ServicesMask" =dword:001c0016

0x00000296 (52)(default)

CallMsgMask

DWORD Value

The unsolicited call events requested from the CTI Server.

0x00ffffff (16777215)

AgentStateMask

DWORD Value

The agent states requested from the CTI Server.

0x000003ff (1023)

ProtocolVersion

DWORD Value

The highest protocol version to use when connecting to the CTI
                                          					 Server. The highest common denominator is used when establishing the CTI
                                          					 Session.

15

IdleTimeout

DWORD Value

The session inactivity timeout (in seconds). The CTI Server
                                          					 disconnects clients after this time threshold has elapsed without other socket
                                          					 messages.

0x7fffffff (2147483647)

MemoryPoolSize

DWORD Value

Size of the memory pool, in bytes.

0x00000064 (100)

## EMS Tracing Values

The registry keys located at
                              		  [ HKEY_LOCAL_MACHINE\SOFTWARE\Cisco
                                 			 Systems,Inc.\ICM\< customer_instance_name >\< CTIOSComponent
                                    				Name >\EMS\CurrentVersion\Library\Processes\ctios ]
                              		  define the settings for Event Management System (EMS) tracing. The following
                              		  table lists the registry values for these keys.

EMSDisplayToScreen

DWORD Value

If set to 1, EMS routines attempt to write formatted messages
                                          					 to standard output.

0

EMSAllLogFilesMax

DWORD Value

The maximum total number of bytes that the EMS library writes
                                          					 to all local log files.

2000000000 (2 billion decimal)

EMSBreakOnExit

DWORD Value

If set to 1, EMS exit routines invoke the Debugger.

0

EMSBreakOnInit

DWORD Value

If set to 1, EMS initialization routines invoke the Debugger.

0

EMSDebugBreak

DWORD Value

If set to 1, EMS failure routines invoke the Debugger before
                                          					 exiting the process.

1

EMSLogFileCountMax

DWORD Value

The maximum number of log files that the EMS library writes.

10000 (decimal)

EMSLogFileLocation

String Value

The directory where the EMS library creates local log files.

Default directory specified at installation.

EMSLogFileMax

DWORD Value

The maximum number of bytes that the EMS library writes to a
                                          					 single local log file.

30000000 (30 million decimal)

EMSNTEventLogLevel

DWORD Value

The minimum severity event that EMS logs in the Application
                                          					 Event Log.

2

EMSTraceMask

DWORD Value

A bitmask that specifies the levels of EMS tracing that are
                                          					 enabled.

395791 (decimal)

EMSUserData

DWORD Value

Placeholder for arbitrary binary user data.

EMSForwardLevel

DWORD Value

The minimum severity event that EMS forwards to the Unified
                                          					 ICM central controller.

0

## Server Registry Key

The Server registry key contains CTI OS Server related configuration information. It contains the following subkeys:

Agent

CallObject

Connections

Device

Peers

Peripherals

SkillGroup

SilentMonitor

Supervisor

ThreadPoolSize

TimerService

### Agent Registry
                           	 Key

The Agent
                                 		  key contains agent related configuration information. The following table lists
                                 		  the registry values for the Agent key.

Registry
                                             					 Value Name

Value Type

Description

Default

AgentChatLevel

string

Defines the
                                             					 call center personnel with whom an agent is permitted to chat. You must set
                                             					 this to one of the values listed in the "AgentChatLevel values" table below.

TeamSupervisors

EnableWrapupDialog

DWORD Value

When enabled
                                             					 (1), a Wrapup dialog box pops up at the end of the call. A value of 0 disables
                                             					 this feature.

1

forceLogoutOnSessionClose

DWORD Value

Set to "1" to
                                             					 turn on the feature to force logout an agent when their session is ended by the
                                             					 agent closing the window without properly logging out.

You must
                                                         						manually enter this value into the registry. If the value is not entered into
                                                         						the registry, the effect is the same as having it set to its default (0).

0

forceLogoutOn SessionCloseReason(Optional unless logout reason
                                             					 is required.)

DWORD Value

Indicates
                                             					 the reason code to be used by the CTI OS Server when the agent is forced to log
                                             					 out.

This need not be defined in the registry when the default value is sufficient. By setting this to a specific reason code,
                                             you can easily determine if an agent is logged out by the CTI OS Server or if it's a typical agent log out.

You must
                                                         						set this to a non-zero value if an idle reason code reason is required. Refer
                                                         						to "Unified
                                                            						  ICM Agent Desk Settings" to determine if the idle reason code is required.

You must
                                                         						manually enter this value into the registry.

0

forceNotReadyOn SessionCloseReason(Optional unless idle reason
                                             					 is required.)

Indicates
                                             					 the reason code to be used by the CTI OS Server when the agent is forced to the
                                             					 Not Ready state before being forced to log out.

This need not be defined in the registry when the default value is sufficient. By setting this to a specific reason code,
                                             you can easily determine if an agent is logged out by the CTI OS Server or if it's a typical agent log out.

You must
                                                         						set this to a non-zero value if an idle reason code reason is required. For
                                                         						more information about the required idle reason code, see "Unified
                                                            						  ICM Agent Desk Settings" .

You must
                                                         						manually enter this value into the registry.

0

LogoutReasonRequired

DWORD Value

On all
                                             					 switches except UCCE, when enabled (1) a Logout Reason Code dialog box pops up
                                             					 when changing state to Logout. On all switches, a value of 0 disables this
                                             					 feature.

0

NotReadyReasonRequired

DWORD Value

On all
                                             					 switches except UCCE, when enabled (1) a Not Ready Reason Code dialog box pops
                                             					 up when changing state to NotReady. On all switches, a value of 0 disables this
                                             					 feature.

0

PollForAgentStatsAtEnd Call

DWORD
                                             					 Value

Controls
                                             					 when agent statistics are sent from CTI OS Server to CTI OS clients. A value of
                                             					 0 means that agent statistics are sent at a regular interval (specified in
                                             					 PollingIntervalSec). A value of 1 means that agent statistics are sent only
                                             					 when a call ends.

Changing
                                                         						the value of PollForAgentStatsAtEndCall may degrade performance.

1

PollingIntervalSec

DWORD
                                             					 Value

The agent
                                             					 statistics polling interval, in seconds.

15

WrapupDataRequired

DWORD
                                             					 Value

When
                                             					 enabled (1), wrapup data is mandatory. When disabled (0), wrapup data is not
                                             					 required. Not applicable to UCCE agents.

0

Value

Meaning

Disabled

All agent
                                             					 chat disabled.

PrimarySupervisor

Agents can
                                             					 chat only with primary supervisor of their team.

TeamSupervisors

Agents can
                                             					 chat with the primary or secondary supervisor of their team.

Team

Agents can
                                             					 chat with anyone in team.

Unrestricted

Agents can
                                             					 chat with anyone on the same peripheral.

The
                                 		  Agent key also contains the following subkeys:

- ReasonCodes

- WrapupStrings

#### ReasonCodes Registry Key

The ReasonCodes key is a site-specific key that defines the
                                    		  reason codes the CTI OS Agent Desktop uses. For each reason code, a string is
                                    		  mapped to an unsigned short value. The CTI OS Agent Desktop displays the string
                                    		  and sends the appropriate value to the CTI Server, which in turn passes the
                                    		  value along to the ACD.

The ReasonCodes key contains two subkeys:

Logout . This key defines the reason codes that appear on
                                          				the Select Reason: Logout screen when an agent logs out. Immediately following
                                          				CTI OS Server installation, the Logout registry key contains four values that
                                          				serve as placeholders for Logout reason codes (see following table).

Registry Value Name

Value Type

Description

Insert logout reason code 1 here

DWORD Value

Placeholder for first Logout reason code.

Insert logout reason code 2 here

DWORD Value

Placeholder for second Logout reason code.

Insert logout reason code 3 here

DWORD Value

Placeholder for third Logout reason code.

Insert logout reason code 4 here

DWORD Value

Placeholder for fourth Logout reason code.

To define the text that appears for each Logout reason code in the
                                          		  Select Reason dialog box, set the value data associated with the reason code to
                                          		  the text you want to appear for that reason code. You may also add additional
                                          		  reason code entries as needed.

NotReady . This key defines the reason codes that appear in
                                          			 the Select Reason: NotReady dialog box when an agent goes to NotReady state. As
                                          			 with the Logout key, the NotReady key initially contains four placeholder DWORD
                                          			 values that you can edit to define the reason codes in the Select Reason:
                                          			 NotReady dialog box.

The maximum length permitted for a reason code is 42 characters.

#### WrapupStrings Registry Key

The WrapupStrings key defines the predefined wrapup text
                                    		  strings that appear in the softphone Wrapup dialog box. The WrapupStrings key
                                    		  contains a subkey, Incoming, that defines the wrapup text for incoming calls.
                                    		  Immediately following CTI OS Server installation, the Incoming key contains the
                                    		  registry values listed in the following table.

Registry Value Name

Value Type

Description

String0

String Value

Placeholder for first wrapup text string.

String1

String Value

Placeholder for second wrapup text string.

String2

String Value

Placeholder for third wrapup text string.

String3

String Value

Placeholder for fourth wrapup text string.

To define the text that appears for each wrapup text string
                                    		  in the WrapUp dialog box, set the value data associated with the reason code to
                                    		  the text you want to appear for that wrapup string. You may also add additional
                                    		  wrapup string entries as desired.

There are no CTI OS registry keys for defining text for outgoing
                                                			 wrapup strings. The Unified ICM does not save any wrapup data for outgoing
                                                			 calls, so you need not define outgoing wrapup strings. This is applicable to
                                                			 transfer and conference initiated calls also. (Both transfer and conference
                                                			 calls are treated as outgoing calls.)

### CallObject Registry
                           	 Key

The
                                 		  CallObject key defines the values pertaining to call objects. The following
                                 		  table defines the CallObject key registry values.

Registry
                                             					 Value Name

Value Type

Description

Default

AgentPreCallEvent Timeout

DWORD Value

Length of
                                             					 time, in seconds, within which an AGENT_PRE_ CALL_EVENT must be followed by a
                                             					 BEGIN_CALL_ EVENT or the call object is deleted.

30

IPCCConference_ SupportsMultipleControllers

DWORD Value

When set to
                                             					 1, allows all parties of a Conference to add new parties to the conference as
                                             					 supported by Unified CM. If running against an earlier version of Unified CM,
                                             					 this registry value must be set to 0. If this value is not set to 0 when running against an earlier
                                             					 version of Unified CM, and a non-controller Conference party tries to make a
                                             					 Consult Call for a Conference, the party receives a Control Failure.

1

MinimizeEventArgs

DWORD Value

When set to
                                             					 1 (optimal), minimizes the amount of nonessential call object parameters sent
                                             					 to the client.

1

TrashCollectionInterval Sec

DWORD value

Controls how
                                             					 often (in seconds) the trash collector activates and removes any stale objects
                                             					 from memory. A value of 0 disables the trash collector.

7200

### Connections Registry
                           	 Key

The
                                 		  Connections key defines the values for client connections to the CTI OS Server.
                                 		  The following table defines the Connections key registry values.

Registry
                                             					 Value Name

Value Type

Description

Default

ClientPoolInitialSize

DWORD Value

The number
                                             					 of Client objects to pre-create.

Caution

Leave this
                                                         						registry entry set to its default value.

1500

ClientPoolMinSize

DWORD Value

The minimum
                                             					 number of Client objects in the pool to trigger gstrowing the pool.

Caution

Leave this
                                                         						registry entry set to its default value.

50

ClientPoolIncrement

DWORD Value

The number
                                             					 of Client objects to create when the pool must be gstrown.

Caution

Leave this
                                                         						registry entry set to its default value.

50

HeartbeatIntervalMs

DWORD Value

The number
                                             					 of milliseconds between heartbeats from the server to its clients.

60000

HeartbeatRetrys

DWORD Value

The number
                                             					 of missed heartbeats before a connection is closed for unresponsiveness.

5

ListenPort

DWORD Value

The TCP/IP
                                             					 port on which the CTI OS Server listens for incoming client connections.

Port
                                             					 specified during CTI OS Server setup.

MaxMonitorMode Connections

DWORD Value

This
                                             					 registry entry controls the number of monitor mode connections connected to a
                                             					 CTI OS Server.

7

The
                                 		  heartbeating mechanism uses the HeartbeatIntervalMs and HeartbeatRetrys values
                                 		  together to determine when a connection is stale and must be closed. The
                                 		  interval serves as a timeout and the retries is the number of attempts that
                                 		  have timed out before closing the socket.

Example
                                 		  with an interval of 5 seconds and three retries:

- After 5 seconds Total time),
                                    			 if the server does not receive a response from the client, it sends a heartbeat
                                    			 request and increments the retry count to 1.

- After another 5 seconds, if
                                    			 the server does not receive a response from the client, it sends a heartbeat
                                    			 request and increments the retry count to 2.

- After another 5 seconds, if
                                    			 the server does not receive a response from the client, it sends a heartbeat
                                    			 request and increments the retry count to 3.

- After another 5 seconds, if
                                    			 the server does not receive a response from the client, the connection is
                                    			 reported failed and the socket is closed.

To disable
                                 		  heartbeating, set the HeartbeatIntervalMs value to 0.

A Retry
                                 		  value of 0 causes the connection to time out after the interval without sending
                                 		  any heartbeat.

### Device Registry Key

The Device registry key contains one value, SnapshotDelaySec. This is a reserved value that must not be changed.

### Peers Registry Key

The Peers registry key informs a CTI OS Server about other
                                 		  CTI OS Servers. This allows CTI OS Servers to make direct connections with one
                                 		  another for the purposes of routing internal messages. On startup,
                                 		  CTIOSServerNode reads this key and opens client connections to all peer
                                 		  servers.

You can define two CTI OS Servers as peer servers only if they are
                                             			 connected to the same CTI Server or CTI Server pair. You cannot define two CTI
                                             			 OS Servers as peer servers if they are connected to CTI Servers that reside on
                                             			 different PGs.

The Peers key contains the values listed in following table.

Registry Value Name

Value Type

Description

Default

Heartbeat IntervalMs

DWORD Value

Number of milliseconds between heartbeats for client
                                             					 connection to peer servers.

5000

HeartbeatRetrys

DWORD Value

Number of retry attempts before a connection to a peer server
                                             					 is determined to be down.

3

In addition, there must be a subkey for each peer server to
                                 		  which the current server connects. The key name is the hostname or IP address
                                 		  of the peer server; for example:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                    			 Inc.\CTIOS\< CTIOSInstanceName >\< CTIOSServerName >\Server\Peers\ DallasCTIOS .

Each such subkey must contain the registry value listed in the
                                 		  following table.

Registry Value Name

Value Type

Description

Port

DWORD Value

The number of the TCP/IP port on which the peer server is
                                             					 listening for the client connection.

### Peripherals Registry Key

The Peripherals key stores the maps of valid PeripheralID
                                 		  and Peripheral Types. On CTI OS System startup, these mappings are read into a
                                 		  map, which creates the appropriate peripheral-type objects on the server.

This information must correspond to the Unified UCCE
                                 		  database Peripheral table Peripheral.PeripheralID and Peripheral.ClientType.
                                 		  While the values in ClientType are not equal to the PeripheralTypes, there is a
                                 		  one-to-one relationship between ClientTypes and PeripheralTypes.

The symbol PERIPHERAL_LOGICAL_NAME can be any logical name
                                 		  that uniquely identifies a Peripheral, such as "Phoenix ACD 1." This is equivalent to the
                                 		  Peripheral.EnterpriseName logical name in the Unified UCCE database. There must
                                 		  be one entry for each valid Peripheral at this site.

The following lists the Peripherals key registry values.

Registry Value Name

Value Type

Description

PeripheralID

DWORD Value

The PeripheralID configured in the Unified UCCE database for
                                             					 this Peripheral.

PeripheralType

DWORD Value

The PeripheralType corresponding to this PeripheralID.

Examples:

```
[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\Ctios\<CTIOS 
InstanceName>\<CTIOSServerName>\Server\Peripherals\G3 ACD]
"PeripheralID"=dword:00001388
"PeripheralType"=dword:00000005

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\Ctios\<CTIOS 
InstanceName>\<CTIOSServerName>\Server\Peripherals\Aspect ACD]
"PeripheralID"=dword:00001390
"PeripheralType"=dword:00000001
```

### SkillGroup Registry Key

The SkillGroup key defines skill group configuration values.
                                 		  The following table lists the SkillGroup key registry values.

Registry Value Name

Value Type

Description

Default

PollingInterval Sec

DWORD Value

The SkillGroup statistics polling interval, in seconds.

10

### Supervisor Registry Key

The Supervisor key contains supervisor related configuration
                                 		  information. The following table lists the registry values for the Supervisor
                                 		  key.

Registry Value Name

Value Type

Description

Default

Supervisor ChatLevel

String Value

Defines the call center personnel with whom a supervisor is
                                             					 permitted to chat. This must be set to one of the values listed in the table
                                             					 below.

Unrestricted

Value

Meaning

Disabled

All supervisor chat disabled.

Team

Supervisors can chat with anyone in their primary team.

Unrestricted

Supervisors can chat with anyone on the same peripheral.

### ThreadPoolSize
                           	 Registry Key

ThreadPoolSize is the number of threads in the IO completion
                                 		  port pool.

The
                                 		  ThreadPoolSize registry value is found under the following registry key:

HKLM\Software\Cisco
                                    			 Systems.Inc.\ctios\CTIOS_< instancename >\CTIOS1\Server\ThreadPool

Registry
                                             						Value Name

Value Type

Description

Default

ThreadPoolSize

DWORD
                                             						Value

If set to
                                             						<= 0, then the number of threads in the pool are calculated using the
                                             						following formula: number of CPU's +2.

Maximum
                                             						threads allowed are 32.

0 for all
                                             						peripheral types except Avaya where the default value is 14.

Balancing threads
                                             			 against overall performance is not a trivial task. If the ThreadPoolSize value
                                             			 is changed, follow up with overall performance monitoring to see whether CTI OS
                                             			 Server performance is affected.

### TimerService Registry Key

The TimerService key specifies configuration parameters for
                                 		  the CTI OS Server's internal TimerService. The following table lists the
                                 		  registry values for the TimerService key.

Registry Value Name

Value Type

Description

Default

ResolutionMSec

DWORD Value

The interval at which the TimerService services queued
                                             					 requests, expressed in milliseconds.

500

## MainScreen Registry Key

The MainScreen key, located at
                              		  [ HKEY_LOCAL_MACHINE\SOFTWARE\ Cisco Systems,Inc.\CTIOS\
                                 			 < CTIOSInstanceName >\< CTIOSServerName >\
                                 			 EnterpriseDesktopSettings\All Desktops\ ScreenPreferences\
                                 			 Name\MainScreen ], includes registry values that define the behavior
                              		  of softphone windows and icons in response to a BeginCallEvent. The following
                              		  table lists the registry values for the MainScreen key.

Registry Value Name

Value Type

Description

Default

BringToFrontOnCall

DWORD Value

When enabled (1), the softphone window is raised above all
                                          					 other windows when a BeginCallEvent occurs.

1

FlashOnCall

DWORD Value

When enabled (1), the softphone icon on the taskbar flashes
                                          					 when a BeginCallEvent occurs.

0

RecordingEnabled

DWORD Value

Controls whether the Record button is enabled on the Agent and
                                          					 Supervisor Softphones (0 = disabled, 1 = enabled).

0

AgentStatistics IntervalSec

DWORD Value

Controls how often (in seconds) the Agent and Supervisor
                                          					 Softphones update time-in-state agent statistics.

0xF

## Unified CCE Silent Monitor
                        	 Configuration

The
                              		  IPCCSilentMonitor key contains silent monitor configuration information. The
                              		  IPCCSilentMonitor key contains one subkey, named Settings.

The
                              		  IPCCSilentMonitor configuration settings are declared in the registry of each
                              		  server on the following location:

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems Inc.\CTIOS\<CTIOS
                                 			 InstanceName>\<CTIOSServerName>\EnterpriseDesktopSettings\All
                                 			 Desktops\IPCCSilentMonitor\Name\Settings]

The
                              		  Settings subkey contains the parameters used by the silent monitor subsystem to
                              		  establish a monitoring session between a supervisor and a monitored agent. The
                              		  values are listed in the following table.

Registry
                                          					 Value Name

Value Type

Description

Default

HeartbeatInterval

DWORD value

The time in
                                          					 seconds between consecutive heartbeats.

5

HeartbeatTimeout

DWORD value

The amount
                                          					 of time in seconds that must elapse without receiving data before a disconnect
                                          					 is signaled.

15

MediaTerminationPort

DWORD value

Reserved.
                                          					 This is the TCP/IP port that the silent monitor subsystem uses to render
                                          					 monitored audio.

4000

MonitoringIPPort

DWORD value

This is the
                                          					 TCP/IP port on the monitoring application to which the monitored application
                                          					 sends monitored audio.

39200

StopSMNonACDCall

DWORD value

This stops
                                          					 silent monitoring of Non-ACD calls. When enabled (1) in Unified CM-based silent
                                          					 monitoring, the supervisor's monitor button is disabled. When enabled in
                                          					 desktop-based silent monitoring, the supervisor's monitor button is enabled but
                                          					 the supervisor can only hear ACD calls.

You must
                                                      						manually enter this value into the registry. If the value has not been entered
                                                      						into the registry, the effect is the same as having it set to its default (0).

0

## ConnectionProfiles
                        	 Registry Key

The
                              		  ConnectionProfiles key contains an organized list of the connection information
                              		  of all configured CTI OS Servers present in the corporate network that you can
                              		  access by a client application. The connection profiles are defined in the
                              		  registry of each server at the following location:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems
                                 			 Inc.\CtiOs\< CTIOS
                                    				InstanceName >\< CTIOSServerName >\ EnterpriseDesktopSettings\All
                                 			 Desktops\Login\ConnectionProfiles\Name\< CtiOsProfileName >

To create
                              		  a profile for a given server, you must define a subkey under
                              		  ConnectionProfiles\Name with the following format:

```
[HKEY_LOCAL_MACHINE\Software\…\ConnectionProfiles\Name\ CtiOsProfileName ]
"PeripheralID"=dword:5000
"Heartbeat"=dword:00000000
"MaxHeartbeats"=dword:00000005
"CtiOsA"="HostName_A"
"CtiOsB"="HostName_B"
"PortA"=dword:0000a42c
"PortB"=dword:0000a42c
"AutoLogin"=dword:00000001
“ShowFieldBitMask”=dword:00000023
"WarnIfAlreadyLoggedIn"=dword:00000001
"RejectIfAlreadyLoggedIn"=dword:00000000
"DisableSkillGroupStatistics"=dword:00000001
"DisableAgentStatistics"=dword:00000001
"UCCESilentMonitorEnabled"=dword:0x00000001
"WarnIfSilentMonitored"=0x00000000
```

The
                              		  following table describes the required ConnectionProfiles key registry values.

SubKey/Value

Description

CtiOsProfileName

The name
                                          					 given to the profile. This string appears on the Login Dialog when a user is
                                          					 about to log in using the CTI OS Agent State Control.

PeripheralID

The numeric
                                          					 value of the peripheral to which the CTI OS Server connects.

Heartbeat

Time
                                          					 interval between heartbeat messages between the client and CTI OS Server.

MaxHeartbeats

Maximum
                                          					 number of heartbeats that can be missed by the CTI OS Client Session before
                                          					 failover occurs.

CtiOsA

DNS name of
                                          					 IP Address of the primary CTI OS Server to which a client application can
                                          					 connect.

CtiOsB

DNS name of
                                          					 IP Address of the secondary CTI OS Server to which a client application can
                                          					 connect.

PortA

TCP/IP port
                                          					 number assigned to the primary server.

PortB

TCP/IP port
                                          					 number assigned to the secondary server.

AutoLogin

Indicates if
                                          					 the client must automatically log in an agent or supervisor after it recovers
                                          					 from a system failure. For all peripherals other than UCCE you must set this
                                          					 field to 0x00000000. For UCCE, set this field to 0x00000001.

ShowFieldBit
                                          					 Mask

WarnIfAlready LoggedIn

Indicates
                                          					 whether to display a warning but still permit login if an agent who is already
                                          					 logged in attempts to log in again. A value of 1 (default) enables the warning;
                                          					 a value of 0 disables the warning. This value is relevant only if
                                          					 RejectIfAlreadyLoggedIn is 0.

RejectIfAlready LoggedIn

Indicates
                                          					 whether or not to permit an agent who is already logged in to log in again. A
                                          					 value of 0 (default) permits an agent to log in again. A value of 1 prohibits
                                          					 an agent from logging in again.

DisableSkillGroup Statistics

Indicates
                                          					 whether skill group statistics are enabled for the agent using this connection
                                          					 profile. A value of 1 disables statistics. If this value is 0 (default) or not
                                          					 present, skill group statistics are enabled for this agent.

DisableAgent
                                          					 Statistics

Indicates
                                          					 whether agent statistics are enabled for the agent using this connection
                                          					 profile. A value of 1 disables statistics. If this value is 0 (default) or not
                                          					 present, statistics are enabled for this agent.

IPCCSilent
                                          					 MonitorEnabled

Indicates
                                          					 whether silent monitor is enabled for the clients using this connection
                                          					 profile. A value of 0x00000001 (default) enables silent monitor. If this value
                                          					 is 0x00000000 or not present, silent monitor is disabled for this client. For
                                          					 all peripherals other than UCCE, you must set this field to 0x00000000.

WarnIfSilent
                                          					 Monitored

Indicates
                                          					 whether to display an indicator on the agent desktop when the agent is silent
                                          					 monitored by the team supervisor. A value of 0x00000001 causes a message to
                                          					 appear on the agent desktop when the supervisor is silent monitoring this
                                          					 agent. If this value is 0x00000000 (default) or not present, no message appears
                                          					 on the agent desktop when the supervisor is silent monitoring this agent.

RasCallMode

Indicates
                                          					 the agent work mode options for the mobile agent login dialog box. Valid values
                                          					 are 0 (agent chooses), 1 (call by call), and 2 (nailed up).

Field

Mask

Instrument

0x00000001

Password

0x00000002

Work Mode

0x00000004

Position
                                          					 ID

0x00000008

Skillgroup

0x00000010

AgentID

0x00000020

Login Name

0x00000040

Mobile
                                          					 Agent

0x00000080

The
                              		  heartbeating mechanism uses the MaxHeartbeats and Heartbeat values together to
                              		  determine when a client must send heartbeat requests to the server and when the
                              		  client must connect to the other server.

MaxHeartbeats is the max number of missed heartbeats before
                              		  failover. (Default = 5)

Heartbeat is the time interval between consecutive heartbeats.
                              		  (Default = 5)

This is
                              		  how the heartbeating mechanism works on the CTI OS client:

- After 5 seconds, if the
                                 			 client does not receive a response from the server, it sends a heartbeat
                                 			 request 1.

- After 5 seconds, if the
                                 			 client does not receive a response from the server, it sends a heartbeat
                                 			 request 2.

- After another 5 seconds, if
                                 			 the client does not receive a response from the server, it sends a heartbeat
                                 			 request 3.

- After yet another 5
                                 			 seconds, if the client does not receive any response from the server, it
                                 			 connects to an alternative server.

The amount of
                                          			 time it takes a client to reconnect to the other server depends on the type of
                                          			 failure that occurs.

The
                              		  heartbeat parameters above are only a factor if the TCP/IP socket is not
                              		  broken. For example, if you disconnect the network cable to the CTI OS Server,
                              		  TCP/IP does not break the socket. In this case, the client uses the
                              		  heartbeating mechanism listed above to detect the failure.

In a
                              		  different case, however, if the CTI OS Server process crashes or the machine is
                              		  turned off, the socket breaks and the client immediately knows that the
                              		  connection has failed. In this case, the client directly connects to the other
                              		  server without heartbeat attempts.

In either case,
                                          			 although the socket connection might get established right away, it might take
                                          			 a few more seconds for the agents to fully recover their previous, pre-failure
                                          			 state. This delay might particularly be experienced if many agents are failing
                                          			 over at the same time, or if the system is experiencing a heavy call load at
                                          			 the time of the failure.

### SilentMonitorService Subkey

The ConnectionProfiles key contains a
                                 		  <profile_name>\SilentMonitorService subkey, which contains parameters
                                 		  that clients use to connect to one of a set of silent monitor services. It
                                 		  contains the following keywords.

Registry Value Name

Value Type

Description

ListenPort

integer

Port on which the silent monitor service is listening for
                                             					 incoming connections.

TOS

integer

QOS setting for the connection.

HeartbeatInterval

integer

Amount of time in milliseconds between heartbeats.

HeartbeatRetries

integer

Number of missed heartbeats before the connection is
                                             					 abandoned.

Cluster

A key that contains a list of silent monitor services to which
                                             					 the CIL tries to connect. The CIL randomly chooses one of the services in this
                                             					 list. This key contains the following subkeys:

- 0 – Index of the
                                                						first silent monitor service

- N – Index of the
                                                						Nth silent monitor service

Both subkeys contain the following keyword.

SilentMonitorService – hostname or IP address of a silent
                                             					 monitor service to which to connect.

### Configuration of Additional Connection Profiles

#### Creation of Second Profile

Use the following template to create a connection profile
                                    		  that includes a silent monitor server:

```
"peripheralID"=dword:00001389
		   "ShowFieldBitMask"=dword:000000a3
     "SwitchCapabilityBitMask"=dword:7f3f1bff
     "CtiOsA"="ctios-a"
     "PortA"=dword:0000a42c
     "UCCESilentMonitorEnabled"=dword:00000001
		   "WarnIfSilentMonitored"=dword:00000000
     "CtiOsB"="ctios-b"
     "PortB"=dword:0000a42c
     "MaxHeartbeats"=dword:00000003
     "Heartbeat"=dword:00000005
     "AutoLogin"=dword:00000001
		   "WarnIfAlreadyLoggedIn"=dword:00000000
     "RejectIfAlreadyLoggedIn"=dword:00000000
     "TOS"=dword:00000000
     "RasCallMode"=dword:00000000
```

```
"HeartbeatInterval"=dword:00001388
		    "HeartbeatRetries"=dword:00000005
      "ListenPort"=dword:0000a42d
      "TOS"=dword:00000000
```

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                       			 Inc.\Ctios\CTIOS_< instance >\CTIOS1\EnterpriseDesktopSettings\All
                                       			 Desktops\Login\ConnectionProfiles\Name\< profileName >\SilentMonitorService\Cluster]

```
"SilentMonitorService"="sms-host-or-ip"
```

The SilentMonitorService key is not always present.

When the SilentMonitorService key is present, the agent desktop
                                                			 attempts to connect to the silent monitor service running on the host specified
                                                			 in the key.

When the SilentMonitorService key is not present, the agent desktop connects to a silent monitor service running locally (on
                                                the same computer as the agent desktop).

#### Two Profiles for Server- and Desktop-Based Silent Monitoring Scenario

If no silent monitor key exists in the connection profile,
                                    		  the profile defaults to desktop silent monitoring. The following template
                                    		  illustrates two connection profiles—one for desktop-based silent monitor, and
                                    		  one for server-based silent monitor:

```
"peripheralID"=dword:00001388
     "ShowFieldBitMask"=dword:00000023
     "SwitchCapabilityBitMask"=dword:7f3f1bff
     "CtiOsA"="ctios-a"
     "PortA"=dword:0000a42c
     "UCCESilentMonitorEnabled"=dword:00000001
     "WarnIfSilentMonitored"=dword:00000001
     "CtiOsB"="ctios-b"
     "PortB"=dword:0000a42c
     "MaxHeartbeats"=dword:00000003
     "Heartbeat"=dword:00000005
     "AutoLogin"=dword:00000001
     "WarnIfAlreadyLoggedIn"=dword:00000000
     "RejectIfAlreadyLoggedIn"=dword:00000000
     "TOS"=dword:00000000
     "SaveShowField"=dword:00000043
```

```
"peripheralID"=dword:00001388
     "ShowFieldBitMask"=dword:000000a3
     "SwitchCapabilityBitMask"=dword:7f3f1bff
     "CtiOsA"="ctios-a"
     "PortA"=dword:0000a42c
     "UCCESilentMonitorEnabled"=dword:00000001
     "WarnIfSilentMonitored"=dword:00000000
     "CtiOsB"="ctios-b"
     "PortB"=dword:0000a42c
     "MaxHeartbeats"=dword:00000003
     "Heartbeat"=dword:00000005
     "AutoLogin"=dword:00000001
     "WarnIfAlreadyLoggedIn"=dword:00000000
     "RejectIfAlreadyLoggedIn"=dword:00000000
     "TOS"=dword:00000000
     "RasCallMode"=dword:00000000
```

```
"HeartbeatInterval"=dword:00001388
     "HeartbeatRetries"=dword:00000005
     "ListenPort"=dword:0000a42d
     "TOS"=dword:00000000
```

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                       			 Inc.\Ctios\CTIOS_<instance>\CTIOS1\EnterpriseDesktopSettings\All
                                       			 Desktops\Login\ConnectionProfiles\Name\Mobile
                                       			 Agent\SilentMonitorService\Cluster]

```
"SilentMonitorService"="sms-host-or-ip"
```

## Call Appearance Grid Configuration

The CallAppearance key contains a list of all the columns
                              		  that appear on the softphone Call Appearance grid.

The columns are declared in the registry of each server on
                              		  the following location:

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco
                                 			 Systems,Inc.\CtiOs\<CTIOS
                                 			 InstanceName>\<CTIOSServerName>\EnterpriseDesktopSettings\ All
                                 			 Desktops\Grid\CallAppearance\Columns\Number\ Position ]

Position represents the actual location in the grid
                              		  where the column appears. For example for the first column Position is "1" and for the fifth column it is "5" .

The following table lists the attributes that a column
                              		  declaration can contain.

Attribute

Type

Description

Type

String Value

Assigns a column to display the Call information identified by
                                          					 the value of this attribute. The "Type values" table below lists the possible values.

Header

String Value

Contains the text string that appears on the header of the
                                          					 column. If not specified, the Type appears instead.

Width

DWORD value

Column width expressed in pixels.

If the Auto Resize Columns property is set on the Call
                                          					 Appearance Grid, this attribute has no effect. The column is automatically
                                          					 sized to match the column header or column cell content, whichever is longer.

If the Auto Resize Columns property is not set, one of the
                                          					 following occurs:

- If Width is
                                             						specified, the column sizes to match it.

- If Width is not specified, the column sizes to a default length.

MaxChars

String Value

Maximum number of characters that can appear in the column.

Name

String Value

Used only when the Type is ECC; contains the name of a given
                                          					 ECC variable. The name in this attribute must be entered without the prefix " user ." For the standard Outbound Option ECC
                                          					 variables, use the prefix BA without any dots following it; for example, BAResponse .

Alignment

String Value

Defines the alignment of the information on the columns.
                                          					 Possible values are "left" , "right" or "centered."

NumericOnly

String Value

If "true" the column accepts only numeric values for display.
                                          					 If "false" alphanumeric values may appear.

editable

String Value

Indicates if the user can modify the cells on the column at
                                          					 runtime.

The following table lists the Type values.

Type

Description

CallID

Associates the column with the unique call ID.

CallStatus or Status

Associates the column with Call Status.

DNIS

Associates the column with DNIS.

ANI

Associates the column with ANI.

CED

Associates the column with the caller entered digits.

DialedNumber or DN

Associates the column with the dialed number.

UserToUserInfo or UserToUser

Associates the column with user to user information.

WrapUp

Associates the column with the call wrap up data.

Var1, Var2, …, Var10

Associates the column with a call variable.

NAMEDVARIABLE, ECCVariable, ECCVar, ECC, or ECCNAME

Associates the column with an scalar ECC Variable.

NAMEDARRAY or ECCARRAY

Associates the column with a Named Array ECC variable.

CampaignID

Campaign ID for value appears in the Agent Real Time table.
                                          					 Set to zero if not used. Applicable only to Outbound Option systems .

QueryRuleID

Query rule ID for value appears in the Agent Real Time table.
                                          					 Set to zero if not used. Applicable only to Outbound Option systems .

The following are examples of column declarations:

```
"Type"="CallID"
```

```
"Type"="Var2"
    "editable"="true"
```

The following is an example of associating a column with an
                              		  ECC variable:

```
"Type"="ECC"
     "Name"="bobc"
     "Header"="ECC Bobc"
     "Maxchars"="8"
     "editable"="true"
```

The following is an example of associating a column with an
                              		  ECC array variable. Note that the "Name" key must contain both the array name and the
                              		  subscript/index:

```
"Type"="ECCARRAY"
     "Name"="bobc[0]"
     "Header"="ECCARRAY Bobc"
     "Maxchars"="8"
     "editable"="true"
```

### Configure Automatic Call Appearance Grid

The CTIOSServer directory contains a file,
                                 		  callappearance.default.reg.txt, which provides the following default definition
                                 		  for Call Appearance grid columns 1 to 18:

```
REGEDIT4

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\ 
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\Columns]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\Columns\ Number\1]
"Type"="CallID"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\Columns\ Number\10]
"Type"="Var2"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\Columns\ Number\11]
"Type"="Var3"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\12]
"Type"="Var4"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\Columns\ Number\13]
"Type"="Var5"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\14]
"Type"="Var6"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\15]
"Type"="Var7"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\16]
"Type"="Var8"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\17]
"Type"="Var9"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\18]
"Type"="Var10"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\2]
"Type"="CallStatus"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\3]
"Type"="DNIS"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\4]
"Type"="ANI"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\5]
"Type"="CED"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\6]
"Type"="DialedNumber"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\7]
"Type"="UserToUserInfo"
"maxchars"="129"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\8]
"Type"="WrapUp"
"maxchars"="40"
"editable"="true"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\CallAppearance\ Columns\Number\9]
"Type"="Var1"
"maxchars"="40"
"editable"="true"
```

To import this default definition into your registry,
                                 		  perform the following steps.

Step 1

Choose Start > Run dialog box.

Step 2

Rename the callappearance.default.reg.txt file to
                                          			 callappearance.default.reg.

Step 3

Enter regedit filename

where filename is the full pathname of the callappearance.default.reg file.

Step 4

Cycle your CTI OS Server process.

## Customize Agent Statistics Grid Configuration

The CTIOSServer directory contains a file,
                              		  agentstatistics.default.reg.txt, that contains the default definition for the
                              		  Agent Statistics grid. The following is an example
                              		  agentstatistics.default.reg.txt file that defines Agent Statistic grid columns
                              		  1 and 2:

```
REGEDIT4

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\AgentStatistics]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\AgentStatistics\Columns]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\AgentStatistics\ Columns\Number]
"DisableStatsMinimization"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\AgentStatistics\ Columns\Number\1]
"Type"="CallsHandledToday" 
"Header"="CallsHandledToday"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\AgentStatistics\Columns\Number\2]
"Type"="TimeLoggedInToday" 
"Header"="TimeLoggedInToday"
```

The DisableStatsMinimization registry value controls the
                              		  quantity of agent statistics that are sent from the CTI OS Server to CTI OS
                              		  clients. Possible values are 0 (only those agent statistics that are configured
                              		  to be displayed on the agent statistics grid are sent to the client) and 1 (all
                              		  agent statistics are sent to the client); default is 0.

To customize the Agent Statistics grid, perform the
                              		  following steps.

Step 1

Make a copy of the agentstatistics.default.reg.txt file.

Step 2

Rename the copied agentstatistics.default.reg.txt file to
                                       			 agentstatistics.default.reg.

Step 3

Add, remove, and renumber column definitions in the copied
                                          				file as desired.

Step 4

Choose Start > Run dialog box.

Step 5

Enter regedit filename

where filename is the full pathname of the
                                          				edited copy of the agentstatistics.default.reg file.

Step 6

Cycle your CTI OS Server process.

## Automatic Skill Group Statistics Grid Configuration

The CTIOSServer directory contains a file,
                              		  skillgroupstatistics.default.reg.txt, that contains the default definition for
                              		  the Skill Group Statistics grid. The following is an example
                              		  skillgroupstatistics.default.reg.txt file that defines columns 1 through 4:

The first column of the Skill Group Statistics window should be
                                          			 SkillGroupNumber.

```
REGEDIT4

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics\Columns]

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics\ Columns\Number]
"DisableStatsMinimization"=dword:00000000
"DisableMonitorModeStatsMinimization"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics\Columns\Number\1]
"Type"="SkillGroupNumber" 
"header"="SkillGroupNumber"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics\Columns\Number\2]
"Type"="AgentsAvail"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics\ Columns\Number\3]
"Type"="AgentsNotReady"

[HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\CTIOS\
<CTIOS InstanceName>\<CTIOSServerName>\
EnterpriseDesktopSettings\All Desktops\Grid\SkillGroupStatistics\ Columns\Number\4]
"Type"="AgentsReady"
```

The DisableStatsMinimization registry value controls the
                              		  quantity of skill group statistics that are sent from the CTI OS Server to CTI
                              		  OS agent mode clients. Possible values are 0 (only those skill group statistics
                              		  that are configured to appear on the skill group statistics grid are sent
                              		  to the client) and 1 (all skill group statistics are sent to the client);
                              		  default is 0.

The DisableMonitorModeStatsMinimization registry value
                              		  controls the quantity of skill group statistics that are sent from the CTI OS
                              		  Server to CTI OS monitor mode clients. Possible values are 0 (only those skill
                              		  group statistics that are configured to appear on the skill group
                              		  statistics grid are sent to the client) and 1 (all skill group statistics are
                              		  sent to the client); default is 0.

When viewing CTIOS with the Supervisors, the default skill group shows up on the CTIOS Agent Skill Group stats. This default
                                          skill group reports all voice calls not routed by a Unified UCCE script.

While you can customize columns in the Skill Group Statistics grid, you should retain the following
                                          			 registry settings:

```
"Type"="SkillGroupNumber"
   "header"="SkillGroupNumber"
```

The header can vary depending on the language you use. To
                              		  customize the Skill Group Statistics grid, perform the following steps.

Step 1

Make a copy of the skillgroupstatistics.default.reg.txt file.

Step 2

Rename the copied skillgroupstatistics.default.reg.txt file to
                                       			 skillgroupstatistics.default.reg.

Step 3

Add, remove, and renumber column definitions in the copied
                                          				file as desired.

Step 4

Open the Windows Start > Run dialog box.

Step 5

Enter regedit filename

where filename is the full pathname of the edited copy
                                          				of the skillgroupstatistics.default.reg file.

Step 6

Cycle your CTI OS Server process.

## Configure Additional Peripherals

The Peripheral Identifier screen in CTI OS Server setup
                              		  lets you supply peripheral information for a single peripheral only. To
                              		  configure additional peripherals, perform the following steps.

Step 1

Define a registry key for the peripheral in [Server\Peripherals\
                                       			 PERIPHERAL_LOGICAL_NAME].

Step 2

Create a connection profile for the peripheral.

The value that you specify for Peripheral ID in the Peripherals
                                          			 registry key definition must match the value that you specify for Peripheral ID in the
                                          			 connection profile definition.

## Quality of
                        	 Service/Type of Service

CTI OS
                              		  supports "Type of
                                 			 Service" ToS.

The
                              		  following connections/components support Qos/ToS:

CTI OS Server to
                                    				CTI OS Client.

CTI OS Client
                                    				(C++ CIL only) to CTI OS Server.

For CTI
                              		  OS, TOS tagging is not implemented in the Java or .NET (C#) CILs. As stated
                              		  above, a system using these could support one-way tagging from server to
                              		  client, but traffic from the client to the server is sent on a best-effort
                              		  basis.

CTI OS
                              		  supports the marking of TCP/IP packets with ToS. This allows for preferential
                              		  treatment (for example, class AF31 for assured forwarding) of CTI signaling
                              		  traffic if the network is configured to support this QoS scheme.

By
                              		  default, CTI OS does not mark packets, which means that the traffic is sent
                              		  with "best effort" (ToS = 0).

To turn
                              		  on the ToS markings, you must configure certain registry keys. In general, ToS
                              		  effects only outgoing packets. For example, the CTI OS Server can send packets
                              		  with ToS markings for assured forwarding to CTI OS clients. However, that does
                              		  not imply that CTI OS clients must also send their network traffic with the
                              		  same ToS value to the CTI OS Server. CTI OS clients could in fact send their
                              		  traffic on a best-effort basis, which would mean that ToS is only active one
                              		  way. Most likely, though, ToS is configured the same for both directions.

### Basic Configuration

To turn on ToS with AF31 for bidirectional
                                 		  communications, add/modify some registry keys for CTI OS Server.

The following key turns on marking of packets CTI OS Server sends
                                       				to CTI OS clients:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                          				  Inc.\Ctios\< customer-instance >\CTIOS1\Server\Connections
                                          				  "TOS"=dword:00000068

The dword value above is listed in hexadecimal format (decimal
                                                   				  104).

This registry key turns on markings of packets sent from the
                                       				client to the server:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                          				  Inc.\Ctios\< customer-instance >\CTIOS1\EnterpriseDesktopSettings\All
                                          				  Desktops\Login\ConnectionProfiles\Name\UCCE< or other profile
                                             					 name > "TOS"=dword:00000068

This key turns on TOS marking for Silent Monitor packets.

Use a different class (real-time/voice) with a
                                                      				different TOS value (Hex B8) for a silent monitor stream.

### Important Additional Configuration Information

Ensure the following registry key in Windows Server is as follows:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TcpIp\Parameters "DisableUserTOSSetting"=dword:00000000

### Caveats

For the ToS to become effective, you must configure the network (specifically the routers) to treat packets with ToS markings
                                       preferentially.

The traffic between the CTI OS Server and CTI OS clients may include types of data that do not qualify for AF31 type of service.
                                       In general, use AF31 for signaling traffic. For example, a calldelivered event sent from the CTI OS Server is time critical,
                                       as is a potential Answer request in response sent from the client in order to answer an alerting call. However, the CTI OS
                                       Server can also send statistics to clients. AF31 is not appropriate for this type of data. However, because CTI OS sends all
                                       traffic on the same connection, either all packets are marked or none. Therefore, you must turn off CTI OS Skillgroupstatistics
                                       with TOS enabled.

When hardphones are used with silent monitoring, the switch in the phone overrides the TOS marking to 0. This affects both
                                       silent monitor and CTI OS client to CTI OS Server traffic. (It does not affect CTI OS Server to CTI OS client traffic.) To
                                       correct this problem, write ACL to classify traffic based on TCP/UDP port number from the endpoint.

| Note | Except where
                                          			 otherwise indicated, the CTI OS registry keys discussed in this chapter are
                                          			 local and start at the [ HKEY_LOCAL_MACHINE\SOFTWARE\ Cisco Systems,
                                             				Inc.\CTIOS\< CTIOS_CTIOSInstanceName >\< CTIOSServerName > ] path. |
|---|---|

| Step 1 | Highlight the
                                       			 existing key in the left panel. |
|---|---|
| Step 2 | Position the
                                       			 cursor in the right panel and click. A popup menu
                                          				appears. |
| Step 3 | From the popup
                                       			 menu, select Key , String
                                          				Value , Binary
                                          				Value , or DWORD value. If you select Key , a placeholder for the key you want to add
                                          				appears highlighted in the left panel. For other items, a placeholder for the
                                          				item you want to add appears highlighted in the right panel. |
| Step 4 | Right-click the
                                       			 highlighted item. A popup menu appears. To name the
                                             				  item, select Rename from the popup menu; then type the new name
                                             				  for the item. To set the
                                             				  value data for String , Binary , and DWORD values, select Modify . A dialog box appears. Enter the value data
                                             				  following the Value Data prompt. |

| Note | After you change the registry, restart the CTI OS processes before the new
                                          			 setting can take effect. |
|---|---|

| Note | You can also run
                                             			 the setup program to reconfigure the CTI OS-based silent monitor. If the server
                                             			 setup program is not run, the CCMBasedSilentMonitor field is not present. As a
                                             			 result, CTI OS-based silent monitor is used. |
|---|---|

| Step 1 | On any VDI agent desktop, run the CTI OS client installer and
                                             			 configure the desktop.  For more information on the
                                             			 deployment, limitations, and supported features of CTI OS desktops on VDI, see CTI OS System Manager Guide for Cisco Unified ICM . |
|---|---|
| Step 2 | When the installation is complete, launch the CTI OS desktop and
                                             			 verify basic functionality by logging in an agent, changing agent states, or
                                             			 making calls. |
| Step 3 | After you complete the testing, follow the same steps on the other
                                             			 VDI agent desktops. |

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| ClientID | String Value | The identifier of the CTI Client. This appears in the CTI
                                          					 Server log file to help identify which session the CTI OS Server is connected
                                          					 on. | CTIOSServer |
| ClientPassword | String Value | The password of the CTI Client. This appears in the CTI
                                          					 Server log file to help identify which session the CTI OS Server is connected
                                          					 on. | CTIOSServer |
| ClientSignature | String Value | The signature of the CTI Client. This appears in the CTI
                                          					 Server log file to help identify which session the CTI OS Server is connected
                                          					 on. | CTIOSServer |
| SideAHost | String Value | The CTI Server (sideA) IP address or hostname to which the CTI
                                          					 OS Server connects. | Host specified during CTI Server installation. |
| SideAPort | DWORD Value | The CTI Server (sideA) IP port to which the CTI OS Server
                                          					 connects. | Port specified during CTI Server installation. |
| SideBHost | String Value | The CTI Server (sideB) IP address or hostname to which the CTI
                                          					 OS Server connects. | Host specified during CTI Server installation. |
| SideBPort | DWORD Value | The CTI Server (sideB) IP port to which the CTI OS Server
                                          					 connects. | Port specified during CTI Server installation. |
| Heartbeat Interval | DWORD Value | The interval (in seconds) at which HEARTBEAT_REQ messages are
                                          					 sent to the CTI Server. | 5 |
| ServicesMask | DWORD Value | The services requested from the CTI Server and provides the
                                          					 functionality that the MinimizeAgentStateEvents registry value used to provide. To suppress multiple state events add the
                                          					 bit:CTI_SERVICE_IGNORE _DUPLICATE_AGENT _STATES = 0x00100000 to the following registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\Ctios\
                                          					 CTIOS_<ctios_instance>\CTIOS1\ CtiDriver\Config Example: Change "ServicesMask" =dword:000c0016 to: "ServicesMask" =dword:001c0016 | 0x00000296 (52)(default) |
| CallMsgMask | DWORD Value | The unsolicited call events requested from the CTI Server. | 0x00ffffff (16777215) |
| AgentStateMask | DWORD Value | The agent states requested from the CTI Server. | 0x000003ff (1023) |
| ProtocolVersion | DWORD Value | The highest protocol version to use when connecting to the CTI
                                          					 Server. The highest common denominator is used when establishing the CTI
                                          					 Session. | 15 |
| IdleTimeout | DWORD Value | The session inactivity timeout (in seconds). The CTI Server
                                          					 disconnects clients after this time threshold has elapsed without other socket
                                          					 messages. | 0x7fffffff (2147483647) |
| MemoryPoolSize | DWORD Value | Size of the memory pool, in bytes. | 0x00000064 (100) |

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| EMSDisplayToScreen | DWORD Value | If set to 1, EMS routines attempt to write formatted messages
                                          					 to standard output. | 0 |
| EMSAllLogFilesMax | DWORD Value | The maximum total number of bytes that the EMS library writes
                                          					 to all local log files. | 2000000000 (2 billion decimal) |
| EMSBreakOnExit | DWORD Value | If set to 1, EMS exit routines invoke the Debugger. | 0 |
| EMSBreakOnInit | DWORD Value | If set to 1, EMS initialization routines invoke the Debugger. | 0 |
| EMSDebugBreak | DWORD Value | If set to 1, EMS failure routines invoke the Debugger before
                                          					 exiting the process. | 1 |
| EMSLogFileCountMax | DWORD Value | The maximum number of log files that the EMS library writes. | 10000 (decimal) |
| EMSLogFileLocation | String Value | The directory where the EMS library creates local log files. | Default directory specified at installation. |
| EMSLogFileMax | DWORD Value | The maximum number of bytes that the EMS library writes to a
                                          					 single local log file. | 30000000 (30 million decimal) |
| EMSNTEventLogLevel | DWORD Value | The minimum severity event that EMS logs in the Application
                                          					 Event Log. | 2 |
| EMSTraceMask | DWORD Value | A bitmask that specifies the levels of EMS tracing that are
                                          					 enabled. | 395791 (decimal) |
| EMSUserData | DWORD Value | Placeholder for arbitrary binary user data. |  |
| EMSForwardLevel | DWORD Value | The minimum severity event that EMS forwards to the Unified
                                          					 ICM central controller. | 0 |

| Registry
                                             					 Value Name | Value Type | Description | Default |
|---|---|---|---|
| AgentChatLevel | string | Defines the
                                             					 call center personnel with whom an agent is permitted to chat. You must set
                                             					 this to one of the values listed in the "AgentChatLevel values" table below. | TeamSupervisors |
| EnableWrapupDialog | DWORD Value | When enabled
                                             					 (1), a Wrapup dialog box pops up at the end of the call. A value of 0 disables
                                             					 this feature. | 1 |
| forceLogoutOnSessionClose | DWORD Value | Set to "1" to
                                             					 turn on the feature to force logout an agent when their session is ended by the
                                             					 agent closing the window without properly logging out. Note You must
                                                         						manually enter this value into the registry. If the value is not entered into
                                                         						the registry, the effect is the same as having it set to its default (0). | Note | You must
                                                         						manually enter this value into the registry. If the value is not entered into
                                                         						the registry, the effect is the same as having it set to its default (0). | 0 |
| Note | You must
                                                         						manually enter this value into the registry. If the value is not entered into
                                                         						the registry, the effect is the same as having it set to its default (0). |
| forceLogoutOn SessionCloseReason(Optional unless logout reason
                                             					 is required.) | DWORD Value | Indicates
                                             					 the reason code to be used by the CTI OS Server when the agent is forced to log
                                             					 out. This need not be defined in the registry when the default value is sufficient. By setting this to a specific reason code,
                                             you can easily determine if an agent is logged out by the CTI OS Server or if it's a typical agent log out. Note You must
                                                         						set this to a non-zero value if an idle reason code reason is required. Refer
                                                         						to "Unified
                                                            						  ICM Agent Desk Settings" to determine if the idle reason code is required. Note You must
                                                         						manually enter this value into the registry. | Note | You must
                                                         						set this to a non-zero value if an idle reason code reason is required. Refer
                                                         						to "Unified
                                                            						  ICM Agent Desk Settings" to determine if the idle reason code is required. | Note | You must
                                                         						manually enter this value into the registry. | 0 |
| Note | You must
                                                         						set this to a non-zero value if an idle reason code reason is required. Refer
                                                         						to "Unified
                                                            						  ICM Agent Desk Settings" to determine if the idle reason code is required. |
| Note | You must
                                                         						manually enter this value into the registry. |
| forceNotReadyOn SessionCloseReason(Optional unless idle reason
                                             					 is required.) |  | Indicates
                                             					 the reason code to be used by the CTI OS Server when the agent is forced to the
                                             					 Not Ready state before being forced to log out. This need not be defined in the registry when the default value is sufficient. By setting this to a specific reason code,
                                             you can easily determine if an agent is logged out by the CTI OS Server or if it's a typical agent log out. Note You must
                                                         						set this to a non-zero value if an idle reason code reason is required. For
                                                         						more information about the required idle reason code, see "Unified
                                                            						  ICM Agent Desk Settings" . Note You must
                                                         						manually enter this value into the registry. | Note | You must
                                                         						set this to a non-zero value if an idle reason code reason is required. For
                                                         						more information about the required idle reason code, see "Unified
                                                            						  ICM Agent Desk Settings" . | Note | You must
                                                         						manually enter this value into the registry. | 0 |
| Note | You must
                                                         						set this to a non-zero value if an idle reason code reason is required. For
                                                         						more information about the required idle reason code, see "Unified
                                                            						  ICM Agent Desk Settings" . |
| Note | You must
                                                         						manually enter this value into the registry. |
| LogoutReasonRequired | DWORD Value | On all
                                             					 switches except UCCE, when enabled (1) a Logout Reason Code dialog box pops up
                                             					 when changing state to Logout. On all switches, a value of 0 disables this
                                             					 feature. | 0 |
| NotReadyReasonRequired | DWORD Value | On all
                                             					 switches except UCCE, when enabled (1) a Not Ready Reason Code dialog box pops
                                             					 up when changing state to NotReady. On all switches, a value of 0 disables this
                                             					 feature. | 0 |
| PollForAgentStatsAtEnd Call | DWORD
                                             					 Value | Controls
                                             					 when agent statistics are sent from CTI OS Server to CTI OS clients. A value of
                                             					 0 means that agent statistics are sent at a regular interval (specified in
                                             					 PollingIntervalSec). A value of 1 means that agent statistics are sent only
                                             					 when a call ends. Note Changing
                                                         						the value of PollForAgentStatsAtEndCall may degrade performance. | Note | Changing
                                                         						the value of PollForAgentStatsAtEndCall may degrade performance. | 1 |
| Note | Changing
                                                         						the value of PollForAgentStatsAtEndCall may degrade performance. |
| PollingIntervalSec | DWORD
                                             					 Value | The agent
                                             					 statistics polling interval, in seconds. | 15 |
| WrapupDataRequired | DWORD
                                             					 Value | When
                                             					 enabled (1), wrapup data is mandatory. When disabled (0), wrapup data is not
                                             					 required. Not applicable to UCCE agents. | 0 |

| Note | You must
                                                         						manually enter this value into the registry. If the value is not entered into
                                                         						the registry, the effect is the same as having it set to its default (0). |
|---|---|

| Note | You must
                                                         						set this to a non-zero value if an idle reason code reason is required. Refer
                                                         						to "Unified
                                                            						  ICM Agent Desk Settings" to determine if the idle reason code is required. |
|---|---|

| Note | You must
                                                         						manually enter this value into the registry. |
|---|---|

| Note | You must
                                                         						set this to a non-zero value if an idle reason code reason is required. For
                                                         						more information about the required idle reason code, see "Unified
                                                            						  ICM Agent Desk Settings" . |
|---|---|

| Note | You must
                                                         						manually enter this value into the registry. |
|---|---|

| Note | Changing
                                                         						the value of PollForAgentStatsAtEndCall may degrade performance. |
|---|---|

| Value | Meaning |
|---|---|
| Disabled | All agent
                                             					 chat disabled. |
| PrimarySupervisor | Agents can
                                             					 chat only with primary supervisor of their team. |
| TeamSupervisors | Agents can
                                             					 chat with the primary or secondary supervisor of their team. |
| Team | Agents can
                                             					 chat with anyone in team. |
| Unrestricted | Agents can
                                             					 chat with anyone on the same peripheral. |

| Registry Value Name | Value Type | Description |
|---|---|---|
| Insert logout reason code 1 here | DWORD Value | Placeholder for first Logout reason code. |
| Insert logout reason code 2 here | DWORD Value | Placeholder for second Logout reason code. |
| Insert logout reason code 3 here | DWORD Value | Placeholder for third Logout reason code. |
| Insert logout reason code 4 here | DWORD Value | Placeholder for fourth Logout reason code. |

| Note | The maximum length permitted for a reason code is 42 characters. |
|---|---|

| Registry Value Name | Value Type | Description |
|---|---|---|
| String0 | String Value | Placeholder for first wrapup text string. |
| String1 | String Value | Placeholder for second wrapup text string. |
| String2 | String Value | Placeholder for third wrapup text string. |
| String3 | String Value | Placeholder for fourth wrapup text string. |

| Note | There are no CTI OS registry keys for defining text for outgoing
                                                			 wrapup strings. The Unified ICM does not save any wrapup data for outgoing
                                                			 calls, so you need not define outgoing wrapup strings. This is applicable to
                                                			 transfer and conference initiated calls also. (Both transfer and conference
                                                			 calls are treated as outgoing calls.) |
|---|---|

| Registry
                                             					 Value Name | Value Type | Description | Default |
|---|---|---|---|
| AgentPreCallEvent Timeout | DWORD Value | Length of
                                             					 time, in seconds, within which an AGENT_PRE_ CALL_EVENT must be followed by a
                                             					 BEGIN_CALL_ EVENT or the call object is deleted. | 30 |
| IPCCConference_ SupportsMultipleControllers | DWORD Value | When set to
                                             					 1, allows all parties of a Conference to add new parties to the conference as
                                             					 supported by Unified CM. If running against an earlier version of Unified CM,
                                             					 this registry value must be set to 0. If this value is not set to 0 when running against an earlier
                                             					 version of Unified CM, and a non-controller Conference party tries to make a
                                             					 Consult Call for a Conference, the party receives a Control Failure. | 1 |
| MinimizeEventArgs | DWORD Value | When set to
                                             					 1 (optimal), minimizes the amount of nonessential call object parameters sent
                                             					 to the client. | 1 |
| TrashCollectionInterval Sec | DWORD value | Controls how
                                             					 often (in seconds) the trash collector activates and removes any stale objects
                                             					 from memory. A value of 0 disables the trash collector. | 7200 |

| Registry
                                             					 Value Name | Value Type | Description | Default |
|---|---|---|---|
| ClientPoolInitialSize | DWORD Value | The number
                                             					 of Client objects to pre-create. Caution Leave this
                                                         						registry entry set to its default value. | Caution | Leave this
                                                         						registry entry set to its default value. | 1500 |
| Caution | Leave this
                                                         						registry entry set to its default value. |
| ClientPoolMinSize | DWORD Value | The minimum
                                             					 number of Client objects in the pool to trigger gstrowing the pool. Caution Leave this
                                                         						registry entry set to its default value. | Caution | Leave this
                                                         						registry entry set to its default value. | 50 |
| Caution | Leave this
                                                         						registry entry set to its default value. |
| ClientPoolIncrement | DWORD Value | The number
                                             					 of Client objects to create when the pool must be gstrown. Caution Leave this
                                                         						registry entry set to its default value. | Caution | Leave this
                                                         						registry entry set to its default value. | 50 |
| Caution | Leave this
                                                         						registry entry set to its default value. |
| HeartbeatIntervalMs | DWORD Value | The number
                                             					 of milliseconds between heartbeats from the server to its clients. | 60000 |
| HeartbeatRetrys | DWORD Value | The number
                                             					 of missed heartbeats before a connection is closed for unresponsiveness. | 5 |
| ListenPort | DWORD Value | The TCP/IP
                                             					 port on which the CTI OS Server listens for incoming client connections. | Port
                                             					 specified during CTI OS Server setup. |
| MaxMonitorMode Connections | DWORD Value | This
                                             					 registry entry controls the number of monitor mode connections connected to a
                                             					 CTI OS Server. | 7 |

| Caution | Leave this
                                                         						registry entry set to its default value. |
|---|---|

| Caution | Leave this
                                                         						registry entry set to its default value. |
|---|---|

| Caution | Leave this
                                                         						registry entry set to its default value. |
|---|---|

| Note | You can define two CTI OS Servers as peer servers only if they are
                                             			 connected to the same CTI Server or CTI Server pair. You cannot define two CTI
                                             			 OS Servers as peer servers if they are connected to CTI Servers that reside on
                                             			 different PGs. |
|---|---|

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| Heartbeat IntervalMs | DWORD Value | Number of milliseconds between heartbeats for client
                                             					 connection to peer servers. | 5000 |
| HeartbeatRetrys | DWORD Value | Number of retry attempts before a connection to a peer server
                                             					 is determined to be down. | 3 |

| Registry Value Name | Value Type | Description |
|---|---|---|
| Port | DWORD Value | The number of the TCP/IP port on which the peer server is
                                             					 listening for the client connection. |

| Registry Value Name | Value Type | Description |
|---|---|---|
| PeripheralID | DWORD Value | The PeripheralID configured in the Unified UCCE database for
                                             					 this Peripheral. |
| PeripheralType | DWORD Value | The PeripheralType corresponding to this PeripheralID. |

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| PollingInterval Sec | DWORD Value | The SkillGroup statistics polling interval, in seconds. | 10 |

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| Supervisor ChatLevel | String Value | Defines the call center personnel with whom a supervisor is
                                             					 permitted to chat. This must be set to one of the values listed in the table
                                             					 below. | Unrestricted |

| Value | Meaning |
|---|---|
| Disabled | All supervisor chat disabled. |
| Team | Supervisors can chat with anyone in their primary team. |
| Unrestricted | Supervisors can chat with anyone on the same peripheral. |

| Registry
                                             						Value Name | Value Type | Description | Default |
|---|---|---|---|
| ThreadPoolSize | DWORD
                                             						Value | If set to
                                             						<= 0, then the number of threads in the pool are calculated using the
                                             						following formula: number of CPU's +2. Maximum
                                             						threads allowed are 32. | 0 for all
                                             						peripheral types except Avaya where the default value is 14. |

| Note | Balancing threads
                                             			 against overall performance is not a trivial task. If the ThreadPoolSize value
                                             			 is changed, follow up with overall performance monitoring to see whether CTI OS
                                             			 Server performance is affected. |
|---|---|

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| ResolutionMSec | DWORD Value | The interval at which the TimerService services queued
                                             					 requests, expressed in milliseconds. | 500 |

| Registry Value Name | Value Type | Description | Default |
|---|---|---|---|
| BringToFrontOnCall | DWORD Value | When enabled (1), the softphone window is raised above all
                                          					 other windows when a BeginCallEvent occurs. | 1 |
| FlashOnCall | DWORD Value | When enabled (1), the softphone icon on the taskbar flashes
                                          					 when a BeginCallEvent occurs. | 0 |
| RecordingEnabled | DWORD Value | Controls whether the Record button is enabled on the Agent and
                                          					 Supervisor Softphones (0 = disabled, 1 = enabled). | 0 |
| AgentStatistics IntervalSec | DWORD Value | Controls how often (in seconds) the Agent and Supervisor
                                          					 Softphones update time-in-state agent statistics. | 0xF |

| Registry
                                          					 Value Name | Value Type | Description | Default |
|---|---|---|---|
| HeartbeatInterval | DWORD value | The time in
                                          					 seconds between consecutive heartbeats. | 5 |
| HeartbeatTimeout | DWORD value | The amount
                                          					 of time in seconds that must elapse without receiving data before a disconnect
                                          					 is signaled. | 15 |
| MediaTerminationPort | DWORD value | Reserved.
                                          					 This is the TCP/IP port that the silent monitor subsystem uses to render
                                          					 monitored audio. | 4000 |
| MonitoringIPPort | DWORD value | This is the
                                          					 TCP/IP port on the monitoring application to which the monitored application
                                          					 sends monitored audio. | 39200 |
| StopSMNonACDCall | DWORD value | This stops
                                          					 silent monitoring of Non-ACD calls. When enabled (1) in Unified CM-based silent
                                          					 monitoring, the supervisor's monitor button is disabled. When enabled in
                                          					 desktop-based silent monitoring, the supervisor's monitor button is enabled but
                                          					 the supervisor can only hear ACD calls. Note You must
                                                      						manually enter this value into the registry. If the value has not been entered
                                                      						into the registry, the effect is the same as having it set to its default (0). | Note | You must
                                                      						manually enter this value into the registry. If the value has not been entered
                                                      						into the registry, the effect is the same as having it set to its default (0). | 0 |
| Note | You must
                                                      						manually enter this value into the registry. If the value has not been entered
                                                      						into the registry, the effect is the same as having it set to its default (0). |

| Note | You must
                                                      						manually enter this value into the registry. If the value has not been entered
                                                      						into the registry, the effect is the same as having it set to its default (0). |
|---|---|

| SubKey/Value | Description |
|---|---|
| CtiOsProfileName | The name
                                          					 given to the profile. This string appears on the Login Dialog when a user is
                                          					 about to log in using the CTI OS Agent State Control. |
| PeripheralID | The numeric
                                          					 value of the peripheral to which the CTI OS Server connects. |
| Heartbeat | Time
                                          					 interval between heartbeat messages between the client and CTI OS Server. |
| MaxHeartbeats | Maximum
                                          					 number of heartbeats that can be missed by the CTI OS Client Session before
                                          					 failover occurs. |
| CtiOsA | DNS name of
                                          					 IP Address of the primary CTI OS Server to which a client application can
                                          					 connect. |
| CtiOsB | DNS name of
                                          					 IP Address of the secondary CTI OS Server to which a client application can
                                          					 connect. |
| PortA | TCP/IP port
                                          					 number assigned to the primary server. |
| PortB | TCP/IP port
                                          					 number assigned to the secondary server. |
| AutoLogin | Indicates if
                                          					 the client must automatically log in an agent or supervisor after it recovers
                                          					 from a system failure. For all peripherals other than UCCE you must set this
                                          					 field to 0x00000000. For UCCE, set this field to 0x00000001. |
| ShowFieldBit
                                          					 Mask | Indicates what fields appear in the CTI OS Login dialog box.
                                       				  Fields appear on the dialog box only if their corresponding bit in the mask is
                                       				  on. The possible fields and their corresponding masks are shown in the table "ShowBitFieldMask Fields" below. The default value at setup
                                       				  for ShowFieldBit Mask is 0x00000023 (AgentID, Instrument, and Password
                                       				  displayed). |
| WarnIfAlready LoggedIn | Indicates
                                          					 whether to display a warning but still permit login if an agent who is already
                                          					 logged in attempts to log in again. A value of 1 (default) enables the warning;
                                          					 a value of 0 disables the warning. This value is relevant only if
                                          					 RejectIfAlreadyLoggedIn is 0. |
| RejectIfAlready LoggedIn | Indicates
                                          					 whether or not to permit an agent who is already logged in to log in again. A
                                          					 value of 0 (default) permits an agent to log in again. A value of 1 prohibits
                                          					 an agent from logging in again. |
| DisableSkillGroup Statistics | Indicates
                                          					 whether skill group statistics are enabled for the agent using this connection
                                          					 profile. A value of 1 disables statistics. If this value is 0 (default) or not
                                          					 present, skill group statistics are enabled for this agent. |
| DisableAgent
                                          					 Statistics | Indicates
                                          					 whether agent statistics are enabled for the agent using this connection
                                          					 profile. A value of 1 disables statistics. If this value is 0 (default) or not
                                          					 present, statistics are enabled for this agent. |
| IPCCSilent
                                          					 MonitorEnabled | Indicates
                                          					 whether silent monitor is enabled for the clients using this connection
                                          					 profile. A value of 0x00000001 (default) enables silent monitor. If this value
                                          					 is 0x00000000 or not present, silent monitor is disabled for this client. For
                                          					 all peripherals other than UCCE, you must set this field to 0x00000000. |
| WarnIfSilent
                                          					 Monitored | Indicates
                                          					 whether to display an indicator on the agent desktop when the agent is silent
                                          					 monitored by the team supervisor. A value of 0x00000001 causes a message to
                                          					 appear on the agent desktop when the supervisor is silent monitoring this
                                          					 agent. If this value is 0x00000000 (default) or not present, no message appears
                                          					 on the agent desktop when the supervisor is silent monitoring this agent. |
| RasCallMode | Indicates
                                          					 the agent work mode options for the mobile agent login dialog box. Valid values
                                          					 are 0 (agent chooses), 1 (call by call), and 2 (nailed up). |

| Field | Mask |
|---|---|
| Instrument | 0x00000001 |
| Password | 0x00000002 |
| Work Mode | 0x00000004 |
| Position
                                          					 ID | 0x00000008 |
| Skillgroup | 0x00000010 |
| AgentID | 0x00000020 |
| Login Name | 0x00000040 |
| Mobile
                                          					 Agent | 0x00000080 |

| Note | The amount of
                                          			 time it takes a client to reconnect to the other server depends on the type of
                                          			 failure that occurs. |
|---|---|

| Note | In either case,
                                          			 although the socket connection might get established right away, it might take
                                          			 a few more seconds for the agents to fully recover their previous, pre-failure
                                          			 state. This delay might particularly be experienced if many agents are failing
                                          			 over at the same time, or if the system is experiencing a heavy call load at
                                          			 the time of the failure. |
|---|---|

| Registry Value Name | Value Type | Description |
|---|---|---|
| ListenPort | integer | Port on which the silent monitor service is listening for
                                             					 incoming connections. |
| TOS | integer | QOS setting for the connection. |
| HeartbeatInterval | integer | Amount of time in milliseconds between heartbeats. |
| HeartbeatRetries | integer | Number of missed heartbeats before the connection is
                                             					 abandoned. |
| Cluster |  | A key that contains a list of silent monitor services to which
                                             					 the CIL tries to connect. The CIL randomly chooses one of the services in this
                                             					 list. This key contains the following subkeys: 0 – Index of the
                                                						first silent monitor service N – Index of the
                                                						Nth silent monitor service Both subkeys contain the following keyword. SilentMonitorService – hostname or IP address of a silent
                                             					 monitor service to which to connect. |

| Note | The SilentMonitorService key is not always present. When the SilentMonitorService key is present, the agent desktop
                                                			 attempts to connect to the silent monitor service running on the host specified
                                                			 in the key. When the SilentMonitorService key is not present, the agent desktop connects to a silent monitor service running locally (on
                                                the same computer as the agent desktop). |
|---|---|

| Attribute | Type | Description |
|---|---|---|
| Type | String Value | Assigns a column to display the Call information identified by
                                          					 the value of this attribute. The "Type values" table below lists the possible values. |
| Header | String Value | Contains the text string that appears on the header of the
                                          					 column. If not specified, the Type appears instead. |
| Width | DWORD value | Column width expressed in pixels. If the Auto Resize Columns property is set on the Call
                                          					 Appearance Grid, this attribute has no effect. The column is automatically
                                          					 sized to match the column header or column cell content, whichever is longer. If the Auto Resize Columns property is not set, one of the
                                          					 following occurs: If Width is
                                             						specified, the column sizes to match it. If Width is not specified, the column sizes to a default length. |
| MaxChars | String Value | Maximum number of characters that can appear in the column. |
| Name | String Value | Used only when the Type is ECC; contains the name of a given
                                          					 ECC variable. The name in this attribute must be entered without the prefix " user ." For the standard Outbound Option ECC
                                          					 variables, use the prefix BA without any dots following it; for example, BAResponse . |
| Alignment | String Value | Defines the alignment of the information on the columns.
                                          					 Possible values are "left" , "right" or "centered." |
| NumericOnly | String Value | If "true" the column accepts only numeric values for display.
                                          					 If "false" alphanumeric values may appear. |
| editable | String Value | Indicates if the user can modify the cells on the column at
                                          					 runtime. |

| Type | Description |
|---|---|
| CallID | Associates the column with the unique call ID. |
| CallStatus or Status | Associates the column with Call Status. |
| DNIS | Associates the column with DNIS. |
| ANI | Associates the column with ANI. |
| CED | Associates the column with the caller entered digits. |
| DialedNumber or DN | Associates the column with the dialed number. |
| UserToUserInfo or UserToUser | Associates the column with user to user information. |
| WrapUp | Associates the column with the call wrap up data. |
| Var1, Var2, …, Var10 | Associates the column with a call variable. |
| NAMEDVARIABLE, ECCVariable, ECCVar, ECC, or ECCNAME | Associates the column with an scalar ECC Variable. |
| NAMEDARRAY or ECCARRAY | Associates the column with a Named Array ECC variable. |
| CampaignID | Campaign ID for value appears in the Agent Real Time table.
                                          					 Set to zero if not used. Applicable only to Outbound Option systems . |
| QueryRuleID | Query rule ID for value appears in the Agent Real Time table.
                                          					 Set to zero if not used. Applicable only to Outbound Option systems . |

| Step 1 | Choose Start > Run dialog box. |
|---|---|
| Step 2 | Rename the callappearance.default.reg.txt file to
                                          			 callappearance.default.reg. |
| Step 3 | Enter regedit filename where filename is the full pathname of the callappearance.default.reg file. |
| Step 4 | Cycle your CTI OS Server process. |

| Step 1 | Make a copy of the agentstatistics.default.reg.txt file. |
|---|---|
| Step 2 | Rename the copied agentstatistics.default.reg.txt file to
                                       			 agentstatistics.default.reg. |
| Step 3 | Add, remove, and renumber column definitions in the copied
                                          				file as desired. |
| Step 4 | Choose Start > Run dialog box. |
| Step 5 | Enter regedit filename where filename is the full pathname of the
                                          				edited copy of the agentstatistics.default.reg file. |
| Step 6 | Cycle your CTI OS Server process. |

| Note | The first column of the Skill Group Statistics window should be
                                          			 SkillGroupNumber. |
|---|---|

| Note | When viewing CTIOS with the Supervisors, the default skill group shows up on the CTIOS Agent Skill Group stats. This default
                                          skill group reports all voice calls not routed by a Unified UCCE script. |
|---|---|

| Note | While you can customize columns in the Skill Group Statistics grid, you should retain the following
                                          			 registry settings: |
|---|---|

| Step 1 | Make a copy of the skillgroupstatistics.default.reg.txt file. |
|---|---|
| Step 2 | Rename the copied skillgroupstatistics.default.reg.txt file to
                                       			 skillgroupstatistics.default.reg. |
| Step 3 | Add, remove, and renumber column definitions in the copied
                                          				file as desired. |
| Step 4 | Open the Windows Start > Run dialog box. |
| Step 5 | Enter regedit filename where filename is the full pathname of the edited copy
                                          				of the skillgroupstatistics.default.reg file. |
| Step 6 | Cycle your CTI OS Server process. |

| Step 1 | Define a registry key for the peripheral in [Server\Peripherals\
                                       			 PERIPHERAL_LOGICAL_NAME]. |
|---|---|
| Step 2 | Create a connection profile for the peripheral. |

| Note | The value that you specify for Peripheral ID in the Peripherals
                                          			 registry key definition must match the value that you specify for Peripheral ID in the
                                          			 connection profile definition. |
|---|---|

| Note | The dword value above is listed in hexadecimal format (decimal
                                                   				  104). |
|---|---|

| Note | Use a different class (real-time/voice) with a
                                                      				different TOS value (Hex B8) for a silent monitor stream. |
|---|---|