---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-sayitsmart-guide-cc-ee9b320334
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/sayitsmart/guide/ccvp_b_1262-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_01000.html
retrieved_at: 2026-08-21T17:39:56.271695+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Phone

## Chapter: Phone

# Phone

Plugin
                                    Name:

phone

Display Name:

Phone Number

Class Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartPhone

## Description

This Say It Smart type handles the reading of a 10 digit phone number.
                           The number must have an area code and cannot be an 11-digit number starting
                           with 1. Many times, a phone number may appear with various formatting. To avoid
                           having to process the data before it is sent to the plug-in, the plug-in will
                           understand the standard phone number formats. The phone number is read
                           digit-by-digit, inserting 150 millisecond pauses after the area code and
                           exchange.

The plug-in Java class can easily be extended to create,
                           in just a few lines of code, a new plug-in performing the same function with a
                           different pause length or additional formatting
                           options.

## Input
                        	 Formats

Name

(Display Name)

Description

10_digit_whole_number

(10 Digit Number)

The data can be handled in any of the following formats:

##########

(###) ###-####

(###)###-####

###-###-####

###.###.####

(###)#######

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

digits_with_pauses

(As Digits w/
                                          Pauses)

10_digit_whole_number

The
                                          phone number is played back digit-by-digit with 150 millisecond pauses where
                                          the number is normally divided.

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
                              extension, the developer can choose whatever file type supported by their voice
                              browser.

0

1

2

3

4

5

6

7

8

9

silence

## Examples

Example #1

Data:

(800) 555-1212

Input Format:

10_digit_whole_number

Output Format:

digits_with_pauses

Fileset

standard

Playback:

"8" "0" "0"

<150ms pause>

"5" "5" "5"

<150ms
                                          pause>

"1" "2" "1" "2"

Example #2

Data:

1112223333

Input
                                          Format:

10_digit_whole_number

Output Format:

digits_with_pauses

Fileset

standard

Playback:

"1" "1" "1"

<150ms pause>

"2" "2" "2"

<150ms
                                          pause>

"3" "3" "3" "3"

| Plugin
                                    Name: | phone |
|---|---|
| Display Name: | Phone Number |
| Class Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartPhone |

| Name (Display Name) | Description |
|---|---|
| 10_digit_whole_number (10 Digit Number) | The data can be handled in any of the following formats: ########## (###) ###-#### (###)###-#### ###-###-#### ###.###.#### (###)####### Note The second format contains a space after the area code;
                                                   						the third does not. | Note | The second format contains a space after the area code;
                                                   						the third does not. |
| Note | The second format contains a space after the area code;
                                                   						the third does not. |

| Note | The second format contains a space after the area code;
                                                   						the third does not. |
|---|---|

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| digits_with_pauses (As Digits w/
                                          Pauses) | 10_digit_whole_number | The
                                          phone number is played back digit-by-digit with 150 millisecond pauses where
                                          the number is normally divided. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard (0-9)) | digits_with_pauses | This fileset contains ten files: 0 through 9. It is
                                          the only fileset
                                          required. |

| Note | The silence file is used when Use Recorded Audio is selected and when there is no TTS
                                       engine in the deployment. The recorded audio requires silence pauses be inserted between digits. These pauses
                                       are inserted automatically if using a TTS engine. If you do not have a TTS
                                       engine in your deployment, then copy the silence file to the same location on
                                       your media server as the number files. The silence file must be 150ms in
                                       duration. |
|---|---|

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | silence |
|---|---|---|---|---|---|---|---|---|---|---|

| Data: | (800) 555-1212 |
|---|---|
| Input Format: | 10_digit_whole_number |
| Output Format: | digits_with_pauses |
| Fileset | standard |
| Playback: | "8" "0" "0" <150ms pause> "5" "5" "5" <150ms
                                          pause> "1" "2" "1" "2" |

| Data: | 1112223333 |
|---|---|
| Input
                                          Format: | 10_digit_whole_number |
| Output Format: | digits_with_pauses |
| Fileset | standard |
| Playback: | "1" "1" "1" <150ms pause> "2" "2" "2" <150ms
                                          pause> "3" "3" "3" "3" |