---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-b-planning-guide-cisco-jabber-14-0-cjab-b-planning-guide-ci-93c7e21bd9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_b_planning-guide-cisco-jabber-14_0/cjab_b_planning-guide-cisco-jabber-129_chapter_01001.html
retrieved_at: 2026-08-21T19:05:13.478564+00:00
---

Planning Guide for Cisco Jabber 14.0

# Planning Guide for Cisco Jabber 14.0

Updated: April 2, 2024

Chapter: Interdomain
	 Federation

## Chapter: Interdomain
	 Federation

- Interdomain                              	 Federation

- Intradomain Federation

- User ID Planning                              	 for Federation

# Interdomain
                     	 Federation

Interdomain
                        		federation enables Cisco Jabber users in an enterprise domain to share
                        		availability and send instant messages with users in another domain.

Cisco Jabber
                                 			 users must manually enter contacts from another domain.

Microsoft
                                          				  Office Communications Server

Microsoft
                                          				  Lync

IBM Sametime

XMPP
                                          				  standard-based environments such as Google Talk

Expressway for Mobile and Remote Access doesn’t enable XMPP Interdomain federation itself. Cisco Jabber clients connecting
                                                      over Expressway for Mobile and Remote Access can use XMPP Interdomain federation if it has been enabled on Cisco Unified Communications
                                                      Manager IM and Presence.

AOL Instant
                                          				  Messenger

You configure
                        		interdomain federation for Cisco Jabber on  Cisco
                        		Unified Communications Manager IM and Presence Service. See the appropriate
                        		server documentation for more information.

## Intradomain Federation

Intradomain federation enables users within the same domain to share availability and send instant messages between Cisco
                              Unified Communications Manager IM and Presence Service and Microsoft Office Communications Server,  Microsoft Live Communications
                              Server, or another presence server.

Intradomain federation allows you to migrate users to Cisco Unified Communications Manager IM and Presence Service from a
                              different presence server. For this reason, you configure intradomain federation for Cisco Jabber on the presence server.
                              See the following for more information:

Cisco Unified Communications Manager IM and Presence Service: Partitioned Intradomain Federation for IM and Presence Service on Cisco Unified Communications Manager

## User ID Planning
                        	 for Federation

For federation, Cisco Jabber requires the contact ID or user ID for
                              		  each user to resolve contacts during contact searches.

Set the attribute for the user ID in the SipUri  parameter. The default value is msRTCSIP-PrimaryUserAddress . If there is a prefix to remove from your user ID you can set a value in the UriPrefix  parameter, see the latest version
                              of the Parameters Reference Guide for Cisco Jabber .

| Note | Expressway for Mobile and Remote Access doesn’t enable XMPP Interdomain federation itself. Cisco Jabber clients connecting
                                                      over Expressway for Mobile and Remote Access can use XMPP Interdomain federation if it has been enabled on Cisco Unified Communications
                                                      Manager IM and Presence. |
|---|---|