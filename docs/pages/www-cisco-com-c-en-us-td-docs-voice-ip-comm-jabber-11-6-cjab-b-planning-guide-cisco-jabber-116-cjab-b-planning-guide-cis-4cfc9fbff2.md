---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-6-cjab-b-planning-guide-cisco-jabber-116-cjab-b-planning-guide-cis-4cfc9fbff2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_01001.html
retrieved_at: 2026-08-25T21:47:48.114694+00:00
---

Planning Guide for Cisco Jabber 11.6

# Planning Guide for Cisco Jabber 11.6

Updated: April 20, 2016

Chapter: Federation

## Chapter: Federation

# Federation

## Interdomain
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

Cisco Unified Communications Manager IM and Presence Service: Partitioned Intradomain Federation for IM and Presence Service on Cisco Unified Communications Manager

## User ID Planning
                        	 for Federation

For federation, Cisco Jabber requires the contact ID or user ID for
                              		  each user to resolve contacts during contact searches.

In the jabber-config.xml file you set the attribute for the user ID in the SipUri BDISipUri parameter. The default value is msRTCSIP-PrimaryUserAddress . If there is a prefix to remove from your user ID you can set a value in the UriPrefix BDIUriPrefix parameter.

| Note | Expressway for Mobile and Remote Access doesn’t enable XMPP Interdomain federation itself. Cisco Jabber clients connecting
                                                         over Expressway for Mobile and Remote Access can use XMPP Interdomain federation if it has been enabled on Cisco Unified Communications
                                                         Manager IM and Presence. |
|---|---|