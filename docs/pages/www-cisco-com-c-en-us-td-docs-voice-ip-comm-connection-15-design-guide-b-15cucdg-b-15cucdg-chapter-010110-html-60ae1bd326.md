---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-guide-b-15cucdg-b-15cucdg-chapter-010110-html-60ae1bd326
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg/b_15cucdg_chapter_010110.html
retrieved_at: 2026-08-17T02:15:22.472521+00:00
---

Design Guide for Cisco Unity Connection 15

# Design Guide for Cisco Unity Connection 15

Updated: August 12, 2025

Chapter: Migrating to
	 Cisco Unity Connection from Another Voice-Messaging System

## Chapter: Migrating to
	 Cisco Unity Connection from Another Voice-Messaging System

- Migrating to                              	 Cisco Unity Connection from Another Voice-Messaging System

- Migrating to Cisco Unity Connection from Another Voice-Messaging System

# Migrating to
                     	 Cisco Unity Connection from Another Voice-Messaging System

## Migrating to Cisco Unity Connection from Another Voice-Messaging System

When the customer is replacing another voice messaging system with Unity Connection, consider the following issues:

How do users interact with each system? For example, the options offered by the Unity Connection standard conversation (the
                                 telephone user interface, or TUI) and the key presses used to accomplish tasks may be different from what users are accustomed
                                 to using. As an alternative to the standard conversation, some customers may want to activate Optional Conversation 1 (the
                                 ARIA-like conversation available in Unity Connection) so that users hear message-retrieval menus that more closely resemble
                                 the choices they are familiar with. However, other menus—those that outside callers and Unity Connection users use to send
                                 and manage messages, as well as the menus that users use to change their Unity Connection settings—are the same as those in
                                 the standard conversation.

Ensure that the customer understands the Unity Connection behaviors that are different from those of the voice messaging system
                                 it is replacing. For example, if the customer does not currently use an automated attendant feature and wants Unity Connection
                                 to be configured the same way, this should be noted so that the installer configures Unity Connection correctly. If it is
                                 necessary to make changes, for example to change the behavior of the opening greeting, or to zero out to an operator option
                                 during a personal greeting, these changes should be made and tested prior to the day of the cutover.

Plan a method for creating Unity Connection users. If they be imported from an LDAP directory, imported from Cisco Unified
                                 Communications Manager, imported from a CSV file, or added using Cisco Unity Connection Administration? If they are imported
                                 from a CSV file or added using Unity Connection Administration, where does the information come from? Creating user accounts
                                 requires planning and testing prior to the cutover.

The larger the installation or number of servers, the greater the need to perform user enrollment tasks prior to the day of
                                 the cutover. If too many users try to enroll simultaneously, some users (up to the number of voice ports available) succeed
                                 in accessing the Unity Connection server and enrolling, but the rest get a busy signal.

If the customer has special audio-text applications set up in the existing voice messaging system, Unity Connection equivalents
                                    should be planned and set up before cutover. Unity Connection supports audio-text applications and provides tools for designing
                                    and configuring them.

Unity Connection does not support group mailboxes, but the same functionality can be made available by setting up a call handler
                                    whose greeting prompts the caller to “press 1 for Pat, press 2 for Chris,” and so on. Dispatch messages may also provide the
                                    necessary functionality needed to support group mailboxes. (For more information about dispatch messaging, see the “ Dispatch Messages ” section of the “Messaging” chapter in the System Administration Guide for Cisco Unity Connection Release 15 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

When the Unity Connection design is finalized and verified through lab qualification, Unity Connection functionality should
                                    also be tested before cutover running a simulated load test and by running application test plans.