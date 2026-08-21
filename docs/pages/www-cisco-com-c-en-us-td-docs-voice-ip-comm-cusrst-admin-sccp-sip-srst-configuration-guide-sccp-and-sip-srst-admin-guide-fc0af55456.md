---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-fc0af55456
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_call_handling.html
retrieved_at: 2026-08-21T02:49:20.940714+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Configuring Call Handling

## Chapter: Configuring Call Handling

# Configuring Call Handling

This chapter describes how to configure Cisco Unified Survivable Remote Site Telephony (Cisco Unified SRST) for incoming and
                        outgoing calls for SCCP phones.

This chapter also describes support for standardized RFC 3261 features for SIP phones. Features include call blocking and
                        call forwarding.

Configuring Call Handling for SIP phones applies to versions 4.0 and 3.4 only.

## Prerequisites for Configuring SIP SRST Features Using Back-to-Back User Agent Mode

Complete the prerequisites documented in the Prerequisites for Configuring Cisco Unified SIP SRST section in the Cisco Unified SRST Feature Overview .

Configure the SIP registrar. The SIP registrar gives users control of accepting or rejecting registrations. To configure acceptance
                                 of incoming SIP Register messages, see the Prerequisites for Configuring the SIP Registrar section.

## Restrictions for Configuring SIP SRST Features Using Back-to-Back User Agent Mode

See the restrictions documented in the Restrictions for Configuring Cisco Unified SIP SRST section in the Cisco Unified SRST Feature Overview .

## Information About Configuring SCCP SRST Call Handling

Cisco Unified SRST offers a smaller set of call handling capabilities than Cisco Unified Communications Manager, and much
                           of the configuration for this feature involves enabling existing Cisco Unified Communications Manager or Cisco Unified IP
                           Phone settings.

H.323 VoIP Call Preservation Enhancements for WAN Link Failures

Toll Fraud Prevention

### H.323 VoIP Call Preservation Enhancements for WAN Link Failures

H.323 VoIP call preservation enhancements for WAN link failures sustain connectivity for H.323 topologies where signaling
                              is handled by an entity, such as Cisco Unified Communications Manager, that is different from the other endpoint and brokers
                              signaling between the two connected parties.

Call preservation is useful when a gateway and the other endpoint (typically a Cisco Unified IP phone) are collocated at the
                              same site and call agent is remote and therefore more likely to experience connectivity failures.

For configuration information see Chapter “Configuring H.323 Gateways” in Cisco IOS H.323 Configuration Guide, Release 12.4T .

H.323 is deprecated from  IOS XE 17.6.1.

### Toll Fraud Prevention

When a Cisco router platform is installed with a voice-capable Cisco IOS Software, appropriate features must be enabled on
                              the platform to prevent potential toll fraud exploitation by unauthorized users. Deploy these features on all Cisco router
                              Cisco Unified Communications applications that process voice calls, such as Cisco Unified Communications Manager Express (Cisco
                              Unified Communications Manager Express), Cisco Survivable Remote Site Telephony (SRST), Cisco Unified Border Element (UBE),
                              Cisco IOS-based router and standalone analog and digital PBX and public-switched telephone network (PSTN) gateways, and Cisco
                              contact-center VoiceXML gateways. For more information about Toll Fraud Prevention, see Toll Fraud Prevention in Cisco Unified Communications Manager Express System Administration Guide .

## Information About Configuring SIP SRST Features Using Back-to-Back User Agent Mode

A Cisco Unified SRST system can now support SIP phones with standard-based RFC 3261 feature support locally and across SIP
                           WAN networks. With Cisco Unified SIP SRST, SIP phones can place calls across SIP networks with similar features, as SCCP phones
                           do. For example, most SCCP phone features such as caller ID, speed dial, and redial are supported now on SIP networks, which
                           give users the opportunity to choose SCCP or SIP.

Cisco Unified SIP SRST also uses a back-to-back user agent (B2BUA), which is a separate call agent that has more features
                           than Cisco SIP SRST 3.0, which used a redirect server that only accepted and forwarded calls. The main advantage of a B2BUA
                           call agent is in call forwarding, because it forwards calls on behalf of the phone. In addition, it maintains a presence as
                           call middleman in the call path.

Cisco  SIP SRST 3.4 supports the following call combinations:

SIP phone to SIP phone

SIP phone to PSTN / router voice port

SIP phone to SCCP phone

### Cisco Unified SIP SRST and Cisco SIP Cisco Unified Communications Manager Express Feature Crossover

The voice register directory number, voice register global, and voice register Pool configuration mode commands are accessible
                              in both Cisco Unified SIP Cisco Unified Communications Manager Express and Cisco Unified SIP SRST modes of operation. However,
                              not all the commands within these modes are intended for use in SIP SRST mode. The following table provides a summary guide
                              to which commands are relevant to the Cisco Unified Communications Manager Express or SRST modes of operation.

For more detailed information, refer to the command reference pages for each of the individual commands.

The following table is not all-inclusive; more commands may exist.

Command

Dial Peer

Voice Register Mode

Configurable for Cisco Unified (SIP) Cisco Unified Communications Manager Express and Cisco Unified SIP SRST

Applicable to Cisco Unified (SIP) Cisco Unified Communications Manager Express Only

After-hour exempt

X

DN

X

—

Auto-answer

—

DN

—

X

Call forward

X

DN

X

—

Huntstop

X

DN

X

—

Label

—

DN

—

X

Name

—

DN

—

X

Number

X

DN

X

—

Preference

X

DN

X

—

Application

X

Global

X

—

Authenticate

—

Global

—

X

Create

—

Global

—

X

Date-format

—

Global

—

X

DST

—

Global

—

X

External ring

—

Global

X

—

File

—

Global

—

X

Hold-alert

—

Global

—

X

Load

—

Global

—

X

Logo

—

Global

—

X

Max-dn

—

Global

X

—

Max-pool

—

Global

X

—

Max-redirect

—

Global

—

X

Mode

—

Global

X

—

MWI

—

Global

—

X

Reset

—

Global

—

X

Tftp-path

—

Global

—

X

Time zone

—

Global

—

X

Upgrade

—

Global

—

X

Url

—

Global

—

X

Voicemail

—

Global

—

X

After-hour exempt

X

Pool

X

—

Application

X

Pool

X

—

Call-forward

—

Pool

X

—

Call-waiting

—

Pool

—

X

Codec

X

Pool

X

—

Description

—

Pool

—

X

Dnd-control

—

Pool

—

X

Dtmf-relay

—

Pool

X

—

Id

—

Pool

X

—

Keep-conference

—

Pool

—

X

Max-pool

—

Pool

X

—

Number

X

Pool

X

—

Preference

X

Pool

X

—

Proxy

X

Pool

X

—

Reset

—

Pool

—

X

Speed-dial

—

Pool

—

X

Template

—

Pool

—

X

Translation-profile

X

Pool

X

—

Type

—

Pool

—

X

Username

—

Pool

—

X

VAD

X

Pool

X

—

Anonymous

—

Template

—

X

Caller-id

—

Template

—

X

Conference

—

Template

—

X

Dnd-control

—

Template

—

X

Forward

—

Template

—

X

Transfer

—

Template

—

X

### How to Configure Cisco Unified SCCP SRST

## Configuring Incoming Calls

Incoming call configuration can include the following tasks:

## Configuring Call Forwarding During a Busy Signal or No Answer

Configure the incoming calls that reach busy signal or go unanswered during the Cisco Unified Communications Manager fallback
                              to call forwarding to one or more E.164 numbers.

### SUMMARY STEPS

- call-manager-fallback

- call-forward busy directory-number

- call-forward noan directory-number timeout seconds

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

call-forward busy directory-number

### Example:

```
Router(config-cm-fallback)# call-forward busy
50..
```

Configures call forwarding to another number when the Cisco IP phone is busy.

directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters
                                          that correspond to the right-justified digits in the directory number extension.

Step 3

call-forward noan directory-number timeout seconds

### Example:

```
Router(config-cm-fallback)# call-forward noan
5005 timeout 10
```

Configures call forwarding to another number when receiving no answer from the Cisco IP phone.

directory-number : Selected directory number representing a fully qualified E.164 number or a local extension number. This number can contain
                                                “.” wildcard characters that correspond to the right-justified digits in the directory number extension.

timeout seconds : Sets the waiting time, in seconds, before the call is forwarded to another phone. The seconds range is 3–60000.

Step 4

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example forwards calls to extension number 5005 when an incoming call reaches a busy or unattended IP phone
                              extension number. Incoming calls ring for 15 seconds before forwarding to extension 5005.

```
call-manager-fallback
call-forward busy 5005
call-forward noan 5005 timeout seconds 15
```

The following example transforms an extension number for a call forwarding when the extension number is busy or unattended.
                              The call-forward busy command has an argument of 50.., which prepends the digits 50 to the last two digits of the called extension. The resulting
                              extension is the call forwarding number when the original extension number is busy or unattended. For instance, forwards an
                              incoming call to busy extension 6002 to extension 5002, and forwards an incoming call to busy extension 3442 to extension
                              5042. Incoming calls ring for 15 seconds before being forwarded.

```
call-manager-fallback
call-forward busy 50..
call-forward noan 50.. timeout seconds 15
```

## Configuring Call Rerouting

We recommend the alias command, which obsoletes the default-destination command, instead of the default-destination command.

The alias command provides a mechanism for rerouting calls to phone numbers that are unavailable during fallback. Up to 50 sets of
                           rerouting alias rules can be created for calls to phone numbers that are unavailable during a Cisco Unified Communications
                           Manager fallback. Sets of alias rules are created using the alias command. An alias is activated when a phone registers that has a phone number matching a configured alternate-number alias. Under that condition, an incoming call is rerouted to the alternate number. The alternate-number argument can be used in multiple alias commands, allowing you to reroute multiple different numbers to the same target number.

The configured alternate-number must be a specific E.164 phone number or extension that belongs to an IP phone registered on the Cisco Unified SRST router.
                           When an IP phone registers with a number that matches an alternate-number , an extra POTS dial peer is created. The destination pattern is set to the initial configured number-pattern , and the POTS dial peer voice port is set to match the voice port associated with the alternate-number .

If other IP phones register with specific phone numbers within the range of the initial number-pattern , the call is routed back to the IP phone rather than to the alternate-number (according to normal dial-peer longest-match, preference, and huntstop rules).

## Configuring Call Pickup

Configuring the pickup command enables the PickUp softkey on all SRST phones. You can then press the PickUp key and answer any currently ringing
                              IP phone that has a DID called number that matches the configured telephone-number . This command does not enable the Group PickUp (GPickUp) softkey.

When a user presses the PickUp softkey, SRST searches through all the SRST phones to find a incoming call that has a called
                              number that matches the configured telephone-number. When a match is found, the call is automatically forwarded to the extension
                              number of the phone that requested the Call Pickup.

The SRST pickup command is designed to operate in a manner compatible with Cisco Unified Communications Manager.

The default phone load on Cisco Unified Communications Manager, Release 4.0(1) for the Cisco 7905 and Cisco 7912 IP phones
                                          does not enable the PickUp softkey during fallback. To enable the PickUp softkey on Cisco 7905 and Cisco 7912 IP phones, upgrade
                                          your default phone load to Cisco Unified Communications Manager, Version 4.0(1) Sr2. Alternatively, you can upgrade the phone
                                          load to cmterm-7905g-sccp.3-3-8.exe or cmterm-7912g-sccp.3-3-8.exe , respectively.

### SUMMARY STEPS

- call-manager-fallback

- no huntstop

- alias tag number-pattern to alternate-number

- pickup telephone number

- end

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

no huntstop

### Example:

```
Router(config-cm-fallback)# no huntstop
```

Disables huntstop.

Step 3

alias tag number-pattern to alternate-number

### Example:

```
Router(config-cm-fallback)# alias 1 8005550100
to 5001
```

Creates a set rule for rerouting calls to sets of phones that are unavailable during Cisco Unified Communications Manager
                                          fallback.

tag : Identifier for the alias rule range. Range is from 1to 50.

number-pattern : Pattern to match the incoming phone number. This pattern may include wildcards.

to : Connects the tag number pattern to the alternate number.

alternate-number : Alternate phone number to route incoming calls to match the number pattern. The alternate number has to be a specific extension
                                                that belongs to an IP phone that is actively registered on the Cisco Unified SRST router. The alternate phone number can be
                                                used in multiple alias commands.

Step 4

pickup telephone number

### Example:

```
Router(config-cm-fallback)# pickup 8005550100
```

Enables the PickUp softkey on all Cisco Unified IP Phones, allowing an external Direct Inward Dialing (DID) call coming into
                                          one extension to be picked up from another extension during SRST. The telephone-number argument is the phone number to match
                                          an incoming called number.

Step 5

end

### Example:

```
Router(config-cm-fallback)# end
```

Returns to privileged EXEC mode.

### Example

The pickup command is best used with the alias command. The following partial output from the show running-config command shows the pickup command and the alias command configured to provide call routing for a pilot number of a hunt group:

```
call-manager-fallback
no huntstop
alias 1 8005550100 to 5001
alias 2 8005550100 to 5002
alias 3 8005550100 to 5003
alias 4 8005550100 to 5004
pickup 8005550100
```

When a DID incoming call to 800 555-0100 is received, the alias command routes the call at random to one of the four extensions (5001–5004). Because the pickup command is configured, if the DID call rings on extension 5002, the call can be answered from any of the other extensions
                              (5001, 5003, 5004) by pressing the PickUp softkey.

The pickup command works by finding a match based on the incoming DID called number. In this example, a call from extension 5004 to
                              extension 5001 (an internal call) does not activate the pickup command because the called number (5001) does not match the
                              configured pickup number (800 555-0100). Thus, the pickup command distinguishes between internal and external calls if multiple calls are ringing simultaneously.

## Configuring Consultative Transfer

Before Cisco Unified SRST 4.3, the consultative transfer feature played dial tone and collected dialed digits until the digits
                           matched the pattern for consultative transfer, blind transfer, or PSTN transfer blocking. The after-hours blocking criteria
                           was applied after the consultative transfer digit collection and pattern matching.

The new feature modifies the transfer digit-collection process to make it consistent with Cisco Unified Communications Manager.
                           This feature is supported only if the transfer-system full-consult command (default) is specified in call-manager-fallback configuration mode and an idle line or channel is available for seizing,
                           digit collection, and dialing.

Requires two lines for consultative transfer. When the transferor party is an octo-line directory number, Cisco Unified SRST
                           selects the next available idle channel on that directory number. If the maximum number of channels of the directory number
                           are in use, consider another idle line on the transferor phone. If the auto-line command is configured on the phone, the specified autoline (if idle) takes precedence over other nonauto lines. If no idle
                           line is available on the transferor phone, initiates blind transfer instead of the consultative transfer.

During the consultative transfer, blocks the transferor line to the transferee party on the transferor phone to prevent being
                           stolen by other phones sharing the same directory number. When you press the Transfer softkey for consultative transfer, does
                           not display the Transfer softkey while collecting and dialing the digits on this seized consultative transfer call leg. The
                           method for consultative transfer pattern matching, blind transfer, PSTN transfer blocking, or after-hour blocking criteria
                           remain the same although the manipulation after the matching is different. On meeting the  criteria for blind transfer, Cisco
                           Unified SMST stops the consultative transfer call leg, informs the Cisco IOS Software to transfer the call, and then stops
                           the original call bubble. Handles the PARK FAC code in the same way as an incoming call which requires applying a ten-second
                           timer by the Cisco IOS Software.

The enhancement, by default, collects the transfer digits from the incoming call leg. If necessary, you can configure the
                                       system to collect the transfer digits from the original call leg. See the Configuring Transfer Digit Collection Method section.

The error handling for transfer failure because of transfer blocking or interdigit timer expiration remains. It includes displaying
                           an error message on the prompt line and logging it if “debug ephone error” is enabled, playing a fast-busy or busy tone, and
                           stopping the consultative transfer call leg.

Requires no new configuration to support these enhancements.

## Configuring Transfer Digit Collection Method

By default, collects transfer digits from the incoming call leg. To change the transfer digit collection method, perform the
                              following steps.

### Before you begin

Cisco Unified SRST 4.3

Cisco Unified Communications Manager 6.0

Cisco IOS Release 12.4(15)XZ

The Cisco 3200 Series Mobile Access Router does not support SRST.

### SUMMARY STEPS

- enable

- configure terminal

- call-manager-fallback

- transfer-digit-collect {new-call | orig-call}

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router# enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 4

transfer-digit-collect {new-call | orig-call}

### Example:

```
Router(config-cm-fallback)#
transfer-digit-collect orig-call
```

Selects the digit-collection method used for consultative Call Transfers.

new-call : Digits are collected from the incoming call leg.

orig-call : Digits are collected from the original call-leg. It was the default behavior in versions before Cisco Unified SRST 4.3.

Step 5

end

### Example:

```
Router(config)# end
```

Returns to privileged EXEC mode.

### Example

The following example shows the transfer-digit-collect method set to the legacy value of orig-call:

```
!
call-manager-fallback
transfer-digit collect orig-call
!
```

## Configuring Global Prefixes

The dialplan-pattern command creates a dial-plan pattern that specifies a global prefix for the expansion of abbreviated extension numbers into
                              fully qualified E.164 numbers.

The extension-pattern keyword allows extra manipulation of abbreviated extension-number prefix digits. When this keyword and its argument are used,
                              the leading digits of an extension pattern are stripped and replaced by the corresponding leading digits of the dial-plan
                              pattern. This command can be used to avoid Direct Inward Dialing (DID) numbers like 408 555-0101 resulting in 4-digit extensions
                              such as 0101.

Global prefixes are set with the dialplan-pattern command. Up to five dial-plan patterns can be created. The no-reg keyword provides dialing flexibility and prevents the E.164 numbers in the dial peer from registering to the gatekeeper.
                              You have the option not to register numbers to the gatekeeper so that those numbers can be used for other telephony services.

### SUMMARY STEPS

- call-manager-fallback

- dialplan-pattern tag pattern extension-length length [ extension-pattern extension-pattern ] [ no-reg ]

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

dialplan-pattern tag pattern extension-length length [ extension-pattern extension-pattern ] [ no-reg ]

### Example:

```
Router(config-cm-fallback)# dialplan-pattern 1
4085550100 extension-length 3 extension-pattern
4..
```

This example maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension 412 corresponds to 4085550112.

Creates a global prefix that can be used to expand the abbreviated extension numbers into fully qualified E.164 numbers.

tag : Dial-plan string tag used before a 10-digit phone number. The tag number is 1–5.

pattern : Dial-plan pattern, such as the area code, the prefix, and the first one or two digits of the extension number, plus wildcard
                                                markers or dots (.) for the remainder of the extension number digits.

extension-length : Sets the number of extension digits.

length : The number of extension digits. The range is 1–32.

extension-pattern : Sets an extension number’s leading digit pattern when it is different from the E.164 phone number’s leading digits defined
                                                in the pattern argument.

extension-pattern : The extension number’s leading digit pattern. Consists of one or more digits and wildcard markers or dots (.). For example,
                                                5..would include extension 500–599; 5... would include 5000–5999.

no-reg : Prevents the E.164 numbers in the dial peer from registering with the gatekeeper.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example shows how to create dial-plan pattern 1 for extension numbers 101–199 with the phone prefix starting
                              with 4085550. If the following example is set, the router recognizes that 4085550144 matches dial-plan pattern 1. It uses
                              the extension-length keyword to extract the last three digits of the number 144 and present this as the caller ID for the incoming call.

```
call-manager-fallback
dialplan-pattern 1 40855501.. extension-length 3 no-reg
```

```
call-manager-fallback
dialplan-pattern 1 40855500.. extension-length 3 extension-pattern 4..
```

In the following example, the dialplan-pattern command creates dial-plan pattern 2 for extensions 801–899 with the phone prefix starting with 4085559. As each number in
                              the extension pattern is declared with the number command, two POTS dial peers are created. In the example, they are 801 (an
                              internal office number) and 4085559001 (an external number).

```
call-manager-fallback
dialplan-pattern 2 40855590.. extension-length 3 extension-pattern 8..
```

## Enabling Digit Translation Rules

Digit translation rules can be enabled during Cisco Unified Communications Manager fallback. Translation rules are a number-manipulation
                              mechanism that performs operations such as automatically adding phone area codes and prefix codes to dialed numbers.

Digit translation rules have many applications and variations. For further information about them, see Cisco IOS Voice Configuration Library .

If you are running Cisco Unified SRST 3.2 and later or Cisco Unified SRST 4.0 and later, use the configuration described in
                                          the Enabling Translation Profiles section instead of using the translate command as described below. Translation Profiles are new to Cisco Unified SRST 3.2 and provide added capabilities.

Translation rules can be used as follows:

To manipulate the answer number indication (ANI) (calling number) or Dialed Number Identification Service (DNIS) (called number)
                                    digits for a voice call.

To convert a phone number into a different number before the call is matched to an inbound dial peer or before the call is
                                    forwarded by the outbound dial peer.

To view the translation rules configured for your system, use the show translation-rule command.

### SUMMARY STEPS

- call-manager-fallback

- translate {called | calling} translation-rule-tag

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

translate {called | calling} translation-rule-tag

### Example:

```
Router(config-cm-fallback)# translate called 20
```

Applies a translation rule to modify the phone number dialed or received by any Cisco Unified IP Phone user while Cisco Unified
                                          Communications Manager fallback is active.

called : Applies the translation rule to an outbound call number.

calling : Applies the translation rule to an inbound call number.

translation-rule-tag : The reference number of the translation rule 1–2147483647.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example applies translation rule 10 to the calls coming into extension 1111. All inbound calls to 1111 will
                              go to 2222 during Cisco Unified Communications Manager fallback.

```
translation-rule 10
rule 1 1111 2222 abbreviated
exit
call-manager-fallback
translate calling 10
```

The following is a sample configuration of digit translation rule 20, where the priority of the translation rule is 1 (the
                              range is 1–15) and the abbreviated representation of a complete number (1234) is replaced with the number 2345:

```
translation-rule 20
rule 1 1234 2345 abbreviated
exit
```

## Enable Translation Profiles

Cisco Unified SRST 3.2 and later and Cisco Unified SRST 4.0 and later support translation profiles. Translation profiles are
                              the suggested way to allow you to group translation rules and provide instructions on how to apply the translation rules to
                              the following:

Called numbers

Calling numbers

Redirected called numbers

In the configuration below, the voice translation-rule and the rule command allow you to set and define how a number is to be manipulated. The translate command in voice translation-profile
                              mode defines the type of number you are going to manipulate, such as a called, calling, or a redirecting number. Once you
                              have defined your translation profiles, you can then apply the translation profiles in various places, such as dial peers
                              and voice ports. For SCCP SRST, you apply your profiles in Cisco Unified Communications Manager fallback mode.

Cisco IP phones support one incoming and one outgoing translation profile when in SRST mode.

For Cisco Unified SRST 3.2 and later versions and Cisco Unified SRST 4.0 and later versions, use the voice translation-rule and translation-profile commands shown below instead of the translation rule configuration described in the Enabling Digit Translation Rules section. Voice translation rules are a separate feature from translation rules. See the voice translation-rule command in Cisco IOS Voice Command Reference for more information and the VoIP Gateway Trunk and Carrier Based Routing Enhancements documentation for more general information on translation rules and profiles.

### SUMMARY STEPS

- voice translation-rule number

- rule precedence/match-pattern/ /replace-pattern/

- exit

- voice translation-profile name

- translate {called | calling | redirect-called} translation-rule-number

- exit

- call-manager-fallback

- translation-profile {incoming | outgoing} name

- exit

### DETAILED STEPS

Step 1

voice translation-rule number

### Example:

```
Router(config)# voice translation-rule 1
```

Defines a translation rule for voice calls and enters voice translation-rule configuration mode.

number : Number that identifies the translation rule. Range is 1–2147483647.

Step 2

rule precedence/match-pattern/ /replace-pattern/

### Example:

```
Router(cfg-translation-rule)# rule 1/^9/ //
```

Defines a translation rule.

precedence : Priority of the translation rule. Range is 1–15.

match-pattern : Stream editor (SED) expression used to match incoming call information. The slash (/) is a delimiter in the pattern.

replace-pattern : SED expression used to replace the match pattern in the call information. The slash (/) is a delimiter in the pattern.

Step 3

exit

### Example:

```
Router(cfg-translation-rule)# exit
```

Exits voice translation-rule configuration mode.

Step 4

voice translation-profile name

### Example:

```
Router(config)# voice translation-profile name1
```

Defines a translation profile for voice calls.

name : Name of the translation profile. Maximum length of the voice translation profile name is 31 alphanumeric characters.

Step 5

translate {called | calling | redirect-called} translation-rule-number

### Example:

```
Router(cfg-translation-profile)# translate
called 1
```

Associates a voice translation rule with a voice translation profile.

called : Associates the translation rule with called numbers.

calling : Associates the translation rule with calling numbers.

redirect-called : Associates the translation rule with redirected called numbers.

translation-rule-number : The reference number of the translation rule 1–2147483647.

Step 6

exit

### Example:

```
Router(cfg-translation-profile)# exit
```

Exits translation-profile configuration mode.

Step 7

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 8

translation-profile {incoming | outgoing} name

### Example:

```
Router(config-cm-fallback)# translation-profile
outgoing name1
```

Assigns a translation profile for incoming or outgoing call legs on a Cisco IP phone.

incoming : Applies the translation profile to incoming calls.

outgoing : Applies the translation profile to outgoing calls.

name : The name of the translation profile.

Step 9

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits from call-manager-fallback configuration mode.

### Example

The following example shows the configuration where a translation profile called name1 is created with two voice translation
                              rules. Rule1 consists of associated calling numbers, and rule2 consists of redirected called numbers. The Cisco Unified IP
                              Phones in SCCP SRST mode are configured with name1.

```
voice translation-profile name1
 translate calling 1
 translate called redirect-called 2

call-manager-fallback
 translation-profile incoming name1
```

## Verifying Translation Profiles

### Before you begin

### SUMMARY STEPS

- show voice translation-rule number

- test voice translation-rule number input-test-string [ test match-type [ plan match-type ] ]

### DETAILED STEPS

Step 1

show voice translation-rule number

### Example:

```
Router# show voice translation-rule 6
Translation-rule tag: 6
Rule 1:
Match pattern: 65088801..
Replace pattern: 6508880101
Match type: none Replace type: none
Match plan: none Replace plan: none
```

Use this command to verify the translation rules that you have defined for your translation profiles.

Step 2

test voice translation-rule number input-test-string [ test match-type [ plan match-type ] ]

### Example:

```
Router(config)# voice translation-rule 5
Router(cfg-translation-rule)# rule 1 /201/ /102/
Router(cfg-translation-rule)# end
Router# test voice translation-rule 5 2015550101
Matched with rule 5
Original number:2015550101 Translated
number:1025550101
Original number type: none Translated number
type: none
Original number plan: none Translated number
plan: none
```

Use this command to test your translation profiles. See the test voice translation-rule command in Cisco IOS Voice Command Reference for more information.

## Configuring Dial-Peer and Channel Hunting

Dial-peer hunting, the search through a group of dial peers for an available phone line, is disabled during Cisco Unified
                              Communications Manager fallback by default. To enable dial-peer hunting, use the no huntstop command. For more information
                              about dial-peer hunting, see Cisco IOS Voice Configuration Library .

If you have a dual-line phone configuration, see the Configuring Dual-Line Phones section. Keep incoming calls from hunting to the second channel if the first channel is busy or does not answer by using
                              the channel keyword in the huntstop command.

Channel huntstop also prevents situations in which a call can ring for 30 seconds on the first channel of a line with no person
                              available to answer and then ring for another 30 seconds on the second channel before rolling over to another line.

### SUMMARY STEPS

- call-manager-fallback

- huntstop [channel]

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

huntstop [channel]

### Example:

```
Router(config-cm-fallback)# huntstop channel
```

Sets the huntstop attribute for the dial peers associated with the Cisco Unified IP Phone dial peers created during Cisco
                                          Unified Communications Manager fallback.

• For dual-line configurations, the channel keyword keeps incoming calls from hunting to the second channel if the first channel is busy or does not answer.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example disables dial-peer hunting during Cisco Unified Communications Manager fallback and hunting to the secondary
                              channels in dual-line phone configurations:

```
call-manager-fallback
no huntstop channel
```

## Configuring Busy Timeout

This task sets the timeout value for Call Transfers to busy destinations. The busy timeout value is the amount of time that
                              can elapse after a transferred call reaches a busy signal before the call is disconnected.

### SUMMARY STEPS

- call-manager-fallback

- timeouts busy seconds

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

timeouts busy seconds

### Example:

```
Router(config-cm-fallback)# timeouts busy 20
```

Sets the amount of time for disconnecting the calls before transferring to busy destinations.

seconds : Number of seconds. Range is 0–30. Default is 10.

This command sets the busy timeout only for calls before transferring to busy destinations and does not affect the timeout
                                                      for calls that directly dial busy destinations.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example sets a timeout of 20 seconds for transferring calls to busy destinations:

```
call-manager-fallback
timeouts busy 20
```

## Configuring the Ringing Timeout Default

The ringing timeout default is the length of time for which a phone can ring with no answer before returning a disconnect
                              code to the caller. This timeout prevents hung calls received over interfaces such as Foreign Exchange Office (FXO) that do
                              not have forward-disconnect supervision. It is used only for extensions that do not have no-answer call forwarding enabled.

### SUMMARY STEPS

- call-manager-fallback

- timeouts ringing seconds

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

timeouts ringing seconds

### Example:

```
Router(config-cm-fallback)# timeouts ringing 30
```

Sets the ringing timeout default, in seconds. The range is from 5 to 60000. There is no default value.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example sets the ringing timeout default to 30 seconds:

```
call-manager-fallback
timeouts ringing 30
```

### Configuring Outgoing Calls

## Configuring Local and Remote Call Transfer

Configure the Cisco Unified SRST to allow Cisco Unified IP Phones to transfer phone calls from outside the local IP network
                              to another Cisco Unified IP Phone. By default, all Cisco Unified IP Phone directory numbers or virtual voice ports are allowed
                              as transfer targets. A maximum of 32 transfer patterns can be entered.

Call Transfer configuration is performed using the transfer-pattern command.

### SUMMARY STEPS

- call-manager-fallback

- transfer-pattern transfer-pattern

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

transfer-pattern transfer-pattern

### Example:

```
Router(config-cm-fallback)# transfer-pattern
52540..
```

Enables the transfer of a call from a non-IP phone number to another Cisco Unified IP Phone on the same IP network using the
                                          specified transfer pattern.

transfer-pattern : String of digits for permitted call

Transfers. Wildcards are permitted.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

In the following example, the transfer-pattern command permits transfers from a non-IP phone number to any Cisco Unified IP
                              Phone on the same IP network with a number in range 5550100–5550199:

```
call-manager-fallback
transfer-pattern 55501..
```

## Enabling Consultative Call Transfer and Forward Using H.450.2 and H.450.3 with Cisco Unified SRST 3.0

Consultative Call Transfer using H.450.2 adds support for initiating Call Transfers and call forwarding on a call leg using
                              the ITU-T H.450.2 and ITU-T H.450.3 standards. Call Transfers and call forwarding using H.450.2 and H.450.3 can be blind or
                              consultative. A blind Call Transfer or blind call forward is one in which the transferring or forwarding phone connects the
                              caller to a destination line before a ringing tone begins. Consultative transfer is one in which the transferring or forwarding
                              party either connects the caller to a ringing phone (ringback heard) or speaks with the third party before connecting the
                              caller to the third party.

For Cisco Unified SRST 3.1 and later versions and Cisco Unified SRST 4.0 and later versions, Call Transfer and call forward
                                          using H.450.2 is supported automatically with the default session application.

### Before you begin

Call Transfer with consultation is available only when an IP phone supports a second line or call instance. Please see the
                              dual-line keyword in the max-dn command.

All voice gateway routers in the VoIP network must support the H.450 standard.

All voice gateway routers in the VoIP network must be running the following software:

Cisco IOS Release 12.3(2)T or a later release

Cisco Unified SRST 3.0

Does not implement a H.450.12 Supplementary Services Capabilities Exchange among routers.

### SUMMARY STEPS

- call-manager-fallback

- call-forward pattern pattern

- transfer-system {blind | full-blind | full-consult | local-consult}

- transfer-pattern transfer-pattern

- exit

- (Optional) voice service voip

- (Optional) h323

- (Optional) h450 h450-2 timeout {T1 | T2 | T3 | T4} milliseconds

- (Optional) end

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

call-forward pattern pattern

### Example:

```
Router(config-cm-fallback)# call-forward
pattern 4...
```

Specifies the H.450.3 standard for a call forwarding.

pattern : Digits to match for a call forwarding using the H.450.3 standard. If an incoming calling-party number matches the pattern,
                                          it can be forwarded using the H.450.3 standard. A pattern of .T forwards all calling parties using the H.450.3 standard.

Step 3

transfer-system {blind | full-blind | full-consult | local-consult}

### Example:

```
Router(config-cm-fallback)# transfer-system
full-consult
```

Not supported if the transfer-to destination is on the Cisco ATA, Cisco VG224, or an SCCP-controlled FXS port.

Defines the call-transfer method for all lines served by the Cisco Unified SRST router.

blind : Calls are transferred without consultation with a single phone line using the Cisco proprietary method.

We do not recommend the blind keyword. Use either the full-blind or full-consult keyword instead.

full-blind : Calls are transferred without consultation using H.450.2 standard methods.

full-consult : Calls are transferred with consultation using a second phone line if available. The calls fall back to full-blind if the
                                                second line is unavailable.

local-consult : Calls are transferred with local consultation using a second phone line if available. The calls fall back to blind for nonlocal
                                                consultation or nonlocal transfer target.

Step 4

transfer-pattern transfer-pattern

### Example:

```
Router(config-cm-fallback)# transfer-pattern
52540..
```

Allows transfer of the phone calls by Cisco Unified IP Phones to specified phone number patterns.

transfer-pattern : String of digits for permitted Call Transfers. Wildcards are allowed.

Step 5

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

Timesaver : Before exiting call-manager-fallback configuration mode, configure any other parameters that you must set for the entire
                                          Cisco Unified SRST phone network.

Step 6

(Optional) voice service voip

### Example:

```
Router(config)# voice service voip
```

Enters voice service configuration mode.

Step 7

(Optional) h323

### Example:

```
Router(conf-voi-serv)# h323
```

Enters H.323 voice service configuration mode.

Step 8

(Optional) h450 h450-2 timeout {T1 | T2 | T3 | T4} milliseconds

### Example:

```
Router(conf-serv-h323)# h450 h450-2 timeout T1
750
```

Sets timeouts for supplementary service timers, in milliseconds. This command is used primarily when the default settings
                                          for these timers do not match your network delay parameters. See the ITU-T H.450.2 specification for more information on these
                                          timers.

T1 : Timeout value to wait to identify response. Default is 2000.

T2 : Timeout value to wait for a call setup. Default is 5000.

T3 : Timeout value to wait to initiate response. Default is 5000.

T4 : Timeout value to wait for setup of response. Default is 5000.

milliseconds : Number of milliseconds. Range is 500–60000.

Step 9

(Optional) end

### Example:

```
Router(conf-serv-h323)# end
```

Returns to privileged EXEC mode.

### Example

The following example specifies transfer with consultation using the H.450.2 standard for all IP phones serviced by the Cisco
                              Unified SRST router:

```
dial-peer voice 100 pots
destination-pattern 9.T
port 1/0/0
dial-peer voice 4000 voip
destination-pattern 4…
session-target ipv4:10.1.1.1
call-manager-fallback
transfer-pattern 4…
transfer-system full-consult
```

The following example enables call forwarding using the H.450.3 standard:

```
dial-peer voice 100 pots
 destination-pattern 9.T
 port 1/0/0
!
dial-peer voice 4000 voip
  destination-pattern 4
  session-target ipv4:10.1.1.1
!
call-manager-fallback
  call-forward pattern 4
```

## Enabling Analog Transfer Using Hookflash and the H.450.2 Standard with Cisco Unified SRST 3.0 or Earlier

Analog Call Transfer using hookflash and the H.450.2 standard allows analog phones to transfer calls with consultation by
                              using the hookflash to initiate transfer. Hookflash refers to the short on-hook period generated by a telephone-like device
                              during a call to indicate that the phone is attempting to perform the dial-tone recall from a PBX. Uses Hookflash to perform
                              Call Transfer. For example, a hookflash occurs when a caller quickly taps once on the button in the cradle of an analog phone’s
                              handset.

This feature requires installation of a Tool Command Language (Tcl) script. Download the script app-h450-transfer.tcl from
                              the Cisco Software Center at http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp and copied to a TFTP server that is available to the Cisco Unified SRST router or copied to the flash memory on the Cisco
                              Unified SRST router. To apply this script globally to all dial peers, use the call application global command in global configuration mode. The Tcl script has parameters to which you can pass values using attribute-value (AV)
                              pairs in the call application voice command. The parameter that applies to this feature is as follows:

delay-time : Speeds up or delays the setting up of the consultation call during a Call Transfer from an analog phone using a delay timer.
                                    On collecting all digits, the delay timer starts. The call setup to the receiving party does not begin until the delay timer
                                    expires. If the transferring party goes on-hook before the delay timer expires, the transfer is considered blind transfer
                                    rather than consultative transfer. If the transferring party goes on-hook after the delay timer expires, either while the
                                    destination phone is ringing or after the destination party answers, the transfer is considered consultative transfer.

In addition to the Tcl script, a ReadMe file describes the script and the configurable attribute-value pairs. Read this file
                              whenever you download a new version of the script because it may contain more script-specific information, such as configuration
                              parameters and user interface descriptions.

For Cisco Unified SRST 3.1 and later versions and Cisco Unified SRST 4.0 and later versions, Call Transfer using H.450.2 is
                                          supported automatically with the default session application.

Restrictions

When consultative transfer is made by an analog FXS phone using hookflash, the consultation call itself cannot be further
                                    transferred (that is, it cannot become a recursive or chained transfer) until after the initial transfer operation is completed
                                    and the transferee and transfer-to parties are connected. After the initial Call Transfer operation is completed and the transferee
                                    and transfer-to parties are now the only parties in the call, the transfer-to party may further transfer the call.

Call Transfer with consultation is not supported for Cisco ATA-186, Cisco ATA-188, and Cisco IP Conference Station 7935. Transfer
                                    attempts from these devices are executed as blind transfers.

### Before you begin

Download the H.450 Tcl script named app-h450-transfer.Tcl from the Cisco Software Center. The following versions of the script
                              are available:

app-h450-transfer.2.0.0.2.tcl for Cisco IOS Release 12.2(11)YT1 and later releases

app-h450-transfer.2.0.0.1.tcl for Cisco IOS Release 12.2(11)YT

All voice gateway routers in the VoIP network must support H.450 and be running the following software:

Cisco IOS Release 12.2(11)YT or a later release

Cisco Unified SRST V3.0 or a lower version

Tcl IVR 2.0

H.450 Tcl script (app-h450-transfer.Tcl)

You can continue to use the app-h450-transfer.2.0.0.1.tcl script if you install Cisco IOS Release 12.2(11)YT1 or later, but
                                          you cannot use the app-h450-transfer.2.0.0.2.tcl script with a release of Cisco IOS Software that is earlier than Cisco IOS
                                          Release 12.2(11)YT1.

### SUMMARY STEPS

- call application voice application-name location

- (Optional) call application voice application-name language number language

- call application voice application-name set-location language category location

- (Optional) call application voice application-name delay-time seconds

- dial-peer voice number pots

- application application-name

- exit

- dial-peer voice number voip

- application application-name

- exit

### DETAILED STEPS

Step 1

call application voice application-name location

### Example:

```
Router(config)# call application voice
transfer_app flash:app-h450-transfer.tcl
```

Loads the Tcl script and specifies its application name.

application-name : User-defined name for the IVR application. This name does not have to match the script filename.

location : Script directory and filename in URL format. For example, flash memory (flash:filename), a TFTP (tftp://../filename), or
                                                an HTTP server (http://../filename) are valid locations.

Step 2

(Optional) call application voice application-name language number language

### Example:

```
Router(config)# call application voice
transfer_app language 1 en
```

Sets the language for dynamic prompts by the application.

application-name : IVR application name that was assigned in Step 1.

number : Specify the number of languages for the audio files for the IVR application.

language : Two-character code that specifies the language of the prompts. Valid entries are en (English:default), sp (Spanish), ch
                                                (Chinese), or aa (all).

Step 3

call application voice application-name set-location language category location

### Example:

```
Router(config)# call application voice
transfer_app set-location en 0 flash:/prompts
```

Defines the location and category of the audio files that are used by the application for dynamic prompts.

application-name : Name of the Tcl IVR application.

language : Two-character code to specify the language of the prompts. Valid entries are en (English: default), sp (Spanish), ch (Chinese),
                                                or aa (all).

category : Category group (0–4) for the audio files from this location. The value 0 means all categories. .

location : URL of the directory that contains the language audio files in the application, without filenames. Flash memory (flash)
                                                or a directory on a server (TFTP, HTTP, or RTSP) are all valid.

Prompts are required for Call Transfer from analog FXS phones. No prompts are needed for Call Transfer from IP phones.

Step 4

(Optional) call application voice application-name delay-time seconds

### Example:

```
Router(config)# call application voice
transfer_app delay-time 1
```

Sets the delay time for consultation call setup for an analog phone that is making a Call Transfer using the H.450 application.
                                          This command passes a value to the Tcl script by using an attribute-value (AV) pair.

seconds : Number of seconds to delay call setup. Range is 1–10. Default is 2.

Delay of more than 2 seconds is noticeable to users.

For more information about attribute-value pairs and the Tcl script for H.450 Call Transfer and forwarding, see the ReadMe
                                          file that accompanies the script.

Step 5

dial-peer voice number pots

### Example:

```
Router(config)# dial-peer voice 25 pots
```

Enters dial-peer configuration mode to configure a POTS dial peer.

Step 6

application application-name

### Example:

```
Router(config-dial-peer)# application
transfer_app
```

Loads the application named in Step 1 onto the dial peer.

Step 7

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits dial-peer configuration mode.

Timesaver : Before exiting dial-peer configuration mode, configure any other dial-peer parameters that you must set for this dial peer.

Step 8

dial-peer voice number voip

### Example:

```
Router(config)# dial-peer voice 29 voip
```

Enters dial-peer configuration mode to configure a VoIP dial peer.

Step 9

application application-name

### Example:

```
Router(config-dial-peer)# application
transfer_app
```

Loads the application named in Step 1 onto the dial peer.

Step 10

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits dial-peer configuration mode.

Timesaver : Before exiting dial-peer configuration mode, configure any other dial-peer parameters that you must set for this dial peer.

### Example

The following example enables the H.450 Tcl script for analog transfer using hookflash and sets delay time of 1 second:

```
call application voice transfer_app flash:app-h450-transfer.tcl
call application voice transfer_app language 1 en
call application voice transfer_app set-location en 0 flash:/prompts
call application voice transfer_app delay-time 1
!
dial-peer voice 25 pots
destination-pattern 9.T
port 1/0/0
application transfer_app
!
dial-peer voice 29 voip
destination-pattern 4…
session-target ipv4:10.1.10.1
application transfer_app
```

## Configuring Trunk Access Codes

Configure trunk access codes only if your normal network dial-plan configuration prevents you from configuring a permanent
                                          POTS voice dial peer to provide trunk access for use during fallback. If you already have local PSTN ports configured with
                                          the appropriate access codes provided by dial peers (for example, dial 9 to select an FXO PSTN line), this configuration is
                                          not needed.

Trunk access codes provide IP phones with access to the PSTN during Cisco Unified Communications Manager fallback by creating
                              POTS voice dial peers that are active during Cisco Unified Communications Manager fallback only. These temporary dial peers,
                              which can be matched to voice ports (BRI, E&M, FXO, and PRI), allow Cisco Unified IP Phones access to trunk lines during Cisco
                              Unified Communications Manager mode. When Cisco Unified SRST is active, all PSTN interfaces of the same type are treated as
                              equivalent, and any port may be selected to place the outgoing PSTN call.

Trunk access codes are created using the access-code command.

### SUMMARY STEPS

- call-manager-fallback

- access-code { { fxo | e&m } dial-string  | { bri | pri } dial-string [ direct-inward-dial ]  }

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

access-code { { fxo | e&m } dial-string  | { bri | pri } dial-string [ direct-inward-dial ]  }

### Example:

```
Router(config-cm-fallback)# access-code e&m 8
```

Configures trunk access codes for each type of line so that the Cisco Unified IP Phones can access the trunk lines only in
                                          Cisco Unified Communications Manager fallback mode when the Cisco Unified SRST is enabled.

fxo : Enables a Foreign Exchange Office (FXO) interface.

e&m : Enables an analog Ear and Mouth (E&M) interface.

dial-string : String of characters that sets up dial access codes for each specified line type by creating dial peers. The dial-string
                                                argument is used to set up temporary dial peers for each specified line type.

bri : Enables a BRI interface.

pri : Enables a PRI interface.

direct-inward-dial : Enables Direct Inward Dialing (DID) on the POTS dial peer.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example creates access code number 8 for BRI and enables DID on the POTS dial peer:

```
call-manager-fallback
access-code bri 8 direct-inward-dial
```

## Configuring Interdigit Timeout Values

Configuring interdigit timeout values involves specifying how long, in seconds, all Cisco Unified IP Phones attached to a
                              Cisco Unified SRST router are to wait after an initial digit or a subsequent digit is dialed. The timeouts interdigit timer is enabled when a caller enters a digit and is restarted each time the caller enters subsequent digits until the destination
                              address is identified. If the configured timeout value is exceeded before the destination address is identified, a tone sounds
                              and the call is stopped.

### SUMMARY STEPS

- call-manager-fallback

- (Optional) timeouts interdigit seconds

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

(Optional) timeouts interdigit seconds

### Example:

```
Router(config-cm-fallback)# timeouts interdigit
5
```

Configures the interdigit timeout value for all Cisco IP phones that are attached to the router.

seconds : Interdigit timeout duration, in seconds, for all Cisco Unified IP Phones. Valid entries are integers from 2 to 120.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example sets the interdigit timeout value to 5 seconds for all Cisco Unified IP Phones. In this example, 5 seconds
                              are the elapsed time after which an incompletely dialed number times out. For example, a caller who dials nine digits (408555010)
                              instead of the required ten digits (4085550100) will hear a busy tone after the second timeout elapses.

```
call-manager-fallback
timeouts interdigit 5
```

## Configuring Class of Restriction

The class of restriction (COR) functionality provides the ability to deny a certain call attempt on the basis of the incoming
                              and outgoing class of restrictions that are provisioned on the dial peers. This functionality provides flexibility in the
                              network design, allows you to block calls (for example, calls to 900 numbers), and applies different restrictions to call
                              attempts from different originators. The cor command sets the dial-peer COR parameter for the dial peers associated with the directory numbers that are created during
                              Cisco Unified Communications Manager fallback.

You can have up to 20 COR lists for each incoming and outgoing call. A default COR is assigned to directory numbers that do
                              not match the COR list numbers or number ranges. An assigned COR is invoked for the dial peers and created for each directory
                              number automatically during Cisco Unified Communications Manager fallback registration.

If a COR is applied on an incoming dial peer (for incoming calls) and it is a superset of or is equal to the COR applied to
                              the outgoing dial peer (for outgoing calls), the call goes through. Voice ports determine whether a call is considered incoming
                              or outgoing. If you hook up a phone to an FXS port on a Cisco Unified SRST router and try to call from that phone, the call
                              will be considered an incoming call to the router and voice port. If you call the FXS phone, consider it as an outgoing call.

By default, an incoming call leg has the highest COR priority; the outgoing call leg has the lowest priority. If there is
                              no COR configuration for incoming calls on a dial peer, you can call from a phone that is attached to the dial peer, so that
                              the call goes out of any dial peer regardless of the COR configuration on that dial peer. The following table describes the
                              call functionality that is based on your COR lists configuration.

COR List on Incoming Dial Peer

COR List on Outgoing Dial Peer

Result

No COR

No COR

The call succeeds.

No COR

COR list applied for outgoing calls

The call succeeds. By default, the incoming dial peer has the highest COR priority when no COR is applied. If you apply no
                                          COR for an incoming call leg to a dial peer, the dial peer can call of any other dial peer regardless of the COR configuration
                                          on the outgoing dial peer.

COR list applied for incoming calls

No COR

The call succeeds. By default, the outgoing dial peer has the lowest priority. Because there are some COR configurations for
                                          incoming calls on the incoming or originating dial peer, it is a superset of the outgoing call’s COR configuration for the
                                          outgoing or stopping dial peer.

COR list applied for incoming calls (superset of a COR list applied for outgoing calls on the outgoing dial peer)

COR list applied for outgoing calls (subsets of a COR list applied for incoming calls on the incoming dial peer)

The call succeeds. The COR list for incoming calls on the incoming dial peer is a superset of the COR list for outgoing calls
                                          on the outgoing dial peer.

COR list applied for incoming calls (subset of a COR list applied for outgoing calls on the outgoing dial peer)

COR list applied for outgoing calls (supersets of a COR list applied for incoming calls on the incoming dial peer)

The call does not succeed. The COR list for incoming calls on the incoming dial peer is not a superset of the COR list for
                                          outgoing calls on the outgoing dial peer.

### SUMMARY STEPS

- call-manager-fallback

- cor {incoming | outgoing} cor-list-name [ cor-list-number starting-number - ending-number  | default ]

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

cor {incoming | outgoing} cor-list-name [ cor-list-number starting-number - ending-number  | default ]

### Example:

```
Router(config-cm-fallback)# cor outgoing
LockforPhoneC 1 5010 – 5020
```

Configures a COR on dial peers that are associated with directory numbers.

incoming : COR list to be used by incoming dial peers.

outgoing : COR list to be used by outgoing dial peers.

cor-list-name : COR list name.

cor-list-number : COR list identifier. You can create maximum 20 COR lists, comprising of incoming or outgoing dial peers. The first six
                                                COR lists are applied to range of directory numbers. Assign the COR configuration to the default COR list if the directory
                                                numbers do not have a COR configuration.

starting-number- ending-number: : Directory number range; for example, 2000–2025.

default : Instructs the router to use an existing default COR list.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example shows how to set a dial-peer COR parameter for outgoing calls to the Cisco Unified IP Phone dial peers
                              and directory numbers that are created during fallback:

```
call-manager-fallback
cor outgoing LockforPhoneC 1 5010 - 5020
```

The following example shows how to set the dial-peer COR parameter for incoming calls to the Cisco IP phone dial peers and
                              directory numbers in the default COR list:

```
call-manager-fallback
cor incoming LockforPhoneC default
```

The following example shows creation of a sub- and super-COR sets. First, create a custom dial-peer COR with declared names
                              under it:

```
dial-peer cor custom
name 911
name 1800
name 1900
name local_call
```

The following configuration example creates the COR lists and applies to the dial peer:

```
dial-peer cor list call911
member 911
dial-peer cor list call1800
member 1800
dial-peer cor list call1900
member 1900
dial-peer cor list calllocal
member local_call
dial-peer cor list engineering
member 911
member local_call
dial-peer cor list manager
member 911
member 1800
member 1900
member local_call
dial-peer cor list hr
member 911
member 1800
member local_call
```

The following example configures five dial peers for destination numbers 734…., 1800…….,1900……., 316…., and 911. A COR list
                              is applied to each of the dial peers.

```
dial-peer voice 1 voip
destination pattern 734....
session target ipv4:10.1.1.1
cor outgoing calllocal
dial-peer voice 2 voip
destination pattern 1800.......
session target ipv4:10.1.1.1
cor outgoing call1800
dial-peer voice 3 pots
destination pattern 1900.......
port 1/0/0
cor outgoing call1900
dial-peer voice 5 pots
destination pattern 316....
port 1/1/0
! No COR is applied.
dial-peer voice 4 pots
destination pattern 911
port 1/0/1
cor outgoing call911
```

Finally, the COR list is applied to the individual phone numbers.

```
call-manager-fallback
max-conferences 8
cor incoming engineering 1 1001 - 1001
cor incoming hr 2 1002 - 1002
cor incoming manager 3 1003 - 1008
```

The sample configuration allows for the following:

Extension 1001 to call 734... numbers, 911, and 316....

Extension 1002 to call 734..., toll-free numbers, 911, and 316....

Extension 1003–1008 to call all the possible Cisco Unified SRST router numbers.

All extensions to call 316....

## Call Blocking (Toll Bar) Based on Time of Day and Day of Week or Date

Call blocking to prevent unauthorized use of phones is implemented by matching a pattern of specified digits during specified
                              time of day and day of the week or date. Specify up to 32 patterns of digits. Supports call blocking on IP phones only and
                              not on analog Foreign Exchange Station (FXS) phones.

When you call to digits that match a pattern for call blocking during a defined time period for a call blocking, fast busy
                              signal plays for approximately 10 seconds. The call stops and places the line back in on-hook status.

In SRST (call-manager-fallback configuration) mode, there is no phone- or pin-based exemption to after-hours call blocking.

### SUMMARY STEPS

- call-manager-fallback

- after-hours block pattern tag pattern [ 7-24 ]

- after-hours day day start-time stop-time

- after-hours date month date start-time stop-time

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

after-hours block pattern tag pattern [ 7-24 ]

### Example:

```
Router(config-cm-fallback)# after-hours block
pattern 1 91900
```

For blocking, defines a pattern of outgoing digits. Define up to 32 patterns, using individual commands.

If you specify the 7–24 keyword, always blocks the pattern, 7 days a week, 24 hours a day.

If you do not specify the 7–24 keyword, blocks the pattern during the days and dates as defined in the after-hours day and
                                                after-hours date commands.

Step 3

after-hours day day start-time stop-time

### Example:

```
Router(config-cm-fallback)# after-hours day mon
19:00 7:00
```

Defines a recurring time period for the day of the week during which calls are blocked to outgoing dial patterns that are
                                          defined using the after-hours block pattern command.

day : Day of the week abbreviation. The following are valid day abbreviations: sun, mon, tue, wed, thu, fri, sat.

start-time stop-time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. If the stop time is smaller value
                                                than the start time, the stop time occurs on the day following the start time. For example, “mon 19:00 07:00” means “from
                                                Monday at 7 p.m. until Tuesday at 7 a.m.”.

Step 4

after-hours date month date start-time stop-time

### Example:

```
Router(config-cm-fallback)# after-hours date
jan 1 0:00 0:00
```

Defines a recurring time period for the month and date for blocking calls to outgoing dial patterns defined in the after-hours
                                          block pattern command.

month : Month abbreviation. The following are valid month abbreviations: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov,
                                                dec.

date : Date of the month. Range is 1–31.

start-time stop time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. The stop time must be larger than
                                                the start time. Value 24:00 is not valid. If you enter 00:00 as stop time, it changes to 23:59. If you enter 00:00 for both
                                                start time and stop time, blocks call for the entire 24-hour period on the specified date.

Step 5

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example defines several patterns of digits for which blocks outgoing calls. Patterns 1 and 2, blocks call to
                              external numbers that begin with “1” and “011”:

On Monday through Friday before 7 a.m. and after 7 p.m.

On Saturday before 7 a.m. and after 1 p.m.

All day Sunday.

Pattern 3 blocks call to 900 numbers 7 days a week, 24 hours a day.

```
call-manager-fallback
after-hours block pattern 1 91
after-hours block pattern 2 9011
after-hours block pattern 3 91900 7-24
after-hours block day mon 19:00 07:00
after-hours block day tue 19:00 07:00
after-hours block day wed 19:00 07:00
after-hours block day thu 19:00 07:00
after-hours block day fri 19:00 07:00
after-hours block day sat 13:00 12:00
after-hours block day sun 12:00 07:00
```

### How to Configure Cisco Unified SIP SRST

## Configuring SIP Phone Features

After setting the voice register Pool, the procedure adds optional features to increase functionality. Some features are per
                              Pool or globally.

In voice register pool configuration, you can now configure several new options per Pool (a Pool can be one phone or a group of phones). There is
                              also a new voice register global configuration mode for Cisco Unified SIP SRST. In the voice register global mode, you can
                              globally assign characteristics to phones.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global tag

- max-pool max-voice-register-pools

- application application-name

- external-ring {bellcore-dr1 | bellcore-dr2 |bellcore-dr3 | bellcore-dr4 | bellcore-dr5}

- exit

- voice register pool tag

- no vad

- codec codec-type [bytes]

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register global tag

### Example:

```
Router(config)# voice register global 12
```

Enters voice register global configuration mode to set global parameters for all supported Cisco SIP IP phones in a Cisco
                                          Unified SIP SRST environment.

Step 4

max-pool max-voice-register-pools

### Example:

```
Router(config-register-global)# max-pool 10
```

Set the maximum number of supported SIP voice register Pools in a Cisco Unified SIP SRST environment.

The max-voice-register-pools argument represents the maximum number of SIP voice register Pools supported by the Cisco Unified
                                          SIP SRST router. The upper limit of voice register Pools is version- and platform-dependent; see Cisco IOS command-line interface
                                          (CLI) help. Default is 0.

Step 5

application application-name

### Example:

```
Router(config-register-global)# application
global_app
```

Selects the session-level application for all dial peers associated with SIP phones. Use the application-name argument to
                                          define specific interactive voice response (IVR) application.

Step 6

external-ring {bellcore-dr1 | bellcore-dr2 |bellcore-dr3 | bellcore-dr4 | bellcore-dr5}

### Example:

```
Router(config-register-global)# external-ring
bellcore-dr1
```

Specifies the type of ring sound on Cisco SIP or Cisco SCCP IP phones for external calls. Each bellcore-dr 1–5 keyword supports
                                          standard distinctive ringing patterns as defined in the standard GR-506-CORE, LSSGR: Signaling for Analog Interfaces.

Step 7

exit

### Example:

```
Router(config-register-global)# exit
```

Exits voice register global configuration mode.

Step 8

voice register pool tag

### Example:

```
Router(config)# voice register pool 20
```

Enters voice register Pool configuration mode for SIP phones.

Use this command to control which phone registrations are accepted or rejected by a Cisco Unified SIP SRST device.

Step 9

no vad

### Example:

```
Router(config-register-pool)# no vad
```

Disables voice activity detection (VAD) on the VoIP dial peer.

VAD is enabled by default. Because there is no comfort noise during periods of silence, the call may disconnect. You may prefer
                                          to set no VAD on the SIP phone pool.

Step 10

codec codec-type [bytes]

### Example:

```
Router(config-register-pool)# codec g729r8
```

Specifies the supported codec by a single SIP phone or a VoIP dial peer in a Cisco Unified SIP SRST environment. The codec-type
                                          argument specifies the preferred codec and can be one of the following:

g711alaw : G.711 a–law 64,000 bps.

g711ulaw : G.711 mu–law 64,000 bps.

g729r8 : G.729 8000 bps (default).

The bytes argument is optional and specifies the number of bytes in the voice payload of each frame.

Step 11

end

### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

## Configuring SIP-to-SIP Call Forwarding

SIP-to-SIP call forwarding (call routing) is available. Call forwarding is provided either by the phone or by using a back-to-back
                              user agent (B2BUA), which allows call forwarding on any dial peer. Calls into a SIP device may be forwarded to other SIP or
                              SCCP devices (including Cisco Unity, third-party voicemail systems, or an auto attendant or IVR system such as Cisco Unified
                              Contact Center and Cisco Unified Contact Center Express). In addition, SCCP IP phones may be forwarded to SIP phones.

Cisco Unity or other voice messaging systems connected by a SIP trunk or SIP user agent are able to pass a message-waiting
                              indicator (MWI) when a message is left. The SIP phone then displays the MWI when indicated by the voice messaging system.

SIP-to-H.323 call forwarding is not supported.

To configure SIP-to-SIP call forwarding, you must first allow connections between specific types of endpoints in a Cisco IP-to-IP
                              gateway. The allow-connections command grants this capability. Once the SIP-to-SIP connections are allowed, you can configure call forwarding under an individual
                              SIP phone pool. Use any of the following commands to configure the call forwarding, according to your needs:

Under voice register pool

Call-forward b2bua all directory-number

Call-forward b2bua busy directory-number

Call-forward b2bua mailbox directory-number

Call-forward b2bua noan directory-number [timeout seconds]

A typical Cisco Unified SIP SRST setup does not use the call-forward b2bua mailbox command. However, Cisco Unified SIP Cisco
                              Unified Communications Manager Express environment uses this command. You can find the detailed procedures for configuring
                              the call-forward b2bua mailbox command in the Cisco Unified Communications Manager documentation on Cisco.com.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool tag voip

- encall-forward b2bua alld directory-number

- call-forward b2bua busy directory-number

- call-forward b2bua mailbox directory-number

- call-forward b2bua noan directory-number timeout seconds

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register pool tag voip

### Example:

```
Router(config)# voice register pool 15
```

Enters voice register Pool configuration mode.

Use this command to control the acceptance or rejections of the phone registrations on a Cisco Unified SIP SRST device.

Step 4

encall-forward b2bua alld directory-number

### Example:

```
Router(config-register-pool)# call-forward
b2bua all 5005
```

Enables call forwarding for a SIP back-to-back user agent (B2BUA) to forward all incoming calls to another non-SIP station
                                          extension. Namely to SIP trunk, H.323 trunk, SCCP device, and analog or digital trunk.

directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                          is 32.

Step 5

call-forward b2bua busy directory-number

### Example:

```
Router(config-register-pool)# call-forward
b2bua busy 5006
```

Enables call forwarding for a SIP B2BUA to forward incoming calls to a busy extension to another extension.

directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                          is 32.

Step 6

call-forward b2bua mailbox directory-number

### Example:

```
Router(config-register-pool)# call-forward
b2bua mailbox 5007
```

Controls the specific voicemail box in a voicemail system at the end of a call forwarding Exchange.

directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                          is 32.

Step 7

call-forward b2bua noan directory-number timeout seconds

### Example:

```
Router(config-register-pool)# call-forward
b2bua noan 5010 timeout 10
```

Enables call forwarding for a SIP B2BUA to forward incoming calls to an extension that does not answer after a configured
                                          amount of time to another extension.

Use this command if a phone is registered with a Cisco Unified SIP SRST router, but the phone is not reachable because there
                                          is no IP connectivity (there is no response to Invite requests).

directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                                is 32.

timeout seconds : Duration, in seconds, that a call can ring with no answer before the call is forwarded to another extension. Range is 3–60000.
                                                The default value is 20.

Step 8

end

### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

## Configuring Call Blocking Based on Time of Day, Day of Week, or Date

This section applies to both SCCP and SIP SRST. Call blocking prevents the unauthorized use of phones. It is implemented by
                              matching a pattern of up to 32 digits during specified time of day, day of the week, or date. Cisco Unified SIP SRST provides
                              SIP endpoints the same time-based call blocking mechanism as provided for SCCP phones. The call blocking feature supports
                              all incoming calls, including incoming SIP and analog FXS calls.

The Cisco Unified SIP SRST does not support the Pin-based exemptions and the “Login” toll-bar override.

Use the same commands for SIP phone call blocking and for SCCP phones on your Cisco Unified SRST system. The Cisco Unified
                              SRST session application accesses the current after-hours configuration under call-manager-fallback mode. It applies to calls
                              originated by Cisco SIP phones and registered to the Cisco Unified SRST router. The commands used in call-manager-fallback
                              mode that set block criteria (time or date or block pattern) are the following:

after-hours block pattern pattern-tag pattern [ 7-24 ]

after-hours day day start-time stop-time

after-hours date month date start-time stop-time

When you call to digits that match the specified patterns for call blocking during a defined time period for call blocking,
                              the call stops and the caller hears a fast busy.

In SRST (call-manager-fallback configuration mode), there is no phone- or pin-based exemption to after-hours call blocking.
                              However, in Cisco Unified SIP SRST (voice register Pool mode), individual IP phones can be exempted from all call blocking
                              using the after-hours exempt command.

### SUMMARY STEPS

- enable

- configure terminal

- call-manager-fallback

- after-hours block pattern tag pattern [ 7-24 ]

- after-hours day day start-time stop-time

- after-hours date month date start-time stop-time

- exit

- voice register pool tag

- after-hour exempt

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 4

after-hours block pattern tag pattern [ 7-24 ]

### Example:

```
Router(config-cm-fallback)# after-hours block
pattern 1 91900
```

For blocking, defines a pattern of outgoing digits. Define up to 32 patterns, using individual commands.

If you specify the 7–24 keyword, always blocks the pattern, 7 days a week, 24 hours a day.

If you do not specify the 7–24 keyword, blocks the pattern during the days and dates as defined in the after-hours day and after-hours date commands.

Step 5

after-hours day day start-time stop-time

### Example:

```
Router(config-cm-fallback)# after-hours day mon
19:00 7:00
```

Defines a recurring time period for the day of the week during which calls are blocked to outgoing dial patterns that are
                                          defined using the after-hours block pattern command.

day : Day of the week abbreviation. The following are valid day abbreviations: sun, mon, tue, wed, thu, fri, sat.

start-time stop-time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. If the stop time is smaller value
                                                than the start time, the stop time occurs on the day following the start time. For example, “mon 19:00 07:00” means “from
                                                Monday at 7 p.m. until Tuesday at 7 a.m.”.

Value 24:00 is not valid. If you enter 00:00 as stop time, it changes to 23:59. If you enter 00:00 for both start time and
                                                stop time, blocks call for the entire 24-hour period on the specified date.

Step 6

after-hours date month date start-time stop-time

### Example:

```
Router(config-cm-fallback)# after-hours date
jan 1 0:00 0:00
```

Defines a recurring time period for the month and date for blocking calls to outgoing dial patterns defined in the after-hours
                                          block pattern command.

month : Month abbreviation. The following are valid month abbreviations: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov,
                                                dec.

date : Date of the month. Range is 1–31.

start-time stop time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. The stop time must be larger than
                                                the start time.

Value 24:00 is not valid. If you enter 00:00 as stop time, it changes to 23:59. If you enter 00:00 for both start time and
                                                stop time, blocks call for the entire 24-hour period on the specified date.

Step 7

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

Step 8

voice register pool tag

### Example:

```
Router(config)# voice register pool 12
```

Enters voice register Pool configuration mode.

Use this command to control the accepted or rejected registrations by a Cisco Unified SIP SRST device.

Step 9

after-hour exempt

### Example:

```
Router(config-register-pool)# after-hour exempt
```

Specifies that for a particular voice register Pool, does not block the outgoing calls although call blocking is enabled.

Step 10

end

### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

### Example

The following example defines several patterns of digits for which blocks outgoing calls. Patterns 1 and 2, blocks call to
                              external numbers that begin with “1” and “011”:

On Monday through Friday before 7 a.m. and after 7 p.m.

On Saturday before 7 a.m. and after 1 p.m.

All day Sunday.

Pattern 3 blocks call to 900 numbers 7 days a week, 24 hours a day.

```
call-manager-fallback
after-hours block pattern 1 91
after-hours block pattern 2 9011
after-hours block pattern 3 91900 7-24
after-hours day mon 19:00 07:00
after-hours day tue 19:00 07:00
after-hours day wed 19:00 07:00
after-hours day thu 19:00 07:00
after-hours day fri 19:00 07:00
```

The following example exempts a Cisco SIP phone pool from the configured blocking criteria:

```
voice register pool 1
after-hour exempt
```

### Verification

To verify the feature’s configuration, enter one of the following commands:

show voice register dial-peer : Displays all the dial peers created dynamically by phones that have registered. This command also displays configurations
                                    for after hours blocking and call forwarding.

show voice register pool tag : Displays information about a specific Pool.

debug ccsip message : Debugs basic B2BUA calls.

For more information about these commands, see Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

## SIP Call Hold and Resume

Cisco Unified SRST supports the ability for SIP phones to place calls on hold and to resume from calls placed on hold. It
                           also includes support for consultative hold where A calls B, B place A on hold, B calls C, and B disconnects from C and then
                           resumes with A. Support for a call hold is signaled by SIP phones using “re-INVITE c=0.0.0.0” and also by the receive-only
                           mechanism.

No configuration is necessary.

```
Router# show running-config
Building configuration...
Current configuration : 1462 bytes
configuration mode exclusive manual
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service internal
!
boot-start-marker
boot-end-marker
!
logging buffered 8000000 debugging
!
no aaa new-model
!
resource policy
!
clock timezone edt -5
clock summer-time edt recurring
ip subnet-zero
!
!
!
ip cef
!
!
!
voice-card 0
no dspfarm
!
!
voice service voip
allow-connections h323 to h323
allow-connections h323 to sip
allow-connections sip to h323
allow-connections sip to sip
sip
registrar server expires max 600 min 60
!
!
!
voice register global
max-dn 10
max-pool 10
!
! Define call forwarding under a voice register pool
voice register pool 1
id mac 0012.7F57.60AA
number 1 1000
call-forward b2bua busy 2413
call-forward b2bua noan 2414 timeout 30
codec g711ulaw
!
voice register pool 2
id mac 0012.7F3B.9025
number 1 2800
codec g711ulaw
!
voice register pool 3
id mac 0012.7F57.628F
number 1 2801
codec g711ulaw
!
!
!
interface GigabitEthernet0/0
ip address 10.0.2.99 255.255.255.0
duplex auto
speed auto
!
interface GigabitEthernet0/1
no ip address
shutdown
duplex auto
speed auto
!
ip classless
ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0
!
ip http server
!
!
!
control-plane
!
!
!
dial-peer voice 1000 voip
destination-pattern 24..
session protocol sipv2
session target ipv4:10.0.2.5
codec g711ulaw
!
! Define call blocking under call-manager-fallback mode
call-manager-fallback
max-conferences 4 gain -6
after-hours block pattern 1 2417
                  after-hours date Dec 25 12:01 20:00
                  !
                  !
                  line con 0
                  exec-timeout 0 0
                  line aux 0
                  line vty 0 4
                  login
                  !
                  scheduler allocate 20000 1000
                  ntp server 10.0.2.10
                  !
                  end
```

## Enable Translation Profiles for SIP SRST

Cisco Unified SRST 3.2 and later and Cisco Unified SRST 4.0 and later support translation profiles. Translation profiles are
                              the suggested way to allow you to group translation rules and provide instructions on how to apply the translation rules to
                              the following:

Called numbers

Calling numbers

Redirected called numbers

To enable translation-rule, see Enabling Digit Translation Rules section.

In the configuration below, the voice translation-rule and the rule command allow you to set and define how a number is to be manipulated. The translate command in voice translation-profile
                              mode defines the type of number you are going to manipulate, such as a called, calling, or a redirecting number. Once you
                              have defined your translation profiles, you can then apply the translation profiles in various places, such as dial peers
                              and voice ports. For SRST, you apply your profiles in Cisco Unified Communications Manager fallback mode.

Cisco IP phones support one incoming and one outgoing translation profile when in SRST mode.

For Cisco Unified SRST 3.2 and later versions and Cisco Unified SRST 4.0 and later versions, use the voice translation-rule and translation-profile commands shown below instead of the translation rule configuration described in the Enabling Digit Translation Rules section. Voice translation rules are a separate feature from translation rules. See the voice translation-rule command in Cisco IOS Voice Command Reference for more information and the VoIP Gateway Trunk and Carrier Based Routing Enhancements documentation for more general information on translation rules and profiles.

### SUMMARY STEPS

- voice translation-rule number

- rule precedence/match-pattern/ /replace-pattern/

- exit

- voice translation-profile name

- translate {called | calling | redirect-called} translation-rule-number

- exit

- voice register pool pool-tag

- translation-profile {incoming | outgoing} name

- exit

### DETAILED STEPS

Step 1

voice translation-rule number

### Example:

```
Router(config)# voice translation-rule 1
```

Defines a translation rule for voice calls and enters voice translation-rule configuration mode.

number : Number that identifies the translation rule. Range is 1–2147483647.

Step 2

rule precedence/match-pattern/ /replace-pattern/

### Example:

```
Router(cfg-translation-rule)# rule 1/^9/ //
```

Defines a translation rule.

precedence : Priority of the translation rule. Range is 1–15.

match-pattern : Stream editor (SED) expression used to match incoming call information. The slash (/) is a delimiter in the pattern.

replace-pattern : SED expression used to replace the match pattern in the call information. The slash (/) is a delimiter in the pattern.

Step 3

exit

### Example:

```
Router(cfg-translation-rule)# exit
```

Exits voice translation-rule configuration mode.

Step 4

voice translation-profile name

### Example:

```
Router(config)# voice translation-profile name1
```

Defines a translation profile for voice calls.

name : Name of the translation profile. Maximum length of the voice translation profile name is 31 alphanumeric characters.

Step 5

translate {called | calling | redirect-called} translation-rule-number

### Example:

```
Router(cfg-translation-profile)# translate
called 1
```

Associates a voice translation rule with a voice translation profile.

called : Associates the translation rule with called numbers.

calling : Associates the translation rule with calling numbers.

redirect-called : Associates the translation rule with redirected called numbers.

translation-rule-number : The reference number of the translation rule 1–2147483647.

Step 6

exit

### Example:

```
Router(cfg-translation-profile)# exit
```

Exits translation-profile configuration mode.

Step 7

voice register pool pool-tag

### Example:

```
Router(config)# voice register pool 10
```

Enters voice register pool configuration mode for SIP phones.

pool-tag : Indicates an unique number assigned to the pool. Range is 1 to 100.

Step 8

translation-profile {incoming | outgoing} name

### Example:

```
Router(config-register-pool)# translation-profile
outgoing name1
```

Assigns a translation profile for incoming or outgoing call legs on a Cisco IP phone.

incoming : Applies the translation profile to incoming calls.

outgoing : Applies the translation profile to outgoing calls.

name : The name of the translation profile.

Step 9

exit

### Example:

```
Router(config-register-pool)# exit
```

Exits from voice register pool configuration mode.

### Example

The following example shows the configuration where a translation profile called name1 is created with two voice translation
                              rules. Rule1 consists of associated calling numbers, and rule2 consists of redirected called numbers. The Cisco Unified IP
                              Phones in SIP SRST mode are configured with name1.

```
voice translation-profile name1
 translate calling 1
 translate called redirect-called 2

voice register pool 10
 translation-profile incoming name1
```

For verification of translation profile configuration, see Verifying Translation Profiles.

## How to Configure Optional Features

This section describes the following optional more call features:

Three-party G.711 ad hoc conferencing—Cisco Unified Survivable Remote Site Telephony (SRST) support for simultaneous three-party
                                 conferences.

XML application program interface (API)—This interface supplies data from Cisco Unified SRST to management software.

The following sections describe how to configure these optional features:

Enabling Three-Party G.711 Ad Hoc Conferencing

Defining XML API Schema

### Enabling Three-Party G.711 Ad Hoc Conferencing

The enabling three-party G.711 ad hoc conferencing involves configuring the maximum number supported simultaneous three-party
                                 conferences by the Cisco Unified SRST router. For conferencing to be available, connect minimum of two lines to one or more
                                 buttons in an IP phone. See the Configuring a Secondary Dial Tone section.

### SUMMARY STEPS

- call-manager-fallback

- max-conferences max-conference-numbers

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

max-conferences max-conference-numbers

#### Example:

```
Router(config-cm-fallback)# max-conferences 16
```

Sets the maximum number of supported simultaneous three-party conferences by the router. The maximum number possible is platform-dependent:

Cisco 1751 router: 8

Cisco 1760 router: 8

Cisco 2600 series routers: 8

Cisco 2600-XM series routers: 8

Cisco 2801 router: 8

Cisco 2811, Cisco 2821, and Cisco 2851 routers: 16

Cisco 3640 and Cisco 3640A routers: 8

Cisco 3660 router: 16

Cisco 3725 router: 16

Cisco 3745 router: 16

Cisco 3800 Series router: 24

Step 3

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Example

The following example configures up to eight simultaneous three-way conferences on a router:

```
call-manager-fallback
max-conferences 8
```

### Defining XML API Schema

The Cisco IOS commands in this section allow you to specify parameters associated with the XML API. For more information,
                                 see XML Provisioning Guide for Cisco CME/SRST . See the Enabling Consultative Call Transfer and Forward Using H.450.2 and H.450.3 with Cisco Unified SRST 3.0 section for configuration instructions.

### SUMMARY STEPS

- call-manager-fallback

- xmlschema schema-url

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

xmlschema schema-url

#### Example:

```
Router(config-cm-fallback)# xmlschema
http://server2.example.com/
schema/schema1.xsd
```

Specifies the URL for an XML API schema to be used with this Cisco Unified SRST system.

schema-url : Local or remote URL as defined in RFC 2396.

Step 3

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Configuration Examples for Call Handling

## Example: Monitoring the Status of Key Expansion Modules

Use the Show commands to monitor the status and other details of Key Expansion Modules (KEMs).

The following example demonstrates how the show voice register all command displays KEM details with all the Cisco Unified Communications Manager Express configurations and registration information:

```
show voice register all
VOICE REGISTER GLOBAL
=====================
CONFIG [Version=9.1]
========================
............
Pool Tag 5
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM
Number list 1 : DN 2
Number list 2 : DN 3
Proxy Ip address is 0.0.0.0
DTMF Relay is disabled
Call Waiting is enabled
DnD is disabled
Video is enabled
Camera is enabled
Busy trigger per button value is 0
keep-conference is enabled
registration expires timer max is 200 and min is 60
kpml signal is enabled
Lpcor Type is none
```

The following example demonstrates how the show voice register pool type command displays all the configured phones with add-on KEMs in Cisco Unified Communications Manager Express:

```
Router# show voice register pool type CKEM
Pool ID              IP Address      Ln DN Number                State
==== =============== =============== == === ==================== ============
4    B4A4.E328.4698  9.45.31.111     1  4   5589$                REGISTERED
```

## Example: Configuring Voice Hunt Groups in Cisco Unified SIP SRST

The following example shows how to configure longest-idle hunt group 20 with pilot number 4701, final number 5000, and 6 numbers
                              in the list. After directing a call six times (makes 6 hops), it is redirected to the final number 5000.

```
Router(config)# voice hunt-group 20 longest-idle
Router(config-voice-hunt-group)# pilot 4701
Router(config-voice-hunt-group)# list 4001, 4002, 4023, 4028, 4045, 4062
Router(config-voice-hunt-group)# final 5000
Router(config-voice-hunt-group)# hops 6
Router(config-voice-hunt-group)# timeout 20
Router(config-voice-hunt-group)# exit
```

## Where to Go Next

If you must configure security, see the  section, or if you must configure voicemail, see the Integrating Voicemail with Cisco Unified SRST section. If you must configure video parameters, see the Setting Video Parameters section. If you do not need any of those features, go to the Monitoring and Maintaining Cisco Unified SRST section.

For additional information, see the Related Documents and References section in the Cisco Unified SRST Feature Overview chapter.

| Note | Configuring Call Handling for SIP phones applies to versions 4.0 and 3.4 only. |
|---|---|

| Note | H.323 is deprecated from  IOS XE 17.6.1. |
|---|---|

| Note | The following table is not all-inclusive; more commands may exist. |
|---|---|

| Command | Dial Peer | Voice Register Mode | Configurable for Cisco Unified (SIP) Cisco Unified Communications Manager Express and Cisco Unified SIP SRST | Applicable to Cisco Unified (SIP) Cisco Unified Communications Manager Express Only |
|---|---|---|---|---|
| After-hour exempt | X | DN | X | — |
| Auto-answer | — | DN | — | X |
| Call forward | X | DN | X | — |
| Huntstop | X | DN | X | — |
| Label | — | DN | — | X |
| Name | — | DN | — | X |
| Number | X | DN | X | — |
| Preference | X | DN | X | — |
| Application | X | Global | X | — |
| Authenticate | — | Global | — | X |
| Create | — | Global | — | X |
| Date-format | — | Global | — | X |
| DST | — | Global | — | X |
| External ring | — | Global | X | — |
| File | — | Global | — | X |
| Hold-alert | — | Global | — | X |
| Load | — | Global | — | X |
| Logo | — | Global | — | X |
| Max-dn | — | Global | X | — |
| Max-pool | — | Global | X | — |
| Max-redirect | — | Global | — | X |
| Mode | — | Global | X | — |
| MWI | — | Global | — | X |
| Reset | — | Global | — | X |
| Tftp-path | — | Global | — | X |
| Time zone | — | Global | — | X |
| Upgrade | — | Global | — | X |
| Url | — | Global | — | X |
| Voicemail | — | Global | — | X |
| After-hour exempt | X | Pool | X | — |
| Application | X | Pool | X | — |
| Call-forward | — | Pool | X | — |
| Call-waiting | — | Pool | — | X |
| Codec | X | Pool | X | — |
| Description | — | Pool | — | X |
| Dnd-control | — | Pool | — | X |
| Dtmf-relay | — | Pool | X | — |
| Id | — | Pool | X | — |
| Keep-conference | — | Pool | — | X |
| Max-pool | — | Pool | X | — |
| Number | X | Pool | X | — |
| Preference | X | Pool | X | — |
| Proxy | X | Pool | X | — |
| Reset | — | Pool | — | X |
| Speed-dial | — | Pool | — | X |
| Template | — | Pool | — | X |
| Translation-profile | X | Pool | X | — |
| Type | — | Pool | — | X |
| Username | — | Pool | — | X |
| VAD | X | Pool | X | — |
| Anonymous | — | Template | — | X |
| Caller-id | — | Template | — | X |
| Conference | — | Template | — | X |
| Dnd-control | — | Template | — | X |
| Forward | — | Template | — | X |
| Transfer | — | Template | — | X |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | call-forward busy directory-number Example: Router(config-cm-fallback)# call-forward busy
50.. | Configures call forwarding to another number when the Cisco IP phone is busy. directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters
                                          that correspond to the right-justified digits in the directory number extension. |
| Step 3 | call-forward noan directory-number timeout seconds Example: Router(config-cm-fallback)# call-forward noan
5005 timeout 10 | Configures call forwarding to another number when receiving no answer from the Cisco IP phone. directory-number : Selected directory number representing a fully qualified E.164 number or a local extension number. This number can contain
                                                “.” wildcard characters that correspond to the right-justified digits in the directory number extension. timeout seconds : Sets the waiting time, in seconds, before the call is forwarded to another phone. The seconds range is 3–60000. |
| Step 4 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | We recommend the alias command, which obsoletes the default-destination command, instead of the default-destination command. |
|---|---|

| Note | The default phone load on Cisco Unified Communications Manager, Release 4.0(1) for the Cisco 7905 and Cisco 7912 IP phones
                                          does not enable the PickUp softkey during fallback. To enable the PickUp softkey on Cisco 7905 and Cisco 7912 IP phones, upgrade
                                          your default phone load to Cisco Unified Communications Manager, Version 4.0(1) Sr2. Alternatively, you can upgrade the phone
                                          load to cmterm-7905g-sccp.3-3-8.exe or cmterm-7912g-sccp.3-3-8.exe , respectively. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | no huntstop Example: Router(config-cm-fallback)# no huntstop | Disables huntstop. |
| Step 3 | alias tag number-pattern to alternate-number Example: Router(config-cm-fallback)# alias 1 8005550100
to 5001 | Creates a set rule for rerouting calls to sets of phones that are unavailable during Cisco Unified Communications Manager
                                          fallback. tag : Identifier for the alias rule range. Range is from 1to 50. number-pattern : Pattern to match the incoming phone number. This pattern may include wildcards. to : Connects the tag number pattern to the alternate number. alternate-number : Alternate phone number to route incoming calls to match the number pattern. The alternate number has to be a specific extension
                                                that belongs to an IP phone that is actively registered on the Cisco Unified SRST router. The alternate phone number can be
                                                used in multiple alias commands. |
| Step 4 | pickup telephone number Example: Router(config-cm-fallback)# pickup 8005550100 | Enables the PickUp softkey on all Cisco Unified IP Phones, allowing an external Direct Inward Dialing (DID) call coming into
                                          one extension to be picked up from another extension during SRST. The telephone-number argument is the phone number to match
                                          an incoming called number. |
| Step 5 | end Example: Router(config-cm-fallback)# end | Returns to privileged EXEC mode. |

| Note | The enhancement, by default, collects the transfer digits from the incoming call leg. If necessary, you can configure the
                                       system to collect the transfer digits from the original call leg. See the Configuring Transfer Digit Collection Method section. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 4 | transfer-digit-collect {new-call \| orig-call} Example: Router(config-cm-fallback)#
transfer-digit-collect orig-call | Selects the digit-collection method used for consultative Call Transfers. new-call : Digits are collected from the incoming call leg. orig-call : Digits are collected from the original call-leg. It was the default behavior in versions before Cisco Unified SRST 4.3. |
| Step 5 | end Example: Router(config)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | dialplan-pattern tag pattern extension-length length [ extension-pattern extension-pattern ] [ no-reg ] Example: Router(config-cm-fallback)# dialplan-pattern 1
4085550100 extension-length 3 extension-pattern
4.. | Note This example maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension 412 corresponds to 4085550112. Creates a global prefix that can be used to expand the abbreviated extension numbers into fully qualified E.164 numbers. tag : Dial-plan string tag used before a 10-digit phone number. The tag number is 1–5. pattern : Dial-plan pattern, such as the area code, the prefix, and the first one or two digits of the extension number, plus wildcard
                                                markers or dots (.) for the remainder of the extension number digits. extension-length : Sets the number of extension digits. length : The number of extension digits. The range is 1–32. extension-pattern : Sets an extension number’s leading digit pattern when it is different from the E.164 phone number’s leading digits defined
                                                in the pattern argument. extension-pattern : The extension number’s leading digit pattern. Consists of one or more digits and wildcard markers or dots (.). For example,
                                                5..would include extension 500–599; 5... would include 5000–5999. no-reg : Prevents the E.164 numbers in the dial peer from registering with the gatekeeper. | Note | This example maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension 412 corresponds to 4085550112. |
| Note | This example maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension 412 corresponds to 4085550112. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | This example maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension 412 corresponds to 4085550112. |
|---|---|

| Note | Digit translation rules have many applications and variations. For further information about them, see Cisco IOS Voice Configuration Library . If you are running Cisco Unified SRST 3.2 and later or Cisco Unified SRST 4.0 and later, use the configuration described in
                                          the Enabling Translation Profiles section instead of using the translate command as described below. Translation Profiles are new to Cisco Unified SRST 3.2 and provide added capabilities. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | translate {called \| calling} translation-rule-tag Example: Router(config-cm-fallback)# translate called 20 | Applies a translation rule to modify the phone number dialed or received by any Cisco Unified IP Phone user while Cisco Unified
                                          Communications Manager fallback is active. called : Applies the translation rule to an outbound call number. calling : Applies the translation rule to an inbound call number. translation-rule-tag : The reference number of the translation rule 1–2147483647. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | For Cisco Unified SRST 3.2 and later versions and Cisco Unified SRST 4.0 and later versions, use the voice translation-rule and translation-profile commands shown below instead of the translation rule configuration described in the Enabling Digit Translation Rules section. Voice translation rules are a separate feature from translation rules. See the voice translation-rule command in Cisco IOS Voice Command Reference for more information and the VoIP Gateway Trunk and Carrier Based Routing Enhancements documentation for more general information on translation rules and profiles. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | voice translation-rule number Example: Router(config)# voice translation-rule 1 | Defines a translation rule for voice calls and enters voice translation-rule configuration mode. number : Number that identifies the translation rule. Range is 1–2147483647. |
| Step 2 | rule precedence/match-pattern/ /replace-pattern/ Example: Router(cfg-translation-rule)# rule 1/^9/ // | Defines a translation rule. precedence : Priority of the translation rule. Range is 1–15. match-pattern : Stream editor (SED) expression used to match incoming call information. The slash (/) is a delimiter in the pattern. replace-pattern : SED expression used to replace the match pattern in the call information. The slash (/) is a delimiter in the pattern. |
| Step 3 | exit Example: Router(cfg-translation-rule)# exit | Exits voice translation-rule configuration mode. |
| Step 4 | voice translation-profile name Example: Router(config)# voice translation-profile name1 | Defines a translation profile for voice calls. name : Name of the translation profile. Maximum length of the voice translation profile name is 31 alphanumeric characters. |
| Step 5 | translate {called \| calling \| redirect-called} translation-rule-number Example: Router(cfg-translation-profile)# translate
called 1 | Associates a voice translation rule with a voice translation profile. called : Associates the translation rule with called numbers. calling : Associates the translation rule with calling numbers. redirect-called : Associates the translation rule with redirected called numbers. translation-rule-number : The reference number of the translation rule 1–2147483647. |
| Step 6 | exit Example: Router(cfg-translation-profile)# exit | Exits translation-profile configuration mode. |
| Step 7 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 8 | translation-profile {incoming \| outgoing} name Example: Router(config-cm-fallback)# translation-profile
outgoing name1 | Assigns a translation profile for incoming or outgoing call legs on a Cisco IP phone. incoming : Applies the translation profile to incoming calls. outgoing : Applies the translation profile to outgoing calls. name : The name of the translation profile. |
| Step 9 | exit Example: Router(config-cm-fallback)# exit | Exits from call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | show voice translation-rule number Example: Router# show voice translation-rule 6
Translation-rule tag: 6
Rule 1:
Match pattern: 65088801..
Replace pattern: 6508880101
Match type: none Replace type: none
Match plan: none Replace plan: none | Use this command to verify the translation rules that you have defined for your translation profiles. |
| Step 2 | test voice translation-rule number input-test-string [ test match-type [ plan match-type ] ] Example: Router(config)# voice translation-rule 5
Router(cfg-translation-rule)# rule 1 /201/ /102/
Router(cfg-translation-rule)# end
Router# test voice translation-rule 5 2015550101
Matched with rule 5
Original number:2015550101 Translated
number:1025550101
Original number type: none Translated number
type: none
Original number plan: none Translated number
plan: none | Use this command to test your translation profiles. See the test voice translation-rule command in Cisco IOS Voice Command Reference for more information. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | huntstop [channel] Example: Router(config-cm-fallback)# huntstop channel | Sets the huntstop attribute for the dial peers associated with the Cisco Unified IP Phone dial peers created during Cisco
                                          Unified Communications Manager fallback. • For dual-line configurations, the channel keyword keeps incoming calls from hunting to the second channel if the first channel is busy or does not answer. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | timeouts busy seconds Example: Router(config-cm-fallback)# timeouts busy 20 | Sets the amount of time for disconnecting the calls before transferring to busy destinations. seconds : Number of seconds. Range is 0–30. Default is 10. Note This command sets the busy timeout only for calls before transferring to busy destinations and does not affect the timeout
                                                      for calls that directly dial busy destinations. | Note | This command sets the busy timeout only for calls before transferring to busy destinations and does not affect the timeout
                                                      for calls that directly dial busy destinations. |
| Note | This command sets the busy timeout only for calls before transferring to busy destinations and does not affect the timeout
                                                      for calls that directly dial busy destinations. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | This command sets the busy timeout only for calls before transferring to busy destinations and does not affect the timeout
                                                      for calls that directly dial busy destinations. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | timeouts ringing seconds Example: Router(config-cm-fallback)# timeouts ringing 30 | Sets the ringing timeout default, in seconds. The range is from 5 to 60000. There is no default value. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | transfer-pattern transfer-pattern Example: Router(config-cm-fallback)# transfer-pattern
52540.. | Enables the transfer of a call from a non-IP phone number to another Cisco Unified IP Phone on the same IP network using the
                                          specified transfer pattern. transfer-pattern : String of digits for permitted call Transfers. Wildcards are permitted. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | For Cisco Unified SRST 3.1 and later versions and Cisco Unified SRST 4.0 and later versions, Call Transfer and call forward
                                          using H.450.2 is supported automatically with the default session application. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | call-forward pattern pattern Example: Router(config-cm-fallback)# call-forward
pattern 4... | Specifies the H.450.3 standard for a call forwarding. pattern : Digits to match for a call forwarding using the H.450.3 standard. If an incoming calling-party number matches the pattern,
                                          it can be forwarded using the H.450.3 standard. A pattern of .T forwards all calling parties using the H.450.3 standard. |
| Step 3 | transfer-system {blind \| full-blind \| full-consult \| local-consult} Example: Router(config-cm-fallback)# transfer-system
full-consult | Not supported if the transfer-to destination is on the Cisco ATA, Cisco VG224, or an SCCP-controlled FXS port. Defines the call-transfer method for all lines served by the Cisco Unified SRST router. blind : Calls are transferred without consultation with a single phone line using the Cisco proprietary method. Note We do not recommend the blind keyword. Use either the full-blind or full-consult keyword instead. full-blind : Calls are transferred without consultation using H.450.2 standard methods. full-consult : Calls are transferred with consultation using a second phone line if available. The calls fall back to full-blind if the
                                                second line is unavailable. local-consult : Calls are transferred with local consultation using a second phone line if available. The calls fall back to blind for nonlocal
                                                consultation or nonlocal transfer target. | Note | We do not recommend the blind keyword. Use either the full-blind or full-consult keyword instead. |
| Note | We do not recommend the blind keyword. Use either the full-blind or full-consult keyword instead. |
| Step 4 | transfer-pattern transfer-pattern Example: Router(config-cm-fallback)# transfer-pattern
52540.. | Allows transfer of the phone calls by Cisco Unified IP Phones to specified phone number patterns. transfer-pattern : String of digits for permitted Call Transfers. Wildcards are allowed. |
| Step 5 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. Timesaver : Before exiting call-manager-fallback configuration mode, configure any other parameters that you must set for the entire
                                          Cisco Unified SRST phone network. |
| Step 6 | (Optional) voice service voip Example: Router(config)# voice service voip | (Optional) Enters voice service configuration mode. |
| Step 7 | (Optional) h323 Example: Router(conf-voi-serv)# h323 | (Optional) Enters H.323 voice service configuration mode. |
| Step 8 | (Optional) h450 h450-2 timeout {T1 \| T2 \| T3 \| T4} milliseconds Example: Router(conf-serv-h323)# h450 h450-2 timeout T1
750 | (Optional) Sets timeouts for supplementary service timers, in milliseconds. This command is used primarily when the default settings
                                          for these timers do not match your network delay parameters. See the ITU-T H.450.2 specification for more information on these
                                          timers. T1 : Timeout value to wait to identify response. Default is 2000. T2 : Timeout value to wait for a call setup. Default is 5000. T3 : Timeout value to wait to initiate response. Default is 5000. T4 : Timeout value to wait for setup of response. Default is 5000. milliseconds : Number of milliseconds. Range is 500–60000. |
| Step 9 | (Optional) end Example: Router(conf-serv-h323)# end | (Optional) Returns to privileged EXEC mode. |

| Note | We do not recommend the blind keyword. Use either the full-blind or full-consult keyword instead. |
|---|---|

| Note | For Cisco Unified SRST 3.1 and later versions and Cisco Unified SRST 4.0 and later versions, Call Transfer using H.450.2 is
                                          supported automatically with the default session application. |
|---|---|

| Note | You can continue to use the app-h450-transfer.2.0.0.1.tcl script if you install Cisco IOS Release 12.2(11)YT1 or later, but
                                          you cannot use the app-h450-transfer.2.0.0.2.tcl script with a release of Cisco IOS Software that is earlier than Cisco IOS
                                          Release 12.2(11)YT1. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call application voice application-name location Example: Router(config)# call application voice
transfer_app flash:app-h450-transfer.tcl | Loads the Tcl script and specifies its application name. application-name : User-defined name for the IVR application. This name does not have to match the script filename. location : Script directory and filename in URL format. For example, flash memory (flash:filename), a TFTP (tftp://../filename), or
                                                an HTTP server (http://../filename) are valid locations. |
| Step 2 | (Optional) call application voice application-name language number language Example: Router(config)# call application voice
transfer_app language 1 en | (Optional) Sets the language for dynamic prompts by the application. application-name : IVR application name that was assigned in Step 1. number : Specify the number of languages for the audio files for the IVR application. language : Two-character code that specifies the language of the prompts. Valid entries are en (English:default), sp (Spanish), ch
                                                (Chinese), or aa (all). |
| Step 3 | call application voice application-name set-location language category location Example: Router(config)# call application voice
transfer_app set-location en 0 flash:/prompts | Defines the location and category of the audio files that are used by the application for dynamic prompts. application-name : Name of the Tcl IVR application. language : Two-character code to specify the language of the prompts. Valid entries are en (English: default), sp (Spanish), ch (Chinese),
                                                or aa (all). category : Category group (0–4) for the audio files from this location. The value 0 means all categories. . location : URL of the directory that contains the language audio files in the application, without filenames. Flash memory (flash)
                                                or a directory on a server (TFTP, HTTP, or RTSP) are all valid. Prompts are required for Call Transfer from analog FXS phones. No prompts are needed for Call Transfer from IP phones. |
| Step 4 | (Optional) call application voice application-name delay-time seconds Example: Router(config)# call application voice
transfer_app delay-time 1 | (Optional) Sets the delay time for consultation call setup for an analog phone that is making a Call Transfer using the H.450 application.
                                          This command passes a value to the Tcl script by using an attribute-value (AV) pair. seconds : Number of seconds to delay call setup. Range is 1–10. Default is 2. Delay of more than 2 seconds is noticeable to users. For more information about attribute-value pairs and the Tcl script for H.450 Call Transfer and forwarding, see the ReadMe
                                          file that accompanies the script. |
| Step 5 | dial-peer voice number pots Example: Router(config)# dial-peer voice 25 pots | Enters dial-peer configuration mode to configure a POTS dial peer. |
| Step 6 | application application-name Example: Router(config-dial-peer)# application
transfer_app | Loads the application named in Step 1 onto the dial peer. |
| Step 7 | exit Example: Router(config-dial-peer)# exit | Exits dial-peer configuration mode. Timesaver : Before exiting dial-peer configuration mode, configure any other dial-peer parameters that you must set for this dial peer. |
| Step 8 | dial-peer voice number voip Example: Router(config)# dial-peer voice 29 voip | Enters dial-peer configuration mode to configure a VoIP dial peer. |
| Step 9 | application application-name Example: Router(config-dial-peer)# application
transfer_app | Loads the application named in Step 1 onto the dial peer. |
| Step 10 | exit Example: Router(config-dial-peer)# exit | Exits dial-peer configuration mode. Timesaver : Before exiting dial-peer configuration mode, configure any other dial-peer parameters that you must set for this dial peer. |

| Note | Configure trunk access codes only if your normal network dial-plan configuration prevents you from configuring a permanent
                                          POTS voice dial peer to provide trunk access for use during fallback. If you already have local PSTN ports configured with
                                          the appropriate access codes provided by dial peers (for example, dial 9 to select an FXO PSTN line), this configuration is
                                          not needed. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | access-code { { fxo \| e&m } dial-string  \| { bri \| pri } dial-string [ direct-inward-dial ]  } Example: Router(config-cm-fallback)# access-code e&m 8 | Configures trunk access codes for each type of line so that the Cisco Unified IP Phones can access the trunk lines only in
                                          Cisco Unified Communications Manager fallback mode when the Cisco Unified SRST is enabled. fxo : Enables a Foreign Exchange Office (FXO) interface. e&m : Enables an analog Ear and Mouth (E&M) interface. dial-string : String of characters that sets up dial access codes for each specified line type by creating dial peers. The dial-string
                                                argument is used to set up temporary dial peers for each specified line type. bri : Enables a BRI interface. pri : Enables a PRI interface. direct-inward-dial : Enables Direct Inward Dialing (DID) on the POTS dial peer. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | (Optional) timeouts interdigit seconds Example: Router(config-cm-fallback)# timeouts interdigit
5 | (Optional) Configures the interdigit timeout value for all Cisco IP phones that are attached to the router. seconds : Interdigit timeout duration, in seconds, for all Cisco Unified IP Phones. Valid entries are integers from 2 to 120. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| COR List on Incoming Dial Peer | COR List on Outgoing Dial Peer | Result |
|---|---|---|
| No COR | No COR | The call succeeds. |
| No COR | COR list applied for outgoing calls | The call succeeds. By default, the incoming dial peer has the highest COR priority when no COR is applied. If you apply no
                                          COR for an incoming call leg to a dial peer, the dial peer can call of any other dial peer regardless of the COR configuration
                                          on the outgoing dial peer. |
| COR list applied for incoming calls | No COR | The call succeeds. By default, the outgoing dial peer has the lowest priority. Because there are some COR configurations for
                                          incoming calls on the incoming or originating dial peer, it is a superset of the outgoing call’s COR configuration for the
                                          outgoing or stopping dial peer. |
| COR list applied for incoming calls (superset of a COR list applied for outgoing calls on the outgoing dial peer) | COR list applied for outgoing calls (subsets of a COR list applied for incoming calls on the incoming dial peer) | The call succeeds. The COR list for incoming calls on the incoming dial peer is a superset of the COR list for outgoing calls
                                          on the outgoing dial peer. |
| COR list applied for incoming calls (subset of a COR list applied for outgoing calls on the outgoing dial peer) | COR list applied for outgoing calls (supersets of a COR list applied for incoming calls on the incoming dial peer) | The call does not succeed. The COR list for incoming calls on the incoming dial peer is not a superset of the COR list for
                                          outgoing calls on the outgoing dial peer. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | cor {incoming \| outgoing} cor-list-name [ cor-list-number starting-number - ending-number  \| default ] Example: Router(config-cm-fallback)# cor outgoing
LockforPhoneC 1 5010 – 5020 | Configures a COR on dial peers that are associated with directory numbers. incoming : COR list to be used by incoming dial peers. outgoing : COR list to be used by outgoing dial peers. cor-list-name : COR list name. cor-list-number : COR list identifier. You can create maximum 20 COR lists, comprising of incoming or outgoing dial peers. The first six
                                                COR lists are applied to range of directory numbers. Assign the COR configuration to the default COR list if the directory
                                                numbers do not have a COR configuration. starting-number- ending-number: : Directory number range; for example, 2000–2025. default : Instructs the router to use an existing default COR list. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | after-hours block pattern tag pattern [ 7-24 ] Example: Router(config-cm-fallback)# after-hours block
pattern 1 91900 | For blocking, defines a pattern of outgoing digits. Define up to 32 patterns, using individual commands. If you specify the 7–24 keyword, always blocks the pattern, 7 days a week, 24 hours a day. If you do not specify the 7–24 keyword, blocks the pattern during the days and dates as defined in the after-hours day and
                                                after-hours date commands. |
| Step 3 | after-hours day day start-time stop-time Example: Router(config-cm-fallback)# after-hours day mon
19:00 7:00 | Defines a recurring time period for the day of the week during which calls are blocked to outgoing dial patterns that are
                                          defined using the after-hours block pattern command. day : Day of the week abbreviation. The following are valid day abbreviations: sun, mon, tue, wed, thu, fri, sat. start-time stop-time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. If the stop time is smaller value
                                                than the start time, the stop time occurs on the day following the start time. For example, “mon 19:00 07:00” means “from
                                                Monday at 7 p.m. until Tuesday at 7 a.m.”. |
| Step 4 | after-hours date month date start-time stop-time Example: Router(config-cm-fallback)# after-hours date
jan 1 0:00 0:00 | Defines a recurring time period for the month and date for blocking calls to outgoing dial patterns defined in the after-hours
                                          block pattern command. month : Month abbreviation. The following are valid month abbreviations: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov,
                                                dec. date : Date of the month. Range is 1–31. start-time stop time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. The stop time must be larger than
                                                the start time. Value 24:00 is not valid. If you enter 00:00 as stop time, it changes to 23:59. If you enter 00:00 for both
                                                start time and stop time, blocks call for the entire 24-hour period on the specified date. |
| Step 5 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global tag Example: Router(config)# voice register global 12 | Enters voice register global configuration mode to set global parameters for all supported Cisco SIP IP phones in a Cisco
                                          Unified SIP SRST environment. |
| Step 4 | max-pool max-voice-register-pools Example: Router(config-register-global)# max-pool 10 | Set the maximum number of supported SIP voice register Pools in a Cisco Unified SIP SRST environment. The max-voice-register-pools argument represents the maximum number of SIP voice register Pools supported by the Cisco Unified
                                          SIP SRST router. The upper limit of voice register Pools is version- and platform-dependent; see Cisco IOS command-line interface
                                          (CLI) help. Default is 0. |
| Step 5 | application application-name Example: Router(config-register-global)# application
global_app | Selects the session-level application for all dial peers associated with SIP phones. Use the application-name argument to
                                          define specific interactive voice response (IVR) application. |
| Step 6 | external-ring {bellcore-dr1 \| bellcore-dr2 \|bellcore-dr3 \| bellcore-dr4 \| bellcore-dr5} Example: Router(config-register-global)# external-ring
bellcore-dr1 | Specifies the type of ring sound on Cisco SIP or Cisco SCCP IP phones for external calls. Each bellcore-dr 1–5 keyword supports
                                          standard distinctive ringing patterns as defined in the standard GR-506-CORE, LSSGR: Signaling for Analog Interfaces. |
| Step 7 | exit Example: Router(config-register-global)# exit | Exits voice register global configuration mode. |
| Step 8 | voice register pool tag Example: Router(config)# voice register pool 20 | Enters voice register Pool configuration mode for SIP phones. Use this command to control which phone registrations are accepted or rejected by a Cisco Unified SIP SRST device. |
| Step 9 | no vad Example: Router(config-register-pool)# no vad | Disables voice activity detection (VAD) on the VoIP dial peer. VAD is enabled by default. Because there is no comfort noise during periods of silence, the call may disconnect. You may prefer
                                          to set no VAD on the SIP phone pool. |
| Step 10 | codec codec-type [bytes] Example: Router(config-register-pool)# codec g729r8 | Specifies the supported codec by a single SIP phone or a VoIP dial peer in a Cisco Unified SIP SRST environment. The codec-type
                                          argument specifies the preferred codec and can be one of the following: g711alaw : G.711 a–law 64,000 bps. g711ulaw : G.711 mu–law 64,000 bps. g729r8 : G.729 8000 bps (default). The bytes argument is optional and specifies the number of bytes in the voice payload of each frame. |
| Step 11 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

| Note | SIP-to-H.323 call forwarding is not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool tag voip Example: Router(config)# voice register pool 15 | Enters voice register Pool configuration mode. Use this command to control the acceptance or rejections of the phone registrations on a Cisco Unified SIP SRST device. |
| Step 4 | encall-forward b2bua alld directory-number Example: Router(config-register-pool)# call-forward
b2bua all 5005 | Enables call forwarding for a SIP back-to-back user agent (B2BUA) to forward all incoming calls to another non-SIP station
                                          extension. Namely to SIP trunk, H.323 trunk, SCCP device, and analog or digital trunk. directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                          is 32. |
| Step 5 | call-forward b2bua busy directory-number Example: Router(config-register-pool)# call-forward
b2bua busy 5006 | Enables call forwarding for a SIP B2BUA to forward incoming calls to a busy extension to another extension. directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                          is 32. |
| Step 6 | call-forward b2bua mailbox directory-number Example: Router(config-register-pool)# call-forward
b2bua mailbox 5007 | Controls the specific voicemail box in a voicemail system at the end of a call forwarding Exchange. directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                          is 32. |
| Step 7 | call-forward b2bua noan directory-number timeout seconds Example: Router(config-register-pool)# call-forward
b2bua noan 5010 timeout 10 | Enables call forwarding for a SIP B2BUA to forward incoming calls to an extension that does not answer after a configured
                                          amount of time to another extension. Use this command if a phone is registered with a Cisco Unified SIP SRST router, but the phone is not reachable because there
                                          is no IP connectivity (there is no response to Invite requests). directory-number : phone number to which calls are forwarded. Represents a fully qualified E.164 number. Maximum length of the phone number
                                                is 32. timeout seconds : Duration, in seconds, that a call can ring with no answer before the call is forwarded to another extension. Range is 3–60000.
                                                The default value is 20. |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

| Note | The Cisco Unified SIP SRST does not support the Pin-based exemptions and the “Login” toll-bar override. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 4 | after-hours block pattern tag pattern [ 7-24 ] Example: Router(config-cm-fallback)# after-hours block
pattern 1 91900 | For blocking, defines a pattern of outgoing digits. Define up to 32 patterns, using individual commands. If you specify the 7–24 keyword, always blocks the pattern, 7 days a week, 24 hours a day. If you do not specify the 7–24 keyword, blocks the pattern during the days and dates as defined in the after-hours day and after-hours date commands. |
| Step 5 | after-hours day day start-time stop-time Example: Router(config-cm-fallback)# after-hours day mon
19:00 7:00 | Defines a recurring time period for the day of the week during which calls are blocked to outgoing dial patterns that are
                                          defined using the after-hours block pattern command. day : Day of the week abbreviation. The following are valid day abbreviations: sun, mon, tue, wed, thu, fri, sat. start-time stop-time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. If the stop time is smaller value
                                                than the start time, the stop time occurs on the day following the start time. For example, “mon 19:00 07:00” means “from
                                                Monday at 7 p.m. until Tuesday at 7 a.m.”. Value 24:00 is not valid. If you enter 00:00 as stop time, it changes to 23:59. If you enter 00:00 for both start time and
                                                stop time, blocks call for the entire 24-hour period on the specified date. |
| Step 6 | after-hours date month date start-time stop-time Example: Router(config-cm-fallback)# after-hours date
jan 1 0:00 0:00 | Defines a recurring time period for the month and date for blocking calls to outgoing dial patterns defined in the after-hours
                                          block pattern command. month : Month abbreviation. The following are valid month abbreviations: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov,
                                                dec. date : Date of the month. Range is 1–31. start-time stop time : Beginning and ending times for call blocking, in an HH:MM format using a 24-hour clock. The stop time must be larger than
                                                the start time. Value 24:00 is not valid. If you enter 00:00 as stop time, it changes to 23:59. If you enter 00:00 for both start time and
                                                stop time, blocks call for the entire 24-hour period on the specified date. |
| Step 7 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |
| Step 8 | voice register pool tag Example: Router(config)# voice register pool 12 | Enters voice register Pool configuration mode. Use this command to control the accepted or rejected registrations by a Cisco Unified SIP SRST device. |
| Step 9 | after-hour exempt Example: Router(config-register-pool)# after-hour exempt | Specifies that for a particular voice register Pool, does not block the outgoing calls although call blocking is enabled. |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

| Note | To enable translation-rule, see Enabling Digit Translation Rules section. |
|---|---|

| Note | For Cisco Unified SRST 3.2 and later versions and Cisco Unified SRST 4.0 and later versions, use the voice translation-rule and translation-profile commands shown below instead of the translation rule configuration described in the Enabling Digit Translation Rules section. Voice translation rules are a separate feature from translation rules. See the voice translation-rule command in Cisco IOS Voice Command Reference for more information and the VoIP Gateway Trunk and Carrier Based Routing Enhancements documentation for more general information on translation rules and profiles. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | voice translation-rule number Example: Router(config)# voice translation-rule 1 | Defines a translation rule for voice calls and enters voice translation-rule configuration mode. number : Number that identifies the translation rule. Range is 1–2147483647. |
| Step 2 | rule precedence/match-pattern/ /replace-pattern/ Example: Router(cfg-translation-rule)# rule 1/^9/ // | Defines a translation rule. precedence : Priority of the translation rule. Range is 1–15. match-pattern : Stream editor (SED) expression used to match incoming call information. The slash (/) is a delimiter in the pattern. replace-pattern : SED expression used to replace the match pattern in the call information. The slash (/) is a delimiter in the pattern. |
| Step 3 | exit Example: Router(cfg-translation-rule)# exit | Exits voice translation-rule configuration mode. |
| Step 4 | voice translation-profile name Example: Router(config)# voice translation-profile name1 | Defines a translation profile for voice calls. name : Name of the translation profile. Maximum length of the voice translation profile name is 31 alphanumeric characters. |
| Step 5 | translate {called \| calling \| redirect-called} translation-rule-number Example: Router(cfg-translation-profile)# translate
called 1 | Associates a voice translation rule with a voice translation profile. called : Associates the translation rule with called numbers. calling : Associates the translation rule with calling numbers. redirect-called : Associates the translation rule with redirected called numbers. translation-rule-number : The reference number of the translation rule 1–2147483647. |
| Step 6 | exit Example: Router(cfg-translation-profile)# exit | Exits translation-profile configuration mode. |
| Step 7 | voice register pool pool-tag Example: Router(config)# voice register pool 10 | Enters voice register pool configuration mode for SIP phones. pool-tag : Indicates an unique number assigned to the pool. Range is 1 to 100. |
| Step 8 | translation-profile {incoming \| outgoing} name Example: Router(config-register-pool)# translation-profile
outgoing name1 | Assigns a translation profile for incoming or outgoing call legs on a Cisco IP phone. incoming : Applies the translation profile to incoming calls. outgoing : Applies the translation profile to outgoing calls. name : The name of the translation profile. |
| Step 9 | exit Example: Router(config-register-pool)# exit | Exits from voice register pool configuration mode. |

| Note | For verification of translation profile configuration, see Verifying Translation Profiles. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | max-conferences max-conference-numbers Example: Router(config-cm-fallback)# max-conferences 16 | Sets the maximum number of supported simultaneous three-party conferences by the router. The maximum number possible is platform-dependent: Cisco 1751 router: 8 Cisco 1760 router: 8 Cisco 2600 series routers: 8 Cisco 2600-XM series routers: 8 Cisco 2801 router: 8 Cisco 2811, Cisco 2821, and Cisco 2851 routers: 16 Cisco 3640 and Cisco 3640A routers: 8 Cisco 3660 router: 16 Cisco 3725 router: 16 Cisco 3745 router: 16 Cisco 3800 Series router: 24 |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | xmlschema schema-url Example: Router(config-cm-fallback)# xmlschema
http://server2.example.com/
schema/schema1.xsd | Specifies the URL for an XML API schema to be used with this Cisco Unified SRST system. schema-url : Local or remote URL as defined in RFC 2396. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |