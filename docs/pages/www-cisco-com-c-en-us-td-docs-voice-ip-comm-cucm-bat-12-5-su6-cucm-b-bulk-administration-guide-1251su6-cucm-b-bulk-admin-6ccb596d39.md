---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-6ccb596d39
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0101001.html
retrieved_at: 2026-08-21T08:56:28.794939+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: User Device Profile Updates

## Chapter: User Device Profile Updates

# User Device Profile Updates

This chapter provides information to update the user device
                        		profile (UDP) settings, such as changing or adding the device pool, or calling
                        		search space for a group of similar user device profiles. You can locate the
                        		existing UDP records that you want to update using either a query search or a
                        		custom file.

## Update UDPs Using Query

You can create a query to locate UDPs to update.

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Update
                                             				  UDP > Query .

The Find and List User Device Profiles To Update window displays.

You can update all user device profiles by not specifying a
                                                      				  query and clicking Find. Skip to the Choose Update Parameters .

From the first Find User Device Profiles where drop-down list, choose one of the following criteria:

Profile Name

Profile Description

Profile Type

Profile Protocol

From the second Find User Device Profiles where drop-down list, choose one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Specify the appropriate search text, if applicable.

To find all user device profiles that are registered in the
                                                      				  database, click Find without entering any search text.

To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down list, and repeat Step 2 and Step 3 .

Click Find .

### What to do next

To complete the procedure for updating UDPs, proceed to choose the update parameters.

## Update UDPs Using Custom File

You can update UDPs using a list of UDPs in a custom file. Use the custom file to search for UDPs in the database that you want to update.

### Before you begin

Before you can update a UDP from , you must perform the following tasks:

Identify the UDPs that you need to update.

Create a text file that lists one of these options on a separate
                                    				line:

Profile Name

Description

Profile Type

Profile Protocol

Upload the text file to the server.

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Update UDP > Custom
                                             				  File .

From the Update Bulk UDP where drop-down list box,
                                       			 choose the type of custom file that you have created from the following
                                       			 criteria:

Profile Name

Description

Device Type

Device Protocol

From the list of custom files, choose the filename of the custom
                                       			 file for this update.

Click Find .

Do not use the insert or export transaction files that are
                                                      				  created with bat.xlt for the update transaction. Instead, create a custom file
                                                      				  with details of the UDP records that need to be updated. Use only this file for
                                                      				  the update transaction. In this custom update file, you do not need a header,
                                                      				  and you can enter values for profile name, description, profile type, or
                                                      				  profile protocol.

### What to do next

To complete the procedure for updating UDPs, proceed to choose the update parameters.

## Choose Update Parameters

After you define the query or custom file to search for UDPs,
                              		  use this procedure to choose parameters and define values for updating UDPs.

Do one of the following:

Click Next in the Find and List User Device Profiles To Update window if you used the Query option to locate UDPs to update.

Click Next in the Find and List UDP window if you used the
                                             				  Custom File option to locate UDPs to update.

Specify the setting that you want to update for all the records
                                       			 that you have defined in your query or custom file. You can choose multiple
                                       			 parameters to update.

Update the required UDP parameters. See Table 1 for field descriptions.

Select the update check box to the left of the field that you want
                                       			 to update. This action tells BAT to overwrite the existing value for the field.

The BAT updates only those fields for which you have selected
                                                      				  the update check box.

In the Job Information area, enter the job description.

Choose an activation method. Do one of the following:

Click Run Immediately to schedule and activate
                                             				  user device profiles immediately.

Click Run Later to schedule and activate user
                                             				  device profiles at a later time.

Click Submit to create a job for updating the
                                       			 records.

On the Update UDPs window, certain fields may not
                                                      				  display if the search results include devices of multiple types and protocols.
                                                      				  Make sure that you have the UDPs of same type and protocol for all the fields
                                                      				  to appear.

### Update UDP Field Descriptions

The following table describes the fields that display when
                                 		  you are updating a UDP.

In the BAT user interface, field names that have an asterisk
                                 		  require an entry. Treat fields that do not have an asterisk as optional.

Field

Description

Description

Enter a description that makes the device easy to recognize.
                                             					 The description can include up to 50 characters in any language, but it cannot
                                             					 include double-quotes ("), percentage sign
                                             					 (%), ampersand (&), backslash
                                             					 (\), or angle brackets (<>).

User Hold MOH Audio Source

Choose the audio source for this group of UDPs or ports.

The user hold audio source plays music when the user puts a
                                             					 call on hold.

User Locale

Choose the country and language set that you want to associate
                                             					 with this user.

This choice determines which culture-dependent attributes
                                             					 exist for this user and which language displays for the user in the Cisco Unified Communications Manager user windows and phones.

Phone Button Template

Choose an appropriate phone button template for this profile.

The phone button template determines the configuration of
                                             					 buttons on a phone and identifies which feature (line, speed dial, and so on)
                                             					 is used for each button.

Softkey Template

Choose the softkey template to be used for all UDPs in this
                                             					 group.

Privacy

Choose the appropriate privacy option for the profile from the
                                             					 drop-down list box:

- Off—Enables
                                                						privacy for each device.

- On—Disables
                                                						privacy for each device.

- Default—Applies
                                                						the default privacy settings to the device.

SUBSCRIBE Calling Search Space

Used with the Presence feature, the SUBSCRIBE Calling Search
                                             					 Space determines how Cisco Unified Communications Manager routes the subscription requests that come
                                             					 from the phone. From the drop-down list box, choose the calling search space
                                             					 that you want to use for this purpose.

Presence Group

From the drop-down list box, choose a presence group for this
                                             					 group of UDPs. The selected group specifies the devices, end users, and
                                             					 application users that can monitor this directory number.

Single Button Barge

From the drop-down list box, enable or disable the Single
                                             					 Button Barge/cBarge feature for this device or choose Default to use the
                                             					 service parameter setting.

- Off—This setting
                                                						disables the Single Button Barge/cBarge feature; however, the regular Barge or
                                                						cBarge features will still work.

- Barge—This setting
                                                						enables the Singe Button Barge feature.

- cBarge—This
                                                						setting enables the Single Button cBarge feature.

- Default—This
                                                						setting uses the Single Button Barge/cBarge setting that the service parameter
                                                						specifies.

Join Across Lines

From the drop-down list box, enable or disable the Join Across
                                             					 Lines feature for this device or choose Default to use the service parameter
                                             					 setting.

- Off—This setting
                                                						disables the Join Across Lines feature.

- On—This setting
                                                						enables the Join Across Lines feature.

- Default—This
                                                						setting uses the Join Across Lines setting that the service parameter
                                                						specifies.

Always Use Prime Line

From the drop-down list box, choose the Always Use Prime Line
                                             					 setting that you want to use from the following values:

- On

- Off

- Default

Always Use Prime Line for Voice Message

From the drop-down list box, choose the Always Use Prime Line
                                             					 for Voice Message setting that you want to use from the following values:

- On

- Off

- Default

Feature Control Policy

From the drop-down list box, choose the Feature Control Policy
                                             					 for this group of UDPs.

A feature control policy specifies the appearance of features
                                             					 and the associated softkeys that display on the UDP.

Ignore Presentation Indicators (internal calls only)

Check this check box if the system must ignore presentation
                                             					 indicators.

Do Not Disturb

If you want to enable the DND feature, check this check box.

DND Option

From the drop-down list box, choose a DND option from the
                                             					 following options:

- None

- Ringer Off

- Call Reject

- Use Common Phone
                                                						Profile Setting

DND Incoming Call Alert

From the drop-down list box, choose one of the following
                                             					 options:

- None

- Disable

- Flash Only

- Beep Only

Extension Mobility Cross Cluster CSS

From the drop-down list box, choose the appropriate setting
                                             					 for this group of UDPs.

The Extension Mobility Cross Cluster CSS setting gets used as
                                             					 the device CSS of the remote phone when the user selects this device profile
                                             					 during EMCC login.

Multilevel Precedence and Preemption (MLPP)
                                                						Information

MLPP Domain

Enter a hexadecimal value for the MLPP domain that is
                                             					 associated with this device. Ensure that this value specifies blank or a value
                                             					 between 0 and FFFFFF.

MLPP Indication

If available, this setting specifies whether a device that is
                                             					 capable of playing precedence tones will use the capability when it places an
                                             					 MLPP precedence call.

From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options:

- Default—This
                                                						device inherits its MLPP indication setting from its device pool.

- Off—This device
                                                						does not send indication of an MLPP precedence call.

- On—This device
                                                						does send indication of an MLPP precedence call.

Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful.

MLPP Preemption

If available, this setting specifies whether a device that is
                                             					 capable of preempting calls in progress will use the capability when it places
                                             					 an MLPP precedence call.

From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options:

- Default—This
                                                						device inherits its MLPP preemption setting from its device pool.

- Disabled—This
                                                						device does not preempt calls in progress when it places an MLPP precedence
                                                						call.

- Forceful—This
                                                						device preempts calls in progress when it places an MLPP precedence call.

Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful.

Logged Out (Default) Profile Information

Login User Id

From the drop-down list box, choose the user ID to be logged
                                             					 out before updating the UDP.

Assign IP Phone Services

Add All Services From This Template

From the drop-down list box, choose the template that contains
                                             					 the list of services with which you want to update the UDPs.

You can click the Edit IP Phone Service link to update the
                                             					 subscribed Cisco Unified IP Phone s services on the template.

Remove Duplicate

Check this check box to remove duplicate IP phone services. If
                                             					 you check this check box, the system removes the duplicate service
                                             					 subscriptions from phones and user device profiles. The IP system deletes
                                             					 services based on the IP service name.

Job Information

Job Description

Enter an appropriate job description.

Run Immediately

Click this radio button to schedule and activate the update
                                             					 user device profiles job immediately.

Run Later

Click this radio button to schedule and activate the update
                                             					 user device profiles job at a later time.

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Update
                                             				  UDP > Query . The Find and List User Device Profiles To Update window displays. Note You can update all user device profiles by not specifying a
                                                      				  query and clicking Find. Skip to the Choose Update Parameters . | Note | You can update all user device profiles by not specifying a
                                                      				  query and clicking Find. Skip to the Choose Update Parameters . |
|---|---|---|---|
| Note | You can update all user device profiles by not specifying a
                                                      				  query and clicking Find. Skip to the Choose Update Parameters . |
| Step 2 | From the first Find User Device Profiles where drop-down list, choose one of the following criteria: Profile Name Profile Description Profile Type Profile Protocol |
| Step 3 | From the second Find User Device Profiles where drop-down list, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable. Tip To find all user device profiles that are registered in the
                                                      				  database, click Find without entering any search text. | Tip | To find all user device profiles that are registered in the
                                                      				  database, click Find without entering any search text. |
| Tip | To find all user device profiles that are registered in the
                                                      				  database, click Find without entering any search text. |
| Step 5 | To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down list, and repeat Step 2 and Step 3 . |
| Step 6 | Click Find . The details of all the records that match the criteria display in the Find and List User Device Profiles To Update window. You can change the number of items that display on each page by choosing a different value from the Rows per Page drop-down list. |

| Note | You can update all user device profiles by not specifying a
                                                      				  query and clicking Find. Skip to the Choose Update Parameters . |
|---|---|

| Tip | To find all user device profiles that are registered in the
                                                      				  database, click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Update UDP > Custom
                                             				  File . The Find and List UDP window displays. |
|---|---|
| Step 2 | From the Update Bulk UDP where drop-down list box,
                                       			 choose the type of custom file that you have created from the following
                                       			 criteria: Profile Name Description Device Type Device Protocol |
| Step 3 | From the list of custom files, choose the filename of the custom
                                       			 file for this update. |
| Step 4 | Click Find . Note Do not use the insert or export transaction files that are
                                                      				  created with bat.xlt for the update transaction. Instead, create a custom file
                                                      				  with details of the UDP records that need to be updated. Use only this file for
                                                      				  the update transaction. In this custom update file, you do not need a header,
                                                      				  and you can enter values for profile name, description, profile type, or
                                                      				  profile protocol. | Note | Do not use the insert or export transaction files that are
                                                      				  created with bat.xlt for the update transaction. Instead, create a custom file
                                                      				  with details of the UDP records that need to be updated. Use only this file for
                                                      				  the update transaction. In this custom update file, you do not need a header,
                                                      				  and you can enter values for profile name, description, profile type, or
                                                      				  profile protocol. |
| Note | Do not use the insert or export transaction files that are
                                                      				  created with bat.xlt for the update transaction. Instead, create a custom file
                                                      				  with details of the UDP records that need to be updated. Use only this file for
                                                      				  the update transaction. In this custom update file, you do not need a header,
                                                      				  and you can enter values for profile name, description, profile type, or
                                                      				  profile protocol. |

| Note | Do not use the insert or export transaction files that are
                                                      				  created with bat.xlt for the update transaction. Instead, create a custom file
                                                      				  with details of the UDP records that need to be updated. Use only this file for
                                                      				  the update transaction. In this custom update file, you do not need a header,
                                                      				  and you can enter values for profile name, description, profile type, or
                                                      				  profile protocol. |
|---|---|

| Step 1 | Do one of the following: Click Next in the Find and List User Device Profiles To Update window if you used the Query option to locate UDPs to update. Click Next in the Find and List UDP window if you used the
                                             				  Custom File option to locate UDPs to update. The Update UDP window shows the type of query that
                                       			 you chose. If you want to change the type of query, click Back . |
|---|---|
| Step 2 | Specify the setting that you want to update for all the records
                                       			 that you have defined in your query or custom file. You can choose multiple
                                       			 parameters to update. |
| Step 3 | Update the required UDP parameters. See Table 1 for field descriptions. |
| Step 4 | Select the update check box to the left of the field that you want
                                       			 to update. This action tells BAT to overwrite the existing value for the field. Note The BAT updates only those fields for which you have selected
                                                      				  the update check box. | Note | The BAT updates only those fields for which you have selected
                                                      				  the update check box. |
| Note | The BAT updates only those fields for which you have selected
                                                      				  the update check box. |
| Step 5 | In the Job Information area, enter the job description. |
| Step 6 | Choose an activation method. Do one of the following: Click Run Immediately to schedule and activate
                                             				  user device profiles immediately. Click Run Later to schedule and activate user
                                             				  device profiles at a later time. |
| Step 7 | Click Submit to create a job for updating the
                                       			 records. Note On the Update UDPs window, certain fields may not
                                                      				  display if the search results include devices of multiple types and protocols.
                                                      				  Make sure that you have the UDPs of same type and protocol for all the fields
                                                      				  to appear. | Note | On the Update UDPs window, certain fields may not
                                                      				  display if the search results include devices of multiple types and protocols.
                                                      				  Make sure that you have the UDPs of same type and protocol for all the fields
                                                      				  to appear. |
| Note | On the Update UDPs window, certain fields may not
                                                      				  display if the search results include devices of multiple types and protocols.
                                                      				  Make sure that you have the UDPs of same type and protocol for all the fields
                                                      				  to appear. |

| Note | The BAT updates only those fields for which you have selected
                                                      				  the update check box. |
|---|---|

| Note | On the Update UDPs window, certain fields may not
                                                      				  display if the search results include devices of multiple types and protocols.
                                                      				  Make sure that you have the UDPs of same type and protocol for all the fields
                                                      				  to appear. |
|---|---|

| Field | Description |
|---|---|
| Description | Enter a description that makes the device easy to recognize.
                                             					 The description can include up to 50 characters in any language, but it cannot
                                             					 include double-quotes ("), percentage sign
                                             					 (%), ampersand (&), backslash
                                             					 (\), or angle brackets (<>). |
| User Hold MOH Audio Source | Choose the audio source for this group of UDPs or ports. The user hold audio source plays music when the user puts a
                                             					 call on hold. |
| User Locale | Choose the country and language set that you want to associate
                                             					 with this user. This choice determines which culture-dependent attributes
                                             					 exist for this user and which language displays for the user in the Cisco Unified Communications Manager user windows and phones. |
| Phone Button Template | Choose an appropriate phone button template for this profile. The phone button template determines the configuration of
                                             					 buttons on a phone and identifies which feature (line, speed dial, and so on)
                                             					 is used for each button. |
| Softkey Template | Choose the softkey template to be used for all UDPs in this
                                             					 group. |
| Privacy | Choose the appropriate privacy option for the profile from the
                                             					 drop-down list box: Off—Enables
                                                						privacy for each device. On—Disables
                                                						privacy for each device. Default—Applies
                                                						the default privacy settings to the device. |
| SUBSCRIBE Calling Search Space | Used with the Presence feature, the SUBSCRIBE Calling Search
                                             					 Space determines how Cisco Unified Communications Manager routes the subscription requests that come
                                             					 from the phone. From the drop-down list box, choose the calling search space
                                             					 that you want to use for this purpose. |
| Presence Group | From the drop-down list box, choose a presence group for this
                                             					 group of UDPs. The selected group specifies the devices, end users, and
                                             					 application users that can monitor this directory number. |
| Single Button Barge | From the drop-down list box, enable or disable the Single
                                             					 Button Barge/cBarge feature for this device or choose Default to use the
                                             					 service parameter setting. Off—This setting
                                                						disables the Single Button Barge/cBarge feature; however, the regular Barge or
                                                						cBarge features will still work. Barge—This setting
                                                						enables the Singe Button Barge feature. cBarge—This
                                                						setting enables the Single Button cBarge feature. Default—This
                                                						setting uses the Single Button Barge/cBarge setting that the service parameter
                                                						specifies. |
| Join Across Lines | From the drop-down list box, enable or disable the Join Across
                                             					 Lines feature for this device or choose Default to use the service parameter
                                             					 setting. Off—This setting
                                                						disables the Join Across Lines feature. On—This setting
                                                						enables the Join Across Lines feature. Default—This
                                                						setting uses the Join Across Lines setting that the service parameter
                                                						specifies. |
| Always Use Prime Line | From the drop-down list box, choose the Always Use Prime Line
                                             					 setting that you want to use from the following values: On Off Default |
| Always Use Prime Line for Voice Message | From the drop-down list box, choose the Always Use Prime Line
                                             					 for Voice Message setting that you want to use from the following values: On Off Default |
| Feature Control Policy | From the drop-down list box, choose the Feature Control Policy
                                             					 for this group of UDPs. A feature control policy specifies the appearance of features
                                             					 and the associated softkeys that display on the UDP. |
| Ignore Presentation Indicators (internal calls only) | Check this check box if the system must ignore presentation
                                             					 indicators. |
| Do Not Disturb | If you want to enable the DND feature, check this check box. |
| DND Option | From the drop-down list box, choose a DND option from the
                                             					 following options: None Ringer Off Call Reject Use Common Phone
                                                						Profile Setting |
| DND Incoming Call Alert | From the drop-down list box, choose one of the following
                                             					 options: None Disable Flash Only Beep Only |
| Extension Mobility Cross Cluster CSS | From the drop-down list box, choose the appropriate setting
                                             					 for this group of UDPs. The Extension Mobility Cross Cluster CSS setting gets used as
                                             					 the device CSS of the remote phone when the user selects this device profile
                                             					 during EMCC login. |
| Multilevel Precedence and Preemption (MLPP)
                                                						Information |
| MLPP Domain | Enter a hexadecimal value for the MLPP domain that is
                                             					 associated with this device. Ensure that this value specifies blank or a value
                                             					 between 0 and FFFFFF. |
| MLPP Indication | If available, this setting specifies whether a device that is
                                             					 capable of playing precedence tones will use the capability when it places an
                                             					 MLPP precedence call. From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options: Default—This
                                                						device inherits its MLPP indication setting from its device pool. Off—This device
                                                						does not send indication of an MLPP precedence call. On—This device
                                                						does send indication of an MLPP precedence call. Note Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. | Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. |
| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. |
| MLPP Preemption | If available, this setting specifies whether a device that is
                                             					 capable of preempting calls in progress will use the capability when it places
                                             					 an MLPP precedence call. From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options: Default—This
                                                						device inherits its MLPP preemption setting from its device pool. Disabled—This
                                                						device does not preempt calls in progress when it places an MLPP precedence
                                                						call. Forceful—This
                                                						device preempts calls in progress when it places an MLPP precedence call. Note Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. | Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. |
| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. |
| Logged Out (Default) Profile Information |
| Login User Id | From the drop-down list box, choose the user ID to be logged
                                             					 out before updating the UDP. |
| Assign IP Phone Services |
| Add All Services From This Template | From the drop-down list box, choose the template that contains
                                             					 the list of services with which you want to update the UDPs. You can click the Edit IP Phone Service link to update the
                                             					 subscribed Cisco Unified IP Phone s services on the template. |
| Remove Duplicate | Check this check box to remove duplicate IP phone services. If
                                             					 you check this check box, the system removes the duplicate service
                                             					 subscriptions from phones and user device profiles. The IP system deletes
                                             					 services based on the IP service name. |
| Job Information |
| Job Description | Enter an appropriate job description. |
| Run Immediately | Click this radio button to schedule and activate the update
                                             					 user device profiles job immediately. |
| Run Later | Click this radio button to schedule and activate the update
                                             					 user device profiles job at a later time. |

| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. |
|---|---|

| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off while MLPP Preemption is set to
                                                         						Forceful. |
|---|---|