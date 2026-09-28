---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-b155aba0df
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/ccvp_mp_se715611_00_subflow-start.html
retrieved_at: 2026-08-21T17:30:53.669951+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

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