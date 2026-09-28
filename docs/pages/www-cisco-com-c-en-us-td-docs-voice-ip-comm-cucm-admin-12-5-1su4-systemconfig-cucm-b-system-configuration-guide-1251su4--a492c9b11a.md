---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-systemconfig-cucm-b-system-configuration-guide-1251su4--a492c9b11a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/systemConfig/cucm_b_system-configuration-guide-1251su4/cucm_m_media-resources-overview.html
retrieved_at: 2026-08-16T17:38:51.774170+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: July 31, 2025

Chapter: Configure Media Resources

## Chapter: Configure Media Resources

# Configure Media Resources

## About Media Resources

Cisco Unified Communications Manager functionality requires the use of media resources. Cisco Unified Communications Manager includes media resources such as:

Annunciators

Interactive Voice Response (IVR)

Media Termination Points (MTP)

Transcoders

Trusted Relay Points

Conference Bridges

Music On Hold/Video on Hold

You can make media resources available to calls by assigning them to a media resource group list, and then assigning that
                              list to a device pool, or to an individual device. The default setting for individual devices is to use the media resources
                              that are assigned to the device pool that the device is using.

### Media Termination Points

A media termination point (MTP) is an entity that accepts two full-duplex media streams, bridging the streams together and
                                 allowing them to be set up and torn down independently. Cisco Unified Communications Manager can insert an MTP in the media
                                 path to resolve many situations:

To act as a Trusted Relay Point (TRP)

To provide conversion between IPv4 and IPv6 for RTP streams

To deliver SIP Early Offer over SIP trunks

To address DTMF transport mismatches

To act as an RSVP agent

#### MTP for H.323 Calls

Media Termination Points can be inserted in the media path for H.323 calls in order to extend supplementary services, such
                                 as call hold, call transfer, call park, and conferencing, that are normally not available when a call is routed to an H.323
                                 endpoint. For H.323 supplementary services, MTPs are only required for endpoints that do not support EmptyCapability Set (ECS)
                                 or FastStart. All Cisco and other third party other endpoints that support ECS and FastStart do not require an MTP.

#### MTP Types

Cisco Unified Communications Manager supports the following MTP types:

Software MTPs in IOS gateways

Hardware MTPs in IOS gateways

Software MTP provided by the Cisco IP Voice Media Streaming service

The Cisco Media Termination Point Software MTP type provides a  default of 48 MTP (user configurable) resources, depending
                                 on the speed of the network and the network interface card (NIC). For example, a 100-MB Network/NIC card can support 48 MTP
                                 resources, while a 10-MB NIC card cannot.

For a 10-MB Network/NIC card, approximately 24 MTP resources can be provided. However, the exact number of MTP resources that
                                 are available depends on the resources that other applications on that PC are consuming, the speed of the processor, network
                                 loading, and various other factors.

#### MTP Registration

An MTP device always registers with its primary Unified Communications Manager if that Unified Communications Manager is available
                                 and informs the Unified Communications Manager about the number of MTP resources it supports. You can register multiple MTPs
                                 with the same Unified Communications Manager. When more than one MTP is registered with a Unified Communications Manager,
                                 that Cisco Unified Communications Manager controls the set of resources for each MTP.

For example, consider MTP server 1 as configured for 48 MTP resources, and the MTP server 2 as configured for 24 resources.
                                 If both MTPs register with the same Unified Communications Manager, that Unified Communications Manager maintains both sets
                                 of resources for a total of 72 registered MTP resources.

When  Unified Communications Manager determines that a call endpoint requires an MTP, it allocates an MTP resource from the
                                 MTP that has the least active streams. That MTP resource gets inserted into the call on behalf of the endpoint. MTP resource
                                 use remains invisible to both the users of the system and to the endpoint on whose behalf it was inserted. If an MTP resource
                                 is not available when it is needed, the call connects without using an MTP resource, and that call does not have supplementary
                                 services.

#### Media Termination Points Interactions and Restrictions

Restriction

Description

Cisco IP
                                                					 Voice Streaming Application

You can
                                                					 activate only one Cisco IP Voice Streaming Application per server. To provide
                                                					 more MTP resources, you can activate the Cisco IP Voice Streaming application
                                                					 on additional networked servers.

Cisco
                                                					 strongly recommends that you do not activate the Cisco IP Voice Streaming Media
                                                					 Application on a Cisco Unified Communications Manager with a high
                                                					 call-processing load because it can adversely affect the performance of the
                                                					 Cisco Unified Communications Manager.

Registering with Cisco Unified Communoications Manager

Each MTP
                                                					 can register with only one Cisco Unified Communications Manager at a time. The
                                                					 system may have multiple MTPs, each of which may be registered to one Cisco
                                                					 Unified Communications Manager, depending on how your system is configured.

Failover and Fallback

- If the primary Cisco Unified Communications Manager fails, the MTP attempts to register with the next available Cisco Unified
                                                   Communications Manager in the Cisco Unified Communications Manager Group that is specified for the device pool to which the
                                                   MTP belongs.

- The MTP device reregisters with the primary Cisco Unified Communications Manager as soon as it becomes available after a failure
                                                   and is currently not in use.

- The system maintains the calls or conferences that were active in call preservation mode until all parties disconnect. The
                                                   system does not make supplementary services available.

- If an MTP attempts to register with a new Cisco Unified Communications Manager and the register acknowledgment is never received,
                                                   the MTP registers with the next Cisco Unified Communications Manager.

The MTP devices unregister and then disconnect after a hard or soft reset. After the reset completes, the devices reregister
                                                with the Cisco Unified Communications Manager.

### Transcoders

A transcoder is a device that performs codec conversion, it converts an input stream from one codec into an output stream
                              that uses a different codec. For example, a transcoder can take a G.711 stream and convert it to a G.729 stream in real time.
                              During a call when the endpoints use different voice codecs, the Cisco Unified Communications Manager invokes a transcoder
                              into the media path. The transcoder converts the data streams between the two incompatible codecs to allow communication between
                              the devices. The transcoder is invisible to the user or the endpoints involved in a call.

Transcoder resources is managed by the Media Resource Manager (MRM).

The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                          providing MTP/TRP functionality.

#### Transcoders with MTP Functionality

In addition to codec conversion, a transcoder can provide the same functionality as a media termination point (MTP). In cases
                                 where both transcoder functionality and MTP functionality are needed, the system allocates a transcoder due to the fact that
                                 transcoders can provide both sets of functionality simultaneously. If only MTP functionality is required, the system allocates
                                 either a transcoder or an MTP from the resource pool. The choice of resource will be determined by the media resource groups.

If a software MTP resource is not available when it is needed, the call tries to connect without using an MTP resource and
                                 MTP/TRP services, if the Fail Call If Trusted Relay Point Allocation Fails and Fail Call If MTP Allocation Fails fields are set to 'False' in the Cisco Unified CM Administration > System > Service Parameters > Service Parameter Configuration window.  If hardware transcoder functionality is required (to convert one codec to another) and a transcoder is not available,
                                 the call will fail.

#### Transcoder Types

Transcoder types in Cisco Unified Communications Manager Administration are listed in the following table.

The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                                providing MTP/TRP functionality.

Transcoder Type

Description

Cisco Media Termination Point Hardware

This type, which supports the Cisco Catalyst 4000 WS-X4604-GWY
                                                					 and the Cisco Catalyst 6000 WS-6608-T1 or WS-6608-E1, provides the following
                                                					 number of transcoding sessions:

For the Cisco Catalyst 4000 WS-X4604-GWY

For transcoding to G.711-16 MTP transcoding sessions

For the Cisco Catalyst 6000 WS-6608-T1 or WS-6608-E1

For transcoding from G.723 to G.711/For transcoding from
                                                      						  G.729 to G.711-24 MTP transcoding sessions per physical port; 192 sessions per
                                                      						  module

Cisco IOS Media Termination Point (hardware)

This type, which supports the Cisco 2600XM, Cisco 2691, Cisco
                                                					 3725, Cisco 3745, Cisco 3660, Cisco 3640, Cisco 3620, Cisco 2600, and Cisco
                                                					 VG200 gateways, provides the following number of transcoding sessions:

Per NM-HDV

Transcoding from G.711 to G.729-60

Transcoding from G.711 to GSM FR/GSM EFR- 45

Cisco IOS Enhanced Media Termination Point (hardware)

Per NM-HD

This type, which supports Cisco 2600XM, Cisco 2691, Cisco
                                                					 3660, Cisco 3725, Cisco 3745, and Cisco 3660 Access Routers, provides the
                                                					 following number of transcoding sessions:

Transcoding for G.711 to G.729a/G.729ab/GSMFR-24

Transcoding for G.711 to G.729/G.729b/GSM EFR-18

Per NM-HDV2

This type, which supports Cisco 2600XM, Cisco 2691, Cisco
                                                					 3725, Cisco 3745, and Cisco 3660 Access Routers, provides the following number
                                                					 of transcoding sessions:

Transcoding for G.711 to G.729a/G.729ab/GSMFR-128

Transcoding for G.711 to G.729/G.729b/GSM EFR-96

PVDM4

Onboard PVDM4 modules (PVDM4-32, PVDM4-64, PVDM4-128, PVDM4-256)

DSP module on T1/E1 modules (PVDM4-32, PVDM4-64, PVDM4-128, PVDM4-256)

DSP NIMs (NIM-PVDM4-32, NIM-PVDM4-64, NIM-PVDM4-128, NIM-PVDM4-256)

These types support ISR4K (ISR44xx, ISR43xx), C83xx, and C82xx platforms provide the following number of transcoding sessions:

Transcoding for G.711 to G.729a/G.729ab/GSMFR-24

Transcoding for G.711 to G.729/G.729b/GSM EFR-18

Transcoding for G.711 to G.729a/G.729ab/GSMFR-128

Transcoding for G.711 to G.729/G.729b/GSM EFR-96

Transcoding for G.711/G.729/G.729ab/G.729a/G.729b to Opus

Cisco Media Termination Point (WS-SVC-CMM)

This type provides 64 transcoding sessions per daughter card
                                                					 that is populated: 64 transcoding sessions with one daughter card, 128
                                                					 transcoding sessions with two daughter cards, 192 transcoding sessions with
                                                					 three daughter cards, and 256 transcoding sessions with four daughter cards
                                                					 (maximum).

This type provides transcoding between any combination of the
                                                					 following codecs:

G.711 a-law and G.711 mu-law

G.729 annex A and annex B

G.723.1

GSM (FR)

GSM (EFR)

#### Transcoder Interactions and Restrictions

##### Transcoder Interactions and Restrictions

Interactions  or Restriction

Description

Transcoder Deletion

You cannot delete a transcoder that is assigned to a media
                                                						resource group. To find out which media resource groups are using the
                                                						transcoder, click Dependency Records from the Related Links drop-down list box on
                                                						the Transcoder Configuration window and
                                                						click Go . The Dependency Records Summary
                                                						window displays information about media resource groups that are using the
                                                						transcoder. To find out more information about the media resource group, click
                                                						the media resource group, and the Dependency Records Details window displays.
                                                						If the dependency records are not enabled for the system, the dependency
                                                						records summary window displays a message. If you try to delete a transcoder
                                                						that is in use, Cisco Unified Communications Manager displays a message. Before
                                                						deleting a transcoder that is currently in use, you must remove the transcoder
                                                						from the media resource group(s) to which it is assigned.

Failover and Fallback

Transcoder failover and fallback works as follows:

If the primary Unified Communications Manager node fails, the transcoder attempts to register with the next available node in the Unified Communications Manager Group that is specified for the device pool to which the transcoder belongs.

The transcoder device reregisters with the primary Cisco Unified Communications Manager node as soon as it becomes available.

A transcoder device unregisters with a Unified Communications Manager node that becomes unreachable. Calls that were using this transcoding profile for transcoding move to the preservation state
                                                      and the transcoder attempts to register with the next available node. Gateway uses RTP/ RTCP timeout to inform to registered
                                                      Unified Communications Manager of resource release.

If a transcoder attempts to register with a new Unified Communications Manager node and the register acknowledgment is never received, the transcoder registers with the next node in the list.

Transcoder devices will unregister and then disconnect after a hard or soft reset. After the reset completes, the devices
                                                reregister with the primary Cisco Unified Communications Manager node.

### Trusted Relay
                           	 Point Overview

A Trusted Relay Point (TRP) is an MTP or transcoder that Cisco Unified Communications Manager can insert into the media stream
                                 to act as a control point for call media. The TRP can provide further processing on the stream and can ensure that the stream
                                 follows a specific path.

When a call requires a trusted relay point, Cisco Unified Communications Manager allocates an MTP or transcoder that has been
                                 enabled with TRP functionality.

#### Configuration

Both MTPs and transcoders can be configured to provide TRP functionality by checking the Trusted Relay Point check box in the Media Termination Point Configuration or Transcoder Configuration window.

You can configure the TRP requirement for individual calls by setting the Use Trusted Relay Point field to On for the following configuration windows:

Phone Configuration

Gateway Configuration

Voicemail Port Configuration

Trunk Configuration

CTI Route Point Configuration

Common Device Configuration

Universal Device Template Configuration

Various media resource configurations (Annunciator, IVR, MTPs, Transcoders, Conference Bridges, Music On Hold)

#### Trusted Relay Points Interactions and Restrictions

Feature

Interactions and Restrictions

Resource
                                                						Reservation Protocol (RSVP)

If RSVP
                                                						is enabled for the call, Cisco Unified
                                                   						  Communications Manager first tries to allocate an RSVPAgent that is
                                                						also labeled as TRP. Otherwise, another TRP device is inserted between the
                                                						RSVPAgent and the endpoint.

Transcoder for call

If you
                                                						need a transcoder for the call and need to allocate it on the same side as the
                                                						endpoint that needs TRP, Cisco Unified
                                                   						  Communications Manager first tries to allocate a transcoder that is
                                                						also labeled as TRP. Otherwise, another TRP device is inserted between the
                                                						transcoder and the endpoint.

MTP allocation for  endpoint

If you check both the Media Termination Point Required check box and the Use Trusted Relay Point check box for an endpoint, Cisco Unified Communications Manager should allocate an MTP that is also a TRP. If the administrator fails to allocate such an MTP or TRP, the call status appears.

TRP allocation

In most instances, TRP is allocated after users answer the call, so if a call fails due to failure to allocate the TRP, users
                                                may receive fast-busy tone after answering the call. (The SIP outbound leg with MTP required, or H.323 outbound faststart,
                                                represents an exception.)

TRP Insertion for endpoint

Cisco Unified Communications Manager must insert a TRP for the endpoint if you have checked the Use Trusted Relay Point check box for either the endpoint or the device pool that is associated with the device. The call may fail if Cisco Unified Communications Manager fails to allocate a TRP while the Fail Call If Trusted Relay Point Allocation Fails service parameter is set to True .

TRP and remote users

TRP is not recommended for providing secure solution for work from home remote users. Expressway's Mobile and Remote Access
                                                is the recommended solution.

#### Call Behavior with Insufficent TRP Resources

The following sections provide examples of how Cisco Unified Communications Manager handles calls when insufficient MTP resources
                                    are allocated. The ulimate call behavior depends on whether MTPs and TRPs are required for those endpoints, and whether the
                                    system is configured to fail calls automatically when MTP or TRP allocation fails.

##### MTP and TRP are Both Required

The following table shows whether a call fails when both the Media Termination Point Required and Use Trusted Relay Point options are selected for an endpoint, and insufficient MTP and TRP resources exist.

The final call status depends on whether the Fail Call If Trusted Relay Point Allocation Fails and the Fail Call if MTP Allocation Fails service parameters are set to fail calls automatically.

Fail Call If TRP Allocation Fails  Service Parameter

Fail Call If MTP Allocation Fails Service Parameter

Unified CM Fails Call?

True

True

Yes

True

False

Yes

False

True

Yes, if MTP is required for H.323 endpoint. No, if MTP is required for SIP endpoint.

False

False

No

##### Automatic Call Failure for Insufficient MTP/TRP Resources Not Enabled

The following table shows the call behavior when insufficient MTP/TRP resources exists and both the Fail Call If Trusted Relay Point Allocation Fails and Fail Call If MTP Allocation Fails service parameters are set to False .

MTP Required = Yes

Use TRP = Yes

Resource Allocation Status

Call Behavior

Y

Y

TRP allocated

Audio call only because no pass-through support exists.

Y

Y or N

MTP only

Audio call only. No TRP support.

Y

Y or N

None allocated

If MTP required is checked for H.323 endpoint, supplementary services will be disabled.

N

Y

TRP allocated

Audio or video call depends on endpoint capabilities, and call admission control (CAC). Supplementary services still work.

N

Y

None allocated

Audio or video call. Supplementary services still work, but no TRP support exists.

### Annunciator
                           	 Overview

An annunciator is an SCCP software devices that runs on Cisco Unified Communications Manager and which allows you to send
                                 prerecorded messages and tones to Cisco IP Phones and gateways. The annunciator is activated on a cluster node by turning
                                 on the Cisco IP Voice Media Streaming service on that node. Features such as MLPP, SIP trunks, IOS gateways, and software
                                 conference bridges rely on the annunciator to send the predefined message to the phone or gateway via a one-way media stream.
                                 In addition:

Both IPv4 and IPV6 are supported. The annunciator is configured automatically in dual mode when the system's platform is configured
                                       for IPv6 and the IPv6 enterprise parameter is enabled.

SRTP is supported

#### Annunciator Scalability

By default, an annunciator supports 48 simultaneous media streams. You can add capacity by activating the annunciator on additional
                                 nodes or by changing the default number of annunciator media streams via the Call Count service parameter. However, it's not recommended to increase this value on a node unless the Cisco CallManager service is deactivated on that node.

If the annunciator runs on a dedicated subscriber node where the Cisco CallManager service does not run, the annunciator can support up to 255 simultaneous announcement streams. If the dedicated subscriber
                                 node meets the OVA virtual machine configuration for 10,000 users, the annunciator can support up to 400 simultaneous announcement
                                 streams.

Caution

We recommend that you do not activate the annunciator on Unified Communications Manager nodes that have a high call-processing load.

#### Annunciator with Conference Bridge

The Annunciator is available to a conference bridge under the following conditions:

If the media resource group list that contains the annunciator is assigned to the device pool where the conference bridge
                                       exists.

If the annunciator is configured as the default media resource.

The annunciator is not available to a conference bridge if the media resource group list is assigned directly to the device
                                 that controls the conference.

Each conference supports only one announcement. If the system requests another announcement while the current announcement
                                 is playing, the new announcement preempts the one that is playing.

#### Default Annunciator Announcements and Tones

Announcement —
                                             				Played for devices that are configured for Cisco Multilevel Precedence and
                                             				Preemption.

Barge tone —
                                             				Heard before a participant joins an ad hoc conference.

Ring back tone
                                             				— When you transfer a call over the PSTN through an IOS gateway, the
                                             				annunciator plays the tone because the gateway cannot play the tone when the
                                             				call is active.

Ring back tone
                                             				— When you transfer calls over an H.323 intercluster trunk, a tone is played.

Ring back tone
                                             				— When you transfer calls to the SIP client from a phone that is running SCCP,
                                             				a tone is played.

You cannot change
                                    		  the default prerecorded annunciator announcements or add additional
                                    		  announcements. Localization of the announcement is supported if the Cisco Unified Communications Manager Locale Installer
                                    		  is installed and the locale settings are configured for the Cisco Unified IP
                                    		  Phone or device pool. For information about the Locale Installer and the files
                                    		  to install for user and (combined) network locales, see Installing
                                       			 Cisco Unified Communications Manager . To download the locale installer,
                                    		  see the support pages at www.cisco.com .

Condition

Announcement

An equal
                                                					 or higher precedence call is in progress.

Precedence
                                                					 access limitation has prevented the completion of your call. Please hang up and
                                                					 try again. This is a recording.

A
                                                					 precedence access limitation exists.

Precedence
                                                					 access limitation has prevented the completion of your call. Please hang up and
                                                					 try again. This is a recording.

Someone
                                                					 attempted an unauthorized precedence level.

The
                                                					 precedence used is not authorized for your line. Please use an authorized
                                                					 precedence or ask your operator for assistance. This is a recording.

The call
                                                					 appears busy, or the administrator did not configure the directory number for
                                                					 call waiting or preemption.

The number
                                                					 you have dialed is busy and not equipped for call waiting or preemption. Please
                                                					 hang up and try again. This is a recording.

The system
                                                					 cannot complete the call.

Your call
                                                					 cannot be completed as dialed. Please consult your directory and call again or
                                                					 ask your operator for assistance. This is a recording.

A service
                                                					 interruption occurred.

A service
                                                					 disruption has prevented the completion of your call. In case of emergency call
                                                					 your operator. This is a recording.

The following
                                    		  table lists the tones that the annunciator supports.

Type

Description

Busy
                                                					 tone

A busy
                                                					 tone is heard when the dialed number is busy.

Barge tone

A
                                                					 conference barge-in tone is heard before the participant joins an ad hoc
                                                					 conference.

Ring back
                                                					 tone

When
                                                         						  you transfer a call over the PSTN through an IOS gateway.

When
                                                         						  you transfer a call over an H.323 intercluster trunk.

When
                                                         						  you transfer a call to the SIP client from an SCCP phone.

### Interactive Voice
                           	 Response Overview

The Interactive
                                 		  Voice Response (IVR) device enables Cisco
                                    			 Unified Communications Manager to play prerecorded feature
                                 		  announcements (.wav files) to devices such as Cisco Unified IP Phones and
                                 		  Gateways. These announcements play on devices that use features which require
                                 		  IVR announcements, like Conference Now.

When you add a
                                 		  node, an IVR device is automatically added to that node. The IVR device remains
                                 		  inactive until the Cisco IP Voice Media Streaming Application service is
                                 		  activated on that node.

An IVR supports 48
                                 		  simultaneous callers by default. You can change the number of IVR callers using
                                 		  the Cisco IP Voice Media Streaming Application service parameter. However, we
                                 		  recommend that you do not exceed 48 IVR callers on a node. You can configure
                                 		  the number of callers for IVR based on expected simultaneous calls to IVR for
                                 		  joining Conference Now.

Caution

Do not activate
                                             			 the IVR device on Cisco
                                                				Unified Communications Manager nodes that have a high call-processing
                                             			 load.

#### Default IVR Announcements and Tones

Announcement

Condition

ConferenceNowAccessCodeFailed Announcement

Plays when
                                                   					 an attendee enters the wrong access code to join Conference Now after exceeding
                                                   					 the maximum number of attempts.

ConferenceNowAccessCodeInvalid Announcement

Plays when
                                                   					 an attendee enters the wrong access code.

ConferenceNowCFBFailed Announcement

Plays when
                                                   					 the conference bridge capacity limit is exceeded while initiating Conference
                                                   					 Now.

ConferenceNowEnterAccessCode Announcement

Plays when
                                                   					 an attendee joins Conference Now and the host sets an attendee access code.

ConferenceNowEnterPIN Announcement

Plays when
                                                   					 a host or attendee tries to join a meeting.

ConferenceNowFailedPIN Announcement

Plays
                                                   					 after the host exceeds the maximum number of attempts to enter a correct PIN.

ConferenceNowGreeting Announcement

Plays a
                                                   					 greeting prompt for Conference Now.

ConferenceNowInvalidPIN Announcement

Plays when
                                                   					 the host enters a wrong PIN.

ConferenceNowNumberFailed Announcement

Plays
                                                   					 when a host or attendee enters the wrong meeting number after exceeding the
                                                   					 maximum number of attempts.

ConferenceNowNumberInvalid Announcement

Plays when
                                                   					 a host or attendee enters a wrong meeting number.

#### Interactive Voice
                              	 Response Restrictions

Feature

Restriction

Load Balancing

The Interactive Voice Response (IVR) uses Real-Time Protocol (RTP) streams through a common media device driver. This device
                                                driver is also used by other software media devices provided by the Cisco IP Voice Media Streaming Application services such
                                                as Music On Hold (MOH), Software Media Termination Point (MTP), Software Conference Bridge (CFB), and Annunciator.

Configuring a larger call volume affects the system performance. This also impacts call processing if the Call Manager service
                                                is active on the same server node.

DTMF Digits

The IVR
                                                						supports only Out-Of-Band (OOB) DTMF digit collection method. If there is a
                                                						DTMF capability mismatch between the calling device and the IVR, an MTP will be
                                                						allocated.

Codecs

The IVR
                                                						only supports codec G.711 (a-law and mu-law), G.729, and Wide Band 256k. If
                                                						there is a codec mismatch between the calling device and the IVR, a transcoder
                                                						will be allocated.

### Announcements Overview

In Cisco Unified Communications Manager Administration, use the Menu Resources > Announcements menu path to configure announcements. There are two classifications of announcements:

- System Announcements—Pre-defined announcements that are used in normal call processing or provided as sample feature announcements.

- Feature Announcements—Used by features such as Music on Hold (MOH), Hunt Pilots with Call Queuing or External Call Control.
                                    You can customize your own feature announcements by uploading Cisco-provided audio files or uploading custom .wav files. Upload all custom announcement .wav files to all servers in the cluster.

You can hear custom announcements such as warning or reorder tones if you are connected through a trunk or gateway. However,
                                          you cannot hear custom announcements on calls between two IP phones or IP phones and Jabber clients.

#### Formats

The recommended format for announcements includes the following specifications:

16-bit PCM wav file

Stereo or mono

Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz

#### Default
                              	 Announcements

You can
                                    		  upload custom announcement .wav files or change the Cisco-provided file for a
                                    		  system announcement. However, you cannot change the announcement identifier.
                                    		  For example, the System announcement (VCA_00121) is played when a caller dials
                                    		  an invalid number. This is commonly known as the vacant call announcement.

Announcement Identifier

Description

Gone_00126

System:
                                                					 Gone

MLPP-BNEA_00123

System:
                                                					 MLPP Busy not equipped

MLPP-BPA_00122

System:
                                                					 MLPP Higher precedence

MLPP-ICA_00120

System:
                                                					 MLPP Service disruption

MLPP-PALA_00119

System:
                                                					 MLPP Precedence access limit

MLPP-UPA_00124

System:
                                                					 MLPP Unauthorized precedence

Mobility_VMA

Please
                                                					 press 1 to be connected

MonitoringWarning_00055

System:
                                                					 Monitoring or Recording

RecordingWarning_00038

System:
                                                					 Recording

TemporaryUnavailable_00125

System:
                                                					 Temporary unavailable

VCA_00121

System:
                                                					 Vacant number / invalid number dialed

Wait_In_Queue_Sample

Builtin:
                                                					 Sample queued caller periodic announcement

Welcome_Greeting_Sample

Builtin:
                                                					 Sample caller greeting

## Media Resources Configuration Task Flow

Step 1

Activate Software Media Resources

Turning on the IPVMS service activates software media resources on the server.

Step 2

Configure Media Termination Points

Configure Media Termination Points (MTPs) for your system.

Step 3

Configure Transcoders

Add Transcoder resources to the system.

Step 4

Configure the Interactive Voice Response (IVR)

Configure default settings for the system IVR.

Step 5

Configure the Annunicator

Configure system settings for the Annunciator.

Step 6

Configure Media Resource Groups

Add your media resources into a Media Resource Group. Set up multiple groups with different combinations of resources.

Step 7

Configure Media Resource Group Lists

Create a list of Media Resource Groups that you can assign to an endpoint, or class of endpoints.

Step 8

Assign Media Resources to Device or Device Pool

Make media resources available to endpoints by assigning them to a device or device pool.

Step 9

Configure Announcement

Optional . Configure settings for specific announcements. Announcements are used in normal processing, or for features like Music On
                                          Hold or IVR.

Step 10

Upload a Customized Announcement

Optional . Upload a prerecorded announcement. Assign the file to a new or existing announcement.

### Activate Software Media Resources

Annunciator

Interactive Voice Response (IVR)

Media Termination Point (MTP)

Software Conference Bridges

Music On Hold

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server , select a Unified Communications Manager node.

Step 3

Check the Cisco IP Voice Media Streaming Service and click Save .

### Configure Media Termination Points

#### Before you begin

Determine the number of MTP resources that are needed and the number of MTP devices that are needed to provide these resources.

Step 1

From Cisco Unified CM
                                          			 Administration, choose Media Resources > Media
                                                				  Termination Point .

Step 2

Do either of the following:

- Click Find and select an existing MTP.

- Click Add New to create a new MTP.

Step 3

Assign a Media Termination Point Name .

Step 4

Assign a Device Pool .

Step 5

Check the Trusted Relay Point check box if you want to designate this MTP as a Trusted Relay Point (TRP).

Step 6

Click Save .

### Configure Transcoders

A transcoder is a
                                 		  device that converts an input stream from one codec into an output stream that
                                 		  uses a different codec.

#### Before you begin

Determine the number of transcoder resources that are needed and the number of transcoder devices that are needed to provide
                                 these resources.

Step 1

Log into Cisco
                                          			 Unified CM Administration and choose Media
                                                				  Resources > Transcoder .

Step 2

Do either of the following:

- Click Find and select an existing transcoder.

- Click Add New .

Step 3

Select the Transcoder Type .

Step 4

Enter the MAC Address of the transcoder.

Step 5

Assign a Device Pool from the drop-down menu.

Step 6

Check the Trusted Relay Point check box if you want to make this transcoder available as a trusted relay point.

Step 7

Click Save .

### Configure the Interactive Voice Response (IVR)

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose Media Resources > Interactive Voice Response .

Step 2

Click Find and select the IVR.

Step 3

Enter a Name and Description .

Step 4

If you want IVR calls to use a trusted relay point, set the Use Trusted Relay Point drop-down to On .

Step 5

Complete the remaining fields in the Interactive Voice Response Configuration window. For help with the fields and their settings, see the online help.

Step 6

Click Save .

### Configure the Annunicator

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose Media Resources > Annunciator .

Step 2

Click Find and select the annunciator.

Step 3

Enter a Name and Description .

Step 4

Select a Device Pool .

Step 5

If you want the annunciator to use a trusted relay point, set the Use Trusted Relay Point drop-down to On .

Step 6

Click Save .

### Configure Media Resource Groups

Step 1

From Cisco Unified CM Administration, choose Media Resources > Media Resource Group .

Step 2

Do either of the following:

- Click Find and select an existing media resource group.

- Click Add New to create a new media resource group.

Step 3

Configure the
                                          			 fields in the Media
                                             				Resource Group Configuration window. See the online help about the
                                          			 fields and their configuration options.

Step 4

Enter a Name and Description for the group.

Step 5

From Available Media Resources , select the resources you want to add to this group, and use the arrows to move the resources to Selected Media Resources .

Step 6

(Optional) To use multicast for Music On Hold audio, check the Use Multi-cast for MOH Audio check box.

Step 7

Click Save .

### Configure Media Resource Group Lists

Step 1

From Cisco Unified CM Administration, choose Media Resources > Media Resource Group List .

Step 2

Do either of the following:

- Click Find and select an existing list.

- Click Add New and create a new list.

Step 3

Enter a Name for the media resource group list.

Step 4

From Available Media Resource Groups , select the groups you want to add, and use the arrows to move them to Selected Media Resource Groups .

Step 5

Click Save .

### Assign Media Resources to Device or Device Pool

Step 1

From the Cisco Unified CM Administration, choose Devices > Phone .

- To add media resources to a device pool, choose System > Device Pools .

- To add media resource directly to an endpoint, choose Device > Phone .

Step 2

Click Find and select the device pool or device to which you want to assign these media resources.

Step 3

From the Media Resource Group List drop-down, select a list.

Step 4

Click Save .

Step 5

Click Apply Config to Selected .

### Configure
                           	 Announcement

You can configure
                                 		  an announcement that you can use as a system announcement or as a feature
                                 		  announcement. A system announcement is used for call processing or for the use
                                 		  of sample feature announcements whereas a feature announcement is used for
                                 		  specific features, such as music on hold (MOH) in association with hunt pilot
                                 		  call queuing or external call control.

You can modify an
                                 		  existing announcement or configure a new announcement in Cisco Unified
                                 		  Communications Manager.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Announcement .

Step 2

Do one of the following:

- Click Find and select an existing announcement to edit.

- Click Add New to add a new announcment.

Step 3

Configure the fields in the Announcement Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Upload a
                           	 Customized Announcement

You can modify a default announcement with an uploaded custom .wav file with a different announcement. When you import an
                                 audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by
                                 the music on hold (MOH) server.

Announcements are specific to the locale (language). If your installation is using more than one language locale, you have
                                             to record each custom announcement each language as a separate .wav file and upload with the correct locale assignment. This
                                             task also requires that the correct locale package is installed on each server before uploading custom announcement .wav files
                                             for languages other than United States English.

Similar to MOH audio source files, the recommended format for announcements includes the following specifications:

16-bit PCM .wav file

Stereo or mono

Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz

You cannot update announcements that are not hyperlinked in the Find and List Announcements window in Unified Communications Manager. You can add customized announcements for Cisco-provided announcements that are
                                             underlined with a hyperlink in this window. For example, MLPP-ICA_00120 and MonitoringWarning_00055.

Step 1

From Cisco Unified CM
                                             				Administration , choose Media
                                                				  Resources > Announcement .

Step 2

From the Find
                                             				and List Announcements window, enter search criteria, click Find , and click the hyperlink for the announcement
                                          			 from the resulting list.

Step 3

From the Announcement Configuration window, click Upload File .

Step 4

From the Upload
                                             				File pop-up window, choose the locale, enter the filename and browse
                                          			 to select the .wav file, and click Upload
                                             				File .

The upload process begins and the status is updated after the processing is complete. Select Close to close the Upload File window.

Step 5

(Optional) If you want Unified Communications Manager to play the customized announcement instead of playing the Cisco-provided announcement, check the Enable check box appears in the Announcement by Locale pane in the Announcements Configuration window.

If the Enable check box is unchecked, Unified Communications Manager plays the Cisco-provided announcement.

Step 6

Click Save .

#### What to do next

Upload the
                                 		  announcement on each node in the cluster as the announcement files are not
                                 		  propagated between servers in a cluster. Browse for Cisco
                                    			 Unified Communications Manager Administration on each server in the
                                 		  cluster and repeat the upload process.

| Note | For information on configuring Music On Hold, refer to the Feature Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Restriction | Description |
|---|---|
| Cisco IP
                                                					 Voice Streaming Application | You can
                                                					 activate only one Cisco IP Voice Streaming Application per server. To provide
                                                					 more MTP resources, you can activate the Cisco IP Voice Streaming application
                                                					 on additional networked servers. Cisco
                                                					 strongly recommends that you do not activate the Cisco IP Voice Streaming Media
                                                					 Application on a Cisco Unified Communications Manager with a high
                                                					 call-processing load because it can adversely affect the performance of the
                                                					 Cisco Unified Communications Manager. |
| Registering with Cisco Unified Communoications Manager | Each MTP
                                                					 can register with only one Cisco Unified Communications Manager at a time. The
                                                					 system may have multiple MTPs, each of which may be registered to one Cisco
                                                					 Unified Communications Manager, depending on how your system is configured. |
| Failover and Fallback | This section describes how MTP devices failover and fallback when the Cisco Unified Communications Manager to which they are
                                             registered becomes unreachable: If the primary Cisco Unified Communications Manager fails, the MTP attempts to register with the next available Cisco Unified
                                                   Communications Manager in the Cisco Unified Communications Manager Group that is specified for the device pool to which the
                                                   MTP belongs. The MTP device reregisters with the primary Cisco Unified Communications Manager as soon as it becomes available after a failure
                                                   and is currently not in use. The system maintains the calls or conferences that were active in call preservation mode until all parties disconnect. The
                                                   system does not make supplementary services available. If an MTP attempts to register with a new Cisco Unified Communications Manager and the register acknowledgment is never received,
                                                   the MTP registers with the next Cisco Unified Communications Manager. The MTP devices unregister and then disconnect after a hard or soft reset. After the reset completes, the devices reregister
                                                with the Cisco Unified Communications Manager. |

| Note | The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                          providing MTP/TRP functionality. |
|---|---|

| Note | The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                                providing MTP/TRP functionality. |
|---|---|

| Transcoder Type | Description |
|---|---|
| Cisco Media Termination Point Hardware | This type, which supports the Cisco Catalyst 4000 WS-X4604-GWY
                                                					 and the Cisco Catalyst 6000 WS-6608-T1 or WS-6608-E1, provides the following
                                                					 number of transcoding sessions: For the Cisco Catalyst 4000 WS-X4604-GWY For transcoding to G.711-16 MTP transcoding sessions For the Cisco Catalyst 6000 WS-6608-T1 or WS-6608-E1 For transcoding from G.723 to G.711/For transcoding from
                                                      						  G.729 to G.711-24 MTP transcoding sessions per physical port; 192 sessions per
                                                      						  module |
| Cisco IOS Media Termination Point (hardware) | This type, which supports the Cisco 2600XM, Cisco 2691, Cisco
                                                					 3725, Cisco 3745, Cisco 3660, Cisco 3640, Cisco 3620, Cisco 2600, and Cisco
                                                					 VG200 gateways, provides the following number of transcoding sessions: Per NM-HDV Transcoding from G.711 to G.729-60 Transcoding from G.711 to GSM FR/GSM EFR- 45 |
| Cisco IOS Enhanced Media Termination Point (hardware) | Per NM-HD This type, which supports Cisco 2600XM, Cisco 2691, Cisco
                                                					 3660, Cisco 3725, Cisco 3745, and Cisco 3660 Access Routers, provides the
                                                					 following number of transcoding sessions: Transcoding for G.711 to G.729a/G.729ab/GSMFR-24 Transcoding for G.711 to G.729/G.729b/GSM EFR-18 Per NM-HDV2 This type, which supports Cisco 2600XM, Cisco 2691, Cisco
                                                					 3725, Cisco 3745, and Cisco 3660 Access Routers, provides the following number
                                                					 of transcoding sessions: Transcoding for G.711 to G.729a/G.729ab/GSMFR-128 Transcoding for G.711 to G.729/G.729b/GSM EFR-96 PVDM4 Onboard PVDM4 modules (PVDM4-32, PVDM4-64, PVDM4-128, PVDM4-256) DSP module on T1/E1 modules (PVDM4-32, PVDM4-64, PVDM4-128, PVDM4-256) DSP NIMs (NIM-PVDM4-32, NIM-PVDM4-64, NIM-PVDM4-128, NIM-PVDM4-256) These types support ISR4K (ISR44xx, ISR43xx), C83xx, and C82xx platforms provide the following number of transcoding sessions: Transcoding for G.711 to G.729a/G.729ab/GSMFR-24 Transcoding for G.711 to G.729/G.729b/GSM EFR-18 Transcoding for G.711 to G.729a/G.729ab/GSMFR-128 Transcoding for G.711 to G.729/G.729b/GSM EFR-96 Transcoding for G.711/G.729/G.729ab/G.729a/G.729b to Opus |
| Cisco Media Termination Point (WS-SVC-CMM) | This type provides 64 transcoding sessions per daughter card
                                                					 that is populated: 64 transcoding sessions with one daughter card, 128
                                                					 transcoding sessions with two daughter cards, 192 transcoding sessions with
                                                					 three daughter cards, and 256 transcoding sessions with four daughter cards
                                                					 (maximum). This type provides transcoding between any combination of the
                                                					 following codecs: G.711 a-law and G.711 mu-law G.729 annex A and annex B G.723.1 GSM (FR) GSM (EFR) |

| Interactions  or Restriction | Description |
|---|---|
| Transcoder Deletion | You cannot delete a transcoder that is assigned to a media
                                                						resource group. To find out which media resource groups are using the
                                                						transcoder, click Dependency Records from the Related Links drop-down list box on
                                                						the Transcoder Configuration window and
                                                						click Go . The Dependency Records Summary
                                                						window displays information about media resource groups that are using the
                                                						transcoder. To find out more information about the media resource group, click
                                                						the media resource group, and the Dependency Records Details window displays.
                                                						If the dependency records are not enabled for the system, the dependency
                                                						records summary window displays a message. If you try to delete a transcoder
                                                						that is in use, Cisco Unified Communications Manager displays a message. Before
                                                						deleting a transcoder that is currently in use, you must remove the transcoder
                                                						from the media resource group(s) to which it is assigned. |
| Failover and Fallback | Transcoder failover and fallback works as follows: If the primary Unified Communications Manager node fails, the transcoder attempts to register with the next available node in the Unified Communications Manager Group that is specified for the device pool to which the transcoder belongs. The transcoder device reregisters with the primary Cisco Unified Communications Manager node as soon as it becomes available. A transcoder device unregisters with a Unified Communications Manager node that becomes unreachable. Calls that were using this transcoding profile for transcoding move to the preservation state
                                                      and the transcoder attempts to register with the next available node. Gateway uses RTP/ RTCP timeout to inform to registered
                                                      Unified Communications Manager of resource release. If a transcoder attempts to register with a new Unified Communications Manager node and the register acknowledgment is never received, the transcoder registers with the next node in the list. Transcoder devices will unregister and then disconnect after a hard or soft reset. After the reset completes, the devices
                                                reregister with the primary Cisco Unified Communications Manager node. |

| Feature | Interactions and Restrictions |
|---|---|
| Resource
                                                						Reservation Protocol (RSVP) | If RSVP
                                                						is enabled for the call, Cisco Unified
                                                   						  Communications Manager first tries to allocate an RSVPAgent that is
                                                						also labeled as TRP. Otherwise, another TRP device is inserted between the
                                                						RSVPAgent and the endpoint. |
| Transcoder for call | If you
                                                						need a transcoder for the call and need to allocate it on the same side as the
                                                						endpoint that needs TRP, Cisco Unified
                                                   						  Communications Manager first tries to allocate a transcoder that is
                                                						also labeled as TRP. Otherwise, another TRP device is inserted between the
                                                						transcoder and the endpoint. |
| MTP allocation for  endpoint | If you check both the Media Termination Point Required check box and the Use Trusted Relay Point check box for an endpoint, Cisco Unified Communications Manager should allocate an MTP that is also a TRP. If the administrator fails to allocate such an MTP or TRP, the call status appears. |
| TRP allocation | In most instances, TRP is allocated after users answer the call, so if a call fails due to failure to allocate the TRP, users
                                                may receive fast-busy tone after answering the call. (The SIP outbound leg with MTP required, or H.323 outbound faststart,
                                                represents an exception.) |
| TRP Insertion for endpoint | Cisco Unified Communications Manager must insert a TRP for the endpoint if you have checked the Use Trusted Relay Point check box for either the endpoint or the device pool that is associated with the device. The call may fail if Cisco Unified Communications Manager fails to allocate a TRP while the Fail Call If Trusted Relay Point Allocation Fails service parameter is set to True . |
| TRP and remote users | TRP is not recommended for providing secure solution for work from home remote users. Expressway's Mobile and Remote Access
                                                is the recommended solution. |

| Fail Call If TRP Allocation Fails  Service Parameter | Fail Call If MTP Allocation Fails Service Parameter | Unified CM Fails Call? |
|---|---|---|
| True | True | Yes |
| True | False | Yes |
| False | True | Yes, if MTP is required for H.323 endpoint. No, if MTP is required for SIP endpoint. |
| False | False | No |

| MTP Required = Yes | Use TRP = Yes | Resource Allocation Status | Call Behavior |
|---|---|---|---|
| Y | Y | TRP allocated | Audio call only because no pass-through support exists. |
| Y | Y or N | MTP only | Audio call only. No TRP support. |
| Y | Y or N | None allocated | If MTP required is checked for H.323 endpoint, supplementary services will be disabled. |
| N | Y | TRP allocated | Audio or video call depends on endpoint capabilities, and call admission control (CAC). Supplementary services still work. |
| N | Y | None allocated | Audio or video call. Supplementary services still work, but no TRP support exists. |

| Caution | We recommend that you do not activate the annunciator on Unified Communications Manager nodes that have a high call-processing load. |
|---|---|

| Condition | Announcement |
|---|---|
| An equal
                                                					 or higher precedence call is in progress. | Precedence
                                                					 access limitation has prevented the completion of your call. Please hang up and
                                                					 try again. This is a recording. |
| A
                                                					 precedence access limitation exists. | Precedence
                                                					 access limitation has prevented the completion of your call. Please hang up and
                                                					 try again. This is a recording. |
| Someone
                                                					 attempted an unauthorized precedence level. | The
                                                					 precedence used is not authorized for your line. Please use an authorized
                                                					 precedence or ask your operator for assistance. This is a recording. |
| The call
                                                					 appears busy, or the administrator did not configure the directory number for
                                                					 call waiting or preemption. | The number
                                                					 you have dialed is busy and not equipped for call waiting or preemption. Please
                                                					 hang up and try again. This is a recording. |
| The system
                                                					 cannot complete the call. | Your call
                                                					 cannot be completed as dialed. Please consult your directory and call again or
                                                					 ask your operator for assistance. This is a recording. |
| A service
                                                					 interruption occurred. | A service
                                                					 disruption has prevented the completion of your call. In case of emergency call
                                                					 your operator. This is a recording. |

| Type | Description |
|---|---|
| Busy
                                                					 tone | A busy
                                                					 tone is heard when the dialed number is busy. |
| Barge tone | A
                                                					 conference barge-in tone is heard before the participant joins an ad hoc
                                                					 conference. |
| Ring back
                                                					 tone | An alert
                                                					 tone is heard for the following scenarios: When
                                                         						  you transfer a call over the PSTN through an IOS gateway. When
                                                         						  you transfer a call over an H.323 intercluster trunk. When
                                                         						  you transfer a call to the SIP client from an SCCP phone. |

| Caution | Do not activate
                                             			 the IVR device on Cisco
                                                				Unified Communications Manager nodes that have a high call-processing
                                             			 load. |
|---|---|

| Announcement | Condition |
|---|---|
| ConferenceNowAccessCodeFailed Announcement | Plays when
                                                   					 an attendee enters the wrong access code to join Conference Now after exceeding
                                                   					 the maximum number of attempts. |
| ConferenceNowAccessCodeInvalid Announcement | Plays when
                                                   					 an attendee enters the wrong access code. |
| ConferenceNowCFBFailed Announcement | Plays when
                                                   					 the conference bridge capacity limit is exceeded while initiating Conference
                                                   					 Now. |
| ConferenceNowEnterAccessCode Announcement | Plays when
                                                   					 an attendee joins Conference Now and the host sets an attendee access code. |
| ConferenceNowEnterPIN Announcement | Plays when
                                                   					 a host or attendee tries to join a meeting. |
| ConferenceNowFailedPIN Announcement | Plays
                                                   					 after the host exceeds the maximum number of attempts to enter a correct PIN. |
| ConferenceNowGreeting Announcement | Plays a
                                                   					 greeting prompt for Conference Now. |
| ConferenceNowInvalidPIN Announcement | Plays when
                                                   					 the host enters a wrong PIN. |
| ConferenceNowNumberFailed Announcement | Plays
                                                   					 when a host or attendee enters the wrong meeting number after exceeding the
                                                   					 maximum number of attempts. |
| ConferenceNowNumberInvalid Announcement | Plays when
                                                   					 a host or attendee enters a wrong meeting number. |

| Feature | Restriction |
|---|---|
| Load Balancing | The Interactive Voice Response (IVR) uses Real-Time Protocol (RTP) streams through a common media device driver. This device
                                                driver is also used by other software media devices provided by the Cisco IP Voice Media Streaming Application services such
                                                as Music On Hold (MOH), Software Media Termination Point (MTP), Software Conference Bridge (CFB), and Annunciator. Configuring a larger call volume affects the system performance. This also impacts call processing if the Call Manager service
                                                is active on the same server node. |
| DTMF Digits | The IVR
                                                						supports only Out-Of-Band (OOB) DTMF digit collection method. If there is a
                                                						DTMF capability mismatch between the calling device and the IVR, an MTP will be
                                                						allocated. |
| Codecs | The IVR
                                                						only supports codec G.711 (a-law and mu-law), G.729, and Wide Band 256k. If
                                                						there is a codec mismatch between the calling device and the IVR, a transcoder
                                                						will be allocated. |

| Note | You can hear custom announcements such as warning or reorder tones if you are connected through a trunk or gateway. However,
                                          you cannot hear custom announcements on calls between two IP phones or IP phones and Jabber clients. |
|---|---|

| Announcement Identifier | Description |
|---|---|
| Gone_00126 | System:
                                                					 Gone |
| MLPP-BNEA_00123 | System:
                                                					 MLPP Busy not equipped |
| MLPP-BPA_00122 | System:
                                                					 MLPP Higher precedence |
| MLPP-ICA_00120 | System:
                                                					 MLPP Service disruption |
| MLPP-PALA_00119 | System:
                                                					 MLPP Precedence access limit |
| MLPP-UPA_00124 | System:
                                                					 MLPP Unauthorized precedence |
| Mobility_VMA | Please
                                                					 press 1 to be connected |
| MonitoringWarning_00055 | System:
                                                					 Monitoring or Recording |
| RecordingWarning_00038 | System:
                                                					 Recording |
| TemporaryUnavailable_00125 | System:
                                                					 Temporary unavailable |
| VCA_00121 | System:
                                                					 Vacant number / invalid number dialed |
| Wait_In_Queue_Sample | Builtin:
                                                					 Sample queued caller periodic announcement |
| Welcome_Greeting_Sample | Builtin:
                                                					 Sample caller greeting |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Software Media Resources | Turning on the IPVMS service activates software media resources on the server. |
| Step 2 | Configure Media Termination Points | Configure Media Termination Points (MTPs) for your system. |
| Step 3 | Configure Transcoders | Add Transcoder resources to the system. |
| Step 4 | Configure the Interactive Voice Response (IVR) | Configure default settings for the system IVR. |
| Step 5 | Configure the Annunicator | Configure system settings for the Annunciator. |
| Step 6 | Configure Media Resource Groups | Add your media resources into a Media Resource Group. Set up multiple groups with different combinations of resources. |
| Step 7 | Configure Media Resource Group Lists | Create a list of Media Resource Groups that you can assign to an endpoint, or class of endpoints. |
| Step 8 | Assign Media Resources to Device or Device Pool | Make media resources available to endpoints by assigning them to a device or device pool. |
| Step 9 | Configure Announcement | Optional . Configure settings for specific announcements. Announcements are used in normal processing, or for features like Music On
                                          Hold or IVR. |
| Step 10 | Upload a Customized Announcement | Optional . Upload a prerecorded announcement. Assign the file to a new or existing announcement. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server , select a Unified Communications Manager node. |
| Step 3 | Check the Cisco IP Voice Media Streaming Service and click Save . |

| Step 1 | From Cisco Unified CM
                                          			 Administration, choose Media Resources > Media
                                                				  Termination Point . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing MTP. Click Add New to create a new MTP. |
| Step 3 | Assign a Media Termination Point Name . |
| Step 4 | Assign a Device Pool . |
| Step 5 | Check the Trusted Relay Point check box if you want to designate this MTP as a Trusted Relay Point (TRP). |
| Step 6 | Click Save . |

| Step 1 | Log into Cisco
                                          			 Unified CM Administration and choose Media
                                                				  Resources > Transcoder . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing transcoder. Click Add New . |
| Step 3 | Select the Transcoder Type . |
| Step 4 | Enter the MAC Address of the transcoder. |
| Step 5 | Assign a Device Pool from the drop-down menu. |
| Step 6 | Check the Trusted Relay Point check box if you want to make this transcoder available as a trusted relay point. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Interactive Voice Response . |
|---|---|
| Step 2 | Click Find and select the IVR. |
| Step 3 | Enter a Name and Description . |
| Step 4 | If you want IVR calls to use a trusted relay point, set the Use Trusted Relay Point drop-down to On . |
| Step 5 | Complete the remaining fields in the Interactive Voice Response Configuration window. For help with the fields and their settings, see the online help. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Annunciator . |
|---|---|
| Step 2 | Click Find and select the annunciator. |
| Step 3 | Enter a Name and Description . |
| Step 4 | Select a Device Pool . |
| Step 5 | If you want the annunciator to use a trusted relay point, set the Use Trusted Relay Point drop-down to On . |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Media Resource Group . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing media resource group. Click Add New to create a new media resource group. |
| Step 3 | Configure the
                                          			 fields in the Media
                                             				Resource Group Configuration window. See the online help about the
                                          			 fields and their configuration options. |
| Step 4 | Enter a Name and Description for the group. |
| Step 5 | From Available Media Resources , select the resources you want to add to this group, and use the arrows to move the resources to Selected Media Resources . |
| Step 6 | (Optional) To use multicast for Music On Hold audio, check the Use Multi-cast for MOH Audio check box. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Media Resource Group List . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing list. Click Add New and create a new list. |
| Step 3 | Enter a Name for the media resource group list. |
| Step 4 | From Available Media Resource Groups , select the groups you want to add, and use the arrows to move them to Selected Media Resource Groups . |
| Step 5 | Click Save . Note For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. | Note | For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. |
| Note | For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. |

| Note | For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. |
|---|---|

| Step 1 | From the Cisco Unified CM Administration, choose Devices > Phone . To add media resources to a device pool, choose System > Device Pools . To add media resource directly to an endpoint, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the device pool or device to which you want to assign these media resources. |
| Step 3 | From the Media Resource Group List drop-down, select a list. |
| Step 4 | Click Save . |
| Step 5 | Click Apply Config to Selected . The Apply Configuration window appears showing the device name and the applicable configuration changes. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Announcement . |
|---|---|
| Step 2 | Do one of the following: Click Find and select an existing announcement to edit. Click Add New to add a new announcment. |
| Step 3 | Configure the fields in the Announcement Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Note | Announcements are specific to the locale (language). If your installation is using more than one language locale, you have
                                             to record each custom announcement each language as a separate .wav file and upload with the correct locale assignment. This
                                             task also requires that the correct locale package is installed on each server before uploading custom announcement .wav files
                                             for languages other than United States English. Similar to MOH audio source files, the recommended format for announcements includes the following specifications: 16-bit PCM .wav file Stereo or mono Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz You cannot update announcements that are not hyperlinked in the Find and List Announcements window in Unified Communications Manager. You can add customized announcements for Cisco-provided announcements that are
                                             underlined with a hyperlink in this window. For example, MLPP-ICA_00120 and MonitoringWarning_00055. |
|---|---|

| Step 1 | From Cisco Unified CM
                                             				Administration , choose Media
                                                				  Resources > Announcement . |
|---|---|
| Step 2 | From the Find
                                             				and List Announcements window, enter search criteria, click Find , and click the hyperlink for the announcement
                                          			 from the resulting list. |
| Step 3 | From the Announcement Configuration window, click Upload File . |
| Step 4 | From the Upload
                                             				File pop-up window, choose the locale, enter the filename and browse
                                          			 to select the .wav file, and click Upload
                                             				File . The upload process begins and the status is updated after the processing is complete. Select Close to close the Upload File window. |
| Step 5 | (Optional) If you want Unified Communications Manager to play the customized announcement instead of playing the Cisco-provided announcement, check the Enable check box appears in the Announcement by Locale pane in the Announcements Configuration window. If the Enable check box is unchecked, Unified Communications Manager plays the Cisco-provided announcement. |
| Step 6 | Click Save . |