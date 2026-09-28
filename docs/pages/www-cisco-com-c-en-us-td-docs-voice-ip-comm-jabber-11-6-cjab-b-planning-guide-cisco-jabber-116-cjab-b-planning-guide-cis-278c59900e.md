---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-6-cjab-b-planning-guide-cisco-jabber-116-cjab-b-planning-guide-cis-278c59900e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_01000.html
retrieved_at: 2026-08-25T21:47:44.334133+00:00
---

Planning Guide for Cisco Jabber 11.6

# Planning Guide for Cisco Jabber 11.6

Updated: April 20, 2016

Chapter: Screen Share

## Chapter: Screen Share

# Screen Share

## Screen
                        	 Share

Cisco WebEx share

BFCP share

IM Only share

Escalate to a meeting and share

### Cisco Webex Screen Share

Applies to Cisco Jabber for desktop clients in cloud deployments.

For cloud deployments, Cisco Webex Screen Share is selected automatically after choosing a contact, if BFCP and IM Only screen share options are not available.

You can start Cisco Webex Screen Share using one of the following methods:

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

### IM Only Screen
                           	 Share

Applies to Cisco Jabber for Windows.

IM Only screen
                                 		  share is a one to one screen share and is enabled using the
                                 		  EnableP2PDesktopShare parameter in the jabber-config.xml file. In a chat window
                                 		  users select ... > Share
                                       				screen .

The port range for
                                 		  this option is 49152 to 65535 and this can be reduced by using the SharePortRangeStart and SharePortRangeSize parameters in the jabber-config.xml
                                 		  file.

### Escalate to a
                           	 Meeting and Share

Applies to all Cisco Jabber clients.

You can escalate to an instant Cisco Webex Meetings and share your screen using the Cisco Webex Meetings controls.