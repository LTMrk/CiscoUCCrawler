---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-3b9a63fd87
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_t4e2a5b5_00_throw.html
retrieved_at: 2026-08-21T17:29:15.986784+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter:  Throw

## Chapter:  Throw

- Throw

- General

# Throw

Example, com.audium.MyException

## General

Name (Label)

Type

Req'd

Default

Notes

Event Code*

String

Yes

This is a
                                          				  mandatory field to be filled if you are using the Throw element in the call
                                          				  flow. You can define the name of the custom event or exception in this field.

Message

String

Yes

You can
                                          				  enter custom exception message and create a substitution tag in this field. For
                                          				  example, {Data.Session.lastException.message}.

Custom Field1

Custom Field 2

Custom Field 3

String

Yes

You can
                                          				  enter the value in this field from the substitutions tag, the last exception
                                          				  session variable will be used for the same. The last exception session variable
                                          				  will hold the last thrown exception.

| The Throw functionality is part of event handler feature. The Throw element is used to raise a custom exception when running a call flow. It can be used in a main flow or in a subflow. The Throw element is used to throw recently caught Java Exceptions, VXML Exception or user defined custom exceptions. Example, com.audium.MyException |
|---|

| Name (Label) | Type | Req'd | Default | Notes |
|---|---|---|---|---|
| Event Code* | String | Yes |  | This is a
                                          				  mandatory field to be filled if you are using the Throw element in the call
                                          				  flow. You can define the name of the custom event or exception in this field. |
| Message | String | Yes |  | You can
                                          				  enter custom exception message and create a substitution tag in this field. For
                                          				  example, {Data.Session.lastException.message}. |
| Custom Field1 Custom Field 2 Custom Field 3 | String | Yes |  | You can
                                          				  enter the value in this field from the substitutions tag, the last exception
                                          				  session variable will be used for the same. The last exception session variable
                                          				  will hold the last thrown exception. |