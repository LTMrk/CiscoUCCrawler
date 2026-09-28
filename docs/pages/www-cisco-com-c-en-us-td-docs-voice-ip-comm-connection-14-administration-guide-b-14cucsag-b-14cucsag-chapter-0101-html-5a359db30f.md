---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-administration-guide-b-14cucsag-b-14cucsag-chapter-0101-html-5a359db30f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag/b_14cucsag_chapter_0101.html
retrieved_at: 2026-08-17T02:25:59.247737+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 18, 2025

Chapter: System Distribution List

## Chapter: System Distribution List

# System Distribution List

## Introduction

System distribution lists enables the users to send or forward voice messages to a group of Cisco Unity Connection users for
                           example, employees of a team who need the same information on a regular basis can be members of a system distribution list.

Distribution List can include users, user templates, contacts, contact templates and distribution lists as members of another
                           distribution list.

Consider an organization with three departments; sales, marketing and admin. Each departments have individual distribution
                           lists, as Sales DL, Marketing DL, and Admin DL. Also, an organization level distribution list, Company DL has been created.
                           Sales DL, Marketing DL, and Admin DL are the members of Company DL.

To send a message to all the members of sales team, an authorized user forwards a voice message to Sales DL. In order to send
                           a message to all the employees of an organization, a user can either send the message to all three distribution lists or to
                           the Company DL.

## Default System
                        	 Distribution Lists

You can create your own system distribution lists from the
                              		  default ones included in Unity Connection.

Default System Distribution Lists in Unity Connection

Undeliverable Messages

Users that are the members of the Undeliverable Messages list
                                          						receive either of the following:

Messages left by outside
                                                							 callers for recipients with mailboxes that cannot be located or have deleted,
                                                							 or

Non-delivery receipts
                                                							 (NDRs) that cannot be delivered to the original sender of a message.

By default, the UndeliverableMessagesMailbox user is the only
                                          						member of the Undeliverable Messages distribution list. You should add a user
                                          						to the list to monitor and re-route any messages, if required.

All Voice Mail Users

All the users with mailboxes and the user templates assigned to
                                          						the voicemail users are automatically added to the All Voicemail Users list.
                                          						When the voicemail users or voicemail user templates are deleted, they are
                                          						automatically removed from this list.

The default users, such as operator and messaging system are not
                                                      						  the members of this list.

All Voicemail Enabled Contacts

By default, the All Voicemail-Enabled Contacts list has no
                                          						members. You can add all the VPIM contacts as members of this list to address
                                          						messages to all the users of the entire group. You can also add contact
                                          						templates that are used to create VPIM contacts to this list. Adding contact
                                          						templates ensure that the VPIM contacts further created are automatically added
                                          						as members of this list.

For information on VPIM, see the Networking chapter.

## Configuring System
                        	 Distribution Lists

This section includes information on creating a system
                              		  distribution list in Unity Connection, defining the settings for the system
                              		  distribution list, and adding alternate names of the distribution lists.

You can also specify alternate names for the distribution lists
                              		  if you want to use the voice recognition feature. The users say the display
                              		  name using voice commands to address a message to the distribution list over
                              		  the phone. For example, the distribution list name for the Technical Support
                              		  department is IT. You would add the pronunciation spelling “Eye Tea” as an
                              		  alternate name. You can also add “Help Desk” as an alternate name.

You can manage the distribution lists using the Bulk
                                          			 Administration Tool. For more information, see the Bulk Administration Tool section.

Tip

The Distribution List Builder tool can be used to
                                          			 add multiple users to a new or existing system distribution list based on a
                                          			 number of search criteria or by importing from a comma-separated value (CSV)
                                          			 file. Download the latest version, and view training videos and Help at http://www.ciscounitytools.com/Applications/CxN/PublicDistributionListBuilder/PublicDistributionListBuilder.html .

Step 1

In Cisco Unity Connection Administration, expand Distribution Lists and select System Distribution Lists .

The Search Distribution Lists page appears displaying the
                                          				currently configured distribution lists.

Step 2

Configure system distribution list (For more information on each
                                       			 field, see Help> This Page):

To add a new distribution list, do the following steps:

On the Search Distribution Lists page, select Add New .

On the New Distribution List page, enter the values of the
                                    				required fields and select Save .

On the Edit Distribution List Basics page, select Edit>
                                    				Alternate Name.

On the Edit Alternate Names page, add a new alternate name in
                                    				the Display Name field and select Add New . When you have finished adding new alternate names,
                                    				select Save .

To edit an existing distribution list, do the following steps:

On the Search Distribution Lists page, select the distribution
                                    				list that you want to edit.

On the Edit Distribution List Basics page, change the values of
                                    				the required fields and select Save.

On the Edit Distribution List Basics page, select Edit>
                                    				Alternate Name.

On the Edit Alternate Names page, change the display name and
                                    				select Save.

To edit more than one distribution lists, do the following
                                    				steps:

On the Search Distribution Lists page, check the check boxes for
                                    				the distribution lists that you want to edit and select Bulk Edit.

On the Edit Distribution List Basics page, change the values of
                                    				the required fields and select Save.

To delete one or more distribution lists, do the following
                                    				steps:

On the Search Distribution Lists page, check the check boxes for
                                    				the distribution lists that you want to delete and select Delete Selected.

Select OK to confirm deletion.

## Adding or Removing Distribution List Members

You can add users, user templates, and other
                              		  distribution lists as members of a distribution list. You can also add contacts
                              		  and contact templates to the All Voicemail-Enabled Contacts distribution list.

When you delete any of the
                              		  components, such as user or user template, Unity Connection automatically
                              		  removes it from the associated distribution list.

Step 1

In Cisco Unity Connection Administration,
                                       			 expand Distribution Lists and
                                       			 select System Distribution
                                          				Lists .

The Search Distribution Lists page appears
                                          				displaying the currently configured distribution lists.

Step 2

On the Search Distribution Lists page,
                                       			 select the distribution list to which you want to add or remove the
                                       			 distribution list members.

Step 3

On the Edit Distribution List Basics page,
                                       			 select Edit> Distribution List Members.

Step 4

Add or remove the distribution list members
                                       			 (For more information on each field, see Help> This Page):

To add a distribution list member, select
                                    				either of the following:

Add User

Add User Template

Add Distribution List

Add Contact (All Voicemail-Enabled
                                          					 Contacts list only)

Add Contact Template (All
                                          					 Voicemail-Enabled Contacts list only)

Check the check boxes of the components that
                                    				you want to add as distribution list members and select Add Selected.

To remove one or more distribution list
                                    				members from the list, on the Distribution List Members page, check the check
                                    				boxes to select the components that you want to remove from the list and then
                                    				select Remove Selected .

## Using Advanced
                        	 Settings to Enable System Distribution List Access Lists

To control which users have access to a distribution list you
                           		can also create partitions and search spaces to manage the users that can send
                           		messages to a system distribution list. However, when you have a large number
                           		of lists, the search space approach may not scale well and you may reach the
                           		limit on the number of partitions and search spaces that you can create on the
                           		server. As an alternative approach, you can configure advanced settings that
                           		allow you to set up individual access lists for each system distribution list
                           		that you want to manage.

A system distribution access list specifies the particular users
                           		who can send messages to a distribution list.

If you want to set up an access list for a distribution list
                           		with alias allvoicemailusers you enable and create a system distribution access
                           		list with the same alias and a suffix you specified like
                           		“allvoicemailusers-accesslist”. The second distribution list is created with
                           		the alias allvoicemailusers-accesslist. You can add the users or contacts, who
                           		need to be able to send messages to allvoicemailusers distribution list, as
                           		members of the access list.

Only a Unity Connection user can be added as a member of system
                                       		  distribution list access list.

Do the following tasks to set up system distribution list access
                           		lists:

Configure the advanced settings that enable and control the
                                 			 access lists by performing the steps in the Enable and Configure System Distribution List Access List section. If you are using digital networking to connect multiple Unity
                                 			 Connection servers, you need to enable and configure distribution list access
                                 			 list on all of the servers.

In a digital network, the values for the advanced settings that
                                 			 enable and control access lists must be configured identically on each location
                                 			 in the network in order for access lists to function properly.

For each system distribution list that you want to control with
                                 			 an access list, create a new system distribution list. With an alias consisting
                                 			 the alias of original list plus a suffix defined in the System Distribution
                                 			 List Alias Suffix for Access Lists field. For more information, see the Configuring System Distribution Lists section.

### Enable and Configure System Distribution List Access List

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select Messaging .

Step 2

Check the Use Access Lists to Control Who Can
                                             				Send to System Distribution Lists check box.

Step 3

Check the Allow Delivery of Messages to System
                                             				Distribution Lists That Have No Access Lis t check box.

Uncheck this check box to reject all
                                                         				  messages sent to system distribution lists that do not have an access list, and
                                                         				  send a Non-Delivery Receipt (NDR) to the message sender.

Step 4

Specify the suffix that is used to
                                          			 distinguish access lists in the System Distribution List Alias
                                             				Suffix for Access Lists field and select Save .

## Enabling Users to Send Messages to a System Distribution List

The users must be configured to send messages to
                              		  a distribution list. The default settings in class of service allow the user to
                              		  send messages to distribution lists.

Step 1

In Cisco Unity Connection Administration,
                                       			 expand Class of Service and select Class of Service.

The Search Class of Service page appears
                                          				displaying the currently configured classes of services.

Step 2

On the Search Class of Service page, select
                                       			 the class of service applied to the voicemail users.

Step 3

On the Edit Class of Service page, in the
                                       			 Message Options section, check the Allow Users to Send Messages to System
                                       			 Distribution Lists check box and select Save.

| Undeliverable Messages | Users that are the members of the Undeliverable Messages list
                                          						receive either of the following: Messages left by outside
                                                							 callers for recipients with mailboxes that cannot be located or have deleted,
                                                							 or Non-delivery receipts
                                                							 (NDRs) that cannot be delivered to the original sender of a message. By default, the UndeliverableMessagesMailbox user is the only
                                          						member of the Undeliverable Messages distribution list. You should add a user
                                          						to the list to monitor and re-route any messages, if required. |
|---|---|
| All Voice Mail Users | All the users with mailboxes and the user templates assigned to
                                          						the voicemail users are automatically added to the All Voicemail Users list.
                                          						When the voicemail users or voicemail user templates are deleted, they are
                                          						automatically removed from this list. Note The default users, such as operator and messaging system are not
                                                      						  the members of this list. | Note | The default users, such as operator and messaging system are not
                                                      						  the members of this list. |
| Note | The default users, such as operator and messaging system are not
                                                      						  the members of this list. |
| All Voicemail Enabled Contacts | By default, the All Voicemail-Enabled Contacts list has no
                                          						members. You can add all the VPIM contacts as members of this list to address
                                          						messages to all the users of the entire group. You can also add contact
                                          						templates that are used to create VPIM contacts to this list. Adding contact
                                          						templates ensure that the VPIM contacts further created are automatically added
                                          						as members of this list. Note For information on VPIM, see the Networking chapter. | Note | For information on VPIM, see the Networking chapter. |
| Note | For information on VPIM, see the Networking chapter. |

| Note | The default users, such as operator and messaging system are not
                                                      						  the members of this list. |
|---|---|

| Note | For information on VPIM, see the Networking chapter. |
|---|---|

| Note | You can manage the distribution lists using the Bulk
                                          			 Administration Tool. For more information, see the Bulk Administration Tool section. |
|---|---|

| Tip | The Distribution List Builder tool can be used to
                                          			 add multiple users to a new or existing system distribution list based on a
                                          			 number of search criteria or by importing from a comma-separated value (CSV)
                                          			 file. Download the latest version, and view training videos and Help at http://www.ciscounitytools.com/Applications/CxN/PublicDistributionListBuilder/PublicDistributionListBuilder.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Distribution Lists and select System Distribution Lists . The Search Distribution Lists page appears displaying the
                                          				currently configured distribution lists. |
|---|---|
| Step 2 | Configure system distribution list (For more information on each
                                       			 field, see Help> This Page): |

| Step 1 | In Cisco Unity Connection Administration,
                                       			 expand Distribution Lists and
                                       			 select System Distribution
                                          				Lists . The Search Distribution Lists page appears
                                          				displaying the currently configured distribution lists. |
|---|---|
| Step 2 | On the Search Distribution Lists page,
                                       			 select the distribution list to which you want to add or remove the
                                       			 distribution list members. |
| Step 3 | On the Edit Distribution List Basics page,
                                       			 select Edit> Distribution List Members. |
| Step 4 | Add or remove the distribution list members
                                       			 (For more information on each field, see Help> This Page): |

| Note | Only a Unity Connection user can be added as a member of system
                                       		  distribution list access list. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select Messaging . |
|---|---|
| Step 2 | Check the Use Access Lists to Control Who Can
                                             				Send to System Distribution Lists check box. |
| Step 3 | Check the Allow Delivery of Messages to System
                                             				Distribution Lists That Have No Access Lis t check box. Note Uncheck this check box to reject all
                                                         				  messages sent to system distribution lists that do not have an access list, and
                                                         				  send a Non-Delivery Receipt (NDR) to the message sender. | Note | Uncheck this check box to reject all
                                                         				  messages sent to system distribution lists that do not have an access list, and
                                                         				  send a Non-Delivery Receipt (NDR) to the message sender. |
| Note | Uncheck this check box to reject all
                                                         				  messages sent to system distribution lists that do not have an access list, and
                                                         				  send a Non-Delivery Receipt (NDR) to the message sender. |
| Step 4 | Specify the suffix that is used to
                                          			 distinguish access lists in the System Distribution List Alias
                                             				Suffix for Access Lists field and select Save . |

| Note | Uncheck this check box to reject all
                                                         				  messages sent to system distribution lists that do not have an access list, and
                                                         				  send a Non-Delivery Receipt (NDR) to the message sender. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                       			 expand Class of Service and select Class of Service. The Search Class of Service page appears
                                          				displaying the currently configured classes of services. |
|---|---|
| Step 2 | On the Search Class of Service page, select
                                       			 the class of service applied to the voicemail users. |
| Step 3 | On the Edit Class of Service page, in the
                                       			 Message Options section, check the Allow Users to Send Messages to System
                                       			 Distribution Lists check box and select Save. |