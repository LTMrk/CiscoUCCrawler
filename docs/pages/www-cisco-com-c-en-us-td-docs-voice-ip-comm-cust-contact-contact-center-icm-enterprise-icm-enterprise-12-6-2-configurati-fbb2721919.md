---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-fbb2721919
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_configuration-guide-for-cisco-unified-icm-enterprise_release_1262/skill-groups-12-6-1.html
retrieved_at: 2026-08-16T14:38:32.844317+00:00
---

Configuration Guide for Cisco Unified ICM Enterprise, Release 12.6(2)

# Configuration Guide for Cisco Unified ICM Enterprise, Release 12.6(2)

Updated: April 28, 2023

Chapter: Skill Targets

## Chapter: Skill Targets

# Skill Targets

## Skill Targets
                        	 Subsystem

After you define a
                              		  peripheral, you must define the skill targets associated with the peripheral.
                              		  The following figure shows the elements in a skill targets subsystem.

Skill targets are the
                              		  entities that the system software chooses to handle calls at a peripheral:
                              		  services, skill groups, and agents.

The other members
                              		  in the skill target subsystem define relationships among skill targets:

Agents are
                                    				members of skill groups.

Skill groups are
                                    				members of services.

An enterprise
                                    				skill group is a collection of skill groups, usually from different
                                    				peripherals.

An enterprise
                                    				service is a collection of services, usually from different peripherals.

The rest of this
                              		  chapter describes how to define these skill targets and establish the
                              		  relationships among them.

## Services

You must provide
                              		  information about each service associated with a peripheral. A service is a
                              		  type of caller need that the peripheral handles; for example, sales, support,
                              		  and information might all be services.

Use the Service
                              		  Explorer to configure services and their associated records.

### Service Explorer

The following sections show you how to use the Service Explorer to
                                 		  view and configure a service and its associated routes, peripheral targets, and
                                 		  labels.

#### View Service

To view a service, follow these steps:

##### Procedure

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > Service Explorer . The
                                             			 Service Explorer window appears.

Step 2

In the Select filter data box, select the peripheral
                                             			 associated with the service you want to view. You can choose the name from the
                                             			 drop-down list.

Note

Once you have saved a service record to the Unified ICM database, you cannot change the peripheral to which it is
                                                            				associated.

Step 3

Select any other filters you want. None in the Optional filter box means all services associated
                                             			 with the selected peripheral will be displayed.

Step 4

Click Retrieve . This lists in the tree list
                                             			 box the names of retrieved services.

Note

A tree object is unassigned if it was made by another
                                                            				configuration tool and was not assigned (mapped) to a parent object; for
                                                            				example, a label might not have been assigned to a peripheral target or a route
                                                            				might not have been assigned to a service, and so on.

Step 5

In the tree list box, select a service to display its
                                             			 configuration information on the right side of the window.

Step 6

If the service has a route associated with it, click its icon in
                                             			 the tree list box to display its configuration information. Do the same for a
                                             			 peripheral target associated with the route and a label associated with the
                                             			 peripheral target.

### Modifying, Defining, and Deleting Services

The following sections show you how to modify, define, and delete
                              		services.

#### Modify a Service

To modify a service, do the following:

##### Procedure

Step 1

Follow the steps for viewing a service.

Step 2

Edit the configuration information.

Note

You cannot modify fields that are greyed out.

With the mouse, you can select an object and then move it to
                                                				another part of the tree, as long as its object type belongs in that tree
                                                				location. For example, to move a route to another service, select it and then
                                                				move the pointer to that service. When that service becomes highlighted, lift
                                                				your finger off the mouse. You can also use the Bulk Configuration tool to take
                                                				the output of a switch and create 20 or 30 labels. Then, using the Service
                                                				Explorer, you can attach the labels to an appropriate location.

When you make a modification, the Changed icon appears next to the selected
                                                				item in the tree list box.

Step 3

Click Save .

The modified data is saved in the Unified ICM database and the Changed icon is removed from the edited object
                                    		  in the tree list box.

#### Define a Service or Associated Record

To define a service and/or its associated records, follow these steps:

##### Procedure

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > Service Explorer . The
                                             			 Service Explorer window appears.

Step 2

In the Select filter data box of the Explorer window, click Retrieve . This enables the Add Service button.

Step 3

Click Add Service . A new service appears in the tree
                                             			 list box with a To Be Inserted icon

next to it. Tabbed fields also appear on the right for the new
                                                				service's configuration information.

Step 4

Fill in the tabbed fields.

Step 5

Click Add Route and fill in its configuration
                                             			 records.

Step 6

Click Add Peripheral Target and also Add Label and fill in those records.

Selecting an item in the tree list box enables the Add button for more items of that type and
                                                				for the associated item immediately beneath it in the tree, if it can have one.

Step 7

If desired, set security settings on the records.

Step 8

Click Save .

#### Delete a Record

To delete a record:

##### Procedure

Step 1

In the Explorer tree list box, select the item or associated items
                                             			 whose records you want to delete.

Note

Step 2

Click Delete . This places a Marked for Deletion icon next to the selected item in
                                             			 the tree list box. This also toggles the Delete button to Undelete .

To undelete an item marked for deletion, select it in the tree
                                                				list box and click Undelete .

Step 3

Click Save .

This deletes from the database items marked for deletion and
                                                				removes them from the tree list box. Once you do this, you cannot undelete
                                                				deleted items.

## Skill Groups

Enter information
                              		  about each skill group associated with each peripheral. A skill group is
                              		  a collection of agents that share a common set of skills.

Use the
                              		  Configuration Manager's Skill Group Explorer to view, modify, or define a skill
                              		  group.

### Skill Group Explorer

The following sections show you how to use the Skill Group Explorer to
                              		view and configure a skill group and its associated routes, peripheral targets,
                              		and labels.

#### View a Skill Group

To view a skill group, follow these steps:

##### Procedure

Step 1

In the Configuration Manager's menu, select Tools > Explorer
                                                   				  Tools > Skill Group Explorer . The
                                             			 Skill Group Explorer window appears.

Step 2

In the Select filter data box, select the peripheral
                                             			 associated with the skill group you want to view. You can choose the name from
                                             			 the drop-down list of peripheral enterprise names.

Step 3

Select any other filters you want. None in the Optional filter box
                                             			 means all skill groups associated with the selected peripheral will be
                                             			 displayed.

Step 4

Click Retrieve . This lists in the tree list
                                             			 box names of skill groups.

Step 5

In the tree list box, select a skill group to display its
                                             			 configuration information on the right side of the window.

Step 6

If the skill group has a route associated with it, click its icon
                                             			 in the tree list box to display its configuration information. Do the same for
                                             			 a peripheral target associated with the route and a label associated with the
                                             			 peripheral target.

Note

### Modifying, Defining, and Deleting Skill Groups

The following sections show you how to modify, define skill groups.

### Modify a Skill Group

To modify a skill group, follow these steps:

#### Procedure

Step 1

Follow the steps to view a skill group.

Step 2

Edit the configuration information.

With the mouse, you can select an object and move it to
                                             				another part of the tree, as long as its object type belongs in that tree
                                             				location. For example, to move a route to another skill group, select it and
                                             				move the pointer to that skill group. When that skill group becomes
                                             				highlighted, lift your finger off the mouse. You can also use the Bulk
                                             				Configuration tool to take the output of a switch and create 20 or 30 labels.
                                             				Then, using the Explorer, you can attach the labels to an appropriate location.

Note

You cannot modify fields that are greyed out.

You cannot update the Peripheral field. 
                                                         			 To modify the Peripheral Number, you can use the Cisco Unified Contact Center Management Portal (CCMP).

When you make a modification, the Changed icon appears next to the selected item
                                             				in the tree list box.

Step 3

Click Save .

The modified data is saved in the Unified ICM database and the Changed icon is removed from the edited object in the tree
                                             				list box.

### Define a Skill Group
                           	 or Its Associated Records

Note

To define a skill
                                 		  group and/or its associated records, follow these steps:

#### Procedure

Step 1

In the
                                          			 Configuration Manager's menu, select Tools > Explorer
                                                				  Tools > Skill Group Explorer . The Skill Group
                                          			 Explorer window appears.

Step 2

In the Select filter
                                             				data area of the Explorer window, click Retrieve . This enables the Add
                                             				Skill Group button.

Step 3

Click Add
                                             				Skill Group . A new skill group appears in the tree list box with a To Be
                                             				Inserted icon next to it. Tabbed fields also appear on the right for the
                                          			 new skill group's configuration information.

Step 4

Fill in the
                                          			 tabbed fields.

Note

These fields
                                                         				  are not automatically populated.

Step 5

Click Add
                                             				Route and fill in its configuration records.

Step 6

Click Add
                                             				Peripheral Target and also Add
                                             				Label and fill in those records.

Selecting an
                                             				item in the tree list box enables the Add button for more items of that type and for the
                                             				associated item immediately beneath it in the tree, if it can have one.

Step 7

If desired, set
                                          			 security settings on the records.

Step 8

Click Save .

### Skill groups on the Child Central Controller

Access the Configuration Manager on the Child Administration & Data
                              		Server to configure skill groups.

#### Configure Skill Groups on the Child Central Controller

Use the Configuration Manager Skill Group Explorer Tool to configure
                                    		  skill groups SG01 and SG02 on the Child Central Controller.

To configure skill groups on the Child Central Controller:

##### Procedure

Step 1

Start the Skill Group Explorer Tool .

Step 2

On the Main window of the Agent Explorer Tool, click Retrieve .

Step 3

Click Add Skill Group .

The Skill Group tab appears.

Step 4

Complete all the fields and click OK .

The skill group name appears in the list, as with all Explorer
                                                				tools.

Step 5

Select the Skill Group Member tab and click Add .

The Add Skill Group Member dialog appears.

Step 6

Select the agents to add to the skill group, then click OK .

The agents become members of the skill group.

Step 7

Select the skill group in the tree list, then click Add Route .

The Route tab appears.

Step 8

Provide the Route Name and click Save .

The route name appears in the tree list and the skill group is
                                                				added to the peripheral.

Step 9

Repeat this to add one more skill group.

Step 10

Click Save , then Close to exit the Skill Group Explorer Tool.

### Skill Groups–to–Services Mapping

When you define services and skill groups, you can establish the
                                 		  mappings of skill groups to services. Each skill group can be mapped to zero,
                                 		  one, or more services; each service can be mapped to zero, one, or more skill
                                 		  groups.

You can define some service member skill groups as being primary for
                                 		  the service. The system software uses the primary attribute in determining the
                                 		  destination for a call to the service. For example, the Longest Available Agent
                                 		  (LAA) for a service is really the LAA for primary groups configured for that
                                 		  service.

### Map Skill Groups to Services

To map skill groups to services, follow these steps:

#### Procedure

Step 1

Within the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Service Explorer . The
                                          			 Service Explorer window appears.

Step 2

Select the filters you want and click Retrieve . The retrieved services appear in the
                                          			 list box.

Step 3

Select the service you want and click the Service Members tab .

Step 4

This step depends on whether you want to add or to remove skill
                                          			 groups:

To remove skill groups, select a skill group's name and click Remove .

To add skill groups, click Add and in the Add Service Member dialog, select the
                                                				  skill groups and click OK .

The available skill groups are all those defined for the
                                                   					 selected peripheral.

Step 5

In the Service Members tab, select the Primary check box for any skill groups that
                                          			 you want to be primary.

Step 6

When finished, in the Skill Group Explorer window, click Save .

## Skill Groups Per Agent Limit

Unified ICM and Unified CCE impose a default limit on the number of skill groups that you can assign to a single agent. Once
                              this limit is reached, more skill groups cannot be assigned.

You can use the
                              		  Configuration Limit Tool to specify your own limit on the number of skill
                              		  groups that can be assigned to an agent. For optimum performance, you can
                              		  specify a limit far lower than the system default. For performance
                              		  considerations in choosing a skill groups per agent limit, see the Solution Design Guide for Cisco Unified Contact Center Enterprise .

Warning

Setting a default value for skill groups per agent that is higher than the system default can adversely affect system performance.
                                          Cisco does not support configurations that exceed the default value.

Caution

The Configuration
                                          			 Limit tool is a command-line tool utility from the bin directory of all Unified
                                          			 ICM and Unified CCE Administration & Data Servers. Access is limited to
                                          			 users with privileges for the Setup or Config Groups in Active Directory for
                                          			 the chosen customer instance. For more information about the Configuration
                                          			 Limit tool, see the Outbound Option Guide for Unified Contact Center Enterprise .

### Change Skill Groups Per Agent Limit

To change the skill groups per agent limit using the Configuration Limit tool, complete the following steps:

#### Procedure

Step 1

From the Windows menu, select Start > Run , type configlimit , and then click Enter .

Note

Run the Configuration Limit tool on the same machine as the Distributor for the
                                                         				instance you want to configure. If more than one instance of the Administration
                                                         				& Data Server is installed on the Distributor machine, use the Select
                                                         				Administration Server tool to select the instance you want to configure.

Step 2

To view currently configured parameter limits, run the following command:

```
cl /show
```

Step 3

To change the  skill groups per agent limit, enter a command in the
                                          			 following format:

```
cl /id 1 /value [ConfigLimitCurrentValue] [/update]
```

Where:

id 1 = the ID of the  skill groups per agent limit.

ConfigLimitCurrentValue = the parameter limit. In this case, the parameter limit is the skill groups per agent limit.

For example, to change the skill groups per agent limit to 5,
                                             				enter the following:

```
cl /id 1 /value 5 /update
```

Note

Using the Configuration Limit tool, you can change the
                                                         				ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue.

### Additional Requirements

#### Lowering the Limit

If you have modified the skill groups per agent limit to be lower than
                                 		the system default, no additional changes are necessary. The new, lower limit
                                 		will be enforced immediately. Note that the new limit will not affect agents whose existing skill group membership exceeds
                                 		the new limit until the next attempt to add a new skill group for those agents.
                                 		At that time, the new limit will be enforced, preventing you from adding
                                 		additional skill groups.

#### Exceeding the Default Limit

If you modified the skill groups per agent limit to be higher than the system default (despite the preceding warning), certain
                                 deployments require additional changes to your system to use the new limit. These additional changes (listed in the following
                                 sections) also allow you to add more skill groups.

#### UCCE Gateway PG

For UCCE Gateway deployments, modify the following registry keys on your
                                 		UCCE Gateway PGs to include the new value. A change to the registry will
                                 		require that the PG service be restarted.

Cisco Unified Contact Center Enterprise Gateway Peripheral Interface Manager (PIM) ( Cisco Unified Contact Center Enterprise parent):

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<
                                    		customer_instance
                                    		>\PG{n}[A|B]\PG\CurrentVersion\PIMS\pim{m}\ACMIData\Config\MaxSkills

Cisco Unified Contact Center Express Gateway PIM ( Cisco Unified Contact Center Express parent):

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<
                                    		customer_instance
                                    		>\PG{n}[A|B]\PG\CurrentVersion\PIMS\pim{n}\ACMIData\Config\MaxSkills

## Persons

Associate every
                              		  agent with a person record. The person record stores the login name, first
                              		  name, last name, and password. On Unified ICM you can
                              		  have multiple agents per person. An agent is an "extension" of a
                              		  person on a given peripheral.

The Person List tool
                              		  allows you to list the persons currently defined in the Unified ICM database, to define new ones, and to view, edit, or delete the records of
                              		  existing ones.

Note

If you are using the Enterprise Chat and
                                                						Email feature, you can create Agents in CCE Configuration Manager. Creating Agents in
                                          			 the Enterprise Chat and
                                                						Email makes them available in Configuration Manager. However, if you create the agent
                                          			 in Configuration Manager, you must enable the agent in Enterprise Chat and
                                                						Email .

Available person
                              		  records are records that have not been mapped to any agent records (including
                              		  logically deleted ones) at the peripheral selected in the Agent Explorer. To
                              		  free a person associated with a logically deleted agent, use the Configuration
                              		  Manager's Deleted Objects tool to permanently delete the logically deleted
                              		  agent.

## Agents

An agent is a person who handles calls from a peripheral or supervises
                              		  those who do. You need to set up each agent associated with each peripheral.

An agent gadget is an application which handles calls from a peripheral. You need to set up each agent gadget associated with each peripheral.

Use the Configuration Manager's Agent Explorer to configure agents.

### Modify Agent Record

To view or modify agents records, follow these steps:

#### Procedure

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Agent Explorer . The Agent
                                          			 Explorer window appears.

Step 2

In the Select filter data box, select the peripheral
                                          			 with which the agent is associated. Enter any other filters you want and click Retrieve .

The retrieved enterprise names for the agents are displayed in the
                                             				list box.

Step 3

Select the agent name whose properties you want to view and use
                                          			 the tabs on the right side of the window to view the properties.

Step 4

Edit the properties appropriate. See the online help if you have
                                          			 questions.

Step 5

When finished, in the Agent Explorer window, click Save .

### Create an Agent

An agent is a person who handles calls from a peripheral or supervises
                                 		  those who do. You need to set up each agent associated with each peripheral.

When you create a new agent, you can also identify the agent as a supervisor.

Note

Caution

Out of Compliance expiry: The system is operating with an insufficient number of licenses and system in enforcement mode.

Authorization expiry: The system has not communicated with Cisco Smart Software Manager , or satellite for 90 days and the system has not automatically renewed the entitlement authorizations.

Evaluation expiry: The license evaluation period expired.

To create an agent:

#### Procedure

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Agent Explorer . The Agent
                                          			 Explorer window appears.

Step 2

In the Select filter data box, select the peripheral
                                          			 with which the agent is to associated and click Retrieve . This enables the Add Agent button.

Step 3

Click Add Agent .

Step 4

In the property tabs on the right side of the window, enter the appropriate property values. (See the online help for field
                                          definitions.) Use the Agent tab to define the agent (and optionally designate the agent as a supervisor) and the Skill Group
                                          Membership tab to map the agent to any skill groups.

Note

Step 5

When finished, click Save .

### Agent Configuration on the Child Central Controller

Access the Configuration Manager on the Child Administration & Data
                              		Server to configure agents.

#### Configure Agents on the Child Central Controller

Use the Configuration Manager Agent Explorer tool to configure agents
                                    		  on the Child Central Controller.

Note

When  you configure an agent on the Child Central Controller, the agent is automatically assigned to a default skill group.
                                                However, if you log onto the parent to view the agent (that you configured on the child), the default skill group appears
                                                in the list of assigned skill groups and not in the default skill group box.

To configure agents on the Child Central Controller:

##### Procedure

Step 1

Start the Agent Explorer tool .

Step 2

On the Main window of the Agent Explorer tool, click Retrieve .

Step 3

Click Add Agent .

The Agent tab appears.

Step 4

Complete all the fields except the Password and the Peripheral
                                             			 Name fields.

The agent name information appears in the list, as with all
                                                				Explorer tools.

Step 5

Repeat this process to add at least three agents.

Step 6

Click Save , and then Close to exit the Agent Explorer tool.

### Designate Agent
                           	 Supervisor

If you define an agent as a supervisor:

If single sign-on is disabled either globally or for the agent you want to designate as a supervisor, the supervisor must have an Active Directory account.
                                       If the supervisor does not have an Active Directory account, the designation fails.

If single sign-on is enabled either globally or for the agent you want to designate as a supervisor, you must enter the individual's name in the format
                                       that your identity provider requires.

To create an agent who is a supervisor:

#### Procedure

Step 1

In the
                                          			 Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Agent Explorer . The Agent Explorer
                                          			 window appears.

Step 2

In the Select
                                             				filter data box, select the peripheral with which the agent is to
                                          			 associated and click Retrieve . This enables the Add
                                             				Agent button.

Step 3

Click Add
                                             				Agent .

Note

You must add the agent supervisor, as both member and supervisor, to the Member tab on the agent team list. To get the benefit from the Team layout in Finesse, the agent supervisor must be a member of
                                                         the team.

Step 4

In the property tabs on the right side of the window, enter the appropriate property values. Use the Agent Tab to define the
                                          agent and designate the agent as a supervisor. Use the Skill Group Membership Tab to map the agent to any skill groups. (See
                                          the Configuration Manager online help for more information.)

Note

Step 5

When finished,
                                          			 click Save .

### Agent to Skill Group Assignment

After you have set up skill groups and agents, enter the assignments of
                              		agents to skill groups as configured for the peripheral. Each agent can belong
                              		to zero, one, or more skill groups.

You can use the Configuration Manager's Skill Group Explorer to map
                              		agents to skill groups.

#### Assign Agents to a Skill Group

Follow these steps to assign agents to a skill group:

##### Procedure

Step 1

Within the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > Agent Explorer . The Agent
                                             			 Explorer window appears.

Step 2

Select the filters you want and click Retrieve . The retrieved agents appear in the
                                             			 list box.

Step 3

Select the agent you want assign to a skill group and click the Skill Group Membership tab.

Step 4

This step depends on whether you want to add or remove an agent.
                                             			 On the 
                                             			 Skill group membership tab:

To remove the selected agent from a skill group, select the
                                                   				  appropriate skill group and click Remove .

To add the selected agent to a skill group, click Add , and in the 
                                                   				  Add Skill Group Member 
                                                   				  dialog, select the appropriate skill group and click OK .

Step 5

When finished, in the Agent Explorer window, click Save .

### Enable or Disable Agent Data at a Peripheral and Define an Agent Distribution

Follow these steps to enable/disable agent data at a peripheral and
                                 		  define an agent distribution:

#### Procedure

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > PG Explorer . The PG
                                          			 Explorer window appears.

Step 2

Click Retrieve .

Step 3

In the tree list box, expand the appropriate logical controller
                                          			 and select the peripheral.

Step 4

In the Agent Distribution tab, select or deselect the Enable agent reporting check box.

Step 5

In the Agent Distribution Entries list box, select an existing
                                          			 distribution site or create a new one by clicking New and entering values for the following
                                          			 fields:

Administration & Data Server site
                                                   					 name . The Admin site name for the Primary/Secondary Pair (Site)
                                                				  name, as specified in the Web Setup tool.

Agent real time data . If checked,
                                                				  enables the flow of agent real time data from the peripheral to the
                                                				  Administration & Data Server. Unchecked, disables the flow of agent real
                                                				  time data.

Agent historical data . If checked, enables the flow of
                                                				  agent historical data from the peripheral to the Administration & Data
                                                				  Server. Unchecked, disables the flow of agent historical data.

Step 6

Click Save to apply your changes.

### Agent State
                           	 Trace

You can set Agent State Trace to track every state (available, talking, and so on) that an agent passes through. To turn on
                                 this feature for an agent, in the Agent Explorer , on the Advanced tab, check the Agent State Trace check box.

Note

When you check the Enable agent reporting check box, configure the Agent distribution entries in the PG Explorer tool, and check the Agent State Trace check box, the Agent_State_Trace table in the database is populated.

### Agent Configuration Data from Peripheral

An automatic call distribution (ACD) requires all the available agents to be configured to allow the
                                 		  agents to log in to the call handling devices with their peripheral number
                                 		  (Agent ID) or peripheral name, password, and so on. Also, these agents are
                                 		  configured to handle specific categories of calls based on Skill Group. There are
                                 		  some other data elements configured on the ACD such as last name, first name, 
                                 		  and other class of services.

The Unified ICM Agent Level Reporting requires these agents to be configured in Unified ICM to identify them with full name, peripheral name,
                                 		  or enterprise name on both the real-time and historical reports.

The agentcfg.exe command line tool provides a process of configuring
                                 		  the agent configuration data elements available on an ACD into the Agent table
                                 		  in the Unified ICM database. This can also be automated by scheduling the process to
                                 		  run as an AT job at a specific time during a day. The frequency of scheduling
                                 		  the agent configuration process depends on your requirements.

Each peripheral requires the Agent configuration process to run.

#### Import Agent Data

Follow these steps to import agent data:

##### Procedure

Step 1

Retrieve the agent configuration data from the peripheral.

Step 2

Form all the information in a tab-delimited text file with one row
                                             			 per agent. Each row of the file must contain the following fields, in order:

PeripheralNumber FirstName LastName Description
                                                   				  PeripheralName

Step 3

To import data from the file into the system software, enter one
                                             			 of the following commands at the command prompt: AgentCfg <Peripheral ID or Peripheral Name> <Input
                                                				file name> [<Second input file>] [<Option>]

These variables are defined as:

<Peripheral ID or Peripheral Name>:

Peripheral ID or Peripheral Name of the peripheral that you
                                                      					 want to configure.

<Input file name>:

The name of the input file contains the agent or skill group
                                                      					 member configuration data on the ACD in the appropriate format (described in
                                                      					 the next section). The file must contain header information, otherwise the tool
                                                      					 assumes the data is for the Agent table.

Full or relative path is allowed.

<Second input file>:

If the first file contains Agent data, the second file must
                                                      					 contains Skill Group Member data. If the first file contained Skill Group Member
                                                      					 data, the second file must contain Agent data.

If no files contain headers, it is assumed that Agent data is
                                                      					 in the first file and Skill Group Member data is in the second file. If headers
                                                      					 are provided, the files may be specified in either order.

Full or relative path is allowed.

<Option>:

/show Only - show configuration changes without committing to
                                                      					 the database.

/nodelete - the tool will not perform any delete operations.
                                                      					 All inserts and updates will be saved.

Example:

AgentCfg.exe peripheral1 c:\temp\agentData.txt
                                                               						  c:\temp\skillGrpMemData.txt

This example will configure both agent and skill group
                                                            						  member data for peripheral1.

AgentCfg.exe peripheral1 c:\temp\skillGrpMemData.txt

This example will configure skill group member data for
                                                            						  peripheral. The file must contain header information.

Step 4

When the system software invokes the AgentCfg command, it performs
                                             			 the following steps for each line in the input file:

The following steps are performed for each line in the input file:

The system software attempts to match the PeripheralNumber
                                                      					 value to a configured agent for the peripheral.

If it finds a match, it proceeds directly to step b.

If it cannot find a match, it creates a new agent row in the
                                                      					 database using the data from the input file, and proceeds to step b.

The system software checks to see if the "temporary" flag is
                                                      					 set. If it is, it updates the existing record.

The system software checks whether the peripheral name values
                                                      					 also match.

If the FirstName and LastName values match, the system
                                                      					 software updates the existing record with the given Description and
                                                      					 PeripheralName values. (If the existing record was for a temporary agent, the
                                                      					 agent is no longer temporary after the update.)

If the values do not match, the system software marks the
                                                      					 existing record as deleted and inserts a new row with the data from the input
                                                      					 file. If an agent is configured for the peripheral in the database, but is not
                                                      					 listed in the input file, the system software marks the agent as deleted
                                                      					 in the database.

The system software does a loop through the Skill Group Member
                                                      					 input file container and compares the records in the file with those in the database:

If the record is found in the file but does not exist in the
                                                            						  database, the record is inserted.

If the record is found in the database but does not exist
                                                            						  in the file, the record is deleted.

#### Input File Formats

When using the AgentCfg.exe tool to import data, the input files must be
                                 		formatted as described below. Note that the _ _TABLE and _ _COLUMNS entries, and the
                                 		line below each are together considered the header. The header is not always required.
                                 		The beginning of this section indicates when headers are needed.

##### Agent Configuration Data File

The input file must contain the list of all the agents configured on
                                    		  the ACD for that peripheral in the following format:

_ _TABLE

Agent

Indicates the name of the table to which the data will be configured.
                                    		  The table name is always Agent (do not change this line).

_ _COLUMNS

Indicates the tab-delimited column names that correspond to the data
                                    		  values (do not change this line). The columns need to be in the order  shown
                                    		  below:

PeripheralNumber<tab>FirstName<tab>LastName<tab>Description<tab>PeripheralName

1045<tab>F1045<tab>L1045<tab>Auto Configured
                                       			 by Router<tab>F1045.L1045

1046<tab>F1046<tab>L1046<tab>Auto Configured
                                       			 by Router<tab>F1046.L1046

1047<tab>F1047<tab>L1047<tab>Auto Configured
                                       			 by

Router<tab>F1047.L1047<eof>

The following indicates the tab delimited data values that correspond to
                                    		  the column names:

1045<tab>F1045<tab>L1045<tab>Auto Configured
                                       			 by Router<tab>F1045.L1045

##### Skill Group Member Configuration Data File

Note that the __TABLE and __COLUMNS entries and the line below each are together
                                    		  considered the header. The header is not always required.

The input file contains the list of all the skill group member data as
                                    		  a relation between skill group and agents, which configured on the ACD for that
                                    		  peripheral in the following format:

_ _TABLE

Skill_Group_Member

Indicates the name of the table to which the data will be configured.
                                    		  The table name is always Skill_Group_Member (do not change this line).

_ _COLUMNS

Indicates the tab delimited column names that correspond to the data
                                    		  values (do not change this line). The columns need to be in the order shown below.

SkillGroupEnterpriseName <tab> AgentPeripheralNumber
                                       			 SkillGroupExterprise1<tab>1045 SkillGroupExterprise2<tab>1046
                                       			 SkillGroupExterprise1<tab>1046

SkillGroupEnterpriseName is the ExterpriseName of the skill group that the agent belongs to.

AgentPeripheralNumber is the agent's login ID assigned at the switch,
                                    		  which is the same as the above Agent Peripheral Number.

The following indicates the tab delimited data values that correspond to
                                    		  the column names:

SkillGroupExterprise1<tab>1045

#### Manage Security

The system generates agent passwords using advanced hashing.

Advanced hashing helps you to ensure greater security of agent passwords in non-SSO mode. To enforce advanced hashing of agent
                                 passwords, you must enable the Enforce button under the tab, Manage Security .

Note

Local and Setup Administrators can perform enforcement.

Before you enforce the global switch, consider the following to ensure that the agent authentication is successful.

All the PG's must be version 12.6 (1) or later.

All the agent passwords must be re-entered.

When you disable Enforce , the system authenticates passwords using old and advanced hashing. When you enable Enforce , the system authenticates passwords only using advanced hashing.

Note

You will be able to disable the global switch from the API. For more information, on how to disable the global switch in UCCE
                                             deployment, see Agent Security API at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html

## Enterprise Data

Within a script, you often want to examine a set of possible targets
                              		  on different peripherals before deciding where to send the call. For example,
                              		  if you are routing a sales call, you might want to check the Sales skill groups
                              		  at each call center to find which has the longest available agent or shortest
                              		  expected delay.

An enterprise service is a set of services that can be referenced in a
                              		  script. The individual services can be associated with different peripherals.
                              		  Similarly, an enterprise skill group is a set of skill groups that can be
                              		  referenced in a script. The individual skill groups can be associated with
                              		  different peripherals.

In addition to using them within a script, you can track enterprise
                              		  services and enterprise skill groups through monitoring screens and reports.
                              		  This allows you to easily follow the performance, for example, of all Support
                              		  services within the system.

### Enterprise Services

Within a routing script, you can use an enterprise service as a
                                 		  shorthand for a set of services. You might want to scan several services to
                                 		  find, for example, the service with the shortest expected delay. Within the
                                 		  script, you can specify individual services to scan or, if you have an
                                 		  enterprise service defined, you can simply specify the enterprise service.

### Assign Specific Services

Follow these steps to create an enterprise service and assign specific
                                 		  services:

#### Procedure

Step 1

In the Configuration Manager menu, select Tools > List
                                                				  Tools > Enterprise Service List .
                                          			 The Enterprise Service List window appears.

Step 2

In the Select filter data box, select the filters you want and
                                          			 click the Members tab. This enables the Add button and lists the currently defined
                                          			 enterprise services for the selected business entities.

Step 3

Click Add .

Step 4

In the Attributes tab, enter values for the following fields:

Name . A name for the enterprise
                                                				  service. This name must be unique among all enterprise services in the system.

Business Entity . Reserved for future use.

Description . Any other information you
                                                				  want about the enterprise service. Any other information you want to add about the
                                                				  enterprise service.

Step 5

Click Save to save the changes.

Step 6

Click the Attribute tab.

Step 7

In the Attribute tab, click Add .

Step 8

In the Add Services dialog, select the services you want to add and click OK . The dialog closes and the selected services are listed as members in the Attribute tab.

Step 9

When finished, click Save to save the changes.

### Enterprise Skill Groups

Just as you can use an enterprise service as a shorthand for a
                                 		  collection of services, so you can use an enterprise skill group as a shorthand
                                 		  for a collection of skill groups. The skill groups can be defined on different
                                 		  peripherals.

### Create an enterprise skill group

Follow these steps to create an enterprise skill group:

#### Procedure

Step 1

In the Configuration Manager menu, select Tools > List
                                                				  Tools > Enterprise Skill Groups
                                                				  List . The Enterprise Skill Group List window appears.

Step 2

In the Select filter data box, select the filters you want and
                                          			 click Retrieve . This enables the Add button and lists the currently defined
                                          			 skill groups for the selected business entities.

Step 3

Click Add , and in the Attributes tab, enter values for the following
                                          			 fields:

Name . A name for the enterprise skill
                                                				  group. This name must be unique among all enterprise skill groups in the
                                                				  system.

Business Entity . Reserved for future use.

Description . Any other information you want to add 
                                                				  about the enterprise skill group.

Step 4

Click Save to save the changes.

Step 5

Click the Members tab.

Step 6

In the Members tab, click Add .

Step 7

In the Add Enterprise Skill Group Member dialog, select the skill
                                          			 groups you want to add and click OK . The dialog closes and the selected skill
                                          			 groups are listed as members in the Members tab.

Note

The Skill Group list includes base skill groups as well as
                                                         				primary and secondary groups for those switches that support them. Typically,
                                                         				add either the base group or the associated primary and secondary groups, but
                                                         				not all three, to the enterprise skill group.

Step 8

Click Save to save the changes to the database.

## Precision Queue
                        	 Configuration

Precision queues are
                           		a combination of steps that include attributes, defined terms for the selected
                           		attributes, wait times, and Consider If formulas.

Precision queues are configured using the CCEAdmin > Organization Setup > Skills > Precision Queue

For more information on precision queues and precision routing, see the Cisco Unified Contact Center Enterprise Features Guide at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_feature_guides_list.html .

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > Service Explorer . The
                                             			 Service Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the peripheral
                                             			 associated with the service you want to view. You can choose the name from the
                                             			 drop-down list. Note Once you have saved a service record to the Unified ICM database, you cannot change the peripheral to which it is
                                                            				associated. | Note | Once you have saved a service record to the Unified ICM database, you cannot change the peripheral to which it is
                                                            				associated. |
| Note | Once you have saved a service record to the Unified ICM database, you cannot change the peripheral to which it is
                                                            				associated. |
| Step 3 | Select any other filters you want. None in the Optional filter box means all services associated
                                             			 with the selected peripheral will be displayed. |
| Step 4 | Click Retrieve . This lists in the tree list
                                             			 box the names of retrieved services. Note A tree object is unassigned if it was made by another
                                                            				configuration tool and was not assigned (mapped) to a parent object; for
                                                            				example, a label might not have been assigned to a peripheral target or a route
                                                            				might not have been assigned to a service, and so on. | Note | A tree object is unassigned if it was made by another
                                                            				configuration tool and was not assigned (mapped) to a parent object; for
                                                            				example, a label might not have been assigned to a peripheral target or a route
                                                            				might not have been assigned to a service, and so on. |
| Note | A tree object is unassigned if it was made by another
                                                            				configuration tool and was not assigned (mapped) to a parent object; for
                                                            				example, a label might not have been assigned to a peripheral target or a route
                                                            				might not have been assigned to a service, and so on. |
| Step 5 | In the tree list box, select a service to display its
                                             			 configuration information on the right side of the window. |
| Step 6 | If the service has a route associated with it, click its icon in
                                             			 the tree list box to display its configuration information. Do the same for a
                                             			 peripheral target associated with the route and a label associated with the
                                             			 peripheral target. |

| Note | Once you have saved a service record to the Unified ICM database, you cannot change the peripheral to which it is
                                                            				associated. |
|---|---|

| Note | A tree object is unassigned if it was made by another
                                                            				configuration tool and was not assigned (mapped) to a parent object; for
                                                            				example, a label might not have been assigned to a peripheral target or a route
                                                            				might not have been assigned to a service, and so on. |
|---|---|

| Step 1 | Follow the steps for viewing a service. |
|---|---|
| Step 2 | Edit the configuration information. Note You cannot modify fields that are greyed out. With the mouse, you can select an object and then move it to
                                                				another part of the tree, as long as its object type belongs in that tree
                                                				location. For example, to move a route to another service, select it and then
                                                				move the pointer to that service. When that service becomes highlighted, lift
                                                				your finger off the mouse. You can also use the Bulk Configuration tool to take
                                                				the output of a switch and create 20 or 30 labels. Then, using the Service
                                                				Explorer, you can attach the labels to an appropriate location. When you make a modification, the Changed icon appears next to the selected
                                                				item in the tree list box. | Note | You cannot modify fields that are greyed out. |
| Note | You cannot modify fields that are greyed out. |
| Step 3 | Click Save . |

| Note | You cannot modify fields that are greyed out. |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > Service Explorer . The
                                             			 Service Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box of the Explorer window, click Retrieve . This enables the Add Service button. |
| Step 3 | Click Add Service . A new service appears in the tree
                                             			 list box with a To Be Inserted icon next to it. Tabbed fields also appear on the right for the new
                                                				service's configuration information. |
| Step 4 | Fill in the tabbed fields. |
| Step 5 | Click Add Route and fill in its configuration
                                             			 records. |
| Step 6 | Click Add Peripheral Target and also Add Label and fill in those records. Selecting an item in the tree list box enables the Add button for more items of that type and
                                                				for the associated item immediately beneath it in the tree, if it can have one. |
| Step 7 | If desired, set security settings on the records. |
| Step 8 | Click Save . |

| Step 1 | In the Explorer tree list box, select the item or associated items
                                             			 whose records you want to delete. Note Deleting any item in the tree list box with branches beneath it
                                                         				also deletes those branches. For example, if you delete a service, you also
                                                         				delete its associated route, peripheral target, and label, if it has such. Deleting a label deletes only that label. | Note | Deleting any item in the tree list box with branches beneath it
                                                         				also deletes those branches. For example, if you delete a service, you also
                                                         				delete its associated route, peripheral target, and label, if it has such. Deleting a label deletes only that label. |
|---|---|---|---|
| Note | Deleting any item in the tree list box with branches beneath it
                                                         				also deletes those branches. For example, if you delete a service, you also
                                                         				delete its associated route, peripheral target, and label, if it has such. Deleting a label deletes only that label. |
| Step 2 | Click Delete . This places a Marked for Deletion icon next to the selected item in
                                             			 the tree list box. This also toggles the Delete button to Undelete . To undelete an item marked for deletion, select it in the tree
                                                				list box and click Undelete . |
| Step 3 | Click Save . This deletes from the database items marked for deletion and
                                                				removes them from the tree list box. Once you do this, you cannot undelete
                                                				deleted items. |

| Note | Deleting any item in the tree list box with branches beneath it
                                                         				also deletes those branches. For example, if you delete a service, you also
                                                         				delete its associated route, peripheral target, and label, if it has such. Deleting a label deletes only that label. |
|---|---|

| Step 1 | In the Configuration Manager's menu, select Tools > Explorer
                                                   				  Tools > Skill Group Explorer . The
                                             			 Skill Group Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the peripheral
                                             			 associated with the skill group you want to view. You can choose the name from
                                             			 the drop-down list of peripheral enterprise names. |
| Step 3 | Select any other filters you want. None in the Optional filter box
                                             			 means all skill groups associated with the selected peripheral will be
                                             			 displayed. |
| Step 4 | Click Retrieve . This lists in the tree list
                                             			 box names of skill groups. |
| Step 5 | In the tree list box, select a skill group to display its
                                             			 configuration information on the right side of the window. |
| Step 6 | If the skill group has a route associated with it, click its icon
                                             			 in the tree list box to display its configuration information. Do the same for
                                             			 a peripheral target associated with the route and a label associated with the
                                             			 peripheral target. Note A tree object is unassigned if it was made by another
                                                         				configuration tool and was not assigned (mapped) to a parent object; for
                                                         				example, a label might not have been assigned to a peripheral target or a route
                                                         				might not have been assigned to a service, and so on. | Note | A tree object is unassigned if it was made by another
                                                         				configuration tool and was not assigned (mapped) to a parent object; for
                                                         				example, a label might not have been assigned to a peripheral target or a route
                                                         				might not have been assigned to a service, and so on. |
| Note | A tree object is unassigned if it was made by another
                                                         				configuration tool and was not assigned (mapped) to a parent object; for
                                                         				example, a label might not have been assigned to a peripheral target or a route
                                                         				might not have been assigned to a service, and so on. |

| Note | A tree object is unassigned if it was made by another
                                                         				configuration tool and was not assigned (mapped) to a parent object; for
                                                         				example, a label might not have been assigned to a peripheral target or a route
                                                         				might not have been assigned to a service, and so on. |
|---|---|

| Step 1 | Follow the steps to view a skill group. |
|---|---|
| Step 2 | Edit the configuration information. With the mouse, you can select an object and move it to
                                             				another part of the tree, as long as its object type belongs in that tree
                                             				location. For example, to move a route to another skill group, select it and
                                             				move the pointer to that skill group. When that skill group becomes
                                             				highlighted, lift your finger off the mouse. You can also use the Bulk
                                             				Configuration tool to take the output of a switch and create 20 or 30 labels.
                                             				Then, using the Explorer, you can attach the labels to an appropriate location. Note You cannot modify fields that are greyed out. You cannot update the Peripheral field. 
                                                         			 To modify the Peripheral Number, you can use the Cisco Unified Contact Center Management Portal (CCMP). When you make a modification, the Changed icon appears next to the selected item
                                             				in the tree list box. | Note | You cannot modify fields that are greyed out. You cannot update the Peripheral field. 
                                                         			 To modify the Peripheral Number, you can use the Cisco Unified Contact Center Management Portal (CCMP). |
| Note | You cannot modify fields that are greyed out. You cannot update the Peripheral field. 
                                                         			 To modify the Peripheral Number, you can use the Cisco Unified Contact Center Management Portal (CCMP). |
| Step 3 | Click Save . The modified data is saved in the Unified ICM database and the Changed icon is removed from the edited object in the tree
                                             				list box. |

| Note | You cannot modify fields that are greyed out. You cannot update the Peripheral field. 
                                                         			 To modify the Peripheral Number, you can use the Cisco Unified Contact Center Management Portal (CCMP). |
|---|---|

| Note | Skill groups on the Child Central Controller contains an example of how to configure skill groups for a child deployment. |
|---|---|

| Step 1 | In the
                                          			 Configuration Manager's menu, select Tools > Explorer
                                                				  Tools > Skill Group Explorer . The Skill Group
                                          			 Explorer window appears. |
|---|---|
| Step 2 | In the Select filter
                                             				data area of the Explorer window, click Retrieve . This enables the Add
                                             				Skill Group button. |
| Step 3 | Click Add
                                             				Skill Group . A new skill group appears in the tree list box with a To Be
                                             				Inserted icon next to it. Tabbed fields also appear on the right for the
                                          			 new skill group's configuration information. |
| Step 4 | Fill in the
                                          			 tabbed fields. Note These fields
                                                         				  are not automatically populated. | Note | These fields
                                                         				  are not automatically populated. |
| Note | These fields
                                                         				  are not automatically populated. |
| Step 5 | Click Add
                                             				Route and fill in its configuration records. |
| Step 6 | Click Add
                                             				Peripheral Target and also Add
                                             				Label and fill in those records. Selecting an
                                             				item in the tree list box enables the Add button for more items of that type and for the
                                             				associated item immediately beneath it in the tree, if it can have one. |
| Step 7 | If desired, set
                                          			 security settings on the records. |
| Step 8 | Click Save . |

| Note | These fields
                                                         				  are not automatically populated. |
|---|---|

| Step 1 | Start the Skill Group Explorer Tool . |
|---|---|
| Step 2 | On the Main window of the Agent Explorer Tool, click Retrieve . |
| Step 3 | Click Add Skill Group . The Skill Group tab appears. |
| Step 4 | Complete all the fields and click OK . The skill group name appears in the list, as with all Explorer
                                                				tools. |
| Step 5 | Select the Skill Group Member tab and click Add . The Add Skill Group Member dialog appears. |
| Step 6 | Select the agents to add to the skill group, then click OK . The agents become members of the skill group. |
| Step 7 | Select the skill group in the tree list, then click Add Route . The Route tab appears. |
| Step 8 | Provide the Route Name and click Save . The route name appears in the tree list and the skill group is
                                                				added to the peripheral. |
| Step 9 | Repeat this to add one more skill group. |
| Step 10 | Click Save , then Close to exit the Skill Group Explorer Tool. |

| Step 1 | Within the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Service Explorer . The
                                          			 Service Explorer window appears. |
|---|---|
| Step 2 | Select the filters you want and click Retrieve . The retrieved services appear in the
                                          			 list box. |
| Step 3 | Select the service you want and click the Service Members tab . |
| Step 4 | This step depends on whether you want to add or to remove skill
                                          			 groups: To remove skill groups, select a skill group's name and click Remove . To add skill groups, click Add and in the Add Service Member dialog, select the
                                                				  skill groups and click OK . The available skill groups are all those defined for the
                                                   					 selected peripheral. |
| Step 5 | In the Service Members tab, select the Primary check box for any skill groups that
                                          			 you want to be primary. |
| Step 6 | When finished, in the Skill Group Explorer window, click Save . |

| Warning | Setting a default value for skill groups per agent that is higher than the system default can adversely affect system performance.
                                          Cisco does not support configurations that exceed the default value. |
|---|---|

| Caution | The Configuration
                                          			 Limit tool is a command-line tool utility from the bin directory of all Unified
                                          			 ICM and Unified CCE Administration & Data Servers. Access is limited to
                                          			 users with privileges for the Setup or Config Groups in Active Directory for
                                          			 the chosen customer instance. For more information about the Configuration
                                          			 Limit tool, see the Outbound Option Guide for Unified Contact Center Enterprise . |
|---|---|

| Step 1 | From the Windows menu, select Start > Run , type configlimit , and then click Enter . Note Run the Configuration Limit tool on the same machine as the Distributor for the
                                                         				instance you want to configure. If more than one instance of the Administration
                                                         				& Data Server is installed on the Distributor machine, use the Select
                                                         				Administration Server tool to select the instance you want to configure. | Note | Run the Configuration Limit tool on the same machine as the Distributor for the
                                                         				instance you want to configure. If more than one instance of the Administration
                                                         				& Data Server is installed on the Distributor machine, use the Select
                                                         				Administration Server tool to select the instance you want to configure. |
|---|---|---|---|
| Note | Run the Configuration Limit tool on the same machine as the Distributor for the
                                                         				instance you want to configure. If more than one instance of the Administration
                                                         				& Data Server is installed on the Distributor machine, use the Select
                                                         				Administration Server tool to select the instance you want to configure. |
| Step 2 | To view currently configured parameter limits, run the following command: cl /show |
| Step 3 | To change the  skill groups per agent limit, enter a command in the
                                          			 following format: cl /id 1 /value [ConfigLimitCurrentValue] [/update] Where: id 1 = the ID of the  skill groups per agent limit. ConfigLimitCurrentValue = the parameter limit. In this case, the parameter limit is the skill groups per agent limit. For example, to change the skill groups per agent limit to 5,
                                             				enter the following: cl /id 1 /value 5 /update Note Using the Configuration Limit tool, you can change the
                                                         				ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. | Note | Using the Configuration Limit tool, you can change the
                                                         				ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. |
| Note | Using the Configuration Limit tool, you can change the
                                                         				ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. |

| Note | Run the Configuration Limit tool on the same machine as the Distributor for the
                                                         				instance you want to configure. If more than one instance of the Administration
                                                         				& Data Server is installed on the Distributor machine, use the Select
                                                         				Administration Server tool to select the instance you want to configure. |
|---|---|

| Note | Using the Configuration Limit tool, you can change the
                                                         				ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. |
|---|---|

| Note | If you are using the Enterprise Chat and
                                                						Email feature, you can create Agents in CCE Configuration Manager. Creating Agents in
                                          			 the Enterprise Chat and
                                                						Email makes them available in Configuration Manager. However, if you create the agent
                                          			 in Configuration Manager, you must enable the agent in Enterprise Chat and
                                                						Email . |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Agent Explorer . The Agent
                                          			 Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the peripheral
                                          			 with which the agent is associated. Enter any other filters you want and click Retrieve . The retrieved enterprise names for the agents are displayed in the
                                             				list box. |
| Step 3 | Select the agent name whose properties you want to view and use
                                          			 the tabs on the right side of the window to view the properties. |
| Step 4 | Edit the properties appropriate. See the online help if you have
                                          			 questions. |
| Step 5 | When finished, in the Agent Explorer window, click Save . |

| Note | Agent Configuration on the Child Central Controller contains an example of how to configure agents for a child deployment. |
|---|---|

| Caution | Adding an agent is no longer allowed, in the following conditions: Out of Compliance expiry: The system is operating with an insufficient number of licenses and system in enforcement mode. Authorization expiry: The system has not communicated with Cisco Smart Software Manager , or satellite for 90 days and the system has not automatically renewed the entitlement authorizations. Evaluation expiry: The license evaluation period expired. |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Agent Explorer . The Agent
                                          			 Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the peripheral
                                          			 with which the agent is to associated and click Retrieve . This enables the Add Agent button. |
| Step 3 | Click Add Agent . |
| Step 4 | In the property tabs on the right side of the window, enter the appropriate property values. (See the online help for field
                                          definitions.) Use the Agent tab to define the agent (and optionally designate the agent as a supervisor) and the Skill Group
                                          Membership tab to map the agent to any skill groups. Note An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. | Note | An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. |
| Note | An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. |
| Step 5 | When finished, click Save . |

| Note | An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. |
|---|---|

| Note | When  you configure an agent on the Child Central Controller, the agent is automatically assigned to a default skill group.
                                                However, if you log onto the parent to view the agent (that you configured on the child), the default skill group appears
                                                in the list of assigned skill groups and not in the default skill group box. |
|---|---|

| Step 1 | Start the Agent Explorer tool . |
|---|---|
| Step 2 | On the Main window of the Agent Explorer tool, click Retrieve . |
| Step 3 | Click Add Agent . The Agent tab appears. |
| Step 4 | Complete all the fields except the Password and the Peripheral
                                             			 Name fields. The agent name information appears in the list, as with all
                                                				Explorer tools. |
| Step 5 | Repeat this process to add at least three agents. |
| Step 6 | Click Save , and then Close to exit the Agent Explorer tool. |

| Step 1 | In the
                                          			 Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Agent Explorer . The Agent Explorer
                                          			 window appears. |
|---|---|
| Step 2 | In the Select
                                             				filter data box, select the peripheral with which the agent is to
                                          			 associated and click Retrieve . This enables the Add
                                             				Agent button. |
| Step 3 | Click Add
                                             				Agent . Note You must add the agent supervisor, as both member and supervisor, to the Member tab on the agent team list. To get the benefit from the Team layout in Finesse, the agent supervisor must be a member of
                                                         the team. | Note | You must add the agent supervisor, as both member and supervisor, to the Member tab on the agent team list. To get the benefit from the Team layout in Finesse, the agent supervisor must be a member of
                                                         the team. |
| Note | You must add the agent supervisor, as both member and supervisor, to the Member tab on the agent team list. To get the benefit from the Team layout in Finesse, the agent supervisor must be a member of
                                                         the team. |
| Step 4 | In the property tabs on the right side of the window, enter the appropriate property values. Use the Agent Tab to define the
                                          agent and designate the agent as a supervisor. Use the Skill Group Membership Tab to map the agent to any skill groups. (See
                                          the Configuration Manager online help for more information.) Note An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. | Note | An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. |
| Note | An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. |
| Step 5 | When finished,
                                          			 click Save . |

| Note | You must add the agent supervisor, as both member and supervisor, to the Member tab on the agent team list. To get the benefit from the Team layout in Finesse, the agent supervisor must be a member of
                                                         the team. |
|---|---|

| Note | An agent team can have only one primary supervisor. There is no upper limit to the number of secondary supervisors for a team.
                                                      Refer to the online help for instructions on how to assign a primary supervisor. |
|---|---|

| Step 1 | Within the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > Agent Explorer . The Agent
                                             			 Explorer window appears. |
|---|---|
| Step 2 | Select the filters you want and click Retrieve . The retrieved agents appear in the
                                             			 list box. |
| Step 3 | Select the agent you want assign to a skill group and click the Skill Group Membership tab. |
| Step 4 | This step depends on whether you want to add or remove an agent.
                                             			 On the 
                                             			 Skill group membership tab: To remove the selected agent from a skill group, select the
                                                   				  appropriate skill group and click Remove . To add the selected agent to a skill group, click Add , and in the 
                                                   				  Add Skill Group Member 
                                                   				  dialog, select the appropriate skill group and click OK . |
| Step 5 | When finished, in the Agent Explorer window, click Save . |

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > PG Explorer . The PG
                                          			 Explorer window appears. |
|---|---|
| Step 2 | Click Retrieve . |
| Step 3 | In the tree list box, expand the appropriate logical controller
                                          			 and select the peripheral. |
| Step 4 | In the Agent Distribution tab, select or deselect the Enable agent reporting check box. |
| Step 5 | In the Agent Distribution Entries list box, select an existing
                                          			 distribution site or create a new one by clicking New and entering values for the following
                                          			 fields: Administration & Data Server site
                                                   					 name . The Admin site name for the Primary/Secondary Pair (Site)
                                                				  name, as specified in the Web Setup tool. Agent real time data . If checked,
                                                				  enables the flow of agent real time data from the peripheral to the
                                                				  Administration & Data Server. Unchecked, disables the flow of agent real
                                                				  time data. Agent historical data . If checked, enables the flow of
                                                				  agent historical data from the peripheral to the Administration & Data
                                                				  Server. Unchecked, disables the flow of agent historical data. |
| Step 6 | Click Save to apply your changes. |

| Note | When you enable Agent State Trace, the system tracks every state change for each agent you select. This puts an added load
                                          on system software resources, such as network bandwidth and database space, and can impact system performance. You may only
                                          track up to 100 agents with Agent State Trace at any one time. You should also take the added load into account when planning
                                          your system capacity. |
|---|---|

| Step 1 | Retrieve the agent configuration data from the peripheral. |
|---|---|
| Step 2 | Form all the information in a tab-delimited text file with one row
                                             			 per agent. Each row of the file must contain the following fields, in order: PeripheralNumber FirstName LastName Description
                                                   				  PeripheralName |
| Step 3 | To import data from the file into the system software, enter one
                                             			 of the following commands at the command prompt: AgentCfg <Peripheral ID or Peripheral Name> <Input
                                                				file name> [<Second input file>] [<Option>] These variables are defined as: <Peripheral ID or Peripheral Name>: Peripheral ID or Peripheral Name of the peripheral that you
                                                      					 want to configure. <Input file name>: The name of the input file contains the agent or skill group
                                                      					 member configuration data on the ACD in the appropriate format (described in
                                                      					 the next section). The file must contain header information, otherwise the tool
                                                      					 assumes the data is for the Agent table. Full or relative path is allowed. <Second input file>: If the first file contains Agent data, the second file must
                                                      					 contains Skill Group Member data. If the first file contained Skill Group Member
                                                      					 data, the second file must contain Agent data. If no files contain headers, it is assumed that Agent data is
                                                      					 in the first file and Skill Group Member data is in the second file. If headers
                                                      					 are provided, the files may be specified in either order. Full or relative path is allowed. <Option>: /show Only - show configuration changes without committing to
                                                      					 the database. /nodelete - the tool will not perform any delete operations.
                                                      					 All inserts and updates will be saved. Example: AgentCfg.exe peripheral1 c:\temp\agentData.txt
                                                               						  c:\temp\skillGrpMemData.txt This example will configure both agent and skill group
                                                            						  member data for peripheral1. AgentCfg.exe peripheral1 c:\temp\skillGrpMemData.txt This example will configure skill group member data for
                                                            						  peripheral. The file must contain header information. |
| Step 4 | When the system software invokes the AgentCfg command, it performs
                                             			 the following steps for each line in the input file: The following steps are performed for each line in the input file: The system software attempts to match the PeripheralNumber
                                                      					 value to a configured agent for the peripheral. If it finds a match, it proceeds directly to step b. If it cannot find a match, it creates a new agent row in the
                                                      					 database using the data from the input file, and proceeds to step b. The system software checks to see if the "temporary" flag is
                                                      					 set. If it is, it updates the existing record. The system software checks whether the peripheral name values
                                                      					 also match. If the FirstName and LastName values match, the system
                                                      					 software updates the existing record with the given Description and
                                                      					 PeripheralName values. (If the existing record was for a temporary agent, the
                                                      					 agent is no longer temporary after the update.) If the values do not match, the system software marks the
                                                      					 existing record as deleted and inserts a new row with the data from the input
                                                      					 file. If an agent is configured for the peripheral in the database, but is not
                                                      					 listed in the input file, the system software marks the agent as deleted
                                                      					 in the database. The system software does a loop through the Skill Group Member
                                                      					 input file container and compares the records in the file with those in the database: If the record is found in the file but does not exist in the
                                                            						  database, the record is inserted. If the record is found in the database but does not exist
                                                            						  in the file, the record is deleted. |

| Note | Local and Setup Administrators can perform enforcement. |
|---|---|

| Note | You will be able to disable the global switch from the API. For more information, on how to disable the global switch in UCCE
                                             deployment, see Agent Security API at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > List
                                                				  Tools > Enterprise Service List .
                                          			 The Enterprise Service List window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the filters you want and
                                          			 click the Members tab. This enables the Add button and lists the currently defined
                                          			 enterprise services for the selected business entities. |
| Step 3 | Click Add . |
| Step 4 | In the Attributes tab, enter values for the following fields: Name . A name for the enterprise
                                                				  service. This name must be unique among all enterprise services in the system. Business Entity . Reserved for future use. Description . Any other information you
                                                				  want about the enterprise service. Any other information you want to add about the
                                                				  enterprise service. |
| Step 5 | Click Save to save the changes. |
| Step 6 | Click the Attribute tab. |
| Step 7 | In the Attribute tab, click Add . |
| Step 8 | In the Add Services dialog, select the services you want to add and click OK . The dialog closes and the selected services are listed as members in the Attribute tab. |
| Step 9 | When finished, click Save to save the changes. |

| Step 1 | In the Configuration Manager menu, select Tools > List
                                                				  Tools > Enterprise Skill Groups
                                                				  List . The Enterprise Skill Group List window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the filters you want and
                                          			 click Retrieve . This enables the Add button and lists the currently defined
                                          			 skill groups for the selected business entities. |
| Step 3 | Click Add , and in the Attributes tab, enter values for the following
                                          			 fields: Name . A name for the enterprise skill
                                                				  group. This name must be unique among all enterprise skill groups in the
                                                				  system. Business Entity . Reserved for future use. Description . Any other information you want to add 
                                                				  about the enterprise skill group. |
| Step 4 | Click Save to save the changes. |
| Step 5 | Click the Members tab. |
| Step 6 | In the Members tab, click Add . |
| Step 7 | In the Add Enterprise Skill Group Member dialog, select the skill
                                          			 groups you want to add and click OK . The dialog closes and the selected skill
                                          			 groups are listed as members in the Members tab. Note The Skill Group list includes base skill groups as well as
                                                         				primary and secondary groups for those switches that support them. Typically,
                                                         				add either the base group or the associated primary and secondary groups, but
                                                         				not all three, to the enterprise skill group. | Note | The Skill Group list includes base skill groups as well as
                                                         				primary and secondary groups for those switches that support them. Typically,
                                                         				add either the base group or the associated primary and secondary groups, but
                                                         				not all three, to the enterprise skill group. |
| Note | The Skill Group list includes base skill groups as well as
                                                         				primary and secondary groups for those switches that support them. Typically,
                                                         				add either the base group or the associated primary and secondary groups, but
                                                         				not all three, to the enterprise skill group. |
| Step 8 | Click Save to save the changes to the database. |

| Note | The Skill Group list includes base skill groups as well as
                                                         				primary and secondary groups for those switches that support them. Typically,
                                                         				add either the base group or the associated primary and secondary groups, but
                                                         				not all three, to the enterprise skill group. |
|---|---|