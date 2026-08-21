---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-4acd08b763
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_01.html
retrieved_at: 2026-08-21T03:08:26.419938+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: February 2, 2020

Chapter: Credit Card

## Chapter: Credit Card

# Credit Card

Basic information about this plugin:

Plugin Name:

creditcard

Display Name:

Credit Card

Class
                                    Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartCreditCard

## Description

This Say It Smart type handles the reading of a credit card number. Any
                           13, 14, 15, or 16 digit number will be handled. Many times, a credit card
                           number may appear with dashes at certain places in the number. To avoid having
                           to process the data before it is sent to the plug-in, it will understand the
                           credit card number with these optional dashes, though no punctuation other than
                           dashes is allowed. The plug-in reads the credit card number back
                           digit-by-digit, inserting 150 millisecond pauses at certain places where the
                           credit card number is normally divided.

The plug-in Java class
                           can easily be extended to create, in just a few lines of code, a new plug-in
                           performing the same function with a different pause length or additional
                           formatting options.

## Input
                        	 Formats

Name

(Display Name)

Description

cc_number

(13/14/15/16 Digit Number)

The data can be handled in any of the following formats:

16-digit cards (Visa, Mastercard, etc.):

################, ####-####-####-####

15-digit cards (American Express):

###############, ####-######-#####

14-digit cards (Diner's Club):

##############, ####-#######-####

13-digit cards (Visa):

#############, ####-###-###-###

## Output Formats

Name

(Display
                                             Name)

Input Format
                                             Depends On

Description

digits_with_pauses

(As digits w/
                                          pauses)

cc_number

The credit card number is played back
                                          digit-by-digit with 150 millisecond pauses where the number is normally
                                          divided.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

standard

(Standard (0-9))

digits_with_pauses

This fileset contains ten files: 0 through 9. It is
                                          the only fileset
                                          required.

## Audio Files

All audio files must be named as appears below. The names do not have an
                              extension, the developer can choose whatever file type is supported by their
                              voice browser.

1

2

3

4

5

6

7

8

9

0

silence

## Examples

Example #1

Data:

1234-5678-9012-3456

Input Format:

cc_number

Output Format:

digits_with_pauses

Fileset

standard

Playback:

"1" "2" "3" "4"

<150ms pause>

"5" "6" "7" "8"

<150ms pause>

"9" "0" "1" "2"

<150ms pause>

"3" "4" "5" "6"

Example #2

Data:

111122222233333

Input Format:

cc_number

Output Format:

digits_with_pauses

Fileset

standard

Playback:

"1" "1" "1" "1"

<150ms pause>

"2" "2" "2" "2" "2" "2"

<150ms pause>

"3" "3" "3" "3" "3"

| Plugin Name: | creditcard |
|---|---|
| Display Name: | Credit Card |
| Class
                                    Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartCreditCard |

| Name (Display Name) | Description |
|---|---|
| cc_number (13/14/15/16 Digit Number) | The data can be handled in any of the following formats: 16-digit cards (Visa, Mastercard, etc.): ################, ####-####-####-#### 15-digit cards (American Express): ###############, ####-######-##### 14-digit cards (Diner's Club): ##############, ####-#######-#### 13-digit cards (Visa): #############, ####-###-###-### |

| Name (Display
                                             Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| digits_with_pauses (As digits w/
                                          pauses) | cc_number | The credit card number is played back
                                          digit-by-digit with 150 millisecond pauses where the number is normally
                                          divided. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard (0-9)) | digits_with_pauses | This fileset contains ten files: 0 through 9. It is
                                          the only fileset
                                          required. |

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | silence |
|---|---|---|---|---|---|---|---|---|---|---|

| Note | The silence file is used when Use Recorded
                                          Audio is selected and when there is no TTS engine in the deployment.
                                       The recorded audio requires silence pauses be inserted
                                       between digits. These pauses are inserted automatically if using a TTS engine.
                                       If you do not have a TTS engine in your deployment, then copy the silence file
                                       to the same location on your media server as the number files. The silence file
                                       must be 150ms in duration. |
|---|---|

| Data: | 1234-5678-9012-3456 |
|---|---|
| Input Format: | cc_number |
| Output Format: | digits_with_pauses |
| Fileset | standard |
| Playback: | "1" "2" "3" "4" <150ms pause> "5" "6" "7" "8" <150ms pause> "9" "0" "1" "2" <150ms pause> "3" "4" "5" "6" |

| Data: | 111122222233333 |
|---|---|
| Input Format: | cc_number |
| Output Format: | digits_with_pauses |
| Fileset | standard |
| Playback: | "1" "1" "1" "1" <150ms pause> "2" "2" "2" "2" "2" "2" <150ms pause> "3" "3" "3" "3" "3" |