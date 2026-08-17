---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-design-guide-b-12xcucdg-b-12xcucdg-chapter-010000-html-c193b413ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg/b_12xcucdg_chapter_010000.html
retrieved_at: 2026-08-17T02:34:39.480998+00:00
---

Design Guide for Cisco Unity Connection 12.x

# Design Guide for Cisco Unity Connection 12.x

Updated: August 17, 2017

Chapter: Optional Network
	 Resource Requirements

## Chapter: Optional Network
	 Resource Requirements

# Optional Network
                     	 Resource Requirements

## DHCP

Use of Dynamic Host Configuration Protocol (DHCP) is optional with Unity Connection and can be used to automatically configure
                           network settings on the Unity Connection server. If DHCP is not used, network settings such as hostname, IP address, IP mask,
                           and gateway address must be manually entered during install or configured after install using the command line interface.

## DNS

Use of DNS name resolution is optional with Unity Connection, but if available, should be used with Unity Connection. If DNS
                           name resolution is not enabled, IP addresses (not hostnames) should be used for all network devices.

## Microsoft
                        	 Exchange

For all versions of Unity Connection, when you are
                           		using Exchange 2016, Exchange 2013 or Exchange 2010 as a calendar application,
                           		you can configure Unity Connection to allow users to do several
                           		meeting-specific tasks using the phone, for example, to hear a list of the
                           		participants for a meeting, send a message to the meeting organizer, or send a
                           		message to the meeting participants. Meeting organizers can also cancel a
                           		meeting. In addition, if users are using Microsoft Outlook, they can hear a
                           		list of upcoming meetings, and accept or decline meeting invitations.

Unity Connection also enables users to import Exchange contacts
                           		using the Messaging Assistant web tool. The contact information can then be
                           		used in rules that users create in the Cisco Unity Connection Personal Call
                           		Transfer Rules web tool and when users place outgoing calls using voice
                           		commands.

Unity Connection can play Exchange email over the phone using
                           		Text to Speech.

You can also synchronize Unity Connection and Exchange mailboxes
                           		so that Unity Connection voice messages appear in the Outlook inbox. This
                           		feature is commonly known as single inbox.

For more information on supported versions of Microsoft Exchange
                           		for accessing calendar information, importing personal contacts, accessing
                           		email, and configuring mailbox synchronization, see the “ Requirements for using Unified
                              		  Messaging Features ” section of the System Requirements Guide for
                           		Cisco Unity Connection Release 12.x ,
                           		available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

Also see the “ Configuring Unified
                              		  Messaging ” chapter of the Unified Messaging Guide for Cisco Unity
                           		Connection, Release 12.x , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/unified_messaging/b_12xcucumgx.html .

## LDAP
                        	 Directory

Unity Connection can optionally use an LDAP directory
                           		(for example, Microsoft Active Directory) for LDAP directory synchronization
                           		and authentication. For more information on supported LDAP directories, see the
                           		“ Requirement for an LDAP
                              		  Directory Integration ” section of the System Requirements for
                           		Cisco Unity Connection Release 12.x ,
                           		available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html

See the LDAP Directory Integration with Cisco Unity Connection chapter for design considerations when integrating Unity Connection with an
                           		LDAP directory.

For LDAP directory to work smoothly with Unity Connection in WAN
                           		environment you need to take care of following:

Latency should not exceed 80 ms round-trip

Access Control lists for corresponding ports and IPs shall be
                                 			 provisioned on the network devices.