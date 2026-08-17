---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-administration-guide-b-15cucsag-b-15cucsag-chapter-0100-html-af9aead958
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag/b_15cucsag_chapter_0100.html
retrieved_at: 2026-08-17T02:19:17.550269+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 12, 2025

Chapter: Contacts

## Chapter: Contacts

# Contacts

## Introduction

Cisco Unity Connection provides a set of tools for
                           		administering, monitoring, and troubleshooting the system. The tools that
                           		enable the system administrators to provision the Unity Connection server and
                           		provide feature rich services, such as integrated voice messaging and audio
                           		text application for enterprise level businesses.

## Types of
                        	 Contacts

Unity Connection supports the following types of contacts:

Administrator defined contacts: Administrator defined contacts
                                 			 are the contacts are available to all users. These contacts can be configured
                                 			 for agents, staff vendors, or contractors that have an external phone number
                                 			 and need to be reachable from the voice messaging system.

Administrator-defined contacts can be configured for VPIM messaging. These contacts represent users on other VPIM-compatible
                           voice messaging systems. When contacts have been set up to represent the VPIM users, Unity Connection users can send and receive
                           messages to and from the VPIM users on the other voice messaging systems. For more information on VPIM network, see the “ Creating VPIM Contacts ” section of the “VPIM Networking” chapter of the Networking Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

User defined contacts: User defined contacts are created by the
                                 			 individual users and are only accessible to the users who create them. You can
                                 			 create such contacts through Cisco Personal Communications Assistant. You can
                                 			 also add such contacts to their personal call routing rules, caller groups, and
                                 			 can also use voice commands to call other contacts.

For more information on how a user can maintain contacts, see the “ Managing Your Contacts ” chapter of User Guide for the Cisco Unity Connection Messaging Assistant Web Tool Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/assistant/b_15cucugasst.html .

## Contact Templates

Contacts are based on contact templates. Contact Template settings apply to all newly created contacts and any change in the
                           template thereafter is not reflected in any existing contact.

Unity Connection includes one predefined contact template that you can edit. You can also create new templates based on your
                           requirements. If Unity Connection has more than one partition defined or is configured for VPIM networking, you may want to
                           create a contact template for each partition or for each VPIM location.

### Configuring
                           	 Contact Templates

Step 1

In Cisco Unity Connection Administration, expand Templates and
                                          			 select Contact Templates.

The Search Contact Templates page appears displaying the
                                             				currently configured contact templates.

Step 2

Configure
                                          			 contact templates (For more information on each field, see Help> This Page):

To add a contact template:

On the Search Contact Templates page, select Add New.

On the New Contact Template page, enter the values of the
                                                   					 required fields and select Save.

On the Edit Contact Template Basics page, enter the values of
                                                   					 the required fields and select Save.

To edit an existing contact template:

On the Search Contact Templates page, select the contact
                                                   					 template that you want to edit.

On the Edit Contact Template Basics page, enter the values of
                                                   					 the required fields and select Save.

To delete one or more contact templates:

On the Search Contact Templates page, check the check boxes to
                                                   					 select the contact templates that you want to delete.

Select Delete Selected and OK to confirm deletion.

## Configuring
                        	 Contacts

You can configure contacts using either of the following
                           		methods:

Configuring Contacts Manually: Allows to manually configure each
                                 			 contact through Search Contacts page. For information, see the Configuring Contacts Manually .

Configuring Contacts through Bulk Administration Tool (BAT):
                                 			 Allows you to configure multiple contacts using BAT at the same time. For
                                 			 information, see the Configuring Contacts through Bulk Administration Tool (BAT) .

### Configuring Contacts Manually

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Contacts and select Contacts.

The Search Contacts page appears displaying
                                             				the currently configured contacts.

Step 2

Configure contacts in Unity Connection (For more information on
                                          			 each field, see Help> This Page):

To add a contact:

On the Search Contacts page, select Add
                                                   					 New.

On the New Contact page, enter the
                                                   					 values of the required fields and select Save.

On the Edit Contact Basics page, enter
                                                   					 the values of the required fields and select Save.

To edit a contact:

On the Search Contacts page, select the
                                                   					 contact that you want to edit.

On the Edit Contacts Basics page, select
                                                   					 Edit to edit the contact settings and select Save.

To edit multiple contacts:

On the Search Contacts page, check the
                                                   					 check boxes for the contacts you want to edit and then select Bulk Edit.

On the Edit Contact Basics page, enter
                                                   					 the values of the required fields and select Submit.

You cannot edit the Alternate Names of
                                                               						multiple contacts using Bulk Edit.

To delete one or more contacts:

On the Search Contacts page, select the
                                                   					 contacts that you want to delete.

Select Delete Selected and OK to confirm
                                                   					 deletion.

### Configuring
                           	 Contacts through Bulk Administration Tool (BAT)

BAT allows you to create Cisco Unity Connection contacts from a
                              		CSV file. For information on configuring contacts and constructing CSV file,
                              		see the Bulk Administration Tool section.

## Contact Settings

Contact settings includes configuring the contacts with alternate names and providing SMTP proxy addresses. Using Alternate
                           names, contacts can be recognized using voice recognition functionality and setting up SMTP proxy address enables the IMAP
                           client users to communicate with Unity Connection contacts or VPIM contacts.

### Alternate Names

Alternate names are different versions of a name than what is listed in the corporate directory. For example, if a caller
                              asks Unity Connection to dial “Mary Jameson,” which was the maiden name of Mary Brown, Unity Connection can reference this
                              information and connect the caller to the correct user.

Alternate names can be created for VPIM contacts, administrator defined contacts, and user defined contacts.You could also
                              use alternate names to add phonetic spellings of hard to pronounce names. For example, you can	 add “Goolay” as an alternate
                              name for the last name “Goulet”.

### SMTP Proxy Addresses

Unity Connection uses SMTP proxy addresses to
                                 		  map the recipients of an incoming SMTP message sent from an IMAP client to the
                                 		  appropriate Unity Connection user or VPIM contact. If users use IMAP clients to
                                 		  send, reply to, or forward messages to VPIM contacts you should configure each
                                 		  VPIM contact with an SMTP address.

Unity Connection handles SMTP messages sent to
                                             			 the contacts that are not associated with a VPIM location according to the
                                             			 option selected for the System Settings > General Configuration > When a
                                             			 Recipient Cannot Be Found setting.

For example, when Robin Smith, whose email
                                 		  client is configured to access Unity Connection with the email address
                                 		  robin.smith@example.com, records a voice message in ViewMail for Outlook and
                                 		  sends it to chris.jones@example.com, Unity Connection searches the list of SMTP
                                 		  proxy addresses for robin.smith@example.com and chris.jones@example.com. If
                                 		  these addresses are defined as SMTP proxy addresses for the Unity Connection
                                 		  users Robin Smith and Chris Jones respectively, Unity Connection delivers the
                                 		  message as a voice message from Robin Smith to Chris Jones.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Contacts and select Contacts.

The Search Contacts page appears displaying
                                             				the currently configured contacts.

Step 2

Configure SMTP proxy addresses for contacts
                                          			 (For more information on each field, see Help> This Page):

To add SMTP proxy address for a contact:

On the Search Contact page, select the
                                       				contact that you want to edit.

On the Edit Contact Basics page, select
                                       				Edit> SMTP Proxy Address.

On the SMTP Proxy Addresses page, select Add
                                       				New.

Enter the SMTP proxy address and select
                                       				Save.

To add SMTP proxy addresses for multiple
                                       				contacts:

On the Search Contact page, select the
                                       				contacts that you want to edit and then select Bulk Edit.

On the Edit Contact Basics page, select
                                       				Edit> SMTP Proxy Address.

Enter the SMTP proxy addresses and select
                                       				Submit.

| Step 1 | In Cisco Unity Connection Administration, expand Templates and
                                          			 select Contact Templates. The Search Contact Templates page appears displaying the
                                             				currently configured contact templates. |
|---|---|
| Step 2 | Configure
                                          			 contact templates (For more information on each field, see Help> This Page): To add a contact template: On the Search Contact Templates page, select Add New. On the New Contact Template page, enter the values of the
                                                   					 required fields and select Save. On the Edit Contact Template Basics page, enter the values of
                                                   					 the required fields and select Save. To edit an existing contact template: On the Search Contact Templates page, select the contact
                                                   					 template that you want to edit. On the Edit Contact Template Basics page, enter the values of
                                                   					 the required fields and select Save. To delete one or more contact templates: On the Search Contact Templates page, check the check boxes to
                                                   					 select the contact templates that you want to delete. Select Delete Selected and OK to confirm deletion. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Contacts and select Contacts. The Search Contacts page appears displaying
                                             				the currently configured contacts. |
|---|---|
| Step 2 | Configure contacts in Unity Connection (For more information on
                                          			 each field, see Help> This Page): To add a contact: On the Search Contacts page, select Add
                                                   					 New. On the New Contact page, enter the
                                                   					 values of the required fields and select Save. On the Edit Contact Basics page, enter
                                                   					 the values of the required fields and select Save. To edit a contact: On the Search Contacts page, select the
                                                   					 contact that you want to edit. On the Edit Contacts Basics page, select
                                                   					 Edit to edit the contact settings and select Save. To edit multiple contacts: On the Search Contacts page, check the
                                                   					 check boxes for the contacts you want to edit and then select Bulk Edit. On the Edit Contact Basics page, enter
                                                   					 the values of the required fields and select Submit. Note You cannot edit the Alternate Names of
                                                               						multiple contacts using Bulk Edit. To delete one or more contacts: On the Search Contacts page, select the
                                                   					 contacts that you want to delete. Select Delete Selected and OK to confirm
                                                   					 deletion. | Note | You cannot edit the Alternate Names of
                                                               						multiple contacts using Bulk Edit. |
| Note | You cannot edit the Alternate Names of
                                                               						multiple contacts using Bulk Edit. |

| Note | You cannot edit the Alternate Names of
                                                               						multiple contacts using Bulk Edit. |
|---|---|

| Note | Unity Connection handles SMTP messages sent to
                                             			 the contacts that are not associated with a VPIM location according to the
                                             			 option selected for the System Settings > General Configuration > When a
                                             			 Recipient Cannot Be Found setting. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Contacts and select Contacts. The Search Contacts page appears displaying
                                             				the currently configured contacts. |
|---|---|
| Step 2 | Configure SMTP proxy addresses for contacts
                                          			 (For more information on each field, see Help> This Page): |