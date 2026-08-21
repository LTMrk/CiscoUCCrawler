---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1262-admin-guide-cfin-b-1262-cis-38a7ead68e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1262/admin/guide/cfin_b_1262_cisco-finesse-administration-guide/cfin_m_1261-manage-call-variables-layouts.html
retrieved_at: 2026-08-21T15:55:20.043805+00:00
---

Cisco Finesse Administration Guide, Release 12.6(2)

# Cisco Finesse Administration Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Manage Call Variables Layouts

## Chapter: Manage Call Variables Layouts

# Manage Call Variables Layouts

## Call Variables Layouts

You can use the Call Variables Layouts gadget to define how call variables appear on the Finesse agent desktop. You can configure
                           up to 200 unique Call Variables Layouts (one default and 199 custom layouts). As part of this functionality:

Each layout has a name (required) and description (optional).

You can change the name and description of the default Call Variables Layout.

You cannot delete the default Call Variables Layout.

Finesse appends (Default) to the name of the default Call Variables Layout.

To display a custom Call Variables Layout, in the Unified CCE routing script set the user.Layout ECC variable to the name of a configured Call Variables Layout. In this case, if no custom layouts match the user.Layout value
                                 (or no custom layouts are configured), Finesse displays the default layout.

Finesse retains the custom layout as specified by the user.Layout ECC variable on CTI server failover. During PG failover,
                                 Finesse changes the active call layout to the default layout while retaining the call variables and time indicators.

## Call Variables

Each Call Variables Layout supports one variable in the header of the call control gadget and up to a total of 20 variables
                           in two columns below the header (up to 10 in each column). You can use call variables, Extended Call Context (ECC) variables,
                           or the following Outbound Option ECC variables:

BACampaign

BAAccountNumber

BAResponse

BAStatus

BADialedListID

BATimeZone

BABuddyName

Columns can be empty.

The administrator can include the following additional fields in the Call Variables Layout. These variables appear as a drop-down
                           list in the call variable gadget which the admin can assign to a layout.

queueNumber

queueName

callKeyCallId

callKeyPrefix

callKeySequenceNum

wrapUpReason

The callKeyPrefix indicates the day when the call was routed.

The callKeyCallId indicates the unique number for the call routed on that day.

To uniquely locate the call in Unified CCE database records, concatenate the two variables callKeyPrefix and callKeyCallId.

To enable Outbound Option data to appear in Cisco Finesse, the administrator must edit the Default Layout to include some
                           or all Outbound Option variables.

### Edit Call Variables

Administrator can set call variables (callVariable1 to callVariable10) values and ECC variable values as editable. Amongst
                                 BA (campaign-based outbound calls) variables, only BAResponse can be edited. The agent and the supervisor can edit the call
                                 variable values during an active call or in the wrap-up state.

Cisco Finesse refers to the ECC variable length from the AWDB and this length is validated while you edit the ECC variable.
                                                   Cisco Finesse server takes about 15 minutes to update these changes from AWDB. Agents must sign in again for the ECC variable
                                                   configuration changes to reflect in the Cisco Finesse desktop.

Call variables edit operation updates the values of the variables within the particular call. All entities listening to dialog
                                                   events receive the updated call variables through the Cisco Finesse notifications. If any CTI clients are connected to the
                                                   same Agent PG , they also receive notifications of the changed call data though CTI call events. However, application scripts or databases
                                                   that are used to populate the call variables are not directly affected by this edit.

Call variables edit operation updates the values of the variables within the particular call. All entities listening to dialog
                                             events receive the updated call variables through the Cisco Finesse notifications. If any CTI clients are connected to the
                                             same Agent PG , they also receive notifications of the changed call data though CTI call events. However, application scripts or databases
                                             that are used to populate the call variables are not directly affected by this edit.

For more information on call variable limits, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

## Configure Call Variables Layouts

Step 1

From the Manage Call Variables Layouts gadget:

Click New to create a new Call Variables Layout.

- Choose a layout from the list and click Edit to modify an existing Call Variables Layout (or click Delete to remove it).

Step 2

Under Create New Layout (or under Edit <layout name> when editing an existing layout):

Enter a name for the Call Variables Layout (maximum 40 characters).

Enter a description of the Call Variables Layout (maximum 128 characters).

Step 3

Under Call Header Layout:

Enter the display name that you want to appear in the header of the Call Control gadget on the Finesse desktop. For example, Customer Name (maximum 50 characters).

From the drop-down list, choose the call variable or Outbound Option ECC variable that you want to appear in the header. For
                                                example, callVariable3 (maximum 32 characters).

Step 4

In the Call Body Left-Hand Layout and Call Body Right-Hand Layout areas:

Click Add Row to add a new row (or click the "X" to delete a row).

For each row:

Enter the display name that you want to appear on the desktop. For example, Customer Name (maximum 50 characters).

Enter the corresponding call variable or Outbound Option ECC variable from the drop-down list (maximum 32 characters).

Step 5

Select up to five call variables using the check box. The selected call variables are displayed in agent call popover and
                                       supervisor active call details.

If you do not select any call variables, the first two call variables from the Call Body Left-Hand layout area will be displayed
                                                      in the agent call popover and supervisor active call details. If there are no call variables in the Left-hand layout area,
                                                      then the call variables in the Right-Hand Layout will be selected.

Step 6

Turn on the toggle switch to enable the edit option for a specific call variable. By default, this option is turned off.

Call variable (callVariable1 to callVariable10) values are editable.

ECC variable values are editable.

Amongst BA variables (campaign-based outbound calls), only BAResponse value is editable.

Step 7

Click Save to save the changes, or Cancel to discard the changes.

When you modify the Call Variables Layout of the agent desktop, the changes you make take effect after three seconds. However,
                                                      agents or supervisors who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                                      on their desktops.

Step 8

To view the latest configured Call Variables Layout, click Refresh from the Manage Call Variables Layouts gadget.

### Call Variables Popover

In the call layout popover configuration, you can configure the call header and up to five call variables in the Call Variables
                                 Layout. These variables are displayed in the agent's call popover and active call details in the Team Performance gadget for
                                 a supervisor.

If you do not select any call variables, the first two call variables from the Call Body Left-Hand layout area will be displayed
                                 in the agent call popover and supervisor active call details. If there are no call variables in the Left-hand layout area,
                                 then the call variables in the Right-Hand Layout will be selected.

In upgrade scenarios, by default, the first two call variables will be displayed in the agent call popover and supervisor
                                 active call details. You can modify the configuration of the popover variables to improve the agent and supervisor experience.

## Add ECC Variables to Call Variables Layout

Step 1

In the header or the row where you want the ECC variable to appear, from the Variable drop-down list, choose Custom .

Step 2

In the Custom/ECC Variable Name field, enter the name of the ECC variable you want to appear on the agent desktop.

Step 3

Click Set .

The ECC variable now appears in the Variable drop-down list for selection.

## Assign Call Variables Layouts

Step 1

In CCE Configuration Manager, create an ECC variable called user.Layout in the Expanded Call Variable list.

If a user.layout and a user.Layout are specified, Finesse will prioritize user.layout over user.Layout. If the layout specified
                                                      in the user.Layout or user.layout is not found, Finesse uses the Default layout.

Step 2

Add user.Layout to the CCE routing script. Use a Set Variable node in an appropriate place in the script to set the value of user.Layout
                                       to the name of the call variables layout to display. The layout name should match the name of a call variables layout that
                                       was created on the Call Variables Layout tab in Finesse Administration .

## Manipulate Call Variables Layouts with a Workflow

You can manipulate the call variables layout that an agent sees when a call is answered by using a workflow. To do so, configure
                              an HTTP Request workflow action and set the value of the ECC variable user. Layout to the name of the custom layout to display.

For information about how and when workflows are run, see Workflows and Workflow Actions .

For more details, see the section, "Adding an HTTP Request Workflow Action" in the technical paper Cisco Finesse: How to Create a Screen-Pop Workflow .

| Note | The callKeyPrefix indicates the day when the call was routed. The callKeyCallId indicates the unique number for the call routed on that day. To uniquely locate the call in Unified CCE database records, concatenate the two variables callKeyPrefix and callKeyCallId. |
|---|---|

| Note | Cisco Finesse refers to the ECC variable length from the AWDB and this length is validated while you edit the ECC variable.
                                                   Cisco Finesse server takes about 15 minutes to update these changes from AWDB. Agents must sign in again for the ECC variable
                                                   configuration changes to reflect in the Cisco Finesse desktop. Call variables edit operation updates the values of the variables within the particular call. All entities listening to dialog
                                                   events receive the updated call variables through the Cisco Finesse notifications. If any CTI clients are connected to the
                                                   same Agent PG , they also receive notifications of the changed call data though CTI call events. However, application scripts or databases
                                                   that are used to populate the call variables are not directly affected by this edit. |
|---|---|

| Note | Call variables edit operation updates the values of the variables within the particular call. All entities listening to dialog
                                             events receive the updated call variables through the Cisco Finesse notifications. If any CTI clients are connected to the
                                             same Agent PG , they also receive notifications of the changed call data though CTI call events. However, application scripts or databases
                                             that are used to populate the call variables are not directly affected by this edit. |
|---|---|

| Step 1 | From the Manage Call Variables Layouts gadget: Click New to create a new Call Variables Layout. Choose a layout from the list and click Edit to modify an existing Call Variables Layout (or click Delete to remove it). |
|---|---|
| Step 2 | Under Create New Layout (or under Edit <layout name> when editing an existing layout): Enter a name for the Call Variables Layout (maximum 40 characters). Enter a description of the Call Variables Layout (maximum 128 characters). |
| Step 3 | Under Call Header Layout: Enter the display name that you want to appear in the header of the Call Control gadget on the Finesse desktop. For example, Customer Name (maximum 50 characters). From the drop-down list, choose the call variable or Outbound Option ECC variable that you want to appear in the header. For
                                                example, callVariable3 (maximum 32 characters). |
| Step 4 | In the Call Body Left-Hand Layout and Call Body Right-Hand Layout areas: Click Add Row to add a new row (or click the "X" to delete a row). For each row: Enter the display name that you want to appear on the desktop. For example, Customer Name (maximum 50 characters). Enter the corresponding call variable or Outbound Option ECC variable from the drop-down list (maximum 32 characters). |
| Step 5 | Select up to five call variables using the check box. The selected call variables are displayed in agent call popover and
                                       supervisor active call details. Note If you do not select any call variables, the first two call variables from the Call Body Left-Hand layout area will be displayed
                                                      in the agent call popover and supervisor active call details. If there are no call variables in the Left-hand layout area,
                                                      then the call variables in the Right-Hand Layout will be selected. | Note | If you do not select any call variables, the first two call variables from the Call Body Left-Hand layout area will be displayed
                                                      in the agent call popover and supervisor active call details. If there are no call variables in the Left-hand layout area,
                                                      then the call variables in the Right-Hand Layout will be selected. |
| Note | If you do not select any call variables, the first two call variables from the Call Body Left-Hand layout area will be displayed
                                                      in the agent call popover and supervisor active call details. If there are no call variables in the Left-hand layout area,
                                                      then the call variables in the Right-Hand Layout will be selected. |
| Step 6 | Turn on the toggle switch to enable the edit option for a specific call variable. By default, this option is turned off. Note Call variable (callVariable1 to callVariable10) values are editable. ECC variable values are editable. Amongst BA variables (campaign-based outbound calls), only BAResponse value is editable. | Note | Call variable (callVariable1 to callVariable10) values are editable. ECC variable values are editable. Amongst BA variables (campaign-based outbound calls), only BAResponse value is editable. |
| Note | Call variable (callVariable1 to callVariable10) values are editable. ECC variable values are editable. Amongst BA variables (campaign-based outbound calls), only BAResponse value is editable. |
| Step 7 | Click Save to save the changes, or Cancel to discard the changes. Note When you modify the Call Variables Layout of the agent desktop, the changes you make take effect after three seconds. However,
                                                      agents or supervisors who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                                      on their desktops. | Note | When you modify the Call Variables Layout of the agent desktop, the changes you make take effect after three seconds. However,
                                                      agents or supervisors who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                                      on their desktops. |
| Note | When you modify the Call Variables Layout of the agent desktop, the changes you make take effect after three seconds. However,
                                                      agents or supervisors who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                                      on their desktops. |
| Step 8 | To view the latest configured Call Variables Layout, click Refresh from the Manage Call Variables Layouts gadget. |

| Note | If you do not select any call variables, the first two call variables from the Call Body Left-Hand layout area will be displayed
                                                      in the agent call popover and supervisor active call details. If there are no call variables in the Left-hand layout area,
                                                      then the call variables in the Right-Hand Layout will be selected. |
|---|---|

| Note | Call variable (callVariable1 to callVariable10) values are editable. ECC variable values are editable. Amongst BA variables (campaign-based outbound calls), only BAResponse value is editable. |
|---|---|

| Note | When you modify the Call Variables Layout of the agent desktop, the changes you make take effect after three seconds. However,
                                                      agents or supervisors who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                                      on their desktops. |
|---|---|

| Step 1 | In the header or the row where you want the ECC variable to appear, from the Variable drop-down list, choose Custom . |
|---|---|
| Step 2 | In the Custom/ECC Variable Name field, enter the name of the ECC variable you want to appear on the agent desktop. |
| Step 3 | Click Set . The ECC variable now appears in the Variable drop-down list for selection. |

| Step 1 | In CCE Configuration Manager, create an ECC variable called user.Layout in the Expanded Call Variable list. Note If a user.layout and a user.Layout are specified, Finesse will prioritize user.layout over user.Layout. If the layout specified
                                                      in the user.Layout or user.layout is not found, Finesse uses the Default layout. | Note | If a user.layout and a user.Layout are specified, Finesse will prioritize user.layout over user.Layout. If the layout specified
                                                      in the user.Layout or user.layout is not found, Finesse uses the Default layout. |
|---|---|---|---|
| Note | If a user.layout and a user.Layout are specified, Finesse will prioritize user.layout over user.Layout. If the layout specified
                                                      in the user.Layout or user.layout is not found, Finesse uses the Default layout. |
| Step 2 | Add user.Layout to the CCE routing script. Use a Set Variable node in an appropriate place in the script to set the value of user.Layout
                                       to the name of the call variables layout to display. The layout name should match the name of a call variables layout that
                                       was created on the Call Variables Layout tab in Finesse Administration . |

| Note | If a user.layout and a user.Layout are specified, Finesse will prioritize user.layout over user.Layout. If the layout specified
                                                      in the user.Layout or user.layout is not found, Finesse uses the Default layout. |
|---|---|