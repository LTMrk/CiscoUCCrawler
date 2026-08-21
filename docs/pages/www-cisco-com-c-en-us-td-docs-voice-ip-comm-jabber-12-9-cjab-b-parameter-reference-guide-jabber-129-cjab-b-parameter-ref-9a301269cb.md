---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-9-cjab-b-parameter-reference-guide-jabber-129-cjab-b-parameter-ref-9a301269cb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_9/cjab_b_parameter-reference-guide-jabber-129/cjab_b_parameter-reference-guide-jabber-129_chapter_0110.html
retrieved_at: 2026-08-21T05:25:14.870839+00:00
---

Parameters reference guide for Cisco Jabber 12.9

# Parameters reference guide for Cisco Jabber 12.9

Updated: September 26, 2023

Chapter: On-Premises Policies

## Chapter: On-Premises Policies

# On-Premises Policies

## DisableMFTForConversationTypes

Applies to Cisco Jabber for desktop clients.

When the Managed File Transfer option is available for the user, use DisableMFTForConversationTypes parameter to disable Managed File Transfer option for conversation types:

P2P—Managed file transfer is disabled for peer to peer conversations.

GroupChat—Managed file transfer is disabled for group chats.

PersistentChat—Managed file transfer is disabled for persistent chat rooms.

Use a semicolon to delimit multiple conversation types, for example P2P;GroupChat;PersistentChat .

Example: <DisableMFTForConversationTypes>P2P;PersistentChat</DisableMFTForConversationTypes>

## Disallowed_File_Transfer_Types

Applies to all Cisco Jabber clients.

Restricts users from
                              		  transferring specific file types. 
                              		You must set the file extensions as the value, for example, .exe .

Use a semicolon to delimit multiple file extensions, for
                              		  example, .exe;.msi;.rar;.zip .

Example: <Disallowed_File_Transfer_Types>.exe;.msi</Disallowed_File_Transfer_Types>

## File_Transfer_Enabled

Applies to all Cisco Jabber clients.

Specifies if the user can send files to someone else using Jabber. This parameter doesn't prevent users from receiving files
                              from other users.

true (default)—Users can send files to each other.

false—Users can't send files to each other.

Example: <File_Transfer_Enabled>false</File_Transfer_Enabled>

## H264HighProfileEnable

Applies to Cisco Jabber for Windows and Mac

You can enable the use of H.264 High profile with this parameter.

false (default)—H.264 use the Baseline profile with Jabber.

true—H.264 uses the High profile with Jabber.

Example: <H264HighProfileEnable>true</H264HighProfileEnable>

## PreferredFT

MFT—Files are
                                       				transferred using the managed file transfer option.

P2P—Files are
                                       				transferred using peer to peer file transfer.

If the parameter
                              		  is not defined, the client checks Cisco Unified Communications Manager IM and
                              		  Presence node, and when managed file transfer is available the client uses this
                              		  option, otherwise it uses peer to peer file transfer.

Example: <PreferredFT>P2P</PreferredFT>

## Screen_Capture_Enabled

Specifies if users can take screen captures.

true (default)—Users can take screen captures.

false—Users cannot take screen captures.

Example: <Screen_Capture_Enabled>false</Screen_Capture_Enabled>

## ShowScreenCaptureButton

true (default)—Screen capture button is enabled.

false—Screen capture button is disabled.

Example: <ShowScreenCaptureButton>false</ShowScreenCaptureButton>

| Note | Disabling this parameter will hide the Screen capture button in Windows and disable it for Mac. |
|---|---|