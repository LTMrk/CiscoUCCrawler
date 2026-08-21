---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-f7a6c6aa70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_01001.html
retrieved_at: 2026-08-21T03:08:59.824565+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: February 2, 2020

Chapter: Social Security

## Chapter: Social Security

# Social Security

Plugin Name:

ssn

Display
                                    Name:

Social Security Number

Class
                                    Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartSocialSecurity

## Description

This Say It Smart type handles the reading of a 9-digit social security
                           number. Many times, a social security number may appear with dashes after the
                           third and fifth digits. To avoid having to process the data before it is sent
                           to the plug-in, it will understand the social security number with these
                           optional dashes, though no punctuation other than dashes is allowed. It reads
                           it back digit-by-digit, inserting 150 millisecond pauses after the third and
                           fifth digits.

The plug-in Java class can easily be extended to
                           create, in just a few lines of code, a new plug-in performing the same function
                           with a different pause length or additional formatting
                           options.

## Input
                        	 Formats

Name

(Display Name)

Description

9_digit_whole_number

(9 Digit Number)

The data can be handled in any of the following formats:

#########

###-##-####

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

digits_with_pauses

(As Digits w/
                                          Pauses)

9_digit_whole_number

The
                                          social security number is played back digit-by-digit with 150 millisecond
                                          pauses after the third and fifth digits.

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
                                          the only fileset required.

## Audio Files

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

123-45-6789

Input
                                          						Format:

9_digit_whole_number

Output
                                          						Format:

digits_with_pauses

Fileset

standard

Playback:

"1" ”2” ”3”

<150ms
                                          						pause>

”4” ”5”

<150ms
                                          						pause>

”6” ”7”
                                          						”8” ”9”

Example #2

Data:

111223333

Input Format:

9_digit_whole_number

Output Format:

digits_with_pauses

Fileset

standard

Playback:

"1" ”1” ”1”

<150ms pause>

”2” ”2”

<150ms pause>

”3” ”3” ”3” ”3”

| Plugin Name: | ssn |
|---|---|
| Display
                                    Name: | Social Security Number |
| Class
                                    Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartSocialSecurity |

| Name (Display Name) | Description |
|---|---|
| 9_digit_whole_number (9 Digit Number) | The data can be handled in any of the following formats: ######### ###-##-#### |

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| digits_with_pauses (As Digits w/
                                          Pauses) | 9_digit_whole_number | The
                                          social security number is played back digit-by-digit with 150 millisecond
                                          pauses after the third and fifth digits. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard (0-9)) | digits_with_pauses | This fileset contains ten files: 0 through 9. It is
                                          the only fileset required. |

| Note | The silence file is used when Use Recorded
                                          Audio is selected and when there is no TTS engine in the deployment.
                                       The recorded audio requires silence pauses be inserted
                                       between digits. These pauses are inserted automatically if using a TTS engine.
                                       If you do not have a TTS engine in your deployment, then copy the silence file
                                       to the same location on your media server as the number files. The silence file
                                       must be 150ms in duration. |
|---|---|

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | silence |
|---|---|---|---|---|---|---|---|---|---|---|

| Data: | 123-45-6789 |
|---|---|
| Input
                                          						Format: | 9_digit_whole_number |
| Output
                                          						Format: | digits_with_pauses |
| Fileset | standard |
| Playback: | "1" ”2” ”3” <150ms
                                          						pause> ”4” ”5” <150ms
                                          						pause> ”6” ”7”
                                          						”8” ”9” |

| Data: | 111223333 |
|---|---|
| Input Format: | 9_digit_whole_number |
| Output Format: | digits_with_pauses |
| Fileset | standard |
| Playback: | "1" ”1” ”1” <150ms pause> ”2” ”2” <150ms pause> ”3” ”3” ”3” ”3” |