---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-9c03f7f954
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_010000.html
retrieved_at: 2026-08-21T09:08:56.732831+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: User Templates

## Chapter: User Templates

# User Templates

This chapter provides information about using Cisco Unified Communications Manager Bulk Administration (BAT) user templates to
                        		define the common user attributes to add a group of new users.

## Find BAT User Template

Unified Communications Manager lets you locate specific user templates on the basis of specific criteria, which is useful when you have more than one user
                              template.

During your work in a browser session, your find/list search preferences get stored in the cookies on the client machine.
                                          If you navigate to other menu items and return to this menu item, or if you close the browser and then reopen a new browser
                                          window, the system retains your Unified Communications Manager search preferences until you modify your search.

Step 1

Choose Bulk
                                             				  Administration > Users > User
                                             				  Template .

The Find and List User Templates window displays.
                                          				Use the two drop-down list boxes to search for a template.

Step 2

From the first Find User Template where drop-down list box,
                                       			 choose one of the following criteria:

- User Template Name

- Department

From the second Find User Template where drop-down list box,
                                          				choose one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Step 3

Specify the appropriate search text, if applicable, and click Find .

Tip

To find all User Templates that are registered in the database,
                                                      				  click Find without entering any search text.

A list of discovered templates displays by

- User Template

- Department

Step 4

From the list of records, click the user template that matches
                                       			 your search criteria.

## Create New BAT User Template

You can create new user templates.

Step 1

Choose Bulk
                                             				  Administration > Users > User
                                             				  Template .

Step 2

Click Add New .

Step 3

Enter the user settings that this group of users have in common.

Step 4

Click Save .

## Modify BAT User Template

You can view or modify an existing user template.

Step 1

Find the user template that you want to modify.

Step 2

In the User Template Configuration window, add, change,
                                       			 or remove settings in the template.

Step 3

After you have modified the settings to update the template, click Save .

## Copy BAT User Template

You can copy the properties of a user template into a new
                              		  user template when you want to change only a few fields.

Step 1

Find the user template that you want to copy.

Step 2

In the User Template Configuration window, verify that
                                       			 this is the template that you want to copy and click Copy .

Step 3

Update the fields as needed for the new template.

Step 4

Click Save .

## Delete BAT User Template

You can delete BAT user templates when you no longer require
                              		  them. Use this procedure to delete a user template.

Caution

The delete action is final. You cannot retrieve deleted templates.

Step 1

Find the user template that you want to delete.

Step 2

In the User Template Configuration window, verify
                                       			 that this is the template that you want to delete and click Delete .

You can also delete the user template from the Find and List User Templates window. Check
                                                      				  the check box next to the template that you want to delete and click Delete Selected .

A message displays that asks you to confirm the delete operation.

Step 3

To delete the template, click OK . The template name disappears from the list
                                       			 of user templates list on the Find and List User Templates window.

Caution

If you submit a job with a particular user template, and if you
                                                      				  delete that user template before the execution of the job, the job also gets
                                                      				  deleted. You have to resubmit the job by creating another user template.

## BAT User Template
                        	 Field Descriptions

In the BAT
                              		  user interface, field names that have an asterisk require an entry. Treat
                              		  fields that do not have an asterisk as optional.

The following
                              		  table provides descriptions of all possible fields that appear after you add a
                              		  BAT user template.

Field

Description

User
                                          					 Template Name

Enter a
                                          					 unique name, up to 30 alphanumeric characters, for the user template.

Default
                                          					 Password to User ID

Check this
                                          					 check box if you want to make the user ID the default password for all users.

Default PIN
                                          					 to Telephone Number

Check this
                                          					 check box to make the telephone number the default PIN.

Default
                                          					 Telephone Number to Primary Extension

Check this
                                          					 check box to make the telephone number the primary extension.

Default Mail
                                          					 ID to User ID

Check this
                                          					 check box to make the mail ID to default for the user ID.

Manager User
                                          					 ID

Enter
                                          					 manager user ID, up to 128 characters, for the user of this phone.

Department

Enter the
                                          					 department number, up to 64 characters, for the user of this phone.

User Locale

Choose the
                                          					 language and country set that you want to associate with this user from the
                                          					 drop-down list. Your choice determines which cultural-dependent attributes
                                          					 exist for this user and which language displays in the Unified CM user
                                          					 windows and phones.

Associated
                                          					 PC

This field, which is required for Cisco SoftPhone and Cisco Unified Communications Manager Attendant Console users, displays after the user is added.

Default
                                          					 Profile

Choose the
                                          					 default profile for this user from the default Profile drop-down list.

BLF Presence
                                          					 Group

From the
                                          					 drop-down list, choose the BLF presence group that watches the status of the
                                          					 directory number, the presence entity.

SUBSCRIBE
                                          					 Calling Search Space

All calling search spaces that you configure in Unified CM Administration appear in the SUBSCRIBE Calling Search Space drop-down list.

The SUBSCRIBE Calling Search Space determines how Cisco Unified Communications Manager routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                          purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ).

Allow
                                          					 Control of Device from CTI

Check this
                                          					 check box to allow CTI to control and monitor this device.

If the associated directory number specifies a shared line, enable this check box as long as at least one associated device
                                          specifies a combination of device type and protocol that CTI supports.

Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled.

EMCC Enabled

Check this
                                          					 check box to enable the EMCC service.

User Rank

From the drop-down list box, select the rank that you want to assign to this user. The highest rank is 1, the lowest is 10.

Access
                                          					 Control Group

From the
                                          					 drop-down list, choose the access control group to which the user belongs. Only those access control groups that are either the same or lower than the user's rank  are available to select from.

Digest
                                          					 Credentials

When you configure digest authentication for phones that are running SIP, Cisco Unified Communications Manager challenges the identity of the phone every time that the phone sends a SIP request to Cisco Unified Communications Manager . The digest credentials that you enter in this field get associated with the phone when you choose a digest user in the Phone Configuration window.

Enter a
                                          					 string of up to 128 alphanumeric characters.

For information about digest authentication, see the Cisco Unified Communications Manager Security Guide .

Confirm
                                          					 Digest Credentials

To confirm that you entered the digest credentials correctly, reenter the credentials in this field.

Home
                                          					 Cluster

Check this check box to home users in this user template to this cluster. The user must only be homed to one cluster within
                                          the enterprise.

IM and Presence does not function properly if a user is assigned to more than one home cluster.

Enable
                                          					 User for Unified CM IM and Presence

Check this check box to enable users in this user template for IM and Presence. Configure IM and Presence in the associated
                                          service profile.

You must install a Cisco Unified Communications Manager IM and Presence node along with this Cisco Unified Communications
                                                      Manager cluster.

Use the User Management > User Settings > UC Services menu to configure the IM and Presence service.

Check this
                                          					 check box to enable the user to include meeting and calendar information in IM
                                             						and Presence Service .

The user
                                          					 must be on the home cluster and have IM and Presence enabled. Also ensure that
                                          					 an Exchange Presence Gateway is configured on the Cisco Unified Communications Manager IM and Presence
                                             						Service server.

Assigned
                                          					 Presence Server

Assign a user to an IM and Presence Service server that is installed in the cluster if the system is nonbalanced. The server you specify using the Bulk Administration
                                          Tool must be part of a Presence Redundancy Group.

For
                                          					 clusters that have the user assignment mode for the IM and Presence server set
                                          					 to balanced or active-standby, user assignments that are made using the Bulk
                                          					 Administration Tool override the automatic user assignments.

UC Service
                                          					 Profile

Choose a UC service profile from the drop-down list.

Use the User Management > User Settings > Service Profile menu to set up service profiles for the users.

Enable
                                          					 Mobility

Check this check box to activate Cisco Unified Mobility, which allows a user to manage calls by using a single phone number
                                          and to pick up calls on the desk phone and mobile phone.

Enable
                                          					 Mobile Voice Access

Check this
                                          					 check box to allow the user to access the Mobile Voice Access integrated voice
                                          					 response (IVR) system to initiate Cisco Unified Mobility calls and activate or
                                          					 deactivate Cisco Unified Mobility capabilities.

Maximum
                                          					 Wait Time for Desk Pickup

Enter the
                                          					 maximum wait time, up to five numerals, for this user.

This value indicates the maximum time that is permitted to pass before the user pickup a call that is transferred from the
                                          mobile phone to the desk phone.

Maximum Login Time (HHH:MM)

Enter the maximum login time in the HHH:MM format to configure maximum login time for the Extension Mobility and Extension
                                          Mobility Cross Cluster users.

The value ranges from 00:01 to 168:00 hours.

For example: 168:00, 25:16, 025:16, :30 or 00:30.

Remote
                                          					 Destination Limit

Enter the
                                          					 maximum number of phones, up to two numerals, to which the user is permitted to
                                          					 transfer calls from the desk phone.

| Note | During your work in a browser session, your find/list search preferences get stored in the cookies on the client machine.
                                          If you navigate to other menu items and return to this menu item, or if you close the browser and then reopen a new browser
                                          window, the system retains your Unified Communications Manager search preferences until you modify your search. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > User
                                             				  Template . The Find and List User Templates window displays.
                                          				Use the two drop-down list boxes to search for a template. |
|---|---|
| Step 2 | From the first Find User Template where drop-down list box,
                                       			 choose one of the following criteria: User Template Name Department From the second Find User Template where drop-down list box,
                                          				choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, and click Find . Tip To find all User Templates that are registered in the database,
                                                      				  click Find without entering any search text. A list of discovered templates displays by User Template Department | Tip | To find all User Templates that are registered in the database,
                                                      				  click Find without entering any search text. |
| Tip | To find all User Templates that are registered in the database,
                                                      				  click Find without entering any search text. |
| Step 4 | From the list of records, click the user template that matches
                                       			 your search criteria. The window displays the user template that you choose. |

| Tip | To find all User Templates that are registered in the database,
                                                      				  click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > User
                                             				  Template . The Find and List User Templates window displays. |
|---|---|
| Step 2 | Click Add New . The User Template Configuration window displays. |
| Step 3 | Enter the user settings that this group of users have in common. See BAT User Template Field Descriptions for field descriptions. |
| Step 4 | Click Save . When the user template is added to the database, the status
                                       			 indicates that the transaction has completed. |

| Step 1 | Find the user template that you want to modify. |
|---|---|
| Step 2 | In the User Template Configuration window, add, change,
                                       			 or remove settings in the template. See Table 1 for field descriptions. |
| Step 3 | After you have modified the settings to update the template, click Save . |

| Step 1 | Find the user template that you want to copy. |
|---|---|
| Step 2 | In the User Template Configuration window, verify that
                                       			 this is the template that you want to copy and click Copy . The template reproduces and creates a copy. The copy
                                       			 duplicates all the values that were specified in the original template. |
| Step 3 | Update the fields as needed for the new template. See Table 1 for field descriptions. |
| Step 4 | Click Save . |

| Caution | The delete action is final. You cannot retrieve deleted templates. |
|---|---|

| Step 1 | Find the user template that you want to delete. |
|---|---|
| Step 2 | In the User Template Configuration window, verify
                                       			 that this is the template that you want to delete and click Delete . Note You can also delete the user template from the Find and List User Templates window. Check
                                                      				  the check box next to the template that you want to delete and click Delete Selected . A message displays that asks you to confirm the delete operation. | Note | You can also delete the user template from the Find and List User Templates window. Check
                                                      				  the check box next to the template that you want to delete and click Delete Selected . |
| Note | You can also delete the user template from the Find and List User Templates window. Check
                                                      				  the check box next to the template that you want to delete and click Delete Selected . |
| Step 3 | To delete the template, click OK . The template name disappears from the list
                                       			 of user templates list on the Find and List User Templates window. Caution If you submit a job with a particular user template, and if you
                                                      				  delete that user template before the execution of the job, the job also gets
                                                      				  deleted. You have to resubmit the job by creating another user template. | Caution | If you submit a job with a particular user template, and if you
                                                      				  delete that user template before the execution of the job, the job also gets
                                                      				  deleted. You have to resubmit the job by creating another user template. |
| Caution | If you submit a job with a particular user template, and if you
                                                      				  delete that user template before the execution of the job, the job also gets
                                                      				  deleted. You have to resubmit the job by creating another user template. |

| Note | You can also delete the user template from the Find and List User Templates window. Check
                                                      				  the check box next to the template that you want to delete and click Delete Selected . |
|---|---|

| Caution | If you submit a job with a particular user template, and if you
                                                      				  delete that user template before the execution of the job, the job also gets
                                                      				  deleted. You have to resubmit the job by creating another user template. |
|---|---|

| Field | Description |
|---|---|
| User
                                          					 Template Name | Enter a
                                          					 unique name, up to 30 alphanumeric characters, for the user template. |
| Default
                                          					 Password to User ID | Check this
                                          					 check box if you want to make the user ID the default password for all users. |
| Default PIN
                                          					 to Telephone Number | Check this
                                          					 check box to make the telephone number the default PIN. |
| Default
                                          					 Telephone Number to Primary Extension | Check this
                                          					 check box to make the telephone number the primary extension. |
| Default Mail
                                          					 ID to User ID | Check this
                                          					 check box to make the mail ID to default for the user ID. |
| Manager User
                                          					 ID | Enter
                                          					 manager user ID, up to 128 characters, for the user of this phone. |
| Department | Enter the
                                          					 department number, up to 64 characters, for the user of this phone. |
| User Locale | Choose the
                                          					 language and country set that you want to associate with this user from the
                                          					 drop-down list. Your choice determines which cultural-dependent attributes
                                          					 exist for this user and which language displays in the Unified CM user
                                          					 windows and phones. |
| Associated
                                          					 PC | This field, which is required for Cisco SoftPhone and Cisco Unified Communications Manager Attendant Console users, displays after the user is added. |
| Default
                                          					 Profile | Choose the
                                          					 default profile for this user from the default Profile drop-down list. |
| BLF Presence
                                          					 Group | From the
                                          					 drop-down list, choose the BLF presence group that watches the status of the
                                          					 directory number, the presence entity. |
| SUBSCRIBE
                                          					 Calling Search Space | All calling search spaces that you configure in Unified CM Administration appear in the SUBSCRIBE Calling Search Space drop-down list. The SUBSCRIBE Calling Search Space determines how Cisco Unified Communications Manager routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                          purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ). |
| Allow
                                          					 Control of Device from CTI | Check this
                                          					 check box to allow CTI to control and monitor this device. If the associated directory number specifies a shared line, enable this check box as long as at least one associated device
                                          specifies a combination of device type and protocol that CTI supports. Note Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. | Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
| Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
| EMCC Enabled | Check this
                                          					 check box to enable the EMCC service. |
| User Rank | From the drop-down list box, select the rank that you want to assign to this user. The highest rank is 1, the lowest is 10. |
| Access
                                          					 Control Group | From the
                                          					 drop-down list, choose the access control group to which the user belongs. Only those access control groups that are either the same or lower than the user's rank  are available to select from. |
| Digest
                                          					 Credentials | When you configure digest authentication for phones that are running SIP, Cisco Unified Communications Manager challenges the identity of the phone every time that the phone sends a SIP request to Cisco Unified Communications Manager . The digest credentials that you enter in this field get associated with the phone when you choose a digest user in the Phone Configuration window. Enter a
                                          					 string of up to 128 alphanumeric characters. For information about digest authentication, see the Cisco Unified Communications Manager Security Guide . |
| Confirm
                                          					 Digest Credentials | To confirm that you entered the digest credentials correctly, reenter the credentials in this field. |
| Home
                                          					 Cluster | Check this check box to home users in this user template to this cluster. The user must only be homed to one cluster within
                                          the enterprise. Note IM and Presence does not function properly if a user is assigned to more than one home cluster. | Note | IM and Presence does not function properly if a user is assigned to more than one home cluster. |
| Note | IM and Presence does not function properly if a user is assigned to more than one home cluster. |
| Enable
                                          					 User for Unified CM IM and Presence | Check this check box to enable users in this user template for IM and Presence. Configure IM and Presence in the associated
                                          service profile. Note You must install a Cisco Unified Communications Manager IM and Presence node along with this Cisco Unified Communications
                                                      Manager cluster. Use the User Management > User Settings > UC Services menu to configure the IM and Presence service. | Note | You must install a Cisco Unified Communications Manager IM and Presence node along with this Cisco Unified Communications
                                                      Manager cluster. Use the User Management > User Settings > UC Services menu to configure the IM and Presence service. |
| Note | You must install a Cisco Unified Communications Manager IM and Presence node along with this Cisco Unified Communications
                                                      Manager cluster. Use the User Management > User Settings > UC Services menu to configure the IM and Presence service. |
| Include meeting information
                                       				  in Presence | Check this
                                          					 check box to enable the user to include meeting and calendar information in IM
                                             						and Presence Service . The user
                                          					 must be on the home cluster and have IM and Presence enabled. Also ensure that
                                          					 an Exchange Presence Gateway is configured on the Cisco Unified Communications Manager IM and Presence
                                             						Service server. |
| Assigned
                                          					 Presence Server | Assign a user to an IM and Presence Service server that is installed in the cluster if the system is nonbalanced. The server you specify using the Bulk Administration
                                          Tool must be part of a Presence Redundancy Group. For
                                          					 clusters that have the user assignment mode for the IM and Presence server set
                                          					 to balanced or active-standby, user assignments that are made using the Bulk
                                          					 Administration Tool override the automatic user assignments. |
| UC Service
                                          					 Profile | Choose a UC service profile from the drop-down list. Note Use the User Management > User Settings > Service Profile menu to set up service profiles for the users. | Note | Use the User Management > User Settings > Service Profile menu to set up service profiles for the users. |
| Note | Use the User Management > User Settings > Service Profile menu to set up service profiles for the users. |
| Enable
                                          					 Mobility | Check this check box to activate Cisco Unified Mobility, which allows a user to manage calls by using a single phone number
                                          and to pick up calls on the desk phone and mobile phone. |
| Enable
                                          					 Mobile Voice Access | Check this
                                          					 check box to allow the user to access the Mobile Voice Access integrated voice
                                          					 response (IVR) system to initiate Cisco Unified Mobility calls and activate or
                                          					 deactivate Cisco Unified Mobility capabilities. |
| Maximum
                                          					 Wait Time for Desk Pickup | Enter the
                                          					 maximum wait time, up to five numerals, for this user. This value indicates the maximum time that is permitted to pass before the user pickup a call that is transferred from the
                                          mobile phone to the desk phone. |
| Maximum Login Time (HHH:MM) | Enter the maximum login time in the HHH:MM format to configure maximum login time for the Extension Mobility and Extension
                                          Mobility Cross Cluster users. The value ranges from 00:01 to 168:00 hours. For example: 168:00, 25:16, 025:16, :30 or 00:30. |
| Remote
                                          					 Destination Limit | Enter the
                                          					 maximum number of phones, up to two numerals, to which the user is permitted to
                                          					 transfer calls from the desk phone. |

| Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
|---|---|

| Note | IM and Presence does not function properly if a user is assigned to more than one home cluster. |
|---|---|

| Note | You must install a Cisco Unified Communications Manager IM and Presence node along with this Cisco Unified Communications
                                                      Manager cluster. Use the User Management > User Settings > UC Services menu to configure the IM and Presence service. |
|---|---|

| Note | Use the User Management > User Settings > Service Profile menu to set up service profiles for the users. |
|---|---|