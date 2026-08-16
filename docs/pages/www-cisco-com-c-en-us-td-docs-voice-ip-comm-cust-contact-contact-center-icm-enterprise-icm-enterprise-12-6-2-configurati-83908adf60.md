---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-83908adf60
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_configuration-guide-for-cisco-unified-icm-enterprise_release_1262/ucce_m_1261-network-ivrs-vrus-config.html
retrieved_at: 2026-08-16T14:38:53.677568+00:00
---

Configuration Guide for Cisco Unified ICM Enterprise, Release 12.6(2)

# Configuration Guide for Cisco Unified ICM Enterprise, Release 12.6(2)

Updated: April 28, 2023

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

### Network VRU Script List Tool

This tool allows you to list the network VRU scripts currently defined
                                 		  in the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

Network VRU scripts are created by VRU engineers for VRUs. This List
                                 		  tool defines these previously created scripts for the system software so it can
                                 		  interact with the scripts.

Note

### VRU Currency List Tool

This tool allows you to list the VRU currencies currently defined in
                                 		  the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

### VRU Defaults List Tool

This tool allows you to list VRU defaults currently defined in the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

### VRU Locale List Tool

This tool allows you to list the VRU locales currently defined in the Unified ICM database, to define new ones, and to view, edit, or delete the
                                 		  records of existing ones.

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

Use this
                                          					 type for calls that originate from a TDM VRU or ACD and need to be transferred
                                          					 to Unified CVP for
                                          					 self service or queuing, and for calls that originate from an Unified CCE or Unified CM , and
                                          					 need to be transferred to Unified CVP for
                                          					 self service or queuing.

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

After you configure Network VRU and VRU scripts, you can use
                                    		  the Script Editor (refer to the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise for additional information) to
                                    		  write a routing script to send a call to the VRU and invoke a specific VRU
                                    		  script.

#### Calls Queued at
                              	 VRUs

You can queue a call
                                    		  at a Network VRU until a specific resource becomes available. A call can be
                                    		  queued directly to an agent, to a precision queue, to one or more skill groups,
                                    		  to an enterprise skill group, or to one or more scheduled targets. As soon as
                                    		  an agent becomes available at one of the specified targets, the call is removed
                                    		  from the queue and sent to the target.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | The Network VRU
                                          		  Explorer is not available on a limited (single Instance) Administration &
                                          		  Data Server. |
|---|---|

| Note | The Network VRU Script List tool is not available on a Limited
                                          		  (single Instance) Administration & Data Server. |
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
                                          					 configuration requirements in Unified Customer Voice Portal (Unified CVP) Comprehensive Model deployments. Use this
                                          					 type for calls that originate from a TDM VRU or ACD and need to be transferred
                                          					 to Unified CVP for
                                          					 self service or queuing, and for calls that originate from an Unified CCE or Unified CM , and
                                          					 need to be transferred to Unified CVP for
                                          					 self service or queuing. | Required:
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