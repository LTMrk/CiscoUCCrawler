---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-user-guide-assistant-b-15cucugasst-b-15cucugasst-chapter-0110--e767db7353
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/assistant/b_15cucugasst/b_15cucugasst_chapter_0110.html
retrieved_at: 2026-08-17T03:34:58.374326+00:00
---

User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 15)

# User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 15)

Updated: December 18, 2023

Chapter: Changing Your Call Transfer and Screening Preferences

## Chapter: Changing Your Call Transfer and Screening Preferences

# Changing Your Call Transfer and Screening Preferences

## About Call Transfer Rules

Call transfer rules control how Cisco Unity Connection handles incoming indirect calls, which are from callers who do not
                           dial you directly (for example, callers who use the directory to reach you). For direct calls—when outside callers or other
                           users dial your personal phone number to reach you—your Connection transfer settings do not apply.

You can choose to answer indirect calls, or you can have indirect calls routed immediately to voicemail.

Tip

To set up call transfers for direct calls to your extension, talk to your Connection administrator. Your desk phone or even
                                       the phone system that your organization uses may offer transfer features that you can use to manage direct calls.

The three basic transfer rules and how they work are described below. Note that Connection follows the basic transfer rule
                           that you enable for the applicable situation, while some transfer rules override other rules when they are enabled.

Standard Transfer Rule

This basic transfer rule applies during the work hours that your Cisco Unity Connection administrator specified for your organization,
                           or in other situations when no other transfer rule is enabled. By design, the standard transfer rule cannot be disabled.

Alternate Transfer Rule

Enable this basic transfer rule to apply during a specific time period when you want to override the other transfer rules.
                           For example, you may want to route all your calls directly to voicemail while you are out of the office or you may want to
                           transfer your calls to a different extension if you are temporarily working from another location. As long as it is enabled,
                           the alternate transfer rule overrides all other transfer rules.

Closed Transfer Rule

Enable this basic transfer rule when you want Connection to perform different transfer actions during the nonwork hours that
                           your Connection administrator specified for your organization. (For example, you may want to route all your calls directly
                           to voicemail during nonwork hours.) As long as it is enabled, the closed transfer rule overrides the standard transfer rule
                           during nonbusiness hours.

## Changing Your Call Transfer Preferences

Call transfer preferences allow you to choose to have indirect calls ring your extension or ring another extension or phone
                              number that you specify, or to be transferred directly to voicemail so your phone does not ring at all. When you send calls
                              to voicemail, callers do not have to wait while your phone rings unanswered; your greeting plays immediately.

Step 1

In the Messaging Assistant, from the Preferences menu, select Transfer and Screening .

Step 2

In the Transfer Rule table, choose the basic transfer rule whose settings you want to change.

Step 3

If the When This Basic Rule Is Active field is displayed at the top of page, choose the applicable option:

Connection applies the settings on this page when this basic transfer rule is active.

Connection ignores the settings on this page and applies personal call transfer rules when this basic transfer rule is active.

This option is available only if you have access to the Personal Call Transfer Rules web tool.

When using this option, first configure your personal call transfer rule sets in the Personal Call Transfer Rules web tool.
                                                   If no rule sets are configured, all calls will be transferred to your primary extension.

Step 4

In the Status field, choose whether the rule is disabled, enabled, or enabled with an end date and time. Note that the standard
                                       transfer rule cannot be disabled.

Step 5

In the Transfer Calls To field, choose the applicable destination for calls:

Calls are transferred to your extension.

Calls are transferred to the number you enter in the text box. (To transfer calls to an external phone number, such as a home
                                                   or mobile phone, contact your Connection administrator.)

Calls are transferred to voicemail without ringing a phone.

Tip

As a convenience, you can edit the transfer number in the text box even when you have specified that Connection transfer calls
                                                      to your extension or to voicemail. Connection transfers calls to the number in the text box only when the radio button next
                                                      to it is selected.

Step 6

Select Save .

## Changing Your Call Holding Preferences

When a basic transfer rule is configured to answer indirect calls at your extension, you can indicate how you want Cisco Unity
                              Connection to handle the calls when your phone is busy.

Step 1

In the Messaging Assistant, from the Preferences menu, select Transfer and Screening .

Step 2

In the Transfer Rule table, select the basic transfer rule whose settings you want to change.

Step 3

In the Transfer Calls To field, select Extension <Your Extension> .

Step 4

In the If My Extension Is Busy list, select how you want Connection to handle calls when your extension is busy:

Connection plays your greeting, then prompts the caller to leave a message.

Connection puts the caller on hold and does not offer the option of leaving a message.

Connection gives the caller the option of holding or leaving a message.

Step 5

Select Save .

## Changing Your Call Screening Preferences

You can choose to have Cisco Unity Connection screen indirect calls. Connection can ask for the name of the caller and play
                              the name for you before connecting the call. It can also tell you when it connects the call, or give you the option of taking
                              an indirect call or routing it to voicemail for the caller to leave a message.

Step 1

In the Messaging Assistant, from the Preferences menu, select Transfer and Screening .

Step 2

In the Transfer Rule table, select the basic transfer rule whose settings you want to change.

Step 3

In the Screen Calls section, check one or more check boxes to set your screening options:

Connection tells you when it connects the call.

Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone.

Connection asks if you want to take the call or have the caller leave a message.

Connection records the name of the caller and plays it for you before connecting the call.

Note the following considerations:

For the option of declining a call for someone with whom you share a phone, check both the Tell Me Who the Call Is For and the Ask Me If I Want to Take the Call check boxes.

For the option of accepting or declining a call based on the identity of the caller, check both the Ask Me If I Want to Take the Call and the Ask For Caller’s Name check boxes.

When you accept, Connection connects the call. When you decline, Connection routes the call to voicemail.

Step 4

Select Save .

## Changing Your Caller Message Preferences

Caller message preferences allow you to choose what callers can do when they leave messages for you.

Step 1

In the Messaging Assistant, from the Preferences menu, select Transfer and Screening .

Step 2

Check or uncheck the check boxes for one or both of the following options, as applicable:

Connection gives callers the options of listening to, adding to, rerecording, or deleting their messages.

Connection asks callers if they want to mark their messages urgent.

Step 3

Select Save .

| Tip | To set up call transfers for direct calls to your extension, talk to your Connection administrator. Your desk phone or even
                                       the phone system that your organization uses may offer transfer features that you can use to manage direct calls. |
|---|---|

| Step 1 | In the Messaging Assistant, from the Preferences menu, select Transfer and Screening . |
|---|---|
| Step 2 | In the Transfer Rule table, choose the basic transfer rule whose settings you want to change. |
| Step 3 | If the When This Basic Rule Is Active field is displayed at the top of page, choose the applicable option: Option Description Apply Basic Settings on This Page Connection applies the settings on this page when this basic transfer rule is active. Apply Personal Call Transfer Rules Connection ignores the settings on this page and applies personal call transfer rules when this basic transfer rule is active. Note This option is available only if you have access to the Personal Call Transfer Rules web tool. When using this option, first configure your personal call transfer rule sets in the Personal Call Transfer Rules web tool.
                                                   If no rule sets are configured, all calls will be transferred to your primary extension. | Option | Description | Apply Basic Settings on This Page | Connection applies the settings on this page when this basic transfer rule is active. | Apply Personal Call Transfer Rules | Connection ignores the settings on this page and applies personal call transfer rules when this basic transfer rule is active. Note This option is available only if you have access to the Personal Call Transfer Rules web tool. When using this option, first configure your personal call transfer rule sets in the Personal Call Transfer Rules web tool.
                                                   If no rule sets are configured, all calls will be transferred to your primary extension. | Note | This option is available only if you have access to the Personal Call Transfer Rules web tool. |
| Option | Description |
| Apply Basic Settings on This Page | Connection applies the settings on this page when this basic transfer rule is active. |
| Apply Personal Call Transfer Rules | Connection ignores the settings on this page and applies personal call transfer rules when this basic transfer rule is active. Note This option is available only if you have access to the Personal Call Transfer Rules web tool. When using this option, first configure your personal call transfer rule sets in the Personal Call Transfer Rules web tool.
                                                   If no rule sets are configured, all calls will be transferred to your primary extension. | Note | This option is available only if you have access to the Personal Call Transfer Rules web tool. |
| Note | This option is available only if you have access to the Personal Call Transfer Rules web tool. |
| Step 4 | In the Status field, choose whether the rule is disabled, enabled, or enabled with an end date and time. Note that the standard
                                       transfer rule cannot be disabled. |
| Step 5 | In the Transfer Calls To field, choose the applicable destination for calls: Option Description Extension <Your Extension> Calls are transferred to your extension. Another Number Calls are transferred to the number you enter in the text box. (To transfer calls to an external phone number, such as a home
                                                   or mobile phone, contact your Connection administrator.) My Personal Greeting Calls are transferred to voicemail without ringing a phone. Tip As a convenience, you can edit the transfer number in the text box even when you have specified that Connection transfer calls
                                                      to your extension or to voicemail. Connection transfers calls to the number in the text box only when the radio button next
                                                      to it is selected. | Option | Description | Extension <Your Extension> | Calls are transferred to your extension. | Another Number | Calls are transferred to the number you enter in the text box. (To transfer calls to an external phone number, such as a home
                                                   or mobile phone, contact your Connection administrator.) | My Personal Greeting | Calls are transferred to voicemail without ringing a phone. | Tip | As a convenience, you can edit the transfer number in the text box even when you have specified that Connection transfer calls
                                                      to your extension or to voicemail. Connection transfers calls to the number in the text box only when the radio button next
                                                      to it is selected. |
| Option | Description |
| Extension <Your Extension> | Calls are transferred to your extension. |
| Another Number | Calls are transferred to the number you enter in the text box. (To transfer calls to an external phone number, such as a home
                                                   or mobile phone, contact your Connection administrator.) |
| My Personal Greeting | Calls are transferred to voicemail without ringing a phone. |
| Tip | As a convenience, you can edit the transfer number in the text box even when you have specified that Connection transfer calls
                                                      to your extension or to voicemail. Connection transfers calls to the number in the text box only when the radio button next
                                                      to it is selected. |
| Step 6 | Select Save . |

| Option | Description |
|---|---|
| Apply Basic Settings on This Page | Connection applies the settings on this page when this basic transfer rule is active. |
| Apply Personal Call Transfer Rules | Connection ignores the settings on this page and applies personal call transfer rules when this basic transfer rule is active. Note This option is available only if you have access to the Personal Call Transfer Rules web tool. When using this option, first configure your personal call transfer rule sets in the Personal Call Transfer Rules web tool.
                                                   If no rule sets are configured, all calls will be transferred to your primary extension. | Note | This option is available only if you have access to the Personal Call Transfer Rules web tool. |
| Note | This option is available only if you have access to the Personal Call Transfer Rules web tool. |

| Note | This option is available only if you have access to the Personal Call Transfer Rules web tool. |
|---|---|

| Option | Description |
|---|---|
| Extension <Your Extension> | Calls are transferred to your extension. |
| Another Number | Calls are transferred to the number you enter in the text box. (To transfer calls to an external phone number, such as a home
                                                   or mobile phone, contact your Connection administrator.) |
| My Personal Greeting | Calls are transferred to voicemail without ringing a phone. |

| Tip | As a convenience, you can edit the transfer number in the text box even when you have specified that Connection transfer calls
                                                      to your extension or to voicemail. Connection transfers calls to the number in the text box only when the radio button next
                                                      to it is selected. |
|---|---|

| Step 1 | In the Messaging Assistant, from the Preferences menu, select Transfer and Screening . |
|---|---|
| Step 2 | In the Transfer Rule table, select the basic transfer rule whose settings you want to change. |
| Step 3 | In the Transfer Calls To field, select Extension <Your Extension> . |
| Step 4 | In the If My Extension Is Busy list, select how you want Connection to handle calls when your extension is busy: Option Description Send Callers to Voicemail Connection plays your greeting, then prompts the caller to leave a message. Put Callers on Hold Without Asking Connection puts the caller on hold and does not offer the option of leaving a message. Ask Callers to Hold Connection gives the caller the option of holding or leaving a message. | Option | Description | Send Callers to Voicemail | Connection plays your greeting, then prompts the caller to leave a message. | Put Callers on Hold Without Asking | Connection puts the caller on hold and does not offer the option of leaving a message. | Ask Callers to Hold | Connection gives the caller the option of holding or leaving a message. |
| Option | Description |
| Send Callers to Voicemail | Connection plays your greeting, then prompts the caller to leave a message. |
| Put Callers on Hold Without Asking | Connection puts the caller on hold and does not offer the option of leaving a message. |
| Ask Callers to Hold | Connection gives the caller the option of holding or leaving a message. |
| Step 5 | Select Save . |

| Option | Description |
|---|---|
| Send Callers to Voicemail | Connection plays your greeting, then prompts the caller to leave a message. |
| Put Callers on Hold Without Asking | Connection puts the caller on hold and does not offer the option of leaving a message. |
| Ask Callers to Hold | Connection gives the caller the option of holding or leaving a message. |

| Step 1 | In the Messaging Assistant, from the Preferences menu, select Transfer and Screening . |
|---|---|
| Step 2 | In the Transfer Rule table, select the basic transfer rule whose settings you want to change. |
| Step 3 | In the Screen Calls section, check one or more check boxes to set your screening options: Option Description Tell Me When the Call Is Connected Connection tells you when it connects the call. Tell Me Who the Call Is For Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. Ask Me If I Want to Take the Call Connection asks if you want to take the call or have the caller leave a message. Ask for Caller's Name Connection records the name of the caller and plays it for you before connecting the call. Note the following considerations: For the option of declining a call for someone with whom you share a phone, check both the Tell Me Who the Call Is For and the Ask Me If I Want to Take the Call check boxes. For the option of accepting or declining a call based on the identity of the caller, check both the Ask Me If I Want to Take the Call and the Ask For Caller’s Name check boxes. When you accept, Connection connects the call. When you decline, Connection routes the call to voicemail. | Option | Description | Tell Me When the Call Is Connected | Connection tells you when it connects the call. | Tell Me Who the Call Is For | Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. | Ask Me If I Want to Take the Call | Connection asks if you want to take the call or have the caller leave a message. | Ask for Caller's Name | Connection records the name of the caller and plays it for you before connecting the call. |
| Option | Description |
| Tell Me When the Call Is Connected | Connection tells you when it connects the call. |
| Tell Me Who the Call Is For | Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. |
| Ask Me If I Want to Take the Call | Connection asks if you want to take the call or have the caller leave a message. |
| Ask for Caller's Name | Connection records the name of the caller and plays it for you before connecting the call. |
| Step 4 | Select Save . |

| Option | Description |
|---|---|
| Tell Me When the Call Is Connected | Connection tells you when it connects the call. |
| Tell Me Who the Call Is For | Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. |
| Ask Me If I Want to Take the Call | Connection asks if you want to take the call or have the caller leave a message. |
| Ask for Caller's Name | Connection records the name of the caller and plays it for you before connecting the call. |

| Step 1 | In the Messaging Assistant, from the Preferences menu, select Transfer and Screening . |
|---|---|
| Step 2 | Check or uncheck the check boxes for one or both of the following options, as applicable: Option Description Listen To and Rerecord the Message Connection gives callers the options of listening to, adding to, rerecording, or deleting their messages. Mark the Message as Urgent Connection asks callers if they want to mark their messages urgent. | Option | Description | Listen To and Rerecord the Message | Connection gives callers the options of listening to, adding to, rerecording, or deleting their messages. | Mark the Message as Urgent | Connection asks callers if they want to mark their messages urgent. |
| Option | Description |
| Listen To and Rerecord the Message | Connection gives callers the options of listening to, adding to, rerecording, or deleting their messages. |
| Mark the Message as Urgent | Connection asks callers if they want to mark their messages urgent. |
| Step 3 | Select Save . |

| Option | Description |
|---|---|
| Listen To and Rerecord the Message | Connection gives callers the options of listening to, adding to, rerecording, or deleting their messages. |
| Mark the Message as Urgent | Connection asks callers if they want to mark their messages urgent. |