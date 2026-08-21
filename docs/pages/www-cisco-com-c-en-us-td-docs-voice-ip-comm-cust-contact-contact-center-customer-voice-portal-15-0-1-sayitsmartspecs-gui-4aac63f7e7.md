---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-sayitsmartspecs-gui-4aac63f7e7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/sayitsmartspecs/guide/cvp_b_1501-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_m_1501-digits.html
retrieved_at: 2026-08-21T03:04:56.685546+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal Release 15.0(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal Release 15.0(1)

Updated: March 1, 2025

Chapter: Digits

## Chapter: Digits

# Digits

## Description

This Say It Smart type handles the reading of any number digit by digit.
                           The number can be negative or positive and can also contain a decimal (though,
                           unlike Number, exponents are not supported). Every character is read
                           individually.

## Input Formats

Name

(Display Name)

Description

number

(Any Length Number)

This number can appear as any
                                          length whole or decimal number. If the number is negative, the minus sign must
                                          be the first
                                          character.

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

digits

(Digit-By-Digit)

number

The number can be played back in only one manner:
                                          digit by digit.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

standard

(Standard)

digits

This single fileset contains all numbers from 0 to 9 as well as point and negative .

## Audio Files

0

2

3

4

5

6

7

8

9

negative

point

## Examples

Example #1

Data:

96.89

Input Format:

number

Output
                                          Format:

digits

Fileset

standard

Playback:

”9” ”6” ”point” ”8”
                                          ”9”

Example #2

Data:

-10

Input
                                          Format:

number

Output Format:

digits

Fileset

standard

Playback:

"negative“ “1" "0"

| Name (Display Name) | Description |
|---|---|
| number (Any Length Number) | This number can appear as any
                                          length whole or decimal number. If the number is negative, the minus sign must
                                          be the first
                                          character. |

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| digits (Digit-By-Digit) | number | The number can be played back in only one manner:
                                          digit by digit. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard) | digits | This single fileset contains all numbers from 0 to 9 as well as point and negative . |

| 0 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 6 | 7 | 8 | 9 |  |
| negative | point |  |  |  |

| Data: | 96.89 |
|---|---|
| Input Format: | number |
| Output
                                          Format: | digits |
| Fileset | standard |
| Playback: | ”9” ”6” ”point” ”8”
                                          ”9” |

| Data: | -10 |
|---|---|
| Input
                                          Format: | number |
| Output Format: | digits |
| Fileset | standard |
| Playback: | "negative“ “1" "0" |