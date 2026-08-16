---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-exchange-integration-15-cup0-b-ms-outlook-calendar-integrat-a9201ea869
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/exchange_integration/15/cup0_b_ms-outlook-calendar-integration-15/cup0_b_ms-outlook-calender-integration-1251_chapter_01.html
retrieved_at: 2026-08-16T16:15:12.493215+00:00
---

Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs

# Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs

Updated: March 18, 2026

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Overview

Microsoft Outlook calendar integration with the IM and Presence Service allows users to incorporate their calendar/meeting status in Microsoft Outlook into their availability status on the IM and Presence Service server. This integration can be accomplished by connecting the IM and Presence Service to an on-premises Microsoft Exchange
                              server or a hosted Office 365 server .

## Deployment

### Exchange Web Services

Exchange Web
                                 		Services (EWS) allows interaction with
                                 		Microsoft Exchange mailboxes and contents over HTTP. EWS provides access to
                                 		much of the same data that is made available through Microsoft Outlook. EWS moves several
                                 		responsibilities from the client computer to the server.

## Microsoft Outlook Calendaring States on the IM and Presence Service

Microsoft Outlook integration with the IM and
                                 		  Presence Service via Microsoft Exchange or Office 365 allows users to incorporate their calendar/meeting
                              		status in Microsoft Outlook into their availability status on the IM and
                                 		  Presence Service . The table below shows the reachability mappings,
                              		and how the IM and
                                 		  Presence Service correlates the status of meetings (as shown in
                              		Microsoft Outlook calendar) in the availability status of users on the IM and
                                 		  Presence Service .

Microsoft Outlook State

IM and Presence
                                             						Service State

Free/Tentative

Available

Busy

In a meeting

Out-of-Office 1

Away

Away 2

Away

1 Microsoft Outlook
                              		2007 
                              	 and Microsoft Outlook 2010 desktop client.

2 Microsoft Outlook
                              		Web Access (OWA) 2010.

## Restrictions and Limitations

The following are
                              		restrictions and limitations for integrating the IM and
                                 		  Presence Service with Microsoft Exchange:

- You can add, update, or
                                 		  delete one or more EWS servers with no maximum limit. However, the Troubleshooter on the Presence
                                    			 Gateway Configuration window is designed to only verify and report
                                 		  status of the first 10 EWS servers that you configure.

- This release of the IM and
                                    			 Presence Service does not support the Exchange autodiscover service.
                                 		  The autodiscover service assumes that a load-balancing mechanism is already in
                                 		  place across the Client Access Server (CAS) or servers.

Upon configuring Exchange server or an Office 365 server as Presence Gateway the Jabber Clients will not be able to set 'In a meeting’ status when they have a meeting received from their local Outlook. The 'In a meeting' status can only come via the Presence Gateway. If the Presence Gateway goes down for any reason the clients will not be able
                                    to set 'In a meeting' status .

| Microsoft Outlook State | IM and Presence
                                             						Service State |
|---|---|
| Free/Tentative | Available |
| Busy | In a meeting |
| Out-of-Office 1 | Away |
| Away 2 | Away |

| Note | In order to have a ‘In a meeting' status set you must restore service for the Presence Gateway. |
|---|---|