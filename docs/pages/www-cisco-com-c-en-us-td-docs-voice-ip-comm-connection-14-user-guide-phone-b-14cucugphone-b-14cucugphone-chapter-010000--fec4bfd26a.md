---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-user-guide-phone-b-14cucugphone-b-14cucugphone-chapter-010000--fec4bfd26a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone/b_14cucugphone_chapter_010000.html
retrieved_at: 2026-08-21T00:35:29.865106+00:00
---

User Guide for the Cisco Unity Connection Phone Interface (Release 14)

# User Guide for the Cisco Unity Connection Phone Interface (Release 14)

Updated: March 31, 2021

Chapter: Managing Personal Call Transfer Rule Sets to Handle Incoming Calls

## Chapter: Managing Personal Call Transfer Rule Sets to Handle Incoming Calls

# Managing Personal Call Transfer Rule Sets to Handle Incoming Calls

## About Personal Call Transfer Rule Sets

You set up personal call transfer rule sets so that Cisco Unity Connection transfers particular calls to you according to
                           caller identity, time of day, and your meeting schedule, or transfers your calls to voicemail or to another phone number.
                           Personal call transfer rules are more advanced than the basic transfer rules—standard, alternate, and closed—which allow you
                           to configure basic transfer settings.

You manage your personal call transfer rule sets in the Personal Call Transfer Rules web tool. Once rule sets have been defined,
                           you can enable them in the web tool or by phone. (For more information on how you use and manage personal call transfer rule
                           sets, see the User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool .)

## Enabling and Disabling the Use of Personal Call Transfer Rule Sets by Basic Transfer Rules

Cisco Unity Connection uses personal call transfer rules to process your calls only when the active basic rule—standard, alternate
                           or closed—is configured to apply personal call transfer rules instead of the basic settings.

### Enabling or Disabling the Use of Personal Call Transfer Rule Sets by a Basic Transfer Rule by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings .

Select the standard, alternate, or closed transfer rule.

After Connection announces your current transfer settings, follow the prompts to enable or disable personal call transfer
                                          rules.

Repeat Step 3 and Step 4 for each basic transfer rule, as applicable.

### Enabling or Disabling the Use of Personal Call Transfer Rule Sets by a Basic Transfer Rule by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do" say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings .

Select the standard, alternate, or closed transfer rule.

After Connection announces your current transfer settings, follow the prompts to enable or disable personal call transfer
                                          rules.

Repeat Step 4 and Step 5 for each basic transfer rule, as applicable.

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

## Enabling and Disabling the Use of Personal Call Transfer Rule Sets

Enabling means that Connection uses your personal call transfer rule sets to process calls if your basic transfer rules—the
                           standard, alternate or closed transfer rule—are configured to apply personal call transfer rules instead of the basic settings.
                           Disabling means that Connection does not use personal call transfer rule sets to process calls even if your basic transfer
                           rules are configured to apply personal call transfer rules. In that case, calls will be transferred to your extension.

### Enabling or Disabling the Use of Personal Call Transfer Rule Sets by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules .

To enable, select the option to turn call routing rules on after Connection tells you that they are off.

To disable, select the option Turn Call Routing Rules Off .

### Enabling or Disabling the Use of Personal Call Transfer Rule Sets by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules .

To enable, select the option to turn call routing rules on after Connection tells you that they are off.

To disable, select the option Turn Call Routing Rules Off .

## Enabling and Disabling Individual Rule Sets

You can enable only one rule set at a time by phone, and the rule set becomes active immediately. Cisco Unity Connection plays
                           the enable prompt only when you have a rule set that is disabled.

Disabling a rule set means making it ineligible to be active. Connection plays the disable prompt only when you have a rule
                           set that is enabled but not active.

When no rule sets are defined or active, calls are transferred to your extension.

### Enabling a Rule Set by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules .

Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use.

Select the option Enable a Transfer Rule Set .

Follow the prompts to activate a rule set and to set the number of days you want the rule set to be active.

### Enabling a Rule Set by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules .

Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use.

Select the option Enable a Transfer Rule Set .

Follow the prompts to activate a rule set and to set the number of days you want the rule set to be active.

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

### Disabling a Rule Set by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , then Personal Call Transfer Rules , and Disable a Transfer Rule Set .

Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active.

Follow the prompts to disable the rule set.

### Disabling a Rule Set by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules , and Disable a Transfer Rule Set .

Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active.

Follow the prompts to disable the rule set.

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

## Using the Transfer All Rule Set

The Transfer All rule set contains a single rule that forwards all of your calls to a specific destination for a specified
                           time. Transfer All is the only rule set that you must set by phone. Cisco Unity Connection activates the rule set and displays
                           it on the Call Transfer Rule Sets page of the Personal Call Transfer Rules web tool.

When you enable Transfer All, it immediately becomes your active rule set for the duration specified. If a transferred call
                           is not answered at the Transfer All destination, Connection transfers the call to voicemail.

### Enabling the Transfer All Rule Set by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules .

Follow the prompts to transfer all calls to voicemail or to a specific phone number, and to set the number of days you want
                                          the Transfer All rule set to be active.

A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration.

### Enabling the Transfer All Rule Set by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules .

Follow the prompts to transfer all calls to voicemail or to a specific phone number, and to set the number of days you want
                                          the Transfer All rule set to be active.

A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration.

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

### Disabling the Transfer All Rule Set by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , then Personal Call Transfer Rules , and Cancel Transferring All Calls to This Destination .

### Disabling the Transfer All Rule Set by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules , and Cancel Transferring All Calls to This Destination .

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

## Forwarding All Calls to Cisco Unity Connection

You can forward all your incoming calls to Cisco Unity Connection so that your personal call transfer rule sets are applied
                           to calls immediately. With this option, the phone system does not ring your extension first before applying personal call
                           transfer rule sets to locate you when there is no answer.

### Forwarding All Calls to Cisco Unity Connection by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules .

Follow the prompts to forward all calls to Connection, and to set the number of days you want the forwarding to be active.

A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration.

### Forwarding All Calls to Cisco Unity Connection by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

"Setup Options." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules .

Follow the prompts to forward all calls to Connection, and to set the number of days you want the forwarding to be active.

A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration.

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

### Canceling Forwarding of All Calls to Cisco Unity Connection by Using the Phone Keypad

Call and sign in to Connection.

At the Main menu, select the option Setup Options , then Transfer Settings , then Personal Call Transfer Rules , and Cancel Forwarding All Calls to Cisco Unity Connection .

### Canceling Forwarding of All Calls to Cisco Unity Connection by Using Voice Commands

Call and sign in to Connection.

When Connection asks, "What do you want to do," say:

" Setup Options ." (Connection temporarily switches to the phone keypad.)

On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules , and Cancel Forwarding All Calls to Cisco Unity Connection .

To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt.

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings . |
| Step 3 | Select the standard, alternate, or closed transfer rule. |
| Step 4 | After Connection announces your current transfer settings, follow the prompts to enable or disable personal call transfer
                                          rules. |
| Step 5 | Repeat Step 3 and Step 4 for each basic transfer rule, as applicable. |

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do" say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings . |
| Step 4 | Select the standard, alternate, or closed transfer rule. |
| Step 5 | After Connection announces your current transfer settings, follow the prompts to enable or disable personal call transfer
                                          rules. |
| Step 6 | Repeat Step 4 and Step 5 for each basic transfer rule, as applicable. Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules . |
| Step 3 | To enable, select the option to turn call routing rules on after Connection tells you that they are off. To disable, select the option Turn Call Routing Rules Off . |

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules . |
| Step 4 | To enable, select the option to turn call routing rules on after Connection tells you that they are off. To disable, select the option Turn Call Routing Rules Off . |

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules . Note Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. | Note | Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. |
| Note | Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. |
| Step 3 | Select the option Enable a Transfer Rule Set . |
| Step 4 | Follow the prompts to activate a rule set and to set the number of days you want the rule set to be active. |

| Note | Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules . Note Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. | Note | Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. |
| Note | Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. |
| Step 4 | Select the option Enable a Transfer Rule Set . |
| Step 5 | Follow the prompts to activate a rule set and to set the number of days you want the rule set to be active. Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Note | Connection plays the prompt to enable a rule set only when personal call transfer rule sets are enabled for use. |
|---|---|

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , then Personal Call Transfer Rules , and Disable a Transfer Rule Set . Note Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. | Note | Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. |
| Note | Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. |
| Step 3 | Follow the prompts to disable the rule set. |

| Note | Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules , and Disable a Transfer Rule Set . Note Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. | Note | Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. |
| Note | Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. |
| Step 4 | Follow the prompts to disable the rule set. Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Note | Connection plays the prompt to disable a rule set only when there is a rule set that is enabled but not active. |
|---|---|

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules . |
| Step 3 | Follow the prompts to transfer all calls to voicemail or to a specific phone number, and to set the number of days you want
                                          the Transfer All rule set to be active. Tip A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. | Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |

| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules . |
| Step 4 | Follow the prompts to transfer all calls to voicemail or to a specific phone number, and to set the number of days you want
                                          the Transfer All rule set to be active. Tip A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
|---|---|

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , then Personal Call Transfer Rules , and Cancel Transferring All Calls to This Destination . |

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules , and Cancel Transferring All Calls to This Destination . Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , and Personal Call Transfer Rules . |
| Step 3 | Follow the prompts to forward all calls to Connection, and to set the number of days you want the forwarding to be active. Tip A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. | Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |

| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: "Setup Options." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules . |
| Step 4 | Follow the prompts to forward all calls to Connection, and to set the number of days you want the forwarding to be active. Tip A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Tip | A day ends at 11:59 p.m., so a duration of one day means until the end of the current day (11:59 p.m.), two days is through
                                                         the end of tomorrow, and so on. You can enter from 1-999 days for duration. |
|---|---|

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | At the Main menu, select the option Setup Options , then Transfer Settings , then Personal Call Transfer Rules , and Cancel Forwarding All Calls to Cisco Unity Connection . |

| Step 1 | Call and sign in to Connection. |
|---|---|
| Step 2 | When Connection asks, "What do you want to do," say: " Setup Options ." (Connection temporarily switches to the phone keypad.) |
| Step 3 | On the phone keypad, select the option Transfer Settings , then Personal Call Transfer Rules , and Cancel Forwarding All Calls to Cisco Unity Connection . Tip To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. | Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |

| Tip | To switch back to using voice commands, keep pressing * until you hear the "Voice Command Conversation" prompt. |
|---|---|