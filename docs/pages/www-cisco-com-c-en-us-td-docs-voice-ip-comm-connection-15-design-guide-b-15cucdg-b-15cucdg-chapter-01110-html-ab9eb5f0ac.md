---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-guide-b-15cucdg-b-15cucdg-chapter-01110-html-ab9eb5f0ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg/b_15cucdg_chapter_01110.html
retrieved_at: 2026-08-17T02:15:47.204627+00:00
---

Design Guide for Cisco Unity Connection 15

# Design Guide for Cisco Unity Connection 15

Updated: August 12, 2025

Chapter: Third-Party Fax Servers Integration

## Chapter: Third-Party Fax Servers Integration

# Third-Party Fax Servers Integration

### Third-Party Fax Servers Integration

## Introduction

Cisco Unity Connection supports third-party fax servers:

OpenText Fax Server and RightFax Edition. For more information, see the https://www.opentext.com/products/fax

Sagemcom Xmedius Fax SP version 6.5.5. For more information, see the https://www.opentext.com/about/brands/xmedius .

## Overview of Third-Party Fax Servers

Unity Connection interacts with the third-party fax servers directly through Simple Mail Transport Protocol (SMTP). Inbound
                           faxes are received by the third-party fax servers and routed to the Unity Connection server through SMTP. Similarly, faxes
                           are routed to the third-party fax servers through SMTP for rendering and outbound faxing.

If attachments are included with a fax or an email message that is sent to the third-party fax servers, Unity Connection sends
                           only the attachments that match the list of file name extensions that were selected during setup. third-party fax servers
                           support.dcx, .tif, and .txt files. You can add other file extensions that are also supported by the third-party fax servers.

Note that the file name of any attachment that cannot be sent to the fax machine will appear at the bottom of the message.

## Administration for Third-Party Fax Server

Administration of the fax service is performed on the third-party fax servers rather than in Cisco Unity Connection Administration.
                           You use the third-party fax servers administration to handle the following functionality:

Routing inbound fax messages to a user mailbox.

Managing and logging inbound fax messages.

Managing and logging outbound fax messages.

Additional functionality such as running reports, creating cover pages, and evaluating least-cost routing.

Cisco Unity Connection Administration is not used in any way to administer the third-party fax servers or the services provided
                           by the third-party fax servers.

## Managing Fax Messages by Users

When you integrate third-party fax servers with
                              		  Unity Connection, users are able to manage their fax messages using the clients
                              		  listed in Table 15-1 . Note that users
                              		  must be added to the third-party fax servers before they can, for example,
                              		  manage fax messages over the phone or from the Messaging Inbox.

Client Application

Details

Unity Connection phone menus

Users can hear new fax messages listed
                                          					 with other messages when they sign-in to Unity Connection by phone. For fax
                                          					 messages, Unity Connection plays only the message properties (for example, the
                                          					 sender, date, and time) and any voice annotation. The contents of the fax
                                          					 itself is not played. Users can forward a fax message to another user (when the
                                          					 message is not marked private) or reply to a fax with a voice message (when the
                                          					 fax message is from another user).

Users can add or change their fax
                                          					 number.

When the system has a fax server and an
                                          					 outgoing fax number is configured, users can send their fax messages to a fax
                                          					 machine. If the fax message has attachments, Unity Connection renders only
                                          					 those attachments with file extensions that were specified during setup.
                                          					 Attachments with other file extensions are removed, and Unity Connection lists
                                          					 the file names at the end of the fax message.

Messaging Assistant

Users can receive notification of new
                                          					 fax messages by phone or pager. Although users can enable a notification device
                                          					 by phone, they must use the Messaging Assistant to do the following:

Set up notification of the arrival
                                                						  of a fax message.

Set up a notification schedule for
                                                						  the notification device that they choose.

Third-party IMAP clients

Third-party IMAP clients can download
                                          					 fax messages. To view fax messages on third-party IMAP client workstations, the
                                          					 workstations must have the third-party fax servers client viewer application
                                          					 installed, or the fax message must be supported for viewing on the client
                                          					 workstation.

Users can forward a fax message to
                                          					 another user in the same way that they forward voice messages, or reply with a
                                          					 voice message if the fax message is from another user. In the fax message,
                                          					 users can use the buttons on the message toolbar to manage the message the same
                                          					 way that they handle email messages.

## Single Direct-Inward-Dial (DID) Number Support for Both Voice and Fax

Unity Connection supports using a single DID number to receive both voice calls and fax calls. In this configuration, incoming
                           calls are directed to a Cisco gateway that can detect a CNG (fax) tone. When a CNG tone is detected, the gateway forwards
                           the fax call to the third-party fax Servers. When no CNG tone is detected, the gateway forwards the voice call to the phone
                           system.

| Client Application | Details |
|---|---|
| Unity Connection phone menus | Users can hear new fax messages listed
                                          					 with other messages when they sign-in to Unity Connection by phone. For fax
                                          					 messages, Unity Connection plays only the message properties (for example, the
                                          					 sender, date, and time) and any voice annotation. The contents of the fax
                                          					 itself is not played. Users can forward a fax message to another user (when the
                                          					 message is not marked private) or reply to a fax with a voice message (when the
                                          					 fax message is from another user). Users can add or change their fax
                                          					 number. When the system has a fax server and an
                                          					 outgoing fax number is configured, users can send their fax messages to a fax
                                          					 machine. If the fax message has attachments, Unity Connection renders only
                                          					 those attachments with file extensions that were specified during setup.
                                          					 Attachments with other file extensions are removed, and Unity Connection lists
                                          					 the file names at the end of the fax message. |
| Messaging Assistant | Users can receive notification of new
                                          					 fax messages by phone or pager. Although users can enable a notification device
                                          					 by phone, they must use the Messaging Assistant to do the following: Set up notification of the arrival
                                                						  of a fax message. Set up a notification schedule for
                                                						  the notification device that they choose. |
| Third-party IMAP clients | Third-party IMAP clients can download
                                          					 fax messages. To view fax messages on third-party IMAP client workstations, the
                                          					 workstations must have the third-party fax servers client viewer application
                                          					 installed, or the fax message must be supported for viewing on the client
                                          					 workstation. Users can forward a fax message to
                                          					 another user in the same way that they forward voice messages, or reply with a
                                          					 voice message if the fax message is from another user. In the fax message,
                                          					 users can use the buttons on the message toolbar to manage the message the same
                                          					 way that they handle email messages. |

| Note | In order to prevent a user from sending a fax messages
                                       		  to a fax machine, do not configure a fax server in the Outgoing Fax Server
                                       		  field for the user on the User > Edit User Basics page in Cisco Unity
                                       		  Connection Administration. Even when prevented from sending a fax message to a
                                       		  fax machine, the user will still be able to receive and forward fax messages to
                                       		  another user. |
|---|---|