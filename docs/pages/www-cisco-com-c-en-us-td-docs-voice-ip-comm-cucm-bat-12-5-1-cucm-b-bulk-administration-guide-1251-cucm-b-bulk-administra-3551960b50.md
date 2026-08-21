---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-3551960b50
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0100100.html
retrieved_at: 2026-08-21T18:00:06.174617+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: User Device Profile Templates

## Chapter: User Device Profile Templates

# User Device Profile Templates

This chapter provides information to create and modify user
                        		device profiles.

## Find User Device Profile Template

You can locate a specific user device profile (UDP) template
                              		  in the Cisco Unified Communications Manager database on the basis of specific criteria
                              		  because you can have several UDP templates.

During your work in a browser session, your find/list search
                                          			 preferences are stored in the cookies on the client machine. If you navigate to
                                          			 other menu items and return to this menu item, or if you close the browser and
                                          			 then reopen a new browser window, your Cisco Unified Communications Manager search preferences are retained until you
                                          			 modify your search.

Step 1

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > User Device Profile
                                             				  Template .

The Find and List UDP Templates window displays.
                                          				Use the two drop-down list boxes to search for a template.

Step 2

From the first Find UDP Templates where drop-down list box,
                                       			 choose one of the following criteria:

- Profile Name

- Profile Description

- Device Type

From the second Find UDP Templates where drop-down list box,
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

To find all UDP templates that are registered in the database,
                                                      				  click Find without entering any search text.

A list of discovered templates displays by:

- Name

- Description

- Device Type

- Profile Type

Step 4

From the list of records, click the template name that matches
                                       			 your search criteria.

## Create Bulk Administration Tool (BAT) Template for User Device Profiles

You can create a template to add user device profiles in
                              		  bulk.

Step 1

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > User Device Profile
                                             				  Template .

Step 2

Click Add New .

Step 3

From the Device Type drop-down list, choose the model of user device profile. Click Next .

Step 4

Enter data for an individual user device profile template on each
                                       			 line in the spreadsheet. Complete all mandatory fields and any relevant
                                       			 optional fields.

Tip

Step 5

Check the Ignore Presentation Indicators (Internal Calls
                                       			 Only) check box, as needed.

Step 6

Check the Do Not Disturb check box if you need the DND
                                       			 feature to be enabled.

Step 7

Choose the DND option from the DND Option drop down list.

Step 8

Choose the DND incoming call alert option from the DND Incoming Call Alert drop down list.

None—Choose this option to have no alert for incoming calls.

Disable—Choose this option if you want to disable incoming call alerts while in the DND mode.

Flash Only—Choose this option to have the device flash while in DND mode.

Beep Only—Choose this option to have the device beep while in the DND mode.

Step 9

Choose the Extension Mobility Cross Cluster CSS from the Extension Mobility Cross Cluster CSS drop-down list.

Step 10

Choose the Feature Control Policy from the Feature Control Policy drop-down list.

Step 11

Click Save .

Step 12

Depending on the phone button template that you chose, links display to add lines, speed dials settings, subscribed Cisco
                                       IP Phone service settings, and busy lamp field speed dial settings.

For some Cisco Unified IP Phone models, you can add Cisco Unified IP Phone services and Speed Dials to the template.

## User Device Profile Template Fields Descriptions in BAT Spreadsheet

The following table describes all the user device profile template
                              		  fields in the BAT spreadsheet.

Depending on the model of device, some of the fields may not be available.

Field

Description

User Device Profile Template Name

Enter a unique identifier for the device profile name up to 50 characters.

Description

Enter a description for the UDP template. The
                                          					 description can include up to 50 characters in any language, but it cannot
                                          					 include double-quotes ( " ), percentage sign
                                          					 ( % ), ampersand (&), back-slash
                                          					 ( \ ), or angle brackets (<>).

User Hold Audio Source

Enter the user hold audio source that this group of IP phones
                                          					 or CTI ports should use.

The user hold audio source identifies the audio source from
                                          					 which music is played when a user places a call on hold.

User Locale

Enter the country and language set that you want to associate
                                          					 with this group of IP phones.

This choice determines which cultural-dependent attributes
                                          					 exist for this user and which language displays for the user in the Cisco Unified Communications Manager user windows and phones.

Phone Button Template

Choose a phone button template for this profile.

Softkey Template

Enter the softkey template to be used for all phones in this
                                          					 group.

Privacy

Choose the appropriate privacy option for the profile. For each Device that wants Privacy, choose On in the Privacy drop-down list box.

Single Button Barge

Choose the appropriate option for the single button barge feature.

Off—This setting disables the Single Button Barge/cBarge feature; however, the regular Barge or cBarge features will still
                                                work.

Barge—This setting enables the Singe Button Barge feature.

cBarge—This setting enables the Single Button cBarge feature.

Default—This setting uses the Single Button Barge/cBarge setting that is in the service parameter.

Join Across Lines

Choose the appropriate option to join across lines.

- Off— This setting disables the Join Across Lines feature.

- On—This setting enables the Join Across Lines feature.

- Default—Uses the Join Across Lines setting that is in the service parameter.

Always Use Prime Line

Enter the Always Use Prime Line setting that you want to use from the following values:

On

Off

Default

Always Use Prime Line for Voice Message

Enter the Always Use Prime Line for Voice Message setting that you want to use from the following values:

On

Off

Default

MLPP Indication

To specify whether the device can play precedence tones when a MLPP precedence call is placed, choose one of the following
                                          values:

- Default—To inherit the MLPP indication from the device pool.

- Off—Does not send MLPP indication tones.

- On—Sends indication of an MLPP precedence call.

MLPP Preemption

To specify whether the device can preempt calls in progress when placing an MLPP precedence call, choose one of the following:

- Default—To inherit the MLPP preemption setting from the device pool.

- Disable—Does not preempt calls when it places an MLPP precedence call.

Do not configure a device with MLPP Indication set to Off while MLPP Preemption is set to Foreceful.

MLPP Domain

Enter a hexadecimal value for the MLPP domain associated with
                                          					 this device. Must be blank or a value between 0 and FFFFFF.

Expansion Module Information

Choose the type of expansion module if installed in the phone or choose <None> for Module 1 and Module 2.

Login User ID

Enter the login user ID for a default profile. After the user logs out from using the user device profile, the user device
                                          profile will automatically log in to this login user ID and use the default profile.

You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field.
                                                      A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want
                                                      to use, and all login user IDs that match the pattern that you entered will display in the Selected login user ID field. Choose
                                                      the desired ID and click OK.

## Modify User Device Profile BAT Template

You can modify the properties of an existing BAT template
                              		  when you want to change only a few fields for the same device.

Step 1

Find the UDP template you want to modify.

Step 2

From the list of displayed templates, click the template name you
                                       			 want to modify.

Step 3

Verify that this is the template that you want to modify.

Step 4

Modify the details in the template fields as needed.

Step 5

Click Save to save the changes to the existing
                                       			 template.

### Copy User Device Profile Template

You can copy the properties of a template into a new
                                 		  template when you want to change only a few fields.

The new template that you create must be the same device type as the
                                             			 original template, such as CiscoIPUser Device Profile model 7960.

Use the following procedure to copy an existing BAT
                                 		  template.

Step 1

Find the UDP template you want to copy.

Step 2

From the list of displayed templates, click the template name you
                                          			 want to copy.

The chosen template details display in the UDP Template Configuration window.

You can also copy the template by clicking the icon in the Copy column corresponding to the template
                                                         				  you want to copy.

Step 3

Verify that this is the template that you want to copy and click Copy .

Step 4

In the User Device Profile Template Name field, enter
                                          			 a new template name, up to 50 alphanumeric characters.

Step 5

Update the fields as needed for the new template.

Step 6

Click Save . The template that is added to BAT
                                          			 displays in the Templates column on the left.

### Delete User Device Profile Template

You can delete BAT user device profile templates when you no
                                 		  longer require them.

Step 1

Find the UDP template you want to delete.

Step 2

From the list of displayed templates, click the template name you
                                          			 want to delete.

The chosen template details display in the UDP Template Configuration window.

You can also delete the template by checking the check box next
                                                         				  to the template name and clicking Delete Selected .

Step 3

Verify that this is the template that you want to delete and click Delete . A message displays that asks you to
                                          			 confirm the delete operation.

Step 4

Click OK to delete the template.

| Note | During your work in a browser session, your find/list search
                                          			 preferences are stored in the cookies on the client machine. If you navigate to
                                          			 other menu items and return to this menu item, or if you close the browser and
                                          			 then reopen a new browser window, your Cisco Unified Communications Manager search preferences are retained until you
                                          			 modify your search. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > User Device Profile
                                             				  Template . The Find and List UDP Templates window displays.
                                          				Use the two drop-down list boxes to search for a template. |
|---|---|
| Step 2 | From the first Find UDP Templates where drop-down list box,
                                       			 choose one of the following criteria: Profile Name Profile Description Device Type From the second Find UDP Templates where drop-down list box,
                                          				choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, and click Find . Tip To find all UDP templates that are registered in the database,
                                                      				  click Find without entering any search text. A list of discovered templates displays by: Name Description Device Type Profile Type | Tip | To find all UDP templates that are registered in the database,
                                                      				  click Find without entering any search text. |
| Tip | To find all UDP templates that are registered in the database,
                                                      				  click Find without entering any search text. |
| Step 4 | From the list of records, click the template name that matches
                                       			 your search criteria. The UDP Template Configuration window displays. |

| Tip | To find all UDP templates that are registered in the database,
                                                      				  click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > User Device Profile
                                             				  Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Device Type drop-down list, choose the model of user device profile. Click Next . |
| Step 4 | Enter data for an individual user device profile template on each
                                       			 line in the spreadsheet. Complete all mandatory fields and any relevant
                                       			 optional fields. Each column heading specifies the length of the field and whether it is required or optional. See Table 1 for field descriptions. Note Depending on the model of device, some of the fields may not display. Tip You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field. A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want to use, and all login user IDs that match the pattern
                                                   that you entered will display in the Selected login user ID field. Choose the desired ID and click OK . | Note | Depending on the model of device, some of the fields may not display. | Tip | You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field. A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want to use, and all login user IDs that match the pattern
                                                   that you entered will display in the Selected login user ID field. Choose the desired ID and click OK . |
| Note | Depending on the model of device, some of the fields may not display. |
| Tip | You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field. A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want to use, and all login user IDs that match the pattern
                                                   that you entered will display in the Selected login user ID field. Choose the desired ID and click OK . |
| Step 5 | Check the Ignore Presentation Indicators (Internal Calls
                                       			 Only) check box, as needed. |
| Step 6 | Check the Do Not Disturb check box if you need the DND
                                       			 feature to be enabled. |
| Step 7 | Choose the DND option from the DND Option drop down list. |
| Step 8 | Choose the DND incoming call alert option from the DND Incoming Call Alert drop down list. None—Choose this option to have no alert for incoming calls. Disable—Choose this option if you want to disable incoming call alerts while in the DND mode. Flash Only—Choose this option to have the device flash while in DND mode. Beep Only—Choose this option to have the device beep while in the DND mode. |
| Step 9 | Choose the Extension Mobility Cross Cluster CSS from the Extension Mobility Cross Cluster CSS drop-down list. |
| Step 10 | Choose the Feature Control Policy from the Feature Control Policy drop-down list. Note This field displays for RoundTable phones only. | Note | This field displays for RoundTable phones only. |
| Note | This field displays for RoundTable phones only. |
| Step 11 | Click Save . |
| Step 12 | Depending on the phone button template that you chose, links display to add lines, speed dials settings, subscribed Cisco
                                       IP Phone service settings, and busy lamp field speed dial settings. For some Cisco Unified IP Phone models, you can add Cisco Unified IP Phone services and Speed Dials to the template. |

| Note | Depending on the model of device, some of the fields may not display. |
|---|---|

| Tip | You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field. A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want to use, and all login user IDs that match the pattern
                                                   that you entered will display in the Selected login user ID field. Choose the desired ID and click OK . |
|---|---|

| Note | This field displays for RoundTable phones only. |
|---|---|

| Note | Depending on the model of device, some of the fields may not be available. |
|---|---|

| Field | Description |
|---|---|
| User Device Profile Template Name | Enter a unique identifier for the device profile name up to 50 characters. |
| Description | Enter a description for the UDP template. The
                                          					 description can include up to 50 characters in any language, but it cannot
                                          					 include double-quotes ( " ), percentage sign
                                          					 ( % ), ampersand (&), back-slash
                                          					 ( \ ), or angle brackets (<>). |
| User Hold Audio Source | Enter the user hold audio source that this group of IP phones
                                          					 or CTI ports should use. The user hold audio source identifies the audio source from
                                          					 which music is played when a user places a call on hold. |
| User Locale | Enter the country and language set that you want to associate
                                          					 with this group of IP phones. This choice determines which cultural-dependent attributes
                                          					 exist for this user and which language displays for the user in the Cisco Unified Communications Manager user windows and phones. |
| Phone Button Template | Choose a phone button template for this profile. |
| Softkey Template | Enter the softkey template to be used for all phones in this
                                          					 group. |
| Privacy | Choose the appropriate privacy option for the profile. For each Device that wants Privacy, choose On in the Privacy drop-down list box. |
| Single Button Barge | Choose the appropriate option for the single button barge feature. Off—This setting disables the Single Button Barge/cBarge feature; however, the regular Barge or cBarge features will still
                                                work. Barge—This setting enables the Singe Button Barge feature. cBarge—This setting enables the Single Button cBarge feature. Default—This setting uses the Single Button Barge/cBarge setting that is in the service parameter. |
| Join Across Lines | Choose the appropriate option to join across lines. Off— This setting disables the Join Across Lines feature. On—This setting enables the Join Across Lines feature. Default—Uses the Join Across Lines setting that is in the service parameter. |
| Always Use Prime Line | Enter the Always Use Prime Line setting that you want to use from the following values: On Off Default |
| Always Use Prime Line for Voice Message | Enter the Always Use Prime Line for Voice Message setting that you want to use from the following values: On Off Default |
| MLPP Indication | To specify whether the device can play precedence tones when a MLPP precedence call is placed, choose one of the following
                                          values: Default—To inherit the MLPP indication from the device pool. Off—Does not send MLPP indication tones. On—Sends indication of an MLPP precedence call. |
| MLPP Preemption | To specify whether the device can preempt calls in progress when placing an MLPP precedence call, choose one of the following: Default—To inherit the MLPP preemption setting from the device pool. Disable—Does not preempt calls when it places an MLPP precedence call. Foreceful—preempts calls in progress when it places an MLPP precedence call. Note Do not configure a device with MLPP Indication set to Off while MLPP Preemption is set to Foreceful. | Note | Do not configure a device with MLPP Indication set to Off while MLPP Preemption is set to Foreceful. |
| Note | Do not configure a device with MLPP Indication set to Off while MLPP Preemption is set to Foreceful. |
| MLPP Domain | Enter a hexadecimal value for the MLPP domain associated with
                                          					 this device. Must be blank or a value between 0 and FFFFFF. |
| Expansion Module Information | Choose the type of expansion module if installed in the phone or choose <None> for Module 1 and Module 2. |
| Login User ID | Enter the login user ID for a default profile. After the user logs out from using the user device profile, the user device
                                          profile will automatically log in to this login user ID and use the default profile. Note You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field.
                                                      A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want
                                                      to use, and all login user IDs that match the pattern that you entered will display in the Selected login user ID field. Choose
                                                      the desired ID and click OK. | Note | You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field.
                                                      A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want
                                                      to use, and all login user IDs that match the pattern that you entered will display in the Selected login user ID field. Choose
                                                      the desired ID and click OK. |
| Note | You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field.
                                                      A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want
                                                      to use, and all login user IDs that match the pattern that you entered will display in the Selected login user ID field. Choose
                                                      the desired ID and click OK. |

| Note | Do not configure a device with MLPP Indication set to Off while MLPP Preemption is set to Foreceful. |
|---|---|

| Note | You can obtain help in finding a valid login user ID by choosing the Select Login User ID link below the Login User ID field.
                                                      A separate dialog box pops up. In the Login User ID field, enter the first few characters of the login user ID that you want
                                                      to use, and all login user IDs that match the pattern that you entered will display in the Selected login user ID field. Choose
                                                      the desired ID and click OK. |
|---|---|

| Step 1 | Find the UDP template you want to modify. |
|---|---|
| Step 2 | From the list of displayed templates, click the template name you
                                       			 want to modify. The chosen template details display in the UDP Template Configuration window. |
| Step 3 | Verify that this is the template that you want to modify. |
| Step 4 | Modify the details in the template fields as needed. |
| Step 5 | Click Save to save the changes to the existing
                                       			 template. |

| Note | The new template that you create must be the same device type as the
                                             			 original template, such as CiscoIPUser Device Profile model 7960. |
|---|---|

| Step 1 | Find the UDP template you want to copy. |
|---|---|
| Step 2 | From the list of displayed templates, click the template name you
                                          			 want to copy. The chosen template details display in the UDP Template Configuration window. Note You can also copy the template by clicking the icon in the Copy column corresponding to the template
                                                         				  you want to copy. | Note | You can also copy the template by clicking the icon in the Copy column corresponding to the template
                                                         				  you want to copy. |
| Note | You can also copy the template by clicking the icon in the Copy column corresponding to the template
                                                         				  you want to copy. |
| Step 3 | Verify that this is the template that you want to copy and click Copy . The template reproduces and creates a copy. The copy
                                          			 duplicates all the values that were specified in the original template. |
| Step 4 | In the User Device Profile Template Name field, enter
                                          			 a new template name, up to 50 alphanumeric characters. |
| Step 5 | Update the fields as needed for the new template. |
| Step 6 | Click Save . The template that is added to BAT
                                          			 displays in the Templates column on the left. |

| Note | You can also copy the template by clicking the icon in the Copy column corresponding to the template
                                                         				  you want to copy. |
|---|---|

| Step 1 | Find the UDP template you want to delete. |
|---|---|
| Step 2 | From the list of displayed templates, click the template name you
                                          			 want to delete. The chosen template details display in the UDP Template Configuration window. Note You can also delete the template by checking the check box next
                                                         				  to the template name and clicking Delete Selected . | Note | You can also delete the template by checking the check box next
                                                         				  to the template name and clicking Delete Selected . |
| Note | You can also delete the template by checking the check box next
                                                         				  to the template name and clicking Delete Selected . |
| Step 3 | Verify that this is the template that you want to delete and click Delete . A message displays that asks you to
                                          			 confirm the delete operation. |
| Step 4 | Click OK to delete the template. The template name disappears from the list of templates in
                                          			 the Find and List UDP Templates window. |

| Note | You can also delete the template by checking the check box next
                                                         				  to the template name and clicking Delete Selected . |
|---|---|