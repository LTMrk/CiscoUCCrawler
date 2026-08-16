---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-reference-g-b6c198f8c1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/reference/guide/ucce_b_acd-supplement-guide-for-avaya-12_6_1/ucce_b_acd-supplement-guide-for-avaya-12_5_chapter_010.html
retrieved_at: 2026-08-16T19:47:37.532597+00:00
---

Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(1)

# Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(1)

Updated: February 4, 2020

Chapter: Unified ICM Software Configuration

## Chapter: Unified ICM Software Configuration

# Unified ICM Software Configuration

In order to properly set up and maintain the Unified ICM database, you need to understand the relationships between the Avaya
                        database objects and the Unified ICM database objects. Some Unified ICM objects (for example, Unified ICM Services) do not
                        correspond directly to a specific object on the Avaya. Other Unified ICM objects, such as trunks, correspond directly to objects
                        on the ECS/MultiVantage/Avaya. By understanding the relationships between the database objects of the Avaya and Unified ICM
                        systems, it will be easier to keep the Avaya ECS/MultiVantage, CMS, and the Unified ICM databases synchronized (that is, up-to-date
                        with each other). This chapter describes how objects map between the Avaya and Unified ICM software. It also provides Avaya-specific
                        information that may assist you in configuring the PG through the Configuration Manager tools. For detailed information on
                        the Configuration Manager tool user interface, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise available at:

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligent-contact-management-enterprise/products-installation-and-configuration-guides-list.html

## Peripheral
                        	 Configuration

In Unified ICM terms, the Avaya corresponds to a peripheral. Unified ICM software treats all contact center devices
                           		(for example, ACD s, PBX s, VRU systems) as peripherals.

No special
                           		peripheral configuration parameters are required for Unified ICM software. However, there are certain
                           		items within the Unified ICM configuration that you may want to
                           		check.

### Peripheral Skill
                           	 Group Mask

The Peripheral
                              		(default) Skill
                                 		  Group Mask , which is available from the PG
                                 		  Explorer tool, are checked and set appropriately. The Skill
                                 		  Group Mask is used when configuring all skill groups for the
                              		peripheral.

If your peripheral
                              		is an EAS type, ensure that all check boxes are
                              		appropriately checked/unchecked. These check boxes identify the sub-groups or
                              		skill levels created for each skill group.

The default setting
                              		is that Skill
                                 		  Level 1 (primary) and Skill
                                 		  Level 2 (secondary) are checked, all other boxes (by default) are
                              		unchecked. The existence of the sub-skill groups can affect agent counts and
                              		call reporting. The Peripheral
                                 		  Skill Group Mask are overridden on a skill group by skill group
                              		basis as required.

### Peripheral Call
                           	 Control Variable Map

The Call
                                 		  Control Variable Map field, which is available on the PG
                                 		  Explorer tool, controls the mapping of route request elements to Peripheral
                                 		  Variables .

The Call
                                 		  Control Variable Map field can be used to set up the specific
                              		peripheral variables. Although these variables are reserved for a CTI application, the PG can use them as well.

Direct the PM : The PIM is directed on which call variables can be
                                       			 accessed. For example, the following setting allows the PIM to set call variable 1 and call variables 5
                                       			 through 10 while preserving the existing values of call variables 2 through 4
                                       			 (that is, the PIM does not set call variables 2 through 4).

/PIM=ynnnyyyyyy

Direct the CTI portion of
                                       				the PG : The CTI portion of the PG can be directed to allow the CTI
                                       				Client to override any PIM
                                       				Call Variable setting. For example, the following setting allows a CTI
                                       				Client to set call variable 1 and call variables 5 through 10.
                                    			 These call variables are set, while preserving the peripheral-determined values
                                    			 of call variables 2 through 4.

/CTI =
                                          					 ynnnyyyyyy

See also: For details on Route Request Elements, see Chapter 4, Post Routing. For more details on Unified ICM CTI capabilities and interaction with the PG, see
                              the ICM Software Enterprise CTI Interface Specification .

### Peripheral
                           	 Configuration Parameters

Several default
                              		settings are entered in the Configuration Parameters field of the PG
                                 		  Explorer tool . This includes default work-mode, default login skill
                              		level, reserved agent preference levels, and station monitoring of logged-in
                              		agents.

/defworkmode auto

/defskilllevel 3

Reserved Agent Preference
                                          				Levels (in ICM software, Release 4.0 and greater) are configured by the Configuration Parameters field. The reserved agent 1
                                       			 and agent 2 preference levels (represented as preference level 51 and 52,
                                       			 respectively, in CMS) are mapped again to a valid preference level. The PIM
                                       			 defaults the values to the highest valid preference level. The keywords / r1pref and /
                                          				r2pref are used to re-map reserve preference level 1 and 2
                                       			 respectively. The following example causes the PG to re-map reserve agent 1 and
                                       			 reserve agent 2 preference levels to preference level 15 and 16, respectively

/r1pref 15 /r2pref 16

Station
                                          				Monitoring of Logged-In Agents

/monitoragent y

/monitoragent is set to y in PIM by default. If you do not want to monitor
                                                            						specific extensions, then it is necessary for you monitor all the logged
                                                            						agents, set /monitoragent to y (use /monitoragent y). Configuring the
                                                            						extensions in the Peripheral Monitor Table of the PG Explorer is not needed. In
                                                            						such configurations, PIM monitors only those extensions, where agents are
                                                            						logged in.

If you
                                                            						are using CMS with Unified ICM and have over 1000 agents, disable the station
                                                            						monitoring of logged-in agents. Monitoring agent stations (That is providing
                                                            						visibility to all station activity) results in increased message traffic to the
                                                            						A, increased switch CPU load, and increased network traffic between the PG and
                                                            						Central Controller.

Use Encoded Trunk
                                          				Information over ANI in Calling Field with a setting of y, the PIM reports
                                       			 events in the calling field populated with encoded trunk information rather
                                       			 than ANI . The default mode is to populate the calling
                                       			 field with ANI . This argument defaults to n. If the argument is
                                       			 not specified or is specified as / UseTrunkOverANIInCallingField .

An example of
                                       			 one event may be:

```
19:31:20 pg1A-pim1 Trace: CSTA DELIVERED, 
	PrivData=[UU=None Consult[CID 603 Dev 6505 DevType 0] II 0
	Alert[Handle -1 Type LT_UNKNOWN] ANI 6505
	dnis_chars [] UCID 0x0
	TG 7 Tk 5 Mult 1]
	LoginDigits [] CallPrompt []
	CallID      = 604  DeviceID = 6505  DeviceType = Static
	Alerting    = 3501
	Calling     = 6505
	Called      = 3501
	Redirection = 6505
	LocalState  = INITIATE
	Cause       = EC_NEW_CALL
```

```
19:31:20 pg1A-pim1 Trace: CSTA DELIVERED, 
	PrivData=[UU=None Consult[CID 603 Dev 6505 DevType 0] II 0
	Alert[Handle -1 Type LT_UNKNOWN] ANI 6505
	dnis_chars [] UCID 0x0
	TG 7 Tk 5 Mult 1]
	LoginDigits [] CallPrompt []
	CallID      = 604  DeviceID = 6505  DeviceType = Static
	Alerting    = 3501
	Calling    = 229381  <= decimal equivalent of encoded trunk	Called      = 3501
	Redirection = 6505
	LocalState = INITIATE
Cause       = EC_NEW_CALL
```

/UseTrunkOverANIInCallingField y

Use Encoded
                                          				Trunk Information over ANI in Calling Field for Outbound Calls

The flag-usage
                                       			 is as follows:

/UseTrunkOverANIInCallingFieldForOutboundCalls y

/UseTrunkOverANIInCallingFieldForOutboundCalls n

- When the value of this
                                                      				  flag is n, ANI appears in the calling device field. Also, the
                                                      				  default value of this flag is n.

- This flag controls the
                                                      				  value of calling device field in CSTA DELIVERED and CSTA ESTABLISHED messages for outbound calls.

- This flag is available
                                                      				  from Releases ICM 6.0(0) SR9, and ICM 7.1(3) onwards.

The UseTrunkOverANIInCallingField and UseTrunkOverANIInCallingFieldForOutboundCalls are
                                                   				not applicable to TAESPIM .

Display the
                                          				Caller Entered Digits (CEDs) on the Agent Desktop

To ensure that
                                       			 the CED s are populated on the agent desktop, set the
                                       			 following parameters in the PG Explorer. In the Advanced
                                          				tab , ensure that the Agent
                                          				auto - configuration check box is checked.

If you do
                                                      				  not select them together, the CED s is not going to get populated on the agent
                                                      				  desktop.

These
                                                      				  settings are applied only to the Avaya
                                                         					 PG with the CMS mode enabled.

## Peripheral
                        	 Targets

A Unified ICM
                           		Peripheral Target is equivalent to the combination of DNIS ( VDN extension or Hunt
                           		Group Extension) and the trunk groups through which incoming calls arrive. VDN s are equivalent to the DNIS (for example, VDN 1100 would be DNIS 1100).

- A Network Target,
                                 		  identified by a Trunk Group and DNIS (VDN) that terminates on the Avaya . A Network Target is a target that Unified
                                 		  ICM software identifies as a termination for calls routed through the network.
                                 		  These trunk group-DNIS pairs are typically associated with labels provisioned
                                 		  by a long-distance carrier.

All Peripheral
                                    			 Targets, both internal (that is transfer points) and network, requires to be
                                    			 configured as Peripheral Targets in the Unified ICM database. This is done by using the
                                    			 Configure ICM tool. It is not necessary to enter every TrunkGroup/VDN in combination in the Unified
                                    			 ICM database unless you require them for call routing. In other words, a VDN requires to be entered only once in the
                                    			 Unified ICM database as a Peripheral Target. This is done for the PG to monitor the calls on that VDN .

You can
                                    			 configure Peripheral Targets by using the Peripheral Target Configuration
                                    			 window within the Configure ICM tool.

### Configuring VDN
                           	 and Hunt Group Extensions as Peripheral Targets

All VDN and Hunt
                                 		  Group extensions that are in any way connected with the handling of
                              		an incoming call must be configured in the Unified ICM database as Peripheral
                                 		  Targets . This ensures complete call monitoring. The PG monitors only those VDN s and, optionally, Hunt Groups that are
                              		configured as Peripheral
                                 		  Targets .

The Avaya PG (ESCPIM) supports extensions up to ten digits. The agent can log in to a Softphone that has an extension up to
                                             ten digits. This ten-digit support applies to Agent Login IDs too.

The Hunt Groups and VDNs support up to seven digits only. In order to use a seven digits, or a ten-digit, the config PIM registry, EnableTenDigitExtension is set to 1 in following path:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, 
Inc.\ICM\<cus01>\<PGXX>\PG\CurrentVersion\PIMS\pim1\ATTData\Config\
```

If the registry EnableTenDigitExtension is set to 0, then it limits support up to five digits for extension, Agent Login IDs, Hunt Groups, and VDNs.

By default, Avaya PG (TAESPIM) supports extensions of up to ten digits and this does not require registry configuration. The
                                             Agent Login IDs support up to ten digits.

## Peripheral Monitor
                        	 Table

VDNs must also
                                          			 be configured as Peripheral Targets in order to be monitored for reporting.

You can set up
                                          			 the Peripheral Monitor Table by choosing Peripherals > Peripheral
                                             				Monitor within Configure ICM to display the Peripheral Monitor table.

Click the Insert button to add records using the Peripheral Monitor Configuration window.

### Monitoring
                           	 Stations

The Peripheral Monitor table is used to specify which
                              		station, or range of stations, should be monitored by the PG. Multiple
                              		peripheral monitor entries are allowed. Set the Peripheral Monitor Type to Station. When
                              		specifying a single station (e.g., 1100), use the Extension field. When
                              		specifying a range of stations (e.g., 1100-1200), use the Param String field.

### VDN Timed ACW
                           	 Settings

VDNs that have a
                              		Timed ACW value on the Avaya is added as a Peripheral Monitor table entry with a Type of VDN . The Peripheral
                                 		  Monitor Param field indicates the Timed
                                 		  ACW value.

For VDN s that do not have
                              		the VDN override set, specify the Timed ACW value in the
                              		Peripheral Monitor table parameter string using the following format:

acw=N

```
acw=30
```

For VDNs that
                                                   				do have VDN override set, specify the Timed ACW value in the Peripheral Monitor table parameter
                                                   				string using the following format:

```
ACW=NNNN
```

The ACW
                                                   				keyword must be in upper-case. Replace N with the number of Timed ACW seconds. For example, a VDN with a Timed ACW of 180 seconds which does not have VDN override set
                                                   				specifies a Timed ACW value in the Peripheral Monitor table.

Only those VDN s that are monitored and for which the Avaya generates call events on their behalf, are
                                                   				considered as being in the call path by the PG when determining the
                                                   				correct Timed ACW value. In other words, if the PG is not notified by the switch that the call has
                                                   				passed through a VDN , the PG cannot consider that VDN when determining the Timed ACW value. The PG endeavors to use the same rule set as documented
                                                   				for the switch in determining the Timed ACW value to use (including VDN override).

### Configuring the
                           	 Return Destination VDN on Unified ICM

The Return
                                 		  Destination feature is configured in the PG
                                 		  Explorer Tool for a particular VDN for which the Return Destination
                              		is enabled on Avaya Switch.

In PG Explorer > Peripheral Monitor tab, set the Parameter string
                              		for the return destination VDN as returndestination .

To set up Return Destination VDN on Avaya Switch, see the section Configuring the Return Destination on Unified ICM

See the section ACD Notes and Restrictions for known caveats for Return Destination VDN.

## PIM
                        	 Configuration

The following figure shows PIM Configuration UI for CVLAN Interface.

The following figure shows PIM Configuration UI for TSAPI Interface .

The following points describe the Avaya ECS PIM Configuration Setup window:

CVLAN interface is not supported.

- Select the Interface Type . This selection of the interface
                                 		  type, determines the interface that the PIM uses to communicate with the Application Enablement Services (AES).

- Check the Enabled option to put the PIM into service. This option allows the PIM to communicate with the peripheral when the
                                 		  Peripheral Gateway is running.

Check the Enabled option to put the PIM into service. This option allows the PIM to communicate with the peripheral when the
                                    			 Peripheral Gateway is running.

In Configuration Manager (use the PG
                                       				Explorer tool to view the Peripheral ID ), each Configuration dialog box contains an Enabled option, a Peripheral name , and a Peripheral ID field. From the Peripheral record, enter the name of the peripheral
                                    			 in the Peripheral name field. Similarly, in the Peripheral ID field, enter the appropriate value.

Follow the below steps:

Use the TSAPI Configuration fields to describe the AES connections for the PG and its duplexed pair (if any).

In the ServerID field, specify the TLink that is configured in the AES Server.

In the LoginID field, specify the CTI username that is configured in the AES Server.

In the Password field, specify the CTI password that is configured in the AES Server.

In the
                                    			 Default Timed ACW value (Seconds) field specify the default time
                                    			 that the agents are allocated for after-call-work (ACW). A zero in this field
                                    			 indicates that the Unified ICM obtains this value from the Peripheral
                                    			 Monitor table. The values you have entered in this field are applicable to the
                                    			 monitored agents.

## Connection
                        	 management with AES using TSAPI Interface

At any point, AVAYA TAESPIM connects to one of the AES
                              		  server . This AES
                              		  server is configured in PIM configuration window.

In case if any
                           		failure occurs in the connection PIM tries to connect to another host. All the
                           		monitoring sessions are started from the beginning against the new AES
                              		  server .

## Installing TSAPI Client

Before you install the TSAPI client on your Avaya PG machine, you must download it from the Avaya Support website or from the Avaya DevConnect website.

Download the 32 Bit version of TSAPI client for Windows that must be installed on the Avaya PG machine.

The following steps help you with the installation of TSAPI Client :

Run setup.exe from the Installation folder and launch
                                 			 the TSAPI
                                    				Client installer wizard.

Click Next . On License Agreement screen, select the appropriate radio button to accept the terms and license agreement.

- Click Next .

To install the TSAPI Client , choose the default destination folder and click Next . In case if you want to select another folder, browse to the applicable folder.

Enter the Hostname or IP Address of the AES server. Click Add to List . This stores all AES server details in TSLIB.ini file of the client installation folder.

Click Next .

A warning message appears. This prompts you to replace the existing DLL files with aes-libeay32.dll and aes-ssleay32.dll,
                                 which is recommended. Select No to continue without replacing the files in icm\bin folder.

Click Finish to complete the installation process.

You can change the AES server details in the TSLIB.ini file, which is located in the client installation folder. This enables you to change the server details without running the
                                       setup again.

## Service Observer

The Service Observer feature allows a supervisor to silently monitor the conversation between an agent and a customer by using
                           various monitor options available from the ACD. The supervisor uses the configured features' codes on the switch to perform
                           service observing.

The Termination Call Detail (TCD) record for an observed call has a call disposition of Conferenced (30).

## Trunk
                        	 Groups

An Avaya Trunk
                           		Group is equivalent to a Unified ICM Trunk Group. The Avaya Trunk Group Number
                           		(For example, trunk group 5) is Unified ICM Trunk Group Peripheral Number. The
                           		Trunk Group Access Code (TAC) is Unified ICM Trunk Group Extension (For
                           		example, 500). TrunkGroupTimer is the value in the Registry that specifies the
                           		interval (in seconds) in which the PIM generates trunk group value requests. In
                           		other words, the TrunkGroupTimer specifies the timer period at which the PIM
                           		issues a Trunk Group query for each configured ICR trunk group. The default
                           		value for TrunkGroupTimer in the Registry is set to 10 seconds.

The PG uses the
                           		Trunk Group Extension to value query the Avaya and monitor Trunk Group trunk
                           		utilization. The PG also uses the Trunk Group Extension to properly identify an
                           		incoming call on translation route applications. The Trunk Group Extension is
                           		set in the Trunk Group Configuration window of Configure ICM.

For example, Trunk
                           		Group 11 with Trunk Access Code 111 would be entered in the Unified ICM
                           		database as Trunk Group 11 with Trunk Group Extension 111.

Create a default
                           		trunk group 9999 for use in those instances where a physical Trunk Group does
                           		not exist. For example, Hunt Groups or VDNs that are internal transfer points
                           		for agents, and therefore not accessible via an external trunk group, uses the
                           		default trunk group 9999 to allow the creation of the Peripheral Target. The
                           		default Trunk Group extension (that is, TAC) can either be left blank or
                           		specify 9999.

During a
                                          			 translation route, you need not set up the Network Trunk Group (NTG) if Unified
                                          			 ICM trunk reports are not required. A dummy NTG configuration, with a dummy
                                          			 peripheral number, can be configured and associated with the configured
                                          			 translation routes.

## Trunks

Individual trunks
                           		may or may not be monitored on the Avaya.

No special
                           		configuration information is required on an individual trunk basis. However,
                           		you must specify the number of trunks in the Trunk Group in the Trunk Group configuration Trunk Count field.
                           		Because the switch provides only the number of trunks-in-use and the
                           		trunks-idle, this count allows the Avaya PIM to determine the number of
                           		out-of-service trunks.

## Services

A Unified ICM
                              		  Service is the combination of call type (known by the VDN) and call
                           		treatment (that is, vector). There is no direct correlation of Unified
                              		  ICM Service to a specific Avaya object. However, a service does appropriate
                           		with what users typically identify Call
                              		  treatment on the Avaya .

The Avaya PIM does not support the updating of Peripheral Service Level .

Using the Service Explorer tool, set the Peripheral Service Level to C omputed By Call Center . The Unified ICM Peripheral Service Peripheral Service Level corresponds to the VDN Service Level.

## Skill
                        	 Groups

The Avaya -to- Unified ICM Skill
                              		  Group mapping is as follows:

Unified ICM
                                          				Software

Avaya

Skill Group

Skill Group

Skill Group
                                          				Peripheral Number

Skill Group
                                          				Number

Skill Group
                                          				Extension

Skill Group
                                          				Extension

Subgroups

Skill Group
                                          				and Skill LevelsTPF FPT

Important

### Skill Group
                           	 Subgroups

Sometimes, while
                              		created, a single Unified ICM skill group causes more than one skill group to
                              		be created in the Unified ICM database. These other skill groups are
                              		sub-skill groups, or subgroups, for the created base (priority 0) skill group. A subgroup has a
                              		unique priority and is associated with the base skill group.

For every base skill group created, at least one sub-group
                                          		  must be created under it.

Important

The PG s require to be cycled every time new subgroup are
                                             			 created.

The creation of
                                             			 these subgroups is determined on which subgroup mask is used at the time of the
                                             			 base skill group creation. The subgroup mask can have one of two settings:
                                             			 Peripheral Default or Specified. These settings are specified in the Skill
                                             			 Group Explorer tool.

If the subgroup
                                             			 mask is Peripheral Default , then the Peripheral's Skill Group Mask is used to determine
                                             			 which subgroups are created; otherwise, the Sub Group Mask for the Skill Group
                                             			 is used.

A subgroup is
                                             			 created for each checked box in the Sub Group Mask. The subgroups are used by
                                             			 the PG to properly log in the agent to the appropriate subgroup based on the
                                             			 agent's skill group skill level. For example, in an EAS type switch
                                             			 configuration, agents may be logged into a skill group with a PRIMARY or
                                             			 SECONDARY skill level. In order to properly account for agent counts and roll
                                             			 up call statistics properly, the subgroup for the agent's skill group requires
                                             			 to be configured in the Unified ICM database.

For CMS Configurations :

Add the name and
                                       			 IP address of the ACD PIM to the host file.

Restart the PG
                                       			 ICM Services.

For CMS-less
                                 		  Configurations :

See also: See the section CMS Cisco Real-Time Report for more information on CMS-related skill group issues related to configuration
                                       and CMS report revision.

### Using Skill Group
                           	 Priorities without Configuring Sub-Skill Groups

In Unified
                                 		  ICM , sub-skill groups are created when configuring the skill group
                              		priority. Each sub-skill group creates a target ID in the Unified ICM database.
                              		This target ID is used by all Unified
                                 		  ICM processes during the real-time messaging. It is essential for
                              		PG to send constant real-time messages and reports to the Central Controller
                              		for each of the configured skill groups. The PG requires to save the reports on
                              		the disk so that they are available to the Central Controller at any time.
                              		These operations are demanding sometimes, when many Unified ICM skill groups
                              		are configured together.

If the number of ACD
                              		skill groups and skill group priorities is large, do not use sub-skill groups.
                              		This causes increased data flow between the PG and the Central
                                 		  Controller . When the sub-skill group is not configured, the PG
                              		reports the skill group peripheral number only. This is defined in the ACD to
                              		the Central
                                 		  Controller without the skill group priority. In this case, Unified
                                 		  ICM reports contain only the skill group defined by the ACD
                              		peripheral number.

To avoid the
                                       			 base and sub-skill groups from being created, you must not have a skill group
                                       			 mask selected.

Skill Group Configuration: When configuring the skill group, do not select a skill group
                                       			 mask. The peripheral number is required to match the ACD skill group number
                                       			 without the skill group priority.

Impact on Unified ICM
                                          				Reports:

Report Type

Impact

Agent Skill
                                                      				Group Half Hour

When you do
                                                      				not set up a skill group priority in Unified ICM , the Agent Skill Group Half Hour report adds all the statistics of the ACD priorities
                                                      				to a single skill group.

If you set up
                                                      				the ACD priority in Unified ICM, the reports display the statistics for each
                                                      				priority.

Skill Group
                                                      				Half Hour

The reports
                                                      				display all the configured Unified ICM skill groups. This happens while using
                                                      				ACD priority, the Unified ICM reports display a skill group for each
                                                      				of the priorities configured (called Unified ICM sub-skill group) and one base skill
                                                      				group.

When you use
                                                      				a skill group with no priority configured, the reports display one Unified ICM
                                                      				skill group configured for each ACD skill group.

Termination
                                                      				Call Detail

The Termination Call Detail for calls for the ACD skill
                                                      				groups with priority configured, contain the Unified ICM skill group. This is
                                                      				defined by the ACD peripheral number (base skill group).

Migrating from Sub-skill
                                          		  Groups to Skill Groups with no ACD Priority Configured:

Remove all
                                                			 references to sub-skill groups in the router scripts and agent skill group
                                                			 membership.

In the Subgroup Mask tab, in the Skill Group Configuration area, uncheck the Override
                                                			 peripheral default mask check box.

In the Skill
                                                			 Group Mask tab, in the Peripheral Explorer configuration area, uncheck all
                                                			 the check boxes.

Restart the PG s to reflect the change in the peripheral
                                                			 configuration.

After the sub-skill
                                       		group migration, the base skill group reporting continues to work the same way
                                       		and there is no impact on historical reporting.

After the migration
                                       		is complete, the sub-skill groups are not permanently deleted from the database
                                       		and are available for historical reporting until they are permanently deleted.
                                       		The sub-skill group records before the migration process was completed are
                                       		available for historical reporting.

### Available Hold Off
                           	 Delay

The Available Hold Off Delay configuration parameter
                              		in the Skill
                                 		  Group Explorer Tool are set to the Timed ACW value on the ACD for this skill group.

## Service-to-Skill
                        	 Group Mappings

Since VDN s typically correspond to Unified ICM Services, the service-to-skill group mapping
                           		is equivalent to the skill groups used by the vector for the VDN . In order to ensure accurate call and agent
                           		reporting, be sure to include all skill
                              		  groups used by the VDN in the service-to-skill group mapping for that VDN . Service-to-skill group mappings are made in the
                           		Service Member window of Configure
                              		  ICM .

## Agents

The ACD -to- Unified ICM Agent mapping is given as follows:

Unified ICM
                                          				  Software

ACD

Agent

Agent

Agent
                                       				Peripheral Number

Agent ID

Agent
                                       				Extension

Agent's
                                       				Physical Extension

Important

For CMS configurations, agent configuration data is not
                                    		  required in the Unified ICM database.

For CMS-less
                                    		  configurations, the agents must be configured in the Unified
                                       			 ICM database. This is done through the Agent
                                       			 Configuration window of Configure ICM .

### Agent
                           	 States

The Table 7: Agent State Definitions lists Avaya agent states and their definitions. Some agent states have an optional call
                              direction, [IN/OUT], in case a call comes in or is initiated while in that state.

The Table 8: Unified ICM-Avaya Agent State Derivation shows how Unified ICM agent states are derived from the Avaya states.

Avaya Agent
                                             				  State

Definition

ACD IN/OUT

Agent is on
                                          				an incoming/outgoing ACD call

DACD

Agent is on a
                                          				direct agent ACD call.

ACW [IN/OUT]

Agent is
                                          				bookkeeping, doing data entry, or is at any other work related to the previous
                                          				call, and is not available to receive another ACD call. Includes times an agent
                                          				is on incoming and outgoing calls during ACW.

If on a call,
                                          				IN/OUT specifies the call direction.

DACW

Agent is in
                                          				the ACW state for a direct agent ACD call.

AUX [IN/OUT]

Agent is
                                          				doing non-ACD work, on break, or in a meeting. Agents initially log in AUX mode
                                          				until they AUTO-IN or MANUAL-IN. Includes times an agent is on incoming and
                                          				outgoing calls during AUX. Agent is not available to receive an ACD call.

If on a call,
                                          				IN/OUT specifies the call direction.

AVAIL

Agent is
                                          				available to receive calls.

RINGING

Call is
                                          				ringing at the agent's extension.

OTHER

Agent is
                                          				doing other work.

The call is on hold

The agent is dialing to call

Access a feature

The agent is handling a personal call

DACD is ringing with no answer

UNKNOWN

Agent is in
                                          				an unknown state (for example, when CMS link to G3 switch is not operational).

Unified ICM
                                             				  Agent State

Derivation
                                          				from Avaya Agent States

Logged_On

Logged_In

Logged_Off

Logged_Out

Ready

All states
                                          				other than AUX and UNKNOWN

Available

AVAIL

WrapUp

ACW, DACW

TalkingIn

ACD-IN, DACD

TalkingOut

ACD-OUT
                                          				(not in AUX)

TalkingOther

AUX IN/OUT,
                                          				ACW IN/OUT

Other

OTHER

Note: Support
                              	 for AUX reason code change in Not Ready state is
                              	 available from ICM 8.5(3) onwards.

## Skill Group
                        	 Members

For CMS-less configurations, the agent skill levels for their logged-in
                           		skill groups can only be determined via Unified ICM configuration. That is,
                           		Avaya does not yet provide skill level information over the CTI link for agent
                           		logins. Therefore, you must preconfigure and associate the agent with the
                           		correct subgroup in order to properly identify the agent's skill level.

## Translation
                        	 Routes

Translation routes are supported on the Avaya PG. Translation routes
                           		can be used to pass caller information to the Avaya (for example, ANI or
                           		Network CED

No special Unified ICM configuration is required for the Avaya.

## Routes

A Unified ICM Route
                           		is one or more Unified ICM Peripheral Targets . A Unified ICM Peripheral Targets is a Network Target
                           		identified by a trunk group and DNIS that terminate on the Avaya. A Peripheral
                           		Target is equivalent to the combination of DNIS ( VDN extension or Hunt Group extension) and the trunk groups through
                           		which the incoming calls arrive.

No special Unified
                           		ICM configuration is required for the Avaya.

## Routing
                        	 Client

The Routing Client
                           		Configuration Parameters field requires to be null‑terminated. The field
                           		delimiter, -DEFROUTE, are specified.

Order and case are
                           		not significant. However, all fields are separated by spaces. The following
                           		example shows a default Post-Route (Avaya Extension) to be used if the PG does
                           		not get a route response from the Router, for a reason:

```
DEFROUTE 3214
```

If a default route
                           		is not configured, the PG gives a negative acknowledgement (NAK) to the Avaya
                           		causing vector processing to proceed. The NAK may be the desirable action,
                           		depending on how the Avaya vectors are written.

## Unified ICM
                        	 Configuration for “CMS-less” PGs

You must set up all agents in the Unified ICM database.

You must map
                                    			 agents to skill groups in the Unified ICM database. The agent-to-skill group mapping must
                                    			 match the Avaya configuration. In addition, the subgroup must
                                    			 correctly map to the agent's priority.

- You must set up monitored
                                 		  instruments in the Peripheral Monitor table of the Unified ICM database. Agent stations are monitored.

You must set up
                                    			 Peripheral Targets in the Unified ICM database for all VDNs through which
                                    			 monitored calls flow.

## Maintaining Your
                        	 Configuration

It is preferred
                           		that changes made to your configuration are accomplished on the Avaya/CMS and in the Unified ICM database consecutively. This ensures
                           		that the PG gets the configuration updates on the Avaya/CMS systems.

It is imperative
                           		that the Avaya , CMS , and the Unified ICM database configurations are kept
                           		synchronized (that is, up-to-date with each other). Inaccurate or incomplete
                           		data results in inaccurate agent or call data.

## Registry
                        	 Keys

This section
                           		provides the usual values for the ESCPIM dynamic registry keys and PIM config
                           		registry keys.

The usual values for the ESCPIM dynamic registry keys are:

BriCheckMeters = 0 (for CMS), 1 (for CMS-less)

This value indicates whether the PIM regulate the ASAI/CTI message rates or not. "1" indicates that it enables message metering (that is, throttle outgoing messages).

BriMaxOutstandingMsgs = 100

SmartAgentStateTimer = 1800 (for CMS), 10 (for CMS-less)

BriCheckMessageRates = 0 (for CMS), 1 (for CMS-less)

This value indicated whether the PIM measures the ASAI/ CTI message rates or not. "1" indicates that the ASAI/ CTI message
                                 rates are measured.

The usual values for the PIM config registry keys are:

MaxActiveAssocPerASAILink key are set, depending on the version of CVLAN server. (The MaxActiveAssocPerASAILink refers to the maximum active association per CTI link)

CVLAN server

MaxActiveAssocPerASAILink

6.1.0

2048

8.2.1

4096

9.1

8192

AES Server

12000

| Note | This argument is
                                       		from the perspective of the PIM . |
|---|---|

| /PIM=ynnnyyyyyy |
|---|

| /CTI =
                                          					 ynnnyyyyyy |
|---|

| /defworkmode auto |
|---|

| /defskilllevel 3 |
|---|

| /r1pref 15 /r2pref 16 |
|---|

| /monitoragent y |
|---|

| Note | /monitoragent is set to y in PIM by default. If you do not want to monitor
                                                            						specific extensions, then it is necessary for you monitor all the logged
                                                            						agents, set /monitoragent to y (use /monitoragent y). Configuring the
                                                            						extensions in the Peripheral Monitor Table of the PG Explorer is not needed. In
                                                            						such configurations, PIM monitors only those extensions, where agents are
                                                            						logged in. If you
                                                            						are using CMS with Unified ICM and have over 1000 agents, disable the station
                                                            						monitoring of logged-in agents. Monitoring agent stations (That is providing
                                                            						visibility to all station activity) results in increased message traffic to the
                                                            						A, increased switch CPU load, and increased network traffic between the PG and
                                                            						Central Controller. |
|---|---|

| Note | The scheme
                                                			 for trunk information encoding is such that the upper 17 bits represent the
                                                			 Trunk Group and the lower 15 bits represent the Trunk. From the above example:
                                                			 For a Trunk Group value of 7 and a trunk value of 5, the binary representation
                                                			 for the encoded value is 00000000000000111 000000000000101. The decimal
                                                			 equivalent is 229381. |
|---|---|

| /UseTrunkOverANIInCallingField y |
|---|

| /UseTrunkOverANIInCallingFieldForOutboundCalls y |
|---|

| /UseTrunkOverANIInCallingFieldForOutboundCalls n |
|---|

| Note | When the value of this
                                                      				  flag is n, ANI appears in the calling device field. Also, the
                                                      				  default value of this flag is n. This flag controls the
                                                      				  value of calling device field in CSTA DELIVERED and CSTA ESTABLISHED messages for outbound calls. This flag is available
                                                      				  from Releases ICM 6.0(0) SR9, and ICM 7.1(3) onwards. |
|---|---|

| Note | The UseTrunkOverANIInCallingField and UseTrunkOverANIInCallingFieldForOutboundCalls are
                                                   				not applicable to TAESPIM . |
|---|---|

| Note | If you do
                                                      				  not select them together, the CED s is not going to get populated on the agent
                                                      				  desktop. These
                                                      				  settings are applied only to the Avaya
                                                         					 PG with the CMS mode enabled. |
|---|---|

| Note | The Avaya PG (ESCPIM) supports extensions up to ten digits. The agent can log in to a Softphone that has an extension up to
                                             ten digits. This ten-digit support applies to Agent Login IDs too. The Hunt Groups and VDNs support up to seven digits only. In order to use a seven digits, or a ten-digit, the config PIM registry, EnableTenDigitExtension is set to 1 in following path: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, 
Inc.\ICM\<cus01>\<PGXX>\PG\CurrentVersion\PIMS\pim1\ATTData\Config\ If the registry EnableTenDigitExtension is set to 0, then it limits support up to five digits for extension, Agent Login IDs, Hunt Groups, and VDNs. |
|---|---|

| Note | By default, Avaya PG (TAESPIM) supports extensions of up to ten digits and this does not require registry configuration. The
                                             Agent Login IDs support up to ten digits. |
|---|---|

| Note | VDNs must also
                                          			 be configured as Peripheral Targets in order to be monitored for reporting. You can set up
                                          			 the Peripheral Monitor Table by choosing Peripherals > Peripheral
                                             				Monitor within Configure ICM to display the Peripheral Monitor table. Click the Insert button to add records using the Peripheral Monitor Configuration window. |
|---|---|

| acw=N |
|---|

| Note | The acw keyword must be in
                                                			 lower-case. Replace the N with the number of Timed ACW seconds. For example,
                                                			 a VDN with a Timed ACW of 30 seconds that does not have VDN override set would specify a Timed ACW value in the Peripheral Monitor table as: acw=30 For VDNs that
                                                   				do have VDN override set, specify the Timed ACW value in the Peripheral Monitor table parameter
                                                   				string using the following format: ACW=NNNN The ACW
                                                   				keyword must be in upper-case. Replace N with the number of Timed ACW seconds. For example, a VDN with a Timed ACW of 180 seconds which does not have VDN override set
                                                   				specifies a Timed ACW value in the Peripheral Monitor table. Only those VDN s that are monitored and for which the Avaya generates call events on their behalf, are
                                                   				considered as being in the call path by the PG when determining the
                                                   				correct Timed ACW value. In other words, if the PG is not notified by the switch that the call has
                                                   				passed through a VDN , the PG cannot consider that VDN when determining the Timed ACW value. The PG endeavors to use the same rule set as documented
                                                   				for the switch in determining the Timed ACW value to use (including VDN override). |
|---|---|

| Note | CVLAN interface is not supported. |
|---|---|

| Note | Before starting the PG service with TSAPI interface, TSAPI Client is required. Please refer Installing TSAPI Client section for the client installation procedure. |
|---|---|

| Note | Download the 32 Bit version of TSAPI client for Windows that must be installed on the Avaya PG machine. |
|---|---|

| Note | You can change the AES server details in the TSLIB.ini file, which is located in the client installation folder. This enables you to change the server details without running the
                                       setup again. |
|---|---|

| Note | During a
                                          			 translation route, you need not set up the Network Trunk Group (NTG) if Unified
                                          			 ICM trunk reports are not required. A dummy NTG configuration, with a dummy
                                          			 peripheral number, can be configured and associated with the configured
                                          			 translation routes. |
|---|---|

| Note | The Avaya PIM does not support the updating of Peripheral Service Level . Using the Service Explorer tool, set the Peripheral Service Level to C omputed By Call Center . The Unified ICM Peripheral Service Peripheral Service Level corresponds to the VDN Service Level. |
|---|---|

| Unified ICM
                                          				Software | Avaya |
|---|---|
| Skill Group | Skill Group |
| Skill Group
                                          				Peripheral Number | Skill Group
                                          				Number |
| Skill Group
                                          				Extension | Skill Group
                                          				Extension |
| Subgroups | Skill Group
                                          				and Skill LevelsTPF FPT |

| Note | Unified ICM Skill Group
                                       		Peripheral Number is the Avaya Skill Group Number . The Unified ICM Skill
                                    	 Group Extension is the Avaya Skill
                                       		Group Extension . For example, if the Spanish skill group has a group number of 11 and an
                                    	 extension of 1100, then the Unified ICM Skill Group Peripheral
                                       		Number is 11 and the Skill Group
                                       		Extension is 1100. |
|---|---|

| Important | The Unified ICM Skill Group Peripheral
                                       		Number and Skill Group
                                       		Extension are important and must be kept synchronized (that is,
                                    	 up-to-date) with the Avaya skill group configuration. Failure to keep the skill
                                    	 group information synchronized between the Avaya and the Unified ICM database may result in incomplete (or worst
                                    	 case, inaccurate) call and agent statistics. |
|---|---|

| Note | For every base skill group created, at least one sub-group
                                          		  must be created under it. |
|---|---|

| Important | subgroups
                                          		  are created. The PG s require to be cycled every time new subgroup are
                                             			 created. The creation of
                                             			 these subgroups is determined on which subgroup mask is used at the time of the
                                             			 base skill group creation. The subgroup mask can have one of two settings:
                                             			 Peripheral Default or Specified. These settings are specified in the Skill
                                             			 Group Explorer tool. If the subgroup
                                             			 mask is Peripheral Default , then the Peripheral's Skill Group Mask is used to determine
                                             			 which subgroups are created; otherwise, the Sub Group Mask for the Skill Group
                                             			 is used. A subgroup is
                                             			 created for each checked box in the Sub Group Mask. The subgroups are used by
                                             			 the PG to properly log in the agent to the appropriate subgroup based on the
                                             			 agent's skill group skill level. For example, in an EAS type switch
                                             			 configuration, agents may be logged into a skill group with a PRIMARY or
                                             			 SECONDARY skill level. In order to properly account for agent counts and roll
                                             			 up call statistics properly, the subgroup for the agent's skill group requires
                                             			 to be configured in the Unified ICM database. |
|---|---|

| Note | In order for
                                          		  AutoLoginBase to work correctly and provide consistent LAA stats for agents in
                                          		  all priorities, at least one agent must be logged in to the base skill group. |
|---|---|

| Note | When working with ICM Version 4.5(x) and later, while activating the ACD PIM if you get an error message that
                                          		  contains the term C_NOENT , do the following: |
|---|---|

| Note | This feature is
                                          		  applicable from ICM 6.0 SR7 and 7.1(2) with Avaya PG. |
|---|---|

| Report Type | Impact |
|---|---|
| Agent Skill
                                                      				Group Half Hour | When you do
                                                      				not set up a skill group priority in Unified ICM , the Agent Skill Group Half Hour report adds all the statistics of the ACD priorities
                                                      				to a single skill group. If you set up
                                                      				the ACD priority in Unified ICM, the reports display the statistics for each
                                                      				priority. |
| Skill Group
                                                      				Half Hour | The reports
                                                      				display all the configured Unified ICM skill groups. This happens while using
                                                      				ACD priority, the Unified ICM reports display a skill group for each
                                                      				of the priorities configured (called Unified ICM sub-skill group) and one base skill
                                                      				group. When you use
                                                      				a skill group with no priority configured, the reports display one Unified ICM
                                                      				skill group configured for each ACD skill group. |
| Termination
                                                      				Call Detail | The Termination Call Detail for calls for the ACD skill
                                                      				groups with priority configured, contain the Unified ICM skill group. This is
                                                      				defined by the ACD peripheral number (base skill group). |

| Unified ICM
                                          				  Software | ACD |
|---|---|
| Agent | Agent |
| Agent
                                       				Peripheral Number | Agent ID |
| Agent
                                       				Extension | Agent's
                                       				Physical Extension |

| Important | The PG configures the agents dynamically. This is
                                    	 applicable for the PG s that are using CMS . The Configure
                                       		ICM tool do not add them individually. For CMS-less PG installations, agents require to be configured by
                                    	 the Configure
                                       		ICM tool. Further, agent skill group member assignments are
                                    	 required to be completed to match the switch configuration. |
|---|---|

| Note | In Unified ICM,
                                       	 issues with reporting and routing arises if the agent is not logged in a
                                       	 station before making and receiving calls. |
|---|---|

| Avaya Agent
                                             				  State | Definition |
|---|---|
| ACD IN/OUT | Agent is on
                                          				an incoming/outgoing ACD call |
| DACD | Agent is on a
                                          				direct agent ACD call. |
| ACW [IN/OUT] | Agent is
                                          				bookkeeping, doing data entry, or is at any other work related to the previous
                                          				call, and is not available to receive another ACD call. Includes times an agent
                                          				is on incoming and outgoing calls during ACW. If on a call,
                                          				IN/OUT specifies the call direction. |
| DACW | Agent is in
                                          				the ACW state for a direct agent ACD call. |
| AUX [IN/OUT] | Agent is
                                          				doing non-ACD work, on break, or in a meeting. Agents initially log in AUX mode
                                          				until they AUTO-IN or MANUAL-IN. Includes times an agent is on incoming and
                                          				outgoing calls during AUX. Agent is not available to receive an ACD call. If on a call,
                                          				IN/OUT specifies the call direction. |
| AVAIL | Agent is
                                          				available to receive calls. |
| RINGING | Call is
                                          				ringing at the agent's extension. |
| OTHER | Agent is
                                          				doing other work. For example, there can be many such scenarios where: The call is on hold The agent is dialing to call Access a feature The agent is handling a personal call DACD is ringing with no answer |
| UNKNOWN | Agent is in
                                          				an unknown state (for example, when CMS link to G3 switch is not operational). |

| Unified ICM
                                             				  Agent State | Derivation
                                          				from Avaya Agent States |
|---|---|
| Logged_On | Logged_In |
| Logged_Off | Logged_Out |
| Ready | All states
                                          				other than AUX and UNKNOWN |
| Available | AVAIL |
| WrapUp | ACW, DACW |
| TalkingIn | ACD-IN, DACD |
| TalkingOut | ACD-OUT
                                          				(not in AUX) |
| TalkingOther | AUX IN/OUT,
                                          				ACW IN/OUT |
| Other | OTHER |

| Note | The dynamic registry field BriMaxOutstandingMessages is used along with BriCheckMeters registry field to indicate the number of outstanding ASAI/ CTI messages (that is, messages waiting for a response from the CVLAN Server). After the PIM has reached the maximum number of outstanding messages, it does not send messages until one pending ASAI/CTI message has been received. |
|---|---|

| Note | During the startup of the PIM process, the PIM sends the ASAI/ CTI messages at a faster rate until the limit controlled by the BriMaxOutstandingMessages field. The high priority outgoing messages take precedence over the usual priority outgoing messages. |
|---|---|

| Note | The PIM also uses message metering to ensure that it does not exceed the maximum number of active associations per CTI link
                                          (see the config registry field, MaxActiveAssocPerASAILink). |
|---|---|

| CVLAN server | MaxActiveAssocPerASAILink |
|---|---|
| 6.1.0 | 2048 |
| 8.2.1 | 4096 |
| 9.1 | 8192 |
| AES Server | 12000 |

| Note | It is not
                                       		  required to cycle (restart) the PG, for the changed dynamic registry values to
                                       		  be effective; however, for the changed config registries to be effective, you
                                       		  need to cycle the PG. |
|---|---|