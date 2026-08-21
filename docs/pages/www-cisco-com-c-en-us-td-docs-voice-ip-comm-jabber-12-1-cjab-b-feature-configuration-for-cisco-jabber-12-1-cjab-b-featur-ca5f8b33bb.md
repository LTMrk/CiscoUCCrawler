---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-1-cjab-b-feature-configuration-for-cisco-jabber-12-1-cjab-b-featur-ca5f8b33bb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_1/cjab_b_feature-configuration-for-cisco-jabber_12_1/cjab_b_feature-configuration-for-cisco-jabber_12_1_chapter_0110.html
retrieved_at: 2026-08-21T05:11:21.848550+00:00
---

Feature Configuration for Cisco Jabber 12.1

# Feature Configuration for Cisco Jabber 12.1

Updated: July 18, 2018

Chapter: Third-Party Integrations

## Chapter: Third-Party Integrations

# Third-Party Integrations

## Calendar Integration and Contact Resolution

Applies to: Cisco Jabber for Windows and Cisco Jabber Softphone for VDI

You can use the following client applications for calendar integration and contact resolution:

Microsoft Outlook 2016, 32 bit and 64 bit

Microsoft Outlook 2013, 32 bit and 64 bit

Microsoft Outlook 2010, 32 bit and 64 bit

IBM Lotus Notes 9, 32 bit

IBM Lotus Notes 8.5.3, 32 bit

IBM Lotus Notes 8.5.2, 32 bit

IBM Lotus Notes 8.5.1, 32 bit

Google Calendar (calendar integration only)

Calendar integration and contact resolution are achieved with one or more of the following parameters:

CalendarIntegrationType—Determines which calendar is integrated with the Meetings tab on the client. Users can overwrite this
                                    value with the Calendar integration type field on the Calendar tab of the Options window.

EnableLocalAddressBookSearch—Specifies if users can search for and add local Microsoft Outlook or IBM Notes contacts to their
                                    contact lists.

EnableLotusNotesContactResolution—Lets users search for and add local IBM Notes contacts to their contact lists.

The following table shows how these parameters interact to achieve calendar integration and contact resolution with third
                              party products.

Parameter Values

Contact Resolution

Calendar Integration

EnableLocalAddress BookSearch

EnableLotusNotes ContactResolution

CalendarIntegration Type

false

false

0 - none

None

None

true

false

0 - none

Microsoft Outlook

None

false

true

0 - none

None

None

true

true

0 - none

Microsoft Outlook

None

false

false

1 - Microsoft Outlook

None

Microsoft Outlook

true

false

1 - Microsoft Outlook

Microsoft Outlook

Microsoft Outlook

false

true

1 - Microsoft Outlook

None

Microsoft Outlook

true

true

1 - Microsoft Outlook

Microsoft Outlook

Microsoft Outlook

false

false

2 - IBM Notes

None

IBM Notes

true

false

2 - IBM Notes

None

IBM Notes

false

true

2 - IBM Notes

None

IBM Notes

true

true

2 - IBM Notes

IBM Notes

IBM Notes

false

false

3 - Google

None

Google

true

false

3 - Google

None

Google

false

true

3 - Google

None

Google

true

true

3 - Google

None

Google

## Chat History in Microsoft Outlook

Applies to: Cisco Jabber for desktop clients.

Supported Microsoft Exchange servers: 2010, 2013, 2016, and Office 365

You can enable the client to automatically save chat histories to a Cisco Jabber Chats folder in the user's Microsoft Outlook
                              application. When a user closes a chat window, the client saves the IM conversation to the Exchange server.

To enable the feature, you must:

Set the SaveChatHistoryToExchangeOperationMode parameter in the jabber-config.xml file.

Set up a method to authenticate users to the Exchange server. If you don't specify an authentication method, then users can
                                    add their credentials in the client.

Specify the method for determining which server to use.

### Set Parameter to Save Chat History in Outlook

Set the SaveChatHistoryToExchangeOperationMode parameter to one of the following:

DisabledByPolicy (default)—Users cannot save chat history to Microsoft Outlook. The option is not visible in the client.

EnabledByPolicy —Chats are saved to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is visible on the client, but users cannot access it.

With this option, you must set up authentication for the client to authenticate with the Exchange server by synching credentials.

DisabledByDefault —Users can save chats to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is unchecked in the client, but users can change it.

EnabledByDefault —Users can save chats to Microsoft Outlook. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is checked in the client, but users can change it.

OnPremOnlyByPolicy —Chats are saved to Microsoft Outlook only when Jabber is on the corporate network. Jabber doesn’t save chats to Outlook over
                                       MRA. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is visible on the Outlook tab of the Options menu, but it is greyed out and users cannot change it.

OnPremOnlyByDefault —Users have the option to save chats to Microsoft Outlook only when Jabber is in corporate network. Jabber doesn't save chats
                                       to Outlook over MRA. The option Save chat sessions to "Cisco Jabber Chats" Folder in Microsoft Outlook is checked on the Outlook tab of the Options menu, but users can change it.

### Limitations for Saving Chat History to an Outlook Folder

#### CUCM Accounts

Users must have a Cisco Unified Communications Manager account.

#### Cisco Expressway for Mobile and Remote Access

For users connecting via Expressway for Mobile and Remote Access, the following limitations apply:

If the client detects that the user is connecting via the Expressway, then the client uses the external server option for
                                       the Exchange connection. If the external server is not set, then it uses the internal server.

If the client detects that the user is not connecting via the Expressway, then the client uses the internal server option
                                       for the Exchange connection. If the internal server is not set, the client uses the external server.

However, if either the internal or external server is set, but for some reason Cisco Jabber can't connect to it, the client
                                       doesn't revert to using the other server.

### Specify Authentication Credentials

Jabber can automatically authenticate your users with the Exchange server, but you must first specify which credentials to
                                 use. When authentication is complete, the client can save chat histories to an Outlook folder on the Exchange server.

If you don’t specify which credentials to use, then your users will have to enter their credentials manually in the client's
                                 settings menu.

#### Authenticate with Windows Domain User Account

For deployments on Windows, Jabber can use domain user account details to authenticate with the Exchange server. This authentication
                                    method uses the Windows NT LAN Manager protocol.

We don’t recommend that you use domain user account details for authentication if a Windows account is shared by several users.
                                    Even if you reset the client and sign in as another user, Jabber will use the Windows account to authenticate with Exchange.
                                    One user’s chat history might be saved to another’s Outlook folder.

##### Before you begin

Users and their computers must use domain user accounts. This authentication method doesn't work with local Windows accounts.

In the jabber-config.xml file, set the ExchangeAuthenticateWithSystemAccount parameter to true .

#### Authenticate with Cisco Credentials

Jabber can authenticate with Exchange using credentials from Cisco’s IM and Presence Service, Unified Communications Manager,
                                    or Webex.

Set the Exchange_UseCredentialsFrom parameter to CUP (for IM and Presence), CUCM (for Unified Communications Manager), or WEBEX (for Webex).

##### Example:

### Specify Exchange Server Addresses

You can either define your Exchange server addresses or set Jabber to discover the Exchange servers automatically in a particular
                                 domain.

If you don't specify a way for the client to find the servers, then users will have to enter the server addresses manually
                                 in the client's settings menu.

#### Detect Server
                              	 Addresses Automatically

You can configure the client to automatically discover the Exchange servers based on users' domain. This domain is defined
                                    when you set up the authentication method by using the domain that was specified for the user's credentials.

In the jabber-config.xml file, configure the ExchangeAutodiscoverDomain parameter. For example, <ExchangeAutodiscoverDomain>domain</ExchangeAutodiscoverDomain>

Define the
                                             			 value of the parameter as the domain to discover the Exchange server.

https://< domain >

https://autodiscover.< domain >

#### Define Server
                              	 Addresses

You can define the
                                    		  internal and external Exchange server addresses in the configuration file.

In
                                             			 the jabber-config.xml file, configure the InternalExchangeServer and ExternalExchangeServer parameters.

Define the
                                             			 value of the parameters using the Exchange server addresses.

## IBM Notes Contact Search and Calendar Integration

Applies to: Cisco Jabber for Windows and Cisco Jabber Softphone for VDI

Prerequisite : IBM Notes contacts must contain a valid value in the Messaging ID field. Without this, users cannot add IBM Notes contacts
                              to their contacts lists.

Cisco Jabber for Windows supports IBM Notes calendar integration in the Meetings tab of the client. Cisco Jabber also lets
                              users search for and add local contacts from IBM Notes. To enable this integration with IBM Notes, you must set the following
                              parameters:

EnableLocalAddressBookSearch =true

EnableLotusNotesContactResolution =true

CalendarIntegrationType =2

The CalendarIntegrationType parameter can be overridden by users. To enable calendar integration and contact resolution with IBM Notes, users must ensure
                              that the Calendar integration type on the Calendar tab of the Options window  is set to IBM Notes .

Cisco Jabber cannot perform contact search and calendar integration if the backup IBM notes nsf files are loaded.

### C and C++ Libraries for IBM Notes Integration

If you have Jabber integrated with IBM Notes, it uses the C library by default. You can change the library to C++ using the EnableLotusNotesCLibrarySupport parameter. See the Parameters Reference Guide for more information.

### Contact Resolution for Incoming Calls

For incoming calls, Cisco Jabber for Windows does not search the address book in IBM Notes, therefore only the phone number
                              for an IBM Notes contact shows in the call history. If Cisco Jabber users subsequently search  for the contact associated
                              with the phone number, the call history changes to show the contact's name instead of the phone number.

## Integration with
                        	 Microsoft Products

Applies to: Cisco Jabber for Windows and Cisco Jabber Softphone for VDI

Cisco
                                 			 Jabber for Windows supports a range of Microsoft products that
                              		  integrate with the application. This section describes the support and
                              		  integrations for these products.

### Internet Explorer

Microsoft Internet Explorer 8 or later is required. Jabber uses Internet Explorer to support Single Sign-On.

Internet Explorer 9 users in Cloud-based deployments that use Single Sign-On (SSO) get security alerts when they sign in to Cisco Jabber for Windows . Add webexconnect.com to the list of websites in the Compatibility View Settings window of Internet Explorer 9 to stop these alerts.

### Office

Integration with the following versions of Office is supported:

Microsoft Office 2016, 32 and 64 bit

Microsoft
                                    				Office 2013, 32 and 64 bit

Microsoft
                                    				Office 2010, 32 and 64 bit

### Office
                              		  365

Microsoft Office 365 supports different configuration types based on the plan or subscription type. Cisco Jabber for Windows
                              has been tested with small business plan P1 of Microsoft Office 365. This plan requires an on-premises Active Directory server.

Client-side
                              		  integration with Microsoft Office 365 is supported with the following
                              		  applications:

Microsoft Office 2016, 32 bit and 64 bit

Microsoft
                                    				Office 2013, 32 bit and 64 bit

Microsoft
                                    				Office 2010, 32 bit and 64 bit

Microsoft
                                    				SharePoint 2010

### SharePoint

Integration with
                              		  the following versions of SharePoint is supported:

Microsoft
                                    				SharePoint 2013

Microsoft
                                    				SharePoint 2010

Availability
                              		  status in Microsoft SharePoint sites is supported only if users access those
                              		  sites with Microsoft Internet Explorer. You should add the Microsoft SharePoint
                              		  site to the list of trusted sites in Microsoft Internet Explorer.

### Skype for Business

Jabber for Windows and Skype for Business can compete for the Windows API and other Windows resources. To potentially mitigate
                              this issue, you can install Jabber with the following command:

```
msiexec.exe /i CiscoJabberSetup.msi CLICK2X=DISABLE
```

## Mac Calendar Integration For Meetings

Applies to: Cisco Jabber for Mac

You can give users the option to connect their calendars to their Cisco Jabber client.

You can use the following applications for calendar integration:

Exchange Server 2016, 2013, and 2010

Office 365

Mac Calendar

You configure calendar integration using the following parameters:

MacCalendarIntegrationType —Defines which calendar options are available to users to select in Cisco Jabber.

0 for None

1 (Default) for Microsoft Outlook

2 for Mac Calendar

InternalExchangeServer , ExternalExchangeServer , or ExchangeAutodiscoverDomain — to define which servers to connect to.

Exchange_UseCredentialsFrom or ExchangeDomain —to authenticate to those servers.

CalendarAutoRefreshTime —to define the number of minutes after which calendars refresh. The default value is zero, meaning that the calendars do not
                                    automatically refresh.

EnableReminderForNoneWebexMeeting —to specify whether users receive reminders from Cisco Jabber for non-Webex meetings that are in their calendars.

DisableNonAcceptMeetingReminder —to specify whether users receive reminders from Cisco Jabber about Cisco Webex Meetings that they haven't accepted.

For more information on how to set up these parameters, see the Parameters Reference Guide for Cisco Jabber or later.

## Microsoft Outlook Calendar Events

Applies to: Cisco Jabber for Windows and Cisco Jabber Softphone for VDI

You must apply a
                              		  setting in 
                              		  Microsoft Outlook so that calendar events display in Cisco Jabber for Windows .

Open the email
                                       			 account settings in 
                                       			 Microsoft Outlook, as in the following example:

Select File > Account
                                                   						Settings .

Select the Email tab on the Account Settings window.

Double-click
                                       			 the server name.

In most cases,
                                          				the server name is Microsoft Exchange .

Select the Use
                                          				Cached Exchange Mode checkbox.

Apply the
                                       			 setting and then restart 
                                       			 Microsoft Outlook.

When users create
                              		  calendar events in 
                              		  Microsoft Outlook, those events display in the Meetings tab.

## Microsoft Outlook Presence Integration

Applies to: Cisco Jabber for Windows and Cisco Jabber for Mac

You can integrate presence for your users' contacts with Microsoft Outlook.

To enable integration with Microsoft Outlook , you must specify SIP:user@cupdomain as the value of the proxyAddresses attribute in Microsoft Active Directory . Users can then share availability in Microsoft Outlook .

You can use the OutlookContactResolveMode parameter to choose how Jabber resolves the presence of a contact in Microsoft Outlook .

Auto (default)—When you configure the proxyaddress attribute with SIP:user@cupdomain then Jabber uses user@cupdomain as a Jabber ID. If you configure the proxyaddress attribute without SIP, Jabber uses user@cupdomain as an email address to resolve the presence of a contact in Microsoft Outlook .

Email—Jabber uses user@cupdomain as an email address to resolve the presence of a contact in Microsoft Outlook .

Use one of the following methods to modify the proxyAddresses attribute:

An Active Directory administrative tool such as Active Directory User and Computers

The Active Directory User and Computers administrative tool allows you to edit attributes on Microsoft Windows Server
                                       			 2008 or later.

ADSchemaWizard.exe utility

The ADSchemaWizard.exe utility is available in the Cisco Jabber administration package . This utility generates an LDIF file that modifies your directory to add the proxyAddresses attribute to each user with the following value: SIP:user@cupdomain .

You should use the ADSchemaWizard.exe utility on servers that do not support the edit attribute feature in the Active Directory
                                    User and Computers administrative tool. You can use a tool such as ADSI Edit to verify the changes that you apply with the
                                    ADSchemaWizard.exe utility.

The ADSchemaWizard.exe utility requires Microsoft .NET Framework version 3.5 or later.

Create a script with Microsoft Windows PowerShell

Refer to the appropriate Microsoft documentation for creating a script to enable presence in Microsoft Outlook .

### Limitation

Your users won't get the presence of their local Outlook contacts when the first search is done for the contact.  Local and
                              Active Directory contacts are merged and stored in a local cache after the first search. By the second search, presence for
                              these contacts will resolve normally.

| Parameter Values | Contact Resolution | Calendar Integration |
|---|---|---|
| EnableLocalAddress BookSearch | EnableLotusNotes ContactResolution | CalendarIntegration Type |
| false | false | 0 - none | None | None |
| true | false | 0 - none | Microsoft Outlook | None |
| false | true | 0 - none | None | None |
| true | true | 0 - none | Microsoft Outlook | None |
| false | false | 1 - Microsoft Outlook | None | Microsoft Outlook |
| true | false | 1 - Microsoft Outlook | Microsoft Outlook | Microsoft Outlook |
| false | true | 1 - Microsoft Outlook | None | Microsoft Outlook |
| true | true | 1 - Microsoft Outlook | Microsoft Outlook | Microsoft Outlook |
| false | false | 2 - IBM Notes | None | IBM Notes |
| true | false | 2 - IBM Notes | None | IBM Notes |
| false | true | 2 - IBM Notes | None | IBM Notes |
| true | true | 2 - IBM Notes | IBM Notes | IBM Notes |
| false | false | 3 - Google | None | Google |
| true | false | 3 - Google | None | Google |
| false | true | 3 - Google | None | Google |
| true | true | 3 - Google | None | Google |

| In the jabber-config.xml file, set the ExchangeAuthenticateWithSystemAccount parameter to true . |
|---|

| Set the Exchange_UseCredentialsFrom parameter to CUP (for IM and Presence), CUCM (for Unified Communications Manager), or WEBEX (for Webex). Example: <Exchange_UseCredentialsFrom>CUCM</Exchange_UseCredentialsFrom> In this example, Cisco Unified Communications Manager is defined as the service which provides the Exchange server with credentials
                                             for authentication. |
|---|

| Step 1 | In the jabber-config.xml file, configure the ExchangeAutodiscoverDomain parameter. For example, <ExchangeAutodiscoverDomain>domain</ExchangeAutodiscoverDomain> |
|---|---|
| Step 2 | Define the
                                             			 value of the parameter as the domain to discover the Exchange server. The client uses the domain to search for the Exchange server at one of the following Web addresses: https://< domain > https://autodiscover.< domain > |

| Step 1 | In
                                             			 the jabber-config.xml file, configure the InternalExchangeServer and ExternalExchangeServer parameters. |
|---|---|
| Step 2 | Define the
                                             			 value of the parameters using the Exchange server addresses. |

| Note | Cisco Jabber cannot perform contact search and calendar integration if the backup IBM notes nsf files are loaded. |
|---|---|

| Note | Internet Explorer 9 users in Cloud-based deployments that use Single Sign-On (SSO) get security alerts when they sign in to Cisco Jabber for Windows . Add webexconnect.com to the list of websites in the Compatibility View Settings window of Internet Explorer 9 to stop these alerts. |
|---|---|

| Step 1 | Open the email
                                       			 account settings in 
                                       			 Microsoft Outlook, as in the following example: Select File > Account
                                                   						Settings . Select the Email tab on the Account Settings window. |
|---|---|
| Step 2 | Double-click
                                       			 the server name. In most cases,
                                          				the server name is Microsoft Exchange . |
| Step 3 | Select the Use
                                          				Cached Exchange Mode checkbox. |
| Step 4 | Apply the
                                       			 setting and then restart 
                                       			 Microsoft Outlook. |