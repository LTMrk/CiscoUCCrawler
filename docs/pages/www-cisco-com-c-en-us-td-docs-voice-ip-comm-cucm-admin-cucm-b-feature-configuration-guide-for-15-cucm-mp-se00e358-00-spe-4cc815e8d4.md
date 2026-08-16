---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-mp-se00e358-00-spe-4cc815e8d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_mp_se00e358_00_speed-dial-and-abbreviated-dial.html
retrieved_at: 2026-08-16T16:03:54.765252+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Speed Dial and Abbreviated Dial

## Chapter: Speed Dial and Abbreviated Dial

# Speed Dial and Abbreviated Dial

## Speed Dial and
                        	 Abbreviated Dial Overview

Administrators can configure
                           		speed dial numbers for phones to provide speed dial buttons for users or to configure phones that do not have a specific
                           user that is assigned to
                           		them. Users use the Cisco Unified Communications Self Care Portal to change the
                           		speed dial buttons on their phones. When configuring speed dial entries, some
                           		of the speed dial entries are assigned to the speed dial buttons on the IP
                           		phone; the remaining speed dial entries are used for abbreviated dialing. When
                           		a user starts dialing digits, the AbbrDial softkey displays, and the user can
                           		access any speed dial entry by entering the appropriate index (code) for
                           		abbreviated dialing.

The speed dial
                           		settings on the phone are associated with a physical button on a phone, whereas
                           		the abbreviated dial settings are not associated with a phone button.

### Programming Speed Dials with Pauses

You can program commas in your speed dials to reach destinations that require a Forced Authorization Code (FAC), Client Matter
                                 Code (CMC), dialing pause, or additional digits (such as a user extension, meeting access number, or voice mail password).
                                 Within a speed dial, each comma (,) represents either:

A delimiter that separates the destination call address from an FAC or CMC code

A pause of 2 seconds prior to sending post-connect DTMF digits

For example, let’s say that you want a speed dial that includes FAC and CMC codes, followed by IVR prompts where:

The called number is 91886543.

The FAC code is 8787.

The CMC code is 5656.

The IVR response is 987989#, which must be entered 4 seconds after the call connects.

In this case, you would program 91886543,8787,5656,,987989# as the speed dial.

## Speed Dial and
                        	 Abbreviated Dial Configuration Task Flow

Step 1

Generate a Phone Feature List

Generate a
                                          				report to identify devices that support the Speed Dial and Abbreviated Dial
                                          				feature.

Step 2

Configure Speed Dial and Abbreviated Dial

Configure
                                          				Speed Dial and Abbreviated Dial numbers.

### Configure Speed
                           	 Dial and Abbreviated Dial

You can configure
                                 		  a total of 199 speed dial and abbreviated dial settings. Configure speed dial
                                 		  settings for the physical buttons on the phone. Configure abbreviated dial
                                 		  settings for the speed dial numbers that you access with abbreviated dialing.
                                 		  You can configure speed dial entries and abbreviated dial indexes in the same
                                 		  window.

You can also
                                 		  configure post connect DTMF digits as well as FAC , CMC codes as part of the
                                 		  speed dial.

Follow these steps
                                 		  to configure speed dial and abbreviated dial.

#### Before you begin

Generate a Phone Feature List

Step 1

From Cisco Unified CM Administration, choose Device > Phone . Enter your search criteria and click Find . Choose the phone for which you want to configure speed dial buttons.

Step 2

From the Phone
                                             				Configuration window, choose Add/Update Speed Dials from the Related Links
                                          			 drop-down list at the top of the window and click Go .

Step 3

In the Number field, enter the number that you want the
                                          			 system to dial when the user presses the speed dial button or the abbreviated
                                          			 dial index for abbreviated dial. You can enter digits 0 through 9, *, #, and +,
                                          			 which is the international escape character. To include dialing pauses in the
                                          			 speed dial, you can enter comma (,) which can act as a delimiter before sending
                                          			 DTMF digits. Each comma you include represents an additional pause of 2
                                          			 seconds. For example, two commas (,,) represent a pause of 4 seconds. Use of
                                          			 commas also allows you to separate FAC and CMC from the other digits in the
                                          			 speed dial string.

FAC must always precede CMC in the speed dial string.

A speed dial label is required for speed dials with FAC and DTMF digits.

Only one comma is allowed between FAC and CMC digits in the string.

Step 4

In the Label field, Enter the text that you want to display
                                          			 for the speed dial button or abbreviated dial number.

Step 5

(Optional) If you are configuring a pause in speed dial, you must add a label so that FAC, CMC, and DTMF digits are not displayed on
                                          the phone screen.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Generate a
                                          				report to identify devices that support the Speed Dial and Abbreviated Dial
                                          				feature. |
| Step 2 | Configure Speed Dial and Abbreviated Dial | Configure
                                          				Speed Dial and Abbreviated Dial numbers. |

| Note | Not all Cisco
                                          		  Unified IP Phones support abbreviated dialing. See the phone user guide for
                                          		  information. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . Enter your search criteria and click Find . Choose the phone for which you want to configure speed dial buttons. |
|---|---|
| Step 2 | From the Phone
                                             				Configuration window, choose Add/Update Speed Dials from the Related Links
                                          			 drop-down list at the top of the window and click Go . The Speed
                                             				Dial and Abbreviated Dial Configuration window appears for the
                                          			 phone. |
| Step 3 | In the Number field, enter the number that you want the
                                          			 system to dial when the user presses the speed dial button or the abbreviated
                                          			 dial index for abbreviated dial. You can enter digits 0 through 9, *, #, and +,
                                          			 which is the international escape character. To include dialing pauses in the
                                          			 speed dial, you can enter comma (,) which can act as a delimiter before sending
                                          			 DTMF digits. Each comma you include represents an additional pause of 2
                                          			 seconds. For example, two commas (,,) represent a pause of 4 seconds. Use of
                                          			 commas also allows you to separate FAC and CMC from the other digits in the
                                          			 speed dial string. Note Ensure that
                                                      				the following requirements are met when you include FAC and CMC in the speed
                                                      				dial string: FAC must always precede CMC in the speed dial string. A speed dial label is required for speed dials with FAC and DTMF digits. Only one comma is allowed between FAC and CMC digits in the string. | Note | Ensure that
                                                      				the following requirements are met when you include FAC and CMC in the speed
                                                      				dial string: FAC must always precede CMC in the speed dial string. A speed dial label is required for speed dials with FAC and DTMF digits. Only one comma is allowed between FAC and CMC digits in the string. |
| Note | Ensure that
                                                      				the following requirements are met when you include FAC and CMC in the speed
                                                      				dial string: FAC must always precede CMC in the speed dial string. A speed dial label is required for speed dials with FAC and DTMF digits. Only one comma is allowed between FAC and CMC digits in the string. |
| Step 4 | In the Label field, Enter the text that you want to display
                                          			 for the speed dial button or abbreviated dial number. Note This field
                                                      				is not available for all the phones. To determine whether this field is
                                                      				available for your Cisco Unified IP Phone, see the user documentation for your
                                                      				phone model. | Note | This field
                                                      				is not available for all the phones. To determine whether this field is
                                                      				available for your Cisco Unified IP Phone, see the user documentation for your
                                                      				phone model. |
| Note | This field
                                                      				is not available for all the phones. To determine whether this field is
                                                      				available for your Cisco Unified IP Phone, see the user documentation for your
                                                      				phone model. |
| Step 5 | (Optional) If you are configuring a pause in speed dial, you must add a label so that FAC, CMC, and DTMF digits are not displayed on
                                          the phone screen. |

| Note | Ensure that
                                                      				the following requirements are met when you include FAC and CMC in the speed
                                                      				dial string: FAC must always precede CMC in the speed dial string. A speed dial label is required for speed dials with FAC and DTMF digits. Only one comma is allowed between FAC and CMC digits in the string. |
|---|---|

| Note | This field
                                                      				is not available for all the phones. To determine whether this field is
                                                      				available for your Cisco Unified IP Phone, see the user documentation for your
                                                      				phone model. |
|---|---|