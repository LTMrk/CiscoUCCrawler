---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-49821639dd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_voicemail.html
retrieved_at: 2026-08-21T02:49:31.316395+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Integrating Voice Mail with Cisco Unified SRST

## Chapter: Integrating Voice Mail with Cisco Unified SRST

# Integrating Voice Mail with Cisco Unified SRST

This chapter describes how to make your existing voicemail system run on phones connected to a Cisco Unified SRST router during
                        Cisco Unified Communications Manager fallback.

Cisco Unified SRST also supports incoming and outgoing Session Initiation Protocol (SIP) calls to and from Cisco Unified IP
                        phones and router voice gateway voice ports. SIP may be used in situations where the Cisco Unified SRST Router is separate
                        from the PSTN gateway and the SRST and PSTN gateways are linked together using SIP (instead of H.323).

For more information about SIP, see Cisco IOS SIP Configuration Guide .

## Information About Integrating Voicemail with Cisco Unified SRST

Cisco Unified SRST can send and receive voicemail messages from Cisco Unity and other voicemail systems during Cisco Unified
                           CM fallback. When the WAN is down, a voicemail system with BRI or PRI access to the Cisco Unified SRST system uses ISDN signaling
                           (see figure 5 - Cisco Unified Communications Manager Fallback with BRI or PRI). Systems with Foreign Exchange Office (FXO)
                           or Foreign Exchange Station (FXS) access connect to a PSTN and use in-band dual tone multifrequency (DTMF) signaling (see
                           figure 6 - Cisco Unified Communications Manager Fallback with PSTN).

From Unified SRST Release 12.0 onwards, Unified SRST supports voicemail on IPv6 protocols for SIP IP phones.

Both configurations allow phone message buttons to remain active and calls to busy or unanswered numbers to be forwarded to
                           the dialed numbers’ mailboxes.

Calls that reach a busy signal, calls that are unanswered, and calls made by pressing the message button are forwarded to
                           the voicemail system. To make this happen, you must configure access from the dial peers to the voicemail system and establish
                           routing to the voicemail system for busy and unanswered calls and for message buttons.

If the voicemail system is accessed over FXO or FXS, you must configure instructions (DTMF patterns) for the voicemail system
                           so that it can access the correct voicemail system mailbox. If your voicemail system is accessed over BRI or PRI, no instructions
                           are necessary because the voicemail system can log in to the calling phone’s mailbox directly.

## How to Integrate Voicemail with Cisco Unified SCCP and SIP SRST

This section contains the following tasks:

Support for SIP SRST is added from IOS release 15.1(4)M3 and 15.2(1)T2.

### Configuring Direct Access to Voicemail

You can configure direct access to voicemail system using BRI/PRI or FXO/FXS. To access voicemail messages with BRI/PRI or
                                 FXO/FXS access, you must have POTS dial peers configured with a destination pattern that matches the voicemail system’s number.
                                 Also, you must associate the dial peer with the port to which the voicemail system is accessed.

Both sets of configurations are done in dial-peer configuration mode. The summary and detailed steps below include only the
                                 basic commands necessary to perform this task. You may require additional commands for your particular dial-peer configuration.

Entry

Description

Digits 0 to 9

—

Letters A through D

—

Asterisk (*) and pound sign (#)

These appear on standard touch-tone dial pads.

Comma (,)

Inserts a pause between digits.

Period (.)

Indicates that the preceding digit occurred zero or more times; similar to the wildcard usage.

Percent sign (%)

Indicates that the preceding digit occurred zero or more times; similar to the wildcard usage.

Plus sign (+)

Indicates that the preceding digit occurred one or more times.

The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                         indicate that the string is an E.164 standard number.

Circumflex (^)

Indicates a match to the beginning of the string.

Parentheses ( ( ) ), which indicate a pattern and are the same as the regular expression rule.

Dollar sign ($)

Matches the null string at the end of the input string.

Backslash symbol (\)

Is followed by a single character and matches that character. Can be used with a single character with no other significance
                                             (matching that character).

Question mark (?)

Indicates that the preceding digit occurred zero or one time.

Brackets ( [ ] )

Indicates a range. A range is a sequence of characters enclosed in the brackets; only numeric characters from 0 to 9 are allowed
                                             in the range.

### SUMMARY STEPS

- dial-peer voice tag { pots | voatm | vofr | voip }

- destination-pattern [ + ] string [ T ]

- port { slot-number / subunit-number / port | slot / port : ds0-group-no }

- forward-digits { num-digit | all | extra }

- Do the following to configure a video codec:

- video codec codec

- exit

### DETAILED STEPS

Step 1

dial-peer voice tag { pots | voatm | vofr | voip }

#### Example:

```
Router(config)# dial-peer voice 1002 pots
```

(FXO or FXS and BRI or PRI) Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial-peer
                                             configuration mode. The dial-peer command provides different syntax for individual routers. This example is syntax for Cisco 3600 series routers.

tag : Digits that define a particular dial peer. Range is from 1 to 2147483647.

pots : Indicates that this is a POTS dial peer that uses VoIP encapsulation on the IP backbone.

voatm : Specifies that this is a VoATM dial peer that uses real-time AAL5 voice encapsulation on the ATM backbone network.

vofr : Specifies that this is a VoFR dial peer that uses FRF.11 encapsulation on the Frame Relay backbone network.

voip : Indicates that this is a VoIP dial peer that uses voice encapsulation on the POTS network.

Step 2

destination-pattern [ + ] string [ T ]

#### Example:

```
Router(config-dial-peer)# destination-pattern 1100T
```

(FXO or FXS and BRI or PRI) Specifies either the prefix or the full E.164 telephone number (depending on your dial plan) to
                                             be used for a dial peer.

+ : (Optional) Character that indicates an E.164 standard number.

string : See Table Valid Entries for the String Argument in the destination-pattern command .

T : (Optional) Control character that indicates that the destination-pattern value is a variable-length dial string.

Step 3

port { slot-number / subunit-number / port | slot / port : ds0-group-no }

#### Example:

```
Router(config-dial-peer)# port 1/1/1
```

(FXO or FXS and BRI or PRI) Associates a dial peer with a specific voice port on Cisco routers.

slot-number : Number of the slot in the router in which the voice interface card (VIC) is installed. Valid entries are from 0 to 3, depending
                                                   on the slot in which it is installed.

subunit-number : Subunit on the VIC in which the voice port is located. Valid entries are 0 or 1.

port : Voice port number. Valid entries are 0 and 1.

ds0-group-no : Specifies the DS0 group number. Each defined DS0 group number is represented on a separate voice port. This allows you to
                                                   define individual DS0s on the digital T1/E1 card.

Step 4

forward-digits { num-digit | all | extra }

#### Example:

```
Router(config-dial-peer)# forward-digits all
```

(Optional for FXO or FXS) Specifies which digits to forward for voice calls.

num-digit : The number of digits to be forwarded. If the number of digits is greater than the length of a destination phone number,
                                                   the length of the destination number is used. Range is 0 to 32. Setting the value to 0 is equivalent to entering the no forward-digits command.

all : Forwards all digits. If all is entered, the full length of the destination pattern is used.

extra : If the length of the dialed digit string is greater than the length of the dial-peer destination pattern, the extra right-justified
                                                   digits are forwarded. However, if the dial-peer destination pattern is variable length and ends with the character “T” (for
                                                   example: T, 123T, 123...T), extra digits are not forwarded.

Step 5

Do the following to configure a video codec:

- video codec codec

#### Example:

```
Device(config-dial-peer)# video codec h261
```

Configures a video codec at the dial peer level.

Step 6

exit

#### Example:

```
Router(config-dial-peer)# exit
```

(FXO or FXS and BRI or PRI) Exits dial-peer configuration mode.

#### Examples

```
voice-port 1/1/1
timing digit 250
timing inter-digit 250 dial-peer voice 1102 pots
destination-pattern 1101
port 1/1/1
forward-digits all
dial-peer voice 1103 pots
destination-pattern 1101
port 1/1/1
forward-digits all
dial-peer voice 1104 pots
destination-pattern 1101
port 1/1/1
forward-digits all
```

The following example sets up a POTS dial peer named 1102 to go directly to 1101 through port 2/0:23:

```
controller T1 2/0
framing esf
clock source line primary
linecode b8zs
cablelength short 133
pri-group timeslots 21-24
interface Serial2/0:23
no ip address
no logging event link-status
isdn switch-type primary-net5
isdn incoming-voice voice
isdn T309-enable
no cdp enable
voice-port 2/0:23 dial-peer voice 1102 pots
destination-pattern 1101T
port 2/0:23
```

### Configuring Message Buttons

To activate the message buttons on Cisco Unified IP phones connected to the Cisco Unified SCCP and SIP SRST router during
                                 Cisco Unified Communications Manager fallback, you must program a speed-dial number to the voicemail system. The speed-dial
                                 number is dialed when message buttons on phones connected to the Cisco Unified SCCP and SIP SRST router are pressed during
                                 Cisco Unified CM fallback. In addition, call forwarding must be configured so that calls to busy and unanswered numbers are
                                 sent to the voicemail number.

This configuration is required for FXO or FXS and BRI or PRI.

### SUMMARY STEPS

- call-manager-fallback

- voicemail phone-number

- call-forward busy directory-number

- call-forward noan directory-number timeout seconds

- exit

- voice register pool tag

- call-forward b2bua busy directory-number

- call-forward b2bua noan directory-number timeout seconds

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

voicemail phone-number

#### Example:

```
Router(config-cm-fallback)# voicemail 5550100
```

Configures the telephone number that is dialed when the message button on a Cisco Unified SCCP IP Phone is pressed.

phone-number : Phone number configured as a speed-dial number for retrieving messages.

Step 3

call-forward busy directory-number

#### Example:

```
Router(config-cm-fallback)# call-forward busy
2000
```

Configures call forwarding to another number when the Cisco SCCP IP phone is busy.

directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters
                                             that correspond to the right-justified digits in the directory number extension.

Step 4

call-forward noan directory-number timeout seconds

#### Example:

```
Router(config-cm-fallback)# call-forward noan
2000 timeout 10
```

Configures call forwarding to another number when no answer is received from the Cisco SCCP IP phone.

directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters that
                                             correspond to the right-justified digits in the directory number extension.

timeout seconds : Sets the waiting time, in seconds, before the call is forwarded to another phone. The seconds range is from 3 to 60000.

Step 5

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

Step 6

voice register pool tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters voice register pool configuration mode.

Step 7

call-forward b2bua busy directory-number

#### Example:

```
Router(config-register-pool)# call-forward
b2bua busy 2000
```

Configures call forwarding to another number when the Cisco SIP IP phone is busy.

directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters that
                                             correspond to the right-justified digits in the directory number extension.

Step 8

call-forward b2bua noan directory-number timeout seconds

#### Example:

```
Router(config-register-pool)# call-forward noan
2000 timeout 10
```

Configures call forwarding to another number when no answer is received from the Cisco SIP IP phone.

directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters that
                                             correspond to the right-justified digits in the directory number extension.

timeout seconds : Sets the waiting time, in seconds, before the call is forwarded to another phone. The seconds range is from 3 to 60000.

Step 9

exit

#### Example:

```
Router(config-register-pool)# exit
```

Exits voice register pool configuration mode.

#### Examples

The following example specifies 1101 as the speed-dial number that is issued when message buttons are pressed on Cisco Unified
                                    IP Phones connected to the Cisco Unified SRST router. All busy and unanswered calls are configured to be forwarded to the
                                    voicemail number (1101).

```
call-manager-fallback
voicemail 1101
call-forward busy 1101
call-forward noan 1101 timeout 3
voice register pool 1
call-forward b2bua busy 1101
call-forward b2bua noan 1101 timeout 3
```

### Redirecting to Cisco Unified Communications Manager Gateway

#### Before you begin

The following task is required for voicemail systems with BRI or PRI access.

### SUMMARY STEPS

- From any page in Cisco Unified CM, click Device and Gateway

- From the Find and List Gateways page, click Find .

- From the Find and List Gateways page, choose a device name.

- From the Gateway Configuration page, check Redirecting Number IE Delivery - Outgoing .

### DETAILED STEPS

Step 1

From any page in Cisco Unified CM, click Device and Gateway

Step 2

From the Find and List Gateways page, click Find .

Step 3

From the Find and List Gateways page, choose a device name.

Step 4

From the Gateway Configuration page, check Redirecting Number IE Delivery - Outgoing .

### Configuring Call Forwarding to Voicemail

The following task is required for voicemail systems with FXO or FXS access.

In addition to supporting message buttons for retrieving personal messages, Cisco Unified SRST allows the automatic forwarding
                              of calls to busy or unanswered numbers to voicemail systems. The forwarded calls can be routed to almost any location in the
                              voicemail system. Typically, calls are forwarded to a location in the called number’s mailbox where the caller can leave messages.

#### Call Routing Instructions Using DTMF Digit Patterns

Cisco Unified SRST Cisco Unified SRST call-routing instructions are required so that forwarded calls can be sent to the correct
                                 voicemail boxes. These instructions consist of DTMF digits configured in patterns that match the dial sequences required by
                                 the voicemail system to get to a particular voicemail location. For example, a voicemail system may be designed so that callers
                                 must do the following to leave a message:

Dial the central voicemail number (1101) and press #.

Dial an extension number (6000) and press #.

Dial 2 to select the menu option for leaving messages in the extension number’s mailbox.

For Cisco Unified SRST to forward a call to a busy or unanswered number to extension 6000’s mailbox, it must be programmed
                                 to issue a sequence of 1101#6000#2. As shown in  the below figure, this is accomplished through the voicemail and pattern commands.

The # cgn #2, # cdn #2, and # fdn #2 portions of the pattern commands shown in are DTMF digit patterns. These patterns are composed of tags and tokens. Tags are sets of characters representing DTMF tones.
                                 Tokens consist of three command keywords ( cgn , cdn , and fdn ) that declare the state of an incoming call transferred to voicemail.

A tag can be up to three character from the DTMF tone set (A to D, 0 to 9, # and *). Voicemail systems can use limited sets
                                 of DTMF tones. For example, Cisco Unity uses all DTMF tones but A to D. Tones can be defined in multiple ways. For example,
                                 when the star (*) is placed in front of a token by itself, it can mean “dial the following token number,” or, if it is at
                                 the end of a token, it can mark the end of a token number. If the asterisk is between other tag characters, it can mean dial
                                 *. The use of tags depends on how DTMF tones are defined by your voicemail system.

Tokens tell Cisco Unified SRST what telephone number in the call forwarding chain to use in the pattern. As shown in the following
                                 figure, there are three types of tokens that correspond to three possible call states during voicemail forwarding.

Sets of tags and tokens or patterns activate a voicemail system when one of the following occurs:

A user presses the message button on a phone ( pattern direct command).

An internal extension attempts to connect to a busy extension and the call is forwarded to voicemail ( pattern ext-to-ext busy command).

An internal extension fails to connect to an extension and the call is forwarded to voicemail ( pattern ext-to-ext no-answer command).

An external trunk call reaches a busy extension and the call is forwarded to voicemail ( pattern trunk-to-ext busy command).

An external trunk call reaches an unanswered extension and the call is forwarded to voicemail ( pattern trunk-to-ext no-answer command).

#### Prerequisites

FXO hairpin-forwarded calls to voicemail systems must have disconnect supervision from the central office. For further information,
                                       see the FXO Answer and Disconnect Supervision document.

To configure patterns that your voicemail system will interpret correctly, you must know how the system routes voicemail calls
                                       and interprets DTMF tones (see the Call Routing Instructions Using DTMF Digit Patterns section).

You can find information about how Cisco Unity handles voicemail calls in the How to Transfer a Caller Directly into a Cisco Unity Mailbox document. Additional call-handling information can be found in the “Subscriber and Operator Orientation”
                                       chapters of any Cisco Unity system administration guide .

For other voicemail systems, see the analog voicemail integration configuration guide or information about the system’s call
                                       handling.

#### Configuring Call Forwarding to Voicemail

### SUMMARY STEPS

- vm-integration

- pattern direct tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern ext-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern ext-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern trunk-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern trunk-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

### DETAILED STEPS

Step 1

vm-integration

##### Example:

```
Router(config)# vm-integration
```

Enters voicemail integration mode and enables voicemail integration with DTMF and analog voicemail systems.

Step 2

pattern direct tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-int)# pattern direct 2 CGN *
```

Configures the DTMF digit pattern forwarding necessary to activate the voicemail system when the user presses the messages
                                                button on the phone.

tag1 : Alphanumeric string fewer than four DTMF digits in length. The alphanumeric string consists of a combination of four letters
                                                      (A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the numbers defined in the voicemail
                                                      system’s integration file, immediately preceding either the number of the calling party, the number of the called party, or
                                                      a forwarding number.

tag2 and tag3 : (Optional) See tag1 .

last-tag: See tag1 . This tag indicates the end of the pattern.

CGN : Calling number (CGN) information is sent to the voicemail system.

CDN : Called number (CDN) information is sent to the voicemail system.

FDN : Forwarding number (FDN) information is sent to the voicemail system.

Step 3

pattern ext-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-int)# pattern ext-to-ext busy 7 FDN * CGN *
```

Configures the DTMF digit pattern forwarding necessary to activate the voicemail system once an internal extension attempts
                                                to connect to a busy extension and the call is forwarded to voicemail.

Step 4

pattern ext-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-int)# pattern ext-to-ext no-answer 5 FDN * CGN *
```

Configures the DTMF digit pattern forwarding necessary to activate the voicemail system once an internal extension fails to
                                                connect to an extension and the call is forwarded to voicemail.  For argument and keyword information, see Step 1.

Step 5

pattern trunk-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-int)# pattern trunk-to-ext busy 6 FDN * CGN *
```

Configures the DTMF digit pattern forwarding necessary to activate the voicemail system once an external trunk call reaches
                                                a busy extension and the call is forwarded to voicemail.

Step 6

pattern trunk-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-int)# pattern trunk-to-ext no-answer 4 FDN * CGN *
```

Configures the DTMF digit pattern forwarding necessary to activate the voicemail system when an external trunk call reaches
                                                an unanswered extension and the call is forwarded to voicemail.

#### Examples

For the following configuration, if the voicemail number is 1101, and 3001 is a phone with a message button, 1101*3001 would
                                    be dialed automatically when the 3001 message button is pressed. Under these circumstances, 3001 is considered to be a calling
                                    number or inbound call number.

```
vm-integration
pattern direct * CGN
```

For the following configuration, if 3001 calls 3006 and 3006 does not answer, the Unified SRST router will forward 3001 to
                                    the voicemail system (1101) and send to the voicemail system the DTMF pattern # 3006 #2. This pattern is intended to select
                                    voicemail box number 3006 (3006’s voice mailbox). For this pattern to be sent, 3001 must be a forwarding number.

```
vm-integration
pattern ext-to-ext no-answer # FDN #2
```

For the following configuration, if 3006 is busy and 3001 calls 3006, the Unified SRST router will forward 3001 to the voicemail
                                    system (1101) and send to the voicemail system the DTMF pattern # 3006 #2. This pattern is intended to select voice mailbox
                                    number 3006 (3006’s voice mailbox). For this pattern to be sent, 3001 must be a forwarding number.

```
vm-integration
pattern ext-to-ext busy # FDN #2
```

### Configuring Message Waiting Indication (Cisco Unified SRST Routers)

The Message Waiting Indication (MWI) relay mechanism is initiated after someone leaves a voicemail message on the remote voicemail
                                 message system. MWI relay is required when one Cisco Unity Voicemail system is shared by multiple Cisco Unified SRST routers.
                                 Unified SRST routers use the SIP Subscribe and Notify methods for MWI. See Configuring Cisco IOS SIP Configuration Guide for more information on SIP MWI and the Subscribe and Notify methods. The Unified SRST router that is the SIP MWI relay server
                                 acts as the SIP notifier. The other remote routers act as the SIP subscribers.

MWI is not supported during a fallback to Unified SRST. The MWI (the phone LED indication) will not correctly reflect when
                                 new messages arrive or when all messages have been listened to. We recommend resynchronizing MWIs after the WAN link is available,
                                 and connection with Unified Communications Manager is reestablished. The MWI behavior is consistent across voicemail support
                                 for IPv4 as well as IPv6 on Unified SRST.

### SUMMARY STEPS

- call-manager-fallback

- configure terminal

- mwi relay

- mwi reg-e164

- exit

- sip-ua

- mwi-server { ipv4: destination - address | dns : host - name } [expires seconds [port port ] [transport ] { tcp | udp }] [unsolicited]]

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

mwi relay

#### Example:

```
Router(config-cm-fallback)# mwi relay
```

Enables the Unified SRST router to relay MWI information to remote Cisco IP phones.

Step 4

mwi reg-e164

#### Example:

```
Router(config-cm-fallback)# mwi reg-e164
```

Registers E.164 numbers rather than extension numbers with a SIP proxy or registrar.

Step 5

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

Step 6

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters SIP user-agent configuration mode.

Step 7

mwi-server { ipv4: destination - address | dns : host - name } [expires seconds [port port ] [transport ] { tcp | udp }] [unsolicited]]

#### Example:

```
Router(config-sip-ua)# mwi-server ipv4:10.0.2.254
```

Configures voicemail server settings on a voice gateway or user agent. The IP address and port for the SIP-based MWI server
                                             should be in the same LAN as the voicemail server. The MWI server is a Cisco Unified SRST router. Keywords and arguments are
                                             as follows:

ipv4: destination-address : IP address of the voicemail server.

dns: host-name : The argument should contain the complete hostname to be associated with the target address; for example, dns:test.cisco.com.

expires seconds : Subscription expiration time, in seconds. Range is from 1 to 999999. Default is 3600.

port port : Port number on the voicemail server. Default is 5060.

transport : Transport protocol to the voicemail server. Valid values are tcp and udp. Default is UDP.

unsolicited : Requires the voicemail server to send a SIP notification message to the voice gateway or UA if the mailbox status changes.
                                                   Removes the requirement that the voice gateway subscribe for MWI service.

Step 8

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP user-agent configuration mode.

### Configuring Message Waiting Indication (SIP Phones in SRST Mode)

On SIP phones operating in the SIP SRST mode, you can use the mwi unsolicited command to configure a message-waiting notification when a message is sent by the Cisco Unity Express (CUE). The SIP phone
                                 then displays the notification when indicated by the voice messaging system. To configure message-waiting notification, perform
                                 the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- mwi-server { ipv4: destination - address | dns : host - name }[ unsolicited ]

- exit

- voice register global

- mwi unsolicited

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

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters Session Initiation Protocol (SIP) user agent (ua) configuration mode for configuring the user agent.

Step 4

mwi-server { ipv4: destination - address | dns : host - name }[ unsolicited ]

#### Example:

```
Router(config-sip-ua)# mwi-server ipv4:10.0.2.254 unsolicited
```

Or

```
Router(config-sip-ua)# mwi-server dns:server.yourcompany.com unsolicited
```

Configures voicemail server settings on a voice gateway or user agent. Keywords and arguments are as follows:

ipv4: destination-address : IP address of the voicemail server.

dns: host-name : The argument should contain the complete hostname to be associated with the target address; for example, dns:test.cisco.com.

unsolicited : Requires the voicemail server to send a SIP notification message to the voice gateway or UA if the mailbox status changes.
                                                   Removes the requirement that the voice gateway subscribe for MWI service.

Step 5

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP user-agent configuration mode.

Step 6

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice register global configuration mode to set parameters for all supported SIP phones in SIP SRST mode.

Step 7

mwi unsolicited

#### Example:

```
Router(config-register-global)# mwi unsolicited
```

Enables all SIP phones to receive MWI notification.

Step 8

end

#### Example:

```
Router(config-register-global)# end
```

Exits to privileged EXEC mode.

## Configuration Examples for Unified SRST

This section provides the following configuration examples:

### Configuring Local Voicemail System (FXO and FXS): Example

The “Dial-Peer Configuration for Integration of Voicemail with Cisco Unified SRST” section of the example below shows a legacy
                              dial-peer configuration for a local voicemail system. The “Cisco Unified SRST Voicemail Integration Pattern Configuration”
                              section must be compatible with your voicemail system configuration.

```
! Dial-Peer Configuration for Integration of voicemail with Cisco Unified SRST
!
dial-peer voice 101 pots
destination-pattern 14011
port 3/0/0
!
dial-peer voice 102 pots
preference 1
destination-pattern 14011
port 3/0/1
!
dial-peer voice 103 pots
preference 2
destination-pattern 14011
port 3/1/0
!
dial-peer voice 104 pots
destination-pattern 14011
port 3/1/1
!
! Cisco Unified SRST configuration
!
call-manager-fallback
max-ephones 24
max-dn 144
ip source-address 1.4.214.104 port 2000
voicemail 14011
call-forward busy 14011
call-forward noan 14011 timeout 3
! Cisco Unified SRST voicemail Integration Pattern Configuration
!
vm-integration
pattern direct 2 CGN *
pattern ext-to-ext no-answer 5 FDN * CGN *
pattern ext-to-ext busy 7 FDN * CGN *
pattern trunk-to-ext no-answer 4 FDN * CGN *
pattern trunk-to-ext busy 6 FDN * CGN *
```

### Configuring Central Location Voicemail System (FXO and FXS): Example

The “Dial-Peer Configuration for Integration of voicemail with Cisco Unified SRST in Central Location” section of the example
                              shows a legacy dial-peer configuration for a central voicemail system. The “Cisco Unified SRST Voicemail Integration Pattern
                              Configuration” section must be compatible with your voicemail system configuration.

Message waiting indicator (MWI) integration is not supported for PSTN access to voicemail systems at central locations.

```
! Dial-Peer Configuration for Integration of voicemail with Cisco Unified SRST in Central
! Location
!
dial-peer voice 101 pots
destination-pattern 14011
port 3/0/0
!
! Cisco Unified SRST configuration
!
call-manager-fallback
max-ephones 24
max-dn 144
ip source-address 1.4.214.104 port 2000
voicemail 14011
call-forward busy 14011
call-forward noan 14011 timeout 3
!
! Cisco Unified SRST Voicemail Integration Pattern Configuration
!
vm-integration
pattern direct 2 CGN *
pattern ext-to-ext no-answer 5 FDN * CGN *
pattern ext-to-ext busy 7 FDN * CGN *
pattern trunk-to-ext no-answer 4 FDN * CGN *
pattern trunk-to-ext busy 6 FDN * CGN *
```

### Configuring Voicemail Access over FXO and FXS: Example

The following example shows how to configure the Cisco Unified SRST router to forward unanswered calls to voicemail. In this
                                 example, the voicemail number is 1101, the voicemail system is connected to FXS voice port 1/1/1, and the voice mailbox numbers
                                 are 3001, 3002, and 3006.

```
voice-port 1/1/1
timing digit 250
timing inter-digit 250
dial-peer voice 1102 pots
destination-pattern 1101T
port 1/1/1
call-manager-fallback
timeouts interdigit 5
ip source-address 1.6.0.199 port 2000
max-ephones 24
max-dn 24
transfer-pattern 3...
voicemail 1101
call-forward busy 1101
call-forward noan 1101 timeout 3
moh minuet.au
vm-integration
pattern direct * CGN
pattern ext-to-ext no-answer # FDN #2
pattern ext-to-ext busy # FDN #2
pattern trunk-to-ext no-answer # FDN #2
pattern trunk-to-ext busy # FDN #2
```

### Configuring Voicemail Access over BRI and PRI: Example

The following example shows how to configure the Cisco Unified SRST router to forward unanswered calls to voicemail. In this
                                 example, the voicemail number is 1101, the voicemail system is connected to a BRI or PRI voice port, and the voice mailbox
                                 numbers are 3001, 3002, and 3006.

```
controller T1 2/0
framing esf
clock source line primary
linecode b8zs
cablelength short 133
pri-group timeslots 21-24
interface Serial2/0:23
no ip address
no logging event link-status
isdn switch-type primary-net5
isdn incoming-voice voice
isdn T309-enable
no cdp enable
voice-port 2/0:23
dial-peer voice 1102 pots
destination-pattern 1101T
direct-inward-dial
port 2/0:23
call-manager-fallback
timeouts interdigit 5
ip source-address 1.6.0.199 port 2000
max-ephones 24
max-dn 24
transfer-pattern 3...
voicemail 1101
call-forward busy 1101
call-forward noan 1101 timeout 3
moh minuet.au
```

### Message Waiting Indication for SIP SRST: Example

The following is an example of a NOTIFY message received at SRST indicating that there is a voicemail for extension 32002:

```
Received:
NOTIFY sip:32002@10.4.49.65:5060;transport=udp SIP/2.0
Via: SIP/2.0/UDP 10.4.49.66:5060;branch=z9hG4bK.D6.7wAl9CN6khf305D1MQ~~194
Max-Forwards: 70
To: <sip:32002@10.4.49.65:5060>
From: <sip:32002@10.4.49.66:5060>;tag=dsd3d29b2f
Call-ID: f0e7ae97-1227@sip:32002@10.4.49.66:5060
CSeq: 1 NOTIFY
Content-Length: 112
Contact: <sip:32002@10.4.49.66:5060>
Content-Type: application/simple-message-summary
Event: message-summary
Messages-Waiting: yes
Message-Account: sip:32002@10.4.49.66
Voice-Message: 1/0 (1/0)
Fax-Message: 0/0 (0/0)
```

## How to Configure DTMF Relay for SIP Applications and Voicemail

For SIP SRST forwarding call to voicemail configuration, see the Configuring Call Handling section.

DTMF relay for SIP applications can be used in two voicemail situations:

### DTMF Relay Using SIP RFC 2833

Cisco Unified Skinny Client Control Protocol (SCCP) Phones, such as those used with Cisco Unified SRST systems, provide only
                                 out-of-band DTMF digit indications. To enable SCCP phones to send digit information to remote SIP-based IVR and voicemail
                                 applications, Cisco Unified SRST 3.2 and later versions provide conversion from the out-of-band SCCP digit indication to the
                                 SIP standard for DTMF relay, which is RFC 2833. You select this method in the SIP VoIP dial peer using the dtmf-relay rtp-nte
                                 command.

The SIP DTMF relay method is needed in the following situations:

When SIP is used to connect a Cisco Unified SRST system to a remote SIP-based IVR or voicemail application, such as Cisco
                                       Unity.

When SIP is used to connect a Cisco Unified SRST system to a remote SIP-PSTN voice gateway that goes through the PSTN to a
                                       voicemail or IVR application.

The need to use out-of-band DTMF relay conversion is limited to SCCP phones. SIP phones natively support in-band DTMF relay
                                             as specified in RFC 2833.

To enable SIP DTMF relay using RFC 2833, the commands in this section must be used on both originating and terminating gateways.

### SUMMARY STEPS

- dial-peer voice tag voip

- dtmf-relay rtp-nte

- dtmf-relay rtp-nte

- exit

- sip-ua

- notify telephone-event max-duration time

- exit

### DETAILED STEPS

Step 1

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters dial-peer configuration mode.

Step 2

dtmf-relay rtp-nte

#### Example:

```
Router(config-dial-peer)# dtmf-relay rtp-nte
```

Enters global configuration mode.

Step 3

dtmf-relay rtp-nte

#### Example:

```
Router(config)# voice register global
```

Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with the Named Telephone Event (NTE) payload type.

Step 4

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits dial-peer configuration mode.

Step 5

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enables SIP user-agent configuration mode.

Step 6

notify telephone-event max-duration time

#### Example:

```
Router(config-sip-ua)# notify telephone-event max-duration 2000
```

Configures the maximum time interval allowed between two consecutive NOTIFY messages for a single DTMF event.

max-duration time : Time interval between consecutive NOTIFY messages for a single DTMF event, in milliseconds. Range is from 500 to 3000.
                                                   Default is 2000.

Step 7

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP user-agent configuration mode.

#### Troubleshooting Tips

The dial-peer section of the show running-config command output displays DTMF relay status when it is configured, as shown in this excerpt:

```
dial-peer voice 123 voip destination-pattern [12]...
monitor probe icmp-ping
session protocol sipv2
session target ipv4:10.8.17.42
dtmf-relay rtp-nte
```

### DTMF Relay Using SIP Notify (Nonstandard)

To use voicemail on a SIP network that connects to a Cisco Unity Express system, use a nonstandard SIP Notify format. To configure
                                 the Notify format, use the sip-notify keyword with the dtmf-relay command. Using the sip-notify keyword may be required for backward compatibility with Cisco Unified SRST Versions 3.0 and 3.1.

### SUMMARY STEPS

- dial-peer voice tag voip

- dtmf-relay sip-notify

- exit

- sip-ua

- notify telephone-event max-duration time

- exit

### DETAILED STEPS

Step 1

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters dial-peer configuration mode.

Step 2

dtmf-relay sip-notify

#### Example:

```
Router(config-dial-peer)# dtmf-relay sip-notify
```

Forwards DTMF tones using SIP NOTIFY messages.

Step 3

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits dial-peer configuration mode.

Step 4

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enables SIP user-agent configuration mode.

Step 5

notify telephone-event max-duration time

#### Example:

```
Router(config-sip-ua)# notify telephone-event max-duration 2000
```

Configures the maximum time interval allowed between two consecutive NOTIFY messages for a single DTMF event.

max-duration time : Time interval between consecutive NOTIFY messages for a single DTMF event, in milliseconds. Range is from 500 to 3000.
                                                   Default is 2000.

Step 6

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP user-agent configuration mode.

#### Troubleshooting Tips

The show sip-ua status command output displays the time interval between consecutive NOTIFY messages for a telephone event. In the following example,
                                 the time interval is 2000 ms:

```
Router# show sip-ua status SIP User Agent Status
SIP User Agent for UDP :ENABLED
SIP User Agent for TCP :ENABLED
SIP User Agent bind status(signaling):DISABLED
SIP User Agent bind status(media):DISABLED
SIP early-media for 180 responses with SDP:ENABLED
SIP max-forwards :6
SIP DNS SRV version:2 (rfc 2782)
NAT Settings for the SIP-UA
Role in SDP:NONE
Check media source packets:DISABLED
Maximum duration for a telephone-event in NOTIFYs:2000 ms
SIP support for ISDN SUSPEND/RESUME:ENABLED
Redirection (3xx) message handling:ENABLED
SDP application configuration:
Version line (v=) required
Owner line (o=) required
Timespec line (t=) required
Media supported:audio image
Network types supported:IN
Address types supported:IP4
Transport types supported:RTP/AVP udptl
```

| Note | Support for SIP SRST is added from IOS release 15.1(4)M3 and 15.2(1)T2. |
|---|---|

| Entry | Description |
|---|---|
| Digits 0 to 9 | — |
| Letters A through D | — |
| Asterisk (*) and pound sign (#) | These appear on standard touch-tone dial pads. |
| Comma (,) | Inserts a pause between digits. |
| Period (.) | Indicates that the preceding digit occurred zero or more times; similar to the wildcard usage. |
| Percent sign (%) | Indicates that the preceding digit occurred zero or more times; similar to the wildcard usage. |
| Plus sign (+) | Indicates that the preceding digit occurred one or more times. Note The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                         indicate that the string is an E.164 standard number. | Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                         indicate that the string is an E.164 standard number. |
| Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                         indicate that the string is an E.164 standard number. |
| Circumflex (^) | Indicates a match to the beginning of the string. Parentheses ( ( ) ), which indicate a pattern and are the same as the regular expression rule. |
| Dollar sign ($) | Matches the null string at the end of the input string. |
| Backslash symbol (\) | Is followed by a single character and matches that character. Can be used with a single character with no other significance
                                             (matching that character). |
| Question mark (?) | Indicates that the preceding digit occurred zero or one time. |
| Brackets ( [ ] ) | Indicates a range. A range is a sequence of characters enclosed in the brackets; only numeric characters from 0 to 9 are allowed
                                             in the range. |

| Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                         indicate that the string is an E.164 standard number. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | dial-peer voice tag { pots \| voatm \| vofr \| voip } Example: Router(config)# dial-peer voice 1002 pots | (FXO or FXS and BRI or PRI) Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial-peer
                                             configuration mode. The dial-peer command provides different syntax for individual routers. This example is syntax for Cisco 3600 series routers. tag : Digits that define a particular dial peer. Range is from 1 to 2147483647. pots : Indicates that this is a POTS dial peer that uses VoIP encapsulation on the IP backbone. voatm : Specifies that this is a VoATM dial peer that uses real-time AAL5 voice encapsulation on the ATM backbone network. vofr : Specifies that this is a VoFR dial peer that uses FRF.11 encapsulation on the Frame Relay backbone network. voip : Indicates that this is a VoIP dial peer that uses voice encapsulation on the POTS network. |
| Step 2 | destination-pattern [ + ] string [ T ] Example: Router(config-dial-peer)# destination-pattern 1100T | (FXO or FXS and BRI or PRI) Specifies either the prefix or the full E.164 telephone number (depending on your dial plan) to
                                             be used for a dial peer. + : (Optional) Character that indicates an E.164 standard number. string : See Table Valid Entries for the String Argument in the destination-pattern command . T : (Optional) Control character that indicates that the destination-pattern value is a variable-length dial string. |
| Step 3 | port { slot-number / subunit-number / port \| slot / port : ds0-group-no } Example: Router(config-dial-peer)# port 1/1/1 | (FXO or FXS and BRI or PRI) Associates a dial peer with a specific voice port on Cisco routers. slot-number : Number of the slot in the router in which the voice interface card (VIC) is installed. Valid entries are from 0 to 3, depending
                                                   on the slot in which it is installed. subunit-number : Subunit on the VIC in which the voice port is located. Valid entries are 0 or 1. port : Voice port number. Valid entries are 0 and 1. ds0-group-no : Specifies the DS0 group number. Each defined DS0 group number is represented on a separate voice port. This allows you to
                                                   define individual DS0s on the digital T1/E1 card. |
| Step 4 | forward-digits { num-digit \| all \| extra } Example: Router(config-dial-peer)# forward-digits all | (Optional for FXO or FXS) Specifies which digits to forward for voice calls. num-digit : The number of digits to be forwarded. If the number of digits is greater than the length of a destination phone number,
                                                   the length of the destination number is used. Range is 0 to 32. Setting the value to 0 is equivalent to entering the no forward-digits command. all : Forwards all digits. If all is entered, the full length of the destination pattern is used. extra : If the length of the dialed digit string is greater than the length of the dial-peer destination pattern, the extra right-justified
                                                   digits are forwarded. However, if the dial-peer destination pattern is variable length and ends with the character “T” (for
                                                   example: T, 123T, 123...T), extra digits are not forwarded. |
| Step 5 | Do the following to configure a video codec: video codec codec Example: For Video Codec Device(config-dial-peer)# video codec h261 | Configures a video codec at the dial peer level. |
| Step 6 | exit Example: Router(config-dial-peer)# exit | (FXO or FXS and BRI or PRI) Exits dial-peer configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | voicemail phone-number Example: Router(config-cm-fallback)# voicemail 5550100 | Configures the telephone number that is dialed when the message button on a Cisco Unified SCCP IP Phone is pressed. phone-number : Phone number configured as a speed-dial number for retrieving messages. |
| Step 3 | call-forward busy directory-number Example: Router(config-cm-fallback)# call-forward busy
2000 | Configures call forwarding to another number when the Cisco SCCP IP phone is busy. directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters
                                             that correspond to the right-justified digits in the directory number extension. |
| Step 4 | call-forward noan directory-number timeout seconds Example: Router(config-cm-fallback)# call-forward noan
2000 timeout 10 | Configures call forwarding to another number when no answer is received from the Cisco SCCP IP phone. directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters that
                                             correspond to the right-justified digits in the directory number extension. timeout seconds : Sets the waiting time, in seconds, before the call is forwarded to another phone. The seconds range is from 3 to 60000. |
| Step 5 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |
| Step 6 | voice register pool tag Example: Router(config)# voice register pool 1 | Enters voice register pool configuration mode. |
| Step 7 | call-forward b2bua busy directory-number Example: Router(config-register-pool)# call-forward
b2bua busy 2000 | Configures call forwarding to another number when the Cisco SIP IP phone is busy. directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters that
                                             correspond to the right-justified digits in the directory number extension. |
| Step 8 | call-forward b2bua noan directory-number timeout seconds Example: Router(config-register-pool)# call-forward noan
2000 timeout 10 | Configures call forwarding to another number when no answer is received from the Cisco SIP IP phone. directory-number : Selected directory number representing a fully qualified E.164 number. This number can contain “.” wildcard characters that
                                             correspond to the right-justified digits in the directory number extension. timeout seconds : Sets the waiting time, in seconds, before the call is forwarded to another phone. The seconds range is from 3 to 60000. |
| Step 9 | exit Example: Router(config-register-pool)# exit | Exits voice register pool configuration mode. |

| Note | The following task is required for voicemail systems with BRI or PRI access. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | From any page in Cisco Unified CM, click Device and Gateway |  |
| Step 2 | From the Find and List Gateways page, click Find . |  |
| Step 3 | From the Find and List Gateways page, choose a device name. |  |
| Step 4 | From the Gateway Configuration page, check Redirecting Number IE Delivery - Outgoing . |  |

| Note | The following task is required for voicemail systems with FXO or FXS access. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | vm-integration Example: Router(config)# vm-integration | Enters voicemail integration mode and enables voicemail integration with DTMF and analog voicemail systems. |
| Step 2 | pattern direct tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-int)# pattern direct 2 CGN * | Configures the DTMF digit pattern forwarding necessary to activate the voicemail system when the user presses the messages
                                                button on the phone. tag1 : Alphanumeric string fewer than four DTMF digits in length. The alphanumeric string consists of a combination of four letters
                                                      (A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the numbers defined in the voicemail
                                                      system’s integration file, immediately preceding either the number of the calling party, the number of the called party, or
                                                      a forwarding number. tag2 and tag3 : (Optional) See tag1 . last-tag: See tag1 . This tag indicates the end of the pattern. CGN : Calling number (CGN) information is sent to the voicemail system. CDN : Called number (CDN) information is sent to the voicemail system. FDN : Forwarding number (FDN) information is sent to the voicemail system. |
| Step 3 | pattern ext-to-ext busy tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-int)# pattern ext-to-ext busy 7 FDN * CGN * | Configures the DTMF digit pattern forwarding necessary to activate the voicemail system once an internal extension attempts
                                                to connect to a busy extension and the call is forwarded to voicemail. |
| Step 4 | pattern ext-to-ext no-answer tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-int)# pattern ext-to-ext no-answer 5 FDN * CGN * | Configures the DTMF digit pattern forwarding necessary to activate the voicemail system once an internal extension fails to
                                                connect to an extension and the call is forwarded to voicemail.  For argument and keyword information, see Step 1. |
| Step 5 | pattern trunk-to-ext busy tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-int)# pattern trunk-to-ext busy 6 FDN * CGN * | Configures the DTMF digit pattern forwarding necessary to activate the voicemail system once an external trunk call reaches
                                                a busy extension and the call is forwarded to voicemail. |
| Step 6 | pattern trunk-to-ext no-answer tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-int)# pattern trunk-to-ext no-answer 4 FDN * CGN * | Configures the DTMF digit pattern forwarding necessary to activate the voicemail system when an external trunk call reaches
                                                an unanswered extension and the call is forwarded to voicemail. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | mwi relay Example: Router(config-cm-fallback)# mwi relay | Enables the Unified SRST router to relay MWI information to remote Cisco IP phones. |
| Step 4 | mwi reg-e164 Example: Router(config-cm-fallback)# mwi reg-e164 | Registers E.164 numbers rather than extension numbers with a SIP proxy or registrar. |
| Step 5 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |
| Step 6 | sip-ua Example: Router(config)# sip-ua | Enters SIP user-agent configuration mode. |
| Step 7 | mwi-server { ipv4: destination - address \| dns : host - name } [expires seconds [port port ] [transport ] { tcp \| udp }] [unsolicited]] Example: Router(config-sip-ua)# mwi-server ipv4:10.0.2.254 | Configures voicemail server settings on a voice gateway or user agent. The IP address and port for the SIP-based MWI server
                                             should be in the same LAN as the voicemail server. The MWI server is a Cisco Unified SRST router. Keywords and arguments are
                                             as follows: ipv4: destination-address : IP address of the voicemail server. dns: host-name : The argument should contain the complete hostname to be associated with the target address; for example, dns:test.cisco.com. expires seconds : Subscription expiration time, in seconds. Range is from 1 to 999999. Default is 3600. port port : Port number on the voicemail server. Default is 5060. transport : Transport protocol to the voicemail server. Valid values are tcp and udp. Default is UDP. unsolicited : Requires the voicemail server to send a SIP notification message to the voice gateway or UA if the mailbox status changes.
                                                   Removes the requirement that the voice gateway subscribe for MWI service. |
| Step 8 | exit Example: Router(config-sip-ua)# exit | Exits SIP user-agent configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters Session Initiation Protocol (SIP) user agent (ua) configuration mode for configuring the user agent. |
| Step 4 | mwi-server { ipv4: destination - address \| dns : host - name }[ unsolicited ] Example: For g711alaw Codec Router(config-sip-ua)# mwi-server ipv4:10.0.2.254 unsolicited Or Router(config-sip-ua)# mwi-server dns:server.yourcompany.com unsolicited | Configures voicemail server settings on a voice gateway or user agent. Keywords and arguments are as follows: ipv4: destination-address : IP address of the voicemail server. dns: host-name : The argument should contain the complete hostname to be associated with the target address; for example, dns:test.cisco.com. unsolicited : Requires the voicemail server to send a SIP notification message to the voice gateway or UA if the mailbox status changes.
                                                   Removes the requirement that the voice gateway subscribe for MWI service. |
| Step 5 | exit Example: Router(config-sip-ua)# exit | Exits SIP user-agent configuration mode. |
| Step 6 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters for all supported SIP phones in SIP SRST mode. |
| Step 7 | mwi unsolicited Example: Router(config-register-global)# mwi unsolicited | Enables all SIP phones to receive MWI notification. |
| Step 8 | end Example: Router(config-register-global)# end | Exits to privileged EXEC mode. |

| Note | Message waiting indicator (MWI) integration is not supported for PSTN access to voicemail systems at central locations. |
|---|---|

| Note | Voicemail number associate with SIP phone message button in SRST is configured by Cisco Unified Communications Manager (CUCM),
                                    and not configurable by SIP SRST. The administrator needs to know the voicemail number set by CUCM to configure proper dial
                                    peer to voicemail system in SIP SRST. |
|---|---|

| Note | The need to use out-of-band DTMF relay conversion is limited to SCCP phones. SIP phones natively support in-band DTMF relay
                                             as specified in RFC 2833. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial-peer configuration mode. |
| Step 2 | dtmf-relay rtp-nte Example: Router(config-dial-peer)# dtmf-relay rtp-nte | Enters global configuration mode. |
| Step 3 | dtmf-relay rtp-nte Example: Router(config)# voice register global | Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with the Named Telephone Event (NTE) payload type. |
| Step 4 | exit Example: Router(config-dial-peer)# exit | Exits dial-peer configuration mode. |
| Step 5 | sip-ua Example: Router(config)# sip-ua | Enables SIP user-agent configuration mode. |
| Step 6 | notify telephone-event max-duration time Example: Router(config-sip-ua)# notify telephone-event max-duration 2000 | Configures the maximum time interval allowed between two consecutive NOTIFY messages for a single DTMF event. max-duration time : Time interval between consecutive NOTIFY messages for a single DTMF event, in milliseconds. Range is from 500 to 3000.
                                                   Default is 2000. |
| Step 7 | exit Example: Router(config-sip-ua)# exit | Exits SIP user-agent configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial-peer configuration mode. |
| Step 2 | dtmf-relay sip-notify Example: Router(config-dial-peer)# dtmf-relay sip-notify | Forwards DTMF tones using SIP NOTIFY messages. |
| Step 3 | exit Example: Router(config-dial-peer)# exit | Exits dial-peer configuration mode. |
| Step 4 | sip-ua Example: Router(config)# sip-ua | Enables SIP user-agent configuration mode. |
| Step 5 | notify telephone-event max-duration time Example: Router(config-sip-ua)# notify telephone-event max-duration 2000 | Configures the maximum time interval allowed between two consecutive NOTIFY messages for a single DTMF event. max-duration time : Time interval between consecutive NOTIFY messages for a single DTMF event, in milliseconds. Range is from 500 to 3000.
                                                   Default is 2000. |
| Step 6 | exit Example: Router(config-sip-ua)# exit | Exits SIP user-agent configuration mode. |