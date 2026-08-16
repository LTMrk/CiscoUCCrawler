---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-cucm-b-feature-configuration-guide-for-cisco1251su3-cuc-ab623f78c6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/cucm_b_feature-configuration-guide-for-cisco1251su3/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_010000.html
retrieved_at: 2026-08-16T17:05:33.749642+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Immediate Divert

## Chapter: Immediate Divert

# Immediate Divert

## Immediate Divert
                        	 Overview

The Immediate Divert feature is a Unified Communications Manager supplementary service that allows you to immediately divert a call to a voicemail system. When Immediate Divert diverts a
                           call, the line becomes available to make or receive new calls. Access the Immediate Divert feature by using the iDivert or
                           Divert softkey on the IP phone.

Immediate Divert provides the following functions:

Diverts a call to a voicemail system in the following manner:

Legacy iDivert diverts the call to the voice mailbox of the party that invokes the iDivert feature.

Enhanced iDivert diverts the call to either the voice mailbox of the party that invokes the iDivert feature or to the voice
                                       mailbox of the original called party.

Diverts inbound calls that are in the Call Offering, Call on Hold, or Call Active states.

Diverts outbound calls in the Call Active or Call on Hold states.

## Immediate Divert
                        	 Prerequisites

You must configure the voicemail profiles and hunt pilots.

For information on how to configure voicemail profiles and hunt pilots, see System Configuration Guide for Cisco Unified Communications Manager

The following devices support Immediate Divert:

Voice-messaging systems such as Cisco Unity Connection that use the Skinny Client Control Protocol (SCCP).

QSIG devices (QSIG-enabled H.323 devices, MGCP PRI QSIG T1 gateways, and MGCP PRI QSIG E1 gateways), depending on the setting
                                          of the Use Legacy Immediate Divert and Allow QSIG During iDivert clusterwide service parameters.

The following table lists the phones that use the Divert or iDivert softkey.

What to configure in softkey template

Cisco Unified IP Phone 6900 Series (except 6901 and 6911)

X

iDivert

Cisco Unified IP Phone 7900 Series

X

iDivert

Cisco Unified IP Phone 8900 Series

X

Configured by default

Cisco Unified IP Phone 9900 Series

X

Configured by default

Cisco Unified
                                          		  IP Phones 8900 and 9900 series have the Divert softkey assigned by default.

## Immediate Divert
                        	 Configuration Task Flow

### Before you begin

Review Immediate Divert Prerequisites .

Step 1

Configure Immediate Divert Service Parameters

Step 2

Configure a Softkey Template for Immediate Divert

Step 3

To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks:

- Add a Softkey Template to the Common Device Configuration

- Associate a Common Device Configuration with a Phone

Optional . To make the softkey template available to phones, you must complete either this step or the following step. Follow this
                                          step if your system uses a Common Device Configuration to apply configuration options to phones.

This is the
                                          				most commonly used method for making a softkey template available to phones.

Step 4

Associate a Softkey Template with a Phone

Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment.

### Configure
                           	 Immediate Divert Service Parameters

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Configure the relevant service parameters and click Save .

Call Park Display Timer

Enter a number from 0 to 100 (inclusive) to control the timer for the Immediate Divert text display on the IP phones. Set
                                                         this timer for the server or for each server in a cluster that has the Cisco CallManager service and Immediate Divert configured.
                                                         The default value for this service parameter is 10 seconds.

Use Legacy Immediate Divert

Select one of the following options from the drop-down list:

True —The user that invokes the iDivert feature can divert an incoming call only to his own voice mailbox. This is the default
                                                               setting.

False —Immediate Divert allows diversion of an incoming call to either the voice mailbox of the original called party or to the
                                                               voice mailbox of the user that invokes the iDivert feature.

Allow QSIG During iDivert

Select one of the following options from the drop-down list:

True —Immediate Divert diverts calls to voicemail systems that can be reached over QSIG, SIP, and QSIG-enabled H.323 devices.

False —Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. This is the default setting.

Immediate Divert User Response Timer

Enter a number from 5 to 30 (inclusive) to determine the time given to the iDivert softkey user to choose the party to whom
                                                         to divert a call. If the user does not choose a party, the call remains connected. The default value for this service parameter
                                                         is 5 seconds.

### Configure a
                           	 Softkey Template for Immediate Divert

To divert incoming calls or outgoing calls, configure a softkey template and assign the iDivert softkey to that template.
                                 You can configure the iDivert softkey in the following call states:

Connected

On hold

Ring in

Immediate Divert supports the following call states:

For incoming calls:

Call offering (shown as Ring In on the softkey template).

Call on hold

Call active

For outgoing calls:

Call on hold

Call active

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template .

Step 2

Perform the following steps to create a new softkey template; otherwise, proceed to the next step.

Click Add New .

Select a default template and click Copy .

Enter a new name for the template in the Softkey Template Name field.

Click Save .

Step 3

Perform the following steps to add softkeys to an existing template.

Click Find and enter the search criteria.

Select the required existing template.

Step 4

Check the Default Softkey Template check box to designate this softkey template as the default softkey template.

If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation.

Step 5

Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                          			 corner and click Go .

Step 6

From the Select
                                             				a Call State to Configure drop-down list, choose the call state for
                                          			 which you want the softkey to display.

Step 7

From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                          			 to change the position of the new softkey.

Step 8

Repeat the previous step to display the softkey in additional call states.

Step 9

Click Save .

Step 10

Perform one
                                          			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                             see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections.

### Associate a
                           	 Softkey Template with a Common Device Configuration

Optional. There
                                 		  are two ways to associate a softkey template with a phone:

Add the
                                       				softkey template to the Phone Configuration .

Add the
                                       				softkey template to the Common Device Configuration .

The procedures in
                                 		  this section describe how to associate the softkey template with a Common
                                    			 Device Configuration . Follow these procedures if your system uses a Common
                                    			 Device Configuration to apply configuration options to phones. This
                                 		  is the most commonly used method for making a softkey template available to
                                 		  phones.

To use the
                                 		  alternative method, see Associate a Softkey Template with a Phone

Step 1

Add a Softkey Template to the Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

#### Add a Softkey Template to the Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                             proceed to the next step.

Click Add New .

Enter a name for the Common Device Configuration in the Name field.

Click Save .

Step 3

Perform the following steps to add the softkey template to an existing Common Device Configuration.

Click Find and enter the search criteria.

Click an existing Common Device Configuration.

Step 4

In the Softkey Template drop-down list, choose the softkey
                                             			 template that contains the softkey that you want to make available.

Step 5

Click Save .

Step 6

Perform one
                                             			 of the following tasks:

- If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices.

- If you created a new Common Device Configuration, associate the configuration with devices and then restart them.

#### Associate a Common Device Configuration with a Phone

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone device to add the softkey template.

Step 3

From the Common Device Configuration drop-down list, choose
                                             				  the common device configuration that contains the new softkey template.

Step 4

Click Save .

Step 5

Click Reset to update the phone settings.

### Associate a
                           	 Softkey Template with a Phone

Optional . Use this procedure as an alternative to associating the softkey template with the Common Device Configuration. This procedure
                                 also works in conjunction with the Common Device Configuration. You can use it when you need to assign a softkey template
                                 that overrides the assignment in the Common Device Configuration or any other default softkey assignment.

#### Before you begin

Configure a Softkey Template for Immediate Divert

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the phone to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template that contains the new softkey.

Step 4

Click Save .

## Immediate Divert
                        	 Interactions

Multilevel Precedence and Preemption (MLPP)

Immediate Divert diverts calls to voice-messaging mailboxes
                                          							 regardless of the type of call (for example, a precedence call).

When
                                          							 Alternate Party Diversion (call precedence) is activated, Call Forward No
                                          							 Answer (CFNA) gets deactivated.

Call
                                          						Forward

When
                                          						the Forward No Answer setting on the Directory Number Configuration window is
                                          						not configured, Call Forward uses the clusterwide CFNA timer service parameter,
                                          						Forward No Answer Timer.

If a
                                          						user presses the iDivert softkey at the same time as the call is being
                                          						forwarded, the call gets diverted to an assigned call forward directory number
                                          						(because the timer was too short), not the voice-messaging mailbox. To resolve
                                          						this situation, set the CFNA timer service parameter to enough time (for
                                          						example, 60 seconds).

Call
                                          						Detail Records (CDR)

Immediate Divert uses the immediate divert code number in the Onbehalf of fields (for example, joinOnbehalfOf and
                                          						lastRedirectRediectOnBehalfOf) in CDR.

Call Park and Directed Call Park

When user A calls user B, and user B parks the call; user B
                                          						retrieves the call and then decides to send the call to a voice-messaging
                                          						mailbox by pressing the iDivert or Divert softkey. User A receives the
                                          						voice-messaging mailbox greeting of user B.

Conference

When a
                                          						conference participant presses the iDivert softkey, the remaining conference
                                          						participants receive the voice-messaging mailbox greeting of the immediate
                                          						divert initiator. Conference types include Ad Hoc, Meet-Me, Barge, cBarge, and
                                          						Join.

Hunt
                                          						List

For
                                          							 calls that reach the phone directly through a hunt list pilot (as part of the
                                          							 hunting algorithms), the iDivert softkey appears dimmed if the Use Legacy
                                          							 Immediate Divert clusterwide service parameter is set to True; otherwise, it
                                          							 does not appear dimmed.

For
                                          							 calls that do not reach the phone directly through a hunt list pilot (as part
                                          							 of the hunting algorithms), the iDivert softkey does not appear dimmed when the
                                          							 Use Legacy Immediate Divert clusterwide service parameter is set to True or
                                          							 False.

For Jabber in desk phone mode, iDivert feature redirection to VM is done through CTI application where ‘Use Legacy Immediate
                                                      Divert’ parameter will not take effect and HP number will be sent as diversion info to Voice mail servers.

Auto
                                          						Call Pickup

If the
                                          						Use Legacy Immediate Divert clusterwide service parameter is set to False, and
                                          						the Auto Call Pickup Enabled clusterwide service parameter is set to True, and
                                          						a user of call pickup group uses call pickup to answer a call, the IP phone
                                          						display will not present any choices to the user when the iDivert softkey is
                                          						pressed.

## Immediate Divert
                        	 Restrictions

Voice
                                          						Mail Profile

When
                                          						you use QSIG integration with your voicemail system, a voicemail profile that
                                          						includes either a voicemail pilot or a voicemail mask or both should leave the Make this the default Voice Mail Profile for the
                                             						  System check box unchecked. Ensure the default Voice Mail Profile
                                          						setting is always set to No Voice Mail.

Call
                                          						Forward All (CFA) and Call Forward Busy (CFB)

When
                                          						Call Forward All (CFA) and Call Forward Busy (CFB) are activated, the system
                                          						does not support Immediate Divert (CFA and CFB have precedence over Immediate
                                          						Divert).

Busy
                                          						Voicemail System

The iDivert detects a busy condition on the voicemail ports, when iDivert reaches a voicemail system over a local or SCCP
                                          connection.

Immediate Divert cannot divert a call to a busy voicemail port; voicemail ports can exist as members of a route or hunt list.

The call cannot divert to a busy voicemail system, but the original call gets maintained. The phone displays "Busy" message on which iDivert was invoked to indicate that the call was not diverted.

When a voicemail system is reached over a QSIG or SIP trunk, iDivert can be detected, but the call does not get maintained.
                                                      When the Allow QSIG During iDivert clusterwide service parameter is set to True , or the Use Legacy Immediate Divert clusterwide service parameter is set to False , Immediate Divert supports access to voicemail systems that can be reached over QSIG or SIP trunks. When the Allow QSIG During iDivert clusterwide service parameter is set to False , and the Use Legacy Immediate Divert clusterwide service parameter is set to True , Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks.

Malicious Caller ID

System
                                          						does not support using Malicious Caller ID and Immediate Divert features
                                          						together.

Forward
                                          						No Answer Timeout

A race
                                          						condition in connection with the Forward No Answer Timeout exists when you
                                          						press the iDivert softkey. For example, if a manager presses the iDivert
                                          						softkey immediately after the Forward No Answer timeout, call forward forwards
                                          						the call to a preconfigured directory number. However, if the manager presses
                                          						the iDivert softkey before the Forward No Answer timeout, immediate divert
                                          						diverts the call to the voice-messaging mailbox of the manager.

Calling
                                          						Parties and Called Parties

The
                                          						calling parties and called parties can divert the call to their voice mailboxes
                                          						if both simultaneously press the iDivert softkey.

Conference Types

When
                                          						one participant in a conference presses the iDivert softkey, all remaining
                                          						participants receive an outgoing greeting of the participant who pressed
                                          						iDivert. Conference types include Meet-Me, Ad Hoc, cBarge, and Join.

Split
                                          						or Join Operation

If
                                          						the last action on a call was Auto Pickup, Call Transfer, Call Park, Call Park
                                          						Reversion, Conference, Meet-Me Conference, or any application that performs a
                                          						split or join operation, enhanced iDivert does not present a screen to a called
                                          						party to choose the voice mailbox. Instead, enhanced iDivert immediately
                                          						diverts the call to the voice mailbox that is associated with the called party.

## Immediate Divert Troubleshooting

### Key is not
                           	 active

The phone displays this message when the user presses iDivert:

```
Key is not active
```

The voice-messaging profile of the user who pressed iDivert does not
                              		have a voice-messaging pilot.

Configure a voice-messaging pilot in the user voice-messaging profile.

### Temporary
                           	 Failure

The phone displays this message when the user presses iDivert:

```
Temporary Failure
```

The voice-messaging system does not work, or a network problem exists.

Troubleshoot your voice-messaging system. See troubleshooting or
                              		voice-messaging documentation.

### Busy

The phone displays this message when the user presses iDivert:

```
Busy
```

This message means that the voice-messaging system is busy.

Configure more voice-messaging ports or try again.

| Note | Although the Immediate Divert feature is not available to CTI applications, a CTI redirect operation exists that performs
                                    the same function as Immediate Divert. Application developers can use the CTI redirect operation to accomplish Immediate Divert. |
|---|---|

| Cisco Unified IP Phone Model | Divert Softkey | iDivert Softkey | What to configure in softkey template |
|---|---|---|---|
| Cisco Unified IP Phone 6900 Series (except 6901 and 6911) | X |  | iDivert |
| Cisco Unified IP Phone 7900 Series |  | X | iDivert |
| Cisco Unified IP Phone 8900 Series | X |  | Configured by default |
| Cisco Unified IP Phone 9900 Series | X |  | Configured by default |

| Note | Cisco Unified
                                          		  IP Phones 8900 and 9900 series have the Divert softkey assigned by default. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Immediate Divert Service Parameters | Configure the
                                       			 service parameters to enable Immediate Divert across various devices and
                                       			 applications. |
| Step 2 | Configure a Softkey Template for Immediate Divert | Create and
                                       			 configure a softkey template and add the iDivert softkey to that template. |
| Step 3 | To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks: Add a Softkey Template to the Common Device Configuration Associate a Common Device Configuration with a Phone | Optional . To make the softkey template available to phones, you must complete either this step or the following step. Follow this
                                          step if your system uses a Common Device Configuration to apply configuration options to phones. This is the
                                          				most commonly used method for making a softkey template available to phones. |
| Step 4 | Associate a Softkey Template with a Phone | Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Configure the relevant service parameters and click Save . Table 2. Service Parameter Fields for Immediate Divert Field Description Call Park Display Timer Enter a number from 0 to 100 (inclusive) to control the timer for the Immediate Divert text display on the IP phones. Set
                                                         this timer for the server or for each server in a cluster that has the Cisco CallManager service and Immediate Divert configured.
                                                         The default value for this service parameter is 10 seconds. Use Legacy Immediate Divert Select one of the following options from the drop-down list: True —The user that invokes the iDivert feature can divert an incoming call only to his own voice mailbox. This is the default
                                                               setting. False —Immediate Divert allows diversion of an incoming call to either the voice mailbox of the original called party or to the
                                                               voice mailbox of the user that invokes the iDivert feature. Allow QSIG During iDivert Select one of the following options from the drop-down list: True —Immediate Divert diverts calls to voicemail systems that can be reached over QSIG, SIP, and QSIG-enabled H.323 devices. False —Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. This is the default setting. Immediate Divert User Response Timer Enter a number from 5 to 30 (inclusive) to determine the time given to the iDivert softkey user to choose the party to whom
                                                         to divert a call. If the user does not choose a party, the call remains connected. The default value for this service parameter
                                                         is 5 seconds. | Field | Description | Call Park Display Timer | Enter a number from 0 to 100 (inclusive) to control the timer for the Immediate Divert text display on the IP phones. Set
                                                         this timer for the server or for each server in a cluster that has the Cisco CallManager service and Immediate Divert configured.
                                                         The default value for this service parameter is 10 seconds. | Use Legacy Immediate Divert | Select one of the following options from the drop-down list: True —The user that invokes the iDivert feature can divert an incoming call only to his own voice mailbox. This is the default
                                                               setting. False —Immediate Divert allows diversion of an incoming call to either the voice mailbox of the original called party or to the
                                                               voice mailbox of the user that invokes the iDivert feature. | Allow QSIG During iDivert | Select one of the following options from the drop-down list: True —Immediate Divert diverts calls to voicemail systems that can be reached over QSIG, SIP, and QSIG-enabled H.323 devices. False —Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. This is the default setting. | Immediate Divert User Response Timer | Enter a number from 5 to 30 (inclusive) to determine the time given to the iDivert softkey user to choose the party to whom
                                                         to divert a call. If the user does not choose a party, the call remains connected. The default value for this service parameter
                                                         is 5 seconds. |
| Field | Description |
| Call Park Display Timer | Enter a number from 0 to 100 (inclusive) to control the timer for the Immediate Divert text display on the IP phones. Set
                                                         this timer for the server or for each server in a cluster that has the Cisco CallManager service and Immediate Divert configured.
                                                         The default value for this service parameter is 10 seconds. |
| Use Legacy Immediate Divert | Select one of the following options from the drop-down list: True —The user that invokes the iDivert feature can divert an incoming call only to his own voice mailbox. This is the default
                                                               setting. False —Immediate Divert allows diversion of an incoming call to either the voice mailbox of the original called party or to the
                                                               voice mailbox of the user that invokes the iDivert feature. |
| Allow QSIG During iDivert | Select one of the following options from the drop-down list: True —Immediate Divert diverts calls to voicemail systems that can be reached over QSIG, SIP, and QSIG-enabled H.323 devices. False —Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. This is the default setting. |
| Immediate Divert User Response Timer | Enter a number from 5 to 30 (inclusive) to determine the time given to the iDivert softkey user to choose the party to whom
                                                         to divert a call. If the user does not choose a party, the call remains connected. The default value for this service parameter
                                                         is 5 seconds. |

| Field | Description |
|---|---|
| Call Park Display Timer | Enter a number from 0 to 100 (inclusive) to control the timer for the Immediate Divert text display on the IP phones. Set
                                                         this timer for the server or for each server in a cluster that has the Cisco CallManager service and Immediate Divert configured.
                                                         The default value for this service parameter is 10 seconds. |
| Use Legacy Immediate Divert | Select one of the following options from the drop-down list: True —The user that invokes the iDivert feature can divert an incoming call only to his own voice mailbox. This is the default
                                                               setting. False —Immediate Divert allows diversion of an incoming call to either the voice mailbox of the original called party or to the
                                                               voice mailbox of the user that invokes the iDivert feature. |
| Allow QSIG During iDivert | Select one of the following options from the drop-down list: True —Immediate Divert diverts calls to voicemail systems that can be reached over QSIG, SIP, and QSIG-enabled H.323 devices. False —Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. This is the default setting. |
| Immediate Divert User Response Timer | Enter a number from 5 to 30 (inclusive) to determine the time given to the iDivert softkey user to choose the party to whom
                                                         to divert a call. If the user does not choose a party, the call remains connected. The default value for this service parameter
                                                         is 5 seconds. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template . |
|---|---|
| Step 2 | Perform the following steps to create a new softkey template; otherwise, proceed to the next step. Click Add New . Select a default template and click Copy . Enter a new name for the template in the Softkey Template Name field. Click Save . |
| Step 3 | Perform the following steps to add softkeys to an existing template. Click Find and enter the search criteria. Select the required existing template. |
| Step 4 | Check the Default Softkey Template check box to designate this softkey template as the default softkey template. Note If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. | Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
| Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
| Step 5 | Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                          			 corner and click Go . |
| Step 6 | From the Select
                                             				a Call State to Configure drop-down list, choose the call state for
                                          			 which you want the softkey to display. |
| Step 7 | From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                          			 to change the position of the new softkey. |
| Step 8 | Repeat the previous step to display the softkey in additional call states. |
| Step 9 | Click Save . |
| Step 10 | Perform one
                                          			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                             see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections. |

| Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a Softkey Template to the Common Device Configuration |  |
| Step 2 | Associate a Common Device Configuration with a Phone |  |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                             proceed to the next step. Click Add New . Enter a name for the Common Device Configuration in the Name field. Click Save . |
| Step 3 | Perform the following steps to add the softkey template to an existing Common Device Configuration. Click Find and enter the search criteria. Click an existing Common Device Configuration. |
| Step 4 | In the Softkey Template drop-down list, choose the softkey
                                             			 template that contains the softkey that you want to make available. |
| Step 5 | Click Save . |
| Step 6 | Perform one
                                             			 of the following tasks: If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices. If you created a new Common Device Configuration, associate the configuration with devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone device to add the softkey template. |
| Step 3 | From the Common Device Configuration drop-down list, choose
                                             				  the common device configuration that contains the new softkey template. |
| Step 4 | Click Save . |
| Step 5 | Click Reset to update the phone settings. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to select the phone to add the softkey template. |
| Step 3 | From the Softkey Template drop-down list, choose the template that contains the new softkey. |
| Step 4 | Click Save . |

| Feature | Interaction |
|---|---|
| Multilevel Precedence and Preemption (MLPP) | Immediate Divert diverts calls to voice-messaging mailboxes
                                          							 regardless of the type of call (for example, a precedence call). When
                                          							 Alternate Party Diversion (call precedence) is activated, Call Forward No
                                          							 Answer (CFNA) gets deactivated. |
| Call
                                          						Forward | When
                                          						the Forward No Answer setting on the Directory Number Configuration window is
                                          						not configured, Call Forward uses the clusterwide CFNA timer service parameter,
                                          						Forward No Answer Timer. If a
                                          						user presses the iDivert softkey at the same time as the call is being
                                          						forwarded, the call gets diverted to an assigned call forward directory number
                                          						(because the timer was too short), not the voice-messaging mailbox. To resolve
                                          						this situation, set the CFNA timer service parameter to enough time (for
                                          						example, 60 seconds). |
| Call
                                          						Detail Records (CDR) | Immediate Divert uses the immediate divert code number in the Onbehalf of fields (for example, joinOnbehalfOf and
                                          						lastRedirectRediectOnBehalfOf) in CDR. |
| Call Park and Directed Call Park | When user A calls user B, and user B parks the call; user B
                                          						retrieves the call and then decides to send the call to a voice-messaging
                                          						mailbox by pressing the iDivert or Divert softkey. User A receives the
                                          						voice-messaging mailbox greeting of user B. |
| Conference | When a
                                          						conference participant presses the iDivert softkey, the remaining conference
                                          						participants receive the voice-messaging mailbox greeting of the immediate
                                          						divert initiator. Conference types include Ad Hoc, Meet-Me, Barge, cBarge, and
                                          						Join. |
| Hunt
                                          						List | For
                                          							 calls that reach the phone directly through a hunt list pilot (as part of the
                                          							 hunting algorithms), the iDivert softkey appears dimmed if the Use Legacy
                                          							 Immediate Divert clusterwide service parameter is set to True; otherwise, it
                                          							 does not appear dimmed. For
                                          							 calls that do not reach the phone directly through a hunt list pilot (as part
                                          							 of the hunting algorithms), the iDivert softkey does not appear dimmed when the
                                          							 Use Legacy Immediate Divert clusterwide service parameter is set to True or
                                          							 False. Note For Jabber in desk phone mode, iDivert feature redirection to VM is done through CTI application where ‘Use Legacy Immediate
                                                      Divert’ parameter will not take effect and HP number will be sent as diversion info to Voice mail servers. | Note | For Jabber in desk phone mode, iDivert feature redirection to VM is done through CTI application where ‘Use Legacy Immediate
                                                      Divert’ parameter will not take effect and HP number will be sent as diversion info to Voice mail servers. |
| Note | For Jabber in desk phone mode, iDivert feature redirection to VM is done through CTI application where ‘Use Legacy Immediate
                                                      Divert’ parameter will not take effect and HP number will be sent as diversion info to Voice mail servers. |
| Auto
                                          						Call Pickup | If the
                                          						Use Legacy Immediate Divert clusterwide service parameter is set to False, and
                                          						the Auto Call Pickup Enabled clusterwide service parameter is set to True, and
                                          						a user of call pickup group uses call pickup to answer a call, the IP phone
                                          						display will not present any choices to the user when the iDivert softkey is
                                          						pressed. |

| Note | For Jabber in desk phone mode, iDivert feature redirection to VM is done through CTI application where ‘Use Legacy Immediate
                                                      Divert’ parameter will not take effect and HP number will be sent as diversion info to Voice mail servers. |
|---|---|

| Restriction | Description |
|---|---|
| Voice
                                          						Mail Profile | When
                                          						you use QSIG integration with your voicemail system, a voicemail profile that
                                          						includes either a voicemail pilot or a voicemail mask or both should leave the Make this the default Voice Mail Profile for the
                                             						  System check box unchecked. Ensure the default Voice Mail Profile
                                          						setting is always set to No Voice Mail. |
| Call
                                          						Forward All (CFA) and Call Forward Busy (CFB) | When
                                          						Call Forward All (CFA) and Call Forward Busy (CFB) are activated, the system
                                          						does not support Immediate Divert (CFA and CFB have precedence over Immediate
                                          						Divert). |
| Busy
                                          						Voicemail System | The iDivert detects a busy condition on the voicemail ports, when iDivert reaches a voicemail system over a local or SCCP
                                          connection. Note Immediate Divert cannot divert a call to a busy voicemail port; voicemail ports can exist as members of a route or hunt list. The call cannot divert to a busy voicemail system, but the original call gets maintained. The phone displays "Busy" message on which iDivert was invoked to indicate that the call was not diverted. When a voicemail system is reached over a QSIG or SIP trunk, iDivert can be detected, but the call does not get maintained.
                                                      When the Allow QSIG During iDivert clusterwide service parameter is set to True , or the Use Legacy Immediate Divert clusterwide service parameter is set to False , Immediate Divert supports access to voicemail systems that can be reached over QSIG or SIP trunks. When the Allow QSIG During iDivert clusterwide service parameter is set to False , and the Use Legacy Immediate Divert clusterwide service parameter is set to True , Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. | Note | Immediate Divert cannot divert a call to a busy voicemail port; voicemail ports can exist as members of a route or hunt list. The call cannot divert to a busy voicemail system, but the original call gets maintained. The phone displays "Busy" message on which iDivert was invoked to indicate that the call was not diverted. When a voicemail system is reached over a QSIG or SIP trunk, iDivert can be detected, but the call does not get maintained.
                                                      When the Allow QSIG During iDivert clusterwide service parameter is set to True , or the Use Legacy Immediate Divert clusterwide service parameter is set to False , Immediate Divert supports access to voicemail systems that can be reached over QSIG or SIP trunks. When the Allow QSIG During iDivert clusterwide service parameter is set to False , and the Use Legacy Immediate Divert clusterwide service parameter is set to True , Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. |
| Note | Immediate Divert cannot divert a call to a busy voicemail port; voicemail ports can exist as members of a route or hunt list. The call cannot divert to a busy voicemail system, but the original call gets maintained. The phone displays "Busy" message on which iDivert was invoked to indicate that the call was not diverted. When a voicemail system is reached over a QSIG or SIP trunk, iDivert can be detected, but the call does not get maintained.
                                                      When the Allow QSIG During iDivert clusterwide service parameter is set to True , or the Use Legacy Immediate Divert clusterwide service parameter is set to False , Immediate Divert supports access to voicemail systems that can be reached over QSIG or SIP trunks. When the Allow QSIG During iDivert clusterwide service parameter is set to False , and the Use Legacy Immediate Divert clusterwide service parameter is set to True , Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. |
| Malicious Caller ID | System
                                          						does not support using Malicious Caller ID and Immediate Divert features
                                          						together. |
| Forward
                                          						No Answer Timeout | A race
                                          						condition in connection with the Forward No Answer Timeout exists when you
                                          						press the iDivert softkey. For example, if a manager presses the iDivert
                                          						softkey immediately after the Forward No Answer timeout, call forward forwards
                                          						the call to a preconfigured directory number. However, if the manager presses
                                          						the iDivert softkey before the Forward No Answer timeout, immediate divert
                                          						diverts the call to the voice-messaging mailbox of the manager. |
| Calling
                                          						Parties and Called Parties | The
                                          						calling parties and called parties can divert the call to their voice mailboxes
                                          						if both simultaneously press the iDivert softkey. |
| Conference Types | When
                                          						one participant in a conference presses the iDivert softkey, all remaining
                                          						participants receive an outgoing greeting of the participant who pressed
                                          						iDivert. Conference types include Meet-Me, Ad Hoc, cBarge, and Join. |
| Split
                                          						or Join Operation | If
                                          						the last action on a call was Auto Pickup, Call Transfer, Call Park, Call Park
                                          						Reversion, Conference, Meet-Me Conference, or any application that performs a
                                          						split or join operation, enhanced iDivert does not present a screen to a called
                                          						party to choose the voice mailbox. Instead, enhanced iDivert immediately
                                          						diverts the call to the voice mailbox that is associated with the called party. |

| Note | Immediate Divert cannot divert a call to a busy voicemail port; voicemail ports can exist as members of a route or hunt list. The call cannot divert to a busy voicemail system, but the original call gets maintained. The phone displays "Busy" message on which iDivert was invoked to indicate that the call was not diverted. When a voicemail system is reached over a QSIG or SIP trunk, iDivert can be detected, but the call does not get maintained.
                                                      When the Allow QSIG During iDivert clusterwide service parameter is set to True , or the Use Legacy Immediate Divert clusterwide service parameter is set to False , Immediate Divert supports access to voicemail systems that can be reached over QSIG or SIP trunks. When the Allow QSIG During iDivert clusterwide service parameter is set to False , and the Use Legacy Immediate Divert clusterwide service parameter is set to True , Immediate Divert does not support access to voicemail systems over QSIG or SIP trunks. |
|---|---|