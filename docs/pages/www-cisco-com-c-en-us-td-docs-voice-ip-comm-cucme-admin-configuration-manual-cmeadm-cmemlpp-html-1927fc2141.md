---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmemlpp-html-1927fc2141
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmemlpp.html
retrieved_at: 2026-08-21T07:23:48.824213+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Multilevel Precedence and Preemption

## Chapter: Multilevel Precedence and Preemption

# Multilevel Precedence and Preemption

This document describes the Multilevel Precedence and Preemption (MLPP)
                        		service introduced in Cisco Unified Communications Manager Express 7.1
                        		(Cisco Unified CME).

## Prerequisites for MLPP

Cisco Unified CME 7.1

Cisco IOS Release 12.4(24)T

To use Cisco Unified CME basic automatic call distribution (B-ACD) and auto-attendant (AA) service as the MLPP attendant-console
                                 application, you must download and install the B-ACD scripts. These scripts are available from the Cisco Unified CME Software
                                 Download site at https://software.cisco.com/download/home/277641082 .

You can use your own audio files for the blocked precedence announcement and busy station not equipped for preemption announcement
                                 or you can use the audio files available from the Cisco Unified CME Software Download site at https://software.cisco.com/download/home/277641082 .

## Information About MLPP

Multilevel Precedence and Preemption (MLPP) service allows validated
                           		users to place priority calls, and if necessary, to preempt lower-priority
                           		calls. Precedence indicates the priority level of a call. Preemption is the
                           		process of terminating a lower-precedence call so a call of higher precedence
                           		can proceed. This capability assures high-ranking personnel can communicate
                           		with critical organizations and personnel during network stress situations,
                           		such as a national emergency or degraded network situation.

### Precedence

Precedence indicates the priority level associated with an MLPP call.
                              		Phone users can apply a precedence level when making a call.

You define an MLPP access digit in Cisco Unified CME and assign a
                              		maximum precedence level to individual phones. Phone users request a precedence
                              		call by dialing the access code NP, where N specifies the pre-configured access
                              		digit and P specifies the requested precedence level, followed by the phone
                              		number.

Table 28-1 lists the precedence levels that can be associated with an MLPP call in the Defense Switched Network (DSN) domain.

Level

Precedence

0 (high)

Flash Override

1

Flash

2

Immediate

3

Priority

4 (low)

Routine

Table 28-2 lists the precedence levels that can be associated with an MLPP call in the Defense Red Switched Network (DRSN) domain.

Level

Precedence

0 (high)

Flash Override Override

1

Flash Override

2

Flash

3

Immediate

4

Priority

5 (low)

Routine

A precedence call is any call with a precedence level higher than
                              		Routine. If precedence is not specifically invoked, the system processes a call
                              		using normal call processing and call forwarding.

Emergency 911 calls are automatically assigned precedence level 0.

Cisco Unified CME provides precedence indications to the source and
                              		destination of a precedence call, respectively, if either has MLPP indication
                              		enabled. For the source, this indication includes a precedence ringback tone
                              		and display of the precedence level of the call, if the device supports
                              		display. For the destination, the indication includes a precedence ringer tone
                              		and display of the precedence level of the call, if the device supports
                              		display.

#### Basic Precedence Call Setup

The following sequence of events occurs during the setup of a precedence
                                 		call:

Phone user goes off hook and dials a precedence call. The call
                                       			 pattern is NP-xxxx, where N is the precedence access digit, P is the precedence
                                       			 level for the call, and xxx is the extension or phone number of the called
                                       			 party.

The calling party receives the precedence ringback tone and the
                                       			 precedence display while the call is processing.

The called party receives the precedence ringer tone and the
                                       			 precedence display that indicates the precedence call.

##### Example

Party 1000 makes a precedence call to party 1001. To do so, party 1000
                                    		  dials the precedence call pattern, such as 80-1001.

While the call processes, the calling party (1000) receives the
                                    		  precedence ringback tone and precedence display on their
                                    		  Cisco Unified IP Phone. After acknowledging the precedence call, the called
                                    		  party (1001) receives a precedence ringer tone and a precedence display on
                                    		  their Cisco Unified IP Phone.

### Preemption

Preemption is the process of terminating an active call of lower
                              		precedence so a call of higher precedence can proceed. Preemption includes the
                              		notification and acknowledgment of preempted users and the reservation of
                              		shared resources immediately after preemption and before call termination.
                              		Preemption can take one of the following two forms:

User Access Preemption—This type of preemption applies to phones and
                                    			 other end-user devices. If a called party is busy with a lower precedence call,
                                    			 both the called party and the party to which it is connected, receive
                                    			 preemption notification and the existing call is cleared immediately.

For calls to Cisco Unified IP phones, the called party can hang up
                                    			 immediately to connect to the new higher precedence call, or if the called
                                    			 party does not hang up, Cisco Unified CME forces the phone on-hook after the
                                    			 configured preemption tone timer expires and connects the call.

For FXS ports, the called party must acknowledge the preemption by
                                    			 going on-hook, before being connected to the new higher precedence call.

Common Network Facility Preemption—This type of preemption applies
                                    			 to trunks. If all channels of a PRI trunk are busy with calls of lower
                                    			 precedence, a call of lower precedence is preempted to complete the higher
                                    			 precedence call.

Cisco Unified CME selects a trunk by first searching for an idle
                                    			 channel on all corresponding trunks (based on matching the called number in the
                                    			 dial peer).

If an idle channel is not found, Cisco Unified CME performs a
                                    			 preemptive-search by searching one trunk at a time for an idle channel. If no
                                    			 idle-channel is available on a trunk, preemption is performed on the lowest of
                                    			 lower-precedence calls corresponding to the trunk. If none of the calls
                                    			 corresponding to the trunk is of lower precedence, the next trunk is searched
                                    			 and so on.

SCCP phones support up to eight calls per directory number. When all
                              		lines are busy and a higher precedence MLPP call comes in, Cisco Unified CME
                              		preempts a lower precedence call on one of the channels of the directory
                              		number.

The maximum precedence level that a user can assign to an MLPP call
                              		originating from a specific phone is set using ephone templates and applied to
                              		individual phones. Calls from directory numbers that are shared by SCCP phones
                              		can have different maximum precedence levels, based on the precedence level of
                              		the phone.

#### Basic Preemption Call

Figure 28-1 shows an example of user access preemption.

In this example, the following sequence of events occurs:

User 1000 places a call with precedence level 1 (flash) to user 1001, and preemption is enabled for user 1001. In this example,
                                       user 1000 dials 81-1001 to place the precedence call.

User 1002 places a precedence call to user 1001 by dialing 80-1001. This call, which is of precedence level 0 (flash override),
                                       is a higher precedence call than the active precedence call.

Phone 1002 receives precedence display (flash override display), and the phones that are involved in the existing lower precedence
                                       call both play preemption tones (users 1000 and 1001).

To complete preemption, the parties who are involved in the lower precedence call hang up (users 1000 and 1001).

The higher level precedence call is offered to user 1001, who receives a precedence ringer tone (if MLPP indication is enabled).
                                       The calling party, user 1002, receives precedence ringback.

### DSN Dialing Format

Cisco Unified CME 8.0 and later releases provide complete support of the DSN dialing format, as outlined in Table 28-3 .

[Access-digit {Precedence-level |Service-digit}]

[Route-code]

[Area-code]

Switch-code

Line-number

[N {P | S}]

[1X]

[KXX]

KXX

XXXX

N is 2 - 9

P is 0 - 4

S is 5 - 9

X is 0 - 9

K is 2 - 8

#### Service Digit

The service digit provides information to the switch for connecting
                                 		calls to government or public telephone services or networks. The services are
                                 		reached through the trunk or route that is selected based on the dialed digits.
                                 		Phone users request a service by dialing the access code NS, where N specifies
                                 		the pre-configured access digit and S specifies the requested service, followed
                                 		by the phone number.

Table 28-4 lists the service digits supported in Cisco Unified CME 8.0 and later versions.

Service Digit

Precedence

5

Off-net 700 services

6

Not assigned

7

DSN CONUS FTS

8

Not assigned

9

Local PSTN

In Cisco Unified CME, the route pattern is configured to supply
                                 		secondary dial-tone and the remainder of the digits are collected and passed to
                                 		the PSTN trunk as the called number. The digits that follow the access digit
                                 		and service digit must be NANP compliant (E.164 number).

Cisco Unified CME provides secondary dial tone after the two digits and
                                 		then routes the call based on the remaining collected digits (using the dial
                                 		plan configuration). These services are assumed to be reached through the trunk
                                 		(or route) selected based on the dialed digits (dialed after the route digits).

#### Route Code

The route code allows a phone user to inform the switch of special
                                 		routing or termination requirements. The route code determines whether a call
                                 		uses circuit-switched data or voice-grade trunking and can be used to disable
                                 		echo suppressors and cancellers, and override satellite link control.

The first digit of the route code is 1. It is a required part of the
                                 		dialing plan to inform the switch that the next digit, the route digit,
                                 		provides network instructions for specialized routing. Phone users dial route
                                 		codes in the form 1X, where X is the route digit. The supported route digits
                                 		that a user can dial are 0 and 1.

Table 28-5 lists the route codes supported in Cisco Unified CME 8.0 and later versions:

Route Code

Use

Description

10

Voice call (default)

Any codec that carries voice or voice band data, such as G.711, G.729, or fax or modem pass-through.

11

Circuit-switched data

Any codec that carries unaltered DS0 traffic over IP (circuit emulation). For Cisco Unified CME, this is the audio/clearmode
                                             codec (RFC-4040).

#### Example for Dialing

If the first digit that the user dials is the configured access digit,
                                 		this indicates an access code where the next digit is either a precedence digit
                                 		or a service digit. If the next digit dialed is:

0-4—This is a precedence call. Cisco Unified CME sets the precedence
                                       			 indication, stores the precedence value, and discards the digits.

5-9—This is a call to a particular service. Cisco Unified CME passes
                                       			 the call to the designated trunk, discards the digits, and plays secondary dial
                                       			 tone.

If the first digit that the user dials or the next digit dialed after
                                 		the access code is:

1—This is a route code and the next digit is a route digit. The
                                       			 supported route digits that a user can dial are 0 and 1. Cisco Unified CME
                                       			 stores the route code for use later in route selection, sets a trunk-type
                                       			 indication, and discards the route code digits.

If the first digit that the user dials or the next digit dialed after
                                 		the access code or route code is:

2-8—This is the first digit of the area code or switch code. Area
                                       			 codes and switch codes in the DSN are allocated so there is no overlap. The
                                       			 area code and/or switch code are used for route selection.

### MLPP Service Domains

Cisco Unified CME 8.0 and later versions support MLPP service domains. A
                              		service domain consists of a group of MLPP subscribers and network resources.
                              		Calls and resources can only be preempted by higher-priority calls from MLPP
                              		subscribers within the same domain.

You can configure each device with a domain type, such as DSN or DRSN,
                              		and a domain identifier. You can assign a global MLPP domain type and
                              		identifier to the Cisco Unified CME router and assign different service domains
                              		to the individual phones registered to Cisco Unified CME through an ephone
                              		template. Calls from any phone that is not configured with a specific service
                              		domain use the global domain type and identifier.

The MLPP precedence and preemption applies only within the same domain.
                              		Only calls within the same domain can be preempted. If a call is placed between
                              		two subscribers with different MLPP service domains, Cisco Unified CME assigns
                              		the service domain of the originator to the call.

Figure 28-2 shows an example of preemption attempted across domains with different identifier numbers.

In the example shown in Figure 28-2 , the following sequence of events occurs:

User 1000, from service domain 0100, places a call with precedence
                                    			 level 1 (flash) to user 1001 in service domain 0200. The call is assigned
                                    			 domain number 0100 because that is the service domain of the call originator.

User 1002, from domain number 0200, places a precedence call to user
                                    			 1001. This call, which is of precedence level 0 (flash override), is a higher
                                    			 precedence call than the active precedence call.

The active call is not preempted because the incoming call is from a
                                    			 different service domain than the active call; a call from domain 0200 cannot
                                    			 preempt a call from domain 0100.

In the example shown in Figure 28-3 , the active call is not preempted because the incoming call is from a different domain type than the active call; a call
                              from the DSN cannot preempt a call from the DRSN.

In the example shown in Figure 28-4 , the active call is successfully preempted because the incoming call has the same domain type and identifier as the active
                              call.

### MLPP Indication

For basic MLPP calls with MLPP indication enabled, Cisco Unified CME
                              		instructs SCCP phones to play the precedence ringer tone and display the
                              		precedence level.

For basic MLPP calls with preemption involved and MLPP indication
                              		enabled, Cisco Unified CME instructs both parties to play the preemption tone
                              		and display the precedence level of the MLPP call on the phone.

For an MLPP call with call waiting, if MLPP indication is enabled,
                              		Cisco Unified CME instructs SCCP phones to play priority the call waiting tone
                              		instead of the regular call waiting tone.

Users receive an error tone if they attempt to make a call with a higher
                              		level of precedence than the highest precedence level that is authorized for
                              		their phone.

For example, user 1002 dials 80 to start a precedence call. Eight (8)
                              		represents the precedence access digit, and zero (0) specifies the precedence
                              		level that the user attempts to use. If this user is not authorized to make
                              		level 0 (flash override) precedence calls, the user receives an error tone.

### MLPP Announcements

Users who are unable to place MLPP calls receive announcements that detail the reasons why a call was unsuccessful. Table 28-6 lists the supported MLPP announcements.

Announcement

Condition

Blocked Precedence Announcement (BPA)

(Switch name and Location). Equal or higher precedence calls have prevented completion of your call. Please hang up and try
                                          again. This is a recording. (Switch name and Location).

An equal or higher precedence call is in progress.

Users receive the BPA if the destination party for the precedence call is off hook or if the destination party is busy with
                                          a precedence call of an equal or higher precedence.

BPA is not played if the destination party is configured for Call Waiting or Call Forwarding, or uses automatic call diversion
                                          to an attendant-console service.

Supported in Cisco Unified CME 7.1 and later versions.

Busy Not Equipped Announcement (BNEA)

(Switch name and Location). A service disruption has prevented the completion of your call. Please wait 30 minutes and try
                                          again. In case of emergency call your operator. This is a recording. (Switch name and Location).

Busy station not equipped for preemption.

Users receive the BNEA if the dialed number is busy and non-preemptable.

BNEA is not played if the dialed number is configured for Call Waiting or Call Forwarding, or has alternate party designations.

Supported in Cisco Unified CME 7.1 and later versions.

Isolated Code Announcement (ICA)

(Switch name and Location). A service disruption has prevented the completion of your call. Please wait 30 minutes and try
                                          again. In case of emergency call your operator. This is a recording. (Switch name and Location).

Operating or equipment problems encountered.

The complete trunk group including all routes is busied manually at either end of the circuit or the complete trunk group
                                          including all routes is in a carrier group alarm state (for example, Loss of Signal, Remote Alarm Indication, or Alarm Indication
                                          Signal).

Supported in Cisco Unified CME 8.0 and later versions.

Loss of C2 Features Announcement (LOC2)

-

Call leaves DSN.

Users receive the LOC2 announcement when the call leaves the Cisco Unified CME router on the trunk or when the user places
                                          a call to a different domain.

For example, DSN callers who place calls to locations that permit off-net terminations may receive an announcement informing
                                          them that they have left the DSN.

Supported in Cisco Unified CME 8.0 and later versions.

Unauthorized Precedence Level Announcement (UPA)

(Switch name and Location). The precedence used is not authorized for your line. Please use an authorized precedence or ask
                                          your attendant for assistance. This is a recording. (Switch name and Location).

Unauthorized precedence level is attempted.

Users receive the UPA when they attempt to make a precedence call by using a higher level of precedence than the highest precedence
                                          level that is authorized for their line.

Supported in Cisco Unified CME 8.0 and later versions.

Vacant Code Announcement (VCA)

(Switch name and Location). Your call cannot be completed as dialed. Please consult your directory and call again or ask your
                                          operator for assistance. This is a recording. (Switch name and Location).

No such service or invalid code.

Users receive the VCA when they dial an invalid or unassigned number.

Supported in Cisco Unified CME 8.0 and later versions.

### Automatic Call Diversion (Attendant Console)

Cisco Unified CME supports automatic diversion of all unanswered
                              		precedence calls above Routine to a designated directory number or attendant
                              		console after a selected period of time.

If automatic call diversion of MLPP calls is configured in
                              		Cisco Unified CME, it overrides the Call Forward settings on the phone for all
                              		incoming precedence calls above Routine and forwards these calls to the
                              		attendant-console application specified in the MLPP configuration.
                              		Cisco Unified CME treats MLPP calls with a precedence level of Routine as
                              		normal calls and honors the Call Forward setting configured on the phone.

How Cisco Unified CME handles forwarded MLPP calls depends on the
                              		following Call Forward options:

Call Forward All (CFA)—Precedence calls are routed to the target
                                    			 number of the attendant console immediately. The CFA target is not used for
                                    			 MLPP calls.

Call Forward Busy (CFB)—Precedence calls are forwarded to the
                                    			 configured CFB destination. If the CFB destination is Voice Mail or an off-net
                                    			 endpoint, the call is forwarded to the target number of the attendant-console
                                    			 service.

Call Forward No Answer (CFNA)—Precedence calls are forwarded to the
                                    			 configured CFNA destination. If the CFNA destination does not answer before the
                                    			 CFNA timer expires, or it is voice mail or an off-net endpoint, the call is
                                    			 forwarded to the target number of the attendant-console service.

Calls diverted to the attendant console are indicated by a visual signal
                              		and placed in the queue for attendant service by precedence and time interval.
                              		The call with the highest precedence and longest holding time is answered
                              		first. Attendant Queue Announcement is played to calls waiting in the queue for
                              		attendant service. Call distribution is performed to reduce excessive waiting
                              		time and each attendant position operates from a common queue.
                              		Cisco Unified CME supports attendant console service for MLPP using Basic
                              		Automatic Call Distribution (B-ACD) and auto-attendant (AA) service.

## Configure MLPP

### Enable MLPP Service Globally in Cisco Unified CME

This task covers the basic steps necessary to enable MLPP on the
                                 		  router.

Restriction

SIP phones are not supported.

Cisco Unified IP Phone 6900 Series phones are not supported.

Cisco Unified CME in SRST Fallback mode is not supported.

Supports only ISDN PRI E1 and T1interfaces.

Supports MLPP service within the local Cisco Unified CME router
                                                   				  only.

Cisco Unified CME 7.1 supports only Basic Calls, Call Forward,
                                                   				  Call Hold and Resume, Consultative Call-Transfer, and Call Waiting. Blind
                                                   				  Transfer is not supported.

Cisco Unified CME 8.0 and later versions support Three-Party Ad
                                                   				  Hoc Conferencing and Call Pickup.

Call Park Retrieval based on precedence level is not supported;
                                                   				  Cisco Unified CME must be configured to accept only one call per park slot.

#### Before you begin

Trunks must belong to a trunk group and have preemption enabled. For configuration information, see Enabling Preemption on the Trunk Group in Integrating Data and Voice Services for ISDN PRI Interfaces on Multiservice Access Routers .

### SUMMARY STEPS

- enable

- configure terminal

- voice mlpp

- access-digit digit

- bnea audio-url

- bpa audio-url

- upa audio-url

- service-domain { drsn | dsn } identifier domain-number

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice mlpp

#### Example:

```
Router(config)# voice mlpp
```

Enters voice MLPP configuration mode.

Step 4

access-digit digit

#### Example:

```
Router(config-voice-mlpp)# access-digit 8
```

Defines the access digit that phone users dial to make an MLPP call.

digit —Single-digit number that users dial. Range: 0 to 9. Default: 0.

Step 5

bnea audio-url

#### Example:

```
Router(config-voice-mlpp)# bnea flash:bnea.au
```

Specifies the audio file to play for the busy station not equipped for preemption announcement.

audio-url —Location of the announcement audio file in URL format. Valid storage locations are TFTP, FTP, HTTP, and flash memory.

Step 6

bpa audio-url

#### Example:

```
Router(config-voice-mlpp)# bpa flash:bpa.au
```

Specifies the audio file to play for the blocked precedence announcement.

Step 7

upa audio-url

#### Example:

```
Router(config-voice-mlpp)# upa flash:upa.au
```

Specifies the audio file to play for the unauthorized precedence announcement.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 8

service-domain { drsn | dsn } identifier domain-number

#### Example:

```
Router(config-voice-mlpp)# service-domain dsn 0010
```

(Optional) Sets the global MLPP domain type and number.

drsn —Defense Red Switched Network (DRSN).

dsn —Defense Switched Network (DSN). This is the default value.

domain-number —Number to identify the global domain, in three-octet format. Range: 0x000000 to 0xFFFFFF. Default: 0.

A phone uses this global domain for MLPP calls if it is not configured with the mlpp service-domain command.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 9

end

#### Example:

```
Router(config-voice-mlpp)# end
```

Exits to privileged EXEC mode.

#### Example

The following example shows MLPP enabled on the Cisco Unified CME
                                 		  router.

```
voice mlpp
		 access-digit 8
		 bpa flash:bpa.au
		 bnea flash:bnea.au
		 upa flash:upa.au
		 service-domain dsn identifier 000010
```

### Enable MLPP
                           	 Service on SCCP Phones

Restriction

The mlpp
                                                   				  max-precedence command is not supported in Cisco Unified CME 8.0
                                             			 and later versions; it is replaced by the mlpp
                                                   				  service-domain command.

#### Before you begin

MLPP must be
                                 		  enabled globally on the Cisco Unified CME router. See Enabling
                                    			 MLPP Service Globally in Cisco Unified CME .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- mlpp service-domain { drsn | dsn } identifier domain-number max-precedence level

- mlpp preemption

- mlpp indication

- exit

- ephone phone-tag

- ephone-template template-tag

- restart

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 15
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range: 1 to 20.

Step 4

mlpp service-domain { drsn | dsn } identifier domain-number max-precedence level

#### Example:

```
Router(config-ephone-template)# mlpp service-domain dsn identifier 0010 max-precedence 0
```

Sets the service domain and maximum precedence (priority) level for MLPP calls from this phone.

drsn —Phone belongs to the Defense Red Switched Network (DRSN).

dsn —Phone belongs to the Defense Switched Network (DSN). This is the default value.

domain-number —Number to identify the global domain, in three-octet format. Range: 0x000000 to 0xFFFFFF.

level —Maximum precedence level. Phone user can specify a precedence level that is less than or equal to this value.

DSN—Range: 0 to 4, where 0 is the highest priority.

DRSN—Range: 0 to 5, where 0 is the highest priority.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 5

mlpp preemption

#### Example:

```
Router(config-ephone-template)# no mlpp preemption
```

(Optional)
                                             				Enables calls on the phone to be preempted.

Preemption is enabled by default. Skip this step unless you want
                                                   					 to disable preemption with the no mlpp
                                                         						  preemption command.

Step 6

mlpp indication

#### Example:

```
Router(config-ephone-template)# no mlpp indication
```

(Optional)
                                             				Enables the phone to play precedence and preemption tones, and display the
                                             				preemption level of calls.

MLPP
                                                   					 indication is enabled by default. Skip this step unless you want to disable
                                                   					 MLPP indication with the no mlpp
                                                         						  indication command.

Step 7

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 8

ephone phone-tag

#### Example:

```
Router(config)# ephone 36
```

Enters
                                             				ephone configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks.

Step 9

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 15
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 10

restart

#### Example:

```
Router(config-ephone)# restart
```

Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information.

Restart
                                                         				  all ephones using the restart all command in telephony-service configuration mode.

Step 11

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows a basic configuration for three phones, all using template 1 with
                                 		  MLPP defined. Figure 28-5 shows an example of a precedence call using this configuration.

```
voice mlpp
		 access-digit 8
		 bpa flash:BPA.au
		 bnea flash:BNEA.au
		 upa flash:UPA.au
		
		ephone-template  1
		 mlpp service-domain dsn identifier 000000 max-precedence 0
		!Configures MLPP domain as DSN, identifier as 000000, and max-precedence set to 0
		
		ephone-dn  1
		 number  1001
		
		ephone-dn  2
		 number 1002
		
		ephone-dn 3 dual-line
		 number 1003
		 huntstop channel
		
		ephone 1
		 description Phone-A
		 mac-address 1111.2222.0001
		 button 1:1
		 ephone-template 1
		! MLPP configuration inherited from ephone-template 1
		
		ephone 2
		 description Phone-B
		 mac-address 1111.2222.0002
		 button 1:2
		 ephone-template 1
		
		ephone-3
		 description Phone-C
		 mac-address 1111.2222.0003
		 button 1:3
		 ephone-template 1
```

The huntstop
                                                   				  channel command must be configured on dual-line and octo-line
                                             			 directory numbers to preempt a call on those types of lines. Otherwise the
                                             			 dual-line or octo-line receives Call Waiting indication and the call is not
                                             			 preempted.

In this example,
                                 		  the following sequence of events occurs:

Phone A
                                       				places a precedence call to Phone C by dialing 831003 (access digit 8 +
                                       				precedence level 3 + destination number 1003).

Phone C
                                       				answers the call.

Phone C
                                       				hears the precedence ringer tone and Phone A hears the precedence ringback.

Phone B
                                       				places a higher precedence call to Phone C by dialing 821003. Phone A and Phone
                                       				C both hear the preemption tone for the duration of the preemption tone
                                             					 timer command (default value is three seconds).

Phone A is
                                       				preempted after three seconds.

Phone C
                                       				starts ringing (precedence ringer) and Phone B hears the precedence ringback.

Phone C
                                       				answers the call.

### Enable MLPP
                           	 Service on Analog FXS Phone Ports

#### Before you begin

MLPP must be
                                 		  enabled globally on the Cisco Unified CME router. See “Enabling
                                    			 MLPP Service Globally in Cisco Unified CME” .

### SUMMARY STEPS

- enable

- configure terminal

- voice-port port

- mlpp service-domain { drsn | dsn } identifier domain-number max-precedence level

- mlpp preemption

- mlpp indication

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice-port port

#### Example:

```
Router(config)# voice-port 0/1/0
```

Enters
                                             				voice-port configuration mode.

Port argument is platform-dependent; type ? to display
                                                   					 syntax.

Step 4

mlpp service-domain { drsn | dsn } identifier domain-number max-precedence level

#### Example:

```
Router(config-voiceport)# mlpp service-domain dsn identifier 0020 max-precedence 0
```

Sets the
                                             				service domain and maximum precedence (priority) level for MLPP calls from this
                                             				port.

drsn —Port belongs to the Defense Red Switched
                                                   					 Network (DRSN).

dsn —Port belongs to the Defense Switched Network
                                                   					 (DSN).

domain-number —Number to identify the global
                                                   					 domain, in three-octet format. Range: 0x000000 to 0xFFFFFF.

level —Maximum precedence level. Phone user can
                                                   					 specify a precedence level that is less than or equal to this value.

DSN—Range: 0 to 4, where 0 is the highest priority.

DRSN—Range: 0 to 5, where 0 is the highest priority.

This
                                                   					 command is supported in Cisco Unified CME 8.0 and later versions.

Step 5

mlpp preemption

#### Example:

```
Router(config-voiceport)# no mlpp preemption
```

(Optional)
                                             				Enables calls on the port to be preempted.

Preemption
                                                   					 is enabled by default. Skip this step unless you want to disable preemption
                                                   					 with the no mlpp
                                                         						  preemption command.

Step 6

mlpp indication

#### Example:

```
Router(config-voiceport)# no mlpp indication
```

(Optional)
                                             				Enables the phone to play precedence and preemption tones, and display the
                                             				preemption level of calls.

MLPP
                                                   					 indication is enabled by default. Skip this step unless you want to disable
                                                   					 MLPP indication with the no mlpp
                                                         						  indication command.

Step 7

end

#### Example:

```
Router(config-voiceport)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows that the analog FXS phone connected to voice port 0/1/0 can make
                                 		  MLPP calls with the highest precedence and its calls cannot be preempted.

```
voice-port 0/1/0
		 mlpp service-domain dsn identifier 000020 max-precedence 0
		 no mlpp preemption
		 station-id name uut1-fxs1
		 caller-id enable
```

### Configure an MLPP Service Domain for Outbound Dial Peers

To assign a service domain to MLPP calls that must leave the
                                 		  Cisco Unified CME router through the trunk, perform the following steps for the
                                 		  corresponding dial peer.

### SUMMARY STEPS

- enable

- configure terminal

- voice class mlpp tag

- service-domain { drsn | dsn }

- exit

- dial-peer voice tag { pots | voip }

- voice-class mlpp tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice class mlpp tag

#### Example:

```
Router(config)# voice class mlpp 1
```

Creates a voice class for the MLPP service.

tag —Unique number to identify the voice class. Range: 1 to 10000.

Step 4

service-domain { drsn | dsn }

#### Example:

```
Router(config-voice-class)# service-domain dsn
```

Sets the network domain in the MLPP voice class.

drsn —Defense Red Switched Network (DRSN).

dsn —Defense Switched Network (DSN).

Step 5

exit

#### Example:

```
Router(config-voice-class)# exit
```

Exits voice-class configuration mode.

Step 6

dial-peer voice tag { pots | voip }

#### Example:

```
Router(config)# dial-peer voice 101 voip
```

Enters dial peer voice configuration mode.

Step 7

voice-class mlpp tag

#### Example:

```
Router(config-dial-peer)# voice-class mlpp 1
```

Assigns a previously configured MLPP voice class to a POTS or VoIP dial peer.

tag —Unique number of the voice class that you created in Step 3.

Step 8

end

#### Example:

```
Router(config-dial-peer)# end
```

Exits dial-peer voice configuration mode.

#### Example

The following example shows an MLPP voice class defined for the DSN
                                 		  service domain. This voice class is assigned to a POTS dial peer so that calls
                                 		  leaving port 0/1/0 use the DSN protocol.

```
voice class mlpp 1
		 service-domain dsn
		!
		!
		dial-peer voice 1011 pots
		 destination-pattern 19101
		 voice-class mlpp 1
		 port 0/1/0
```

### Configure MLPP Options

To configure optional MLPP features or modify default settings,
                                 		  perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- voice mlpp

- preemption trunkgroup

- preemption user

- preemption tone timer seconds

- preemption reserve timer seconds

- service-domain midcall-mismatch { method1 | method2 | method3 | method4 }

- service-digit

- route-code

- attendant-console number redirect-timer seconds

- ica audio-url

- loc2 audio-url

- vca audio-url voice-class cause-code tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice mlpp

#### Example:

```
Router(config)# voice mlpp
```

Enters voice MLPP configuration mode.

Step 4

preemption trunkgroup

#### Example:

```
Router(config-voice-mlpp)# preemption trunkgroup
```

Enables preemption capabilities on a trunk group.

Step 5

preemption user

#### Example:

```
Router(config-voice-mlpp)# preemption user
```

Enables all supported phones to preempt calls.

Step 6

preemption tone timer seconds

#### Example:

```
Router(config-voice-mlpp)# preemption tone timer 15
```

Sets the amount of time that the preemption tone plays on the called phone when a lower precedence call is being preempted.

seconds —Expiry time, in seconds. Range: 3 to 30. Default: 0 (disabled).

Step 7

preemption reserve timer seconds

#### Example:

```
Router(config-voice-mlpp)# preemption reserve timer 10
```

Sets the amount of time to reserve a channel for a preemption call.

seconds —Range: 3 to 30. Default: 0 (disabled).

Step 8

service-domain midcall-mismatch { method1 | method2 | method3 | method4 }

#### Example:

```
Router(config-voice-mlpp)# service-domain midcall-mismatch method2
```

Defines the behavior when there is a domain mismatch between the two legs of a call.

method1 —Domain remains unchanged for each of the connections and the precedence level of the lower priority call changes to that
                                                   of the higher priority call. This is the default value.

method2 —Domain and precedence level of the lower priority call changes to that of the higher priority call.

method3 —Domain remains unchanged for each of the connections and the precedence levels change to Routine for both calls.

method4 —Domains change to that of the connection for which supplementary service was invoked (for example, transferee in case of
                                                   transfer). Precedence levels change to Routine for both calls.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 9

service-digit

#### Example:

```
Router(config-voice-mlpp)# service-digit
```

Enables phone users to request off-net services by dialing a
                                             				service digit.

This command is supported in Cisco Unified CME 8.0 and later
                                                   					 versions.

Step 10

route-code

#### Example:

```
Router(config-voice-mlpp)# route-code
```

Enables phone users to specify special routing for a call by
                                             				dialing a route code.

This command is supported in Cisco Unified CME 8.0 and later
                                                   					 versions.

Step 11

attendant-console number redirect-timer seconds

#### Example:

```
Router(config-voice-mlpp)# attendant-console 8100 redirect-timer 10
```

Specifies the telephone number of the MLPP attendant-console service where calls are redirected if the phone does not answer.

number —Extension or E.164 telephone number of the Cisco Unified CME basic automatic call distribution (B-ACD) and auto-attendant
                                                   (AA) service.

seconds —Number of seconds to wait for the phone to answer before redirecting the call.

Step 12

ica audio-url

#### Example:

```
Router(config-voice-mlpp)# ica flash:ica.au
```

(Optional) Specifies the audio file to play for the isolated code announcement.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 13

loc2 audio-url

#### Example:

```
Router(config-voice-mlpp)# loc2 flash:loc2.au
```

(Optional) Specifies the audio file to play for the loss of C2 features announcement.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 14

vca audio-url voice-class cause-code tag

#### Example:

```
Router(config-voice-mlpp)# vca flash:vca.au voice-class cause-code 29
```

(Optional) Specifies the audio file to play for the vacant code announcement.

tag —Number of the voice class that defines the cause codes for which the VCA is played. Range: 1 to 64.

This command is supported in Cisco Unified CME 8.0 and later versions.

Step 15

end

#### Example:

```
Router(config-voice-mlpp)# end
```

Exits to privileged EXEC mode.

#### Examples

The following example shows an MLPP configuration with optional
                                 		  parameters.

```
voice mlpp
		 preemption trunkgroup
		 preemption user
		 preemption tone timer 15
		 preemption reserve timer 10
		 access-digit 8
		 attendant-console 8100 redirect-timer 10
		 service-digit
		 route-code
		 bpa flash:bpa.au
		 bnea flash:bnea.au
		 upa flash:upa.au
		 ica flash:ica.au
		 loc2 flash:loc2.au
		 vca flash:vca.au voice-class cause-code 29
		 service-domain midcall-mismatch method2
		 service-domain dsn identifier 000010
```

### Troubleshooting MLPP Service

### SUMMARY STEPS

- enable

- debug ephone mlpp

- debug voice mlpp

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

debug ephone mlpp

#### Example:

```
Router# debug ephone mlpp
```

Displays debugging information for MLPP calls to phones in a
                                             				Cisco Unified CME system.

Step 3

debug voice mlpp

#### Example:

```
Router# debug voice mlpp
```

Displays debugging information for the MLPP service.

## Feature
                        	 Information for MLPP

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

MLPP Enhancements

8.0

Adds support for the following:

Additional MLPP announcements

Multiple service domains

Route codes and service digits

Interaction with supplementary services, such as Three-Way
                                                						  Conference, Call Pickup, and Cancel Call Waiting on Analog FXS ports

MLPP for Cisco Unified CME

7.1

Allows validated users to place priority calls, and if
                                          					 necessary, to preempt lower-priority calls.

| Level | Precedence |
|---|---|
| 0 (high) | Flash Override |
| 1 | Flash |
| 2 | Immediate |
| 3 | Priority |
| 4 (low) | Routine |

| Level | Precedence |
|---|---|
| 0 (high) | Flash Override Override |
| 1 | Flash Override |
| 2 | Flash |
| 3 | Immediate |
| 4 | Priority |
| 5 (low) | Routine |

| [Access-digit {Precedence-level \|Service-digit}] | [Route-code] | [Area-code] | Switch-code | Line-number |
|---|---|---|---|---|---|
| [N {P \| S}] | [1X] | [KXX] | KXX | XXXX |
| N is 2 - 9 | P is 0 - 4 | S is 5 - 9 | X is 0 - 9 | K is 2 - 8 |  |

| Service Digit | Precedence |
|---|---|
| 5 | Off-net 700 services |
| 6 | Not assigned |
| 7 | DSN CONUS FTS |
| 8 | Not assigned |
| 9 | Local PSTN |

| Route Code | Use | Description |
|---|---|---|
| 10 | Voice call (default) | Any codec that carries voice or voice band data, such as G.711, G.729, or fax or modem pass-through. |
| 11 | Circuit-switched data | Any codec that carries unaltered DS0 traffic over IP (circuit emulation). For Cisco Unified CME, this is the audio/clearmode
                                             codec (RFC-4040). |

| Announcement | Condition |
|---|---|
| Blocked Precedence Announcement (BPA) |
| (Switch name and Location). Equal or higher precedence calls have prevented completion of your call. Please hang up and try
                                          again. This is a recording. (Switch name and Location). | An equal or higher precedence call is in progress. |
| Users receive the BPA if the destination party for the precedence call is off hook or if the destination party is busy with
                                          a precedence call of an equal or higher precedence. BPA is not played if the destination party is configured for Call Waiting or Call Forwarding, or uses automatic call diversion
                                          to an attendant-console service. Supported in Cisco Unified CME 7.1 and later versions. |
| Busy Not Equipped Announcement (BNEA) |
| (Switch name and Location). A service disruption has prevented the completion of your call. Please wait 30 minutes and try
                                          again. In case of emergency call your operator. This is a recording. (Switch name and Location). | Busy station not equipped for preemption. |
| Users receive the BNEA if the dialed number is busy and non-preemptable. BNEA is not played if the dialed number is configured for Call Waiting or Call Forwarding, or has alternate party designations. Supported in Cisco Unified CME 7.1 and later versions. |
| Isolated Code Announcement (ICA) |
| (Switch name and Location). A service disruption has prevented the completion of your call. Please wait 30 minutes and try
                                          again. In case of emergency call your operator. This is a recording. (Switch name and Location). | Operating or equipment problems encountered. |
| The complete trunk group including all routes is busied manually at either end of the circuit or the complete trunk group
                                          including all routes is in a carrier group alarm state (for example, Loss of Signal, Remote Alarm Indication, or Alarm Indication
                                          Signal). Supported in Cisco Unified CME 8.0 and later versions. |
| Loss of C2 Features Announcement (LOC2) |
| - | Call leaves DSN. |
| Users receive the LOC2 announcement when the call leaves the Cisco Unified CME router on the trunk or when the user places
                                          a call to a different domain. For example, DSN callers who place calls to locations that permit off-net terminations may receive an announcement informing
                                          them that they have left the DSN. Supported in Cisco Unified CME 8.0 and later versions. |
| Unauthorized Precedence Level Announcement (UPA) |
| (Switch name and Location). The precedence used is not authorized for your line. Please use an authorized precedence or ask
                                          your attendant for assistance. This is a recording. (Switch name and Location). | Unauthorized precedence level is attempted. |
| Users receive the UPA when they attempt to make a precedence call by using a higher level of precedence than the highest precedence
                                          level that is authorized for their line. Supported in Cisco Unified CME 8.0 and later versions. |
| Vacant Code Announcement (VCA) |
| (Switch name and Location). Your call cannot be completed as dialed. Please consult your directory and call again or ask your
                                          operator for assistance. This is a recording. (Switch name and Location). | No such service or invalid code. |
| Users receive the VCA when they dial an invalid or unassigned number. Supported in Cisco Unified CME 8.0 and later versions. |

| Restriction | SIP phones are not supported. Cisco Unified IP Phone 6900 Series phones are not supported. Cisco Unified CME in SRST Fallback mode is not supported. Supports only ISDN PRI E1 and T1interfaces. Supports MLPP service within the local Cisco Unified CME router
                                                   				  only. Cisco Unified CME 7.1 supports only Basic Calls, Call Forward,
                                                   				  Call Hold and Resume, Consultative Call-Transfer, and Call Waiting. Blind
                                                   				  Transfer is not supported. Cisco Unified CME 8.0 and later versions support Three-Party Ad
                                                   				  Hoc Conferencing and Call Pickup. Call Park Retrieval based on precedence level is not supported;
                                                   				  Cisco Unified CME must be configured to accept only one call per park slot. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice mlpp Example: Router(config)# voice mlpp | Enters voice MLPP configuration mode. |
| Step 4 | access-digit digit Example: Router(config-voice-mlpp)# access-digit 8 | Defines the access digit that phone users dial to make an MLPP call. digit —Single-digit number that users dial. Range: 0 to 9. Default: 0. Note Your domain type must support the access digit that you select. For example, the valid range for the DSN is 2 to 9. | Note | Your domain type must support the access digit that you select. For example, the valid range for the DSN is 2 to 9. |
| Note | Your domain type must support the access digit that you select. For example, the valid range for the DSN is 2 to 9. |
| Step 5 | bnea audio-url Example: Router(config-voice-mlpp)# bnea flash:bnea.au | Specifies the audio file to play for the busy station not equipped for preemption announcement. audio-url —Location of the announcement audio file in URL format. Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
| Step 6 | bpa audio-url Example: Router(config-voice-mlpp)# bpa flash:bpa.au | Specifies the audio file to play for the blocked precedence announcement. |
| Step 7 | upa audio-url Example: Router(config-voice-mlpp)# upa flash:upa.au | Specifies the audio file to play for the unauthorized precedence announcement. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 8 | service-domain { drsn \| dsn } identifier domain-number Example: Router(config-voice-mlpp)# service-domain dsn 0010 | (Optional) Sets the global MLPP domain type and number. drsn —Defense Red Switched Network (DRSN). dsn —Defense Switched Network (DSN). This is the default value. domain-number —Number to identify the global domain, in three-octet format. Range: 0x000000 to 0xFFFFFF. Default: 0. A phone uses this global domain for MLPP calls if it is not configured with the mlpp service-domain command. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 9 | end Example: Router(config-voice-mlpp)# end | Exits to privileged EXEC mode. |

| Note | Your domain type must support the access digit that you select. For example, the valid range for the DSN is 2 to 9. |
|---|---|

| Restriction | The mlpp
                                                   				  max-precedence command is not supported in Cisco Unified CME 8.0
                                             			 and later versions; it is replaced by the mlpp
                                                   				  service-domain command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 15 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range: 1 to 20. |
| Step 4 | mlpp service-domain { drsn \| dsn } identifier domain-number max-precedence level Example: Router(config-ephone-template)# mlpp service-domain dsn identifier 0010 max-precedence 0 | Sets the service domain and maximum precedence (priority) level for MLPP calls from this phone. drsn —Phone belongs to the Defense Red Switched Network (DRSN). dsn —Phone belongs to the Defense Switched Network (DSN). This is the default value. domain-number —Number to identify the global domain, in three-octet format. Range: 0x000000 to 0xFFFFFF. level —Maximum precedence level. Phone user can specify a precedence level that is less than or equal to this value. DSN—Range: 0 to 4, where 0 is the highest priority. DRSN—Range: 0 to 5, where 0 is the highest priority. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 5 | mlpp preemption Example: Router(config-ephone-template)# no mlpp preemption | (Optional)
                                             				Enables calls on the phone to be preempted. Preemption is enabled by default. Skip this step unless you want
                                                   					 to disable preemption with the no mlpp
                                                         						  preemption command. |
| Step 6 | mlpp indication Example: Router(config-ephone-template)# no mlpp indication | (Optional)
                                             				Enables the phone to play precedence and preemption tones, and display the
                                             				preemption level of calls. MLPP
                                                   					 indication is enabled by default. Skip this step unless you want to disable
                                                   					 MLPP indication with the no mlpp
                                                         						  indication command. |
| Step 7 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 8 | ephone phone-tag Example: Router(config)# ephone 36 | Enters
                                             				ephone configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. |
| Step 9 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 15 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 10 | restart Example: Router(config-ephone)# restart | Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information. Note Restart
                                                         				  all ephones using the restart all command in telephony-service configuration mode. | Note | Restart
                                                         				  all ephones using the restart all command in telephony-service configuration mode. |
| Note | Restart
                                                         				  all ephones using the restart all command in telephony-service configuration mode. |
| Step 11 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Restart
                                                         				  all ephones using the restart all command in telephony-service configuration mode. |
|---|---|

| Note | The huntstop
                                                   				  channel command must be configured on dual-line and octo-line
                                             			 directory numbers to preempt a call on those types of lines. Otherwise the
                                             			 dual-line or octo-line receives Call Waiting indication and the call is not
                                             			 preempted. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice-port port Example: Router(config)# voice-port 0/1/0 | Enters
                                             				voice-port configuration mode. Port argument is platform-dependent; type ? to display
                                                   					 syntax. |
| Step 4 | mlpp service-domain { drsn \| dsn } identifier domain-number max-precedence level Example: Router(config-voiceport)# mlpp service-domain dsn identifier 0020 max-precedence 0 | Sets the
                                             				service domain and maximum precedence (priority) level for MLPP calls from this
                                             				port. drsn —Port belongs to the Defense Red Switched
                                                   					 Network (DRSN). dsn —Port belongs to the Defense Switched Network
                                                   					 (DSN). domain-number —Number to identify the global
                                                   					 domain, in three-octet format. Range: 0x000000 to 0xFFFFFF. level —Maximum precedence level. Phone user can
                                                   					 specify a precedence level that is less than or equal to this value. DSN—Range: 0 to 4, where 0 is the highest priority. DRSN—Range: 0 to 5, where 0 is the highest priority. This
                                                   					 command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 5 | mlpp preemption Example: Router(config-voiceport)# no mlpp preemption | (Optional)
                                             				Enables calls on the port to be preempted. Preemption
                                                   					 is enabled by default. Skip this step unless you want to disable preemption
                                                   					 with the no mlpp
                                                         						  preemption command. |
| Step 6 | mlpp indication Example: Router(config-voiceport)# no mlpp indication | (Optional)
                                             				Enables the phone to play precedence and preemption tones, and display the
                                             				preemption level of calls. MLPP
                                                   					 indication is enabled by default. Skip this step unless you want to disable
                                                   					 MLPP indication with the no mlpp
                                                         						  indication command. |
| Step 7 | end Example: Router(config-voiceport)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice class mlpp tag Example: Router(config)# voice class mlpp 1 | Creates a voice class for the MLPP service. tag —Unique number to identify the voice class. Range: 1 to 10000. |
| Step 4 | service-domain { drsn \| dsn } Example: Router(config-voice-class)# service-domain dsn | Sets the network domain in the MLPP voice class. drsn —Defense Red Switched Network (DRSN). dsn —Defense Switched Network (DSN). |
| Step 5 | exit Example: Router(config-voice-class)# exit | Exits voice-class configuration mode. |
| Step 6 | dial-peer voice tag { pots \| voip } Example: Router(config)# dial-peer voice 101 voip | Enters dial peer voice configuration mode. |
| Step 7 | voice-class mlpp tag Example: Router(config-dial-peer)# voice-class mlpp 1 | Assigns a previously configured MLPP voice class to a POTS or VoIP dial peer. tag —Unique number of the voice class that you created in Step 3. |
| Step 8 | end Example: Router(config-dial-peer)# end | Exits dial-peer voice configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice mlpp Example: Router(config)# voice mlpp | Enters voice MLPP configuration mode. |
| Step 4 | preemption trunkgroup Example: Router(config-voice-mlpp)# preemption trunkgroup | Enables preemption capabilities on a trunk group. |
| Step 5 | preemption user Example: Router(config-voice-mlpp)# preemption user | Enables all supported phones to preempt calls. |
| Step 6 | preemption tone timer seconds Example: Router(config-voice-mlpp)# preemption tone timer 15 | Sets the amount of time that the preemption tone plays on the called phone when a lower precedence call is being preempted. seconds —Expiry time, in seconds. Range: 3 to 30. Default: 0 (disabled). |
| Step 7 | preemption reserve timer seconds Example: Router(config-voice-mlpp)# preemption reserve timer 10 | Sets the amount of time to reserve a channel for a preemption call. seconds —Range: 3 to 30. Default: 0 (disabled). |
| Step 8 | service-domain midcall-mismatch { method1 \| method2 \| method3 \| method4 } Example: Router(config-voice-mlpp)# service-domain midcall-mismatch method2 | Defines the behavior when there is a domain mismatch between the two legs of a call. method1 —Domain remains unchanged for each of the connections and the precedence level of the lower priority call changes to that
                                                   of the higher priority call. This is the default value. method2 —Domain and precedence level of the lower priority call changes to that of the higher priority call. method3 —Domain remains unchanged for each of the connections and the precedence levels change to Routine for both calls. method4 —Domains change to that of the connection for which supplementary service was invoked (for example, transferee in case of
                                                   transfer). Precedence levels change to Routine for both calls. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 9 | service-digit Example: Router(config-voice-mlpp)# service-digit | Enables phone users to request off-net services by dialing a
                                             				service digit. This command is supported in Cisco Unified CME 8.0 and later
                                                   					 versions. |
| Step 10 | route-code Example: Router(config-voice-mlpp)# route-code | Enables phone users to specify special routing for a call by
                                             				dialing a route code. This command is supported in Cisco Unified CME 8.0 and later
                                                   					 versions. |
| Step 11 | attendant-console number redirect-timer seconds Example: Router(config-voice-mlpp)# attendant-console 8100 redirect-timer 10 | Specifies the telephone number of the MLPP attendant-console service where calls are redirected if the phone does not answer. number —Extension or E.164 telephone number of the Cisco Unified CME basic automatic call distribution (B-ACD) and auto-attendant
                                                   (AA) service. seconds —Number of seconds to wait for the phone to answer before redirecting the call. |
| Step 12 | ica audio-url Example: Router(config-voice-mlpp)# ica flash:ica.au | (Optional) Specifies the audio file to play for the isolated code announcement. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 13 | loc2 audio-url Example: Router(config-voice-mlpp)# loc2 flash:loc2.au | (Optional) Specifies the audio file to play for the loss of C2 features announcement. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 14 | vca audio-url voice-class cause-code tag Example: Router(config-voice-mlpp)# vca flash:vca.au voice-class cause-code 29 | (Optional) Specifies the audio file to play for the vacant code announcement. tag —Number of the voice class that defines the cause codes for which the VCA is played. Range: 1 to 64. This command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 15 | end Example: Router(config-voice-mlpp)# end | Exits to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | debug ephone mlpp Example: Router# debug ephone mlpp | Displays debugging information for MLPP calls to phones in a
                                             				Cisco Unified CME system. |
| Step 3 | debug voice mlpp Example: Router# debug voice mlpp | Displays debugging information for the MLPP service. |

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| MLPP Enhancements | 8.0 | Adds support for the following: Additional MLPP announcements Multiple service domains Route codes and service digits Interaction with supplementary services, such as Three-Way
                                                						  Conference, Call Pickup, and Cancel Call Waiting on Analog FXS ports |
| MLPP for Cisco Unified CME | 7.1 | Allows validated users to place priority calls, and if
                                          					 necessary, to preempt lower-priority calls. |