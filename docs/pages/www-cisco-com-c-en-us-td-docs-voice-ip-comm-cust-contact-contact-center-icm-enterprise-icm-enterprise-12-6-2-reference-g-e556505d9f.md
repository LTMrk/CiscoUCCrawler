---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-reference-g-e556505d9f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/reference/guide/ucce_b_acd-supplement-guide-for-avaya-12_6_2/ucce_m_post-routing-12_6_2.html
retrieved_at: 2026-08-16T19:46:03.148721+00:00
---

Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(2)

# Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(2)

Updated: April 28, 2023

Chapter: Post-Routing

## Chapter: Post-Routing

# Post-Routing

## Post Route Dial
                        	 Number Registration for TSAPI Interface

## Route
                        	 Request

To initiate a
                           		post-route, the Avaya vector that is handling the incoming call
                           		must include an adjunct route request step with the correct ASAI/CTI extension specified.

A wait
                              		  time is specified after the adjunct route request to allow for Unified ICM software to route the call. Although
                           		Unified ICM post-route destination decision is(virtually) instantaneous, a
                           		typical wait time of four to six seconds in the vector is appropriate. The wait
                           		time may require to be adjusted depending on anticipated call volumes.

Vector writers
                           		consider the state of the call, if Avaya cannot properly route the post-routed call,
                           		or if the CTI link is down. There can be a scenario, where the label (call
                           		destination) returned from the CallRouter is not valid. For example incorrect
                           		Trunk Access Code, extension destination is busied-out, Class of Restriction
                           		(COR) does not allow the call to complete. In this case, it is necessary for
                           		you to consider how you want the call to be handled.

### Route Request
                           	 Elements

Calling number
                                       			 (CLID)

Called number
                                       			 (typically the VDN)

User-user
                                       			 information (32 bytes maximum, where the data type is (a) user defined or (b)
                                       			 ASCII)

Last set of
                                       			 Avaya collected digits (CED) (if any)

Digit collection
                                       			 timeout (seconds)

Call priority
                                       			 level (values: not_used, not_in_queue, low, medium, high, top)

Interflow type
                                       			 (that is, cause of interflow; values: all, threshold, vector)

Time (time the
                                       			 routed call is to spend in the queue before interflow)

DNIS chars
                                       			 (optional)

Call ID

Trunk group number and trunk number (optional; mutually exclusive with calling number)

UCID

II -
                                       			 digits\Call Originator Information

### Route Request
                           	 Peripheral Variable Usage

If PIM is allowed
                              		Peripheral variable modification through Call Control Variable Map , the Route
                                 		  Request elements (such as CLID and Called Number) into Peripheral
                                 		  Variables . Unified ICM script writer can then use the information in
                              		the Peripheral
                                 		  Variables to create scripts that determine which destination best
                              		suits the caller's needs. All Peripheral
                                 		  Variable data types are ASCII.

The Call
                                 		  Control Variable Map field is available on the Peripheral
                                 		  Configuration window of the Configure
                                 		  ICM tool. This field controls the mapping of Route
                                 		  Request Elements to Peripheral
                                 		  Variables .

### Call Control
                           	 Variable Map

Direct the PIM . The PIM can be directed on which call variables are
                                       			 accessed. For example, the following setting (made in the Call Control Variable
                                       			 Map field) allows the PIM to set call variable 1 and call variables 5 through
                                       			 10. The call variables are set, while preserving the existing values of call
                                       			 variables 2 through 4 (which means that the PIM does not set call variables 2
                                       			 through 4). This argument is from the perspective of the PIM .

```
/PIM=ynnnyyyyyy
```

Direct the CTI portion of the PG. The CTI portion of the PG can be
                                       			 directed to allow the CTI Client to override any PIM Call Variable setting. For
                                       			 example, the following setting allows a CTI Client to set call variable 1 and
                                       			 call variables 5 through 10 while preserving the peripheral-determined values
                                       			 of call variables 2 through 4.

```
/CTI = ynnnyyyyyy
```

See also : For more details on Unified ICM CTI capabilities and interaction with the PG, see the ICM Software Enterprise CTI Interface Specification. The Route Select Peripheral Variable Map displays the Peripheral Variable numbers and the Route Request Elements which these numbers represent. It also displays the possible values contained in the Route Request Elements .

Peripheral Variable

Route
                                                      						Request Element

Possible Values

UUI data (ASCII and non-ASCII) is stored in the Termination call Detail table Unified ICM
                                             		  database. ICM Schema guide can be referred for more details.

## Route
                        	 Select

The PG receives the
                           		selected route information from the Call Router and converts it to a Route Select message for the Avaya . The Route
                              		  Select message can be used to set call attributes, request digit
                           		collection from the switch, provide dial-ahead digits to the switch for
                           		collection, or specify user-user information to be included in the call.

You can specify the Route
                              		  Select functionality through the Peripheral
                              		  Variables or the syntax used in the Label . Unified ICM script can be used to set the
                           		Peripheral Variable contents. Where the setting of Route Select functionality
                           		overlaps, the Peripheral Variable setting takes precedence.
                           		Refer to the Avaya documentation to determine when any of the
                           		Route Select features can be used. For example, it may not make sense to have
                           		call priority ON if the destination is a VDN or Split . As another example, direct agent calling does
                           		not make sense if the destination is a VDN .

### Route Select
                           	 Message

Destination
                                       			 route select. On-switch or off-switch called number.

User-user
                                       			 information.

DataType:
                                                				  (a) UU_TYPE_USER (user defined); or (b) UU_TYPE_IA5 (ASCII)

Length:
                                                				  number of bytes (40 bytes maximum)

Data

Call priority
                                       			 ( ON or OFF ). If ON , this parameter represents a special type
                                       			 of call. This call carries three burst distinctive ringing. The call does not
                                       			 go to the covering point for coverage or send all calls.

Agent
                                                				  extension.

ACD Split
                                                				  extension, specifies the queue, to place the waiting call. The agent must be
                                                				  logged in to this split.

User data type :

- COLLECT that specifies digits are to be
                                                   					 collected

COLLECTED , which specifies dial-ahead
                                                      						digits

The PIM
                                                				  default is COLLECTED .

Digit collection timeout
                                                   					 (0-63 seconds) : Specifies the number of seconds tone detector will continue
                                                				  to collect digits after the first digit is received. The PIM default is no timeout.

Data : If the user data
                                                				  type is COLLECT , this field is interpreted as a
                                                				  binary integer specifying the number of digits to collect. If the user data
                                                				  type is COLLECTED , this field is an ASCII string
                                                				  specifying the dial-ahead digits.

Use external trunk
                                                   					 identified by Trunk Access Code (TAC) . The TAC can be prefixed in the
                                                				  called_number field.

### Restrictions on
                           	 Digit Collection

Only incoming
                                       			 trunks of any type, including ISDN , MFC , and R2MFC , are eligible for ASAI/CTI-requested
                                       			 digit collection.

Incoming
                                       			 disconnect supervision must be administered on the incoming trunk to allow a
                                       			 call prompter/tone detector to connect.

### Route Select
                           	 Peripheral Variable Usage

The PG maps the Peripheral Variables received in the CallRouter’s Route Select message as shown in Table 9: Route Request
                              Peripheral Variable Map. All Peripheral Variable data types are ASCII. Peripheral Variables 1-4 and 6-10 are unassigned and
                              can be used for the Route Select elements shown in  Label Syntax table.

Peripheral
                                          				Variable

Route Select
                                          				element

Possible
                                          				Values

1-4, 6-10

Call Priority

CP_ON, CP_OFF
                                          				(default).

1-4, 6-10

Digit
                                          				Collection/Dial Ahead

See the topic
                                          				Digit Collection/Dial Ahead for more information.

1-4, 6-10

Trunk Access
                                          				Code

See the topic
                                          				Trunk Access Code for more information.

5

User-User
                                          				Information

See the topic
                                          				User-User Information for more information.

A Peripheral Variable
                              	 can only be used for one Route Select element at a time. If a Peripheral Variable syntax is invalid or the Peripheral Variable is an empty string, the Peripheral Variable is ignored. The only fixed Peripheral Variable is PV 5, that is designated for
                              	 UUI.

### Digit
                           	 Collection/Dial Ahead

The Digit
                              		Collection/Dial Ahead peripheral variable string has the following syntax:

```
COLLECT NUMBER_OF_DIGITS_TO_COLLECT TIMEOUT DIGIT_COLLECTION_TIMEOUT
```

or

```
DIAL DIAL_AHEAD_DIGITS
```

The number of
                                       			 digits to collect must be between one (1) and 24, inclusively.

All fields are
                                       			 separated by spaces.

Every # and *
                                       			 count as one digit each.

The digit
                                       			 collection timeout must be between one (1) and 31, inclusively.

The following
                              		example indicates that four digits are collected with a digit collection
                              		timeout of ten seconds:

```
COLLECT 4 TIMEOUT 10
```

The next example
                              		indicates that the digits 3, 2, 1 precedes the route selection:

```
DIAL 321
```

With proper
                              		configuration using translation routes, the DIAL syntax can allow you to
                              		provide the caller's ANI (or any set of digits) to the Avaya . Afterwards it is displayed on an agent's
                              		console.

### Trunk Access
                           	 Code

```
TAC TRUNK_ACCESS_CODE
```

TAC is a keyword delimiter and must be specified
                              		as shown (case is not important). The TRUNK_ACCESS_CODE field specifies a valid
                              		T runk Access Code extension for the Peripheral . The TAC can also be pre-pended in the Label. All
                              		fields must be space separated.

The following
                              		example indicates a Trunk Access Code of 111 for the route selection:

```
TAC 111
```

### User-user Information

This is a
                              		null-terminated ASCII character string. The UUI data is stored in Peripheral
                                 		  Variable 5 for both the Route Request and Route Select messages
                              		only if the protocol format of the UUI data is C_UU_IA5. Therefore, unless
                              		modified, all UUI data received for a call are included when sent to the calls'
                              		destination. UUI data is limited to 40 bytes.

Avaya PIM was
                              		designed to support the User-to-User information (UUI) up to 32 bytes inline
                              		with the older switch version support, which was 32 bytes.

ASAI supports UUI up
                              		to 96 bytes for Avaya
                                 		  CVLAN Server Release 8, and link version 4 and beyond.

With this
                              		enhancement Avaya
                                 		  PIM supports 40 bytes for the UUI field.

### Label
                           	 Syntax

The Unified
                                 		  ICM Label can be used to specify additional Route Select 1 functionality.
                              		Incorrect or incomplete Route Select data may result in the Avaya denying the Route Selection and proceeding with vector
                              		processing.

A special label type
                              		to support the incorporation of dial-ahead digits into the label is supported.
                              		The string DTMF within the label indicates the presence of
                              		these dial-ahead digits.

The format of this
                              		label type is as follows:

```
XXXXXDTMFYYYYY
```

The XXXXX is required and is the destination where the post-routed call are directed. YYYYY, maximum 16 digits (can include
                              * and #), are included as dial-ahead digits when the route response is sent to the switch for the post-routed call. This label
                              type can be used for post-routed or translation-routed calls. A label using this special label type cannot use any of the
                              other special label formatting capabilities listed in the following table Table 11: Label Identifiers and Capabilities. Peripheral
                              Variables can still be used.

Label
                                          				Identifiers

Definition

Example

!

An
                                          				exclamation point at the beginning of the label indicates that Call Priority are turned ON. The default is Call
                                          				Priority OFF.

See Note 1

!1234
                                          				indicates that the call directed to extension 1234 has call priority ON.

@

The “at” sign
                                          				(@) at the beginning of the label indicates that this is a DACD call. The call destination must be an agent’s
                                          				extension. The default is No DACD call. (See Note 1.)

@2345
                                          				indicates that the call directed to the agent at extension 2345 is a DACD call.
                                          				Because no agent group or agent group extension was specified in this example,
                                          				the PIM attempts to select the first known agent group login for the agent.
                                          				Both the agent and the destination agent group must have been previously known
                                          				to the PIM for this to be successful.

&

The ampersand
                                          				(&) used within the Label is used to specify the Agent Group Peripheral Number . The Agent Group
                                          				Peripheral Number must immediately follow the ampersand and must be configured
                                          				in Unified ICM software. The PIM determines the correct Agent Group extension.

@2345 &11
                                          				indicates that the call directed to the agent at extension 2345 is a DACD call and the agents group number is 11. Using
                                          				the Agent Group Peripheral number may be convenient if the agent group
                                          				extension is changed anytime.

#

The pound sign
                                          				(#) used within the Label is used to specify the Agent Group Extension number. The Agent Group Extension must immediately follow the
                                          				pound sign. The Agent must be a logged-in member of that agent group.

@2345 #1000
                                          				indicates that the call directed to the agent at extension 2345 is a DACD call
                                          				and the agents’ agent group extension is 1000.

%1

%2

.....

%10

The percent
                                          				sign ‘%’ at the beginning of the label indicates that the call destination is
                                          				contained in the specified Peripheral Variable number.

See Note 2

“%1” indicates
                                          				that the call destination is contained in Peripheral Variable 1 (PV1). This is
                                          				useful if you want to specify the destination in the PV’s or to place CEDs in a
                                          				PV as a destination.

All Label
                                                   			 Identifiers can be used together unless otherwise noted. Label Identifiers
                                                   			 designated to be at the beginning of the label cannot be preceded by any
                                                   			 digits. For example, "!%1" indicates a Priority call to the agent specified in
                                                   			 Peripheral Variable 1.

Peripheral
                                                   			 Variable 5 is reserved for User-User Information (UUI) only

1 ICM 5.0 SR13
                              	 supports star (*) as a valid routing label for translation routing and
                              	 post-routing in Avaya PIM. For example, *173001 is a valid routing label where
                              	 *17 can be the Trunk Access Code and 3001 indicates the extension/VDN to which
                              	 the call would be directed. The post-route label containing the star (*)
                              	 character is configured in Service explorer.

### Network Take-Back and Transfer Support

The Adjunct Switch Application Interface (ASAI) provides messages to enable an application (for example, the PG) to take advantage
                              of the Network Take-Back and Transfer feature. The message set enables a host to generate a transfer call request to the carrier.
                              Unified ICM customers currently perform the following actions when transferring inter-switch calls using Unified ICM Enterprise
                              Routing:

An agent receives an inbound call.

The agent begins a consultative call (#8XXX or speed dial #), which results in a new call in a VDN that performs a Post-Route
                                    Request.

The Unified ICM response to the Post-Route request is either of the following:

A VDN that targets another Switch using tie lines between ACDs.

A VDN that targets agent groups locally on the requesting ACD.

The agent then consults with the target agent and either conferences or transfers the call.

When inter-switch transfers are performed, the ACD requires trunk lines between all targeted ACDs.

The following steps are performed when transferring inter-switch calls using the Network Take-Back and Transfer feature:

An agent receives an inbound call.

The agent then starts a consultative call (#8XXX or speed dial #). A new call get initiated owing to the consult call, that
                                    runs a vector that performs a Post-Route Request.

Unified ICM response to the Post-Route request is a label of the form DTMF*8xxxxxxxx or DTMFD*8xxxxxxx. The DTMF and DTMFD
                                    prefix in the label informs the PIM that it must perform a Carrier Call Transfer.

PIM performs the following steps for Carrier Call Transfer:

The PG terminates or clears the consultative call that performed the post-route request by issuing a ClearCall Request.

When the PG receives a Clear Call confirmation response for the consult call disconnecting, the PG connects back the initial
                                    call that was placed on HOLD with the customer, by issuing a Retrieve Call Request. The feature requires that the call stays
                                    in the connected state to run the Carrier Call Transfer.

The DTMFD is similar to the DTMF prefix, except that DTMFD instructs the PG to disconnect the original call when the Send
                                    DTMF tone processing completes. This enables the PIM to clear the agent's association with the call if the DTMFD prefix is
                                    used (similar to a blind transfer case where the network clears the original call with the associated agent).

The PIM currently uses the Clear Call Request and Retrieve Call Request for CTI Third-Party Call Control Interfaces. These
                                    enable hands-free transfer steps after initiating the consultative call.

| Peripheral Variable | Route
                                                      						Request Element | Possible Values |
|---|---|---|
| 1 | CallPriorityLevel | CP_UNUSED, CP_NOT_IN_QUEUE, CP_LOW, CP_MEDIUM, CP_HIGH, CP_TOP |
| 2 | InterflowType | IT_UNUSED, IT_ALL, IT_THRESHOLD, IT_VECTOR |
| 3 | TimeInQBeforeInterflow | ASCII char string (empty string if unused), units = Seconds |
| 4 | DNIS | ASCII char string (empty string if unused) |
| 5 | User-User Information | See Note 1. |
| 6 | CED | Caller Entered Digits (empty string if unused) |
| 7 | II - digits \ UCID | II - digits (ASCII form) (empty string if unused) Note Peripheral Variable 7 is set to UCID value by TSAPI PIM. | Note | Peripheral Variable 7 is set to UCID value by TSAPI PIM. |
| Note | Peripheral Variable 7 is set to UCID value by TSAPI PIM. |
| 8 | Trunk Information | Format (if provided by switch): TrunkGroup Number, Trunk
                                                   					 Number, Trunk Direction |
| 9 | Calling Number | If provided by switch (for example if on ISDN trunks or
                                                   					 on-switch call) |
| 10 | VDN | Vector Directory Number |

| Note | Peripheral Variable 7 is set to UCID value by TSAPI PIM. |
|---|---|

| Note | The UUI is limited to ASCII characters (null-terminated ASCII character string). That is,
                                          		any non-ASCII UUI data received are not stored in the Peripheral Variable. UUI data (ASCII and non-ASCII) is stored in the Termination call Detail table Unified ICM
                                             		  database. ICM Schema guide can be referred for more details. |
|---|---|

| Peripheral
                                          				Variable | Route Select
                                          				element | Possible
                                          				Values |
|---|---|---|
| 1-4, 6-10 | Call Priority | CP_ON, CP_OFF
                                          				(default). |
| 1-4, 6-10 | Digit
                                          				Collection/Dial Ahead | See the topic
                                          				Digit Collection/Dial Ahead for more information. |
| 1-4, 6-10 | Trunk Access
                                          				Code | See the topic
                                          				Trunk Access Code for more information. |
| 5 | User-User
                                          				Information | See the topic
                                          				User-User Information for more information. |

| Label
                                          				Identifiers | Definition | Example |
|---|---|---|
| ! | An
                                          				exclamation point at the beginning of the label indicates that Call Priority are turned ON. The default is Call
                                          				Priority OFF. See Note 1 | !1234
                                          				indicates that the call directed to extension 1234 has call priority ON. |
| @ | The “at” sign
                                          				(@) at the beginning of the label indicates that this is a DACD call. The call destination must be an agent’s
                                          				extension. The default is No DACD call. (See Note 1.) | @2345
                                          				indicates that the call directed to the agent at extension 2345 is a DACD call.
                                          				Because no agent group or agent group extension was specified in this example,
                                          				the PIM attempts to select the first known agent group login for the agent.
                                          				Both the agent and the destination agent group must have been previously known
                                          				to the PIM for this to be successful. |
| & | The ampersand
                                          				(&) used within the Label is used to specify the Agent Group Peripheral Number . The Agent Group
                                          				Peripheral Number must immediately follow the ampersand and must be configured
                                          				in Unified ICM software. The PIM determines the correct Agent Group extension. | @2345 &11
                                          				indicates that the call directed to the agent at extension 2345 is a DACD call and the agents group number is 11. Using
                                          				the Agent Group Peripheral number may be convenient if the agent group
                                          				extension is changed anytime. |
| # | The pound sign
                                          				(#) used within the Label is used to specify the Agent Group Extension number. The Agent Group Extension must immediately follow the
                                          				pound sign. The Agent must be a logged-in member of that agent group. | @2345 #1000
                                          				indicates that the call directed to the agent at extension 2345 is a DACD call
                                          				and the agents’ agent group extension is 1000. |
| %1 %2 ..... %10 | The percent
                                          				sign ‘%’ at the beginning of the label indicates that the call destination is
                                          				contained in the specified Peripheral Variable number. See Note 2 | “%1” indicates
                                          				that the call destination is contained in Peripheral Variable 1 (PV1). This is
                                          				useful if you want to specify the destination in the PV’s or to place CEDs in a
                                          				PV as a destination. |

| Note | All Label
                                                   			 Identifiers can be used together unless otherwise noted. Label Identifiers
                                                   			 designated to be at the beginning of the label cannot be preceded by any
                                                   			 digits. For example, "!%1" indicates a Priority call to the agent specified in
                                                   			 Peripheral Variable 1. Peripheral
                                                   			 Variable 5 is reserved for User-User Information (UUI) only |
|---|---|