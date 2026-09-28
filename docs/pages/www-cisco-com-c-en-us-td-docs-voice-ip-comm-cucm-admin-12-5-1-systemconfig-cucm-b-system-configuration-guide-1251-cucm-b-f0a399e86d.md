---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-f0a399e86d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111101.html
retrieved_at: 2026-08-16T17:33:49.542098+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Interactive Voice Response

## Chapter: Configure Interactive Voice Response

# Configure Interactive Voice Response

## Interactive Voice
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

## Default IVR Announcements and Tones

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

## Interactive Voice
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

## Interactive Voice
                        	 Response Configuration Task Flow

Step 1

Activate the Interactive Voice Response

Activate the
                                          				Cisco IP Voice Media Streaming Application service on the node to activate the
                                          				IVR for that node. Activate only one Cisco IP Voice Media Streaming Application
                                          				service for each IVR device in the cluster.

Step 2

View List of Media Resource Groups That Have IVR

Add the IVR to
                                          				media resource groups and lists to manage your media resources using Cisco Unified
                                             				  Communications Manager Administration .

Step 3

(Optional) Change the Default Number of Media Streams

You can change
                                          				the default number of media streams for an IVR.

### Activate the
                           	 Interactive Voice Response

Activate one or
                                 		  more Cisco IP Voice Media Streaming Application service for each node to have
                                 		  Interactive Voice Response (IVR) device registered in the cluster.

Caution

Do not activate
                                             			 the IVR on Cisco Unified Communications Manager nodes that have a
                                             			 high call-processing load.

Step 1

From the Cisco
                                          			 Unified Serviceability GUI, choose Tools > Activation . The Service
                                             				Activation window appears.

Step 2

Select the
                                          			 node in the Server field and click Go .

Step 3

Check the Cisco
                                             				IP Voice Media Streaming Application check box, and then click Save .

### View List of Media
                           	 Resource Groups That Have IVR

Step 1

From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Interactive Voice Response (IVR) .

Step 2

From the Find
                                             				and List Interactive Voice Response (IVR) where window, click Find .

Step 3

Choose the IVR
                                          			 on which you want to see the associated list of media resource groups.

Step 4

Choose Dependency Records from the Related Links drop-down list and click Go .

If the
                                             				dependency records are not enabled for the system, the Dependency Records Summary window displays a message.

#### IVR
                              	 Settings

Field

Description

Server

Displays the preconfigured server (servers are added at installation), by default.

Name

Designates the name that is used when the device registers with the Cisco Unified Communications Manager . Enter a name of up to 15 alphanumeric characters (you can use periods, dashes, and underscores).

Description

Enter a description of up to 128 alphanumeric characters (you can use periods, dashes, and underscores). Default uses the
                                                server name, which includes the prefix IVR_.

Device
                                                						Pool

Choose Default or choose a device pool from the drop-down list of configured device pools.

Location

Use locations to implement call admission control (CAC) in a centralized call-processing system. CAC allows you to regulate
                                                audio quality and video availability by limiting the bandwidth that is available for audio and video calls over links between
                                                locations. The location specifies the total bandwidth that is available for calls to and from this location.

From the drop-down list, choose the appropriate location for this IVR.

A location setting of Hub_None means that the locations feature does not keep track of the bandwidth that this IVR consumes.
                                                A location setting of Phantom specifies a location that enables successful CAC across intercluster trunks that use H.323 protocol
                                                or SIP.

To
                                                						configure a new location, use the System > Location menu option.

For
                                                						details on setting up a location-based CAC across intercluster trunks, see the System Configuration Guide for Cisco Unified Communications
                                                   						  Manager .

Use
                                                						Trusted Relay Point

From the drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with this media endpoint. Choose one of the following values:

Off—Choose this value to disable the use of a TRP with this device.

On—Choose this value to enable the use of a TRP with this device.

A
                                                						Trusted Relay Point (TRP) device designates an MTP or transcoder device that is
                                                						labeled as Trusted Relay Point.

Unified Communications Manager places the TRP closest to the associated endpoint device if more than one resource is needed for the endpoint (for example,
                                                a transcoder or RSVPAgent).

If both
                                                						TRP and MTP are required for the endpoint, TRP gets used as the required MTP.

If both TRP and RSVPAgent are needed for the endpoint, Unified Communications Manager searches for an RSVPAgent that can also be used as a TRP.

If both
                                                						TRP and transcoder are needed for the endpoint, Cisco Unified Communications Manager searches for a
                                                						transcoder that is also designated as a TRP.

### Change IVR
                           	 Parameters

Step 1

From Cisco Unified
                                             				Communications Manager Administration , choose System > Service
                                                				  Parameters . The Service
                                             				Parameters Configuration window appears.

Step 2

Select the
                                          			 server and then select the service called Cisco IP Voice Media Streaming App.
                                          			 The Service
                                             				Parameter Configuration window appears.

Step 3

Enter the
                                          			 number of simultaneous media streams in the Call
                                             				Count field of the Interactive Voice Response (IVR) Parameters section,
                                          			 and then click Save .

When you
                                             				update the IVR, the changes automatically occur when the IVR is idle and no
                                             				active announcements are playing.

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

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate the Interactive Voice Response | Activate the
                                          				Cisco IP Voice Media Streaming Application service on the node to activate the
                                          				IVR for that node. Activate only one Cisco IP Voice Media Streaming Application
                                          				service for each IVR device in the cluster. |
| Step 2 | View List of Media Resource Groups That Have IVR | Add the IVR to
                                          				media resource groups and lists to manage your media resources using Cisco Unified
                                             				  Communications Manager Administration . |
| Step 3 | (Optional) Change the Default Number of Media Streams | (Optional) You can change
                                          				the default number of media streams for an IVR. |

| Caution | Do not activate
                                             			 the IVR on Cisco Unified Communications Manager nodes that have a
                                             			 high call-processing load. |
|---|---|

| Step 1 | From the Cisco
                                          			 Unified Serviceability GUI, choose Tools > Activation . The Service
                                             				Activation window appears. |
|---|---|
| Step 2 | Select the
                                          			 node in the Server field and click Go . |
| Step 3 | Check the Cisco
                                             				IP Voice Media Streaming Application check box, and then click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Interactive Voice Response (IVR) . The Find
                                             				and List Interactive Voice Response (IVR) window is displayed. |
|---|---|
| Step 2 | From the Find
                                             				and List Interactive Voice Response (IVR) where window, click Find . A list
                                          			 of IVRs that are available on Cisco
                                             				Unified Communications Manager is displayed. |
| Step 3 | Choose the IVR
                                          			 on which you want to see the associated list of media resource groups. |
| Step 4 | Choose Dependency Records from the Related Links drop-down list and click Go . If the
                                             				dependency records are not enabled for the system, the Dependency Records Summary window displays a message. |

| Field | Description |
|---|---|
| Server | Displays the preconfigured server (servers are added at installation), by default. |
| Name | Designates the name that is used when the device registers with the Cisco Unified Communications Manager . Enter a name of up to 15 alphanumeric characters (you can use periods, dashes, and underscores). |
| Description | Enter a description of up to 128 alphanumeric characters (you can use periods, dashes, and underscores). Default uses the
                                                server name, which includes the prefix IVR_. |
| Device
                                                						Pool | Choose Default or choose a device pool from the drop-down list of configured device pools. |
| Location | Use locations to implement call admission control (CAC) in a centralized call-processing system. CAC allows you to regulate
                                                audio quality and video availability by limiting the bandwidth that is available for audio and video calls over links between
                                                locations. The location specifies the total bandwidth that is available for calls to and from this location. From the drop-down list, choose the appropriate location for this IVR. A location setting of Hub_None means that the locations feature does not keep track of the bandwidth that this IVR consumes.
                                                A location setting of Phantom specifies a location that enables successful CAC across intercluster trunks that use H.323 protocol
                                                or SIP. To
                                                						configure a new location, use the System > Location menu option. For
                                                						details on setting up a location-based CAC across intercluster trunks, see the System Configuration Guide for Cisco Unified Communications
                                                   						  Manager . |
| Use
                                                						Trusted Relay Point | From the drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with this media endpoint. Choose one of the following values: Off—Choose this value to disable the use of a TRP with this device. On—Choose this value to enable the use of a TRP with this device. A
                                                						Trusted Relay Point (TRP) device designates an MTP or transcoder device that is
                                                						labeled as Trusted Relay Point. Unified Communications Manager places the TRP closest to the associated endpoint device if more than one resource is needed for the endpoint (for example,
                                                a transcoder or RSVPAgent). If both
                                                						TRP and MTP are required for the endpoint, TRP gets used as the required MTP. If both TRP and RSVPAgent are needed for the endpoint, Unified Communications Manager searches for an RSVPAgent that can also be used as a TRP. If both
                                                						TRP and transcoder are needed for the endpoint, Cisco Unified Communications Manager searches for a
                                                						transcoder that is also designated as a TRP. |

| Step 1 | From Cisco Unified
                                             				Communications Manager Administration , choose System > Service
                                                				  Parameters . The Service
                                             				Parameters Configuration window appears. |
|---|---|
| Step 2 | Select the
                                          			 server and then select the service called Cisco IP Voice Media Streaming App.
                                          			 The Service
                                             				Parameter Configuration window appears. |
| Step 3 | Enter the
                                          			 number of simultaneous media streams in the Call
                                             				Count field of the Interactive Voice Response (IVR) Parameters section,
                                          			 and then click Save . When you
                                             				update the IVR, the changes automatically occur when the IVR is idle and no
                                             				active announcements are playing. |