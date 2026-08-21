---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-ccb9ac3db2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_150-configuration-guide-for-cisco-unified-customer-voice-portal/unified_icm_configuration.html
retrieved_at: 2026-08-21T02:58:38.344603+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 5, 2025

Chapter: Unified ICM Configuration

## Chapter: Unified ICM Configuration

# Unified ICM Configuration

## Configure Unified ICM Server

Step 1

Log in to Operations Console and click Device
                                             				  Management > Unified ICM .

Step 2

Click Add New .

To use an existing ICM Server as a template for configuring a
                                                      				new ICM Server, select an ICM Server from the list of available Unified ICM Servers and click Use As Template and perform Steps 3 to 6.

Step 3

Click  the General tab and enter the field values. See General Settings .

Step 4

(Optional)   Click the Device Pool tab and add the Unified ICM
                                       			 Server to a device pool.
                                       		  See Add Unified ICM to Device Pool .

Step 5

Click Save .

## ICM Server Settings

### General Settings

Unified CVP provides VoIP routing services for the Unified CCE and Unified CCX products. Unified ICM provides the services
                                 to determine where calls should be routed. These calls can be routed to ACDs, specific agents, or to VRUs. However, the routing
                                 services themselves must be provided by an external routing client.

A Unified ICM Server is required in Unified CVP Comprehensive, Call Director, and VRU-Only call flow models.

To configure General settings on an ICM Server, on the General tab, enter the field values, as listed in the following table:

Field

Description

Default

Value

Restart Required

IP Address

The  IP address of a Unified ICM Server

None

Valid IP address

No

Hostname

The name of the Unified ICM Server

None

Valid DNS name. It  includes alphanumeric characters and a dash.

No

Description

Additional information about the Unified ICM Server

None

Up to 1024 characters

No

Device Admin URL

The URL for the Unified ICM Web configuration
                                             							 application.

None

Valid URL

No

### Add Unified ICM to  Device Pool

See Add or Remove Device From Device Pool .

## Configure ICM Settings for Standalone Call Flow Model

Step 1

Create an application using Cisco Unified Call Studio and deploy it as a zip file.

For ICM Lookup, use the ReqICMLabel Element .  This element has two exit states: error and done . The done state must connect to a transfer element to transfer
                                                            the caller to ReqICMLabel as referenced by the ReqICMLabel Element .

For details on the ReqICMLabel Element , see the Element Specifications for Cisco Unified CVP VXML Server and Unified Call Studio .

For information about Unified Call
                                                            Studio, see the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio .

Step 2

Enable
                                       logging.

See the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio for details on configuring loggers using Unified Call
                                          Studio.

Step 3

Enable the CVPSNMPLogger for SNMP monitoring.

By default, CVPSNMPLogger is enabled when a new Unified Call Studio application
                                                      is created and deployed to the VXML Server.

Step 4

Add and configure a standard Call Server and enable the ICM service.
                                       See Configure Call Server .

Step 5

Configure the VXML Server.

Log in to 
                                             Operations Console, select Device Management > VXML Server and add a VXML Server with an associated Primary Call Server.

To enable reporting for this VXML Server, in the Operations Console,
                                             click the Configuration tab and select Enable
                                                Reporting for this VXML Server .

Add appropriate filtering.

Step 6

Deploy the Call Studio Application on the VXML
                                       Server.

Select Device Management > VXML Server in the Operations Console.

Select the VXML Server
                                             and click Save and Deploy .

Step 7

Using the ICM Script Editor, create
                                       a Unified ICME script that returns a label.

To transfer information from Unified ICME to
                                          the VXML Server in addition to the label, use the ToExtVXML 0 - 4 ECC Variables or
                                          Peripheral Variables 1 to 10. The format for using the ToExtVXML 0 to  4 is with
                                          name-value pairs that are delimited by semicolons.

### Example:

Use the Peripheral Variables 1 to 10
                                          to pass information to the VXML Server. The values in these variables will be
                                          taken as is.

For information about creating a
                                          Unified ICME script that returns a label in, see the Unified ICME documentation .

For information about using the ReqICMLabel element, see Pass Data to Unified ICME .

## Configure ICM
                        	 Settings for Comprehensive Call Flow Model for ICME and ICMH

Step 1

Define Network
                                       			 VRUs, create an instance, and define a customer.

On
                                             				  Unified ICME or NAM, in the ICM Configuration Manager, select the Network
                                                					 VRU Explorer tool, define a Network VRU for the VRU leg and labels for each
                                             				  Call Server.

On the
                                             				  Cisco Intelligent Contact Manager (CICM) only, in the ICM Configuration
                                             				  Manager, select Network
                                                					 VRU Explorer tool , define a Network VRU for the VRU leg and labels for
                                             				  reaching the NAM.

For Steps
                                          				1(a) and 1(b), enter the following values:

Type: 10

Name: <Network VRU Name> . For example: cvp

Define a
                                                					 label for each Unified CVP Call Server that is handling the switch leg:

Label: <Network Routing Number>

Type: Normal

Routing client for Unified ICME or NAM: From the drop-down list, select the
                                                      						  routing client configured for that Call Server peripheral.

Routing client for CICM only: From the drop-down list, select the INCRP routing
                                                      						  client.

The Network
                                                      				  VRU label in NAM and CICM must be same. Similarly, the Network VRU Names on the
                                                      				  NAM and CICM should also be same.

Step 2

Configure
                                       			 the ICM VRU Label.

Step 3

Define
                                       			 network VRUs and peripheral gateways for the switch leg in the ICM
                                       			 Configuration Manager.

On Unified
                                          				ICMH, on the NAM and CICMs, in the Network VRU Explorer tool, define one label
                                          				for each Unified CVP Call Server or NIC routing client.

Use the same
                                                      				  Type 10 Network VRU that you defined in the Step 1 for the VRU leg.

For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition .

Step 4

Set the client
                                       			 type for the INCRP NIC. On the CICM, in the ICM Configuration Manager, NIC
                                       			 Explorer tool, set the client type for the INCRP NIC. Select the Client
                                          				Type as VRU .

Step 5

Define a VRU
                                       			 that uses INCRP. On the CICM, in the ICM Configuration Manager, Network VRU
                                       			 Explorer tool:

Define a
                                             				  Network VRU with a label that uses INCRP as its routing client.

Specify
                                                					 the following:

Type: 10

Name: <name of Unified CVP VRU>

### Example:

Define a
                                             				  label for the NAM routing client.

Specify
                                                					 the following:

Type: Normal

Label: <Network Routing Number>

Routing client: INCRP NIC

For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition .

Step 6

Configure
                                       			 Peripheral Gateways .

On the NAM,
                                          				ICM Configuration Manager, PG
                                             				  Explorer tool, configure a peripheral gateway (PG) for the Unified CVP.
                                          				Configure a PG for each Unified CVP Call Server as follows:

In the tree
                                          				view pane, select the applicable PG.

Logical
                                             				  Controller tab:

Client
                                                					 Type: VRU

Name: A
                                                					 name descriptive of this PG

For
                                                					 example: <location>_A for side A of a particular location

Peripheral tab:

Peripheral
                                                					 Name: Descriptive name of this Unified CVP peripheral. For example: <location>_<cvp1> or <dns_name>

Client
                                                					 Type: VRU

Check the Enable
                                                   						Post-routing check box.

Advanced tab:
                                          				Select the name of the Unified CVP VRU from the Network VRU field drop-down
                                          				list. For example: cvpVRU

Routing Client tab:

Name: By
                                                					 convention, use the same name as the peripheral

Client
                                                					 Type: VRU

If you
                                                					 are in a Unified ICMH environment and configuring the CICM, then do the following:

Do
                                                      						  not check the Network Transfer Preferred check box.

Routing client: INCRP NIC

Step 7

Define a
                                       			 default network VRU on Unified ICME or
                                       			 the NAM, in the ICM Configuration Manager, the System
                                          				Information tool:

For Unified ICME or
                                             				  on the CICM
                                                					 only , define a default Network VRU.

If
                                             				  there are Routing Scripts on the NAM ,
                                             				  define a default Network VRU.

For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition .

Step 8

Configure
                                       			 dialed numbers, call types, and customers on the Unified ICME or Unified ICMH Server in the ICM Configuration Manager:

Dialed Number List Tool tab: Configure the dialed
                                             				  numbers.

Call Type List tool
                                                					 tab: Configure the call types.

ICM Instance Explorer tool tab: Configure the applicable customers.

For more
                                          				information, see ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition .

Step 9

Install and
                                       			 configure one or multiple Call Servers.

Log in to
                                          				the Operations Console and perform the following steps:

Enable
                                             				  the ICM and SIP Services on the Call Server.

On
                                                      						  the Operations Console, click Device
                                                            								Management > Unified CVP Call Server .

Check the ICM and SIP check boxes.

Click Device Management > Unified CVP Call Server > SIP . Configure the SIP Service:

If
                                                      						  you are using a SIP Proxy Server, enable the Outbound Proxy and select the SIP
                                                      						  Proxy Server.

Select the SIP
                                                         							 tab and configure the following values:

Enable Outbound Proxy: Yes

Outbound Proxy Host: Select from drop-down list.

Configure Local Static Routes on the SIP Proxy Server itself.

If
                                                      						  you are not using a SIP Proxy Server, configure Local Static Routes using the
                                                      						  Dialed Number Pattern system configuration on the Operations Console. A Local
                                                      						  Static Route must be configured for each SIP gateway or automatic call
                                                      						  distributor (ACD) so that SIP endpoint can receive calls.

Local Static Routes, Dialed Number (DN): Specify the dialed number pattern for
                                                      						  the destination.

Valid number patterns include the following characters:

Use the period or the X character for single-digit wildcard matching in any
                                                            								position.

Small letter x cannot be used as a wildcard.

Use the greater than ( > ), asterisk ( * ), or exclamation mark ( ! ) characters as a
                                                            								wildcard for zero or more digits at the end of the DN.

Avoid the T character for wildcard matching.

Dialed numbers must not exceed 24 characters.

For valid format and precedence information about dialed
                                                            								numbers, see Valid Format for Dialed Numbers .

Example: 9> (Errors are 9292 and ringtone is 9191)

For more information, see SIP Dialed Number Pattern Matching Algorithm .

The
                                                      						  following static route configuration is incorrect because the least explicit
                                                      						  routes must appear at the end. Load balancing or failover of calls require DNS
                                                      						  SRV domain names, not multiple routes with the same DN Pattern, but a single
                                                      						  route to an SRV domain name.

```
1>,10.2.6.1
2>,10.2.6.2
3>,10.2.6.20
2229191>,10.2.6.241
2229292>,10.2.6.241
2229191>,10.2.6.242
2229292>,10.2.6.242
2>,ccm-subscribers.cisco.com
3>,ccm-subscribers.cisco.com
```

```
22291>,cvp-ringtone.cisco.com
22292>,cvp-error.cisco.com
1>,ccm-subscribers.cisco.com
2>,ccm-subscribers.cisco.com
3>,ccm-subscribers.cisco.com
```

"91919191>" pattern
                                                                  							 does not match the dialed number "91919191" .

Check the default values for the SIP Service and change, if desired.

Configure the ICM Service. Select Device
                                                   						Management > CVP Call Server > ICM
                                                   						tab , In the Maximum Length of DNIS field, enter the
                                             				  length of the Network Routing Number.

Example: For the Gateway dial pattern as 1800******, the maximum DNIS length is 10 .

### Configure Common Unified ICMH for Unified CVP Switch Leg

Step 1

On the NAM , in the ICM Configuration Manager, Network VRU Explorer tool

Define a Network VRU for Unified CVP for Type as 10 and Name as cvpVRU .

Assign
                                                labels.                                                     Define one Label per Unified CVP or NIC routing client.
                                                Select the 
                                                Type as Normal and                                                         Label as Network
                                                Routing Number.

Step 2

Set the client type.

On the CICM , using the ICM Configuration
                                             Manager, NIC Explorer tool:

Select
                                                   the Routing Client tab for the INCRP NIC.

Enter the Client Type as VRU .

Step 3

Define a Network VRU.

On the CICM , using
                                             the ICM Configuration Manager, Network VRU Explorer tool,
                                             define a Network VRU with a label that uses INCRP as its routing
                                             client.

Enter the
                                             following:

Type: 10

Name: cvpVRU

Define
                                                   one Label for the NAM routing client:

Label: Network Routing Number

Type: Normal

Routing client: INCRP
                                                            NIC

Step 4

Define the Peripheral Gateways (PGs).

On the NAM , using the ICM Configuration Manager, PG
                                                Explorer tool, configure a peripheral gate for each ICM Service to be
                                             used for a switch leg that is connected to each PG.

For each Unified CVP ICM Service connected to this PG, in the tree view
                                             pane, select the applicable PG.

On the Logical
                                                Controller tab, enter the following:

Client Type: VRU

Name: A name descriptive of this
                                                   PG.

For example: <location>_A , for
                                                   side A of a particular location.

On the Peripheral tab, enter the following:

Peripheral Name: A name descriptive of this Unified CVP peripheral, for
                                                   example, <location>_<cvp1> or <dns_name>

Client Type: VRU

Check the Enable
                                                      Post-routing checkbox

On the Advanced tab, select
                                                   the name cvpVRU from the Network VRU field drop-down
                                                   list.

On the Routing Client tab, enter the following:

Name: By convention, use the same name as the
                                                   peripheral

Client Type: VRU

Do not check the Network Transfer
                                                      Preferred check box.

### ECC Payloads

You can define as many ECC variables as necessary. But, you can only pass 2000 bytes of ECC variables on a specific interface
                                 at any one time. To aid you in organizing ECC variables for specific purposes, the solution has ECC payloads .

An ECC payload is a defined set of ECC variables with a maximum size of 2000 bytes. You can create ECC payloads to suit the necessary information for a given operation. You can include a specific ECC variable
                                    in multiple ECC payloads. The particular ECC variables in a given ECC payload are called its members .

For ECC payloads to a CTI client, the size limit is 2000 bytes plus an extra 500 bytes for the ECC variable names. Unlike
                                             other interfaces, the CTI message includes ECC variable names.

In certain cases, mainly when using APIs, you might create an ECC payload that exceeds the CTI Server message size limit.
                                             If you use such an ECC payload in a client request, the CTI Server rejects the request. For an OPC message with such an ECC
                                             payload, the CTI Server sends the message without the ECC data. In this case, the following event is logged, “CTI Server was
                                             unable to forward ECC variables due to an overflow condition.”

You can use several ECC payloads in the same call flow, but only one ECC payload has scope at a given moment. TCDs and RCDs
                                 record the ID of the ECC payload that had scope during that leg of the call. The Call.ECCPayloadID variable contains the ID of the ECC payload which currently has scope.

For VRU and media routing leg of the call, the TCD contains the VRU PayloadID setting associated with the peripheral. If not,
                                 TCD contains the default payload ID. The Termination Call Variables are persisted only based on this payload setting.

In solutions that only use the default ECC payload, the system doesn’t create an ECC variable that exceeds the 2000-byte limit
                                 for an ECC payload or the 2500-byte CTI Message Size limit. The system does this because it automatically adds all ECC variables to the default ECC payload if that is the only ECC payload.

If you create another ECC payload, the system no longer checks the 2000-byte limit when creating ECC variables. The system
                                 creates the ECC variables without assigning them to an ECC payload. Assign the new ECC variable to an appropriate ECC payload
                                 yourself through the ECC Payload Tool.

You can create and modify ECC payloads in the Configuration Manager > List Tools > Expanded Call Variable Payload List tool.

#### Default ECC Payload

The solution includes an ECC payload named "Default" for backward compatibility. If your solution does not require more ECC
                                 variable space, you only need the Default payload. The solution uses the Default payload unless you override it.

If your solution only has the Default payload, the solution automatically adds any new ECC variables to the Default payload
                                 until it reaches the 2000-byte limit.

You cannot delete the Default payload. But, you can change its members.

Important

During upgrades, when the system first migrates your existing ECC variables to the Default payload, it does not check the
                                             CTI message size limit. The member names might exceed the extra 500 bytes that is allocated for ECC payloads to a CTI client.
                                             If the Default payload exceeds the limit, modify it to meet the limit.

In a fresh install, the Default payload includes the predefined system ECC variables. In an upgrade, the Default payload's
                                 contents depend on whether the starting release supports ECC payloads:

ECC payloads not supported —During the upgrade, a script adds your existing ECC variables to the Default payload.

ECC payloads are supported —The upgrade brings forward the existing definition of your Default payload.

If your solution includes PGs from a previous release that does not support ECC payloads, the Router always sends the Default
                                             payload to those PGs. Those PGs can properly handle the Default payload.

The ECC Payload node is available from the General tab on the Object Palette :

Use this node to change the ECC payload that has scope for the following part of your script. Once you select an ECC payload,
                                 it has scope for all non-VRU operations until changed. You can select the ECC payload either statically or dynamically by
                                 the payload's EnterpriseName or ID.

The Call.ECCPayloadID variable contains the ID of the ECC payload which currently has scope.

If the selected ECC payload is valid, the node updates Call.ECCPayloadID and your script follows the success path to the next node. If the selected ECC payload is invalid, your script follows the
                                 failure path from the node. The ECC payload that last had scope continues to have scope.

The node's monitor counts calls and tasks that traverse the node. There is also a meter on the failure path.

### Define Unified CVP
                           	 ECC Variables

Set up the ECC
                                 		  variables that Unified CVP uses to exchange information with Unified ICME/ICMH.

Step 1

On the ICM
                                          			 Configuration Manager, select Tools > Miscellaneous
                                                				  Tools > System Information and check the Enable expanded call context check box.

Step 2

On the ICM
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Expanded Call Variable List .

Step 3

In the
                                          			 Expanded Call Variable List window, enable the Add button by clicking Retrieve .

Step 4

Click Add .

The Attributes
                                             				property tab is enabled.

Step 5

Create each
                                          			 of the variables in the following table by clicking Save after defining each variable.

If you
                                                         				  change the configuration of any ECC variable with the Expanded Call Variable
                                                         				  List tool, stop and restart the Unified CVP Call Server.

Caution

It is
                                                         				  important that you enter the ECC's Name values listed in following table exactly as specified. If you do not, the
                                                         				  Unified ICME/ICMH software does not communicate with
                                                         				  the micro-applications on the ICM Service.

Length values are more
                                             				flexible. Unless the values listed in following table are noted as "required,"
                                             				the value in the Length column is the maximum that Unified ICMH can handle for
                                             				that ECC. Specify a value between 1 and the maximum length.

In a Unified
                                                         				  ICME/ICMH configuration, the ECC variable configuration, including the length,
                                                         				  defined in the NAM must be defined same in the CICM.

If you create or modify the ECC variables while the Unified CVP ICM Service is running, you must restart the VRU PG during
                                                         non-production time or during a scheduled maintenance window for the changes to take full effect. To restart the VRU PG, access
                                                         the service control of the PG in ICM and restart the ICM PIM and Unified CVP Call Server.

Step 6

Click Save to apply your changes.

Name

Length

Definition

user.CourtesyCallbackEnabled

Required
                                             					 for using Courtesy Callback.

Length:1

Used to
                                             					 determine if Courtesy Callback must be offered to a caller.

Valid
                                             					 values are:

"1" = Yes

"0" = No

user.cvp_server_info

Length: 15

Used by
                                             					 Unified CVP to send the IP address of the Call Server sending the request to
                                             					 Unified ICME.

Example:
                                             					 An IPv4 address like 192.168.150.181

user.microapp.currency

Value: 6

Currency
                                             					 type.

user.microapp.error_code

Value: 2

Return
                                             					 status error code to be returned from the Unified CVP to Unified ICME/ICMH upon
                                             					 a False return code in the Run Script Result.

user.microapp.fetchaudio

Recommended length: 20; but length depends on the filename.

Filename for audio to be played  while the voice browser loads and processes the requested resource when there is significant network latency.

Default:
                                             					 none

Example:
                                             					 "flash:holdmusic.wav"

This
                                                         						feature is not supported in Cisco VVB.

user.microapp.fetchdelay

Length: 1

The length of time (in seconds) to wait at the start of the fetch delay before playing the audio specified by user.microapp.fetchaudio . This setting only takes effect if the value of fetchaudio is not empty.

Default: 2 seconds; used to avoid a "blip" sound heard in a usual network scenario.

Setting this value to zero plays hold music immediately, for a minimum of five seconds.

Values: 1
                                             					 to 9

This feature is not supported in Cisco VVB.

user.microapp.fetchminimum

Length: 1

The
                                             					 minimum length of time to play audio specified by user.microapp.fetchaudio , even if the requested resource
                                             					 arrives in the meantime. This setting only takes effect if value of fetchaudio
                                             					 is not empty.

Default:
                                             					 5 seconds

Values; 1
                                             					 to 9

This
                                                         						feature is not supported in Cisco VVB.

user.microapp.isPostCallSurvey

Length: 1

Used to
                                             					 determine if post call survey must be offered to a caller after the agent hangs
                                             					 up.

Valid
                                             					 values: "y" or "Y" is "Yes"

"n" or
                                             					 "N" is "No"

Default
                                             					 value is "Yes"

user.microapp.locale

Value: 5

Locale, a
                                             					 combination of language and country which defines the grammar and prompt set to
                                             					 use.

user.microapp.media_server

Required for any IVR
                                             					 scripting.

Maximum
                                             					 length: 210 characters

Recommended length: 30

Root of
                                             					 the URL for all media files and external grammar files used in the script.

HTTP and
                                             					 HTTPS schemes can be specified as:

HTTP
                                                   						  scheme is specified as "http://<servername>"

HTTPS scheme is specified as "https://<servername>"

user.microapp.play_data

40

Default
                                             					 storage area for data for Play Data micro-application.

user.microapp.sys_media_lib

10

Directory for all system media files, such as individual digits, months,
                                             					 default error messages, and so forth.

user.microapp.app_media_lib

Maximum
                                             					 length: 210 characters

Recommended length: 10

Directory for all application-specific media files and grammar files.

You can
                                             					 also set this value to ".." (literally two periods in quotes), which bypasses
                                             					 the user.microapp.app_media_lib and user.microapp.locale ECC Variables when
                                             					 writing a URL path. For example, if you set the user.microapp.app_media_lib to ".." , the path:

http://server/locale/../hello.wav

would
                                             					 really be:

http://server/hello.wav

user.microapp.grammar_choices

Configurable on Unified ICME .
                                             					 Maximum length: 210 characters.

Specifies the ASR choices that a caller can input for the Get Speech
                                             					 micro-application. Each option in the list of choices is delimited by a forward
                                             					 slash (/).

user.microapp.inline_tts

Configurable on the ICM. Maximum length: 210 characters.

Specifies the text for inline Text To Speech (TTS).

user.microapp.input_type

Value:
                                             					 1

Specifies the type of input that is allowed.

Valid
                                             					 contents are:

D - DTMF

B - (Both, the
                                                   						  default) DTMF and Voice

If you
                                             					 are not using an ASR, you can set this variable to D. If you
                                             					 are using an ASR, you can set the variable to either D or B.

user.microapp.caller_input

Configurable on Unified ICME/ICMH. Maximum length: 210 characters.

Storage
                                             					 area for any ASR input that is collected from Get Speech.

user.microapp.pd_tts

Value:
                                             					 1

Specifies whether Unified CVP’s Text To Speech (TTS) or media files must be
                                             					 played to the caller.

Valid
                                             					 contents are:

Y - Yes, use TTS
                                                   						  capabilities

N - No, do not use
                                                   						  TTS capabilities; play media files instead.

user.microapp.UseVXMLParams

Value:
                                             					 1

This
                                             					 parameter specifies the manner in which you pass information to the external
                                             					 VoiceXML. Set this parameter to either "Y" (for yes) or "N" (for no).

Y uses
                                             					 the values in the user.microapp.ToExtVXML variable array. N appends the
                                             					 name/value pairs in user.microapp.ToExtVXML to the URL of the external
                                             					 VoiceXML.

Default:
                                             					 "N"

user.microapp.ToExtVXML

210

This
                                             					 variable array sends information to the external VoiceXML file. Must be
                                             					 configured as Array variables, not Scalar variables, even if the array length
                                             					 is set to 1.

For more information on user.microapp.ToExtVXML variable
                                             					 length, see the Configure the CCE Script for Courtesy Callback section.

user.microapp.FromExtVXML

210

This
                                             					 variable array returns information from the external VoiceXML file. Must be
                                             					 configured as Array variables, not Scalar variables, even if the array length
                                             					 is set to 1.

See Pass Data to Unified ICME for more information.

For more information on user.microapp.FromExtVXML variable
                                             					 length, see the Configure the CCE Script for Courtesy Callback section.

user.microapp.override_cli

Configurable on Unified ICME/ICMH. Maximum length: 200 characters.

Used by
                                             					 system to override the CLI field on outgoing transfers.

user.microapp.metadata

The variable length would usually be configured as 62 bytes, but if ECC space is restricted, you can configure it as 21 bytes.

Following the Menu (M), Get Data (GD) and Get Speech (GS) micro-applications, Unified CVP returns information about the micro-application
                                             that is run.

The
                                             					 user.microapp.metadata ECC variable is structured as follows:

m|con|tr|to|iv|duratn|vruscriptname

user.microapp.uui

Configurable on Unified ICME/ICMH. Maximum length: 131 characters.

Used to
                                             					 pass user-to-user information back to Unified CVP from Unified ICME/ICMH.

user.sip.refertransfer

Optional

Maximum
                                             					 length: 1 character.

SIP
                                             					 Service uses REFERs when transferring to the agents:

y -
                                                   						  Use REFER when transferring

n -
                                                   						  Do not use REFER when transferring

user.suppress.sendtovru

Optional

Length:
                                             					 1

Suppress the Temporary Connect message generated by SendToVRU node (explicitly
                                             					 or implicitly, for example by a Translation Route to VRU node).

Used in
                                             					 call flows where the Temporary Connect is generated right before the Connect
                                             					 message (that is, no Run Script messages expected) to avoid the extra overhead
                                             					 of setting up a VRU leg temporarily before the Connect arrives.

Valid
                                             					 values are: "y" or "Y" (yes, suppress the message)

#### What to do next

If your solution only has a Default payload, the solution automatically adds any new ECC variables to the Default payload
                                             until it reaches the 2000-byte limit.

### Define ECC Payloads

You can create and modify ECC payloads in the Expanded Call Variable Payload List tool.

The tool checks that the ECC payload does not exceed the 2000-byte limit only when you save your changes. The counters on
                                             the Members tab only show what the current size is with all the selected members. They are only informational and do not enforce the
                                             limit. The limit is enforced when you attempt to save the changes.

To define an ECC payload, you create the ECC payload and then add its members.

Step 1

In the Configuration Manager, open Tools > List Tools > Expanded Call Variable Payload List .

The ECC Payload List window appears.

Step 2

Click Retrieve to enable adding ECC payloads.

Step 3

Click Add .

The Attributes property tab appears.

Step 4

Complete the Attributes property tab. See the List Tools Online Help for details on the Attributes property tab.

Step 5

On the Members tab, click Add .

A dialog box listing all the existing ECC variables appears.

Step 6

Select the members for your ECC payload and click OK .

Watch that the ECC Variable Size counter does not exceed 2000 bytes. For ECC payloads that go to CTI clients, watch that the CTI Message Size counter does not exceed 2500 bytes.

Step 7

Click Save to apply your changes.

### Metadata ECC Variable

Following the Menu (M), Get Data (GD) and Get Speech (GS) micro-applications, Unified CVP returns information about the micro-application
                                 that is run. This information is returned in the user.microapp.metadata ECC variable. Its format is defined in terms of a number of subfields, each separated by a vertical bar character (‘|’).
                                 Also, the subfields are of fixed length in order to facilitate extraction either at reporting time or within the ICM routing
                                 script itself.

The user.microapp.metadata ECC
                                 variable is structured as follows:

m|con|tr|to|iv|duratn|vruscriptname

The following table
                                 shows the values for this variable:

Metadata

ECC Variable Value

m

D, V or N  -  Indicates whether the user responded with Voice (V), DTMF
                                             (D), or not at all (N). (Note that for the Menu micro-application, any
                                             successful single digit entry will result in m being set to V or D, even if the
                                             entry was an invalid menu selection.)

con

000
                                             to 100  -  Indicates the ASR percent confidence level at which the voice input
                                             was finally recognized. This field is only valid if m is Voice (V).

tr

00 to 99  -  Indicates how many tries were required.
                                             01 means user responded successfully after the first
                                             prompt.

to

00 to 99  -  Indicates how many timeouts occurred.
                                             Does not include interdigit timeouts.

iv

00 to
                                             99  -  Indicates how many invalid entries were received, including interdigit
                                             timeouts.

duratn

000000 to 999999  - 
                                             Indicates the micro-application duration in milliseconds. Duration is defined
                                             as the elapsed time between entering and exiting the RunExternalScript node, as
                                             measured in the IVR Service.

vru script name

Full name of the VRU script which was run. This is the only variable length field.

This ECC variable is optional. If you have used it, you must define it in the Unified ICME Expanded Call Context Variables
                                 configuration tool. Generally, the variable length to be configured is 62 bytes, but if ECC space is restricted, you can configure
                                 it as 21 bytes. This configuration drops the vruscriptname subfield. If you do define this variable, its contents get written
                                 to the Unified ICME database with every termination record, and can be used to provide a record of meta-information about
                                 the each input micro-application that is run.

### Common Configuration for Differentiating VRUs Based on Dialed Number

As per the Network VRU configuration instructions,  all callers are routed to the same VRUs (Unified CVPs) for VRU
                                 treatment purposes. Under this assumption, it is always simplest to rely on the
                                 system default Network VRU. However, it is sometimes necessary to differentiate
                                 the VRUs (Unified CVPs) based on dialed number.

For example, some calls need to assign different customers or applications to their own
                                 Unified CVP machines.

To configure
                                 Unified ICME to differentiate the VRUs, perform the
                                 following tasks:

Configure more than one Network
                                       VRU.

On Unified ICME, in the ICM Configuration
                                       Manager of the ICM Instance Explorer tool:

Configure one or multiple customers.

Configure the Network VRU for
                                             each customer if that customer wants to use in a Network VRU other than the
                                             default in future.

Associate the dialed
                                       number(s) to the customer in the Dialed Number List tool.

Since each configured VRU script is specific to one specified Network
                                       VRU, create a distinct set of VRU scripts for each Network VRU.
                                       Also, ensure that the ICM routing script calls the correct set of VRU
                                       scripts.

## Configure ICM
                        	 Settings for Call Director Call Flow Model

Step 1

On the
                                       			 Unified CM server, CCMAdmin Publisher, perform the following SIP-specific
                                       			 action:

Add route
                                             				  patterns for outbound calls from the Unified CM devices using a SIP Trunk to the Unified CVP Call Server. Also, add a route
                                             				  pattern for error DN.

Select Call Routing > Route/Hunt > Route Pattern > Add New and add the following:

Route Pattern: Specify the route pattern; for example: 3XXX for a TDM phone that dials 9+3xxx and all Unified ICME scripts are set up for 3xxx dialed numbers.

Gateway/Route List: Select the SIP Trunk defined in the previous substep.

For
                                                            						warm transfers, the call from one agent to another does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the
                                                            						Unified CM server and associate that number with your peripheral gateway user
                                                            						(PGUSER) for the JTAPI gateway on the Unified CM peripheral gateway. An
                                                            						alternative is to use the Dialed Number Plan on Unified ICME to bypass the CTI
                                                            						Route Point.

Step 2

Configure the
                                       			 peripheral gateways for the switch leg.

On Unified
                                          				ICME, ICM Configuration Manager, PG
                                             				  Explorer tool:

Configure
                                             				  each peripheral gateway (PG) to be used for the Switch leg. In the tree view pane, select the applicable peripheral gateway, and set
                                             				  the following:

On the Logical Controller tab:

Client Type: VRU

Name: A name descriptive of this PG

For example: <location>_A for side A of a particular location

On the Peripheral tab:

Peripheral Name: A name descriptive of this Unified CVP peripheral

For example: <location>_<cvp1> or <dns_name>

Client Type: VRU

Select the check box: Enable Post-routing

On the Routing Client tab:

Name: By convention, use the same name as the peripheral.

Client Type: VRU

For more
                                                					 information, see the ICM Configuration Guide for
                                                   						Cisco ICM Enterprise Edition .

Configure
                                             				  a peripheral for each Unified CVP Call Server to be used for a Switch leg
                                             				  connected to each PG.

Step 3

Configure
                                       			 dialed numbers.

On the
                                          				Unified ICME or Unified ICMH Server, in the ICM Configuration Manager,
                                          				configure the following items:

Dialed Number List Tool tab: Configure the dialed numbers.

Call Type List
                                                					 tool tab: Configure the call types.

ICM Instance Explorer tool tab: Configure the applicable customers.

For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition .

Step 4

Create a
                                       			 Routing Script.

On the Unified ICME or Unified ICMH Server in the ICM Script Editor tool:

Create a routing script that handles the incoming call. The routing script must run a Label node or Select node (node that
                                          returns a label right away).

Do not use
                                                      				  the Queue node in the routing script.

The label
                                          				must be configured in the SIP Proxy Server to the IP address of the device that
                                          				the label corresponds to. The Proxy Server is optional. If you do not have one,
                                          				you must configure the Gateway dial-peer to point to the Call Server (refer to
                                          				the first step in this process). Also, you must configure the destination
                                             				  labels in the SIP Service for the Call Server.

See the Scripting and Media Routing
                                             				  Guide for Cisco Unified ICM/Contact Center Enterprise & Hosted for
                                          				more information.

Step 5

In the
                                       			 Operations Console, install and configure Call Servers.

Enable the
                                             				  ICM and SIP Services on the Call Server.

In the
                                                					 Operations Console, select Device
                                                      						  Management > Unified CVP Call Server .

Select
                                                					 the check boxes: ICM and SIP

Configure the SIP Service:

Select Device
                                                      						  Management > CVP Call Server > SIP
                                                      						  tab .

If
                                                      						  you are using a SIP Proxy Server, enable the Outbound Proxy and select the SIP
                                                      						  Proxy Server. If using a SIP Proxy Server, configure Local Static Routes on the
                                                      						  SIP Proxy Server itself.

If
                                                      						  you are not using a SIP Proxy Server, configure Local Static Routes using the
                                                      						  Dialed Number Pattern system configuration in the Operations Console. A local
                                                      						  static route must be configured for each SIP gateway/ACD, SIP endpoint in order
                                                      						  to receive calls.

Check the default values for the SIP Service and change, if desired.

See the SIP Devices Configuration and SIP Dialed Number Pattern Matching Algorithm for detailed information.

Configure the ICM Service by setting the maximum length DNIS to the length of
                                             				  the Network Routing Number:

Select Device
                                                            								Management > CVP Call Server > ICM
                                                            								tab .

Set
                                                      						  the Maximum Length of DNIS to length of the Network Routing Number.

Example: For the Gateway dial pattern as 1800******, the maximum DNIS length is
                                                					 10.

For
                                                					 detailed information, see the Operations Console Online Help .

## Configure ICM
                        	 Settings for VRU-Only Call Flow Model: Type 8

Step 1

Perform
                                       			 Steps 1 to 4 of the Set Up Type 8 VRU-Only Call Flow Model for ICME and ICMH procedure.

Step 2

Define a
                                       			 Network VRU on Unified ICME or
                                       			 (for Unified ICMH ) on
                                       			 the NAM and each CICM.

Using the ICM
                                          				Configuration Manager, the Network VRU Explorer tool, specify the following:

Type: 8

Name: cvpVRU

Although any
                                                      				  name works, cvpVRU is used by convention, and is an example name referenced in this guide.

Step 3

Configure the
                                       			 Peripheral Gates (PGs) on Unified ICME or
                                       			 (for Unified ICMH ) on
                                       			 each CICM.

Configure
                                             				  each PG.

Configure
                                             				  a peripheral for each Unified CVP ICM Service connected to each PG.

Use the ICM
                                          				Configuration Manager, the PG
                                             				  Explorer tool. For each Unified CVP ICM Service connected to this PG, in
                                          				the tree view pane, select the applicable PG and configure the following items:

Logical
                                             				  Controller tab:

Client
                                                					 Type: VRU

Name: A
                                                					 name descriptive of this PG

Example: <location>_A for side A of a particular location

Peripheral tab:

Peripheral Name: A name descriptive of this Unified CVP peripheral

Examples: <location>_<cvp1> or <dns_name>

Client
                                                					 Type: VRU

Select
                                                					 the checkbox: Enable Post-routing

Advanced tab:

From the
                                                					 Network VRU field drop-down list, select the name: cvpVRU

Routing Client tab:

Name: By
                                                					 convention, use the same name as the peripheral.

Client
                                                					 Type: VRU

Step 4

Configure a
                                       			 Service and Route for each VRU on Unified ICME or (for Unified ICMH) on each
                                       			 CICM.

You can also
                                                      				  use service arrays. See the Unified ICME documentation set for more
                                                      				  information.

Using the ICM
                                          				Configuration Manager, the Service
                                             				  Explorer tool, specify the following:

Service
                                                					 Name: cvpVRU

Route
                                                					 Name: PeripheralName_cvpVRU

Peripheral Number: 2

Must
                                                					 match the "Pre-routed Call Service ID" in the Call Server configuration on the
                                                					 ICM tab in the Operations Console

Select
                                                					 the Enable Post-routing checkbox.

Step 5

Define trunk
                                       			 groups.

Configure
                                                      				  one Network Transfer Group and one associated Trunk Group for each VRU leg
                                                      				  Unified CVP ICM Service.

Define and
                                          				configure the network trunk group on Unified ICME or
                                          				(for Unified ICMH ) on
                                          				each CICM.

Using the ICM
                                          				Configuration Manager, the Network Trunk Group
                                             				  Explorer tool:

Identify
                                             				  the network trunk group.

Network Trunk Group Name: A name descriptive of this trunk group

For each
                                             				  Unified CVP ICM Service for the VRU leg, configure an associated trunk group.

Peripheral Name: A name descriptive of this trunk group

Peripheral Number: 200

Must match the Pre-routed Call Trunk Group ID in the Call Server
                                                      						  configuration on the ICM tab in the Operations Console

Trunk Count: Select Use Trunk Data from the drop-down list

Do
                                                      						  not configure any trunks

Step 6

Define
                                       			 translation route(s).

Define and
                                          				configure a Translation Route for each VRU Peripheral on Unified ICME or
                                          				(for Unified ICMH )
                                          				on each CICM.

On Unified ICME ,
                                          				ICM Configuration Manager, Translation Route Explorer tool:

Define
                                             				  a Translation Route for each VRU Peripheral. Specify the following:

Translation Route tab:

Set
                                                      						  the Name field to the name of the target VRU peripheral. (This
                                                      						  is by convention; this value must be unique in the enterprise)

Set
                                                      						  the Type field to DNIS and select the Service defined in the previous step

Configure translation route and label information for each VRU peripheral.
                                             				  Complete the following:

Route tab:

Set
                                                      						  the Name : by convention, this is the name of the target VRU
                                                      						  peripheral, followed by the DNIS that this route will use, for example,
                                                      						  MyVRU_2000

This value must be unique in the enterprise

Service Name drop-down list, select: PeripheralName.cvpVRU

Peripheral Target tab:

Enter the first DNIS that will be seen by the VRU that you will be using for
                                                      						  this translation route.

The DNIS pool used for each VRU peripheral must be unique

From the drop-down list, select a Network Trunk Group which belongs to the target VRU

Label tab:

Enter the translation route label (which might or might not be the same DNIS
                                                      						  you entered on the Peripheral Target tab)

Type: Normal

Routing Client: Select the NIC Routing Client

You must create an additional label for each NIC routing client.

Repeat the Route and corresponding Peripheral Target and Label
                                                                  							 information for each DNIS in the pool.

Step 7

Create VRU
                                       			 and routing scripts.

Create VRU
                                          				scripts and routing scripts for IVR treatment and agent transfer on Unified ICME or
                                          				(for Unified ICMH )
                                          				on each CICM .

Using the
                                          				ICM Script
                                             				  Editor tool, create the VRU scripts and routing scripts to be used for IVR
                                          				treatment and agent transfer, as described in other sections of this manual and
                                          				in the ICM manuals.

The VRU
                                          				scripts are associated with the applicable Network VRU.

For
                                          				example, cvpVRU

Use the ICM
                                          				Script Editor’s TranslationRouteToVRU node to connect the call to the Network
                                          				VRU.

Step 8

Configure
                                       			 the ECC variables on Unified ICME or
                                       			 (for Unified ICMH )
                                       			 on the NAM and each CICM.

Using the
                                          				ICM Configuration Manager, create the ECC variables.

For more
                                          				information, see Define Unified CVP ECC Variables .

Step 9

Configure
                                       			 dialed numbers and call types on Unified ICME or
                                       			 (for Unified ICMH )
                                       			 on the NAM and each CICM.

On Unified ICME ,
                                          				using the ICM Configuration Manager, configure dialed numbers and call types.

For more
                                          				information, see ICM Configuration Guide
                                             				  for Cisco ICM Enterprise Edition .

Step 10

On Unified CM ,
                                       			 configure Unified CM.

For more
                                          				information, see the Unified CM user
                                          				documentation.

Step 11

Install and
                                       			 configure the Call Servers.

Log in to
                                          				the Operations Console, select Device
                                                					 Management > CVP Call Server and install and
                                          				configure the Call Servers.

Check the ICM and IVR check boxes.

For
                                          				detailed information, see the Operations Console online help.

Step 12

Configure
                                       			 the ICM service.

On the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > ICM
                                                					 tab . On each Unified CVP Call Server, configure the ICM
                                             				  Service by specifying the following required information:

VRU
                                             				  connection port number.

Set the
                                                					 VRU Connection Port to match the VRU connection Port defined in ICM Setup for
                                                					 the corresponding VRU peripheral gateway (PIM).

Maximum
                                             				  Length of DNIS.

Set the
                                                					 maximum length DNIS to a number which is at least the length of the translation
                                                					 route DNIS numbers.

Example: if the Gateway dial pattern is 1800******, the maximum DNIS length is
                                                					 10.

Call
                                             				  service IDs: New Call and Pre-routed.

Enter
                                                					 the new and pre-routed call service IDs. Configure the ports for both groups
                                                					 according to the licenses purchased, call profiles, and capacity by completing
                                                					 the required fields on this tab.

Trunk
                                             				  group IDs: New Call and Pre-routed.

Enter the new and pre-routed call trunk group IDs

Configure the group number for the Pre-routed Call Trunk group. The group
                                                      						  number must match the trunk group number in the Network Trunk group used for
                                                      						  the translation route

Configure the number of ports according to the licenses purchased and capacity

Configure each of the numbers used for translation routes. (The "New Call" group is not used since the calls are being sent to
                                                      						  the VRU (Unified CVP) after some initial processing by the NIC/ Unified ICME )

Dialed
                                             				  numbers used in the translation route.

Add the
                                                					 dialed numbers in the DNIS field.

Check
                                             				  the default values of the other settings and change, if desired.

Step 13

Configure
                                       			 the IVR Service.

On the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > IVR tab.

Check the
                                          				default values and change, if desired.

Refer to
                                          				the Operations Console online help for information about other settings you
                                          				might want to adjust from their default values.

Step 14

(Optional) Configure
                                       			 the Reporting Server.

In the
                                          				Operations Console, select Device
                                                					 Management > CVP Reporting Server > General
                                                					 tab :

Configure the Reporting Server.

Select
                                                					 a Call Server to associate with this Reporting Server.

Check
                                                					 the default values of the Reporting properties and change, if desired.

For more
                                          				information, see Reporting Guide for Cisco
                                             				  Unified Customer Voice Portal

### VoiceXML
                              		  Gateway Configuration Examples

Applies a timestamp to debugging and log messages

Turns
                                             						on logging

Turns
                                             						off printing to the command line interface console

Sends
                                             						RTP packets

Configures ASR/TTS Server

Configures gateway settings

Initiates the VoiceXML leg

Plays
                                             						a .wav file that enables caller to hear message from critical_error.wav

Logs
                                             						errors on the gateway when the call fails

```
service timestamps debug datetime msec
service timestamps log datetime msec
service internal
logging buffered 99999999 debugging
no logging console
ip cef
no ip domain lookup
ip host tts-en-us <IP of TTS or MRCP Server>
ip host asr-en-us <IP of ASR or MRCP Server>
voice rtp send-recv
!
voice service voip
allow-connections h323 to h323
signaling forward unconditional
h323
sip
min-se 360
header-passing
voice class codec 1
codec preference 1 g711ulaw
codec preference 2 g729r8
!
ivr prompt memory 15000
ivr prompt streamed none
ivr asr-server rtsp://asr-en-us/recognizer
ivr tts-server rtsp://tts-en-us/synthesizer
mrcp client timeout connect 10
mrcp client timeout message 10
mrcp client rtpsetup enable
rtsp client timeout connect 10
rtsp client timeout message 10
vxml tree memory 500
http client cache memory file 500
http client connection timeout 60
http client response timeout 30
http client connection idle timeout 10
gateway
timer receive-rtcp 6
!
ip rtcp report interval 3000
application
service new-call flash:bootstrap.vxml
service cvperror flash:cvperror.tcl
service handoff flash:handoff.tcl
```

```
dial-peer voice 777 voip
 description ICM VRU label
 service bootstrap
 voice-class codec 1
 incoming called-number <your sendtovru label pattern here> 
 dtmf-relay rtp-nte
 no vad
 !
```

## Configure ICM
                        	 Settings for VRU-Only Call Flow Model: Type 7

Step 1

Perform
                                       			 Steps 1 to 4 of the Set Up Type 8 VRU-Only Call Flow Model for ICME and ICMH procedure.

Step 2

Configure
                                       			 each PG.

On the NAM , ICM
                                          				Configuration Manager, PG
                                             				  Explorer tool:

Configure
                                             				  each PG to be used for the VRU
                                                					 Client leg.

Configure
                                             				  a peripheral for each Unified CVP ICM Service to be used as a VRU leg connected
                                             				  to each PG.

For each
                                                					 Unified CVP ICM Service connected to this PG, in the tree view pane, select the
                                                					 applicable PG.

Logical
                                                   						Controller tab, configure:

Client Type: VRU

Name:
                                                      						  A name descriptive of this PG

For
                                                      						  example: <location>_A for side A of a particular location

Peripheral tab,
                                                					 configure:

Peripheral Name: A name descriptive of this VRU peripheral.

For
                                                      						  example: <location>_<cvp1> or <dns_name>

Client Type: VRU

Select the checkbox: Enable Post-routing

Routing Client tab:

Name:
                                                      						  By convention, use the same name as the peripheral.

Client Type: VRU

Step 3

Define a
                                       			 Network VRU and labels.

On the CICM ,
                                          				ICM Configuration Manager, Network VRU
                                             				  Explorer tool, define a Network VRU for the VRU leg and labels for reaching
                                          				the NAM.

Specify the
                                          				following:

Type: 7

Name: cvpVRU

Define a Label for the NAM.

Label:
                                                      						  Network routing number

Type: Normal

Routing client: Select the INCRP Routing Client from the drop-down list.

Step 4

Define a
                                       			 Network VRU and a label for each NIC.

On the NAM , ICM
                                          				Configuration Manager, Network VRU
                                             				  Explorer tool, define a Network VRU and a label for each NIC that is using
                                          				this VRU.

Specify the
                                          				following:

Type: 7

Name: cvpVRU

Define a Label for each NIC that is using this VRU:

Label:
                                                      						  Network routing number

Type: Normal

Routing client: Select the Routing Client for that NIC from the drop-down list.

Step 5

If there are
                                       			 Routing Scripts on the NAM, define a default Network VRU.

On the NAM , ICM
                                          				Configuration Manager, System
                                             				  Information tool, in the General section:

Define
                                                					 the Default Network VRU: cvpVRU

Step 6

Define a
                                       			 default VRU.

On the CICM ,
                                          				ICM Configuration Manager, System
                                             				  Information tool, in the General section:

Define
                                                					 a default Network VRU: cvpVRU

Step 7

Create the
                                       			 VRU and routing scripts.

On the CICM ,
                                          				ICM Script
                                             				  Editor tool:

Create the
                                          				VRU scripts and routing scripts to be used for IVR treatment and agent
                                          				transfer, as described in other sections of this manual and in the Unified ICME manuals. The VRU scripts are associated with the applicable Network VRU, that
                                          				is, cvpVRU .

Use the ICM
                                          				Script Editor’s SendToVRU node to connect the call to the Network VRU.

Step 8

Configure
                                       			 the ECC variables.

On the NAM and CICM ,
                                          				ICM Configuration Manager, configure the ECC variables.

For more
                                          				information, see Define Unified CVP ECC Variables .

Step 9

Configure
                                       			 dialed numbers and call types.

On the NAM and CICM ,
                                          				ICM Configuration Manager, configure dialed numbers and call types.

For more
                                          				information, see ICM Configuration Guide
                                             				  for Cisco ICM Enterprise Edition

Step 10

Define
                                       			 customers.

On the NAM and CICM ,
                                          				ICM Configuration Manager:

If
                                             				  necessary, differentiate VRUs (Unified CVPs) based on dialed number.

Define
                                             				  customers and their Network VRU.

For more
                                          				information, see Common Configuration for Differentiating VRUs Based on Dialed Number .

Step 11

On Cisco Unified CM ,
                                       			 configure Unified CM .

For more
                                          				information, see the Unified CM user
                                          				documentation.

Step 12

Install and
                                       			 configure the Call Server.

In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server .

Install
                                             				  and configure the Call Server.

To
                                             				  enable the ICM and IVR Services on the Call Server, select the ICM and IVR check boxes.

Step 13

Configure
                                       			 the ICM Service for each Call Server.

In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > ICM
                                                					 tab . For each Unified CVP Call Server, configure the ICM
                                             				  Service by specifying the following required information:

VRU
                                             				  connection port number.

Set the
                                                					 VRU Connection Port to match the VRU connection Port defined in ICM Setup for
                                                					 the corresponding VRU peripheral gateway (PIM).

Set the
                                             				  maximum length DNIS to the length of the Network Routing Number.

Example: if the Gateway dial pattern is 1800******, the maximum DNIS length is
                                                					 10.

Call
                                             				  service IDs: New Call and Pre-routed.

Enter
                                                					 the new and pre-routed call service IDs. Configure the ports for both groups
                                                					 according to the licenses purchased, call profiles, and capacity by completing
                                                					 the required fields on this tab

Trunk
                                             				  group IDs: New Call and Pre-routed.

Enter
                                                					 the new and pre-routed call trunk group IDs. Configure the group number for the
                                                					 Pre-routed Call Trunk group. The group number must match the trunk group number
                                                					 in the Network Trunk group used for the translation route.

Configure the number of ports according to the licenses purchased and capacity.
                                                					 Configure each of the numbers used for translation routes. (The New Call group is not used because the calls are
                                                					 sent to the VRU (Unified CVP) after an initial processing by the NIC/ Unified ICME ).

Check
                                             				  the default values of other settings and change, if desired.

Step 14

Configure
                                       			 the IVR service.

In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > IVR and configure the IVR
                                             				  Service .

Check the
                                          				default values and change, if desired.

See the
                                          				Operations Console online help for information about settings.

Step 15

(Optional)
                                       			 Configure the Reporting Server.

On the
                                          				Operations Console, select Device
                                                					 Management > CVP Reporting Server > General and configure the Reporting
                                          				Server.

Configure the Reporting Server.

Select
                                             				  a Call Server to associate with this Reporting Server.

Check
                                             				  the default values of the Reporting properties and change, if desired.

For more information, see Reporting Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

## Pass Data to Unified ICME

In the Unified CVP VXML Server (standalone) with ICM Lookup call flow model, Unified ICME sends a label to Unified CVP. This
                              process
                              requires the following configuration:

The
                              Standalone with Request ICM Label variation of the Standalone call flow model
                              performs a route request to Unified ICME, and then
                              Unified ICME starts a script (new call).
                              Unified ICME sees whatever the device puts in the new call
                              message, then Unified ICME chooses a target, such as an
                              agent, and sends a label back to the device. That route request to Unified ICME sends other information, such as ECC variables.
                              Unified ICME can pass other ECC variables to Unified
                              CVP. Also, you need to configure a Unified CVP VXML Server in the Unified CVP Call Server
                              for the call flow model.

### Configure the Connections

The following procedure describes how to set up a VXML Server that
                                 connects to a Call Server through the ICM Service, and the
                                 connection from the ICM Service to the peripheral gateway.

Step 1

Start the VXML Server. The VXML Server starts the VoiceXML Service
                                          using the DataFeed mechanism or the ReqICMLabel element.

The ReqICMLabel element allows a Call Studio script to pass caller input,
                                             call variables, and External Call Context (ECC) variables to a
                                             Unified ICME script. The ReqICMLabel must be inserted into a
                                             Call Studio script as a decision element. In Call Studio, the returned
                                             Unified ICME label contains a result which can be used by
                                             other elements in the same application, such as the Transfer or Audio element.
                                             The Transfer element sends instructions to the IOS Voice Browser to transfer
                                             the caller to the desired location.

After
                                             the VoiceXML Service starts, it starts communicating with the ICM
                                             Service.

Step 2

Log in to the  Operations
                                          Console and configure a Call Server and ICM service. See Configure Call Server .
                                          See
                                          the Unified ICME documentation for instructions on configuring
                                          the VRU PIM to connect to a VRU. For example, Unified
                                          CVP.

### Configure a Gateway for IP to TDM Calls

The following components
                                 are required for the gateway to process IP to TDM
                                 calls:

Phones and numbers must be configured on the
                                       TDM switch.

Gateway must be defined on
                                       Unified CM.

Route pattern on
                                       the Unified CM that sends the call to the gateway.

Dial peer on the gateway that sends
                                       calls that must be configured.

Dial 888800605x on the IP phone (this is a specific
                                       physical phone extension).

Step 1

Configure the gateway to send the call to a particular Unified CVP VXML Server
                                          application, as follows:

```
dial-peer voice 8888 voip
                                    service [gateway application name]
                                    incoming called-number 888800....
                                    dtmf-relay rtp-nte
                                    codec g711ulaw
                                    no vad
```

Step 2

To match the number in the Unified CVP VXML Server transfer node and send it out the T1 port to the G3 to its destination,
                                          use the following configuration:

```
dial-peer voice 8880 pots
                                    destination-pattern 888800....
                                    incoming called-number
                                    direct-inward-dial
                                    port 1/0:D
```

### Configure a Cisco Multiservice IP-to-IP Gateway for Unified CM Connections

For information on
                                 configuring the Cisco IOS gateway for Unified CM
                                 connections, see the Cisco Multiservice IP-to-IP Gateway Software
                                 documentation.

### Configure SNMP Monitoring for the Unified CVP VXML Server

When a Call Studio application is created, the
                                 simple network management protocol (SNMP) monitoring for the VXML Server is provided. CVPSNMPLogger is enabled when a new Call Studio application is created
                                 and deployed to the Unified CVP VXML Server. CVPSNMPLogger logs error
                                 events received from theVXML Server.  For example, using this process you can configure to send a page to a technical support
                                 representative when a
                                 particular error alert is triggered on the customer site.

Step 1

To view CVPSNMPLogger for the Unified CVP VXML Server, access the Call Studio
                                          interface.

Step 2

From Call Studio for each Call Studio application, right-click the application and
                                          select Properties > Cisco Unified CVP > General Settings .

CVPSNMPLogger appears in
                                             the Loggers drop-down box.

Caution

| Step 1 | Log in to Operations Console and click Device
                                             				  Management > Unified ICM . |
|---|---|
| Step 2 | Click Add New . Note To use an existing ICM Server as a template for configuring a
                                                      				new ICM Server, select an ICM Server from the list of available Unified ICM Servers and click Use As Template and perform Steps 3 to 6. | Note | To use an existing ICM Server as a template for configuring a
                                                      				new ICM Server, select an ICM Server from the list of available Unified ICM Servers and click Use As Template and perform Steps 3 to 6. |
| Note | To use an existing ICM Server as a template for configuring a
                                                      				new ICM Server, select an ICM Server from the list of available Unified ICM Servers and click Use As Template and perform Steps 3 to 6. |
| Step 3 | Click  the General tab and enter the field values. See General Settings . |
| Step 4 | (Optional)   Click the Device Pool tab and add the Unified ICM
                                       			 Server to a device pool.
                                       		  See Add Unified ICM to Device Pool . |
| Step 5 | Click Save . |

| Note | To use an existing ICM Server as a template for configuring a
                                                      				new ICM Server, select an ICM Server from the list of available Unified ICM Servers and click Use As Template and perform Steps 3 to 6. |
|---|---|

| Field | Description | Default | Value | Restart Required |
|---|---|---|---|---|
| IP Address | The  IP address of a Unified ICM Server | None | Valid IP address | No |
| Hostname | The name of the Unified ICM Server | None | Valid DNS name. It  includes alphanumeric characters and a dash. | No |
| Description | Additional information about the Unified ICM Server | None | Up to 1024 characters | No |
| Device Admin URL | The URL for the Unified ICM Web configuration
                                             							 application. | None | Valid URL | No |

| Variations | Applicable steps |
|---|---|
| Reporting | Steps 2, 5, and 6 |
| Without Reporting | Not applicable |
| ICM lookup | Steps 1 to 7 |
| All variations | Step 1 |

| Step 1 | Create an application using Cisco Unified Call Studio and deploy it as a zip file. Note For ICM Lookup, use the ReqICMLabel Element .  This element has two exit states: error and done . The done state must connect to a transfer element to transfer
                                                            the caller to ReqICMLabel as referenced by the ReqICMLabel Element . For details on the ReqICMLabel Element , see the Element Specifications for Cisco Unified CVP VXML Server and Unified Call Studio . For information about Unified Call
                                                            Studio, see the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio . | Note | For ICM Lookup, use the ReqICMLabel Element .  This element has two exit states: error and done . The done state must connect to a transfer element to transfer
                                                            the caller to ReqICMLabel as referenced by the ReqICMLabel Element . For details on the ReqICMLabel Element , see the Element Specifications for Cisco Unified CVP VXML Server and Unified Call Studio . For information about Unified Call
                                                            Studio, see the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio . |
|---|---|---|---|
| Note | For ICM Lookup, use the ReqICMLabel Element .  This element has two exit states: error and done . The done state must connect to a transfer element to transfer
                                                            the caller to ReqICMLabel as referenced by the ReqICMLabel Element . For details on the ReqICMLabel Element , see the Element Specifications for Cisco Unified CVP VXML Server and Unified Call Studio . For information about Unified Call
                                                            Studio, see the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio . |
| Step 2 | Enable
                                       logging. See the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio for details on configuring loggers using Unified Call
                                          Studio. |
| Step 3 | Enable the CVPSNMPLogger for SNMP monitoring. Note By default, CVPSNMPLogger is enabled when a new Unified Call Studio application
                                                      is created and deployed to the VXML Server. | Note | By default, CVPSNMPLogger is enabled when a new Unified Call Studio application
                                                      is created and deployed to the VXML Server. |
| Note | By default, CVPSNMPLogger is enabled when a new Unified Call Studio application
                                                      is created and deployed to the VXML Server. |
| Step 4 | Add and configure a standard Call Server and enable the ICM service.
                                       See Configure Call Server . |
| Step 5 | Configure the VXML Server. Log in to 
                                             Operations Console, select Device Management > VXML Server and add a VXML Server with an associated Primary Call Server. To enable reporting for this VXML Server, in the Operations Console,
                                             click the Configuration tab and select Enable
                                                Reporting for this VXML Server . Add appropriate filtering. |
| Step 6 | Deploy the Call Studio Application on the VXML
                                       Server. Select Device Management > VXML Server in the Operations Console. Select the VXML Server
                                             and click Save and Deploy . |
| Step 7 | Using the ICM Script Editor, create
                                       a Unified ICME script that returns a label. To transfer information from Unified ICME to
                                          the VXML Server in addition to the label, use the ToExtVXML 0 - 4 ECC Variables or
                                          Peripheral Variables 1 to 10. The format for using the ToExtVXML 0 to  4 is with
                                          name-value pairs that are delimited by semicolons. Example: ToExtVXML0 = "company=Cisco
                                          Systems;state=MA" Use the Peripheral Variables 1 to 10
                                          to pass information to the VXML Server. The values in these variables will be
                                          taken as is. For information about creating a
                                          Unified ICME script that returns a label in, see the Unified ICME documentation . For information about using the ReqICMLabel element, see Pass Data to Unified ICME . |

| Note | For ICM Lookup, use the ReqICMLabel Element .  This element has two exit states: error and done . The done state must connect to a transfer element to transfer
                                                            the caller to ReqICMLabel as referenced by the ReqICMLabel Element . For details on the ReqICMLabel Element , see the Element Specifications for Cisco Unified CVP VXML Server and Unified Call Studio . For information about Unified Call
                                                            Studio, see the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio . |
|---|---|

| Note | By default, CVPSNMPLogger is enabled when a new Unified Call Studio application
                                                      is created and deployed to the VXML Server. |
|---|---|

| Step 1 | Define Network
                                       			 VRUs, create an instance, and define a customer. On
                                             				  Unified ICME or NAM, in the ICM Configuration Manager, select the Network
                                                					 VRU Explorer tool, define a Network VRU for the VRU leg and labels for each
                                             				  Call Server. On the
                                             				  Cisco Intelligent Contact Manager (CICM) only, in the ICM Configuration
                                             				  Manager, select Network
                                                					 VRU Explorer tool , define a Network VRU for the VRU leg and labels for
                                             				  reaching the NAM. For Steps
                                          				1(a) and 1(b), enter the following values: Type: 10 Name: <Network VRU Name> . For example: cvp Define a
                                                					 label for each Unified CVP Call Server that is handling the switch leg: Label: <Network Routing Number> Type: Normal Routing client for Unified ICME or NAM: From the drop-down list, select the
                                                      						  routing client configured for that Call Server peripheral. Routing client for CICM only: From the drop-down list, select the INCRP routing
                                                      						  client. Note The Network
                                                      				  VRU label in NAM and CICM must be same. Similarly, the Network VRU Names on the
                                                      				  NAM and CICM should also be same. | Note | The Network
                                                      				  VRU label in NAM and CICM must be same. Similarly, the Network VRU Names on the
                                                      				  NAM and CICM should also be same. |
|---|---|---|---|
| Note | The Network
                                                      				  VRU label in NAM and CICM must be same. Similarly, the Network VRU Names on the
                                                      				  NAM and CICM should also be same. |
| Step 2 | Configure
                                       			 the ICM VRU Label. |
| Step 3 | Define
                                       			 network VRUs and peripheral gateways for the switch leg in the ICM
                                       			 Configuration Manager. On Unified
                                          				ICMH, on the NAM and CICMs, in the Network VRU Explorer tool, define one label
                                          				for each Unified CVP Call Server or NIC routing client. Note Use the same
                                                      				  Type 10 Network VRU that you defined in the Step 1 for the VRU leg. For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition . | Note | Use the same
                                                      				  Type 10 Network VRU that you defined in the Step 1 for the VRU leg. |
| Note | Use the same
                                                      				  Type 10 Network VRU that you defined in the Step 1 for the VRU leg. |
| Step 4 | Set the client
                                       			 type for the INCRP NIC. On the CICM, in the ICM Configuration Manager, NIC
                                       			 Explorer tool, set the client type for the INCRP NIC. Select the Client
                                          				Type as VRU . |
| Step 5 | Define a VRU
                                       			 that uses INCRP. On the CICM, in the ICM Configuration Manager, Network VRU
                                       			 Explorer tool: Define a
                                             				  Network VRU with a label that uses INCRP as its routing client. Specify
                                                					 the following: Type: 10 Name: <name of Unified CVP VRU> Example: cvpVRU Define a
                                             				  label for the NAM routing client. Specify
                                                					 the following: Type: Normal Label: <Network Routing Number> Routing client: INCRP NIC For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition . |
| Step 6 | Configure
                                       			 Peripheral Gateways . On the NAM,
                                          				ICM Configuration Manager, PG
                                             				  Explorer tool, configure a peripheral gateway (PG) for the Unified CVP.
                                          				Configure a PG for each Unified CVP Call Server as follows: In the tree
                                          				view pane, select the applicable PG. Logical
                                             				  Controller tab: Client
                                                					 Type: VRU Name: A
                                                					 name descriptive of this PG For
                                                					 example: <location>_A for side A of a particular location Peripheral tab: Peripheral
                                                					 Name: Descriptive name of this Unified CVP peripheral. For example: <location>_<cvp1> or <dns_name> Client
                                                					 Type: VRU Check the Enable
                                                   						Post-routing check box. Advanced tab:
                                          				Select the name of the Unified CVP VRU from the Network VRU field drop-down
                                          				list. For example: cvpVRU Routing Client tab: Name: By
                                                					 convention, use the same name as the peripheral Client
                                                					 Type: VRU If you
                                                					 are in a Unified ICMH environment and configuring the CICM, then do the following: Do
                                                      						  not check the Network Transfer Preferred check box. Routing client: INCRP NIC |
| Step 7 | Define a
                                       			 default network VRU on Unified ICME or
                                       			 the NAM, in the ICM Configuration Manager, the System
                                          				Information tool: For Unified ICME or
                                             				  on the CICM
                                                					 only , define a default Network VRU. Define
                                             				  the Default Network VRU: <Network VRU Name> . For example: cvpVRU If
                                             				  there are Routing Scripts on the NAM ,
                                             				  define a default Network VRU. For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition . |
| Step 8 | Configure
                                       			 dialed numbers, call types, and customers on the Unified ICME or Unified ICMH Server in the ICM Configuration Manager: Dialed Number List Tool tab: Configure the dialed
                                             				  numbers. Call Type List tool
                                                					 tab: Configure the call types. ICM Instance Explorer tool tab: Configure the applicable customers. For more
                                          				information, see ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition . |
| Step 9 | Install and
                                       			 configure one or multiple Call Servers. Log in to
                                          				the Operations Console and perform the following steps: Enable
                                             				  the ICM and SIP Services on the Call Server. On
                                                      						  the Operations Console, click Device
                                                            								Management > Unified CVP Call Server . Check the ICM and SIP check boxes. Click Device Management > Unified CVP Call Server > SIP . Configure the SIP Service: If
                                                      						  you are using a SIP Proxy Server, enable the Outbound Proxy and select the SIP
                                                      						  Proxy Server. Select the SIP
                                                         							 tab and configure the following values: Enable Outbound Proxy: Yes Outbound Proxy Host: Select from drop-down list. Configure Local Static Routes on the SIP Proxy Server itself. If
                                                      						  you are not using a SIP Proxy Server, configure Local Static Routes using the
                                                      						  Dialed Number Pattern system configuration on the Operations Console. A Local
                                                      						  Static Route must be configured for each SIP gateway or automatic call
                                                      						  distributor (ACD) so that SIP endpoint can receive calls. Local Static Routes, Dialed Number (DN): Specify the dialed number pattern for
                                                      						  the destination. Valid number patterns include the following characters: Use the period or the X character for single-digit wildcard matching in any
                                                            								position. Note Small letter x cannot be used as a wildcard. Use the greater than ( > ), asterisk ( * ), or exclamation mark ( ! ) characters as a
                                                            								wildcard for zero or more digits at the end of the DN. Avoid the T character for wildcard matching. Dialed numbers must not exceed 24 characters. For valid format and precedence information about dialed
                                                            								numbers, see Valid Format for Dialed Numbers . Example: 9> (Errors are 9292 and ringtone is 9191) For more information, see SIP Dialed Number Pattern Matching Algorithm . The
                                                      						  following static route configuration is incorrect because the least explicit
                                                      						  routes must appear at the end. Load balancing or failover of calls require DNS
                                                      						  SRV domain names, not multiple routes with the same DN Pattern, but a single
                                                      						  route to an SRV domain name. Incorrect Example: 1>,10.2.6.1
2>,10.2.6.2
3>,10.2.6.20
2229191>,10.2.6.241
2229292>,10.2.6.241
2229191>,10.2.6.242
2229292>,10.2.6.242
2>,ccm-subscribers.cisco.com
3>,ccm-subscribers.cisco.com Correct static route
                                                      						  configuration example: 22291>,cvp-ringtone.cisco.com
22292>,cvp-error.cisco.com
1>,ccm-subscribers.cisco.com
2>,ccm-subscribers.cisco.com
3>,ccm-subscribers.cisco.com Note "91919191>" pattern
                                                                  							 does not match the dialed number "91919191" . Check the default values for the SIP Service and change, if desired. Configure the ICM Service. Select Device
                                                   						Management > CVP Call Server > ICM
                                                   						tab , In the Maximum Length of DNIS field, enter the
                                             				  length of the Network Routing Number. Example: For the Gateway dial pattern as 1800******, the maximum DNIS length is 10 . | Note | Small letter x cannot be used as a wildcard. | Note | "91919191>" pattern
                                                                  							 does not match the dialed number "91919191" . |
| Note | Small letter x cannot be used as a wildcard. |
| Note | "91919191>" pattern
                                                                  							 does not match the dialed number "91919191" . |

| Note | The Network
                                                      				  VRU label in NAM and CICM must be same. Similarly, the Network VRU Names on the
                                                      				  NAM and CICM should also be same. |
|---|---|

| Note | Use the same
                                                      				  Type 10 Network VRU that you defined in the Step 1 for the VRU leg. |
|---|---|

| Note | Small letter x cannot be used as a wildcard. |
|---|---|

| Note | "91919191>" pattern
                                                                  							 does not match the dialed number "91919191" . |
|---|---|

| Step 1 | On the NAM , in the ICM Configuration Manager, Network VRU Explorer tool Define a Network VRU for Unified CVP for Type as 10 and Name as cvpVRU . Assign
                                                labels.                                                     Define one Label per Unified CVP or NIC routing client.
                                                Select the 
                                                Type as Normal and                                                         Label as Network
                                                Routing Number. |
|---|---|
| Step 2 | Set the client type. On the CICM , using the ICM Configuration
                                             Manager, NIC Explorer tool: Select
                                                   the Routing Client tab for the INCRP NIC. Enter the Client Type as VRU . |
| Step 3 | Define a Network VRU. On the CICM , using
                                             the ICM Configuration Manager, Network VRU Explorer tool,
                                             define a Network VRU with a label that uses INCRP as its routing
                                             client. Enter the
                                             following: Type: 10 Name: cvpVRU Define
                                                   one Label for the NAM routing client: Label: Network Routing Number Type: Normal Routing client: INCRP
                                                            NIC |
| Step 4 | Define the Peripheral Gateways (PGs). On the NAM , using the ICM Configuration Manager, PG
                                                Explorer tool, configure a peripheral gate for each ICM Service to be
                                             used for a switch leg that is connected to each PG. For each Unified CVP ICM Service connected to this PG, in the tree view
                                             pane, select the applicable PG. On the Logical
                                                Controller tab, enter the following: Client Type: VRU Name: A name descriptive of this
                                                   PG. For example: <location>_A , for
                                                   side A of a particular location. On the Peripheral tab, enter the following: Peripheral Name: A name descriptive of this Unified CVP peripheral, for
                                                   example, <location>_<cvp1> or <dns_name> Client Type: VRU Check the Enable
                                                      Post-routing checkbox On the Advanced tab, select
                                                   the name cvpVRU from the Network VRU field drop-down
                                                   list. On the Routing Client tab, enter the following: Name: By convention, use the same name as the
                                                   peripheral Client Type: VRU Do not check the Network Transfer
                                                      Preferred check box. |

| Note | For ECC payloads to a CTI client, the size limit is 2000 bytes plus an extra 500 bytes for the ECC variable names. Unlike
                                             other interfaces, the CTI message includes ECC variable names. In certain cases, mainly when using APIs, you might create an ECC payload that exceeds the CTI Server message size limit.
                                             If you use such an ECC payload in a client request, the CTI Server rejects the request. For an OPC message with such an ECC
                                             payload, the CTI Server sends the message without the ECC data. In this case, the following event is logged, “CTI Server was
                                             unable to forward ECC variables due to an overflow condition.” |
|---|---|

| Note | You cannot delete the Default payload. But, you can change its members. |
|---|---|

| Important | During upgrades, when the system first migrates your existing ECC variables to the Default payload, it does not check the
                                             CTI message size limit. The member names might exceed the extra 500 bytes that is allocated for ECC payloads to a CTI client.
                                             If the Default payload exceeds the limit, modify it to meet the limit. |
|---|---|

| Note | If your solution includes PGs from a previous release that does not support ECC payloads, the Router always sends the Default
                                             payload to those PGs. Those PGs can properly handle the Default payload. |
|---|---|

| Step 1 | On the ICM
                                          			 Configuration Manager, select Tools > Miscellaneous
                                                				  Tools > System Information and check the Enable expanded call context check box. |
|---|---|
| Step 2 | On the ICM
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Expanded Call Variable List . |
| Step 3 | In the
                                          			 Expanded Call Variable List window, enable the Add button by clicking Retrieve . |
| Step 4 | Click Add . The Attributes
                                             				property tab is enabled. |
| Step 5 | Create each
                                          			 of the variables in the following table by clicking Save after defining each variable. Note If you
                                                         				  change the configuration of any ECC variable with the Expanded Call Variable
                                                         				  List tool, stop and restart the Unified CVP Call Server. Caution It is
                                                         				  important that you enter the ECC's Name values listed in following table exactly as specified. If you do not, the
                                                         				  Unified ICME/ICMH software does not communicate with
                                                         				  the micro-applications on the ICM Service. Length values are more
                                             				flexible. Unless the values listed in following table are noted as "required,"
                                             				the value in the Length column is the maximum that Unified ICMH can handle for
                                             				that ECC. Specify a value between 1 and the maximum length. Note In a Unified
                                                         				  ICME/ICMH configuration, the ECC variable configuration, including the length,
                                                         				  defined in the NAM must be defined same in the CICM. If you create or modify the ECC variables while the Unified CVP ICM Service is running, you must restart the VRU PG during
                                                         non-production time or during a scheduled maintenance window for the changes to take full effect. To restart the VRU PG, access
                                                         the service control of the PG in ICM and restart the ICM PIM and Unified CVP Call Server. | Note | If you
                                                         				  change the configuration of any ECC variable with the Expanded Call Variable
                                                         				  List tool, stop and restart the Unified CVP Call Server. | Caution | It is
                                                         				  important that you enter the ECC's Name values listed in following table exactly as specified. If you do not, the
                                                         				  Unified ICME/ICMH software does not communicate with
                                                         				  the micro-applications on the ICM Service. | Note | In a Unified
                                                         				  ICME/ICMH configuration, the ECC variable configuration, including the length,
                                                         				  defined in the NAM must be defined same in the CICM. If you create or modify the ECC variables while the Unified CVP ICM Service is running, you must restart the VRU PG during
                                                         non-production time or during a scheduled maintenance window for the changes to take full effect. To restart the VRU PG, access
                                                         the service control of the PG in ICM and restart the ICM PIM and Unified CVP Call Server. |
| Note | If you
                                                         				  change the configuration of any ECC variable with the Expanded Call Variable
                                                         				  List tool, stop and restart the Unified CVP Call Server. |
| Caution | It is
                                                         				  important that you enter the ECC's Name values listed in following table exactly as specified. If you do not, the
                                                         				  Unified ICME/ICMH software does not communicate with
                                                         				  the micro-applications on the ICM Service. |
| Note | In a Unified
                                                         				  ICME/ICMH configuration, the ECC variable configuration, including the length,
                                                         				  defined in the NAM must be defined same in the CICM. If you create or modify the ECC variables while the Unified CVP ICM Service is running, you must restart the VRU PG during
                                                         non-production time or during a scheduled maintenance window for the changes to take full effect. To restart the VRU PG, access
                                                         the service control of the PG in ICM and restart the ICM PIM and Unified CVP Call Server. |
| Step 6 | Click Save to apply your changes. |

| Note | If you
                                                         				  change the configuration of any ECC variable with the Expanded Call Variable
                                                         				  List tool, stop and restart the Unified CVP Call Server. |
|---|---|

| Caution | It is
                                                         				  important that you enter the ECC's Name values listed in following table exactly as specified. If you do not, the
                                                         				  Unified ICME/ICMH software does not communicate with
                                                         				  the micro-applications on the ICM Service. |
|---|---|

| Note | In a Unified
                                                         				  ICME/ICMH configuration, the ECC variable configuration, including the length,
                                                         				  defined in the NAM must be defined same in the CICM. If you create or modify the ECC variables while the Unified CVP ICM Service is running, you must restart the VRU PG during
                                                         non-production time or during a scheduled maintenance window for the changes to take full effect. To restart the VRU PG, access
                                                         the service control of the PG in ICM and restart the ICM PIM and Unified CVP Call Server. |
|---|---|

| Name | Length | Definition |
|---|---|---|
| user.CourtesyCallbackEnabled | Required
                                             					 for using Courtesy Callback. Length:1 | Used to
                                             					 determine if Courtesy Callback must be offered to a caller. Valid
                                             					 values are: "1" = Yes "0" = No |
| user.cvp_server_info | Length: 15 | Used by
                                             					 Unified CVP to send the IP address of the Call Server sending the request to
                                             					 Unified ICME. Example:
                                             					 An IPv4 address like 192.168.150.181 |
| user.microapp.currency | Value: 6 | Currency
                                             					 type. |
| user.microapp.error_code | Value: 2 | Return
                                             					 status error code to be returned from the Unified CVP to Unified ICME/ICMH upon
                                             					 a False return code in the Run Script Result. |
| user.microapp.fetchaudio | Recommended length: 20; but length depends on the filename. | Filename for audio to be played  while the voice browser loads and processes the requested resource when there is significant network latency. Default:
                                             					 none Example:
                                             					 "flash:holdmusic.wav" Note This
                                                         						feature is not supported in Cisco VVB. | Note | This
                                                         						feature is not supported in Cisco VVB. |
| Note | This
                                                         						feature is not supported in Cisco VVB. |
| user.microapp.fetchdelay | Length: 1 | The length of time (in seconds) to wait at the start of the fetch delay before playing the audio specified by user.microapp.fetchaudio . This setting only takes effect if the value of fetchaudio is not empty. Default: 2 seconds; used to avoid a "blip" sound heard in a usual network scenario. Setting this value to zero plays hold music immediately, for a minimum of five seconds. Values: 1
                                             					 to 9 Note This feature is not supported in Cisco VVB. | Note | This feature is not supported in Cisco VVB. |
| Note | This feature is not supported in Cisco VVB. |
| user.microapp.fetchminimum | Length: 1 | The
                                             					 minimum length of time to play audio specified by user.microapp.fetchaudio , even if the requested resource
                                             					 arrives in the meantime. This setting only takes effect if value of fetchaudio
                                             					 is not empty. Default:
                                             					 5 seconds Values; 1
                                             					 to 9 Note This
                                                         						feature is not supported in Cisco VVB. | Note | This
                                                         						feature is not supported in Cisco VVB. |
| Note | This
                                                         						feature is not supported in Cisco VVB. |
| user.microapp.isPostCallSurvey | Length: 1 | Used to
                                             					 determine if post call survey must be offered to a caller after the agent hangs
                                             					 up. Valid
                                             					 values: "y" or "Y" is "Yes" "n" or
                                             					 "N" is "No" Default
                                             					 value is "Yes" |
| user.microapp.locale | Value: 5 | Locale, a
                                             					 combination of language and country which defines the grammar and prompt set to
                                             					 use. |
| user.microapp.media_server | Required for any IVR
                                             					 scripting. Maximum
                                             					 length: 210 characters Recommended length: 30 | Root of
                                             					 the URL for all media files and external grammar files used in the script. HTTP and
                                             					 HTTPS schemes can be specified as: HTTP
                                                   						  scheme is specified as "http://<servername>" HTTPS scheme is specified as "https://<servername>" |
| user.microapp.play_data | 40 | Default
                                             					 storage area for data for Play Data micro-application. |
| user.microapp.sys_media_lib | 10 | Directory for all system media files, such as individual digits, months,
                                             					 default error messages, and so forth. |
| user.microapp.app_media_lib | Maximum
                                             					 length: 210 characters Recommended length: 10 | Directory for all application-specific media files and grammar files. You can
                                             					 also set this value to ".." (literally two periods in quotes), which bypasses
                                             					 the user.microapp.app_media_lib and user.microapp.locale ECC Variables when
                                             					 writing a URL path. For example, if you set the user.microapp.app_media_lib to ".." , the path: http://server/locale/../hello.wav would
                                             					 really be: http://server/hello.wav |
| Note The
                                                      					 system and application media libraries need message and prompt files created or
                                                      					 recorded for each locale that is referenced. For more information, see Pass Data to Unified ICME . | Note | The
                                                      					 system and application media libraries need message and prompt files created or
                                                      					 recorded for each locale that is referenced. For more information, see Pass Data to Unified ICME . |
| Note | The
                                                      					 system and application media libraries need message and prompt files created or
                                                      					 recorded for each locale that is referenced. For more information, see Pass Data to Unified ICME . |
| user.microapp.grammar_choices | Configurable on Unified ICME .
                                             					 Maximum length: 210 characters. | Specifies the ASR choices that a caller can input for the Get Speech
                                             					 micro-application. Each option in the list of choices is delimited by a forward
                                             					 slash (/). Note If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. | Note | If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. |
| Note | If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. |
| user.microapp.inline_tts | Configurable on the ICM. Maximum length: 210 characters. | Specifies the text for inline Text To Speech (TTS). Note If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. | Note | If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. |
| Note | If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. |
| user.microapp.input_type | Value:
                                             					 1 | Specifies the type of input that is allowed. Valid
                                             					 contents are: D - DTMF B - (Both, the
                                                   						  default) DTMF and Voice If you
                                             					 are not using an ASR, you can set this variable to D. If you
                                             					 are using an ASR, you can set the variable to either D or B. Note With
                                                      					 input_mode set to "B" (both), either DTMF or speech is accepted,
                                                      					 but mixed mode input is not. Once you begin entering with one mode, input using
                                                      					 the other mode is ignored and has no effect. | Note | With
                                                      					 input_mode set to "B" (both), either DTMF or speech is accepted,
                                                      					 but mixed mode input is not. Once you begin entering with one mode, input using
                                                      					 the other mode is ignored and has no effect. |
| Note | With
                                                      					 input_mode set to "B" (both), either DTMF or speech is accepted,
                                                      					 but mixed mode input is not. Once you begin entering with one mode, input using
                                                      					 the other mode is ignored and has no effect. |
| user.microapp.caller_input | Configurable on Unified ICME/ICMH. Maximum length: 210 characters. | Storage
                                             					 area for any ASR input that is collected from Get Speech. Note Get
                                                      					 Speech text results are written to this ECC variable. Results
                                                      					 from Get Digits or Menu micro-applications are written to the
                                                      					 CED. | Note | Get
                                                      					 Speech text results are written to this ECC variable. Results
                                                      					 from Get Digits or Menu micro-applications are written to the
                                                      					 CED. |
| Note | Get
                                                      					 Speech text results are written to this ECC variable. Results
                                                      					 from Get Digits or Menu micro-applications are written to the
                                                      					 CED. |
| user.microapp.pd_tts | Value:
                                             					 1 | Specifies whether Unified CVP’s Text To Speech (TTS) or media files must be
                                             					 played to the caller. Valid
                                             					 contents are: Y - Yes, use TTS
                                                   						  capabilities N - No, do not use
                                                   						  TTS capabilities; play media files instead. Note Used
                                                      					 only with Play Data micro-application. | Note | Used
                                                      					 only with Play Data micro-application. |
| Note | Used
                                                      					 only with Play Data micro-application. |
| user.microapp.UseVXMLParams | Value:
                                             					 1 | This
                                             					 parameter specifies the manner in which you pass information to the external
                                             					 VoiceXML. Set this parameter to either "Y" (for yes) or "N" (for no). Y uses
                                             					 the values in the user.microapp.ToExtVXML variable array. N appends the
                                             					 name/value pairs in user.microapp.ToExtVXML to the URL of the external
                                             					 VoiceXML. Default:
                                             					 "N" |
| user.microapp.ToExtVXML | 210 | This
                                             					 variable array sends information to the external VoiceXML file. Must be
                                             					 configured as Array variables, not Scalar variables, even if the array length
                                             					 is set to 1. For more information on user.microapp.ToExtVXML variable
                                             					 length, see the Configure the CCE Script for Courtesy Callback section. |
| user.microapp.FromExtVXML | 210 | This
                                             					 variable array returns information from the external VoiceXML file. Must be
                                             					 configured as Array variables, not Scalar variables, even if the array length
                                             					 is set to 1. See Pass Data to Unified ICME for more information. For more information on user.microapp.FromExtVXML variable
                                             					 length, see the Configure the CCE Script for Courtesy Callback section. |
| user.microapp.override_cli | Configurable on Unified ICME/ICMH. Maximum length: 200 characters. | Used by
                                             					 system to override the CLI field on outgoing transfers. |
| user.microapp.metadata | The variable length would usually be configured as 62 bytes, but if ECC space is restricted, you can configure it as 21 bytes. | Following the Menu (M), Get Data (GD) and Get Speech (GS) micro-applications, Unified CVP returns information about the micro-application
                                             that is run. The
                                             					 user.microapp.metadata ECC variable is structured as follows: m\|con\|tr\|to\|iv\|duratn\|vruscriptname |
| user.microapp.uui | Configurable on Unified ICME/ICMH. Maximum length: 131 characters. | Used to
                                             					 pass user-to-user information back to Unified CVP from Unified ICME/ICMH. |
| user.sip.refertransfer | Optional Maximum
                                             					 length: 1 character. | SIP
                                             					 Service uses REFERs when transferring to the agents: y -
                                                   						  Use REFER when transferring n -
                                                   						  Do not use REFER when transferring |
| user.suppress.sendtovru | Optional Length:
                                             					 1 | Suppress the Temporary Connect message generated by SendToVRU node (explicitly
                                             					 or implicitly, for example by a Translation Route to VRU node). Used in
                                             					 call flows where the Temporary Connect is generated right before the Connect
                                             					 message (that is, no Run Script messages expected) to avoid the extra overhead
                                             					 of setting up a VRU leg temporarily before the Connect arrives. Valid
                                             					 values are: "y" or "Y" (yes, suppress the message) |
|  |  |  |

| Note | This
                                                         						feature is not supported in Cisco VVB. |
|---|---|

| Note | This feature is not supported in Cisco VVB. |
|---|---|

| Note | This
                                                         						feature is not supported in Cisco VVB. |
|---|---|

| Note | The
                                                      					 system and application media libraries need message and prompt files created or
                                                      					 recorded for each locale that is referenced. For more information, see Pass Data to Unified ICME . |
|---|---|

| Note | If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. |
|---|---|

| Note | If
                                                      					 text is placed in this variable that is longer than the variable is configured
                                                      					 to handle, only the first 210 characters are sent. |
|---|---|

| Note | With
                                                      					 input_mode set to "B" (both), either DTMF or speech is accepted,
                                                      					 but mixed mode input is not. Once you begin entering with one mode, input using
                                                      					 the other mode is ignored and has no effect. |
|---|---|

| Note | Get
                                                      					 Speech text results are written to this ECC variable. Results
                                                      					 from Get Digits or Menu micro-applications are written to the
                                                      					 CED. |
|---|---|

| Note | Used
                                                      					 only with Play Data micro-application. |
|---|---|

| Note | If your solution only has a Default payload, the solution automatically adds any new ECC variables to the Default payload
                                             until it reaches the 2000-byte limit. |
|---|---|

| Note | The tool checks that the ECC payload does not exceed the 2000-byte limit only when you save your changes. The counters on
                                             the Members tab only show what the current size is with all the selected members. They are only informational and do not enforce the
                                             limit. The limit is enforced when you attempt to save the changes. |
|---|---|

| Step 1 | In the Configuration Manager, open Tools > List Tools > Expanded Call Variable Payload List . The ECC Payload List window appears. |
|---|---|
| Step 2 | Click Retrieve to enable adding ECC payloads. |
| Step 3 | Click Add . The Attributes property tab appears. |
| Step 4 | Complete the Attributes property tab. See the List Tools Online Help for details on the Attributes property tab. |
| Step 5 | On the Members tab, click Add . A dialog box listing all the existing ECC variables appears. |
| Step 6 | Select the members for your ECC payload and click OK . Watch that the ECC Variable Size counter does not exceed 2000 bytes. For ECC payloads that go to CTI clients, watch that the CTI Message Size counter does not exceed 2500 bytes. |
| Step 7 | Click Save to apply your changes. |

| Metadata | ECC Variable Value |
|---|---|
| m | D, V or N  -  Indicates whether the user responded with Voice (V), DTMF
                                             (D), or not at all (N). (Note that for the Menu micro-application, any
                                             successful single digit entry will result in m being set to V or D, even if the
                                             entry was an invalid menu selection.) |
| con | 000
                                             to 100  -  Indicates the ASR percent confidence level at which the voice input
                                             was finally recognized. This field is only valid if m is Voice (V). |
| tr | 00 to 99  -  Indicates how many tries were required.
                                             01 means user responded successfully after the first
                                             prompt. |
| to | 00 to 99  -  Indicates how many timeouts occurred.
                                             Does not include interdigit timeouts. |
| iv | 00 to
                                             99  -  Indicates how many invalid entries were received, including interdigit
                                             timeouts. |
| duratn | 000000 to 999999  - 
                                             Indicates the micro-application duration in milliseconds. Duration is defined
                                             as the elapsed time between entering and exiting the RunExternalScript node, as
                                             measured in the IVR Service. |
| vru script name | Full name of the VRU script which was run. This is the only variable length field. |

| Note | This section is
                                          only applicable to call flow models which use the SendToVRU node to transfer
                                          the call to Unified CVP's VRU leg (it does not apply to Translation Route
                                          transfers). |
|---|---|

| Step 1 | On the
                                       			 Unified CM server, CCMAdmin Publisher, perform the following SIP-specific
                                       			 action: Add route
                                             				  patterns for outbound calls from the Unified CM devices using a SIP Trunk to the Unified CVP Call Server. Also, add a route
                                             				  pattern for error DN. Select Call Routing > Route/Hunt > Route Pattern > Add New and add the following: Route Pattern: Specify the route pattern; for example: 3XXX for a TDM phone that dials 9+3xxx and all Unified ICME scripts are set up for 3xxx dialed numbers. Gateway/Route List: Select the SIP Trunk defined in the previous substep. Note For
                                                            						warm transfers, the call from one agent to another does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the
                                                            						Unified CM server and associate that number with your peripheral gateway user
                                                            						(PGUSER) for the JTAPI gateway on the Unified CM peripheral gateway. An
                                                            						alternative is to use the Dialed Number Plan on Unified ICME to bypass the CTI
                                                            						Route Point. | Note | For
                                                            						warm transfers, the call from one agent to another does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the
                                                            						Unified CM server and associate that number with your peripheral gateway user
                                                            						(PGUSER) for the JTAPI gateway on the Unified CM peripheral gateway. An
                                                            						alternative is to use the Dialed Number Plan on Unified ICME to bypass the CTI
                                                            						Route Point. |
|---|---|---|---|
| Note | For
                                                            						warm transfers, the call from one agent to another does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the
                                                            						Unified CM server and associate that number with your peripheral gateway user
                                                            						(PGUSER) for the JTAPI gateway on the Unified CM peripheral gateway. An
                                                            						alternative is to use the Dialed Number Plan on Unified ICME to bypass the CTI
                                                            						Route Point. |
| Step 2 | Configure the
                                       			 peripheral gateways for the switch leg. On Unified
                                          				ICME, ICM Configuration Manager, PG
                                             				  Explorer tool: Configure
                                             				  each peripheral gateway (PG) to be used for the Switch leg. In the tree view pane, select the applicable peripheral gateway, and set
                                             				  the following: On the Logical Controller tab: Client Type: VRU Name: A name descriptive of this PG For example: <location>_A for side A of a particular location On the Peripheral tab: Peripheral Name: A name descriptive of this Unified CVP peripheral For example: <location>_<cvp1> or <dns_name> Client Type: VRU Select the check box: Enable Post-routing On the Routing Client tab: Name: By convention, use the same name as the peripheral. Client Type: VRU For more
                                                					 information, see the ICM Configuration Guide for
                                                   						Cisco ICM Enterprise Edition . Configure
                                             				  a peripheral for each Unified CVP Call Server to be used for a Switch leg
                                             				  connected to each PG. |
| Step 3 | Configure
                                       			 dialed numbers. On the
                                          				Unified ICME or Unified ICMH Server, in the ICM Configuration Manager,
                                          				configure the following items: Dialed Number List Tool tab: Configure the dialed numbers. Call Type List
                                                					 tool tab: Configure the call types. ICM Instance Explorer tool tab: Configure the applicable customers. For more
                                          				information, see the ICM Configuration Guide for
                                             				  Cisco ICM Enterprise Edition . |
| Step 4 | Create a
                                       			 Routing Script. On the Unified ICME or Unified ICMH Server in the ICM Script Editor tool: Create a routing script that handles the incoming call. The routing script must run a Label node or Select node (node that
                                          returns a label right away). Note Do not use
                                                      				  the Queue node in the routing script. The label
                                          				must be configured in the SIP Proxy Server to the IP address of the device that
                                          				the label corresponds to. The Proxy Server is optional. If you do not have one,
                                          				you must configure the Gateway dial-peer to point to the Call Server (refer to
                                          				the first step in this process). Also, you must configure the destination
                                             				  labels in the SIP Service for the Call Server. See the Scripting and Media Routing
                                             				  Guide for Cisco Unified ICM/Contact Center Enterprise & Hosted for
                                          				more information. | Note | Do not use
                                                      				  the Queue node in the routing script. |
| Note | Do not use
                                                      				  the Queue node in the routing script. |
| Step 5 | In the
                                       			 Operations Console, install and configure Call Servers. Enable the
                                             				  ICM and SIP Services on the Call Server. In the
                                                					 Operations Console, select Device
                                                      						  Management > Unified CVP Call Server . Select
                                                					 the check boxes: ICM and SIP Configure the SIP Service: Select Device
                                                      						  Management > CVP Call Server > SIP
                                                      						  tab . If
                                                      						  you are using a SIP Proxy Server, enable the Outbound Proxy and select the SIP
                                                      						  Proxy Server. If using a SIP Proxy Server, configure Local Static Routes on the
                                                      						  SIP Proxy Server itself. If
                                                      						  you are not using a SIP Proxy Server, configure Local Static Routes using the
                                                      						  Dialed Number Pattern system configuration in the Operations Console. A local
                                                      						  static route must be configured for each SIP gateway/ACD, SIP endpoint in order
                                                      						  to receive calls. Check the default values for the SIP Service and change, if desired. See the SIP Devices Configuration and SIP Dialed Number Pattern Matching Algorithm for detailed information. Configure the ICM Service by setting the maximum length DNIS to the length of
                                             				  the Network Routing Number: Select Device
                                                            								Management > CVP Call Server > ICM
                                                            								tab . Set
                                                      						  the Maximum Length of DNIS to length of the Network Routing Number. Example: For the Gateway dial pattern as 1800******, the maximum DNIS length is
                                                					 10. For
                                                					 detailed information, see the Operations Console Online Help . |

| Note | For
                                                            						warm transfers, the call from one agent to another does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the
                                                            						Unified CM server and associate that number with your peripheral gateway user
                                                            						(PGUSER) for the JTAPI gateway on the Unified CM peripheral gateway. An
                                                            						alternative is to use the Dialed Number Plan on Unified ICME to bypass the CTI
                                                            						Route Point. |
|---|---|

| Note | Do not use
                                                      				  the Queue node in the routing script. |
|---|---|

| Step 1 | Perform
                                       			 Steps 1 to 4 of the Set Up Type 8 VRU-Only Call Flow Model for ICME and ICMH procedure. |
|---|---|
| Step 2 | Define a
                                       			 Network VRU on Unified ICME or
                                       			 (for Unified ICMH ) on
                                       			 the NAM and each CICM. Using the ICM
                                          				Configuration Manager, the Network VRU Explorer tool, specify the following: Type: 8 Name: cvpVRU Note Although any
                                                      				  name works, cvpVRU is used by convention, and is an example name referenced in this guide. | Note | Although any
                                                      				  name works, cvpVRU is used by convention, and is an example name referenced in this guide. |
| Note | Although any
                                                      				  name works, cvpVRU is used by convention, and is an example name referenced in this guide. |
| Step 3 | Configure the
                                       			 Peripheral Gates (PGs) on Unified ICME or
                                       			 (for Unified ICMH ) on
                                       			 each CICM. Configure
                                             				  each PG. Configure
                                             				  a peripheral for each Unified CVP ICM Service connected to each PG. Use the ICM
                                          				Configuration Manager, the PG
                                             				  Explorer tool. For each Unified CVP ICM Service connected to this PG, in
                                          				the tree view pane, select the applicable PG and configure the following items: Logical
                                             				  Controller tab: Client
                                                					 Type: VRU Name: A
                                                					 name descriptive of this PG Example: <location>_A for side A of a particular location Peripheral tab: Peripheral Name: A name descriptive of this Unified CVP peripheral Examples: <location>_<cvp1> or <dns_name> Client
                                                					 Type: VRU Select
                                                					 the checkbox: Enable Post-routing Advanced tab: From the
                                                					 Network VRU field drop-down list, select the name: cvpVRU Routing Client tab: Name: By
                                                					 convention, use the same name as the peripheral. Client
                                                					 Type: VRU |
| Step 4 | Configure a
                                       			 Service and Route for each VRU on Unified ICME or (for Unified ICMH) on each
                                       			 CICM. Note You can also
                                                      				  use service arrays. See the Unified ICME documentation set for more
                                                      				  information. Using the ICM
                                          				Configuration Manager, the Service
                                             				  Explorer tool, specify the following: Service
                                                					 Name: cvpVRU Route
                                                					 Name: PeripheralName_cvpVRU Peripheral Number: 2 Must
                                                					 match the "Pre-routed Call Service ID" in the Call Server configuration on the
                                                					 ICM tab in the Operations Console Select
                                                					 the Enable Post-routing checkbox. | Note | You can also
                                                      				  use service arrays. See the Unified ICME documentation set for more
                                                      				  information. |
| Note | You can also
                                                      				  use service arrays. See the Unified ICME documentation set for more
                                                      				  information. |
| Step 5 | Define trunk
                                       			 groups. Note Configure
                                                      				  one Network Transfer Group and one associated Trunk Group for each VRU leg
                                                      				  Unified CVP ICM Service. Define and
                                          				configure the network trunk group on Unified ICME or
                                          				(for Unified ICMH ) on
                                          				each CICM. Using the ICM
                                          				Configuration Manager, the Network Trunk Group
                                             				  Explorer tool: Identify
                                             				  the network trunk group. Network Trunk Group Name: A name descriptive of this trunk group For each
                                             				  Unified CVP ICM Service for the VRU leg, configure an associated trunk group. Peripheral Name: A name descriptive of this trunk group Peripheral Number: 200 Must match the Pre-routed Call Trunk Group ID in the Call Server
                                                      						  configuration on the ICM tab in the Operations Console Trunk Count: Select Use Trunk Data from the drop-down list Do
                                                      						  not configure any trunks | Note | Configure
                                                      				  one Network Transfer Group and one associated Trunk Group for each VRU leg
                                                      				  Unified CVP ICM Service. |
| Note | Configure
                                                      				  one Network Transfer Group and one associated Trunk Group for each VRU leg
                                                      				  Unified CVP ICM Service. |
| Step 6 | Define
                                       			 translation route(s). Define and
                                          				configure a Translation Route for each VRU Peripheral on Unified ICME or
                                          				(for Unified ICMH )
                                          				on each CICM. On Unified ICME ,
                                          				ICM Configuration Manager, Translation Route Explorer tool: Define
                                             				  a Translation Route for each VRU Peripheral. Specify the following: Translation Route tab: Set
                                                      						  the Name field to the name of the target VRU peripheral. (This
                                                      						  is by convention; this value must be unique in the enterprise) Set
                                                      						  the Type field to DNIS and select the Service defined in the previous step Configure translation route and label information for each VRU peripheral.
                                             				  Complete the following: Route tab: Set
                                                      						  the Name : by convention, this is the name of the target VRU
                                                      						  peripheral, followed by the DNIS that this route will use, for example,
                                                      						  MyVRU_2000 This value must be unique in the enterprise Service Name drop-down list, select: PeripheralName.cvpVRU Peripheral Target tab: Enter the first DNIS that will be seen by the VRU that you will be using for
                                                      						  this translation route. Note The DNIS pool used for each VRU peripheral must be unique From the drop-down list, select a Network Trunk Group which belongs to the target VRU Label tab: Enter the translation route label (which might or might not be the same DNIS
                                                      						  you entered on the Peripheral Target tab) Type: Normal Routing Client: Select the NIC Routing Client Note You must create an additional label for each NIC routing client. Repeat the Route and corresponding Peripheral Target and Label
                                                                  							 information for each DNIS in the pool. | Note | The DNIS pool used for each VRU peripheral must be unique | Note | You must create an additional label for each NIC routing client. Repeat the Route and corresponding Peripheral Target and Label
                                                                  							 information for each DNIS in the pool. |
| Note | The DNIS pool used for each VRU peripheral must be unique |
| Note | You must create an additional label for each NIC routing client. Repeat the Route and corresponding Peripheral Target and Label
                                                                  							 information for each DNIS in the pool. |
| Step 7 | Create VRU
                                       			 and routing scripts. Create VRU
                                          				scripts and routing scripts for IVR treatment and agent transfer on Unified ICME or
                                          				(for Unified ICMH )
                                          				on each CICM . Using the
                                          				ICM Script
                                             				  Editor tool, create the VRU scripts and routing scripts to be used for IVR
                                          				treatment and agent transfer, as described in other sections of this manual and
                                          				in the ICM manuals. The VRU
                                          				scripts are associated with the applicable Network VRU. For
                                          				example, cvpVRU Use the ICM
                                          				Script Editor’s TranslationRouteToVRU node to connect the call to the Network
                                          				VRU. |
| Step 8 | Configure
                                       			 the ECC variables on Unified ICME or
                                       			 (for Unified ICMH )
                                       			 on the NAM and each CICM. Using the
                                          				ICM Configuration Manager, create the ECC variables. For more
                                          				information, see Define Unified CVP ECC Variables . |
| Step 9 | Configure
                                       			 dialed numbers and call types on Unified ICME or
                                       			 (for Unified ICMH )
                                       			 on the NAM and each CICM. On Unified ICME ,
                                          				using the ICM Configuration Manager, configure dialed numbers and call types. For more
                                          				information, see ICM Configuration Guide
                                             				  for Cisco ICM Enterprise Edition . |
| Step 10 | On Unified CM ,
                                       			 configure Unified CM. For more
                                          				information, see the Unified CM user
                                          				documentation. |
| Step 11 | Install and
                                       			 configure the Call Servers. Log in to
                                          				the Operations Console, select Device
                                                					 Management > CVP Call Server and install and
                                          				configure the Call Servers. Check the ICM and IVR check boxes. For
                                          				detailed information, see the Operations Console online help. |
| Step 12 | Configure
                                       			 the ICM service. On the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > ICM
                                                					 tab . On each Unified CVP Call Server, configure the ICM
                                             				  Service by specifying the following required information: VRU
                                             				  connection port number. Set the
                                                					 VRU Connection Port to match the VRU connection Port defined in ICM Setup for
                                                					 the corresponding VRU peripheral gateway (PIM). Maximum
                                             				  Length of DNIS. Set the
                                                					 maximum length DNIS to a number which is at least the length of the translation
                                                					 route DNIS numbers. Example: if the Gateway dial pattern is 1800******, the maximum DNIS length is
                                                					 10. Call
                                             				  service IDs: New Call and Pre-routed. Enter
                                                					 the new and pre-routed call service IDs. Configure the ports for both groups
                                                					 according to the licenses purchased, call profiles, and capacity by completing
                                                					 the required fields on this tab. Trunk
                                             				  group IDs: New Call and Pre-routed. Enter the new and pre-routed call trunk group IDs Configure the group number for the Pre-routed Call Trunk group. The group
                                                      						  number must match the trunk group number in the Network Trunk group used for
                                                      						  the translation route Configure the number of ports according to the licenses purchased and capacity Configure each of the numbers used for translation routes. (The "New Call" group is not used since the calls are being sent to
                                                      						  the VRU (Unified CVP) after some initial processing by the NIC/ Unified ICME ) Dialed
                                             				  numbers used in the translation route. Add the
                                                					 dialed numbers in the DNIS field. Check
                                             				  the default values of the other settings and change, if desired. |
| Step 13 | Configure
                                       			 the IVR Service. On the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > IVR tab. Check the
                                          				default values and change, if desired. Refer to
                                          				the Operations Console online help for information about other settings you
                                          				might want to adjust from their default values. |
| Step 14 | (Optional) Configure
                                       			 the Reporting Server. In the
                                          				Operations Console, select Device
                                                					 Management > CVP Reporting Server > General
                                                					 tab : Configure the Reporting Server. Select
                                                					 a Call Server to associate with this Reporting Server. Check
                                                					 the default values of the Reporting properties and change, if desired. For more
                                          				information, see Reporting Guide for Cisco
                                             				  Unified Customer Voice Portal |

| Note | Although any
                                                      				  name works, cvpVRU is used by convention, and is an example name referenced in this guide. |
|---|---|

| Note | You can also
                                                      				  use service arrays. See the Unified ICME documentation set for more
                                                      				  information. |
|---|---|

| Note | Configure
                                                      				  one Network Transfer Group and one associated Trunk Group for each VRU leg
                                                      				  Unified CVP ICM Service. |
|---|---|

| Note | The DNIS pool used for each VRU peripheral must be unique |
|---|---|

| Note | You must create an additional label for each NIC routing client. Repeat the Route and corresponding Peripheral Target and Label
                                                                  							 information for each DNIS in the pool. |
|---|---|

| Step 1 | Perform
                                       			 Steps 1 to 4 of the Set Up Type 8 VRU-Only Call Flow Model for ICME and ICMH procedure. |
|---|---|
| Step 2 | Configure
                                       			 each PG. On the NAM , ICM
                                          				Configuration Manager, PG
                                             				  Explorer tool: Configure
                                             				  each PG to be used for the VRU
                                                					 Client leg. Configure
                                             				  a peripheral for each Unified CVP ICM Service to be used as a VRU leg connected
                                             				  to each PG. For each
                                                					 Unified CVP ICM Service connected to this PG, in the tree view pane, select the
                                                					 applicable PG. Logical
                                                   						Controller tab, configure: Client Type: VRU Name:
                                                      						  A name descriptive of this PG For
                                                      						  example: <location>_A for side A of a particular location Peripheral tab,
                                                					 configure: Peripheral Name: A name descriptive of this VRU peripheral. For
                                                      						  example: <location>_<cvp1> or <dns_name> Client Type: VRU Select the checkbox: Enable Post-routing Routing Client tab: Name:
                                                      						  By convention, use the same name as the peripheral. Client Type: VRU |
| Step 3 | Define a
                                       			 Network VRU and labels. On the CICM ,
                                          				ICM Configuration Manager, Network VRU
                                             				  Explorer tool, define a Network VRU for the VRU leg and labels for reaching
                                          				the NAM. Specify the
                                          				following: Type: 7 Name: cvpVRU Note This
                                                         					 name is used by convention. Although any name will do, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. Define a Label for the NAM. Label:
                                                      						  Network routing number Type: Normal Routing client: Select the INCRP Routing Client from the drop-down list. | Note | This
                                                         					 name is used by convention. Although any name will do, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. |
| Note | This
                                                         					 name is used by convention. Although any name will do, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. |
| Step 4 | Define a
                                       			 Network VRU and a label for each NIC. On the NAM , ICM
                                          				Configuration Manager, Network VRU
                                             				  Explorer tool, define a Network VRU and a label for each NIC that is using
                                          				this VRU. Specify the
                                          				following: Type: 7 Name: cvpVRU Note This
                                                         					 name is used by convention. Although any name will work, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. Define a Label for each NIC that is using this VRU: Label:
                                                      						  Network routing number Type: Normal Routing client: Select the Routing Client for that NIC from the drop-down list. Note Ensure the
                                                   				Network VRU label is identical in the NAM and CICM. The Network VRU Name must
                                                   				be same to avoid confusion. | Note | This
                                                         					 name is used by convention. Although any name will work, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. | Note | Ensure the
                                                   				Network VRU label is identical in the NAM and CICM. The Network VRU Name must
                                                   				be same to avoid confusion. |
| Note | This
                                                         					 name is used by convention. Although any name will work, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. |
| Note | Ensure the
                                                   				Network VRU label is identical in the NAM and CICM. The Network VRU Name must
                                                   				be same to avoid confusion. |
| Step 5 | If there are
                                       			 Routing Scripts on the NAM, define a default Network VRU. On the NAM , ICM
                                          				Configuration Manager, System
                                             				  Information tool, in the General section: Define
                                                					 the Default Network VRU: cvpVRU |
| Step 6 | Define a
                                       			 default VRU. On the CICM ,
                                          				ICM Configuration Manager, System
                                             				  Information tool, in the General section: Define
                                                					 a default Network VRU: cvpVRU |
| Step 7 | Create the
                                       			 VRU and routing scripts. On the CICM ,
                                          				ICM Script
                                             				  Editor tool: Create the
                                          				VRU scripts and routing scripts to be used for IVR treatment and agent
                                          				transfer, as described in other sections of this manual and in the Unified ICME manuals. The VRU scripts are associated with the applicable Network VRU, that
                                          				is, cvpVRU . Use the ICM
                                          				Script Editor’s SendToVRU node to connect the call to the Network VRU. Note A RunVRU
                                                   				Script or Queue node is an implicit SendToVRU node, although error handling
                                                   				will be easier if the explicit SendToVRU node is used. | Note | A RunVRU
                                                   				Script or Queue node is an implicit SendToVRU node, although error handling
                                                   				will be easier if the explicit SendToVRU node is used. |
| Note | A RunVRU
                                                   				Script or Queue node is an implicit SendToVRU node, although error handling
                                                   				will be easier if the explicit SendToVRU node is used. |
| Step 8 | Configure
                                       			 the ECC variables. On the NAM and CICM ,
                                          				ICM Configuration Manager, configure the ECC variables. For more
                                          				information, see Define Unified CVP ECC Variables . |
| Step 9 | Configure
                                       			 dialed numbers and call types. On the NAM and CICM ,
                                          				ICM Configuration Manager, configure dialed numbers and call types. For more
                                          				information, see ICM Configuration Guide
                                             				  for Cisco ICM Enterprise Edition |
| Step 10 | Define
                                       			 customers. On the NAM and CICM ,
                                          				ICM Configuration Manager: If
                                             				  necessary, differentiate VRUs (Unified CVPs) based on dialed number. Define
                                             				  customers and their Network VRU. For more
                                          				information, see Common Configuration for Differentiating VRUs Based on Dialed Number . |
| Step 11 | On Cisco Unified CM ,
                                       			 configure Unified CM . For more
                                          				information, see the Unified CM user
                                          				documentation. |
| Step 12 | Install and
                                       			 configure the Call Server. In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server . Install
                                             				  and configure the Call Server. To
                                             				  enable the ICM and IVR Services on the Call Server, select the ICM and IVR check boxes. |
| Step 13 | Configure
                                       			 the ICM Service for each Call Server. In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > ICM
                                                					 tab . For each Unified CVP Call Server, configure the ICM
                                             				  Service by specifying the following required information: VRU
                                             				  connection port number. Set the
                                                					 VRU Connection Port to match the VRU connection Port defined in ICM Setup for
                                                					 the corresponding VRU peripheral gateway (PIM). Set the
                                             				  maximum length DNIS to the length of the Network Routing Number. Example: if the Gateway dial pattern is 1800******, the maximum DNIS length is
                                                					 10. Call
                                             				  service IDs: New Call and Pre-routed. Enter
                                                					 the new and pre-routed call service IDs. Configure the ports for both groups
                                                					 according to the licenses purchased, call profiles, and capacity by completing
                                                					 the required fields on this tab Trunk
                                             				  group IDs: New Call and Pre-routed. Enter
                                                					 the new and pre-routed call trunk group IDs. Configure the group number for the
                                                					 Pre-routed Call Trunk group. The group number must match the trunk group number
                                                					 in the Network Trunk group used for the translation route. Configure the number of ports according to the licenses purchased and capacity.
                                                					 Configure each of the numbers used for translation routes. (The New Call group is not used because the calls are
                                                					 sent to the VRU (Unified CVP) after an initial processing by the NIC/ Unified ICME ). Check
                                             				  the default values of other settings and change, if desired. |
| Step 14 | Configure
                                       			 the IVR service. In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > IVR and configure the IVR
                                             				  Service . Check the
                                          				default values and change, if desired. See the
                                          				Operations Console online help for information about settings. |
| Step 15 | (Optional)
                                       			 Configure the Reporting Server. On the
                                          				Operations Console, select Device
                                                					 Management > CVP Reporting Server > General and configure the Reporting
                                          				Server. Configure the Reporting Server. Select
                                             				  a Call Server to associate with this Reporting Server. Check
                                             				  the default values of the Reporting properties and change, if desired. For more information, see Reporting Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html . |

| Note | This
                                                         					 name is used by convention. Although any name will do, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. |
|---|---|

| Note | This
                                                         					 name is used by convention. Although any name will work, since it is referenced
                                                         					 elsewhere in this document, cvpVRU is assumed. |
|---|---|

| Note | Ensure the
                                                   				Network VRU label is identical in the NAM and CICM. The Network VRU Name must
                                                   				be same to avoid confusion. |
|---|---|

| Note | A RunVRU
                                                   				Script or Queue node is an implicit SendToVRU node, although error handling
                                                   				will be easier if the explicit SendToVRU node is used. |
|---|---|

| Note | The VRU PIM initiates
                                          the connection from the PG to the Call Server. The ICM Service listens for a
                                          connection from the VRU PIM. |
|---|---|

| Step 1 | Start the VXML Server. The VXML Server starts the VoiceXML Service
                                          using the DataFeed mechanism or the ReqICMLabel element. The ReqICMLabel element allows a Call Studio script to pass caller input,
                                             call variables, and External Call Context (ECC) variables to a
                                             Unified ICME script. The ReqICMLabel must be inserted into a
                                             Call Studio script as a decision element. In Call Studio, the returned
                                             Unified ICME label contains a result which can be used by
                                             other elements in the same application, such as the Transfer or Audio element.
                                             The Transfer element sends instructions to the IOS Voice Browser to transfer
                                             the caller to the desired location. After
                                             the VoiceXML Service starts, it starts communicating with the ICM
                                             Service. |
|---|---|
| Step 2 | Log in to the  Operations
                                          Console and configure a Call Server and ICM service. See Configure Call Server .
                                          See
                                          the Unified ICME documentation for instructions on configuring
                                          the VRU PIM to connect to a VRU. For example, Unified
                                          CVP. |

| Step 1 | Configure the gateway to send the call to a particular Unified CVP VXML Server
                                          application, as follows: dial-peer voice 8888 voip
                                    service [gateway application name]
                                    incoming called-number 888800....
                                    dtmf-relay rtp-nte
                                    codec g711ulaw
                                    no vad |
|---|---|
| Step 2 | To match the number in the Unified CVP VXML Server transfer node and send it out the T1 port to the G3 to its destination,
                                          use the following configuration: dial-peer voice 8880 pots
                                    destination-pattern 888800....
                                    incoming called-number
                                    direct-inward-dial
                                    port 1/0:D |

| Step 1 | To view CVPSNMPLogger for the Unified CVP VXML Server, access the Call Studio
                                          interface. |
|---|---|
| Step 2 | From Call Studio for each Call Studio application, right-click the application and
                                          select Properties > Cisco Unified CVP > General Settings . CVPSNMPLogger appears in
                                             the Loggers drop-down box. |

| Caution | Do not remove CVPSNMPLogger because doing so disables viewing of SNMP events and
                                          alerts. |
|---|---|