---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-8ed291a672
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_1501_configuration-guide-for-cisco-unified-icm-enterprise-release/ucce_m_1501_network-ivrs-vrus.html
retrieved_at: 2026-08-16T14:33:58.241488+00:00
---

Configuration Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Configuration Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Network IVRs/VRUs

## Chapter: Network IVRs/VRUs

# Network IVRs/VRUs

## VRU Configuration Tools

### Network VRU Explorer
                           	 Tool

This tool allows a
                                 		  network applications manager (NAM) to view, edit, or define network VRUs,
                                 		  labels, and their associations. The system software can send a customer call to
                                 		  a network VRU.

Note

To begin, select the
                                 		  filters you want and click Retrieve .

The changes you make
                                 		  in the Network VRU Explorer window are not applied to the database until you
                                 		  click Save .

#### Select Filter Data
                              	 Box

Use the Select filter
                                 		data box to select and retrieve data from the database. Until you retrieve
                                 		database data, no data is displayed.

##### Network VRU Label
                                 	 Tree

Hide/Show legend

This button toggles
                                    		between Hide and Show .
                                    		Click to hide or show a diagram identifying all the objects that can be
                                    		displayed in the tree list box and showing their hierarchy.

Tree list box

The tree list box
                                    		displays the names of the retrieved Network VRUs and, when expanded, the labels
                                    		associated with them.

When you select an
                                    		item within the tree, details about that item appear in the tabbed property
                                    		fields to the right of the tree list box.

Tree list box
                                    		properties

Expanding
                                          			 (+)/contracting (-) the tree (+ and – buttons)

Displaying option
                                          			 menu (right mouse button clicking)

Making tree
                                          			 connections (drag and drop)

With the mouse,
                                          			 you can select an object and move it to another part of the tree, as long as
                                          			 its object type belongs in that tree location.

For example, to
                                          			 move a route to another service, select it by clicking the left mouse button,
                                          			 and move the pointer to that service. When that service becomes highlighted,
                                          			 lift your finger off the mouse. You could also use the Bulk Configuration tool
                                          			 to take the output of a switch and create 20 or 30 labels. Then, using one of
                                          			 the Explorer tools, you could attach these UNASSIGNED labels to an appropriate
                                          			 location.

Symbols indicating object state (see Explorer, Bulk, and List Tools Common Features )

UNASSIGNED tree
                                          			 objects

A tree object is
                                          			 marked UNASSIGNED if it was made by another configuration tool and was not
                                          			 assigned (mapped) to a parent object.

For example, a
                                          			 label might not have been assigned to a peripheral target or a route might not
                                          			 have been assigned to a service.

With the mouse,
                                          			 you can select an UNASSIGNED object and move it to a tree branch, as long as
                                          			 it's an object that belongs in that tree location. Use the window legend to see
                                          			 what objects belong where.

When you move an
                                          			 UNASSIGNED object to an appropriate tree-branch location, you assign that
                                          			 object to the object above it in the tree. Then the object is no longer
                                          			 unassigned. For example, in this way you might assign an unassigned label to a
                                          			 peripheral target.

Button

Description

Add

When an object
                                                				in the tree is selected, you can add another object of the same kind or an
                                                				object immediately below it in the tree hierarchy. The Add buttons are enabled accordingly.

Add Network
                                                   				  VRU

Click to add a
                                                				network VRU to the database.

Add
                                                   				  Label

Click to add a
                                                				label to the selected network VRU.

Delete

Click to
                                                				delete the selected object in the tree. This marks the selected object for
                                                				deletion. When you click Save ,
                                                				the object is deleted from the database.

If a network
                                                				VRU is selected, it and the labels associated with it are marked for deletion.
                                                				If a label is selected, only that label's record is marked for deletion.

Undelete

The Delete button toggles to Undelete when you select an object marked for deletion. To undelete an object marked for
                                                				deletion, select it and click Undelete.

ID status
                                                   				  box

The label in the ID box at the bottom of the screen identifies the Unified ICM system on which you are working.

##### Network VRU Tab

The Network VRU tab allows you to view (and define or edit, if you have maintenance access)
                                    		the properties of the selected network VRU.

Field

Description

Name (required)

An enterprise name for the network VRU. This name must be unique
                                                				for all network VRUs in the enterprise

Type (required)

(selection list) The type of network VRU.

Description

Additional information about the network VRU.

##### Network VRU Banks
                                 	 Tab

This is enabled when a
                                    		Type 9 is selected in the Network VRU tab.

Button

Description

Add

Displays a list
                                                				of trunk groups that are on an IPCC System Peripheral.

Remove

Removes the
                                                				added items from the list of trunk groups.

##### Label Tab

The Label tab allows you to view (and create, delete, or edit, if you have maintenance
                                    		access) the properties of the selected label.

Field

Description

Network VRU Bank

Specifies the Network Target for the Label to be associated with.

Routing client (required)

The enterprise name of the routing client associated with the
                                                				label.

Label (required)

The label value.

Label type (required)

(drop-down list) The valid types depend on the type of routing
                                                				client. Select one valid type for your routing client. Check with your carrier
                                                				for the latest information about supported label types. Typical types are
                                                				Normal, DNIS Override, Busy, Ring, and Post-Query.

Customer (optional)

The customer associated with the label.

Description

Additional information about the label.

### Network VRU Script List Tool

This tool allows you to list the network VRU scripts currently defined
                                 		  in the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

Network VRU scripts are created by VRU engineers for VRUs. This List
                                 		  tool defines these previously created scripts for the system software so it can
                                 		  interact with the scripts.

Note

#### Select Filter Data Box

Use the Select filter data box to select and retrieve data from the
                                 		database. Until you retrieve database data, no data is displayed.

##### Network VRU Script List box

The Network vRU Script List box lists the network VRU scripts retrieved or created in the current
                                    		editing session. The tabbed fields on the right side of the window display the
                                    		properties of the selected network VRU script.

##### Attributes Tab

The Attributes tab allows you to view and (if you have maintenance access) to define, edit,
                                    		or delete the attributes of the selected network VRU script.

Field

Description

Name (required)

An enterprise name for the VRU script. This name must be unique
                                                				for all VRU scripts in the system.

Network VRU (required)

(selection list) The network VRU associated with the VRU script.

VRU script name (required)

The number by which the script is known to the VRU.

Timeout (seconds) (required)

The number of seconds Unified ICM will wait for a response after directing the routing client to
                                                				run this script. If Unified ICM does not receive a response from the routing client within this
                                                				time, it assumes the VRU script has failed.

Configuration param

A string to be passed to the VRU when the script is invoked.

Customer

(selection list) The customer associated with the VRU script, if
                                                				any.

Interruptible

Checked, indicates the script can be interrupted (for example, if
                                                				an agent becomes available to handle the call).

Overridable

Checked, indicates the script can make itself interruptible or
                                                				non-interruptible.

Description

Any additional information about the VRU script.

##### Security Tab

The Security tab is visible only on partitioned systems and enabled only on records for
                                    		which you have maintenance access.

### VRU Currency List Tool

This tool allows you to list the VRU currencies currently defined in
                                 		  the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

#### Select Filter Data
                              	 Box

Use the Select filter
                                 		data box to select and retrieve data from the database. Until you retrieve
                                 		database data, no data is displayed.

##### VRU Currency List Box

Lists the VRU currencies retrieved and or created in the current editing
                                    		session. The tabbed field on the right side of the window displays the name of
                                    		the selected VRU currency.

###### Currency (Required)

The VRU currency list box lists the type of currency (pounds, dollars, yen, and so on) that the VRU
                                       		  uses when playing prompts. For example, the type of currency is needed if a
                                       		  caller requests information regarding a bank statement. The currency type
                                       		  cannot be longer than 10 characters.

##### Attributes Tab

Allows you to view and (if you have maintenance access) to define,
                                    		modify, and delete currencies.

### VRU Defaults List Tool

This tool allows you to list VRU defaults currently defined in the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

#### Select Filter Data Box

Use the Select filter data box to select and retrieve data from the
                                 		database. Until you retrieve database data, no data is displayed.

##### VRU Defaults List Box

The VRU defaults list box lists the VRU defaults retrieved and or created in the current editing
                                    		session. The tabbed fields on the right side of the window display the
                                    		properties of the selected VRU defaults.

##### Attributes Tab

Allows you to view and (if you have maintenance access) to update the
                                    		defaults used by ISN (Internet Service Node).

Field

Description

Name (required)

A unique name for the VRU defaults list.

Description

Additional information about the VRU defaults list.

Media server set (required)

The base URL for all media files used
                                                				in the VRU script. For example: www.machine1/dir1/dirs.

Part of the base URL is the application server IP address or DNS
                                                				name. The maximum string size is 30 characters. The default value is  localhost.

When the Media Server URL is a DNS name and if the DNS Server is
                                                				configured to return multiple IP addresses for a host name, ISN will
                                                				attempt to get the media files from each Media Server IP address in sequence
                                                				with the priority to the closest IP address (as determined by the subnet mask).

Note

Locale (required)

(selection list) A combination of language and country which
                                                				define the grammar and prompt set to use. The default is en_US.

System media library

The name of the system library of media files and prompts for
                                                				individual digits, months, default error messages, and so on. The maximum
                                                				string size is 10 characters. The default is sys.

Note

Application media library

The name of the application library of media files and prompts for
                                                				individual digits, months, default error messages, and so on. Indicates the
                                                				application media library that contains the application media file to be played
                                                				to the caller. The maximum string size is 10 characters. The default is app.

Note

Currency (required)

(selection list) The currency type used in the prompts to the
                                                				caller. The default is dollar.

DTMF termination key (required)

(selection list) The key the caller presses to signify the end of
                                                				digit entry. The default value is #. The choices are 0 through 9, #, or *.

DTMF (dual-tone multi-frequency) is the "touch-tone" method used by the telephone system to
                                                				communicate the keys pressed when dialing.

InterDigit Timeout (required)

The timeout in seconds allowed between entering digits before the
                                                				system assumes the caller is finished. The range is from 1 to 99 seconds. The
                                                				default value is 3 seconds.

No Entry

Defaults for when the caller does not enter data.

Number of tries (required)

The number of times the VRU queries the caller when the caller
                                                				does not entry any data. The range of value is from 1 to 9. The default value
                                                				is 3.

Timeout (required)

The number of seconds allowed before the caller starts entering
                                                				data. After this time, the call is ended. The timeout range is from 0 to 99
                                                				seconds. The default value is 5 seconds.

Invalid Entry

Defaults for when the caller enters incorrect data.

Number of tries (required)

The number of times the VRU queries the caller when the caller
                                                				enters incorrect data. The range is from 1 to 9. The default value is 3.

### VRU Locale List Tool

This tool allows you to list the VRU locales currently defined in the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

#### Select Filter Data Box

Use the Select filter data box to select and retrieve data from the
                                 		database. Until you retrieve database data, no data is displayed.

##### VRU Locales List Box

Lists the VRU locales retrieved and or created in the current editing
                                    		session. The tabbed fields on the right side of the window display the
                                    		properties of the selected VRU locales.

###### VRU Locale

A combination of language and country which define the grammar and
                                       		  prompt set to use when the VRU plays prompts.

##### Attributes Tab

Allows you to view and (if you have maintenance access) to define,
                                    		modify, and delete VRU locales.

###### Locale (Required)

A combination of language and country which define the grammar and
                                       		  prompt set to use when the VRU plays prompts. The default is en_US. This cannot
                                       		  be longer than 10 characters.

## Configuring Network
                        	 VRUs and VRU Scripts

Before you start configuring a Network VRU, you must know its type. The VRU type determines what routing script nodes the
                              system software needs to use to communicate with the VRU. For example, when interacting with a Type 3 VRU, the system software
                              runs a routing script containing a Send to VRU node to successfully process a call.

The following table
                              		  lists the VRU types that are currently available.

Type

Description

Nodes to use
                                          					 with this type

1

Normal label
                                          					 type and a correlation ID.

2

Normal label
                                          					 type and a DNIS.

Required:
                                          					 Translation Route to VRU. Optional: Queue and Run VRU Script.

3

Resource
                                          					 label type and a correlation ID. The routing client can automatically take back
                                          					 the call from the VRU when the system software returns a destination label.

Note

Optional:
                                          					 Send to VRU, Queue, and Run VRU Script.

5

Resource
                                          					 label type and either a correlation ID or a DNIS.

Note

Required:
                                          					 Send to VRU. Optional: Queue and Run VRU Script.

6

No label, no
                                          					 correlation ID, and no DNIS (call is already at the VRU).

The VRU for
                                          					 this type is programmed so that it can recognize such a request based on the
                                          					 call qualifiers, so you can assume the call is already at the VRU.

Optional:
                                          					 Queue and Run VRU Script.

7

Similar to
                                          					 Type 3, but the system software automatically instructs the VRU to release the
                                          					 call when it sends a destination label to the routing client.

Note

Optional:
                                          					 Send to VRU, Queue, and Run VRU Script.

8

Similar to
                                          					 Type 2, but a Type 8 VRU is used when the NAM has a routing client that
                                          					 controls the call to the VRU.

Required:
                                          					 Translation Route to VRU. Optional: Queue and Run VRU Script.

9

Simplifies
                                          					 configuration requirements in Unified Customer Voice Portal (Unified CVP) Comprehensive Model deployments.

Use this type for calls that originate from ACD and need to be transferred to Unified CVP for self service or queuing, and for calls that originate from an Unified CCE or Unified CM , and need to be transferred to Unified CVP for self service or queuing.

Required:
                                          					 All Unified CVP micro-application scripts

10

Type 10 was designed to simplify the configuration requirements in Unified CVP Comprehensive Model deployments.

There is a Handoff of routing client responsibilities to the Unified CVP switch leg.

There is an automatic transfer to the Unified CVP VRU leg, resulting in a second transfer in the case of calls originated
                                          by the VRU, ACD, or Cisco Unified Communications Manager.

For calls originated by Cisco Unified Communications Manager, the Correlation ID transfer mechanism is used. The Correlation
                                          ID is automatically added to the end of the transfer label defined in the Type 10 Network VRU configuration.

The final transfer to the Unified CVP VRU leg is similar to a Type 7 transfer, in that a RELEASE message is sent to the VRU
                                          prior to any transfer.

It is not really necessary to include a Send to VRU node in a script referring to a Type 3 or Type 7 VRU, as the Queue and
                              Run VRU Script nodes automatically send the call to the VRU if it is not already there when they run. However, including it
                              in such scripts can act as a visual aid if you ever need to troubleshoot the script.

For Types 3 and 7
                              		  you must use the System Information dialog to configure a range of correlation
                              		  IDs. These IDs allow the system software to match calls arriving at the VRU
                              		  with calls sent there by the system software. (For Types 2 and 8, the system
                              		  software uses the DNIS values associated with the translation route to match up
                              		  the calls. For Type 6, no matching is required since the call is already at the
                              		  VRU.)

### VRU Port Map Data
                           	 Descriptions

A VRU port map
                                 		  associates a VRU trunk with an ACD trunk or an ADC port. In cases where ACD and
                                 		  VRU PIMs are controlled by the same PG, each row in the VRU_Port_Map table
                                 		  specifies how a VRU port maps to an ACD trunk or port.

You can add or modify the VRU Port Map in bulk using the VRU Port Map Bulk Inster or Bulk Edit tools in Configuration Manager > Bulk Configuration > .

Field

Description

State

(display
                                             					 only) A symbol indicating whether a row's record is changed, not changed, to be
                                             					 deleted, or to be inserted.

VRU Trunk Group
                                                						(required)

Indicates
                                             					 the VRU Trunk Group associated with this port map.

VRU Trunk Number
                                                						(required)

Indicates
                                             					 the VRU Trunk associated with this port map.

Mapping Type (required)

Type of
                                             					 mapping associated with this port map. There are two mapping types:

VRU
                                                   						  Trunk, which maps to ACD Trunk

VRU
                                                   						  Port, which maps to ACD Port

This
                                             					 selection determines which two of the next four fields are editable.

ACD Trunk Group

(optional)
                                             					 Indicates the ACD Trunk Group associated with this port map.

ACD Trunk Number

(optional)
                                             					 Indicates the ACD Trunk associated with this port map.

ACD Peripheral

(optional)
                                             					 Indicates the ACD Peripheral associated with this port map.

ACD Port

(optional)
                                             					 Indicates the ACD Port associated with this port map.

### Network VRU Script Data Descriptions

Each row identifies a script used by a network VRU to handle a call. A
                                 		  VRU script is managed by the VRU itself. It is not stored in the Unified ICM database or directly managed by the system software. The system
                                 		  software can only direct the VRU to run the script.

Note

Field

Description

State

(display only) A symbol indicating whether a row's record is
                                             					 changed, not changed, to be deleted, or to be inserted.

Network Target (required)

Identifies the network VRU associated with the script.

VRU Script Name (required)

The name of the script as known at the VRU.

Network VRU Script (required)

The enterprise name of the script.

Customer

(optional) The name of the customer associated with the
                                             					 script.

Interruptible (required)

Indicates whether the system software can interrupt the script
                                             					 (for example, if a routing target becomes available): Yes or No.

Overridable (required)

Indicates whether the script can override its own
                                             					 Interruptible attribute: Yes or No.

Configuration Parameter

(optional) A parameter string that is sent to the VRU to
                                             					 initialize the script.

Timeout

(optional) The number of seconds the system software will wait
                                             					 for a response after invoking the script.

If the system software does not receive a response from the
                                             					 routing client within this time, it assumes the VRU script has failed.

Description

(optional) Additional information about the script.

### Network VRUs

Define each logical VRU in the database before continuing to the following sections.

#### Create Network VRU Target

##### Procedure

Step 1

Within the Configuration Manager, select Tools > Explorer
                                                   				  Tools > Network VRU Explorer .

The
                                                			 Network VRU Explorer window appears.

Step 2

In the Network VRU Explorer window, click Retrieve to enable Add Network VRU .

Step 3

Click Add Network VRU .

The Network VRU property tab
                                                			 appears.

Step 4

Complete the Network VRU property tab.

The Name and Type fields are required. All other fields are optional.

The ECC Payload field provides the name of the ECC payload that has scope for interactions with this network VRU. For additional
                                                information refer to the Online Help.

Step 5

Click Save to apply your changes.

#### Define Network VRU Label

You must associate all VRU Types (except Type 6) with a Network VRU
                                    		label.

##### Procedure

Step 1

In the Network VRU Explorer window, click Retrieve and select the Network VRU you want
                                             			 to add the label to.

The Label property tab appears.

Step 2

Complete the Label property tab.

Step 3

Click Save to apply your changes.

#### Set Default Network VRU and Range of Correlation Numbers

For Network VRUs, you must use the System Information dialog to define a
                                    		range of correlation IDs so the system software can communicate with the VRU
                                    		about the call.

##### Procedure

Step 1

Within the Configuration Manager, select Tools > Miscellaneous
                                                   				  Tools > System Information .

The
                                                			 System Information window appears.

Step 2

In the System Information window, select the Default Network VRU .

Step 3

Enter the Minimum Correlation Number .

Step 4

Enter the Maximum Correlation Number .

Step 5

Click Save to apply your changes.

#### Configure VRU Scripts

To allow a routing script to control the processing on the VRU, you
                                    		  must configure VRU-based scripts within the system software. A routing script
                                    		  can then direct the VRU to run a specific script.

Note

##### Procedure

Step 1

Within the Configuration Manager, select Tools > Network VRU
                                                   				  Script List . The Network VRU Script List window
                                             			 appears.

Step 2

In the Network VRU Script List window, enable Add by clicking Retrieve .

Step 3

Click Add . The Attributes property tab appears.

Step 4

Complete the Attributes property tab.

Note

Step 5

Click Save to apply your changes. The system
                                             			 software database manager automatically generates a unique Network VRU Script
                                             			 ID.

#### Accessing VRUs in Scripts

After you configure Network VRU and VRU scripts, you can use the Script Editor (refer to the Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise for additional information) to write a routing script to send a call to the VRU and invoke a specific VRU script.

#### Calls Queued at
                              	 VRUs

You can queue a call
                                    		  at a Network VRU until a specific resource becomes available. A call can be
                                    		  queued directly to an agent, to a precision queue, to one or more skill groups,
                                    		  to an enterprise skill group, or to one or more scheduled targets. As soon as
                                    		  an agent becomes available at one of the specified targets, the call is removed
                                    		  from the queue and sent to the target.

## Mapping to
                        	 ACD-Specific Terminology

The following table
                              		  summarizes the mapping of Unified Intelligent Contact Management (Unified ICM) terminology to ACD-specific terminology.

Unified ICM term

Peripheral-specific
                                             						equivalent

Service

Aspect Contact Center :
                                          					 Application

Avaya Communication
                                             						Manager : Vector Directory Number (VDN)

Trunk

Aspect Contact Center: Instrument 4

Trunk

Trunk
                                          					 group

Trunk
                                          					 group

Note

In some cases the Unified ICM concept is very close to the corresponding ACD feature. In other cases, the ACD does not have a feature that maps exactly
                              to the Unified ICM feature. In these cases, you might choose a different mapping than shown in the above table.

On an Avaya Communication Manager running in EAS mode, each skill group has primary and secondary subgroups. The system software
                              emulates this by automatically creating additional skill groups for these peripheral types. In monitoring and scripts, you
                              can reference the .pri and .sec skill groups directly or you can refer to the base skill group.

Some ACDs have
                              		  limitations that prevent them from making full use of specific features of the
                              		  system software.

Refer to the Pre-installation Planning Guide for Cisco Unified ICM for the current list of supported peripherals with any
                              		  peripheral-specific limitations.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | The Network VRU
                                          		  Explorer is not available on a limited (single Instance) Administration &
                                          		  Data Server. |
|---|---|

| Button | Description |
|---|---|
| Add | When an object
                                                				in the tree is selected, you can add another object of the same kind or an
                                                				object immediately below it in the tree hierarchy. The Add buttons are enabled accordingly. |
| Add Network
                                                   				  VRU | Click to add a
                                                				network VRU to the database. |
| Add
                                                   				  Label | Click to add a
                                                				label to the selected network VRU. |
| Delete | Click to
                                                				delete the selected object in the tree. This marks the selected object for
                                                				deletion. When you click Save ,
                                                				the object is deleted from the database. If a network
                                                				VRU is selected, it and the labels associated with it are marked for deletion.
                                                				If a label is selected, only that label's record is marked for deletion. |
| Undelete | The Delete button toggles to Undelete when you select an object marked for deletion. To undelete an object marked for
                                                				deletion, select it and click Undelete. |
| ID status
                                                   				  box | The label in the ID box at the bottom of the screen identifies the Unified ICM system on which you are working. |

| Field | Description |
|---|---|
| Name (required) | An enterprise name for the network VRU. This name must be unique
                                                				for all network VRUs in the enterprise |
| Type (required) | (selection list) The type of network VRU. |
| Description | Additional information about the network VRU. |

| Button | Description |
|---|---|
| Add | Displays a list
                                                				of trunk groups that are on an IPCC System Peripheral. |
| Remove | Removes the
                                                				added items from the list of trunk groups. |

| Field | Description |
|---|---|
| Network VRU Bank | Specifies the Network Target for the Label to be associated with. |
| Routing client (required) | The enterprise name of the routing client associated with the
                                                				label. |
| Label (required) | The label value. |
| Label type (required) | (drop-down list) The valid types depend on the type of routing
                                                				client. Select one valid type for your routing client. Check with your carrier
                                                				for the latest information about supported label types. Typical types are
                                                				Normal, DNIS Override, Busy, Ring, and Post-Query. |
| Customer (optional) | The customer associated with the label. |
| Description | Additional information about the label. |

| Note | The Network VRU Script List tool is not available on a Limited
                                          		  (single Instance) Administration & Data Server. |
|---|---|

| Field | Description |
|---|---|
| Name (required) | An enterprise name for the VRU script. This name must be unique
                                                				for all VRU scripts in the system. |
| Network VRU (required) | (selection list) The network VRU associated with the VRU script. |
| VRU script name (required) | The number by which the script is known to the VRU. |
| Timeout (seconds) (required) | The number of seconds Unified ICM will wait for a response after directing the routing client to
                                                				run this script. If Unified ICM does not receive a response from the routing client within this
                                                				time, it assumes the VRU script has failed. |
| Configuration param | A string to be passed to the VRU when the script is invoked. |
| Customer | (selection list) The customer associated with the VRU script, if
                                                				any. |
| Interruptible | Checked, indicates the script can be interrupted (for example, if
                                                				an agent becomes available to handle the call). |
| Overridable | Checked, indicates the script can make itself interruptible or
                                                				non-interruptible. |
| Description | Any additional information about the VRU script. |

| Field | Description |
|---|---|
| Name (required) | A unique name for the VRU defaults list. |
| Description | Additional information about the VRU defaults list. |
| Media server set (required) | The base URL for all media files used
                                                				in the VRU script. For example: www.machine1/dir1/dirs. Part of the base URL is the application server IP address or DNS
                                                				name. The maximum string size is 30 characters. The default value is  localhost. When the Media Server URL is a DNS name and if the DNS Server is
                                                				configured to return multiple IP addresses for a host name, ISN will
                                                				attempt to get the media files from each Media Server IP address in sequence
                                                				with the priority to the closest IP address (as determined by the subnet mask). Note For multi-tenant systems, you can include the customer name at
                                                         				the end of the string. | Note | For multi-tenant systems, you can include the customer name at
                                                         				the end of the string. |
| Note | For multi-tenant systems, you can include the customer name at
                                                         				the end of the string. |
| Locale (required) | (selection list) A combination of language and country which
                                                				define the grammar and prompt set to use. The default is en_US. |
| System media library | The name of the system library of media files and prompts for
                                                				individual digits, months, default error messages, and so on. The maximum
                                                				string size is 10 characters. The default is sys. Note Each locale has a specific system media library. | Note | Each locale has a specific system media library. |
| Note | Each locale has a specific system media library. |
| Application media library | The name of the application library of media files and prompts for
                                                				individual digits, months, default error messages, and so on. Indicates the
                                                				application media library that contains the application media file to be played
                                                				to the caller. The maximum string size is 10 characters. The default is app. Note Each locale has a specific application media library. | Note | Each locale has a specific application media library. |
| Note | Each locale has a specific application media library. |
| Currency (required) | (selection list) The currency type used in the prompts to the
                                                				caller. The default is dollar. |
| DTMF termination key (required) | (selection list) The key the caller presses to signify the end of
                                                				digit entry. The default value is #. The choices are 0 through 9, #, or *. DTMF (dual-tone multi-frequency) is the "touch-tone" method used by the telephone system to
                                                				communicate the keys pressed when dialing. |
| InterDigit Timeout (required) | The timeout in seconds allowed between entering digits before the
                                                				system assumes the caller is finished. The range is from 1 to 99 seconds. The
                                                				default value is 3 seconds. |
| No Entry | Defaults for when the caller does not enter data. Number of tries (required) The number of times the VRU queries the caller when the caller
                                                				does not entry any data. The range of value is from 1 to 9. The default value
                                                				is 3. Timeout (required) The number of seconds allowed before the caller starts entering
                                                				data. After this time, the call is ended. The timeout range is from 0 to 99
                                                				seconds. The default value is 5 seconds. |
| Invalid Entry | Defaults for when the caller enters incorrect data. Number of tries (required) The number of times the VRU queries the caller when the caller
                                                				enters incorrect data. The range is from 1 to 9. The default value is 3. |

| Note | For multi-tenant systems, you can include the customer name at
                                                         				the end of the string. |
|---|---|

| Note | Each locale has a specific system media library. |
|---|---|

| Note | Each locale has a specific application media library. |
|---|---|

| Type | Description | Nodes to use
                                          					 with this type |
|---|---|---|
| 1 | Normal label
                                          					 type and a correlation ID. |  |
| 2 | Normal label
                                          					 type and a DNIS. | Required:
                                          					 Translation Route to VRU. Optional: Queue and Run VRU Script. |
| 3 | Resource
                                          					 label type and a correlation ID. The routing client can automatically take back
                                          					 the call from the VRU when the system software returns a destination label. Note Use this
                                                   					 type (rather than Type 7) when the routing client can automatically take back
                                                   					 the call from the VRU when the system software returns a destination. | Note | Use this
                                                   					 type (rather than Type 7) when the routing client can automatically take back
                                                   					 the call from the VRU when the system software returns a destination. | Optional:
                                          					 Send to VRU, Queue, and Run VRU Script. |
| Note | Use this
                                                   					 type (rather than Type 7) when the routing client can automatically take back
                                                   					 the call from the VRU when the system software returns a destination. |
| 5 | Resource
                                          					 label type and either a correlation ID or a DNIS. Note Use this
                                                   					 type (rather than a Type 3 or Type 7) when the routing client itself takes care
                                                   					 of mapping the call to requests from the system software. | Note | Use this
                                                   					 type (rather than a Type 3 or Type 7) when the routing client itself takes care
                                                   					 of mapping the call to requests from the system software. | Required:
                                          					 Send to VRU. Optional: Queue and Run VRU Script. |
| Note | Use this
                                                   					 type (rather than a Type 3 or Type 7) when the routing client itself takes care
                                                   					 of mapping the call to requests from the system software. |
| 6 | No label, no
                                          					 correlation ID, and no DNIS (call is already at the VRU). | The VRU for
                                          					 this type is programmed so that it can recognize such a request based on the
                                          					 call qualifiers, so you can assume the call is already at the VRU. Optional:
                                          					 Queue and Run VRU Script. |
| 7 | Similar to
                                          					 Type 3, but the system software automatically instructs the VRU to release the
                                          					 call when it sends a destination label to the routing client. Note Use this
                                                   					 type (instead of Type 3) when the routing client cannot take back the call from
                                                   					 the VRU. That is, the system software automatically instructs the VRU to
                                                   					 release when it sends a route response to the routing client; for example, CWC
                                                   					 Network VRUs. | Note | Use this
                                                   					 type (instead of Type 3) when the routing client cannot take back the call from
                                                   					 the VRU. That is, the system software automatically instructs the VRU to
                                                   					 release when it sends a route response to the routing client; for example, CWC
                                                   					 Network VRUs. | Optional:
                                          					 Send to VRU, Queue, and Run VRU Script. |
| Note | Use this
                                                   					 type (instead of Type 3) when the routing client cannot take back the call from
                                                   					 the VRU. That is, the system software automatically instructs the VRU to
                                                   					 release when it sends a route response to the routing client; for example, CWC
                                                   					 Network VRUs. |
| 8 | Similar to
                                          					 Type 2, but a Type 8 VRU is used when the NAM has a routing client that
                                          					 controls the call to the VRU. | Required:
                                          					 Translation Route to VRU. Optional: Queue and Run VRU Script. |
| 9 | Simplifies
                                          					 configuration requirements in Unified Customer Voice Portal (Unified CVP) Comprehensive Model deployments. Use this type for calls that originate from ACD and need to be transferred to Unified CVP for self service or queuing, and for calls that originate from an Unified CCE or Unified CM , and need to be transferred to Unified CVP for self service or queuing. | Required:
                                          					 All Unified CVP micro-application scripts |
| 10 | Type 10 was designed to simplify the configuration requirements in Unified CVP Comprehensive Model deployments. There is a Handoff of routing client responsibilities to the Unified CVP switch leg. There is an automatic transfer to the Unified CVP VRU leg, resulting in a second transfer in the case of calls originated
                                          by the VRU, ACD, or Cisco Unified Communications Manager. For calls originated by Cisco Unified Communications Manager, the Correlation ID transfer mechanism is used. The Correlation
                                          ID is automatically added to the end of the transfer label defined in the Type 10 Network VRU configuration. The final transfer to the Unified CVP VRU leg is similar to a Type 7 transfer, in that a RELEASE message is sent to the VRU
                                          prior to any transfer. |  |

| Note | Use this
                                                   					 type (rather than Type 7) when the routing client can automatically take back
                                                   					 the call from the VRU when the system software returns a destination. |
|---|---|

| Note | Use this
                                                   					 type (rather than a Type 3 or Type 7) when the routing client itself takes care
                                                   					 of mapping the call to requests from the system software. |
|---|---|

| Note | Use this
                                                   					 type (instead of Type 3) when the routing client cannot take back the call from
                                                   					 the VRU. That is, the system software automatically instructs the VRU to
                                                   					 release when it sends a route response to the routing client; for example, CWC
                                                   					 Network VRUs. |
|---|---|

| Field | Description |
|---|---|
| State | (display
                                             					 only) A symbol indicating whether a row's record is changed, not changed, to be
                                             					 deleted, or to be inserted. |
| VRU Trunk Group
                                                						(required) | Indicates
                                             					 the VRU Trunk Group associated with this port map. |
| VRU Trunk Number
                                                						(required) | Indicates
                                             					 the VRU Trunk associated with this port map. |
| Mapping Type (required) | Type of
                                             					 mapping associated with this port map. There are two mapping types: VRU
                                                   						  Trunk, which maps to ACD Trunk VRU
                                                   						  Port, which maps to ACD Port This
                                             					 selection determines which two of the next four fields are editable. |
| ACD Trunk Group | (optional)
                                             					 Indicates the ACD Trunk Group associated with this port map. |
| ACD Trunk Number | (optional)
                                             					 Indicates the ACD Trunk associated with this port map. |
| ACD Peripheral | (optional)
                                             					 Indicates the ACD Peripheral associated with this port map. |
| ACD Port | (optional)
                                             					 Indicates the ACD Port associated with this port map. |

| Note | The Network VRU Script Bulk tool is not available on a Limited
                                          		  (single Instance) Administration & Data Server. |
|---|---|

| Field | Description |
|---|---|
| State | (display only) A symbol indicating whether a row's record is
                                             					 changed, not changed, to be deleted, or to be inserted. |
| Network Target (required) | Identifies the network VRU associated with the script. |
| VRU Script Name (required) | The name of the script as known at the VRU. |
| Network VRU Script (required) | The enterprise name of the script. |
| Customer | (optional) The name of the customer associated with the
                                             					 script. |
| Interruptible (required) | Indicates whether the system software can interrupt the script
                                             					 (for example, if a routing target becomes available): Yes or No. |
| Overridable (required) | Indicates whether the script can override its own
                                             					 Interruptible attribute: Yes or No. |
| Configuration Parameter | (optional) A parameter string that is sent to the VRU to
                                             					 initialize the script. |
| Timeout | (optional) The number of seconds the system software will wait
                                             					 for a response after invoking the script. If the system software does not receive a response from the
                                             					 routing client within this time, it assumes the VRU script has failed. |
| Description | (optional) Additional information about the script. |

| Step 1 | Within the Configuration Manager, select Tools > Explorer
                                                   				  Tools > Network VRU Explorer . The
                                                			 Network VRU Explorer window appears. |
|---|---|
| Step 2 | In the Network VRU Explorer window, click Retrieve to enable Add Network VRU . |
| Step 3 | Click Add Network VRU . The Network VRU property tab
                                                			 appears. |
| Step 4 | Complete the Network VRU property tab. The Name and Type fields are required. All other fields are optional. The ECC Payload field provides the name of the ECC payload that has scope for interactions with this network VRU. For additional
                                                information refer to the Online Help. |
| Step 5 | Click Save to apply your changes. |

| Step 1 | In the Network VRU Explorer window, click Retrieve and select the Network VRU you want
                                             			 to add the label to. The Label property tab appears. |
|---|---|
| Step 2 | Complete the Label property tab. The Routing client , Label , and Label type fields are required. All other
                                             				fields are optional. For additional information refer to the online Help. |
| Step 3 | Click Save to apply your changes. |

| Step 1 | Within the Configuration Manager, select Tools > Miscellaneous
                                                   				  Tools > System Information . The
                                                			 System Information window appears. |
|---|---|
| Step 2 | In the System Information window, select the Default Network VRU . |
| Step 3 | Enter the Minimum Correlation Number . |
| Step 4 | Enter the Maximum Correlation Number . For additional information refer to the online help. |
| Step 5 | Click Save to apply your changes. |

| Note | VRU scripts are defined and maintained on the VRU. The system
                                             		  software maintains only a name for each VRU script. It does not maintain the
                                             		  scripts themselves. |
|---|---|

| Step 1 | Within the Configuration Manager, select Tools > Network VRU
                                                   				  Script List . The Network VRU Script List window
                                             			 appears. |
|---|---|
| Step 2 | In the Network VRU Script List window, enable Add by clicking Retrieve . |
| Step 3 | Click Add . The Attributes property tab appears. |
| Step 4 | Complete the Attributes property tab. Note The Name , Network VRU , VRU script
                                                            				  name , and Timeout fields are required. All other
                                                         				fields are optional. For additional information refer to the online Help. | Note | The Name , Network VRU , VRU script
                                                            				  name , and Timeout fields are required. All other
                                                         				fields are optional. For additional information refer to the online Help. |
| Note | The Name , Network VRU , VRU script
                                                            				  name , and Timeout fields are required. All other
                                                         				fields are optional. For additional information refer to the online Help. |
| Step 5 | Click Save to apply your changes. The system
                                             			 software database manager automatically generates a unique Network VRU Script
                                             			 ID. |

| Note | The Name , Network VRU , VRU script
                                                            				  name , and Timeout fields are required. All other
                                                         				fields are optional. For additional information refer to the online Help. |
|---|---|

| Unified ICM term | Peripheral-specific
                                             						equivalent |
|---|---|
|  |  |
|  |  |
| Service | Aspect Contact Center :
                                          					 Application Avaya Communication
                                             						Manager : Vector Directory Number (VDN) |
|  |  |
| Trunk | Aspect Contact Center: Instrument 4 Trunk |
| Trunk
                                          					 group | Trunk
                                          					 group |

| Note | Multi-channel
                                       		  applications function as application instances. |
|---|---|