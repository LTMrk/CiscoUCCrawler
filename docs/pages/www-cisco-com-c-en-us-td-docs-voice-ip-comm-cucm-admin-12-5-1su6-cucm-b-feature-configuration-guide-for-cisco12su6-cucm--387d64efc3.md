---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--387d64efc3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0111101.html
retrieved_at: 2026-08-16T16:39:26.747463+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Configure Flexible DSCP Marking and Video Promotion

## Chapter: Configure Flexible DSCP Marking and Video Promotion

# Configure Flexible DSCP Marking and Video Promotion

## Flexible DSCP
                        	 Marking and Video Promotion Overview

Devices and
                              		  applications use Differentiated Services Code Point (DSCP) markings to indicate
                              		  the Quality of Service (QoS) treatment of IP communications. For example,
                              		  desktop video endpoints may use multimedia conferencing AF41 marking for video
                              		  media streams, while high-definition video room systems may use real-time
                              		  interactive CS4 marking. When an application sends and receives IP
                              		  communications to and from the same type of application, the DSCP markings are
                              		  symmetric, and the QoS treatments of the IP communications that each
                              		  application sends and receives are the same. However, when an application sends
                              		  and receives media to and from a different type of application, the DSCP
                              		  markings may be asymmetric, and the QoS treatments of the IP communications
                              		  that each application sends and receives may be inconsistent. For example, the
                              		  QoS treatment of the video media stream that a video room system receives from
                              		  a desktop video endpoint may be inadequate to support the expected quality of
                              		  the video room system.

Devices and
                              		  applications are subjected to Call Admission Control (CAC) to ensure that
                              		  adequate bandwidth is available for the duration of established sessions. The
                              		  bandwidth that is utilized by established sessions is updated as the sessions
                              		  begin and end. Attempts to establish new sessions that would exceed the
                              		  available bandwidth are blocked. The amount of bandwidth available may be
                              		  tracked independently for devices and applications of different types. For
                              		  example, independent tracking of bandwidth may be available for desktop video
                              		  endpoints and high-definition video room systems to send and receive video
                              		  media streams.

When devices and
                              		  applications of the same type send and receive communications, the same type of
                              		  bandwidth deductions are made in each direction. However, when devices and
                              		  applications of different types send and receive communications, different
                              		  types of bandwidth deductions must be made in each direction. Moreover, the
                              		  bandwidth deductions are usually symmetric in amount, by design, to reflect the
                              		  usual behavior of an IP network. As a result, when devices and applications of
                              		  different types send and receive communications, the total bandwidth deductions
                              		  may be up to double the amount of network bandwidth that is actually utilized.
                              		  This inconsistency in bandwidth accounting may cause attempts to establish new
                              		  sessions to be blocked unnecessarily.

The Flexible DSCP
                              		  Marking and Video Promotion feature allows you to configure a Video Promotion
                              		  policy that reconciles the inconsistency in bandwidth accounting in favor of
                              		  the application that receives more favorable CAC and QoS treatment. For
                              		  example, if a session between a desktop video endpoint and a high-definition
                              		  video room system is reconciled in favor of the video room system, then the
                              		  reconciliation is deemed a promotion for the desktop video endpoint.

When
                              		  reconciliation is in effect between devices and applications of different
                              		  types, bandwidth is deducted only for the type of application that is favored
                              		  by reconciliation. If sufficient bandwidth is available for a session of this
                              		  type to be admitted, the device or application of the type that is not favored
                              		  by reconciliation is instructed to change the DSCP markings that it uses to
                              		  those that are used by the device or application of the type that is favored by
                              		  reconciliation. For example, if a desktop video endpoint is promoted in a
                              		  session with a high-definition video room system, bandwidth accounting takes
                              		  place as if the desktop video endpoint were an application of the same type as
                              		  the video room system. The desktop video endpoint is instructed to change its
                              		  DSCP markings to those that are used by the video room system. The QoS
                              		  treatment is consistent in both directions, bandwidth is deducted for a session
                              		  between devices and applications of the same type as the video room system, and
                              		  bandwidth is not deducted for a session between devices and applications of the
                              		  same type as the desktop video endpoint.

When you activate
                              		  the Flexible DSCP Marking and Video Promotion feature, Unified Communications
                              		  Manager dynamically signals desktop video devices a Traffic Class Label that is
                              		  indicative of the DSCP marking for each negotiated media stream.

## Custom QoS Settings for Users

You can customize Quality of Service (QoS) settings within a SIP profile and apply those settings to your users. The SIP Profile Configuration window has been enhanced with the following types of QoS settings:

Custom DSCP values for audio and video streams

Custom UDP port ranges for audio and video streams

### Custom DSCP Values for Audio and Video

You can configure DSCP values for audio and video calls within a SIP profile and apply them to the SIP phones that use that
                              profile. The SIP Profile Configuration window includes custom DSCP settings for the following types of calls:

Audio calls

Video calls

Audio portion of a video call

TelePresence calls

Audio portion of a TelePresence call

If your company has a set of employees, such as a sales force, or a CEO, who require higher QoS priority settings than the
                              majority of your employees, you can use the SIP profile configurations to configure custom DSCP values for those users. The
                              settings within the SIP profile override the corresponding clusterwide service parameter settings.

### Custom UDP Port Ranges for Audio and Video

You can configure separate UDP port ranges for the audio stream and video stream of a SIP call. Because video typically requires
                              considerably more bandwidth than audio, creating dedicated port ranges for each media type simplifies network bandwidth management.
                              It also protects against audio stream degradation by guaranteeing that the audio stream will have a dedicated channel that
                              is separate from the higher-bandwidth video stream.

You can apply this configuration by setting the Media Port Ranges field in the SIP profile to Separate Port Ranges for Audio and Video . You can then apply the configuration to a phone by associating the SIP profile to a phone.

## Traffic Class
                        	 Label

The Flexible DSCP and Video Promotion feature uses the Traffic Class
                              		  Label (TCL) to instruct the SIP endpoint dynamically to mark its DSCP on a per
                              		  call basis, based on the Video Promotion policy that you configure. Because TCL
                              		  is a SIP Session Description Protocol (SDP) attribute that is defined per media
                              		  line, the TCL and its associated DSCP markings can be different for the audio
                              		  media line and the video media line of a video call. You can choose different
                              		  DSCP markings for the audio stream and the video stream of the video call.

## DSCP Settings Configuration Task Flow

Perform the following tasks to configure DSCP values and a video promotion policy for your network.

Step 1

Configure Flexible DSCP Marking and Video Promotion Policy

Configure a video promotion policy to handle the different types of video.

Step 2

Configure Custom QoS Policy for Users

If your company  has users  that require higher priority than other users in your company, configure a SIP Profile that includes
                                          custom DSCP values for audio and video streams. For example, if your company has a telephone sales force or CEO whom require
                                          higher priority, you can apply the customized SIP profile to those users' phones.

### Configure Flexible
                           	 DSCP Marking and Video Promotion Policy

Follow these steps to configure a video promotion policy to handle the
                                 		  different types of video.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server where you
                                          			 want to configure the parameters.

Step 3

From the Service drop-down list, choose the Cisco
                                             				CallManager (Active) service.

If the service
                                             				does not display as active, ensure that the service is activated in Cisco
                                             				Unified Serviceability.

Step 4

To configure a
                                          			 Video Promotion policy that promotes desktop video endpoints to immersive video
                                          			 endpoints, set the Use
                                             				Video BandwidthPool for Immersive Video Calls parameter to False and set the Video
                                             				Call QoS Marking Policy parameter to Promote to Immersive .

Step 5

To configure other parameters, scroll to the appropriate area of the Service Parameter Configuration window and update the parameter values. See Flexible DSCP Marking and Video Promotion Service Parameters for information about the service parameters and their configuration options.

Step 6

Click Save .

#### Flexible DSCP
                              	 Marking and Video Promotion Service Parameters

For more
                                                			 information about the service parameters, click the parameter name or click the
                                                			 question mark (?) icon that displays in the Service
                                                   				Parameter Configuration window.

Parameter

Description

Clusterwide Parameters (System - QoS)

This
                                                					 section of service parameters includes clusterwide DSCP values for a wide range
                                                					 of audio and video call types, including DSCP for audio calls, video calls, the
                                                					 audio portion of a video call, TelePresence calls, and the audio portion of a
                                                					 TelePresence call.

It is
                                                					 highly recommended that you keep these parameters set to the default value
                                                					 unless a Cisco support engineer instructs otherwise.

Clusterwide Parameters (Call Admission Control)

Video Call
                                                					 QoS Marking Policy

This
                                                					 parameter allows you to configure a Promote to Immersive policy that reconciles
                                                					 bandwidth allocation inconsistencies between a desktop video endpoint and a
                                                					 Cisco TelePresence immersive video endpoint in favor of the immersive endpoint.
                                                					 When promotion is performed, the audio and video bandwidth are reserved from
                                                					 the immersive bandwidth pool allocation. The policy of Promote to Immersive
                                                					 takes effect only for calls between an immersive video device and a desktop
                                                					 video device that supports flexible DSCP marking.

Clusterwide Parameters (System - Location and Region)

Default
                                                					 Intraregion Max Immersive Video Call Bit Rate (Includes Audio)

This
                                                					 parameter specifies the default maximum total bit rate for each immersive video
                                                					 call within a particular region, when the Use System Default option is selected as the Max Immersive Video Call Bit Rate in the Region Configuration window for the relationship of
                                                					 the region with itself.

Default
                                                					 Interregion Max Immersive Video Call Bit Rate (Includes Audio)

This
                                                					 parameter specifies the default maximum total bit rate for each immersive video
                                                					 call between a particular region and another region, when the Use System Default option is selected as the Max Immersive Video Call Bit Rate in the Region Configuration window for the relationship of
                                                					 the region with the other region.

Use Video
                                                					 BandwidthPool for Immersive Video Calls

This
                                                					 parameter specifies whether Unified Communications Manager reserves bandwidth
                                                					 from the desktop video bandwidth pool for immersive video calls.

### Configure Custom QoS Policy for Users

Perform the following tasks to set up a custom Quality of Service (QoS) policy for users. You may want to apply a custom policy
                                 if a set of users within your company has different QoS requirements from the rest of the company such as telephone sales
                                 force or a CEO.

Step 1

Configure Custom QoS Settings in SIP Profile

Configure a SIP Profile with customized DSCP values and a UDP port range for audio and video streams.

Step 2

Apply Custom QoS Policy to a Phone

Apply the SIP Profile to a phone. The DSCP settings in the SIP Profile override the DSCP clusterwide service parameter settings..

#### Configure Custom QoS Settings in SIP Profile

Configure custom DSCP values and UDP port ranges for the phones that use this SIP Profile. You can use these settings to
                                    configure a customized QoS policy that you can apply to specific phones and users within your network. You may want to do
                                    this if you want to apply specific QoS settings to specific users within your enterprise, such as a sales force, or a CEO.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Perform either of the following steps:

- Click Find and select an existing SIP Profile.

- Click Add New to create a new SIP Profile.

Step 3

From the Media Port Ranges field, select whether you want to assign a single UDP port range that handles both audio and video media, or separate port
                                             ranges for audio and video streams.

- If you want to configure a single port range for audio and video media, enter the range of ports   in the Start Media Port and Stop Media Port fields. The possible port values are between 2048 and 65535.

- If you want separate port ranges for audio and video streams, enter the range of audio ports using the Start Audio Port and Stop Audio Port fields. Enter the range of video ports using the Start Video Port and Stop Video Port fields. The possible port values for each are between 2048 and 65535.The two port ranges must not overlap.

Step 4

In the following fields, configure customized DSCP values for audio and video streams.

- DSCP for Audio Calls

- DSCP for Video Calls

- DSCP for Audio Portion of Video Calls

- DSCP for TelePresence Calls

- DSCP for Audio Portion of TelePresence Calls

Step 5

Complete the remaining fields in the SIP Profile Configuration window. For help with the fields and their settings, refer to the online help.

Step 6

Click Save .

#### Apply Custom QoS Policy to a Phone

Use this procedure to apply a SIP Profile that contains customized QoS settings, including  DSCP values and a UDP port range
                                    for audio and video media. When you apply this SIP profile to a phone, the phone uses the custom settings from the SIP Profile.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Perform any one of the following steps:

- Click Find and select an existing phone.

- Click Add New to create a new phone.

Step 3

From the SIP Profile drop-down list, select the SIP profile that you set up with the custom DSCP values and UDP port range values.

Step 4

Complete the remaining fields in the Phone Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

## Flexible DSCP Marking and Video Promotion Interactions

Device

Interaction

SIP
                                          					 Intercluster Trunks

The
                                          					 Flexible DSCP Marking and Video Promotion feature is supported over SIP
                                          					 intercluster trunks.

Skinny
                                          					 Client Control Protocol (SCCP) Devices

The
                                          					 Flexible DSCP Marking and Video Promotion feature is supported for SCCP
                                          					 devices.

Pass-Through MTPs

If
                                          					 pass-through MTPs are inserted in a call, Unified Communications Manager
                                          					 signals the MTP to mark the packets with the DSCP marking that is expected from
                                          					 the endpoint device that originally emitted the packet for the video stream. If
                                          					 the two endpoints on a call use different DSCP markings (for example, a Cisco
                                          					 TelePresence immersive video endpoint and a desktop video endpoint without
                                          					 Video Promotion), the MTPs preserve the DSCP marking in each stream direction.

## Flexible DSCP
                        	 Marking and Video Promotion Restrictions

Restriction

Description

Trunks and
                                          					 gateways

The
                                          					 Flexible DSCP Marking and Video Promotion feature is not supported over H.323
                                          					 trunks and Media Gateway Control Protocol (MGCP) gateways.

Multilevel
                                          					 Precedence and Preemption

Cisco
                                          					 recommends that you do not use the Flexible DSCP Marking and Video Promotion
                                          					 feature with Multilevel Precedence and Preemption (MLPP) service calls. When
                                          					 you need MLPP service functionality, Cisco recommends that you set the Video
                                          					 Call QoS Marking Policy and Use Video BandwidthPool for Immersive Video Calls
                                          					 service parameters to their default values. With default values for the Video
                                          					 Call QoS Marking Policy and Use Video BandwidthPool for Immersive Video Calls
                                          					 service parameters, Unified Communications Manager and endpoints use MLPP DSCP
                                          					 markings for the media packets.

SIP video
                                          					 endpoints

The
                                          					 Flexible DSCP Marking and Video Promotion feature is dependent on desktop SIP
                                          					 video endpoint support. Currently, only Cisco DX650 series SIP phones provide
                                          					 the required endpoint support.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Flexible DSCP Marking and Video Promotion Policy | Configure a video promotion policy to handle the different types of video. |
| Step 2 | Configure Custom QoS Policy for Users | If your company  has users  that require higher priority than other users in your company, configure a SIP Profile that includes
                                          custom DSCP values for audio and video streams. For example, if your company has a telephone sales force or CEO whom require
                                          higher priority, you can apply the customized SIP profile to those users' phones. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server where you
                                          			 want to configure the parameters. |
| Step 3 | From the Service drop-down list, choose the Cisco
                                             				CallManager (Active) service. If the service
                                             				does not display as active, ensure that the service is activated in Cisco
                                             				Unified Serviceability. |
| Step 4 | To configure a
                                          			 Video Promotion policy that promotes desktop video endpoints to immersive video
                                          			 endpoints, set the Use
                                             				Video BandwidthPool for Immersive Video Calls parameter to False and set the Video
                                             				Call QoS Marking Policy parameter to Promote to Immersive . |
| Step 5 | To configure other parameters, scroll to the appropriate area of the Service Parameter Configuration window and update the parameter values. See Flexible DSCP Marking and Video Promotion Service Parameters for information about the service parameters and their configuration options. |
| Step 6 | Click Save . |

| Note | For more
                                                			 information about the service parameters, click the parameter name or click the
                                                			 question mark (?) icon that displays in the Service
                                                   				Parameter Configuration window. |
|---|---|

| Parameter | Description |
|---|---|
| Clusterwide Parameters (System - QoS) | This
                                                					 section of service parameters includes clusterwide DSCP values for a wide range
                                                					 of audio and video call types, including DSCP for audio calls, video calls, the
                                                					 audio portion of a video call, TelePresence calls, and the audio portion of a
                                                					 TelePresence call. It is
                                                					 highly recommended that you keep these parameters set to the default value
                                                					 unless a Cisco support engineer instructs otherwise. |
| Clusterwide Parameters (Call Admission Control) |  |
| Video Call
                                                					 QoS Marking Policy | This
                                                					 parameter allows you to configure a Promote to Immersive policy that reconciles
                                                					 bandwidth allocation inconsistencies between a desktop video endpoint and a
                                                					 Cisco TelePresence immersive video endpoint in favor of the immersive endpoint.
                                                					 When promotion is performed, the audio and video bandwidth are reserved from
                                                					 the immersive bandwidth pool allocation. The policy of Promote to Immersive
                                                					 takes effect only for calls between an immersive video device and a desktop
                                                					 video device that supports flexible DSCP marking. |
| Clusterwide Parameters (System - Location and Region) |
| Default
                                                					 Intraregion Max Immersive Video Call Bit Rate (Includes Audio) | This
                                                					 parameter specifies the default maximum total bit rate for each immersive video
                                                					 call within a particular region, when the Use System Default option is selected as the Max Immersive Video Call Bit Rate in the Region Configuration window for the relationship of
                                                					 the region with itself. |
| Default
                                                					 Interregion Max Immersive Video Call Bit Rate (Includes Audio) | This
                                                					 parameter specifies the default maximum total bit rate for each immersive video
                                                					 call between a particular region and another region, when the Use System Default option is selected as the Max Immersive Video Call Bit Rate in the Region Configuration window for the relationship of
                                                					 the region with the other region. |
| Use Video
                                                					 BandwidthPool for Immersive Video Calls | This
                                                					 parameter specifies whether Unified Communications Manager reserves bandwidth
                                                					 from the desktop video bandwidth pool for immersive video calls. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Custom QoS Settings in SIP Profile | Configure a SIP Profile with customized DSCP values and a UDP port range for audio and video streams. |
| Step 2 | Apply Custom QoS Policy to a Phone | Apply the SIP Profile to a phone. The DSCP settings in the SIP Profile override the DSCP clusterwide service parameter settings.. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Perform either of the following steps: Click Find and select an existing SIP Profile. Click Add New to create a new SIP Profile. |
| Step 3 | From the Media Port Ranges field, select whether you want to assign a single UDP port range that handles both audio and video media, or separate port
                                             ranges for audio and video streams. If you want to configure a single port range for audio and video media, enter the range of ports   in the Start Media Port and Stop Media Port fields. The possible port values are between 2048 and 65535. If you want separate port ranges for audio and video streams, enter the range of audio ports using the Start Audio Port and Stop Audio Port fields. Enter the range of video ports using the Start Video Port and Stop Video Port fields. The possible port values for each are between 2048 and 65535.The two port ranges must not overlap. |
| Step 4 | In the following fields, configure customized DSCP values for audio and video streams. DSCP for Audio Calls DSCP for Video Calls DSCP for Audio Portion of Video Calls DSCP for TelePresence Calls DSCP for Audio Portion of TelePresence Calls Note By default, each of the above fields is configured to use the value from a corresponding service parameter. If you assign
                                                         new values, the new value overrides the service parameter setting. | Note | By default, each of the above fields is configured to use the value from a corresponding service parameter. If you assign
                                                         new values, the new value overrides the service parameter setting. |
| Note | By default, each of the above fields is configured to use the value from a corresponding service parameter. If you assign
                                                         new values, the new value overrides the service parameter setting. |
| Step 5 | Complete the remaining fields in the SIP Profile Configuration window. For help with the fields and their settings, refer to the online help. |
| Step 6 | Click Save . |

| Note | By default, each of the above fields is configured to use the value from a corresponding service parameter. If you assign
                                                         new values, the new value overrides the service parameter setting. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Perform any one of the following steps: Click Find and select an existing phone. Click Add New to create a new phone. |
| Step 3 | From the SIP Profile drop-down list, select the SIP profile that you set up with the custom DSCP values and UDP port range values. |
| Step 4 | Complete the remaining fields in the Phone Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . |

| Device | Interaction |
|---|---|
| SIP
                                          					 Intercluster Trunks | The
                                          					 Flexible DSCP Marking and Video Promotion feature is supported over SIP
                                          					 intercluster trunks. |
| Skinny
                                          					 Client Control Protocol (SCCP) Devices | The
                                          					 Flexible DSCP Marking and Video Promotion feature is supported for SCCP
                                          					 devices. |
| Pass-Through MTPs | If
                                          					 pass-through MTPs are inserted in a call, Unified Communications Manager
                                          					 signals the MTP to mark the packets with the DSCP marking that is expected from
                                          					 the endpoint device that originally emitted the packet for the video stream. If
                                          					 the two endpoints on a call use different DSCP markings (for example, a Cisco
                                          					 TelePresence immersive video endpoint and a desktop video endpoint without
                                          					 Video Promotion), the MTPs preserve the DSCP marking in each stream direction. |

| Restriction | Description |
|---|---|
| Trunks and
                                          					 gateways | The
                                          					 Flexible DSCP Marking and Video Promotion feature is not supported over H.323
                                          					 trunks and Media Gateway Control Protocol (MGCP) gateways. |
| Multilevel
                                          					 Precedence and Preemption | Cisco
                                          					 recommends that you do not use the Flexible DSCP Marking and Video Promotion
                                          					 feature with Multilevel Precedence and Preemption (MLPP) service calls. When
                                          					 you need MLPP service functionality, Cisco recommends that you set the Video
                                          					 Call QoS Marking Policy and Use Video BandwidthPool for Immersive Video Calls
                                          					 service parameters to their default values. With default values for the Video
                                          					 Call QoS Marking Policy and Use Video BandwidthPool for Immersive Video Calls
                                          					 service parameters, Unified Communications Manager and endpoints use MLPP DSCP
                                          					 markings for the media packets. |
| SIP video
                                          					 endpoints | The
                                          					 Flexible DSCP Marking and Video Promotion feature is dependent on desktop SIP
                                          					 video endpoint support. Currently, only Cisco DX650 series SIP phones provide
                                          					 the required endpoint support. |