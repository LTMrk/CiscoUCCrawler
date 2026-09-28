---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-41e0e12598
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/alert.html
retrieved_at: 2026-08-21T17:11:16.718747+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Alert

## Chapter: Alert

# Alert

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

SNMP

Boolean

Yes

true

false

true

This
                                          				  settings specifies whether SNMP alert to be generated.

Syslog

Boolean

Yes

false

false

false

This
                                          				  settings specifies whether Syslog alert to be generated.

Message

Boolean

Yes

Not Applicable

true

Blank

The alert
                                          				  message to be logged in SNMP ans Syslog.

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

## Exit
                        	 States

Name

Notes

done

The element is successfully run.

| The Alert element is used to generate syslog alerts and
                                 			 SNMP alerts based on the values set in the Element Configuration view. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| SNMP | Boolean | Yes | true | false | true | This
                                          				  settings specifies whether SNMP alert to be generated. |
| Syslog | Boolean | Yes | false | false | false | This
                                          				  settings specifies whether Syslog alert to be generated. |
| Message | Boolean | Yes | Not Applicable | true | Blank | The alert
                                          				  message to be logged in SNMP ans Syslog. |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |

| Name | Notes |
|---|---|
| done | The element is successfully run. |