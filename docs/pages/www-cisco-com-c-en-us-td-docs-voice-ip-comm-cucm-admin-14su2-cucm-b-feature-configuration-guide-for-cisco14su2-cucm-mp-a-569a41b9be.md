---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-cucm-b-feature-configuration-guide-for-cisco14su2-cucm-mp-a-569a41b9be
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/cucm_b_feature-configuration-guide-for-cisco14su2/cucm_mp_a61d542b_00_ad-hoc-conferencing-12-0.html
retrieved_at: 2026-08-16T16:23:13.616274+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: May 7, 2026

Chapter: Ad Hoc Conferencing

## Chapter: Ad Hoc Conferencing

# Ad Hoc Conferencing

## Ad Hoc
                        	 Conferencing Overview

Ad Hoc conferences
                           		allow the conference controller (or in some cases, another participant) to add
                           		participants to the conference.

Ad Hoc conferences
                           		comprise two types: basic and advanced. In basic ad hoc conferencing, the
                           		originator of the conference acts as the controller of the conference and is
                           		the only participant who can add or remove other participants. In advanced Ad
                           		Hoc conferencing, any participant can add or remove other participants.
                           		Advanced Ad Hoc conferencing also allows you to link multiple ad hoc
                           		conferences together.

Advanced
                           		Ad Hoc conferencing allows you to link multiple Ad Hoc conferences together by
                           		adding an Ad Hoc conference to another Ad Hoc conference as if it were an
                           		individual participant. If you attempt to link multiple conferences together
                           		when the Advanced Ad Hoc Conference Enabled service parameter is set to False,
                           		the IP phone displays a message. You can also use the methods that are
                           		available for adding individual participants to an Ad Hoc conference to add
                           		another conference to an Ad Hoc conference.

## Ad Hoc
                        	 Conferencing Task Flow

Step 1

Configure Softkey Template for Conferencing

Add the
                                          				Conference List, Join, and Remove Last Conference Party softkeys to a softkey
                                          				template.

Step 2

To Associate Softkey Template Common Device ,
                                       			 complete the following subtasks:

- Add a Softkey Template to a Common Device Configuration

- Associate a Common Device Configuration with a Phone

Optional . To make the softkey template available to phones, you must complete either this step or the following step. Follow this
                                          step if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                          phones.

Step 3

Associate a Softkey Template with a Phone

Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment.

Step 4

Configure Ad Hoc Conferencing

Enable
                                          				advanced conferencing, specify the maximum number of participants, and specify
                                          				when to drop a conference connection.

Step 5

Configure Join Across Lines

Enable Join
                                          				Across Lines to create a conference.

### Configure Softkey Template for Conferencing

Use this procedure
                                 		  to make  the following conferencing softkeys available:

Softkey

Description

Call
                                             						States

Conference List 
                                             					 ( ConfList )

View a list of participant directory numbers that are in an Ad Hoc
                                             		  conference. The name of the participant is displayed if it is configured in Cisco Unified Communications Manager Administration .

On Hook

Connected

Join

Join up to 15 established
                                             		  calls (for a total of 16) to create a conference.

On Hold

Remove
                                             						Last Conference Party 
                                             					 ( Remove )

The conference controller can invoke the conference list and remove any participant in the conference by using the Remove softkey.

On Hook

Connected

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

#### What to do next

Complete one of the following procedures:

Associate Softkey Template Common Device

Associate a Softkey Template with a Phone

### Associate Softkey
                           	 Template Common Device

Optional . There are two ways to associate a softkey template with a phone:

Add the softkey template to the Phone Configuration .

Add the
                                       				softkey template to the Common Device Configuration .

The
                                 		  procedures in this section describe how to associate the softkey template with
                                 		  a Common
                                    			 Device Configuration . Follow these procedures if your system uses a Common
                                    			 Device Configuration to apply configuration options to phones. This
                                 		  is the most commonly used method for making a softkey template available to
                                 		  phones.

To use the
                                 		  alternative method, go to Associate a Softkey Template with a Phone

#### Before you begin

Configure Softkey Template for Conferencing

Step 1

Add a Softkey Template to a Common Device Configuration

Perform this
                                             				step to add a conferencing softkey template to the Common Device Configuration.

Step 2

Associate a Common Device Configuration with a Phone

Perform this
                                             				step to link the conferencing softkey Common Device Configuration to a phone.

#### Add a Softkey Template to a Common Device Configuration

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

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to select the phone to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template that contains the new softkey.

Step 4

Click Save .

Step 5

Press Reset to update the phone settings.

### Configure Ad Hoc
                           	 Conferencing

Configure advanced Ad Hoc conferencing to allow non-controller
                                 		  participants to add and remove other participants and the ability of all
                                 		  participants to link ad hoc conferences together.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server.

Step 3

From the Service drop-down list, choose Cisco
                                             				CallManager .

Step 4

Configure the fields in the Clusterwide Parameters (Features - Conference) area. For parameter descriptions, see Ad Hoc Conferencing Service Parameters .

Step 5

Click Save.

#### What to do next

Configure Join Across Lines

#### Ad Hoc
                              	 Conferencing Service Parameters

The following table lists the main service parameters for Ad Hoc conferencing. For additional conferencing service parameters,
                                    refer to the Service Parameter Configuration window's Advanced option. Conferencing service parameters appear under Clusterwide Parameters (Feature - Conference) .

Service
                                                						Parameters

Description

Drop Ad
                                                						Hoc Conference

Drop Ad Hoc Conference, prevents toll fraud (where an internal conference controller disconnects from the conference while
                                                outside callers remain connected). The service parameter settings specify conditions under which an ad hoc conference gets
                                                dropped.

Never —The conference does not get dropped. (We recommend that you use the default option to avoid unintentional termination of
                                                      a conference).

When No OnNet Parties Remain in the Conference —The system drops the active conference when the last on-network party in the conference hangs up or drops out of the conference. Unified Communications Manager releases all resources that are assigned to the conference.

Drop Ad Hoc Conference feature in an ILS deployment will not drop the parties when it set at When No OnNet Parties Remain in the Conference because the route patterns learned are classified as On Net.

When Conference Controller Leaves —The active conference terminates when the primary controller (conference creator) hangs up. Unified Communications Manager releases all resources that are assigned to the conference.

We recommend that you set this service parameter to Never . Any other setting can result in unintentional termination of a conference.

The Drop Ad Hoc Conference service parameter works differently for conference calls that are initiated from a Cisco Unified IP Phone 7940 or 7960 that is running SIP, or a third-party phone that is running SIP

Maximum
                                                						Ad Hoc Conference

This
                                                						parameter specifies the maximum number of participants that are allowed in a
                                                						single Ad Hoc conference.

Default
                                                						Value: 4

Advanced
                                                						Ad Hoc Conference Enabled

This
                                                						parameter determines whether advanced Ad Hoc conference features are
                                                						enabled. This includes the ability of non-controller participants to add and
                                                						remove other participants and the ability of all participants to link ad hoc
                                                						conferences together.

Non-linear Ad Hoc Conference Linking Enabled

This
                                                						parameter determines whether more than two Ad Hoc conferences can be linked
                                                						directly to an Ad Hoc conference in a non-linear fashion ( three or more
                                                						conferences linked to any one conference).

Choose Encrypted Audio Conference Instead Of Video Conference

This parameter determines whether Unified Communications Manager chooses an encrypted audio conference bridge or an unencrypted video conference bridge for an Ad-Hoc conference call when
                                                the conference controller's Device Security Mode is set to either Authenticated or Encrypted and at least two conference participants
                                                are video-capable. Because encrypted video conference bridges are not supported in this release, Unified Communications Manager must choose between an encrypted audio conference bridge and an unencrypted video conference bridge. The default value is True .

Minimum  Video Capable Participants To Allocate Video Conference

This parameter specifies the number of video-capable conference participants that must be present in an Ad Hoc conference
                                                to allocate a video conference bridge. If the number of video-capable participants is less than the number specified in this
                                                parameter, Unified Communications Manager allocates an audio conference bridge. If the number of video-capable participants is equal to, or greater than, the number
                                                specified in this parameter, Unified Communications Manager allocates a video conference bridge, when available, from the configured media resource group list (MRGL). Specifying a value
                                                of zero means that video conference bridges will always be allocated, even when none of the participants on the conference
                                                are video-capable. When a conference has been established using an audio bridge and then additional video-capable participants
                                                join the conference, the conference will remain on the audio bridge and will not convert to video. The default value is 2 .

Allocate Video Conference Bridge For Audio Only Conferences When The Video Conference Bridge Has Higher Priority

This parameter determines whether Unified Communications Manager chooses a video conference bridge, when available, for an Ad Hoc audio-only conference call when the video conference bridge
                                                has a higher priority than an audio conference bridge in the media resource group list (MRGL). If an audio conference bridge
                                                has higher priority than any video conference bridge in the MRGL, Unified Communications Manager ignores this parameter. This parameter proves useful in situations where the local conference bridge is a video bridge (and
                                                configured in the MRGL with the highest priority) and audio conference bridges are only available in remote locations; in
                                                that situation, enabling this parameter means that Unified Communications Manager would attempt to use the local video conference bridge first, even for audio-only conference calls. The default value is False .

Enable
                                                						Click-to-Conference for Third-Party Applications

This parameter determines whether the Click-to-Conference functionality over the SIP trunk is enabled on Unified Communications Manager . The Click-to-Conference feature allows third-party applications to setup a conference using the SIP out of dialog REFER
                                                method and subscribe to the SIP trunk for Conference Event Package through SIP SUBSCRIBE/NOTIFY.

Warning

Enabling this parameter could negatively affect CTI applications that are not
                                                            						  coded to support this feature.

Default
                                                						value: False

Cluster Conferencing Prefix Identifier

This parameter defines a number, up to 8 digits (e.g. 0001), that is prefixed to a conference identifier generated for Adhoc
                                                and Meet-Me conferences that will be hosted on a SIP conference bridge such as Cisco Telepresence MCU or Cisco Telepresence
                                                Conductor. This field should be populated by the administrator when there are multiple clusters in a network that will be
                                                sharing the SIP conference bridges that Unified Communications Manager manages. Every cluster should be configured with a unique prefix to ensure that the conference identifier for Adhoc and Meet-Me
                                                conferences is unique. If conference resources are not being shared across clusters, then this field may not be populated.

### Configure Join
                           	 Across Lines

The Join Across
                                 		  Lines feature allows a user to join calls on multiple phone lines (either on
                                 		  different directory numbers or on the same directory number but on different
                                 		  partitions) to create a conference.

#### Before you begin

Ensure the phone model supports Join Across Lines Generate a Phone Feature List

Configure Ad Hoc Conferencing

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Default Device Profile .

Step 2

From the Device
                                             				Profile Type drop-down list, choose the phone model.

Step 3

From the Device
                                             				Protocol drop-down list, choose the relevant SCCP or SIP protocol.

Step 4

Set the Join
                                             				Across Lines to On .

Step 5

Click Save .

## Conference
                        	 Interactions

Feature

Interaction

Conference by Using cBarge

Initiate a conference by pressing the cBarge softkey, or if the Single Button cBarge
                                          						feature is enabled, by pressing the shared-line button of the active call. When
                                          						cBarge is initiated, a barge call gets set up by using the shared conference
                                          						bridge, if available. The original call gets split and then joined at the
                                          						conference bridge. The call information for all parties gets changed to
                                          						Conference.

The barged call becomes a conference call with the barge target
                                          						device as the conference controller. It can add more parties to the conference
                                          						or can drop any party.

When any party releases from the call, leaving only two parties
                                          						in the conference, the remaining two parties experience a brief interruption
                                          						and then get reconnected as a point-to-point call, which releases the shared
                                          						conference resource.

Interaction with Call Park, Call Transfer, and Redirect

If the
                                          						conference controller transfers, parks, or redirects the conference to another
                                          						party, the party that retrieves the call acts as the virtual controller for the
                                          						conference. A virtual controller cannot add new parties to the conference nor
                                          						remove any party that was added to the conference, but a virtual controller can
                                          						transfer, park, or redirect the conference to another party, who would, in
                                          						turn, become the virtual controller of the conference. When this virtual
                                          						controller hangs up the call, the conference ends.

Softkey display on SIP phones

The ConfList and the Remove softkey feature is available only on SCCP phones. The SIP phones have a Show Details button with
                                          similar functionality.

## Conference
                        	 Restrictions

The following restrictions apply to ad hoc conferencing:

Feature

Restrictions

Ad Hoc conference

Unified Communications Manager supports a maximum of 100 simultaneous Ad Hoc conferences for each Unified Communications Manager server.

Cisco Unified Communications Manager supports a maximum of 64 participants per Ad Hoc conference (provided adequate conference resources are available). In the
                                          case of linked Ad Hoc conferences, the system considers each conference as one participant.

Ad Hoc conference on SIP phones:

Cisco Unified IP Phone 7911

Cisco Unified IP Phone 7941

Cisco Unified IP Phone 7961

Unified Communications Manager uses " beep" and "beepbeep" tones when a new party is added and when the new party drops from the Ad Hoc conference, respectively. When a party is added
                                          to an Ad Hoc conference, a user on a phone that is running SIP may not hear the beep; when a participant drops from the Ad
                                          Hoc conference, a user on a phone that is running SIP may not hear the "beepbeep" . Users might not hear the beeps because of the time it takes Unified Communications Manager to set up and tear down connections during the conferencing process.

You can invoke Ad Hoc conference linking for phones that are running SIP only by using the Conference and Transfer functions.
                                          The system does not support Direct Transfer and Join. Supported phones that are running SIP comprise Cisco Unified IP Phone 7911, 7941, 7961.

Ad Hoc conference on SIP phones:

Cisco Unified IP Phone 7940

Cisco Unified IP Phone 7960

Third-Party Phone

Phones display individual calls as conference calls. Cisco Unified IP Phones 7940 and 7960 can create local conference calls
                                                but not Ad Hoc conference calls.

Conference list (ConfList), is not available.

Remove last conference participant (RmLstC), is not available.

Drop Ad Hoc conference is not supported.

The SIP Profile parameter Conference Join Enabled controls behavior of the phone that is running SIP when the conference controller
                                                exits a locally hosted conference. If the Conference Join Enabled check box is unchecked, all legs disconnect when the conference
                                                controller exits the Ad Hoc conference call. If the Conference Join Enabled check box is checked, the remaining two parties
                                                stay connected.

To achieve the same level of control that the Drop Ad Hoc Conference parameter settings provide for conference calls that
                                                a phone that is running SCCP initiates, the administrator can use a combination of the Conference Join Enabled SIP profile
                                                parameter and the Block OffNet to OffNet Transfer service parameter for conferences that are initiated on the phone that is
                                                running SIP ( Cisco Unified IP Phone 7940 or 60). (Because the phone that is running SIP performs a transfer when it drops out of the conference call, the Block
                                                OffNet to OffNet Transfer can prevent toll fraud by not allowing two offnet phones to remain in the call.)

Unified Communications Manager uses "beep" and "beepbeep" tones when a new party is added and when the new party drops from the Ad Hoc conference, respectively. When a party is added
                                                to an Ad Hoc conference, a user on a phone that is running SIP may not hear the beep when a participant drops from the Ad
                                                Hoc conference, a user on a phone that is running SIP may not hear the "beepbeep" . Users might not hear the beeps because of the time it takes Unified Communications Manager to set up and tear down connections during the conferencing process.

Phone displaying "To Conference" even when two parties are connected

Configure a Call Manager cluster with Publisher (CmA11) and Subscribers (CmA2).

Phones A, B, C are registered with CmA1. Phones D is registered with CmA2.

Setup an consultative or blind ad-hoc conference between A(1000), B(4000), C(5000), D(6000) with A as the controller.

Shutdown Cma2.

Phone D will go to Preservation mode & press end call softkey .

Phone A,B & C are in conference.

Phone A,B & C are in conference.

Disconnect Phone A ,then Phone B & C should be in a Direct call. Issue: Phone B & C are still in conference

Disconnect Phone A ,then Phone B & C should be in a Direct call. Issue: Phone B & C are still in conference

Disconnect Phone B, there should be no call on phone C. Phone B & C are still in conference. Issue: Phone C is still in Conference
                                                .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Softkey Template for Conferencing | Add the
                                          				Conference List, Join, and Remove Last Conference Party softkeys to a softkey
                                          				template. |
| Step 2 | To Associate Softkey Template Common Device ,
                                       			 complete the following subtasks: Add a Softkey Template to a Common Device Configuration Associate a Common Device Configuration with a Phone | Optional . To make the softkey template available to phones, you must complete either this step or the following step. Follow this
                                          step if your system uses a Common Device Configuration to apply configuration options to phones. This is the most commonly used method for making a softkey template available to
                                          phones. |
| Step 3 | Associate a Softkey Template with a Phone | Optional . Use this procedure either as an alternative to associating the softkey template with the Common Device Configuration, or
                                          in conjunction with the Common Device Configuration. Use this procedure in conjunction with the Common Device Configuration
                                          if you need assign a softkey template that overrides the assignment in the Common Device Configuration or any other default
                                          softkey assignment. |
| Step 4 | Configure Ad Hoc Conferencing | Enable
                                          				advanced conferencing, specify the maximum number of participants, and specify
                                          				when to drop a conference connection. |
| Step 5 | Configure Join Across Lines | Enable Join
                                          				Across Lines to create a conference. |

| Softkey | Description | Call
                                             						States |
|---|---|---|
| Conference List 
                                             					 ( ConfList ) | View a list of participant directory numbers that are in an Ad Hoc
                                             		  conference. The name of the participant is displayed if it is configured in Cisco Unified Communications Manager Administration . | On Hook Connected |
| Join | Join up to 15 established
                                             		  calls (for a total of 16) to create a conference. | On Hold |
| Remove
                                             						Last Conference Party 
                                             					 ( Remove ) | The conference controller can invoke the conference list and remove any participant in the conference by using the Remove softkey. | On Hook Connected |

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
| Step 1 | Add a Softkey Template to a Common Device Configuration | Perform this
                                             				step to add a conferencing softkey template to the Common Device Configuration. |
| Step 2 | Associate a Common Device Configuration with a Phone | Perform this
                                             				step to link the conferencing softkey Common Device Configuration to a phone. |

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
| Step 5 | Press Reset to update the phone settings. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server. |
| Step 3 | From the Service drop-down list, choose Cisco
                                             				CallManager . |
| Step 4 | Configure the fields in the Clusterwide Parameters (Features - Conference) area. For parameter descriptions, see Ad Hoc Conferencing Service Parameters . |
| Step 5 | Click Save. |

| Service
                                                						Parameters | Description |
|---|---|
| Drop Ad
                                                						Hoc Conference | Drop Ad Hoc Conference, prevents toll fraud (where an internal conference controller disconnects from the conference while
                                                outside callers remain connected). The service parameter settings specify conditions under which an ad hoc conference gets
                                                dropped. Never —The conference does not get dropped. (We recommend that you use the default option to avoid unintentional termination of
                                                      a conference). When No OnNet Parties Remain in the Conference —The system drops the active conference when the last on-network party in the conference hangs up or drops out of the conference. Unified Communications Manager releases all resources that are assigned to the conference. Note Drop Ad Hoc Conference feature in an ILS deployment will not drop the parties when it set at When No OnNet Parties Remain in the Conference because the route patterns learned are classified as On Net. When Conference Controller Leaves —The active conference terminates when the primary controller (conference creator) hangs up. Unified Communications Manager releases all resources that are assigned to the conference. Note We recommend that you set this service parameter to Never . Any other setting can result in unintentional termination of a conference. The Drop Ad Hoc Conference service parameter works differently for conference calls that are initiated from a Cisco Unified IP Phone 7940 or 7960 that is running SIP, or a third-party phone that is running SIP . | Note | Drop Ad Hoc Conference feature in an ILS deployment will not drop the parties when it set at When No OnNet Parties Remain in the Conference because the route patterns learned are classified as On Net. | Note | We recommend that you set this service parameter to Never . Any other setting can result in unintentional termination of a conference. The Drop Ad Hoc Conference service parameter works differently for conference calls that are initiated from a Cisco Unified IP Phone 7940 or 7960 that is running SIP, or a third-party phone that is running SIP . |
| Note | Drop Ad Hoc Conference feature in an ILS deployment will not drop the parties when it set at When No OnNet Parties Remain in the Conference because the route patterns learned are classified as On Net. |
| Note | We recommend that you set this service parameter to Never . Any other setting can result in unintentional termination of a conference. The Drop Ad Hoc Conference service parameter works differently for conference calls that are initiated from a Cisco Unified IP Phone 7940 or 7960 that is running SIP, or a third-party phone that is running SIP . |
| Maximum
                                                						Ad Hoc Conference | This
                                                						parameter specifies the maximum number of participants that are allowed in a
                                                						single Ad Hoc conference. Default
                                                						Value: 4 |
| Advanced
                                                						Ad Hoc Conference Enabled | This
                                                						parameter determines whether advanced Ad Hoc conference features are
                                                						enabled. This includes the ability of non-controller participants to add and
                                                						remove other participants and the ability of all participants to link ad hoc
                                                						conferences together. |
| Non-linear Ad Hoc Conference Linking Enabled | This
                                                						parameter determines whether more than two Ad Hoc conferences can be linked
                                                						directly to an Ad Hoc conference in a non-linear fashion ( three or more
                                                						conferences linked to any one conference). |
| Choose Encrypted Audio Conference Instead Of Video Conference | This parameter determines whether Unified Communications Manager chooses an encrypted audio conference bridge or an unencrypted video conference bridge for an Ad-Hoc conference call when
                                                the conference controller's Device Security Mode is set to either Authenticated or Encrypted and at least two conference participants
                                                are video-capable. Because encrypted video conference bridges are not supported in this release, Unified Communications Manager must choose between an encrypted audio conference bridge and an unencrypted video conference bridge. The default value is True . |
| Minimum  Video Capable Participants To Allocate Video Conference | This parameter specifies the number of video-capable conference participants that must be present in an Ad Hoc conference
                                                to allocate a video conference bridge. If the number of video-capable participants is less than the number specified in this
                                                parameter, Unified Communications Manager allocates an audio conference bridge. If the number of video-capable participants is equal to, or greater than, the number
                                                specified in this parameter, Unified Communications Manager allocates a video conference bridge, when available, from the configured media resource group list (MRGL). Specifying a value
                                                of zero means that video conference bridges will always be allocated, even when none of the participants on the conference
                                                are video-capable. When a conference has been established using an audio bridge and then additional video-capable participants
                                                join the conference, the conference will remain on the audio bridge and will not convert to video. The default value is 2 . |
| Allocate Video Conference Bridge For Audio Only Conferences When The Video Conference Bridge Has Higher Priority | This parameter determines whether Unified Communications Manager chooses a video conference bridge, when available, for an Ad Hoc audio-only conference call when the video conference bridge
                                                has a higher priority than an audio conference bridge in the media resource group list (MRGL). If an audio conference bridge
                                                has higher priority than any video conference bridge in the MRGL, Unified Communications Manager ignores this parameter. This parameter proves useful in situations where the local conference bridge is a video bridge (and
                                                configured in the MRGL with the highest priority) and audio conference bridges are only available in remote locations; in
                                                that situation, enabling this parameter means that Unified Communications Manager would attempt to use the local video conference bridge first, even for audio-only conference calls. The default value is False . |
| Enable
                                                						Click-to-Conference for Third-Party Applications | This parameter determines whether the Click-to-Conference functionality over the SIP trunk is enabled on Unified Communications Manager . The Click-to-Conference feature allows third-party applications to setup a conference using the SIP out of dialog REFER
                                                method and subscribe to the SIP trunk for Conference Event Package through SIP SUBSCRIBE/NOTIFY. Warning Enabling this parameter could negatively affect CTI applications that are not
                                                            						  coded to support this feature. Default
                                                						value: False | Warning | Enabling this parameter could negatively affect CTI applications that are not
                                                            						  coded to support this feature. |
| Warning | Enabling this parameter could negatively affect CTI applications that are not
                                                            						  coded to support this feature. |
| Cluster Conferencing Prefix Identifier | This parameter defines a number, up to 8 digits (e.g. 0001), that is prefixed to a conference identifier generated for Adhoc
                                                and Meet-Me conferences that will be hosted on a SIP conference bridge such as Cisco Telepresence MCU or Cisco Telepresence
                                                Conductor. This field should be populated by the administrator when there are multiple clusters in a network that will be
                                                sharing the SIP conference bridges that Unified Communications Manager manages. Every cluster should be configured with a unique prefix to ensure that the conference identifier for Adhoc and Meet-Me
                                                conferences is unique. If conference resources are not being shared across clusters, then this field may not be populated. |

| Note | Drop Ad Hoc Conference feature in an ILS deployment will not drop the parties when it set at When No OnNet Parties Remain in the Conference because the route patterns learned are classified as On Net. |
|---|---|

| Note | We recommend that you set this service parameter to Never . Any other setting can result in unintentional termination of a conference. The Drop Ad Hoc Conference service parameter works differently for conference calls that are initiated from a Cisco Unified IP Phone 7940 or 7960 that is running SIP, or a third-party phone that is running SIP . |
|---|---|

| Warning | Enabling this parameter could negatively affect CTI applications that are not
                                                            						  coded to support this feature. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Default Device Profile . The Default Device Profile Configuration window is displayed. |
|---|---|
| Step 2 | From the Device
                                             				Profile Type drop-down list, choose the phone model. |
| Step 3 | From the Device
                                             				Protocol drop-down list, choose the relevant SCCP or SIP protocol. |
| Step 4 | Set the Join
                                             				Across Lines to On . |
| Step 5 | Click Save . |

| Feature | Interaction |
|---|---|
| Conference by Using cBarge | Initiate a conference by pressing the cBarge softkey, or if the Single Button cBarge
                                          						feature is enabled, by pressing the shared-line button of the active call. When
                                          						cBarge is initiated, a barge call gets set up by using the shared conference
                                          						bridge, if available. The original call gets split and then joined at the
                                          						conference bridge. The call information for all parties gets changed to
                                          						Conference. The barged call becomes a conference call with the barge target
                                          						device as the conference controller. It can add more parties to the conference
                                          						or can drop any party. When any party releases from the call, leaving only two parties
                                          						in the conference, the remaining two parties experience a brief interruption
                                          						and then get reconnected as a point-to-point call, which releases the shared
                                          						conference resource. |
| Interaction with Call Park, Call Transfer, and Redirect | If the
                                          						conference controller transfers, parks, or redirects the conference to another
                                          						party, the party that retrieves the call acts as the virtual controller for the
                                          						conference. A virtual controller cannot add new parties to the conference nor
                                          						remove any party that was added to the conference, but a virtual controller can
                                          						transfer, park, or redirect the conference to another party, who would, in
                                          						turn, become the virtual controller of the conference. When this virtual
                                          						controller hangs up the call, the conference ends. |
| Softkey display on SIP phones | The ConfList and the Remove softkey feature is available only on SCCP phones. The SIP phones have a Show Details button with
                                          similar functionality. |

| Feature | Restrictions |
|---|---|
| Ad Hoc conference | Unified Communications Manager supports a maximum of 100 simultaneous Ad Hoc conferences for each Unified Communications Manager server. Cisco Unified Communications Manager supports a maximum of 64 participants per Ad Hoc conference (provided adequate conference resources are available). In the
                                          case of linked Ad Hoc conferences, the system considers each conference as one participant. |
| Ad Hoc conference on SIP phones: Cisco Unified IP Phone 7911 Cisco Unified IP Phone 7941 Cisco Unified IP Phone 7961 | Unified Communications Manager uses " beep" and "beepbeep" tones when a new party is added and when the new party drops from the Ad Hoc conference, respectively. When a party is added
                                          to an Ad Hoc conference, a user on a phone that is running SIP may not hear the beep; when a participant drops from the Ad
                                          Hoc conference, a user on a phone that is running SIP may not hear the "beepbeep" . Users might not hear the beeps because of the time it takes Unified Communications Manager to set up and tear down connections during the conferencing process. You can invoke Ad Hoc conference linking for phones that are running SIP only by using the Conference and Transfer functions.
                                          The system does not support Direct Transfer and Join. Supported phones that are running SIP comprise Cisco Unified IP Phone 7911, 7941, 7961. |
| Ad Hoc conference on SIP phones: Cisco Unified IP Phone 7940 Cisco Unified IP Phone 7960 Third-Party Phone | Phones display individual calls as conference calls. Cisco Unified IP Phones 7940 and 7960 can create local conference calls
                                                but not Ad Hoc conference calls. Conference list (ConfList), is not available. Remove last conference participant (RmLstC), is not available. Drop Ad Hoc conference is not supported. The SIP Profile parameter Conference Join Enabled controls behavior of the phone that is running SIP when the conference controller
                                                exits a locally hosted conference. If the Conference Join Enabled check box is unchecked, all legs disconnect when the conference
                                                controller exits the Ad Hoc conference call. If the Conference Join Enabled check box is checked, the remaining two parties
                                                stay connected. To achieve the same level of control that the Drop Ad Hoc Conference parameter settings provide for conference calls that
                                                a phone that is running SCCP initiates, the administrator can use a combination of the Conference Join Enabled SIP profile
                                                parameter and the Block OffNet to OffNet Transfer service parameter for conferences that are initiated on the phone that is
                                                running SIP ( Cisco Unified IP Phone 7940 or 60). (Because the phone that is running SIP performs a transfer when it drops out of the conference call, the Block
                                                OffNet to OffNet Transfer can prevent toll fraud by not allowing two offnet phones to remain in the call.) Unified Communications Manager uses "beep" and "beepbeep" tones when a new party is added and when the new party drops from the Ad Hoc conference, respectively. When a party is added
                                                to an Ad Hoc conference, a user on a phone that is running SIP may not hear the beep when a participant drops from the Ad
                                                Hoc conference, a user on a phone that is running SIP may not hear the "beepbeep" . Users might not hear the beeps because of the time it takes Unified Communications Manager to set up and tear down connections during the conferencing process. |
| Phone displaying "To Conference" even when two parties are connected | Configure a Call Manager cluster with Publisher (CmA11) and Subscribers (CmA2). Phones A, B, C are registered with CmA1. Phones D is registered with CmA2. Setup an consultative or blind ad-hoc conference between A(1000), B(4000), C(5000), D(6000) with A as the controller. Shutdown Cma2. Phone D will go to Preservation mode & press end call softkey . Phone A,B & C are in conference. Phone A,B & C are in conference. Disconnect Phone A ,then Phone B & C should be in a Direct call. Issue: Phone B & C are still in conference Disconnect Phone A ,then Phone B & C should be in a Direct call. Issue: Phone B & C are still in conference Disconnect Phone B, there should be no call on phone C. Phone B & C are still in conference. Issue: Phone C is still in Conference
                                                . |