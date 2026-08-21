---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-user-guide-pctr-b-14cucugpctr-b-14cucugpctr-chapter-0100-html-a2c4293774
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/pctr/b_14cucugpctr/b_14cucugpctr_chapter_0100.html
retrieved_at: 2026-08-21T00:34:13.433275+00:00
---

User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 14)

# User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 14)

Updated: March 31, 2021

Chapter: Changing Your Preferences

## Chapter: Changing Your Preferences

- Changing Your Preferences

- Changing Your Rule-Processing Preferences

- Changing Your Call Holding and Call Screening Preferences

# Changing Your Preferences

## Changing Your Rule-Processing Preferences

You can enable and disable the processing of personal call transfer rules, and you can choose whether to have Cisco Unity
                              Connection always ring the dialed extension first, before processing any active personal rules.

If you choose not to have Connection ring the dialed extension first, direct- and indirect-call behavior is different:

Direct calls are those that dial your phone directly—for example when another Connection user dials your extension or when
                              an outside caller dials your direct line, if you have one. Indirect calls are those that are routed to you from the Connection
                              system, for example, from callers using the directory to reach you.

In the Personal Call Transfer Rules web tool, from the Preferences menu, select Rules Settings .

Check one of the following check boxes, as applicable:

When checked, all personal call transfer rule sets are disabled and are not considered by Connection when processing incoming
                                                   calls. Incoming calls are routed to the dialed extension.

Existing rule sets are not deleted when the sets are disabled.

When checked, Connection rings the primary extension first before applying any rule sets, regardless of whether the incoming
                                                   call is a direct or indirect call.

If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations.

If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection.

Select Save .

## Changing Your Call Holding and Call Screening Preferences

When a transfer rule is configured to transfer calls to your primary extension, you can indicate how you want Cisco Unity
                              Connection to handle the calls when your phone is busy.

In addition, if your Connection administrator has enabled screening options for you, you can choose to have Cisco Unity Connection
                              screen calls. Connection can ask for the name of the caller and play the name for you before connecting the call. It can also
                              tell you when it connects the call, or give you the option of taking a call or transferring it to voicemail for the caller
                              to leave a message. Each personal call transfer rule can be configured whether or not to screen calls that meet the rules
                              criteria.

If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                          any call screening options that are enabled. If you do not want such calls to be screened, use wildcard characters to create
                                          a rule that will match all calls and order it as the last rule in the rule set.

In the Personal Call Transfer Rules web tool, from the Preferences menu, select Call Holding and Screening .

To change your call holding preferences, in the If My Extension Is Busy list, select how you want Connection to handle calls
                                       when your extension is busy:

Connection plays your greeting, then prompts the caller to leave a message.

Connection puts the caller on hold and does not offer the option of leaving a message.

Connection gives the caller the option of holding or leaving a message.

To change your call screening preferences, in the Screen Calls section, check one or more check boxes, as applicable:

Connection tells you when it connects the call.

Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone.

Connection asks if you want to take the call or have the caller leave a message.

Connection records the name of the caller and plays it for you before connecting the call.

Note the following considerations:

For the option of declining a call for someone with whom you share a phone, check both the Tell Me Who the Call Is For and the Ask Me If I Want to Take the Call check boxes.

For the option of accepting or declining a call based on the identity of the caller, check both the Ask Me If I Want to Take the Call and the Ask For Caller’s Name check boxes.

When you accept, Connection connects the call. When you decline, Connection forwards the call to voicemail.

Select Save .

| Direct calls | These calls ring the extension. If there is no answer, the call is routed to Connection, where personal call transfer rules
                                       are applied. |
|---|---|
| Indirect calls | These calls are routed through Connection, and personal call transfer rules are applied without ringing the extension. |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Preferences menu, select Rules Settings . |
|---|---|
| Step 2 | Check one of the following check boxes, as applicable: Option Description Disable All Processing of Personal Call Transfer Rules When checked, all personal call transfer rule sets are disabled and are not considered by Connection when processing incoming
                                                   calls. Incoming calls are routed to the dialed extension. Note Existing rule sets are not deleted when the sets are disabled. Always Ring Primary Extension Before Applying Personal Call Transfer Rules When checked, Connection rings the primary extension first before applying any rule sets, regardless of whether the incoming
                                                   call is a direct or indirect call. Tip If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. | Option | Description | Disable All Processing of Personal Call Transfer Rules | When checked, all personal call transfer rule sets are disabled and are not considered by Connection when processing incoming
                                                   calls. Incoming calls are routed to the dialed extension. Note Existing rule sets are not deleted when the sets are disabled. | Note | Existing rule sets are not deleted when the sets are disabled. | Always Ring Primary Extension Before Applying Personal Call Transfer Rules | When checked, Connection rings the primary extension first before applying any rule sets, regardless of whether the incoming
                                                   call is a direct or indirect call. Tip If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. | Tip | If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. |
| Option | Description |
| Disable All Processing of Personal Call Transfer Rules | When checked, all personal call transfer rule sets are disabled and are not considered by Connection when processing incoming
                                                   calls. Incoming calls are routed to the dialed extension. Note Existing rule sets are not deleted when the sets are disabled. | Note | Existing rule sets are not deleted when the sets are disabled. |
| Note | Existing rule sets are not deleted when the sets are disabled. |
| Always Ring Primary Extension Before Applying Personal Call Transfer Rules | When checked, Connection rings the primary extension first before applying any rule sets, regardless of whether the incoming
                                                   call is a direct or indirect call. Tip If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. | Tip | If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. |
| Tip | If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. |
| Step 3 | Select Save . |

| Option | Description |
|---|---|
| Disable All Processing of Personal Call Transfer Rules | When checked, all personal call transfer rule sets are disabled and are not considered by Connection when processing incoming
                                                   calls. Incoming calls are routed to the dialed extension. Note Existing rule sets are not deleted when the sets are disabled. | Note | Existing rule sets are not deleted when the sets are disabled. |
| Note | Existing rule sets are not deleted when the sets are disabled. |
| Always Ring Primary Extension Before Applying Personal Call Transfer Rules | When checked, Connection rings the primary extension first before applying any rule sets, regardless of whether the incoming
                                                   call is a direct or indirect call. Tip If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. | Tip | If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. |
| Tip | If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. |

| Note | Existing rule sets are not deleted when the sets are disabled. |
|---|---|

| Tip | If your phone is set to Call Forward Answer, check this check box to achieve consistent behavior when callers dial you directly
                                                               and when callers dial your number through Connection. Your primary extension will always ring before Connection tries to locate
                                                               you at other destinations. If you do not want your primary extension to ring at all, uncheck this check box and set the Call Forward Answer setting on
                                                               your phone to Cisco Unity Connection. |
|---|---|

| Tip | If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                          any call screening options that are enabled. If you do not want such calls to be screened, use wildcard characters to create
                                          a rule that will match all calls and order it as the last rule in the rule set. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Preferences menu, select Call Holding and Screening . |
|---|---|
| Step 2 | To change your call holding preferences, in the If My Extension Is Busy list, select how you want Connection to handle calls
                                       when your extension is busy: Option Description Send Callers to Voicemail Connection plays your greeting, then prompts the caller to leave a message. Put Callers on Hold Without Asking Connection puts the caller on hold and does not offer the option of leaving a message. Ask Callers to Hold Connection gives the caller the option of holding or leaving a message. | Option | Description | Send Callers to Voicemail | Connection plays your greeting, then prompts the caller to leave a message. | Put Callers on Hold Without Asking | Connection puts the caller on hold and does not offer the option of leaving a message. | Ask Callers to Hold | Connection gives the caller the option of holding or leaving a message. |
| Option | Description |
| Send Callers to Voicemail | Connection plays your greeting, then prompts the caller to leave a message. |
| Put Callers on Hold Without Asking | Connection puts the caller on hold and does not offer the option of leaving a message. |
| Ask Callers to Hold | Connection gives the caller the option of holding or leaving a message. |
| Step 3 | To change your call screening preferences, in the Screen Calls section, check one or more check boxes, as applicable: Option Description Tell Me When the Call Is Connected Connection tells you when it connects the call. Tell Me Who The Call Is For Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. Ask Me If I Want to Take the Call Connection asks if you want to take the call or have the caller leave a message. Ask for Caller’s Name Connection records the name of the caller and plays it for you before connecting the call. Note the following considerations: For the option of declining a call for someone with whom you share a phone, check both the Tell Me Who the Call Is For and the Ask Me If I Want to Take the Call check boxes. For the option of accepting or declining a call based on the identity of the caller, check both the Ask Me If I Want to Take the Call and the Ask For Caller’s Name check boxes. When you accept, Connection connects the call. When you decline, Connection forwards the call to voicemail. | Option | Description | Tell Me When the Call Is Connected | Connection tells you when it connects the call. | Tell Me Who The Call Is For | Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. | Ask Me If I Want to Take the Call | Connection asks if you want to take the call or have the caller leave a message. | Ask for Caller’s Name | Connection records the name of the caller and plays it for you before connecting the call. |
| Option | Description |
| Tell Me When the Call Is Connected | Connection tells you when it connects the call. |
| Tell Me Who The Call Is For | Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. |
| Ask Me If I Want to Take the Call | Connection asks if you want to take the call or have the caller leave a message. |
| Ask for Caller’s Name | Connection records the name of the caller and plays it for you before connecting the call. |
| Step 4 | Select Save . |

| Option | Description |
|---|---|
| Send Callers to Voicemail | Connection plays your greeting, then prompts the caller to leave a message. |
| Put Callers on Hold Without Asking | Connection puts the caller on hold and does not offer the option of leaving a message. |
| Ask Callers to Hold | Connection gives the caller the option of holding or leaving a message. |

| Option | Description |
|---|---|
| Tell Me When the Call Is Connected | Connection tells you when it connects the call. |
| Tell Me Who The Call Is For | Connection plays the name associated with the dialed extension. Use this setting when two or more people share a phone. |
| Ask Me If I Want to Take the Call | Connection asks if you want to take the call or have the caller leave a message. |
| Ask for Caller’s Name | Connection records the name of the caller and plays it for you before connecting the call. |