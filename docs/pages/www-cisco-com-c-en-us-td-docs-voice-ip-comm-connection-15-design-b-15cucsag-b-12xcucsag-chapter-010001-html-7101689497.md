---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-b-15cucsag-b-12xcucsag-chapter-010001-html-7101689497
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/b_15cucsag/b_12xcucsag_chapter_010001.html
retrieved_at: 2026-08-17T03:46:38.051135+00:00
---

System Administration Guide

# System Administration Guide

Updated: June 27, 2023

Chapter: Fax Server

## Chapter: Fax Server

# Fax Server

## Fax Server

Cisco Unity Connection supports third-party fax servers. Fax server integration is one of the advanced features supported
                           with Unity Connection providing additional messaging capabilities. It enables users to receive faxes in the mailbox and forward
                           a received fax to other users or fax machines for printing. Users can manage faxes using phone, Messaging Inbox, or IMAP client.

Unity Connection interacts with the third-party fax servers directly through Simple Mail Transport Protocol (SMTP). Inbound
                           faxes are received by the third-party fax servers and routed to the Unity Connection server through SMTP. Similarly, faxes
                           are routed to the third-party fax servers through SMTP for rendering and outbound faxing.

For more information on fax servers supported with Unity Connection, see the “Third-Party Fax Servers Integration” chapter
                           of the Design Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

Cisco does not sell Cisco Fax Server. Refer to the end-of-sale/end-of-line notice at https://docplayer.net/42962914-End-of-sale-and-end-of-life-announcement-for-the-cisco-fax-server.html .

## Task List for Configuring Fax Server Integration

Fax server must be installed and configured before configuring the Unity Connection server. Do the following steps to create
                           a Fax Server integration in Unity Connection:

Install and Configure the Fax Server.

Configure Unity Connection. See the Configuring Unity Connection for Fax Server Integration section.

Configure the Unity Connection user accounts. See the Configuring or Updating Users for Fax Server Integration section.

## Configuring Unity Connection for Fax Server Integration

### Configure SMTP on Unity Connection server

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings and select SMTP Configuration > Server.

Step 2

On the SMTP Server Configuration page, in
                                          			 the Edit menu, select Search IP Address Access List.

Step 3

On the Search IP Address Access List page,
                                          			 select Add New.

Step 4

On the New Access IP Address page, in the IP Address field, enter the IP address of the Fax Server and select Save.

Step 5

Check the Allow Unity Connection check box
                                          			 and select Save.

### Enabling or Updating Fax Server Integration on Unity Connection

Step 1

In Unity Connection Administration, expand
                                          			 System Settings and select Fax Server.

Step 2

On the Edit Fax Server page, check the
                                          			 Enabled check box.

Step 3

In the Fax Server Name field, enter a descriptive name for the Fax Server.

Step 4

In the SMTP Address field, enter the fully qualified SMTP address of the SMTP server on the Fax Server.

Caution

This fully qualified SMTP address must match the server address and domain that are configured for the POP3 mailbox on the
                                                         Fax Server. Otherwise, the integration do not function correctly.

Step 5

In the IP Address field, enter the IP address of the Fax Server.

Step 6

If you use a smart host SMTP server to deliver faxes from the Fax Server to Unity Connection, check the Use Smart SMTP Host
                                          check box. Otherwise, uncheck this check box.

Step 7

Select Save.

### Customizing or Updating Fax Server Integration on Unity Connection

To Customize or Update the Fax Server Integration on Unity Connection

Step 1

In Unity Connection Administration, expand System Settings, then select Advanced > Fax.

Step 2

In the Fax Configuration page, in the Faxable File Types field, enter the file extensions (separated by a comma) that Unity
                                          Connection keeps in messages that are delivered to the Fax Server. Unity Connection removes all files with other file extensions
                                          before delivering the message to the Fax Server.

Step 3

In the Subject Prefix for Notification of a Successful Fax field, enter the prefix that the Fax Server adds to the Subject
                                          field of fax reports. When Unity Connection detects this prefix, it generates a delivery receipt and places it in the user
                                          mailbox.

Step 4

In the Subject Prefix for Notification of a Failed Fax field, enter the prefix that the Fax Server adds to the Subject field
                                          of fax reports. When Unity Connection detects this prefix, it generates a non-delivery receipt and places it in the user mailbox.

Step 5

Select Save.

## Configuring or Updating Users for Fax Server Integration

The Fax Server must have a subscriber for each Unity Connection user that you are configuring.

While on the phone, users can add or change the number for the fax machine that they send faxes to for printing.

To Configure Unity Connection Users for Fax Server Integration

Step 1

In Unity Connection Administration, expand Users and select
                                       			 Users.

Step 2

On the Search Users page, select the alias of a user.

If the user alias does not appear in the search results table,
                                                      				  set the applicable parameters in the search fields at the top of the page and
                                                      				  select Search.

Step 3

On the Edit User Basics page, in the Outgoing Fax Number field,
                                       			 enter the number for the fax machine that users send faxes to for printing.

Step 4

In the Outgoing Fax Server field, select the name of the Fax Server.

Step 5

Select Save.

Step 6

Repeat Step 2 through Step 5 for all remaining users.

You can use Bulk Edit mode to add or change fax extensions for
                                                      				  multiple users at once.

## Testing Fax Server Integration

Step 1

Send a fax to the fax extension of a user who has been configured for the Fax Server integration.

Step 2

Sign in to the Unity Connection mailbox of the user to whom you
                                       			 sent the fax.

Step 3

If the user account is configured for speech access, say Play
                                       			 Messages.

If the user account is not configured for speech access, press
                                          				1, and then follow the prompts to list messages.

Step 4

When you hear the system announce the fax that you just sent,
                                       			 either say Fax, or press the applicable keys on the phone keypad to print the
                                       			 fax.

| Note | Cisco does not sell Cisco Fax Server. Refer to the end-of-sale/end-of-line notice at https://docplayer.net/42962914-End-of-sale-and-end-of-life-announcement-for-the-cisco-fax-server.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings and select SMTP Configuration > Server. |
|---|---|
| Step 2 | On the SMTP Server Configuration page, in
                                          			 the Edit menu, select Search IP Address Access List. |
| Step 3 | On the Search IP Address Access List page,
                                          			 select Add New. |
| Step 4 | On the New Access IP Address page, in the IP Address field, enter the IP address of the Fax Server and select Save. |
| Step 5 | Check the Allow Unity Connection check box
                                          			 and select Save. |

| Step 1 | In Unity Connection Administration, expand
                                          			 System Settings and select Fax Server. |
|---|---|
| Step 2 | On the Edit Fax Server page, check the
                                          			 Enabled check box. |
| Step 3 | In the Fax Server Name field, enter a descriptive name for the Fax Server. |
| Step 4 | In the SMTP Address field, enter the fully qualified SMTP address of the SMTP server on the Fax Server. Caution This fully qualified SMTP address must match the server address and domain that are configured for the POP3 mailbox on the
                                                         Fax Server. Otherwise, the integration do not function correctly. | Caution | This fully qualified SMTP address must match the server address and domain that are configured for the POP3 mailbox on the
                                                         Fax Server. Otherwise, the integration do not function correctly. |
| Caution | This fully qualified SMTP address must match the server address and domain that are configured for the POP3 mailbox on the
                                                         Fax Server. Otherwise, the integration do not function correctly. |
| Step 5 | In the IP Address field, enter the IP address of the Fax Server. |
| Step 6 | If you use a smart host SMTP server to deliver faxes from the Fax Server to Unity Connection, check the Use Smart SMTP Host
                                          check box. Otherwise, uncheck this check box. |
| Step 7 | Select Save. |

| Caution | This fully qualified SMTP address must match the server address and domain that are configured for the POP3 mailbox on the
                                                         Fax Server. Otherwise, the integration do not function correctly. |
|---|---|

| Step 1 | In Unity Connection Administration, expand System Settings, then select Advanced > Fax. |
|---|---|
| Step 2 | In the Fax Configuration page, in the Faxable File Types field, enter the file extensions (separated by a comma) that Unity
                                          Connection keeps in messages that are delivered to the Fax Server. Unity Connection removes all files with other file extensions
                                          before delivering the message to the Fax Server. |
| Step 3 | In the Subject Prefix for Notification of a Successful Fax field, enter the prefix that the Fax Server adds to the Subject
                                          field of fax reports. When Unity Connection detects this prefix, it generates a delivery receipt and places it in the user
                                          mailbox. |
| Step 4 | In the Subject Prefix for Notification of a Failed Fax field, enter the prefix that the Fax Server adds to the Subject field
                                          of fax reports. When Unity Connection detects this prefix, it generates a non-delivery receipt and places it in the user mailbox. |
| Step 5 | Select Save. |

| Note | The Fax Server must have a subscriber for each Unity Connection user that you are configuring. |
|---|---|

| Step 1 | In Unity Connection Administration, expand Users and select
                                       			 Users. |
|---|---|
| Step 2 | On the Search Users page, select the alias of a user. Note If the user alias does not appear in the search results table,
                                                      				  set the applicable parameters in the search fields at the top of the page and
                                                      				  select Search. | Note | If the user alias does not appear in the search results table,
                                                      				  set the applicable parameters in the search fields at the top of the page and
                                                      				  select Search. |
| Note | If the user alias does not appear in the search results table,
                                                      				  set the applicable parameters in the search fields at the top of the page and
                                                      				  select Search. |
| Step 3 | On the Edit User Basics page, in the Outgoing Fax Number field,
                                       			 enter the number for the fax machine that users send faxes to for printing. |
| Step 4 | In the Outgoing Fax Server field, select the name of the Fax Server. |
| Step 5 | Select Save. |
| Step 6 | Repeat Step 2 through Step 5 for all remaining users. Note You can use Bulk Edit mode to add or change fax extensions for
                                                      				  multiple users at once. | Note | You can use Bulk Edit mode to add or change fax extensions for
                                                      				  multiple users at once. |
| Note | You can use Bulk Edit mode to add or change fax extensions for
                                                      				  multiple users at once. |

| Note | If the user alias does not appear in the search results table,
                                                      				  set the applicable parameters in the search fields at the top of the page and
                                                      				  select Search. |
|---|---|

| Note | You can use Bulk Edit mode to add or change fax extensions for
                                                      				  multiple users at once. |
|---|---|

| Step 1 | Send a fax to the fax extension of a user who has been configured for the Fax Server integration. |
|---|---|
| Step 2 | Sign in to the Unity Connection mailbox of the user to whom you
                                       			 sent the fax. |
| Step 3 | If the user account is configured for speech access, say Play
                                       			 Messages. If the user account is not configured for speech access, press
                                          				1, and then follow the prompts to list messages. |
| Step 4 | When you hear the system announce the fax that you just sent,
                                       			 either say Fax, or press the applicable keys on the phone keypad to print the
                                       			 fax. |