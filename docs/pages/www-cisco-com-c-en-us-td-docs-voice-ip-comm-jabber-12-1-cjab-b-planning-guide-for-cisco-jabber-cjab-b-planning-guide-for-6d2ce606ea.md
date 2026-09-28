---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-1-cjab-b-planning-guide-for-cisco-jabber-cjab-b-planning-guide-for-6d2ce606ea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_1/cjab_b_planning-guide-for-cisco-jabber/cjab_b_planning-guide-for-cisco-jabber_chapter_01001.html
retrieved_at: 2026-08-21T19:02:09.623799+00:00
---

Planning Guide for Cisco Jabber 12.1

# Planning Guide for Cisco Jabber 12.1

Updated: April 5, 2024

Chapter: Screen Share

## Chapter: Screen Share

# Screen Share

## Screen
                        	 Share

There are four types of screen share:

Cisco Webex share

BFCP share

IM Only share

Escalate to a meeting and share

### Webex Screen Share

Applies to Cisco Jabber for desktop clients in cloud deployments.

For cloud deployments, Webex Screen Share is selected automatically after choosing a contact, if BFCP and IM Only screen share options are not available.

You can start Webex Screen Share using one of the following methods:

Right-click on a contact in the hub window and choose Share screen.. from the menu options.

Select a contact in the hub window and click on the Settings menu. Choose Communicate and select Share screen... from the menu options.

When BFCP and IM Only screen share options are not available, then in a conversation window select ... > Share screen from the menu options.

### BFCP Screen
                           	 Share

Applies to Cisco Jabber desktop clients, Cisco Jabber for mobile
                                 		  clients can only receive BFCP screen shares.

Binary Floor
                                 		  Control Protocol (BFCP) screen share is controlled by Cisco Unified
                                 		  Communications Manager. Cisco Unified Communications Manager handles the BFCP
                                 		  packets that users transmit when using video desktop sharing capabilities. When
                                 		  on a call select ... > Share
                                       				screen to start a BFCP screen share.

Remote screen control is not supported with this feature.

Video desktop sharing using BFCP is not supported if Trusted Relay Point or Media Termination Point are enabled on the software phone device.

### IM Only Screen
                           	 Share

Applies to Cisco Jabber for Windows.

IM-only screen share is a one-to-one client-to-client screen share over Remote Desktop Protocol (RDP). The EnableP2PDesktopShare parameter controls whether IM-only screen shares are available. The PreferP2PDesktopShare parameter controls whether Jabber prefers video sharing or IM-only screen shares.

If your deployment allows IM-only screen share, select ... > Share screen in the chat window to start a screen share.

RDP requires port 3389 by default. IM-only screen share default port range is 49152–65535 TCP and UDP. You can use the SharePortRangeStart and SharePortRangeSize parameters to restrict the port range.

### Escalate to a
                           	 Meeting and Share

Applies to all Cisco Jabber clients.

You can escalate to an instant Webex Meetings and share your screen using the Webex Meetings controls.