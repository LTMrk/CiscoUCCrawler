---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-70361bd4d7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_rab9e1a5_00_reqicmlabel.html
retrieved_at: 2026-08-21T17:26:17.358627+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: ReqICMLabel

## Chapter: ReqICMLabel

# ReqICMLabel

The ReqICMLabel element allows a Call Studio script to pass caller input, Call Peripheral Variables, and Expanded Call Context (ECC) variables
                                    to an ICM script. The ReqICMLabel must be inserted into a Call Studio script as a decision element. In Call Studio, the returned
                                    ICM label contains a result, which can be used by other elements in the same application, such as the Transfer or Audio element.

After the
                                    				ReqICMLabel exits its done path, you can retrieve the values set by the ICM
                                    				script by selecting the Element Data tab for the ReqICMLabel element. The
                                    				element data value is {Data.Element. ReqICMLabelElement .result}. ReqICMLabelElement is the name
                                    				of the ReqICMLabel element in the Studio script. The default name for this
                                    				element is ReqICMLabel_ <n> , where <n> is a number. The first ReqICMLabel you add to the script is named ReqICMLabel_01 , the second is named ReqICMLabel_02 , etc. For example, if you changed ReqICMLabel
                                    				to GetICMLabel, the value returned from ICM would be
                                    				{Data.Element.GetICMLabel.result}, where result is the variable of the
                                    				ReqICMLabel element that contains the ICM label.

For more
                                    				information on using the ReqICMLabel, refer to the Configuration Guide for Cisco
                                       				  Unified Customer Voice Portal .

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Call Peripheral Variables 1 – 10

(callvar1 – callvar10)

string

No

true

true

None

Call Peripheral Variables passed by the Studio
                                          script to the ICM Server. Each of these settings can be a maximum length of 210
                                          characters. The ICM Server returns a name-value pair for up to 10 Call
                                          Peripheral Variables in a result. Any value that is placed in callvar<n>
                                          from a Call Studio script is returned unchanged, if the ICM Script does not
                                          change it.

Call
                                          Peripheral Variables Return 1 – 10

(callvarReturn1 –
                                          callvarReturn10)

string

No

true

true

None

Call Peripheral Variables created upon the return
                                          of the ICM Label request, regardless of whether or not these variables are
                                          filled by the ICM Script. The reason we need two sets of these variables is to
                                          keep reporting the To ICM Call Peripheral Variables separate from what is
                                          returned from the ICM.

FromExtVXML0 - 3

(External VXML 0 – External VXML 3)

string array

No

true

true

None

Expanded Call Context (ECC) variables passed by the Studio script to the ICM Server. Each variable is a string of name-value
                                          pairs, separated by semicolons, for up to 4 external VXML variables. Each of these settings can be a maximum length of 210
                                          characters.

ToExtVXML0 - 4

(External VXML 0 –
                                          External VXML 4)

string
                                          array

No

true

true

None

Expanded Call Context (ECC) variables received from the ICM script. The ICM Server returns a string of name-value pairs, separated
                                          by semicolons, for up to 5 external VXML variables.

Timeout

integer

Yes

true

true

3000 (ms)

The number of
                                          milliseconds the transfer request waits for a response from the ICM Server
                                          before timing out. Note: This value can only be increased or decreased by
                                          increments of 500 ms.

caller_input

(Caller Input)

string

No

true

true

None

This
                                          setting can be a maximum length of 210 characters. The value of this setting
                                          will be sent from VXML Server to ICM at runtime. Should a response from ICM be
                                          needed, the Call Peripheral Variables or ToExtVXML settings should be
                                          used.

## Element Data

Name

Type

Notes

result

string

ICM Label returned from an ICM
                                          server.

callvar<n>

string

Call Peripheral
                                          Variables that the Studio scripts passes to the ICM Server. Valid Call
                                          Peripheral Variables are callvar1 – callvar10.

callvarReturn<n>

string

Call Peripheral Variables that the ICM script returns to the VXML Server.
                                          Valid Call Peripheral Variables are callvarReturn1 – callvarReturn10.

For example, if an ICM script contains call peripheral variable 3 with
                                          the string value "CompanyName=Cisco Systems, Inc" , you can access the value of
                                          CompanyName that is returned by the ICM script by using:

Data.Element.ReqICMLabelElement.callvarReturn3 .

The returned value is Cisco Systems, Inc .

## Session Data

Name

Type

Notes

name

string

Value for a name-value pair contained in a ToExtVXML variable returned in the ICM label. You
                                          must know which name-value pairs are set in the ICM script to retrieve the
                                          correct value from the Call Studio script.

For example, if an ICM
                                          script contains a user.microapp.ToExtVXML0 variable
                                          with the string value CustomerName=Mantle , specify Data.Session.CustomerName . If the same ICM script
                                          contains a user.microapp.ToExtVXML0 variable with
                                          the string value BusinessType=Manufacturing , you can
                                          access the customer business type returned by the ICM script by using Data.Session.BusinessType .

## Exit States

Name

Notes

done

The element is run successfully and the value is retrieved.

error

The element failed to
                                          retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco

com.cisco.cvp.vxml.custelem.ReqICMLabel

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The ReqICMLabel element allows a Call Studio script to pass caller input, Call Peripheral Variables, and Expanded Call Context (ECC) variables
                                    to an ICM script. The ReqICMLabel must be inserted into a Call Studio script as a decision element. In Call Studio, the returned
                                    ICM label contains a result, which can be used by other elements in the same application, such as the Transfer or Audio element. After the
                                    				ReqICMLabel exits its done path, you can retrieve the values set by the ICM
                                    				script by selecting the Element Data tab for the ReqICMLabel element. The
                                    				element data value is {Data.Element. ReqICMLabelElement .result}. ReqICMLabelElement is the name
                                    				of the ReqICMLabel element in the Studio script. The default name for this
                                    				element is ReqICMLabel_ <n> , where <n> is a number. The first ReqICMLabel you add to the script is named ReqICMLabel_01 , the second is named ReqICMLabel_02 , etc. For example, if you changed ReqICMLabel
                                    				to GetICMLabel, the value returned from ICM would be
                                    				{Data.Element.GetICMLabel.result}, where result is the variable of the
                                    				ReqICMLabel element that contains the ICM label. For more
                                    				information on using the ReqICMLabel, refer to the Configuration Guide for Cisco
                                       				  Unified Customer Voice Portal . |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Call Peripheral Variables 1 – 10 (callvar1 – callvar10) | string | No | true | true | None | Call Peripheral Variables passed by the Studio
                                          script to the ICM Server. Each of these settings can be a maximum length of 210
                                          characters. The ICM Server returns a name-value pair for up to 10 Call
                                          Peripheral Variables in a result. Any value that is placed in callvar<n>
                                          from a Call Studio script is returned unchanged, if the ICM Script does not
                                          change it. |
| Call
                                          Peripheral Variables Return 1 – 10 (callvarReturn1 –
                                          callvarReturn10) | string | No | true | true | None | Call Peripheral Variables created upon the return
                                          of the ICM Label request, regardless of whether or not these variables are
                                          filled by the ICM Script. The reason we need two sets of these variables is to
                                          keep reporting the To ICM Call Peripheral Variables separate from what is
                                          returned from the ICM. |
| FromExtVXML0 - 3 (External VXML 0 – External VXML 3) | string array | No | true | true | None | Expanded Call Context (ECC) variables passed by the Studio script to the ICM Server. Each variable is a string of name-value
                                          pairs, separated by semicolons, for up to 4 external VXML variables. Each of these settings can be a maximum length of 210
                                          characters. |
| ToExtVXML0 - 4 (External VXML 0 –
                                          External VXML 4) | string
                                          array | No | true | true | None | Expanded Call Context (ECC) variables received from the ICM script. The ICM Server returns a string of name-value pairs, separated
                                          by semicolons, for up to 5 external VXML variables. |
| Timeout | integer | Yes | true | true | 3000 (ms) | The number of
                                          milliseconds the transfer request waits for a response from the ICM Server
                                          before timing out. Note: This value can only be increased or decreased by
                                          increments of 500 ms. |
| caller_input (Caller Input) | string | No | true | true | None | This
                                          setting can be a maximum length of 210 characters. The value of this setting
                                          will be sent from VXML Server to ICM at runtime. Should a response from ICM be
                                          needed, the Call Peripheral Variables or ToExtVXML settings should be
                                          used. |

| Name | Type | Notes |
|---|---|---|
| result | string | ICM Label returned from an ICM
                                          server. |
| callvar<n> | string | Call Peripheral
                                          Variables that the Studio scripts passes to the ICM Server. Valid Call
                                          Peripheral Variables are callvar1 – callvar10. |
| callvarReturn<n> | string | Call Peripheral Variables that the ICM script returns to the VXML Server.
                                          Valid Call Peripheral Variables are callvarReturn1 – callvarReturn10. For example, if an ICM script contains call peripheral variable 3 with
                                          the string value "CompanyName=Cisco Systems, Inc" , you can access the value of
                                          CompanyName that is returned by the ICM script by using: Data.Element.ReqICMLabelElement.callvarReturn3 . The returned value is Cisco Systems, Inc . |

| Name | Type | Notes |
|---|---|---|
| name | string | Value for a name-value pair contained in a ToExtVXML variable returned in the ICM label. You
                                          must know which name-value pairs are set in the ICM script to retrieve the
                                          correct value from the Call Studio script. For example, if an ICM
                                          script contains a user.microapp.ToExtVXML0 variable
                                          with the string value CustomerName=Mantle , specify Data.Session.CustomerName . If the same ICM script
                                          contains a user.microapp.ToExtVXML0 variable with
                                          the string value BusinessType=Manufacturing , you can
                                          access the customer business type returned by the ICM script by using Data.Session.BusinessType . |

| Name | Notes |
|---|---|
| done | The element is run successfully and the value is retrieved. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco | com.cisco.cvp.vxml.custelem.ReqICMLabel |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |