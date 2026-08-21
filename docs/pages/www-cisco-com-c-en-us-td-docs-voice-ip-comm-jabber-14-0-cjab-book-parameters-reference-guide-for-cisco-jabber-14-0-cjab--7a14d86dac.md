---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-book-parameters-reference-guide-for-cisco-jabber-14-0-cjab--7a14d86dac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_book_parameters-reference-guide-for-cisco-jabber-14_0/cjab_b_parameter-reference-guide-jabber-129_chapter_0100.html
retrieved_at: 2026-08-21T21:02:57.199830+00:00
---

Parameters Reference Guide for Cisco Jabber 14.0

# Parameters Reference Guide for Cisco Jabber 14.0

Updated: March 29, 2021

Chapter: Options

## Chapter: Options

# Options

## AdminConfiguredBot

Applies to Cisco Jabber desktop, iPhone, and iPad clients.

Automatically adds bots to users' contacts list in Jabber, using the Jabber ID assigned to the bot in the company directory.
                              A group _BotGroup is created in the users' contacts list. Your users can also add bots manually to their contacts lists.

```
<AdminConfiguredBot>bot1@example.com;bot2@example.com;bot3@example.com</AdminConfiguredBot>
```

## AllowUserCustomTabs

Applies to Cisco Jabber for desktop and mobile clients.

Specifies if users can create custom embedded tabs in the client.

For mobile clients, you can add any number of custom tabs, but only 10 custom tabs appear in the client. If you have added
                              10 custom tabs in the client, then the users cannot add anymore custom tabs.

true (default)—Menu option to create custom tabs is shown in the client.

false— Menu option to create custom tabs is not shown in the client.

Example: <AllowUserCustomTabs>false</AllowUserCustomTabs>

## BrowserEngineForCustomTab

Applies to Cisco Jabber for Windows

Jabber uses Chrome as the default browser engine for custom tabs. But, the Chrome engine might not work well in some deployments.

In Release 12.6(2) and later, you can choose the browser engine for custom tabs with BrowserEngineForCustomTab . The allowed values are:

Chrome (default)—Use Chrome as the browser engine for custom tabs.

IE—Use IE as the browser engine for custom tabs.

Example: <BrowserEngineForCustomTab>Chrome</BrowserEngineForCustomTab>

## CalendarAutoRefreshTime

Applies to Cisco Jabber for Desktop clients .

Defines the number of minutes after which integrated calendars refresh. The default value is zero, meaning that the calendars
                              do not automatically refresh. This configuration key only works for Google Calendar and IBM Notes calendar integration.

The default value for Mac is five, which means calendars automatically refresh every five seconds. This configuration key
                                 only works for Exchange calendar integration.

A high frequency refresh may affect performance of the IBM Lotus Notes server.

Example: <CalendarAutoRefreshTime>0</CalendarAutoRefreshTime>

## CalendarIntegrationType

Applies to Cisco Jabber for Windows.

This parameter works with the Meetings_Enabled parameter.

0—Disables calendar integration in the Meetings tab of the client user interface. If you disable this parameter, the Meetings
                                    tab in the client is empty, but the Meetings tab remains on the hub window.

1—Enables Microsoft Outlook calendar integration in the Meetings tab of the client user interface.

2—Enables IBM Lotus Notes calendar integration in the Meetings tab of the client user interface.

3—Enables Google Calendar integration in the Meetings tab of the client user interface.

Restart Cisco Jabber to apply the changes.

Example: <CalendarIntegrationType>1</CalendarIntegrationType>

Client users can override this setting on the Calendar tab of the Options dialog.

These parameters interact for calendar integration and contact resolution:

CalendarIntegrationType

EnableLocalAddressBookSearch

EnableLotusNotesContactResolution

See the Feature Configuration for Cisco Jabber guide for details.

## Callhistory_Expire_Days

Applies to all clients.

Specifies the number of days before the call history is deleted. The maximum number of records stored is 250.

If the value is zero or not specified, then the call history will store the maximum number of call records, which is 250.

Example: <Callhistory_Expire_Days>2</Callhistory_Expire_Days>

The oldest item is deleted when call history items reach the count 250 or specified expire days.

## ConfigRefetchInterval

Applies to Cisco Jabber for all clients.

Specifies the interval in hours when Jabber fetches a fresh configuration from the server. Jabber picks a random re-fetch
                              point within an hour before or after the specified value. For example, for a value of 5, Jabber will choose a random time
                              between 4 and 6 hours. Minimum value is 4.

The default value is 8 hours.

## ConfMediaType

Applies to all clients.

Specifies the conference invitation type for Cisco Collaboration Meeting Rooms.

BridgeOnly—The join button joins the conference using SIP.

WebExOnly—The join button joins the conference using Webex .

Nothing defined—The join button joins the conference using SIP and the link joins the conference using Webex .

Example: <ConfMediaType>WebExOnly</ConfMediaType>

## Disable_Meeting_SSO_Browser_Cache

Applies to Cisco Jabber for Mac

Specifies the users to enable or disable the browser cache for meeting SSO SessionTicket.

true—The browser cache is disabled.

false (default)—The browser cache is enabled.

## DisableClientConfigExchangeServer

Applies to Cisco Jabber for Windows and Cisco Jabber for Mac.

Disables client settings for InternalExchangeServer and ExternalExchangeServer, and forces to use InternalExchangeServer and
                              ExternalExchangeServer on TFTP server.

true—Disables client settings for InternalExchangeServer and ExternalExchangeServer.

false(default)—Enables client settings for InternalExchangeServer and ExternalExchangeServer

```
<DisableClientConfigExchangeServer>true</DisableClientConfigExchangeServer>
```

## DockedWindowPosition

Applies to Cisco Jabber for Windows.

TopCenter
                                       				(default)—The position of the docked window is at the top center of the screen.

TopLeft—The
                                       				position of the docked window is at the top left of the screen.

TopRight—The
                                       				position of the docked window is at the top right of the screen.

Example: <DockedWindowPosition>TopLeft</DockedWindowPosition>

## DockedWindowVisible

Applies to Cisco Jabber for Windows.

true
                                       				(default)—The docked window displays when the client starts.

false—The
                                       				docked window does not display when the client starts.

Example: <DockedWindowVisible>false</DockedWindowVisible>

## EnableBridgeConferencing

Applies to all Cisco Jabber clients.

true—Conference service options are shown in the client.

false(default)—Conference service options are not shown in the
                                       				client.

Example: <EnableBridgeConferencing>true</EnableBridgeConferencing>

## EnableCalendarIntegration

Applies to Cisco Jabber for mobile clients.

Specifies if the meeting option is available in the client.

true—The meeting option is available in the client. All events, in the user's device calendar, are integrated with Jabber.

false (default)—The meeting option is not available in the client.

```
<EnableCalendarIntegration>true</EnableCalendarIntegration>
```

## EnableLoadAddressBook

Applies to Cisco Jabber for mobile clients.

Specifies if
                              		  the native contacts in the phone are loaded on Cisco Jabber contact list or not.

true(default)—Native contacts are loaded on the Cisco Jabber contact list.

false—Native contacts are not loaded the Cisco Jabber contact list.

Example: <EnableLoadAddressBook>true</EnableLoadAddressBook>

## EnableProximity

Applies to Cisco Jabber for Windows and Mac.

Enables Jabber clients to connect to proximity-enabled devices, and then share their screen wirelessly. Proximity is enabled
                              by ultrasound listening. The ultrasound audio capturing requires 48KHz sample rate. Microphones need to be unmuted for ultrasound
                              audio capturing to work. If a Bluetooth headset is used, it may impact the device detection.

Supported devices include Cisco MX, SX, DX, IX, and Cisco Webex Room Series endpoints. The devices have maximum connection
                              limitations. If the connection is full, new pairing requests will not be accepted until someone else disconnects from the
                              device.

true (default)—Users can pair to proximity-enabled devices.

false—Users can't pair to proximity-enabled devices.

Example: <EnableProximity>true</EnableProximity>

## EnableSaveChatHistoryToExchange

Applies to Cisco Jabber for Windows and Mac for on-premises and Office 365 deployments.

Enables the client
                              		  to automatically save chat histories to a Cisco Jabber Chats folder in users'
                              		  Microsoft Outlook application.

true—Enables saving chat history to an Outlook folder.

false (default)—Does not save chat history to an Outlook folder.

Example: <EnableSaveChatHistoryToExchange>true</EnableSaveChatHistoryToExchange>

## EnableVoipSocket

Applies to Cisco Jabber for iPhone and iPad.

We deprecated this parameter as of August 2020 because of changes in Apple Push Notifications (APNs). We have closed the VoIP
                                          socket.

Specifies if Jabber uses the VoIP sockets to set up SIP connection with Cisco Unified Communication Manager server. Even if
                              Jabber is inactive, Jabber refreshes the keep alive timer parameter to re-register the Cisco Unified Communication Manager
                              server to keep SIP registered through the VoIP sockets.

If you're using APNs, Jabber users will always receive calls in Jabber even if their Jabber app is inactive. If you're not
                              using APNs, then set this parameter to true to ensure Jabber users receive their calls even if their app is inactive.

Jabber will be registered in the Cisco UC Manager device page until the TCP connection times out by iOS.

true(default) —VoIP sockets and keep alive timers are enabled to ensure Jabber will receive calls even if it's inactive.

false—VoIP sockets and keep alive timers are disabled. We recommend you only set the value to false if APNs are enabled. Otherwise,
                                    if you set this parameter to false, the SIP connections with Cisco Unified Communication Manager close after a short period,
                                    which is controlled by the operating system, and Jabber becomes inactive.

Cisco Jabber will automatically sign users out if the parameter value is changed.

Example: <EnableVoipSocket>true</EnableVoipSocket>

## Exchange_UseCredentialsFrom

Applies to Cisco Jabber for desktop clients.

Cannot be used with Office 365 deployments.

An authentication
                              		  method to the Microsoft Exchange server. To save chat history to a Microsoft Outlook folder,
                              		  it synchronizes the Exchange credentials using one of the following
                              		  Authenticator argument credentials for users:

CUP—Use IM and Presence Service
                                    				credentials for Exchange

CUCM—Use Cisco Unified Communications Manager
                                    				credentials for Exchange

WEBEX—Use Webex credentials for Exchange

Example: <Exchange_UseCredentialsFrom>CUCM</Exchange_UseCredentialsFrom> .

## ExchangeAuthenticateWithSystemAccount

Applies to Cisco Jabber for Windows.

An authentication method to the Microsoft Exchange server. To save chat history to a Microsoft Outlook folder, the parameter
                              enables the client to use the operating system account details of the signed-in user to authenticate with the Exchange server.
                              This authentication method uses the Windows NT LAN Manager (NTLM) security protocol.

true (default)—The client uses the operating system account details of the user to authenticate to the Exchange server.

false—The client does not use the user's operating system account details to authenticate to the Exchange server. Instead,
                                    users must enter their credentials in the Outlook tab of the Options dialog.

If ExchangeModernAuthentication is enabled, Jabber ignores ExchangeAuthenticateWithSystemAccount .

Example: <ExchangeAuthenticateWithSystemAccount>false</ExchangeAuthenticateWithSystemAccount>

## ExchangeAutodiscoverDomain

Applies to Cisco Jabber for Windows and Mac on-premises deployments.

Specifies the domain that the client uses to search for the Exchange server. This is used when the domain of the exchange
                              server is different to the domain of the users credentials.

Define the value
                              		  of the parameter as the domain to discover the Exchange server. The client uses
                              		  the domain to search for the Exchange server at one of the following web
                              		  addresses:

https://<domain>/autodiscover/autodiscover.svc

https://autodiscover.<domain>/
                                 			 autodiscover/autodiscover.svc

If ExchangeModernAuthentication is enabled, Jabber ignores ExchangeAutodiscoverDomain .

Jabber gives priority to the Microsoft Exchange server discovery parameters in this order:

EmailAsExchangeDiscoverDomain

ExchangeAutodiscoverDomain

ExchangeDomain

Example: <ExchangeAutodiscoverDomain> domain </ExchangeAutodiscoverDomain>

## ExchangeDomain

Applies to Cisco Jabber for desktop clients.

Specifies the domain of the Microsoft Exchange server. This parameter works with the Exchange_UseCredentialsFrom parameter as shown in the following example:

Exchange_UseCredentialsFrom = CUCM (where the username is in the format username@domain.com)

ExchangeDomain = otherdomain.com

In this case, username@otherdomain.com is used to authenticate with the Exchange server.

Use this parameter in the following scenarios:

If you have different domains for the Exchange Server and Cisco Unified Communications Manager.

If your Cisco Unified Communications Manager is pre 10.5 Release and you want to authenticate with Office 365. In pre 10.5
                                    Cisco Unified Communications Manager, credentials do not contain a domain, however authentication with Office 365 does require
                                    a domain. Use this parameter to set a domain for the Exchange server.

For Cisco Jabber for Windows, this parameter does not have any effect if the ExchangeAuthenticateWithSystemAccount parameter is set to true.

Jabber gives priority to the Microsoft Exchange server discovery parameters in this order:

EmailAsExchangeDiscoverDomain

ExchangeAutodiscoverDomain

ExchangeDomain

## ExchangeModernAuthentication

Applies to Cisco Jabber for desktop clients.

Determines whether Jabber uses modern authentication to authenticate to the Exchange servers.

Set the key to true to enable Office 365 autodiscover and modern authentication to the Exchange service in Office 365 deployments.

When ExchangeModernAuthentication is enabled, Jabber ignores these parameters: ExchangeAuthenticateWithSystemAccount , ExchangeAutodiscoverDomain , InternalExchangeServer , ExternalExchangeServer .

true—modern authentication is enabled.

false (default)—modern authentication is disabled

## ExternalExchangeServer

Applies to Cisco Jabber for desktop clients.

Specifies the Exchange server address, the client uses this server when saving chat history to an Outlook folder.

If ExchangeModernAuthentication is enabled, Jabber ignores ExchangeAuthenticateWithSystemAccount .

Example: <ExternalExchangeServer>external_exchange_server</ExternalExchangeServer>

## HeadsetPreference

Applies to Cisco Jabber for Windows and Mac

Specifies whether Cisco Jabber adds a new audio device to the top or bottom of the device priority list. The device priority
                              list is in the Advanced audio settings.

PreferNewDevice (default)—Cisco Jabber adds the new audio device to the top of the list, and makes it the preferred device.

PreferOldDevice—Cisco Jabber adds a new audio device to the bottom of the list, with no change to the configured preferred
                                    device.

This parameter replaces the deprecated HeadsetPreferenceOnVDI parameter.

Example:

```
<HeadsetPreference>PreferOldDevice</HeadsetPreference>
```

## InternalExchangeServer

Applies to Cisco Jabber for desktop clients.

Method of specifying server address. To save chat history to an Outlook folder, manually defines the internal Exchange server.

If ExchangeModernAuthentication is enabled, Jabber ignores InternalExchangeServer .

Example: <InternalExchangeServer>Internal_exchange_server</InternalExchangeServer>

## lastselectedline

Applies to Cisco Jabber for Windows and Mac

Specifies the last selected line on a multiline phone.

Example:

```
<lastselectedline>Line3: 332102</lastselectedline>
```

## Location_Enabled

Applies to Cisco Jabber for desktop clients.

Specifies whether the Location tab is displayed in Jabber settings or not. The location tab is used for location-related settings.

true (default)—The Location tab is shown in the client.

false—The Location tab is not shown in the client.

Example: <Location_Enabled>false</Location_Enabled>

## LOCATION_MATCHING_MODE

Applies to Cisco Jabber for desktop clients.

Determines how the client detects the current network locations for the Location feature.

MacAddressOnly (default)—The client uses the Mac address of the network default gateway.

MacAddressWithSubnet—The client uses a unique pair of subnet addresses and Mac address of the default gateway.

Example: <LOCATION_MATCHING_MODE>MacAddressWithSubnet</LOCATION_MATCHING_MODE>

## Location_Mode

Applies to Cisco Jabber for desktop clients.

Specifies whether the Location feature is enabled and whether users are notified when new locations are detected.

ENABLED (default)—Location feature is turned on. Users are notified when new locations are detected.

DISABLED—Location feature is turned off. Users are not notified when new locations are detected.

ENABLEDNOPROMPT—Location feature is turned on. Users are not notified when new locations are detected.

Example: <Location_Mode>DISABLED</Location_Mode>

## MacCalendarIntegrationType

Applies to Cisco Jabber for Mac.

This parameter works with the Meetings_Enabled parameter to specify which type of calendar to integrate with Jabber.

0—Disables calendar integration in the Meetings tab of the client. If you disable this parameter, the Meetings tab stays in the client but is empty.

1— (Default) Enables Microsoft Outlook calendar integration in the Meetings tab of the client.

2—Enables Mac Calendar integration in the Meetings tab of the client.

3—Enables Google Calendar integration in the Meetings tab of the client.

Example: <MacCalendarIntegrationType>2</MacCalendarIntegrationType>

## multiline1_ringtonename Through multiline8_ringtonename

Applies to Cisco Jabber for Windows and Mac

Specifies the ringtone to use for a particular line on a multiline phone. You can specify ringtones for up to eight lines.

Example: This example sets the ringtone for the third line on the phone.

```
<multiline3_ringtonename>Playful</multiline3_ringtonename>
```

## RefreshCustomTabsOnNetworkChange

Applies to desktop clients

Specifies if Jabber refreshes a custom tab that failed to load due to a network issue.

true—Jabber refreshes custom tabs that experienced a loading error when the network changes.

false (default)—Jabber doesn't refresh custom tabs that experienced a loading error when the network changes.

Example: <RefreshCustomTabsOnNetworkChange>true</RefreshCustomTabsOnNetworkChange>

## SaveChatHistoryToExchangeOperationMode

Applies to Cisco Jabber for desktop clients.

Replaces the EnableSaveChatHistoryToExchange parameter.

Specifies if
                              		  users can save chat history to a Cisco Jabber Chats folder in users'
                              		  Microsoft Outlook application.

DisabledByPolicy (default)—Users cannot save chat history to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is not visible in the client.

EnabledByPolicy—Chats are saved to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is visible in the client, but users cannot access it.

With this
                                                				  option, you must set up a method of authentication for the client to
                                                				  authenticate with the Exchange server. You can choose to authenticate using
                                                				  single sign-on, or by Synching credentials. For more information, see the On-Premises Deployment for Cisco Jabber .

DisabledByDefault—Users can save chats to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is unchecked in the client, but users can change it.

EnabledByDefault—Users can save chats to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is checked in the client, but users can change it.

OnPremOnlyByPolicy—Chats are saved to Microsoft Outlook only when Jabber is on the corporate network. Jabber doesn’t save
                                    chats to Outlook over MRA. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is visible on the Outlook tab of the Options menu, but it is greyed out and users cannot change it.

OnPremOnlyByDefault—Users have the option to save chats to Microsoft Outlook only when Jabber is in corporate network. Jabber
                                    doesn't save chats to Outlook over MRA. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is checked on the Outlook tab of the Options menu, but users can change it.

Example: <SaveChatHistoryToExchangeOperationMode>EnabledByDefault</SaveChatHistoryToExchangeOperationMode>

## Set_Status_Away_On_Inactive

true
                                       				(default)—Availability status changes to Away when users are inactive.

false—Availability status does not change to Away when users are inactive.

Example: <Set_Status_Away_On_Inactive>false</Set_Status_Away_On_Inactive>

## Set_Status_Away_On_Lock_OS

Applies to Cisco Jabber for Windows.

true
                                       				(default)—Availability status changes to Away when users lock their operating systems.

false—Availability status does not change to Away when users lock their operating systems.

Example: <Set_Status_Away_On_Lock_OS>false</Set_Status_Away_On_Lock_OS>

## Set_Status_Inactive_Timeout

Sets the amount of
                              		  time, in minutes, before the availability status changes to Away if users are inactive.

The default value
                              		  is 15.

Example: <Set_Status_Inactive_Timeout>10</Set_Status_Inactive_Timeout>

## ShowContactPictures

true
                                       				(default)—Contact pictures display in the contact list.

false—Contact
                                       				pictures do not display in the contact list.

Example: <ShowContactPictures>false</ShowContactPictures>

## ShowOfflineContacts

Applies to Cisco Jabber for Windows and mobile clients only.

true
                                       				(default)—Offline contacts display in the contact list.

false—Offline
                                       				contacts do not display in the contact list.

Example: <ShowOfflineContacts>false</ShowOfflineContacts>

## ShowTabLabel

Applies to Cisco Jabber for desktop clients.

By default in Release 12.6, the client didn't display tab labels in the hub window. Users can enable tab labels through their
                              preferences.

If you want to change the default behavior for displaying tabs, use the ShowTabLabel parameter. The allowed values are:

true—The client displays the tab labels.

false (default)—The client doesn't display the tab labels.

Example: <ShowTabLabel>true</ShowTabLabel>

## Start_Client_On_Start_OS

Applies to Cisco Jabber for Windows.

Specifies if the client starts automatically when the operating system starts.

true—The client starts automatically.

false (default)—The client does not start automatically.

Example: <Start_Client_On_Start_OS>true</Start_Client_On_Start_OS>

## StartCallWithVideo

Specifies how calls start when users place calls. Calls can start with audio only or audio and video.

true (default)—Calls always start with audio and video.

false—Calls always start with audio only.

Example: <StartCallWithVideo>false</StartCallWithVideo>

Server settings take priority over this parameter in the client configuration file. However, if users change the default option
                                          in the client user interface, that setting takes priority over both the server and client configurations.

For Cisco Unified Communications Manager release 9.x and later

Open the Cisco Unified CM Administration interface.

Select System > Enterprise Parameters .

Set a value for the Never Start Call with Video parameter and then select Save .

## UseBridgeForConferenceCalls

Applies to all clients.

true
                                       				(default)—Users see Use
                                          				  My Conference Service is enabled.

false—Users
                                       				see Use
                                          				  My Conference Service is disabled.

Example: <UseBridgeForConferenceCalls>false</UseBridgeForConferenceCalls>

## UserBridgeUriAdmin

Applies to all clients.

Specifies the pattern for conference service in the client. For example, if the pattern is set as %%uid%%@example.com , and the user Adam McKenzie's user id is amckenzie, then the conference service is automatically set as amckenzie@example.com.
                              This parameter is used with the EnableBridgeConferencing .

Example: <UserBridgeUriAdmin>%%uid%%@example.com</UserBridgeUriAdmin>

| Note | A high frequency refresh may affect performance of the IBM Lotus Notes server. |
|---|---|

| Note | Client users can override this setting on the Calendar tab of the Options dialog. These parameters interact for calendar integration and contact resolution: CalendarIntegrationType EnableLocalAddressBookSearch EnableLotusNotesContactResolution See the Feature Configuration for Cisco Jabber guide for details. |
|---|---|

| Important | We deprecated this parameter as of August 2020 because of changes in Apple Push Notifications (APNs). We have closed the VoIP
                                          socket. |
|---|---|

| Note | Jabber gives priority to the Microsoft Exchange server discovery parameters in this order: EmailAsExchangeDiscoverDomain ExchangeAutodiscoverDomain ExchangeDomain |
|---|---|

| Note | For Cisco Jabber for Windows, this parameter does not have any effect if the ExchangeAuthenticateWithSystemAccount parameter is set to true. |
|---|---|

| Note | Jabber gives priority to the Microsoft Exchange server discovery parameters in this order: EmailAsExchangeDiscoverDomain ExchangeAutodiscoverDomain ExchangeDomain |
|---|---|

| Note | This parameter replaces the deprecated HeadsetPreferenceOnVDI parameter. |
|---|---|

| Note | With this
                                                				  option, you must set up a method of authentication for the client to
                                                				  authenticate with the Exchange server. You can choose to authenticate using
                                                				  single sign-on, or by Synching credentials. For more information, see the On-Premises Deployment for Cisco Jabber . |
|---|---|

| Important | Server settings take priority over this parameter in the client configuration file. However, if users change the default option
                                          in the client user interface, that setting takes priority over both the server and client configurations. |
|---|---|