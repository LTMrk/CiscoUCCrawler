---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-1a4944cc07
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_m011be71_00_menu-support-for-2-10.html
retrieved_at: 2026-08-21T17:25:31.923022+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Menu Support for
	 2_Option_Menu Through 10_Option_Menu

## Chapter: Menu Support for
	 2_Option_Menu Through 10_Option_Menu

# Menu Support for
                     	 2_Option_Menu Through 10_Option_Menu

These voice
                                    				elements define menus that support from 2 to 10 options. The Menu voice
                                    				elements are similar to the Form voice element, however the number of choices
                                    				is fixed and all grammars are defined in the voice element itself.
                                    				Additionally, there is an exit state for each option, therefore the captured
                                    				value does not have to be analyzed afterwards to determine the next dialog in
                                    				the call flow. Use Menu elements when the situation defines a fixed number of
                                    				choices where each choice does something different in the call flow.

Because the
                                    				number of exit states is fixed for a voice element, there are separate voice
                                    				elements for Menu voice elements with 2 to10 options. For each additional
                                    				option, three additional settings are added to handle the spoken keyword, DTMF
                                    				entry, and interpretation value for each option. The audio groups and element
                                    				data saved are the same for all Menu voice elements.

Each option must
                                    				be assigned an interpretation value that the element will return as element
                                    				data named value when any of the keywords or DTMF key presses
                                    				assigned to that option are captured. The element variable ( value ) will contain
                                    				the same value regardless of the input mode (speech or DTMF).

The audio groups
                                    				are identical to those of the Form voice element. The done_audio_group group may be used for a message that
                                    				is to be played regardless of what option is chosen. If you require an option
                                    				specific message, use an Audio voice element after the particular choice is
                                    				made and do not configure a done_audio_group

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

noinput_timeout

(Noinput
                                          				  Timeout)

string

Yes

true

true

5s

The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s.

max_noinput_count

(Max NoInput
                                          				  Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during input capture. 0 = infinite noinputs
                                          				  allowed.

max_nomatch_count

(Max NoMatch
                                          				  Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of nomatch events allowed during input capture. 0 = infinite nomatches
                                          				  allowed.

confidence_level

(Confidence
                                          				  Level)

decimal (0.0
                                          				  to 1.0)

Yes

true

true

0.40

The confidence
                                          				  level threshold to use.

modal

(Disable
                                          				  Hotlinks)

boolean

Yes

true

true

false

Whether or not
                                          				  to temporarily disable all hotlink grammars (global or local) and universal
                                          				  grammars. If set to true, only the grammars of the current X_Option_Menu
                                          				  element will be enabled for the duration of the element. Otherwise all active
                                          				  grammars will be enabled.

optionX_dtmf

(Option X
                                          				  DTMF)

Character
                                          				  (0-9, #, *)

No

true

true

None

This setting
                                          				  defines the DTMF grammar that can be used to select the menu optionX . The valid format is a string separated with a
                                          				  semi-colon specifying two values in this order:

The
                                                						language context in which the current input should be included in the menu
                                                						grammar (optional). If omitted the language used will be the same as the
                                                						page-scoped language.

The dtmf
                                                						keypress or keypresses that is included in the menu DTMF grammar (required)

Sample
                                          				  configurations values are:

en-US;1

1

Additional optionX_dtmf settings may be used to define multiple
                                          				  dtmf keypresses corresponding to the same return value.

optionX_voice

(Option X
                                          				  Voice)

string

No

true

true

None

This setting
                                          				  defines the voice grammar that can be used to select the menu optionX . Each configuration of this setting specifies
                                          				  an option for the grammar. The valid format is a string separated with
                                          				  semi-colons specifying three values in this order:

The
                                                						language context in which the current input should be included in the menu
                                                						grammar (optional). If omitted the language used will be the same as the
                                                						page-scoped language.

exact or approximate (optional) for the accept attribute value, where
                                                						if exact , the spoken utterance must match the expected value
                                                						exactly; and where if approximate , the spoken utterance may match one of several
                                                						words

The
                                                						voice keyword or keywords (required) that is included in the menu voice
                                                						grammar.

If one of
                                          				  the optional parameters is defined, two semi-colons must be used, even if the
                                          				  other parameter is not used. Sample configuration values are:

en-US;exact;news report

;approximate;news report

fr-FR;;news report

news
                                                						report

Additional optionX_voice settings may be used to define multiple
                                          				  matching voice keywords corresponding to the same return value.

optionX_value

(Option X
                                          				  Value)

string

Yes

false

true

None

The value to
                                          				  be stored in the element data value for this voice element when the caller
                                          				  selects optionX .

Where X is 2
                                          				  – 10 as applicable.

Some voice
                                          				  browsers may not support menu options using * or #.

## Element Data

Name

Type

Notes

value

string

The value associated with the keyword or DTMF
                                          keypress inputted by the caller is stored in this
                                          variable.

value_confidence

float

This is the confidence
                                          value of the matched
                                          utterance.

## Exit States

Name

Notes

max_nomatch

The maximum
                                          				  number of nomatch events has occurred. If the max_nomatch_count is 0, this exit
                                          				  state will never occur.

max_noinput

The maximum
                                          				  number of noinput events has occurred. If the max_noinput_count is 0, this exit
                                          				  state will never occur.

optionX

The utterance
                                          				  or DTMF entry matched optionX.

Where X is 2 –
                                          				  10 as applicable.

## Audio Groups

### Menu Option Capture

Name
                                                (Label)

Req'd

Max1

Notes

initial_audio_group

(Initial)

Yes

Yes

Played when the voice
                                             element first begins.

nomatch_audio_group

(NoMatch)

No

No

Played when a nomatch event
                                             occurs.

noinput_audio_group

(NoInput)

No

No

Played when a noinput event
                                             occurs.

help_audio_group

(Help)

No

No

Played when the caller asked for help. If not
                                             specified, by default help is treated as a
                                             nomatch.

### End

Name
                                                (Label)

Req'd

Max 1

Notes

done_audio_group (Done)

No

Yes

Played when the voice element completes any of the
                                             option exit
                                             states.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Menu

com.audium.server.voiceElement.menu.MFoundationXOptionMenu

| These voice
                                    				elements define menus that support from 2 to 10 options. The Menu voice
                                    				elements are similar to the Form voice element, however the number of choices
                                    				is fixed and all grammars are defined in the voice element itself.
                                    				Additionally, there is an exit state for each option, therefore the captured
                                    				value does not have to be analyzed afterwards to determine the next dialog in
                                    				the call flow. Use Menu elements when the situation defines a fixed number of
                                    				choices where each choice does something different in the call flow. Because the
                                    				number of exit states is fixed for a voice element, there are separate voice
                                    				elements for Menu voice elements with 2 to10 options. For each additional
                                    				option, three additional settings are added to handle the spoken keyword, DTMF
                                    				entry, and interpretation value for each option. The audio groups and element
                                    				data saved are the same for all Menu voice elements. Each option must
                                    				be assigned an interpretation value that the element will return as element
                                    				data named value when any of the keywords or DTMF key presses
                                    				assigned to that option are captured. The element variable ( value ) will contain
                                    				the same value regardless of the input mode (speech or DTMF). The audio groups
                                    				are identical to those of the Form voice element. The done_audio_group group may be used for a message that
                                    				is to be played regardless of what option is chosen. If you require an option
                                    				specific message, use an Audio voice element after the particular choice is
                                    				made and do not configure a done_audio_group |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s. |
| max_noinput_count (Max NoInput
                                          				  Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during input capture. 0 = infinite noinputs
                                          				  allowed. |
| max_nomatch_count (Max NoMatch
                                          				  Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of nomatch events allowed during input capture. 0 = infinite nomatches
                                          				  allowed. |
| confidence_level (Confidence
                                          				  Level) | decimal (0.0
                                          				  to 1.0) | Yes | true | true | 0.40 | The confidence
                                          				  level threshold to use. |
| modal (Disable
                                          				  Hotlinks) | boolean | Yes | true | true | false | Whether or not
                                          				  to temporarily disable all hotlink grammars (global or local) and universal
                                          				  grammars. If set to true, only the grammars of the current X_Option_Menu
                                          				  element will be enabled for the duration of the element. Otherwise all active
                                          				  grammars will be enabled. |
| optionX_dtmf (Option X
                                          				  DTMF) | Character
                                          				  (0-9, #, *) | No | true | true | None | This setting
                                          				  defines the DTMF grammar that can be used to select the menu optionX . The valid format is a string separated with a
                                          				  semi-colon specifying two values in this order: The
                                                						language context in which the current input should be included in the menu
                                                						grammar (optional). If omitted the language used will be the same as the
                                                						page-scoped language. The dtmf
                                                						keypress or keypresses that is included in the menu DTMF grammar (required) Sample
                                          				  configurations values are: en-US;1 1 Additional optionX_dtmf settings may be used to define multiple
                                          				  dtmf keypresses corresponding to the same return value. Note At
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. Note Keypresses are currently limited to single digits. | Note | At
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. | Note | Keypresses are currently limited to single digits. |
| Note | At
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. |
| Note | Keypresses are currently limited to single digits. |
| optionX_voice (Option X
                                          				  Voice) | string | No | true | true | None | This setting
                                          				  defines the voice grammar that can be used to select the menu optionX . Each configuration of this setting specifies
                                          				  an option for the grammar. The valid format is a string separated with
                                          				  semi-colons specifying three values in this order: The
                                                						language context in which the current input should be included in the menu
                                                						grammar (optional). If omitted the language used will be the same as the
                                                						page-scoped language. exact or approximate (optional) for the accept attribute value, where
                                                						if exact , the spoken utterance must match the expected value
                                                						exactly; and where if approximate , the spoken utterance may match one of several
                                                						words The
                                                						voice keyword or keywords (required) that is included in the menu voice
                                                						grammar. If one of
                                          				  the optional parameters is defined, two semi-colons must be used, even if the
                                          				  other parameter is not used. Sample configuration values are: en-US;exact;news report ;approximate;news report fr-FR;;news report news
                                                						report Additional optionX_voice settings may be used to define multiple
                                          				  matching voice keywords corresponding to the same return value. Note At the
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. | Note | At the
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. |
| Note | At the
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. |
| optionX_value (Option X
                                          				  Value) | string | Yes | false | true | None | The value to
                                          				  be stored in the element data value for this voice element when the caller
                                          				  selects optionX . Note Only a
                                                   				  single value is allowed for each option. | Note | Only a
                                                   				  single value is allowed for each option. |
| Note | Only a
                                                   				  single value is allowed for each option. |

| Note | At
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. |
|---|---|

| Note | Keypresses are currently limited to single digits. |
|---|---|

| Note | At the
                                                   				  minimum, one of the two settings: optionX_dtmf or optionX_voice must be specified. |
|---|---|

| Note | Only a
                                                   				  single value is allowed for each option. |
|---|---|

| Where X is 2
                                          				  – 10 as applicable. Some voice
                                          				  browsers may not support menu options using * or #. |
|---|

| Name | Type | Notes |
|---|---|---|
| value | string | The value associated with the keyword or DTMF
                                          keypress inputted by the caller is stored in this
                                          variable. |
| value_confidence | float | This is the confidence
                                          value of the matched
                                          utterance. |

| Name | Notes |
|---|---|
| max_nomatch | The maximum
                                          				  number of nomatch events has occurred. If the max_nomatch_count is 0, this exit
                                          				  state will never occur. |
| max_noinput | The maximum
                                          				  number of noinput events has occurred. If the max_noinput_count is 0, this exit
                                          				  state will never occur. |
| optionX | The utterance
                                          				  or DTMF entry matched optionX. |

| Where X is 2 –
                                          				  10 as applicable. |
|---|

| Note Each option
                                                   				  can react on just a spoken keyword, just DTMF keypresses, or both, but at least
                                                   				  one method must be specified or an error will be reported. Note All options
                                                   				  in the menu must have a consistent input mode. For example, a menu cannot be
                                                   				  configured so that option 1 is chosen through both voice and DTMF but option 2
                                                   				  is chosen only through voice. Note There are
                                                   				  no menus with more than 10 options. In cases where more are needed, use a Form
                                                   				  voice element. | Note | Each option
                                                   				  can react on just a spoken keyword, just DTMF keypresses, or both, but at least
                                                   				  one method must be specified or an error will be reported. | Note | All options
                                                   				  in the menu must have a consistent input mode. For example, a menu cannot be
                                                   				  configured so that option 1 is chosen through both voice and DTMF but option 2
                                                   				  is chosen only through voice. | Note | There are
                                                   				  no menus with more than 10 options. In cases where more are needed, use a Form
                                                   				  voice element. |
|---|---|---|---|---|---|---|
| Note | Each option
                                                   				  can react on just a spoken keyword, just DTMF keypresses, or both, but at least
                                                   				  one method must be specified or an error will be reported. |
| Note | All options
                                                   				  in the menu must have a consistent input mode. For example, a menu cannot be
                                                   				  configured so that option 1 is chosen through both voice and DTMF but option 2
                                                   				  is chosen only through voice. |
| Note | There are
                                                   				  no menus with more than 10 options. In cases where more are needed, use a Form
                                                   				  voice element. |

| Note | Each option
                                                   				  can react on just a spoken keyword, just DTMF keypresses, or both, but at least
                                                   				  one method must be specified or an error will be reported. |
|---|---|

| Note | All options
                                                   				  in the menu must have a consistent input mode. For example, a menu cannot be
                                                   				  configured so that option 1 is chosen through both voice and DTMF but option 2
                                                   				  is chosen only through voice. |
|---|---|

| Note | There are
                                                   				  no menus with more than 10 options. In cases where more are needed, use a Form
                                                   				  voice element. |
|---|---|

| Name
                                                (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| nomatch_audio_group (NoMatch) | No | No | Played when a nomatch event
                                             occurs. |
| noinput_audio_group (NoInput) | No | No | Played when a noinput event
                                             occurs. |
| help_audio_group (Help) | No | No | Played when the caller asked for help. If not
                                             specified, by default help is treated as a
                                             nomatch. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| done_audio_group (Done) | No | Yes | Played when the voice element completes any of the
                                             option exit
                                             states. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Menu | com.audium.server.voiceElement.menu.MFoundationXOptionMenu |