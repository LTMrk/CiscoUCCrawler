---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-common-xml-ref-guide-tpcc-b-xml-command-ref-html-8db16e5d7f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/common/xml_ref_guide/tpcc_b_xml-command-ref.html
retrieved_at: 2026-08-17T01:06:58.020155+00:00
---

XML Reference Guide for Cisco IP Phone Multiplatform Phones

# XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Download Options

Updated: November 19, 2025

First Published: November 19, 2025

# New and Changed Information

## Revision History

Release

What's New and Updated

Font_Size

TLS_Client_Min_Version

TLS_Server_Min_Version

SSRC_Reset_on_Rx_RE-INVITE

SSRC_Reset_on_Tx_RE-INVITE

TLS_Client_Min_Version

TLS_Server_Min_Version

Office_Hours_Enabled

Work_Days

Working_Hours_Start

Working_Hours_End

LED_Indicator_In_Display_Off_Mode

Display_Off_Idle_Timeout__mins_

Certificate_Select

CDC_Server_1_

CDC_Root_CA_Fingerprint_1_

CDC_Challenge_Password_1_

Enable_802.1X_Authentication

Accessibility

Voice_Feedback_Enable

Voice_Feedback_Speed

Key_Again_Reset_Time

Key_Double_Press_Time

Key_Triple_Press_Time

Voice_Feedback_Volume

Font_Size

SDP_IP_Preference

Forced_NAT64

Call_Appearances_Per_Line

X-SWITCH-INFO_Support

BLF_Callpark_On_Line_Key_Enable

Firmware Release 12.0(3)

Time_Format

Unit_n_Extension_m_

Unit_n_Share_Call_Appearance_m

Unit_n_Short_Name_m_

Display_Password_Warnings

Enable_Protocol

Web_Server_Port

Firmware Release 12.0(2)

Auth_Support_RFC8760

Webex Metrics Enable Parameter

PRT Upload at Crash Enable

Callinfo_subscribe_1

TLS_Client_Min_Version

Transition_Authorization_Error_Retry_Delay

Firmware Release 11.3(7)

Connect_on_Bootup

Disable_Side_USB_Port

Enable_Direct_PLK_Configuration

LDAP_Unified_Search_Enable

PAC_URL

Proxy_Host

Proxy_Mode

Proxy_Password

Proxy_Port

Proxy_Server_Requires_Authentication

Proxy_Username

Use_Auto_Discovery__WPAD_

VPN_Password

VPN_Server

VPN_Tunnel_Group

VPN_User_Name

Webex_Directory_Enable

Webex_Directory_Name

Firmware Release 11.3(6)

Forward_Softkey

Display_Recents_From

Keep_Focus_On_Active_Call

Webex_Onboard_Enable

Webex_Directory_Enable

Webex_Directory_Name

Firmware Release 11.3(5)

Keep_Focus_On_Active_Call

MIC_Cert_Info

MIC_Cert_Provisioning_Status

MIC_Cert_Refresh_Enable

MIC_Cert_Refresh_Rule

Share_Line_Event_Package_Type

Trans_Auth_Rule

Trans_Auth_Type

Voice_Mail_Enable_n_

Firmware Release 11.3(4)

Introduced document for Cisco IP Phone Multiplatform Phones XML parameters running SIP Firmware Release 11.3(4) with Cisco BroadWorks 24.0.

This version contains only Rel 11.3(4) parameters.

Firmware Release 11.3(3)

Introduced document for Cisco IP Phone Multiplatform Phones XML parameters running SIP Firmware Release 11.3(3) with Cisco BroadWorks 24.0.

This version contains only Rel 11.3(3) parameters.

Firmware Release 11.3(2)

Introduced document for Cisco IP Phone Multiplatform Phones XML parameters running SIP Firmware Release 11.3(2) with BroadSoft BroadWorks 23.0.

This version contains only Rel 11.3(2) parameters.

## Accessibility

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Available on LCD UI.

Description

Controls whether to show the Accessibility menu on the phone screen.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## ACD_Logged-off_LED

## Syntax Description

XML Tag Name

```
ACD_Logged-off_LED
```

Example:

```
<ACD_Logged-off_LED ua="na">c=o</ACD_Logged-off_LED>
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

The LED color and cadence state when the ACD PLK selected line has logged off ACD. It will
                              								follow the LED Pattern which is defined by customers. The LED
                              								Pattern Format is c=<COLOR> [; p=<PATTERN>]. c is

Phone Model

All MPP phones except 7832 and 8832

Labels

Att console

## ACD_Logged-on_LED

## Syntax Description

XML Tag Name

```
ACD_Logged-on_LED
```

Example:

```
<ACD_Logged-on_LED ua="na">c=g;p=n</ACD_Logged-on_LED>
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

The LED color and cadence state when the ACD PLK selected line has logged on ACD. It will
                              								follow the LED Pattern which is defined by customers. The LED
                              								Pattern Format is c=<COLOR> [; p=<PATTERN>].  c is mandatory
                              								and p is optional where default behavior is "no blink with solid
                              								color" if it is not specified.

Phone Model

All MPP phones except 7832 and 8832

Labels

Att Console

## ACD_Status_n_

## Syntax Description

XML Tag Name

```
ACD_Status_n_
```

Example:

```
<ACD_Status_1_ ua="na">Sync From Local</ACD_Status_1_>
```

where n is the extension from 1 to 16

Web Parameter

Default Value

Sync From Server

Allowed Values

Option list: Sync From Server|Sync From Local

Units

Options without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Sync From Server: When phone boots up, it will get ACD initial
                              								status from server, which is the legacy behavior.

Sync From Local: When the phone boots up, status is changed to
                              								"Registered" from "Unregistered" or "Registration failed", or
                              								registration destination ip address is changed due to failover,
                              								fallback or DNS response is changed, , it will set ACD status to the
                              								most recent local value.

Phone Model

All MPP phones

Labels

ACD Settings

## Add_Contacts_to_Directory_Personal

## Syntax Description

XML Tag Name

```
Add_Contacts_to_Directory_Personal
```

Example:

```
<Add_Contacts_to_Directory_Personal ua="na">Yes</Add_Contacts_to_Directory_Personal>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether to add contacts to the BroadSoft Personal directory instead of the local personal address book.

Phone Model

All MPP phones

Labels

Directory

## Allowed_APIs

## Syntax Description

XML Tag Name

```
Allowed_APIs
```

Example:

```
<Allowed_APIs ua="na">.*</Allowed_APIs>
```

Web Parameter

Default Value

.*

Allowed Values

String/regular expression

.* : All APIs are allowed

/api/Call/v1/.* : All v1 Call interface calls are
                              								allowed.

/api/Call/v1/(Dial|Hangup) : Only the v1 Call interface calls Dial and Hangup are allowed.

Units

String without units

Limits

String

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

ua=na

Description

A
                              								regular expression that can be used to limit the API calls that are
                              								allowed from the controlling server.

The regular expression provided is matched with the Request-URI path
                              								provided in the API request from the controlling server. If the
                              								entire path is not matched by the given regular expression, the API
                              								call is rejected.

Phone Model

All MPP phones

Labels

API

## Assistant_Call_Filter

## Syntax Description

XML Tag Name

```
Assistant_Call_Filter
```

Example:

```
<Assistant_Call_Filter ua="na">Yes</Assistant_Call_Filter>
```

Web Parameter

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether to show the Call filter menu on the phone screen for the assistant role. Set this field to Yes to show the menu. Otherwise, set it to No .

Phone Model

Supported by 6871 and 8800 Series (not including 8832)

Labels

Phone Menu Visibility

## Audio_Overload_Point_9dB

## Syntax Description

XML Tag Name

```
Audio_Overload_Point_9dB
```

Example:

```
<Audio_Overload_Point_9dB ua="rw">No</Audio_Overload_Point_9dB>
```

Phone Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw. Available on XML config
                              								file only. Not available on LCD UI.

Description

Customer can use 9dB as the acoustic overload point when they select ETSI standard. It is
                              								not found on the Web UI.

Phone Model

Supported by 6841, 6851, 6861, 6871, 8811, 8851, 8861

Labels

Audio

## Auth_Support_RFC8760

## Syntax Description

XML Tag Name

```
Auth_Support_RFC8760
```

Example:

```
<Auth_Support_RFC8760>Yes</Auth_Support_RFC8760>
```

Web Parameter

Default Value

No

Allowed Values

Boolean

Units

Limits

Yes/No

User or Admin

Admin level only.

Description

Enabling Phone Authorization with RFC-8760.

Phone Model

All MPP phones

Labels

SIP Settings

## Auto_Available_After_Sign-In_n_

## Syntax Description

XML Tag Name

```
Auto_Available_After_Sign-In_n_
```

n is the extensions number of the phone.

Example:

```
<Auto_Available_After_Sign-In_1_
ua="na">Yes</Auto_Available_After_Sign-In_1_>
```

Web Parameter

Default Value

No

Allowed Values

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Sets the agent status to Available automatically when the user signs
                              								into the phone as a call center agent.

Phone Model

All MPP phones

Labels

ACD Settings

## Auto_Register_When_Failover

## Syntax Description

XML Tag Name

```
Auto_Register_When_Failover
```

Example:

```
<Auto_Register_When_Failover_1_
ua="na">Yes</Auto_Register_When_Failover_1_>
```

Web Parameter

Default Value

Yes

Allowed Values

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on LCD UI.

Description

Controls the fallback duration.

If set to Yes, the fallback happens only when current
                                 									registration expires, which means only a REGISTER message can
                                 									trigger fallback.

For example, when the value for Register Expires is 3600 seconds
                                 									and Proxy Fallback Intvl is 600 seconds, the fallback is
                                 									triggered 3600 seconds later and not 600 seconds later. When the
                                 									value for Register Expires is 600 seconds and Proxy Fallback
                                 									Intvl is 1000 seconds, the fallback is triggered at 1200
                                 									seconds. After successfully registering back to primary server,
                                 									all the SIP messages go to primary server.

Phone Model

All MPP phones

Labels

SIP

## BLF_Callpark_On_Line_Key_Enable

## Syntax Description

XML Tag Name

```
BLF_Callpark_On_Line_Key_Enable
```

Example:

```
“<BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable>”
```

Web Parameter

N/A

Default Value

No

Allowed Values

Yes/No

Units

N/A

Limits

N/A

User or Admin

Admin level only.

Description

If selected, the BLF Call Park is supported on a specific line key.

Phone Model

Applicable to all models.

Labels

Voice>Att Console>General

## BLF_List_URI

## Syntax Description

XML Tag Name

```
BLF_List_URI
```

Example:

```
<BLF_List_URI ua="na">uri_name@server</BLF_List_URI>
```

Web Parameter

Default Value

N/A

Allowed Values

uri_name@server

Units

N/A

Limits

N/A

User or Admin

Admin

Description

The Uniform Resource Identifier (URI) of the Busy Lamp Field
                                 									(BLF) list that you have set up for a user of the phone, on the
                                 									BroadSoft server.This field is only applicable if the phone is
                                 									registered to a BroadSoft server. The BLF list is the list of
                                 									users whose lines the phone is allowed to monitor.

The BLF List URI must be specified in the format
                                 									<URI_name>@<server>. The BLF List URI specified must be
                                 									the same as the value configured for the List URI: sip parameter
                                 									on the BroadSoft server. Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string
                                 									in this format:

<BLF_List_URI
                                 									ua="na">MonitoredUsersList@sipurash22.com</BLF_List_URI>

On the phone web interface, specify the BLF list that is defined
                                 									on the BroadSoft server.

Phone Model

All MPP phones

Labels

BLF

## BLF_List_Feature_Options

## Syntax Description

XML Tag Name

```
BLF_List_Feature_Options
```

Example:

```
<BLF_List_Feature_Options ua="na">prk</BLF_List_Feature_Options>
```

Phone Web Parameter

Default Value

blf+sd+cp

Allowed Values

blf+sd+cp|prk

Units

String without units

Limits

Options

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on LCD UI

Description

This parameter decides which functions are enabled for those BLF
                                 									List URI auto-assigned linekeys. Enables One-Button Call Park
                                 									and there is no need to enter a combination of key strokes for
                                 									parking and unparking a call.

blf+sd+cp —BLF List URI auto-assigned linekey will
                                       											support "BLF", "Speed Dial" and "Call Pickup"
                                       											functions.

prk—BLF List URI auto-assigned linekey will only support
                                       											"Call Park/Unpark" function.

Phone Model

Supported by 78xx, 88xx, and 68xx except 7811, 7832 and 8832.

Labels

Att console

## Block_Anonymous_Call_Enable_n_

## Syntax Description

XML Tag Name

```
Block_Anonymous_Call_Enable_n_
```

n is the extension number of the phone.

Example:

```
<Block_Anonymous_Call_Enable_n_ ua="na">Yes</Block_Anonymous_Call_Enable_n_>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Enables synchronization of Anonymous Call Rejection between a specific line and a BroadSoft server.

Phone Model

All MPP phones

Labels

XSI Line Service

## Broadsoft_Call_History_Key_List

## Syntax Description

XML Tag Name

```
Broadsoft_Call_History_Key_List
```

Example:

```
<Broadsoft_Call_History_Key_List ua="na">option|1;call|2;editcall|3</Broadsoft_Call_History_Key_List>
```

Web Parameter

Default Value

option|1;call|2;editcall|3;back|4;

option|1;call|2;editcall|3;

Allowed Values

Supported strings: option, call, editcall, filter, and back.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Defines the values for the softkeys Option , Call , Edit call , Filter , and Back for All, Placed, Received, and Missed calls history list.

Phone Model

All MPP phones

Labels

PSK

## Browse_Mode_Enable

## Syntax Description

XML Tag Name

```
Browse_Mode_Enable
```

Example:

```
<Browse_Mode_Enable ua="na">Yes</Browse_Mode_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Directory Display Mode. When enabled, the contact list will be shown
                              								when you enter a directory.

Phone Model

All MPP phones

Labels

Directory

## Call_Appearances_Per_Line

## Syntax Description

XML Tag Name

```
Call_Appearances_Per_Line
```

Example:

```
<Call_Appearances_Per_Line="na">1</Call_Appearances_Per_Line>
```

Web Parameter

Default Value

2

Allowed Values

1to 10

Units

N/A

Limits

Options

User or Admin

Admin level only.

Description

Sets a line to allow single call or multiple calls at a time.

Phone Model

All MPP phones

Labels

Phone

## Callinfo_subscribe_1

## Syntax Description

XML Tag Name

```
CallInfo_Subscribe_1_
```

Example:

```
<CallInfo_Subscribe_1_ ua="na">Yes</CallInfo_Subscribe_1_>
```

Web Parameter

Default Value

No

Allowed Values

Boolean

Units

Limits

Yes/No

User or Admin

Admin level only.

Description

The parameter enables the phone to subscribe the Call-Info header. Only when the Call-Info is subscribed, the phone receives
                              Ad Hoc conference participants list from server. The Call-Info header also includes the call status changes.

Phone Model

All MPP phones

Labels

Ext

## Call_Statistics

## Syntax Description

XML Tag Name

```
Call_Statistics
```

Example:

```
<Call_Statistics ua="na">No</Call_Statistics>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

ua=na

Description

Specifies whether the phone sends end-of-call statistics within SIP
                              								messages when a call terminates or is put on hold.

Phone Model

All MPP phones

Labels

RTP

## Call_Waiting_Enable_n_

## Syntax Description

XML Tag Name

```
Call_Waiting_Enable_n_
```

n is the extension number of the phone.

Example:

```
<Call_Waiting_Enable_n_ ua="na">Yes</Call_Waiting_Enable_n_>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Enables synchronization of Call Waiting between a specific line and a BroadSoft server.

Phone Model

All MPP phones

Labels

XSI Line Service

## Cfwd_All

## Syntax Description

XML Tag Name

```
Cfwd_All
```

Example:

```
<Cfwd_All ua="rw">No</Cfwd_All>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in user level, honored with ua = rw. Available on LCD UI.

Description

Forwards all calls. The setting of this parameter takes precedence
                              								over Cfwd Busy and Cfwd No Answer.

Phone Model

All MPP phones

Labels

UI/CCTRL

## Cfwd_Busy

## Syntax Description

XML Tag Name

```
Cfwd_Busy
```

Example:

```
<Cfwd_Busy ua="rw">No</Cfwd_Busy>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in user level, honored with ua = rw. Available on LCD UI.

Description

Forwards calls only if the line is busy.

Phone Model

All MPP phones

Labels

UI/CCTRL

## Cfwd_No_Answer

## Syntax Description

XML Tag Name

```
Cfwd_No_Answer
```

Example:

```
<Cfwd_No_Answer ua="rw">No</Cfwd_No_Answer>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in user level, honored with ua = rw. Available on LCD UI.

Description

Forwards the incoming call only if the call isn’t answered for a waiting interval.

Phone Model

All MPP phones

Labels

UI/CCTRL

## Cfwd_Setting

## Syntax Description

XML Tag Name

```
Cfwd_Setting
```

Example:

```
<Cfwd_Setting ua="rw">Yes</Cfwd_Setting>
```

Web Parameter

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in user level, honored with ua = rw. Not available on LCD
                              								UI.

Description

Provides a user the ability to modify the call forward settings from
                              								the phone web page.

This parameter isnot available in Release 11.3(2). It is available in Release 11.3(1) and
                              								earlier.

Phone Model

All MPP phones

Labels

UI/CCTRL

## Call_Forward_On_LED

## Syntax Description

XML Tag Name

```
Call_Forward_On_LED
```

Example:

```
<Call_Forward_On_LED ua="na">c=r;p=n</Call_Forward_On_LED>
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a Color. This is equivalent to the system default of Slow
                              								Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

The LED color and cadence state when the call forward PLK indicates that the selected
                              								line's call forward state is On . It will follow the LED
                              								Pattern which is defined by customers. The LED Pattern Format is
                              								c=<COLOR> [; p=<PATTERN>]. c is mandatory and p is optional
                              								where default behavior is "no blink with solid color" if it is not
                              								specified

Phone Model

All MPP phones except 7832 and 8832

Labels

Att Console

## Call_Forward_Off_LED

## Syntax Description

XML Tag Name

```
Call_Forward_Off_LED
```

Example:

```
<Call_Forward_Off_LED ua="na">c=o</Call_Forward_Off_LED>
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

The LED color and cadence state when the call forward PLK indicates
                              								that the selected line's call forward state is Off . It will
                              								follow the LED Pattern which is defined by customers. The LED
                              								Pattern Format is c=<COLOR> [; p=<PATTERN>]. c is mandatory
                              								and p is optional where default behavior is "no blink with solid
                              								color" if it is not specified

Phone Model

All MPP phones except 7832 and 8832

Labels

Att Console

## CDC_Challenge_Password_1_

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

N/A

Allowed Values

String

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Specifies the challenge password for Certificate Authority (CA) authorization against the phone during a certificate enrollment
                              via SCEP.

Phone Model

All MPP phones

Labels

Certificate

## CDC_Root_CA_Fingerprint_1_

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

N/A

Allowed Values

String

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Specifies the SHA256 or SHA1 fingerprint of the Root CA for validation during the SCEP process. When the SCEP parameters are
                              configured correctly, the phone sends requests to the SCEP server, and the CA certificate is validated by device using the
                              defined fingerprint.

Phone Model

All MPP phones

Labels

Certificate

## CDC_Server_1_

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

N/A

Allowed Values

String

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Specifies an SCEP server address when automatically installing the Custom Device Certificate (CDC). When the SCEP parameters
                              are configured correctly, the phone sends requests to the SCEP server, and the CA certificate is validated by device using
                              the defined fingerprint.

Phone Model

All MPP phones

Labels

Certificate

## Certificate_Select

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Manufacturing installed

Allowed Values

Option list: Manufacturing installed|Custom installed

Units

N/A

Limits

N/A

User or Admin

Exposed in user level, honored with ua=rw. Available on LCD UI.

Description

Select a certificate (MIC or custom) for the 802.1X authentication.

Phone Model

All MPP phones

Labels

System

## Connect_on_Bootup

## Syntax Description

XML Tag Name

```
<Connect_on_Bootup>
```

Example:

```
<Connect_on_Bootup ua="rw">No</Connect_on_Bootup>
```

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Controls whether to connect to the specified VPN server automatically after the phone reboots.

Phone Model

All MPP phones except 6821, 7832, and 8832

Labels

VPN

## Control_Server_URL

## Syntax Description

XML Tag Name

```
Control_Server_URL
```

Example:

```
<Control_Server_URL ua="na"/>
```

In the phone web page enter the URL of a WebSocket server.

```
<Control_Server_URL>wss://my-server.com
/ws-server-path</Control_Server_URL>
```

Web Parameter

Default Value

Empty

Allowed Values

URL

Units

URL

Limits

URL

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

The URL of a WebSocket server to which the phone attempts to stay
                              								connected.

URL should be in one of the following formats:

For a nonsecure HTTP connection: ws://your-server-name/path

For a secure HTTPS connection: wss://your-server-name/some-path

We recommend a secure connection.

Phone Model

All MPP phones

Labels

Remote SDK

## Customizable_PLK_Options

## Syntax Description

XML Tag Name

```
Customizable_PLK_Options
```

Example:

```
<Customizable_PLK_Options ua="na">mwi;sd;blf;shortcut;dnd;</Customizable_PLK_Options>
```

Example: sd;blf;cp;dnd;acd;callinfo

Example: proxycall;callpush;callretrieve;divert;bridgein

Web Parameter

Default Value

sd

Allowed Values

dnd|acd|callinfo|calllist|cfwd|lcr|proxycall|callpush|callretrieve|divert|bridgein|shortcut

Units

String without units

Limits

String Length range is 0 to 511

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enables users to configure features on the line keys.

Phone Model

All MPP phones

Labels

Att Console

## Device_Administration

## Syntax Description

XML Tag Name

```
Device_Administration
```

Example:

```
<Device_Administration ua="na">Yes</Device_Administration>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available as Device administration on the LCD UI.

Description

Controls whether to show the Device
                                 									administration menu on the phone screen. Set this
                              								field to Yes to show the menu. Otherwise, set
                              								it to No .

Phone Model

All MPP phones

Labels

Phone Menu Visibility

## Device_Config_Version

## Syntax Description

XML Tag Name

```
Device_Config_Version
```

Example:

```
<Device_Config_Version ua="na">2021-01-05-v1</Device_Config_Version>
```

Web Parameter

N/A

Default Value

Empty

Allowed Values

Any string

Units

String without units

Limits

0–64 characters

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI and the phone web page.

Description

Customizes the product configuration version that shows as the menu item Configuration version on the phone screen Product information .

If the tag doesn't exist in the cfg.xml file or the parameter value is empty, the menu item doesn't display on the phone screen.

Phone Model

All MPP phones

Labels

Phone Menu

## Disable_DF

## Syntax Description

XML Tag Name

```
Disable_DF
```

Example:

```
<Disable_DF ua="na">Yes</Disable_DF>
```

Web Parameter

Disable DF

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether an IP packet can be fragmented.

When the parameter is set to Yes , the Don't Fragment (DF) bit is disabled. In this case, the network can fragment an IP packet. This is the default behaviour.

When the parameter is set to No , the Don't Fragment (DF) bit is enabled. In this case, the network can't fragment an IP packet. This setting doesn't allow
                              fragmentation in cases where the receiving host doesn't have sufficient resources to reassemble internet fragments.

Phone Model

All models

Labels

Network Settings

## Display_Off_Idle_Timeout__mins_

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

5

Allowed Values

1 to 60

Units

Minutes

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Set the timeout period in minutes for the phone to automatically turn off the screen after being awakened from the Display
                              Off Mode.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## Display_Password_Warnings

## Syntax Description

XML Tag Name

```
Display_Password_Warnings
```

Example:

```
<Display_Password_Warnings ua="na">Yes</Display_Password_Warnings>
```

Web Parameter

Display Password Warnings

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Options

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Specifies whether to show password alerts on the phone and the web page.

Phone Model

Supported by all phones

Labels

System

## Disable_Side_USB_Port

## Syntax Description

XML Tag Name

```
Disable_Side_USB_Port
```

Example:

```
<Disable_Side_USB_Port ua="na">No</Disable_Side_USB_Port>
```

Web Parameter

Disable Side USB Port

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether to disable or enable the side USB port on the phone (if the phone has this port).

When the side USB port is disabled, it doesn't work on the phone. And it doesn't charge the connected device.

Phone Model

Supported by 8851, 8861, and 8865

Labels

Power Settings

## Display_Recents_From

## Syntax Description

XML Tag Name

```
Display_Recents_From
```

Example:

```
<Display_Recents_From ua="na">Phone</Display_Recents_From>
```

Web Parameter

Display Recents From

Default Value

Phone

Allowed Values

Option list: Phone|XSI Server|Webex

Units

String without units

Limits

Options

User or Admin

Exposed in admin level, which is honored with ua = na. Not available on LCD UI.

Description

Sets the source of recent call histories that the phone retrieves from.

This parameter is associated with the parameter CallLog Enable .

When CallLog Enable is set to Yes , the phone can display the Display recents from field in the Recents screen. The user can select the source of the call histories through the Display recents from field.

The Webex option from the Display recents from field displays only when the phone connects to the Webex.

Phone Model

All MPP phones supports options XSI Server and Phone. Option Webex is only supported by onlyrted 8800 Series and 8832

Labels

Calls

## Display_XMPP_User_ID_With_Top_Priority

## Syntax Description

XML Tag Name

```
Display_XMPP_User_ID_With_Top_Priority
```

Example:

```
<Display_XMPP_User_ID_With_Top_Priority ua="na">Yes</Display_XMPP_User_ID_With_Top_Priority>
```

Web Parameter

Display XMPP User ID With Top Priority

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Displays the XMPP user ID with the highest priority at the top left of the phone screen.

If enabled, the XMPP user ID overrides other display names, for example, Station Name.

Phone Model

Supported by 8800 Series

Labels

Directory

## Divert_Off_LED

## Syntax Description

XML Tag Name

```
Divert_Off_LED
```

Example:

```
<Divert_Off_LED ua="na">c=r</Divert_Off_LED>
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

The LED color and cadence when the Divert PLK indicates that the selected line's divert
                              								state is Off . It will follow the LED Pattern which is defined
                              								by customers. The LED Pattern Format is c=<COLOR> [;
                              								p=<PATTERN>]. c is mandatory and p is optional where default
                              								behavior is "no blink with solid color" if it is not specified.

Phone Model

All MPP phones except 7832 and 8832

Labels

Att Console

## DND_Off_LED

## Syntax Description

XML Tag Name

```
DND_Off_LED
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

Turns off the DND LED pattern on the phone screen.

Phone Model

All MPP phones except 7832 and 8832

Labels

Calls

## DND_On_LED

## Syntax Description

XML Tag Name

```
DND_On_LED
```

Example:

```
<DND_On_LED ua="na">c=r</DND_On_LED>
```

Web Parameter

Default Value

Empty

Allowed Values

COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it.

PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color

Examples:

LED = Solid Red

User Input = c=r; p=n

c=r

LED = Blinking Amber

User Input = c=a; p=b

LED = OFF

User Input = c=o

Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides.

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI.

Description

The LED color and cadence when the DND PLK indicates that the selected line's DND is On . It will follow the LED Pattern which is defined by
                              								customers. The LED Pattern Format is c=<COLOR> [;
                              								p=<PATTERN>]. c is mandatory and p is optional where default
                              								behavior is "no blink with solid color" if it is not specified.

Phone Model

All 68xx, 78xx, 88xx, phones except 7832 and 8832

Labels

Att Console

## Enable_802.1X_Authentication

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

N/A

Limits

N/A

User or Admin

Exposed in user level, honored with ua=rw. Available on LCD UI.

Description

Enables 802.1X authentication on the phone.

When 802.1X authentication is enabled, the phone uses 802.1X authentication to request network access.When 802.1X authentication
                              is turned off, the phone uses CDP to acquire VLAN and network access.

Phone Model

All MPP phones

Labels

System

## Enable_Direct_PLK_Configuration

## Syntax Description

XML Tag Name

```
Enable_Direct_PLK_Configuration
```

Example:

```
<Enable_Direct_PLK_Configuration ua="na">Yes</Enable_Direct_PLK_Configuration>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether the extension of a line key must be disabled to apply the Programmable Line Key (PLK) configuration.

Before the 11.3(7) release, you must disable the extension of a line key to apply the PLK configuration.

If the parameter is set to Yes , you can skip disabling the extension of a line key, and you can directly configure the PLK on a line key.

If the parameter is set to No , you still need to disable the extension of a line key to apply the PLK configuration.

To make this feature take effect, ensure that the <Proxy_ n _> and <User_ID_ n _> are empty, where n is the extension number of the line key.

The Direct PLK Configuration feature on a certain line key doesn't work in the following situations:

<Make_Call_Without_Reg_ n _> is Yes , where n is the extension number of the line key.

<Bluetooth_Mode> is Handsfree or Both , and <Line> is configured with a number. For example, <Line> is 2 . In this case, the feature doesn't work on the line key with the extension number 2.

The Direct PLK

Phone Model

All MPP phones except 7811, 7832, and 8832

Labels

Line Key

## Enable_Protocol

## Syntax Description

XML Tag Name

```
Enable_Protocol
```

Example:

```
<Enable_Protocol ua="na">Https</Enable_Protocol>
```

Web Parameter

Enable Protocol

Default Value

Https

Allowed Values

Option list: Https|Http

Units

Options

Limits

Options

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Enables https by default to access the phone administration web page.

Phone Model

Supported by all phones

Labels

System

## Executive_Assistant_Role

## Syntax Description

XML Tag Name

```
Executive_Assistant_Role
```

Example:

```
<Executive_Assistant_Role ua="na">Default</Executive_Assistant_Role>
```

Web Parameter

Default Value

Default

Allowed Values

Option list: Default|Executive|Assistant

Units

Options without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Preassigns the executive-assistant role to a phone extension.

This preassignment doesn't directly determine the executive-assistant role of the phone. Both the preassignments on the extensions
                              and the role settings by the BroadWorks server determine the executive-assistant role of the phone.

Phone Model

Supported by 6871 and 8800 Series (not including 8832)

Labels

Executive Assistant

## Extended_Function_n_

## Syntax Description

XML Tag Name

```
Extended_Function_n_
```

n is the extension number of the phone.

Call park to a line key

For a private line, enter

```
nc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1
```

For a shared line, enter

```
fnc=prk;sub=$USER@$PROXY;nme=Call-Park1;orbit=<DN of primary line>
```

You can configure this feature on the line key on which Extension is disabled .

where:

fnc= prk means function=call park

sub= 999999 is the phone to which the call parks. Replace 999999
                                 									with a numbers.

nme= XXXX is the name displayed on the phone for the call park
                                 									line key. Replace XXXX with a name.

Example:

```
<Extended_Function_2_
ua="na">fnc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1</Extended_Function_2_>
```

A line key as a phone menu shortcut

Example:

```
<Extended_Function_1_ ua="na">fnc=shortcut;url=userpref;nme=User
Preferences</Extended_Function_1_>
```

Web Parameter

Default Value

Empty

Allowed Values

String, the well-formated one is "fnc=type(;name=value)*", where * means zero or more
                                 									repeats

Units

String without units

Limits

String Length: 0 to 511

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available
                                 									on LCD UI.

Description

Adds extended functions to a line key.

Phone Model

All MPP phones

Labels

Line key

## Extension_n_

## Syntax Description

XML Tag Name

```
Extension_n_
```

n is the extension number of the phone.

Example:

```
<Extension_1_ ua="na">Disabled</Extension_1_>
```

Web Parameter

Default Value

n

where n is the extension (1-10) assigned to a line key.

Allowed Values

Drop-down list: n|Disabled

where n is the extension (1to10) assigned to a line key.

Units

Options with integer and string.

Limits

Options

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								the LCD UI.

Description

Specifies the n extension to be assigned to Line Key n.

Phone Model

All MPP phones

Labels

Line Key

## EXT_SIP_Port

## Syntax Description

XML Tag Name

```
EXT_SIP_Port
```

Example:

```
<EXT_SIP_Port_1_ua="na">5060</EXT_SIP_Port_1_>
```

Web Parameter

Default Value

5060

Allowed Values

Units

Integer

Limits

0 to 65535

User or Admin

Admin

Description

The external SIP port number.

Phone Model

All MPP phones

Labels

SIP

## Factory_Reset_Menu

## Syntax Description

XML Tag Name

```
Factory_Reset_Menu
```

Example:

```
<Factory_Reset_Menu ua="na">Yes</Factory_Reset_Menu>
```

Web Parameter

Default Value

Yes

Allowed Values

Units

Boolean

Limits

N/A

User or Admin

Admin

Description

Specifies if the user requires authentication to access Factory
                                 									reset menu on the phone.

This parameter can be customized to Yes or No only when the Require
                                    										Authentication for LCD Menu Access parameter is
                                 									set to Customized .

Phone Model

All MPP phones

Labels

User Authentication Control for Phone menus

## Feature_Activation_Code_Sync

## Syntax Description

XML Tag Name

```
Feature_Activation_Code_Sync
```

Example:

```
<Feature_Activation_Code_Sync_n_ ua="na">Yes</Feature_Activation_Code_Sync_n_>
```

where n is the extension number.

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enable or disable sending FAC code to server when dial vertical
                              								activation code.

Phone Model

All MPP phones

Labels

Call Feature setting

## FIPS_MODE

## Syntax Description

XML Tag Name

```
FIPS_Mode
```

Example:

```
<FIPS_Mode>Disabled</FIPS_Mode>
```

Web Parameter

Default Value

Disabled

Allowed Values

Disabled|Enabled

Units

Options without units

Limits

Options

User or Admin

Admin level only. Not available on LCD UI.

Description

Enables CiscoSSL FIPS mode when Enabled is selected.

Phone Model

All MPP phones

Labels

System

## Firewall

## Syntax Description

XML Tag Name

```
Firewall
```

Example:

```
<Firewall ua="na">Enabled</Firewall>
```

Web Parameter

Default Value

Enabled

Allowed Values

Option list: Disabled|Enabled

Units

Options without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

ua=na

Description

Improves phone security by by hardening the operating system. Tracks
                              								the ports for incoming and outgoing data. It detects incoming
                              								traffic from unexpected sources and blocks the access. Your firewall
                              								allows all outgoing traffic.

Phone Model

All MPP phones

Labels

Security

## Firewall_Config

## Syntax Description

XML Tag Name

```
Firewall_Config
```

Example:

```
<Firewall_Config ua="na">NO_ICMP_PING</Firewall_Config>
```

Web Parameter

Default Value

Empty

Allowed Values

String

NO_ICMP_PING, NO_ICMP_UNREACHABLE, NO_CISCO_TFTP

The following keywords and options apply when the phone runs custom
                              								apps that handle incoming requests.

UDP:<xxx>, UDP:<xxx:yyy>, TCP:<xxx>, TCP:<xxx:yyy>

Units

String without units

Limits

String

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

ua=na

Description

Configures additional options in the Firewall Options field.
                              								Type the keyword for each option in the field, and separate the
                              								keywords by commas (,). Some keywords have values. Separate the
                              								values by colons (:).

Phone Model

All MPP phones

Labels

Security

## Font_Size

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Regular

Allowed Values

Option list: Regular|Large

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Available on LCD UI.

Description

Controls the size of the fonts that are displayed on the phone screen.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## Forced_NAT64

## Syntax Description

XML Tag Name

```
<Forced_NAT64>
```

Example:

```
<Forced_NAT64>Yes</Forced_NAT64>
```

Web Parameter

Default Value

No

Allowed Values

Yes | No

Units

N/A

Limits

Yes | No

User or Admin

Admin level only

Description

Sets the web parameter for Forced NAT64. Takes effect after a warm reboot.

Phone Model

All MPP phones

Labels

NAT64

## Forward_Softkey

## Syntax Description

XML Tag Name

```
Forward_Softkey
```

Example:

```
<Forward_Softkey ua="na">All Cfwds</Forward_Softkey>
```

Web Parameter

Forward Softkey

Default Value

All Cfwds

Allowed Values

Option list: All Cfwds|Only the Cfwd All

Units

String without units

Limits

Options

User or Admin

Exposed in admin level, which is honored with ua = na. Not available on LCD UI.

Description

Allows the user to set up all call forward services or only the Call Forward All service by a specific softkey. Options are:

All Cfwds : The user can set up all call forward services, including Call Forward All, Call Forward Busy, and Call Forward No Answer
                                    by a specific softkey. In this setting, the softkey is Forward .

After the user sets up any of the call forward services, the softkey changes to Clf fwd . And the user can disable all call forward services by pressing it.

Only the Cfwd All : The user can only set up the Call Forward All service by a specific softkey. In this setting, the softkey is Forward all .

After the user sets up the Call Forward All service, the softkey changes to Clf fwd all . And the user can disable the Call Forward All service by pressing it.

Phone Model

All MPP phones

Labels

UI/CCTRL

## Group_n_Paging_Script

## Syntax Description

XML Tag Name

```
Group_1_Paging_Script
```

n is the group ID (1-10)

Example:

```
<Group_1_Paging_Script ua="na">pggrp=224.168.168.168:34560;name=Group_1;
num=800;listen=yes;pri=1;codec=g722</Group_1_Paging_Script>
```

Web Parameter

Default Value

pggrp=224.168.168.168:34560;name=All;num=800;listen=yes;

Allowed Values

String

Units

String

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

A string to configure the phone to listen for and initiate multicast
                              								paging. You can add a phone to up to 10 paging groups.

Phone Model

All MPP phones

Labels

Multiple paging

## ice_stun_enable

## Syntax Description

XML Tag Name

```
ice_stun_enable
```

Example:

```
<ice_stun_enable>Yes</ice_stun_enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list Yes|No

Units

Boolean without units

Limits

Boolean/Option

User or Admin

Exposed in admin level through xml configuration file (Webex Calling
                              								Server). Honored with ua = rw/ro/na. Not available on the LCD
                              								UI.

Description

Optimizes media path for calls.

Phone Model

All MPP phones

Labels

NAT

## Idle_Key_List

## Syntax Description

XML Tag Name

```
Idle_Key_List
```

Example:

```
<Idle_Key_List
ua="rw">psk2;em_login;acd_login;acd_logout;astate;redial;cfwd;dnd;lcr;</Idle_Key_List>
```

Web Parameter

Default Value

N/A

Allowed Values

Units

N/A

Limits

N/A

User or Admin

Admin

Description

Programmable softkey fields. Enter a string in these fields to
                                 									configure softkeys that display on the phone screen. You can
                                 									create softkeys for speed dials to numbers or extensions,
                                 									vertical service activation codes (* codes), or XML. Configure
                                 									the PSKs in this format:

Speed Dial:

```
fnc=sd;ext=extension_number@$PROXY;vid=n;nme=display_name
```

Vertical Service Activation Code:

```
fnc=sd;ext=star_code@$PROXY;vid=n;nme=display_name
```

XML Service:

```
fnc=xml;url=http://server_IP/services.xml;vid=n;nme=display_name
```

Menu shortcut:

```
fnc=shortcut;url=userpref;nme=User preferences
```

When you add a programmable softkey to a softkey list, such as
                                 									Idle Key List, Missed Call Key List, and so on, the programmable
                                 									softkey displays on the phone screen.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string
                                 									in this format:

```
<PSK_1 ua="na">fnc=xml;url=http://server_IP/services.xml;vid=n;
```

```
nme=display_name</PSK_1 ua="na">
```

In the phone web interface, set the PSKs in the valid format or
                                 									scripts.

Phone Model

All MPP phones

Labels

PSK

## Keep_Focus_On_Active_Call

## Syntax Description

XML Tag Name

```
Keep_Focus_On_Active_Call
```

Example:

```
<Keep_Focus_On_Active_Call ua="na">Yes</Keep_Focus_On_Active_Call>
```

Web Parameter

Keep Focus On Active Call

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether to keep the focus on the active call on the phone screen when the phone receives an incoming call.

Yes : When a user is on an active call and receives one or more incoming calls, the focus still remains on the active call. However, if the user places the active call on hold, the focus automatically moves from the active call to the incoming call.
                                       If there are multiple incoming calls, the focus always moves to the first one.

No : When a user is on an active call and receives an incoming call, the focus automatically moves from the active call to the
                                    incoming call.

Phone Model

All MPP phones

Labels

Calls

## Key_Again_Reset_Time

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

1200

Allowed Values

100 to 2000

Units

Milliseconds

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Not available on LCD UI.

Description

Sets the reset time required for performing a key double or triple press again.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## Key_Double_Press_Time

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

600

Allowed Values

100 to 2000

Units

Milliseconds

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Not available on LCD UI.

Description

Sets the maximum delay time for a key double press to perform a named function on the phone.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## Key_Triple_Press_Time

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

1000

Allowed Values

100 to 2000

Units

Milliseconds

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Not available on LCD UI.

Description

Sets the maximum delay time for a key triple press to enable or disable the voice feedback feature on the phone.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## LED_Indicator_In_Display_Off_Mode

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Enabled

Allowed Values

Option list: Enabled|Disabled

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Determines whether to turn off the backlight of the Select button in the Navigation cluster when the phone enters the Display Off Mode.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## LDAP_StartTLS_Enable

## Syntax Description

XML Tag Name

```
LDAP_StartTLS_Enable
```

Example:

```
<LDAP_StartTLS_Enable ua="na">Yes</LDAP_StartTLS_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

StartTLS Enable = Yes : If Ldap_server is ldap://server:port , then phone will start to
                                    										send Start_TLS request. If Ldap_server is ldaps://server:port , then phone will keep LDAPs
                                    										and will ignore this parameter.

StartTLS Enable = No : Phone will keep the existing
                                    										behavior.

Phone Model

All MPP phones

Labels

LDAP

## LDAP_Prompt_For_Empty_Credentials

## Syntax Description

XML Tag Name

```
LDAP_Prompt_For_Empty_Credentials
```

Example:

```
<LDAP_Prompt_For_Empty_Credentials ua="na">Yes</LDAP_Prompt_For_Empty_Credentials>
```

where n is the extension number.

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Hidden. Not available on LCD UI.

ua=na

Description

Enable or disable the LDAP sign-in prompt when there’s no user
                              								credential on the phone. This function is used only for the simple
                              								authentication method that involves the anonymous simple bind
                              								operation.

Phone Model

All MPP phones

Labels

LDAP

## LDAP_Unified_Search_Enable

## Syntax Description

XML Tag Name

LDAP_Unified_Search_Enable

Example:

<LDAP_Unified_Search_Enable>Yes</LDAP_Unified_Search_Enable>

Web Parameter

Unified Search Enable

Default Value

No

Allowed Values

Yes/No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed only in the phone web page for admin.

Description

When the parameter is set to Yes , it enables the unified search for the LDAP directory.

Phone Model

All MPP phones

Labels

Phone

## Max_Display_Records

## Syntax Description

XML Tag Name

```
Max_Display_Records
```

Example:

```
<Max_Display_Records ua="na">50</Max_Display_Records>
```

Web Parameter

Default Value

50

Allowed Values

50 to 999

Units

Record number

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Maximum display records for a directory.

Phone Model

All MPP phones except 7811 and 7832

Labels

Directory

## MediaSec_Request_n_

## Syntax Description

XML Tag Name

```
MediaSec_Request_n_
```

where n is the extension number (1 to 16) of the phone

Example:

```
<MediaSec_Request_1_ ua="na">Yes</MediaSec_Request_1_>
```

Phone Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI

Description

Specifies whether the phone initiates media plane security
                              								negotiation with the server.

Yes—The phone initiates media plane security negotiations.

No—The phone doesn't initiate negotiations but can handle
                                    										negotiation requests from the server.

Phone Model

All models

Labels

SIP

## MediaSec_Over_TLS_Only_n_

## Syntax Description

XML Tag Name

```
MediaSec_Over_TLS_Only_n_
```

n is the extension number of the phone.

Example:

```
<MediaSec_Over_TLS_Only_1_ ua="na">No</MediaSec_Over_TLS_Only_1_>
```

Web Parameter

Default Value

No

Allowed Values

Options: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Specifies the signaling transport protocol over which media plane
                              								security negotiation is applied.

Before setting this field to Yes , ensure that the signaling
                              								transport protocol is TLS.

Phone Model

All MPP phones

Labels

Security

## MIC_Cert_Info

## Syntax Description

XML Tag Name

N/A

Web Parameter

MIC Cert Info

Default Value

N/A

Allowed Values

N/A

Units

N/A

Limits

N/A

User or Admin

Exposed only in the phone web page for both user and admin. Not available on LCD UI.

Description

Shows the overall status of the MIC certificate renewal procedure.

For example, Renewed or Not Renewed .

Phone Model

All MPP phones

Labels

Secure

## MIC_Cert_Provisioning_Status

## Syntax Description

XML Tag Name

N/A

Web Parameter

MIC Cert Provisioning Status

Default Value

N/A

Allowed Values

N/A

Units

N/A

Limits

N/A

User or Admin

Exposed only in the phone web page for both user and admin. Not available on LCD UI.

Description

Shows the status of the Manufacture Installed Certificate (MIC) certificate to see whether the SUDI server has renewed the
                              certificate successfully. This parameter contains the following information:

Date and time of the last renewal

Request URL to the SUDI service

Result message (success or failure)

The information shows in this format:

<time><url><result message>

Phone Model

All MPP phones

Labels

Secure

## MIC_Cert_Refresh_Enable

## Syntax Description

XML Tag Name

MIC_Cert_Refresh_Enable

Example:

<MIC_Cert_Refresh_Enable ua="na">Yes</MIC_Cert_Refresh_Enable>

Web Parameter

MIC Cert Refresh Enable

Default Value

No

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether to enable the MIC certificate renewal procedure.

Phone Model

All MPP phones

Labels

Secure

## MIC_Cert_Refresh_Rule

## Syntax Description

XML Tag Name

MIC_Cert_Refresh_Rule

Example:

<MIC_Cert_Refresh_Rule ua="na">http://hostname.cisco.com/</MIC_Cert_Refresh_Rule>

Web Parameter

MIC Cert Refresh Rule

Default Value

http://sudirenewal.cisco.com/

Allowed Values

URL

Units

URL

Limits

URL

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

HTTP URL for requesting the renewed MIC certificate from the SUDI server.

Currently, only the default URL can be used for the MIC certificate renewal.

Phone Model

All MPP phones

Labels

Secure

## Office_Hours_Enabled

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

False

Allowed Values

Option list: True|False

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Enables Office Hours. When enabled, the phone automatically enters Display Off Mode and turns off the screen to save power
                              outside of the designated working hours.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## PAC_URL

## Syntax Description

XML Tag Name

```
PAC_URL
```

Example:

```
<PAC_URL ua="rw">http://proxy.department.branch.example.com/pac</PAC_URL>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

Maximum of 511 characters

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

The URL that instructs the phone to retrieve a Proxy Auto-Configuration (PAC) file.

TFTP, HTTP, and HTTPS are supported.

The parameter configuration takes effect when the Proxy Mode is Auto and Use Auto Discovery (WPAD) is set to No . For details, see Proxy_Mode and Use_Auto_Discovery__WPAD_ .

Phone Model

All MPP phones

Labels

Proxy

## Peripheral_Inventory_Enable

## Syntax Description

XML Tag Name

```
Peripheral_Inventory_Enable
```

Example:

```
<Peripheral_Inventory_Enable ua="na">Yes</Peripheral_Inventory_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Enables the phone to report the connected or disconnected peripheral information to the server.

When the parameter is set to Yes , the peripheral inventory headers are included in the SIP Register message. When set to No , the headers are not included in the SIP message.

When one peripheral is connected or disconnected to the phone, next scheduled Register provides the peripheral information
                                 in the Peripheral-Data header. All subsequent Registers do not carry peripheral information. The Peripheral-Data header is
                                 included for each peripheral, for example, if there are two headsets present, the header appears twice.

Phone Model

Supported by 6851, 6871, and 8800 Series (not including 8832)

Labels

SIP

## Personal_Directory_Enable

## Syntax Description

XML Tag Name

```
Personal_Directory_Enable
```

Example:

```
<Personal_Directory_Enable
ua="na">Yes</Personal_Directory_Enable>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Enables the personal address book directory for the phone
                                 									user.

When you disable the directory,

users can't search contacts from their personal address
                                       											book

users can't add a contact in their personal address
                                       											book

Phone Model

All MPP phones

Labels

Directory Services

## Precondition_Support_n_

XML Tag Name

```
Precondition_Support_n_
```

n is the extension number of the phone.

Example:

```
<Precondition_Support_1_ua="na">Enabled</Precondition_Support_1_>
```

Web Parameter

Default Value

Disabled

Allowed Values

Option list: Disabled|Enabled

Units

Options without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Determines whether the phone includes the precondition tag (defined in RFC 3312) in the Supported header field.

Disabled :  The phone doesn't include the precondition tag in the Supported header filed. And the phone doesn't return the 183 response
                                    when it receives the INVITE request that contains the QoS precondition in the SDP description.

Enabled : The phone includes the precondition tag in the Supported header field.

Phone Model

All MPP phones

Labels

SIP Settings

## Programmable_Softkey_Enable

## Syntax Description

XML Tag Name

```
Programmable_Softkey_Enable
```

Example:

```
<Programmable_Softkey_Enable ua="rw">Yes</Programmable_Softkey_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

Description

Enables or disables the programmable softkeys. Set this field to Yes to enable the
                                 									programmable softkeys.

Phone Model

All MPP phones

Labels

PSK

## Profile_Rule_Menu

## Syntax Description

XML Tag Name

```
Profile_Rule_Menu
```

Example:

```
<Profile_Rule_Menu ua="na">Yes</Profile_Rule_Menu>
```

Web Parameter

Default Value

Yes

Allowed Values

Units

Boolean

Limits

N/A

User or Admin

Admin

Description

Specifies if the user requires authentication to access Profile
                                 									rule menu on the phone.

You can customize this parameter to Yes or No only when you set
                                 									the Require Authentication for LCD Menu
                                    										Access parameter to Customized .

Phone Model

All MPP phones

Labels

User authentication to phone menus

## Proxy_Fallback_Intvl

## Syntax Description

XML Tag Name

```
Proxy_Fallback_Intvl
```

Example:

```
<Proxy_Fallback_Intvl_n_ ua="na">60</Proxy_Fallback_Intvl_n_>
```

n is the extension number.

Web Parameter

Default Value

N/A

Allowed Values

Units

Seconds

Limits

N/A

User or Admin

Admin

Description

The proxy failback requires a value other than zero specified in
                                 									the Proxy Fallback Intvl field on the Ext (n) tab in the phone
                                 									web interface. If you set this field to 0, the SIP proxy
                                 									failback feature is disabled.

The time when the phone triggers a failback depends on the phone
                                 									configuration and the SIP transport protocols in use.

To enable the phone to perform failback between different SIP
                                 									transport protocols, set SIP Transport to Auto on the Ext (n)
                                 									tab in the phone web interface. You can also configure this
                                 									extension-specific parameter in the configuration file with the
                                 									following XML string:

<SIP_Transport_n_ ua="na">Auto</SIP_Transport_n_>

where n is the extension number.

Phone Model

All MPP phones

Labels

## Proxy_Host

## Syntax Description

XML Tag Name

```
Proxy_Host
```

Example:

```
<Proxy_Host ua="rw">proxy.example.com</Proxy_Host>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

Maximum of 255 characters

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Specifies an IP address or hostname of the proxy host server that the phone uses. For example:

proxy.example.com

The scheme ( http:// or https:// ) is not required.

The parameter configuration is required if the Proxy Mode is set to Manual . For details, see Proxy_Mode .

Phone Model

All MPP phones

Labels

Proxy

## Proxy_Mode

## Syntax Description

XML Tag Name

```
Proxy_Mode
```

Example:

```
<Proxy_Mode ua="rw">Off</Proxy_Mode>
```

Web Parameter

Default Value

Off

Allowed Values

Auto|Manual|Off

Units

Options without units

Limits

Option

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Determines which proxy mode that the phone uses or to disable the HTTP proxy feature on the phone. Options are:

Auto : In this mode, the phone retrieves a Proxy Auto-Configuration (PAC) file that defines how to automatically choose an appropriate
                                       proxy server. This mode contains the following methods:

Web Proxy Auto-Discovery (WPAD): Uses DHCP server or DNS Service Discovery, or both to automatically retrieve a PAC file.

Proxy Auto-Configuration (PAC) URL: Specifies a PAC URL that can locate to a PAC file.

Manual : In this mode, the user needs to manually specify a proxy server (a hostname or IP address) and a proxy port. If the proxy
                                       server requires authentication, then the user needs to further enter the username and password to access the server.

Off : The HTTP proxy feature is disabled on the phone.

Phone Model

All MPP phones

Labels

Proxy

## Proxy_Password

## Syntax Description

XML Tag Name

```
Proxy_Password
```

Example:

```
<Proxy_Password ua="rw">Example</Proxy_Password>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

N/A

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Provides the password of the specified username that the proxy server requires.

The parameter configuration is required when Proxy Mode is set to Manual and Proxy Server Requires Authentication is set to Yes . For details, see Proxy_Mode and Proxy_Server_Requires_Authentication .

Phone Model

All MPP phones

Labels

Proxy

## Proxy_Port

## Syntax Description

XML Tag Name

```
Proxy_Port
```

Example:

```
<Proxy_Port ua="rw">3128</Proxy_Port>
```

Web Parameter

Default Value

3128

Allowed Values

Integer (0-9), String

Units

Integer

Limits

0 to 65535

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Specifies a port number of the proxy host server that the phone uses.

The parameter configuration is required if the Proxy Mode is set to Manual . For details, see Proxy_Mode .

Phone Model

All MPP phones

Labels

Proxy

## Proxy_Server_Requires_Authentication

## Syntax Description

XML Tag Name

```
Proxy_Server_Requires_Authentication
```

Example:

```
<Proxy_Server_Requires_Authentication ua="rw">No</Proxy_Server_Requires_Authentication>
```

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Selects the option according to the actual behaviour of the proxy server. If the proxy server requires the user to provide
                                 authentication credentials, select Yes . Otherwise, select No .

If the parameter is set to Yes , the proxy server requires username and password to grant the access right. For details, see Proxy_Username and Proxy_Password .

Phone Model

All MPP phones

Labels

Proxy

## Proxy_Username

## Syntax Description

XML Tag Name

```
Proxy_Username
```

Example:

```
<Proxy_Username ua="rw">Example</Proxy_Username>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

Strings without units

Limits

N/A

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Specifies a username for the authentication purpose of the proxy server.

The parameter configuration is required when Proxy Mode is set to Manual and Proxy Server Requires Authentication is set to Yes . For details, see Proxy_Mode and Proxy_Server_Requires_Authentication .

Phone Model

All MPP phones

Labels

Proxy

## PRT_HTTP_Header

## Syntax Description

XML Tag Name

```
PRT_HTTP_Header
```

Example:

```
<PRT_HTTP_Header ua="na">x-cisco-spark-canary-opts</PRT_HTTP_Header>
```

Web Parameter

Default Value

Empty

Allowed Values

Units

N/A

Limits

Maximum of 127 characters

User or Admin

Admin

Description

Specifies the HTTP header for the URL in PRT Upload Rule .

The parameter value is associated with PRT HTTP Header Value .

Only when both parameters are configured, the HTTP header is included in the HTTP request.

Phone Model

All MPP phones

Labels

Provisioning

## PRT_HTTP_Header_Value

## Syntax Description

XML Tag Name

```
PRT_HTTP_Header_Value
```

Example:

```
<PRT_HTTP_Header_Value ua="na">always</PRT_HTTP_Header_Value>
```

Web Parameter

Default Value

Empty

Allowed Values

Except for the underscore (_), the first character must not be a special character.

Units

N/A

Limits

0 or 2–127 characters

User or Admin

Admin

Description

Sets the value of the specified HTTP header.

The parameter value is associated with PRT HTTP Header .

Only when both parameters are configured, the HTTP header is included in the HTTP request.

Phone Model

All MPP phones

Labels

Provisioning

## PRT Upload at Crash Enable

## Syntax Description

XML Tag Name

```
PRT_Upload_at_Crash
```

Example:

```
<PRT_Upload_at_Crash ua="na">Yes</PRT_Upload_at_Crash>
```

Web Parameter

PRT Upload at Crash

Default Value

No

Allowed Values

Option list: Yes|No

Units

Yes|No

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

You can indicate whether to automatically upload the PRT package to the server when the phone crashes.

Phone Model

Supported by all Series

Labels

Directory

## PSK_n

## Syntax Description

XML Tag Name

```
PSK_n
```

n is the PSK ID (1-16)

Example:

```
<PSK_1 ua="na">fnc=sd;ext=5014@$PROXY;nme=sktest1</PSK_1>
```

Web Parameter

Default Value

N/A

Allowed Values

Units

Integer

Limits

1 to 16

User or Admin

Admin

Description

Programmable softkey fields. Enter a string in these fields to
                                 									configure softkeys that display on the phone screen. You can
                                 									create softkeys for speed dials to numbers or extensions,
                                 									vertical service activation codes (* codes), or XML scripts.

Phone Model

All MPP phones

Labels

PSK

## Register_Expires_n_

## Syntax Description

XML Tag Name

```
Register_Expires_n_
```

Example:

```
<Register_Expires_1_ ua="na">3600</Register_Expires_1_>
```

Web Parameter

Default Value

3600

Allowed Values

Units

Seconds

Limits

Integer ranges 0 to 86400

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available
                                 									on LCD UI.

Description

Defines how often the phone renews registration with the proxy.
                                 									If the proxy responds to a REGISTER with a lower expires value,
                                 									the phone renews registration based on that lower value instead
                                 									of the configured value. If registration fails with an “Expires
                                 									too brief” error response, the phone retries with the value
                                 									specified in the Min-Expires header of the error.

Phone Model

All MPP phones

Labels

SIP

## Replace_Unresolved_Caller_Name_with_Number

## Syntax Description

XML Tag Name

```
Replace_Unresolved_Caller_Name_with_Number
```

Example:

```
<Replace_Unresolved_Caller_Name_with_Number
ua="na">Yes</Replace_Unresolved_Caller_Name_with_Number>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available
                                 									on LCD UI.

Description

Controls whether to replace the caller name with the phone number
                                 									when installed font cannot resolve the full caller name.

Phone Model

All MPP phones

Labels

Locale

## Report_Problem_Menu

## Syntax Description

XML Tag Name

```
Report_Problem_Menu
```

Example:

```
<Report_Problem_Menu ua="na">Yes</Report_Problem_Menu>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Controls whether to show the Report problem menu on the phone screen. Set this field to Yes to show the menu. Otherwise, set it
                              								to No .

When the Status menu is invisible on the phone, the Report problem menu is invisible as
                              								well.

Phone Model

All MPP phones

Labels

Phone Menu Visibility

## Require_Authentication_for_LCD_Menu_Access

## Syntax Description

XML Tag Name

```
Require_Authentication_for_LCD_Menu_Access
```

Example:

```
<Require_Authentication_for_LCD_Menu_Access
ua="na">Default</Require_Authentication_for_LCD_Menu_Access>
```

Web Parameter

Default Value

Default

Allowed Values

Units

N/A

Limits

N/A

User or Admin

Admin

Description

Controls whether the user requires authentication to access phone
                                 									menus.

Default—When selected, user needs to provide password and
                                       											then sign in to access the phone menus that requires
                                       											authentication. Phone continues to support all the
                                       											functionalities that are supported in the releases prior
                                       											to 11.3(2). Phone displays lock screen icon.

To access any phone menus that require authentication,
                                       											user needs to provide the password and press Sign in.
                                       											The lock icon remains locked. After the user signs in,
                                       											the lock icon is unlocked.

Customized—When selected, user requires authentication
                                       											only to access Profile rule and Factory reset menus on the
                                       											phone. Authenticaion control of these two menus also
                                       											depends on the settings of the Factory Reset
                                          												Menu menu and the Profile
                                          												Rule Menu menu. User will not require
                                       											any authentication to access other phone menus.

No—When selected, the Sign in menu, the Sign out menu, the lock
                                       											icon, and the Set password menus
                                       											are not available on the phone. User can access phone
                                       											menus without any authentication.

Phone Model

All MPP phones

Labels

User Authentication Phone menus

## Ringer_Volume_Control

## Syntax Description

XML Tag Name

Ringer_Volume_Control

Example:

<Ringer_Volume_Control ua="na">Yes</Ringer_Volume_Control>

Web Parameter

Ringer Volume Control

Default Value

Yes

Allowed Values

Yes/No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed only in the phone web page for admin.

Description

When the parameter is set to Yes , the user can change the ringer volume. But when the parameter is set to No , the user can't change the ringer volume using the phone volume button or from the phone administration web page.

Phone Model

All MPP phones except 7832 and 8832

Labels

User

## Search_All_Enable

## Syntax Description

XML Tag Name

```
Search_All_Enable
```

Example:

```
<Search_All_Enable ua="na">Yes</Search_All_Enable>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

u=na

Description

Determines whether the phone user can search for contacts in the All directories .

All directories only contain the enabled
                                 									directories with the priority from highest to lowest.

Personal address book

BroadSoft directory

LDAP directory

Bluetooth phone directory

Phone Model

All MPP phones

Labels

Directory Service

## SDP_IP_Preference

## Syntax Description

XML Tag Name

```
SDP_IP_Preference
```

Example:

```
<SDP_IP_Preference ua="na">Auto</SDP_IP_Preference>
```

Web Parameter

Default Value

IPv4

Allowed Values

IPv4 | IPv6 | Auto

Units

Options

Limits

IPv4 | IPv6 | Auto

User or Admin

Admin level only

Description

Sets RTP IP address in SIP calls to align with the phone's registration IP.

Phone Model

All MPP phones

Labels

Auto

## Secure_Call_Option_n_

## Syntax Description

XML Tag Name

```
Secure_Call_Option_n_
```

n is the extension number of the phone.

Example:

```
<Secure_Call_Option_1_ ua="na">Optional</Secure_Call_Option_1_>
```

Web Parameter

Default Value

Optional

Allowed Values

Option list: Optional|Required|Strict

Units

N/A

Limits

N/A

User or Admin

Exposed in user level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Optional－Retains the current secure call option for the phone.

Required－Rejects nonsecure calls from other phones.

Strict－Allows SRTP only when SIP transport is set to TLS . Allows RTP only when SIP transport
                              								is UDP/TCP .

Phone Model

All MPP phones

Labels

Call Setting Features

## Share_Line_Event_Package_Type

## Syntax Description

XML Tag Name

```
Share_Line_Event_Package_Type
```

Example:

```
<Share_Line_Event_Package_Type ua="na">Call-Info</Share_Line_Event_Package_Type>
```

Web Parameter

Share Line Event Package Type

Default Value

Call-Info

Allowed Values

Call-Info

Dialog

Units

N/A

Limits

N/A

User or Admin

Exposed only in the phone web page for both user and admin. Not available on LCD UI.

Description

Enables dialog-based shared line so that the phones in the shared line can subscribe to the dialog event package.

Phone Model

All MPP phones

Labels

SIP

## SIP_100REL_Enable_n_

XML Tag Name

```
SIP_100REL_Enable_n_
```

n is the extension number of the phone.

Example:

```
<SIP_100REL_Enable_1_ ua="na">No</SIP_100REL_Enable_1_>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Individually enables the SIP 100REL feature.

When enabled, the phone supports the 100REL SIP extension for reliable transmission of provisional responses (18x) and uses
                              PRACK requests.

Phone Model

All MPP phones

Labels

SIP Settings

## SIP_IP_Preference

## Syntax Description

XML Tag Name

```
<SIP_IP_Preference>
```

Example:

```
<SIP_IP_Preference>IPv6</SIP_IP_Preference>
```

Web Parameter

Default Value

IPv4

Allowed Values

IPv4 | IPv6

Units

N/A

Limits

Options

User or Admin

Admin level only

Description

Sets the SIP IP Preference for the phone.

Phone Model

All MPP phones

Labels

SIP

## SIP_Timer_F

## Syntax Description

XML Tag Name

```
SIP_Timer_F
```

Example:

Web Parameter

Default Value

N/A

Allowed Values

Units

Seconds

Limits

0 to 64 seconds

User or Admin

Admin

Description

Non-INVITE time-out value.

Phone Model

All MPP phones

Labels

SIP

## SIP_Transport

## Syntax Description

XML Tag Name

```
SIP_Transport
```

Example:

```
<SIP_Transport_n_ ua="na">UDP</SIP_Transport_n_>
```

where n is the extension number.

Web Parameter

Default Value

N/AUDP

Allowed Values

Units

N/A

Limits

N/A

User or Admin

Admin

Description

Specifies the transport protocol for SIP messages. For SIP
                                 									messages, you can configure each extension to use:

a specific protocol

the protocol automatically selected by the phone

When you set up automatic selection, the phone determines the
                                 									transport protocol based on the Name Authority Pointer (NAPTR)
                                 									records on the DNS server. The phone uses the protocol with the
                                 									highest priority in the records.

Phone Model

All MPP phones

Labels

SIP Settings

## Speed_Dials

## Syntax Description

XML Tag Name

```
Speed_Dials
```

Example:

```
<Speed_Dials ua="na">Yes</Speed_Dials>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Controls whether to show the Speed dials menu
                              								on the phone screen. Set this field to Yes to
                              								show the menu. Otherwise, set it to No .

Phone Model

All MPP phones

Labels

Speed Dial

## SSRC_Reset_on_Rx_RE-INVITE

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on incoming RE-INVITE.

When the parameter is set to Yes , the phone can avoid the call transfer error, where only one person on the call hears the audio. This occurs on calls of
                              30 minutes or longer, and often on three-way calls.

When the parameter is set to No , the SSRC still remains during a long duration call. In this case, this error might occur.

Phone Model

All MPP phones

Labels

SIP

## SSRC_Reset_on_Tx_RE-INVITE

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on outgoing RE-INVITE.

When the parameter is set to Yes , the phone can avoid the one-way audio issue on a long duration call followed by a hold-resume action in certain Webex Calling
                              environments where the SRTP is end-to-end encrypted.

When the parameter is set to No , the SSRC still remains during a long duration call. In this case, this error might occur.

Phone Model

All MPP phones

Labels

SIP

## Status

## Syntax Description

XML Tag Name

```
Status
```

Example:

```
<Status ua="na">Yes</Status>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Controls whether to show the Status menu on
                              								the phone screen. Set this field to Yes to
                              								show the menu. Otherwise, set it to No .

Phone Model

All MPP phones

Labels

Phone Menu Visibility

## Survivability_Proxy_n_

## Syntax Description

XML Tag Name

```
Survivability_Proxy_n_
```

Syntax:

```
<Survivability_Proxy_n_>hostname[:port][:A=ip-list] [| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_>
```

Example:

```
<Survivability_Proxy_n_>wxclsg.example.com:8933:A=192.169.10.1</Survivability_Proxy_n_>
```

Web Parameter

Default Value

Blank

Allowed Values

String

Units

NA

Limits

NA

User or Admin

Admin level only. Not available on LCD UI.

Description

The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform
                              a failover to a survivability gateway.

Phone Model

All MPP phones

Labels

Proxy and Registration

## Survivability_Proxy_Fallback_Intvl_n_

## Syntax Description

XML Tag Name

```
Survivability_Proxy_Fallback_Intvl_n_
```

Example:

```
<Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_>
```

Web Parameter

Default Value

30 sec

Allowed Values

Integer

Units

Seconds

Limits

0 to 65535

User or Admin

Admin level only. Not available on LCD UI.

Description

The interval in seconds after which the phone will attempt to fallback to the SSE nodes

Phone Model

All MPP phones

Labels

Proxy and Registration

## Survivability_Test_Mode

## Syntax Description

XML Tag Name

```
Survivability_Test_Mode
```

Example:

```
<Survivability_Test_Mode>No</Survivability_Test_Mode>
```

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean

Limits

Yes|No

User or Admin

Admin level only. Not available on LCD UI.

Description

If set it to Yes, phone will always register to Site Survivability Gateway (SGW) nodes.

Phone Model

All MPP phones

Labels

System

## Time_Format

## Syntax Description

XML Tag Name

```
Time_Format
```

Example:

```
<Time_Format ua="na">12hr</Time_Format>
```

Web Parameter

Default Value

12 hr

Allowed Values

12hr|24hr

Units

N/A

Limits

Options

User or Admin

Admin level only.

Description

Specifies a time format in which the user can enter a time until which the desk will be reserved.

Phone Model

All MPP phones

Labels

User

## TLS_Cipher_List

## Syntax Description

XML Tag Name

```
TLS_Cipher_List
```

Example:

```
<TLS_Cipher_List ua="na">RSA:!aNULL:!eNULL</TLS_Cipher_List>
```

Web Parameter

Default Value

(Blank)

Allowed Values

Any string

Units

String without units

Limits

Min length: 0 Max length: 521

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Allows you to specify the cipher list that the phone TLS applications
                              								use.

For the cipher list formats, see
                              								https://www.openssl.org/docs/man1.0.2/man1/ciphers.html.

Phone Model

All MPP phones

Labels

Security

## TLS_Client_Min_Version

## Syntax Description

XML Tag Name

Example:

Web Parameter

TLS Client Min Version

Default Value

TLS 1.2

Allowed Values

Option list: TLS 1.0|TLS 1.1|TLS 1.2|TLS 1.3

Units

N/A

Limits

TLS 1.0|TLS 1.1|TLS 1.2|TLS 1.3

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls the minimum TLS version that the phone supports when the phone works as a TLS client.

Phone Model

All MPP phones

The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3.

Labels

System

## TLS_Name_Validate_n_

## Syntax Description

XML Tag Name

```
TLS_Name_Validate_n_
```

n is the extension number of the phone.

Example:

```
<TLS_Name_Validate_1_ ua="na">Yes</TLS_Name_Validate_1_>
```

Web Parameter

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Option

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Specifies whether hostname verification is required when the phone
                              								line uses SIP over TLS.

This parameter works only when SIP Transport is set to TLS for the phone line.

Phone Model

All MPP phones

Labels

Security

## TLS_Server_Min_Version

## Syntax Description

XML Tag Name

Example:

Web Parameter

TLS Server Min Version

Default Value

TLS 1.2

Allowed Values

Option list: TLS 1.1|TLS 1.2|TLS 1.3

Units

N/A

Limits

TLS 1.1|TLS 1.2|TLS 1.3

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls the minimum TLS version that the phone supports when the phone works as a TLS server.

Phone Model

All MPP phones

The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3.

Labels

System

## Transition_Authorization_Error_Retry_Delay

## Syntax Description

XML Tag Name

```
Transition_Authorization_Error_Retry_Delay
```

Example:

```
<Transition_Authorization_Error_Retry_Delay>1800</Transition_Authorization_Error_Retry_Delay>
```

Web Parameter

Default Value

1800

Allowed Values

An integer

Multiple integers

A time range

Units

Limits

User or Admin

Admin level only

Description

If an authorization operation fails, the device tries to authorize again after a time specified in seconds. If the delay is
                              set to 0, the device does not do the retry.

Phone Model

7800 MPP, 8800 MPP, 7832 MPP, and 8832 MPP phoness

Labels

Provisioning

## Trans_Auth_Rule

## Syntax Description

XML Tag Name

```
Trans_Auth_Rule
```

Example:

```
<Trans_Auth_Rule ua="na">http://10.74.51.81/prov/migration/E2312.lic</Trans_Auth_Rule>
```

Web Parameter

Transition Authorization Rule

Default Value

Blank

Allowed Values

String

Units

N/A

Limits

N/A

User or Admin

Exposed only in the phone web page for admin. Not available on the LCD UI.

Description

Obtains and authorizes the licence from the server.

Phone Model

Supported by all 78xx and 88xx

Labels

Firmware Upgrade

## Trans_Auth_Type

## Syntax Description

XML Tag Name

```
Trans_Auth_Type
```

Example:

```
<Trans_Auth_Type ua="na">Classic</Trans_Auth_Type>
```

Web Parameter

Transition Authorization Type

Default Value

Classic

Allowed Values

Classic

WxC

Units

N/A

Limits

N/A

User or Admin

Exposed only in the phone web page for admin. Available on LCD UI.

Description

Indicates the license type obtained from the server during migration process.

Phone Model

Supported by all 78xx and 88xx

Labels

Firmware Upgrade

## Unavailable_Reason_Code_Enable_n_

## Syntax Description

XML Tag Name

```
Unavailable_Reason_Code_Enable_n_
```

n is the extension number of the phone.

Example:

```
<Unavailable_Reason_Code_Enable_n_ ua="na">Yes</Unavailable_Reason_Code_Enable_n_>
```

Web Parameter

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether to show or hide the Unavailable menu text box of the Set agent status screen on the phone.

Phone Model

All MPP phones

Labels

ACD Settings

## Unit_n_Extension_m_

## Syntax Description

XML Tag Name

```
Unit_n_Extension_m_
```

Example:

```
<Unit_n_Extension_m_ >Disabled</Unit_n_Extension_m_ >
```

where, [n] is the unit number that ranges from 1 to 3 for Cisco IP phone 8861 and 8865 and 1 to 2 for Cisco IP phone 8851;
                                 [m] is the line key number that ranges from 1 to 28.

Web Parameter

Default Value

Disabled

Allowed Values

1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|Disabled

Units

N/A

Limits

Options

User or Admin

Admin level only.

Description

Assign an extension to the audio and video key expansion module line key.

Phone Model

Cisco IP Phone 8851, 8861, 8865 Multiplatform phone.

Labels

Att Console

## Unit_n_Key_m_

## Syntax Description

XML Tag Name

```
Unit_n_Key_m_
```

n is unit number of the key expansion module, and m is the key
                              								number.

Web Parameter

Default Value

N/A

Allowed Values

N/a

Units

String without units

Limits

N/A

User or Admin

Admin

ua=na

Description

Adds a menu shortcut to a line key of the attached key expansion
                              								module. Then, the user can press the configured line key to access
                              								the menu.

Adds an extended feature to a line key of the attached key expansion
                              								module. Then, the user can press the line key to access the
                              								feature.

Example:

```
<Unit_1_Key_2_ ua="na">fnc=shortcut;url=userpref;nme=User preferences</Unit_1_Key_2_>
```

where

fnc= shortcut means function=phone menu shortcut.

url= userpref is the menu to open with this line key. It's
                                    										the User preferences menu in this
                                    										example.

nme= XXXX is the menu shortcut name displayed on the key
                                    										expansion module screen. If you don't specify a display
                                    										name, the line key displays the target menu item. In the
                                    										example, the line key displays User
                                       											preferences .

Phone Model

All MPP phones

Labels

Menu Shortcut key expansion module

## Unit_n_Share_Call_Appearance_m

## Syntax Description

XML Tag Name

```
Unit_n_Share_Call_Appearance_m
```

Example:

```
<Unit_n_Share_Call_Appearance_m >private</Unit_n_Share_Call_Appearance_m >
```

where, [n] is the unit number that ranges from 1 to 3 for Cisco IP phone 8861 and 8865 and 1 to 2 for Cisco IP phone 8851;
                              [m] is the line key number that ranges from 1 to 28.

Web Parameter

Default Value

shared|private

Allowed Values

Options

Units

N/A

Limits

Options

User or Admin

Admin level only.

Description

Specifies if the line is private or shared.

Phone Model

Cisco IP Phone 8851, 8861, and 8865 Multiplatform phone.

Labels

Att Console

## Unit_n_Short_Name_m_

## Syntax Description

XML Tag Name

```
Unit_n_Short_Name_m_
```

Example:

```
<Unit_n_Short_Name_m_ ua="na">$USER</Unit_n_Short_Name_m>
```

where, [n] is the unit number that ranges from 1 to 3 for Cisco IP phone 8861 and 8865 and 1 to 2 for Cisco IP phone 8851;
                              [m] is the line key number that ranges from 1 to 28.

Web Parameter

Default Value

$USER

Allowed Values

Alpha numeric

Units

N/A

Limits

N/A

User or Admin

Admin level only.

Description

Assign a short name.

Phone Model

Cisco IP Phone 8851, 8861, and 8865 Multiplatform phone.

Labels

Att Console

## Use_Auto_Discovery__WPAD_

## Syntax Description

XML Tag Name

```
<Use_Auto_Discovery__WPAD_>
```

Example:

```
<Use_Auto_Discovery__WPAD_ ua="rw">No</Use_Auto_Discovery__WPAD_>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Controls whether to use the Web Proxy Auto-Discovery (WPAD) protocol to retrieve a Proxy Auto-Configuration (PAC) file. The
                                 phone will search for the PAC file by DHCP or DNS service.

If the parameter is set to No , the user must manually specify a PAC URL that locates to the PAC file. For details, see PAC_URL PAC_URL .

The parameter configuration takes effect only when the Proxy Mode is set to Auto . For details, see Proxy_Mode .

Phone Model

All MPP phones

Labels

Proxy

## User_Preferences

## Syntax Description

XML Tag Name

```
User_Preferences
```

Example:

```
<User_Preferences ua="na">Yes</User_Preferences>
```

Web Parameter

Default Value

Yes

Allowed Values

Yes|No

Units

Boolean

Limits

N/A

User or Admin

Admin

ua=na

Description

Controls whether to show the User preferences menu on the phone screen.

Set this field to Yes to show the menu.
                              								Otherwise, set it to No .

Phone Model

All MPP phones

Labels

Phone Menu Visibility

## Voice_Feedback_Enable

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Not available on LCD UI.

Description

Controls whether to enable the voice feedback feature for the user.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## Voice_Feedback_Speed

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Normal

Allowed Values

Option list: Slowest|Slower|Normal|Faster|Fastest

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Available on LCD UI.

Description

Controls the voice speed for the Voice Feedback feature.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## Voice_Feedback_Volume

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Normal

Allowed Values

Option list: Lowest|Low|Normal|High|Highest

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=rw. Available on LCD UI.

Description

Controls the volume for Voice Feedback.

Phone Model

Supported by 8800 Series and 8832

Labels

User

## Voice_Mail_Enable_n_

## Syntax Description

XML Tag Name

```
Voice_Mail_Enable_n_
```

n is the extension number of the phone.

Example:

```
<Voice_Mail_Enable_1_ ua="na">Yes</Voice_Mail_Enable_1_>
```

Web Parameter

Voice Mail Enable

Default Value

Yes

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Controls whether the extension is allowed to subscribe to the voicemail server.

Phone Model

All MPP phones

Labels

Call Feature Settings

## VPN_Password

## Syntax Description

XML Tag Name

```
VPN_Password
```

Example:

```
<VPN_Password ua="rw">Example</VPN_Password>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

Maximum of 31 characters

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Provides the password of the specified username that the VPN server requires.

Phone Model

All MPP phones except 6821, 7832, and 8832

Labels

VPN

## VPN_Server

## Syntax Description

XML Tag Name

```
VPN_Server
```

Example:

```
<VPN_Server ua="rw"> <Server IP or FQDN> </VPN_Server>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

Maximum of 31 characters

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Specifies an IP address or FQDN of the VPN server that the phone uses. For example:

100.101.1.218

Phone Model

All MPP phones except 6821, 7832, and 8832

Labels

VPN

## VPN_Tunnel_Group

## Syntax Description

XML Tag Name

```
VPN_Tunnel_Group
```

Example:

```
<VPN_Tunnel_Group ua="rw">Example</VPN_Tunnel_Group>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

Maximum of 31 characters

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Specifies a VPN tunnel group for the VPN connection.

A tunnel group is used to determine the tunnel connection policies and rules.

Phone Model

All MPP phones except 6821, 7832, and 8832

Labels

VPN

## VPN_User_Name

## Syntax Description

XML Tag Name

```
VPN_User_Name
```

Example:

```
<VPN_User_Name ua="rw">Example</VPN_User_Name>
```

Web Parameter

Default Value

Empty

Allowed Values

String

Units

String without units

Limits

Maximum of 31 characters

User or Admin

Exposed both in admin and user level, honored with ua = rw. Available on LCD UI.

Description

Specifies a username required to connect to the specified VPN server.

Phone Model

All MPP phones except 6821, 7832, and 8832

Labels

VPN

## Webex_Onboard_Enable

## Syntax Description

XML Tag Name

```
Webex_Onboard_Enable
```

Example:

```
<Webex_Onboard_Enable ua="na">Yes</Webex_Onboard_Enable>
```

Web Parameter

Onboard Enable

Default Value

Yes

Allowed Values

Yes/No

Units

Boolean

Limits

N/A

User or Admin

Exposed only in the phone web page for admin. Not available on LCD

UI.

Description

Enables onboarding of the phone to Cisco Webex cloud.

Phone Model

All MPP phones

Labels

Webex

## Webex_Directory_Enable

## Syntax Description

XML Tag Name

```
Webex_Directory_Enable
```

Example:

```
<Webex_Directory_Enable ua="na”>No</Webex_Directory_Enable>
```

Web Parameter

Directory Enable

Default Value

No

Allowed Values

Yes/No

Units

Boolean

Limits

N/A

User or Admin

Exposed only in the phone web page for admin. Not available on LCD UI.

Description

Enables webex contacts.

Phone Model

All MPP phones

Labels

Webex

## Webex_Directory_Name

## Syntax Description

XML Tag Name

```
Webex_Directory_Name
```

Example:

```
<Webex_Directory_Name ua="na”/>
```

Web Parameter

Directory Name

Default Value

Blank

Allowed Values

N/A

Units

N/A

Limits

N/A

User or Admin

Exposed in the phone web page for admin. Available on LCD UI.

Description

Modifies Webex directory name.

Phone Model

All MPP phones

Labels

Webex

## Webex_Calendar_Enable

## Syntax Description

XML Tag Name

```
Webex_Calendar_Enable
```

Example:

```
<Webex_Calendar_Enable ua="na">Yes</Webex_Calendar_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Yes|No

Units

Boolean

Limits

Yes|No

User or Admin

Admin level only. Not available on LCD UI.

Description

If set it to Yes, phone supports Webex OBTJ meetings with display of multiple meeting notifications in the meeting list. Also, Meeting softkey appears.

Phone Model

8800 MPP phones only

Labels

Webex

## Webex Metrics Enable Parameter

## Syntax Description

XML Tag Name

```
Webex_Metrics_Enable
```

Example:

```
<Webex_Metrics_Enable ua="na">Yes</Webex_Metrics_Enable>
```

Web Parameter

Webex Metrics Enable

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean

Limits

Yes|No

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

With Metrics Enable, enable the phone control of all metric services.

Phone Model

Supported by all Series

Labels

Directory

## Web_Server_Port

## Syntax Description

XML Tag Name

```
Web_Server_Port
```

Example:

```
<Web_Server_Port ua="na">443</Web_Server_Port>
```

Web Parameter

Web Server Port

Default Value

443

Allowed Values

Numeric

Units

Numeric

Limits

User or Admin

Exposed in admin level, honored with ua = na. Not available on LCD UI.

Description

Set the default port to 443.

Phone Model

Supported by all phones

Labels

System

## Work_Days

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

Monday|Tuesday|Wednesday|Thursday|Friday

Allowed Values

Option list: Saturday|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Specifies work days. During non-workdays, the phone will automatically turn off the screen. By default, workdays are set from
                              Monday to Friday.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## Working_Hours_End

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

19:00

Allowed Values

00:00 to 24:00

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Specifies the end time for working hours using the 24-hour format. Outside of the specified working hours, the phone will
                              automatically turn off the screen.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## Working_Hours_Start

## Syntax Description

XML Tag Name

Example:

Web Parameter

Default Value

07:00

Allowed Values

00:00 to 24:00

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua=na. Not available on LCD UI.

Description

Specifies the start time for working hours using the 24-hour format. Outside of the specified working hours, the phone will
                              automatically turn off the screen.

Phone Model

Supported by 8800 Series and 8832

Labels

Phone

## XsiDir_EnterpriseCommon_Enable

## Syntax Description

XML Tag Name

```
XsiDir_EnterpriseCommon_Enable
```

Example:

```
<XsiDir_EnterpriseCommon_Enable ua="na">Yes</XsiDir_EnterpriseCommon_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enables BroadSoft EnterpriseCommon directory.

The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_EnterpriseCommon_Name

## Syntax Description

XML Tag Name

```
XsiDir_EnterpriseCommon_Name
```

Example:

```
<XsiDir_EnterpriseCommon_Name ua="na">DirEnterpriseCommon</XsiDir_EnterpriseCommon_Name>
```

Web Parameter

Default Value

Empty

Allowed Values

String without units

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Name of the BroadSoft personal directory. Displays on the phone as a
                              								directory choice.

If the value is empty, the phone displays default name Enterprise Common .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Enterprise_Enable

## Syntax Description

XML Tag Name

```
XsiDir_Enterprise_Enable
```

Example:

```
<XsiDir_Enterprise_Enable ua="na">Yes</XsiDir_Enterprise_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enables BroadSoft enterprise directory.

The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Enterprise_Name

## Syntax Description

XML Tag Name

```
XsiDir_Enterprise_Name
```

Example:

```
<XsiDir_Enterprise_Name ua="na">DirEnterpriseName</XsiDir_Enterprise_Name>
```

Web Parameter

Default Value

Empty

Allowed Values

String without units

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Name of the BroadSoft Enterprise directory. Displays on the phone as
                              								a directory choice.

If the value is empty, the phone displays default name Enterprise .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Group_Enable

## Syntax Description

XML Tag Name

```
XsiDir_Group_Enable
```

Example:

```
<XsiDir_Group_Enable ua="na">Yes</XsiDir_Group_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enables BroadSoft Group directory.

The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Group_Name

## Syntax Description

XML Tag Name

```
XsiDir_Group_Name
```

Example:

```
<XsiDir_Group_Name ua="na">DirGroupName</XsiDir_Group_Name>
```

Web Parameter

Default Value

Empty

Allowed Values

String without units

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Name of the BroadSoft Group directory. Displays on the phone as a
                              								directory choice.

If the value is empty, the phone displays default name Group .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_GroupCommon_Enable

## Syntax Description

XML Tag Name

```
XsiDir_GroupCommon_Enable
```

Example:

```
<XsiDir_GroupCommon_Enable ua="na">Yes</XsiDir_GroupCommon_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enables BroadSoft GroupCommon directory.

The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_GroupCommon_Name

## Syntax Description

XML Tag Name

```
XsiDir_GroupCommon_Name
```

Example:

```
<XsiDir_GroupCommon_Name ua="na">DirGroupCommon</XsiDir_GroupCommon_Name>
```

Web Parameter

Default Value

Empty

Allowed Values

String without units

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Name of the BroadSoft personal directory. Displays on the phone as a
                              								directory choice.

If the value is empty, the phone displays default name Group Common .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Individual_Mode_Enable

## Syntax Description

XML Tag Name

```
XsiDir_Individual_Mode_Enable
```

Example:

```
<XsiDir_Individual_Mode_Enable ua="na">Yes</XsiDir_Individual_Mode_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Individually enable or disable broadsoft directories. Only valid when XSI Directory Enable parameter is set to Yes .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Personal_Enable

## Syntax Description

XML Tag Name

```
XsiDir_Personal_Enable
```

Example:

```
<XsiDir_Personal_Enable ua="na">Yes</XsiDir_Personal_Enable>
```

Web Parameter

Default Value

No

Allowed Values

Option list: Yes|No

Units

Boolean without units

Limits

Boolean

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Enables BroadSoft personal directory.

The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes .

Phone Model

All MPP phones

Labels

Directory

## XsiDir_Personal_Name

## Syntax Description

XML Tag Name

```
XsiDir_Personal_Name
```

Example:

```
<XsiDir_Personal_Name ua="na">DirPersonalName</XsiDir_Personal_Name>
```

Web Parameter

Default Value

Empty

Allowed Values

String without units

Units

N/A

Limits

N/A

User or Admin

Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI.

Description

Name of the BroadSoft personal directory. Displays on the phone as a
                              								directory choice.

If the value is empty, the phone displays default name Personal .

Phone Model

All MPP phones

Labels

Directory

## X-SWITCH-INFO_Support

## Syntax Description

XML Tag Name

```
X-SWITCH-INFO_Support
```

Example:

```
“<X-SWITCH-INFO_Support ua=”na“>Yes</X-SWITCH-INFO_Support>”
```

Web Parameter

N/A

Default Value

No

Allowed Values

Yes/No

Units

Bool

Limits

N/A

User or Admin

Admin level only.

Description

If selected, the Register message will include the X-switch-info header.

Phone Model

Applicable to all models.

Labels

Network

| Release | What's New and Updated |
|---|---|
| Firmware Release 12.0(7)SR3 | Font_Size TLS_Client_Min_Version TLS_Server_Min_Version SSRC_Reset_on_Rx_RE-INVITE SSRC_Reset_on_Tx_RE-INVITE |
| Firmware Release 12.0(7)SR2 | TLS_Client_Min_Version TLS_Server_Min_Version |
| Firmware Release 12.0(7) | Office_Hours_Enabled Work_Days Working_Hours_Start Working_Hours_End LED_Indicator_In_Display_Off_Mode Display_Off_Idle_Timeout__mins_ Certificate_Select CDC_Server_1_ CDC_Root_CA_Fingerprint_1_ CDC_Challenge_Password_1_ Enable_802.1X_Authentication Accessibility Voice_Feedback_Enable Voice_Feedback_Speed Key_Again_Reset_Time Key_Double_Press_Time Key_Triple_Press_Time Voice_Feedback_Volume Font_Size |
| Firmware Release 12.0(5) | SDP_IP_Preference Forced_NAT64 |
| Firmware Release 12.0(4) | Call_Appearances_Per_Line X-SWITCH-INFO_Support BLF_Callpark_On_Line_Key_Enable |
| Firmware Release 12.0(3) | Time_Format Unit_n_Extension_m_ Unit_n_Share_Call_Appearance_m Unit_n_Short_Name_m_ Display_Password_Warnings Enable_Protocol Web_Server_Port |
| Firmware Release 12.0(2) | Auth_Support_RFC8760 Webex Metrics Enable Parameter PRT Upload at Crash Enable Callinfo_subscribe_1 TLS_Client_Min_Version Transition_Authorization_Error_Retry_Delay |
| Firmware Release 11.3(7) | Connect_on_Bootup Disable_Side_USB_Port Enable_Direct_PLK_Configuration LDAP_Unified_Search_Enable PAC_URL Proxy_Host Proxy_Mode Proxy_Password Proxy_Port Proxy_Server_Requires_Authentication Proxy_Username Use_Auto_Discovery__WPAD_ VPN_Password VPN_Server VPN_Tunnel_Group VPN_User_Name Webex_Directory_Enable Webex_Directory_Name |
| Firmware Release 11.3(6) | Forward_Softkey Display_Recents_From Keep_Focus_On_Active_Call Webex_Onboard_Enable Webex_Directory_Enable Webex_Directory_Name |
| Firmware Release 11.3(5) | Keep_Focus_On_Active_Call MIC_Cert_Info MIC_Cert_Provisioning_Status MIC_Cert_Refresh_Enable MIC_Cert_Refresh_Rule Share_Line_Event_Package_Type Trans_Auth_Rule Trans_Auth_Type Voice_Mail_Enable_n_ |
| Firmware Release 11.3(4) | Introduced document for Cisco IP Phone Multiplatform Phones XML parameters running SIP Firmware Release 11.3(4) with Cisco BroadWorks 24.0. This version contains only Rel 11.3(4) parameters. |
| Firmware Release 11.3(3) | Introduced document for Cisco IP Phone Multiplatform Phones XML parameters running SIP Firmware Release 11.3(3) with Cisco BroadWorks 24.0. This version contains only Rel 11.3(3) parameters. |
| Firmware Release 11.3(2) | Introduced document for Cisco IP Phone Multiplatform Phones XML parameters running SIP Firmware Release 11.3(2) with BroadSoft BroadWorks 23.0. This version contains only Rel 11.3(2) parameters. |

| XML Tag Name | Accessibility Example: <Accessibility ua="na">Yes</Accessibility> |
|---|---|
| Web Parameter | Accessibility |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Available on LCD UI. |
| Description | Controls whether to show the Accessibility menu on the phone screen. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | ACD_Logged-off_LED Example: <ACD_Logged-off_LED ua="na">c=o</ACD_Logged-off_LED> |
|---|---|
| Web Parameter | ACD Logged-off LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | The LED color and cadence state when the ACD PLK selected line has logged off ACD. It will
                              								follow the LED Pattern which is defined by customers. The LED
                              								Pattern Format is c=<COLOR> [; p=<PATTERN>]. c is |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | Att console |

| XML Tag Name | ACD_Logged-on_LED Example: <ACD_Logged-on_LED ua="na">c=g;p=n</ACD_Logged-on_LED> |
|---|---|
| Web Parameter | ACD Logged-on LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | The LED color and cadence state when the ACD PLK selected line has logged on ACD. It will
                              								follow the LED Pattern which is defined by customers. The LED
                              								Pattern Format is c=<COLOR> [; p=<PATTERN>].  c is mandatory
                              								and p is optional where default behavior is "no blink with solid
                              								color" if it is not specified. |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | Att Console |

| XML Tag Name | ACD_Status_n_ Example: <ACD_Status_1_ ua="na">Sync From Local</ACD_Status_1_> where n is the extension from 1 to 16 |
|---|---|
| Web Parameter | ACD Status |
| Default Value | Sync From Server |
| Allowed Values | Option list: Sync From Server\|Sync From Local |
| Units | Options without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Sync From Server: When phone boots up, it will get ACD initial
                              								status from server, which is the legacy behavior. Sync From Local: When the phone boots up, status is changed to
                              								"Registered" from "Unregistered" or "Registration failed", or
                              								registration destination ip address is changed due to failover,
                              								fallback or DNS response is changed, , it will set ACD status to the
                              								most recent local value. |
| Phone Model | All MPP phones |
| Labels | ACD Settings |

| XML Tag Name | Add_Contacts_to_Directory_Personal Example: <Add_Contacts_to_Directory_Personal ua="na">Yes</Add_Contacts_to_Directory_Personal> |
|---|---|
| Web Parameter | Add Contacts to Directory Personal |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether to add contacts to the BroadSoft Personal directory instead of the local personal address book. |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | Allowed_APIs Example: <Allowed_APIs ua="na">.*</Allowed_APIs> |
|---|---|
| Web Parameter | Allowed APIs |
| Default Value | .* |
| Allowed Values | String/regular expression .* : All APIs are allowed /api/Call/v1/.* : All v1 Call interface calls are
                              								allowed. /api/Call/v1/(Dial\|Hangup) : Only the v1 Call interface calls Dial and Hangup are allowed. |
| Units | String without units |
| Limits | String |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. ua=na |
| Description | A
                              								regular expression that can be used to limit the API calls that are
                              								allowed from the controlling server. The regular expression provided is matched with the Request-URI path
                              								provided in the API request from the controlling server. If the
                              								entire path is not matched by the given regular expression, the API
                              								call is rejected. |
| Phone Model | All MPP phones |
| Labels | API |

| XML Tag Name | Assistant_Call_Filter Example: <Assistant_Call_Filter ua="na">Yes</Assistant_Call_Filter> |
|---|---|
| Web Parameter | Assistant Call Filter |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether to show the Call filter menu on the phone screen for the assistant role. Set this field to Yes to show the menu. Otherwise, set it to No . |
| Phone Model | Supported by 6871 and 8800 Series (not including 8832) |
| Labels | Phone Menu Visibility |

| XML Tag Name | Audio_Overload_Point_9dB Example: <Audio_Overload_Point_9dB ua="rw">No</Audio_Overload_Point_9dB> |
|---|---|
| Phone Web Parameter | N/A |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw. Available on XML config
                              								file only. Not available on LCD UI. |
| Description | Customer can use 9dB as the acoustic overload point when they select ETSI standard. It is
                              								not found on the Web UI. |
| Phone Model | Supported by 6841, 6851, 6861, 6871, 8811, 8851, 8861 |
| Labels | Audio |

| XML Tag Name | Auth_Support_RFC8760 Example: <Auth_Support_RFC8760>Yes</Auth_Support_RFC8760> |
|---|---|
| Web Parameter | Auth Support RFC8760 |
| Default Value | No |
| Allowed Values | Boolean |
| Units |  |
| Limits | Yes/No |
| User or Admin | Admin level only. |
| Description | Enabling Phone Authorization with RFC-8760. |
| Phone Model | All MPP phones |
| Labels | SIP Settings |

| XML Tag Name | Auto_Available_After_Sign-In_n_ n is the extensions number of the phone. Example: <Auto_Available_After_Sign-In_1_
ua="na">Yes</Auto_Available_After_Sign-In_1_> |
|---|---|
| Web Parameter | Auto Available After Sign-In |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Sets the agent status to Available automatically when the user signs
                              								into the phone as a call center agent. |
| Phone Model | All MPP phones |
| Labels | ACD Settings |

| XML Tag Name | Auto_Register_When_Failover Example: <Auto_Register_When_Failover_1_
ua="na">Yes</Auto_Register_When_Failover_1_> |
|---|---|
| Web Parameter | Auto Register When Failover |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on LCD UI. |
| Description | Controls the fallback duration. If set to Yes, the fallback happens only when current
                                 									registration expires, which means only a REGISTER message can
                                 									trigger fallback. For example, when the value for Register Expires is 3600 seconds
                                 									and Proxy Fallback Intvl is 600 seconds, the fallback is
                                 									triggered 3600 seconds later and not 600 seconds later. When the
                                 									value for Register Expires is 600 seconds and Proxy Fallback
                                 									Intvl is 1000 seconds, the fallback is triggered at 1200
                                 									seconds. After successfully registering back to primary server,
                                 									all the SIP messages go to primary server. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | BLF_Callpark_On_Line_Key_Enable Example: “<BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable>” |
|---|---|
| Web Parameter | N/A |
| Default Value | No |
| Allowed Values | Yes/No |
| Units | N/A |
| Limits | N/A |
| User or Admin | Admin level only. |
| Description | If selected, the BLF Call Park is supported on a specific line key. |
| Phone Model | Applicable to all models. |
| Labels | Voice>Att Console>General |

| XML Tag Name | BLF_List_URI Example: <BLF_List_URI ua="na">uri_name@server</BLF_List_URI> |
|---|---|
| Web Parameter | BLF List URI |
| Default Value | N/A |
| Allowed Values | uri_name@server |
| Units | N/A |
| Limits | N/A |
| User or Admin | Admin |
| Description | The Uniform Resource Identifier (URI) of the Busy Lamp Field
                                 									(BLF) list that you have set up for a user of the phone, on the
                                 									BroadSoft server.This field is only applicable if the phone is
                                 									registered to a BroadSoft server. The BLF list is the list of
                                 									users whose lines the phone is allowed to monitor. The BLF List URI must be specified in the format
                                 									<URI_name>@<server>. The BLF List URI specified must be
                                 									the same as the value configured for the List URI: sip parameter
                                 									on the BroadSoft server. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string
                                 									in this format: <BLF_List_URI
                                 									ua="na">MonitoredUsersList@sipurash22.com</BLF_List_URI> On the phone web interface, specify the BLF list that is defined
                                 									on the BroadSoft server. |
| Phone Model | All MPP phones |
| Labels | BLF |

| XML Tag Name | BLF_List_Feature_Options Example: <BLF_List_Feature_Options ua="na">prk</BLF_List_Feature_Options> |
|---|---|
| Phone Web Parameter | BLF List Feature Options |
| Default Value | blf+sd+cp |
| Allowed Values | blf+sd+cp\|prk |
| Units | String without units |
| Limits | Options |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on LCD UI |
| Description | This parameter decides which functions are enabled for those BLF
                                 									List URI auto-assigned linekeys. Enables One-Button Call Park
                                 									and there is no need to enter a combination of key strokes for
                                 									parking and unparking a call. blf+sd+cp —BLF List URI auto-assigned linekey will
                                       											support "BLF", "Speed Dial" and "Call Pickup"
                                       											functions. prk—BLF List URI auto-assigned linekey will only support
                                       											"Call Park/Unpark" function. |
| Phone Model | Supported by 78xx, 88xx, and 68xx except 7811, 7832 and 8832. |
| Labels | Att console |

| XML Tag Name | Block_Anonymous_Call_Enable_n_ n is the extension number of the phone. Example: <Block_Anonymous_Call_Enable_n_ ua="na">Yes</Block_Anonymous_Call_Enable_n_> |
|---|---|
| Web Parameter | Block Anonymous Call Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Enables synchronization of Anonymous Call Rejection between a specific line and a BroadSoft server. |
| Phone Model | All MPP phones |
| Labels | XSI Line Service |

| XML Tag Name | Broadsoft_Call_History_Key_List Example: <Broadsoft_Call_History_Key_List ua="na">option\|1;call\|2;editcall\|3</Broadsoft_Call_History_Key_List> |
|---|---|---|---|---|
| Web Parameter | Broadsoft Call History Key List |
| Default Value | option\|1;call\|2;editcall\|3;back\|4; option\|1;call\|2;editcall\|3; |
| Allowed Values | Supported strings: option, call, editcall, filter, and back. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Defines the values for the softkeys Option , Call , Edit call , Filter , and Back for All, Placed, Received, and Missed calls history list. |
| Phone Model | All MPP phones |
| Labels | PSK |

| XML Tag Name | Browse_Mode_Enable Example: <Browse_Mode_Enable ua="na">Yes</Browse_Mode_Enable> |
|---|---|
| Web Parameter | Browse Mode Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Directory Display Mode. When enabled, the contact list will be shown
                              								when you enter a directory. |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | Call_Appearances_Per_Line Example: <Call_Appearances_Per_Line="na">1</Call_Appearances_Per_Line> |
|---|---|
| Web Parameter | Call Appearances Per Line |
| Default Value | 2 |
| Allowed Values | 1to 10 |
| Units | N/A |
| Limits | Options |
| User or Admin | Admin level only. |
| Description | Sets a line to allow single call or multiple calls at a time. |
| Phone Model | All MPP phones |
| Labels | Phone |

| XML Tag Name | CallInfo_Subscribe_1_ Example: <CallInfo_Subscribe_1_ ua="na">Yes</CallInfo_Subscribe_1_> |
|---|---|
| Web Parameter | N/A |
| Default Value | No |
| Allowed Values | Boolean |
| Units |  |
| Limits | Yes/No |
| User or Admin | Admin level only. |
| Description | The parameter enables the phone to subscribe the Call-Info header. Only when the Call-Info is subscribed, the phone receives
                              Ad Hoc conference participants list from server. The Call-Info header also includes the call status changes. |
| Phone Model | All MPP phones |
| Labels | Ext |

| XML Tag Name | Call_Statistics Example: <Call_Statistics ua="na">No</Call_Statistics> |
|---|---|
| Web Parameter | Call Statistics |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. ua=na |
| Description | Specifies whether the phone sends end-of-call statistics within SIP
                              								messages when a call terminates or is put on hold. |
| Phone Model | All MPP phones |
| Labels | RTP |

| XML Tag Name | Call_Waiting_Enable_n_ n is the extension number of the phone. Example: <Call_Waiting_Enable_n_ ua="na">Yes</Call_Waiting_Enable_n_> |
|---|---|
| Web Parameter | Call Waiting Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Enables synchronization of Call Waiting between a specific line and a BroadSoft server. |
| Phone Model | All MPP phones |
| Labels | XSI Line Service |

| XML Tag Name | Cfwd_All Example: <Cfwd_All ua="rw">No</Cfwd_All> |
|---|---|
| Web Parameter | Cfwd All |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in user level, honored with ua = rw. Available on LCD UI. |
| Description | Forwards all calls. The setting of this parameter takes precedence
                              								over Cfwd Busy and Cfwd No Answer. |
| Phone Model | All MPP phones |
| Labels | UI/CCTRL |

| XML Tag Name | Cfwd_Busy Example: <Cfwd_Busy ua="rw">No</Cfwd_Busy> |
|---|---|
| Web Parameter | Cfwd Busy |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in user level, honored with ua = rw. Available on LCD UI. |
| Description | Forwards calls only if the line is busy. |
| Phone Model | All MPP phones |
| Labels | UI/CCTRL |

| XML Tag Name | Cfwd_No_Answer Example: <Cfwd_No_Answer ua="rw">No</Cfwd_No_Answer> |
|---|---|
| Web Parameter | Cfwd No Answer |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in user level, honored with ua = rw. Available on LCD UI. |
| Description | Forwards the incoming call only if the call isn’t answered for a waiting interval. |
| Phone Model | All MPP phones |
| Labels | UI/CCTRL |

| XML Tag Name | Cfwd_Setting Example: <Cfwd_Setting ua="rw">Yes</Cfwd_Setting> |
|---|---|
| Web Parameter | Cfwd Setting |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in user level, honored with ua = rw. Not available on LCD
                              								UI. |
| Description | Provides a user the ability to modify the call forward settings from
                              								the phone web page. This parameter isnot available in Release 11.3(2). It is available in Release 11.3(1) and
                              								earlier. |
| Phone Model | All MPP phones |
| Labels | UI/CCTRL |

| XML Tag Name | Call_Forward_On_LED Example: <Call_Forward_On_LED ua="na">c=r;p=n</Call_Forward_On_LED> |
|---|---|
| Web Parameter | Call Forward On LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a Color. This is equivalent to the system default of Slow
                              								Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | The LED color and cadence state when the call forward PLK indicates that the selected
                              								line's call forward state is On . It will follow the LED
                              								Pattern which is defined by customers. The LED Pattern Format is
                              								c=<COLOR> [; p=<PATTERN>]. c is mandatory and p is optional
                              								where default behavior is "no blink with solid color" if it is not
                              								specified |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | Att Console |

| XML Tag Name | Call_Forward_Off_LED Example: <Call_Forward_Off_LED ua="na">c=o</Call_Forward_Off_LED> |
|---|---|
| Web Parameter | Call Forward Off LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | The LED color and cadence state when the call forward PLK indicates
                              								that the selected line's call forward state is Off . It will
                              								follow the LED Pattern which is defined by customers. The LED
                              								Pattern Format is c=<COLOR> [; p=<PATTERN>]. c is mandatory
                              								and p is optional where default behavior is "no blink with solid
                              								color" if it is not specified |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | Att Console |

| XML Tag Name | CDC_Challenge_Password_1_ Example: <CDC_Challenge_Password_1_ ua="na"></CDC_Challenge_Password_1_> |
|---|---|
| Web Parameter | Challenge Password |
| Default Value | N/A |
| Allowed Values | String |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Specifies the challenge password for Certificate Authority (CA) authorization against the phone during a certificate enrollment
                              via SCEP. |
| Phone Model | All MPP phones |
| Labels | Certificate |

| XML Tag Name | CDC_Root_CA_Fingerprint_1_ Example: <CDC_Root_CA_Fingerprint_1_ ua="na">12040870625C5B755D73F5925285F8F5FF5D55AF</CDC_Root_CA_Fingerprint_1_> |
|---|---|
| Web Parameter | Root CA Fingerprint |
| Default Value | N/A |
| Allowed Values | String |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Specifies the SHA256 or SHA1 fingerprint of the Root CA for validation during the SCEP process. When the SCEP parameters are
                              configured correctly, the phone sends requests to the SCEP server, and the CA certificate is validated by device using the
                              defined fingerprint. |
| Phone Model | All MPP phones |
| Labels | Certificate |

| XML Tag Name | CDC_Server_1_ Example: <CDC_Server_1_ ua="na">http://10.79.57.91</CDC_Server_1_> |
|---|---|
| Web Parameter | Server |
| Default Value | N/A |
| Allowed Values | String |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Specifies an SCEP server address when automatically installing the Custom Device Certificate (CDC). When the SCEP parameters
                              are configured correctly, the phone sends requests to the SCEP server, and the CA certificate is validated by device using
                              the defined fingerprint. |
| Phone Model | All MPP phones |
| Labels | Certificate |

| XML Tag Name | Certificate_Select Example: <Certificate_Select ua="rw">Custom installed</Certificate_Select> |
|---|---|
| Web Parameter | Certificate Select |
| Default Value | Manufacturing installed |
| Allowed Values | Option list: Manufacturing installed\|Custom installed |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in user level, honored with ua=rw. Available on LCD UI. |
| Description | Select a certificate (MIC or custom) for the 802.1X authentication. |
| Phone Model | All MPP phones |
| Labels | System |

| XML Tag Name | <Connect_on_Bootup> Example: <Connect_on_Bootup ua="rw">No</Connect_on_Bootup> |
|---|---|
| Web Parameter | Connect on Bootup |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Controls whether to connect to the specified VPN server automatically after the phone reboots. |
| Phone Model | All MPP phones except 6821, 7832, and 8832 |
| Labels | VPN |

| XML Tag Name | Control_Server_URL Example: <Control_Server_URL ua="na"/> In the phone web page enter the URL of a WebSocket server. <Control_Server_URL>wss://my-server.com
/ws-server-path</Control_Server_URL> |
|---|---|
| Web Parameter | Control Server URL |
| Default Value | Empty |
| Allowed Values | URL |
| Units | URL |
| Limits | URL |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | The URL of a WebSocket server to which the phone attempts to stay
                              								connected. URL should be in one of the following formats: For a nonsecure HTTP connection: ws://your-server-name/path For a secure HTTPS connection: wss://your-server-name/some-path We recommend a secure connection. |
| Phone Model | All MPP phones |
| Labels | Remote SDK |

| XML Tag Name | Customizable_PLK_Options Example: <Customizable_PLK_Options ua="na">mwi;sd;blf;shortcut;dnd;</Customizable_PLK_Options> Example: sd;blf;cp;dnd;acd;callinfo Example: proxycall;callpush;callretrieve;divert;bridgein |
|---|---|
| Web Parameter | Customizable PLK Options |
| Default Value | sd |
| Allowed Values | dnd\|acd\|callinfo\|calllist\|cfwd\|lcr\|proxycall\|callpush\|callretrieve\|divert\|bridgein\|shortcut |
| Units | String without units |
| Limits | String Length range is 0 to 511 |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enables users to configure features on the line keys. |
| Phone Model | All MPP phones |
| Labels | Att Console |

| XML Tag Name | Device_Administration Example: <Device_Administration ua="na">Yes</Device_Administration> |
|---|---|
| Web Parameter | Device Administration |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available as Device administration on the LCD UI. |
| Description | Controls whether to show the Device
                                 									administration menu on the phone screen. Set this
                              								field to Yes to show the menu. Otherwise, set
                              								it to No . |
| Phone Model | All MPP phones |
| Labels | Phone Menu Visibility |

| XML Tag Name | Device_Config_Version Example: <Device_Config_Version ua="na">2021-01-05-v1</Device_Config_Version> |
|---|---|
| Web Parameter | N/A |
| Default Value | Empty |
| Allowed Values | Any string |
| Units | String without units |
| Limits | 0–64 characters |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI and the phone web page. |
| Description | Customizes the product configuration version that shows as the menu item Configuration version on the phone screen Product information . If the tag doesn't exist in the cfg.xml file or the parameter value is empty, the menu item doesn't display on the phone screen. |
| Phone Model | All MPP phones |
| Labels | Phone Menu |

| XML Tag Name | Disable_DF Example: <Disable_DF ua="na">Yes</Disable_DF> |
|---|---|
| Web Parameter | Disable DF |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether an IP packet can be fragmented. When the parameter is set to Yes , the Don't Fragment (DF) bit is disabled. In this case, the network can fragment an IP packet. This is the default behaviour. When the parameter is set to No , the Don't Fragment (DF) bit is enabled. In this case, the network can't fragment an IP packet. This setting doesn't allow
                              fragmentation in cases where the receiving host doesn't have sufficient resources to reassemble internet fragments. |
| Phone Model | All models |
| Labels | Network Settings |

| XML Tag Name | Display_Off_Idle_Timeout__mins_ Example: <Display_Off_Idle_Timeout__mins_ ua="na" um="y">1</Display_Off_Idle_Timeout__mins_> |
|---|---|
| Web Parameter | Idle Timeout (mins) |
| Default Value | 5 |
| Allowed Values | 1 to 60 |
| Units | Minutes |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Set the timeout period in minutes for the phone to automatically turn off the screen after being awakened from the Display
                              Off Mode. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | Display_Password_Warnings Example: <Display_Password_Warnings ua="na">Yes</Display_Password_Warnings> |
|---|---|
| Web Parameter | Display Password Warnings |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Options |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Specifies whether to show password alerts on the phone and the web page. |
| Phone Model | Supported by all phones |
| Labels | System |

| XML Tag Name | Disable_Side_USB_Port Example: <Disable_Side_USB_Port ua="na">No</Disable_Side_USB_Port> |
|---|---|
| Web Parameter | Disable Side USB Port |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether to disable or enable the side USB port on the phone (if the phone has this port). When the side USB port is disabled, it doesn't work on the phone. And it doesn't charge the connected device. |
| Phone Model | Supported by 8851, 8861, and 8865 |
| Labels | Power Settings |

| XML Tag Name | Display_Recents_From Example: <Display_Recents_From ua="na">Phone</Display_Recents_From> |
|---|---|
| Web Parameter | Display Recents From |
| Default Value | Phone |
| Allowed Values | Option list: Phone\|XSI Server\|Webex |
| Units | String without units |
| Limits | Options |
| User or Admin | Exposed in admin level, which is honored with ua = na. Not available on LCD UI. |
| Description | Sets the source of recent call histories that the phone retrieves from. This parameter is associated with the parameter CallLog Enable . When CallLog Enable is set to Yes , the phone can display the Display recents from field in the Recents screen. The user can select the source of the call histories through the Display recents from field. The Webex option from the Display recents from field displays only when the phone connects to the Webex. |
| Phone Model | All MPP phones supports options XSI Server and Phone. Option Webex is only supported by onlyrted 8800 Series and 8832 |
| Labels | Calls |

| XML Tag Name | Display_XMPP_User_ID_With_Top_Priority Example: <Display_XMPP_User_ID_With_Top_Priority ua="na">Yes</Display_XMPP_User_ID_With_Top_Priority> |
|---|---|
| Web Parameter | Display XMPP User ID With Top Priority |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Displays the XMPP user ID with the highest priority at the top left of the phone screen. If enabled, the XMPP user ID overrides other display names, for example, Station Name. |
| Phone Model | Supported by 8800 Series |
| Labels | Directory |

| XML Tag Name | Divert_Off_LED Example: <Divert_Off_LED ua="na">c=r</Divert_Off_LED> |
|---|---|
| Web Parameter | Divert Off LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | The LED color and cadence when the Divert PLK indicates that the selected line's divert
                              								state is Off . It will follow the LED Pattern which is defined
                              								by customers. The LED Pattern Format is c=<COLOR> [;
                              								p=<PATTERN>]. c is mandatory and p is optional where default
                              								behavior is "no blink with solid color" if it is not specified. |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | Att Console |

| XML Tag Name | DND_Off_LED |
|---|---|
| Web Parameter | DND Off LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | Turns off the DND LED pattern on the phone screen. |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | Calls |

| XML Tag Name | DND_On_LED Example: <DND_On_LED ua="na">c=r</DND_On_LED> |
|---|---|
| Web Parameter | DND On LED |
| Default Value | Empty |
| Allowed Values | COLOR (c)g = GREENr = REDa = AMBERo = OFFWhen you set COLOR to OFF,
                              								PATTERN is ignored even if you set it. PATTERN (p)b = Blink with a ColorThis is equivalent to the system
                              								default of Slow Blink.n = No Blink, Solid Color Examples: LED = Solid Red User Input = c=r; p=n c=r LED = Blinking Amber User Input = c=a; p=b LED = OFF User Input = c=o Refer to "Color-Pattern Key" and "Sample LED Configurations" in the
                              								Admin Guides. |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Available on LCD
                              								UI. |
| Description | The LED color and cadence when the DND PLK indicates that the selected line's DND is On . It will follow the LED Pattern which is defined by
                              								customers. The LED Pattern Format is c=<COLOR> [;
                              								p=<PATTERN>]. c is mandatory and p is optional where default
                              								behavior is "no blink with solid color" if it is not specified. |
| Phone Model | All 68xx, 78xx, 88xx, phones except 7832 and 8832 |
| Labels | Att Console |

| XML Tag Name | Enable_802.1X_Authentication Example: <Enable_802.1X_Authentication ua="rw">Yes</Enable_802.1X_Authentication> |
|---|---|
| Web Parameter | Enable 802.1X Authentication |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in user level, honored with ua=rw. Available on LCD UI. |
| Description | Enables 802.1X authentication on the phone. When 802.1X authentication is enabled, the phone uses 802.1X authentication to request network access.When 802.1X authentication
                              is turned off, the phone uses CDP to acquire VLAN and network access. |
| Phone Model | All MPP phones |
| Labels | System |

| XML Tag Name | Enable_Direct_PLK_Configuration Example: <Enable_Direct_PLK_Configuration ua="na">Yes</Enable_Direct_PLK_Configuration> |
|---|---|
| Web Parameter | Enable Direct PLK Configuration |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether the extension of a line key must be disabled to apply the Programmable Line Key (PLK) configuration. Before the 11.3(7) release, you must disable the extension of a line key to apply the PLK configuration. If the parameter is set to Yes , you can skip disabling the extension of a line key, and you can directly configure the PLK on a line key. If the parameter is set to No , you still need to disable the extension of a line key to apply the PLK configuration. To make this feature take effect, ensure that the <Proxy_ n _> and <User_ID_ n _> are empty, where n is the extension number of the line key. Note The Direct PLK Configuration feature on a certain line key doesn't work in the following situations: <Make_Call_Without_Reg_ n _> is Yes , where n is the extension number of the line key. <Bluetooth_Mode> is Handsfree or Both , and <Line> is configured with a number. For example, <Line> is 2 . In this case, the feature doesn't work on the line key with the extension number 2. The Direct PLK | Note | The Direct PLK Configuration feature on a certain line key doesn't work in the following situations: <Make_Call_Without_Reg_ n _> is Yes , where n is the extension number of the line key. <Bluetooth_Mode> is Handsfree or Both , and <Line> is configured with a number. For example, <Line> is 2 . In this case, the feature doesn't work on the line key with the extension number 2. |
| Note | The Direct PLK Configuration feature on a certain line key doesn't work in the following situations: <Make_Call_Without_Reg_ n _> is Yes , where n is the extension number of the line key. <Bluetooth_Mode> is Handsfree or Both , and <Line> is configured with a number. For example, <Line> is 2 . In this case, the feature doesn't work on the line key with the extension number 2. |
| Phone Model | All MPP phones except 7811, 7832, and 8832 |
| Labels | Line Key |

| Note | The Direct PLK Configuration feature on a certain line key doesn't work in the following situations: <Make_Call_Without_Reg_ n _> is Yes , where n is the extension number of the line key. <Bluetooth_Mode> is Handsfree or Both , and <Line> is configured with a number. For example, <Line> is 2 . In this case, the feature doesn't work on the line key with the extension number 2. |
|---|---|

| XML Tag Name | Enable_Protocol Example: <Enable_Protocol ua="na">Https</Enable_Protocol> |
|---|---|
| Web Parameter | Enable Protocol |
| Default Value | Https |
| Allowed Values | Option list: Https\|Http |
| Units | Options |
| Limits | Options |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Enables https by default to access the phone administration web page. |
| Phone Model | Supported by all phones |
| Labels | System |

| XML Tag Name | Executive_Assistant_Role Example: <Executive_Assistant_Role ua="na">Default</Executive_Assistant_Role> |
|---|---|
| Web Parameter | Executive Assistant Role |
| Default Value | Default |
| Allowed Values | Option list: Default\|Executive\|Assistant |
| Units | Options without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Preassigns the executive-assistant role to a phone extension. This preassignment doesn't directly determine the executive-assistant role of the phone. Both the preassignments on the extensions
                              and the role settings by the BroadWorks server determine the executive-assistant role of the phone. |
| Phone Model | Supported by 6871 and 8800 Series (not including 8832) |
| Labels | Executive Assistant |

| XML Tag Name | Extended_Function_n_ n is the extension number of the phone. Call park to a line key For a private line, enter nc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1 For a shared line, enter fnc=prk;sub=$USER@$PROXY;nme=Call-Park1;orbit=<DN of primary line> You can configure this feature on the line key on which Extension is disabled . where: fnc= prk means function=call park sub= 999999 is the phone to which the call parks. Replace 999999
                                 									with a numbers. nme= XXXX is the name displayed on the phone for the call park
                                 									line key. Replace XXXX with a name. Example: <Extended_Function_2_
ua="na">fnc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1</Extended_Function_2_> A line key as a phone menu shortcut Example: <Extended_Function_1_ ua="na">fnc=shortcut;url=userpref;nme=User
Preferences</Extended_Function_1_> |
|---|---|
| Web Parameter | Extended Function |
| Default Value | Empty |
| Allowed Values | String, the well-formated one is "fnc=type(;name=value)*", where * means zero or more
                                 									repeats |
| Units | String without units |
| Limits | String Length: 0 to 511 |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available
                                 									on LCD UI. |
| Description | Adds extended functions to a line key. |
| Phone Model | All MPP phones |
| Labels | Line key |

| XML Tag Name | Extension_n_ n is the extension number of the phone. Example: <Extension_1_ ua="na">Disabled</Extension_1_> |
|---|---|
| Web Parameter | Extension |
| Default Value | n where n is the extension (1-10) assigned to a line key. |
| Allowed Values | Drop-down list: n\|Disabled where n is the extension (1to10) assigned to a line key. |
| Units | Options with integer and string. |
| Limits | Options |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								the LCD UI. |
| Description | Specifies the n extension to be assigned to Line Key n. |
| Phone Model | All MPP phones |
| Labels | Line Key |

| XML Tag Name | EXT_SIP_Port Example: <EXT_SIP_Port_1_ua="na">5060</EXT_SIP_Port_1_> |
|---|---|
| Web Parameter | EXT SIP Port |
| Default Value | 5060 |
| Allowed Values | Integer (0-9), String |
| Units | Integer |
| Limits | 0 to 65535 |
| User or Admin | Admin |
| Description | The external SIP port number. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | Factory_Reset_Menu Example: <Factory_Reset_Menu ua="na">Yes</Factory_Reset_Menu> |
|---|---|
| Web Parameter | Factory Reset Menu |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin |
| Description | Specifies if the user requires authentication to access Factory
                                 									reset menu on the phone. This parameter can be customized to Yes or No only when the Require
                                    										Authentication for LCD Menu Access parameter is
                                 									set to Customized . |
| Phone Model | All MPP phones |
| Labels | User Authentication Control for Phone menus |

| XML Tag Name | Feature_Activation_Code_Sync Example: <Feature_Activation_Code_Sync_n_ ua="na">Yes</Feature_Activation_Code_Sync_n_> where n is the extension number. |
|---|---|
| Web Parameter | Feature Activation Code Sync |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enable or disable sending FAC code to server when dial vertical
                              								activation code. |
| Phone Model | All MPP phones |
| Labels | Call Feature setting |

| XML Tag Name | FIPS_Mode Example: <FIPS_Mode>Disabled</FIPS_Mode> |
|---|---|
| Web Parameter | FIPS Mode |
| Default Value | Disabled |
| Allowed Values | Disabled\|Enabled |
| Units | Options without units |
| Limits | Options |
| User or Admin | Admin level only. Not available on LCD UI. |
| Description | Enables CiscoSSL FIPS mode when Enabled is selected. |
| Phone Model | All MPP phones |
| Labels | System |

| XML Tag Name | Firewall Example: <Firewall ua="na">Enabled</Firewall> |
|---|---|
| Web Parameter | Firewall |
| Default Value | Enabled |
| Allowed Values | Option list: Disabled\|Enabled |
| Units | Options without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. ua=na |
| Description | Improves phone security by by hardening the operating system. Tracks
                              								the ports for incoming and outgoing data. It detects incoming
                              								traffic from unexpected sources and blocks the access. Your firewall
                              								allows all outgoing traffic. |
| Phone Model | All MPP phones |
| Labels | Security |

| XML Tag Name | Firewall_Config Example: <Firewall_Config ua="na">NO_ICMP_PING</Firewall_Config> |
|---|---|
| Web Parameter | Firewall Options |
| Default Value | Empty |
| Allowed Values | String NO_ICMP_PING, NO_ICMP_UNREACHABLE, NO_CISCO_TFTP The following keywords and options apply when the phone runs custom
                              								apps that handle incoming requests. UDP:<xxx>, UDP:<xxx:yyy>, TCP:<xxx>, TCP:<xxx:yyy> |
| Units | String without units |
| Limits | String |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. ua=na |
| Description | Configures additional options in the Firewall Options field.
                              								Type the keyword for each option in the field, and separate the
                              								keywords by commas (,). Some keywords have values. Separate the
                              								values by colons (:). |
| Phone Model | All MPP phones |
| Labels | Security |

| XML Tag Name | Font_Size Example: <Font_Size ua="rw">Large</Font_Size> |
|---|---|
| Web Parameter | Font Size |
| Default Value | Regular |
| Allowed Values | Option list: Regular\|Large |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Available on LCD UI. |
| Description | Controls the size of the fonts that are displayed on the phone screen. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | <Forced_NAT64> Example: <Forced_NAT64>Yes</Forced_NAT64> |
|---|---|
| Web Parameter | Forced NAT64 |
| Default Value | No |
| Allowed Values | Yes \| No |
| Units | N/A |
| Limits | Yes \| No |
| User or Admin | Admin level only |
| Description | Sets the web parameter for Forced NAT64. Takes effect after a warm reboot. |
| Phone Model | All MPP phones |
| Labels | NAT64 |

| XML Tag Name | Forward_Softkey Example: <Forward_Softkey ua="na">All Cfwds</Forward_Softkey> |
|---|---|
| Web Parameter | Forward Softkey |
| Default Value | All Cfwds |
| Allowed Values | Option list: All Cfwds\|Only the Cfwd All |
| Units | String without units |
| Limits | Options |
| User or Admin | Exposed in admin level, which is honored with ua = na. Not available on LCD UI. |
| Description | Allows the user to set up all call forward services or only the Call Forward All service by a specific softkey. Options are: All Cfwds : The user can set up all call forward services, including Call Forward All, Call Forward Busy, and Call Forward No Answer
                                    by a specific softkey. In this setting, the softkey is Forward . After the user sets up any of the call forward services, the softkey changes to Clf fwd . And the user can disable all call forward services by pressing it. Only the Cfwd All : The user can only set up the Call Forward All service by a specific softkey. In this setting, the softkey is Forward all . After the user sets up the Call Forward All service, the softkey changes to Clf fwd all . And the user can disable the Call Forward All service by pressing it. |
| Phone Model | All MPP phones |
| Labels | UI/CCTRL |

| XML Tag Name | Group_1_Paging_Script n is the group ID (1-10) Example: <Group_1_Paging_Script ua="na">pggrp=224.168.168.168:34560;name=Group_1;
num=800;listen=yes;pri=1;codec=g722</Group_1_Paging_Script> |
|---|---|
| Web Parameter | Group n Paging Script |
| Default Value | pggrp=224.168.168.168:34560;name=All;num=800;listen=yes; |
| Allowed Values | String |
| Units | String |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | A string to configure the phone to listen for and initiate multicast
                              								paging. You can add a phone to up to 10 paging groups. |
| Phone Model | All MPP phones |
| Labels | Multiple paging |

| XML Tag Name | ice_stun_enable Example: <ice_stun_enable>Yes</ice_stun_enable> |
|---|---|
| Web Parameter | N/A |
| Default Value | No |
| Allowed Values | Option list Yes\|No |
| Units | Boolean without units |
| Limits | Boolean/Option |
| User or Admin | Exposed in admin level through xml configuration file (Webex Calling
                              								Server). Honored with ua = rw/ro/na. Not available on the LCD
                              								UI. |
| Description | Optimizes media path for calls. |
| Phone Model | All MPP phones |
| Labels | NAT |

| XML Tag Name | Idle_Key_List Example: <Idle_Key_List
ua="rw">psk2;em_login;acd_login;acd_logout;astate;redial;cfwd;dnd;lcr;</Idle_Key_List> |
|---|---|
| Web Parameter | Idle Key List |
| Default Value | N/A |
| Allowed Values |  |
| Units | N/A |
| Limits | N/A |
| User or Admin | Admin |
| Description | Programmable softkey fields. Enter a string in these fields to
                                 									configure softkeys that display on the phone screen. You can
                                 									create softkeys for speed dials to numbers or extensions,
                                 									vertical service activation codes (* codes), or XML. Configure
                                 									the PSKs in this format: Speed Dial: fnc=sd;ext=extension_number@$PROXY;vid=n;nme=display_name Vertical Service Activation Code: fnc=sd;ext=star_code@$PROXY;vid=n;nme=display_name XML Service: fnc=xml;url=http://server_IP/services.xml;vid=n;nme=display_name Menu shortcut: fnc=shortcut;url=userpref;nme=User preferences When you add a programmable softkey to a softkey list, such as
                                 									Idle Key List, Missed Call Key List, and so on, the programmable
                                 									softkey displays on the phone screen. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string
                                 									in this format: <PSK_1 ua="na">fnc=xml;url=http://server_IP/services.xml;vid=n; nme=display_name</PSK_1 ua="na"> In the phone web interface, set the PSKs in the valid format or
                                 									scripts. |
| Phone Model | All MPP phones |
| Labels | PSK |

| XML Tag Name | Keep_Focus_On_Active_Call Example: <Keep_Focus_On_Active_Call ua="na">Yes</Keep_Focus_On_Active_Call> |
|---|---|
| Web Parameter | Keep Focus On Active Call |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether to keep the focus on the active call on the phone screen when the phone receives an incoming call. Yes : When a user is on an active call and receives one or more incoming calls, the focus still remains on the active call. However, if the user places the active call on hold, the focus automatically moves from the active call to the incoming call.
                                       If there are multiple incoming calls, the focus always moves to the first one. No : When a user is on an active call and receives an incoming call, the focus automatically moves from the active call to the
                                    incoming call. |
| Phone Model | All MPP phones |
| Labels | Calls |

| XML Tag Name | Key_Again_Reset_Time Example: <Key_Again_Reset_Time ua="rw">1200</Key_Again_Reset_Time> |
|---|---|
| Web Parameter | Key Again Reset Time |
| Default Value | 1200 |
| Allowed Values | 100 to 2000 |
| Units | Milliseconds |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Not available on LCD UI. |
| Description | Sets the reset time required for performing a key double or triple press again. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | Key_Double_Press_Time Example: <Key_Double_Press_Time ua="rw">600</Key_Double_Press_Time> |
|---|---|
| Web Parameter | Key Double Press Time |
| Default Value | 600 |
| Allowed Values | 100 to 2000 |
| Units | Milliseconds |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Not available on LCD UI. |
| Description | Sets the maximum delay time for a key double press to perform a named function on the phone. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | Key_Triple_Press_Time Example: <Key_Triple_Press_Time ua="rw">1000</Key_Triple_Press_Time> |
|---|---|
| Web Parameter | Key Triple Press Time |
| Default Value | 1000 |
| Allowed Values | 100 to 2000 |
| Units | Milliseconds |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Not available on LCD UI. |
| Description | Sets the maximum delay time for a key triple press to enable or disable the voice feedback feature on the phone. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | LED_Indicator_In_Display_Off_Mode Example: <LED_Indicator_In_Display_Off_Mode ua="na">Enabled</LED_Indicator_In_Display_Off_Mode> |
|---|---|
| Web Parameter | LED Indicator In Display Off Mode |
| Default Value | Enabled |
| Allowed Values | Option list: Enabled\|Disabled |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Determines whether to turn off the backlight of the Select button in the Navigation cluster when the phone enters the Display Off Mode. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | LDAP_StartTLS_Enable Example: <LDAP_StartTLS_Enable ua="na">Yes</LDAP_StartTLS_Enable> |
|---|---|
| Web Parameter | StartTLS Enable |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | StartTLS Enable = Yes : If Ldap_server is ldap://server:port , then phone will start to
                                    										send Start_TLS request. If Ldap_server is ldaps://server:port , then phone will keep LDAPs
                                    										and will ignore this parameter. StartTLS Enable = No : Phone will keep the existing
                                    										behavior. |
| Phone Model | All MPP phones |
| Labels | LDAP |

| XML Tag Name | LDAP_Prompt_For_Empty_Credentials Example: <LDAP_Prompt_For_Empty_Credentials ua="na">Yes</LDAP_Prompt_For_Empty_Credentials> where n is the extension number. |
|---|---|
| Web Parameter | N/A |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Hidden. Not available on LCD UI. ua=na |
| Description | Enable or disable the LDAP sign-in prompt when there’s no user
                              								credential on the phone. This function is used only for the simple
                              								authentication method that involves the anonymous simple bind
                              								operation. |
| Phone Model | All MPP phones |
| Labels | LDAP |

| XML Tag Name | LDAP_Unified_Search_Enable Example: <LDAP_Unified_Search_Enable>Yes</LDAP_Unified_Search_Enable> |
|---|---|
| Web Parameter | Unified Search Enable |
| Default Value | No |
| Allowed Values | Yes/No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed only in the phone web page for admin. |
| Description | When the parameter is set to Yes , it enables the unified search for the LDAP directory. |
| Phone Model | All MPP phones |
| Labels | Phone |

| XML Tag Name | Max_Display_Records Example: <Max_Display_Records ua="na">50</Max_Display_Records> |
|---|---|
| Web Parameter | Max Display Records |
| Default Value | 50 |
| Allowed Values | 50 to 999 |
| Units | Record number |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Maximum display records for a directory. |
| Phone Model | All MPP phones except 7811 and 7832 |
| Labels | Directory |

| XML Tag Name | MediaSec_Request_n_ where n is the extension number (1 to 16) of the phone Example: <MediaSec_Request_1_ ua="na">Yes</MediaSec_Request_1_> |
|---|---|
| Phone Web Parameter | MediaSec Request |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI |
| Description | Specifies whether the phone initiates media plane security
                              								negotiation with the server. Yes—The phone initiates media plane security negotiations. No—The phone doesn't initiate negotiations but can handle
                                    										negotiation requests from the server. |
| Phone Model | All models |
| Labels | SIP |

| XML Tag Name | MediaSec_Over_TLS_Only_n_ n is the extension number of the phone. Example: <MediaSec_Over_TLS_Only_1_ ua="na">No</MediaSec_Over_TLS_Only_1_> |
|---|---|
| Web Parameter | MediaSec Over TLS Only |
| Default Value | No |
| Allowed Values | Options: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Specifies the signaling transport protocol over which media plane
                              								security negotiation is applied. Before setting this field to Yes , ensure that the signaling
                              								transport protocol is TLS. |
| Phone Model | All MPP phones |
| Labels | Security |

| XML Tag Name | N/A |
|---|---|
| Web Parameter | MIC Cert Info |
| Default Value | N/A |
| Allowed Values | N/A |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for both user and admin. Not available on LCD UI. |
| Description | Shows the overall status of the MIC certificate renewal procedure. For example, Renewed or Not Renewed . |
| Phone Model | All MPP phones |
| Labels | Secure |

| XML Tag Name | N/A |
|---|---|
| Web Parameter | MIC Cert Provisioning Status |
| Default Value | N/A |
| Allowed Values | N/A |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for both user and admin. Not available on LCD UI. |
| Description | Shows the status of the Manufacture Installed Certificate (MIC) certificate to see whether the SUDI server has renewed the
                              certificate successfully. This parameter contains the following information: Date and time of the last renewal Request URL to the SUDI service Result message (success or failure) The information shows in this format: <time><url><result message> |
| Phone Model | All MPP phones |
| Labels | Secure |

| XML Tag Name | MIC_Cert_Refresh_Enable Example: <MIC_Cert_Refresh_Enable ua="na">Yes</MIC_Cert_Refresh_Enable> |
|---|---|
| Web Parameter | MIC Cert Refresh Enable |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether to enable the MIC certificate renewal procedure. |
| Phone Model | All MPP phones |
| Labels | Secure |

| XML Tag Name | MIC_Cert_Refresh_Rule Example: <MIC_Cert_Refresh_Rule ua="na">http://hostname.cisco.com/</MIC_Cert_Refresh_Rule> |
|---|---|
| Web Parameter | MIC Cert Refresh Rule |
| Default Value | http://sudirenewal.cisco.com/ |
| Allowed Values | URL |
| Units | URL |
| Limits | URL |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | HTTP URL for requesting the renewed MIC certificate from the SUDI server. Note Currently, only the default URL can be used for the MIC certificate renewal. | Note | Currently, only the default URL can be used for the MIC certificate renewal. |
| Note | Currently, only the default URL can be used for the MIC certificate renewal. |
| Phone Model | All MPP phones |
| Labels | Secure |

| Note | Currently, only the default URL can be used for the MIC certificate renewal. |
|---|---|

| XML Tag Name | Office_Hours_Enabled Example: <Office_Hours_Enabled ua="na" um="y">True</Office_Hours_Enabled> |
|---|---|
| Web Parameter | Office Hours Enabled |
| Default Value | False |
| Allowed Values | Option list: True\|False |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Enables Office Hours. When enabled, the phone automatically enters Display Off Mode and turns off the screen to save power
                              outside of the designated working hours. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | PAC_URL Example: <PAC_URL ua="rw">http://proxy.department.branch.example.com/pac</PAC_URL> |
|---|---|
| Web Parameter | PAC URL |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | Maximum of 511 characters |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | The URL that instructs the phone to retrieve a Proxy Auto-Configuration (PAC) file. TFTP, HTTP, and HTTPS are supported. The parameter configuration takes effect when the Proxy Mode is Auto and Use Auto Discovery (WPAD) is set to No . For details, see Proxy_Mode and Use_Auto_Discovery__WPAD_ . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | Peripheral_Inventory_Enable Example: <Peripheral_Inventory_Enable ua="na">Yes</Peripheral_Inventory_Enable> |
|---|---|
| Web Parameter | Peripheral Inventory Enable |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Enables the phone to report the connected or disconnected peripheral information to the server. When the parameter is set to Yes , the peripheral inventory headers are included in the SIP Register message. When set to No , the headers are not included in the SIP message. When one peripheral is connected or disconnected to the phone, next scheduled Register provides the peripheral information
                                 in the Peripheral-Data header. All subsequent Registers do not carry peripheral information. The Peripheral-Data header is
                                 included for each peripheral, for example, if there are two headsets present, the header appears twice. |
| Phone Model | Supported by 6851, 6871, and 8800 Series (not including 8832) |
| Labels | SIP |

| XML Tag Name | Personal_Directory_Enable Example: <Personal_Directory_Enable
ua="na">Yes</Personal_Directory_Enable> |
|---|---|
| Web Parameter | Personal Directory Enable |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Enables the personal address book directory for the phone
                                 									user. When you disable the directory, users can't search contacts from their personal address
                                       											book users can't add a contact in their personal address
                                       											book |
| Phone Model | All MPP phones |
| Labels | Directory Services |

| XML Tag Name | Precondition_Support_n_ n is the extension number of the phone. Example: <Precondition_Support_1_ua="na">Enabled</Precondition_Support_1_> |
|---|---|
| Web Parameter | Precondition Support |
| Default Value | Disabled |
| Allowed Values | Option list: Disabled\|Enabled |
| Units | Options without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Determines whether the phone includes the precondition tag (defined in RFC 3312) in the Supported header field. Disabled :  The phone doesn't include the precondition tag in the Supported header filed. And the phone doesn't return the 183 response
                                    when it receives the INVITE request that contains the QoS precondition in the SDP description. Enabled : The phone includes the precondition tag in the Supported header field. |
| Phone Model | All MPP phones |
| Labels | SIP Settings |

| XML Tag Name | Programmable_Softkey_Enable Example: <Programmable_Softkey_Enable ua="rw">Yes</Programmable_Softkey_Enable> |
|---|---|
| Web Parameter | Programmable Softkey Enable |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin |
| Description | Enables or disables the programmable softkeys. Set this field to Yes to enable the
                                 									programmable softkeys. |
| Phone Model | All MPP phones |
| Labels | PSK |

| XML Tag Name | Profile_Rule_Menu Example: <Profile_Rule_Menu ua="na">Yes</Profile_Rule_Menu> |
|---|---|
| Web Parameter | Profile Rule Menu |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin |
| Description | Specifies if the user requires authentication to access Profile
                                 									rule menu on the phone. You can customize this parameter to Yes or No only when you set
                                 									the Require Authentication for LCD Menu
                                    										Access parameter to Customized . |
| Phone Model | All MPP phones |
| Labels | User authentication to phone menus |

| XML Tag Name | Proxy_Fallback_Intvl Example: <Proxy_Fallback_Intvl_n_ ua="na">60</Proxy_Fallback_Intvl_n_> n is the extension number. |
|---|---|
| Web Parameter | Proxy Fallback Intvl |
| Default Value | N/A |
| Allowed Values |  |
| Units | Seconds |
| Limits | N/A |
| User or Admin | Admin |
| Description | The proxy failback requires a value other than zero specified in
                                 									the Proxy Fallback Intvl field on the Ext (n) tab in the phone
                                 									web interface. If you set this field to 0, the SIP proxy
                                 									failback feature is disabled. The time when the phone triggers a failback depends on the phone
                                 									configuration and the SIP transport protocols in use. To enable the phone to perform failback between different SIP
                                 									transport protocols, set SIP Transport to Auto on the Ext (n)
                                 									tab in the phone web interface. You can also configure this
                                 									extension-specific parameter in the configuration file with the
                                 									following XML string: <SIP_Transport_n_ ua="na">Auto</SIP_Transport_n_> where n is the extension number. |
| Phone Model | All MPP phones |
| Labels |  |

| XML Tag Name | Proxy_Host Example: <Proxy_Host ua="rw">proxy.example.com</Proxy_Host> |
|---|---|
| Web Parameter | Proxy Host |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | Maximum of 255 characters |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Specifies an IP address or hostname of the proxy host server that the phone uses. For example: proxy.example.com The scheme ( http:// or https:// ) is not required. The parameter configuration is required if the Proxy Mode is set to Manual . For details, see Proxy_Mode . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | Proxy_Mode Example: <Proxy_Mode ua="rw">Off</Proxy_Mode> |
|---|---|
| Web Parameter | Proxy Mode |
| Default Value | Off |
| Allowed Values | Auto\|Manual\|Off |
| Units | Options without units |
| Limits | Option |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Determines which proxy mode that the phone uses or to disable the HTTP proxy feature on the phone. Options are: Auto : In this mode, the phone retrieves a Proxy Auto-Configuration (PAC) file that defines how to automatically choose an appropriate
                                       proxy server. This mode contains the following methods: Web Proxy Auto-Discovery (WPAD): Uses DHCP server or DNS Service Discovery, or both to automatically retrieve a PAC file. Proxy Auto-Configuration (PAC) URL: Specifies a PAC URL that can locate to a PAC file. Manual : In this mode, the user needs to manually specify a proxy server (a hostname or IP address) and a proxy port. If the proxy
                                       server requires authentication, then the user needs to further enter the username and password to access the server. Off : The HTTP proxy feature is disabled on the phone. |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | Proxy_Password Example: <Proxy_Password ua="rw">Example</Proxy_Password> |
|---|---|
| Web Parameter | Password |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | N/A |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Provides the password of the specified username that the proxy server requires. The parameter configuration is required when Proxy Mode is set to Manual and Proxy Server Requires Authentication is set to Yes . For details, see Proxy_Mode and Proxy_Server_Requires_Authentication . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | Proxy_Port Example: <Proxy_Port ua="rw">3128</Proxy_Port> |
|---|---|
| Web Parameter | Proxy Port |
| Default Value | 3128 |
| Allowed Values | Integer (0-9), String |
| Units | Integer |
| Limits | 0 to 65535 |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Specifies a port number of the proxy host server that the phone uses. The parameter configuration is required if the Proxy Mode is set to Manual . For details, see Proxy_Mode . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | Proxy_Server_Requires_Authentication Example: <Proxy_Server_Requires_Authentication ua="rw">No</Proxy_Server_Requires_Authentication> |
|---|---|
| Web Parameter | Proxy Server Requires Authentication |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Selects the option according to the actual behaviour of the proxy server. If the proxy server requires the user to provide
                                 authentication credentials, select Yes . Otherwise, select No . If the parameter is set to Yes , the proxy server requires username and password to grant the access right. For details, see Proxy_Username and Proxy_Password . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | Proxy_Username Example: <Proxy_Username ua="rw">Example</Proxy_Username> |
|---|---|
| Web Parameter | Username |
| Default Value | Empty |
| Allowed Values | String |
| Units | Strings without units |
| Limits | N/A |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Specifies a username for the authentication purpose of the proxy server. The parameter configuration is required when Proxy Mode is set to Manual and Proxy Server Requires Authentication is set to Yes . For details, see Proxy_Mode and Proxy_Server_Requires_Authentication . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | PRT_HTTP_Header Example: <PRT_HTTP_Header ua="na">x-cisco-spark-canary-opts</PRT_HTTP_Header> |
|---|---|
| Web Parameter | PRT HTTP Header |
| Default Value | Empty |
| Allowed Values | a-z, A-Z, 0-9, underscore (_), and hyphen (-) |
| Units | N/A |
| Limits | Maximum of 127 characters |
| User or Admin | Admin |
| Description | Specifies the HTTP header for the URL in PRT Upload Rule . The parameter value is associated with PRT HTTP Header Value . Only when both parameters are configured, the HTTP header is included in the HTTP request. |
| Phone Model | All MPP phones |
| Labels | Provisioning |

| XML Tag Name | PRT_HTTP_Header_Value Example: <PRT_HTTP_Header_Value ua="na">always</PRT_HTTP_Header_Value> |
|---|---|
| Web Parameter | PRT HTTP Header Value |
| Default Value | Empty |
| Allowed Values | a-z, A-Z, 0-9, underscore (_), comma (,), semicolon (;), equal (=), and hyphen (-) Note Except for the underscore (_), the first character must not be a special character. | Note | Except for the underscore (_), the first character must not be a special character. |
| Note | Except for the underscore (_), the first character must not be a special character. |
| Units | N/A |
| Limits | 0 or 2–127 characters |
| User or Admin | Admin |
| Description | Sets the value of the specified HTTP header. The parameter value is associated with PRT HTTP Header . Only when both parameters are configured, the HTTP header is included in the HTTP request. |
| Phone Model | All MPP phones |
| Labels | Provisioning |

| Note | Except for the underscore (_), the first character must not be a special character. |
|---|---|

| XML Tag Name | PRT_Upload_at_Crash Example: <PRT_Upload_at_Crash ua="na">Yes</PRT_Upload_at_Crash> |
|---|---|
| Web Parameter | PRT Upload at Crash |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Yes\|No |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | You can indicate whether to automatically upload the PRT package to the server when the phone crashes. |
| Phone Model | Supported by all Series |
| Labels | Directory |

| XML Tag Name | PSK_n n is the PSK ID (1-16) Example: <PSK_1 ua="na">fnc=sd;ext=5014@$PROXY;nme=sktest1</PSK_1> |
|---|---|
| Web Parameter | PSK |
| Default Value | N/A |
| Allowed Values | Integers |
| Units | Integer |
| Limits | 1 to 16 |
| User or Admin | Admin |
| Description | Programmable softkey fields. Enter a string in these fields to
                                 									configure softkeys that display on the phone screen. You can
                                 									create softkeys for speed dials to numbers or extensions,
                                 									vertical service activation codes (* codes), or XML scripts. |
| Phone Model | All MPP phones |
| Labels | PSK |

| XML Tag Name | Register_Expires_n_ Example: <Register_Expires_1_ ua="na">3600</Register_Expires_1_> |
|---|---|
| Web Parameter | Register Expires |
| Default Value | 3600 |
| Allowed Values | Integer (0-9) String |
| Units | Seconds |
| Limits | Integer ranges 0 to 86400 |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available
                                 									on LCD UI. |
| Description | Defines how often the phone renews registration with the proxy.
                                 									If the proxy responds to a REGISTER with a lower expires value,
                                 									the phone renews registration based on that lower value instead
                                 									of the configured value. If registration fails with an “Expires
                                 									too brief” error response, the phone retries with the value
                                 									specified in the Min-Expires header of the error. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | Replace_Unresolved_Caller_Name_with_Number Example: <Replace_Unresolved_Caller_Name_with_Number
ua="na">Yes</Replace_Unresolved_Caller_Name_with_Number> |
|---|---|
| Web Parameter | Replace Unresolved Caller Name with
                                 								Number |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available
                                 									on LCD UI. |
| Description | Controls whether to replace the caller name with the phone number
                                 									when installed font cannot resolve the full caller name. |
| Phone Model | All MPP phones |
| Labels | Locale |

| XML Tag Name | Report_Problem_Menu Example: <Report_Problem_Menu ua="na">Yes</Report_Problem_Menu> |
|---|---|
| Web Parameter | Report Problem |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Controls whether to show the Report problem menu on the phone screen. Set this field to Yes to show the menu. Otherwise, set it
                              								to No . When the Status menu is invisible on the phone, the Report problem menu is invisible as
                              								well. |
| Phone Model | All MPP phones |
| Labels | Phone Menu Visibility |

| XML Tag Name | Require_Authentication_for_LCD_Menu_Access Example: <Require_Authentication_for_LCD_Menu_Access
ua="na">Default</Require_Authentication_for_LCD_Menu_Access> |
|---|---|
| Web Parameter | Require Authentication for LCD Menu
                                 								Access |
| Default Value | Default |
| Allowed Values | Default\|Customized\|No |
| Units | N/A |
| Limits | N/A |
| User or Admin | Admin |
| Description | Controls whether the user requires authentication to access phone
                                 									menus. Default—When selected, user needs to provide password and
                                       											then sign in to access the phone menus that requires
                                       											authentication. Phone continues to support all the
                                       											functionalities that are supported in the releases prior
                                       											to 11.3(2). Phone displays lock screen icon. To access any phone menus that require authentication,
                                       											user needs to provide the password and press Sign in.
                                       											The lock icon remains locked. After the user signs in,
                                       											the lock icon is unlocked. Customized—When selected, user requires authentication
                                       											only to access Profile rule and Factory reset menus on the
                                       											phone. Authenticaion control of these two menus also
                                       											depends on the settings of the Factory Reset
                                          												Menu menu and the Profile
                                          												Rule Menu menu. User will not require
                                       											any authentication to access other phone menus. No—When selected, the Sign in menu, the Sign out menu, the lock
                                       											icon, and the Set password menus
                                       											are not available on the phone. User can access phone
                                       											menus without any authentication. |
| Phone Model | All MPP phones |
| Labels | User Authentication Phone menus |

| XML Tag Name | Ringer_Volume_Control Example: <Ringer_Volume_Control ua="na">Yes</Ringer_Volume_Control> |
|---|---|
| Web Parameter | Ringer Volume Control |
| Default Value | Yes |
| Allowed Values | Yes/No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed only in the phone web page for admin. |
| Description | When the parameter is set to Yes , the user can change the ringer volume. But when the parameter is set to No , the user can't change the ringer volume using the phone volume button or from the phone administration web page. |
| Phone Model | All MPP phones except 7832 and 8832 |
| Labels | User |

| XML Tag Name | Search_All_Enable Example: <Search_All_Enable ua="na">Yes</Search_All_Enable> |
|---|---|
| Web Parameter | Search All Enable |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin u=na |
| Description | Determines whether the phone user can search for contacts in the All directories . All directories only contain the enabled
                                 									directories with the priority from highest to lowest. Personal address book BroadSoft directory LDAP directory Bluetooth phone directory |
| Phone Model | All MPP phones |
| Labels | Directory Service |

| XML Tag Name | SDP_IP_Preference Example: <SDP_IP_Preference ua="na">Auto</SDP_IP_Preference> |
|---|---|
| Web Parameter | SDP IP Preference |
| Default Value | IPv4 |
| Allowed Values | IPv4 \| IPv6 \| Auto |
| Units | Options |
| Limits | IPv4 \| IPv6 \| Auto |
| User or Admin | Admin level only |
| Description | Sets RTP IP address in SIP calls to align with the phone's registration IP. |
| Phone Model | All MPP phones |
| Labels | Auto |

| XML Tag Name | Secure_Call_Option_n_ n is the extension number of the phone. Example: <Secure_Call_Option_1_ ua="na">Optional</Secure_Call_Option_1_> |
|---|---|
| Web Parameter | Secure Call Option |
| Default Value | Optional |
| Allowed Values | Option list: Optional\|Required\|Strict |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in user level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Optional－Retains the current secure call option for the phone. Required－Rejects nonsecure calls from other phones. Strict－Allows SRTP only when SIP transport is set to TLS . Allows RTP only when SIP transport
                              								is UDP/TCP . |
| Phone Model | All MPP phones |
| Labels | Call Setting Features |

| XML Tag Name | N/A Share_Line_Event_Package_Type Example: <Share_Line_Event_Package_Type ua="na">Call-Info</Share_Line_Event_Package_Type> |
|---|---|
| Web Parameter | Share Line Event Package Type |
| Default Value | Call-Info |
| Allowed Values | Call-Info Dialog |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for both user and admin. Not available on LCD UI. |
| Description | Enables dialog-based shared line so that the phones in the shared line can subscribe to the dialog event package. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | SIP_100REL_Enable_n_ n is the extension number of the phone. Example: <SIP_100REL_Enable_1_ ua="na">No</SIP_100REL_Enable_1_> |
|---|---|
| Web Parameter | SIP 100REL Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Individually enables the SIP 100REL feature. When enabled, the phone supports the 100REL SIP extension for reliable transmission of provisional responses (18x) and uses
                              PRACK requests. |
| Phone Model | All MPP phones |
| Labels | SIP Settings |

| XML Tag Name | <SIP_IP_Preference> Example: <SIP_IP_Preference>IPv6</SIP_IP_Preference> |
|---|---|
| Web Parameter | SIP IP Preference |
| Default Value | IPv4 |
| Allowed Values | IPv4 \| IPv6 |
| Units | N/A |
| Limits | Options |
| User or Admin | Admin level only |
| Description | Sets the SIP IP Preference for the phone. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | SIP_Timer_F Example: |
|---|---|
| Web Parameter | SIP Timer F |
| Default Value | N/A |
| Allowed Values | Integer |
| Units | Seconds |
| Limits | 0 to 64 seconds |
| User or Admin | Admin |
| Description | Non-INVITE time-out value. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | SIP_Transport Example: <SIP_Transport_n_ ua="na">UDP</SIP_Transport_n_> where n is the extension number. |
|---|---|
| Web Parameter | SIP Transport |
| Default Value | N/AUDP |
| Allowed Values | UDP\|TCP\|TLS\|Auto |
| Units | N/A |
| Limits | N/A |
| User or Admin | Admin |
| Description | Specifies the transport protocol for SIP messages. For SIP
                                 									messages, you can configure each extension to use: a specific protocol the protocol automatically selected by the phone When you set up automatic selection, the phone determines the
                                 									transport protocol based on the Name Authority Pointer (NAPTR)
                                 									records on the DNS server. The phone uses the protocol with the
                                 									highest priority in the records. |
| Phone Model | All MPP phones |
| Labels | SIP Settings |

| XML Tag Name | Speed_Dials Example: <Speed_Dials ua="na">Yes</Speed_Dials> |
|---|---|
| Web Parameter | Speed Dials |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Controls whether to show the Speed dials menu
                              								on the phone screen. Set this field to Yes to
                              								show the menu. Otherwise, set it to No . |
| Phone Model | All MPP phones |
| Labels | Speed Dial |

| XML Tag Name | SSRC_Reset_on_Rx_RE-INVITE Example: <SSRC_Reset_on_Rx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Rx_RE-INVITE> |
|---|---|
| Web Parameter | SSRC Reset on Rx RE-INVITE |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on incoming RE-INVITE. When the parameter is set to Yes , the phone can avoid the call transfer error, where only one person on the call hears the audio. This occurs on calls of
                              30 minutes or longer, and often on three-way calls. When the parameter is set to No , the SSRC still remains during a long duration call. In this case, this error might occur. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | SSRC_Reset_on_Tx_RE-INVITE Example: <SSRC_Reset_on_Tx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Tx_RE-INVITE> |
|---|---|
| Web Parameter | SSRC Reset on Tx RE-INVITE |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on outgoing RE-INVITE. When the parameter is set to Yes , the phone can avoid the one-way audio issue on a long duration call followed by a hold-resume action in certain Webex Calling
                              environments where the SRTP is end-to-end encrypted. When the parameter is set to No , the SSRC still remains during a long duration call. In this case, this error might occur. |
| Phone Model | All MPP phones |
| Labels | SIP |

| XML Tag Name | Status Example: <Status ua="na">Yes</Status> |
|---|---|
| Web Parameter | Status |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Controls whether to show the Status menu on
                              								the phone screen. Set this field to Yes to
                              								show the menu. Otherwise, set it to No . |
| Phone Model | All MPP phones |
| Labels | Phone Menu Visibility |

| XML Tag Name | Survivability_Proxy_n_ Syntax: <Survivability_Proxy_n_>hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_> Example: <Survivability_Proxy_n_>wxclsg.example.com:8933:A=192.169.10.1</Survivability_Proxy_n_> |
|---|---|---|
| Web Parameter | Survivability Proxy |
| Default Value | Blank |
| Allowed Values | String |
| Units | NA |
| Limits | NA |
| User or Admin | Admin level only. Not available on LCD UI. |
| Description | The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform
                              a failover to a survivability gateway. |
| Phone Model | All MPP phones |
| Labels | Proxy and Registration |

| XML Tag Name | Survivability_Proxy_Fallback_Intvl_n_ Example: <Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_> |
|---|---|
| Web Parameter | Survivability Proxy Fallback Intvl |
| Default Value | 30 sec |
| Allowed Values | Integer |
| Units | Seconds |
| Limits | 0 to 65535 |
| User or Admin | Admin level only. Not available on LCD UI. |
| Description | The interval in seconds after which the phone will attempt to fallback to the SSE nodes |
| Phone Model | All MPP phones |
| Labels | Proxy and Registration |

| XML Tag Name | Survivability_Test_Mode Example: <Survivability_Test_Mode>No</Survivability_Test_Mode> |
|---|---|
| Web Parameter | Survivability Proxy Fallback Intvl |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | Yes\|No |
| User or Admin | Admin level only. Not available on LCD UI. |
| Description | If set it to Yes, phone will always register to Site Survivability Gateway (SGW) nodes. |
| Phone Model | All MPP phones |
| Labels | System |

| XML Tag Name | Time_Format Example: <Time_Format ua="na">12hr</Time_Format> |
|---|---|
| Web Parameter | Time Format |
| Default Value | 12 hr |
| Allowed Values | 12hr\|24hr |
| Units | N/A |
| Limits | Options |
| User or Admin | Admin level only. |
| Description | Specifies a time format in which the user can enter a time until which the desk will be reserved. |
| Phone Model | All MPP phones |
| Labels | User |

| XML Tag Name | TLS_Cipher_List Example: <TLS_Cipher_List ua="na">RSA:!aNULL:!eNULL</TLS_Cipher_List> |
|---|---|
| Web Parameter | TLS Cipher List |
| Default Value | (Blank) |
| Allowed Values | Any string |
| Units | String without units |
| Limits | Min length: 0 Max length: 521 |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Allows you to specify the cipher list that the phone TLS applications
                              								use. For the cipher list formats, see
                              								https://www.openssl.org/docs/man1.0.2/man1/ciphers.html. |
| Phone Model | All MPP phones |
| Labels | Security |

| XML Tag Name | TLS_Client_Min_Version Example: <TLS_Client_Min_Version ua="na">TLS 1.2</TLS_Client_Min_Version> |
|---|---|
| Web Parameter | TLS Client Min Version |
| Default Value | TLS 1.2 |
| Allowed Values | Option list: TLS 1.0\|TLS 1.1\|TLS 1.2\|TLS 1.3 |
| Units | N/A |
| Limits | TLS 1.0\|TLS 1.1\|TLS 1.2\|TLS 1.3 |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls the minimum TLS version that the phone supports when the phone works as a TLS client. |
| Phone Model | All MPP phones Note The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. | Note | The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. |
| Note | The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. |
| Labels | System |

| Note | The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. |
|---|---|

| XML Tag Name | TLS_Name_Validate_n_ n is the extension number of the phone. Example: <TLS_Name_Validate_1_ ua="na">Yes</TLS_Name_Validate_1_> |
|---|---|
| Web Parameter | TLS Name Validate |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Option |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Specifies whether hostname verification is required when the phone
                              								line uses SIP over TLS. This parameter works only when SIP Transport is set to TLS for the phone line. |
| Phone Model | All MPP phones |
| Labels | Security |

| XML Tag Name | TLS_Server_Min_Version Example: <TLS_Server_Min_Version ua="na">TLS 1.2</TLS_Server_Min_Version> |
|---|---|
| Web Parameter | TLS Server Min Version |
| Default Value | TLS 1.2 |
| Allowed Values | Option list: TLS 1.1\|TLS 1.2\|TLS 1.3 |
| Units | N/A |
| Limits | TLS 1.1\|TLS 1.2\|TLS 1.3 |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls the minimum TLS version that the phone supports when the phone works as a TLS server. |
| Phone Model | All MPP phones Note The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. | Note | The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. |
| Note | The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. |
| Labels | System |

| Note | The option TLS 1.3 is only available on Cisco IP Conference Phone 7832 and 8832 Multiplatform Phone as of release 12.0(7)SR3. |
|---|---|

| XML Tag Name | Transition_Authorization_Error_Retry_Delay Example: <Transition_Authorization_Error_Retry_Delay>1800</Transition_Authorization_Error_Retry_Delay> |
|---|---|
| Web Parameter | Transition Authorization Error Retry Delay |
| Default Value | 1800 |
| Allowed Values | An integer Multiple integers A time range |
| Units |  |
| Limits |  |
| User or Admin | Admin level only |
| Description | If an authorization operation fails, the device tries to authorize again after a time specified in seconds. If the delay is
                              set to 0, the device does not do the retry. |
| Phone Model | 7800 MPP, 8800 MPP, 7832 MPP, and 8832 MPP phoness |
| Labels | Provisioning |

| XML Tag Name | Trans_Auth_Rule Example: <Trans_Auth_Rule ua="na">http://10.74.51.81/prov/migration/E2312.lic</Trans_Auth_Rule> |
|---|---|
| Web Parameter | Transition Authorization Rule |
| Default Value | Blank |
| Allowed Values | String |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for admin. Not available on the LCD UI. |
| Description | Obtains and authorizes the licence from the server. |
| Phone Model | Supported by all 78xx and 88xx |
| Labels | Firmware Upgrade |

| XML Tag Name | N/A Trans_Auth_Type Example: <Trans_Auth_Type ua="na">Classic</Trans_Auth_Type> |
|---|---|
| Web Parameter | Transition Authorization Type |
| Default Value | Classic |
| Allowed Values | Classic WxC |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for admin. Available on LCD UI. |
| Description | Indicates the license type obtained from the server during migration process. |
| Phone Model | Supported by all 78xx and 88xx |
| Labels | Firmware Upgrade |

| XML Tag Name | Unavailable_Reason_Code_Enable_n_ n is the extension number of the phone. Example: <Unavailable_Reason_Code_Enable_n_ ua="na">Yes</Unavailable_Reason_Code_Enable_n_> |
|---|---|
| Web Parameter | Unavailable Reason Code Enable |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether to show or hide the Unavailable menu text box of the Set agent status screen on the phone. |
| Phone Model | All MPP phones |
| Labels | ACD Settings |

| XML Tag Name | Unit_n_Extension_m_ Example: <Unit_n_Extension_m_ >Disabled</Unit_n_Extension_m_ > where, [n] is the unit number that ranges from 1 to 3 for Cisco IP phone 8861 and 8865 and 1 to 2 for Cisco IP phone 8851;
                                 [m] is the line key number that ranges from 1 to 28. |
|---|---|
| Web Parameter | Extension |
| Default Value | Disabled |
| Allowed Values | 1\|2\|3\|4\|5\|6\|7\|8\|9\|10\|11\|12\|13\|14\|15\|16\|Disabled |
| Units | N/A |
| Limits | Options |
| User or Admin | Admin level only. |
| Description | Assign an extension to the audio and video key expansion module line key. |
| Phone Model | Cisco IP Phone 8851, 8861, 8865 Multiplatform phone. |
| Labels | Att Console |

| XML Tag Name | Unit_n_Key_m_ n is unit number of the key expansion module, and m is the key
                              								number. |
|---|---|
| Web Parameter | Unit n Key m |
| Default Value | N/A |
| Allowed Values | N/a |
| Units | String without units |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Adds a menu shortcut to a line key of the attached key expansion
                              								module. Then, the user can press the configured line key to access
                              								the menu. Adds an extended feature to a line key of the attached key expansion
                              								module. Then, the user can press the line key to access the
                              								feature. Example: <Unit_1_Key_2_ ua="na">fnc=shortcut;url=userpref;nme=User preferences</Unit_1_Key_2_> where fnc= shortcut means function=phone menu shortcut. url= userpref is the menu to open with this line key. It's
                                    										the User preferences menu in this
                                    										example. nme= XXXX is the menu shortcut name displayed on the key
                                    										expansion module screen. If you don't specify a display
                                    										name, the line key displays the target menu item. In the
                                    										example, the line key displays User
                                       											preferences . |
| Phone Model | All MPP phones |
| Labels | Menu Shortcut key expansion module |

| XML Tag Name | Unit_n_Share_Call_Appearance_m Example: <Unit_n_Share_Call_Appearance_m >private</Unit_n_Share_Call_Appearance_m > where, [n] is the unit number that ranges from 1 to 3 for Cisco IP phone 8861 and 8865 and 1 to 2 for Cisco IP phone 8851;
                              [m] is the line key number that ranges from 1 to 28. |
|---|---|
| Web Parameter | Share Call Appearance |
| Default Value | shared\|private |
| Allowed Values | Options |
| Units | N/A |
| Limits | Options |
| User or Admin | Admin level only. |
| Description | Specifies if the line is private or shared. |
| Phone Model | Cisco IP Phone 8851, 8861, and 8865 Multiplatform phone. |
| Labels | Att Console |

| XML Tag Name | Unit_n_Short_Name_m_ Example: <Unit_n_Short_Name_m_ ua="na">$USER</Unit_n_Short_Name_m> where, [n] is the unit number that ranges from 1 to 3 for Cisco IP phone 8861 and 8865 and 1 to 2 for Cisco IP phone 8851;
                              [m] is the line key number that ranges from 1 to 28. |
|---|---|
| Web Parameter | Short Name |
| Default Value | $USER |
| Allowed Values | Alpha numeric |
| Units | N/A |
| Limits | N/A |
| User or Admin | Admin level only. |
| Description | Assign a short name. |
| Phone Model | Cisco IP Phone 8851, 8861, and 8865 Multiplatform phone. |
| Labels | Att Console |

| XML Tag Name | <Use_Auto_Discovery__WPAD_> Example: <Use_Auto_Discovery__WPAD_ ua="rw">No</Use_Auto_Discovery__WPAD_> |
|---|---|
| Web Parameter | Use Auto Discovery WPAD |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Controls whether to use the Web Proxy Auto-Discovery (WPAD) protocol to retrieve a Proxy Auto-Configuration (PAC) file. The
                                 phone will search for the PAC file by DHCP or DNS service. If the parameter is set to No , the user must manually specify a PAC URL that locates to the PAC file. For details, see PAC_URL PAC_URL . The parameter configuration takes effect only when the Proxy Mode is set to Auto . For details, see Proxy_Mode . |
| Phone Model | All MPP phones |
| Labels | Proxy |

| XML Tag Name | User_Preferences Example: <User_Preferences ua="na">Yes</User_Preferences> |
|---|---|
| Web Parameter | User Preferences |
| Default Value | Yes |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Admin ua=na |
| Description | Controls whether to show the User preferences menu on the phone screen. Set this field to Yes to show the menu.
                              								Otherwise, set it to No . |
| Phone Model | All MPP phones |
| Labels | Phone Menu Visibility |

| XML Tag Name | Voice_Feedback_Enable Example: <Voice_Feedback_Enable ua="rw">Yes</Voice_Feedback_Enable> |
|---|---|
| Web Parameter | Voice Feedback Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Not available on LCD UI. |
| Description | Controls whether to enable the voice feedback feature for the user. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | Voice_Feedback_Speed Example: <Voice_Feedback_Speed ua="rw">Normal</Voice_Feedback_Speed> |
|---|---|
| Web Parameter | Voice Feedback Speed |
| Default Value | Normal |
| Allowed Values | Option list: Slowest\|Slower\|Normal\|Faster\|Fastest |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Available on LCD UI. |
| Description | Controls the voice speed for the Voice Feedback feature. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | Voice_Feedback_Volume Example: <Voice_Feedback_Volume ua="rw">Normal</Voice_Feedback_Volume> |
|---|---|
| Web Parameter | Voice Feedback Volume |
| Default Value | Normal |
| Allowed Values | Option list: Lowest\|Low\|Normal\|High\|Highest |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=rw. Available on LCD UI. |
| Description | Controls the volume for Voice Feedback. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | User |

| XML Tag Name | Voice_Mail_Enable_n_ n is the extension number of the phone. Example: <Voice_Mail_Enable_1_ ua="na">Yes</Voice_Mail_Enable_1_> |
|---|---|
| Web Parameter | Voice Mail Enable |
| Default Value | Yes |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Controls whether the extension is allowed to subscribe to the voicemail server. |
| Phone Model | All MPP phones |
| Labels | Call Feature Settings |

| XML Tag Name | VPN_Password Example: <VPN_Password ua="rw">Example</VPN_Password> |
|---|---|
| Web Parameter | VPN Password |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | Maximum of 31 characters |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Provides the password of the specified username that the VPN server requires. |
| Phone Model | All MPP phones except 6821, 7832, and 8832 |
| Labels | VPN |

| XML Tag Name | VPN_Server Example: <VPN_Server ua="rw"> <Server IP or FQDN> </VPN_Server> |
|---|---|
| Web Parameter | VPN Server |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | Maximum of 31 characters |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Specifies an IP address or FQDN of the VPN server that the phone uses. For example: 100.101.1.218 |
| Phone Model | All MPP phones except 6821, 7832, and 8832 |
| Labels | VPN |

| XML Tag Name | VPN_Tunnel_Group Example: <VPN_Tunnel_Group ua="rw">Example</VPN_Tunnel_Group> |
|---|---|
| Web Parameter | VPN Tunnel Group |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | Maximum of 31 characters |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Specifies a VPN tunnel group for the VPN connection. A tunnel group is used to determine the tunnel connection policies and rules. |
| Phone Model | All MPP phones except 6821, 7832, and 8832 |
| Labels | VPN |

| XML Tag Name | VPN_User_Name Example: <VPN_User_Name ua="rw">Example</VPN_User_Name> |
|---|---|
| Web Parameter | VPN User Name |
| Default Value | Empty |
| Allowed Values | String |
| Units | String without units |
| Limits | Maximum of 31 characters |
| User or Admin | Exposed both in admin and user level, honored with ua = rw. Available on LCD UI. |
| Description | Specifies a username required to connect to the specified VPN server. |
| Phone Model | All MPP phones except 6821, 7832, and 8832 |
| Labels | VPN |

| XML Tag Name | Webex_Onboard_Enable Example: <Webex_Onboard_Enable ua="na">Yes</Webex_Onboard_Enable> |
|---|---|
| Web Parameter | Onboard Enable |
| Default Value | Yes |
| Allowed Values | Yes/No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for admin. Not available on LCD UI. |
| Description | Enables onboarding of the phone to Cisco Webex cloud. |
| Phone Model | All MPP phones |
| Labels | Webex |

| XML Tag Name | Webex_Directory_Enable Example: <Webex_Directory_Enable ua="na”>No</Webex_Directory_Enable> |
|---|---|
| Web Parameter | Directory Enable |
| Default Value | No |
| Allowed Values | Yes/No |
| Units | Boolean |
| Limits | N/A |
| User or Admin | Exposed only in the phone web page for admin. Not available on LCD UI. |
| Description | Enables webex contacts. |
| Phone Model | All MPP phones |
| Labels | Webex |

| XML Tag Name | Webex_Directory_Name Example: <Webex_Directory_Name ua="na”/> |
|---|---|
| Web Parameter | Directory Name |
| Default Value | Blank |
| Allowed Values | N/A |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in the phone web page for admin. Available on LCD UI. |
| Description | Modifies Webex directory name. |
| Phone Model | All MPP phones |
| Labels | Webex |

| XML Tag Name | Webex_Calendar_Enable Example: <Webex_Calendar_Enable ua="na">Yes</Webex_Calendar_Enable> |
|---|---|
| Web Parameter | Calendar_Enable |
| Default Value | No |
| Allowed Values | Yes\|No |
| Units | Boolean |
| Limits | Yes\|No |
| User or Admin | Admin level only. Not available on LCD UI. |
| Description | If set it to Yes, phone supports Webex OBTJ meetings with display of multiple meeting notifications in the meeting list. Also, Meeting softkey appears. |
| Phone Model | 8800 MPP phones only |
| Labels | Webex |

| XML Tag Name | Webex_Metrics_Enable Example: <Webex_Metrics_Enable ua="na">Yes</Webex_Metrics_Enable> |
|---|---|
| Web Parameter | Webex Metrics Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean |
| Limits | Yes\|No |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | With Metrics Enable, enable the phone control of all metric services. |
| Phone Model | Supported by all Series |
| Labels | Directory |

| XML Tag Name | Web_Server_Port Example: <Web_Server_Port ua="na">443</Web_Server_Port> |
|---|---|
| Web Parameter | Web Server Port |
| Default Value | 443 |
| Allowed Values | Numeric |
| Units | Numeric |
| Limits |  |
| User or Admin | Exposed in admin level, honored with ua = na. Not available on LCD UI. |
| Description | Set the default port to 443. |
| Phone Model | Supported by all phones |
| Labels | System |

| XML Tag Name | Work_Days Example: <Work_Days ua="na">Monday\|Tuesday\|Wednesday\|Thursday\|Friday</Work_Days> |
|---|---|---|---|---|---|
| Web Parameter | Work Days |
| Default Value | Monday\|Tuesday\|Wednesday\|Thursday\|Friday |
| Allowed Values | Option list: Saturday\|Sunday\|Monday\|Tuesday\|Wednesday\|Thursday\|Friday |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Specifies work days. During non-workdays, the phone will automatically turn off the screen. By default, workdays are set from
                              Monday to Friday. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | Working_Hours_End Example: <Working_Hours_End ua="na" um="y">19:00</Working_Hours_End> |
|---|---|
| Web Parameter | Working Hours End |
| Default Value | 19:00 |
| Allowed Values | 00:00 to 24:00 |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Specifies the end time for working hours using the 24-hour format. Outside of the specified working hours, the phone will
                              automatically turn off the screen. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | Working_Hours_Start Example: <Office_Hours_Enabled ua="na" um="y">True</Office_Hours_Enabled> |
|---|---|
| Web Parameter | Working_Hours_Start |
| Default Value | 07:00 |
| Allowed Values | 00:00 to 24:00 |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua=na. Not available on LCD UI. |
| Description | Specifies the start time for working hours using the 24-hour format. Outside of the specified working hours, the phone will
                              automatically turn off the screen. |
| Phone Model | Supported by 8800 Series and 8832 |
| Labels | Phone |

| XML Tag Name | XsiDir_EnterpriseCommon_Enable Example: <XsiDir_EnterpriseCommon_Enable ua="na">Yes</XsiDir_EnterpriseCommon_Enable> |
|---|---|
| Web Parameter | Directory EnterpriseCommon Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enables BroadSoft EnterpriseCommon directory. The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_EnterpriseCommon_Name Example: <XsiDir_EnterpriseCommon_Name ua="na">DirEnterpriseCommon</XsiDir_EnterpriseCommon_Name> |
|---|---|
| Web Parameter | Directory EnterpriseCommon Name |
| Default Value | Empty |
| Allowed Values | String without units |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Name of the BroadSoft personal directory. Displays on the phone as a
                              								directory choice. If the value is empty, the phone displays default name Enterprise Common . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Enterprise_Enable Example: <XsiDir_Enterprise_Enable ua="na">Yes</XsiDir_Enterprise_Enable> |
|---|---|
| Web Parameter | Directory Enterprise Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enables BroadSoft enterprise directory. The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Enterprise_Name Example: <XsiDir_Enterprise_Name ua="na">DirEnterpriseName</XsiDir_Enterprise_Name> |
|---|---|
| Web Parameter | Directory Enterprise Name |
| Default Value | Empty |
| Allowed Values | String without units |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Name of the BroadSoft Enterprise directory. Displays on the phone as
                              								a directory choice. If the value is empty, the phone displays default name Enterprise . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Group_Enable Example: <XsiDir_Group_Enable ua="na">Yes</XsiDir_Group_Enable> |
|---|---|
| Web Parameter | Directory Group Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enables BroadSoft Group directory. The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Group_Name Example: <XsiDir_Group_Name ua="na">DirGroupName</XsiDir_Group_Name> |
|---|---|
| Web Parameter | Directory Group Name |
| Default Value | Empty |
| Allowed Values | String without units |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Name of the BroadSoft Group directory. Displays on the phone as a
                              								directory choice. If the value is empty, the phone displays default name Group . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_GroupCommon_Enable Example: <XsiDir_GroupCommon_Enable ua="na">Yes</XsiDir_GroupCommon_Enable> |
|---|---|
| Web Parameter | Directory GroupCommon Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enables BroadSoft GroupCommon directory. The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_GroupCommon_Name Example: <XsiDir_GroupCommon_Name ua="na">DirGroupCommon</XsiDir_GroupCommon_Name> |
|---|---|
| Web Parameter | Directory GroupCommon Name |
| Default Value | Empty |
| Allowed Values | String without units |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Name of the BroadSoft personal directory. Displays on the phone as a
                              								directory choice. If the value is empty, the phone displays default name Group Common . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Individual_Mode_Enable Example: <XsiDir_Individual_Mode_Enable ua="na">Yes</XsiDir_Individual_Mode_Enable> |
|---|---|
| Web Parameter | Directory Individual Mode Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Individually enable or disable broadsoft directories. Only valid when XSI Directory Enable parameter is set to Yes . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Personal_Enable Example: <XsiDir_Personal_Enable ua="na">Yes</XsiDir_Personal_Enable> |
|---|---|
| Web Parameter | Directory Personal Enable |
| Default Value | No |
| Allowed Values | Option list: Yes\|No |
| Units | Boolean without units |
| Limits | Boolean |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Enables BroadSoft personal directory. The parameter is valid only when both Directory
                                 									Enable and Directory Individual Mode
                                 									Enable are set to Yes . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | XsiDir_Personal_Name Example: <XsiDir_Personal_Name ua="na">DirPersonalName</XsiDir_Personal_Name> |
|---|---|
| Web Parameter | Directory Personal Name |
| Default Value | Empty |
| Allowed Values | String without units |
| Units | N/A |
| Limits | N/A |
| User or Admin | Exposed in admin level, honored with ua = rw/ro/na. Not available on
                              								LCD UI. |
| Description | Name of the BroadSoft personal directory. Displays on the phone as a
                              								directory choice. If the value is empty, the phone displays default name Personal . |
| Phone Model | All MPP phones |
| Labels | Directory |

| XML Tag Name | X-SWITCH-INFO_Support Example: “<X-SWITCH-INFO_Support ua=”na“>Yes</X-SWITCH-INFO_Support>” |
|---|---|
| Web Parameter | N/A |
| Default Value | No |
| Allowed Values | Yes/No |
| Units | Bool |
| Limits | N/A |
| User or Admin | Admin level only. |
| Description | If selected, the Register message will include the X-switch-info header. |
| Phone Model | Applicable to all models. |
| Labels | Network |