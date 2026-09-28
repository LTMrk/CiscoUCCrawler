---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-de6b3bb064
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/configuration-guide-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/ucce_b_1251-configuration-guide-unified-cce_chapter_0110.html
retrieved_at: 2026-08-20T18:08:44.550967+00:00
---

Configuration Guide for Cisco Unified ICM Enterprise-Release 12.6(1)

# Configuration Guide for Cisco Unified ICM Enterprise-Release 12.6(1)

Updated: May 14, 2021

Chapter: Routing Clients

## Chapter: Routing Clients

# Routing Clients

## The Routing Client
                        	 Subsystem

A routing client is an entity that sends route requests to the system software.

A routing client can
                              		  be:

A public network
                                    				interexchange carrier (IXC), such as AT&T, BT, or MCI

A private
                                    				network peripheral, such as an Aspect automatic call distribution (ACD)

The following
                                    				figure shows the elements of the routing client subsystem.

### Interface
                           	 Controllers

Each routing client
                                 		  must be associated with an interface controller. An interface controller
                                 		  operates on two levels: physical and logical . A
                                 		  physical device is a single instance of a device. A logical device is either a
                                 		  single physical device or more than one physical device running duplexed.

A physical interface
                                 		  controller can be a:

Network Interface Controller
                                          				  (NIC) . An NIC communicates directly with the IXC's signaling network,
                                       				reading call routing requests from the network and transferring them to the
                                       				Central Controller. This chapter describes how to set up a NIC .

Peripheral Gateway (PG) .
                                       				A PG communicates with the ACD, PBX, or VRU at a contact center, monitoring
                                       				status information from the peripheral and sending it to the Central
                                       				Controller. The PG can also act as a routing client, sending routing requests
                                       				to Unified ICM software.

### Routing Client
                           	 Subsystems Examples

You can associate
                                 		  more than one routing client with a single logical interface controller. For
                                 		  example, if a Unified ICM NIC is
                                 		  serving two AT&T Intelligent Call Processing (ICP) subsystems, as shown in
                                 		  the following figure, you can define each as a separate routing client through
                                 		  the single logical interface controller.

On the other hand,
                                 		  if you have two ACDs performing private network routing through two different
                                 		  peripheral gateways (PG), as shown in the following figure, you must define
                                 		  each as a routing client because each Peripheral Gateway is a separate logical
                                 		  interface controller.

## NIC Configuration

Use the NIC Explorer to view, define, modify, or delete NIC information and its associated routing client information.

The NIC is the interface between the ICM platform and the Interexchange Carrier signaling network. Within the Unified ICM software the NIC reads call routing requests from the network and transfers them to the Central Controller. It consists of
                              a logical interface controller and one or two physical interface controllers. The number of physical interface controllers
                              permitted depends on the client type.

The NIC Explorer generates records that set up a logical interface
                              		  controller, one or more physical interface controllers, and one or more routing
                              		  clients.

### View NIC and Routing Clients

To view a NIC and its routing clients, follow these steps:

Step 1

From the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > NIC Explorer .

The NIC Explorer window appears.

Step 2

In the Select filter data box, select the filters you
                                          			 want.

Step 3

Click Retrieve . The names of retrieved NICs are
                                          			 listed in the tree list box.

Step 4

In the tree list box, select the NIC whose records you want to
                                          			 view. The configuration information displays in the fields on the right.

Step 5

To view a routing client record, in the tree list box, expand the
                                          			 tree branch for the selected NIC and select the routing client icon.

The routing client configuration information displays in the
                                             				window on the right.

### NIC Explorer Tab Descriptions

The following tables describe the tabbed property fields and buttons
                                 		  that configure a NIC and its routing clients.

#### Logical Interface
                              	 Controller Tab

The Logical Interface
                                 		Controller tab allows you to view (and define or edit, if you have maintenance
                                 		access) the properties of the selected logical interface controller.

Field/Button

Description

Controller ID (required)

A unique
                                             				identifier for the NIC's logical controller. This is a read-only field. When you create a new NIC , the
                                             				system places UNASSIGNED in this field and automatically creates an ID when
                                             				you save your edits.

Name (required)

The enterprise
                                             				name for the NIC's logical controller. This name also identifies the NIC and
                                             				must be unique for all logical controllers in the enterprise.

Client Type (required)

The type of
                                             				routing client serviced by the NIC. For example, Lucent, MCI, and so
                                             				on. When defining a new NIC, select one from the pop-up selection box.

Selecting a type
                                             				of routing client automatically places that type's default values in the
                                             				Routing Client's Timeout Threshold, Late Threshold, Timeout Limit, Use DN/Label
                                             				Map, and Client Type fields.

Configuration Parameter

A string
                                             				containing information such as logon information, specific to the interface
                                             				controller device. For example:

-rtuser UserName -rtpswd
                                                				  Password .

Description

Additional
                                             				information about the Logical interface controller.

Add Physical Interface
                                                				  Controller

Click this
                                             				button to add one or more physical interface controllers.

This button is
                                             				disabled when there is no client type, as in a new NIC record, or when the NIC
                                             				node reaches its upper limit of Physical Interface Controllers.

#### Physical Interface Controller Tab

The Physical Interface Controller tab allows you to view (and define or
                                 		edit, if you have maintenance access) the properties of the selected NIC's
                                 		physical interface controllers.

Field/Button

Description

Associated Physical Interface Controllers

A duplexed NIC has two entries in the Physical Interface Controller
                                             				table and a single entry in the Logical Interface Controller table.

ID

A unique identifier for the NIC's associated physical interface
                                             				controller. This is a read-only field. When you create a new NIC, the system
                                             				places UNASSIGNED in this field and automatically creates an ID when you save your edits.

Name

The enterprise name of the routing client associated with the NIC . This name must be unique for all physical controllers
                                             				in the enterprise.

Description

Any other information about the physical interface controller.

Modify

To edit the name or description of the 
                                             				physical interface controller, click this button.  In the
                                             				Physical Interface Controller dialog enter your edits and click OK .

New

To enter a record for a new associated physical interface
                                             				controller, click this button and in the 
                                             				Physical Interface Controller dialog, enter its enterprise
                                             				name and click OK .

The system assigns an ID to the controller when you save it to the
                                             				database. The NIC can represent multiple physical devices. The limit is
                                             				different for different client types.

Delete

Deletes the selected physical interface controller.

#### Routing Client
                              	 Tab

The Routing Client tab
                                 		allows you to view (and define or edit, if you have maintenance access) the
                                 		properties of the selected routing client. The routing client is the entity
                                 		that sends routing requests to the system software.

Field

Description

Name
                                                				  (required)

The enterprise
                                             				name of the routing client associated with the NIC. You can have more than one
                                             				routing client associated with a NIC. Typically, each routing client maps to a
                                             				subsystem within the ICX network.

Timeout
                                                				  threshold (required)

The maximum
                                             				time, in milliseconds, that the routing client can wait for a response to a
                                             				routing request. The NIC sends a default response slightly before this
                                             				threshold.

Late threshold
                                                				  (required)

A threshold
                                             				value, in milliseconds, for classifying responses as late. Any response that
                                             				exceeds this threshold is considered late even if it does not exceed the
                                             				Timeout Threshold.

Timeout limit
                                                				  (required)

The maximum
                                             				time, in seconds, that the routing client waits for a response. This is the
                                             				maximum time the routing client will tolerate consecutive response timeouts
                                             				before it stops sending requests to the system software.

Default call
                                                				  type

An enterprise
                                             				name for the call type. Initially, you can leave this field blank. For
                                             				information on this field, refer to the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise .

Configuration
                                                				  parameters

A string
                                             				containing any initialization parameters that must be passed to the routing
                                             				client. For a public network, this might include the subsystem number. A null
                                             				value indicates no configuration parameters are provided.

Use DN/Label
                                                				  map

Indicates
                                             				whether the Dialed Number (DN) Label table is used to determine which labels
                                             				are valid for each dialed number. If not, all labels for the routing client are
                                             				valid for all dialed numbers.

Client type
                                                				  (required)

The type of
                                             				routing client that ultimately routes the call on the requesting Unified ICM
                                             				system.

This field is
                                             				enabled only for the routing client associated with an intelligent network call
                                             				routing protocol (INCRP) NIC. In all other cases, it is the same as the logical
                                             				interface controller's client type.

Description

Additional
                                             				information about the routing client.

Network
                                                				  routing client

A name used to
                                             				associate routing clients across instances.

The same string value for the
                                             				routing client on the network analysis module (NAM) and the corresponding
                                             				routing client on the Unified ICM (applies only for a network Unified ICM).

Default Media
                                                				  Routing Domain

(selection list)
                                             				The MRD associated with the routing client.

Congestion Treatment Mode

This field sets
                                             				the congestion treatment mode for routing clients. The default value is 0 when
                                             				you add a new routing client.

The congestion
                                             				treatment mode definitions are as follows:

0 - Use
                                                   					 Congestion Control settings.

1 - Use
                                                   					 Dialed Number (DN) as default label for call treatment.

2 - Use
                                                   					 routing client as default label for call treatment.

3 - Use
                                                   					 global user-defined label for call treatment.

To
                                                               						configure a user-defined label, use the Congestion Setting Configuration tool.

4 - Dialog
                                                   					 fail with an appropriate error code.

5 -
                                                   					 Release message to the routing client.

Default Label

Indicates the
                                             				default label for the routing client to treat the call when the system is
                                             				congested. Also see the following section: Gate
                                                				  Keeper (GK) NIC .

##### Gate Keeper (GK)
                                    		NIC

If you specify GK
                                    		NIC as the type of routing client, the NIC Explorer automatically creates two
                                    		labels that are associated with the new routing client.

The following two
                                    		fields are dimmed:

Congestion
                                          			 Treatment Mode (with default value as 4: to treat the calls on congestion with
                                          			 Dialog Fail)

Default Label
                                          			 (will be empty)

When a GK NIC
                                    		routing client record is deleted, the preceding labels associated with the
                                    		routing client are also deleted.

#### Modify NIC and Routing Clients

To modify a NIC and or its routing clients, follow these steps:

Step 1

Follow the steps for viewing a NIC.

The selected NIC's configuration information displays in the
                                                				fields on the right.

Step 2

Edit the configuration information.

You can modify all fields in the Logical Controller, Physical
                                                				Controller, and Router Client tabs that are not dimmed.

When you make a modification, the Changed icon appears next to the edited item
                                                				(NIC or routing client) in the tree list box.

Step 3

Click Save .

The modified data in the Unified ICM database is saved and the Changed icon is removed from the display in
                                                				the tree list box.

#### Define NIC

To define a NIC,
                                    		  follow these steps:

Step 1

From the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > NIC Explorer . The NIC Explorer window
                                             			 appears.

Step 2

In the Select
                                                				filter data box, click Retrieve . This enables the Add
                                                				NIC button.

Step 3

Click Add
                                                				NIC . A new NIC and its routing client display in the tree list box.
                                             			 Next to each is a To Be
                                                				Inserted icon .

On the right of
                                                				the tree list box, tabbed fields also display for the new NIC's and routing
                                                				client's configuration information.

Step 4

Fill in the
                                             			 tabbed fields.

Step 5

Click Save . The newly defined NIC is saved in the database
                                             			 and the To Be
                                                				Inserted icon is removed from the tree list box.

#### Define Routing Client

To define a routing client, follow these steps:

Step 1

Follow the steps for viewing a NIC. The selected NIC's
                                             			 configuration information displays in the fields on the right.

Step 2

In the tree list box, select the NIC to which you want to add a
                                             			 routing client. This enables the Add Routing Client button.

Step 3

Click Add Routing Client . A new routing client icon
                                             			 appears under the selected NIC in the tree list box and a new Routing Client
                                             			 tab appears in the window on the right.

Step 4

Enter the needed routing client configuration information in the
                                             			 fields on the right.

Step 5

Click Save .

#### Delete NIC

Follow these steps to delete a NIC:

Step 1

Follow the steps for viewing a NIC.

The selected NIC's configuration information displays in the
                                                				fields on the right.

Step 2

In the tree list box, select the NIC whose records you want to
                                             			 delete.

Step 3

Click Delete . This places a Marked for Deletion icon next to the NIC in the tree
                                             			 list box. This also toggles the Delete button to Undelete .

To undelete a NIC marked for deletion, select it in the tree list
                                                				box and click Undelete .

Step 4

Click Save .

This deletes from the database the NIC marked for deletion and
                                                				removes it from the tree list box. After you do this, you cannot undelete the
                                                				NIC.

## Dialed Number/Script Selectors

After you have set up a routing client, you need to define the dialed
                              		  number/script selectors serviced by it. A dialed number/script selector can
                              		  represent an actual number dialed by a caller or any string passed by a routing
                              		  client to indicate the number dialed.

The Configuration Manager's Dialed Number/Script Selector List tool
                              		  allows you to list the dialed number/script selectors currently defined in the Unified ICM database, to define new ones, and to view, edit, or delete the
                              		  records of existing ones. The following instructions show you how to configure
                              		  individual dialed number/script selectors.

### Manage Dialed Number/Script Selectors

Follow the steps below to view, define, delete, or modify dialed
                                 		  number/script selectors:

Step 1

From within the Configuration Manager menu, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . The Dialed Number/Script Selector List window
                                          			 appears.

Step 2

In the Select filter data area, select the Routing client and Customer associated with the dialed number/script selector.

Once you have saved a Dialed Number record to the Unified ICM database, you cannot update the Routing Client field.

If you are viewing or modifying a previously created record and
                                             				you want to limit the number of records retrieved from the database, also
                                             				select one of the optional filters.

Step 3

Click Retrieve . This enables the Add button and displays a list of the
                                          			 retrieved dialed number/script selectors.

The properties of the dialed number/script selector selected in
                                             				the Dialed Number/Script Selector list box on the left side of the window are
                                             				displayed in the property tabs on the right side of the window:

The following properties are displayed:

The Attributes tab allows you to view and (if you have
                                                   					 maintenance access) to define, edit, or delete the attributes of the selected
                                                   					 dialed number/script selector. Attributes with an asterisk are required.

The Dialed Number Label tab allows you to map labels (in
                                                   					 addition to a default label) to the selected dialed number/script selector.

Step 4

This step depends on what you want to do:

To add a new dialed number/script selector, click Add and enter the appropriate values in
                                                   					 the tabbed property fields on the right side of the window.

To delete a dialed number/script selector, select that number
                                                   					 in the Dialed Number/Script Selector list box
                                                   					 and click Delete .

To edit a dialed number/script selector, select that number in
                                                   					 the Dialed Number/Script Selector list box
                                                   					 and edit the appropriate values in the tabbed property fields on the right side
                                                   					 of the window.

Step 5

Click Save to enter any edits into the database.

The dialog closes, and for a new dialed number/script selector,
                                             				the Unified ICM database manager automatically generates a unique Dialed Number
                                             				ID for the routing client.

### Dialed Numbers on the Child Central Controller

Access the Configuration Manager on the Child Administration &
                                 		  Data Server to configure dialed numbers.

#### Configure Dialed Numbers on the Child Central Controller

To configure dialed numbers on the Child Central Controller with  the Configuration Manager Dialed Number/Script Selector
                                    List Tool:

Step 1

Start the Dialed Number/Script Selector List Tool .

Step 2

On the Main window of the Dialed Number/Script Selector List Tool,
                                             			 click Retrieve .

Step 3

Click Add .

The Dialed Number Attributes tab appears.

Step 4

Select IPCC_RC as the Routing Client.

Step 5

Select Cisco_Voice for the Media Routing Domain.

Step 6

Set the Dialed Number String/Script Selector to 2500 (the route point set up on the Unified CM .

Step 7

Set IPCC_RC_2500 as the Name, then select bh03 as the Customer setting.

Step 8

Check Permit Application Routing on the route points
                                             			 controlled by the Parent (the Post route points and the Translation route
                                             			 points).

This provides the link between the Parent and the Child. It gives
                                                				the Parent visibility to the Dialed Number so it can handle it.

Step 9

Click Save .

The dialed number appears in the tree list.

Step 10

Repeat this to add two more dialed numbers (one for each skill
                                             			 group).

When complete, you have the following DNs:

2500

Connects to all of the skill groups.

Named IPCC_RC_2500.

2501

Connects to SG01.

Named IPCC_RC_2501.

2502

Connects to SG02.

Named IPCC_RC_2502.

Step 11

Click Save , then Close to exit the Skill Group Explorer Tool.

### Dialed Number/Script Selector List Tab Descriptions

The following tables describe the tabbed property fields and buttons
                              		that configure a dialed number record.

#### Attributes Tab

Allows you to view and (if you have maintenance access) to define, edit,
                                 		or delete the attributes of the dialed number/script selector.

Attributes with an asterisk are required.

Attribute

Description

Routing Client (required)

(selection list) The enterprise name of the routing client
                                             				associated with this dialed number/script selector. Once you select a routing
                                             				client and save to the database, this field becomes read only.

Dialed number/script selector string (required)

The string value by which the routing client identifies this
                                             				dialed number/script selector. This must be the value the routing client passes
                                             				to the system software for calls to this number. For example: 8005551212.

Wildcard pattern is supported in dialed number configuration.

Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X.

You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                               For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX.

During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number.

Name (required)

The enterprise name for the dialed number/script selector. This
                                             				name must be unique among all dialed number/script selectors in the system.

Media routing domain (required)

(selection list) The media routing domain associated with the
                                             				selected dialed number/script selector.

Customer

(optional) (selection list) The customer associated with the
                                             				dialed number/script selector.

Default label

(optional) (selection list) The name of the default label for this
                                             				dialed number/script selector. The label must have been previously defined for
                                             				it to be in the selection list.

Use the Configuration Manager's Label List tool
                                                         				to define labels.

If the system software fails to determine a target for the call
                                             				within the routing client's timeout threshold, the default label for the
                                             				dialed number/script selector is used.

Description

(optional) Additional description for the dialed number/script
                                             				selector.

Permit Application Routing

Check this box to allow Application Routing. Indicates if remote
                                             				routing is permitted on this dialed number's script selector.

Reserved by IVR

Enabled when a Type 9 is selected in the Network VRU tab.

#### Dialed Number Mapping tab

Allows you to view the call types that are mapped to the selected dialed
                                 		number/script selector and to add, edit, or remove call-type mappings.

A call type is a classification for incoming calls. The call type
                                 		determines which routing script is executed to find a destination for the call.
                                 		A call type maps to specific combinations of dialed number (DN), calling line
                                 		ID (CLID), and caller-entered digits (CED).

You can create as many different mappings for each call type as you
                                 		want.

Column/ button

Description

CLID/App String 1

The string value by which the routing client identifies the
                                             				Calling Line ID.

CED/AppString 2

The string value by which the routing client identifies the caller-entered-digits.

Call Type

Name of the call type to map to the selected dialed number/script
                                             				selector.

Add

Allows selection of Application Strings and the Call Type. Click Add , and then in the Dialed Number Map Entry
                                             				dialog, select any of the radio buttons for:

Application String 1

All - To Make All CLID Values Valid.

None - To indicate no caller-entered digits are required
                                                   					 and/or are entered for the call type.

Prefix String 1 - Enter the prefix characters.

Match String 1 -Enter a string.

Application String 2

All - To Make All CLID Values Valid.

None - To indicate no caller-entered digits are required
                                                   					 and/or are entered for the call type.

Match String 2 - Enter a string.

Call Type

Choose a call type from the drop-down list.

Edit

Use this to edit the mapped entry.

Remove

Removes the entry.

Up/ Down

Allows sorting of the Call Type order.

#### Dialed Number Label tab

Allows you to view, add, or remove the mapping of labels to the selected
                                 		dialed number/script selector. These are additional to the default label
                                 		assigned in the Attributes tab.

Column/Button

Description

Name

This list contains all the labels currently assigned to the
                                             				selected dialed number/script selector.

Description

Additional information about the label.

Add

To assign a label to the dialed number/script selector selected in
                                             				the Dialed Number/Script Selector list box, click Add . Then in the Add Label dialog, select a
                                             				label name and click OK .

Remove

To remove a label from the dialed number/list selector selected in
                                             				the Dialed Number/Script Selector list box, select the label
                                             				name and click Remove .

| Step 1 | From the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > NIC Explorer . The NIC Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the filters you
                                          			 want. |
| Step 3 | Click Retrieve . The names of retrieved NICs are
                                          			 listed in the tree list box. |
| Step 4 | In the tree list box, select the NIC whose records you want to
                                          			 view. The configuration information displays in the fields on the right. |
| Step 5 | To view a routing client record, in the tree list box, expand the
                                          			 tree branch for the selected NIC and select the routing client icon. The routing client configuration information displays in the
                                             				window on the right. |

| Field/Button | Description |
|---|---|
| Controller ID (required) | A unique
                                             				identifier for the NIC's logical controller. This is a read-only field. When you create a new NIC , the
                                             				system places UNASSIGNED in this field and automatically creates an ID when
                                             				you save your edits. |
| Name (required) | The enterprise
                                             				name for the NIC's logical controller. This name also identifies the NIC and
                                             				must be unique for all logical controllers in the enterprise. |
| Client Type (required) | The type of
                                             				routing client serviced by the NIC. For example, Lucent, MCI, and so
                                             				on. When defining a new NIC, select one from the pop-up selection box. Selecting a type
                                             				of routing client automatically places that type's default values in the
                                             				Routing Client's Timeout Threshold, Late Threshold, Timeout Limit, Use DN/Label
                                             				Map, and Client Type fields. |
| Configuration Parameter | A string
                                             				containing information such as logon information, specific to the interface
                                             				controller device. For example: -rtuser UserName -rtpswd
                                                				  Password . |
| Description | Additional
                                             				information about the Logical interface controller. |
| Add Physical Interface
                                                				  Controller | Click this
                                             				button to add one or more physical interface controllers. This button is
                                             				disabled when there is no client type, as in a new NIC record, or when the NIC
                                             				node reaches its upper limit of Physical Interface Controllers. |

| Field/Button | Description |
|---|---|
| Associated Physical Interface Controllers | A duplexed NIC has two entries in the Physical Interface Controller
                                             				table and a single entry in the Logical Interface Controller table. |
| ID | A unique identifier for the NIC's associated physical interface
                                             				controller. This is a read-only field. When you create a new NIC, the system
                                             				places UNASSIGNED in this field and automatically creates an ID when you save your edits. |
| Name | The enterprise name of the routing client associated with the NIC . This name must be unique for all physical controllers
                                             				in the enterprise. |
| Description | Any other information about the physical interface controller. |
| Modify | To edit the name or description of the 
                                             				physical interface controller, click this button.  In the
                                             				Physical Interface Controller dialog enter your edits and click OK . |
| New | To enter a record for a new associated physical interface
                                             				controller, click this button and in the 
                                             				Physical Interface Controller dialog, enter its enterprise
                                             				name and click OK . The system assigns an ID to the controller when you save it to the
                                             				database. The NIC can represent multiple physical devices. The limit is
                                             				different for different client types. |
| Delete | Deletes the selected physical interface controller. |

| Field | Description |
|---|---|
| Name
                                                				  (required) | The enterprise
                                             				name of the routing client associated with the NIC. You can have more than one
                                             				routing client associated with a NIC. Typically, each routing client maps to a
                                             				subsystem within the ICX network. |
| Timeout
                                                				  threshold (required) | The maximum
                                             				time, in milliseconds, that the routing client can wait for a response to a
                                             				routing request. The NIC sends a default response slightly before this
                                             				threshold. |
| Late threshold
                                                				  (required) | A threshold
                                             				value, in milliseconds, for classifying responses as late. Any response that
                                             				exceeds this threshold is considered late even if it does not exceed the
                                             				Timeout Threshold. |
| Timeout limit
                                                				  (required) | The maximum
                                             				time, in seconds, that the routing client waits for a response. This is the
                                             				maximum time the routing client will tolerate consecutive response timeouts
                                             				before it stops sending requests to the system software. |
| Default call
                                                				  type | An enterprise
                                             				name for the call type. Initially, you can leave this field blank. For
                                             				information on this field, refer to the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Configuration
                                                				  parameters | A string
                                             				containing any initialization parameters that must be passed to the routing
                                             				client. For a public network, this might include the subsystem number. A null
                                             				value indicates no configuration parameters are provided. |
| Use DN/Label
                                                				  map | Indicates
                                             				whether the Dialed Number (DN) Label table is used to determine which labels
                                             				are valid for each dialed number. If not, all labels for the routing client are
                                             				valid for all dialed numbers. |
| Client type
                                                				  (required) | The type of
                                             				routing client that ultimately routes the call on the requesting Unified ICM
                                             				system. This field is
                                             				enabled only for the routing client associated with an intelligent network call
                                             				routing protocol (INCRP) NIC. In all other cases, it is the same as the logical
                                             				interface controller's client type. |
| Description | Additional
                                             				information about the routing client. |
| Network
                                                				  routing client | A name used to
                                             				associate routing clients across instances. The same string value for the
                                             				routing client on the network analysis module (NAM) and the corresponding
                                             				routing client on the Unified ICM (applies only for a network Unified ICM). |
| Default Media
                                                				  Routing Domain | (selection list)
                                             				The MRD associated with the routing client. |
| Congestion Treatment Mode | This field sets
                                             				the congestion treatment mode for routing clients. The default value is 0 when
                                             				you add a new routing client. The congestion
                                             				treatment mode definitions are as follows: 0 - Use
                                                   					 Congestion Control settings. 1 - Use
                                                   					 Dialed Number (DN) as default label for call treatment. 2 - Use
                                                   					 routing client as default label for call treatment. 3 - Use
                                                   					 global user-defined label for call treatment. Note To
                                                               						configure a user-defined label, use the Congestion Setting Configuration tool. 4 - Dialog
                                                   					 fail with an appropriate error code. 5 -
                                                   					 Release message to the routing client. | Note | To
                                                               						configure a user-defined label, use the Congestion Setting Configuration tool. |
| Note | To
                                                               						configure a user-defined label, use the Congestion Setting Configuration tool. |
| Default Label | Indicates the
                                             				default label for the routing client to treat the call when the system is
                                             				congested. Also see the following section: Gate
                                                				  Keeper (GK) NIC . |

| Note | To
                                                               						configure a user-defined label, use the Congestion Setting Configuration tool. |
|---|---|

| Step 1 | Follow the steps for viewing a NIC. The selected NIC's configuration information displays in the
                                                				fields on the right. |
|---|---|
| Step 2 | Edit the configuration information. You can modify all fields in the Logical Controller, Physical
                                                				Controller, and Router Client tabs that are not dimmed. When you make a modification, the Changed icon appears next to the edited item
                                                				(NIC or routing client) in the tree list box. |
| Step 3 | Click Save . The modified data in the Unified ICM database is saved and the Changed icon is removed from the display in
                                                				the tree list box. |

| Step 1 | From the Configuration Manager menu, select Tools > Explorer
                                                   				  Tools > NIC Explorer . The NIC Explorer window
                                             			 appears. |
|---|---|
| Step 2 | In the Select
                                                				filter data box, click Retrieve . This enables the Add
                                                				NIC button. |
| Step 3 | Click Add
                                                				NIC . A new NIC and its routing client display in the tree list box.
                                             			 Next to each is a To Be
                                                				Inserted icon . On the right of
                                                				the tree list box, tabbed fields also display for the new NIC's and routing
                                                				client's configuration information. |
| Step 4 | Fill in the
                                             			 tabbed fields. |
| Step 5 | Click Save . The newly defined NIC is saved in the database
                                             			 and the To Be
                                                				Inserted icon is removed from the tree list box. |

| Step 1 | Follow the steps for viewing a NIC. The selected NIC's
                                             			 configuration information displays in the fields on the right. |
|---|---|
| Step 2 | In the tree list box, select the NIC to which you want to add a
                                             			 routing client. This enables the Add Routing Client button. |
| Step 3 | Click Add Routing Client . A new routing client icon
                                             			 appears under the selected NIC in the tree list box and a new Routing Client
                                             			 tab appears in the window on the right. |
| Step 4 | Enter the needed routing client configuration information in the
                                             			 fields on the right. |
| Step 5 | Click Save . |

| Step 1 | Follow the steps for viewing a NIC. The selected NIC's configuration information displays in the
                                                				fields on the right. |
|---|---|
| Step 2 | In the tree list box, select the NIC whose records you want to
                                             			 delete. |
| Step 3 | Click Delete . This places a Marked for Deletion icon next to the NIC in the tree
                                             			 list box. This also toggles the Delete button to Undelete . To undelete a NIC marked for deletion, select it in the tree list
                                                				box and click Undelete . |
| Step 4 | Click Save . This deletes from the database the NIC marked for deletion and
                                                				removes it from the tree list box. After you do this, you cannot undelete the
                                                				NIC. |

| Note | Dialed Numbers on the Child Central Controller contains an example of how to configure dialed numbers on a child deployment. |
|---|---|

| Step 1 | From within the Configuration Manager menu, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . The Dialed Number/Script Selector List window
                                          			 appears. |
|---|---|
| Step 2 | In the Select filter data area, select the Routing client and Customer associated with the dialed number/script selector. Note Once you have saved a Dialed Number record to the Unified ICM database, you cannot update the Routing Client field. If you are viewing or modifying a previously created record and
                                             				you want to limit the number of records retrieved from the database, also
                                             				select one of the optional filters. | Note | Once you have saved a Dialed Number record to the Unified ICM database, you cannot update the Routing Client field. |
| Note | Once you have saved a Dialed Number record to the Unified ICM database, you cannot update the Routing Client field. |
| Step 3 | Click Retrieve . This enables the Add button and displays a list of the
                                          			 retrieved dialed number/script selectors. The properties of the dialed number/script selector selected in
                                             				the Dialed Number/Script Selector list box on the left side of the window are
                                             				displayed in the property tabs on the right side of the window: The following properties are displayed: The Attributes tab allows you to view and (if you have
                                                   					 maintenance access) to define, edit, or delete the attributes of the selected
                                                   					 dialed number/script selector. Attributes with an asterisk are required. The Dialed Number Label tab allows you to map labels (in
                                                   					 addition to a default label) to the selected dialed number/script selector. |
| Step 4 | This step depends on what you want to do: To add a new dialed number/script selector, click Add and enter the appropriate values in
                                                   					 the tabbed property fields on the right side of the window. To delete a dialed number/script selector, select that number
                                                   					 in the Dialed Number/Script Selector list box
                                                   					 and click Delete . To edit a dialed number/script selector, select that number in
                                                   					 the Dialed Number/Script Selector list box
                                                   					 and edit the appropriate values in the tabbed property fields on the right side
                                                   					 of the window. |
| Step 5 | Click Save to enter any edits into the database. The dialog closes, and for a new dialed number/script selector,
                                             				the Unified ICM database manager automatically generates a unique Dialed Number
                                             				ID for the routing client. |

| Note | Once you have saved a Dialed Number record to the Unified ICM database, you cannot update the Routing Client field. |
|---|---|

| Step 1 | Start the Dialed Number/Script Selector List Tool . |
|---|---|
| Step 2 | On the Main window of the Dialed Number/Script Selector List Tool,
                                             			 click Retrieve . |
| Step 3 | Click Add . The Dialed Number Attributes tab appears. |
| Step 4 | Select IPCC_RC as the Routing Client. |
| Step 5 | Select Cisco_Voice for the Media Routing Domain. |
| Step 6 | Set the Dialed Number String/Script Selector to 2500 (the route point set up on the Unified CM . |
| Step 7 | Set IPCC_RC_2500 as the Name, then select bh03 as the Customer setting. |
| Step 8 | Check Permit Application Routing on the route points
                                             			 controlled by the Parent (the Post route points and the Translation route
                                             			 points). This provides the link between the Parent and the Child. It gives
                                                				the Parent visibility to the Dialed Number so it can handle it. |
| Step 9 | Click Save . The dialed number appears in the tree list. |
| Step 10 | Repeat this to add two more dialed numbers (one for each skill
                                             			 group). When complete, you have the following DNs: 2500 Connects to all of the skill groups. Named IPCC_RC_2500. 2501 Connects to SG01. Named IPCC_RC_2501. 2502 Connects to SG02. Named IPCC_RC_2502. |
| Step 11 | Click Save , then Close to exit the Skill Group Explorer Tool. |

| Attribute | Description |
|---|---|
| Routing Client (required) | (selection list) The enterprise name of the routing client
                                             				associated with this dialed number/script selector. Once you select a routing
                                             				client and save to the database, this field becomes read only. |
| Dialed number/script selector string (required) | The string value by which the routing client identifies this
                                             				dialed number/script selector. This must be the value the routing client passes
                                             				to the system software for calls to this number. For example: 8005551212. Note Wildcard pattern is supported in dialed number configuration. Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X. You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                               For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX. During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number. | Note | Wildcard pattern is supported in dialed number configuration. Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X. You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                               For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX. During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number. |
| Note | Wildcard pattern is supported in dialed number configuration. Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X. You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                               For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX. During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number. |
| Name (required) | The enterprise name for the dialed number/script selector. This
                                             				name must be unique among all dialed number/script selectors in the system. |
| Media routing domain (required) | (selection list) The media routing domain associated with the
                                             				selected dialed number/script selector. |
| Customer | (optional) (selection list) The customer associated with the
                                             				dialed number/script selector. |
| Default label | (optional) (selection list) The name of the default label for this
                                             				dialed number/script selector. The label must have been previously defined for
                                             				it to be in the selection list. Note Use the Configuration Manager's Label List tool
                                                         				to define labels. If the system software fails to determine a target for the call
                                             				within the routing client's timeout threshold, the default label for the
                                             				dialed number/script selector is used. | Note | Use the Configuration Manager's Label List tool
                                                         				to define labels. |
| Note | Use the Configuration Manager's Label List tool
                                                         				to define labels. |
| Description | (optional) Additional description for the dialed number/script
                                             				selector. |
| Permit Application Routing | Check this box to allow Application Routing. Indicates if remote
                                             				routing is permitted on this dialed number's script selector. |
| Reserved by IVR | Enabled when a Type 9 is selected in the Network VRU tab. |

| Note | Wildcard pattern is supported in dialed number configuration. Only the last two characters of the dialed number can be configured as wildcards. The supported wildcard character is X. You cannot assign a valid number in the wildcard defined range, when the last two digits of dialed number are defined as wildcards.
                                                               For example, you cannot configure the valid dialed number 18000001101 under the wildcard entry 180000011XX. During DNlookup in the script editor, the dialed number is evaluated based on the wildcard-configured dialed number. |
|---|---|

| Note | Use the Configuration Manager's Label List tool
                                                         				to define labels. |
|---|---|

| Column/ button | Description |
|---|---|
| CLID/App String 1 | The string value by which the routing client identifies the
                                             				Calling Line ID. |
| CED/AppString 2 | The string value by which the routing client identifies the caller-entered-digits. |
| Call Type | Name of the call type to map to the selected dialed number/script
                                             				selector. |
| Add | Allows selection of Application Strings and the Call Type. Click Add , and then in the Dialed Number Map Entry
                                             				dialog, select any of the radio buttons for: Application String 1 All - To Make All CLID Values Valid. None - To indicate no caller-entered digits are required
                                                   					 and/or are entered for the call type. Prefix String 1 - Enter the prefix characters. Match String 1 -Enter a string. Application String 2 All - To Make All CLID Values Valid. None - To indicate no caller-entered digits are required
                                                   					 and/or are entered for the call type. Match String 2 - Enter a string. Call Type Choose a call type from the drop-down list. |
| Edit | Use this to edit the mapped entry. |
| Remove | Removes the entry. |
| Up/ Down | Allows sorting of the Call Type order. |

| Column/Button | Description |
|---|---|
| Name | This list contains all the labels currently assigned to the
                                             				selected dialed number/script selector. |
| Description | Additional information about the label. |
| Add | To assign a label to the dialed number/script selector selected in
                                             				the Dialed Number/Script Selector list box, click Add . Then in the Add Label dialog, select a
                                             				label name and click OK . Note For labels to appear in this dialog, they must have been
                                                      				previously defined for the selected dialed number/script selector routing
                                                      				client. Use the Label List tool to define labels. | Note | For labels to appear in this dialog, they must have been
                                                      				previously defined for the selected dialed number/script selector routing
                                                      				client. Use the Label List tool to define labels. |
| Note | For labels to appear in this dialog, they must have been
                                                      				previously defined for the selected dialed number/script selector routing
                                                      				client. Use the Label List tool to define labels. |
| Remove | To remove a label from the dialed number/list selector selected in
                                             				the Dialed Number/Script Selector list box, select the label
                                             				name and click Remove . |

| Note | For labels to appear in this dialog, they must have been
                                                      				previously defined for the selected dialed number/script selector routing
                                                      				client. Use the Label List tool to define labels. |
|---|---|