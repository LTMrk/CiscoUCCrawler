---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-e788564d1a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/subflow_return.html
retrieved_at: 2026-08-21T17:09:19.012807+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Subflow
	 Start

## Chapter: Subflow
	 Start

- Subflow                              	 Start

- Events

- Exit

# Subflow
                     	 Start

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

| Subflow Start element is the first element for a subflow. This element is not created from the element view however, it is created automatically
                                 when a new subflow is created. Subflow Start element cannot be deleted it can just be renamed. You can have only one Subflow
                                 Start element in a subflow. Subflow Start element provides the definition of a subflow using its configuration. This element
                                 defines the parameters subflow can receive while running the subflow. Subflow Start Element uses a data model to save its
                                 configuration which is implemented in SubflowStartConfig class. The Subflow Argument Data available at the Element Configuration view. Subflows accepts inputs from the calling flows
                                 as arguments. Subflow Call element allows to send multiple arguments of different types to a subflow. The set of arguments
                                 in Subflow Start should match with the set of arguments in Subflow Call. |
|---|

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception, VXML Event, or Custom Exception
                                       				event handler type for this element from the drop-down list. |

| Name | Notes |
|---|---|
| next | The default exit state.
                                          				  The events that are entered for this element as added as the exit state in the
                                          				  call flow. |