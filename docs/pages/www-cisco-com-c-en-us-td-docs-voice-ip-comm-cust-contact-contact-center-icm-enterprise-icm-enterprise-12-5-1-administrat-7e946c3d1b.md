---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-administrat-7e946c3d1b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_0110.html
retrieved_at: 2026-08-16T20:49:51.865038+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

Updated: February 7, 2019

Chapter: Dialed Number Plan

## Chapter: Dialed Number Plan

# Dialed Number Plan

## About Dialed Number Plan

The Dialed Number Plan allows you to manage and track agent-initiated
                           		calls.

The Dialed Number Plan applies only to calls initiated by the agent on
                           		their soft phone and not on their hard phone. Calls made on the hard phone are not
                           		subject to the permission, interpretation, translation, posting routing, and so
                           		on, specified in the Dialed Number Plan.

### Dialed Number Plan Explained

The Dialed Number Plan consists of a number of entries intended to
                                 		  accommodate the different types of calls agents might make. Each entry contains
                                 		  a wildcard string that is used to match a number that an agent might dial. Each
                                 		  digit of the string is processed until a matching dial plan entry is found.
                                 		  When found, the selected trunk group or resource is used to complete the call.

Each entry contains additional information indicating how to handle
                                 		  the calls matching that wildcard string.

For example, dialing a 9 to receive an outside line on a PBX or ACD is
                                 		  specified in the dial plan. All patterns that reference network trunks might
                                 		  begin with a "9" digit. Subsequent digits might be "1" for long distance
                                 		  patterns, "0" for operator assisted or international calls, "2" through "9" to
                                 		  specify an area code. The dial plan allows a customer to have multiple phone
                                 		  carrier trunks terminated at the PBX or ACD for different outbound call types.
                                 		  A customer might choose MCI as the long distance carrier while AT&T is the
                                 		  international carrier, and Bell Atlantic is the local carrier. The dial plan
                                 		  configuration is used to determine which carrier to use based on the patterns
                                 		  defined within the dial plan.

You use the Dialed Number Plan to:

Ensure agent-initiated calls are routed by a Unified ICM routing
                                       				script

Set up basic dialing substitutions

### Dialed Number Plan and Routing of Agent Calls

The most common and powerful use of the Dialed Number Plan is to ensure
                                 that agent-initiated calls are routed through the system software. In this
                                 case, you must specify that you want to request a PostRoute for the call and
                                 specify a dialed number associated with a routing script designed to handle the
                                 type of agent call.

Use this method of configuring the
                                 Dialed Number Plan for:

Agent-to-agent
                                       transfers

Agent-to-agent calling

Agent-initiated outbound calls

### Dialed Number Plan and Basic Dialing Substitutions

You can also use the Dialed Number Plan to specify basic dialing
                                 substitutions. In this scenario, you identify a wildcard pattern to match the
                                 number dialed by an agent. However, you do not request a Post Route and the
                                 call is not matched to a Dialed Number, and thus not
                                 routed by the system software. Instead, you enter the string you want to be
                                 dialed in the Dial String field. That string is used to place the agent's
                                 call.

Using the Dialed Number Plan in this way is most
                                 useful for setting up such things as:

Speed
                                       dial

Using alphanumeric characters to dial
                                       from a soft phone

## Dialed Number Plan
                        	 Values

Each field on the Dialed Number Plan dialog box is defined in the Configuration Manager online help. This section provides additional information about these
                              fields and how you can use them to set up agent dialing for your contact center.

### Wildcard Pattern

The wildcard pattern
                                 you enter can contain letters, digits, and number signs (#). It can also
                                 include the following wildcard characters.

Character

Description

?

Represents any single alphanumeric
                                             character.

!

Represents any string of character and can appear only at the end of a
                                             pattern.

### Routing Client

The Routing Client field lets you specify the routing client for the
                                 		  agent call. In Unified CCE configurations, set this field to identify the
                                 		  Unified CM PG.

### Post Route

Use the Post Route
                                 field to specify whether this type of agent call will be sent to a routing
                                 script. If you set Post Route to Yes , you must also enter a
                                 Dialed Number that is associated with a routing script designed to handle the
                                 type of agent call.

### Dialed Number

Use the Dialed Number field if you have set the Post Route field to Yes , indicating that you want a Unified ICM routing script to
                                 		  handle this agent call.

### Dial String

Use the Dial String field only when you set the Post Route field to No , indicating that you want to use this entry for dialing
                                 		  substitutions. This field cannot be used when PostRoute is selected to send the
                                 		  call to a Unified ICM routing script.

The Dial String field can contain wildcard characters used to
                                 		  translate the dialed number string provided by the agent to the dial string
                                 		  that will be delivered to the switching platform. The following table describes
                                 		  the wildcard characters that might appear in the DialString field.

Wildcard Character

Description

!

Matches any group of characters

?

Matches any single character

X or x

Excludes the character in the agent supplied dialed number
                                             						string at the position identified from the offset as defined from the beginning
                                             						of the DialedNumberPlan DialString field

The following table provides examples of the translation of a
                                 		  DialedNumber string specified by an agent to a resultant DialString as defined
                                 		  by the DialString entry of the matching DialedNumberPlan entry.

Agent Dialed Number

DialedNumber Plan Dial String

Dial string result

Description

5133

6100

6100

Direct substitution.

5133

6X???

6133

Partial replacement.

5133

!

5133

Complete Copy.

5133

9275!

92755133

Prefix Addition.

5133

62XX??

6233

First 2 char substitution.

5133

????

5133

Complete Copy.

5133

?XXX000

5000

Retain first character; substitute the remaining characters.

2755100

????200

2755200

Replace last three characters.

2755100

!220

2755100220

Suffix addition.

### Dial String Configuration for Speed Dialing

You
                                 can configure Static Dial String translations to provide speed dial
                                 capabilities. Here, you enter the abbreviated string an agent dials in the
                                 wildcard pattern. You enter the actual target number in the Dial String of the
                                 entry.

When a dialed number (provided by an agent) matches the
                                 wildcard pattern of the Dialed Number Plan entry, the Dial String configured
                                 entry is sent in place of the agent supplied Dialed Number string.

The following table provides an example of a speed dial
                                 configuration.

Agent Dialed Number

Wildcard Pattern

Dial String

Result

133

1??

919782755!

919782755133

### Dial String Configuration for Alphanumeric Substitutions

You can use the Dialed Number Plan to allow agents to specify an
                                 		  alphanumeric string when dialing. For instance, an agent might dial SALES when calling the sales department rather
                                 		  than a numeric value that might be harder to remember.

To configure an alphanumeric substitution, configure the alphanumeric
                                 		  dial string as the wildcard pattern and the target number as the Dial String of
                                 		  the DialedNumberPlan entry. When a dialed number provided by an agent matches
                                 		  the wildcard pattern of the Dialed Number Plan entry, the configured Dial
                                 		  String is sent in place of the agent supplied string.

You can combine wildcard characters with this feature to allow Alpha
                                 		  prefixes to be added to numbers to identify the location of the number.
                                 		  Examples are shown the following table.

Agent Dialed Number

DialedNumberPlan Dial String

Resultant Dial String

SALES

919782755100

919782755100

BOS5133

9782755133

9782755133

FL14Office1433

5133

5133

### Dial Number Type Plan

The Dial Number
                                 Type Plan lets you specify the type of call that will be placed.

Dialed Number Plan

Description

International

Allows agents to place calls
                                             classified as international calls.

National

Allows agents to place
                                             calls classified as national long distance calls.

Local

Allows agents to
                                             place calls classified as national local calls.

Operator Assisted

Allows
                                             agents to place calls classified as operator assisted
                                             calls.

PBX

Allows agents to place calls to agents on the same
                                             peripheral.

The options for
                                 this field map exactly with the options on the agent desk settings list window.
                                 The system software checks the agent desk settings for the agent placing the
                                 outbound call. agent desk settings define which types of calls agents are
                                 permitted to make. If the agent desk settings for an agent prevent them
                                 from placing a particular type of call (for instance, international), the call
                                 is not placed.

## Dialed Number Plan Configuration

### Use Dialed Number Plan to Ensure Routing of Agent Calls

Step 1

Create a routing script to handle each type of agent-initiated
                                          			 call using the Script Editor.

This step ensures agent-initiated calls are routed appropriately
                                             				by the system software.

The script can target agent, services, or skill groups using
                                             				Unified ICM script nodes. When a target is chosen, the associated label is sent
                                             				back to the requesting peripheral. The label value is substituted for the dial
                                             				string specified by the agent and sent to the switching platform to place the
                                             				outbound call.

Step 2

Select ICM Configuration
                                                				  Manager > Tools > List
                                                				  Tools > Call Type List .

Allows you to set up the call type and associate it with the
                                             				dialed number to target to routing scripts.

You can also use a pre-existing call type and script.

Step 3

Select ICM Configuration
                                                				  Manager > Tools > Bulk
                                                				  Configuration > Insert > Dialed Number
                                                				  Plan Bulk Insert and insert an entry in the Dialed
                                          			 Number Plan dialog.

Using the fields in this window, make sure to:

- Indicate the
                                                				  appropriate wildcard character.

- Set the Post Route
                                                				  text box to Yes .

- Select a valid Dialed
                                                				  Number associated with the routing script used to route the agent call.

- Set the Dial Number
                                                				  Type Plan to indicate the type of call.

This step matches the agent's dialed string to a Dialed Number.
                                             				This ensures the agent's call will be routed by a Unified ICM routing script.

Step 4

Select ICM Configuration
                                                				  Manager > Tools > List
                                                				  Tools > Agent Desk Settings List and ensure that Agent Desk Settings are set to identify the types of calls
                                          			 agents can place.

Ensures that agents are allowed to or restricted from placing
                                             				different types of outbound calls.

### Use Dialed Number
                           	 Plan to Set Up Basic Dialing Substitutions

Follow these steps to configure a Dialed Number Plan entry to do basic dialing substitutions:

Step 1

Insert an entry
                                          			 in the Dialed Number Plan dialog box by selecting ICM Configuration
                                                				  Manager > Tools > Bulk Configuration > Insert > Dialed Number Plan Bulk
                                                				  Insert .

Using the
                                             				fields in this window, make sure to:

- Indicate the appropriate
                                                				  wildcard character.

- Set the PostRoute field to No .

- Identify a valid Dial String
                                                				  used to place the call.

- Set the Dial Number Type Plan
                                                				  to indicate the type of call.

Matches the
                                             				agent's dialed string to the Dial String indicated in the entry. This Dial
                                             				String is used to place the call (the call will not be routed by the system
                                             				software).

Step 2

Ensure agent
                                          			 desk settings are set to identify the types of calls agents can place by
                                          			 selecting ICM Configuration
                                                				  Manager > Tools > List Tools > Agent Desk Settings
                                                				  List .

Ensures that
                                             				agents make only the types of outbound calls they are permitted to make.

For more information about Unified ICM Routing Scripts, see Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise

| Note | Do not confuse the Dialed Number Plan Bulk Insert tool with the
                                          		  Dialed Number Bulk Insert tool. |
|---|---|

| Character | Description |
|---|---|
| ? | Represents any single alphanumeric
                                             character. |
| ! | Represents any string of character and can appear only at the end of a
                                             pattern. |

| Wildcard Character | Description |
|---|---|
| ! | Matches any group of characters |
| ? | Matches any single character |
| X or x | Excludes the character in the agent supplied dialed number
                                             						string at the position identified from the offset as defined from the beginning
                                             						of the DialedNumberPlan DialString field |

| Agent Dialed Number | DialedNumber Plan Dial String | Dial string result | Description |
|---|---|---|---|
| 5133 | 6100 | 6100 | Direct substitution. |
| 5133 | 6X??? | 6133 | Partial replacement. |
| 5133 | ! | 5133 | Complete Copy. |
| 5133 | 9275! | 92755133 | Prefix Addition. |
| 5133 | 62XX?? | 6233 | First 2 char substitution. |
| 5133 | ???? | 5133 | Complete Copy. |
| 5133 | ?XXX000 | 5000 | Retain first character; substitute the remaining characters. |
| 2755100 | ????200 | 2755200 | Replace last three characters. |
| 2755100 | !220 | 2755100220 | Suffix addition. |

| Agent Dialed Number | Wildcard Pattern | Dial String | Result |
|---|---|---|---|
| 133 | 1?? | 919782755! | 919782755133 |

| Agent Dialed Number | DialedNumberPlan Dial String | Resultant Dial String |
|---|---|---|
| SALES | 919782755100 | 919782755100 |
| BOS5133 | 9782755133 | 9782755133 |
| FL14Office1433 | 5133 | 5133 |

| Dialed Number Plan | Description |
|---|---|
| International | Allows agents to place calls
                                             classified as international calls. |
| National | Allows agents to place
                                             calls classified as national long distance calls. |
| Local | Allows agents to
                                             place calls classified as national local calls. |
| Operator Assisted | Allows
                                             agents to place calls classified as operator assisted
                                             calls. |
| PBX | Allows agents to place calls to agents on the same
                                             peripheral. |

| Step 1 | Create a routing script to handle each type of agent-initiated
                                          			 call using the Script Editor. This step ensures agent-initiated calls are routed appropriately
                                             				by the system software. The script can target agent, services, or skill groups using
                                             				Unified ICM script nodes. When a target is chosen, the associated label is sent
                                             				back to the requesting peripheral. The label value is substituted for the dial
                                             				string specified by the agent and sent to the switching platform to place the
                                             				outbound call. |
|---|---|
| Step 2 | Select ICM Configuration
                                                				  Manager > Tools > List
                                                				  Tools > Call Type List . Allows you to set up the call type and associate it with the
                                             				dialed number to target to routing scripts. Note You can also use a pre-existing call type and script. | Note | You can also use a pre-existing call type and script. |
| Note | You can also use a pre-existing call type and script. |
| Step 3 | Select ICM Configuration
                                                				  Manager > Tools > Bulk
                                                				  Configuration > Insert > Dialed Number
                                                				  Plan Bulk Insert and insert an entry in the Dialed
                                          			 Number Plan dialog. Using the fields in this window, make sure to: Indicate the
                                                				  appropriate wildcard character. Set the Post Route
                                                				  text box to Yes . Select a valid Dialed
                                                				  Number associated with the routing script used to route the agent call. Set the Dial Number
                                                				  Type Plan to indicate the type of call. This step matches the agent's dialed string to a Dialed Number.
                                             				This ensures the agent's call will be routed by a Unified ICM routing script. |
| Step 4 | Select ICM Configuration
                                                				  Manager > Tools > List
                                                				  Tools > Agent Desk Settings List and ensure that Agent Desk Settings are set to identify the types of calls
                                          			 agents can place. Ensures that agents are allowed to or restricted from placing
                                             				different types of outbound calls. |

| Note | You can also use a pre-existing call type and script. |
|---|---|

| Step 1 | Insert an entry
                                          			 in the Dialed Number Plan dialog box by selecting ICM Configuration
                                                				  Manager > Tools > Bulk Configuration > Insert > Dialed Number Plan Bulk
                                                				  Insert . Using the
                                             				fields in this window, make sure to: Indicate the appropriate
                                                				  wildcard character. Set the PostRoute field to No . Identify a valid Dial String
                                                				  used to place the call. Set the Dial Number Type Plan
                                                				  to indicate the type of call. Matches the
                                             				agent's dialed string to the Dial String indicated in the entry. This Dial
                                             				String is used to place the call (the call will not be routed by the system
                                             				software). |
|---|---|
| Step 2 | Ensure agent
                                          			 desk settings are set to identify the types of calls agents can place by
                                          			 selecting ICM Configuration
                                                				  Manager > Tools > List Tools > Agent Desk Settings
                                                				  List . Ensures that
                                             				agents make only the types of outbound calls they are permitted to make. |