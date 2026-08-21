---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeconf-html-d6d9d5a125
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeconf.html
retrieved_at: 2026-08-21T07:25:11.842541+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Conferencing

## Chapter: Conferencing

# Conferencing

## Information About Conferencing

Conferencing allows three or more parties to join a telephone conversation. Unified CME offers conferencing functionality
                           for the Unified phones and endpoints that it supports. Unified CME supports conferencing across the SIP and SCCP protocols.
                           Also, the platforms Cisco Integrated Services Router Generation 2 and Cisco 4000 Series Integrated Services Routers support
                           conferencing in Unified CME.

Cisco Cloud Services Routers (CSR) do not support DSP resources. As DSP resources are mandatory to support hardware conferencing
                                       in Unified CME, you cannot host hardware conferences in a CSR router.

## Types of Conference

Based on the conferencing method, conferencing in Unified CME is of two types:

Hardware Conferencing —Conferencing based on the Unified CME hardware and DSP resources. The types of hardware conferencing in Unified CME include:

Ad Hoc Hardware Conference

Meet Me Conference.

Connected Conference

Software Conferencing —Software Conferencing is a three party conference that is hosted on the phone or on Unified CME. The types of software conferencing
                                    in Unified CME include:

Ad Hoc Software or Built-in Bridge (BIB) Conference (Supported on Unified IP Phones such as Cisco IP Phone 7800 Series and
                                          8800 Series).

Three-Party Software Conference (For Unified CME, the support is only on Cisco Integrated Services Router Generation 2. For
                                          Cisco 4000 Series Integrated Service Routers, support is only for Unified SRST.)

The following table provides details on the support for various conferencing types in Unified CME:

Conferencing Feature

Hardware-based

Software-based (Built-in Bridge)

Max Participants

SIP

SCCP

SIP

SCCP

Ad Hoc

Yes

Yes

Yes

No (Except 8900 Series Unified IP Phones)

Ad Hoc (Hardware)—8

Ad Hoc (Software)—3

Meet Me

Yes

Yes

No

No

32

Connected

Yes (Only for 7800 and 8800 Series Unified IP Phones)

Yes (Supported as Select and Join functionality for SCCP)

No

No

8

Three-party Software Conference

No

No

No

Yes

3

Three-party software conference is supported only on Cisco Integrated Services Router Generation 2 for Unified CME. Cisco
                                          4000 Series Integrated Services Routers supports three-party software conference only for Unified SRST.

### Hardware Conference

In a hardware-based conference, the conference is established using the hardware resources of a Unified CME system. This includes
                              the routers and the Digital Signal Processors (DSPs.) From Unified CME Release 11.7, Cisco 4000 Series Integrated Services
                              Routers support hardware conferencing.

Hardware-based conferencing uses the DSP resources in a router to perform audio mixing. The DSP resources used for conferencing
                              take care of transcoding, and not just audio mixing. The participants of the conference can be IP phones that are connected
                              to Unified CME or external callers. The external callers are the participants who join the conference call over TDM or SIP
                              trunks. You must configure the DSP resources in a DSP farm for conferencing. Also, the DSP resources that are required for
                              conferencing varies based on the codec complexity. For more information, see Configure the DSP Farm Profile .

The following are the hardware-based conferencing models that are supported in Unified CME:

Ad Hoc Hardware Conference

Meet Me Conference

Connected Conference

For information on the basic configurations that are required to enable a hardware conference, see Configure Hardware Conferencing .

#### Ad Hoc Hardware Conference

Ad hoc conferences can be of two types:

Hardware-based

Software-based

For more information on Ad Hoc software conference, see Ad Hoc Software Conferencing .

Ad Hoc conferences allow the conference host or participant to add new participants to the conference. Ad hoc conferences
                                 are created when one party calls another, then either party decides to add another party and turn the call into a conference.
                                 Hence, Ad Hoc conferencing is not predetermined, but a conference call that is created instantaneously. From Cisco Unified
                                 CME Release 11.7, Cisco 4000 Series Integrated Services Routers support Ad Hoc conferencing.

Hardware Ad Hoc Conference is a conference with minimum of three participants and a maximum of eight participants. Hardware-based
                                 Ad Hoc conference uses digital signal processors (DSPs) to allow more parties than software-based ad hoc conferences and provides
                                 extra features such as Join and Conference Participant List (ConfList). Unified CME manages the conference bridge by using
                                 the DSP resources available.

For an Ad Hoc hardware conference hosted on Unified CME:

You need to configure ephone-dn as a placeholder directory number configuration for conference hosting.

From Unified CME 11.7 onwards, conference participants (line or trunk) with different codecs can be added to the conference
                                       bridge without the need for configuring extra DSP resources for LTI-based transcoding. For more information, see Local Transcoding Interface (LTI) Based Transcoding .

The conference bridge is established when minimum of three participants join the conference and becomes a point-to-point call
                                       when there are only two participants.

Ad Hoc conference supports a mixed deployment of SIP and SCCP phones.

An Ad Hoc conference supports ITSP or SIP trunk external party.

Ad Hoc conference supports the ability to play join tone when a participant joins the conference, and leave tone when a participant
                                       drops from the conference.

During a two-party transcoded call on Unified CME (Cisco 4000 Series Integrated Services Router), LTI-based transcoding is
                                       invoked. When the two-party call becomes an ad hoc conference, LTI-based transcoding is released, and SCCP-based DSP conference
                                       is invoked.

The DSP inserted for conferencing takes care of both transcoding and mixing of the audio stream.

For Unified CME 4.1 and earlier, support for ad hoc conferencing was limited to three participants—all participants on G.711
                                       codec.

You need to configure max-participant under dspfarm configuration mode to define the number of participants supported by an ad hoc conference.

Hardware-based multi-party ad hoc conference bridges do not support video phones. In a scenario where the participants joins
                                       the conference with video enabled phones, the caller on that phone can connect to the conference as an audio only participant.

When the participant puts the call on hold in a conference, the other parties in the conference remain connected. The Resume
                                       softkey is not displayed to the other active remote-in-use calls on the shared lines. Only, the participant who puts the call
                                       on hold can resume the call.

The maximum number of conference parties you can support on a hardware conference call is limited to eight.

You can setup an Ad Hoc hardware conference even if different codecs are configured on the conference parties.

The transcoder is invoked when it is a point-to-point call and its released once the conference is setup. The conference bridge
                                       performs codec mixing.

You need to configure dspfarm to support transcoding:

```
enable
	configure terminal
	dspfarm profile tag transcode universal
	codec codec_type
	maximum sessions <1-40>
	associate application CUBE
	no shutdown
	end
```

Ad Hoc hardware conferences can be created in several ways. For example, you can configure the Ad Hoc conference in Unified
                                 CME, such that:

Only the conference creator can add parties to the conference.

Any participant can add new participants to the conference (default behavior for ad hoc conference).

Conference drops when the creator hangs up.

Conference drops when the last local party hangs up.

The default behavior for termination of ad hoc conference is that the conference is not dropped provided three parties remain
                                       in the conference. It is regardless of whether the creator hangs up or not.

The maximum number of simultaneous conferences is specific to the type of Cisco Unified CME router, and each individual Cisco Unified
                                 IP phone can host a maximum of one conference at a time. You cannot create a new conference on a phone if you already have
                                 an existing conference on hold.

For information on configuration of Ad Hoc or Meet Me conferencing for SIP and SCCP phones, see Configure Ad Hoc or Meet Me Hardware Conference

#### Meet Me Conference

Meet Me conferences consist of at least three parties dialing a Meet Me conference number. . The number is predetermined by
                                 the system administrator. Hence, it is not necessary for participants to dial another party to add them into the conference.
                                 The conference host uses the MeetMe softkey on the phone and dials the designated conference number to initiate the conference. The other participants can join
                                 the conference only when the conference host has initiated the conference.

For example, the conference shown in Simple Meet Me Conference Scenario is created when the conference creator at extension 1215 presses the MeetMe softkey and hears a confirmation tone, then dials the Meet Me conference number 1500. Extension 1225 and extension 1235 join
                                 the Meet Me conference by dialing 1500. Extensions 1215, 1225, and 1235 are now parties in a Meet Me conference on extension
                                 1500.

For a Meet Me Conference in Unified CME:

Meet Me conference is supported only as a hardware-based conference.

If you configure software-based conferencing, you cannot host Meet Me conferences.

For a Meet Me conference configured for multiple ephone-dns with octo line configurations that use the same directory number,
                                       a maximum of 32 participants can join. The support for participants is based upon the configuration of DSP resources.

You can configure the maximum number of conference parties to be lower than the actual maximum of 32 for Meet Me conferences.
                                       For more information, see Configure the DSP Farm Profile .

With octo-line ephone directory numbers, only one directory number is required for an eight-party Meet Me conference. Hence,
                                       you need four ephone octo-line directory numbers for 32 parties.

The conference initiator presses MeetMe softkey before dialing the conference number. Other Meet Me conference parties (line or trunk) dials the conference number
                                       to join the conference.

If only one party remains in the Meet Me conference, (For example, if one party has forgotten to hang up and other participants
                                       have left), the conference call is disconnected after five minutes to free system resources.

If the creator is waiting for parties to join the conference (that is, only one party has joined the conference), the conference
                                       is not disconnected because significant resources are not being used.

If only one party remains in the Meet Me conference, the conference call is disconnected after five minutes to free system
                                       resources.

Maximum number of participants in a single conference with G.711 codec conference bridge is 32. For a single conference with
                                       G.729 codec conference bridge, the maximum numbe rof participants is 16.

If Music on Hold (MOH) is configured for a conference party that puts the call on hold, the MOH is not played to the other
                                       conference. This is because other parties are in an active call.

For information on configuration of Ad Hoc or Meet Me conferencing for SIP and SCCP phones, see Configure Ad Hoc or Meet Me Hardware Conference

##### Meet-Me
                                 	 Conferencing in Cisco Unified CME 11.7 and Later Versions

From Cisco Unified CME Release 11.7, Meet-Me conferencing is supported on Cisco 4000 Series Integrated Services Router.

Configuration of multi party conference on Cisco 4000 Series Integrated Services Routers for Unified CME Release 11.7 and
                                    later is same as that of previous releases. Also, the configuraton remains same across both SIP and SCCP phones. For more
                                    information, see Configure Hardware Conferencing .

#### Connected
                              	 Conference

Connected Conference supports Unified CME to host a conference for phones in connected call state. In a connected call scenario
                                 for SIP phones, a line on the phone is in an active call. The other lines are in held state. Using the Connected conference
                                 feature, you can allow one of the calls on hold to join the active call.

For Connected Conference to work on phones, you must enable Ad Hoc hardware conferencing in Unified CME.

Only Cisco IP Phone 7800 Series and Cisco IP Phone 8800 Series support Connected Conference.

Only one held call can join the active call at a time for SIP phones. If the other lines on the SIP phone have to join the
                                 conference, they can join one at a time.

Connected Conference supports a maximum of eight participants.

From Cisco Unified CME Release 11.7 onwards, Connected Conference feature is supported on SIP phones as well. As part of
                                 this enhancement, Unified CME introduced a new softkey Active calls for SIP phones.

For the Connected Conference feature, the behavior is different across Cisco IP Phone 7800 Series and Cisco IP Phone 8800
                                 Series. Cisco IP Phone 7800 Series uses the line key for Connected Conference feature. However, Cisco IP Phone 8800 Series
                                 uses Active calls softkey.

Following are the
                                 		steps to invoke connected conferencing on Cisco IP Phone 8800 Series:

A call from
                                       			 Phone A (Cisco IP Phone 8800 Series) is answered by Phone B.

Phone A puts the
                                       			 call with Phone B on hold.

Phone A makes
                                       			 another call to Phone C, and the call is answered by Phone C.

Press the Conference hard button or softkey on Phone A.

Then, press
                                       			 the Active calls softkey on Phone A to select the option
                                       			 Phone B.

Repeat the
                                       			 above steps to add more parties into conference.

A connected
                                 		conference between Cisco IP Phone 8800 Series Phone A, Phone B, and Phone C is
                                 		established.

Following are the
                                 		steps to invoke connected conferencing on Cisco IP Phone 7800 Series:

A call from
                                       			 Phone A (Cisco IP Phone 7800 Series) is answered by Phone B.

Phone A puts
                                       			 the call with Phone B on hold.

Phone A makes
                                       			 another call to Phone C, and the call is answered by Phone C.

Use the line
                                       			 key on Phone A to select the option Phone B.

Repeat the preceding steps to add more parties into conference.

A connected
                                 		conference between Cisco IP Phone 7800 Series IP Phone A, Phone B, and Phone C
                                 		is established.

The phone firmware files that support Connected Conference on Cisco IP
                                             		  Phone 8800 Series is unavailable until the next Unified CME release. Hence,
                                             		  Connected Conference support for SIP phones is limited to Cisco IP Phone 7800
                                             		  Series for Unified CME Release 11.7.

#### cBarge Conference

cBarge enables multiple phone users who share a directory number to join an active call on the shared line by pressing a softkey.
                                 cBarge facilitates a conference by invoking hardware conference on Unified CME. When the conference initiator barges into
                                 a call, hardware conference is created on Unified CME. The conference is established between the barge initiator, the target
                                 party, and the other parties connected in the call.

To support cBarge:

Enable hardware conference

Disable Privacy

If hardware conference is disabled, cBarge softkey invokes barge. Barge uses the built-in conference bridge on the target
                                 phone (the phone that is barged).  Hence, a barge conference supports only up to three parties. Configure cBarge if you must
                                 support more participants.

Even if you have configured cBarge softkey, the softkey display on the phone is Barge .

The configurations for cBarge on the conference bridge of Unified CME are same as an Ad Hoc hardware conference, except:

The configuration to enable cBarge softkey on phone in remote-in-use state.

Configure no privacy under voice register global .

To configure softkey template to enable cBarge softkey on phone in remote-in-use:

```
enable
	configure terminal
	voice register template <template-tag>
	    softkeys remote-in-use {[ Barge ] [ Newcall ] [ cBarge ]}
	exit
```

To associate softkey template with the pool:

```
voice register pool <phone-tag>
	    template <template-tag>
	end
```

To disable privacy and enable conference hardware under voice register global configuration mode:

```
voice register global
	    no privacy
	    conference hardware                                   
	    create profile
	    reset
	end
```

For more information on Barge and cBarge, see Barge and cBarge .

##### Drop Mode Conference

A person who initiates a conference call and hangs up can either keep the remaining parties connected or disconnect them.
                                    Based on this configuration option, Unified CME supports Drop Mode Conference as an End of Conference option for Hardware
                                    Conferencing.

To configure the mode for terminating hardware conferences when parties drop out, use the conference drop-mode and conference add-mode command in ephone or ephone-template configuration mode for SCCP phones. Configure conference drop-mode and conference add-mode command in voice register configuration mode for SIP phones.

The behavior for the end of three-way conferences can be configured at a phone level. The options specify whether the last
                                    party that joined a conference can be dropped from the conference and whether the remaining two parties should be allowed
                                    to continue their connection after the conference initiator has left the conference.

For information on configuration of Drop Mode and Add Mode for hardware conferencing, see Configure Softkeys and End of Conference Options for Hardware Conferencing

For more information on configuration of Add Mode and Drop Mode Conference for SCCP phones, see conference add-mode and conference drop-mode .

For more information on configuration of Add Mode and Drop Mode Conference for SIP phones, see conference add-mode (voice register) conference drop-mode (voice register) .

### Software Conference

Software conference can host a maximum of three participants. There are two types of software-based conferencing available
                              in Unified CME:

Ad Hoc Software Conference—Ad Hoc Software Conference or Built-in Bridge Conference is established using the phone or endpoint
                                    hardware that provides audio mixing. There is no dependency upon the Unified CME router hardware for Ad Hoc software conferencing.

Three-Party Software Conference—In a three-party software conference, Unified CME router supports conferencing for phones
                                    that do not support BIB-based conferencing (SCCP phones). When BIB conference is enabled, three-party software conference
                                    is disabled. It is supported only on Cisco Integrated Services Router Generation 2 and only for SCCP phones. For information
                                    on how to configure a three-party software conference, see Configure Three-Party Software Conference .

#### Ad Hoc Software Conferencing

Ad Hoc software conference is also known as Built-in bridge (BIB) conferencing. Ad hoc software conferences do not depend
                                 on the Unified CME hardware to support conferencing. Press the conferencing softkey on the phone that hosts the conference
                                 bridge to enable the Ad Hoc software conference. In an Ad Hoc software conference, the phone that hosts the conference also
                                 performs audio mixing.

The conference that is shown in AdHoc Software Conference Using the Conference Softkey is created when extension 1215 dials extension 1225. The two parties decide to add a third party, extension 1235. Extensions
                                 1215, 1225, and 1235 are now parties in an ad hoc conference. Extension 1215 is the conference initiator. Hence, audio mixing
                                 happens in 1215.

For a software-based Ad Hoc conference:

The number of participants is limited to three parties.

You do not need Unified CME hardware or DSP resources for audio mixing.

The phone that hosts the conference performs audio mixing.

Transcoding is not supported in a software-based conference call. Hence, you cannot host a software conference for calls with
                                       different audio codecs.

Software conference is enabled using softkeys on the Unified IP phones. The softkey varies depending on the phone model used. confrn and conference are some of the common softkeys for Software Conferencing in Unified IP Phones.

To configure a software conference, you have to disable hardware conferencing in Unified CME:

Configure no conference hardware under telephony service for SCCP phones and no conference hardware under voice register global for SIP phones to disable hardware conference.

Also, you must configure create profile under voice register global and create cnf-files under telephony-service configuration mode.

##### Keep Conference

A person who initiates a conference call and hangs up can either keep the remaining parties connected or disconnect them.
                                    Based on this configuration option, Unified CME supports Keep Conference as an End of Conference option for Software Conferencing.

Keep Conference is an end of conference option in Software Conferencing. With Keep Conference option, Unified IP phones can
                                    be configured to keep the remaining conference parties connected when the conference initiator hangs up (places the handset
                                    back in the on-hook position). Conference originators can disconnect from their conference calls by pressing the Confrn (conference) soft key. When an initiator uses the Confrn key to disconnect from the conference call, the oldest call leg will be put on hold, leaving the initiator connected to the
                                    most recent call leg. The conference initiator can then navigate between the two parties by pressing either the Hold soft
                                    key or the line buttons to select the desired call.

The behavior for the end of three-way conferences can be configured at a phone level. The options specify whether the last
                                    party that joined a conference can be dropped from the conference and whether the remaining two parties should be allowed
                                    to continue their connection after the conference initiator has left the conference.

For information on configuration of Keep Conference for SCCP phones, see Configure Keep Conference for SCCP Phones .

For an example of Keep Conference for SCCP phones, see Example for Keep Conference Configuration on SCCP Phones .

For information on configuration of Keep Conference for SIP phones, see Configure Keep Conference Option for SIP Phones .

For an example of Keep Conference for SIP phones, see Example for Keep Conference Configuration on SIP Phones .

##### Max Conference

You can set the maximum number of three-party software conferences that are supported simultaneously by the Unified CME router
                                    using Max Conference option. Configure the max-conferences command in telephony-service configuration mode to define maximum number of software conferences.

For Max Conference in Unified CME, the configuration is same for both SIP and SCCP phones.

For information on configuration of max-conferences , see Configure Three-Party Software Conference .

For an example of Max conference, see Example for Configuration of Max Conference and Gain Levels .

###### Conference Gain Levels

You can adjust the gain level of an external call to provide more adequate volume. This functionality is applied to inbound
                                       audio packets so that conference participants can more clearly hear a remote PSTN or VoIP caller joining their call. Note
                                       that this functionality cannot discriminate between a remote VoIP/foreign exchange office (FXO) source, which requires a volume
                                       gain, and a remote VoIP/IP phone, which does not require a volume gain and may therefore incur some sound distortions.

Conference gain levels are set using the variable gain configured under the CLI command max-conference under telephony-service configuration mode. The Conference Gain Level configuration is consistent across all the hardware conferencing options supported
                                       in Unified CME. For more information, see Configure Three-Party Software Conference .

For an example of Max conference, see Example for Configuration of Max Conference and Gain Levels .

## Design Considerations for Conferencing

The following are some of the characteristics of conferencing in Unified CME:

The maximum number of conference participants that you can host in a conference is specific to the mode of conference. For
                                 more information, see Types of Conference .

Consider a scenario where the ad hoc hardware conference creator transfers the call or parks the call with another call. For
                                 Unified CME 11.7 and later releases, the conference bridge remains active, irrespective of whether you have enabled drop-mode creator CLI command or not.

When you are configuring dial peers or ephone-dns (including park slots and conferencing extensions) on Cisco Integrated Services
                                 Router Voice Bundles, the following message may appear to warn you that memory is not available:

%DIALPEER_DB-3-ADDPEER_MEM_THRESHOLD: Addition of dial-peers limited by available memory

To configure more dial peers or ephone-dns, increase the DRAM in the system. Moderately complex configuration may exceed the
                                 default 256 MB of DRAM and require 512 MB of DRAM. Many factors contribute to memory usage, in addition to the number of dial
                                 peers and ephone-dns configured.

Secure Conferencing in Unified CME —If Unified CME uses a conference DSP farm resource for Ad Hoc or Meet Me hardware conference, it can use a secure or nonsecure
                                 DSP farm resource. However, it is recommended that you pick a nonsecure DSP farm resource for Unified CME. This is because
                                 the conference itself cannot be secure in Unified CME. Also, you can avoid wastage of the session capacity of the more expensive
                                 secure DSP farm resource.

To avoid using valuable secure DSP farm resources, we recommend that you do not register a secure conference DSP farm profile
                                 to a Unified CME. Unified CME cannot use the DSP farm’s secure capabilities.

LTI-based Transcoding —From Unified CME 11.7 onwards, LTI-based transcoding is supported for hardware conferencing in Unified CME. With LTI-based
                                 transcoding, conference participants (line or trunk) with different codecs can be added to the conference bridge without configuring
                                 extra DSP resources. During a two-party transcoded call on Unified CME (Cisco 4000 Series Integrated Services Router), LTI-based
                                 transcoding is invoked. When the two-party call becomes an Ad Hoc conference, LTI-based transcoding is released and SCCP-based
                                 DSP conference is invoked. The DSP inserted for conferencing takes care of both transcoding and mixing the audio stream. For
                                 information about LTI-based conferencing and configuration, see Local Transcoding Interface (LTI) Based Transcoding and Configure LTI-based Transcoding .

Conference Blocking (Conference Pattern Blocked) —To prevent extensions in an ephone or a voice register pool from initiating conferences, configure the conference-pattern blocked command . For more information, see Conference-Pattern Blocked and Configure Conference Blocking Options for Phones .

Conference Max Length —When conference max-length command is configured, Unified CME allows the conferences only if the dialed digits are within the max-length limit. For
                                 more information on Conference Max-length and configuration, see Conference Max-Length and Configure the Maximum Number of Digits for a Conference Call .

Octo-line Directory Numbers —With octo-line directory numbers, only one directory number is required for an eight-party Meet Me or Ad Hoc conference.
                                 An octo-line directory number supports up to eight active calls, both incoming and outgoing, in a single phone button. It
                                 supports up to eight Select and Join instances. When a conference initiator is an octo-line directory number, Unified CME
                                 selects an idle channel from that directory number. Establish a new call to complete the conference. If an idle channel is
                                 not available in the same octo-line directory number, the conference terminates and a No Line Available message displays.

If an idle channel is not available in the same octo-line directory number, Unified CME does not pick an idle channel from
                                             another directory number. Also, you cannot select hold calls in the other channels of the directory number or for other directory numbers. It is supported only for single-line
                                             and dual-line directory numbers.

### Deploy the DSP Farm Resource with Unified CME

It is mandatory to have DSP farm resources to support hardware conferencing in Unified CME. For more information on configuration
                              of DSP resources with Unified CME, see Configure Transcoding Resources .

You can deploy a DSP farm with Unified CME in two ways:

Configure DSP Farm and Unified CME in the same router.

For a sample configuration, see Example of DSP Farm and Cisco Unified CME on the Same Router .

Configure DSP Farm and Unified CME in different routers.

For a sample configuration, see Example of DSP Farm and Cisco Unified CME on Different Routers .

## Softkeys for Conference Functions

For the conferencing functions that you configure on Unified CME, you have corresponding softkeys on the phone. The following
                           soft keys provide conferencing functions for conferencing enhancements on your phone:

ConfList—Conference list. Lists all parties in a conference. For multi-party ad hoc conferences, this soft key is available
                                 for all parties in a conference. For meet-me conferences, this soft key is available for the creator only. Press Update to update the list of parties in the conference. For instance, press Update to verify that a party has been removed from the conference. Press Remove softkey to remove the appropriate parties. The suboption Remove is available for the conference creator and phones that have conference admin configured.

Join—Joins an established call to an adhoc conference. You must first press Select to choose each connected call that you want to join in a conference, then press Join to join the selected calls.

RmLstC—Remove last caller. Removes the last party added to the conference. This soft key works for the creator only.

Select—Selects a call or conference to join to a conference and selects a call to remove from a conference. The creator can
                                 remove other parties by pressing the ConfList soft key, then use the Select and Remove soft keys to remove the appropriate parties.

MeetMe—Initiates a Meet Me conference. The creator presses this soft key before dialing the conference number. Other meet-me
                                 conference parties only dial the conference number to join the conference. This soft key must be configured before you can
                                 start a Meet Me conference.

In Cisco Unified CME
                           		11.7 and later versions, the following softkeys are also supported.

Details (Supported only on Cisco IP Phone 7800 Series)—Lists all the participants in a conference. For multi-party ad hoc
                                 conferences, this soft key is available for all parties in a conference. For meet-me conferences, this soft key is available
                                 for the creator only. Press Update to update the list of parties in the conference. Press Remove softkey to remove the appropriate parties. The suboption Remove is available to the conference creator and phones that have conference admin configured.

Show detail (Supported only on Cisco IP Phone 8800 Series)—Lists all the participants in a conference. For multi-party ad
                                 hoc conferences, this soft key is available for all parties in a conference. For meet-me conferences, this soft key is available
                                 for the creator only. Press Update to update the list of parties in the conference. Press Remove softkey to remove the appropriate parties. The suboption Remove is available to the conference creator and phones that have conference admin configured.

Active calls (Supported on Cisco IP Phone 8800 Series)—As part of the Connected Conference support on Unified CME 11.7 and
                                 later releases, a new softkey Active calls is introduced. The Active calls softkey is added to the SIP phones configured on Unified CME. Active calls softkey is used in Cisco IP Phone 8800 Series for Unified CME.

For more information on the configuration, see Configure Hardware Conferencing .

## Restrictions for Conferencing

Unified CME does not support secure conferencing. All conference calls are nonsecure. This is because Unified CME cannot use
                                 the secure conference DSP farm capability.

For a phone registered to Unified CME, you can support only one conference. If an existing conference is put on hold, you
                                 cannot create another conference.

For calls having different audio codecs, you cannot host a hardware conference call without transcoding (DSPs).

For calls having different audio codecs, you cannot host a software conference in Unified CME. The calls do not merge into
                                 a conference.

A Software (BIB) conference does not support more than three parties.

Cisco Jabber is supported only by hardware conferencing in Unified CME.

At a time, only one held call can be selected to join the Connected conference for SIP phones.

Each individual Unified IP phone can host a maximum of one conference at a time. You cannot support a new conference in a
                                 phone if you have a conference on hold.

For cBarge, the conference type is listed as Ad Hoc Barge instead of Ad Hoc.

For cBarge, Caller ID on phones in the Barge conference is displayed as Barge instead of Conference .

Configurations, limitations and attributes associated with Connected Conference on Unified CME is same as that for Ad Hoc
                                 hardware conference.

## Configure Software Conferencing

### Configure Three-Party Software Conference

You can configure software conferencing on Unified CME as follows. To globally modify the default configuration and change
                                 any of the following parameters for three-party software conferencing, perform the following steps.

The configuration no conference hardware is required to enable software conferencing on Unified CME  and BIB conferencing on phones.

Maximum number of simultaneous three-party software conferences that are supported by a router is platform-dependent. The
                                       default value is half of the maximum number.

Increase the sound volume of VoIP and public switched telephony network (PSTN) parties joining a conference call.

For Max Conference and Gain level in Unified CME, the configuration is consistent across SIP and SCCP phones.

Restriction

When a three-way software conference is established, a participant cannot use call transfer to join the remaining conference
                                                   participants to a different number.

Three-party software conferencing does not support meet-me conferences.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- max-conferences max-conference-number [ gain -6 | 0 | 3 | 6 ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)#
```

Enters
                                             				telephony-service configuration mode.

Step 4

max-conferences max-conference-number [ gain -6 | 0 | 3 | 6 ]

#### Example:

```
Router(config-telephony)# max-conferences 6
```

Sets the maximum number of simultaneous three-party conferences that are supported by the router.

max-conference-number —Maximum value is platform-dependent. Type ? for maximum value. Default is half of the maximum value.

gain —(Optional) Amount to increase the sound volume of VoIP and PSTN calls joining a conference call, in decibels. Valid values
                                                   are -6 , 0 , 3 , and 6 . The default is -6 .

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure Keep Conference for SCCP Phones

Keep Conference is supported only for BIB Conferencing.

Keep Conference on SCCP is supported only for Cisco Integrated Services Router Generation 2.

To configure optional end-of-conference options for three-party ad hoc conferencing on a Cisco Unified IP phone running Skinny
                                       Client Control Protocol (SCCP), perform the following steps for each phone to be configured.

#### Before you begin

Conferencing
                                          				uses call transfer to connect the two remaining parties of a conference when a
                                          				conference initiator leaves the conference. To use this feature, you must
                                          				configure the transfer-system command. For configuration information, see Configure Call Transfer and Forwarding .

Drop-last
                                          				feature of Keep Conference on analog phones connected to the Cisco Unified CME
                                          				system through a Cisco VG 224 requires Cisco IOS Release 12.4(9)T or later
                                          				release.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- keep-conference [ drop-last ] [ endcall ] [ local-only ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                      					 this ephone during configuration tasks.

Step 4

keep-conference [ drop-last ] [ endcall ] [ local-only ]

#### Example:

```
Router(config-ephone)# keep-conference endcall
```

Allows
                                             				conference initiators to exit from conference calls and to either end or
                                             				maintain the conference for the remaining parties.

no keep-conference —(Default; the no form of
                                                      					 the command) The conference initiator can hang up or press the EndCall soft key
                                                      					 to end the conference and disconnect all parties or press the Confrn soft key
                                                      					 to drop only the last party that was connected to the conference.

keep-conference —(No keywords used) The conference
                                                      					 initiator can press the EndCall soft key to end the conference and disconnect
                                                      					 all parties or hang up to leave the conference and keep the other two parties
                                                      					 connected. The conference initiator can also use the Confrn soft key (IP phone)
                                                      					 or hookflash (analog phone) to break up the conference but stay connected to
                                                      					 both parties.

drop-last —The action of the Confrn soft key is
                                                      					 changed; the conference initiator can press the Confrn soft key (IP phone) or
                                                      					 hookflash (analog phone) to drop the last party.

endcall —The action of the EndCall soft key is
                                                      					 changed; the conference initiator can hang up or press the EndCall soft key to
                                                      					 leave the conference and keep the other two parties connected.

local-only —The conference initiator can hang up to
                                                      					 end the conference and leave the other two parties connected only if one of the
                                                      					 remaining parties is local to the Cisco Unified CME system (an internal
                                                      					 extension).

Step 5

end

#### Example:

```
Router(config)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If you are
                                 		  finished modifying the configuration, you are ready to generate configuration
                                 		  files for the phones to be connected. See Generate Configuration Profiles for SIP Phones .

### Configure Keep Conference Option for SIP Phones

To configure
                                 		  optional end-of-conference options for three-party ad hoc conferencing on a
                                 		  Cisco Unified IP phone running SIP, perform the following steps for each phone
                                 		  to be configured.

#### Before you begin

To facilitate
                                          				call transfer by using the Confrn soft key, conference, and transfer attended
                                          				or transfer blind must be enabled. For configuration information, see Configure Call Transfer and Forwarding .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag | OR voice register template template-tag

- keep-conference

- voice register
                                       				  pool pool-tag

- template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register pool pool-tag | OR voice register template template-tag

#### Example:

```
Router(config)# voice register pool 3
```

```
Router(config)# voice register template 3
```

Enters voice
                                             				register pool or voice register template configuration mode to set
                                             				phone-specific parameters for SIP phones.

pool-tag —Unique sequence number of the SIP phone
                                                      					 to be configured. Range is 1 to 100 or the upper limit as defined by max-pool command.

template-tag —Unique
                                                      					 sequence number of the template to be applied to the SIP phone. Range is 1 to
                                                      					 10.

Step 4

keep-conference

#### Example:

```
Router(config-register-pool)# keep-conference
```

```
Router(config-register-temp)# keep-conference
```

Allows a
                                             				Cisco Unified IP phone conference initiator to exit from conference calls and
                                             				keeps the remaining parties connected.

This step is
                                                         				  included to illustrate how to enable the command if it was previously disabled.

Default is
                                                      					 enabled.

Remaining
                                                      					 calls are transferred without consultation as enabled by the transfer-attended (voice register template) or transfer-blind (voice register template) commands.

keep-conference command is configured
                                                         				  under voice register template only if you configure voice register template
                                                         				  command in the previous step.

Step 5

voice register
                                                				  pool pool-tag

#### Example:

```
Router(config-register-temp)# voice register pool 1
```

(Optional) Enters voice register pool configuration mode to set
                                             				phone-specific parameters for SIP phones.

This step is required only if you configure voice register
                                                         				  template.

Step 6

template template-tag

#### Example:

```
Router(config-register-pool)# template 1
```

(Optional) Attaches the
                                             				template tag configured to the voice register pool.

This step is required only if you configure voice register
                                                         				  template.

Step 7

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If you are
                                          				finished modifying the configuration, you are ready to generate configuration
                                          				files for the phones to be connected. See Generate Configuration Profiles for SIP Phones .

## Configure Hardware Conferencing

Prerequisites

The following configuration is applicable to all hardware conferencing types supported in Unified CME, including Meet Me and
                                 Ad Hoc conferencing.

DSP resources are mandatory to support a hardware conference in Unified CME.

Restriction

The maximum number of meet-me conference parties is 32 for one DSP using the G.711 codec and 16 for the G.729 codec.

A participant cannot join more than one conference at the same time.

Hardware-based multi-party ad hoc conferencing for more than three parties is not supported on phones that do not support
                                             soft keys.

Hardware based Ad Hoc conferencing does not support the local-consult transfer method ( transfer-system local-consult command).

### Enable DSP Farm
                           	 Services for a Voice Card

To enable DSP farm services for a voice card to support hardware conferences, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- voice-card slot

- dsp services dspfarm

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice-card slot

#### Example:

```
Router(config)# voice-card 2
```

Enters
                                             				voice-card configuration mode and configure a voice card.

Step 4

dsp services dspfarm

#### Example:

```
Router(config-voicecard)# dsp services dspfarm
```

Enables
                                             				digital-signal-processor (DSP) farm services for a particular voice network
                                             				module.

Step 5

exit

#### Example:

```
Router(config-voicecard)# exit
```

Exits
                                             				voice-card configuration mode.

### Configure Join and Leave Tones

The Join and Leave configuration is applicable for:

both SIP and SCCP phones in Unified CME.

all hardware conferencing types supported in Unified CME, including Ad Hoc and Meet Me.

To configure tones
                                 		  to be played when parties join and leave multi-party ad hoc conferences and
                                 		  meet-me conferences, perform the following steps for each tone to be
                                 		  configured.

### SUMMARY STEPS

- enable

- configure terminal

- voice class custom-cptone cptone-name

- dualtone conference

- frequency frequency-1 [ frequency-2 ]

- cadence { cycle-1-on-time cycle-1-off-time [ cycle-2-on-time cycle-2-off-time ] [ cycle-3-on-time
                                       				  cycle-3-off-time ] [ cycle-4-on-time cycle-4-off-time ] | continuous }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice class custom-cptone cptone-name

#### Example:

```
Router(config)# voice class custom-cptone jointone
```

Creates a
                                             				voice class for defining custom call-progress tones to be detected.

Step 4

dualtone conference

#### Example:

```
Router(cfg-cptone)# dualtone conference
```

Configures
                                             				conference join and leave tones.

Step 5

frequency frequency-1 [ frequency-2 ]

#### Example:

```
Router(cfg-cp-dualtone)# frequency 600 900
```

Defines the
                                             				frequency components for a call-progress tone.

Step 6

cadence { cycle-1-on-time cycle-1-off-time [ cycle-2-on-time cycle-2-off-time ] [ cycle-3-on-time
                                                				  cycle-3-off-time ] [ cycle-4-on-time cycle-4-off-time ] | continuous }

#### Example:

```
Router(cfg-cp-dualtone)# cadence 300 150 300 100 300 50
```

Defines the
                                             				tone-on and tone-off durations for a call-progress tone.

Step 7

end

#### Example:

```
Router(cfg-cp-dualtone)# exit
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure SCCP Infrastructure for Conferencing in Unified CME

The SCCP Infrastructure configuration is applicable to:

Both SIP and SCCP phones in Unified CME.

All hardware conferencing types supported in Unified CME, including Ad Hoc and Meet Me.

To enable SCCP Infrastructure in Unified CME to support multi-party ad hoc and meet-me conferences, perform the following
                                 steps:

### SUMMARY STEPS

- enable

- configure terminal

- sccp local interface-type interface-number [ port port-number ]

- sccp ccm { ip-address | dns } identifier identifier-number [ port port-number ][ version version-number ]

- sccp ccm group group-number

- bind interface interface-type interface-number

- exit

- sccp

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

sccp local interface-type interface-number [ port port-number ]

#### Example:

```
Router(config)# sccp local FastEthernet0/0
```

Selects the
                                             				local interface that SCCP applications (transcoding and conferencing) use to
                                             				register with Cisco Unified CME.

Step 4

sccp ccm { ip-address | dns } identifier identifier-number [ port port-number ][ version version-number ]

#### Example:

```
Router(config)# sccp ccm 10.4.158.3 identifier 100 version 4.0
```

Enables the
                                             				Cisco Unified CME router to register SCCP applications.

version-number —Must be set to 4.0 or later.

Step 5

sccp ccm group group-number

#### Example:

```
Router(config)# sccp ccm group 123
```

Creates a
                                             				Cisco Unified CME group.

Step 6

bind interface interface-type interface-number

#### Example:

```
Router(config-sccp-cm)# bind interface fastethernet 0/0
```

Binds an
                                             				interface to a Cisco Unified CME group.

Step 7

exit

#### Example:

```
Router(config-sccp-cm)# exit
```

Exits SCCP
                                             				Cisco Unified CME configuration mode.

Step 8

sccp

#### Example:

```
Router(config)# sccp
```

Enables SCCP
                                             				and its related applications (transcoding and conferencing).

Step 9

exit

#### Example:

```
Router(config)# exit
```

Exits global
                                             				configuration mode.

### Configure the DSP Farm Profile

The DSP Farm Profile is applicable to:

Both SIP and SCCP phones in Unified CME.

All hardware conferencing types supported in Unified CME, including Ad Hoc and Meet Me.

To configure the
                                 		  DSP farm profile for multi-party ad hoc and meet-me conferencing, perform the
                                 		  following steps.

The DSP farm can
                                             			 be on the same router as the Cisco Unified CME or on a different router.

### SUMMARY STEPS

- enable

- configure terminal

- dspfarm profile profile-identifier conference

- codec { codec-type | pass-through }

- conference-join custom-cptone cptone-name

- conference-leave custom-cptone cptone-name

- maximum conference-participants max-participants

- maximum sessions number

- associate application sccp

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

dspfarm profile profile-identifier conference

#### Example:

```
Router(config)# dspfarm profile 1 conference
```

Enters DSP
                                             				farm profile configuration mode and defines a profile for DSP farm services.

Step 4

codec { codec-type | pass-through }

#### Example:

```
Router(config-dspfarm-profile)# codec g711ulaw
```

Specifies the
                                             				codecs supported by a DSP farm profile.

Repeat this
                                                         				  step as necessary to specify all the supported codecs.

Step 5

conference-join custom-cptone cptone-name

#### Example:

```
Router(config-dspfarm-profile)# conference-join custom-cptone jointone
```

Associates a
                                             				custom call-progress tone to indicate joining a conference with a DSP farm
                                             				profile.

The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card .

Step 6

conference-leave custom-cptone cptone-name

#### Example:

```
Router(config-dspfarm-profile)# conference-leave custom-cptone leavetone
```

Associates a
                                             				custom call-progress tone to indicate leaving a conference with a DSP farm
                                             				profile.

The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card .

Step 7

maximum conference-participants max-participants

#### Example:

```
Router(config-dspfarm-profile)# maximum conference-participants 32
```

(Optional)
                                             				Configures the maximum number of conference parties allowed in each meet-me
                                             				conference. The maximum is codec-dependent.

Step 8

maximum sessions number

#### Example:

```
Router(config-dspfarm-profile)# maximum sessions 8
```

Specifies the
                                             				maximum number of sessions that are supported by the profile.

Step 9

associate application sccp

#### Example:

```
Router(config-dspfarm-profile)# associate application sccp
```

Associates
                                             				SCCP with the DSP farm profile.

Step 10

end

#### Example:

```
Router(config-dspfarm-profile)# end
```

Exits to
                                             				privileged EXEC mode.

### Associate Unified CME with a DSP Farm Profile

The steps to associate Unified CME with a DSP farm profile is applicable to:

Both SIP and SCCP phones in Unified CME.

All hardware conferencing types supported in Unified CME, including Ad Hoc and Meet Me.

To associate a DSP
                                 		  farm profile with a group of Cisco Unified CME routers that control DSP
                                 		  services, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- sccp ccm group group-number

- associate ccm identifier-number priority priority-number

- associate profile profile-identifier register device-name

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

sccp ccm group group-number

#### Example:

```
Router(config)# sccp ccm group 1
```

Creates a
                                             				Cisco Unified CME group.

Step 4

associate ccm identifier-number priority priority-number

#### Example:

```
Router(config-sccp-ccm)# associate ccm 100 priority 1
```

Associates a
                                             				Cisco Unified CME router with the group and establishes its priority within the
                                             				group.

Step 5

associate profile profile-identifier register device-name

#### Example:

```
Router(config-sccp-ccm)# associate profile 2 register confdsp1
```

Associates a
                                             				DSP farm profile with the Cisco Unified CME group.

device-name is a maximum of 16 characters.

Repeat this
                                                         				  step for every conferencing DSP farm and transcoding DSP farm.

Step 6

end

#### Example:

```
Router(config-sccp-ccm)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable Hardware Conferencing

To allow hardware-based multi-party conferences with more than three parties, perform the following steps.

You cannot configure Hardware and Software conference simultaneously in Unified CME. Configuring multi-party hardware conference
                                                   in Unified CME disables three-party Ad Hoc software conferencing.

This configuration is applicable to both SIP and SCCP phones in Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- conference hardware

- transfer-system full-consult

- sdspfarm units number

- sdspfarm tag number device-name

- sdspfarm conference mute-on mute-on-digits mute-off mute-off-digits

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

conference hardware

#### Example:

```
Router(config-telephony)# conference hardware
```

Configures a
                                             				Cisco Unified CME system for multi-party conferencing only.

Step 5

transfer-system full-consult

#### Example:

```
Router(config-telephony)# transfer-system full-consult
```

Transfers
                                             				calls using H.450.2 with consultation using a second phone line, if available.

The calls fall back to full-blind if a second line is not available.

This is the default transfer method in Cisco Unified CME 4.0 and later versions.

Step 6

sdspfarm units number

#### Example:

```
Router(config-telephony)# sdspfarm units 3
```

Specifies the
                                             				maximum number of DSP farms that are allowed to be registered to the SCCP
                                             				server.

Step 7

sdspfarm tag number device-name

#### Example:

```
Router(config-telephony)# sdspfarm tag 2 confdsp1
```

Permits a DSP
                                             				farm to register to Cisco Unified CME and associates it with a SCCP client
                                             				interface's MAC address.

The device-name in this step must be the same as the device-name in the associate
                                                               						profile command in Step 5 of the section Associate Unified CME with a DSP Farm Profile .

Step 8

sdspfarm conference mute-on mute-on-digits mute-off mute-off-digits

#### Example:

```
Router(config-telephony)# sdspfarm conference mute-on 111 mute-off 222
```

Defines
                                             				mute-on and mute-off digits for conferencing.

Maximum: 3 digits. Valid values are the numbers and symbols that appear on your telephone keypad: 1, 2, 3, 4, 5, 6, 7, 8,
                                                   9, 0, *, and #.

Mute-on and mute-off digits can be the same.

Step 9

end

#### Example:

```
Router(config-telephony)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure Ad Hoc or Meet Me Hardware Conference

The configuration steps are applicable to:

Both SIP and SCCP phones in Unified CME.

All hardware conferencing types supported in Unified CME.

To configure extension numbers for hardware conferencing based on the maximum number of conference participants you configure,
                                 perform the following steps. Ad Hoc conferences require four extensions per conference, regardless of how many extensions
                                 are actually used by the conference parties.

For Meet Me conference to be enabled, you need to press the MeetMe softkey on the phone as well.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag octo-line

- number number [ secondary number ] [ no-reg [ both | primary ]]

- Enter one of the following commands:

- conference ad-hoc

- conference meetme

- preference preference-order [ secondary secondary-order ]

- no huntstop [ channel ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag octo-line

#### Example:

```
Router(config)# ephone-dn 18 octo-line
```

Enters ephone-dn configuration mode to configure an extension (ephone-dn) for a phone line.

Each ephone-dn can carry eight parties if it is configured as an octo line.

Configure enough ephone-dns to accommodate the maximum number of conference participants to be supported.

For multi-party ad hoc conferencing, maximum number of directory numbers is 8, but you can configure a lower maximum.

For meet-me conferencing, maximum number of directory numbers is 32, but you can configure a lower maximum.

Minimum number of directory numbers required: 2.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 6789
```

Associates a
                                             				telephone or extension number with an ephone-dn in a Cisco Unified CME system.

Each DN
                                                      					 for a conference must have the same primary and secondary number.

Step 5

Enter one of the following commands:

- conference ad-hoc

- conference meetme

#### Example:

```
Router(config-ephone-dn)# conference ad-hoc
```

```
Router(config-ephone-dn)# conference meetme
```

Configures a number as a placeholder for ad hoc conferencing to associate the call with the DSP farm.

or

(Optional) Associates meet-me conferencing with a directory number.

Step 6

preference preference-order [ secondary secondary-order ]

#### Example:

```
Router(config-ephone-dn)# preference 1
```

Sets dial-peer
                                             				preference order for an extension (ephone-dn) associated with a
                                             				Cisco Unified IP phone.

Remember
                                                      					 to configure “preference x” with low value to last DN.

The lower
                                                      					 the value of the preference-order argument, the higher the
                                                      					 preference of the extension.

Step 7

no huntstop [ channel ]

#### Example:

```
Router(config-ephone-dn)# no huntstop
```

Continues
                                             				call hunting behavior for an extension (ephone-dn) or an extension channel.

Remember
                                                      					 to configure no huntstop for all DNs except the last one.

Step 8

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure Softkeys and End of Conference Options for Hardware Conferencing

To configure a
                                 		  template of conferencing features such as the add party mode, drop party mode,
                                 		  and soft keys for hardware-based multi-party ad hoc and meet-me conferences and
                                 		  apply the template to a phone, perform the following steps.

The following
                                             			 commands can also be configured in ephone configuration mode. Commands
                                             			 configured in ephone configuration mode have priority over commands in
                                             			 ephone-template configuration mode.

Restriction

The ConfList (including the Remove, Update, and Exit soft keys within the ConfList function) and RmLstC soft keys do not work
                                                   on a Cisco Unified IP Phone 7902, 7935, and 7936.

The RmLstC, ConfList, Join, and Select functions and soft keys are not supported for software-based conferencing.

The steps to configure end of conference and softkeys for hardware conference is applicable:

Only for SCCP phones in Unified CME.

For End of Conference option on SIP phones, you need to configure conference add-mode and conference drop-mode under voice register configuration mode.   For more information, see Cisco Unified Communications Manager Express Command Reference .

For softkey configuration on SIP phones, you need to configure softkeys under voice register template configuration mode.  For more information, see Cisco Unified Communications Manager Express Command Reference .

For Ad Hoc and Meet Me hardware conferencing.

#### Before you begin

The RmLstC, ConfList, Join, and Select functions and soft keys are supported for hardware-based conferencing only and require
                                       the appropriate DSP farm configuration. For configuration information, see these tasks in this module:

Enable DSP Farm Services for a Voice Card

Configure the DSP Farm Profile

Associate Unified CME with a DSP Farm Profile

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- conference add-mode [ creator ]

- conference drop-mode [ | creator local ]

- conference admin

- softkeys
                                       				  connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]}

- softkeys hold {[ Join ] [ Newcall ] [ Resume ] [ Select ]}

- softkeys idle {[ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ]}

- softkeys seized {[ CallBack ] [ Cfwdall ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ]}

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 1
```

Enter
                                             				ephone-template configuration mode to create an ephone template to configure a
                                             				set of phone features.

Step 4

conference add-mode [ creator ]

#### Example:

```
Router(config-ephone-template)# conference add-mode creator
```

(Optional)
                                             				Configures the mode for adding parties to conferences.

creator —Only the creator can add parties to the conference.

Step 5

conference drop-mode [ | creator local ]

#### Example:

```
Router(config-ephone-template)# conference drop-mode creator
```

(Optional)
                                             				Configures the mode for dropping parties from multi-party ad hoc conferences.

creator —The active conference terminates when the creator hangs up.

local —The active conference terminates when the last local party in the conference hangs up or drops out of the conference.

Step 6

conference admin

#### Example:

```
Router(config-ephone-template)# conference admin
```

(Optional)
                                             				Configures the ephone as the conference administrator. The administrator can:

Dial in to any conference directly through the conference number

Use the ConfList soft key to list conference parties

Remove any party from any conference

Step 7

softkeys
                                                				  connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]}

#### Example:

```
Router(config-ephone-template)# softkeys connected Hold Trnsfer Park Endcall Confrn ConfList Join Select RmLstC
```

Configures
                                             				an ephone template for softkey display during the connected call stage.

The soft keys used for multi-party conferencing are RmLstC , ConfList , Join , and Select . These soft keys are supported for hard-ware based conferencing only and require the appropriate DSP farm configuration.

The number and order of soft key keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone.

Step 8

softkeys hold {[ Join ] [ Newcall ] [ Resume ] [ Select ]}

#### Example:

```
Router(config-ephone-template)# softkeys hold Join Newcall Resume Select
```

Configures
                                             				an ephone template to modify softkey display during the call-hold call stage.

The soft keys used for multi-party conferencing are Join and Select . These soft keys are supported for hard-ware based conferencing only and require the appropriate DSP farm configuration.

The number and order of softkey keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone.

Step 9

softkeys idle {[ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ]}

#### Example:

```
Router(config-ephone-template)# softkeys idle ConfList Gpickup Join Login Newcall Pickup Redial RmLstC
```

Configures
                                             				an ephone template for softkey display during the idle call stage.

The soft keys used for multi-party conferencing are RmLstC , ConfList , and Join . These soft keys are supported for hard-ware based conferencing only and require the appropriate DSP farm configuration.

The number and order of soft key keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone.

Step 10

softkeys seized {[ CallBack ] [ Cfwdall ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ]}

#### Example:

```
Router(config-ephone-template)# softkeys seized Redial Endcall Cfwdall Pickup Gpickup Callback Meetme
```

(Optional)
                                             				Configures an ephone template for softkey display during the seized call stage.

You must configure the MeetMe soft key in the seized state for the ephone to initiate a meet-me conference.

The number and order of soft key keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone.

Step 11

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 12

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters
                                             				ephone configuration mode to create and configure an ephone.

Step 13

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-dn-template 1
```

Applies an
                                             				ephone-dn template to an ephone-dn.

The template-tag must be the same as the template-tag in Step 3.

Step 14

end

#### Example:

```
Router(config-ephone)# exit
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If you are
                                 		  finished modifying the configuration, you are ready to generate configuration
                                 		  files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

## Verify Conferencing

Use the show
                                             				  running-config command to verify your configuration. Any
                                       			 non-default conferencing parameters are listed in the telephony-service portion
                                       			 of the output, and end-of-conference options are listed in the ephone portion.

### Example:

```
Router# show running-config !
		  ephone-dn  1  dual-line
		   ring feature secondary
		   number 126 secondary 1261
		   description Sales
		   name Smith
		   call-forward busy 500 secondary
		   call-forward noan 500 timeout 10
		   huntstop channel
		   no huntstop
		   no forward local-calls
		  !
		  ephone  1
		   mac-address 011F.92A0.C10B
		   type 7960 addon 1 7914
		   no dnd feature-ring
		   keep-conference
```

### Verify Hardware Conferencing

The CLI commands to troubleshoot hardware conferencing is applicable to:

Both SIP and SCCP conference configurations in Unified CME.

#### Ad Hoc Hardware Conference

You can configure the following show commands to verify Ad Hoc hardwarwe conferencing:

show telephony-service conference hardware

show dspfarm profile <profile number>

show sccp

show call active voice compact

show call active voice brief

The following is a sample output for show telephony-service conference hardware command.

```
Router#show telephony-service conference hardware
Conference   Type              Active  Max  Peak    Host         HostPhone   Last
                                                                   cur(initial)      
============================================================================================
A002         Ad-hoc                4     8     5    1111 sip1      1     (  1)   5555 sccp2
```

The following is a sample output for show dspfarm dsp active command.

```
Router#show dspfarm dsp active
SLOT   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED

0/1    1   44.1.0   UP     1    USED  conf    1      498       3384      3329     
0/1    1   44.1.0   UP     1    USED  conf    1      499       3383      1739     
0/1    1   44.1.0   UP     1    USED  conf    1      500       3382      3384     
0/1    1   44.1.0   UP     1    USED  conf    1      503       2899      671      
0/1    1   44.1.0   UP     1    USED  conf    1      506       2525      1269
```

#### Meet Me Conference

You can configure the following show commands to verify Ad Hoc hardwarwe conferencing:

show sccp connection

show ephone-dn conference

show telephony-service conference hardware

show dspfarm dsp active

show call active voice compact

Show voip rtp connections

The following is a sample output for show ephone-dn conference command.

```
Router#show ephone-dn conference 
type         active inactive  numbers
=================================
Meetme          4       28     5555  
DN tags: 9, 10, 11, 12
```

The following is a sample output for show telephony-service conference hardware command.

```
Router#sh telephony-service conference hardware 
Conference   Type              Active  Max  Peak    Host         HostPhone   Last
                                                                   cur(initial)      
=============================================================================================
5555         Meetme               4     32    4    phone2 1002      2     (2)   1003 1003
```

The following is a sample output for show dspfarm dsp active command.

```
Router#show dspfarm dsp active
SLOT   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED

0/1    4   44.2.0   UP     1    USED  conf    1      8         8574      8599     
0/1    4   44.2.0   UP     1    USED  conf    1      10        8223      8250     
0/1    4   44.2.0   UP     1    USED  conf    1      12        7724      7639     
0/1    4   44.2.0   UP     1    USED  conf    1      14        7274      7299     

Total number of DSPFARM DSP channel(s) 1
```

The following is a sample output for show call active voice compact command.

```
Router#show call active voice compact
 <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>        VRF
Total call-legs: 8
     68771 ANS     T301   g711ulaw    VOIP        P1002       10.0.0.1:22018                                 
     68772 ORG     T302   g711ulaw    TELE        P5555
     68775 ANS     T295   g711ulaw    VOIP        P1004       10.0.0.2:22462                                 
     68776 ORG     T296   g711ulaw    TELE        P5555
     68778 ANS     T286   g711ulaw    VOIP        P1001       10.0.0.3:31890                                 
     68779 ORG     T287   g711ulaw    TELE        P5555
     68781 ANS     T278   g711ulaw    VOIP        P1003       10.0.0.4:31202                                 
     68782 ORG     T279   g711ulaw    TELE        P5555
```

### Verify Keep Conference

The following is a sample output for show voice register tftp-bind command.

```
Router#sh voice register tftp-bind
tftp-server url flash:/its/SEPE0D173E54508.cnf.xml alias SEPE0D173E54508.cnf.xml

    With keep-conference enabled in voice register pool or voice register template Router#more flash:/its/SEPE0D173E54508.cnf.xml | sec cnf 
    <cnfJoinEnabled>true</cnfJoinEnabled>
     
    With keep-conference disabled in both voice register pool and voice register template Router#more flash:/its/SEPE0D173E54508.cnf.xml | sec cnf 
    <cnfJoinEnabled>false</cnfJoinEnabled>
```

### Troubleshoot Conferencing

Step 1

Use the debug ephone commands to observe messages and states associated with an ephone. For more information, see Cisco Unified CME Command Reference .

Step 2

Use the debug ephone detail command for SCCP calls in a software conference.

Step 3

Use the debug ccsip all command for SIP calls in a software conference.

Step 4

Use the debug ephone hw-conference command for SIP and SCCP calls in a hardware conference.

## Configuration Examples for Conferencing

### Example for Configuration of Max Conference and Gain Levels

The following example sets the maximum number of conferences for a
                                 		  Cisco Unified IP phone to 4 and configures a gain of 6 db for inbound audio
                                 		  packets from remote PSTN or VoIP calls joining a conference:

```
telephony-service
max-conferences 4 gain 6
```

### Example for Keep Conference Configuration on SCCP Phones

In the following example, extension 3555 initiates a three-way
                                 		  conference. After the conference is established, extension 3555 can press the
                                 		  Confrn soft key to disconnect the last party that was connected and remain
                                 		  connected to the first party that was connected. If extension 3555 hangs up
                                 		  from the conference, the other two parties remain connected if one of them is
                                 		  local to the Cisco Unified CME system.

```
ephone-dn 35
		   number 3555
		  
		  ephone 24
		   button 1:35
		   keep-conference drop-last local-only
```

In the following example, extension 3666 initiates a three-way
                                 		  conference. After the conference is established, extension 3666 can press the
                                 		  Confrn soft key to disconnect the last party that was connected and remain
                                 		  connected to the first party that was connected. Also, extension 3666 can hang
                                 		  up or press the EndCall soft key to leave the conference and keep the other two
                                 		  parties connected.

```
ephone-dn 36
		 number 3666
		
		ephone 25
		 button 1:36
		 keep-conference drop-last endcall
```

In the following example, extension 3777 initiates a three-way
                                 		  conference. After the conference is established, extension 3777 can press the
                                 		  Confrn soft key to disconnect the last party that was connected and remain
                                 		  connected to the first party that was connected. Also, extension 3777 can hang
                                 		  up or press the EndCall soft key to leave the conference and keep the other two
                                 		  parties connected only if one of the two parties is local to the Cisco Unified CME
                                 		  system.

```
ephone-dn 38
		 number 3777
		
		ephone 27
		 button 1:38
		 keep-conference drop-last endcall local-only
```

In the following example, extension 3999 initiates a three-way
                                 		  conference. After the conference is established, extension 3999 can hang up or
                                 		  press the EndCall soft key to leave the conference and keep the other two
                                 		  parties connected only if one of the two parties is local to the Cisco Unified CME
                                 		  system. Extension 3999 can also use the Confrn soft key to break up the
                                 		  conference but stay connected to both parties.

```
ephone-dn 39
		 number 3999
		
		ephone 29
		 button 1:39
		 keep-conference endcall local-only
```

### Example for Keep Conference Configuration on SIP Phones

In the following example, extension 3555 initiates a three-way
                                 		  conference on SIP phones using keep-conference configured under voice register pool .

```
voice register dn 35
    number 3555

  voice register pool 24
    number 1 dn 35
    keep-conference
```

Following is a sample configuration for keep-conference under voice register template .

```
voice register template 24
    keep-conference

  voice register pool 35
    template 24
```

### Example of DSP
                           	 Farm and Cisco Unified CME on the Same Router

In this example,
                                 		  the DSP farm and Cisco Unified CME are on the same router as shown in CME and the
                                    			 DSP Farm on the Same Router .

```
Current configuration : 16345 bytes
		!
		version 12.4
		service timestamps debug datetime msec
		service timestamps log uptime
		no service password-encryption
		service internal
		!
		hostname cmedsprtr
		!
		boot-start-marker
		boot-end-marker
		!
		logging buffered 90000 debugging
		!
		no aaa new-model
		!
		resource policy
		!
		no network-clock-participate slot 1
		no network-clock-participate wic 0
		ip cef
		!
		!
		ip dhcp pool phone1
		 host 10.4.188.66 255.255.0.0
		 client-identifier 0100.0ab7.b144.4a
		 default-router 10.4.188.65
		 option 150 ip 10.4.188.65
		!
		ip dhcp pool phone2
		 host 1.4.188.67 255.255.0.0
		 client-identifier 0100.3094.c269.35
		 default-router 10.4.188.65
		 option 150 ip 10.4.188.65
		!
		!
		voice-card 1
		 dsp services dspfarm
		!
		!
		voice call send-alert
		voice call carrier capacity active
		!
		voice service voip
		 allow-connections h323 to h323 
		 supplementary-service h450.12
		 h323
		!
		!
		!
		!
		controller E1 1/0
		 framing NO-CRC4
		!
		controller E1 1/1
		!
		!
		interface FastEthernet0/0
		 ip address 10.4.188.65 255.255.0.0
		 duplex auto
		 speed auto
		 no keepalive
		 no cdp enable
		 no clns route-cache
		!
		interface FastEthernet0/1
		 no ip address
		 shutdown
		 duplex auto
		 speed auto
		 no clns route-cache
		!
		ip route 10.4.0.0 255.255.0.0 FastEthernet0/0
		ip route 192.168.254.254 255.255.255.255 10.4.0.1
		!
		ip http server
		!
		!
		control-plane
		!
		!
		sccp local FastEthernet0/0
		sccp ccm 10.4.188.65 identifier 1 version 4.0
		sccp
		!
		sccp ccm group 123
		 associate ccm 1 priority 1
		 associate profile 1 register mtp00097c5e9ce0
		 keepalive retries 5
		! 
		!
		dspfarm profile 1 conference
		 codec g711ulaw
		 codec g711alaw
		 codec g729ar8
		 codec g729abr8
		 codec g729r8
		 codec g729br8
		 maximum sessions 6
		 associate application SCCP
		!
		dial-peer cor custom
		!
		!
		!
		dial-peer voice 6 voip
		 destination-pattern 6...
		 session target ipv4:10.4.188.90
		!
		telephony-service
		 conference hardware
		 load 7960-7940 P00307020400
		 load 7905 CP7905060100SCCP050309A.sbin
		 max-ephones 48
		 max-dn 180
		 ip source-address 10.4.188.65 port 2000
		 timeouts ringing 500
		 system message MY MELODY (2611)
		 sdspfarm units 4
		 sdspfarm tag 1 mtp00097c5e9ce0
		 max-conferences 4 gain -6
		 call-forward pattern ....
		 transfer-system full-consult
		 transfer-pattern 7...
		 transfer-pattern ....
		 create cnf-files version-stamp Jan 01 2002 00:00:00
		!
		!
		ephone-template 1
		 softkeys hold Newcall Resume Select Join
		 softkeys idle Cfwdall ConfList Dnd Gpickup HLog Join Login Newcall Pickup Redial RmLstC
		 softkeys seized Redial Pickup Gpickup HLog Meetme Endcall
		 softkeys connected Acct ConfList Confrn Endcall Flash HLog Hold Join Park RmLstC Select Trnsfer
		!
		!
		ephone-dn 1 dual-line
		 number 8001
		 name melody-8001
		!
		!
		ephone-dn 2 dual-line
		 number 8002
		!
		!
		ephone-dn 3 dual-line
		 number 8003
		!
		!
		ephone-dn 4 dual-line
		 number 8004
		!
		!
		ephone-dn 5 dual-line
		 number 8005
		!
		!
		ephone-dn 6 dual-line
		 number 8006
		!
		!
		ephone-dn 7 dual-line
		 number 8007
		!
		!
		ephone-dn 8 dual-line
		 number 8008
		!
		!
		ephone-dn 60 dual-line
		 number 8887
		 conference meetme
		 no huntstop
		!
		!
		ephone-dn 61 dual-line
		 number 8887
		 conference meetme
		 preference 1
		 no huntstop
		!
		!
		ephone-dn 62 dual-line
		 number 8887
		 conference meetme
		 preference 2
		 no huntstop
		!
		!
		ephone-dn 63 dual-line
		 number 8887
		 conference meetme
		 preference 3
		!
		!
		ephone-dn 64 dual-line
		 number 8889
		 name Conference
		 conference ad-hoc
		 no huntstop
		!
		!
		ephone-dn 65 dual-line
		 number 8889
		 name Conference
		 conference ad-hoc
		 preference 1
		 no huntstop
		!
		!
		ephone-dn 66 dual-line
		 number 8889
		 name Conference
		 conference ad-hoc
		 preference 2
		 no huntstop
		!
		!
		ephone-dn 67 dual-line
		 number 8889
		 name Conference
		 conference ad-hoc
		 preference 3
		!
		!
		ephone 1
		 ephone-template 1
		 mac-address 0030.94C2.6935
		 type 7960
		 button 1:1 2:2
		!
		!
		ephone 2
		 ephone-template 1
		 mac-address 000A.B7B1.444A
		 type 7940
		 button 1:4 2:8
		!
		line con 0
		 exec-timeout 0 0
		line aux 0
		 exec-timeout 0 0
		line vty 0 4
		 exec-timeout 0 0
		 login
		line vty 5 15
		 login
		!
		!
		end
```

The following is an example of DSP Farm and Unified CME on the same
                                 		  router for SIP Phones.

```
Current configuration : 10821 bytes
!
version 16.5
service timestamps debug datetime msec
service timestamps log datetime msec
service sequence-numbers
!
boot-start-marker
boot-end-marker
!
!
vrf definition Mgmt-intf
!
address-family ipv4
exit-address-family
!        
 address-family ipv6
exit-address-family
!
! card type command needed for slot/bay 0/1
no logging queue-limit
logging buffered 100000000
no logging rate-limit
no logging console
!
no aaa new-model
!
!
ipv6 unicast-routing
!
!
subscriber templating
! 
! 
multilink bundle-name authenticated
!
!
voice service voip
no ip address trusted authenticate
media disable-detailed-stats
allow-connections sip to sip
no supplementary-service sip refer
fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
sip
  registrar server expires max 240 min 60
!
!
voice register global
mode cme
source-address 8.39.23.16 port 5060
no privacy
timeouts interdigit 30
max-dn 40
max-pool 40
voicemail 9000
tftp-path flash:
create profile sync 0095202153430137
conference hardware
!
voice register dn  1
number 1001
name SIP Ph 1
!
voice register dn  2
number 1002
name SIP Ph 2
!
voice register dn  3
number 1003
name SIP Ph 3
!
voice register template  1
softkeys idle  HLog Mobility Newcall Pickup Redial
softkeys ringIn  Answer DND
softkeys connected  ConfList Confrn Endcall Hold Mobility Park Trnsfer
softkeys remote-in-use  Barge Newcall cBarge
!
voice register pool  1
busy-trigger-per-button 10
id mac B000.B4BA.F3DA
type 8851
number 1 dn 1
template 1
dtmf-relay rtp-nte
username xxxx password xxxx
codec g711ulaw
no vad
!
voice register pool  2
busy-trigger-per-button 10
id mac 1CE8.5DC9.C054
type 8851
number 1 dn 2
template 1
dtmf-relay rtp-nte
username xxxx password xxxx
codec g711ulaw
no vad
!
voice register pool  3
busy-trigger-per-button 10
id mac 00AF.1F9D.FB9F
type 8841
number 1 dn 3
template 1
dtmf-relay rtp-nte
username xxxx password xxxx
codec g711ulaw
no vad
!
!
voice translation-rule 1
rule 1 /^1234/ /301/
!
voice translation-rule 4
rule 4 /^1(..)$/ /51237812\1/
!
!
voice translation-profile PSTN_Callforwarding
translate redirect-target 4
!
voice translation-profile cmein
translate called 1
!
!
voice-card 0/1
dsp services dspfarm
!         
restconf
!
username xxxx password xxxx
!
redundancy
mode none
!
!
threat-visibility
!
!
interface GigabitEthernet0/0/0
ip address 8.39.23.16 255.255.0.0
negotiation auto
!
interface GigabitEthernet0/0/1
ip address 10.64.86.106 255.255.0.0
shutdown
media-type rj45
negotiation auto
ipv6 address 2001:420:54FF:13::312:55/119
ipv6 enable
!
interface GigabitEthernet0/0/2
no ip address
shutdown
negotiation auto
!
interface GigabitEthernet0/0/3
no ip address
shutdown
negotiation auto
!
interface Service-Engine0/1/0
!
interface GigabitEthernet0
vrf forwarding Mgmt-intf
no ip address
shutdown
negotiation auto
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
ip http secure-port 8443
ip tftp source-interface GigabitEthernet0/0/1
ip tftp blocksize 8192
ip dns server
ip rtcp report interval 65535 
ip route 0.0.0.0 0.0.0.0 8.39.0.1
ip route 8.0.0.0 255.0.0.0 8.39.0.1
ip route 202.153.144.0 255.255.255.0 8.39.0.1
!
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!
!
!
tftp-server bootflash
tftp-server flash:vc488xx.12-0-1MN-113.sbn
tftp-server flash:sip88xx.12-0-1MN-113.loads
tftp-server flash:sb288xx.BE-01-020.sbn
tftp-server flash:kern88xx.12-0-1MN-113.sbn
tftp-server flash:fbi88xx.BE-01-010.sbn
tftp-server flash:rootfs88xx.12-0-1MN-113.sbn
!
!
ipv6 access-list preauth_v6
permit udp any any eq domain
permit tcp any any eq domain
permit icmp any any nd-ns
permit icmp any any nd-na
permit icmp any any router-solicitation
permit icmp any any router-advertisement
permit icmp any any redirect
permit udp any eq 547 any eq 546
permit udp any eq 546 any eq 547
deny ipv6 any any
!
control-plane
!
!
mgcp behavior rsip-range tgcp-only
mgcp behavior comedia-role none
mgcp behavior comedia-check-media-src disable
mgcp behavior comedia-sdp-force disable
!
mgcp profile default
!         
sccp local GigabitEthernet0/0/0
sccp ccm 8.39.23.16 identifier 1 version 7.0 
sccp
!
sccp ccm group 1
associate ccm 1 priority 1
associate profile 1 register conf-moto
!
!
!
telephony-service
sdspfarm units 2
sdspfarm tag 1 conf-moto
no privacy
conference hardware
no auto-reg-ephone
max-ephones 40
max-dn 40
ip source-address 8.39.23.16 port 2000
service phone sshAccess 0
service phone webAccess 0
service directed-pickup gpickup
max-conferences 8 gain -6
call-park system application
hunt-group logout HLog
moh enable-g711 "flash:/scripts/en_bacd_music_on_hold.au"
transfer-system full-consult
fac standard
create cnf-files version-stamp Jan 01 2002 00:00:00
!
!
dspfarm profile 2 transcode universal  
 codec g729abr8
codec g729ar8
codec g711alaw
codec g711ulaw
codec g729br8
maximum sessions 2
associate application CUBE
!
dspfarm profile 1 conference  
 codec g729br8
codec g729r8
codec g729abr8
codec g729ar8
codec g711alaw
codec g711ulaw
maximum sessions 2
associate application SCCP
!
dial-peer voice 1 voip
destination-pattern 20..
session protocol sipv2
session target ipv4:8.39.24.41
dtmf-relay rtp-nte
!
!
gateway 
 media-inactivity-criteria all
timer receive-rtcp 1000
timer receive-rtp 1200
!
sip-ua 
 mwi-server ipv4:8.41.24.7 expires 3600 port 5060 transport udp unsolicited
presence enable
!
!
ephone-dn  1  octo-line
number 1006
!
!
ephone-dn  2  octo-line
number 1007
!
!
ephone-dn  3  octo-line
number 1008
!
!
ephone-dn  4  octo-line
number 1009
!
!
ephone-dn  5  octo-line
number A001
conference ad-hoc
!
!
ephone-dn  6  octo-line
number A002
conference ad-hoc
!         
!
ephone  1
device-security-mode none
mac-address 9876.0000.0006
type 7975
button  1:1
!
!
!
ephone  2
device-security-mode none
mac-address 9876.0000.0007
type 7975
button  1:2
!
!
!
ephone  3
device-security-mode none
mac-address 9876.0000.0008
type 7975
button  1:3
!         
!
!
ephone  4
device-security-mode none
mac-address 9876.0000.0009
type 7975
button  1:4
!
!
alias exec poolall show voice register pool all brief
!
line con 0
transport input none
stopbits 1
speed 115200
line aux 0
stopbits 1
line vty 0 4
password xxxx
login local
transport input telnet
!
no network-clock synchronization automatic
!
end
```

### Example of DSP
                           	 Farm and Cisco Unified CME on Different Routers

In this example,
                                 		  the DSP farm and Cisco Unified CME are on different routers as shown in Cisco
                                    			 Unified CME and the DSP Farm on Different Routers .

This section
                                 		  contains configuration examples for the following routers:

Example of Cisco Unified CME Router Configuration

Example of DSP Farm Router Configuration

#### Example of Cisco Unified CME Router Configuration

```
Current configuration : 5659 bytes 
		!
		version 12.4 
		no service timestamps debug uptime 
		no service timestamps log uptime
		no service password-encryption
		!
		boot-start-marker
		boot-end-marker
		!
		!
		card type command needed for slot 1
		logging buffered 3000000 debugging
		!
		no aaa new-model
		!
		resource policy
		!
		no network-clock-participate slot 1
		no network-clock-participate aim 0
		!
		voice-card 1
		 no dspfarm
		!
		voice-card 3
		 dspfarm
		!
		ip cef
		!
		!
		no ip dhcp use vrf connected
		!
		ip dhcp pool IPPhones
		 network 10.15.15.0 255.255.255.0
		 option 150 ip 10.15.15.1
		 default-router 10.15.15.1
		!
		!
		interface FastEthernet0/0
		 ip address 10.3.111.102 255.255.0.0
		 duplex auto
		 speed auto
		! 
		interface FastEthernet0/1
		 no ip address
		 duplex auto
		 speed auto
		!
		interface FastEthernet0/1.1
		 encapsulation dot1Q 10
		 ip address 10.15.14.1 255.255.255.0
		!
		interface FastEthernet0/1.2
		 encapsulation dot1Q 20
		 ip address 10.15.15.1 255.255.255.0
		!
		ip route 0.0.0.0 0.0.0.0 10.5.51.1
		ip route 0.0.0.0 0.0.0.0 10.3.0.1
		!
		ip http server
		!
		!
		!
		!
		control-plane!
		!
		!
		!
		dial-peer voice 1 voip
		 destination-pattern 3...
		 session target ipv4:10.3.111.101
		!
		!
		telephony-service
		 conference hardware
		 load 7910 P00403020214
		 load 7960-7940 P003-07-5-00
		 max-ephones 50
		 max-dn 200
		 ip source-address 10.15.15.1 port 2000
		 sdspfarm units 4
		 sdspfarm transcode sessions 12
		 sdspfarm tag 1 confer1
		 sdspfarm tag 4 xcode1
		 max-conferences 8 gain -6
		 moh flash:music-on-hold.au
		 multicast moh 239.0.0.0 port 2000
		 transfer-system full-consult
		 create cnf-files version-stamp Jan 01 2002 00:00:00
		!
		!
		ephone-template 1
		 softkeys hold Resume Newcall Select Join
		 softkeys idle Redial Newcall ConfList RmLstC Cfwdall Join Pickup Login HLog Dnd Gpickup
		 softkeys seized Endcall Redial Cfwdall Meetme Pickup Callback
		 softkeys alerting Endcall Callback
		 softkeys connected Hold Endcall Confrn Trnsfer Select Join ConfList RmLstC Park Flash !
		ephone-dn 1 dual-line
		 number 6000
		!
		!
		ephone-dn 2 dual-line
		 number 6001
		!
		!
		ephone-dn 3 dual-line
		 number 6002
		!
		!
		ephone-dn 4 dual-line
		 number 6003
		!
		!
		ephone-dn 5 dual-line
		 number 6004
		!
		!
		ephone-dn 6 dual-line
		 number 6005
		!
		!
		ephone-dn 7 dual-line
		 number 6006
		!
		!
		ephone-dn 8 dual-line
		 number 6007
		!
		!
		ephone-dn 9 dual-line
		 number 6008
		!
		!
		ephone-dn 10 dual-line
		 number 6009
		!
		!
		ephone-dn 11
		 number 6011
		!
		!
		ephone-dn 12
		 number 6012
		!
		!
		ephone-dn 13
		 number 6013
		!
		!
		ephone-dn 14
		 number 6014
		!
		!
		ephone-dn 15
		 number 6015
		!
		!
		ephone-dn 16
		 number 6016
		!
		!
		ephone-dn 17
		 number 6017
		!
		!
		ephone-dn 18
		 number 6018
		!
		!
		ephone-dn 19
		 number 6019
		!
		!
		ephone-dn 20
		 number 6020
		!
		!
		ephone-dn 21
		 number 6021
		!
		!
		ephone-dn 22
		 number 6022
		!
		!
		ephone-dn 23
		 number 6023
		!
		!
		ephone-dn 24
		 number 6024
		!
		!
		ephone-dn 25 dual-line
		 number 6666
		 conference meetme
		 preference 1
		 no huntstop
		!
		!
		ephone-dn 26 dual-line
		 number 6666
		 conference meetme
		 preference 2
		 no huntstop
		!
		!
		ephone-dn 27 dual-line
		 number 6666
		 conference meetme
		 preference 3
		 no huntstop
		!
		!
		ephone-dn 28 dual-line
		 number 6666
		 conference meetme
		 preference 4
		 no huntstop
		!
		!
		ephone-dn 29 dual-line
		 number 8888
		 conference meetme
		 preference 1
		 no huntstop
		!
		!
		ephone-dn 30 dual-line
		 number 8888
		 conference meetme
		 preference 2
		 no huntstop
		!
		!
		ephone-dn 31 dual-line
		 number 8888
		 conference meetme
		 preference 3
		 no huntstop
		!
		!
		ephone-dn 32 dual-line
		 number 8888
		 conference meetme
		 preference 4
		!
		!
		ephone-dn 33
		 number 6033
		!
		!
		ephone-dn 34
		 number 6034
		!
		!
		ephone-dn 35
		 number 6035
		!
		!
		ephone-dn 36
		 number 6036
		!
		!
		ephone-dn 37
		 number 6037
		!
		!
		ephone-dn 38
		 number 6038
		!
		!
		ephone-dn 39
		 number 6039
		!
		!
		ephone-dn 40
		 number 6040
		!
		!
		ephone-dn 41 dual-line
		 number 6666
		 conference meetme
		 preference 5
		 no huntstop
		!
		!
		ephone-dn 42 dual-line
		 number 6666
		 conference meetme
		 preference 6
		 no huntstop
		!
		!
		ephone-dn 43 dual-line
		 number 6666
		 conference meetme
		 preference 7
		 no huntstop
		!
		!
		ephone-dn 44 dual-line
		 number 6666
		 conference meetme
		 preference 8
		 no huntstop
		!
		!
		ephone-dn 45 dual-line
		 number 6666
		 conference meetme
		 preference 9
		 no huntstop
		!
		!
		ephone-dn 46 dual-line
		 number 6666
		 conference meetme
		 preference 10
		 no huntstop
		!
		!
		ephone-dn 47 dual-line
		 number 6666
		 conference meetme
		 preference 10
		 no huntstop
		!
		!
		ephone-dn 48 dual-line
		 number 6666
		 conference meetme
		 preference 10
		!
		!
		ephone-dn 51 dual-line
		 number A0001
		 name conference
		 conference ad-hoc
		 preference 1
		 no huntstop
		!
		!
		ephone-dn 52 dual-line
		 number A0001
		 name conference
		 conference ad-hoc
		 preference 2
		 no huntstop
		!
		!
		ephone-dn 53 dual-line
		 number A0001
		 name conference
		 conference ad-hoc
		 preference 3
		 no huntstop
		!
		!
		ephone-dn 54 dual-line
		 number A0001
		 name conference
		 conference ad-hoc
		 preference 4
		!
		!
		ephone 1
		 ephone-template 1
		 mac-address C863.B965.2401
		 type anl
		 button 1:1
		!
		!
		!
		ephone 2
		 ephone-template 1
		 mac-address 0016.C8BE.A04A
		 type 7920
		!
		!
		!
		ephone 3
		 ephone-template 1
		 mac-address C863.B965.2400
		 type anl
		 button 1:2 
		!
		!
		!
		ephone 4
		 no multicast-moh
		 ephone-template 1
		 mac-address 0017.952B.7F5C
		 type 7912
		 button 1:4
		!
		!
		!
		ephone 5
		 ephone-template 1
		 ephone 6
		 no multicast-moh
		 ephone-template 1
		 mac-address 0017.594F.1468
		 type 7961GE
		 button 1:6
		!
		!
		!
		ephone 11
		 ephone-template 1
		 mac-address 0016.C8AA.C48C
		 button 1:10 2:15 3:16 4:17
		 button 5:18 6:19 7:20 8:21
		 button 9:22 10:23 11:24 12:33
		 button 13:34 14:35 15:36 16:37
		 button 17:38 18:39 19:40
		!
		!
		line con 0
		line aux 0
		line vty 0 4
		 login
		!
		!
		end
```

#### Example of DSP Farm Router Configuration

```
Current configuration : 2179 bytes
		!
		! Last configuration change at 05:47:23 UTC Wed Jul 12 2006
		!
		version 12.4
		service timestamps debug datetime msec localtime
		no service timestamps log uptime
		no service password-encryption
		hostname dspfarmrouter
		!
		boot-start-marker
		boot-end-marker
		!
		!
		card type command needed for slot 1
		logging buffered 4096 debugging enable password lab
		!
		no aaa new-model
		!
		resource policy
		!
		no network-clock-participate slot 1
		!
		!
		ip cef
		!
		!
		no ip domain lookup
		!
		!
		voice-card 0
		 no dspfarm
		!
		voice-card 1
		 no dspfarm
		 dsp services dspfarm
		
		interface GigabitEthernet0/0
		 ip address 10.3.111.100 255.255.0.0
		 duplex auto
		 speed auto
		! 
		interface GigabitEthernet0/1.1
		 encapsulation dot1Q 100
		 ip address 192.168.1.10 255.255.255.0
		!
		interface GigabitEthernet0/1.2
		 encapsulation dot1Q 200
		 ip address 192.168.2.10 255.255.255.0
		!
		interface GigabitEthernet0/1.3
		 encapsulation dot1Q 10
		 ip address 10.15.14.10 255.255.255.0
		!
		interface GigabitEthernet0/1.4
		 encapsulation dot1Q 20
		 ip address 10.15.15.10 255.255.255.0 !
		ip route 10.0.0.0 255.0.0.0 10.3.0.1
		ip route 192.168.0.0 255.0.0.0 10.3.0.1
		!
		!
		ip http server
		!
		!
		!
		!
		control-plane
		!
		sccp local GigabitEthernet0/0
		sccp ccm 10.15.15.1 identifier 1 version 4.1
		!
		!
		sccp ccm group 1
		 associate ccm 1 priority 1
		 associate profile 101 register confer1
		 associate profile 103 register xcode1
		!
		!
		dspfarm profile 103 transcode
		 codec g711ulaw
		 codec g711alaw
		 codec g729r8
		 maximum sessions 6
		 associate application SCCP
		!
		dspfarm profile 101 conference
		 codec g711ulaw
		 codec g711alaw
		 codec g729r8
		 maximum sessions 5
		 associate application SCCP
		!
		!
		!
		!
		line con 0
		 exec-timeout 0 0
		line aux 0
		line vty 0 4
		 session-timeout 300
		 exec-timeout 0 0
		 password 
		 no login
		!
		scheduler allocate 20000 1000
		!
		end
```

### Example for Verification of Meet Me Conference

The following partial output from the show running-config command shows the configuration on a Cisco 2821 router with Unified CME and Cisco Unity Express, with comments describing
                                 the configuration for setting up Meet-Me Conferencing.

```
Router# show running-config building configuration...
.
.
.
.
.
! !---Two T1 ports connected back-to-back to bridge VOIP to Multicast controller T1 0/3/0
 framing esf
 linecode b8zs
ds0-group 1 timeslots 1 type e&-immediate-start
ds0-group 2 timeslots 2 type e&-immediate-start
ds0-group 3 timeslots 3 type e&-immediate-start
ds0-group 4 timeslots 4 type e&-immediate-start
ds0-group 5 timeslots 5 type e&-immediate-start
ds0-group 6 timeslots 6 type e&-immediate-start
ds0-group 7 timeslots 7 type e&-immediate-start
ds0-group 8 timeslots 8 type e&-immediate-start
ds0-group 9 timeslots 9 type e&-immediate-start
ds0-group 10 timeslots 10 type e&-immediate-start
ds0-group 11 timeslots 11 type e&-immediate-start
ds0-group 12 timeslots 12 type e&-immediate-start
ds0-group 13 timeslots 13 type e&-immediate-start
ds0-group 14 timeslots 14 type e&-immediate-start
ds0-group 15 timeslots 15 type e&-immediate-start
ds0-group 16 timeslots 16 type e&-immediate-start
ds0-group 17 timeslots 17 type e&-immediate-start
ds0-group 18 timeslots 18 type e&-immediate-start
ds0-group 19 timeslots 19 type e&-immediate-start
ds0-group 20 timeslots 20 type e&-immediate-start
ds0-group 21 timeslots 21 type e&-immediate-start
ds0-group 22 timeslots 22 type e&-immediate-start
ds0-group 23 timeslots 23 type e&-immediate-start
ds0-group 24 timeslots 24 type e&-immediate-start
!
controller T1 0/3/1
 framing esf
 clock source internal
 linecode b8zs
ds0-group 1 timeslots 1 type e&-immediate-start
ds0-group 2 timeslots 2 type e&-immediate-start
ds0-group 3 timeslots 3 type e&-immediate-start
ds0-group 4 timeslots 4 type e&-immediate-start
ds0-group 5 timeslots 5 type e&-immediate-start
ds0-group 6 timeslots 6 type e&-immediate-start
ds0-group 7 timeslots 7 type e&-immediate-start
ds0-group 8 timeslots 8 type e&-immediate-start
ds0-group 9 timeslots 9 type e&-immediate-start
ds0-group 10 timeslots 10 type e&-immediate-start
ds0-group 11 timeslots 11 type e&-immediate-start
ds0-group 12 timeslots 12 type e&-immediate-start
ds0-group 13 timeslots 13 type e&-immediate-start
ds0-group 14 timeslots 14 type e&-immediate-start
ds0-group 15 timeslots 15 type e&-immediate-start
ds0-group 16 timeslots 16 type e&-immediate-start
ds0-group 17 timeslots 17 type e&-immediate-start
ds0-group 18 timeslots 18 type e&-immediate-start
ds0-group 19 timeslots 19 type e&-immediate-start
ds0-group 20 timeslots 20 type e&-immediate-start
ds0-group 21 timeslots 21 type e&-immediate-start
ds0-group 22 timeslots 22 type e&-immediate-start
ds0-group 23 timeslots 23 type e&-immediate-start
ds0-group 24 timeslots 24 type e&-immediate-start
!
!
! !--- Disable keepalive packet to multicast network on voice class and apply to LMR port !
voice class permanent 1
 signal timing oos restart 50000
 signal timing oos timeout disabled
 signal keepalive disabled
 signal sequence oos no-action !---Loopback0 used as source for all H323 and SCCP packets generated by CME interface Loopback0
 ip address 11.1.1.1 255.255.255.255
 h323-gateway voip interface
 h323-gateway voip bind srcaddr 11.1.1.1
! !---Vif1 (virtual host interface) used as source for all multicast packets generated by CME !
interface Vif1
 ip address 192.168.11.1 255.255.255.252
 ip pim dense-mode
!
interface FastEthernet0/0
 no ip address
 shutdown
! !---Service-engine interface used to access Cisco Unity Express !
interface Service-Engine0/0
 ip unnumbered Vlan10
service-module ip address 192.168.1.2 255.255.255.0
service-module ip default-gateway 192.168.1.1
!
interface FastEthernet0/1
no ip address
shutdown
!
interface FastEthernet0/0/0
 switchport access vlan 10
 no ip address
!
interface FastEthernet0/0/1
 switchport access vlan 10
 no ip address
!
interface FastEthernet0/0/2
 switchport access vlan 10
 no ip address
!
interface FastEthernet0/0/3
 switchport access vlan 10
 no ip address
!
interface Vlan1
 no ip address
! !---All IP phones reside on VLAN 10 interface Vlan10
 ip address 192.168.1.1 255.255.255.0
 ip pim dense-mode
!
 ip classless !--- Static route to reach other devices on network ip route 0.0.0.0 0.0.0.0 192.168.1.2 !--- Static route to reach Cisco Unity Express ip route 192.168.1.2 255.255.255.255 Service-Engine0/0
!
ip http server
ip http path flash:
!
!
tftp-server flash:P00305000301.sbn
!
control-plane
!
!
! !---VOIP side of the Back-to-Back T1 used for bridging VOIP to !---Multicast (Hoot n' Holler) !---Port 0/3/0:x connects to Port 0/3/1:x voice-port 0/3/0:1
 auto-cut-through
!
voice-port 0/3/0:2
 auto-cut-through
!
.
.
.
!
voice-port 0/3/0:24
 auto-cut-through
! !---Multicast side of the Back-to-Back T1 used for bridging VOIP to !---Multicast (Hoot n' Holler) !--- Port 0/3/1:1 - 8 is permanently trunked to multicast bridge A212 !--- Port 0/3/1:9 - 16 is permanently trunked to multicast bridge A213 !--- Port 0/3/1:17 - 24 is permanently trunked to multicast bridge A214 voice-port 0/3/1:1
 auto-cut-through
 timeouts call-disconnect 3
 connection trunk A212
!
.
.
.
!
voice-port 0/3/1:9
 auto-cut-through
 timeouts call-disconnect 3
 connection trunk A213
!
.
.
.
!
voice-port 0/3/1:17
 auto-cut-through
 timeouts call-disconnect 3
 connection trunk A214
.
.
.
! !--- Analog FXO lines on port 0/2/x route incoming calls to CUE AA external extension 203 voice-port 0/2/0
 connection plar opx 203
!
voice-port 0/2/1
 connection plar opx 203
!
voice-port 0/2/2
 connection plar opx 203
!
voice-port 0/2/3
 connection plar opx 203
! !--- LMR devices are connected to E& ports 0/1/x. The E& ports are permanently trunked to multicast conference bridges. Port 0/1/0 will send and receive audio from conference A212 and port 0/1/1 will send and receive audio from conference A213. voice-port 0/1/0
 voice-class permanent 1
 lmr m-lead audio-gate-in
 lmr e-lead voice
 auto-cut-through
 operation 4-wire
 type 3
 signal lmr
 timeouts call-disconnect 3
 connection trunk A212
!
voice-port 0/1/1
 voice-class permanent 1
 lmr m-lead audio-gate-in
 lmr e-lead voice
 auto-cut-through
 operation 4-wire
 type 3
 signal lmr
 timeouts call-disconnect 3
 connection trunk A213
! !--- Dial-peers to route extension 212 to T1 loopback, which is trunked to bridge A212 dial-peer voice 1 pots
 preference 1
 destination-pattern 212
 port 0/3/0:1
!
.
.
.
!
dial-peer voice 8 pots
 preference 8
 destination-pattern 212
 port 0/3/0:8
! !--- Dial-peers to route extension 213 to T1 loopback, which is trunked to bridge A213 dial-peer voice 9 pots
 preference 1
 destination-pattern 213
 port 0/3/0:9
!
.
.
.
!
dial-peer voice 16 pots
 preference 8
 destination-pattern 213
 port 0/3/0:16
! !--- Dial-peers to route extension 214 to T1 loopback, which is trunked to bridge A214 dial-peer voice 17 pots
 preference 1
 destination-pattern 214
 port 0/3/0:17
!
.
.
.
!
dial-peer voice 24 pots
 preference 8
 destination-pattern 214
 port 0/3/0:24 !--- Dial-peer to route calls to CUE AA for internal ext. 202 and external ext. 203 dial-peer voice 200 voip
 destination-pattern 20.
 session protocol sipv2
 session target ipv4:192.168.1.2
 dtmf-relay sip-notify
 codec g711ulaw
 no vad
! !--- Dial-peers for multicast bridges dial-peer voice 212 voip
 destination-pattern A212
 voice-class permanent 1
 session protocol multicast
 
 session target ipv4:237.111.0.0:22222
 dtmf-relay cisco-rtp
 codec g711ulaw
 vad aggressive
!
dial-peer voice 213 voip
 destination-pattern A213
 voice-class permanent 1
 session protocol multicast
 session target ipv4:237.111.0.1:22222
 dtmf-relay cisco-rtp
 codec g711ulaw
 vad aggressive
!
dial-peer voice 214 voip
 destination-pattern A214
 voice-class permanent 1
 session protocol multicast
 session target ipv4:237.111.0.2:22222
 dtmf-relay cisco-rtp
 codec g711ulaw
 vad aggressive
!
telephony-service
 load 7960-7940 P00305000301
 max-ephones 24
 max-dn 144
 ip source-address 11.1.1.1 port 2000
  create cnf-files version-stamp Jan 01 2002 00:00:00
 voicemail 200
 web admin system name cisco password cisco
 max-conferences 8 gain -6
 transfer-system full-consult
!
!
ephone-dn 1 dual-line
 number 150
!
.
.
.
```

## Where to Go
                        	 Next

Controlling Use of the
                              		  Conference Soft Key

To block the
                           		functioning of the conference (Confrn) soft key without removing the key
                           		display, create and apply an ephone template that contains the features
                                 			 blocked command. For more information, see Templates .

To remove the
                           		conference (Confrn) soft key from one or more phones, create and apply an
                           		ephone template that contains the appropriate softkeys command. For more information, see Customize Softkeys .

## Feature
                        	 Information for Conferencing

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco
                                          					 Unified CME Version

Feature
                                          					 Information

Meet-me
                                          					 Conference

11.7

Added support for
                                          					 hardware-based Meet-me Conference on Cisco 4000 Series Integrated Services
                                          					 Router.

4.1

Added
                                          					 support for hardware-based meet-me conferences created by parties calling a
                                          					 designated conference number.

Multi-party Ad Hoc Conference

11.7

Added support for
                                          					 hardware-based Multi-party Conference on Cisco 4000 Series Integrated Services
                                          					 Router.

4.1

Added
                                          					 support for hardware-based Multi-party Conferencing Enhancements which uses
                                          					 DSPs to enhance ad hoc conferencing by allowing more parties than
                                          					 software-based ad hoc conferencing. Configuring multi-party ad hoc conferencing
                                          					 disables three-party ad hoc conferencing.

Three-Party Ad Hoc Conference

11.7

Added support for
                                          					 three-party Ad Hoc conference on Cisco 4000 Series Integrated Services Router.

4.0

End-of-conference options were introduced.

Phones connected in a three-way conference display “Conference.”

3.2.2

Conference gain control for external calls was introduced.

3.2

Conference initiator drop-off control was introduced.

2.0

Support
                                          					 for software-based conferencing was introduced.

| Note | Cisco Cloud Services Routers (CSR) do not support DSP resources. As DSP resources are mandatory to support hardware conferencing
                                       in Unified CME, you cannot host hardware conferences in a CSR router. |
|---|---|

| Conferencing Feature | Hardware-based | Software-based (Built-in Bridge) | Max Participants |
|---|---|---|---|
|  | SIP | SCCP | SIP | SCCP |  |
| Ad Hoc | Yes | Yes | Yes | No (Except 8900 Series Unified IP Phones) | Ad Hoc (Hardware)—8 Ad Hoc (Software)—3 |
| Meet Me | Yes | Yes | No | No | 32 |
| Connected | Yes (Only for 7800 and 8800 Series Unified IP Phones) | Yes (Supported as Select and Join functionality for SCCP) | No | No | 8 |
| Three-party Software Conference | No | No | No | Yes | 3 |

| Note | Three-party software conference is supported only on Cisco Integrated Services Router Generation 2 for Unified CME. Cisco
                                          4000 Series Integrated Services Routers supports three-party software conference only for Unified SRST. |
|---|---|

| Note | For more information on Ad Hoc software conference, see Ad Hoc Software Conferencing . |
|---|---|

| Note | For Connected Conference to work on phones, you must enable Ad Hoc hardware conferencing in Unified CME. Only Cisco IP Phone 7800 Series and Cisco IP Phone 8800 Series support Connected Conference. |
|---|---|

| Note | Connected Conference supports a maximum of eight participants. |
|---|---|

| Note | The phone firmware files that support Connected Conference on Cisco IP
                                             		  Phone 8800 Series is unavailable until the next Unified CME release. Hence,
                                             		  Connected Conference support for SIP phones is limited to Cisco IP Phone 7800
                                             		  Series for Unified CME Release 11.7. |
|---|---|

| Note | Even if you have configured cBarge softkey, the softkey display on the phone is Barge . |
|---|---|

| Note | For Max Conference in Unified CME, the configuration is same for both SIP and SCCP phones. |
|---|---|

| Note | If an idle channel is not available in the same octo-line directory number, Unified CME does not pick an idle channel from
                                             another directory number. Also, you cannot select hold calls in the other channels of the directory number or for other directory numbers. It is supported only for single-line
                                             and dual-line directory numbers. |
|---|---|

| Restriction | When a three-way software conference is established, a participant cannot use call transfer to join the remaining conference
                                                   participants to a different number. Three-party software conferencing does not support meet-me conferences. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# | Enters
                                             				telephony-service configuration mode. |
| Step 4 | max-conferences max-conference-number [ gain -6 \| 0 \| 3 \| 6 ] Example: Router(config-telephony)# max-conferences 6 | Sets the maximum number of simultaneous three-party conferences that are supported by the router. max-conference-number —Maximum value is platform-dependent. Type ? for maximum value. Default is half of the maximum value. gain —(Optional) Amount to increase the sound volume of VoIP and PSTN calls joining a conference call, in decibels. Valid values
                                                   are -6 , 0 , 3 , and 6 . The default is -6 . |
| Step 5 | end Example: Router(config-telephony)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                      					 this ephone during configuration tasks. |
| Step 4 | keep-conference [ drop-last ] [ endcall ] [ local-only ] Example: Router(config-ephone)# keep-conference endcall | Allows
                                             				conference initiators to exit from conference calls and to either end or
                                             				maintain the conference for the remaining parties. no keep-conference —(Default; the no form of
                                                      					 the command) The conference initiator can hang up or press the EndCall soft key
                                                      					 to end the conference and disconnect all parties or press the Confrn soft key
                                                      					 to drop only the last party that was connected to the conference. keep-conference —(No keywords used) The conference
                                                      					 initiator can press the EndCall soft key to end the conference and disconnect
                                                      					 all parties or hang up to leave the conference and keep the other two parties
                                                      					 connected. The conference initiator can also use the Confrn soft key (IP phone)
                                                      					 or hookflash (analog phone) to break up the conference but stay connected to
                                                      					 both parties. drop-last —The action of the Confrn soft key is
                                                      					 changed; the conference initiator can press the Confrn soft key (IP phone) or
                                                      					 hookflash (analog phone) to drop the last party. endcall —The action of the EndCall soft key is
                                                      					 changed; the conference initiator can hang up or press the EndCall soft key to
                                                      					 leave the conference and keep the other two parties connected. local-only —The conference initiator can hang up to
                                                      					 end the conference and leave the other two parties connected only if one of the
                                                      					 remaining parties is local to the Cisco Unified CME system (an internal
                                                      					 extension). |
| Step 5 | end Example: Router(config)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag \| OR voice register template template-tag Example: Router(config)# voice register pool 3 OR Router(config)# voice register template 3 | Enters voice
                                             				register pool or voice register template configuration mode to set
                                             				phone-specific parameters for SIP phones. pool-tag —Unique sequence number of the SIP phone
                                                      					 to be configured. Range is 1 to 100 or the upper limit as defined by max-pool command. template-tag —Unique
                                                      					 sequence number of the template to be applied to the SIP phone. Range is 1 to
                                                      					 10. |
| Step 4 | keep-conference Example: Router(config-register-pool)# keep-conference OR Router(config-register-temp)# keep-conference | Allows a
                                             				Cisco Unified IP phone conference initiator to exit from conference calls and
                                             				keeps the remaining parties connected. Note This step is
                                                         				  included to illustrate how to enable the command if it was previously disabled. Default is
                                                      					 enabled. Remaining
                                                      					 calls are transferred without consultation as enabled by the transfer-attended (voice register template) or transfer-blind (voice register template) commands. Note keep-conference command is configured
                                                         				  under voice register template only if you configure voice register template
                                                         				  command in the previous step. | Note | This step is
                                                         				  included to illustrate how to enable the command if it was previously disabled. | Note | keep-conference command is configured
                                                         				  under voice register template only if you configure voice register template
                                                         				  command in the previous step. |
| Note | This step is
                                                         				  included to illustrate how to enable the command if it was previously disabled. |
| Note | keep-conference command is configured
                                                         				  under voice register template only if you configure voice register template
                                                         				  command in the previous step. |
| Step 5 | voice register
                                                				  pool pool-tag Example: Router(config-register-temp)# voice register pool 1 | (Optional) Enters voice register pool configuration mode to set
                                             				phone-specific parameters for SIP phones. Note This step is required only if you configure voice register
                                                         				  template. | Note | This step is required only if you configure voice register
                                                         				  template. |
| Note | This step is required only if you configure voice register
                                                         				  template. |
| Step 6 | template template-tag Example: Router(config-register-pool)# template 1 | (Optional) Attaches the
                                             				template tag configured to the voice register pool. Note This step is required only if you configure voice register
                                                         				  template. | Note | This step is required only if you configure voice register
                                                         				  template. |
| Note | This step is required only if you configure voice register
                                                         				  template. |
| Step 7 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

| Note | This step is
                                                         				  included to illustrate how to enable the command if it was previously disabled. |
|---|---|

| Note | keep-conference command is configured
                                                         				  under voice register template only if you configure voice register template
                                                         				  command in the previous step. |
|---|---|

| Note | This step is required only if you configure voice register
                                                         				  template. |
|---|---|

| Note | This step is required only if you configure voice register
                                                         				  template. |
|---|---|

| Restriction | The maximum number of meet-me conference parties is 32 for one DSP using the G.711 codec and 16 for the G.729 codec. A participant cannot join more than one conference at the same time. Hardware-based multi-party ad hoc conferencing for more than three parties is not supported on phones that do not support
                                             soft keys. Hardware based Ad Hoc conferencing does not support the local-consult transfer method ( transfer-system local-consult command). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice-card slot Example: Router(config)# voice-card 2 | Enters
                                             				voice-card configuration mode and configure a voice card. |
| Step 4 | dsp services dspfarm Example: Router(config-voicecard)# dsp services dspfarm | Enables
                                             				digital-signal-processor (DSP) farm services for a particular voice network
                                             				module. |
| Step 5 | exit Example: Router(config-voicecard)# exit | Exits
                                             				voice-card configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice class custom-cptone cptone-name Example: Router(config)# voice class custom-cptone jointone | Creates a
                                             				voice class for defining custom call-progress tones to be detected. |
| Step 4 | dualtone conference Example: Router(cfg-cptone)# dualtone conference | Configures
                                             				conference join and leave tones. |
| Step 5 | frequency frequency-1 [ frequency-2 ] Example: Router(cfg-cp-dualtone)# frequency 600 900 | Defines the
                                             				frequency components for a call-progress tone. |
| Step 6 | cadence { cycle-1-on-time cycle-1-off-time [ cycle-2-on-time cycle-2-off-time ] [ cycle-3-on-time
                                                				  cycle-3-off-time ] [ cycle-4-on-time cycle-4-off-time ] \| continuous } Example: Router(cfg-cp-dualtone)# cadence 300 150 300 100 300 50 | Defines the
                                             				tone-on and tone-off durations for a call-progress tone. |
| Step 7 | end Example: Router(cfg-cp-dualtone)# exit | Exits
                                             				configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | sccp local interface-type interface-number [ port port-number ] Example: Router(config)# sccp local FastEthernet0/0 | Selects the
                                             				local interface that SCCP applications (transcoding and conferencing) use to
                                             				register with Cisco Unified CME. |
| Step 4 | sccp ccm { ip-address \| dns } identifier identifier-number [ port port-number ][ version version-number ] Example: Router(config)# sccp ccm 10.4.158.3 identifier 100 version 4.0 | Enables the
                                             				Cisco Unified CME router to register SCCP applications. version-number —Must be set to 4.0 or later. |
| Step 5 | sccp ccm group group-number Example: Router(config)# sccp ccm group 123 | Creates a
                                             				Cisco Unified CME group. |
| Step 6 | bind interface interface-type interface-number Example: Router(config-sccp-cm)# bind interface fastethernet 0/0 | Binds an
                                             				interface to a Cisco Unified CME group. |
| Step 7 | exit Example: Router(config-sccp-cm)# exit | Exits SCCP
                                             				Cisco Unified CME configuration mode. |
| Step 8 | sccp Example: Router(config)# sccp | Enables SCCP
                                             				and its related applications (transcoding and conferencing). |
| Step 9 | exit Example: Router(config)# exit | Exits global
                                             				configuration mode. |

| Note | The DSP farm can
                                             			 be on the same router as the Cisco Unified CME or on a different router. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dspfarm profile profile-identifier conference Example: Router(config)# dspfarm profile 1 conference | Enters DSP
                                             				farm profile configuration mode and defines a profile for DSP farm services. |
| Step 4 | codec { codec-type \| pass-through } Example: Router(config-dspfarm-profile)# codec g711ulaw | Specifies the
                                             				codecs supported by a DSP farm profile. Note Repeat this
                                                         				  step as necessary to specify all the supported codecs. | Note | Repeat this
                                                         				  step as necessary to specify all the supported codecs. |
| Note | Repeat this
                                                         				  step as necessary to specify all the supported codecs. |
| Step 5 | conference-join custom-cptone cptone-name Example: Router(config-dspfarm-profile)# conference-join custom-cptone jointone | Associates a
                                             				custom call-progress tone to indicate joining a conference with a DSP farm
                                             				profile. Note The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . | Note | The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . |
| Note | The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . |
| Step 6 | conference-leave custom-cptone cptone-name Example: Router(config-dspfarm-profile)# conference-leave custom-cptone leavetone | Associates a
                                             				custom call-progress tone to indicate leaving a conference with a DSP farm
                                             				profile. Note The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . | Note | The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . |
| Note | The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . |
| Step 7 | maximum conference-participants max-participants Example: Router(config-dspfarm-profile)# maximum conference-participants 32 | (Optional)
                                             				Configures the maximum number of conference parties allowed in each meet-me
                                             				conference. The maximum is codec-dependent. |
| Step 8 | maximum sessions number Example: Router(config-dspfarm-profile)# maximum sessions 8 | Specifies the
                                             				maximum number of sessions that are supported by the profile. |
| Step 9 | associate application sccp Example: Router(config-dspfarm-profile)# associate application sccp | Associates
                                             				SCCP with the DSP farm profile. |
| Step 10 | end Example: Router(config-dspfarm-profile)# end | Exits to
                                             				privileged EXEC mode. |

| Note | Repeat this
                                                         				  step as necessary to specify all the supported codecs. |
|---|---|

| Note | The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . |
|---|---|

| Note | The cptone-name argument in this step must be the same as the cptone-argument in the voice class
                                                               						custom-cptone command configured in Enable DSP Farm Services for a Voice Card . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | sccp ccm group group-number Example: Router(config)# sccp ccm group 1 | Creates a
                                             				Cisco Unified CME group. |
| Step 4 | associate ccm identifier-number priority priority-number Example: Router(config-sccp-ccm)# associate ccm 100 priority 1 | Associates a
                                             				Cisco Unified CME router with the group and establishes its priority within the
                                             				group. |
| Step 5 | associate profile profile-identifier register device-name Example: Router(config-sccp-ccm)# associate profile 2 register confdsp1 | Associates a
                                             				DSP farm profile with the Cisco Unified CME group. device-name is a maximum of 16 characters. Note Repeat this
                                                         				  step for every conferencing DSP farm and transcoding DSP farm. | Note | Repeat this
                                                         				  step for every conferencing DSP farm and transcoding DSP farm. |
| Note | Repeat this
                                                         				  step for every conferencing DSP farm and transcoding DSP farm. |
| Step 6 | end Example: Router(config-sccp-ccm)# end | Exits to
                                             				privileged EXEC mode. |

| Note | Repeat this
                                                         				  step for every conferencing DSP farm and transcoding DSP farm. |
|---|---|

| Note | You cannot configure Hardware and Software conference simultaneously in Unified CME. Configuring multi-party hardware conference
                                                   in Unified CME disables three-party Ad Hoc software conferencing. This configuration is applicable to both SIP and SCCP phones in Unified CME. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | conference hardware Example: Router(config-telephony)# conference hardware | Configures a
                                             				Cisco Unified CME system for multi-party conferencing only. |
| Step 5 | transfer-system full-consult Example: Router(config-telephony)# transfer-system full-consult | Transfers
                                             				calls using H.450.2 with consultation using a second phone line, if available. The calls fall back to full-blind if a second line is not available. This is the default transfer method in Cisco Unified CME 4.0 and later versions. |
| Step 6 | sdspfarm units number Example: Router(config-telephony)# sdspfarm units 3 | Specifies the
                                             				maximum number of DSP farms that are allowed to be registered to the SCCP
                                             				server. |
| Step 7 | sdspfarm tag number device-name Example: Router(config-telephony)# sdspfarm tag 2 confdsp1 | Permits a DSP
                                             				farm to register to Cisco Unified CME and associates it with a SCCP client
                                             				interface's MAC address. Note The device-name in this step must be the same as the device-name in the associate
                                                               						profile command in Step 5 of the section Associate Unified CME with a DSP Farm Profile . | Note | The device-name in this step must be the same as the device-name in the associate
                                                               						profile command in Step 5 of the section Associate Unified CME with a DSP Farm Profile . |
| Note | The device-name in this step must be the same as the device-name in the associate
                                                               						profile command in Step 5 of the section Associate Unified CME with a DSP Farm Profile . |
| Step 8 | sdspfarm conference mute-on mute-on-digits mute-off mute-off-digits Example: Router(config-telephony)# sdspfarm conference mute-on 111 mute-off 222 | Defines
                                             				mute-on and mute-off digits for conferencing. Maximum: 3 digits. Valid values are the numbers and symbols that appear on your telephone keypad: 1, 2, 3, 4, 5, 6, 7, 8,
                                                   9, 0, *, and #. Mute-on and mute-off digits can be the same. |
| Step 9 | end Example: Router(config-telephony)# end | Exits to
                                             				privileged EXEC mode. |

| Note | The device-name in this step must be the same as the device-name in the associate
                                                               						profile command in Step 5 of the section Associate Unified CME with a DSP Farm Profile . |
|---|---|

| Note | Ensure that you configure enough directory numbers to accommodate the anticipated number of conferences. The maximum number
                                          of parties in a multi-party ad hoc conference on an IP phone is eight; the maximum on an analog phone is three. |
|---|---|

| Note | For Meet Me conference to be enabled, you need to press the MeetMe softkey on the phone as well. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag octo-line Example: Router(config)# ephone-dn 18 octo-line | Enters ephone-dn configuration mode to configure an extension (ephone-dn) for a phone line. Each ephone-dn can carry eight parties if it is configured as an octo line. Configure enough ephone-dns to accommodate the maximum number of conference participants to be supported. For multi-party ad hoc conferencing, maximum number of directory numbers is 8, but you can configure a lower maximum. For meet-me conferencing, maximum number of directory numbers is 32, but you can configure a lower maximum. Minimum number of directory numbers required: 2. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 6789 | Associates a
                                             				telephone or extension number with an ephone-dn in a Cisco Unified CME system. Each DN
                                                      					 for a conference must have the same primary and secondary number. |
| Step 5 | Enter one of the following commands: conference ad-hoc conference meetme Example: Router(config-ephone-dn)# conference ad-hoc or Router(config-ephone-dn)# conference meetme | Configures a number as a placeholder for ad hoc conferencing to associate the call with the DSP farm. or (Optional) Associates meet-me conferencing with a directory number. |
| Step 6 | preference preference-order [ secondary secondary-order ] Example: Router(config-ephone-dn)# preference 1 | Sets dial-peer
                                             				preference order for an extension (ephone-dn) associated with a
                                             				Cisco Unified IP phone. Remember
                                                      					 to configure “preference x” with low value to last DN. The lower
                                                      					 the value of the preference-order argument, the higher the
                                                      					 preference of the extension. |
| Step 7 | no huntstop [ channel ] Example: Router(config-ephone-dn)# no huntstop | Continues
                                             				call hunting behavior for an extension (ephone-dn) or an extension channel. Remember
                                                      					 to configure no huntstop for all DNs except the last one. |
| Step 8 | end Example: Router(config-ephone-dn)# end | Exits to
                                             				privileged EXEC mode. |

| Note | The following
                                             			 commands can also be configured in ephone configuration mode. Commands
                                             			 configured in ephone configuration mode have priority over commands in
                                             			 ephone-template configuration mode. |
|---|---|

| Restriction | The ConfList (including the Remove, Update, and Exit soft keys within the ConfList function) and RmLstC soft keys do not work
                                                   on a Cisco Unified IP Phone 7902, 7935, and 7936. The RmLstC, ConfList, Join, and Select functions and soft keys are not supported for software-based conferencing. The steps to configure end of conference and softkeys for hardware conference is applicable: Only for SCCP phones in Unified CME. Note For End of Conference option on SIP phones, you need to configure conference add-mode and conference drop-mode under voice register configuration mode.   For more information, see Cisco Unified Communications Manager Express Command Reference . For softkey configuration on SIP phones, you need to configure softkeys under voice register template configuration mode.  For more information, see Cisco Unified Communications Manager Express Command Reference . For Ad Hoc and Meet Me hardware conferencing. | Note | For End of Conference option on SIP phones, you need to configure conference add-mode and conference drop-mode under voice register configuration mode.   For more information, see Cisco Unified Communications Manager Express Command Reference . For softkey configuration on SIP phones, you need to configure softkeys under voice register template configuration mode.  For more information, see Cisco Unified Communications Manager Express Command Reference . |
|---|---|---|---|
| Note | For End of Conference option on SIP phones, you need to configure conference add-mode and conference drop-mode under voice register configuration mode.   For more information, see Cisco Unified Communications Manager Express Command Reference . For softkey configuration on SIP phones, you need to configure softkeys under voice register template configuration mode.  For more information, see Cisco Unified Communications Manager Express Command Reference . |

| Note | For End of Conference option on SIP phones, you need to configure conference add-mode and conference drop-mode under voice register configuration mode.   For more information, see Cisco Unified Communications Manager Express Command Reference . For softkey configuration on SIP phones, you need to configure softkeys under voice register template configuration mode.  For more information, see Cisco Unified Communications Manager Express Command Reference . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 1 | Enter
                                             				ephone-template configuration mode to create an ephone template to configure a
                                             				set of phone features. |
| Step 4 | conference add-mode [ creator ] Example: Router(config-ephone-template)# conference add-mode creator | (Optional)
                                             				Configures the mode for adding parties to conferences. creator —Only the creator can add parties to the conference. |
| Step 5 | conference drop-mode [ \| creator local ] Example: Router(config-ephone-template)# conference drop-mode creator | (Optional)
                                             				Configures the mode for dropping parties from multi-party ad hoc conferences. creator —The active conference terminates when the creator hangs up. local —The active conference terminates when the last local party in the conference hangs up or drops out of the conference. |
| Step 6 | conference admin Example: Router(config-ephone-template)# conference admin | (Optional)
                                             				Configures the ephone as the conference administrator. The administrator can: Dial in to any conference directly through the conference number Use the ConfList soft key to list conference parties Remove any party from any conference |
| Step 7 | softkeys
                                                				  connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]} Example: Router(config-ephone-template)# softkeys connected Hold Trnsfer Park Endcall Confrn ConfList Join Select RmLstC | Configures
                                             				an ephone template for softkey display during the connected call stage. The soft keys used for multi-party conferencing are RmLstC , ConfList , Join , and Select . These soft keys are supported for hard-ware based conferencing only and require the appropriate DSP farm configuration. The number and order of soft key keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone. |
| Step 8 | softkeys hold {[ Join ] [ Newcall ] [ Resume ] [ Select ]} Example: Router(config-ephone-template)# softkeys hold Join Newcall Resume Select | Configures
                                             				an ephone template to modify softkey display during the call-hold call stage. The soft keys used for multi-party conferencing are Join and Select . These soft keys are supported for hard-ware based conferencing only and require the appropriate DSP farm configuration. The number and order of softkey keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone. |
| Step 9 | softkeys idle {[ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ]} Example: Router(config-ephone-template)# softkeys idle ConfList Gpickup Join Login Newcall Pickup Redial RmLstC | Configures
                                             				an ephone template for softkey display during the idle call stage. The soft keys used for multi-party conferencing are RmLstC , ConfList , and Join . These soft keys are supported for hard-ware based conferencing only and require the appropriate DSP farm configuration. The number and order of soft key keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone. |
| Step 10 | softkeys seized {[ CallBack ] [ Cfwdall ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ]} Example: Router(config-ephone-template)# softkeys seized Redial Endcall Cfwdall Pickup Gpickup Callback Meetme | (Optional)
                                             				Configures an ephone template for softkey display during the seized call stage. You must configure the MeetMe soft key in the seized state for the ephone to initiate a meet-me conference. The number and order of soft key keywords you enter in this command correspond to the number and order of soft keys on your
                                                   phone. |
| Step 11 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 12 | ephone phone-tag Example: Router(config)# ephone 1 | Enters
                                             				ephone configuration mode to create and configure an ephone. |
| Step 13 | ephone-template template-tag Example: Router(config-ephone)# ephone-dn-template 1 | Applies an
                                             				ephone-dn template to an ephone-dn. Note The template-tag must be the same as the template-tag in Step 3. | Note | The template-tag must be the same as the template-tag in Step 3. |
| Note | The template-tag must be the same as the template-tag in Step 3. |
| Step 14 | end Example: Router(config-ephone)# exit | Exits to
                                             				privileged EXEC mode. |

| Note | The template-tag must be the same as the template-tag in Step 3. |
|---|---|

| Use the show
                                             				  running-config command to verify your configuration. Any
                                       			 non-default conferencing parameters are listed in the telephony-service portion
                                       			 of the output, and end-of-conference options are listed in the ephone portion. Example: Router# show running-config !
		  ephone-dn  1  dual-line
		   ring feature secondary
		   number 126 secondary 1261
		   description Sales
		   name Smith
		   call-forward busy 500 secondary
		   call-forward noan 500 timeout 10
		   huntstop channel
		   no huntstop
		   no forward local-calls
		  !
		  ephone  1
		   mac-address 011F.92A0.C10B
		   type 7960 addon 1 7914
		   no dnd feature-ring
		   keep-conference |
|---|

| Step 1 | Use the debug ephone commands to observe messages and states associated with an ephone. For more information, see Cisco Unified CME Command Reference . |
|---|---|
| Step 2 | Use the debug ephone detail command for SCCP calls in a software conference. |
| Step 3 | Use the debug ccsip all command for SIP calls in a software conference. |
| Step 4 | Use the debug ephone hw-conference command for SIP and SCCP calls in a hardware conference. |

| Feature
                                          					 Name | Cisco
                                          					 Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Meet-me
                                          					 Conference | 11.7 | Added support for
                                          					 hardware-based Meet-me Conference on Cisco 4000 Series Integrated Services
                                          					 Router. |
| 4.1 | Added
                                          					 support for hardware-based meet-me conferences created by parties calling a
                                          					 designated conference number. |
| Multi-party Ad Hoc Conference | 11.7 | Added support for
                                          					 hardware-based Multi-party Conference on Cisco 4000 Series Integrated Services
                                          					 Router. |
| 4.1 | Added
                                          					 support for hardware-based Multi-party Conferencing Enhancements which uses
                                          					 DSPs to enhance ad hoc conferencing by allowing more parties than
                                          					 software-based ad hoc conferencing. Configuring multi-party ad hoc conferencing
                                          					 disables three-party ad hoc conferencing. |
| Three-Party Ad Hoc Conference | 11.7 | Added support for
                                          					 three-party Ad Hoc conference on Cisco 4000 Series Integrated Services Router. |
| 4.0 | End-of-conference options were introduced. Phones connected in a three-way conference display “Conference.” |
| 3.2.2 | Conference gain control for external calls was introduced. |
| 3.2 | Conference initiator drop-off control was introduced. |
| 2.0 | Support
                                          					 for software-based conferencing was introduced. |