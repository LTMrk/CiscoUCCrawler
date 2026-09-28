---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-routing-dial-plans-64020-number-voice-translation-profiles-html-763ff119d3
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-routing-dial-plans/64020-number-voice-translation-profiles.html
retrieved_at: 2026-08-16T23:24:39.828568+00:00
---

Configure Number Translation with Voice Translation Profiles

# Configure Number Translation with Voice Translation Profiles

### Download Options

Updated: September 10, 2024

Document ID: 64020

Contents

## Contents

## Introduction

This document describes how to configure number translation with the Voice Translation Profiles.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on the Voice Gateways that run Cisco IOS®Software Release 12.2(11)T or later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

### Conventions

Refer to the Cisco Technical Tips Conventions for more information on document conventions.

## Background Information

Voice Translation Profiles introduce a new scheme to translate numbers. The older translation rules are to be gradually phased out of the system. Cisco strongly recommends you only use one scheme of translation rules. If you mix the old and new schemes, you can have unforeseen results. Central to the new scheme is the ability to perform regular expression matches and replace sub strings. The Stream Editor (SED) utility is used to translate numbers. See the Related Information section for more information on SED.

This document describes highlighted features and configurations for new Voice Translation Profiles and specific examples for the most common scenarios.

The translation rules replace a sub string of the input number if the number matches the match pattern, number plan, and type present in the rule. The SED utility is used to check for a match based on the match pattern. Another ability of the translation rules is the ability to block calls on specific numbers. These rules are specified with a special keyword called 'reject'.

Features:

New translation rules come after regular expression that match in a way similar to SED:

An escape sequence similar to UNIX via backslashes is supported.

The keywords NULL and ANY are not supported in new translation rules, but these keywords can be replaced by regular expressions similar to SED.

Up to fifteen translation rules can be defined per translation rule table.

Up to 1000 translation profiles can be defined. Up to 128 translation rules can be defined.

## Configure

This section presents you with the information used to configure the features described in this document.

Note : Use the Command Lookup Tool to find more information on the commands used in this document. Only registered Cisco users can access internal Cisco tools and information.

### Assign Translation Profiles

New translation rules can be referenced by a translation profile. You can define these types of call numbers in a translation profile:

Called

Calling

Redirect-called

Each type of call number in the profile can have different translation rules.

Once a translation profile is defined, it can be referenced by:

Trunk Group—Two different translation profiles can be defined in a trunk group in order to perform number translation for incoming and outgoing POTS calls. If an outgoing translation profile is defined in a trunk group, the number translation is done while the outgoing call is setup.

Source IP Group—A translation profile can be defined in a source IP group in order to perform number translation for incoming VoIP calls.

Dial Peer—Two different translation profiles can be defined in a dial peer in order to perform number translation for incoming and outgoing calls.

Voice Port—The translation profile can be defined in a voice port in order to perform number translation for incoming and outgoing POTS calls. If a voice port is also a trunk group member, then the incoming translation profile of a voice port overrides the translation profile of a trunk group.

Non-Facility Associated Signaling (NFAS) Interface—The translation profile can be defined for an NFAS interface through the translation-profile command line from the global voice service pots configuration in order to perform the number translation for incoming and outgoing NFAS calls. This translation profile has a higher precedence than the translation profile of a voice port and trunk group in case a channel also belongs to a voice port and/or trunk group with the translation profile defined.

VoIP Incoming—The translation profile can be defined globally for all incoming VoIP (h323/sip) calls in order to perform number translation. If an incoming H.323/SIP call is associated with a Source IP Group with a translation profile defined, then the translation profile of the Source IP Group overrides the global translation profile for incoming VoIP calls.

### Voice Translation-rule Command

Issue the voice translation-rule command in global configuration mode in order to define a translation rule for voice calls. Use the no form of this command in order to delete the translation rule.

voice translation-rule number

no voice translation-rule number

Note : The number parameter is the unique identifier for the translation rule. The range is from 1 to 2147483647. There is no default.

#### rule (voice translation-rule)

In order to define a translation rule, use the rule command in voice translation-rule configuration mode. In order to delete the translation rule, use the no form of this command.

Match and Replace Rule

```
rule precedence /match-pattern/ /replace-pattern/ [type { match-type replace-type } [plan { match-type replace-type }]] no rule precedence
```

Reject Rule

```
rule precedence reject / match-pattern / [type match-type [plan match-type ]] no rule precedence
```

#### Syntax Description

abbreviated

any

international

national

network

reserved

- subscriber

- unknown

- abbreviated

- international

- national

- network

- reserved

- subscriber

- unknown

- any

- data

- ermes

- isdn

- national

- private

- reserved

- telex

- unknown

- data

- ermes

- isdn

- national

- private

- reserved

- telex

- unknown

#### Example

This example initiates translation rule 150. This includes two rules:

```
Router(config)# voice translation-rule 150 Router(cfg-translation-rule)# rule 1 reject /^919\(.(\)/ Router(cfg-translation-rule)# rule 2 /\(^...\)853\(...\)/ /\1525\2/
```

The voice translation rules use characters similar to Regular Expression Syntax (regexp), but there are some minor differences and limitations. Most of the limitations are of no real concern since only digit manipulation is performed.

```
/^$/
```

```
/ /
```

```
/^.*/
```

```
/ /
```

```
//
```

```
//
```

```
/^392\(.*\)/
```

```
/555\1/
```

```
/^\(555\)\(....\)/
```

```
/444\2/
```

```
/^555\(....\)/
```

```
/444\1/
```

```
/\(^...\)555\(....\)/
```

```
/\1444\2/
```

```
/\(^...\)\(555\)\(....\)/
```

```
/\1444\3/
```

```
/\(.*\)1212$/
```

```
/\13434/
```

```
/\(.*\)1212/
```

```
/\13434/
```

```
/444/
```

```
/555/
```

```
/^[135]/
```

```
/9/
```

```
/^[1-35]/
```

```
/9/
```

```
/^[^1-35]/
```

```
/9/
```

```
/^1#/
```

```
//
```

```
/^1\#\(.*\)/
```

```
/\1/
```

```
/^1\*/
```

```
//
```

```
/^1\*\(.*\)/
```

```
/\1/
```

```
/^5+/
```

```
/9/
```

```
/^\(555\)+\(.*\)/
```

```
/444\2/
```

```
/^9?1?\(919\)/
```

```
/\1/
```

```
/1234/
```

```
/00&00/
```

```
/1234/
```

```
/00\000/
```

### Translation Profile Configuration

```
voice translation-profile <name>
translate called <translation-rule num>
translate calling <translation-rule num> 
translate redirect-called <translation-rule num>
 no
```

```
voice translation-profile <name>
```

```
translate called <translation rule #>
```

```
translate calling <translation rule #>
```

```
translate redirect-called <translation rule #>
```

Based on the signaling type of the incoming call, the calling number is equivalent to Automatic Number Identifier (ANI) or the calling line id. The redirect-called number is equivalent to redirect Dialed Number Identification Service (DNIS) or the original called number.

### VoIP Incoming Configuration

voip-incoming translation -profile <name>

```
voip-incoming translation-profile
```

This VoIP incoming translation profile configuration example assigns the translation profile named global-definition to all incoming VoIP calls.

```
Router(config)# voip-incoming translation-profile global-definition
```

### Dial Peer Configuration

Inbound Dial Peer

```
dial-peer voice <num> [pots|voip|vofr|voatm]
translation-profile [incoming | outgoing] <name>
```

To Block Calls

```
dial-peer voice <num> [pots|voip]
 call-block translation-profile incoming <name>
 call-block disconnect-cause incoming <cause>
 carrier-id source <name>
```

```
call-block translation-profile incoming <name>
```

```
call-block disconnect-cause incoming <cause>
```

- Invalid-Number

- Unassigned-number

- User-Busy

- Call-Rejected

```
carrier-id source <name>
```

```
translation-profile incoming <name>
```

Outbound Dial Peer

```
dial-peer voice <num> pots
 carrier-id target <name>
 trunkgroup <num> [preference_num]
 trunkgroup <num> [preference_num]
 translation-profile outgoing <name>
```

```
carrier-id target <name>
```

```
translation-profile outgoing <name>
```

```
trunkgroup <number> [preference_num]
```

### Voice Port Configuration

```
voice-port <number>
 translation-profile [incoming | outgoing] <name>
 trunk-group <name> [preference]
```

```
translation-profile incoming
```

```
trunk-group
```

### Controller Translation Profile

The controller translation profile is used for an incoming NFAS call or outgoing NFAS call which is routed through a trunk group.

```
voice service pots
 translation-profile [incoming | outgoing] controller [T1 | E1] <unit#> <name>
```

```
translation-profile
```

```
[incoming | outgoing]
```

```
controller
```

```
[T1 | E1] <unit#>
```

```
<name>
```

### Trunk Group Configurations

```
trunk group <name>
 carrier-id <name>
 hunt-scheme { [least-idle [even|odd] [up|down] |
             least-used [even|odd] [up|down] |
             longest-idle [even|odd] [up|down |
             random
             round-robin [even|odd] [up|down] |
             sequential [even|odd] [up|down] 
 translation-profile incoming <name>
 translation-profile outgoing <name>
```

```
trunk group <name> [<preference>]
```

A trunk group member can be a PRI, BRI, or CAS interface or FXS, FX0, or E&M voice port. The preference number is an optional parameter which is used to sort trunk group members in order. If the preference number is not defined, then a new trunk group member becomes the last member of a trunk group. The preference number range is 0 through 63. Up to 64 members (interfaces or voice ports) can be defined to a trunk group. trunk group under voice-port is used to configure an analog voice port trunk group member. The trunk group member CLI that exists for ISDN PRI and BRI trunks through the interface serial or interface bri commands remains unchanged. The size of a trunk group name is 32 characters.

```
carrier-id <name>
```

The ID for the carrier that owns the trunk group. The size of a carrier id is 64 characters.

```
hunt-scheme
```

Specify the method used in order to select a member/channel from a trunk group for an outgoing call.

least-idle [even | odd] [up | down]

least-used [even | odd] [up | down]

longest-idle [even | odd] [up | down]

random

round-robin [even | odd] [up | down]

sequential [even | odd] [up | down]

The default value of a hunt-scheme is least-used .

```
description
```

The size of a literal description about a trunk group is sixty-four characters.

```
translation-profile
```

Define call number translation profiles for incoming and outgoing calls.

### Trunk Group Member Configurations

```
interface serial <slot/port>:<num>
   trunk-group <name> [<preference>]

interface bri <number>
   trunk-group <name> [<preference>]

voice-port <number>
   trunk-group <name> [<preference>]
 
/* ds0-group trunk group configuration example */

controller T1 1/0
   ds0-group 1 timeslots 1-10 type e&m-fgd
   ds0-group 2 timeslots 12-20 type e&m-fgd
   cas-custom 1
    trunk-group 11
   cas-custom 2
    trunk-group 22
```

### Source IP Group Configurations

```
voice source-group <name>
  access-list <num>
  carrier-id source <name>
  carrier-id target <name>
  description <text>
  disconnect-cause <user-selected-reason>
  translation-profile incoming <name>
       h323zone-id <text>
```

```
voice source-group <name>
```

```
access-list
```

```
carrier-id source <name>
```

```
carrier-id target <name>
```

```
description
```

```
disconnect-cause
```

- Invalid-number

- Unassigned-number

- User-busy

- Call-rejected

```
translation-profile incoming
```

```
h323zone-id
```

### CallManager Fallback Configuration

You can also apply Translation profiles in a Cisco CallManager fallback configuration. When applied under the call-manager-fallback mode, the calls are translated only when the IP phones fallback to SRST mode. Under normal circumstances (when phones are registered to Cisco CallManager servers), the call made by the phones are not translated. The translation-profile under the call-manager-fallback affect the incoming and outgoing calls to the router from the IP phone. This is a different behavior than when you apply the translation-profile under a dial-peer . The incoming and outgoing commands are related to the IP phone. The incoming command changes the parameters of calls that come from the IP phone. The outgoing command changes the values of calls that go out of the router to the IP phone.

```
voice translation-rule 1
 rule 1 /^.*/ /5551234/
!
!
voice translation-profile srst-in
 translate calling 1
!
call-manager-fallback
 translation-profile incoming srst-in
!
```

When the IP phone makes a call, the calling number of the incoming calling number changes and is then processed by the router. The router routes the call with that calling number. In this example, all calls from IP phones to the router show the calling number as 5551234. This includes the calls between IP phones. In order to change the calling number to calls that leave the router to the PSTN only, apply the translation-profile in the dial-peer pots so that IP phone to IP phone calls are not affected.

Refer to the Cisco IOS Voice Command Reference for information on the call-manager-fallback command.

## Call Blocking Configuration Examples

### Call Blocking All Calls on a Dial Peer

Configure a voice translation rule that matches any number.

```
!
voice translation-rule 1 
 rule 1 reject /^.*/ !--- Matches any number string and rejects the call. ! !--- Apply the rule to a translation profile for called, 
!--- calling, or redirect-called numbers. !
voice translation profile call_block 
 translate calling 1 !--- Invokes voice translation rule 1 in order to determine which calls 
!--- to reject based on the calling number. ! !--- Include the translation profile within a dial peer definition. 
!--- You can use incoming called-number to only match this dial peer at certain times. !
dial-peer voice 100 pots !--- This can be any dial peer that matches the desired inbound call. incoming called-number 3927393 !--- Matches this dial peer for inbound POTS calls 
!--- that go to the number string listed. call-block translation-profile incoming call_block !--- Invokes the voice translation profile “call_block” 
!--- on inbound POTS calls that match this peer in order to 
!--- determine which calls to reject. call-block disconnect-cause incoming call-reject !--- Sets the cause code to “call-reject” for blocked calls.
```

### Call Blocking Specific Calling Numbers

Configure a voice translation rule to block the desired calling number you want to block. This example uses 9193927393.

```
voice translation-rule 1
 rule 1 reject /9193927393/ !--- Matches the defined number string and rejects the call. ! !--- Apply the rule to a translation profile for the calling number. 
!--- You could also reject based on called or redirect-called numbers . !
voice translation-profile call_block
 translate calling 1 !--- Invokes voice translation rule 1 in order to determine 
!--- which calls to reject based on the calling number. ! !--- Include the translation profile within a dial peer definition. !
dial-peer voice 100 pots
 call-block translation-profile incoming call_block !--- Invokes the voice translation profile “call_block” on 
!--- inbound POTS calls that match this peer 
!--- in order to determine which calls to reject. call-block disconnect-cause incoming call-reject
 incoming called-number !--- Matches this peer for all inbound POTS calls. port 1/1:23
```

### Call Blocking Specific Called Numbers

Configure a voice translation rule to match the desired called number you want to block. This example uses 3927393.

```
!
voice translation-rule 1
 rule 1 reject /3927393/ !--- Matches the defined number string and rejects the call. ! !--- Apply the rule to a translation profile for the called number. 
!--- You could also reject based on calling or redirect-called numbers. !
voice translation-profile call_block
 translate called 1 !--- Invokes voice translation rule 1 in order to determine which 
!--- calls to reject based on the called number. ! !--- Include the translation profile within a dial peer definition. !
dial-peer voice 100 voip
 call-block translation-profile incoming call_block !--- Invokes the voice translation profile “call_block” on 
!--- inbound POTS calls that match this peer 
!--- in order to determine which calls to reject. call-block disconnect-cause incoming call-reject
 incoming called-number
```

### Translate Any Number to a Specific Number

```
voice translation-rule 1
 rule 1 /\(.*\)/ /300/ !--- Matches any number string and replaces it with 300. !
voice translation-profile my_profile
 translate called 1 !--- Invokes voice translation rule 1 in order to translate the called number. !
dial-peer voice 1000 pots !--- This can be any dial peer that matches the inbound call. translation-profile incoming my_profile !--- Invokes voice translation profile “my_profile” for incoming calls. direct-inward-dial
 incoming called-number .
 port 1/0:23

Router#
Router# test voice translation-rule 1 5551234 Matched with rule 1
Original number: 5551234        Translated number: 300
Original number type: none      Translated number type: none
Original number plan: none      Translated number plan: none
```

### Translate Inbound Seven Digit Numbers to Four Digits

```
voice translation-rule 1 !--- Matches any number string that begins with 498 and 
!--- changes those three digits to null (removes them). rule 1 /^498/ //
  !
  !
  voice translation-profile Voice !--- Invokes voice translation rule 1 to translate the called number. translate called 1
  !
  dial-peer voice 225 pots
   translation-profile incoming Voice !--- Invokes voice translation profile “Voice” for incoming calls. direct-inward-dial
   port 1/0:23

Router# test voice translation-rule 1 4985555 Matched with rule 1
  Original number: 4985555 Translated number: 5555
  Original number type: none      Translated number type: none
  Original number plan: none      Translated number plan: none
```

### Prefix the Inbound Called Number

```
voice translation-rule 1 !--- Matches any number string and places 555 in front of the original number. rule 1 // /555/
!
voice translation-profile prefix !--- Invokes voice translation rule 1 in order to translate the called number. translate called 1
!
dial-peer voice 1 pots
    translation-profile incoming prefix !--- Invokes voice translation profile “prefix” for incoming calls. Router# test voice translation-rule 1 1234 Matched with rule 1
Original number: 1234   Translated number: 5551234
Original number type: none      Translated number type: none
Original number plan: none      Translated number plan: none
```

### Change Outbound Calls with a Plan and Type of Unknown to ISDN and National

```
voice translation-rule 1
 rule 1 // // type unknown national plan unknown isdn !--- Matches any number string with a plan and type of 
!--- unknown. Also changes the type to national and the plan to isdn. !
voice translation-profile isdn_map
 translate called 1 !--- Invokes voice translation rule 1 in order to translate the called number. !
dial-peer voice 1 pots
    translation-profile outgoing isdn_map !--- Invokes voice translation profile “isdn_map” for outgoing calls. kearly01# test voice translation-rule 1 5551234 type unknown plan unknown Matched with rule 1
Original number: 5551234        Translated number: 5551234
Original number type: unknown   Translated number type: national
Original number plan: unknown   Translated number plan: isdn
```

### Prefix the Calling Number

```
voice translation-rule 1 !--- Matches number strings that start with 4 
!--- and places 9059514 in the beginning 4 place. 
!--- It serves the same type of function for the number 0. rule 1 /^4/ /9059514/
 rule 2 /^0/ /9059510/
!
voice translation-profile Prefix !--- Invokes voice translation rule 1 in order to translate the calling number. translate calling 1
!
dial-peer voice 100 pots
 translation-profile outgoing Prefix !--- Invokes voice translation profile “Prefix” for outgoing calls.
```

### Make Phones Go Out Specific Ports

```
voice translation-rule 29 !--- Matches anything that starts with a 9 and replaces the 9 with 29. rule 1 /^9/ /29/
!
voice translation-rule 39 !--- Matches anything that starts with a 9 and replaces the 9 with 39. rule 1 /^9/ /39/
!
voice translation-profile FXS29 !--- Invokes voice translation profile “FXS29” in order to translate the called number. translate called 29
!
voice translation-profile FXS39 !--- Invokes voice translation profile “FXS39” in order to translate the called number. translate called 39
!
voice-port 1/1/0
 connection plar 8005 !--- Sends inbound calls directly to the IP phone with 8005 DN. !
voice-port 1/1/1
 connection plar 8006 !--- Sends inbound calls directly to the IP phone with 8006 DN. !
dial-peer voice 110 pots !--- Since calls from 8005 that begin with a 9 are changed 
!--- to begin with 29, all these calls match this dial peer 
!--- and go out port 1/1/0 (when not in SRST mode). destination-pattern 29T
 port 1/1/0
!
dial-peer voice 111 pots !--- Since calls from 8006 that begin with a 9 are changed 
!--- to begin with 39, all these calls match this dial peer 
!--- and go out port 1/1/1 (when not in SRST mode). destination-pattern 39T
 port 1/1/1
!
dial-peer voice 1000 voip !--- To Cisco CallManager. preference 1
 destination-pattern .T
 voice-class h323 1
 session target ipv4:10.1.0.13
 dtmf-relay h245-alphanumeric
 ip qos dscp cs5 media
!
dial-peer voice 29 voip
 translation-profile incoming FXS29 !--- Matches calls from the IP phone with a DN of 8005, and invokes 
!--- voice translation profile FXS29 in order to change numbers that start 
!--- with a 9 to begin with 29. answer-address 8005
!
dial-peer voice 39 voip
 translation-profile incoming FXS39 !--- Matches calls from the IP phone with a DN of 8006, 
!--- and invokes voice translation profile FXS39 in order to change 
!--- numbers that start with a 9 to begin with 39. answer-address 8006
```

### Make Calls from Specific Ports go to the Desired VoIP Peer with the Same Called Number

```
voice translation-rule 27 !--- Matches anything that starts with a 7 and replaces the 7 with 27. rule 1 /^7/ /27/
!
voice translation-rule 37 !--- Matches anything that starts with a 7 and replaces the 7 with 37. rule 1 /^7/ /37/
!
voice translation-profile FXS27 !--- Invokes voice translation profile “FXS27” in order to translate the called number. translate called 27
!
voice translation-profile FXS37 !--- Invokes voice translation profile “FXS37” in order to translate the called number. translate called 37
!
dial-peer voice 270 voip !--- Matches the called number of 27 which is 
!--- translated from port 2/0. You can use a translation 
!--- profile in order to change the number back to 7 here if needed. destination-pattern 27
 session target ipv4:10.1.1.2
!
dial-peer voice 370 voip !--- Matches the called number of 37 which is translated 
!--- from port 2/1. You can use a translation profile in order to 
!--- change the number back to 7 here if needed. destination-pattern 37
 session target ipv4:10.1.1.3
!
dial-peer voice 27 pots
 translation-profile incoming FXS27 !--- Matches calls from port 2/0, and invokes voice translation 
!--- profile FXS27 in order to change numbers that start with a 7 to begin with 27. port 2/0
!
dial-peer voice 37 pots
 translation-profile incoming FXS37 !--- Matches calls from port 2/1, and invokes voice translation 
!--- profile FXS37 in order to change numbers that start with a 7 to begin with 37. port 2/1
```

## Verify

Certain show commands are supported by theOutput Interpreter Tool, which allows you to view an analysis of show command output.

Note : Only registered Cisco users have access to internal Cisco tools and information.

You can use the test voice translation-rule command to test the behavior of the rule.

In order to test the functionality of a translation rule, use the test voice translation-rule command in privileged EXEC mode.

```
test voice translation-rule number input-test-string [type match-type [plan match-type]]
```

- abbreviated — Abbreviated representation of the complete number as supported by this network.

- any — Any type of called number.

- international — Number called that reaches a subscriber in another country.

- national — Number called that reaches a subscriber in the same country, but outside the local network.

- network — Administrative or service number specific to the serving network.

- reserved — Reserved for extension.

- subscriber — Number called that reaches a subscriber in the same local network.

- unknown — Number of a type that is unknown to the network.

- any — Any type of called number.

- data — Number called for data calls.

- ermes — European Radio Message standard numbering plan.

- isdn —Called number for an ISDN network.

- national — Number called that reaches a subscriber in the same country, but outside the local network.

- private — Number called for a private network.

- reserved — Reserved for extension.

- telex — Numbering plan for Telex equipment.

- unknown — Number of a type that is unknown to the network.

Example

```
voice translation-rule 1
  rule 1 /^555\(....\)/ /444\1/
  rule 2 /777/ /888/ type national unknown plan any isdn kearly01# test voice translation-rule 1 5551234 Matched with rule 1
Original number: 5551234        Translated number: 4441234
Original number type: none      Translated number type: none
Original number plan: none      Translated number plan: none

kearly01# test voice translation-rule 1 7771234 7771234 Didn't match with any of rules

kearly01# test voice translation-rule 1 7771234 type national plan isdn Matched with rule 2
Original number: 7771234        Translated number: 8881234
Original number type: national  Translated number type: unknown
Original number plan: isdn      Translated number plan: isdn
```

The translation rule is used with this test:

Note : The show voice translation-rule and show voice translation-profile commands can also be useful.

```
kearly01# show voice translation-rule 1 Translation-rule tag: 1

        Rule 1:
        Match pattern: ^555\(....\)
        Replace pattern: 444\1
        Match type: none                Replace type: none
        Match plan: none                Replace plan: none

        Rule 2:
        Match pattern: 777
        Replace pattern: 888
        Match type: national            Replace type: unknown
        Match plan: any                 Replace plan: isdn

kearly01# show voice translation-profile Translation Profile: mytranslation
        Rule for Calling number: 
        Rule for Called number: 1
        Rule for Redirect number:
```

## Troubleshoot

This section provides information you can use to troubleshoot your configuration.

Note : Refer to Important Information on Debug Commands before you issue debug commands.

WIth the same translation rule, use debug voice translation and then run the test voice translation-rule command again.

```
kearly01# test voice translation-rule 1 7771234 7771234 Didn't match with any of rules

*Apr  4 14:44:31.665: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match: 
No match; number=7771234 rule precedence=1

*Apr  4 14:44:31.665: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match: 
Error: type didn't match; in.type=0x9 rule.type = 0x2

*Apr  4 14:44:31.665: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match: 
No match; number=7771234 rule precedence=1

*Apr  4 14:44:31.665: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match: 
Error: type didn't match; in.type=0x9 rule.type = 0x2test voice trans
```

The debugs show the rule does not match. Once you change the type and plan, it matches.

```
kearly01# test voice translation-rule 1 7771234 type national plan isdn Matched with rule 2
Original number: 7771234        Translated number: 8881234
Original number type: national  Translated number type: unknown
Original number plan: isdn      Translated number plan: isdn

*Apr  4 14:44:51.665: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match:
No match; number=7771234 rule precedence=1

*Apr  4 14:44:51.665: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match: 
No match; number=7771234 rule precedence=1

*Apr  4 14:44:51.669: //-1/xxxxxxxxxxxx/RXRULE/regxrule_match:
 No match; number=7771234 rule precedence=1

*Apr  4 14:44:51.669: //-1/xxxxxxxxxxxx/RXRULE/sed_subst: 
Successful substitution; pattern=7771234 matchPattern=777 
replacePattern=888 replaced pattern=8881234

*Apr  4 14:44:51.669: //-1/xxxxxxxxxxxx/RXRULE/regxrule_subst_num_type: 
Match Type = national, Replace Type = unknown Input Type = national

*Apr  4 14:44:51.669: //-1/xxxxxxxxxxxx/RXRULE/regxrule_subst_num_plan: 
Match Plan = any, Replace Plan = isdn Input Plan = isdn
```

## Related Information

- Voice Translation Rules in Media Gateways

- Troubleshooting Cisco IP Telephony

- Cisco Technical Support & Downloads

### Revision History

3.0

10-Sep-2024

Updated Machine Translation and Formatting.

2.0

07-Apr-2023

Updated format, corrections. Recertification.

1.0

15-Feb-2005

Initial Release

### Contributed by Cisco Engineers

Cisco TAC Engineers

### Customers Also Viewed

- Determine Voice Translation Rules

- Understand Matching Inbound/Outbound Dial Peers on IOS Platforms

### This Document Applies to These Products

- Call Routing / Dial Plans

| Syntax | Description |
|---|---|
| precedence | Priority of the translation rule. The range is from 1 to 15. |
| /match-pattern/ | Stream editor (SED) expression that is used to match incoming call information. The slash / is a delimiter in the pattern. |
| /replace-pattern/ | The SED expression that is used to replace the match pattern in the call information. The slash / is a delimiter in the pattern. |
| type match-type replace-type | (Optional) The numbering type match can be: abbreviated any international national network reserved subscriber unknown The numbering type replacement can be: abbreviated international national network reserved subscriber unknown |
| plan match-type replace-type | (Optional) The plan type match can be: any data ermes isdn national private reserved telex unknown The plan type replacement can be: data ermes isdn national private reserved telex unknown |
| reject | The match pattern of a translation rule is used for call-reject purposes. |

| Voice Translation Rule Character | Description |
|---|---|
| ^ | Match the expression at the start of a line. |
| $ | Match the expression at the end of the line. |
| / | Delimiter that marks the start and end of both the equivalent and replacement strings. |
| \ | Escape the special meaning of the next character. |
| - | Indicates a range when not in the first/last position. Used with the [ and ]. |
| [list] | Match a single character in a list. |
| [^list] | Do not match a single character specified in the list. |
| . | Match any single character. |
| * | Repeat the previous regexp zero or more times. |
| + | Repeat the previous regular expression one or more times. |
| ? | Repeat the previous regular expression zero or one time (use CTRL-V in order to enter in Cisco IOS). |
| () | Groups regular expressions. |

| Match String | Replace String | Dialed String | Replaced String | Comments |
|---|---|---|---|---|
| /^$/ | / / | NULL | NULL | Simple Null to Null translation. |
| /^.*/ | / / | 9195551212 | NULL | Any to Null translation. |
| // | // | 9195551212 | 9195551212 | Match any string but no replacement. Use this to manipulate the call plan or call type. |
| /^392\(.*\)/ | /555\1/ | 3921212 | 5551212 | Match the beginning of a variable length string. |
| /^\(555\)\(....\)/ | /444\2/ | 5551212 | 4441212 | Match the beginning of the string. The second parenthesis structure is pulled to the new string. |
| /^555\(....\)/ | /444\1/ | 5551212 | 4441212 | Match the beginning of the string. Notice the \1 replaces the first group of the regular expression within parenthesis. |
| /\(^...\)555\(....\)/ | /\1444\2/ | 9195551212 | 9194441212 | Match the middle of a string. |
| /\(^...\)\(555\)\(....\)/ | /\1444\3/ | 9195551212 | 9194441212 | Match the middle of a string. |
| /\(.*\)1212$/ | /\13434/ | 9195551212 555121212 | 9195553434 555123434 | Match the end of a string. |
| /\(.*\)1212/ | /\13434/ | 9195551212 555121212 | 9195553434 555123434 | Match the end of a string. There is no need for an implicit $ at the end for this particular example. |
| /444/ | /555/ | 4441212 44441212 44414441212 | 5551212 55541212 55514441212 | Match the substring. |
| /^[135]/ | /9/ | 12345 22345 32345 | 92345 22345 93245 | Match certain numbers. |
| /^[1-35]/ | /9/ | 1234 2345 4567 8456 | 9234 9345 4567 8456 | Match a range. |
| /^[^1-35]/ | /9/ | 1234 2345 4567 8456 | 1234 2345 9567 9456 | The ^ in the list means do not match these items. |
| /^1#/ | // | 1#456 | 456 | Match 1# at the beginning and replace it with Null. |
| /^1\#\(.*\)/ | /\1/ | 1#456 | 456 | The same as the previous expression, but composed differently. |
| /^1\*/ | // | 1*456 | 456 | Match 1* in a pattern and replace it with Null. |
| /^1\*\(.*\)/ | /\1/ | 1*456 | 456 | The same as the previous expression but composed slightly different. |
| /^5+/ | /9/ | 5888 55888 555888 5588855 | 9888 9888 9888 988855 | This is an example of the use of the + option. |
| /^\(555\)+\(.*\)/ | /444\2/ | 5551212 555551212 5555551212 5551212555 | 4441212 444551212 4441212 4441212555 | This is another example of the + option. This searches for the 555 pattern repeated at the beginning. |
| /^9?1?\(919\)/ | /\1/ | 9195551212 19195551212 919195551212 99195551212 | 9195551212 9195551212 9195551212 9195551212 | Here is how the ? string can be used. For example, if you want to strip some previous digits that are or are not present. In this case you want to strip the prefix 9 or 1 or 9 and 1 together. |
| /1234/ | /00&00/ | 5551234 | 55500123400 | Match the substring. |
| /1234/ | /00\000/ | 5551234 | 55500123400 | Match the substring (same as &). |

| Attribute | Description |
|---|---|
| voice translation-profile <name> | The size of a translation profile name is thirty-one characters. |
| translate called <translation rule #> | Define the translation profile rule for the called number. |
| translate calling <translation rule #> | Define the translation profile rule for the calling number. |
| translate redirect-called <translation rule #> | Define the translation profile rule for the redirect-called number. |

| Attribute | Description |
|---|---|
| voip-incoming translation-profile | Define a call number translation profile for all incoming VoIP calls. This CLI is mutually exclusive with the voip-incoming translation-rule command from the old style translation rules. |

| Attribute | Description |
|---|---|
| call-block translation-profile incoming <name> | Define a call blocking translation profile for incoming calls which are used by the session or Interactive Voice Response (IVR) application when the call is handled by either the session or IVR application. The size of call-block translation-profile is thirty-one characters. |
| call-block disconnect-cause incoming <cause> | The value of this attribute is returned to the source when a call is blocked due to the incoming call number checking by the session or IVR application. A user can select these disconnect causes: Invalid-Number Unassigned-number User-Busy Call-Rejected The default value of this attribute is No Service. |
| carrier-id source <name> | Defines the source carrier id in an inbound dial peer which is used as a equivalent key in inbound dial peer equivalent. This attribute is only supported in a POTS or VoIP dial peer configuration. The size of a source carrier-id is 127 characters. |
| translation-profile incoming <name> | Define a call number translation profile for incoming calls. The size of the translation-profile is thirty-one characters. |

| Attribute | Description |
|---|---|
| carrier-id target <name> | Defines the target carrier-id in an outbound dial peer which is used as a equivalent key in outbound dial peer equivalent. This attribute is only supported in a POTS or VoIP dial peer configuration. The size of a target carrier-id is 127 characters. |
| translation-profile outgoing <name> | Define a call number translation profile for outgoing calls. |
| trunkgroup <number> [preference_num] | A single or multiple trunk groups can be provisioned as a target in an outbound dial peer. Up to 64 trunk groups can be defined in a dial peer. This attribute is mutually exclusive with port attributes. The range of preference is 1 through 64. |

| Attribute | Description |
|---|---|
| translation-profile incoming | Define a call number translation profile for incoming POTS calls. This CLI is mutually exclusive with translate called and translate calling commands from the old style rules. |
| trunk-group | Define an analog voice port as a trunk group member. Assign a CAS voice port to a trunk group under the CAS User CLI of the controller configuration. For PRIs, assign the trunk group under the serial interface of the D-channel. On BRIs, configure the trunk group under the BRI interface. |

| Attribute | Description |
|---|---|
| translation-profile | Define a translation profile for a controller. |
| [incoming \| outgoing] | Number translation on an incoming or outgoing call. |
| controller | Controller keyword. |
| [T1 \| E1] <unit#> | T1 or E1 controller unit. |
| <name> | Name of the translation profile name. The size of a translation profile name is 64 characters. |

| Attribute | Description |
|---|---|
| trunk group <name> [<preference>] | A trunk group member can be a PRI, BRI, or CAS interface or FXS, FX0, or E&M voice port. The preference number is an optional parameter which is used to sort trunk group members in order. If the preference number is not defined, then a new trunk group member becomes the last member of a trunk group. The preference number range is 0 through 63. Up to 64 members (interfaces or voice ports) can be defined to a trunk group. trunk group under voice-port is used to configure an analog voice port trunk group member. The trunk group member CLI that exists for ISDN PRI and BRI trunks through the interface serial or interface bri commands remains unchanged. The size of a trunk group name is 32 characters. |
| carrier-id <name> | The ID for the carrier that owns the trunk group. The size of a carrier id is 64 characters. |
| hunt-scheme | Specify the method used in order to select a member/channel from a trunk group for an outgoing call. least-idle [even \| odd] [up \| down] least-used [even \| odd] [up \| down] longest-idle [even \| odd] [up \| down] random round-robin [even \| odd] [up \| down] sequential [even \| odd] [up \| down] The default value of a hunt-scheme is least-used . |
| description | The size of a literal description about a trunk group is sixty-four characters. |
| translation-profile | Define call number translation profiles for incoming and outgoing calls. |

| Attribute | Description |
|---|---|
| voice source-group <name> | The size of a source IP group name is thirty-two characters. |
| access-list | An Cisco IOS access list id is used to identify the source of an incoming VoIP call. |
| carrier-id source <name> | The source carrier id is associated to an incoming VoIP call for the CSR application at the terminating gateway in order to select a target carrier that routes an outgoing POTS call. The size of a carrier-id is sixty-four characters. |
| carrier-id target <name> | The default target carrier id which can be used to match up an outbound dial. |
| description | The size of the literal description about a VoIP source group is sixty-four characters. |
| disconnect-cause | The value of this attribute is returned to the source when a call is blocked due to access-list restriction. A user can select these disconnect causes: Invalid-number Unassigned-number User-busy Call-rejected The default value of this attribute is No-service. |
| translation-profile incoming | Specify number translation rules that are applied to an incoming VoIP call. |
| h323zone-id | Specify the zone-id that matches the source zone id of an incoming H.323 call. The size of an h323zone-id is sixty-four characters. |

| Syntax | Description |
|---|---|
| number | Specifies the number of the translation rule that is tested. The range is from 1 through 2147483647. |
| input-test-string | String that is tested by the translation rule. |
| type match-type | (Optional) The number type of the call. Valid values for the match-type argument are: abbreviated — Abbreviated representation of the complete number as supported by this network. any — Any type of called number. international — Number called that reaches a subscriber in another country. national — Number called that reaches a subscriber in the same country, but outside the local network. network — Administrative or service number specific to the serving network. reserved — Reserved for extension. subscriber — Number called that reaches a subscriber in the same local network. unknown — Number of a type that is unknown to the network. |
| plan match-type | (Optional) Numbering plan of the call. Valid values for the match-type argument are: any — Any type of called number. data — Number called for data calls. ermes — European Radio Message standard numbering plan. isdn —Called number for an ISDN network. national — Number called that reaches a subscriber in the same country, but outside the local network. private — Number called for a private network. reserved — Reserved for extension. telex — Numbering plan for Telex equipment. unknown — Number of a type that is unknown to the network. |

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 10-Sep-2024 | Updated Machine Translation and Formatting. |
| 2.0 | 07-Apr-2023 | Updated format, corrections. Recertification. |
| 1.0 | 15-Feb-2005 | Initial Release |