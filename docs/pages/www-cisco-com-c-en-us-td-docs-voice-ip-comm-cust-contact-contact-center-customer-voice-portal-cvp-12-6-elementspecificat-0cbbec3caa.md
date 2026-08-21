---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-0cbbec3caa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_s373d96f_00_subflow-call.html
retrieved_at: 2026-08-21T17:23:12.023165+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Subflow
	 Call

## Chapter: Subflow
	 Call

- Subflow                              	 Call

- Events

- Exit

# Subflow
                     	 Call

General - This tab provides the means to associate a subflow
                                          					 call with Call Subflow element. It provides a drop down list of all the
                                          					 available subflows in a project. Only one of the subflow can be selected from
                                          					 the list.

Data - This tab provides the information about subflow argument data and return
                                          					 data.

Subflow Argument Data -
                                                						  Subflows accepts inputs from the calling flows as arguments. Subflow Call
                                                						  element allows to send multiple arguments of different types to a subflow.

Subflow Return Data -
                                                						  Subflows returns data as processed output. Subflow Call element allows to
                                                						  accept multiple return values of different types from a subflow.

Sub flow call parameters (Argument Data and Return Data) are
                                                				  auto populated from the sub flow start and return elements respectively. If
                                                				  changes are done to sub flow start or return after the call element is created
                                                				  and assigned to the sub flow, call element needs to be reloaded. This can be
                                                				  done by clicking out and clicking back on the sub flow call element.

Cisco Unified Call Studio
                                    				allows you to modify both the Subflow Argument Data and Subflow Return Data
                                    				variable value directly from the Variables View while debugging a call flow.
                                    				You can modify the data value directly from the value pane or right-click on
                                    				the data variable and select Change Value to modify the value.

## Events

Name (Label)

Notes

Event Type

## Exit

Name

Notes

next

The default exit state.
                                          				  The events that are entered for this element as added as the exit state in the
                                          				  call flow.

| The Subflow
                                    				call element is used to call the subflows from any call flows inside
                                 			 the application. The Subflow Call element is available in elements view. The
                                 			 Subflow Call element can be deleted, renamed, or can be used multiple times.
                                 			 The Call Subflow Element has the following three configurable tabs: General - This tab provides the means to associate a subflow
                                          					 call with Call Subflow element. It provides a drop down list of all the
                                          					 available subflows in a project. Only one of the subflow can be selected from
                                          					 the list. Data - This tab provides the information about subflow argument data and return
                                          					 data. Subflow Argument Data -
                                                						  Subflows accepts inputs from the calling flows as arguments. Subflow Call
                                                						  element allows to send multiple arguments of different types to a subflow. Subflow Return Data -
                                                						  Subflows returns data as processed output. Subflow Call element allows to
                                                						  accept multiple return values of different types from a subflow. Note Sub flow call parameters (Argument Data and Return Data) are
                                                				  auto populated from the sub flow start and return elements respectively. If
                                                				  changes are done to sub flow start or return after the call element is created
                                                				  and assigned to the sub flow, call element needs to be reloaded. This can be
                                                				  done by clicking out and clicking back on the sub flow call element. Cisco Unified Call Studio
                                    				allows you to modify both the Subflow Argument Data and Subflow Return Data
                                    				variable value directly from the Variables View while debugging a call flow.
                                    				You can modify the data value directly from the value pane or right-click on
                                    				the data variable and select Change Value to modify the value. | Note | Sub flow call parameters (Argument Data and Return Data) are
                                                				  auto populated from the sub flow start and return elements respectively. If
                                                				  changes are done to sub flow start or return after the call element is created
                                                				  and assigned to the sub flow, call element needs to be reloaded. This can be
                                                				  done by clicking out and clicking back on the sub flow call element. |
|---|---|---|
| Note | Sub flow call parameters (Argument Data and Return Data) are
                                                				  auto populated from the sub flow start and return elements respectively. If
                                                				  changes are done to sub flow start or return after the call element is created
                                                				  and assigned to the sub flow, call element needs to be reloaded. This can be
                                                				  done by clicking out and clicking back on the sub flow call element. |

| Note | Sub flow call parameters (Argument Data and Return Data) are
                                                				  auto populated from the sub flow start and return elements respectively. If
                                                				  changes are done to sub flow start or return after the call element is created
                                                				  and assigned to the sub flow, call element needs to be reloaded. This can be
                                                				  done by clicking out and clicking back on the sub flow call element. |
|---|---|

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception, VXML Event, or Custom Exception
                                       				event handler type for this element from the drop-down list. |

| Name | Notes |
|---|---|
| next | The default exit state.
                                          				  The events that are entered for this element as added as the exit state in the
                                          				  call flow. |