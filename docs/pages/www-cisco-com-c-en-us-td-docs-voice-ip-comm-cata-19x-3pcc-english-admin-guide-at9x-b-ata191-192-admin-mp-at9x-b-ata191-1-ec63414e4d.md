---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-ec63414e4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_01000.html
retrieved_at: 2026-08-22T01:03:58.185478+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Advanced Options for Phone Services

## Chapter: Advanced Options for Phone Services

# Advanced Options for Phone Services

## Optimize Fax Completion Rates

Issues can occur with fax transmissions over IP networks, even with the T.38 standard. Use the following task to help avoid
                              any issues.

Step 1

Ensure that you have enough bandwidth for the uplink and the downlink.

For G.711 fallback, we recommend approximately 100 kbps.

For T.38, allocate at least 50 kbps.

Step 2

Click Voice in the menu bar, and then click Line 1 or Line 2 in the navigation tree.

Step 3

In the Network Settings section, enter the following settings:

Network Jitter Level— very high .

Jitter Buffer Adjustment— no .

Step 4

In the Supplementary Service Subscription section, enter the following settings:

Call Waiting Serv— no .

Three Way Call Serv— no .

Step 5

In the Audio Configuration section, enter the following settings to support T.38 fax:

Preferred Codec— G.711u (USA) or G.711a (rest of the world).

Use pref. codec only— Yes .

Silence Supp Enable— No .

Echo Canc Enable— No .

FAX Passthru Method— ReINVITE .

Step 6

Click Submit to save your settings or click Cancel to abandon the unsaved settings.

Step 7

If you are using a Cisco media gateway for PSTN termination, disable T.38 (fax relay) and enable fax using modem passthrough.

For example:

modem passthrough nse payload-type 110 codec g711ulaw

fax rate disable

fax protocol pass-through g711ulaw

If a T.38 call cannot be set up, then the call automatically reverts to G.711 fallback.

Step 8

If you are using a Cisco media gateway, make sure that the Cisco gateway is correctly configured for T.38 with the dial peer.

For example:

fax protocol T38

fax rate voice

fax-relay ecm disable

fax nsf 000000

no vad

### Troubleshoot Your Fax

If you have problems sending or receiving faxes, complete the following steps:

Step 1

Verify that your fax machine is set to a speed between 7200 and 14400.

Step 2

Send a test fax in a controlled environment between two ATAs.

Step 3

Determine the success rate.

Step 4

Monitor the network and record the statistics for jitter, loss, and delay.

Step 5

If faxes fail consistently, capture a copy of the configuration. You can then send this file to Technical Support.

In your web browser, enter the path for the configuration file:

https://<ATA_Local_IP_Address>/admin/config.xml&xuser=

<admin_user>&xpassword=<admin_password>

On the File menu, choose Save As , and save the file with a filename such as MyConfiguration.xml .

Step 6

To enable logging, go to the Voice > System page, and set the IP address of your syslog or debug server. Set the Debug Level to 3. For more information, see System .

You can also capture data using a sniffer trace.

Step 7

Identify the type of fax machine connected to the ATA.

Step 8

Contact technical support:

If you are an user of VoIP products, contact the reseller or service provider that supplied the equipment.

If you are an authorized Cisco partner, contact Cisco technical support. For contact options, see https://www.cisco.com/go/sbc .

## Dial Plan Configuration

Dial plans determine how dialed digits are interpreted and transmitted. They also determine whether the dialed number is accepted
                           or rejected. You can use a dial plan to facilitate dialing or to block certain types of calls such as long distance or international.

To edit a dial plan, click Voice on the menu bar, and then click Line 1 or Line 2 in the navigation tree. Scroll down to the Dial Plan section, and then enter the digit sequences in the Dial Plan field.

### Digit Sequences

A dial plan contains a series of digit sequences, separated by the pipe character: | .

The entire collection of sequences is enclosed within parentheses. Each digit sequence within the dial plan includes a series
                                 of elements, which are individually matched to the keys that the user presses.

White space is ignored, but may be used for readability.

Digit Sequence

Function

0 1 2 3 4 5 6 7 8 9 0 * #

Enter any of these characters to represent a key that the user must press on the phone keypad.

x

Enter x to represent any character on the phone keypad.

[sequence]

Enter characters within square brackets to create a list of accepted key presses. The user can press any one of the keys in
                                             the list.

Numeric range: For example, you would enter [2-9] to allow the user to press any one digit from 2 through 9.

Numeric range with other characters: For example, you would enter [35-8*] to allow the user to press 3, 5, 6, 7, 8, or *.

. (period)

Enter a period for element repetition. The dial plan accepts zero or more entries of the digit. For example, 01. allows users
                                             to enter 0, 01, 011, 0111, and so on.

<dialed:substituted>

Use this format to indicate that certain dialed digits are replaced by other characters when the sequence is transmitted.
                                             The dialed digits can be zero or more characters.

EXAMPLE 1: <8:1650>xxxxxxx

When the user presses 8 followed by a seven digit number, the system automatically replaces the dialed 8 with 1650. If the
                                             user dials 85550112, the system transmits 16505550112.

EXAMPLE 2: <:1>xxxxxxxxxx

In this example, no digits are replaced. When the user enters a 10-digit string of numbers, the number 1 is added at the beginning
                                             of the sequence. If the user dials 9725550112, the system transmits 19725550112.

, (comma)

Enter a comma between digits to play an “outside line” dial tone after a user-entered sequence.

EXAMPLE: 9, 1xxxxxxxxxx

An “outside line” dial tone is sounded after the user presses 9, and the tone continues until the user presses 1.

! (exclamation point)

Enter an exclamation point to prohibit a dial sequence pattern.

EXAMPLE: 1900xxxxxxx!

The system rejects any 11-digit sequence that begins with 1900.

*xx

Enter an asterisk to allow the user to enter a 2-digit star code.

S0 or L0

Enter S0 to reduce the short inter-digit timer to 0 seconds, or enter L0 to reduce the long inter-digit timer to 0 seconds.

#### Digit Sequence Examples

The following examples show digit sequences that you can enter in a dial plan.

In a complete dial plan entry, sequences are separated by a pipe character (|), and the entire set of sequences is enclosed
                                 within parentheses.

EXAMPLE: ([1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9,
                                 011xxxxxx. | 0 | [49]11 )

Extensions on your system

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx.
                                       | 0 | [49]11 )

[1-8]xx Allows a user dial any three-digit number that starts with the digits 1 through 8. If your system uses four-digit
                                       extensions, you would instead enter the following string: [1-8]xxx.

Local dialing with seven-digit number

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx.
                                       | 0 | [49]111)

9, xxxxxxx After a user presses 9, an external dial tone sounds. The user can then dial any seven-digit number, as in a local
                                       call.

Local dialing with 3-digit area code and a 7-digit local number

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8,<:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx !| 9, 011xxxxxx.
                                       | 0 | [49]11 )

9, <:1>[2-9]xxxxxxxxx This example is useful where a local area code is required. After a user presses 9, an external dial
                                       tone sounds. The user must enter a 10-digit number that begins with a digit 2 through 9. The system automatically inserts
                                       the 1 prefix before transmitting the number to the carrier.

Local dialing with an automatically inserted 3-digit area code

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx.
                                       | 0 | [49]11 )

8, <:1212>xxxxxxx This is example is useful where a local area code is required by the carrier but the majority of calls go
                                       to one area code. After the user presses 8, an external dial tone sounds. The user can enter any seven-digit number. The system
                                       automatically inserts the 1 prefix and the 212 area code before transmitting the number to the carrier.

U.S. long-distance dialing

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx |8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9,011xxxxxx.
                                       | 0 | [49]11 )

9, 1 [2-9] xxxxxxxxx After the user presses 9, an external dial tone sounds. The user can enter any 11-digit number that starts
                                       with 1 and is followed by a digit 2 through 9.

Blocked number

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx |8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! |9, 011xxxxxx.
                                       | 0 | [49]11 )

9, 1 900 xxxxxxx ! This digit sequence is useful if you want to prevent users from dialing numbers that are associated with
                                       high tolls or inappropriate content, such as 1-900 numbers in the United States. After the user press 9, an external dial
                                       tone sounds. If the user enters an 11-digit number that starts with the digits 1900, the call is rejected.

U.S. international dialing

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx.
                                       | 0 | [49]11 )

9, 011xxxxxx. After the user presses 9, an external dial tone sounds. The user can enter any number that starts with 011,
                                       as in an international call from the United States.

Informational numbers

( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx.
                                       | 0 | [49]11 )

0 | [49]11 This example includes two digit sequences, separated by the pipe character. The first sequence allows a user to
                                       dial 0 for an operator. The second sequence allows the user to enter 411 for local information or 911 for emergency services.

### Acceptance and Transmission of the Dialed Digits

When you dial a series of digits, each sequence in the dial plan is tested as a possible match. The matching sequences form
                                 a set of candidate digit sequences. As more digits are entered, the set of candidates diminishes until only one or none are
                                 valid. When a terminating event occurs, the ATA either accepts the dialed sequence and initiates a call, or else rejects the
                                 sequence as invalid. You hear the reorder (fast busy) tone if the dialed sequence is invalid.

The following table explains how terminating events are processed.

Terminating Event

Processing

The dialed digits do not match any sequence in the dial plan.

The number is rejected.

The dialed digits exactly match one sequence in the dial plan.

If the sequence is allowed by the dial plan, the number is accepted and is transmitted according to the dial plan.

If the sequence is blocked by the dial plan, the number is rejected.

A timeout occurs.

The number is rejected if the dialed digits don''t matched a digit sequence in the dial plan within the time specified by
                                             the interdigit timer.

The Interdigit Long Timer applies when the dialed digits do not match any digit sequence in the dial plan. Default setting:
                                                   10 seconds

The Interdigit Short Timer applies when the dialed digits match one or more candidate sequences in the dial plan. Default
                                                   setting: 3 seconds

You press the # key.

If the sequence is complete and permitted by the dial plan, the number is accepted and is transmitted according to the dial
                                                   plan.

If the sequence is incomplete or is blocked by the dial plan, the number is rejected.

### Dial Plan Timer (Off-Hook Timer)

You can think of the Dial Plan Timer as the "off-hook timer." This timer starts counting when the phone goes off hook. If no digits are dialed within the specified number of seconds,
                                 the timer expires and the null entry is evaluated. Unless you have a special dial plan string to allow a null entry, the call
                                 is rejected. Default setting: 5

#### Syntax for the Dial Plan Timer

(Ps<:n> | dial plan )

s: The number of seconds; if no number is entered after P, the default timer of 5 seconds applies.

n: (optional): The number to transmit automatically when the timer expires; you can enter a valid number. No wildcard characters
                                       are allowed because the number will be transmitted as shown. If you omit the number substitution, <:n>, then the user hears
                                       a reorder (fast busy) tone after the specified number of seconds.

#### Examples for the Dial Plan Timer

Allow more time for users to start dialing after taking a phone off hook.

(P9 | (9,8<:1408>[2-9]xxxxxx | 9,8,1[2 9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)

P9 After taking a phone off hook, a user has 9 seconds to begin dialing. If no digits are pressed within 9 seconds, the user
                                       hears a reorder (fast busy) tone. By setting a longer timer, you allow more time for users to enter the digits.

xx This code allows the entry of one or more digits. Do not use a single x, allowing 0 or more digits. This setting will produce
                                       unwanted results especially if you are deploying timers.

Create a hotline for all sequences on the System Dial Plan

(P9<:23> | (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)

P9<:23> After taking the phone off hook, a user has 9 seconds to begin dialing. If no digits are pressed within 9 seconds,
                                       the call is transmitted automatically to extension 23.

Create a hotline on a line button for an extension

(P0 <:1000>)

With the timer set to 0 seconds, the call is transmitted automatically to the specified extension when the phone goes off
                                       hook.

### Interdigit Long Timer (Incomplete Entry Timer)

You can think of this timer as the “incomplete entry” timer. This timer measures the interval between dialed digits. It applies
                                 as long as the dialed digits do not match any digit sequences in the dial plan. Unless the user enters another digit within
                                 the specified number of seconds, the entry is evaluated as incomplete, and the call is rejected. Default setting: 10 seconds

This section explains how to edit a timer as part of a dial plan. Alternatively, you can modify the Control Timer that controls
                                 the default interdigit timers for all calls. See Reset the Control Timers .

#### Syntax for the Interdigit Long Timer

L:s, ( dial plan )

s: The number of seconds; if no number is entered after L:, the default timer of 5 seconds applies. The timer sequence appears
                                 to the left of the initial parenthesis for the dial plan.

#### Example for the Interdigit Long Timer

L:15, (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)

L:15, This dial plan allows the user to pause for up to 15 seconds between digits before the Interdigit Long Timer expires.

### Interdigit Short Timer (Complete Entry Timer)

You can think of this timer as the “complete entry” timer. This timer measures the interval between dialed digits. It applies
                                 when the dialed digits match at least one digit sequence in the dial plan. Unless the user enters another digit within the
                                 specified number of seconds, the entry is evaluated. If it is valid, the call proceeds. If it is invalid, the call is rejected.
                                 Default setting: 3 seconds

#### Syntax for the Interdigit Short Timer

SYNTAX 1: S:s, ( dial plan )

Use this syntax to apply the new setting to the entire dial plan within the parentheses.

SYNTAX 2: sequence Ss

Use this syntax to apply the new setting to a particular dialing sequence.

s: The number of seconds; if no number is entered after S, the default timer of 5 seconds applies.

#### Examples for the Interdigit Short Timer

Set the timer for the entire dial plan.

S:6,(9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)

S:6, While entering a number with the phone off hook, a user can pause for up to 15 seconds between digits before the Interdigit
                                 Short Timer expires.

Set an instant timer for a particular sequence within the dial plan.

(9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxxS0 | 9,8,011xx. | 9,8,xx.|[1-8]xx)

9,8,1[2-9]xxxxxxxxxS0 With the timer set to 0, the call is transmitted automatically when the user dials the final digit in
                                 the sequence.

### Reset the Control Timers

You can use the following procedure to reset the default timer settings for all calls.

To edit a timer setting only for a particular digit sequence or type of call, you can edit the dial plan. See Digit Sequences .

Step 1

Log in to the ATA web page. If prompted, enter the administrative login provided by the Service Provider.

Step 2

Under the Voice menu, click Regional .

Step 3

In the Control Timer Values section, enter the desired values in the Interdigit Long Timer field and the Interdigit Short Timer field. See the definitions at the beginning of this section.

## Emergency Calls

### Emergency Call Support Background

Emergency call service providers can register an ATA's location for each IP-based phone in a company. The location information
                                 server (LIS) transfers the emergency response location (ERL) to the ATA. The ATA stores its location during registration,
                                 after the ATA restarts. The location entry can specify the street address, building number, floor, room, and other office
                                 location information.

When you place an emergency call, the ATA transfers the location to the call server. The call server forwards the call and
                                 the location to the emergency call service provider. The emergency call service provider forwards the call and a unique call-back
                                 number (ELIN) to the emergency services. The emergency service or public safety answering point (PSAP) receives the ATA's
                                 location. The PSAP also receives a number to call you back, if the call disconnects.

See Emergency Call Support Terminology for the terms used to describe emergency calls from the phone.

The phone requests new location information for the following activities:

You register the ATA with the call server.

You or the user restarts the ATA and the ATA was previously registered with the call server.

You change the network interface used in the SIP registration.

You change the IP address of the ATA.

If both of the location servers do not send a location response, the phone resends the location request every two minutes.

### Emergency Call Support Terminology

The following terms describe emergency call support for the ATA.

Emergency Location ID Number (ELIN)–A number used to represent one or more ATA lines that locate the person who dialed emergency
                                       services.

Emergency Response Location (ERL)–A logical location that groups a set of ATA lines.

HTTP Enabled Location Delivery (HELD)–An encrypted protocol that obtains the PIDF-LO location for the ATA from a location
                                       information server (LIS).

Location Information Server (LIS)–A server that responds to a SIP-based ATA HELD request and provides the ATA location using
                                       a HELD XML response.

Emergency Call Service Provider–The company that responds to an ATA HELD request with the ATA's location. When you make an
                                       emergency call (which carries the ATA's location), a call server routes the call to this company. The emergency call service
                                       provider adds an ELIN and routes the call to the emergency services (PSAP). If the call is disconnected, the PSAP uses the
                                       ELIN to reconnect with the ATA used to make the emergency call.

Public Safety Answering Point (PSAP)–Any emergency service (for example, fire, police, or ambulance) joined to the Emergency
                                       Services IP Network.

Universally Unique Identifier (UUID)–A 128-bit number used to uniquely identify a company using emergency call support.

### Configure the ATA to Make Emergency Calls

#### Before you begin

Obtain the E911 Geolocation Configuration URLs and the company identifier for the ATA from your emergency call services provider.
                                       You can use the same Geolocation URLs and company identifier for line 1 and line 2 (PHONE 1 and PHONE 2).

Access the phone adapter administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Line n , where n is the line number that represents PHONE 1 or PHONE 2.

Step 2

In the section Call Feature Settings , set the parameter Emergency Number as described in Call Feature Settings .

Step 3

In the section E911 Geolocation Configuration , set the parameters Company UUID , Primary Request URL , and Secondary Request URL as described in E911 Geolocation Configuration .

Step 4

Click Submit .

| Step 1 | Ensure that you have enough bandwidth for the uplink and the downlink. For G.711 fallback, we recommend approximately 100 kbps. For T.38, allocate at least 50 kbps. |
|---|---|
| Step 2 | Click Voice in the menu bar, and then click Line 1 or Line 2 in the navigation tree. |
| Step 3 | In the Network Settings section, enter the following settings: Network Jitter Level— very high . Jitter Buffer Adjustment— no . |
| Step 4 | In the Supplementary Service Subscription section, enter the following settings: Call Waiting Serv— no . Three Way Call Serv— no . |
| Step 5 | In the Audio Configuration section, enter the following settings to support T.38 fax: Preferred Codec— G.711u (USA) or G.711a (rest of the world). Use pref. codec only— Yes . Silence Supp Enable— No . Echo Canc Enable— No . FAX Passthru Method— ReINVITE . |
| Step 6 | Click Submit to save your settings or click Cancel to abandon the unsaved settings. |
| Step 7 | If you are using a Cisco media gateway for PSTN termination, disable T.38 (fax relay) and enable fax using modem passthrough. For example: modem passthrough nse payload-type 110 codec g711ulaw fax rate disable fax protocol pass-through g711ulaw Note If a T.38 call cannot be set up, then the call automatically reverts to G.711 fallback. | Note | If a T.38 call cannot be set up, then the call automatically reverts to G.711 fallback. |
| Note | If a T.38 call cannot be set up, then the call automatically reverts to G.711 fallback. |
| Step 8 | If you are using a Cisco media gateway, make sure that the Cisco gateway is correctly configured for T.38 with the dial peer. For example: fax protocol T38 fax rate voice fax-relay ecm disable fax nsf 000000 no vad |

| Note | If a T.38 call cannot be set up, then the call automatically reverts to G.711 fallback. |
|---|---|

| Step 1 | Verify that your fax machine is set to a speed between 7200 and 14400. |
|---|---|
| Step 2 | Send a test fax in a controlled environment between two ATAs. |
| Step 3 | Determine the success rate. |
| Step 4 | Monitor the network and record the statistics for jitter, loss, and delay. |
| Step 5 | If faxes fail consistently, capture a copy of the configuration. You can then send this file to Technical Support. In your web browser, enter the path for the configuration file: https://<ATA_Local_IP_Address>/admin/config.xml&xuser= <admin_user>&xpassword=<admin_password> On the File menu, choose Save As , and save the file with a filename such as MyConfiguration.xml . |
| Step 6 | To enable logging, go to the Voice > System page, and set the IP address of your syslog or debug server. Set the Debug Level to 3. For more information, see System . Note You can also capture data using a sniffer trace. | Note | You can also capture data using a sniffer trace. |
| Note | You can also capture data using a sniffer trace. |
| Step 7 | Identify the type of fax machine connected to the ATA. |
| Step 8 | Contact technical support: If you are an user of VoIP products, contact the reseller or service provider that supplied the equipment. If you are an authorized Cisco partner, contact Cisco technical support. For contact options, see https://www.cisco.com/go/sbc . |

| Note | You can also capture data using a sniffer trace. |
|---|---|

| Note | White space is ignored, but may be used for readability. |
|---|---|

| Digit Sequence | Function |
|---|---|
| 0 1 2 3 4 5 6 7 8 9 0 * # | Enter any of these characters to represent a key that the user must press on the phone keypad. |
| x | Enter x to represent any character on the phone keypad. |
| [sequence] | Enter characters within square brackets to create a list of accepted key presses. The user can press any one of the keys in
                                             the list. Numeric range: For example, you would enter [2-9] to allow the user to press any one digit from 2 through 9. Numeric range with other characters: For example, you would enter [35-8*] to allow the user to press 3, 5, 6, 7, 8, or *. |
| . (period) | Enter a period for element repetition. The dial plan accepts zero or more entries of the digit. For example, 01. allows users
                                             to enter 0, 01, 011, 0111, and so on. |
| <dialed:substituted> | Use this format to indicate that certain dialed digits are replaced by other characters when the sequence is transmitted.
                                             The dialed digits can be zero or more characters. EXAMPLE 1: <8:1650>xxxxxxx When the user presses 8 followed by a seven digit number, the system automatically replaces the dialed 8 with 1650. If the
                                             user dials 85550112, the system transmits 16505550112. EXAMPLE 2: <:1>xxxxxxxxxx In this example, no digits are replaced. When the user enters a 10-digit string of numbers, the number 1 is added at the beginning
                                             of the sequence. If the user dials 9725550112, the system transmits 19725550112. |
| , (comma) | Enter a comma between digits to play an “outside line” dial tone after a user-entered sequence. EXAMPLE: 9, 1xxxxxxxxxx An “outside line” dial tone is sounded after the user presses 9, and the tone continues until the user presses 1. |
| ! (exclamation point) | Enter an exclamation point to prohibit a dial sequence pattern. EXAMPLE: 1900xxxxxxx! The system rejects any 11-digit sequence that begins with 1900. |
| *xx | Enter an asterisk to allow the user to enter a 2-digit star code. |
| S0 or L0 | Enter S0 to reduce the short inter-digit timer to 0 seconds, or enter L0 to reduce the long inter-digit timer to 0 seconds. |

| Terminating Event | Processing |
|---|---|
| The dialed digits do not match any sequence in the dial plan. | The number is rejected. |
| The dialed digits exactly match one sequence in the dial plan. | If the sequence is allowed by the dial plan, the number is accepted and is transmitted according to the dial plan. If the sequence is blocked by the dial plan, the number is rejected. |
| A timeout occurs. | The number is rejected if the dialed digits don''t matched a digit sequence in the dial plan within the time specified by
                                             the interdigit timer. The Interdigit Long Timer applies when the dialed digits do not match any digit sequence in the dial plan. Default setting:
                                                   10 seconds The Interdigit Short Timer applies when the dialed digits match one or more candidate sequences in the dial plan. Default
                                                   setting: 3 seconds |
| You press the # key. | If the sequence is complete and permitted by the dial plan, the number is accepted and is transmitted according to the dial
                                                   plan. If the sequence is incomplete or is blocked by the dial plan, the number is rejected. |

| Step 1 | Log in to the ATA web page. If prompted, enter the administrative login provided by the Service Provider. |
|---|---|
| Step 2 | Under the Voice menu, click Regional . |
| Step 3 | In the Control Timer Values section, enter the desired values in the Interdigit Long Timer field and the Interdigit Short Timer field. See the definitions at the beginning of this section. |

| Step 1 | Select Voice > Line n , where n is the line number that represents PHONE 1 or PHONE 2. |
|---|---|
| Step 2 | In the section Call Feature Settings , set the parameter Emergency Number as described in Call Feature Settings . |
| Step 3 | In the section E911 Geolocation Configuration , set the parameters Company UUID , Primary Request URL , and Secondary Request URL as described in E911 Geolocation Configuration . |
| Step 4 | Click Submit . |