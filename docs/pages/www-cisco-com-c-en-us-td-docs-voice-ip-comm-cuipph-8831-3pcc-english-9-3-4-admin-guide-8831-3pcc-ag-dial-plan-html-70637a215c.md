---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-admin-guide-8831-3pcc-ag-dial-plan-html-70637a215c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/admin-guide/8831-3pcc-ag/dial-plan.html
retrieved_at: 2026-08-21T02:09:34.646595+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

Updated: October 22, 2014

Chapter: Configure Dial Plan

## Chapter: Configure Dial Plan

## Configure Dial Plan

Dial plans determine how the digits are interpreted and transmitted. They also determine whether the dialed number is accepted or rejected. You can use a dial plan to facilitate dialing or to block certain types of calls such as long distance or international.

The dial plans can be configured on the IP phone by using the phone web user interface.

This section includes information that you need to understand dial plans, as well as procedures for configuring your own dial plans:

## About Dial Plan

The conference phone has various levels of dial plans and processes the digits sequence.

When a user presses the speaker button on the phone, the following sequence of events begins:

1. The phone begins collecting the dialed digits. The inter-digit timers starts tracking the time that elapses between digits.

2. If the inter-digit timer value is reached, or if another terminating event occurs, the phone compares the dialed digits with the IP phone dial plan. (This dial plan is configured in the phone web user interface in the Voice tab > Extension under the Dial Plan section.)

### Digit Sequences

A dial plan contains a series of digit sequences, separated by the | character. The entire collection of sequences is enclosed within parentheses. Each digit sequence within the dial plan consists of a series of elements that are individually matched to the keys that the user presses.

White space is ignored, but can be used for readability.

0 1 2 3 4 5 6 7 8 9 0 * #

Characters that represent a key that the user must press on the phone keypad.

x

Any character on the phone keypad.

[sequence]

Characters within square brackets create a list of accepted key presses. The user can press any one of the keys in the list.

A numeric range, for example, [2-9] allows a user to press any one digit from 2 through 9 .

A numeric range can include other characters. For example, [35-8*] allows a user to press 3, 5, 6, 7, 8, or *.

. (period)

A period indicates element repetition. The dial plan accepts 0 or more entries of the digit. For example, 01. allows users to enter 0, 01, 011, 0111, and so forth.

<dialed:substituted>

This format indicates that certain dialed digits are replaced by the substituted characters when the sequence is transmitted. The dialed digits can be zero to 9. For example:

When the user presses 8 followed by a seven-digit number, the system automatically replaces the dialed 8 with the sequence 1650 . If the user dials 85550112 , the system transmits 16505550112 .

If the dialed parameter is empty and there is a value in the substituted field, no digits are replaced and the substituted value is always prepended to the transmitted string. For example:

When the user dials 9725550112 , the number 1 is added at the beginning of the sequence; the system transmits 19725550112 .

, (comma)

An intersequence tone played (and placed) between digits plays an outside line dial tone. For example:

An outside line dial tone is sounded after the user presses 9 . The tone continues until the user presses 1 .

! (exclamation point)

Prohibits a dial sequence pattern. For example:

Rejects any 11-digit sequence that begins with 1900.

*xx

Allows a user to enter a 2-digit star code.

S0 or L0

For Interdigit Timer Master Override, enter S0 to reduce the short inter-digit timer to 0 seconds, or enter L0 to reduce the long inter-digit timer to 0 seconds.

P

To pause, enter P , the number of seconds to pause, and a space. This feature is typically used for implementation of a hot line and warm line, with a 0 delay for the hot line and a non-zero delay for a warm line. For example:

EXAMPLE: P5

A pause of 5 seconds is introduced.

### Digit Sequence Examples

The following examples show digit sequences that you can enter in a dial plan.

In a complete dial plan entry, sequences are separated by a pipe character (|), and the entire set of sequences is enclosed within parentheses:

Extensions on your system:

[1-8]xx Allows a user dial any three-digit number that starts with the digits 1 through 8. If your system uses four-digit extensions, you would instead enter the following string: [1-8]xxx

Local dialing with seven-digit number:

9, xxxxxxx After a user presses 9, an external dial tone sounds. The user can enter any seven-digit number, as in a local call.

Local dialing with 3-digit area code and a 7-digit local number:

9, <:1>[2-9]xxxxxxxxx This example is useful where a local area code is required. After a user presses 9, an external dial tone sounds. The user must enter a 10-digit number that begins with a digit 2 through 9. The system automatically inserts the 1 prefix before transmitting the number to the carrier.

Local dialing with an automatically inserted 3-digit area code:

8, <:1212>xxxxxxx This is example is useful where a local area code is required by the carrier but the majority of calls go to one area code. After the user presses 8, an external dial tone sounds. The user can enter any seven-digit number. The system automatically inserts the 1 prefix and the 212 area code before transmitting the number to the carrier.

U.S. long distance dialing:

9, 1 [2-9] xxxxxxxxx After the user presses 9, an external dial tone sounds. The user can enter any 11-digit number that starts with 1 and is followed by a digit 2 through 9.

Blocked number:

9, 1 900 xxxxxxx ! This digit sequence is useful if you want to prevent users from dialing numbers that are associated with high tolls or inappropriate content, such as 1-900 numbers in the U.S.. After the user press 9, an external dial tone sounds. If the user enters an 11-digit number that starts with the digits 1900, the call is rejected.

U.S. international dialing:

9, 011xxxxxx. After the user presses 9, an external dial tone sounds. The user can enter any number that starts with 011, as in an international call from the U.S.

Informational numbers:

0 | [49]11 This example includes two digit sequences, separated by the pipe character. The first sequence allows a user to dial 0 for an operator. The second sequence allows the user to enter 411 for local information or 911 for emergency services.

### Acceptance and Transmission of the Dialed Digits

When a user dials a series of digits, each sequence in the dial plan is tested as a possible match. The matching sequences form a set of candidate digit sequences. As more digits are entered by the user, the set of candidates diminishes until only one or none are valid. When a terminating event occurs, the IP PBX either accepts the user-dialed sequence and initiates a call, or else rejects the sequence as invalid. The user hears the reorder (fast busy) tone if the dialed sequence is invalid.

The following table explains how terminating events are processed.

Dialed digits do not match any sequence in the dial plan.

The number is rejected.

Dialed digits exactly match one sequence in the dial plan.

If the sequence is allowed by the dial plan, the number is accepted and is transmitted according to the dial plan.

If the sequence is blocked by the dial plan, the number is rejected.

A timeout occurs.

The number is rejected if the dialed digits are not matched to a digit sequence in the dial plan within the time specified by the applicable interdigit timer.

The Interdigit Long Timer applies when the dialed digits do not match any digit sequence in the dial plan. The default value is 10 seconds.

The Interdigit Short Timer applies when the dialed digits match one or more candidate sequences in the dial plan. The default value is 3 seconds.

A user presses the # key or the dial softkey on the IP phone screen.

If the sequence is complete and is allowed by the dial plan, the number is accepted and is transmitted according to the dial plan.

If the sequence is incomplete or is blocked by the dial plan, the number is rejected.

### Dial Plan Timer (Off-Hook Timer)

You can think of the Dial Plan Timer as the off-hook timer . This timer starts when the phone goes off hook. If no digits are dialed within the specified number of seconds, the timer expires and the null entry is evaluated. Unless you have a special dial plan string to allow a null entry, the call is rejected. The default value is 5.

### Syntax for the Dial Plan Timer

SYNTAX: (P s <: n > | dial plan )

- s: The number of seconds; if no number is entered after P , the default timer of 5 seconds applies. With the timer set to 0 seconds, the call is transmitted automatically to the specified extension when the phone goes off hook.

- n: (optional): The number to transmit automatically when the timer expires; you can enter an extension number or a DID number. No wildcard characters are allowed because the number will be transmitted as shown. If you omit the number substitution, <:n>, then the user hears a reorder (fast busy) tone after the specified number of seconds.

### Examples for the Dial Plan Timer

Allow more time for users to start dialing after taking a phone off hook:

P9 After taking a phone off hook, a user has 9 seconds to begin dialing. If no digits are pressed within 9 seconds, the user hears a reorder (fast busy) tone. By setting a longer timer, you allow more time for users to enter the digits.

Create a hotline for all sequences on the System Dial Plan:

P9<:23> After taking the phone off hook, a user has 9 seconds to begin dialing. If no digits are pressed within 9 seconds, the call is transmitted automatically to extension 23.

Create a hotline on a line button for an extension:

With the timer set to 0 seconds, the call is transmitted automatically to the specified extension when the phone goes off hook. Enter this sequence in the Phone Dial Plan for Ext 2 or higher on a client phone.

### Interdigit Long Timer (Incomplete Entry Timer)

You can think of this timer as the incomplete entry timer. This timer measures the interval between dialed digits. It applies as long as the dialed digits do not match any digit sequences in the dial plan. Unless the user enters another digit within the specified number of seconds, the entry is evaluated as incomplete, and the call is rejected. The default value is 10 seconds.

This section explains how to edit a timer as part of a dial plan. Alternatively, you can modify the Control Timer that controls the default interdigit timers for all calls. See the “Reset the Control Timers” section .

### Syntax for the Interdigit Long Timer

SYNTAX: L :s, ( dial plan )

- s: The number of seconds; if no number is entered after L: , the default timer is 5 seconds. With the timer set to 0 seconds, the call is transmitted automatically to the specified extension when the phone goes off hook.

- Note that the timer sequence appears to the left of the initial parenthesis for the dial plan.

### Example for the Interdigit Long Timer

L:15, This dial plan allows the user to pause for up to 15 seconds between digits before the Interdigit Long Timer expires. This setting is especially helpful to users such as sales people, who are reading the numbers from business cards and other printed materials while dialing.

### Interdigit Short Timer (Complete Entry Timer)

You can think of this timer as the “complete entry” timer. This timer measures the interval between dialed digits. It applies when the dialed digits match at least one digit sequence in the dial plan. Unless the user enters another digit within the specified number of seconds, the entry is evaluated. If it is valid, the call proceeds. If it is invalid, the call is rejected. The default value is 3 seconds.

### Syntax for the Interdigit Short Timer

SYNTAX 1: S :s, ( dial plan )

Use this syntax to apply the new setting to the entire dial plan within the parentheses.

SYNTAX 2: sequence Ss

Use this syntax to apply the new setting to a particular dialing sequence.

s: The number of seconds; if no number is entered after S , the default timer of 5 seconds applies.

### Examples for the Interdigit Short Timer

Set the timer for the entire dial plan:

S:6, While entering a number with the phone off hook, a user can pause for up to 15 seconds between digits before the Interdigit Short Timer expires. This setting is especially helpful to users such as sales people, who are reading the numbers from business cards and other printed materials while dialing.

Set an instant timer for a particular sequence within the dial plan:

9,8,1[2-9]xxxxxxxxxS0 With the timer set to 0, the call is transmitted automatically when the user dials the final digit in the sequence.

## Edit Dial Plan on the IP Phone

You can edit the dial plan and modify the control timers. To edit the dial plan on the IP conference phone:

Step 1 Navigate to Admin Login > advanced > Voice .

Step 2 Click the Extension tab and scroll to Dial Plan.

Step 3 In the Dial Plan section, enter the digit sequences in the Dial Plan field. For more information and examples, see the “Digit Sequences” section .

The default (US-based) system-wide dial plan appears automatically in the field. You can delete digit sequences, add digit sequences, or replace the entire dial plan with a new dial plan. For more information and examples, see the “Digit Sequences” section .

Separate each digit sequence with a pipe character, and enclose the entire set of digit sequences within parentheses. Refer to the following example:

Step 4 Click Submit All Changes . The phone reboots.

Step 5 Verify that you can successfully complete a call using each digit sequence that you entered in the dial plan.

Note If you hear a reorder (fast busy) tone, you need to review your entries and modify the dial plan appropriately. See the “Digit Sequences” section .

## Reset the Control Timers

You can use the following procedure to reset the default timer settings for all calls.

If you need to edit a timer setting only for a particular digit sequence or type of call, you can edit the dial plan. See the “About Dial Plan” section .

Step 1 Log in to the phone web user interface.

Step 2 Click Admin Login and advanced .

Step 3 Click Voice > Regional .

Step 4 Scroll down to the Control Timer Values (sec) section.

Step 5 Enter the desired values in the Interdigit Long Timer field and the Interdigit Short Timer field. Refer to the definitions at the beginning of this section.

| Digit Sequence | Function |
|---|---|
| 0 1 2 3 4 5 6 7 8 9 0 * # | Characters that represent a key that the user must press on the phone keypad. |
| x | Any character on the phone keypad. |
| [sequence] | Characters within square brackets create a list of accepted key presses. The user can press any one of the keys in the list. A numeric range, for example, [2-9] allows a user to press any one digit from 2 through 9 . A numeric range can include other characters. For example, [35-8*] allows a user to press 3, 5, 6, 7, 8, or *. |
| . (period) | A period indicates element repetition. The dial plan accepts 0 or more entries of the digit. For example, 01. allows users to enter 0, 01, 011, 0111, and so forth. |
| <dialed:substituted> | This format indicates that certain dialed digits are replaced by the substituted characters when the sequence is transmitted. The dialed digits can be zero to 9. For example: <8:1650>xxxxxxx When the user presses 8 followed by a seven-digit number, the system automatically replaces the dialed 8 with the sequence 1650 . If the user dials 85550112 , the system transmits 16505550112 . If the dialed parameter is empty and there is a value in the substituted field, no digits are replaced and the substituted value is always prepended to the transmitted string. For example: <:1>xxxxxxxxxx When the user dials 9725550112 , the number 1 is added at the beginning of the sequence; the system transmits 19725550112 . |
| , (comma) | An intersequence tone played (and placed) between digits plays an outside line dial tone. For example: 9, 1xxxxxxxxxx An outside line dial tone is sounded after the user presses 9 . The tone continues until the user presses 1 . |
| ! (exclamation point) | Prohibits a dial sequence pattern. For example: 1900xxxxxxx! Rejects any 11-digit sequence that begins with 1900. |
| *xx | Allows a user to enter a 2-digit star code. |
| S0 or L0 | For Interdigit Timer Master Override, enter S0 to reduce the short inter-digit timer to 0 seconds, or enter L0 to reduce the long inter-digit timer to 0 seconds. |
| P | To pause, enter P , the number of seconds to pause, and a space. This feature is typically used for implementation of a hot line and warm line, with a 0 delay for the hot line and a non-zero delay for a warm line. For example: EXAMPLE: P5 A pause of 5 seconds is introduced. |

| Terminating Event | Processing |
|---|---|
| Dialed digits do not match any sequence in the dial plan. | The number is rejected. |
| Dialed digits exactly match one sequence in the dial plan. | If the sequence is allowed by the dial plan, the number is accepted and is transmitted according to the dial plan. If the sequence is blocked by the dial plan, the number is rejected. |
| A timeout occurs. | The number is rejected if the dialed digits are not matched to a digit sequence in the dial plan within the time specified by the applicable interdigit timer. The Interdigit Long Timer applies when the dialed digits do not match any digit sequence in the dial plan. The default value is 10 seconds. The Interdigit Short Timer applies when the dialed digits match one or more candidate sequences in the dial plan. The default value is 3 seconds. |
| A user presses the # key or the dial softkey on the IP phone screen. | If the sequence is complete and is allowed by the dial plan, the number is accepted and is transmitted according to the dial plan. If the sequence is incomplete or is blocked by the dial plan, the number is rejected. |