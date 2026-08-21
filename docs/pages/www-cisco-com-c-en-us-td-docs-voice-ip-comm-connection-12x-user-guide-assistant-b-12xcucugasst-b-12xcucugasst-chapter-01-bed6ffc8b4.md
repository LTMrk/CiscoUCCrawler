---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-user-guide-assistant-b-12xcucugasst-b-12xcucugasst-chapter-01-bed6ffc8b4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/assistant/b_12xcucugasst/b_12xcucugasst_chapter_01001.html
retrieved_at: 2026-08-21T00:25:02.098753+00:00
---

User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x)

# User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x)

Updated: August 9, 2017

Chapter: Managing Your Contacts

## Chapter: Managing Your Contacts

# Managing Your Contacts

## About Your Contacts

Cisco Unity Connection uses the information in your contacts list to forward your incoming calls and to help you place outgoing
                           calls. Connection also uses your contacts to identify the people who call you.

Your contact information supplements the information in the Cisco Unity Connection directory. The Connection directory is
                           internal to your organization and maintained by your system administrator, while contacts are set up and maintained by you.

You can use your contacts to store names and numbers for people who are not included in the Connection directory, including
                           customers, suppliers, family members, and friends.

You manage contacts in the Messaging Assistant web tool. You can add Connection users to your contacts; however, the entries
                           are not automatically updated and maintained by the system. For example, if a co-worker who is listed leaves the company,
                           you will need to manually delete the entry from your contacts.

If you use voice commands to place calls, consider the following advantages to adding other Connection users to your contacts:

Using alternate names—Alternate names can improve accuracy when you use voice commands to dial co-workers. Add nickname entries
                                 or other alternate-name entries to your contacts list for those people in the Connection directory to whom you regularly place
                                 calls or whose names you find difficult to pronounce.

Using external numbers—If you regularly call co-workers on their personal mobile phones, add their Connection directory information
                                 to your contact entries along with their mobile phone number so that you can use voice commands to reach them quickly.

(Note that to place calls by using voice commands, you must be signed in to Connection.)

## Adding Contacts

Use the Dialed Work Phone, Dialed Home Phone, and Dialed Mobile Phone fields when you want to be able to call contacts by
                                             using voice commands.

For dialed phone numbers, include any additional numbers necessary to dial outside calls (for example 9) and for long-distance
                                             dialing (for example, 1).

Email addresses are for your information only; Connection does not use the email addresses in contact entries.

You can import Microsoft Exchange contacts into your Connection contacts. See Importing Exchange Contact Information into Your Contacts .

In the Messaging Assistant, from the Contacts menu, select New Contact . (Alternatively, from the View Contacts page, you can select the New Contact icon below the menu bar.)

On the Create Contact page, enter the first and last names.

If you enter the names by using non-Roman alphabet characters (for example, Kanji characters for a Japanese contact), also
                                       enter the names by using the Roman alphabet in the Alternate Spelling of First Name and Alternate Spelling of Last Name fields

You can use the characters A-Z, a-z, and 0-9. Entering this alternate spelling enables Connection to identify the names if
                                          you call the contact by using voice commands.

If you use voice commands and the contact is known by any alternate names (for example, a maiden name or a nickname), enter
                                       the name(s) in the Alternate Names section.

To add another alternate name for the contact, select Add Row , and enter the name(s).

Repeat Step 5 to add any additional alternate names for the contact.

Optionally, in the Email field, enter the email address of the contact. (Email addresses are for your information only.)

If you use voice commands to call contacts, in the Phone Numbers to Call Contact By Using Voice Commands section, enter the
                                       work, home, or mobile phone number that Connection dials for the contact.

When entering dialed phone numbers, if the phone number is an internal number, enter the extension for the contact. For external
                                          numbers, enter the phone number beginning with any access code needed to make an outside call (for example, 9). You can enter
                                          digits 0 through 9. Do not use spaces, dashes, or parentheses between digits. For long-distance numbers, also include the
                                          applicable dialing codes (for example, 1 and the area code). You can also enter:

, (comma) to insert a one-second pause.

# and * to correspond to the # and * keys on the phone.

If you use personal call transfer rules to manage calls from contacts, in the Phone Numbers to Identify Contact for Personal
                                       Call Transfer Rules section, enter a work, home, and mobile phone number for the contact.

When entering numbers to be used by personal call transfer rules, enter the number as it appears on a caller ID display. Connection
                                          can identify the call as being from the contact only when the phone number of an incoming call matches exactly what you enter
                                          in the field.

Select Save . The entry is added to your contacts.

## Changing Information for Contacts

Do the procedure in this section when you want to change the name or phone number for a contact, or to assign an alternate
                              name.

In the Messaging Assistant, from the Contacts menu, select View Contacts .

On the Contacts page, select the first name of the contact whose information you want to change.

In the Alternate Spelling of First Name and Alternate Spelling of Last Name fields, change the alternate spellings of your contact’s name, as applicable.

If you use non-Roman alphabet characters in the First Name and Last Name fields, using the Roman alphabet for the alternate
                                          spellings enables Connection to identify the names if you call the contact by using voice commands. You can use the characters
                                          A-Z, a-z, and 0-9.

In the Alternate Names section, change the information as applicable:

To delete an alternate name, check the check box next to the name, and select Delete Selected .

To add an alternate name, select Add Row and enter the name(s).

Optionally, in the Email field, change the email address of the contact, as applicable. (Email addresses are for your information only.)

In the Phone Numbers to Call Contact By Using Voice Commands section, change the work, home, or mobile phone number that Connection
                                       dials for the contact, as applicable.

When entering dialed phone numbers, if the phone number is an internal number, enter the extension for the contact. For external
                                          numbers, enter the phone number beginning with any access code needed to make an outside call (for example, 9). You can enter
                                          digits 0 through 9. Do not use spaces, dashes, or parentheses between digits. For long-distance numbers, also include the
                                          applicable dialing codes (for example, 1 and the area code). You can also enter:

, (comma) to insert a one-second pause.

# and * to correspond to the # and * keys on the phone.

In the Phone Numbers to Identify Contact for Personal Call Transfer Rules section, change the work, home, or mobile phone
                                       number for the contact, as applicable.

When entering numbers to be used by personal call transfer rules, enter the number as it appears on a caller ID display. Connection
                                          can identify the call as being from the contact only when the phone number of an incoming call matches exactly what you enter
                                          in the field.

In the Caller Group Membership section, change the information as applicable:

To remove the contact from a caller group, uncheck the check box next to the group name.

To add the contact to a caller group, check the check box next to the group name.

If you have no caller groups set up, the Caller Group Membership section is not displayed. (You create caller groups in the
                                                            Personal Call Transfer Rules web tool.)

Select Save .

## Deleting Contacts

In the Messaging Assistant, from the Contacts menu, select View Contacts .

On the Contacts page, check the check box next to the contact name. You can check multiple check boxes to delete more than
                                       one contact at a time.

Contacts cannot be deleted if they are part of a caller group or a personal call transfer rule; you must remove the contact
                                                      from the caller group or rule first before deleting the contact entry.  (You create rules in the Personal Call Transfer Rules
                                                      web tool.)

Select the Delete Selected Rows icon below the menu bar.

## Importing Exchange Contact Information into Your Contacts

You can save time entering information in your contacts by importing entries from your Microsoft Exchange Contacts folder.
                              This is also a good method for ensuring that your contacts information is current.

Cisco Unity Connection imports only the names, phone numbers, and email addresses of the contacts stored on the Exchange server.
                              During the import process, Connection does the following:

Displays the number of contacts in your contacts before the import.

Imports new Exchange contact information into your contacts.

Updates any Exchange contact information that may have changed since the last import.

Removes entries from your contacts that have been deleted in Exchange since the last import.

Note that Connection does not distinguish duplicate entries or enter phone number information in the Dialed Phone fields.
                              After the import is complete, you may want to review your contacts to remove duplicate entries or to add dialed phone numbers
                              for use if you call contacts by using voice commands.

In the Messaging Assistant, from the Contacts menu, select Import Contacts .

On the Import Contacts from Exchange page, select Import Contacts .

Connection imports the entries from your Exchange Contacts folder, and displays the results of the import.

| Phone numbers to call contact by using voice commands | Use the Dialed Work Phone, Dialed Home Phone, and Dialed Mobile Phone fields when you want to be able to call contacts by
                                             using voice commands. For dialed phone numbers, include any additional numbers necessary to dial outside calls (for example 9) and for long-distance
                                             dialing (for example, 1). |
|---|---|
| Phone numbers to identify contact for personal call transfer rules | Use the Work Phone, Home Phone, and Mobile Phone fields to enter phone numbers that Connection uses when matching your personal
                                          call transfer rules against incoming phone calls from contacts. (For example, if you want to create a personal call transfer
                                          rule based on the home phone number for your mother, enter the number in the Home Phone field.) |

| Tip | You can import Microsoft Exchange contacts into your Connection contacts. See Importing Exchange Contact Information into Your Contacts . |
|---|---|

| Step 1 | In the Messaging Assistant, from the Contacts menu, select New Contact . (Alternatively, from the View Contacts page, you can select the New Contact icon below the menu bar.) |
|---|---|
| Step 2 | On the Create Contact page, enter the first and last names. |
| Step 3 | If you enter the names by using non-Roman alphabet characters (for example, Kanji characters for a Japanese contact), also
                                       enter the names by using the Roman alphabet in the Alternate Spelling of First Name and Alternate Spelling of Last Name fields You can use the characters A-Z, a-z, and 0-9. Entering this alternate spelling enables Connection to identify the names if
                                          you call the contact by using voice commands. |
| Step 4 | If you use voice commands and the contact is known by any alternate names (for example, a maiden name or a nickname), enter
                                       the name(s) in the Alternate Names section. |
| Step 5 | To add another alternate name for the contact, select Add Row , and enter the name(s). |
| Step 6 | Repeat Step 5 to add any additional alternate names for the contact. |
| Step 7 | Optionally, in the Email field, enter the email address of the contact. (Email addresses are for your information only.) |
| Step 8 | If you use voice commands to call contacts, in the Phone Numbers to Call Contact By Using Voice Commands section, enter the
                                       work, home, or mobile phone number that Connection dials for the contact. When entering dialed phone numbers, if the phone number is an internal number, enter the extension for the contact. For external
                                          numbers, enter the phone number beginning with any access code needed to make an outside call (for example, 9). You can enter
                                          digits 0 through 9. Do not use spaces, dashes, or parentheses between digits. For long-distance numbers, also include the
                                          applicable dialing codes (for example, 1 and the area code). You can also enter: , (comma) to insert a one-second pause. # and * to correspond to the # and * keys on the phone. |
| Step 9 | If you use personal call transfer rules to manage calls from contacts, in the Phone Numbers to Identify Contact for Personal
                                       Call Transfer Rules section, enter a work, home, and mobile phone number for the contact. When entering numbers to be used by personal call transfer rules, enter the number as it appears on a caller ID display. Connection
                                          can identify the call as being from the contact only when the phone number of an incoming call matches exactly what you enter
                                          in the field. |
| Step 10 | Select Save . The entry is added to your contacts. |

| Step 1 | In the Messaging Assistant, from the Contacts menu, select View Contacts . |
|---|---|
| Step 2 | On the Contacts page, select the first name of the contact whose information you want to change. |
| Step 3 | In the Alternate Spelling of First Name and Alternate Spelling of Last Name fields, change the alternate spellings of your contact’s name, as applicable. If you use non-Roman alphabet characters in the First Name and Last Name fields, using the Roman alphabet for the alternate
                                          spellings enables Connection to identify the names if you call the contact by using voice commands. You can use the characters
                                          A-Z, a-z, and 0-9. |
| Step 4 | In the Alternate Names section, change the information as applicable: To delete an alternate name, check the check box next to the name, and select Delete Selected . To add an alternate name, select Add Row and enter the name(s). |
| Step 5 | Optionally, in the Email field, change the email address of the contact, as applicable. (Email addresses are for your information only.) |
| Step 6 | In the Phone Numbers to Call Contact By Using Voice Commands section, change the work, home, or mobile phone number that Connection
                                       dials for the contact, as applicable. When entering dialed phone numbers, if the phone number is an internal number, enter the extension for the contact. For external
                                          numbers, enter the phone number beginning with any access code needed to make an outside call (for example, 9). You can enter
                                          digits 0 through 9. Do not use spaces, dashes, or parentheses between digits. For long-distance numbers, also include the
                                          applicable dialing codes (for example, 1 and the area code). You can also enter: , (comma) to insert a one-second pause. # and * to correspond to the # and * keys on the phone. |
| Step 7 | In the Phone Numbers to Identify Contact for Personal Call Transfer Rules section, change the work, home, or mobile phone
                                       number for the contact, as applicable. When entering numbers to be used by personal call transfer rules, enter the number as it appears on a caller ID display. Connection
                                          can identify the call as being from the contact only when the phone number of an incoming call matches exactly what you enter
                                          in the field. |
| Step 8 | In the Caller Group Membership section, change the information as applicable: To remove the contact from a caller group, uncheck the check box next to the group name. To add the contact to a caller group, check the check box next to the group name. Note If you have no caller groups set up, the Caller Group Membership section is not displayed. (You create caller groups in the
                                                            Personal Call Transfer Rules web tool.) | Note | If you have no caller groups set up, the Caller Group Membership section is not displayed. (You create caller groups in the
                                                            Personal Call Transfer Rules web tool.) |
| Note | If you have no caller groups set up, the Caller Group Membership section is not displayed. (You create caller groups in the
                                                            Personal Call Transfer Rules web tool.) |
| Step 9 | Select Save . |

| Note | If you have no caller groups set up, the Caller Group Membership section is not displayed. (You create caller groups in the
                                                            Personal Call Transfer Rules web tool.) |
|---|---|

| Step 1 | In the Messaging Assistant, from the Contacts menu, select View Contacts . |
|---|---|
| Step 2 | On the Contacts page, check the check box next to the contact name. You can check multiple check boxes to delete more than
                                       one contact at a time. Note Contacts cannot be deleted if they are part of a caller group or a personal call transfer rule; you must remove the contact
                                                      from the caller group or rule first before deleting the contact entry.  (You create rules in the Personal Call Transfer Rules
                                                      web tool.) | Note | Contacts cannot be deleted if they are part of a caller group or a personal call transfer rule; you must remove the contact
                                                      from the caller group or rule first before deleting the contact entry.  (You create rules in the Personal Call Transfer Rules
                                                      web tool.) |
| Note | Contacts cannot be deleted if they are part of a caller group or a personal call transfer rule; you must remove the contact
                                                      from the caller group or rule first before deleting the contact entry.  (You create rules in the Personal Call Transfer Rules
                                                      web tool.) |
| Step 3 | Select the Delete Selected Rows icon below the menu bar. |

| Note | Contacts cannot be deleted if they are part of a caller group or a personal call transfer rule; you must remove the contact
                                                      from the caller group or rule first before deleting the contact entry.  (You create rules in the Personal Call Transfer Rules
                                                      web tool.) |
|---|---|

| Step 1 | In the Messaging Assistant, from the Contacts menu, select Import Contacts . |
|---|---|
| Step 2 | On the Import Contacts from Exchange page, select Import Contacts . |
| Step 3 | Connection imports the entries from your Exchange Contacts folder, and displays the results of the import. |