---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-116001-uc-singleinbox-00-html-2000c05d5c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/116001-uc-singleinbox-00.html
retrieved_at: 2026-08-16T18:57:35.815088+00:00
---

Unity Connection Single Inbox Troubleshooting TechNote

# Unity Connection Single Inbox Troubleshooting TechNote

### Download Options

Updated: March 15, 2023

Document ID: 116001

Contents

## Contents

## Introduction

This document describes how to troubleshoot Unified Messaging Services and Unified Messaging Accounts. Cisco Unity Connection Version 8.5 and later supports single inbox (SIB), which is also referred to as Unified Messaging. In versions before Version 8.5, Unity Connection had the capability to accept only and to relay the voicemails to external email addresses.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unity Connection

- Microsoft Exchange 2003/2007/2010

- ViewMail for Microsoft Outlook (VMO)

- Active Directory

### Components Used

The information in this document is based on these software and hardware versions:

- Unity Connection Version 8.5 or Later

- Microsoft Exchange 2003/2007/2010

- VMO

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

SIB, one of the Unified Messaging features in Cisco Unity Connection Version 8.5, synchronizes voice messages in Connection and Exchange mailboxes. When a user is enabled for SIB, all Connection voice messages that are sent to the user, which includes those sent from Cisco Unity Connection VMO, are first stored in Connection and are immediately replicated to the user's Exchange mailbox. In addition, status changes (for example, from unread to read), changes to the subject line, and changes to the priority are replicated from Connection to Exchange and vice versa. The Message Waiting Indicator (MWI) turns off when the message is read - either via phone or email client.

## SIB Configuration

Refer to Task List for Configuring Cisco Unity Connection 8.5 and Later and Exchange for Unified Messaging for information on how to configure SIB.

These two main sections must be configured for SIB on Unity Connection:

- Unified Messaging Service A Unified Messaging service can be configured in order to search for all Exchange servers in the environment. It can also be configured to connect to a single Exchange server. In this case, configure Unified Messaging Services for each Exchange server that hosts user mailboxes. In order to configure, navigate to CUC Administration > Unified Messaging > Unified Messaging Service > Add New .

Note : The Bulk Administration Tool can also be used to bulk add Unified Messaging accounts for all users.

## Troubleshoot

This section provides tips used in order to troubleshoot Unified Messaging Service and Unified Messaging Accounts.

### Unified Messaging Services Issues

Problem: Scenario 1

Under Unified Messaging Service, if Specify an Exchange Server is selected instead of Search for Exchange Servers , the test succeeds. If Search for Exchange Servers is selected, this error displays when the Test button on the page is clicked:

```
Searching the network Failed to locate a Domain Controller via DNS. Searching the network Failed to locate an Exchange 2003 server. Connection will not be able to Locate Exchange 2003 subscribers.
```

Here are sample Tomcat logs (set the CsExMbxLocator micro trace, Level 10-13):

```
CsExMbxLocator,13,AutoDiscoverURLS not found in cache CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:331]: Run DNS query for: _ldap._tcp.dc._msdcs.xxx.xxx CsExMbxLocator,13,[CsExMbxLocator/CCsDNSResolver.cpp:168]: querying dns for _ldap._tcp.dc._msdcs.xxx.xxx question type 33 CsExMbxLocator,13,[CsExMbxLocator/CCsDNSResolver.cpp:186] Length of returned DNS response is -1 CsExMbxLocator,10,[CsExMbxLocator/CCsDNSResolver.cpp:190] failed to get dns results for _ldap._tcp.dc._msdcs.xxx.xxx question type 33 CsExMbxLocator,11,[CsExMbxLocator/CsExMbxLocator.cpp:359]: DNS query for: _ldap._tcp.dc._msdcs.xxx.xxx didn't return results CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:192] Test Button result: Failed to locate a Domain Controller via DNS. CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:192] Test Button result: Failed to locate an Exchange 2003 server. Connection will not be able to Locate Exchange 2003 subscribers. CsExMbxLocator,11,Failed to find DC required for 2003 support
```

For additional troubleshooting steps, refer to Cisco bug ID CSCtq10780 and Granting Permissions to the Unified Messaging Services Account for Cisco Unity Connection 8.5 and Later (Exchange 2003 Only).

Problem: Scenario 2

This error displays when the Test button on the page is clicked:

```
Could not connect to Domain Controller (dc1.xxx.xxx) from DNS Could not connect to Domain Controller (dc2.xxx.xxx) from DNS Could not connect to Domain Controller (dc3.xxx.xxx) from DNS
```

Here are sample Tomcat logs (set the CsExMbxLocator micro trace, Level 10-13):

```
CsExMbxLocator,10,LDAP initialize non-SSL Return Code (0) CsExMbxLocator,10,LDAP authentication bind failed: INVALID_CREDENTIALS CsExMbxLocator,10,CCsLDAPHelper::Init():exit AUTH_NOT_INITIALIZED CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:192] Test Button result: Could not connect to Domain Controller (dc1.xxx.xxx) from DNS
```

Solution

This problem might be caused as a result of an expired password or an incorrect password that is entered in Unity Connection (account locked in Active Directory). In order to fix this problem, change the password in Active Directory, and enter it again in Unity Connection.

Problem: Scenario 3

This error displays when the Test button on the page is clicked:

```
Searching the network Could not connect to Domain Controller (dc1.xxx.xxx) from DNS Searching the network Could not connect to Domain Controller (dc2.xxx.xxx) from DNS Searching the network Failed to locate a Domain Controller via DNS. Searching the network Failed connected to Exchange CAS server at (https://xxx.xxx/autodiscover/autodiscover.xml) Searching the network Failed connected to Exchange CAS server at (https://autodiscover.xxx.xxx/autodiscover/autodiscover.xml) Searching the network Could not find an Exchange CAS server via Autodiscover DNS SRV record Searching the network Failed to locate an Exchange CAS server. Connection will not be able to Locate Exchange 2007/2010 subscribers.
```

Possible Solutions

From logs, a similar trace entry is seen as mentioned in Scenario 2. If Unity Connection is unable to connect to a domain controller, the issue is most likely an incorrect password. If Unity Connection is able to connect to a domain controller and still receives the remaining errors, check Scenario 5.

Here are sample Tomcat logs (set the CsExMbxLocator micro trace, level 10-13):

```
CsExMbxLocator,10,[CsExMbxLocator/CsExMbxLocator.cpp:1173]: HTTP request failed with error: Couldn't connect to server -- couldn't connect to host, HTTP status code: 503, for Autodiscovery URL: http://autodiscover.xxxxxxxxx.xxx/ autodiscover/autodiscover.xml, verb: GET, query: CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:192] Test Button result: Failed connected to Exchange CAS server at (http://autodiscover.xxxxxxxxx.xxx/autodiscover/autodiscover.xml) CsExMbxLocator,13,[CsExMbxLocator/CCsDNSResolver.cpp:168]: querying dns for_autodiscover._tcp.xxxxxxxxx.xxx question type 33 CsExMbxLocator,13,[CsExMbxLocator/CCsDNSResolver.cpp:186] Length of returned DNS response is -1 CsExMbxLocator,10,[CsExMbxLocator/CCsDNSResolver.cpp:190] failed to get dns results for_autodiscover._tcp.xxxxxxxxx.xxx question type 33 CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:192] Test Button result: Could not find an Exchange CAS server via Autodiscover DNS SRV record CsExMbxLocator,11,[CsExMbxLocator/CsExMbxLocator.cpp:636]: DNS query for: _autodiscover._tcp.xxxxxxxxx.xxx didn't return results CsExMbxLocator,13,[CsExMbxLocator/CsExMbxLocator.cpp:192] Test Button result: Failed to locate an Exchange CAS server. Connection will not be able to Locate Exchange 2007/2010 subscribers.
```

If these traces are seen in the log, navigate to Unified Messaging > Unified Messaging Services > Exchange Servers > Search for Exchange Servers > Active Directory DNS Domain Name , and make sure the domain name is correct.

Problem: Scenario 4

This error displays when the Test button on the page is clicked:

```
Peer certificate cannot be authenticated with known CA certificates - SSL certification problem, verify that the CA cert is OK. Details: error:14090086SL routinesSL3_GET_SERVER_CERTIFICATE: certificate verify failed
```

The certificate can be uploaded successfully to Connection-Trust; however, this error is received when you upload the same certificate to Tomcat-Trust:

```
Error reading the certificate
```

Possible Solutions

- The problem might be caused by the certificates. Make sure that you upload the correct certificates. If the correct certificates are not available, uncheck the validate option, and proceed as a workaround.

- Generate certificates with 2,048 bits instead of 1,024 bits.

```
Root Certificate ---------------------- Here the Issuer Name and Subject Name will be the same. Issuer Name: CN=ABC, OU=XXXX, OU=XXX, O=XXXXX, C=XX Validity From: Tue Nov 07 16:00:00 PST 2006 To:   Wed Jul 16 16:59:59 PDT 2036 Subject Name: CN=ABC, OU=XXXX, OU=XXX, O=XXXXX, C=XX Intermediate Certificate ---------------------------- Here the Issuer Name will be that of the Root Certificate and Suject Name will have information about the Intermediate Certificate. Issuer Name: CN=ABC, OU=XXXX, OU=XXX, O=XXXXX, C=XX Validity From: Sun Feb 07 16:00:00 PST 2010 To:   Fri Feb 07 15:59:59 PST 2020 Subject Name: CN=XYZ, OU=XXXXXXXXXXXXXXXXX, OU=XXXXXXXXXXXXXXX, O=XXXXXXXX, C=XX Server Certificate -------------------------- Here the  Issuer name will be that of the Intermediate certificate and the Subject Name will contain information about the Exchange server Issuer Name: CN=XYZ, OU=XXXXXXXXXXXXXXXXX, OU=XXXXXXXXXXXXXXX, O=XXXXXXXX, C=XX Validity From: Thu Aug 01 17:00:00 PDT 2013 To:   Thu Aug 17 16:59:59 PDT 2017 Subject Name: CN=mail.abc.lab, OU=XXXX, OU=XX, O=XXXXXXX, L=XXXX, ST=XXXX, C=XX
```

Problem: Scenario 5

This error displays when the Test button on the page is clicked:

```
Searching the network Successfully connected to Domain Controller (dc1.xxx.xxx) from DNS Searching the network Could not connect to Exchange CAS server (https://EX2010-1.xxx.xxx/Autodiscover/Autodiscover.xml) from Active Directory Searching the network Could not find an Exchange CAS server via Active Directory Searching the network Successfully connected to Exchange 2003 server (EX2003.xxx.xxx) from Active Directory Searching the network Failed connected to Exchange CAS server at (https://xxx.xxx/autodiscover/autodiscover.xml) Searching the network Failed connected to Exchange CAS server at (https://autodiscover.xxx.xxx/autodiscover/autodiscover.xml) Searching the network Could not find an Exchange CAS server via Autodiscover DNS SRV record Searching the network Failed to locate an Exchange CAS server. Connection will not be able to Locate Exchange 2007/2010 subscribers.
```

Possible Solution

Check whether Exchange 2010 Central Authentication Service (CAS) is set in order to require HTTPS, and the Exchange 2003 server is set to HTTP only. Set the CAS in order to allow HTTP or HTTPS.

Here is a similar scenario:

```
Searching the network Successfully connected to Domain Controller (dc1.xxx.xxx) from DNS Searching the network Could not connect to Exchange CAS server (https://EX2010-1.xxx.xxx/Autodiscover/Autodiscover.xml) from Active Directory Searching the network Could not find an Exchange CAS server via Active Directory Searching the network Failed to locate an Exchange 2003 server. Connection will not be able to locate Exchange 2003 subscribers. Searching the network Failed connected to Exchange CAS server at (https://xxx.xxx/autodiscover/autodiscover.xml) Searching the network Failed connected to Exchange CAS server at (https://autodiscover.xxx.xxx/autodiscover/autodiscover.xml) Searching the network Could not find an Exchange CAS server via Autodiscover DNS SRV record Searching the network Failed to locate an Exchange CAS server. Connection will not be able to Locate Exchange 2007/2010 subscribers.
```

Possible Solutions

- Check permissions on the account as described in Creating the Unified Messaging Services Account in Active Directory and Granting Permissions for Cisco Unity Connection 8.5 and Later .

- Refer to Cisco bug ID CSCtq10780 .

- Check to see if a domain user has sufficient rights in order to search Exchange servers, which is the ideal set up. The issue might be due to Group Policies applied on Active Directory. This solution is tested and works fine with just a domain user. In order to test, give Exchange View Only Admin rights and verify. It should also work to give Enterprise Admin rights to the Unified Messaging (UM) account, but company policies might not permit this.

- Open the Active Directory Service Interfaces (ADSI) Editor, and check whether the Exchange servers are listed after you log in with the UM account.

Problem: Scenario 6

This error displays when the Test button on the page is clicked:

```
Could not connect to Exchange 2003 server (ncacn_ip_tcp: <exchangemailboxserver1.example.com>) from Active Directory Could not connect to Exchange 2003 server (ncacn_ip_tcp: <exchangemailboxserver2.example.com>) from Active Directory Could not connect to Exchange 2003 server (ncacn_ip_tcp: <exchangemailboxserver3.example.com>) from Active Directory
```

For additional troubleshooting steps, refer to Cisco bug ID CSCto35509 .

### Unified Messaging Accounts Issues

Problem: Scenario 1

This error displays when the Test button on the page is clicked:

```
The system failed to perform an IMAP operation. Refer to other warnings and errors generated by the tool, and check the Tomcat log file for details. The system failed while trying to make an API call.
```

Here are sample CuImapSvr logs (set CuImapSvr Micro Trace - All Levels):

```
CML,19,Connection attempt to IMAP server at {10.xxx.xxx.xx:143/imap/notls/user="xxx/um/TestUser"}INBOX failed. CML,19,E_CML_IMAP_CONNECT_FAILED (0x80046410) Connection failed on IMAP request. Logged from HRESULT CCsCmlImapDriver::ExecuteRequest(TCsAutoPtr<CCsCmlImapRequest>&) in CsCml/CsCmlImapDriver.cpp at line 355. CML,19,E_CML_IMAP_CONNECT_FAILED (0x80046410) Unable to count messages using search-term ALL on imapfolder[login={10.xxx.xxx.xx:143/imap/notls/user="xxx/um/TestUser"}INBOX] in imapmbx[store=10.xxx.xxx.xx login=xxx/um/TestUser in session[id=5 alias=TestUser]. Logged from virtual HRESULT CCsCmlImapFolder::GetMessageCount(const CCsCmlSearchTerm&, int&) in CsCml/CsCmlImapFolder.cpp at line 258. CML,11,E_CML_IMAP_CONNECT_FAILED (0x80046410) Unable to get a message count from the External inbox for subscriber TestUser. Logged from HRESULT <unnamed>::VerifyMailbox(CCsCdlSubscriber&, CCsCmlMailbox&) in CsCml/CsCmlSession.cpp at line 486.
```

Possible Solutions

- Navigate to Users > Select User > Unified Messaging Accounts > Edit Unified Messaging Account ; under Account Information (Used Only for Exchange 2003 Text to Speech (TTS)), select Sign-In Type as Use User ID Provided , and User ID as Domain\username .

- Check whether the Internet Message Access Protocol (IMAP) 4 service has started on the Exchange server.

- Add the domain name with the user account under Unified Messaging Services: Unified Messaging > Unified Messaging Services > Active Directory Account Used to Access Exchange > Username > Domain\username .

- Use Telnet in order to verify basic IMAP connectivity.

- If there is an IMAP round-trip delay between Exchange and Unity Connection, navigate to Unity Connection Admin page > System Settings > Advanced > Unified Messaging Services Configuration : TTS and Calendars: Time to Wait for a response (in seconds). The default setting is 4. This value can be increased.

- Refer to Cisco bug IDs CSCto57555 and CSCto54535 .

- If this message appears on a packet capture taken from UC, navigate to AD Users and Computers > Select the User > Properties > Exchange Features > IMAP4 > Enable : IMAP 122 Response: 00000003 NO Logon failure: account currently disabled.

Problem: Scenario 2

This error displays when the Test button on the page is clicked:

```
The system failed to perform a typical calendar operation.
```

Possible Solutions

- Uncheck the Enable Forms Based Authentication check box. Refer to To Configure Basic Access to Exchange 2003 for the Calendar and Contact Integration (Without SSL) in Cisco Unity Connection 8.0 for more information.

- Refer to Test Fails the Last Check (Exchange 2003 Only) for additional troubleshooting steps.

Note : Frequently, when the other issues described in this document are fixed, this issue is fixed as well.

Problem: Scenario 3

This error displays when the Test button on the page is clicked:

```
Failed accessing xxx@ayz.com Diagnostic=[Timeout was reached -- operation timed out after 1000 milliseconds with 0 bytes recieved]
```

Possible Solutions

- Check the Require SSL check box under Exchange Web Services (EWS). Often, this is done under Autodiscover instead of EWS.

- Perform a reset of the Synchronize Connection and Exchange Mailboxes (SIB) from the Edit Unified Messaging Account page.

Problem: Scenario 4

This error displays when the Test button on the page is clicked:

```
Failed accessing xxx@ayz.com Diagnostic=[] Verb =[] url=[] request=[] response[]
```

Possible Solutions

Sample logs:

```
HTTP request failed with error: Bad response from server, HTTP code returned: 401, HTTP status code: 401
```

- Check the authentication method on both sides. Check settings in Internet Information Services (IIS) for both AutoDiscover and EWS.

- If the Microsoft Office 365 is used, the UM messaging account should be in the format account@domain.onmicrosoft.com .

- Reset the password, and enter the password again on Unity Connection.

- The UM account should not have a mailbox.

Sample logs:

```
HTTP request failed with error: Couldn't connect to server -- couldn't connect to host, HTTP status code: 503
```

- Check if there are any firewalls.

- Check if Unified Messaging Service points to the correct Exchange server.

- Refer to Cisco Bug ID CSCts82396 .

Problem: Scenario 5

This error displays when the Test button on the page is clicked:

```
The error is error:0200206F:system library:connect:Connection refused. Refer to the tomcat log
```

Here are sample Tomcat logs:

```
HTTP 503 ERRORS: HTTP request failed with error: Couldn't connect to server -- couldn't connect to host, HTTP status code: 503, for ews URL: https://xxxxxxxx.outlook.com/EWS/Exchange.ASMX, verb: POST HTTP 401 ERRORS: HTTP request failed with error: Bad response from server, HTTP code returned: 401, HTTP status code: 401, for ews URL: https://xxxxxxxxxx.outlook.com/EWS/Exchange.ASMX, verb: POST HTTP 404 ERRORS: HTTP request failed with error: Bad response from server, HTTP code returned: 404, HTTP status code: 404, for Autodiscovery URL: https://xxxx.com/autodiscover/autodiscover.xml, verb: GET, query:
```

Possible Solutions

- Check whether the firewall blocks port 443.

- Check if the correct domain is used.

Problem: Scenario 6

This error displays when the Test button on the page is clicked:

```
Diagnostic=[SSL connect error -- error:1408F119:SSL routines:SSL3_GET_RECORD: decryption failed or bad record mac] Verb=[POST]
```

Solution

This is due to corrupt certificates. From the OS Administration page, regenerate tomcat.pem certificate. Restart Tomcat Service.

Error codes

Here are some error codes that you might encounter:

- Possible causes include an incorrect password for the Unified Messaging Services account, an incorrect username, or an invalid format for the username. (If the domain\user format is used, do not use Fully Qualified Domain Name (FQDN) format for the domain name.) Another possible cause is that the value of the Web-Based Authentication Mode list does not match the authentication mode configured in Exchange. All values appear on the Edit Unified Messaging Service page.

- Check the password under Unified Messaging > Unified Messaging Services > Active Directory Account Used to Access Exchange > Password . Many times the UM service test will pass with wrong passwords.

- Make sure all the IIS settings are configured in BOTH EWS and Autodiscovery .

- Check the authentication mode on both sides: Unity Connection and Exchange.

- NT LAN Manager (NTLM) v2 is not supported; refer to Cisco bug ID CSCub61107 .

- Impersonation right issue: Complete the steps described in Creating the Unified Messaging Services Account in Active Directory and Granting Permissions for Cisco Unity Connection 8.5 and Later .

- Exchange user mailbox is uninitialized.

- Make sure the UM account does not have a mailbox. If it does, delete and recreate the account, and apply permissions. It does not help if you simply delete the mailbox.

- The exchange server might expect the username to be in this format - user@domain instead of domain\user . Use this format Unified Messaging > Unified Messaging Services .

```
Log Name:      Application Source:        MSExchange Web Services Date:          9/7/2013 7:59:16 PM Event ID:      24 Task Category: Core Level:         Error Keywords:      Classic User:          N/A Computer:      XXX.XXXXXXXXX.com Description: The Exchange certificate [Subject] CN=XXX.XXXXXXXXX.com, OU=XXXXXXXXX, OU=XX, O=XXXXXXXXXXXX, L=XXXXXX, S=XXXXXXX, C=XX [Issuer] CN=XXXXXXXXXXX, OU=XXXXXXXXXXX, OU=XXXXXXXXX, O=XXXXXXXXX, C=XX [Serial Number] XXXXXXXXXXXXXXXXXXXXXXXXX [Not Before] 8/9/2012 5:00:00 PM [Not After] 8/17/2013 4:59:59 PM [Thumbprint] XXXXXXXXXXXXXXXXXXXXXXXXXXXXX expired on 8/17/2013 4:59:59 PM.
```

- Secure Sockets Layer (SSL) is required in Exchange, but the public certificates from the certification authority (CA) that signed the certificates on the Exchange servers have not been uploaded to the Unity Connection server.

- One possible cause is that the Unified Messaging service is configured to use the HTTPS protocol in order to communicate with Exchange servers, but SSL is not enabled in Exchange. Another possible cause is that Exchange 2003 is used as the message store, but WebDav extensions have not been enabled.

- Navigate to Users > Select the User > Unified Messaging Accounts > Edit Unified Messaging Account, Under Account Information > Use this Email Address , and make sure the email address is correct.

- Incorrect server or Domain Name Server (DNS) resolves to the wrong server.

- The server does not run the necessary service (EWS, WebDAV, Autodiscovery).

- Login Timeout error/ Bad response from server

- Refer to Cisco bug ID CSCto91728 .

- Unity Connection SIB does not work with Exchange 2003 when a Forms-Based Authentication is configured on Exchange 2003 that contains a mailstore that Unity Connection must access.

- 500 error

- Server configuration problem. Incorrect authentication mode. Internet Information Service is unavailable. Email address (primary SMTP address) not found.

- If permissions are applied at the organization level, this error can be seen. Apply the same permissions at the server level. For more information, refer to Granting Rights to the Unified Messaging Services Account for Cisco Unity Connection 8.5 and Later (Exchange 2007 Only) .

- Impersonation issue: On the test page, this message is seen > HTTP status=[500 Internal Server Error]................ErrorImpersonateUserDenied.......The account does not have permission to impersonate the requested user. In order to fix this, refer to Assign Application Impersonation Management Role to Unified Messaging Services Account . If the UM service account was created initially with a mailbox, deleting the mailbox alone will not fix this issue. The account has to be deleted, and recreated without a mailbox.

- Check the Impersonation role assignment using get-ManagementRoleAssignment on the Exchange Management Shell. At the end of the output, check if there is a warning that says the role assignment is corrupt and is in an inconsistent state. If so, remove the assignment with Remove-ManagementRoleAssignment "< policy name >" , and readd it.

- ErrorNonExistentMailbox : The Simple Mail Transfer Protocol (SMTP) address has no mailbox associated with it.

Some of these error codes are also mentioned in this document: Single Inbox Is Not Working for Users Associated with a Unified Messaging Service .

If the Exchange server response is slow, increase Time to Wait for a Response (In Seconds) in Cisco Unity Connection (under System Settings > Advanced > Unified Messaging Services ).

Other Issues

In scenarios where the Test is successful on both the Unified Messaging Account and Unified Messaging Services page, enable these traces:

- Navigate to Cisco Unity Connection Serviceability > Trace > Macro Trace .

- Select Single Inbox Traces .

- CsMbxSync

- CsWebDav (If Exchange 2003 is used)

- CsEws (For Exchange 2007 and higher)

- CsExMbxLocator

Problem: Scenario

Unity Connection is configured in order to connect with Exchange 2003.

This is from the logs:

```
01:10:20.300 |6549,mail.xxxxxx.com,{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}, CsWebDav,14,[CsWebDav/CsWebDavMbxClient.cpp:3340]: HTTP Status code: 500, WEBDAV response headers: HTTP/1.1 500 Internal Server Error
```

This is from the Exchange logs:

```
Event ID: 9667 Type: Error Category: General Source: msgidNamedPropsQuotaError Description: Failed to create a new named property for database "<databasename>" because the number of named properties reached the quota limit (<configured quota>). User attempting to create the named property: <user name>. Named property GUID: <GUID of named property>. Named property name/id: <name of named property>.
```

Solution

These events are logged when a database on an Exchange server with the Mailbox server role installed approaches or reaches the maximum limit of named properties or replica identifiers.

A registry change is required in order to fix this issue as mentioned in this Microsoft Technet article - How to Configure Named Properties and Replica Identifier Quotas .

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MSExchangeIS\ <ServerName>\<Database Type-GUID>
```

Change the DWORD - NonMAPI Named Props Quota value. It is normally set to 8,192. Modify this to 16,384.

Refer to these documents for more information on this:

- Understanding the Impact of Named Property and Replica Identifier Limits on Exchange Databases

- Events 9666, 9667, 9668, and 9669 Received When Named Properties or Replica Identifiers Are Depleted for An Exchange Database

### Revision History

2.0

15-Mar-2023

March 15

1.0

01-Mar-2013

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 15-Mar-2023 | March 15 |
| 1.0 | 01-Mar-2013 | Initial Release |