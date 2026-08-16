---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--87214dc33c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0110010.html
retrieved_at: 2026-08-16T16:38:36.954505+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Emergency Call Handler

## Chapter: Emergency Call Handler

# Emergency Call Handler

## Emergency Call Handler Overview

Emergency Call Handler helps you to manage emergency calls in your telephony network while following local ordinances and
                              regulations.

When an emergency call is made the following is required:

The emergency call must be routed to the local Public-Safety Answering Point (PSAP) based on the location of the caller.

The caller's location information must be displayed at the emergency operator terminal. The location information can be obtained
                                    from an Automatic Location Information (ALI) database.

The caller's location is determined by the Emergency Location Identification Number (ELIN). An ELIN is a Direct Inward Dial
                              (DID) number that the PSAP can dial to reconnect to the emergency caller if the emergency call is cut off or if the PSAP needs
                              to talk to the caller again. The emergency call is routed to the PSAP based on the location information that is associated
                              with this number.

For multiline phone systems, such as an office system, the ELIN can be associated with more than one telephone by grouping
                              the phones in an ELIN  group. An ELIN group in Emergency Call Handler identifies a location. The ELINs under this ELIN group
                              must be mapped to the location in the ALI database.

Each location should have as many ELINs created as needed to support simultaneous emergency calls. For example, to support
                              five simultaneous calls, five ELINs would be needed in an ELIN group.

Emergency Call Handler supports a maximum of 100 ELINs per cluster.

Make sure that the mapping of ELIN to the original called party is active until the ELIN is used for the next emergency call
                                          from the same location. If the ELIN mapping is not used, the DN will be active for a maximum period of 3 hours only.

The following types of phone are supported to use ELIN groups:

SIP and SCCP IP phones

CTI ports

MGCP and SCCP analog phones

H.323 phones

## Emergency Call Handler Prerequisites

### Example

Before deploying Emergency Call Handler in your network, we recommend that you test the ALI submission process. With your
                              service provider's help, test that the PSAP can successfully call back into your network using the ALI data.

Reserve the ELIN number from your local PSAP.  Ordinances and regulations can differ across different locations and across
                              different companies, so research your security and legal needs before deploying this feature.

## Emergency Call
                        	 Handler Task Flow

### Before you begin

Review Emergency Call Handler Prerequisites

Step 1

Enable Emergency Call Handler

Enable the Emergency Call
                                          				Handler feature on Cisco Unified Communications Manager. Emergency Call Handler
                                          				provides essential emergency call features and supports a limited number of
                                          				locations with phone location assignment by static configuration. If you
                                          				require advanced emergency call features, such as a greater amount of specific
                                          				locations or dynamic location assignment, consider Cisco Emergency Responder.

Step 2

Configure Emergency Location Groups

Configure an Emergency
                                          				Location (ELIN) Group for a particular site or location.

Step 3

Add a Device Pool to an Emergency Location Group

Configure device pools to
                                          				use an Emergency Location (ELIN) Group.

Step 4

(Optional) Add Device to an Emergency Location Group

Configure a particular
                                          				device to use a particular Emergency Location (ELIN) Group. If you want to use
                                          				the device pool ELIN Group that is associated for this device, you can ignore
                                          				this section.

Configurations that are made at the device level will overwrite
                                                      				  any configurations that were made at the device pool level.

Step 5

Enable Route Patterns and Translation Patterns

Enable the Emergency
                                          				Location (ELIN) service for a route pattern or a translation pattern.

Caution

No Calling
                                                      				  Party Transformation masks are set at the Gateway or Trunk, because these may
                                                      				  transform the ELIN that is set by Emergency Call Handler.

It is
                                                      				  mandatory that you enable either route patterns or translation patterns, but it
                                                      				  is possible to enable both.

Step 6

(Optional) Use
                                       			 the following procedures to perform bulk administration tasks on ELIN group
                                       			 information and phones:

- Import Emergency Location Group Information

- Export Emergency Location Group Information

- Update Phones with a new Emergency Location Group

This section provides
                                          				information about the Bulk Administration tasks you can use to update ELIN
                                          				group information and to add phones to new ELIN groups. For Bulk
                                          				Administration, see the Cisco
                                             				  Unified Communications Manager Bulk Administration Guide, Release
                                             				  11.0(1) .

### Enable Emergency Call Handler

Enable the Emergency Call
                                 				Handler feature on Cisco Unified Communications Manager. Emergency Call Handler
                                 				provides essential emergency call features and supports a limited number of
                                 				locations with phone location assignment by static configuration. If you
                                 				require advanced emergency call features, such as a greater amount of specific
                                 				locations or dynamic location assignment, consider Cisco Emergency Responder.

Do not enable this feature if you are already using an external emergency calling solution such as Cisco Emergency Responder.

If you decide to enable this feature, make sure you disable the external one.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Emergency Call Handler > Emergency Location Configuration .

Step 2

From the Emergency Location Configuration window:

- To enable the Emergency Call Handler feature, check the Enable Emergency Location (ELIN) Support check box. The setting default is Disabled.  When enabled, the settings related to this feature appear in the Related Settings
                                             pane. You must configure these settings for the feature to work. Refer to the tasks below for further details on how to configure
                                             these related settings.

If you disable this feature, all related settings that are configured will be removed. See the Related Settings Pane for all
                                                            configured settings.

If you 	want to disable the feature and you have more than 500 devices associated with ELIN Groups, then you must manually
                                                            delete the associations until there are fewer than 500 associations before you can disable the feature.

Step 3

Click Save .

### Configure Emergency Location Groups

Configure an Emergency
                                 				Location (ELIN) Group for a particular site or location.

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose Call Routing > Emergency Call Handler > Emergency Location (ELIN) Group .

Step 2

In the Emergency Location (ELIN) Group Configuration window,  enter a name  for the group in the Name field.

Step 3

In the Number field, enter the pool of DID numbers that are registered in the Public Safety Answering Point (PSAP).

Step 4

Click Save .

### Add a Device Pool to an Emergency Location Group

Configure device pools to
                                 				use an Emergency Location (ELIN) Group.

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose System > Device Pool .

Step 2

In the Find and List Device Pools window, if you are adding an existing device pool, click Find and choose the device pool from the list. If you are adding a new device pool click Add New .

Step 3

In the Device Pool Configuration window, choose the ELIN group to which you want to add the device pool from the Emergency Location (ELIN) Group drop-down list. If you are adding a new device pool, fill out any other required fields.

Step 4

Click Save .

### Add Device to an Emergency Location Group

Configure a particular
                                 				device to use a particular Emergency Location (ELIN) Group. If you want to use
                                 				the device pool ELIN Group that is associated for this device, you can ignore
                                 				this section.

Configurations that are made at the device level will overwrite
                                             				  any configurations that were made at the device pool level.

The devices that you add to the ELIN Group, should be added to the ELIN Group that represents the particular location at which
                                             those devices are located.

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

If you are using a type of phone that is not an IP phone, go to the relevant configuration page for that type of phone.

Step 2

In the Find and List Phones window,  if you are adding an existing device, click Find and choose the device you want to configure from the list. If you are adding a new device, click Add New .

Step 3

If you are adding a new phone, choose the type of phone you want to add from the Phone Type drop-down list and click Next .

Step 4

In the Phone Configuration window, choose the ELIN group to which you want to add the device from the Emergency Location (ELIN) Group drop-down list. If you are adding a new device, fill out any other required fields.

Step 5

Click Save .

### Enable Route Patterns and Translation Patterns

Enable the Emergency
                                 				Location (ELIN) service for a route pattern or a translation pattern.

It is
                                             				  mandatory that you enable either route patterns or translation patterns, but it
                                             				  is possible to enable both.

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose one of the following:

- To enable  a route pattern, choose Call Routing > Route/Hunt > Route Pattern .

- To enable a translation pattern, choose Call Routing > Translation Pattern .

Step 2

In the Find and List Route Patterns or Find and List Translation Patterns window, click Find and choose a route pattern or translation pattern from the list.

Step 3

In the Route Pattern Configuration or Translation Pattern Configuration window, check the Is an Emergency Services Number check box.

Check this check box only if you are using Emergency Call Handler and not another external emergency calling solution such
                                                         as Cisco Emergency Responder.

Step 4

Click Save .

### Bulk Administration of Emergency Location Groups and Phones

Bulk Administration of Emergency Location Groups and Phones Task Flow

#### Bulk Administration of Emergency Location Groups and Phones Task Flow

This section provides information about the Bulk Administration tasks you can use to update ELIN group information and to
                                    add phones to new ELIN groups. For more information about Bulk Administration, see the Cisco Unified Communications Manager Bulk Administration Guide, Release 11.0(1) .

Before you perform these procedures, make sure that you have enable the Emergency Call Handler feature. See Enable Emergency Call Handler .

Step 1

Import Emergency Location Group Information

Import Emergency Location (ELIN) Group information using the Bulk Administration Tool.

Step 2

Export Emergency Location Group Information

Export Emergency Location (ELIN) Group information using the Bulk Administration Tool.

Step 3

Update Phones with a new Emergency Location Group

Find and list multiple phones and configure them with a new Emergency Location (ELIN) Group.

##### Import Emergency
                                 	 Location Group Information

Import Emergency Location (ELIN) Group information using the Bulk Administration Tool.

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Import/Export > Import .

Step 2

From the File
                                                   				Name drop-down list, choose the name of the .tar file you want to
                                                			 import, and click Next .

Step 3

The Import
                                                   				Configuration section lists all the components of the .tar file.
                                                			 Check the ELIN Group-related check boxes for the options that you want to
                                                			 import.

Step 4

Choose to run
                                                			 the job immediately or later by clicking the corresponding radio button.

Step 5

To create a
                                                			 job for importing the selected data, click Submit . A message in the Status section notifies you
                                                			 know that the job was submitted successfully.

Step 6

Use the Job
                                                			 Scheduler option in the Bulk Administration main menu to schedule or activate
                                                			 this job.

##### Export Emergency
                                 	 Location Group Information

Export Emergency Location (ELIN) Group information using the Bulk Administration Tool.

###### Before you begin

Import Emergency Location Group Information

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Import/Export > Export .

Step 2

In the Export
                                                   				Data window, in the Job
                                                   				Information pane, enter the .tar file name, without the extension,
                                                			 in the Tar
                                                   				File Name field. BPS uses this filename to export the configuration
                                                			 details.

All files
                                                               				  that are exported at the same time get bundled together (.tar) and can be
                                                               				  downloaded from the server.

Step 3

To export ELIN
                                                			 Group information, check the Elin
                                                   				Group check box on the Select
                                                   				items to Export pane.

Step 4

(Optional) Perform these steps:

- To export device pools with ELIN Groups configured, check the Device Pools check box.

- To export phones with ELIN Groups configured, check the Phone check box.

Step 5

In the Job
                                                   				Descripton field, enter the description that you want to override
                                                			 for the job. Export Configuration is the default description.

Step 6

You can choose
                                                			 to run the job immediately or later by clicking the corresponding radio button.

Step 7

To create a
                                                			 job for exporting the selected data, click Submit . A message in the Status pane notifies you that the job was submitted
                                                			 successfully.

Step 8

Use the Job
                                                			 Scheduler option in the Bulk Administration main menu to schedule or activate
                                                			 this job.

##### Update Phones with
                                 	 a new Emergency Location Group

Find and list multiple phones and configure them with a new Emergency Location (ELIN) Group.

###### Before you begin

Export Emergency Location Group Information

Step 1

From Cisco
                                                			 Unified CM Administration, choose Bulk
                                                      				  Administration > Phones > Update
                                                      				  Phone > Query .

Step 2

In the Find
                                                   				and List Phones To Update window, set the parameters for your
                                                			 search and click Find .

To update
                                                               				  all phones, click Find and do not specify a query.

Step 3

The Find
                                                   				and List Phones To Update window displays the details of the phones
                                                			 that you chose. Click Next .

Step 4

In the Update
                                                   				Phones window, check the Emergency Location (ELIN) Group check box, and
                                                			 choose a new ELIN Group from the drop-down list.

Step 5

Click Submit .

## Interactions

Feature

Interaction

Do Not Disturb Call Reject

Calls made by PSAP CallBack will overwrite a  Do Not Disturb (DND) configuration of a destination device.

If DND Call Reject is enabled, when the emergency number is dialed using the translation pattern, an ELIN will be associated
                                          for this outbound emergency call. If the call is disconnected  and the ELIN is called back using PSAP CallBack, the call is
                                          routed to the phone irrespective of the phone's DND settings.

Call Forward All

Calls made by PSAP CallBack will overwrite Call Forward All (CFA) settings of the destination device.

If a phone has CFA enabled and if the emergency number using the translation pattern is dialed, an ELIN  will be associated
                                          for this outbound emergency call. If the call is disconnected and the ELIN is called back using PSAP CallBack, the call is
                                          routed to the phone irrespective of the phone's CFA settings.

Single Number Reach

PSAP CallBack will ignore the Single Number Reach (SNR) configuration.

When a phone has SNR enabled with the Remote Destination pointing to a mobile number. If the emergency number is dialed  using
                                          the translation pattern, an ELIN will be associated for this outbound emergency call. If the call is disconnected, and the
                                          ELIN number is called back using PSAP CallBack, the call is routed to the phone and not to the remote destination.

Extension Mobility

PSAP CallBack call will consider Extension Mobility (EM) status.

If you log in with EM profile credentials and dial the emergency number using the translation pattern, an ELIN will be associated
                                          for this outbound emergency call. If the call is disconnected and the ELIN  where the user is still logged in is called back
                                          using PSAP CallBack, the call is routed to the device which initiated the call.

This is the device on which the user is still logged in.

PSAP CallBack will fail if a user logs out of EM before a PSAP CallBack is performed.

When a user logs in with  EM profile credentials, and the emergency number is dialed using the translation pattern, an ELIN
                                          will be associated for this outbound emergency call. If the call is disconnected and is called back  using PSAP CallBack,
                                          if the user has since logged out, the call will not route to the device that initiated the call and will fail.

PSAP CallBack with a user logged in on a different device.

When a user logs in with EM profile credentials at Phone A and dials the emergency number using the translation pattern, an
                                          ELIN will be associated for this outbound emergency call. If the call is disconnected, the user should log out from Phone
                                          A. If the user then logs in to another phone, Phone B, with the same profile, and  the ELIN is called back using PSAP CallBack,
                                          the call is then be routed to Phone B with normal priority, meaning  CFA settings will be ignored and DND settings will not
                                          be ignored.

PSAP CallBack call with multiple logins.

When a user logs in with EM profile credentials at Phone A and dials the emergency number using the translation pattern, an
                                          ELIN number will be associated for this outbound emergency call. If the call is disconnected and the user logs in to another
                                          phone, Phone B, with the same profile while the user is still logged in on Phone A, and the ELIN is called back using PSAP
                                          CallBack, then the call is routed to Phone A only, the device on which the call originated.

Device Mobility

A roaming device will use the Roaming Device Pool's ELIN Group for an outbound emergency call.

Move a device with Device Mobility enabled from its home location to the Roaming location, a change in IP subnet, so that
                                          it gets associated with the Roaming device pool. If the emergency number is dialed using the translation pattern, an ELIN
                                          is associated for this outbound emergency call. The ELIN belongs to the ELIN Group that is associated with the Roaming Device
                                          Pool.

Shared Lines

PSAP CallBack rings only on the device which made the emergency call even if the line is shared by different devices.

Phone A and Phone B share a Directory Number (DN). If the emergency number is dialed using the translation pattern, an ELIN
                                          is associated for this outbound emergency call. If the call is disconnected, and the ELIN is called back using PSAP CallBack,
                                          the call is routed to Phone A only, the device from which the call originated.

## Emergency Call Handler Troubleshooting

### About Emergency Call Handler Troubleshooting Scenarios

This section provides information about some Emergency Call Handler troubleshooting scenarios in the following areas:

Configuration Scenarios

Outgoing Calls Scenarios

Incoming Calls Scenarios

Configuration Scenarios

### Emergency Calls Get Busy Signals and Are Not Routed

Problem:

Emergency calls get busy signals and are not routed.

Solution:

If a user who is dialing the emergency call is running a reorder tone, perform the following checks:

Check whether the translation or route pattern for the emergency call has been used. This may require checking for the device
                                       or phone on CSS.

Check whether the Is an Emergency Services Number check box has been checked for the translation or route pattern of the emergency call, and that it is correctly routing to
                                       the gateway.

If the user who is dialing the emergency call is not reaching the correct gateway or Public Service Answering Point (PSAP),
                                 check that the settings or device pool settings for the phone or device are configured with the correct Emergency Location
                                 (ELIN) Group.

### Emergency Location Numbers Are Dialed from Outside Running a Reorder Tone

Problem:

Emergency Location (ELIN) numbers are dialed from outside while running a reorder tone.

Cause:

In this case the ELINs have been set as DID which is  used to identify  a caller's location. This should not be used on any
                                 phone or for any other purpose.

Solution:

Check the ELIN configuration information, and unset the ELINs that have been set as DID.

Outgoing Calls Scenarios

### Outgoing Emergency Call Does Not Contain Calling Party as Emergency Location Number

Problem:

An outgoing emergency call does not contain the calling party as an Emergency Location (ELIN) number.

Cause:

The translation pattern or route pattern for this ELIN was not configured correctly.

Solution:

Check that the translation pattern or route pattern settings are correctly configured for this ELIN, and make sure that the Is an Emergency Services number check box is checked on the relevant translation pattern or route pattern configuration page.

### Outgoing Emergency Call Contains Modified Emergency Location Number

Problem:

An outgoing emergency call contains a modified  Emergency Location (ELIN) number.

Cause:

The outgoing trunk or route list contains extra transformations that are not required for ELINs.

Solution:

Check the transformations that were applied for the call, and make sure that  only the required transformations for ELINs
                                 are present on the outgoing trunk or route list.

Incoming Calls Scenarios

### Incoming PSAP Callback Call Fails

Problem:

An incoming PSAP Callback call fails.

Cause:

The device that made the original emergency call was not registered correctly.

Solution:

Check whether the device that made the original emergency call is still registered and whether any Extension Mobility is
                                 involved.

### Incoming PSAP CallBack Call is Not Routed as Expected

Problem:

An incoming PSAP CallBack call does not get routed as expected.

Cause:

The Emergency Location (ELIN) number does not match the number of the original dialed party.

Solution:

For an ELIN to be successfully reverse mapped to the original dialed party, these two numbers must match. If there are already
                                 transformations at the incoming Gateway or Trunk and significant digits configured, make sure that the final transformed called
                                 party matches the ELIN number.

| Note | Emergency Call Handler supports a maximum of 100 ELINs per cluster. Make sure that the mapping of ELIN to the original called party is active until the ELIN is used for the next emergency call
                                          from the same location. If the ELIN mapping is not used, the DN will be active for a maximum period of 3 hours only. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Emergency Call Handler | Enable the Emergency Call
                                          				Handler feature on Cisco Unified Communications Manager. Emergency Call Handler
                                          				provides essential emergency call features and supports a limited number of
                                          				locations with phone location assignment by static configuration. If you
                                          				require advanced emergency call features, such as a greater amount of specific
                                          				locations or dynamic location assignment, consider Cisco Emergency Responder. |
| Step 2 | Configure Emergency Location Groups | Configure an Emergency
                                          				Location (ELIN) Group for a particular site or location. |
| Step 3 | Add a Device Pool to an Emergency Location Group | Configure device pools to
                                          				use an Emergency Location (ELIN) Group. |
| Step 4 | (Optional) Add Device to an Emergency Location Group | Configure a particular
                                          				device to use a particular Emergency Location (ELIN) Group. If you want to use
                                          				the device pool ELIN Group that is associated for this device, you can ignore
                                          				this section. Note Configurations that are made at the device level will overwrite
                                                      				  any configurations that were made at the device pool level. | Note | Configurations that are made at the device level will overwrite
                                                      				  any configurations that were made at the device pool level. |
| Note | Configurations that are made at the device level will overwrite
                                                      				  any configurations that were made at the device pool level. |
| Step 5 | Enable Route Patterns and Translation Patterns | Enable the Emergency
                                          				Location (ELIN) service for a route pattern or a translation pattern. Caution No Calling
                                                      				  Party Transformation masks are set at the Gateway or Trunk, because these may
                                                      				  transform the ELIN that is set by Emergency Call Handler. Note It is
                                                      				  mandatory that you enable either route patterns or translation patterns, but it
                                                      				  is possible to enable both. | Caution | No Calling
                                                      				  Party Transformation masks are set at the Gateway or Trunk, because these may
                                                      				  transform the ELIN that is set by Emergency Call Handler. | Note | It is
                                                      				  mandatory that you enable either route patterns or translation patterns, but it
                                                      				  is possible to enable both. |
| Caution | No Calling
                                                      				  Party Transformation masks are set at the Gateway or Trunk, because these may
                                                      				  transform the ELIN that is set by Emergency Call Handler. |
| Note | It is
                                                      				  mandatory that you enable either route patterns or translation patterns, but it
                                                      				  is possible to enable both. |
| Step 6 | (Optional) Use
                                       			 the following procedures to perform bulk administration tasks on ELIN group
                                       			 information and phones: Import Emergency Location Group Information Export Emergency Location Group Information Update Phones with a new Emergency Location Group | This section provides
                                          				information about the Bulk Administration tasks you can use to update ELIN
                                          				group information and to add phones to new ELIN groups. For Bulk
                                          				Administration, see the Cisco
                                             				  Unified Communications Manager Bulk Administration Guide, Release
                                             				  11.0(1) . |

| Note | Configurations that are made at the device level will overwrite
                                                      				  any configurations that were made at the device pool level. |
|---|---|

| Caution | No Calling
                                                      				  Party Transformation masks are set at the Gateway or Trunk, because these may
                                                      				  transform the ELIN that is set by Emergency Call Handler. |
|---|---|

| Note | It is
                                                      				  mandatory that you enable either route patterns or translation patterns, but it
                                                      				  is possible to enable both. |
|---|---|

| Note | Do not enable this feature if you are already using an external emergency calling solution such as Cisco Emergency Responder. If you decide to enable this feature, make sure you disable the external one. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Emergency Call Handler > Emergency Location Configuration . |
|---|---|
| Step 2 | From the Emergency Location Configuration window: To enable the Emergency Call Handler feature, check the Enable Emergency Location (ELIN) Support check box. The setting default is Disabled.  When enabled, the settings related to this feature appear in the Related Settings
                                             pane. You must configure these settings for the feature to work. Refer to the tasks below for further details on how to configure
                                             these related settings. To disable the Emergency Call Handler feature, uncheck the Enable Emergency Location (ELIN) Support check box. Note If you disable this feature, all related settings that are configured will be removed. See the Related Settings Pane for all
                                                            configured settings. Note If you 	want to disable the feature and you have more than 500 devices associated with ELIN Groups, then you must manually
                                                            delete the associations until there are fewer than 500 associations before you can disable the feature. | Note | If you disable this feature, all related settings that are configured will be removed. See the Related Settings Pane for all
                                                            configured settings. | Note | If you 	want to disable the feature and you have more than 500 devices associated with ELIN Groups, then you must manually
                                                            delete the associations until there are fewer than 500 associations before you can disable the feature. |
| Note | If you disable this feature, all related settings that are configured will be removed. See the Related Settings Pane for all
                                                            configured settings. |
| Note | If you 	want to disable the feature and you have more than 500 devices associated with ELIN Groups, then you must manually
                                                            delete the associations until there are fewer than 500 associations before you can disable the feature. |
| Step 3 | Click Save . |

| Note | If you disable this feature, all related settings that are configured will be removed. See the Related Settings Pane for all
                                                            configured settings. |
|---|---|

| Note | If you 	want to disable the feature and you have more than 500 devices associated with ELIN Groups, then you must manually
                                                            delete the associations until there are fewer than 500 associations before you can disable the feature. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Emergency Call Handler > Emergency Location (ELIN) Group . |
|---|---|
| Step 2 | In the Emergency Location (ELIN) Group Configuration window,  enter a name  for the group in the Name field. |
| Step 3 | In the Number field, enter the pool of DID numbers that are registered in the Public Safety Answering Point (PSAP). |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Device Pool . |
|---|---|
| Step 2 | In the Find and List Device Pools window, if you are adding an existing device pool, click Find and choose the device pool from the list. If you are adding a new device pool click Add New . |
| Step 3 | In the Device Pool Configuration window, choose the ELIN group to which you want to add the device pool from the Emergency Location (ELIN) Group drop-down list. If you are adding a new device pool, fill out any other required fields. |
| Step 4 | Click Save . |

| Note | Configurations that are made at the device level will overwrite
                                             				  any configurations that were made at the device pool level. |
|---|---|

| Note | The devices that you add to the ELIN Group, should be added to the ELIN Group that represents the particular location at which
                                             those devices are located. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . Note If you are using a type of phone that is not an IP phone, go to the relevant configuration page for that type of phone. | Note | If you are using a type of phone that is not an IP phone, go to the relevant configuration page for that type of phone. |
|---|---|---|---|
| Note | If you are using a type of phone that is not an IP phone, go to the relevant configuration page for that type of phone. |
| Step 2 | In the Find and List Phones window,  if you are adding an existing device, click Find and choose the device you want to configure from the list. If you are adding a new device, click Add New . |
| Step 3 | If you are adding a new phone, choose the type of phone you want to add from the Phone Type drop-down list and click Next . |
| Step 4 | In the Phone Configuration window, choose the ELIN group to which you want to add the device from the Emergency Location (ELIN) Group drop-down list. If you are adding a new device, fill out any other required fields. |
| Step 5 | Click Save . |

| Note | If you are using a type of phone that is not an IP phone, go to the relevant configuration page for that type of phone. |
|---|---|

| Note | It is
                                             				  mandatory that you enable either route patterns or translation patterns, but it
                                             				  is possible to enable both. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose one of the following: To enable  a route pattern, choose Call Routing > Route/Hunt > Route Pattern . To enable a translation pattern, choose Call Routing > Translation Pattern . |
|---|---|
| Step 2 | In the Find and List Route Patterns or Find and List Translation Patterns window, click Find and choose a route pattern or translation pattern from the list. |
| Step 3 | In the Route Pattern Configuration or Translation Pattern Configuration window, check the Is an Emergency Services Number check box. Note Check this check box only if you are using Emergency Call Handler and not another external emergency calling solution such
                                                         as Cisco Emergency Responder. | Note | Check this check box only if you are using Emergency Call Handler and not another external emergency calling solution such
                                                         as Cisco Emergency Responder. |
| Note | Check this check box only if you are using Emergency Call Handler and not another external emergency calling solution such
                                                         as Cisco Emergency Responder. |
| Step 4 | Click Save . |

| Note | Check this check box only if you are using Emergency Call Handler and not another external emergency calling solution such
                                                         as Cisco Emergency Responder. |
|---|---|

| Note | Before you perform these procedures, make sure that you have enable the Emergency Call Handler feature. See Enable Emergency Call Handler . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Import Emergency Location Group Information | Import Emergency Location (ELIN) Group information using the Bulk Administration Tool. |
| Step 2 | Export Emergency Location Group Information | Export Emergency Location (ELIN) Group information using the Bulk Administration Tool. |
| Step 3 | Update Phones with a new Emergency Location Group | Find and list multiple phones and configure them with a new Emergency Location (ELIN) Group. |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Import/Export > Import . |
|---|---|
| Step 2 | From the File
                                                   				Name drop-down list, choose the name of the .tar file you want to
                                                			 import, and click Next . |
| Step 3 | The Import
                                                   				Configuration section lists all the components of the .tar file.
                                                			 Check the ELIN Group-related check boxes for the options that you want to
                                                			 import. |
| Step 4 | Choose to run
                                                			 the job immediately or later by clicking the corresponding radio button. |
| Step 5 | To create a
                                                			 job for importing the selected data, click Submit . A message in the Status section notifies you
                                                			 know that the job was submitted successfully. |
| Step 6 | Use the Job
                                                			 Scheduler option in the Bulk Administration main menu to schedule or activate
                                                			 this job. |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Import/Export > Export . |
|---|---|
| Step 2 | In the Export
                                                   				Data window, in the Job
                                                   				Information pane, enter the .tar file name, without the extension,
                                                			 in the Tar
                                                   				File Name field. BPS uses this filename to export the configuration
                                                			 details. Note All files
                                                               				  that are exported at the same time get bundled together (.tar) and can be
                                                               				  downloaded from the server. | Note | All files
                                                               				  that are exported at the same time get bundled together (.tar) and can be
                                                               				  downloaded from the server. |
| Note | All files
                                                               				  that are exported at the same time get bundled together (.tar) and can be
                                                               				  downloaded from the server. |
| Step 3 | To export ELIN
                                                			 Group information, check the Elin
                                                   				Group check box on the Select
                                                   				items to Export pane. |
| Step 4 | (Optional) Perform these steps: To export device pools with ELIN Groups configured, check the Device Pools check box. To export phones with ELIN Groups configured, check the Phone check box. |
| Step 5 | In the Job
                                                   				Descripton field, enter the description that you want to override
                                                			 for the job. Export Configuration is the default description. |
| Step 6 | You can choose
                                                			 to run the job immediately or later by clicking the corresponding radio button. |
| Step 7 | To create a
                                                			 job for exporting the selected data, click Submit . A message in the Status pane notifies you that the job was submitted
                                                			 successfully. |
| Step 8 | Use the Job
                                                			 Scheduler option in the Bulk Administration main menu to schedule or activate
                                                			 this job. |

| Note | All files
                                                               				  that are exported at the same time get bundled together (.tar) and can be
                                                               				  downloaded from the server. |
|---|---|

| Step 1 | From Cisco
                                                			 Unified CM Administration, choose Bulk
                                                      				  Administration > Phones > Update
                                                      				  Phone > Query . |
|---|---|
| Step 2 | In the Find
                                                   				and List Phones To Update window, set the parameters for your
                                                			 search and click Find . Note To update
                                                               				  all phones, click Find and do not specify a query. | Note | To update
                                                               				  all phones, click Find and do not specify a query. |
| Note | To update
                                                               				  all phones, click Find and do not specify a query. |
| Step 3 | The Find
                                                   				and List Phones To Update window displays the details of the phones
                                                			 that you chose. Click Next . |
| Step 4 | In the Update
                                                   				Phones window, check the Emergency Location (ELIN) Group check box, and
                                                			 choose a new ELIN Group from the drop-down list. |
| Step 5 | Click Submit . |

| Note | To update
                                                               				  all phones, click Find and do not specify a query. |
|---|---|

| Feature | Interaction |
|---|---|
| Do Not Disturb Call Reject | Calls made by PSAP CallBack will overwrite a  Do Not Disturb (DND) configuration of a destination device. If DND Call Reject is enabled, when the emergency number is dialed using the translation pattern, an ELIN will be associated
                                          for this outbound emergency call. If the call is disconnected  and the ELIN is called back using PSAP CallBack, the call is
                                          routed to the phone irrespective of the phone's DND settings. |
| Call Forward All | Calls made by PSAP CallBack will overwrite Call Forward All (CFA) settings of the destination device. If a phone has CFA enabled and if the emergency number using the translation pattern is dialed, an ELIN  will be associated
                                          for this outbound emergency call. If the call is disconnected and the ELIN is called back using PSAP CallBack, the call is
                                          routed to the phone irrespective of the phone's CFA settings. |
| Single Number Reach | PSAP CallBack will ignore the Single Number Reach (SNR) configuration. When a phone has SNR enabled with the Remote Destination pointing to a mobile number. If the emergency number is dialed  using
                                          the translation pattern, an ELIN will be associated for this outbound emergency call. If the call is disconnected, and the
                                          ELIN number is called back using PSAP CallBack, the call is routed to the phone and not to the remote destination. |
| Extension Mobility | PSAP CallBack call will consider Extension Mobility (EM) status. If you log in with EM profile credentials and dial the emergency number using the translation pattern, an ELIN will be associated
                                          for this outbound emergency call. If the call is disconnected and the ELIN  where the user is still logged in is called back
                                          using PSAP CallBack, the call is routed to the device which initiated the call. Note This is the device on which the user is still logged in. | Note | This is the device on which the user is still logged in. |
| Note | This is the device on which the user is still logged in. |
| PSAP CallBack will fail if a user logs out of EM before a PSAP CallBack is performed. When a user logs in with  EM profile credentials, and the emergency number is dialed using the translation pattern, an ELIN
                                          will be associated for this outbound emergency call. If the call is disconnected and is called back  using PSAP CallBack,
                                          if the user has since logged out, the call will not route to the device that initiated the call and will fail. |
| PSAP CallBack with a user logged in on a different device. When a user logs in with EM profile credentials at Phone A and dials the emergency number using the translation pattern, an
                                          ELIN will be associated for this outbound emergency call. If the call is disconnected, the user should log out from Phone
                                          A. If the user then logs in to another phone, Phone B, with the same profile, and  the ELIN is called back using PSAP CallBack,
                                          the call is then be routed to Phone B with normal priority, meaning  CFA settings will be ignored and DND settings will not
                                          be ignored. |
| PSAP CallBack call with multiple logins. When a user logs in with EM profile credentials at Phone A and dials the emergency number using the translation pattern, an
                                          ELIN number will be associated for this outbound emergency call. If the call is disconnected and the user logs in to another
                                          phone, Phone B, with the same profile while the user is still logged in on Phone A, and the ELIN is called back using PSAP
                                          CallBack, then the call is routed to Phone A only, the device on which the call originated. |
| Device Mobility | A roaming device will use the Roaming Device Pool's ELIN Group for an outbound emergency call. Move a device with Device Mobility enabled from its home location to the Roaming location, a change in IP subnet, so that
                                          it gets associated with the Roaming device pool. If the emergency number is dialed using the translation pattern, an ELIN
                                          is associated for this outbound emergency call. The ELIN belongs to the ELIN Group that is associated with the Roaming Device
                                          Pool. |
| Shared Lines | PSAP CallBack rings only on the device which made the emergency call even if the line is shared by different devices. Phone A and Phone B share a Directory Number (DN). If the emergency number is dialed using the translation pattern, an ELIN
                                          is associated for this outbound emergency call. If the call is disconnected, and the ELIN is called back using PSAP CallBack,
                                          the call is routed to Phone A only, the device from which the call originated. |

| Note | This is the device on which the user is still logged in. |
|---|---|