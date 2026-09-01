---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-socialminer-200892-integrate-uccx-with-socialminer-for-agen-ht-afa800b9d5
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/socialminer/200892-integrate-uccx-with-socialminer-for-agen.html
retrieved_at: 2026-09-01T14:57:27.810399+00:00
---

Integrate UCCX with SocialMiner for Agent Email - Exchange Best Practices

# Integrate UCCX with SocialMiner for Agent Email - Exchange Best Practices

### Download Options

Updated: October 12, 2017

Document ID: 200892

Contents

## Contents

## Introduction

This document provides an overview of the Best Practices to be followed on Exchange for integration with SocialMiner and Cisco Unified Contact Center Express (UCCX) for Agent Email.

Built on the implementation of multi-session chat in UCCX in version 10.5, version 10.6 introduces email.  Emails are fetched from Microsoft Exchange by SocialMiner and are routed to agents by UCCX.  Agents use a new email reply template in the multi-session gadget in Finesse to reply to emails.

UCCX 11.5 and SocialMiner 11.5 provides the capability of integration with Microsoft Office 365 for email feature. Office365 is a cloud based email account management from Microsoft and hence it does not have any specific performance improvements.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Express (UCCX) Release 10.6 onwards

- Microsoft Active Directory - AD installed on Windows Server

- Microsoft Exchange 2010 and 2013

- Cisco SocialMiner Release 10.6 onwards

### Components Used

The information used in this document is based on these software and hardware versions:

- Microsoft Active Directory - AD on Windows 2012 R2

- Microsoft Exchange 2010 and 2013

- SocialMiner version 10.6

- Cisco Unified Contact Center Express (UCCX) version 10.6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Network Diagram

Note : Please note that SocialMiner does not actually store emails in it's database. It stores metadata that it uses to retrieve the email from the email server. This metadata is also used when the agent replies to the email.

### Configurations

Note : This document provides the lab install and configuration of Exchange 2013 as an example. Although this is a tested configuration on the Exchange, Cisco does not provide any restrictions on the Exchange deployments. This document does not take into production deployments and custom configurations.

Note : This document provides the examples of Exchange focused on 2013 and similar considerations are to be observed on Exchange 2010. It is recommended to use this article with the help of an Exchange Administrator for the optimal solution.

Note : This document provides the best practices in conjunction to the problems seen from custom deployments since there is no major restriction from SocialMiner and UCCX for Exchange.

### Time Synchronization

Be sure to have your ESX host configured for NTP and verify the status.  Check the configuration tab of the host and select time configuration.

For the Domain controller, ensure the time is synchronized with the host.  This is under the vm/edit settings/options tab, VMware Tools.  Check the box that says synchronize guest time with host and click OK.

Note : The Domain Controller can have the time synchronization with any other source. In most deployments, the Domain Controller itself would act as the time source. Ensure that this remains in sync with the host where the exchange would be deployed.

### Exchange 2013

Set DNS to the Active Directory Server in the domain.

Join the domain as highlighted below.

Authenticate with an Administrative Account in the domain.

#### Prerequisites

The prerequisites are documented in the link here

In the above link, follow Windows Server 2012 R2 and Windows Server 2012 prerequisites section (depends on the platform used for install), Mailbox or Client Access server roles need to be to followed to install Mailbox or client access server roles.

Open PowerShell with Administrator privileges and run following commands:

```
Install-WindowsFeature AS-HTTP-Activation, Desktop-Experience, NET-Framework-45-Features, RPC-over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-Clustering-Mgmt, RSAT-Clustering-PowerShell, Web-Mgmt-Console, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression, Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console, Web-Metabase, Web-Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-Request-Monitor, Web-Server, Web-Stat-Compression, Web-Static-Content, Web-Windows-Auth, Web-WMI, Windows-Identity-Foundation, RSAT-ADDS
```

```
Install-WindowsFeature Server-Media-Foundation
```

Reboot the server to finish the installation.

Download and install "Unified Communications Managed API 4.0 Runtime". This installation is simple. Accept the license, click Next on each intermediate dialog, and then click Finish.

(You must reboot now before starting the exchange 2013 install)

#### Install

Run the "Exchange 2013" installer. The first frame prompts to check for updates. Click next.

In this case, no updates we found. Click next.

The introduction screen displays. Click next.

Accept the license and click next.

Select "Use recommended settings" and click next.

Select "Mailbox role", "Client Access role", and "Automatically install Windows Server roles". Click next.

Keep the default location and click next.

Set the organization. Click next.

Leave malware scanning enabled. Click next.

Final verifications are performed. This can take a while to get started. Once complete, click next.

Note : A restart of the server would possibly be needed, if it gets to the end of Readiness Checks and informs about a pending restart. Restart the server at this point and rerun the installer. After the restart we can continue with the readiness checks and proceed with install.

Select install.

Click Finish. Exchange installation is successful.  Reboot as instructed.

#### Administration

Exchange administration can be accessed by the URL:

```
https://<exchangeServerIp>/ecp/ or just https://localhost/ecp
```

Ensure HTTPS.

Select "User mailbox".

Note : The account type must be User Mailbox. Room and Equipment mailboxes are not supported as they only accept and respond to Outlook Meeting and Event Requests.

This brings up the"User Mailbox" dialog. Enter the details for a new email user.

#### Outlook Web Access

Log in to Outlook Web Access:

```
https://<exchangeServerIp>/owa or just https://localhost/owa
```

Ensure HTTPS.

#### UCCX Integration with SocialMiner

The configuration for the UCCX and SocialMiner based Agent Email requires configuration on the UCCX appadmin page to create the SocialMiner configuration, create the Mail Server and the email Contact Service Queue.

Refer to this document for further information

UCCX Agent Email

## Best Practices

### Enable IMAP4 on Exchange 2013

From the Exchange Management Shell Run the following commands:

Set the Microsoft Exchange IMAP4 service to start automatically:

```
Set-service msExchangeIMAP4 -startuptype automatic
```

Start the Microsoft Exchange IMAP4 service:

```
Start-service msExchangeIMAP4
```

Set the Microsoft Exchange IMAP4 Backend service to start automatically:

```
Set-service msExchangeIMAP4BE -startuptype automatic
```

Start the Microsoft Exchange IMAP4 Backend service:

```
Start-service msExchangeIMAP4BE
```

### Set Connection Limits for IMAP4 on Exchange 2013

From the Exchange Management Shell Run the following commands:

This example sets the connection limit for a user:

```
Set-ImapSettings -MaxConnectionsPerUser Value
```

Note : The default value is 16. This has been set to 200 in the lab environments, however it can be increased for larger deployments.

### Message Size Limits (SocialMiner 11.6 and up)

From SocialMiner 11.6, we allow attachments up to 20 MB in size for inbound and outbound emails. As a general rule, to account for size increases due to encoding and encryption, we suggest setting the maximum message size limit in Exchange to 30 MB .

Note : Exchange does not consider attachment size limit on the transport configuration. Exchange considers the combined size of all the message parts, body and attachments, when message size limit rules are applied.

### Message Rate Limits

The following commands are useful to examine and adjust rate limiprets for the Client Frontent connector. This is the connector used by SMTP. All of these commands must be executed from the Exchange Management Shell.

Get message rate limit for connectors:

```
Get-ReceiveConnector | ft Name,MessageRateLimit
```

Get details for a connector:

```
Get-ReceiveConnector -Identity "Client Frontend <EXCHANGE2013 hostname>"
```

Increase the rate limit for the connector that supports SMTP:

```
Get-ReceiveConnector -Identity "Client Frontend <EXCHANGE2013 hostname>" | Set-ReceiveConnector -MessageRateLimit 50
```

```
Get-ReceiveConnector -Identity "Client Proxy <EXCHANGE2013 hostname>" |  Set-ReceiveConnector -MessageRateLimit 100
```

### How to Create New Databases and Move mailboxes into them in Exchange 2010

- Open Exchange Management Console

- Navigate to Organization Configuration -> Mailbox

- In the Action pannel on the right - click "New Mailbox Database..."

- Give the Database a name, Browse to select a server, click Next.  Click Next.  Click Next.  Click Finish

- Navigate to Recipient Configuration -> Mailbox

- Click to select the mailbox(s) you want to move, then click "New Local Move Request..."

- Browse to select the target database you want to move the mailbox to.  Click Next.  Click Next.  Click New.  Click Finish

- To see the progress of the Move request: Navigate to Recipient Configuration -> Move Request

### How to Create New Databases and Move mailboxes into them in Exchange 2013

- Open ECP : https://<yourExchangeServer>/ecp

- Navigate to Servers -> Databases and click Add

- Give the new database a name and browse to select your server.  Click save

- Navigate to Recipients -> Migration and click Add

- Select Move to a different database

- Select the user mailboxes that you want to move.  Click next.  Give it a name.  Click next.  Click new

- You can see the progress of the move request by selecting the request that you just created and clicking on View details in the pane to the right

#### How to prevent the rapid growth of disk space on exchange server

Turn on Circular logging for both Exchange 2010 and 2013

Open Exchange Management Shell

Run the command: Get-Mailboxdatabase | Set-MailboxDatabase -CircularloggingEnabled:$true

You then need to dismount and mount the databases for the change to take effect.

Dismount-Database -Identity "Mailbox Database Name"

Mount-Database -Identity "Mailbox Database Name"

You can also mount and dismount when you login to the Exchange Management Console (2010) or ecp (2013)

(2010) Organization Configuration -> Mailbox

Select the database and in the Actions on the bottom right, select Dismount Database.  When finished, select Mount Database.

(2013) Servers -> Databases

Select the database then click the "..." icon and click Dismount.  When finished, click the "..." icon again and click Mount.

Wait for indexes to be healthy.  Run the command to verify

Get-MailboxDatabaseCopyStatus

Note : Please note that SocialMiner does not support encoding format other than UTF -8 for Exchange. Also it is recommended to install spam/malware detection tool on Exchange since UCCX or SocialMiner do not have the capability to identify malware/spam emails and can lead to issues.

## Common Problems

### Email Reply Issues

Problem Summary

1. Replies to emails sent from a Finesse Agent to external email addresses fail, while replies to internal email addresses succeeed but with the FROM address as you User Principal Name (UPN) rather than a valid email address.

2. SocialMiner cannot connect the email feed to Exchange because Exchange does not allow authentication with the external .com account

Error Message

Finesse:

"Unable to reply to customer's email. Click Send to retry, or requeue. If the problem persists, contact your system administrator."

SocialMiner Email feed:

Red X - "Cannot establish connection with the email server. Check that the username and password are correct"

Possible Cause

Check the UPN settings on the Active Directory

Recommended Action

Example:

In CCX Admin, Email CSQ was configured with - Mail Server: companyXX.local Email username: CSQname@XXindustries.com IMAP port: 993 SMTP port: 587

The organization doesn't have the imap and smtp as same entity. We have split DNS, internal .local and external .com

For SocialMiner to work, we put in the email address that is used for both IMAP and SMTP, but the internal emails only pass with the .local and reply emails can only be sent from a .com

Resolution:

Create an UPN suffix for a .com that would allow for authentication flexibility across the internal and external environments. This is done on the AD on the Exchange side to include the .com in the local network for authentication purposes. This is typically used for an orgnaization with presence in multiple countries for usernames to authenticate with different domain suffixes. This allows both the IMAP traffic and the SMTP traffic to authenticate.

In Domain Name Server (DNS) - "Domains and Properties", create a UPN suffix for the accounts to simplify logging in across large organizations.

Active Directory "Users and Computers" requires the default UPN that was specified at log in. The UPN specified at log in would match the email address.

### Non Voice Subsystem Crash on UCCX

Problem Summary

Non Voice Subsystem Crashes on UCCX

Possible Cause

Recommended Action

- Apply a filter to detect emoji characters in the From/To or Subject line on the Exchange side.

- Refer to the defect CSCuz48341 . This issue has been fixed on UCCX release 11.5.1.

### Openfire Heap Dumps on SocialMiner

Problem Summary

SocialMiner Extensible Messaging and Presence Protocol (XMPP) Service (Openfire) does not clean up http sessions properly that lead to a leak. Heap dumps are created which lead to performance issues on Chat and Email with SocialMiner

Possible Cause

OpenFire version 3.7.1 that is used for SocialMiner 10.6 has a known bug and this seems to have been addressed in a later version. http://issues.igniterealtime.org/browse/OF-453

Recommended Action

- SocialMiner 11.x has the latest openfire version 3.8.2, which has the known fix.

If you are on 10.6, then apply the COP file here

### Email Feed unable to Connect

Problem Summary

SocialMiner cannot connect email feed to Exchange

Possible Cause

SocialMiner and UCCX are functional on version 11.5 integrated with Exchange 2010 and 2013. Once upgraded to 11.6, the Email Server on UCCX Appadmin will show Red X.

SocialMiner logs indicate:

runtime/CCBU-runtime.2017-06-20T18-37-42.745.log: Caused by: javax.net.ssl.SSLHandshakeException: Server chose TLSv1, but that protocol version is not enabled or not supported by the client.

runtime/CCBU-runtime.2017-06-20T18-37-42.745.log:0000837786:: Jun 20 2017 21:18:36.552 +0000: %CCBU__________FEEDS-3-SECURE_IMAP_CLIENT_CONNECTION_EXCEPTION: %[FEED_ID=100021][FEED_NAME=CCX Email Feed Team_IT_Tier2_Email][exception= javax.mail.MessagingException: Server chose TLSv1, but that protocol version is not enabled or not supported by the client.;

Recommended Action

Login to the SocialMiner Command Line Interface (CLI) and run the following commands:

- set tls client min-version 1.0

- utils system restart (This restarts the SocialMiner server)

## Troubleshoot

### Resolve DNS related errors on Exchange 2013

Exchange 2013 451 4.7.0 Temporary server error. Please try again later. PRX5 . It is a known issue on exchange 2013 (check for updates from Microsoft).

Resolution : Ensure the receive connectors network adapter is bound to a specific IP address and not "All IPv4 addresses" . More details

http://www.techieshelp.com/exchange-2013-451-4-7-0-temporary-server-error-please-try-again-later-prx5/

User sends an email but instead of a successful send, the email sits in the "Draft" folder.

Resolution: Use Exchange Administration Center (EAC) follow the below steps :

- Log in into EAC

- Navigate to Servers (item on the bottom left in the EAC UI)

- Double click the server (you must see your exchange server listed)

- Click on DSN lookups

- Ensure the network adapter settings are correct and is set to correct host instead of "All IPv4 addresses"

#### Setup Permissions in Exchange so that you can clean the database and troubleshoot

In 2010

- Open Exchange Management Console.  Expand the tree and select Toolbox.  Double click on Role Based Access Control (RBAC) User Editor

- When the browser opens, Log in as Administrator

- Edit Discovery Management and Add Administrator as a Member

- Edit Organization Management and Add Mailbox Import Export as a Role

- Save

- Close and Re-open the Exchange Management Shell.  The new permissions are loaded

In 2013

- Open ECP.  Navigate to Permissions -> Admin Roles

- Edit Discovery Management and Add Administrator as a Member

- Edit Organization Management and Add Mailbox Import Export as a Role

- Save

- Close and Re-open the Exchange Management Shell.  The new permissions are loaded

#### To prevent extensive disk growth, turn off deleted Item retention

Open Exchange Management Console

For each database,

Set-MailboxDatabase -Identity <DatabaseName> -DeletedItemRetention 0

To verify it worked,

Get-MailboxDatabase | ft name,deleteditemretention

#### Purge all deleted Items (after you change the retention option down)

Purge all deleted Items saved for potential recovery.  Do this for perfcustomer and perfqueue1-20.

Search-Mailbox -Identity "<mailboxName>" -SearchDumpsterOnly -DeleteContent -Force

#### Shrink the .EDB file to check the free space is available in your Database and Recover space

Recover any empty space left in the database to shrink the EDB file:

Get-MailboxDatabase -Status | ft name,databasesize,availablenewmailboxspace -auto

If you see a large amount of AvailableNewMailboxSpace, then the database can be defragmented to recover the space.

You need at least the amount of the new DatabaseSize available to run the below commands.  You can calculate how much you need by ("DatabaseSize" - " AvailableNewMailboxSpace") * 1.1 = DiskSpaceNeeded for NewDatabaseSize

Dismount-Database "DBtoShrink"

cd c:\Program Files\Microsoft\Exchange Server\V15\Mailbox\DBtoShrink

eseutil /d DBtoShrink.edb /t C:\defrag\temp.edb

When this completes, remount the database:

Mount-Database "DBtoShrink"

Run this command again to see how much space is available now:

Get-MailboxDatabase -Status | ft name,databasesize,availablenewmailboxspace -auto

#### If your .EDB file is still very large, but you don't have much data in it - create a new Database, move your old mailboxes into it and delete the old database to reclaim the space

To completely reclaim all Disk space, create a new database and move all of the mailboxes to it, then delete the old.

New-MailboxDatabase -Name "NewDB1" -Server "ExchangeServerName" -EdbFilePath C:\Program Files\Microsoft\Exchange Server\V15\Mailbox\NewDB1\NewDB1.edb

Mount-Database -Identity "NewDB1"

Turn on circular logging,

Get-Mailboxdatabase | Set-MailboxDatabase -CircularloggingEnabled:$true

Dismount-Database -Identity "NewDB1"

Mount-Database -Identity "NewDB1"

Wait for indexes to be healthy.  Run the command to verify:

Get-MailboxDatabaseCopyStatus

Move mailboxes from old database to new database:

Get-Mailbox -Database "OldDB1" | New-MoveRequest -TargetDatabase "NewDB1"

In Exchange 2010 you can clear existing MoveRequests before you can run the above command.  Open Exchange Management Console.  Navigate to Recipient Configuration -> Move Request.

Select all move requests and click on "Clear Move Request" in the Action panel on the right.

Wait until the status is completed.  To see the status,

Get-MoveRequestStatistics -MoveRequestQueue "NewDB1"

Dismount old database:

Dismount-Database "OldDB1"

Verify that you can access all mailboxes in the new database as expected, then delete the old database.  Use the command line or ECP. Under  Servers -> Databases.  Select the oldDB1 database and click on delete.

#### Common problems for slowness on Exchange Server

Step 1. Exchange Server physical disk is low on space.

Step 2. Exchange mailboxes have reached their limit (Default is 2GB).

Step 3. Check the database content index state - it can show failed or failedAndSuspended.

Use ECP for Exchange 2013

- Navigate to https://<your exchange server>/ecp and Log in

- Navigate to Servers -> Databases , select your mailbox database, and look in the right pane where you should see "Content index state:".  It must show "Healthy".  If it doesn't, follow the link below to fix

Use Exchange Management Shell (Both Exchange 2013 and Exchange 2010)

- Run the command: Get-MailboxDatabaseCopyStatus

- "Content index state:" must show "Healthy".  If it doesn't, follow the link below to fix

Use Exchange Management Console for Exchange 2010

- Navigate to Microsoft Exchange On-Premises -> Server Configuration -> Mailbox

- In the Database Copies tab, click on your Database

- Under Actions on the right, click on Properties.  In the pop-up window general tab check "Content index state:".  It must show "Healthy".  If it doesn't, follow the link below to fix

To fix the content index state follow these instructions: http://theucguy.net/fix-corrupted-content-index-catalog-of-a-mailbox-database-with-single-copy/

## Related Information

- Unsupported configurations for UCCX and SocialMiner Integration for Non-Voice

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see  What’s New in Cisco Product Documentation at: http://www.cisco.com/c/en/us/td/docs/general/whats new/whatsnew.html .

Subscribe to What’s New in Cisco Product Documentation, which lists all new and revised Cisco technical documentation, as an RSS feed and deliver content directly to your desktop using a reader application. The RSS feeds are a free service.

### Revision History

1.0

17-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Arundeep Nagaraj

Cisco TAC Engineer

Gino Schweinsberger

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Express

| Problem Summary | 1. Replies to emails sent from a Finesse Agent to external email addresses fail, while replies to internal email addresses succeeed but with the FROM address as you User Principal Name (UPN) rather than a valid email address. 2. SocialMiner cannot connect the email feed to Exchange because Exchange does not allow authentication with the external .com account |
|---|---|
| Error Message | Finesse: "Unable to reply to customer's email. Click Send to retry, or requeue. If the problem persists, contact your system administrator." SocialMiner Email feed: Red X - "Cannot establish connection with the email server. Check that the username and password are correct" |
| Possible Cause | Check the UPN settings on the Active Directory |
| Recommended Action | Example: In CCX Admin, Email CSQ was configured with - Mail Server: companyXX.local Email username: CSQname@XXindustries.com IMAP port: 993 SMTP port: 587 The organization doesn't have the imap and smtp as same entity. We have split DNS, internal .local and external .com For SocialMiner to work, we put in the email address that is used for both IMAP and SMTP, but the internal emails only pass with the .local and reply emails can only be sent from a .com Resolution: Create an UPN suffix for a .com that would allow for authentication flexibility across the internal and external environments. This is done on the AD on the Exchange side to include the .com in the local network for authentication purposes. This is typically used for an orgnaization with presence in multiple countries for usernames to authenticate with different domain suffixes. This allows both the IMAP traffic and the SMTP traffic to authenticate. In Domain Name Server (DNS) - "Domains and Properties", create a UPN suffix for the accounts to simplify logging in across large organizations. Active Directory "Users and Computers" requires the default UPN that was specified at log in. The UPN specified at log in would match the email address. |

| Problem Summary | Non Voice Subsystem Crashes on UCCX |
|---|---|
| Possible Cause | Non Voice Subsystem Crashes due to the presence of Emoji characters in the email subject line. The issue happens when this email is presented to an agent and the agent requeues the email back to the same or another CSQ. The reason is that when characters are passed to Openfire of UCCX, the Openfire crashes as it accepts only valid XML (Extensible Markup Language) 1.0 character set. Emoji's characters are not a part of the XML 1.0 character set. |
| Recommended Action | Apply a filter to detect emoji characters in the From/To or Subject line on the Exchange side. Refer to the defect CSCuz48341 . This issue has been fixed on UCCX release 11.5.1. |

| Problem Summary | SocialMiner Extensible Messaging and Presence Protocol (XMPP) Service (Openfire) does not clean up http sessions properly that lead to a leak. Heap dumps are created which lead to performance issues on Chat and Email with SocialMiner |
|---|---|
| Possible Cause | OpenFire version 3.7.1 that is used for SocialMiner 10.6 has a known bug and this seems to have been addressed in a later version. http://issues.igniterealtime.org/browse/OF-453 |
| Recommended Action | SocialMiner 11.x has the latest openfire version 3.8.2, which has the known fix. If you are on 10.6, then apply the COP file here |

| Problem Summary | SocialMiner cannot connect email feed to Exchange |
|---|---|
| Possible Cause | SocialMiner and UCCX are functional on version 11.5 integrated with Exchange 2010 and 2013. Once upgraded to 11.6, the Email Server on UCCX Appadmin will show Red X. SocialMiner logs indicate: runtime/CCBU-runtime.2017-06-20T18-37-42.745.log: Caused by: javax.net.ssl.SSLHandshakeException: Server chose TLSv1, but that protocol version is not enabled or not supported by the client. runtime/CCBU-runtime.2017-06-20T18-37-42.745.log:0000837786:: Jun 20 2017 21:18:36.552 +0000: %CCBU__________FEEDS-3-SECURE_IMAP_CLIENT_CONNECTION_EXCEPTION: %[FEED_ID=100021][FEED_NAME=CCX Email Feed Team_IT_Tier2_Email][exception= javax.mail.MessagingException: Server chose TLSv1, but that protocol version is not enabled or not supported by the client.; |
| Recommended Action | Login to the SocialMiner Command Line Interface (CLI) and run the following commands: set tls client min-version 1.0 utils system restart (This restarts the SocialMiner server) |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Oct-2017 | Initial Release |