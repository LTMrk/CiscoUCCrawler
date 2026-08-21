---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-book-parameters-reference-guide-for-cisco-jabber-14-0-cjab--d251cd3089
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_book_parameters-reference-guide-for-cisco-jabber-14_0/cjab_b_parameter-reference-guide-jabber-129_chapter_011.html
retrieved_at: 2026-08-21T21:02:53.288777+00:00
---

Parameters Reference Guide for Cisco Jabber 14.0

# Parameters Reference Guide for Cisco Jabber 14.0

Updated: March 29, 2021

Chapter: Client

## Chapter: Client

# Client

## AllowUserSelectChatsFileDirectory

Applies to Cisco Jabber for Windows.

Determines whether users can change the directory for the MyJabberChats and MyJabberFiles folders.

true (default)—Users can change the directory of the MyJabberChats and MyJabberFiles folders using the Change Folder button on the Chats tab of the Options dialog.

false—Users are not allowed to change the directory for the MyJabberChats and MyJabberFiles folders. The Change Folder button is not visible on the Chats tab of the Options dialog.  The directory for the MyJabberChats and MyJabberFiles folders is determined by the AutosaveChatsLocation parameter.

If this parameter is not set, then the behavior is as for true.

Example: <AllowUserSelectChatsFileDirectory> true </AllowUserSelectChatsFileDirectory>

## AutoAcceptFileTransfer

Applies to Cisco Jabber desktop clients.

Specifies whether files are automatically accepted by users during file transfer. This parameter doesn't apply to images,
                              which you can configure using the AutoAcceptImage parameter.

true—Files are automatically accepted to be downloaded when sent in an IM.

false (default)—Files are not automatically accepted and the recipient must manually agree to receive the file.

Example: <AutoAcceptFileTransfer>true</AutoAcceptFileTransfer>

## AutoAcceptImage

Applies to Cisco Jabber for desktop clients.

Set up .jpg, .jpeg, .gif, and .png images to be automatically accepted by users. The AutoAcceptFileTransfer parameter (which is off by default) does not affect this parameter as it does not apply to image files.

true (default)—Images are automatically accepted in the client.

false—Images are not automatically accepted and standard file transfer is used.

## AutoAnswerForGuidedAccess

Applies to Cisco Jabber for iPhone and iPad

Specifies whether the Auto Answer option is available in the client when Guided Access is active on the device. Auto Answer
                              allows the client to automatically answer incoming Jabber calls with voice and video.

true—Auto Answer is available in the client settings when Guided Access is active.

false (default)—Auto Answer is not available.

## AutosaveChatsLocation

Applies to Cisco Jabber for Windows.

Defines the path
                              		  where instant messages and file transfers are automatically saved each time a user closes a
                              		  conversation. Use the absolute path on the local file system. 
                              		Chats are saved in a folder called MyJabberChats and files are saved in a folder called MyJabberFiles .

If the AllowUserSelectChatsFileDirectory parameter is set to false, then this parameter works with the MyJabberFilesLocation parameter as follows:

If both the AutosaveChatsLocation parameter and the MyJabberFilesLocation parameter have a value, then the MyJabberFilesLocation value takes priority.

If the MyJabberFilesLocation parameter does not have a value, then the AutosaveChatsLocation value determines the path to the MyJabberChats and MyJabberFiles folders.

If both the AutosaveChatsLocation parameter and the MyJabberFilesLocation parameter have no value, then all chats and files are saved to the default location ( Documents folder).

Example: <AutosaveChatsLocation> Local_Path </AutosaveChatsLocation>

## CachePasswordMobile

Applies to Cisco Jabber for mobile clients.

Specifies whether the client stores the password in the cache or not.

true (default)— The client stores the user password in cache; therefore, the users can automatically sign in when the client
                                    starts.

false— The client cannot store the user password in cache; therefore, the users must enter their password each time the client
                                    starts.

## CacheSessionCookieInDevice

Applies to Cisco
                              		  Jabber for iPhone and iPad

true
                                       				(default)—The cookies are  cached to the iOS keychain.

false—The cookies are  not cached to the iOS keychain.

## Call_Center_Audio_Enhance_Mode

Adjusts how the Media engine plays the audio for the contact center. Use this parameter when your contact center call flows
                              include Agent Greeting or Whisper Announcement.

true—Enables the call center audio enhance mode in the Media engine (CPVE)

false (default)—Disables the call center audio enhance mode in the Media engine (CPVE)

Example: <Call_Center_Audio_Enhance_Mode>true</Call_Center_Audio_Enhance_Mode>

## ChatAlert

Applies to Cisco Jabber for Windows

Specifies the default sound for chat alerts. Users can change this value in the Sounds and Alerts tab of the Options window.

Example: <ChatAlert>IMAlert_1</ChatAlert>

## ChatTelephonyEscalationLimit

Applies to Cisco
                              		  Jabber for Windows.

Defines the
                              		  maximum number of participants allowed when telephony escalations are enabled
                              		  for group chats and persistent chat.

Default value is
                              		  25 participants. If you set it to zero participants, then the parameter is disabled. However, there is no maximum limit
                              for the participants.

Example: <ChatTelephonyEscalationLimit>10</ChatTelephonyEscalationLimit>

## ContactCardonHover

Applies to Cisco Jabber for desktop clients.

Specifies whether contact cards are displayed when you hover over contact names in your Contacts list and in search result.

true (default)—The contact card is displayed if you hover over contacts in the hub window or in a search result. For Jabber
                                    for Windows the contact card is displayed when you press CTRL + I over a contacts' name.

false—The contact card is not displayed when you hover over names in the Contacts list or in a search result.

Example: <ContactCardonHover>false</ContactCardonHover>

## DefaultActionOfContactList

Applies to Cisco Jabber for mobile clients.

Specifies what happens when a Jabber user taps a contact from the contacts list or from the contact search result .

Chat (default)—The client starts a chat session with the contact.

Call—The client starts a VoIP call with the contact.

The setting specified for DefaultActionOfContactList parameter is not applicable for users with a Phone Only or IM Only account. If the Call option is configured for users who have full service deployed, then the client starts a mobile call when phone service is
                              not available.

Example: <DefaultActionOfContactList>Call</DefaultActionOfContactList>

## Disable_IM_History

Applies to all Cisco Jabber clients from 11.8 version onwards.

Specifies whether the client retains the chat history after participants log out. The client retains the chat history until
                              the participants reset Jabber.

If the Disable_IM_History key is false and the participants reopen the chat window, the client displays only the last 200 messages.

For persistent chat users, you must use false (default value). If you disable the Disable_IM_History parameter, then it affects the @mention feature in persistent chat rooms.

This parameter is not available for IM-only deployments.

true—Client does not retain the chat history after participants log out.

If the Disable_IM_History parameter is true, this takes precedence (the client saves no history) over the following settings:

Allow clients to log instant message history in the IM and Presence Server.

Webex Messenger Org Admin > Policy editor > Policy name > Local Archive option.

false (default)—Client retains the chat history after participants log out.

To retain chat history, you must also enable either the Allow clients to log instant message history option in the IM and Presence Server or the Webex Messenger Org Admin > Policy editor > Policy name > Local Archive option in Webex Messenger.

Example: <Disable_IM_History>true</Disable_IM_History>

## DisableAllMeetingReminder

Applies to Cisco Jabber for Windows and Cisco Jabber for Mac.

Specifies whether users receive reminders for Webex Meetings that are in their Jabber Meetings tab.

true—Reminders are disabled.

false (default)—Reminders are enabled.

## DisableAudioDucking

Applies to Cisco Jabber for Windows

Specifies if the Audio Ducking feature is enabled.

true(default)—Audio ducking is disabled

false—Audio ducking is enabled

Example: <DisableAudioDucking>true</DisableAudioDucking>

## DisableCallHistoryResolution

Applies to all clients

When you launch Jabber, Jabber attempts to look up each caller in the call history from the contact source. In deployments
                              like contact centers where most calls are from external numbers, these requests are unnecessary overhead for external phone
                              numbers. With a high volume of external calls, these requests can place a significant load on your LDAP or UDS server.

Use DisableCallHistoryResolution to eliminate the load on your server, if necessary.

true—Block all phone number resolution requests.

false (default)—Enable phone-number resolution requests.

Example: <DisableCallHistoryResolution>true</DisableCallHistoryResolution>

## DisableLocusCMR

Applies to all clients

Specifies to disable meeting control for CMR meeting features when when common
                              identity (CI) is enabled.

true —Disables meeting control.

false (default) — Enables meeting control.

Example: <DisableLocusCMR>false</DisableLocusCMR>

## DisableNonAcceptMeetingReminder

Applies to Cisco Jabber for  desktop clients.

Determines whether the Cisco Jabber popup meeting reminder is displayed for non-accepted Webex Meetings .

true—The Jabber popup meeting reminder isn't displayed for Webex Meetings that have not been accepted.

false (default)—The Jabber popup meeting reminder is displayed for non-accepted Webex Meetings .

Example: <DisableNonAcceptMeetingReminder>false</DisableNonAcceptMeetingReminder>

## DisableRemoteDesktopControl

Applies to Cisco Jabber for Windows

true—disable Remote Desktop Control

false(default)—enable Remote Desktop Control

< DisableRemoteDesktopControl >true</ DisableRemoteDesktopControl >

## DisableStartOnlineForOfflineMeeting

Applies to Cisco Jabber for Windows

Determines whether the Start online button is displayed in the Meetings tab for non- Webex Meetings . This parameter has no effect on Webex Meetings .

true (default)—The Start online button does not display in the Meetings tab for non- Webex Meetings .

false —The Start online button displays in the Meetings tab for non- Webex Meetings .

Example: <DisableStartOnlineForOfflineMeeting>false</DisableStartOnlineForOfflineMeeting>

## DisplayScreenshotWhenSwitchApps

Applies to Jabber for Android

Specifies whether to show a generic screenshot of Jabber when users switch apps by swiping up the home button.

true (Default)—When users swipe up the home button, they see the Jabber application.

false—When users swipe up the home button, they see a generic screenshot of Jabber.

Example: <DisplayScreenshotWhenSwitchApps>false</DisplayScreenshotWhenSwitchApps>

## EMMType

Applies to Cisco Jabber mobile clients

When you use Enterprise Mobility Management (EMM), EMMType enables you to block Jabber mobile clients with which you don't want users to sign in. If you don't configure this parameter,
                              Jabber defaults to allowing usage of any client type. This parameter accepts a semicolon-separated list (1;2) of allowed Jabber
                              clients.

0—Allow standard Jabber mobile clients

1—Allow Jabber for Intune

2—Allow Jabber for BlackBerry

Example: <EMMType>1;2</EMMType>

## EnableAutosave

Applies to Cisco Jabber for desktop clients.

Prerequisites:

Users must have a Cisco Unified Communications Manager account.

You must also enable local archiving in the Webex (using the Org Admin > Local Archive Policy) or Cisco Unified Communications
                                    Manager for IM and Presence (using Messages > Settings > Allow clients to log instant message history) servers.

Specifies whether users can save instant messages to an HTML file automatically, each time they close a conversation. The
                              file persists even the user signs out or resets Jabber.. Enable the option in the client as follows:

Windows— File > Options > Chats > Autosave chat session to:

Mac— Jabber > Preferences > Chats > Save chat archives to:

true—The check box is available.

false (default)—The check box is unavailable.

Example: <EnableAutosave>true</EnableAutosave>

Here is an example of the saved HTML file, when the user chooses Documents (default) as the autosave folder, on a Windows
                              platform:

```
C:\Users\user id\Documents\MyJabberChats\userA@domain.com\Chats\userB@domain.com\2019-04-02\userB@domain.com2019-04-02_10-55-15.html
```

## EnableConvertNumberToURI

Applies to Cisco Jabber for all clients.

true(default)—Cisco Jabber converts numbers into SIP URI.

false—Cisco Jabber doesn't convert numbers into SIP URI.

```
<EnableConvertNumberToURI>false</EnableConvertNumberToURI>
```

## EnableFecc

Applies to all
                              		  Cisco Jabber clients.

true
                                       				(default)—Far-end camera control is enabled. The Far-End Camera Control button is enabled on the call
                                       				video window.

false—Far-end
                                       				camera control is disabled. The Far-End Camera Control button is disabled on the
                                       				call video window, even if the endpoint can control far-end camera.

Example: <EnableFecc>false</EnableFecc>

## EnableFTE

Applies to Windows Cisco Jabber clients.

Specifies whether the user sees the first time experience after Jabber is reset or
                              the cache cleared.

true (default)—First time experience dialog is enabled after a reset or cache
                                    clearing.

false—First time experience dialog is disabled after a reset or cache
                                    clearing.

Example: <EnableFTE>false</EnableFTE>

## EnableInlineImages

Applies to Cisco Jabber for desktop clients.

Set up inline images so that they are allowed or prevented from being displayed  in the client without being downloaded first.

true (default)—The image is displayed in Jabber automatically.

false—File transfer is used where users must accept an image to see it.

Example: <EnableInlineImages>false</EnableInlineImages>

## EnablePrt

Applies to Cisco Jabber for desktop clients.

true
                                       				(default)—The Report a problem menu item is available.

false—The Report a problem menu item is removed.

Example: <EnablePrt>True</EnablePrt>

If you disable
                              		  this parameter, users can still manually use the Start
                                    				Menu > Cisco Jabber directory, or the Program
                              		  files directory and launch the Problem Report Tool manually.

If a user manually
                              		  creates a PRT, and this parameter value is set to false, then the zip file
                              		  created from the PRT has no content.

## EnablePrtEncryption

true—PRT files
                                       				sent by Cisco Jabber clients are encrypted.

false
                                       				(default)—PRT files sent by Cisco Jabber clients are not encrypted.

PRT encryption
                              		  requires a public or private key pair to encrypt and decrypt the Cisco Jabber
                              		  problem report. For more information, refer to the Decrypt the
                                 			 Problem Report section in the document Features and Options for Cisco Jabber .

Example: <EnablePrtEncryption>true</EnablePrtEncryption>

## EnableReminderForNoneWebExMeeting

Applies to Cisco Jabber for Desktop clients .

Specifies whether users receive reminders for Microsoft Outlook, Google Calendar, Mac iCalendar , IBM Notes and other non- Webex Meetings that are in their Jabber Meetings tab.

true—Reminders are enabled.

false (default)—Reminders are disabled.

## EnableSaveLogsToLocal

Applies to Cisco Jabber for Android

If your organization does not allow users to send emails from their mobile phone, you need another method to capture PRT logs.
                              You can allow users to save the logs locally with EnableSaveLogsToLocal . The allowed values are:

true (default)—Allow user to save PRT logs in local storage

false—Do not allow user to save PRT logs in local storage

Example: <EnableSaveLogsToLocal>true</EnableSaveLogsToLocal>

## EnableSingleNumberReach

Applies to Cisco Jabber for all clients.

Specifies if users can access Single Number Reach option.

Users can access Single Number Reach only when it is configured in Cisco Unified Communications Manager and EnableSingleNumberReach parameter is enabled.

true (Default)—User can access Single Number Reach option provided it is also configured in Cisco Unified Communications Manager.

false—User cannot access Single Number Reach option.

```
<EnableSingleNumberReach>true</EnableSingleNumberReach>
```

## EnableVDIFallback

Applies to Cisco Jabber Softphone for VDI only (all platforms).

Specifies whether to enable VDI Fallback mode when the JVDI Agent can't communicate with the JVDI Client.

true

false (default)

Example:

```
<EnableVDIFallback>true</EnableVDIFallback>
```

## EnableVDIFullScan

Applies to Cisco Jabber for Windows

Added for CSCvz75206 . The minimum versions for this parameter are JVDI 14.0.3 with Jabber for Windows 14.0.4.

Certain third-party application window can make preview, remote video, and remote share display as gray when the window is
                              close to a Jabber conversation window. If this issue occurs, enabling this parameter might correct the issue. The allowed
                              values are:

true—Enables a full scan of JVDI to correct the display issue.

false (default)—Maintains the standard Jabber behavior.

Example: <EnableVDIFullScan>true</EnableVDIFullScan>

## ForceLogoutTimerDesktop

Applies to Cisco Jabber desktop clients.

Specifies the number of minutes of inactivity before the user is automatically signed out of Cisco Jabber desktop clients.
                              If the parameter is not set, then  the client does not sign out automatically.

The value for minutes is from 1 to 480.

Example:

<ForceLogoutTimerDesktop>15</ForceLogoutTimerDesktop>

## ForceLogoutTimerMobile

Applies to Cisco Jabber mobile clients.

Specifies the number of minutes of inactivity before the user is automatically signed out of Cisco Jabber mobile clients.
                              If the parameter is not set the client does not sign out automatically.

The value for minutes is from 1 to 480.

Example: <ForceLogoutTimerMobile>15</ForceLogoutTimerMobile>

## Forgot_Password_URL

Applies to Cisco Jabber for Desktop clients.

Specifies the URL
                              		  of your web page for users to reset or retrieve forgotten passwords.

In hybrid cloud-based deployments, use the Cisco Webex Administration Tool to direct users to the web page to reset or retrieve
                              forgotten passwords.

Example:

<Forgot_Password_URL>http://http_servername/Forgot_Password_URL</Forgot_Password_URL>

## GlobalPhoneServiceErrorOnMobile

Applies to Cisco Jabber mobile clients

Specifies where the error message appears in the client when the phone service is registered on another device:

true—The error message appears at the top of the client. This position is always visible to the user.

false (default)—The error message appears in the Calls tab.

Example: <GlobalPhoneServiceErrorOnMobile>true</GlobalPhoneServiceErrorOnMobile>

This parameter is available starting in Release 12.8(1).

## HideCallControlStrip

Applies to Cisco
                              		  Jabber for Windows.

Specifies whether the call window displays the call control strip.

enable—Hides the call control strip during calls. Users see a call conversation window without the call control strip. On
                                    the top bar of the Cisco Jabber call window, users have an option to see or hide the call control strip.

disable (default)—Displays the call control strip during calls.

Example:

<HideCallControlStrip>enable</HideCallControlStrip>

## IP_Mode

Applies to all clients.

Specifies the network IP protocol for the Cisco Jabber client.

IPV4_Only—Jabber will only attempt to make IPv4 connections.

IPV6_Only—Jabber will only attempt to make IPv6 connections.

Dual_Stack (Default)—Jabber can connect with either IPv4 or IPv6.

Example: <IP_Mode>IPV4_Only</IP_Mode>

## J2JMaxBandwidthKbps

Applies to all Cisco Jabber clients in cloud deployments only.

Specifies the maximum bandwidth (in kilobits per second)  to be used for Jabber to Jabber calls. The video quality (resolution)
                              of the call is lowered so that it meets the bandwidth limit.

On startup, Cisco Jabber applies this setting from the jabber-config.xml file that is downloaded from Webex Messenger .

Minimum value—128 kbps. Values lower than this are automatically increased to 128Kbps.

Maximum value—4000 kbps. This is the default value. Values higher than 4000 kbps are automatically decreased to 4000 kbps.

## jabber-plugin-config

Applies to Cisco Jabber for all clients.

Contains plug-in
                              		  definitions such as custom embedded tabs that display HTML content. 
                              		 For more information, see Custom Embedded Tab Definitions section from the document Features and Options for Cisco Jabber .

```
<jabber-plugin-config>
<browser-plugin>
<page refresh="true" preload="true">
<tooltip>Cisco</tooltip>
<icon>http://www.cisco.com/web/fw/i/logo.gif</icon>
<url>www.cisco.com</url>
</page>
</browser-plugin>
</jabber-plugin-config>
```

## JabberHelpLink

Applies to Jabber for Windows

Controls whether the Help > Cisco Jabber help option appears.

true (default)—The Help menu includes the link to the Jabber Help Center.

false—The Help menu doesn't include the link to the Jabber Help Center.

Example: <JabberHelpLink>false</JabberHelpLink>

## JawsSounds

Applies to Cisco Jabber for Windows

Determines whether the default Windows notification sound is played when a contact search returns a result.

true (default)—The default Windows notification sound is played when a contact search returns a result.

false—No notification sound is played when a contact search returns a result.

## MakeUsernameReadOnly

Applies to Cisco Jabber for desktop clients.

Makes the Username field on the Sign In screen read-only after
                              		  the user signs in successfully for the first time.

true— Username field on the Sign In screen becomes
                                    				read-only after the user signs in successfully for the first time. To enable
                                    				the Username field again, or to switch to a different user,
                                    				users must reset Cisco Jabber from the File menu.

false
                                    				(default)— Username field on the Sign In screen remains
                                    				editable after the user signs in successfully for the first time.

Example: <MakeUsernameReadOnly>true</MakeUsernameReadOnly>

## MaxNumberOfBookmarks

Applies to Cisco Jabber for desktop and mobile clients .

30 (default)—sets a maximum of 30 bookmarks.

Example: <MaxNumberOfBookmarks>30</MaxNumberOfBookmarks>

## Mention_GroupChat

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—Enables mentions in group chat.

false—Disables
                                       				mentions in group chat.

Example: <Mention_GroupChat>false</Mention_GroupChat>

## Mention_P2Pchat

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—Enables mentions in person to person chat.

false—Disables
                                       				mentions in person to person chat.

Example: <Mention_P2Pchat>false</Mention_P2Pchat>

## Mention_PersistentChat

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—Enables mentions in persistent chat.

false—Disables
                                       				mentions in persistent chat.

Example: <Mention_PersistentChat>false</Mention_PersistentChat>

## MyJabberFilesLocation

Applies to Cisco Jabber for Windows.

Defines the path
                              		  where instant messages and file transfers are automatically saved each time a user closes a
                              		  conversation. Chats are saved in a folder called MyJabberChats and files are saved in a folder called MyJabberFiles.

The user sets this parameter in the Chats tab of the Options dialog. 
                              		When the user clicks the Change Folder button,  a browse dialog opens and the filepath to the chosen folder is written to the MyJabberFilesLocation parameter.

This parameter can be set only if the AllowUserSelectChatsFileDirectory parameter is set to false.

This parameter works with the AutosaveChatsLocation parameter as follows:

If both the AutosaveChatsLocation parameter and the MyJabberFilesLocation parameter have a value, then the MyJabberFilesLocation value takes priority.

If the MyJabberFilesLocation parameter does not have a value, then the AutosaveChatsLocation value determines the path to the MyJabberChats and MyJabberFiles folders.

If both the AutosaveChatsLocation parameter and the MyJabberFilesLocation parameter have no value, then all chats and files are saved to the default location (Documents folder).

## pChatMeeting

Applies to Cisco
                              		  Jabber for Windows.

true (default)— Webex Meetings capabilities are enabled for users in persistent chat rooms. Users see the Meet Now option displayed.

false— Webex Meetings capabilities are disabled for users in persistent chat rooms. Users do not see the Meet Now option displayed.

Example: <pChatMeeting>false</pChatMeeting>

## pChatShare

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—Screen sharing capabilities are enabled for users in persistent chat
                                       				rooms. Users see the Share screen option displayed.

false—Screen
                                       				sharing capabilities are disabled for users in persistent chat rooms. Users do
                                       				not see the Share screen option displayed.

Example: <pChatShare>false</pChatShare>

## Persistent_Chat_Enabled

Applies to Cisco
                              		  Jabber for desktop clients.

true—The
                                       				persistent chat interface is shown in the client.

false
                                       				(default)—The parameter is set to the default value if the setting is not present in the
                                       				configuration file.

Example: <Persistent_Chat_Enabled>true</Persistent_Chat_Enabled>

## Persistent_Chat_Mobile_Enabled

Applies to Cisco Jabber for mobile clients.

Specifies if persistent chat is available in the client.

Prerequisites:

You can set the value to true, only if the Cisco Unified Communications Manager Instant Messaging and Presence server version
                              is 11.5su5 or later.

true—Persistent chat is available in the client. You can set this

false (default)—Persistent chat is not available in the client.

Example: <Persistent_Chat_Mobile_Enabled>false</Persistent_Chat_Mobile_Enabled>

## PersistentChatTelephonyEnabled

Applies to Cisco
                              		  Jabber for Windows.

Specifies if the Call button is available when users are in persistent chat conversations.

- true (default)—Enables the Call button in persistent chat, which allows users
                                    			 to click on it to initiate a phone call.

- false—The Call button won't be displayed in persistent chat,
                                    			 so users can't initiate a conference.

Example: <PersistentChatTelephonyEnabled>false</PersistentChatTelephonyEnabled>

## PersistIMNotifications

Applies to Cisco Jabber for Windows.

Keeps IM notifications of new messages on the screen until you dismiss them so they do not fade away. Newer notifications
                              are stacked above older ones.

true - Messages can stay on the screen until users dismiss them. Users have the option to turn persistent display off in their Options menu under Notifications .

false (default) - Messages do not remain on the screen until dismissed. Messages are displayed and begin to fade away until
                                    there is no notification and only a flashing Jabber icon on the taskbar.

## PrtCertificateName

Applies to Cisco
                              		  Jabber for desktop clients.

Specifies the name
                              		  of a certificate with a public key in the Enterprise Trust or Trusted Root
                              		  Certificate Authorities certificate store. The certificate public key is used
                              		  to encrypt Cisco Jabber Problem reports. You must configure this parameter with
                              		  the EnablePrtEncryption parameter.

Example: <PrtCertificateName> Certificate_Name </PrtCertificateName>

## PRTCertificateUrl

Applies to Cisco
                              		  Jabber for mobile clients.

Specifies the URL to the certificate with a public key in the trusted
                              		  root certificate store. The client downloads the public key, and uses it to
                              		  encrypt the Cisco Jabber problem report. If EnablePrtEncryption is true, and no certificate is
                              		  downloaded, due to a wrong URL or a network problem, Cisco Jabber does not send
                              		  a PRT.

Example: <PRTCertificateUrl> http://server_name/path/Certificate_Name </PRTCertificateUrl>

## PrtLogServerURL

Specifies the
                              		  custom script for submitting problem reports. 
                              		 For more information, see Configure Problem Reporting section from the document Features and Options for Cisco Jabber .

Example: <PrtLogServerURL>http://server_name:port/path/prt_script.php</PrtLogServerURL>

## ResetOnLogOutOnMobile

Applies to Cisco Jabber mobile clients

Specifies whether Jabber automatically forces a reset when the user signs out:

true—The client automatically resets when the user signs out. The Sign Out button changes to Reset Jabber when you set this value.

false (default)—Signing out does not automatically reset the client.

Example: <ResetOnLogOutOnMobile>true</ResetOnLogOutOnMobile>

This parameter is available starting in Release 12.8(1).

## RestoreChatOnLogin

Applies to Cisco Jabber for desktop clients.

Specifies if the Remember my open conversations check box on the General tab of the Options window is checked when users first sign in.

true—The Remember my open conversations check box is checked when users sign in to Cisco Jabber for the first time. Each time users sign into the client, Jabber
                                    restores all the person-to-person conversations that were open when they signed out.

false (default)—The Remember my open conversations check box isn’t checked when users sign in to Cisco Jabber for the first time.

Users can override the initial setting by checking or unchecking the Remember my open conversations check box at any time.

If chat history isn’t enabled, then the restored chat windows are empty.

Jabber Team Messaging Mode always remembers open chats. The General tab doesn't have the Remember my open conversations check box in Jabber Team Messaging Mode.

Example: <RestoreChatOnLogin>false</RestoreChatOnLogin>

## SaveLogToLocal

Applies to Cisco Jabber for Android.

Determines whether users can save problem reports directly to their mobile device. If the parameter is set to true , users have two ways to export a problem report: have the client attach the report to a blank email, or save the problem
                              report directly to the mobile device. If the parameter is set to false , then users will have only the email option.

true (default)—Users can save problem reports to their mobile device.

false—Users can not save problem reports to their mobile device.

## ScreenReaderShowErrors

Applies to Cisco Jabber for Windows.

If a screen reader is running, displays informational messages in Jabber as pop-out windows.

true (default) - If a screen reader is running, messages that are otherwise displayed in the client are instead displayed
                                    as pop-out windows for screen readers to capture them. If a screen reader is not running, informational messages are displayed
                                    as normal.

false -  If a screen reader is running, messages are not displayed in a pop-out window.

## ShowCallAlerts

Applies to all clients

Controls whether the incoming call alerts (toasts) appear.

true (default)—The alerts appear.

false—The alerts don't appear.

Example: <ShowCallAlerts>false</ShowCallAlerts>

## ShowIconWhenMobile

Applies to Cisco Jabber for mobile clients.

Specifies if the mobile icon is displayed when a user signs in to Jabber using mobile device. The mobile icon is available
                              next to the user's availability status.

The mobile status icon, like other location sharing, is visible only on desktop clients. When ShowIconWhenMobile is enabled, and a user is signed in to both a desktop and mobile client, then only the desktop location is visible.

On—The mobile icon is displayed. Also, the Show icon when on mobile option is not available in the client.

Off—The mobile icon is not displayed. Also, the Show icon when on mobile option is not available in the client.

Default_on (default)—The mobile icon is displayed only if the user enables Show icon when on mobile option in the client. When the user launches the client, by default the Show icon when on mobile option is enabled.

Default_off—The mobile icon is displayed only if the user enables Show icon when on mobile option in the client. When the user launches the client, by default the Show icon when on mobile option is disabled.

Empty or no value—The mobile icon is displayed.

```
<ShowIconWhenMobile>Default_on</ShowIconWhenMobile>
```

## ShowRecentsTab

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—The Recents tab is displayed.

false—The Recents tab is not displayed.

Example: <ShowRecentsTab>false</ShowRecentsTab>

## SingleLinePhoneLabel

Applies to Cisco Jabber for desktop clients

In multiline operation, users choose between their configured lines in a selection list. The selection list displays the directory
                              number or the label for each line.

For users who only have a single line, whether the number or label for their line appears by default depends on the deployment
                              mode:

Phone-Only Mode and Phone Mode with Contacts —The single line's number or label appears by default.

Full UC Mode —The single line's number or label is hidden by default.

You can override the default behavior for single-line operation with the new SingleLinePhoneLabel parameter. The allowed values are:

true—The single line's number or label appears.

false—The single line's number or label is hidden.

Example: <SingleLinePhoneLabel>true</SingleLinePhoneLabel>

## spell_check_enabled

Applies to Cisco Jabber for Windows.

true—Spell
                                       				check is enabled.

false
                                       				(default)—Spell check is disabled.

Example: <spell_check_enabled>true</spell_check_enabled>

## spell_check_language

Applies to Cisco Jabber for Windows.

Specifies the
                              		  default spell check language used. The client uses the default spell check language set. You can define the default
                              		  language dictionary that you want   the client to use.

From the
                              		  conversation windows, users can select different default languages for each
                              		  user they chat with.

Example: <spell_check_language>1031</spell_check_language> defines German as the default spell check language.

## StartCallsWithVideoOverCellular

Applies to Cisco Jabber mobile clients

By default, Jabber calls over cellular networks start without video. You can control this with the StartCallsWithVideoOverCellular parameter. The allowed values are:

true—Calls over a cellular network default to "Use audio and video".

false (default)—Calls over a cellular network default to "Use audio only".

Example: <StartCallsWithVideoOverCellular>true</StartCallsWithVideoOverCellular>

## STARTUP_AUTHENTICATION_REQUIRED

Applies to all the Cisco Jabber clients.

false (default)—Fast Sign-in is enabled for your client.

true—Fast Sign-in is disabled for your client.

The STARTUP_AUTHENTICATION_REQUIRED parameter has dependency on CachePasswordMobile parameter. To enable Fast Sign-in, set STARTUP_AUTHENTICATION_REQUIRED to false and CachePasswordMobile to true.

If you have configured CachePasswordMobile parameter in releases earlier than 11.8, then in the release 11.9, configure both STARTUP_AUTHENTICATION_REQUIRED and CachePasswordMobile parameter to enable Fast Sign-in.

If you have not configured CachePasswordMobile parameter in releases earlier than 11.8, then you can configure only STARTUP_AUTHENTICATION_REQUIRED parameter to enable Fast Sign-in.

You can configure both of these parameters over Enterprise Mobility Management (EMM) also.

Example:

```
<STARTUP_AUTHENTICATION_REQUIRED>false</STARTUP_AUTHENTICATION_REQUIRED>
```

## SwapDisplayNameOrder

Applies to all Cisco Jabber clients.

Specifies that for
                              		  certain locales, when the displayname directory field is empty or not
                              		  available, users' own display names and the display names of their contacts can
                              		  be changed to Lastname,
                                 			 Firstname format.

true
                                       				(default)—In the following locales: Chinese (Hong Kong), Chinese (People's
                                       				Republic of China), Chinese (Taiwan), Japanese, Korean; the format for users'
                                       				own display names and the display names of their contacts is in the Lastname,
                                          				  Firstname format.

false—Users'
                                       				own display names and the display names of their contacts is in the Firstname,
                                          				  Lastname format.

Example: <SwapDisplayNameOrder>false</SwapDisplayNameOrder>

## SystemIdleDuringCalls

Applies to Cisco
                              		  Jabber for Windows.

Specifies if the
                              		  screen saver or computer lock function activates during a Cisco Jabber call if
                              		  the user is inactive, and if the function is enabled on your Windows computer.

true—Screen
                                       				saver can activate during calls.

false
                                       				(default)—Screen saver cannot activate during calls or when users receive a new
                                       				incoming call alert. When the call ends, or the new incoming call alert is
                                       				accepted or rejected, then the screen saver or screen lock is enabled again.

Example: <SystemIdleDuringCalls>true</SystemIdleDuringCalls>

## TelephonyOnlyDiscovery

Applies to all Cisco Jabber clients operating in on-premises and cloud deployment modes.

True—Cisco Jabber users can access phone services only.

False (default)—Cisco Jabber users can access all services that you’ve configured in your environment.

```
<TelephonyOnlyDiscovery>True</TelephonyOnlyDiscovery>
```

## UnreadMessageDeleteAlert

Applies to Cisco Jabber for iPhone and iPad

When you enable IM push notifications, users can receive notifications about
                              impending deletions of unread messages from the server. The notifications can appear
                              when the message queue is too large or when session suspensions last too long.

You can control these messages with the UnreadMessageDeleteAlert parameter. The allowed values are:

true (default)—The notifications appear.

false—The notifications do not appear.

The parameter suppresses these notifications. The default value of true shows the notifications. If you set the value to false , these notifications do not appear.

Example: <UnreadMessageDeleteAlert>false</UnreadMessageDeleteAlert>

This parameter is not supported when using Apple Push Notification service in
                                          iOS13 or above.

## UpdateURL

Applies to Cisco Jabber desktop clients.

Specifies the URL
                              		  to the automatic updates XML definition file on your HTTP server. The client
                              		  uses this URL to retrieve the update XML file. 
                              		 For more information, see Configure Automatic Updates section from the document Features and Options for Cisco Jabber .

Example: <UpdateURL> http://http_servername/UpdateURL_file </UpdateURL>

## LdapAnonymousBinding

Applies to all Cisco Jabber clients for on-premises deployments.

Specifies whether or not to bind to the LDAP server using anonymous binding instead of a user or service account.

true—Cisco Jabber does not use credentials when connecting to the LDAP server. Users are not allowed to enter credentials
                                    for the directory service in the Options window.

false (default)—Cisco Jabber uses credentials when connecting to the LDAP server.

Do not use the LdapAnonymousBinding parameter with any of the following parameters because they can cause conflicting configuration:

LDAP_UseCredentialsFrom

ConnectionUsername and ConnectionPassword

Example: <LdapAnonymousBinding>true</LdapAnonymousBinding>

## UseSystemLanguage

Applies to Cisco Jabber for Windows Release 11.1(1) onwards.

Specifies which language is used for the client. The language is determined using the following process:

The system checks the bootstrap file. If the language is specified in the bootstrap file (using the LANGUAGE parameter), then
                                    the specified language is used.

If the language is not specified in the bootstrap file, then the system checks the UseSystemLanguage parameter:

true—The language is set to the same value as the operating system.

false
                                          				(default)—The client uses the regional language as specified by the user. The regional language is set  at Control Panel > Clock, Language, and Region > Region and Language > Change the date, time, or number format > Formats tab > Format dropdown .

Example: <UseSystemLanguage>true</UseSystemLanguage>

If the language is not specified in the bootstrap file and the UseSystemLanguage parameter is not included in the jabber-config.xml file, then the regional language is used.

When this parameter is specified in the jabber-config.xml file on a TFTP server, it becomes effective only after the client
                                          is restarted ( File > Exit ).

## UXModel

Applies to Cisco Jabber for desktop clients

Jabber defaults to the Modern Design in all deployments. But, on-premises and Webex Messenger deployments also support the
                              Classic Design. Jabber Team Messaging Mode only supports the Modern Design.

If you want an on-premises or Webex Messenger deployment to start the Classic Design, use the UXModel parameter. The allowed values are:

modern (default)—Jabber starts in the Modern Design.

classic—Jabber starts in the Classic Design.

Each user can set a personal preference in Jabber, which takes precedence over this parameter.

Example: <UXModel>modern</UXModel>

| Note | These values are case-sensitive. |
|---|---|

| Note | For persistent chat users, you must use false (default value). If you disable the Disable_IM_History parameter, then it affects the @mention feature in persistent chat rooms. |
|---|---|

| Note | This parameter is not available for IM-only deployments. |
|---|---|

| Note | This parameter is available starting in Release 12.8(1). |
|---|---|

| Note | This parameter is available starting in Release 12.8(1). |
|---|---|

| Note | If chat history isn’t enabled, then the restored chat windows are empty. Jabber Team Messaging Mode always remembers open chats. The General tab doesn't have the Remember my open conversations check box in Jabber Team Messaging Mode. |
|---|---|

| Note | This parameter is not supported when using Apple Push Notification service in
                                          iOS13 or above. |
|---|---|

| Note | Do not use the LdapAnonymousBinding parameter with any of the following parameters because they can cause conflicting configuration: LDAP_UseCredentialsFrom ConnectionUsername and ConnectionPassword |
|---|---|

| Note | When this parameter is specified in the jabber-config.xml file on a TFTP server, it becomes effective only after the client
                                          is restarted ( File > Exit ). |
|---|---|