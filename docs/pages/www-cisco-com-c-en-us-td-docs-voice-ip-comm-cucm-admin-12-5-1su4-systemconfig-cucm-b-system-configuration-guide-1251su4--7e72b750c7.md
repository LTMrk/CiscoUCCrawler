---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-systemconfig-cucm-b-system-configuration-guide-1251su4--7e72b750c7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/systemConfig/cucm_b_system-configuration-guide-1251su4/cucm_mp_cb1967ad_00_configure-rsvp-cac12-0.html
retrieved_at: 2026-08-16T17:39:03.891812+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: July 31, 2025

Chapter: Configure Resource Reservation Protocol

## Chapter: Configure Resource Reservation Protocol

# Configure Resource Reservation Protocol

## RSVP Call Admission Control Overview

Resource Reservation Protocol (RSVP) is a resource-reservation,
                              transport-level protocol for reserving resources in IP networks. You can use RSVP as an alternative to
                              enhanced-locations call admission control (CAC). RSVP reserves
                              resources for specific sessions. A session is a flow that has a
                              particular destination address, destination port, and a protocol identifier
                              (TCP or UDP).

## RSVP Call Admission Control Prerequisites

## RSVP Configuration Task Flow

Step 1

Configure Clusterwide Default RSVP Policy

Configure the RSVP policy for all nodes in the cluster.

Step 2

Configure Location-pair RSVP Policy

Optional. You can configure the RSVP
                                          		  policy for a specific location pair if you want the location pair to use a different policy than the rest of the cluster.

Step 3

Configure RSVP Retry

Configure the frequency and number of RSVP retries.

Step 4

Configure Midcall RSVP Error Handling

Configure how the system responds when RSVP fails during a call.

Step 5

Configure MLPP-to-RSVP Priority Mapping

Optional. If you use multilevel precedence and preemption (MLPP), map the caller MLPP precedence level to an RSVP priority.

Step 6

Configure RSVP agents.

Perform this IOS procedure on your gateway device. See the documentation for device for information about how to configure
                                          an RSVP agent.

Step 7

Configure the Application ID

When you configure the RSVP application ID, the system adds an identifier to both the voice and video traffic so that the
                                          Cisco RSVP Agent can set a separate bandwidth limit on either type of traffic, based on the identifier it receives.

Step 8

Configure DSCP Marking

Configure DSCP marking so that if the RSVP reservation fails, the system can instruct the RSVP agent or endpoint devices to
                                          change media Differentiated Services Control Point (DSCP) marking to best effort. Otherwise, an excess of EF-marked media
                                          packets can degrade quality of service (QoS) even for flows that have a reservation.

### Configure Clusterwide Default RSVP Policy

Configure the RSVP policy for all nodes in the cluster.

Step 1

In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters .

Step 2

In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the Default Interlocation RSVP Policy service parameter.

You can set this service parameter to the following values:

No Reservation-No RSVP reservations get made between any two
                                                   					 locations.

Optional (Video Desired)-A call can proceed as a best-effort,
                                                   					 audio-only call if failure to obtain reservations for both audio and video
                                                   					 streams occurs. RSVP agent continues to attempt RSVP reservation for audio and
                                                   					 informs Cisco Unified Communications Manager if reservation succeeds.

Mandatory- Cisco Unified Communications Manager does not ring the terminating device until RSVP reservation
                                                   					 succeeds for the audio stream and, if the call is a video call, for the video
                                                   					 stream as well.

Mandatory (Video Desired)-A video call can proceed as an
                                                   					 audio-only call if a reservation for the audio stream succeeds but a
                                                   					 reservation for the video stream does not succeed.

#### What to do next

Choose one of the following options:

If you want a location pair to use a different policy than the rest of the cluster, Configure Location-pair RSVP Policy .

If you are using the same RSVP policy for all nodes in the cluster, Configure RSVP Retry .

### Configure Location-pair RSVP Policy

You can configure the RSVP
                                 		  policy for a specific location pair if you want the location pair to use a different policy than the rest of the cluster.
                                 When you use this procedure, the RSVP policy that you configure for the
                                 		  location pair overrides the policy that you
                                 		  configured for the cluster.

Step 1

In Cisco Unified Communications Manager Administration , choose the System > Location .

Step 2

Find one location of the location pair and select this location.

Step 3

To modify the RSVP policy between the selected location and
                                          			 another location, select the other location in the location pair.

Step 4

In the RSVP Setting drop-down list, choose an RSVP policy for
                                          			 this location pair.

You can set this field to the following values:

Use System Default –The RSVP policy for the location pair
                                                   					 matches the cluster-wide RSVP policy.

No Reservation –No RSVP reservations get made between any two
                                                   					 locations.

Video Desired (Optional) –A call can proceed as a best-effort,
                                                   					 audio-only call if failure to obtain reservations for both audio and video
                                                   					 streams occurs. The RSVP agent continues to attempt RSVP reservation for audio
                                                   					 and informs Cisco Unified Communications Manager if reservation succeeds. 
                                                   				  The system does not ring the terminating device
                                                   					 until RSVP reservation succeeds for the audio stream and, if the call is a
                                                   					 video call, for the video stream as well.

Video Desired –A video call can proceed as an audio-only call
                                                   					 if a reservation for the audio stream succeeds but the reservation for the
                                                   					 video stream does not succeed.

#### What to do next

Configure RSVP Retry

### Configure RSVP Retry

Use this procedure to configure the frequency and number of RSVP retries.

#### Before you begin

Configure Clusterwide Default RSVP Policy

Optional. Configure Location-pair RSVP Policy

Step 1

In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters .

Step 2

In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the specified service parameters.

You can set these service parameters to the following
                                             				values:

RSVP Retry Timer-Specify the RSVP retry timer value in
                                                   					 seconds. If you set this parameter to 0, you disable RSVP retry on the system.

Mandatory RSVP Midcall Retry Counter-Specify the midcall RSVP
                                                   					 retry counter when the RSVP policy specifies Mandatory and midcall error
                                                   					 handling option is set to "call fails following retry counter exceeds." The default
                                                   					 value specifies 1 time. If you set the service parameter to -1, retry continues
                                                   					 indefinitely until either the reservation succeeds or the call gets torn down.

#### What to do next

Configure Midcall RSVP Error Handling

### Configure Midcall RSVP Error Handling

Use this procedure to configure midcall RSVP error handling.

#### Before you begin

Configure RSVP Retry

Step 1

In Cisco Unified Communications Manager Administration, choose System > Service Parameters .

Step 2

In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the specified service parameter.

You can set the Mandatory RSVP mid call error handle
                                             				option service parameter to the following values:

Call becomes best effort-If RSVP fails during a call, the call
                                                   					 becomes a best-effort call. If retry is enabled, RSVP retry attempts begin
                                                   					 simultaneously.

Call fails following retry counter exceeded-If RSVP fails
                                                   					 during a call, the call fails after N retries of RSVP, where the Mandatory RSVP
                                                   					 Mid-call Retry Counter service parameter specifies N.

#### What to do next

Configure RSVP agents on your gateway device. See the documentation for device for information about how to configure an RSVP
                                 agent. After you have configure RSVP agents on your gateway, return to Cisco Unified Communications Manager Administration
                                 and choose one of the following options:

Optional. Configure MLPP-to-RSVP Priority Mapping if you are using multilevel precedence and preemption in your network.

Configure the Application ID

### Configure MLPP-to-RSVP Priority Mapping

Optional. Use the following clusterwide (System - RSVP) service
                                 		  parameters to configure the mapping from a caller MLPP precedence level to RSVP
                                 		  priority:

MLPP EXECUTIVE OVERRIDE To RSVP Priority Mapping

- MLPP FLASH OVERRIDE To
                                    			 RSVP Priority Mapping

- MLPP FLASH To RSVP
                                    			 Priority Mapping

- MLPP IMMEDIATE To RSVP
                                    			 Priority Mapping

- MLPP PL PRIORITY To RSVP
                                    			 Priority Mapping

- MLPP PL ROUTINE To RSVP
                                    			 Priority Mapping

To locate and configure these service parameters, follow
                                 		  these steps:

Step 1

In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters .

Step 2

In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the specified service parameters.

These service parameters function as follows:

Cisco Unified Communications Manager maps the caller precedence level to
                                                   					 RSVP priority when initiating an RSVP reservation based on the following
                                                   					 configuration: the higher the service parameter value, the higher the priority.

The IOS router preempts the call based on RSVP priority.

The RSVP agent must notify Cisco Unified Communications Manager about the reason for an RSVP reservation
                                                   					 failure, including the cause for preemption.

Cisco Unified Communications Manager uses the existing MLPP mechanism to
                                                   					 notify the preempted calling and called parties about the preemption.

#### What to do next

Configure RSVP agents on your gateway device. See the documentation for device for information about how to configure an RSVP
                                 agent. After you have configure RSVP agents on your gateway, return to Cisco Unified Communications Manager Administration and Configure the Application ID .

### Configure the Application ID

When you configure the RSVP application ID, the system adds an identifier to both the voice and video traffic so that the
                                 Cisco RSVP Agent can set a separate bandwidth limit on either type of traffic, based on the identifier it receives.

Before you begin this procedure, configure RSVP agents on your gateway device. See the documentation for device for information
                                 about how to configure an RSVP agent.

#### Before you begin

To deploy the RSVP application ID in the network, you must use a minimum version of Cisco IOS Release 12.4(6)T or higher on
                                 the Cisco RSVP Agent router.

Step 1

In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters .

Step 2

In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the RSVP Audio Application ID service parameter.

(Default = AudioStream)

Step 4

In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the RSVP Video Application ID

(Default = VideoStream)

#### What to do next

Configure DSCP Marking

### Configure DSCP Marking

If the RSVP reservation fails, the system instructs the RSVP agent or endpoint devices (in case a failure to allocate an RSVP
                                 agent occurs) to change media Differentiated Services Control Point (DSCP) marking to best effort. Otherwise, an excess of
                                 EF-marked media packets can degrade quality of service (QoS) even for flows that have a reservation.

#### Before you begin

Configure the Application ID

Step 1

In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters .

Step 2

In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (System - QoS) section, configure
                                          			 the DSCP for Audio Calls When RSVP Fails service parameter.

Step 4

In the Clusterwide Parameters (System - QoS) section, configure
                                          			 the DSCP for Video Calls When RSVP Fails service parameter.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Clusterwide Default RSVP Policy | Configure the RSVP policy for all nodes in the cluster. |
| Step 2 | Configure Location-pair RSVP Policy | Optional. You can configure the RSVP
                                          		  policy for a specific location pair if you want the location pair to use a different policy than the rest of the cluster. |
| Step 3 | Configure RSVP Retry | Configure the frequency and number of RSVP retries. |
| Step 4 | Configure Midcall RSVP Error Handling | Configure how the system responds when RSVP fails during a call. |
| Step 5 | Configure MLPP-to-RSVP Priority Mapping | Optional. If you use multilevel precedence and preemption (MLPP), map the caller MLPP precedence level to an RSVP priority. |
| Step 6 | Configure RSVP agents. | Perform this IOS procedure on your gateway device. See the documentation for device for information about how to configure
                                          an RSVP agent. |
| Step 7 | Configure the Application ID | When you configure the RSVP application ID, the system adds an identifier to both the voice and video traffic so that the
                                          Cisco RSVP Agent can set a separate bandwidth limit on either type of traffic, based on the identifier it receives. |
| Step 8 | Configure DSCP Marking | Configure DSCP marking so that if the RSVP reservation fails, the system can instruct the RSVP agent or endpoint devices to
                                          change media Differentiated Services Control Point (DSCP) marking to best effort. Otherwise, an excess of EF-marked media
                                          packets can degrade quality of service (QoS) even for flows that have a reservation. |

| Step 1 | In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the Default Interlocation RSVP Policy service parameter. You can set this service parameter to the following values: No Reservation-No RSVP reservations get made between any two
                                                   					 locations. Optional (Video Desired)-A call can proceed as a best-effort,
                                                   					 audio-only call if failure to obtain reservations for both audio and video
                                                   					 streams occurs. RSVP agent continues to attempt RSVP reservation for audio and
                                                   					 informs Cisco Unified Communications Manager if reservation succeeds. Mandatory- Cisco Unified Communications Manager does not ring the terminating device until RSVP reservation
                                                   					 succeeds for the audio stream and, if the call is a video call, for the video
                                                   					 stream as well. Mandatory (Video Desired)-A video call can proceed as an
                                                   					 audio-only call if a reservation for the audio stream succeeds but a
                                                   					 reservation for the video stream does not succeed. |

| Step 1 | In Cisco Unified Communications Manager Administration , choose the System > Location . |
|---|---|
| Step 2 | Find one location of the location pair and select this location. |
| Step 3 | To modify the RSVP policy between the selected location and
                                          			 another location, select the other location in the location pair. |
| Step 4 | In the RSVP Setting drop-down list, choose an RSVP policy for
                                          			 this location pair. You can set this field to the following values: Use System Default –The RSVP policy for the location pair
                                                   					 matches the cluster-wide RSVP policy. No Reservation –No RSVP reservations get made between any two
                                                   					 locations. Video Desired (Optional) –A call can proceed as a best-effort,
                                                   					 audio-only call if failure to obtain reservations for both audio and video
                                                   					 streams occurs. The RSVP agent continues to attempt RSVP reservation for audio
                                                   					 and informs Cisco Unified Communications Manager if reservation succeeds. 
                                                   				  The system does not ring the terminating device
                                                   					 until RSVP reservation succeeds for the audio stream and, if the call is a
                                                   					 video call, for the video stream as well. Video Desired –A video call can proceed as an audio-only call
                                                   					 if a reservation for the audio stream succeeds but the reservation for the
                                                   					 video stream does not succeed. |

| Step 1 | In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the specified service parameters. You can set these service parameters to the following
                                             				values: RSVP Retry Timer-Specify the RSVP retry timer value in
                                                   					 seconds. If you set this parameter to 0, you disable RSVP retry on the system. Mandatory RSVP Midcall Retry Counter-Specify the midcall RSVP
                                                   					 retry counter when the RSVP policy specifies Mandatory and midcall error
                                                   					 handling option is set to "call fails following retry counter exceeds." The default
                                                   					 value specifies 1 time. If you set the service parameter to -1, retry continues
                                                   					 indefinitely until either the reservation succeeds or the call gets torn down. |

| Step 1 | In Cisco Unified Communications Manager Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the specified service parameter. You can set the Mandatory RSVP mid call error handle
                                             				option service parameter to the following values: Call becomes best effort-If RSVP fails during a call, the call
                                                   					 becomes a best-effort call. If retry is enabled, RSVP retry attempts begin
                                                   					 simultaneously. Call fails following retry counter exceeded-If RSVP fails
                                                   					 during a call, the call fails after N retries of RSVP, where the Mandatory RSVP
                                                   					 Mid-call Retry Counter service parameter specifies N. |

| Step 1 | In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the specified service parameters. These service parameters function as follows: Cisco Unified Communications Manager maps the caller precedence level to
                                                   					 RSVP priority when initiating an RSVP reservation based on the following
                                                   					 configuration: the higher the service parameter value, the higher the priority. The IOS router preempts the call based on RSVP priority. The RSVP agent must notify Cisco Unified Communications Manager about the reason for an RSVP reservation
                                                   					 failure, including the cause for preemption. Cisco Unified Communications Manager uses the existing MLPP mechanism to
                                                   					 notify the preempted calling and called parties about the preemption. |

| Step 1 | In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the RSVP Audio Application ID service parameter. (Default = AudioStream) |
| Step 4 | In the Clusterwide Parameters (System - RSVP) section, configure
                                          			 the RSVP Video Application ID (Default = VideoStream) |

| Step 1 | In Cisco Unified Communications Manager Administration , choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server and
                                          			 choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (System - QoS) section, configure
                                          			 the DSCP for Audio Calls When RSVP Fails service parameter. |
| Step 4 | In the Clusterwide Parameters (System - QoS) section, configure
                                          			 the DSCP for Video Calls When RSVP Fails service parameter. |