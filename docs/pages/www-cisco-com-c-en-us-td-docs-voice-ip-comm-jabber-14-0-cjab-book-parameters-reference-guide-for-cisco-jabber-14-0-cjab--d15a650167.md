---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-book-parameters-reference-guide-for-cisco-jabber-14-0-cjab--d15a650167
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_book_parameters-reference-guide-for-cisco-jabber-14_0/cjab_b_parameter-reference-guide-jabber-129_chapter_0111.html
retrieved_at: 2026-08-21T21:03:10.456147+00:00
---

Parameters Reference Guide for Cisco Jabber 14.0

# Parameters Reference Guide for Cisco Jabber 14.0

Updated: March 29, 2021

Chapter: Common Policies

## Chapter: Common Policies

# Common Policies

## AddContactProtocolRateLimit

Applies to Cisco
                              		  Jabber for Android on Synergy devices.

Specifies the
                              		  number of times that users can cross-launch after adding a contact with a URL
                              		  to their contact lists. The Add Contact scheme can be used to add contacts into
                              		  the contact list of a user with a URL (such as contact=username@cisco.com). For
                              		  example, if the AddContactProtocolRateLimit is 3, and the AddContactProtocolTimeLimit is 15 seconds, then a
                              		  user can cross-launch the Add Contact scheme on Cisco Jabber three times every 15
                              		  seconds.

You can set the
                              		  value between 1 to 100. The default value is 3.

Example: <AddContactProtocolRateLimit>10</AddContactProtocolRateLimit>

## AddContactProtocolTimeLimit

Applies to Cisco
                              		  Jabber for Android on Synergy devices.

Specifies the
                              		  time within which users can cross-launch after adding a contact with a URL to
                              		  their contact lists. You can set the value between 1 to 300 seconds. The default
                              		  value is 15 seconds.

Examples: <AddContactProtocolTimeLimit>10</AddContactProtocolTimeLimit>

## AlertOnAvailableEnabled

Applies to Cisco Jabber for desktop clients.

Enables users to add contacts to their availability watch list.

true (default)—Users can add contacts to their availability watch list.

false—Users cannot add contacts to their availability watch list.

Example: <AlertOnAvailableEnabled>false</AlertOnAvailableEnabled>

## BlockAccessoriesManagerPlugins

Applies to Cisco Jabber for desktop clients.

Disables specific
                              		  Accessories Manager plugins from third party vendors such as Jabra or Logitech.
                              		  You should set the name of the plugin DLL file as the value. Use a comma to
                              		  separate multiple values.

```
<BlockAccessoriesManagerPlugins> JabraJabberPlugin.dll,lucpcisco.dll </BlockAccessoriesManagerPlugins>
```

## BlockVersionBelow

Applies to all clients

Administrators can specify the earliest release, later than 12.9(0), of the client with which users can sign in. After setting
                              this parameter, Jabber clients from Release 12.9 onward force users on releases earlier than the specified release to sign
                              out. The client then displays an instruction to upgrade the client.

Only Jabber clients from Release 12.9 forward recognize this parameter. For example, if a Release 12.8(1) client reads this
                                          parameter in the jabber-config.xml , the client ignores it. So, this parameter only becomes effective after your users have installed at least Release 12.9 clients.

If you use the UpdateUrl parameter to have your Unified Communications Manager TFTP server auto-update Jabber, Jabber ignores BlockVersionBelow .

```
<BlockVersionBelow>12.9.1</BlockVersionBelow>
```

You can also use ForceUpgradingOnMobile to force Android users to upgrade to the latest version. BlockVersionBelow is more effective in BYOD deployments where users can disable autoupgrading on their device.

## CiscoTelProtocolCrossLaunchBackNotificationEnabled

Applies to Cisco Jabber for mobile clients.

Specifies if a
                              		  dialog box is shown asking users whether they want to return to another
                              		  application when a call ends or to stay in Jabber.

true
                                    				(default)—Dialog box is shown.

false—Dialog
                                    				box is not shown.

Example: <CiscoTelProtocolCrossLaunchBackNotificationEnabled>false</CiscoTelProtocolCrossLaunchBackNotificationEnabled>

## CiscoTelProtocolCrossLaunchBackSchema

Applies to Cisco Jabber for mobile clients.

Users can specify
                              		  parameters in a URL that are used to launch back to the original app.
                              		  CrossLaunchBackSchema is a white list of allowed app schemas that can be cross
                              		  launched back. You can specify additional parameters with each schema to allow
                              		  cross launching the app with additional parameters. You can set specific
                              		  parameters for the launched back schema. For example, for http, you can set the
                              		  web site “www.cisco.com”. After specifying a schema and any additional
                              		  parameters, use the semicolon to specify any additional schema you want to add.

none
                                    				(default)—No list.

schema_names —Semicolon-delimited list of permitted
                                    				application types.

Example: <CiscoTelProtocolCrossLaunchBackSchema>AppSchema1://parameter1;
                                 			 AppSchema2</CiscoTelProtocolCrossLaunchBackSchema>

## ClickToCallProtocolPermissionEnabled

Applies to Cisco Jabber for Windows.

true(default)—Dialog box is enabled, and users are asked to
                                       				confirm if they want to use Cisco Jabber to call.

false—Dialog
                                       				box is disabled, and the call is made without requesting confirmation first.

Example: <ClickToCallProtocolPermissionEnabled>false</ClickToCallProtocolPermissionEnabled>

## ClickToCallWithEditProtocolPermissionEnabled

Applies to Cisco Jabber for Windows.

true(default)—Dialog box is enabled, and users are asked to
                                       				confirm that they want to use Cisco Jabber to place the call with edit option.

false—Dialog
                                       				box is disabled, and the call is made without requesting confirmation first.

Example: <ClickToCallWithEditProtocolPermissionEnabled>false</ClickToCallWithEditProtocolPermissionEnabled>

## CommonCriteriaEndCallTimeout

Applies to Cisco Jabber for Windows, Cisco Jabber for iPhone and iPad, and Cisco Jabber for Android.

You must already be running Jabber in Common Criteria mode, by deploying the CC_MODE installation argument or EMM parameter.
                              When you deploy CC_MODE, the CommonCriteriaEndCallTimeout parameter is enabled automatically. It ensures that, during an active call, if the user doesn't receive any media data from
                              the other caller for a specific period, then the call is ended automatically. You can change the default value of 300 seconds.

Example: <CommonCriteriaEndCallTimeout> 60 </CommonCriteriaEndCallTimeout>

## CTIWindowBehaviour

Applies to Cisco
                              		  Jabber for Mac.

OnCall
                                       				(default)—Conversation window is always displayed when a call is answered.

Never—Conversation window is never displayed when a call is
                                       				answered.

If you configured
                              		  this parameter for earlier versions of Cisco Jabber for Windows, it can still
                              		  be used for this release. However, we recommend using the DeskPhoneModeWindowBehavior parameter instead.

Example: <CTIWindowBehaviour>Never</CTIWindowBehaviour>

## DeskPhoneModeWindowBehavior

Applies to Cisco
                              		  Jabber for Windows.

OnVideo—Conversation window is only displayed for video calls.

OnCall
                                       				(default)—Conversation window is always displayed when a call is answered.

Never—Conversation window is never displayed when a call is
                                       				answered.

Example: <DeskPhoneModeWindowBehavior>Never</DeskPhoneModeWindowBehavior>

## DetailedLogDurationDesktop

Applies to Cisco Jabber for desktop clients.

If you configure
                              		  the LogWritingDesktop parameter with the value UserCanEnable , then this parameter defines the number
                              		of hours that the desktop client writes logs to the disc. After the defined
                              		period expires, all logs are cleared from the disc.

If you do not
                              		  specify a value for this parameter (default), then the client writes logs to
                              		  the disc indefinitely, or until the user disables detailed logging.

Example: <DetailedLogDurationDesktop>10</DetailedLogDurationDesktop>

## DetailedLogDurationMobile

Applies to Cisco Jabber for mobile clients.

If you configure
                              		  the LogWritingMobile parameter with the value UserCanEnable , then this parameter defines the number
                              		of hours that the mobile client writes logs to the disc. After the defined
                              		period expires, all logs are cleared from the disc.

If you do not
                              		  specify a value for this parameter (default), then the client writes logs to
                              		  the disc indefinitely, or until the user disables detailed logging.

Example: <DetailedLogDurationMobile>10<DetailedLogDurationMobile>

## DiagnosticsToolEnabled

Applies to Jabber for Windows

In Jabber for Windows releases before 12.8(2), you can only disable the Jabber Diagnostic Tool by installing the client with
                              the DIAGNOSTICSTOOLENABLED installation argument set to false.

Release 12.8(2) adds the DiagnosticsToolEnabled parameter to enable you to disable the tool in jabber-config.xml .

true (default)—Users can display the Jabber Diagnostics Tool by entering Ctrl+Shift+D.

false—The Jabber Diagnostics Tool isn’t available to users.

Example: <DiagnosticsToolEnabled>false</DiagnosticsToolEnabled>

## Disable_MultiDevice_Message

Applies to all Cisco Jabber clients in cloud and on-premises deployments.

Disables the multiple device messaging feature.

true—Disables the multiple device  messaging feature.

false (default)—The multiple device  messaging feature is enabled. Users can see all sent and received messages on all devices
                                    that they are signed into.

Multiple device  messaging does not support file transfer or screen captures. Files are available only on the active devices
                                          that sent or received the files.

Example:

<Disable_MultiDevice_Message>true</Disable_MultiDevice_Message>

## DisableVoicemailSentBox

Applies to all clients

Release 12.8 added the option for users to see their sent voicemails in Visual Voicemail. The client makes periodic requests
                              to your server to refresh the Sent box. To eliminate this extra traffic, you can use DisableVoicemailSentBox to disable the Sent box.

true—Disable the Sent box.

false (default)—Don't disable the Sent box.

Example: <DisableVoicemailSentBox>true</DisableVoicemailSentBox>

## Disallow_File_Transfer_On_Mobile

Applies to Cisco Jabber for mobile clients.

Specifies whether
                              		  the user can send or receive files on mobile.

true—Users
                                    				cannot send or receive files on mobile.

false
                                    				(default)—Users can send or receive files on mobile.

Example: <Disallow_File_Transfer_On_Mobile>true</Disallow_File_Transfer_On_Mobile>

## EnableAccessoriesManager

Applies to Cisco Jabber for desktop clients.

Enables the accessories API in the client. This API lets accessory vendors create plug-ins to enable call management functionality
                              for devices such as headsets.

true (default)—Enable the accessories API.

false—Disable the accessories API.

When set to false, call control buttons on some headsets don’t work.

Example: <EnableAccessoriesManager>false</EnableAccessoriesManager>

## EnableADLockPrevention

Applies to all clients

Administrators can configure your Active Directory server for a maximum number of failed sign-in attempts. This setting can
                              lead to incorrect account lockouts in some Jabber deployments. For example, in a deployment without SSO authentication, all
                              Jabber services can send the same incorrect credentials to the AD server, rapidly incrementing the failure counter.

If you encounter this issue, you can use EnableADLockPrevention to prevent services from sending the same incorrect credentials to the AD server. The allowed values are:

true—Jabber stops all services which have the same credentials after one service receives an invalid credentials error.

false (default)—Jabber ignores invalid credential errors and continues sign-in attempts.

Example: <EnableADLockPrevention>true</EnableADLockPrevention>

## EnableBFCPVideoDesktopShare

Applies to all Cisco Jabber clients.

true
                                       				(default)—Enables BFCP video desktop sharing on the client.

false—Disables
                                       				BFCP video desktop sharing.

Example: <EnableBFCPVideoDesktopShare>false</EnableBFCPVideoDesktopShare>

## EnableCallPickup

Applies to Cisco Jabber for desktop clients.

Specifies if a user can pickup a call in their call pickup group.

true—Enables call pickup.

false (default)—Disables call pickup.

Example: <EnableCallPickup>true</EnableCallPickup>

## EnableCiscoChatProtocol

Applies to Cisco
                              		  Jabber for mobile clients.

true
                                       				(default)—The client registers as the protocol handler for the ciscochat:
                                       				protocol.

false—The
                                       				client does not register as the protocol handler for the ciscochat: protocol.

Example: <EnableCiscoChatProtocol>false</EnableCiscoChatProtocol>

## EnableCiscoIMGroupProtocol

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—The client registers as the protocol handler for the ciscoimgroup:
                                       				URI.

false—The
                                       				client does not register as the protocol handler for the ciscoimgroup: URI.

Example: <EnableCiscoIMGroupProtocol>false</EnableCiscoIMGroupProtocol>

## EnableCiscoIMProtocol

Applies to Cisco
                              		  Jabber for Android, iPhone and iPad, and Windows.

true
                                       				(default)—The client registers as the protocol handler for the ciscoim: URI.

false—The
                                       				client does not register as the protocol handler for the ciscoim: URI.

Example: <EnableCiscoIMProtocol>false</EnableCiscoIMProtocol>

## EnableCiscoTelConfProtocol

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—The client registers as the protocol handler for the ciscotelconf:
                                       				URI.

false—The
                                       				client does not register as the protocol handler for the ciscotelconf: URI.

Example: <EnableCiscoTelConfProtocol>false</EnableCiscoTelConfProtocol>

## EnableCiscoTelProtocol

Applies to Cisco
                              		  Jabber for Android, iPhone and iPad, and Windows.

true
                                       				(default)—The client registers as the protocol handler for the ciscotel: URI.

false—The
                                       				client does not register as the protocol handler for the ciscotel: URI.

Example: <EnableCiscoTelProtocol>false</EnableCiscoTelProtocol>

## EnableClickToCallProtocol

Applies to Cisco
                              		  Jabber for Android, iPhone and iPad, and Windows.

true
                                       				(default)—The client registers as the protocol handler for the clicktocall:
                                       				URI.

false—The
                                       				client does not register as the protocol handler for the clicktocall: URI.

Example: <EnableClickToCallProtocol>false</EnableClickToCallProtocol>

## EnableDualConnections

Applies to all clients.

Enables the client to establish an active connection to the primary node and an
                              inactive connection to the backup node.

true —Enables dual connections.

false (default)—Dual connections are disabled.

Example: <EnableDualConnections>True</EnableDualConnections>

## EnableForensicsContactData

true
                                       				(default)—Contacts folder is collected by the PRT tool.

false—Contacts
                                       				folder is not collected by the PRT tool.

Example: <EnableForensicsContactData>false</EnableForensicsContactData>

## EnableGroupCallPickup

Applies to Cisco Jabber for desktop clients.

Specifies if a user can pickup incoming calls in another call pickup group, by entering the call pickup group number.

true—Enables group call pickup.

false (default)—Disables group call pickup.

Example: <EnableGroupCallPickup>true</EnableGroupCallPickup>

## EnableHuntGroup

Applies to all Cisco Jabber clients.

Specifies if a user can log into a hunt group.

true—Users can log into their hunt group.

false (default)—Users cannot log into their hunt group.

Example: <EnableHuntGroup>true</EnableHuntGroup>

## EnableIMProtocol

Applies to all Cisco Jabber clients.

Specifies if the client registers as the protocol handler for the im: URI.

true (default)—The client registers as the protocol handler for the im: URI.

false—The client does not register as the protocol handler for the im: URI.

Example: <EnableIMProtocol>false</EnableIMProtocol>

## EnableLocalAddressBookSearch

Applies to Cisco Jabber for Windows and mobile clients .

Specifies if users can search for local contacts. For Jabber Windows client, users can also add these local contacts to their
                              contact lists.

true (default)—Users can search for contacts.

false—Users cannot search for contacts.

Example: <EnableLocalAddressBookSearch>false</EnableLocalAddressBookSearch>

These parameters interact for calendar integration and contact resolution:

CalendarIntegrationType

EnableLocalAddressBookSearch

EnableLotusNotesContactResolution

See the Feature Configuration for Cisco Jabber guide for details.

## EnableLotusNotesCLibrarySupport

Applies to Cisco Jabber for Windows.

Specifies if IBM Lotus Notes is using the C Library.

true (default)—Notes C Library

false—Notes C++ Library

Example: <EnableLotusNotesCLibrarySupport>true</EnableLotusNotesCLibrarySupport>

## EnableLotusNotesContactResolution

Applies to Cisco Jabber for Windows.

Lets users search
                              		  for and add local IBM Notes contacts to their contact lists.

true—Users can
                                    				search for and add local contacts from IBM Notes to their contact lists.

The EnableLocalAddressBookSearch parameter must also be
                                                				  set to true.

false
                                    				(default)—Users cannot search for or add local contacts from IBM Notes to their
                                    				contact lists.

Example: <EnableLotusNotesContactResolution>true</EnableLotusNotesContactResolution>

These parameters interact for calendar integration and contact resolution:

CalendarIntegrationType

EnableLocalAddressBookSearch

EnableLotusNotesContactResolution

See the Feature Configuration for Cisco Jabber guide for details.

## EnableMediaStatistics

true (default)—Real-time audio and video statistics can be viewed when on a call.

false—No real-time audio and video are available when on a call.

Example: <EnableMediaStatistics>FALSE</EnableMediaStatistics>

## EnableOtherGroupPickup

Applies to Cisco Jabber for desktop clients.

Specifies if a user can pickup an incoming call in a group that is associated with their own call pickup group.

true—Enables other group call pickup.

false (default)—Disables other group call pickup.

Example: <EnableOtherGroupPickup>true</EnableOtherGroupPickup>

## EnableP2PDesktopShare

true
                                       				(default)—Allows users to share their screens.

false—Users
                                       				cannot do a person to person screen sharing.

Example: <EnableP2PDesktopShare>false</EnableP2PDesktopShare>

## EnableProfileProtocol

Applies to Cisco
                              		  Jabber for mobile clients.

true
                                       				(default)—The client registers as the protocol handler for the profile:
                                       				protocol.

false—The
                                       				client does not register as the protocol handler for the profile: protocol.

Example: <EnableProfileProtocol>false</EnableProfileProtocol>

## EnablePromoteMobile

Applies to Cisco Jabber for Windows.

true —The notification to download the mobile clients is shown in the client.

false (default)—The notification is not shown.

If Cisco Jabber is deployed in Full UC mode, the user will receive this notification only once after it's been enabled. If
                                             Cisco Jabber is deployed in a Phone-only mode, the notification will be displayed only if a mobile device has been configured
                                             for the user.

You can change the default text of the user notification by configuring the key PromotionWelcomeText , the accepted input value is text.

You can also change the download link by configuring the AndroidDownloadURL parameter for Android and the IOSDownloadURL parameter for iOS. By default these parameters are configured to direct the users to the Cisco Jabber download page on the
                              Google Play Store or the Apple App Store.

Example: <EnablePromoteMobile>false</EnablePromoteMobile>

<PromotionWelcomeText> Download the Cisco Jabber for Android app. </PromotionWelcomeText>

<AndroidDownloadURL> www.example.com/download </AndroidDownloadURL>

<IOSDownloadURL> www.example.com/download </IOSDownloadURL>

## EnableProvisionProtocol

Applies to Cisco Jabber for Android, iPhone and iPad, and Mac.

Specifies if the client registers as the protocol handler for URL provisioning.

true (default)—The client registers as the protocol handler for URL provisioning.

false—The client does not register as the protocol handler for URL provisioning.

Example: <EnableProvisionProtocol>false</EnableProvisionProtocol>

## EnableRecordingTone

Applies to all clients

Enables recording tones for the user. This parameter works with these other parameters: LocalRecordingToneVolume , NearEndRecordingToneVolume , and RecordingToneInterval .

Enable the Unified CM service parameter to play recording notification tones before adding the Jabber recording tone parameters.
                                          See the monitoring and recording chapter of the Features and Services Guide for Cisco Unified Communications Manager for details.

true (default)—Enable recording tones.

false—Disable recording tones.

Example: <EnableRecordingTone>true</EnableRecordingTone>

## EnableSaveChatToFile

Applies to Cisco Jabber for desktop clients.

Allows users to right click on their chats and save them to the file system as HTML.

true (default)—Users can save their chats to file.

false—Users cannot save their chats to file.

Example: <EnableSaveChatToFile>false</EnableSaveChatToFile>

## EnableShareProtocol

Applies to Cisco
                              		  Jabber for mobile.

true
                                       				(default)—The client registers as the protocol handler for the share: URI.

false—The
                                       				client does not register as the protocol handler for the share: URI.

Example: <EnableShareProtocol>false</EnableShareProtocol>

## EnablesSendLogsViaEmail

Applies to mobile clients.

Enables the Send via email button in the Problem
                                 reporting window.

true  (default) —User can send logs via email.

false — Button is not available.

Example: <EnablesSendLogsViaEmail>True</EnablesSendLogsViaEmail>

## EnableSIPProtocol

Applies to all Cisco Jabber clients.

Specifies if the client registers as the protocol handler for the sip: URI.

true (default)—The client registers as the protocol handler for the sip: URI.

false—The client does not register as the protocol handler for the sip: URI.

Example: <EnableSIPProtocol>false</EnableSIPProtocol>

## EnableSIPURIDialling

Applies to all Cisco Jabber clients.

Enables URI dialing with Cisco Jabber and allows users to make calls with URIs.

true (default)—Users can make calls with URIs.

Default value changed to "true" in Release 12.6 to support meeting controls for Webex Collaboration Meeting Rooms.

false—Users cannot make calls with URIs.

Example: <EnableSIPURIDialling>true</EnableSIPURIDialling>

## EnableStatusProtocol

Applies to Cisco
                              		  Jabber for mobile clients.

true
                                       				(default)—The client registers as the protocol handler for the status:
                                       				protocol.

false—The
                                       				client does not register as the protocol handler for the status: protocol.

Example: <EnableStatusProtocol>false</EnableStatusProtocol>

## EnableTelephonyProtocolRateLimit

Applies to Cisco Jabber for Mac.

Specifies if there is a limit on the number of times the telephony protocol handler is used in the client.

true (default)—Rate limiting is enabled for
                                    executing the telephony protocol handlers.

false—Rate limiting is disabled for executing the
                                    telephony protocol handlers.

Example: <EnableTelephonyProtocolRateLimit>false</EnableTelephonyProtocolRateLimit>

## EnableTelProtocol

Applies to all Cisco Jabber clients.

Specifies if the client registers as the protocol handler for the tel: URI.

true (default)—The client registers as the protocol handler for the tel: URI.

false—The client does not register as the protocol handler for the tel: URI.

Example: <EnableTelProtocol>false</EnableTelProtocol>

## EnableTelProtocolPopupWindow /
                        	 CiscoTelProtocolPermissionEnabled

Applies to Cisco Jabber for Windows.

true
                                       				(default)—Dialog box is enabled, and users are asked to confirm that they want
                                       				to place the call.

false—Dialog
                                       				box is disabled, and the call is made without requesting confirmation first.
                                       				This may cause accidental or unwanted calls.

The CiscoTelProtocolPermissionEnabled parameter replaces
                                             			 the EnableTelProtocolPopupWindow parameter. Both
                                             			 parameters are supported in the client, however the dialog box is disabled if of the
                                             			 either parameter is set to false.

Example: <CiscoTelProtocolPermissionEnabled>false</CiscoTelProtocolPermissionEnabled>

## EnableVideo

Enables or
                              		  disables video capabilities during a Cisco Jabber video call.

true
                                    				(default)—Users can make and receive video calls.

false—Users
                                    				cannot make or receive video calls.

Example: <EnableVideo>false</EnableVideo>

## EnableVoicePush

Applies to Cisco Jabber for iPhone and iPad.

Specifies if Cisco Jabber receives voice and video push notifications whenever there is a call, even if Cisco Jabber is inactive.

The option to set an automatic away timer is not available when push notifications are enabled.

true (default)—Push notifications are enabled whenever there is a call.

false—Push notifications are disabled.

Example: <EnableVoicePush>true</EnableVoicePush>

## EnableXMPPProtocol

Applies to Cisco
                              		  Jabber for Android, iPhone and iPad, and Windows.

true
                                       				(default)—The client registers as the protocol handler for the xmpp: URI.

false—The
                                       				client does not register as the protocol handler for the xmpp: URI.

Example: <EnableXMPPProtocol>false</EnableXMPPProtocol>

## FCM_Push_Notification_Enabled

Applies to Jabber for Android

Specifies if the client receives push notification wen there's a new call or IM, even if Jabber is inactive.

You can't set an automatic away timer when you have enabled push notifications.

true (default)—Push notifications are enabled for new calls and IMs.

false—Push notifications are disabled.

Example: <FCM_Push_Notification_Enabled>false</FCM_Push_Notification_Enabled>

## ForceC2XDirectoryResolution

Applies to Cisco Jabber for Windows.

true
                                       				(default)—The client queries the directory when users perform click-to-x
                                       				actions.

false—The
                                       				client does not query the directory for click-to-x actions.

This parameter
                                             				does not take effect when users connect to the corporate network through
                                             				Expressway for Mobile and Remote Access. In this case, UDS provides contact
                                             				resolution and the client cannot query the directory.

Example: <ForceC2XDirectoryResolution>false</ForceC2XDirectoryResolution>

## ForceDevicePin

Applies to Cisco Jabber for mobile clients.

This parameter specifies that Jabber must be running on secured devices only.  Configure ForceDevicePin parameter with these values:

false(default)—Jabber does not check if the users have secured their devices.

true—Jabber checks if the users have secured their devices.

Example:

<ForceDevicePin>false</ForceDevicePin>

## ForceFontSmoothing

Applies to Cisco Jabber for Windows.

true
                                       				(default)—The client applies anti-aliasing to text.

false—The
                                       				operating system applies anti-aliasing to text.

Example: <ForceFontSmoothing>false</ForceFontSmoothing>

## ForceUpgradingOnMobile

Applies to Cisco Jabber for Android

Administrators can enforce upgrading to the latest version with this parameter.

true—If newer client found in periodic check, start Android's Immediate in-app upgrade to force upgrade.

false (default)—Don’t force upgrade when newer client is available.

You can also use BlockVersionBelow to stop users from signing in with clients that are earlier than a specified release. BlockVersionBelow is more effective in BYOD deployments where users can disable autoupgrading on their device.

Example: <ForceUpgradingOnMobile>true</ForceUpgradingOnMobile>

## Inactive_Connection_Activation_Timer

Applies to all clients.

The amount of time, in seconds, to wait for the connection activation signal. Default
                              is 120.

Example: <Inactive_Connection_Activation_Timer>60</Inactive_Connection_Activation_Timer>

## InitialPhoneSelection

Sets the phone
                              		  type for users when the client starts for the first time. Users can change
                              		  their phone type after starting the client for the first time. The client then saves the user
                              		  preference, and uses it for the next time when the client starts.

deskphone—Use
                                    				the desk phone device for calls.

softphone
                                    				(default)—Use the software phone (CSF) device for calls.

Software phone
                                       				devices

Desk phone
                                       				devices

This parameter does not apply to Jabber deployed in a Virtual environment.

## InstantMessageLabels

Applies to Cisco Jabber for Windows.

Defines a catalog of security labels, such as SECRET and CONFIDENTIAL, that users must apply before they send an instant message.
                              The label appears before each message that is sent. For example, SECRET: message text .

You can specify a
                              maximum of 17 labels.

Cisco Jabber uses the XEP-0258 standard to implement security labels. For more information, refer to XEP-0258: Security Labels in XMPP .

Cisco Jabber does not control message distribution based on these labels. Any such control requires the use of a third-party
                              product, such as a compliance server, which supports XEP-0258 label headers.

Example for jabber-config.xml for security labels:

```
<InstantMessageLabels> 
  <item selector="Classified|SECRET"> 
    <securitylabel xmlns='urn:xmpp: sec-label:0'> 
     <displaymarking fgcolor='black' bgcolor='red'>SECRET </displaymarking>
      <label>
       <edhAttrs xmlns="https://www.surevine.com/protocol/xmpp/edh">
       <specification>2.0.2</specification>
       <version>XXXX:1.0.0</version>
       <policyRef></policyRef>
       <originator>Acme</originator>
       <custodian>Acme</custodian>
       <classification>A</classification>
       <nationalities>Acme</nationalities>
       <organisations>Acme</organisations>
       </edhAttrs>
     </label>
    </securitylabel> 
  </item> 
<item…> … </item> 
</InstantMessageLabels>
```

## InvalidCredentialsLogout

Applies to all Cisco Jabber clients.

When InvalidCredentialsLogout is set to <value>true</value> the client checks for expired tokens for non-SSO credentials. If the tokens are expired, the
                              user is signed out and prompted to reauthenticate.The allowed values are:

true—Jabber checks for expired tokens.

false (default)—Jabber never checks for expired tokens.

Example: <InvalidCredentialsLogout>true</InvalidCredentialsLogout>

## LegacyOAuthLogout

Applies to all Cisco Jabber clients.

If you have OAuth enabled in your deployment, Jabber checks, by default, for expired refresh tokens when users sign in. If
                              a refresh token has expired, the user must re-authenticate. If the refresh token expires while a user is signed in, Jabber
                              signs them out with a message that their session expired.

The LegacyOAuthLogout parameter controls this behavior. The allowed values are:

true—Jabber never checks for expired refresh tokens.

false (default)—Jabber checks for expired refresh tokens

Example: <LegacyOAuthLogout>true</LegacyOAuthLogout>

## LocalRecordingToneVolume

Applies to all clients

Specified the volume at which the client plays the recording tone locally.

The range is 0-100 and defaults to 10.

Example: <LocalRecordingToneVolume>25</LocalRecordingToneVolume>

See EnableRecordingTone for details on properly configuring recording tones.

## LogWritingDesktop

Applies to Cisco Jabber for desktop clients.

Always (default)—Logs are always written to disc at DEBUG level. No option appears in the client Help menu.

UserCanEnable—Allows users to decide whether logs are written to disc or not. Setting this value creates a Detailed Logging option in the Help menu of the client, where the user can enable or disable detailed logging. If enabled, DEBUG level logging is created, and
                                       if disabled, INFO level logging is created.

Never—Logs are never written to disc. INFO level logging is created. When a PRT is manually generated, in-memory logs are
                                       flushed to a temporary file that is deleted as soon as the PRT is generated.

Example: <LogWritingDesktop>UserCanEnable</LogWritingDesktop>

For INFO level logging, logs are kept in the in-memory buffer only, which is circular.

For DEBUG level logging, the in-memory buffer is flushed to disc when it is full. When resetting Jabber, all logs on disc
                              are wiped.

## LogWritingMobile

Applies to Cisco Jabber for mobile clients.

Defines the level of security for PRT logging by specifying whether Jabber writes logs to disc for mobile clients.

Always (default)—Jabber always writes logs to disc at the INFO level. No option appears in the client Help menu.

UserCanEnable—Allows you to decide whether to write logs to disc. Setting this value creates a Detailed Logging option in the Help menu of the client. You can enable or disable detailed logging. If enabled, creates DEBUG level logging, and if disabled,
                                    creates INFO level logging.

Never—Jabber never writes logs to disc. This setting creates INFO level logging. When you manually generate a PRT, Jabber
                                    flushes in-memory logs to a temporary file and then deletes the file after generating the PRT.

Example: <LogWritingMobile>UserCanEnable</LogWritingMobile>

For INFO level logging, Jabber keeps logs in the in-memory buffer only, which is circular.

For DEBUG level logging, Jabber flushes the in-memory buffer to disc when it is full. Resetting Jabber wipes all logs on disc.

## MaxNumberOfFilesDesktop

Applies to Cisco Jabber for desktop clients

Specifies the maximum number of Jabber problem reports. The range is 1–20. By default, the desktop clients allow 10.

Example:

```
<MaxNumberOfFilesDesktop>15</MaxNumberOfFilesDesktop>
```

## MaxNumberOfFilesMobile

Applies to Cisco Jabber for mobile clients

Specifies the maximum number of Jabber problem reports. The default is 5(50MB).

Example:

```
<MaxNumberOfFilesMobile>20</MaxNumberOfFilesMobile>
```

## Meetings_Enabled

true (default)—Enables meetings capabilities, allowing you to create meetings and get reminders to join meetings.

false—Disables meetings capabilities.

Example: <Meetings_Enabled>false</Meetings_Enabled>

## MuteAudioByDefault

Applies to all Cisco Jabber clients.

Specifies if the microphone is automatically muted for all Jabber calls.

false (default)—Your users microphone isn't muted for Jabber calls.

true—Your users microphone is muted for Jabber calls.

Example: <MuteAudioByDefault> true </MuteAudioByDefault>

## NearEndRecordingToneVolume

Applies to all clients

Specifies the volume of the recording tone which Jabber sends to the remote device and to the near-end recording server.

The range is 0-100 and defaults to 10.

Example: <NearEndRecordingToneVolume>25</NearEndRecordingToneVolume>

See EnableRecordingTone for details on properly configuring recording tones.

## Prefer_BIB_Recorder

Applies to Cisco Jabber desktop clients

In deployments with Unified Communications Manager Release 12.5(1) and later, Jabber can support Unified CM's on-demand recording
                              using Jabber's Built-In Bridge (BiB). By default, if the user joins a conference call that has an external bridge set up to
                              record calls, Jabber uses that external bridge for recording.

Some organizations might prefer all recording to use the Jabber BiB for compliance reasons. You can use the Prefer_BIB_Recorder parameter to enforce recording on the Jabber BiB. The allowed values are:

true—Use the Jabber BiB recorder for all calls.

false (default)—If available, record on the external bridge.

Example: <Prefer_BIB_Recorder>true</Prefer_BIB_Recorder>

## PresenceProtocolRateLimit

Applies to Cisco
                              		  Jabber for Android on Synergy devices.

Specifies the
                              		  number of times that the  users can launch the Presence or Edit Presence screens
                              		  from other applications. For example, if the PresenceProtocolRateLimit is three times, and the PresenceProtocolTimeLimit is 15 seconds, then a user
                              		  can start the launch of Presence or Edit Presence screens from other
                              		  applications three times every 15 seconds.

You can set the
                              		  value between 1 to 100. The default value is 3.

Example: <PresenceProtocolRateLimit>10</PresenceProtocolRateLimit>

## PresenceProtocolTimeLimit

Applies to Cisco
                              		  Jabber for Android on Synergy devices.

Specifies the time
                              		  within which users can launch the Presence or Edit Presence screens from other
                              		  applications. You can set the value between 1 to 300 seconds. The default value is
                              		  15 seconds.

Example: <PresenceProtocolTimeLimit>5</PresenceProtocolTimeLimit>

## PreventDeclineOnHuntCall

Applies to all Cisco Jabber clients.

Specifies in softphone mode if the Ignore button appears for an incoming call in a hunt group.

true (default)— Ignore button doesn't appear for an incoming call in a hunt group.

false— Ignore button appears for an incoming call in a hunt group.

Example: <PreventDeclineOnHuntCall>true</PreventDeclineOnHuntCall>

## PrintIMEnabled

Applies to Cisco
                              		  Jabber for Windows.

true
                                       				(default)—Users can print conversations from the chat window by right-clicking
                                       				and selecting Print .

false—Users
                                       				cannot print conversations from the chat window. If they right-click inside the
                                       				window, the Print option is not in the menu.

Example: <PrintIMEnabled>false</PrintIMEnabled>

## ProfileProtocolRateLimit

Applies to Cisco
                              		  Jabber for Android on Synergy devices.

Specifies the
                              		  number of times that users can launch the Profile screen of a contact from
                              		  other applications. For example, if the ProfileProtocolRateLimit is three times, and the ProfileProtocolTimeLimit is 15 seconds, then a user
                              		  can start the launch of the Profile screen of a contact from other
                              		  applications three times every 15 seconds.

You can set the
                              		  value between 1 to 100. The default value is 3.

Example: <ProfileProtocolRateLimit>10</ProfileProtocolRateLimit>

## ProfileProtocolTimeLimit

Applies to Cisco
                              		  Jabber for Android on Synergy devices.

Specifies the
                              		  time limit for users to launch the Profile screen of a contact from other
                              		  applications. You can set the value between 1 to 300 seconds. The default value is
                              		  15 seconds.

Example: <ProfileProtocolTimeLimit>10</ProfileProtocolTimeLimit>

## ProvisionProtocolRateLimit

Applies to Cisco
                              		  Jabber for Android.

Specifies the
                              		  number of times the URL provision protocol can be initiated.

For example, if
                              		  the ProvisionProtocolRateLimit is 3 times, and the ProvisionProtocolTimeLimit is 15 seconds, then a user
                              		  can launch Cisco Jabber with the URL provision three times every 15 seconds.

You can set the
                              		  value between 1 to 100. The default value is 3.

Example: <ProvisionProtocolRateLimit>10</ProvisionProtocolRateLimit>

## ProvisionProtocolTimeLimit

Applies to Cisco
                              		  Jabber for Android.

Specifies the time
                              		  within which the URL provision protocol can be initiated. You can set the value
                              		  between 1 to 300 seconds. The default value is 15 seconds.

Example: <ProvisionProtocolTimeLimit>10</ProvisionProtocolTimeLimit>

## Push_Notification_Enabled

Applies to Cisco Jabber for iPhone and iPad.

Specifies if Cisco Jabber receives push notifications whenever there is a new IM, even if Cisco Jabber is inactive.

The option to set an automatic away timer is not available when push notifications are enabled.

true (default)—Push notifications are enabled whenever there is a new IM.

false—Push notifications are disabled.

Example <Push_Notification_Enabled>false</Push_Notification_Enabled

## Recent_Chats_Enabled

Applies to Cisco Jabber for Windows.

Determines whether the Chats tab is available on the Hub window. This parameter is not applicable in phone-only deployments.

true (default)—the Chats tab is shown on the Hub window.

false—the Chats tab is not shown on the Hub window.

Example: <Recent_Chats_Enabled>false</Recent_Chats_Enabled>

## RecordingToneInterval

Applies to all clients

Specifies the milliseconds between consecutive tones.

The range is 8000-32000 and defaults to 11500.

Example: <RecordingToneInterval>true</RecordingToneInterval>

See EnableRecordingTone for details on properly configuring recording tones.

## RememberChatList

Applies to Cisco Jabber for mobile clients.

Specifies if the user's chat list is saved and restored after relaunching Jabber.

on (default)—If you set the parameter as on or if you leave it empty, then the user's chat list is saved and restored after relaunching Jabber. Also, Save chat list option is available in the client.

off—User's chat list is not saved, and Save chat list option is not available the client.

```
<RememberChatList>on</RememberChatList>
```

## RemoteDestinationEditingWithMultipleDevices

Applies to Cisco
                              		  Jabber for Windows.

Allows you to
                              		  determine whether users with multiple devices can edit or add remote
                              		  destinations.
                              		 For more information, see Configure Extend and Connect chapter from the document On-Premises Deployment for Cisco Jabber .

true
                                    				(default)—Users with multiple devices can edit or add remote destinations.

false—Users
                                    				with multiple devices cannot edit or add remote destinations.

Example: <RemoteDestinationEditingWithMultipleDevices>false</RemoteDestinationEditingWithMultipleDevices>

## RemotePRTServer

Applies to Cisco Jabber for Windows and Mac

Specifies the script that uploads the PRT logs to your server when your administrator generates the logs through the Phone list in Unified CM Administration .

Example: <RemotePRTServer>http:// server path /UploadZIP.php</RemotePRTServer>

## SaveLogToLocal

Applies to mobile clients.

Enables the Send logs to button in the Problem
                                 reporting window.

true  (default) —User can save logs.

false — Button is not available.

Example: <SaveLogToLocal>True</SaveLogToLocal>

## ScreenShareAuditMessages

Applies to Cisco Jabber for Windows

Enables Jabber clients to send information about all user actions to the Presence server for compliance or auditing purposes.

If you also have an active compliance server, the Presence server sends the information to compliance server.

true—Jabber sends information to the Presence server about user actions during IM-only screen sharing.

false (default)—Jabber doesn’t send any information to the Presence server about user actions during IM-only screen sharing.

If you want to enable this feature, ensure that all Jabber clients are running at least release 11.0(1). For clients earlier
                                          than 11.0(1), the collected information during IM-only screen sharing is sent to the clients as instant messages.

Example: <ScreenShareAuditMessages>true</ScreenShareAuditMessages>

## selfcareURL

Specifies the
                              		  fully qualified domain name (FQDN) of Cisco Unified Communications Manager
                              		  service.

Defines the URL
                              		  for the Self Care Portal when no default service profile is selected in Cisco
                              		  Unified Communications Manager.

Example: <selfcareURL> http://server_name/selfcareURL </selfcareURL>

## SelfMuteTone

Applies to Cisco Jabber for Windows and Cisco Jabber for Mac.

Determines whether Jabber plays an audio tone when the user mutes or unmutes  their own microphone. This tone can be heard
                              only by the user themselves, not the other participants in a call or meeting.

true (default)—The tone plays when the user mutes or unmutes their microphone.

false—The tone does not play when the user mutes or unmutes their microphone.

## ServiceDiscoveryExcludedServices

Applies to all
                              		  Cisco Jabber clients.

Specifies whether to exclude certain services from Service Discovery.

WEBEX—When you set this value, the client:

Does not perform CAS lookup

Looks for _cisco-uds , _cuplogin , and _collab-edge .

CUCM—When you set this value, the client:

Does not look for _cisco_uds

Looks for _cuplogin and _collab-edge .

You can specify
                              		  multiple, comma-separated values to exclude multiple services.

Example: <ServiceDiscoveryExcludedServices> WEBEX,CUCM
                                 			 </ServiceDiscoveryExcludedServices>

## ServicesDomainSsoEmailPrompt

Applies to all the Cisco Jabber clients.

ON—The prompt
                                       				is shown.

OFF
                                       				(default)—The prompt is not shown.

Example: <ServicesDomainSsoEmailPrompt>ON</ServicesDomainSsoEmailPrompt>

## SharePortRangeSize

Applies to Cisco Jabber for Windows.

Specifies the size of the port range, when used with the SharePortRangeStart parameter. The minimum value is 40. The default is 16383. The value when added to the SharePortRangeStart parameter cannot exceed 65535.

For more
                              		  information on port ranges, see the topic on Ports and
                                 			 Protocols in the Planning Guide for Cisco Jabber .

```
<Policies> 
<SharePortRangeStart>45130</SharePortRangeStart> 
<SharePortRangeSize>100</SharePortRangeSize> 
</Policies>
```

## SharePortRangeStart

Applies to Cisco Jabber for Windows.

This parameter is
                              		  used with SharePortRangeSize to specify a port range to use
                              		  when users share their screen from a chat window.

If you do not
                              		  configure these parameters, then the client uses the default port range for IM
                              		  screen share, 49152 to 65535. For more information on default port ranges, see
                              		  the topic on Ports and
                                 			 Protocols in the Cisco Jabber
                                 			 Planning Guide .

The value you enter specifies the start of the port range. The minimum
                              		  value is 1024. The value cannot exceed 65535 minus the SharePortRangeSize .

```
<Policies> 
<SharePortRangeStart>45130</SharePortRangeStart> 
<SharePortRangeSize>100</SharePortRangeSize> 
</Policies>
```

## ShareProtocolRateLimit

Applies to Cisco
                              		  Jabber for Android.

Specifies the
                              		  number of times sharing files or messages can be initiated. For example, if
                              		  the ShareProtocolRateLimit is 3, and the ShareProtocolTimeLimit is 15 seconds, then a user can
                              		  start files sharing or message sharing on Cisco Jabber three times every 15 seconds.

You can set the
                              		  value between 1 to 100. The default value is 3.

Example: <ShareProtocolRateLimit>10</ShareProtocolRateLimit>

## ShareProtocolTimeLimit

Applies to Cisco
                              		  Jabber for Android.

Specifies the time
                              		  within which sharing files or messages can be initiated. You can set the value
                              		  between 1 to 300 seconds. The default value is 15 seconds.

Example: <ShareProtocolTimeLimit>10</ShareProtocolTimeLimit>

## ShowSelfCarePortal

Applies to Cisco Jabber for desktop clients.

Determines whether the Self Care Portal tab displays in the Options dialog.

true (default)—the Self Care Portal tab displays in the Options dialog.

false—the Self Care Portal tab does not display  in the Options dialog

Example: <ShowSelfCarePortal>false</ShowSelfCarePortal>

## SoftPhoneModeWindowBehavior

Applies to Cisco
                              		  Jabber for Windows.

OnVideo—Conversation window is only displayed for video calls.

OnCall
                                       				(default)—Conversation window is always displayed when a call is answered.

Never—Conversation window is never displayed when a call is
                                       				answered.

Example: <SoftPhoneModeWindowBehavior>Never</SoftPhoneModeWindowBehavior>

## TelemetryCustomerID

Applies to all the Cisco Jabber clients.

Mac OS X -
                                       				uuidgen

Linux -
                                       				uuidgen

Microsoft
                                       				Windows - [guid]::NewGuid().ToString() or (from cmd.exe) powershell -command
                                       				"[guid]::NewGuid().ToString()"

Online -
                                       				guid.us

This identifier
                              		  must be globally unique regardless of the method used to create the GUID.

Example: <TelemetryCustomerID> customerIdentifier </TelemetryCustomerID>

## TelemetryEnabled

Applies to all Cisco Jabber clients.

true
                                       				(default)—Analytics data will be gathered.

false—Analytics data will not be gathered.

Example: <TelemetryEnabled>false</TelemetryEnabled>

## TelemetryEnabledOverCellularData

Applies to Cisco Jabber for mobile clients.

true
                                       				(default)—Analytics data will be sent over Wi-Fi and mobile data connections.

false—Analytics data will be sent over Wi-Fi connections only.

Example: <TelemetryEnabledOverCellularData>false</TelemetryEnabledOverCellularData>

## Telephony_Enabled

Applies to all Cisco Jabber clients.

true
                                       				(default)—Enables audio and video capabilities and user interface.

false—Disables
                                       				audio and video capabilities and user interface.

If your client is
                              		  enabled for IM-only mode, then you must set this parameter to false. If you do
                              		  not set this parameter in IM-only mode deployments, then users may see disabled
                              		  telephony capabilities on their user interface.

Example: <Telephony_Enabled>false</Telephony_Enabled>

## TelephonyProtocolRateLimit

Applies to Cisco Jabber for Windows, Mac, and Android.

Specifies the
                              		  number of times a call can be initiated from one of the telephony protocol
                              		  handlers (tel: ciscotel, sip). For example, if the TelephonyProtocolRateLimit is 2, and the TelephonyProtocolTimeLimit is 10 seconds, then a user
                              		  can start a call from one of the telephony protocol handlers two times every
                              		  10 seconds.

You can set the
                              		  value between 1 to 100. The default value is 2.

Example: <TelephonyProtocolRateLimit>10</TelephonyProtocolRateLimit>

## TelephonyProtocolTimeLimit

Applies to Cisco Jabber for Windows, Mac, and Android.

Specifies the time within which a user can start a call from one of the telephony protocol handlers (sip, tel, ciscotel) before
                              the TelephonyProtocolRateLimit is hit or reset. The default value for initiating a call from one of the telephony protocol handlers is 10 seconds for every
                              two attempts. You can set the value between 1-300 seconds.

Example: <TelephonyProtocolTimeLimit>10</TelephonyProtocolTimeLimit>

## UserDefinedRemoteDestinations

Applies to Cisco Jabber for Windows.

Lets users add,
                              		  edit, and delete remote destinations through the client interface. Use this
                              		  parameter to change the default behavior when you provision Extend and Connect
                              		  capabilities.

By default, if a
                              		  user's device list contains only a CTI remote device, the client does not let
                              		  that user add, edit, or delete remote destinations. This occurs to prevent
                              		  users from modifying dedicated remote devices that you assign. However, if the
                              		  user's device list contains a software device or a desk phone device, the
                              		  client lets users add, edit, and delete remote destinations.

true—Users can
                                    				add, edit, and delete remote destinations.

false
                                    				(default)—Users cannot add, edit, and delete remote destinations.

Example: <UserDefinedRemoteDestinations>true</UserDefinedRemoteDestinations>

## UserEnabledDetailedLogging

Applies to mobile clients.

Enables the Detailed logging option in the Problem
                                 reporting window.

true  —User can select detailed logging.

false (default) — Option is not available.

Example: <UserEnabledDetailedLogging>True</UserEnabledDetailedLogging>

## Voicemail_Enabled

true
                                       				(default)—Enables voicemail capabilities and user interface.

false—Disables
                                       				voicemail capabilities and user interface.

Example: <Voicemail_Enabled>false</Voicemail_Enabled>

## VoiceServicesDomain

Specifies the Fully Qualified Domain Name that represents the DNS domain where the DNS SRV records for _collab-edge and _cisco-uds are configured.

Example: Given the following DNS SRV records:

_ collab-edge ._tls.voice.example.com

_ cisco-uds ._tcp.voice.example.com

The VoiceServicesDomain value will be voice.example.com .

Don't configure this parameter for MRA when your voice services domain is the same as the sign-in account domain. For deployments
                                          with MRA, only configure this parameter if the domains are different.

## WhitelistBot

Applies to all the Cisco Jabber clients.

Only Bots listed in WhitelistBot are allowed to start group chats,conference calls or join instant meetings. If WhitelistBot
                              configuration parameter is not defined, the default will be the JIDs defined in AdminConfiguredBot .

Cisco Jabber allows regular expressions in WhitelistBot, like the * special character. For example * would open "robot-type"
                              messages coming from any client, or {bot}*{@cisco.com} would whitelist JIDs beginning with bot, for example, bot1@cisco.com,
                              bot_thisworks@cisco.com.

Example: <WhitelistBot>bot1@example.com;bot2@example.com;bot3@example.com</WhitelistBot>

| Important | Only Jabber clients from Release 12.9 forward recognize this parameter. For example, if a Release 12.8(1) client reads this
                                          parameter in the jabber-config.xml , the client ignores it. So, this parameter only becomes effective after your users have installed at least Release 12.9 clients. If you use the UpdateUrl parameter to have your Unified Communications Manager TFTP server auto-update Jabber, Jabber ignores BlockVersionBelow . |
|---|---|

| Note | Multiple device  messaging does not support file transfer or screen captures. Files are available only on the active devices
                                          that sent or received the files. |
|---|---|

| Note | When set to false, call control buttons on some headsets don’t work. |
|---|---|

| Note | These parameters interact for calendar integration and contact resolution: CalendarIntegrationType EnableLocalAddressBookSearch EnableLotusNotesContactResolution See the Feature Configuration for Cisco Jabber guide for details. |
|---|---|

| Note | The EnableLocalAddressBookSearch parameter must also be
                                                				  set to true. |
|---|---|

| Note | These parameters interact for calendar integration and contact resolution: CalendarIntegrationType EnableLocalAddressBookSearch EnableLotusNotesContactResolution See the Feature Configuration for Cisco Jabber guide for details. |
|---|---|

| Note | If Cisco Jabber is deployed in Full UC mode, the user will receive this notification only once after it's been enabled. If
                                             Cisco Jabber is deployed in a Phone-only mode, the notification will be displayed only if a mobile device has been configured
                                             for the user. |
|---|---|

| Note | Enable the Unified CM service parameter to play recording notification tones before adding the Jabber recording tone parameters.
                                          See the monitoring and recording chapter of the Features and Services Guide for Cisco Unified Communications Manager for details. |
|---|---|

| Note | Default value changed to "true" in Release 12.6 to support meeting controls for Webex Collaboration Meeting Rooms. |
|---|---|

| Note | The CiscoTelProtocolPermissionEnabled parameter replaces
                                             			 the EnableTelProtocolPopupWindow parameter. Both
                                             			 parameters are supported in the client, however the dialog box is disabled if of the
                                             			 either parameter is set to false. |
|---|---|

| Note | You can't set an automatic away timer when you have enabled push notifications. |
|---|---|

| Note | This parameter
                                             				does not take effect when users connect to the corporate network through
                                             				Expressway for Mobile and Remote Access. In this case, UDS provides contact
                                             				resolution and the client cannot query the directory. |
|---|---|

| Note | You can also use BlockVersionBelow to stop users from signing in with clients that are earlier than a specified release. BlockVersionBelow is more effective in BYOD deployments where users can disable autoupgrading on their device. |
|---|---|

| Note | This parameter does not apply to Jabber deployed in a Virtual environment. |
|---|---|

| Note | If you also have an active compliance server, the Presence server sends the information to compliance server. |
|---|---|

| Note | If you want to enable this feature, ensure that all Jabber clients are running at least release 11.0(1). For clients earlier
                                          than 11.0(1), the collected information during IM-only screen sharing is sent to the clients as instant messages. |
|---|---|

| Note | Only one protocol handler can be processed at one time. Any other protocol handler arriving when the user already has a call
                                       alert are either discarded or queued up. |
|---|---|

| Note | Don't configure this parameter for MRA when your voice services domain is the same as the sign-in account domain. For deployments
                                          with MRA, only configure this parameter if the domains are different. |
|---|---|