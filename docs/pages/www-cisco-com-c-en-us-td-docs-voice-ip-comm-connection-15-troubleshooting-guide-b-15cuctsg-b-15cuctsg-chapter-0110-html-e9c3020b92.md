---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-0110-html-e9c3020b92
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_0110.html
retrieved_at: 2026-08-17T02:38:36.893381+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Unified Messaging

## Chapter: Troubleshooting Unified Messaging

# Troubleshooting Unified Messaging

Troubleshooting Unified Messaging

## Troubleshooting Single Inbox Issues

You may face some issues with single inbox that you can troubleshoot using the information provided in the sections mentioned
                           further.

### Mismatch of Date and Time for Messages in Unity Connection and Exchange 2003

Following are the circumstances when the date and time Unity Connection received a message is not synchronized with the date
                              and time on Exchange 2003:

A user already has voice messages when the administrator configures single inbox for the user. In Unity Connection, the messages
                                    continue to have the date and time that they were received. In Exchange 2003, the messages have the date and time that they
                                    were synchronized with Exchange.

A administrator uses the Disaster Recovery System to restore voice messages and the backup contains messages that do not exist
                                    in Exchange 2003 because the user deleted them from Exchange after the backup. Unity Connection resynchronizes the voice message
                                    into Exchange. The date and time on the messages in Unity Connection are the original date and time that the messages were
                                    received, but the date and time on the messages in Exchange is the date and time that they were synchronized with Exchange.

Single inbox is configured and the connectivity between Unity Connection and Exchange 2003 is interrupted and restored. In
                                    Unity Connection, messages received during the interruption in connectivity have the date and time that they were received.
                                    In Exchange, the messages have the date and time that they were synchronized after connectivity is restored.

### Message Relay Not
                           	 Working or is Not Working as Expected

If messages are not being relayed at all, confirm that you have
                              		specified the IP address for an SMTP smart host through which Unity Connection
                              		relays SMTP messages. (If DNS is configured, you can also specify the fully
                              		qualified domain name of the smart host.) To verify this, log in to Unity
                              		Connection Administration, navigate to the System Settings > SMTP Configuration > Smart Host page and verify the IP address or hostname of smart
                              		host.

If messages are being relayed but not as you expect, check how
                              		the message actions are relaying messages for a specific user through the
                              		Message Actions page in Unity Connection Administration for that user.

If messages are disappearing, see the Unity Connection Unable to Relay Messages .

### Single Inbox Not
                           	 Working for Anyone on Unity Connection

When single inbox is not working for any of the users on a
                              		Cisco Unity Connection server (for example, Unity Connection voice messages are
                              		not synchronized into Office 365 and the messages sent from ViewMail for
                              		Outlook are not delivered), do the following tasks.

On the primary server, in Cisco Unity Connection Serviceability,
                                    			 go to Tools > Service
                                          				  Management , and confirm that the status of the
                                    			 Connection Mailbox Sync (in the Critical Services section) service is Started:

If a firewall is configured between the Unity Connection and Exchange servers or between Unity Connection and Active Directory
                                    domain controllers, confirm that the necessary ports are opened. For more information, see the “ IP Communications Required by Cisco Unity Connection ” chapter in the Security Guide for Cisco Unity Connection, Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/security/guide/b_14cucsecx.html .

When single inbox configuration with Gmail server is not working for any of the users on Cisco Unity Connection server, do
                              the following task.

On primary server, in Cisco Unity Connection Serviceability , go to Tools > Service Management and confirm that the status of the Connection Google Workspace Sync Service (in the Critical Services section) is started.

### Single Inbox configuration with Exchange not working for Unified Messaging Users

When Single Inbox configuration with Exchange is not working only for the Unity Connection users whose unified messaging accounts
                              are associated with the same unified messaging service, do the following tasks.

When a cluster is configured, do the Unity Connection-specific tasks only on the primary (active) server.

Confirm that the unified messaging service is enabled and that single inbox is enabled:

In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services.

On the Search Unified Messaging Services page, select the unified messaging service of which you want to check the status.

On the Edit Unified Messaging Service page, confirm that the Enabled check box is checked.

Confirm that the Synchronize Unity Connection and Exchange Mailboxes (Single Inbox) check box is checked.

Test the unified messaging service:

In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services.

On the Search Unified Messaging Services page, select the unified messaging service that you want to test.

On the Edit Unified Messaging Service page, select Test.

Correct any problems that are listed on the Task Execution Results page.

Test one of the affected unified messaging accounts:

In Unity Connection Administration, expand Users and select Users.

On the Search Users page, select the user for which you want to update the unified messaging account.

On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts. On the Unified Messaging Accounts page,
                                    select Test.

Correct any problems that are listed on the Task Execution Results page. Among the problems that the Task Execution Results
                                    page may list are the following browser errors:

401 error: Possible causes include an incorrect password for the unified messaging services account, an incorrect username, or an invalid
                                    format for the username. (If you use the domain\user format, do not use FQDN format for the domain name.) Another possible
                                    cause is that the value of the Web-Based Authentication Mode list does not match the authentication mode configured in Exchange.
                                    All values appear on the Edit Unified Messaging Service page.

403 error: SSL is required in Exchange or Office 365, but the public certificates from the certification authority (CA) that signed
                                    the certificates on the Exchange servers have not been uploaded to the Unity Connection server.

404 error: (Exchange Only) One possible cause is that the unified messaging service is configured to use the HTTPS protocol to communicate
                                    with Exchange servers, but SSL is not enabled in Exchange.

In Cisco Unity Connection Serviceability, go to Tools > Service Management . In the Critical Services section, confirm that the service status for the Connection Mailbox Sync service is Started.

Check Active Directory settings on the unified messaging services account:

Confirm that the account is not locked.

Confirm that the password for the account has not expired.

Temporarily replace the unified messaging services account with the Active Directory account for a Unity Connection user associated
                                    with this unified messaging service:

In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services. On the Edit Unified Messaging
                                    Service page of the select unified messaging service, in the Username and Password fields, replace the credentials for the
                                    unified messaging services account with the credentials for a Unity Connection user associated with the service.

Send the user a Unity Connection voice message, and determine whether the voice message synchronized to Exchange or Office
                                    365.

If the message did not synchronize, switch the Username and Password fields back to the values for the unified messaging services
                                    account, then skip to Task 7.

If the message did synchronize, the problem is probably with permissions on the unified messaging services account. Continue
                                    with Task 6. c.

Switch the Username and Password fields back to the values for the unified messaging services account.

Regrant permissions as documented in the “Configuring Unified Messaging” chapter in the Unified Messaging Guide for Cisco Unity
                                    Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

Send the Unity Connection user another voice message, and determine whether the voice message synchronized to Exchange or
                                    Office 365.

If the message did not synchronize, skip to Task 7.

If the message did synchronize, test with some other users who are associated with the same unified messaging service to ensure
                                    that the problem is resolved.

If Exchange mailboxes for the users are all homed on the same Exchange server, confirm that the required services are running
                                    on the Exchange servers:

If the mailboxes are all homed on Exchange 2010, confirm that the EWS virtual directory is running on that Exchange server.

Confirm that Exchange authentication and SSL settings are the same on all the Exchange servers and confirm that Unity Connection
                                    settings match the Exchange settings. For more information, see the “ Confirming Exchange Authentication and SSL Settings for Unity Connection ” section of the “ Configuring Unified Messaging ” chapter in the Unified Messaging Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

(Office 365 Only) Confirm that Office 365 servers, which Unity Connection accesses have authentication mode set to Basic or
                                    OAuth2.

(Office 365 Only) If authentication mode is set to OAuth2 for Office 365 service, then verify the following:

If "EvtMbxOAuthAccessTokenDBSaveSuccess" event occurs in the CiscoSysLog in every 50 minutes, this confirms that the OAuth
                                          access token is successfully updated in the database for Unified Messaging Service.

If CiscoSysLog contains "EvtMbxOAuthAccessTokenRefreshThreadFailed" event, this confirms that the refresh token thread is
                                          not successfully started.

To resolve the issue, restart the Connection Mailbox Sync service on Cisco Unity Connection Serviceability page.

If you are not able to resolve the issue, contact to Cisco TAC.

If CiscoSysLog contains "EvtMbxOAuthDBHelperFailedToSetAccessToken" event, this confirms that OAuth access token is not successfully
                                          saved in database.

If you are not able to resolve the issue, contact to Cisco TAC.

If CiscoSysLog contains "EvtMbxOAuthDecryptionFailed" event, this confirms that while fetching the token, Unified Messaging
                                          Service password is not decrypted successfully.

To resolve the issue, go to Cisco Unity Connection Administration and navigate Unified Messaging > Unified Messaging Services > Edit Unified Messaging Service .

On Edit Unified Messaging Service page, enter the password again in Account Used to Access Exchange field and Save the page.

If you are not able to resolve the issue, contact to Cisco TAC.

If CiscoSysLog contains "EvtMbxOAuthEmptyAccessTokenAfterMaxRetries" event, this confirms that empty access token has been
                                          received.

To resolve the issue, go to Edit Unified Messaging Service page on Cisco Unity Connection Administration and check all the
                                          configuration entered on the page.

If you are not able to resolve the issue, contact to Cisco TAC.

If CiscoSysLog contains "EvtMbxOAuthHttpStatusCode" event, this confirms that access token requset getting bad response. You
                                          may get below error code in CiscoSysLog.

401 error : Possible causes include the incorrect values of Application ID, Client Secret and Client ID. Verify the values on the Edit
                                                Unified Messaging Service page.

0 error : Possible causes include the incorrect values of Proxy Server and Active Directory DNS Domain Name. Verify the values on
                                                the Edit Unified Messaging Service page.

After resolving the errors, either wait for the OAuth access token to be successfully updated in the database or run the below
                                          CLI for immediate resolution.

```
admin:run cuc dbquery unitydirdb update tbl_externalservicetoken set exchservertoken="" where externalserviceobjectid='<obejectid of corresponding unified messaging service>'
```

If you configured the unified messaging service to validate certificates for Exchange or Office 365 servers or for Active
                                    Directory domain controllers:

Confirm that the applicable certification authority certificates have been uploaded to the Unity Connection server.

Confirm that the certification authority certificates have not expired.

(Exchange Only) If all Unity Connection users associated with this unified messaging service have mailboxes homed on the same
                                    Exchange server, and if you are using HTTPS as the web-based protocol, confirm that SSL is properly configured:

Confirm that certification authority certificates have been uploaded to the Unity Connection server.

In Unity Connection Administration, confirm that the Exchange server name specified in the unified messaging service exactly
                                    matches the common name in the SSL certificate for that Exchange server.

Confirm that the SSL certificates have not expired.

(Exchange Only) Use Microsoft EWSEditor to access the Exchange mailbox of a Unity Connection user using the unified messaging
                                    services account. This allows you to determine whether the problem occurs even when Unity Connection is not involved.

EWSEditor software and documentation are available on the
                              		Microsoft website.

Confirm DNS settings:

Confirm that the Exchange server is reachable from Unity
                                          				  Connection.

If you configured the unified messaging service to search for
                                          				  Exchange or Office 365 servers, confirm that the Unity Connection server is
                                          				  configured to use DNS.

If you configured the unified messaging service to search for
                                          				  Exchange or Office 365 servers, confirm that the name of the Exchange or Office
                                          				  365 server is resolvable by the DNS server that Unity Connection is configured
                                          				  to use.

If you configured the unified messaging service to search for
                                          				  Exchange or Office 365 servers, confirm that the DNS server that Unity
                                          				  Connection is using is configured with appropriate records for auto-discovery.

### Single Inbox configuration with Gmail Server not working for Unified Messaging Users

When Single Inbox configuration with Gmail Server is not working for Unity Connection users whose unified messaging accounts
                              are associated with same unified messaging service, do the following tasks.

When a cluster is configured, do Unity Connection specific tasks only on the primary(active) server.

Confirm that Unified Messaging service is enabled and Google Workspace is also enabled by performing below steps:

In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services.

On Search Unified Messaging Services page, select the service, of which user want to check the status.

On the Edit Unified Messaging Service page, confirm that the Enabled check box is checked.

Confirm that the Synchronize Connection and Google Workspace Mailboxes (Single Inbox) check box is checked.

Test Unified Messaging Service by performing below steps:

In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services.

On Search Unified Messaging Services page, select the unified messaging service, of which user want to test.

On Edit Unified Messaging Service page, select Test.

Correct any problems that are listed on Task Execution Results page.

Test one of the affected Unified Messaging Accounts:

In Unity Connection Administration, expand Users and select Users.

On Search Users page, select the user for which you want to update the unified messaging account.

On Edit User Basics page, in Edit menu, select Unified Messaging Accounts. On Unified Messaging Accounts page, select Test.

Correct any problems that are listed on Task Execution Results page.

In Cisco Unity Connection Serviceability, go to Tools > Service Management . In Critical Services section, confirm that the service status for Connection Google Workspace Service is Started.

Check Active Directory settings on Unified Messaging Services Account:

Confirm that account is not locked.

Confirm that password for the account has not expired.

Confirm DNS settings

Confirm that Gmail server is reachable from Unity Connection. This can be confirmed by clicking Test button on Edit Unified
                                          Messaging Service page.

Correct any problems that are listed on Task Execution Results page.

### Single Inbox configuration with Exchange is not working for user or subset of users

When single inbox configuration with Exchange is not working (for example, Unity Connection voice messages are not synchronized
                              into Exchange, and messages sent from ViewMail for Outlook are not delivered), and when the problem is occurring for one or
                              more Unity Connection users but not for all users associated with a unified messaging service, do the following tasks.

When a cluster is configured, do the Unity Connection-specific
                                          		  tasks only on the primary (active) server.

In Unity Connection Administration, expand Users and select
                                                				Users. On the Edit User Basics page, in the Edit menu, select Unified Messaging
                                                				Accounts. On the Unified Messaging Accounts page for the user, confirm that the
                                                				user is associated with a unified messaging service on which single inbox is
                                                				enabled.

If you created an Exchange 2010 mailbox for the unified
                                                				messaging services account, and if Exchange mailboxes for the affected users
                                                				were moved from one Exchange 2003 mailbox store to another, delete the Exchange
                                                				2010 mailbox.

In Cisco Unity Connection Administration, expand Users and
                                                				select Users. On the Edit User Basics page, in the Edit menu, select Unified
                                                				Messaging Accounts. On the Unified Messaging Accounts page for the user,
                                                				confirm that single inbox is enabled in one of the user’s unified messaging
                                                				accounts.

In Cisco Unity Connection Administration, expand Users and
                                                				select Users. On the Edit User Basics page, in the Edit menu, select Unified
                                                				Messaging Accounts. On the Unified Messaging Accounts page for the user,
                                                				confirm that Unity Connection is configured to use the correct Exchange email
                                                				address.

In Cisco Unity Connection Administration, expand Users and
                                                				select Users. On the Edit User Basics page, in the Edit menu, select SMTP Proxy
                                                				Addresses. On the SMTP Proxy Addresses page for the user, confirm that there is
                                                				an SMTP proxy address that matches the user’s Exchange mail address.

If the user’s Exchange mailbox was not moved, skip to Task 8.

If the user’s Exchange mailbox was moved, and if the user is associated with a unified messaging service that specifies an
                              Exchange server instead of allowing Unity Connection to search for Exchange servers, determine whether Unity Connection is
                              able to automatically detect mailbox moves. See the “Configuring Unified Messaging” chapter in the Unified Messaging Guide
                              for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

If the user’s Exchange mailbox is homed on a new Exchange server, confirm that the unified messaging services account has
                                    the permissions necessary to access the server. For more information, see the “Configuring Unified Messaging” chapter in the
                                    Unified Messaging Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

If single inbox is not working for all of the Unity Connection
                                    			 users whose mailboxes are homed on the same Exchange server, confirm that the
                                    			 required services are running on the Exchange servers:

If the mailboxes are all homed on an Exchange 2013, Exchange
                                          				  2010,Unity Connection or Exchange 2007 server, confirm that the EWS service is
                                          				  running on that Exchange server.

If the mailboxes are all homed on an Exchange 2003 server,
                                          				  confirm that the WebDav service is running on that Exchange server.

If single inbox is not working for all of the Unity Connection
                                    			 users whose mailboxes are homed on the same Exchange server, and if you are
                                    			 using HTTPS as the web-based protocol, confirm that SSL is properly configured:

In Unity Connection Administration, uncheck the Validate
                                          				  Certificates for Exchange Servers check box, and determine whether single inbox
                                          				  is now working.

Confirm that SSL certificates have been uploaded to the Unity
                                          				  Connection server.

Confirm that the SSL certificates have not expired.

### Single Inbox configuration with Gmail Server not working for a user or subset of users

When Single Inbox configuration with Gmail Server is not working (for example, Unity Connection voice messages are not synchronized
                              into Gmail Server), and when problem is occurring for one or more Unity Connection users but not for all users associated
                              with a unified messaging service, check the user settings.

When a cluster is configured, do Unity Connection specific tasks only on the primary (active) server.

In Cisco Unity Connection Administration , expand Users and select Users. On Edit User Basics page, in Edit menu, Select Unified Messaging Accounts . Check below mentioned settings on this page :

On Unified Messaging Accounts page for user, confirm that user is associated with unified messaging service on which Google
                                    Workspace is enabled.

On Unified Messaging Accounts page for user, confirm that Google Workspace is enabled in one of the user’s unified messaging
                                    accounts.

On Unified Messaging Accounts page for user, confirm that Unity Connection is configured to use Gmail address.

On Edit User Basics page, in Edit menu, select SMTP Proxy Addresses.On SMTP Proxy Addresses page for user, confirm that there
                                    is an SMTP proxy address that matches the user’s Gmail address.

### Single Inbox
                           	 Synchronization from Exchange is Delayed

If Unity Connection synchronization to Exchange is working (for
                              		example, voice messages are synchronized to users’ Exchange mailboxes) but
                              		synchronization from Exchange is delayed (for example, the message waiting
                              		indicator is not turned off immediately after the last Unity Connection voice
                              		message is heard in ViewMail for Outlook), do the following tasks.

In Cisco Unity Connection Serviceability, go to Tools > Service
                                          				  Management and confirm that the service status for
                                    			 the Unity Connection Jetty service is Started. If not, activate and start the
                                    			 service, then test one of the affected users.

At a command line on the Exchange server, run the following
                                    			 command to telnet from the Exchange server to the Unity Connection server
                                    			 (confirm that port 7080 is open in the firewall, if applicable):

telnet < IP address of the Unity
                                 		  Connection server > 7080

If no error message is returned, the Exchange server was able to
                              		connect to the Unity Connection server. If an error message is returned:

In Cisco Unity Connection Serviceability, confirm that the Unity
                                    			 Connection Jetty service is running.

Troubleshoot the network problem.

Press Ctrl-K to exit from Telnet.

In Cisco Unity Connection Administration, display the unified
                                    			 messaging account for one of the affected users and select Reset .

If synchronization from Exchange to Unity Connection starts
                              		working for the affected user, in Unity Connection Administration, display the
                              		unified messaging service associated with the affected user (Unified
                              		Messaging > Unified Messaging Services) and select Reset .

If you Reset a particular unified messaging service, the
                              		synchronization is delayed for all of the users associated with the unified
                              		messaging service as Unity Connection resynchronizes data with Exchange.

If the synchronization from Exchange is delayed, you can also
                              		check if the number of outstanding requests is consistently not exceeding 999.
                              		To check the number of outstanding request, you need to enable the CsMbxSync
                              		(level 19) traces. For more information on traces, see Traces in Cisco Unity Connection Serviceability .

If the number of outstanding requests is consistently increasing to a value greater than 999, check the EWS latency (EWS request-response
                              RTT time) between Unity Connection and Exchange Server. If the latency is more than the supported value, calculate the number
                              of connections and change the number of connections to a calculated value. For information on maximum EWS latency and the
                              method to calculate connections, see the “ Calculating the Number of Connections for One Unity Connection Server ” section of the "Single Inbox" chapter in Design Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/design/guide/b_14cucdg.html .

### Single Inbox Synchronization from Office 365 is Delayed

If Unity Connection synchronization to Office 365 is working (for example, voice messages are synchronized to users’ Exchange
                              mailboxes) but synchronization from Office 365 is delayed (for example, the message waiting indicator is not turned off immediately
                              after the last Unity Connection voice message is heard in ViewMail for Outlook), do the following tasks.

In Cisco Unity Connection Administration, display the unified messaging account for one of the affected users, and select Reset .

If synchronization from Exchange to Unity Connection starts working for the affected user, in Unity Connection Administration,
                                    display the unified messaging service associated with the affected user (Unified Messaging > Unified Messaging Services) and
                                    select Reset.

### Single Inbox Synchronization from Gmail Server is Delayed

If Unity Connection synchronization to Gmail Server is working but synchronization from Gmail Server is delayed, do the following
                              tasks.

In Cisco Unity Connection Administration, display Unified Messaging Account for one of the affected users and select Reset .

In Unity Connection Administration, display Unified Messaging Service associated with the affected user (Unified Messaging >
                                    Unified Messaging Services) and select Reset .

Check number of outstanding requests by enabling the CuGsuiteSyncSrv (level 11) traces. For more information on traces, see
                                    " Traces in Cisco Unity Connection Serviceability " section in chapter "Troubleshooting Cisco Unity Connection" of Troubleshooting Guide for Cisco Unity Connection Release 14 available at link https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg.html .

If a particular unified messaging service is reset, then synchronization is delayed for all of the users associated with the
                                          unified messaging service as Unity Connection resynchronizes data with Gmail Server.

### Single Inbox Synchronization from Server Failed

If synchronization from Unity Connection to Exchange/Gmail server fails for set of users and Unified Messaging Account Reset
                              button press is not resolving problem, do the following tasks:

```
select y.alias from vw_mailboxmap as x, vw_user as y where x.userobjectid=y.objectid AND x.status != 0
```

```
update tbl_mailboxmap set status = 0
```

Updating the value of "status" as zero is just a work around and user must investigate reason of status change in logs.

### Single Inbox Fails with Office 365 Using ADFS

If you are integrating Unity Connection with Office 365 for Single Inbox where the Unity Connection Account used to access
                              Office 365 was created on active directory and imported into Office 365, the Single Inbox may not work as Unity Connection
                              is not equipped to handle ADFS.

To get the Single Inbox working, the account must be created locally on the Office 365 side.

### Duplicate Message
                           	 Issue with Single Inbox

Internet Message
                                 		  ID is a unique identifier for internet messages. Cisco Unity Connection
                              		assigns a unique Internet message ID to each voice message. If messages are
                              		restored with same internet message ID, the duplicate messages are created in
                              		the mailbox of a user. When mailbox synchronizes with Exchange, the duplicate
                              		messages are reflected in the Single Inbox.

To resolve the
                              		issue of duplicate messages in Single Inbox, a user or administrator must
                              		delete the duplicate messages from the mailbox.

## Resolving SMTP
                        	 Domain Name Configuration Issues

Step 1

In Cisco Unity Connection Administration, expand System Settings > SMTP
                                             				  Configuration , then select Smart Host.

Step 2

On the Smart Host page, in the Smart Host field, enter the IP
                                       			 address or fully qualified domain name of the SMTP smart host server and select
                                       			 Save. (Enter the fully qualified domain name of the server only if DNS is
                                       			 configured.)

Step 3

In Cisco Unity Connection Administration, expand System Settings
                                       			 and select General Configuration.

Step 4

On the General Configuration page, in the When a recipient
                                       			 cannot be found list, select Relay message to smart host.

Step 5

Click Save.

Step 6

In Cisco Unity Connection Administration, expand Users >
                                       			 Message Actions and select the Accept the message option from the Voicemail
                                       			 drop- down list.

Step 7

Enter an SMTP Proxy Address for the relay address field.

Do not create any SMTP Proxy Address for the user. Make sure to
                                                      				  select the Relay the message option from the Email, Fax, and receipt drop -down
                                                      				  lists.

Step 8

Setup a recipient policy on Exchange Server such that the Unity
                                       			 Connection alias resolves to the corporate email Id.

For Exchange 2013 or Exchange 2010, see the following link:

http://technet.microsoft.com/en-us/library/bb232171.aspx

For Exchange 2007, see the following link: http://technet.microsoft.com/en-us/library/bb232171(v=exchg.80).aspx

For Exchange 2003, see the following link:

http://support.microsoft.com/kb/822447

For Configuring Exchange Email Policies with Unity Connection,
                                                					 please see the following white paper link: http://www.cisco.com/en/US/prod/collateral/voicesw/ps6788/ps12506/ps6509/guide_c07-728014.html .

## Troubleshooting Problems with Cisco ViewMail for Microsoft Outlook

You may face some issues with ViewMail for Outlook that you can troubleshoot using the information provided in the sections
                           mentioned further.

### Voice Messages or Receipts are Not Received in the Outlook Inbox

If single inbox users do not receive incoming voice messages or receipts in the Outlook Inbox, note the following:

Check the Junk E-mail folder to see whether the messages or receipts are automatically being filtered to this folder. The
                                    junk-email filter can be updated to add specific sender addresses or domain names to the safe filter list. For information
                                    on configuring the Junk E-mail folder to exclude a class of messages, refer to the Microsoft documentation.

Check the configuration of any email anti-spam filters in your organization to see whether voice messages are being routed
                                    to a location other than the Outlook Inbox folder, .wav attachments are being removed, or the policy is otherwise interfering
                                    with the delivery of voice messages or receipts to Outlook.

If you have Unity Connection mailbox quotas configured, and if a user has exceeded the send/receive quota, Unity Connection
                                    prevents messages from being received in the user’s Unity Connection mailbox. ViewMail for Outlook does not notify a user
                                    that the send/receive threshold has been reached and that callers are therefore not allowed to leave voice messages for that
                                    user; the user would know only by checking voice messages in Unity Connection. However, when a user sends a message after
                                    reaching the send quota, ViewMail for Outlook does notify the user. The send quota is a lower threshold, so a user reaches
                                    the send/receive quota only by ignoring the earlier warning.

### Messages Sent from a Single Inbox Outlook Client are Not Received

If single inbox users cannot send messages through the Unity Connection server from the Outlook client—for example, users
                              receive non-delivery receipts (NDRs)—consider the following possibilities:

The email address of the message sender must exactly match a primary or proxy SMTP address configured in Unity Connection.

The email address of the message recipient must match a primary or proxy SMTP address that is configured for a Unity Connection
                                    user, or an SMTP proxy address that is configured for a VPIM contact. If no such match is found, Unity Connection relays the
                                    message to the SMTP smart host, or sends an NDR to the sender, depending on the option selected in the When a Recipient Cannot
                                    be Found setting on the System Settings > General Configuration page in Unity Connection Administration. By default, Unity
                                    Connection sends an NDR.

### Messages Received
                           	 in an Email Account Other than the Single Inbox Account

If users unexpectedly
                              		receive voice messages in their corporate or other email accounts rather than
                              		their Unity Connection mailboxes, consider the following possibilities:

The email address of the message recipient must match a primary or proxy SMTP address that is configured for a Unity Connection
                                    user, or an SMTP proxy address that is configured for a VPIM contact. If no such match is found and Unity Connection is configured
                                    to relay the message to the SMTP smart host, the message is relayed to the applicable email address. Confirm that the message
                                    recipient has a proxy SMTP address configured for the applicable email address. See the “ SMTP Proxy Addresses ” section of the “User Settings” chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

If message actions for the recipient are configured to relay
                                    			 messages of a particular type (voice, email, fax or delivery receipt) to the
                                    			 user at the corporate email address, the seemingly erroneous routing of
                                    			 messages may be expected behavior. Message actions are also configured in the
                                    			 unified messaging service that is specified in the recipient’s unified
                                    			 messaging account, and the interaction of the user-level setting and the
                                    			 setting in the unified messaging service may produce unanticipated results. For
                                    			 a summary of how message actions are relaying messages for a specific user, in
                                    			 Unity Connection Administration, see the Message Actions page for that user.

### Messages cannot be Played in Outlook

To play secure messages from Outlook, you must install Cisco Unity Connection ViewMail for Microsoft Outlook version. When
                              you view a secure message in Outlook, the text in the message briefly explains secure messages but does not include a .wav
                              attachment. The only copy of the .wav file remains on the Unity Connection server.

Caution

If you delete a secure message from Outlook, Unity Connection moves the message to the deleted items folder in Unity Connection.
                                          If message aging is configured, the message is eventually deleted.

### Messages Moved
                           	 into a .PST Folder in Outlook cannot be Played

Unity Connection synchronizes voice messages in the following
                              		Outlook folders with the Unity Connection Inbox folder for the user, so the
                              		messages are still visible in the Unity Connection Inbox folder:

Subfolders under the Outlook Inbox folder

Subfolders under the Outlook Deleted Items folder

The Outlook Junk Email folder

Unity Connection synchronizes voice messages in the Sent Items
                              		Outlook folder with the Unity Connection Sent Items folder for the user, so the
                              		messages are still visible in the Unity Connection Sent Items folder.

When Unity Connection replicates a secure voice message to
                              		Exchange, the replicated message contains only text that briefly explains
                              		secure messages; only the copy of the .wav file remains on the Unity Connection
                              		server. When a user plays a secure message using ViewMail for Outlook, ViewMail
                              		retrieves the message from the Unity Connection server and plays it without
                              		ever storing the message in Exchange or on the computer of the user.

If the user moves a secure message to an Outlook folder that is
                              		not synchronized with the Unity Connection Inbox folder, the only copy of the
                              		voice message is moved to the deleted items folder in Unity Connection, and the
                              		message can no longer be played in Outlook. If the user moves the message back
                              		into the Outlook Inbox folder or into an Outlook folder that is synchronized
                              		with the Unity Connection Inbox folder, and:

If the message is still in the deleted items folder in Unity
                                    			 Connection, the message is synchronized back into the Unity Connection Inbox
                                    			 for that user, and the message becomes playable again in Outlook.

If the message is not in the deleted items folder in Unity
                                    			 Connection, the message is not resynchronized into Unity Connection and can no
                                    			 longer be played in Outlook or Unity Connection.

For more information, see the “Synchronization with Outlook Folders” section of the "Introduction to Unified Messaging" chapter
                              in the Unified Messaging Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

### Playing a Message Does Not Turn Off the Message Waiting Indicator

If you upgraded from Cisco Unity that was configured as unified messaging server and migrated the messages from the server,
                              note the following:

Two copies of migrated messages appear in the Exchange mailbox for each user: the original message and the migrated message
                                    that is synchronized into the Exchange mailbox when single inbox is configured.

If a user uses Outlook to play the original message in Exchange (the copy that Cisco Unity put into Exchange when the message
                                    was received), the message remains unread in Unity Connection, and the message waiting indicator remains on. Playing the migrated
                                    message (the copy that was synchronized into the Exchange mailbox by the single inbox feature) or playing messages that are
                                    received after the migration turns off the message waiting indicator as appropriate.

### Message Waiting Indicator Turns Off Before the Message is Played

If you have enabled the Mark Items as Read When Viewed in the Reading Pane option in Outlook, the message is marked as read
                              as soon as you select it in the Outlook inbox. If this is the only Unity Connection voice message that you have not heard,
                              Unity Connection turns off the message waiting indicator.

### Deleting a Message
                           	 in Outlook Does Not Delete the Corresponding Message

If you upgraded from Cisco Unity that was configured as unified
                              		messaging server and migrated the messages from the server, note the following:

Two copies of migrated messages appear in the Exchange mailbox
                                    			 for each user: the original message and the migrated message that is
                                    			 synchronized into the Exchange mailbox when single inbox is configured.

If a user uses Outlook to delete the original message in
                                    			 Exchange (the copy that Cisco Unity put into Exchange when the message was
                                    			 received), the migrated message remains in the user’s inbox in Unity
                                    			 Connection. Deleting the migrated message in Outlook (the copy that was
                                    			 synchronized into the Exchange mailbox by the single inbox feature) causes the
                                    			 message to be moved from the user’s inbox in Unity Connection to the user’s
                                    			 deleted items folder in Unity Connection.

For more information on how the deleted messages are handled, see the Location for Deleted Messages section of the “Introduction to Unified Messaging” chapter of Unified Messaging Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

### Messages Moved
                           	 into a .PST Folder in Outlook are Deleted

Unity Connection synchronizes voice messages in the following
                              		Outlook folders with the Unity Connection Inbox folder for the user, so the
                              		messages are still visible in the Unity Connection Inbox folder:

Subfolders under the Outlook Inbox folder

Subfolders under the Outlook Deleted Items folder

The Outlook Junk Email folder

If a user moves voice messages into Outlook folders that are not
                              		under the Inbox folder, the messages are moved to the deleted items folder in
                              		Unity Connection.

For more information, see the “ Synchronization with Outlook Folder ” section of the “Introduction to Unified Messaging” chapter in the Unified Messaging Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

### Troubleshooting Problems with Invalid Passwords

When users change their Cisco Personal Communications Assistant (PCA) password in the Messaging Assistant, they must also
                              																																									update the password configured in ViewMail options so that the client can continue
                              to access Unity Connection and retrieve voice messages. Likewise, when LDAP authentication is configured and the PCA password
                              is changed in LDAP, the password configured in ViewMail options must be updated. If the PCA password has been changed but
                              ViewMail has not been updated, users typically see a message indicating that the invalid credentials were entered for the
                              account when they try to use ViewMail features.

### Changing a Cisco
                           	 ViewMail for Microsoft Outlook Password

Step 1

If you are using Outlook 2010:

On the user workstation, in Outlook 2010, click the ViewMail tab.

Select Settings .

Step 2

If you are
                                          			 using Outlook 2007 or Outlook 2003:

On the
                                                				  user workstation, on the Outlook Tools menu, select Options .

Select the
                                                				  ViewMail tab.

Step 3

From the
                                          			 Associated Email Account list, select the Microsoft Exchange/Single Inbox
                                          			 account for the user and select Edit .

Step 4

On the
                                          			 Viewmail Account Settings window, change the password for the user.

Step 5

Select Test Settings .

Step 6

If the test
                                          			 passes successfully, select OK . If the test fails, reenter the password and
                                          			 repeat

Step 7

Select OK to close the window, and then select OK again to close the Options dialog.

### Collecting Diagnostics from ViewMail for Outlook on the User Workstation

To troubleshoot problems with the Cisco ViewMail for Microsoft Outlook form, you can enable diagnostics on the user workstation.

### Enabling Cisco
                           	 ViewMail for Microsoft Outlook Diagnostics and View the Log Files on the User
                           	 Workstation

Step 1

If you are using Outlook 2010:

On the user workstation, in Outlook 2010, click the ViewMail tab.

Select Settings .

Step 2

If you are
                                          			 using Outlook 2007 or Outlook 2003:

On the
                                                				  user workstation, on the Outlook Tools menu, select Options .

Select the
                                                				  ViewMail tab.

Step 3

Check the Turn on Diagnostic Traces check box.

Step 4

Select OK .

Step 5

Reproduce the
                                          			 problem.

Step 6

If you are
                                          			 using Outlook 2010:

On the
                                                				  user workstation, in Outlook 2010, click the ViewMail tab.

Select Email Log Files , and send the resulting message with logs
                                                				  attached to an email address.

Step 7

If you are
                                          			 using Outlook 2007 or Outlook 2003:

On the Help menu, select Cisco ViewMail for Outlook > Email Log Files .

Send the
                                                				  resulting message with logs attached to an email address.

### Collecting
                           	 Diagnostics on the Unity Connection Server for Problems with Single Inbox and
                           	 ViewMail for Outlook

You can enable the
                              		Unity Connection VMO macro trace to troubleshoot client problems from the
                              		server side.

For detailed instructions on enabling and collecting diagnostic
                              		traces, see the Using Diagnostic Traces for Troubleshooting .

Troubleshooting Access to Emails in an External Message Store

## User on the Phone Hears “Invalid Selection” after Pressing Seven

When a user has signed in by phone, presses seven on the main menu, and is told that the selection is invalid, the unified
                           messaging service account for the user is not enabled for access to email in the external message store.

## Enabling User
                        	 Access to Email in an External Message Store

Step 1

In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select an
                                       			 applicable user.

Step 2

On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts > .

Step 3

On the Unified Messaging Accounts page, select the name of the
                                       			 unified messaging service that connects to the external message store.

Step 4

On the Edit Unified Messaging Account page, check the Access Exchange by Using Text to Speech (TTS) check box and select Save .

## User on the Phone Hears “Your Messages are Not Available” after Pressing Seven

When a user has signed in by phone, presses seven on the main menu, and is told that messages are not available, use the following
                           task list to determine the cause and to resolve the problem. Do the tasks in the order presented until the problem is resolved.

Follow the given steps for troubleshooting a “Your Messages are Not Available” after pressing seven:

Test the unified messaging service that enables access to email in the external message store, and correct any errors that
                                 are reported. See the “Testing the Unified Messaging Service to Access Emails in an External Message Store” section on page 7-15 .

Test the unified messaging account of the user who is enabled to access email in the external message store, and correct any
                                 errors that are reported. See the “Testing Unified Messaging Account for User to Access Email in an External Message Store” section on page 7-15 .

In Cisco Unity Connection Administration, expand Class of Service and select Class of Service. Select the class of service
                                 applied to voicemail users. On the Edit Class of Service page, confirm that the Allow Access to Exchange Email by Using Text
                                 to Speech (TTS) check box is checked.

In Cisco Unity Connection Administration, expand Users and select Users. Confirm that the Allow Access to Exchange Email by
                                 Using Text to Speech (TTS) check box is checked. See the “Enabling User Access to Email in an External Message Store” section on page 7-16 .

Ping the server to which the unified messaging service connects using the value in the Server field on the Unified Messaging>
                                 Unified Messaging Services> if you select Specify an Exchange Server check box, enter the IP address or hostname of the Exchange
                                 2003 server. If the ping fails, Unity Connection is not functional. You must restore the net work functionality to Unity Connection.

If the unified messaging service is configured for SSL and the Validate Certificates for Exchange Servers check box is checked,
                                 determine whether certificate validation is causing the problem. In Cisco Unity Connection Administration, go to Unified Messaging>
                                 Unified Messaging Services and uncheck the Validate Certificates for Exchange Servers check box and select Save .

(Exchange 2003 only) Follow the given steps for Exchange 2003 only:

In Unity Connection Administration, on the Users > Edit Unified Messaging Accounts page for the user, confirm that the User
                                 ID field entry matches the Exchange login alias of the user. If the Login Type field is set to Use Unity Connection Alias,
                                 the user Exchange login alias must match the Unity Connection user alias.

On the Exchange server, confirm that the Microsoft Exchange IMAP4 service is running.

Confirm that the Exchange server is set up to support basic authentication for IMAP4.

### Testing the
                           	 Unified Messaging Service to Access Emails in an External Message Store

Step 1

In Cisco Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services . On the Search Unified
                                          			 Messaging Services page, select the name of the applicable service.

Step 2

On the Edit Unified Messaging Service page, select Test .

Step 3

In the Task Execution Results window, refer to the list of
                                          			 issues and recommendations and do the applicable troubleshooting steps.

Step 4

Repeat Step 2 and Step 3 until the test
                                          			 succeeds.

### Testing Unified
                           	 Messaging Account for User to Access Email in an External Message Store

Step 1

In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select the alias of
                                          			 the user.

Step 2

On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts .

Step 3

On the Unified Messaging Accounts page, select the name of the
                                          			 applicable unified messaging account and select Test .

Step 4

In the Task Execution Results window, refer to the list of
                                          			 issues and recommendations and do the applicable troubleshooting steps.

Step 5

Repeat Step 2 and Step 4 until the test
                                          			 succeeds.

### Enabling User
                           	 Access to Email in an External Message Store

Step 1

In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select the alias of
                                          			 the user.

Step 2

On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts .

Step 3

On the Unified Messaging Accounts page, select the name of the
                                          			 unified messaging service that connects to the external message store.

Step 4

On the Edit Unified Messaging Account page, check the Access Exchange Email by Using Text to Speech (TTS) check box and select Save .

## Users Hear Gibberish at the End or Beginning of an Email

When users hear gibberish at the end or beginning of an email, the gibberish is part of the email formatting that Text to
                           Speech (TTS) plays back. Although the TTS engine is able to clean up some of the gibberish that can be found in various email
                           formats, there are formats that cause some gibberish to be played.

## Email Deleted by Phone is Still in the Inbox Folder (Exchange 2003 Only)

When accessing an email account with a MAPI client (such as Microsoft Outlook), email that was deleted by phone may still
                           appear in the Inbox and not in the Deleted Items folder.

Unity Connection uses the IMAP protocol to interact with Exchange 2003. Exchange 2003 handles messages that are soft-deleted
                           via IMAP differently than those that are soft-deleted using the MAPI protocol. When a message is soft-deleted through IMAP,
                           it is marked as deleted and is left in the Inbox folder. When a message is soft-deleted through MAPI, it is moved to the Deleted
                           Items folder.

## Using Traces to
                        	 Troubleshoot Access to Emails in an External Message Store

You can use traces to troubleshoot access to emails in an
                           		external message store. For detailed instructions, see the Using Diagnostic Traces for Troubleshooting .

Troubleshooting Calendar Integrations

## Using Unified
                        	 Messaging Accounts are Used for Calendar Integrations

The following configuration principles apply to unified
                           		messaging accounts that are used for calendar integrations:

A user can have only one unified messaging account for which the
                                 			 Access Exchange Calendar and Contacts check box is checked on the Unified
                                 			 Messaging Accounts page for the user.

A user can have multiple unified messaging accounts for which
                                 			 the MeetingPlace Scheduling and Joining check box is checked on the Unified
                                 			 Messaging Services page.

If a user has more than one unified messaging account for which
                                 			 the MeetingPlace Scheduling and Joining check box is checked, the Primary
                                 			 Meeting Service check box (on the Users > Edit Unified Messaging Account
                                 			 page) can be checked on only one of them.

Each user can access calendar information from only one unified
                           		messaging account. If the calendar-enabled unified messaging account connects
                           		to an Exchange server, the user has access to events only from the Exchange
                           		calendar. Similarly, if the calendar-enabled unified messaging account connects
                           		to a Cisco Unified MeetingPlace server, the user has access to events only from
                           		the Cisco Unified MeetingPlace calendar.

If a user has more than one unified messaging account for which
                           		the MeetingPlace Scheduling and Joining check box is checked, the unified
                           		messaging account for which the Primary Meeting Service check box is checked
                           		determines which Cisco Unified MeetingPlace server is used to schedule
                           		reservationless meetings.

For information on configuring a calendar integration between Cisco Unity Connection and Exchange, see the “Configuring Unified
                           Messaging” chapter in the Unified Messaging Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html .

## Testing the
                        	 Calendar Integration

Step 1

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, select the alias of
                                       			 a user.

Step 2

On the Edit User Basics page, on the Edit menu, select Unified Messaging Accounts .

Step 3

On the Unified Messaging Accounts page, select the name of the
                                       			 applicable unified messaging service account.

Step 4

On the Edit Unified Messaging Account page, select Test .

Step 5

In the Task Execution Results window, refer to the list of
                                       			 issues and recommendations and do the applicable troubleshooting steps.

Step 6

Repeat Step 4 and Step 5 until the test
                                       			 succeeds.

## Obtaining Unified Messaging Account Status

In Cisco Unity Connection Administration, browse to the Unified Messaging > Unified Messaging Accounts Status page. The status
                           icon on the page indicates the state of the Cisco Unity Connection configuration.

The Unified Messaging Accounts page for an individual user also displays Unity Connection configuration status.

## Test Fails the Last Check

When you select Test on the Edit Unified Messaging Account page to troubleshoot a calendar integration and all checks succeed
                           except for the last check (which fails with the message “The system failed to perform a typical calendar operation”), use
                           the following task list to determine the cause and to resolve the problem. Do the tasks in the order presented until the problem
                           is resolved:

On the Exchange server, confirm that SP2 or later is installed.

On the Exchange server, confirm that the user is enabled for Outlook Web Access (OWA).

In Cisco Unity Connection Administration, on the Users > Edit Unified Messaging Account page for the user, confirm that the
                                 entry in the Email Address field matches the primary SMTP address for the user.

On the Exchange server, confirm that the Microsoft Exchange Outlook Web Access service is available.

You can manually check whether the Microsoft Exchange Outlook Web Access service is available by entering one of the following
                                 URLs in a web browser:

http://<servername>/exchange/<emailaddress>

https://<servername>/exchange/<emailaddress>

Note the following:

If the unified messaging account in which the Access Exchange Calendar and Contacts check box is checked is associated with
                                       a unified messaging service in which the value of the Web-Based Protocol list is “HTTPS,” the URL must begin with “https”.

If you chose to specify an Exchange Server on the Unified Messaging > Unified Messaging Services page, for <servername>, enter
                                       the value of the Exchange Server. Use the unified messaging service to which the unified messaging account of the user refers.
                                       If you chose to search for Exchange servers, verify that you can ping the domain, and that the protocol (LDAP or LDAPS) is
                                       correct.

For <emailaddress>, enter the email address that the user’s unified messaging account is using. See the Account Information
                                       section of the Users > Edit Unified Messaging Account page for the user. When prompted to authenticate, enter the user’s Active
                                       Directory alias and password.

(Exchange 2003 only) In Cisco Unified Operating System Administration, on the Services > Ping Configuration page, confirm
                                 that Unity Connection can ping the IP address or hostname of the Exchange server.

If the unified messaging service is configured to use HTTPS for the web-based protocol and the Validate Certificates for Exchange
                                 Servers check box is checked, determine whether certificate validation is causing the problem by doing the following sub-tasks.

In Unity Connection Administration, browse to the Unified Messaging > Unified Messaging Services page, and select the unified
                                 messaging service associated with the unified messaging account that you are testing.

On the Edit Unified Messaging Service page, uncheck the Validate Server Certificate check box and select Save .

On a phone, sign in as the user who experiences the problem and access calendar information.

If the user is able to access calendar information, confirm that the public root certificate of the Certificate Authority
                                 (CA) that issued the Exchange server certificate is installed on Unity Connection as a trusted certificate, that it is self-signed,
                                 and that it has not expired.

In Unity Connection Administration, on the System Settings > Unified Messaging Services > Edit Unified Messaging Services
                                 page, check the Validate Server Certificate check box and select Save .

Confirm that the service account on Exchange that the unified messaging service uses has the Administer Information Store,
                                 Receive As, and Send As permissions allowed.

If the Exchange server is slow enough to respond to calendar information requests that Unity Connection times out, in Unity
                                 Connection Administration, on the System Settings > Advanced > Unified Messaging Services page, set the TTS and Calendars:
                                 Time to Wait for a Response (In Seconds) field to a value greater than 4.

Increasing the value of TTS and Calendars: Time to Wait for a Response (In Seconds) may result in delays when accessing calendar
                                             information.

## Test Succeeds but the Calendar Integration Still Does Not Work (Exchange 2003 Only)

When you select Test on the Edit Unified Messaging Account page to troubleshoot a calendar integration and all checks succeed
                           but the calendar integration still does not work, use the following task list to determine the cause and to resolve the problem.
                           Do the tasks in the order presented until the problem is resolved.

### Task List for Troubleshooting a Calender Integration When the Test Succeeds

In Cisco Unity Connection Administration, browse to the Unified Messaging > Unified Messaging Services page, and select the
                                    unified messaging service associated with the unified messaging account that you are testing. On the Edit Unified Messaging
                                    Service page, confirm that the fully qualified DNS name (FQDN) of the Exchange server is resolvable via DNS.Even if the unified
                                    messaging service is configured with the IP address of the Exchange server, calendar information from the Exchange server
                                    is provided with URLs that contain the FQDN of the server. Unity Connection uses these URLs, which must be resolved by a DNS
                                    server so that the user can access calendar information. If the Exchange server is slow enough to respond to calendar information
                                    requests that Unity Connection times out, in Unity Connection Administration, on the System Settings > Advanced > Unified
                                    Messaging Services page, set the TTS and Calendars: Time to Wait for a Response (In Seconds) field to a value greater than 4.

Increasing the value of TTS and Calendars: Time to Wait for a Response (In Seconds) may result in delays when accessing calendar
                                                information.

Confirm that the system clocks on the Unity Connection and Exchange servers are both correct.

Confirm that the meetings appear on the Outlook calendar of the user.

If Cisco Unified MeetingPlace meetings are scheduled through the user web interface for these applications, the scheduled
                              meetings do not appear on the Outlook calendar of the user. If you configure the profile for Cisco Unified MeetingPlace with
                              an email type of “Exchange,” meeting requests appear on the Outlook calendar of the user.

## Non-Published Meetings Do Not Appear in List of Meetings (Cisco Unified MeetingPlace Only)

When Cisco Unity Connection has an calendar integration with Cisco Unified MeetingPlace, all applicable published and non-published
                           meetings are listed when the user accesses meeting information.

If non-published meetings are not listed in the list of meetings, the service account that Unity Connection uses to access
                           calendar information is not correctly configured.

## Configuring the Unity Connection Service Account (Cisco Unified
                        	 MeetingPlace Only)

Step 1

Sign in to the Cisco Unified MeetingPlace
                                       			 Administration Server as an administrator.

Step 2

Select User Configuration > User Profiles .

Step 3

Select the Unity Connection service account.

Step 4

In the Type of User field, select System Administrator .

Step 5

Select Save .

Step 6

Sign out of Cisco Unified MeetingPlace.

## Meetings Do Not Appear in List of Meetings

When meetings do not appear in the list of meetings, the cause may be the interval that Cisco Unity Connection waits to update
                           calendar information.

### Changing the Interval that Cisco Unity Connection Waits to Update
                           	 Calendar Information

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced , then select Unified Messaging Services.

Step 2

On the Unified Messaging Services
                                          			 Configuration page, in the Calendars: Normal Calendar Caching Poll Interval (In
                                          			 Minutes) field, enter the length of time that Unity Connection waits between
                                          			 polling cycles when it caches upcoming Outlook calendar data for users who are
                                          			 configured for a calendar integration.

A larger number reduces the impact on the Unity Connection server
                                             				while reducing the ability of the server to handle last-minute changes to the
                                             				Outlook calendar data for users in a timely manner. A smaller number increases
                                             				the impact on the Unity Connection server while increasing the ability of the
                                             				server to handle last-minute changes to the Outlook calendar data for users in
                                             				a timely manner.

In the Calendars: Short Calendar Caching
                                             				Poll Interval (In Minutes) field, enter the length of time that Unity
                                             				Connection waits between polling cycles when it caches upcoming Outlook
                                             				calendar data for calendar users who must have their calendar caches updated
                                             				more frequently.

This setting applies to users who have the
                                             				Use Short Calendar Caching Poll Interval check box checked on their Edit User
                                             				Basics page.

Step 3

Select Save .

## “Access Exchange Calendar and Contacts” Option Not Available for Unified Messaging Accounts

When the Access Exchange Calendar and Contacts check box does not appear on the Unified Messaging Account page, use the following
                           task list to determine the cause and to resolve the problem. Do the tasks in the order presented until the problem is resolved:

In Cisco Unity Connection Administration, browse to the Unified Messaging > Unified Messaging Services page, and select the
                                 unified messaging service associated with the unified messaging account that you are testing.

On the Edit Unified Messaging Service page, confirm that the Access Exchange Calendar and Contacts check box is checked.

## Using Traces to
                        	 Troubleshoot a Calendar Integration

You can use traces to troubleshoot a calendar integration. For
                           		detailed instructions, see the Using Diagnostic Traces for Troubleshooting .

## Troubleshooting
                        	 Access to Calendar Information Using Personal Call Transfer Rules

When users have problems accessing calendar information when
                           		using Personal Call Transfer Rules, the cause may be the interval that Unity
                           		Connection waits to update calendar information. Do the following procedure.

You can use traces
                           		to troubleshoot issues related to accessing calendar information when using
                           		personal call transfer rules. For detailed instructions, see the Using Diagnostic Traces for Troubleshooting .

See also the Troubleshooting Personal Call Transfer Rules chapter.

### Changing the Interval Unity Connection Waits to Update Calendar
                           	 Information

### SUMMARY STEPS

- In Cisco Unity Connection Administration,
                                 			 expand System Settings > Advanced > and select Unified Messaging Services.

- On the Unified Messaging Services
                                 			 Configuration page, in the Calendars: Normal Calendar Caching Poll Interval (In
                                 			 Minutes) field, enter the length of time that Unity Connection waits between
                                 			 polling cycles when it caches upcoming Outlook calendar data for users who are
                                 			 configured for a calendar integration.

- Select Save .

### DETAILED STEPS

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced > and select Unified Messaging Services.

Step 2

On the Unified Messaging Services
                                          			 Configuration page, in the Calendars: Normal Calendar Caching Poll Interval (In
                                          			 Minutes) field, enter the length of time that Unity Connection waits between
                                          			 polling cycles when it caches upcoming Outlook calendar data for users who are
                                          			 configured for a calendar integration.

A larger number reduces the impact on the
                                             				Unity Connection server while reducing the ability of the server to handle
                                             				last-minute changes to the Outlook calendar data for users in a timely manner.
                                             				A smaller number increases the impact on the Unity Connection server while
                                             				increasing the ability of the server to handle last-minute changes to the
                                             				Outlook calendar data for users in a timely manner.

In the Calendars: Short Calendar Caching
                                             				Poll Interval (In Minutes) field, enter the length of time that Unity
                                             				Connection waits between polling cycles when it caches upcoming Outlook
                                             				calendar data for calendar users who must have their calendar caches updated
                                             				more frequently.

This setting applies to users who have the
                                             				Use Short Calendar Caching Poll Interval check box checked on their Edit User
                                             				Basics page.

Step 3

Select Save .

## Troubleshooting
                        	 the Test Button for Unified Messaging Services and Unified Messaging
                        	 Accounts

You can use traces to troubleshoot problems with
                           		the Test button (the unified messaging service diagnostic tool). This button is
                           		available on the following pages in Cisco Unity Connection Administration:

Unified Messaging > Unified Messaging Services> select a
                                 			 unified messaging service on the Search Unified Messaging Services page>
                                 			 Edit Unified Messaging Services page.

Users > Users > select a user on the Search Users page>
                                 			 Edit User Basics page> Edit> Unified Messaging Accounts> select an
                                 			 applicable account> Edit Unified Messaging Account page.

For information on using traces to troubleshoot problems with
                           		the Test button, see the Using Diagnostic Traces for Troubleshooting .

| Note | When a cluster is configured, do Unity Connection specific tasks only on the primary(active) server. |
|---|---|

| Note | When a cluster is configured, do the Unity Connection-specific
                                          		  tasks only on the primary (active) server. In Unity Connection Administration, expand Users and select
                                                				Users. On the Edit User Basics page, in the Edit menu, select Unified Messaging
                                                				Accounts. On the Unified Messaging Accounts page for the user, confirm that the
                                                				user is associated with a unified messaging service on which single inbox is
                                                				enabled. If you created an Exchange 2010 mailbox for the unified
                                                				messaging services account, and if Exchange mailboxes for the affected users
                                                				were moved from one Exchange 2003 mailbox store to another, delete the Exchange
                                                				2010 mailbox. In Cisco Unity Connection Administration, expand Users and
                                                				select Users. On the Edit User Basics page, in the Edit menu, select Unified
                                                				Messaging Accounts. On the Unified Messaging Accounts page for the user,
                                                				confirm that single inbox is enabled in one of the user’s unified messaging
                                                				accounts. In Cisco Unity Connection Administration, expand Users and
                                                				select Users. On the Edit User Basics page, in the Edit menu, select Unified
                                                				Messaging Accounts. On the Unified Messaging Accounts page for the user,
                                                				confirm that Unity Connection is configured to use the correct Exchange email
                                                				address. In Cisco Unity Connection Administration, expand Users and
                                                				select Users. On the Edit User Basics page, in the Edit menu, select SMTP Proxy
                                                				Addresses. On the SMTP Proxy Addresses page for the user, confirm that there is
                                                				an SMTP proxy address that matches the user’s Exchange mail address. If the user’s Exchange mailbox was not moved, skip to Task 8. |
|---|---|

| Note | When a cluster is configured, do Unity Connection specific tasks only on the primary (active) server. |
|---|---|

| Note | If a particular unified messaging service is reset, then synchronization is delayed for all of the users associated with the
                                          unified messaging service as Unity Connection resynchronizes data with Gmail Server. |
|---|---|

| Note | Updating the value of "status" as zero is just a work around and user must investigate reason of status change in logs. |
|---|---|

| Note | COBRA is one
                                          		  of the interfaces that provide the option to restore the messages as duplicate
                                          		  messages. To avoid the duplicate message issue in Single Inbox, do not select
                                          		  the option to restore the messages as duplicate messages. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > SMTP
                                             				  Configuration , then select Smart Host. |
|---|---|
| Step 2 | On the Smart Host page, in the Smart Host field, enter the IP
                                       			 address or fully qualified domain name of the SMTP smart host server and select
                                       			 Save. (Enter the fully qualified domain name of the server only if DNS is
                                       			 configured.) |
| Step 3 | In Cisco Unity Connection Administration, expand System Settings
                                       			 and select General Configuration. |
| Step 4 | On the General Configuration page, in the When a recipient
                                       			 cannot be found list, select Relay message to smart host. |
| Step 5 | Click Save. |
| Step 6 | In Cisco Unity Connection Administration, expand Users >
                                       			 Message Actions and select the Accept the message option from the Voicemail
                                       			 drop- down list. |
| Step 7 | Enter an SMTP Proxy Address for the relay address field. Note Do not create any SMTP Proxy Address for the user. Make sure to
                                                      				  select the Relay the message option from the Email, Fax, and receipt drop -down
                                                      				  lists. | Note | Do not create any SMTP Proxy Address for the user. Make sure to
                                                      				  select the Relay the message option from the Email, Fax, and receipt drop -down
                                                      				  lists. |
| Note | Do not create any SMTP Proxy Address for the user. Make sure to
                                                      				  select the Relay the message option from the Email, Fax, and receipt drop -down
                                                      				  lists. |
| Step 8 | Setup a recipient policy on Exchange Server such that the Unity
                                       			 Connection alias resolves to the corporate email Id. For Exchange 2013 or Exchange 2010, see the following link: http://technet.microsoft.com/en-us/library/bb232171.aspx For Exchange 2007, see the following link: http://technet.microsoft.com/en-us/library/bb232171(v=exchg.80).aspx For Exchange 2003, see the following link: http://support.microsoft.com/kb/822447 For Configuring Exchange Email Policies with Unity Connection,
                                                					 please see the following white paper link: http://www.cisco.com/en/US/prod/collateral/voicesw/ps6788/ps12506/ps6509/guide_c07-728014.html . |

| Note | Do not create any SMTP Proxy Address for the user. Make sure to
                                                      				  select the Relay the message option from the Email, Fax, and receipt drop -down
                                                      				  lists. |
|---|---|

| Caution | If you delete a secure message from Outlook, Unity Connection moves the message to the deleted items folder in Unity Connection.
                                          If message aging is configured, the message is eventually deleted. |
|---|---|

| Step 1 | If you are using Outlook 2010: On the user workstation, in Outlook 2010, click the ViewMail tab. Select Settings . |
|---|---|
| Step 2 | If you are
                                          			 using Outlook 2007 or Outlook 2003: On the
                                                				  user workstation, on the Outlook Tools menu, select Options . Select the
                                                				  ViewMail tab. |
| Step 3 | From the
                                          			 Associated Email Account list, select the Microsoft Exchange/Single Inbox
                                          			 account for the user and select Edit . |
| Step 4 | On the
                                          			 Viewmail Account Settings window, change the password for the user. |
| Step 5 | Select Test Settings . |
| Step 6 | If the test
                                          			 passes successfully, select OK . If the test fails, reenter the password and
                                          			 repeat |
| Step 7 | Select OK to close the window, and then select OK again to close the Options dialog. |

| Step 1 | If you are using Outlook 2010: On the user workstation, in Outlook 2010, click the ViewMail tab. Select Settings . |
|---|---|
| Step 2 | If you are
                                          			 using Outlook 2007 or Outlook 2003: On the
                                                				  user workstation, on the Outlook Tools menu, select Options . Select the
                                                				  ViewMail tab. |
| Step 3 | Check the Turn on Diagnostic Traces check box. |
| Step 4 | Select OK . |
| Step 5 | Reproduce the
                                          			 problem. |
| Step 6 | If you are
                                          			 using Outlook 2010: On the
                                                				  user workstation, in Outlook 2010, click the ViewMail tab. Select Email Log Files , and send the resulting message with logs
                                                				  attached to an email address. |
| Step 7 | If you are
                                          			 using Outlook 2007 or Outlook 2003: On the Help menu, select Cisco ViewMail for Outlook > Email Log Files . Send the
                                                				  resulting message with logs attached to an email address. |

| Step 1 | In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select an
                                       			 applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts > . |
| Step 3 | On the Unified Messaging Accounts page, select the name of the
                                       			 unified messaging service that connects to the external message store. |
| Step 4 | On the Edit Unified Messaging Account page, check the Access Exchange by Using Text to Speech (TTS) check box and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services . On the Search Unified
                                          			 Messaging Services page, select the name of the applicable service. |
|---|---|
| Step 2 | On the Edit Unified Messaging Service page, select Test . |
| Step 3 | In the Task Execution Results window, refer to the list of
                                          			 issues and recommendations and do the applicable troubleshooting steps. |
| Step 4 | Repeat Step 2 and Step 3 until the test
                                          			 succeeds. |

| Step 1 | In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select the alias of
                                          			 the user. |
|---|---|
| Step 2 | On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts . |
| Step 3 | On the Unified Messaging Accounts page, select the name of the
                                          			 applicable unified messaging account and select Test . |
| Step 4 | In the Task Execution Results window, refer to the list of
                                          			 issues and recommendations and do the applicable troubleshooting steps. |
| Step 5 | Repeat Step 2 and Step 4 until the test
                                          			 succeeds. |

| Step 1 | In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select the alias of
                                          			 the user. |
|---|---|
| Step 2 | On the Edit User Basics page, in the Edit menu, select Unified Messaging Accounts . |
| Step 3 | On the Unified Messaging Accounts page, select the name of the
                                          			 unified messaging service that connects to the external message store. |
| Step 4 | On the Edit Unified Messaging Account page, check the Access Exchange Email by Using Text to Speech (TTS) check box and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, select the alias of
                                       			 a user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Unified Messaging Accounts . |
| Step 3 | On the Unified Messaging Accounts page, select the name of the
                                       			 applicable unified messaging service account. |
| Step 4 | On the Edit Unified Messaging Account page, select Test . |
| Step 5 | In the Task Execution Results window, refer to the list of
                                       			 issues and recommendations and do the applicable troubleshooting steps. |
| Step 6 | Repeat Step 4 and Step 5 until the test
                                       			 succeeds. |

| Note | Increasing the value of TTS and Calendars: Time to Wait for a Response (In Seconds) may result in delays when accessing calendar
                                             information. |
|---|---|

| Note | Increasing the value of TTS and Calendars: Time to Wait for a Response (In Seconds) may result in delays when accessing calendar
                                                information. |
|---|---|

| Step 1 | Sign in to the Cisco Unified MeetingPlace
                                       			 Administration Server as an administrator. |
|---|---|
| Step 2 | Select User Configuration > User Profiles . |
| Step 3 | Select the Unity Connection service account. |
| Step 4 | In the Type of User field, select System Administrator . |
| Step 5 | Select Save . |
| Step 6 | Sign out of Cisco Unified MeetingPlace. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced , then select Unified Messaging Services. |
|---|---|
| Step 2 | On the Unified Messaging Services
                                          			 Configuration page, in the Calendars: Normal Calendar Caching Poll Interval (In
                                          			 Minutes) field, enter the length of time that Unity Connection waits between
                                          			 polling cycles when it caches upcoming Outlook calendar data for users who are
                                          			 configured for a calendar integration. A larger number reduces the impact on the Unity Connection server
                                             				while reducing the ability of the server to handle last-minute changes to the
                                             				Outlook calendar data for users in a timely manner. A smaller number increases
                                             				the impact on the Unity Connection server while increasing the ability of the
                                             				server to handle last-minute changes to the Outlook calendar data for users in
                                             				a timely manner. In the Calendars: Short Calendar Caching
                                             				Poll Interval (In Minutes) field, enter the length of time that Unity
                                             				Connection waits between polling cycles when it caches upcoming Outlook
                                             				calendar data for calendar users who must have their calendar caches updated
                                             				more frequently. This setting applies to users who have the
                                             				Use Short Calendar Caching Poll Interval check box checked on their Edit User
                                             				Basics page. |
| Step 3 | Select Save . |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced > and select Unified Messaging Services. |
|---|---|
| Step 2 | On the Unified Messaging Services
                                          			 Configuration page, in the Calendars: Normal Calendar Caching Poll Interval (In
                                          			 Minutes) field, enter the length of time that Unity Connection waits between
                                          			 polling cycles when it caches upcoming Outlook calendar data for users who are
                                          			 configured for a calendar integration. A larger number reduces the impact on the
                                             				Unity Connection server while reducing the ability of the server to handle
                                             				last-minute changes to the Outlook calendar data for users in a timely manner.
                                             				A smaller number increases the impact on the Unity Connection server while
                                             				increasing the ability of the server to handle last-minute changes to the
                                             				Outlook calendar data for users in a timely manner. In the Calendars: Short Calendar Caching
                                             				Poll Interval (In Minutes) field, enter the length of time that Unity
                                             				Connection waits between polling cycles when it caches upcoming Outlook
                                             				calendar data for calendar users who must have their calendar caches updated
                                             				more frequently. This setting applies to users who have the
                                             				Use Short Calendar Caching Poll Interval check box checked on their Edit User
                                             				Basics page. |
| Step 3 | Select Save . |