---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-ad4e5fed76
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111011.html
retrieved_at: 2026-08-16T17:33:41.399169+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Trusted Relay Points

## Chapter: Configure Trusted Relay Points

# Configure Trusted Relay Points

## Trusted Relay
                        	 Point Overview

A Trusted Relay Point (TRP) is an MTP or transcoder that Cisco Unified Communications Manager can insert into the media stream
                              to act as a control point for call media. The TRP can provide further processing on the stream and can ensure that the stream
                              follows a specific path.

When a call requires a trusted relay point, Cisco Unified Communications Manager allocates an MTP or transcoder that has been
                              enabled with TRP functionality.

### Configuration

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

## Trusted Relay
                        	 Points Task Flow

Step 1

Configure Trusted Relay Point for a Device .

Configure trusted relay points (TRP) for one or multiple devices
                                          				where media ends and insert TRP in Cisco Unified Communications Manager .

Step 2

Configure Trusted Relay Point for Media Termination Point .

Step 3

Configure Trusted Relay Point for Transcoder .

Configure transcoder so that you can use the device as a trusted
                                          				relay point.

Step 4

Enable Trusted Relay Point Service Parameter .

Enable the TRP service parameter to determine whether a call that
                                          				requires a TRP is allowed to proceed if no TRP resource is available.

### Configure Trusted
                           	 Relay Point for a Device

You can configure
                                 		  trusted relay points (TRP) for one or multiple devices where media ends and
                                 		  insert TRP in Cisco Unified Communications Manager. By configuring the TRP for
                                 		  a device, the device provides further processing on that stream or acts as a
                                 		  method to ensure that the stream follows a specific path.

Step 1

From the Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > Common Device Configuration .

Step 2

To configure a
                                          			 trusted relay point for an existing device, from the Find
                                             				and List Common Device Configurations window, specify the appropriate filters and click Find .

Step 3

To configure
                                          			 trusted relay point for a new device, from the Common
                                             				Device Configuration window, click Add
                                             				New .

Step 4

Configure the
                                          			 fields in the Common
                                             				Device Configuration window. See the online help for more
                                          			 information about the fields and their configuration options.

Step 5

In the Common
                                             				Device Configuration Information section, click the Use
                                             				Trusted Relay Point check box.

Step 6

Click Save .

#### What to do next

Configure Trusted Relay Point for Media Termination Point .

### Configure Trusted
                           	 Relay Point for Media Termination Point

You can configure
                                 		  a media termination point (MTP) so that you can use a device as a trusted relay
                                 		  point.

#### Before you begin

Configure Trusted Relay Point for a Device .

Step 1

From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Media Termination Point .

Step 2

To configure a
                                          			 trusted relay point for an existing media termination point, from the Find
                                             				and List Media Termination Points window, specify the appropriate filters and click Find .

Step 3

To configure
                                          			 trusted relay point for a new media termination point, click Add
                                             				New .

Step 4

Configure the
                                          			 fields on the Media
                                             				Termination Point Configuration window. See the online help for more
                                          			 information about the fields and their configuration options.

Step 5

In the Media
                                             				Termination Point Information section, click the Use
                                             				Trusted Relay Point check box.

Step 6

Click Save .

#### What to do next

Configure Trusted Relay Point for Transcoder .

### Configure Trusted
                           	 Relay Point for Transcoder

You can configure
                                 		  a transcoder so that you can use the device as a trusted relay point.

#### Before you begin

Configure Trusted Relay Point for Media Termination Point .

Step 1

From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Transcoder .

Step 2

To configure a
                                          			 trusted relay point for an existing transcoder, from the Find
                                             				and List Transcoder window, specify the appropriate filters and click Find .

Step 3

To configure
                                          			 trusted relay point for a new transcoder, click Add
                                             				New .

Step 4

Configure the
                                          			 fields on the Transcoder Configuration window. See the online help
                                          			 for more information about the fields and their configuration options.

Step 5

In the Media
                                             				Server Transcoder Info section, click the Use
                                             				Trusted Relay Point check box.

Step 6

Click Save .

#### What to do next

Enable Trusted Relay Point Service Parameter .

### Enable Trusted
                           	 Relay Point Service Parameter

You can enable the
                                 		  TRP service parameter to determine whether a call that requires a TRP is
                                 		  allowed to proceed if no TRP resource is available.

#### Before you begin

Configure Trusted Relay Point for Transcoder .

Step 1

From the Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters .

Only Server drop-down list appears.

Step 2

From the Service
                                             				Parameter Configuration window, choose a server from the Server drop-down list.

Step 3

Choose a Cisco
                                          			 Unified Communications Manager server from the Server drop-down list.

Step 4

From the
                                          			 Clusterwide Parameters (Device - General) section, choose True for Fail
                                             				Call If Trusted Relay Point Allocation Fails drop-down list. See
                                          			 the Related Topics section about the fields and their configuration options.

Step 5

From the
                                          			 Clusterwide Parameters (Device - H323) section, choose True for Fail
                                             				Call If MTP Allocation Fails drop-down list. See the Related Topics
                                          			 section about the fields and their configuration options.

Step 6

Click Save .

#### Call Status When
                              	 MTP and TRP Service Parameters are Selected

If you check both
                                    		  the Media Termination Point Required and the Use Trusted Relay Point check boxes for an
                                    		  endpoint, Cisco Unified Communications
                                       			 Manager allocates a Media Termination Point (MTP) that is also a
                                    		  Trusted Relay Point (TRP). If the administrator fails to allocate such an MTP
                                    		  or TRP, the call status appears.

The following table shows the call status with the values of the Fail
                                       			 Call If Trusted Relay Point Allocation Fails and the Fail
                                       			 Call if MTP Allocation Fails service parameters when a call fails.

Fail
                                                						Call If TRP Allocation Fails

Fail
                                                						Call If MTP Allocation Fails

Fail
                                                						Call?

True

True

Yes

True

False

Yes

False

True

Yes, if
                                                						MTP is required for H.323 endpoint. No, if MTP is required for SIP endpoint.

False

False

No

#### Call Status When
                              	 MTP and TRP Service Parameters are Not Selected

If both the Fail Call If Trusted Relay Point Allocation
                                       			 Fails service parameter and the Fail Call If MTP
                                       			 Allocation Fails service parameter are set to False , the following table shows the call
                                    		  behavior in relationship to the MTP that is required and Use Trusted Relay Point configuration and the
                                    		  resource allocation status.

MTP Required

Use TRP

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

If MTP required is checked for H.323 endpoint, supplementary
                                                						services will be disabled.

N

Y

TRP allocated

Audio or video call depends on endpoint capabilities, and
                                                						call admission control (CAC). Supplementary services still work.

N

Y

None allocated

Audio or video call. Supplementary services still work, but
                                                						no TRP support exists.

## Trusted Relay Points Interactions and Restrictions

### Trusted Relay Points Interactions and Restrictions

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

### Trusted Relay Points Restrictions

Restriction

Description

Insertion of trusted relay point for an endpoint

Cisco Unified Communications
                                                						Manager must insert a TRP for the endpoint if you have checked the Use Trusted Relay Point check box for
                                             					 either the endpoint or the device pool that is associated with the device. The
                                             					 call may fail if Cisco Unified Communications
                                                						Manager fails to allocate a TRP while the Fail Call If Trusted Relay Point Allocation Fails service parameter is set to True .

Allocation of media termination point for an endpoint

If you check both the Media Termination Point Required check
                                             					 box and the Use Trusted Relay Point check box for an
                                             					 endpoint, Cisco Unified
                                                						Communications Manager should allocate an MTP that is also a TRP. If
                                             					 the administrator fails to allocate such an MTP or TRP, the call status
                                             					 appears.

Allocation of trusted relay point

In most instances, TRP is allocated after users answer the
                                             					 call, so if a call fails due to failure to allocate the TRP, users may receive
                                             					 fast-busy tone after answering the call. (The SIP outbound leg with MTP
                                             					 required, or H.323 outbound faststart, represents an exception.)

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Trusted Relay Point for a Device . | Configure trusted relay points (TRP) for one or multiple devices
                                          				where media ends and insert TRP in Cisco Unified Communications Manager . |
| Step 2 | Configure Trusted Relay Point for Media Termination Point . | Configure media termination point (MTP) so that you can use the
                                          				device as a trusted relay point. Note Ensure that a device that is configured as a TRP in Cisco Unified
                                                         					 Communications Manager has the appropriate network connectivity and
                                                      				  configuration between the TRP and any endpoints that are involved in the call. | Note | Ensure that a device that is configured as a TRP in Cisco Unified
                                                         					 Communications Manager has the appropriate network connectivity and
                                                      				  configuration between the TRP and any endpoints that are involved in the call. |
| Note | Ensure that a device that is configured as a TRP in Cisco Unified
                                                         					 Communications Manager has the appropriate network connectivity and
                                                      				  configuration between the TRP and any endpoints that are involved in the call. |
| Step 3 | Configure Trusted Relay Point for Transcoder . | Configure transcoder so that you can use the device as a trusted
                                          				relay point. Note Ensure that a device that is configured as a TRP in Cisco Unified Communications
                                                      				  Manager has the appropriate network connectivity and configuration
                                                   				between the TRP and any endpoints that are involved in the call. | Note | Ensure that a device that is configured as a TRP in Cisco Unified Communications
                                                      				  Manager has the appropriate network connectivity and configuration
                                                   				between the TRP and any endpoints that are involved in the call. |
| Note | Ensure that a device that is configured as a TRP in Cisco Unified Communications
                                                      				  Manager has the appropriate network connectivity and configuration
                                                   				between the TRP and any endpoints that are involved in the call. |
| Step 4 | Enable Trusted Relay Point Service Parameter . | Enable the TRP service parameter to determine whether a call that
                                          				requires a TRP is allowed to proceed if no TRP resource is available. |

| Note | Ensure that a device that is configured as a TRP in Cisco Unified
                                                         					 Communications Manager has the appropriate network connectivity and
                                                      				  configuration between the TRP and any endpoints that are involved in the call. |
|---|---|

| Note | Ensure that a device that is configured as a TRP in Cisco Unified Communications
                                                      				  Manager has the appropriate network connectivity and configuration
                                                   				between the TRP and any endpoints that are involved in the call. |
|---|---|

| Step 1 | From the Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > Common Device Configuration . |
|---|---|
| Step 2 | To configure a
                                          			 trusted relay point for an existing device, from the Find
                                             				and List Common Device Configurations window, specify the appropriate filters and click Find . |
| Step 3 | To configure
                                          			 trusted relay point for a new device, from the Common
                                             				Device Configuration window, click Add
                                             				New . |
| Step 4 | Configure the
                                          			 fields in the Common
                                             				Device Configuration window. See the online help for more
                                          			 information about the fields and their configuration options. |
| Step 5 | In the Common
                                             				Device Configuration Information section, click the Use
                                             				Trusted Relay Point check box. |
| Step 6 | Click Save . |

| Step 1 | From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Media Termination Point . |
|---|---|
| Step 2 | To configure a
                                          			 trusted relay point for an existing media termination point, from the Find
                                             				and List Media Termination Points window, specify the appropriate filters and click Find . |
| Step 3 | To configure
                                          			 trusted relay point for a new media termination point, click Add
                                             				New . |
| Step 4 | Configure the
                                          			 fields on the Media
                                             				Termination Point Configuration window. See the online help for more
                                          			 information about the fields and their configuration options. |
| Step 5 | In the Media
                                             				Termination Point Information section, click the Use
                                             				Trusted Relay Point check box. |
| Step 6 | Click Save . |

| Step 1 | From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Transcoder . |
|---|---|
| Step 2 | To configure a
                                          			 trusted relay point for an existing transcoder, from the Find
                                             				and List Transcoder window, specify the appropriate filters and click Find . |
| Step 3 | To configure
                                          			 trusted relay point for a new transcoder, click Add
                                             				New . |
| Step 4 | Configure the
                                          			 fields on the Transcoder Configuration window. See the online help
                                          			 for more information about the fields and their configuration options. |
| Step 5 | In the Media
                                             				Server Transcoder Info section, click the Use
                                             				Trusted Relay Point check box. |
| Step 6 | Click Save . |

| Step 1 | From the Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters . Only Server drop-down list appears. |
|---|---|
| Step 2 | From the Service
                                             				Parameter Configuration window, choose a server from the Server drop-down list. The Service drop-down list appears. |
| Step 3 | Choose a Cisco
                                          			 Unified Communications Manager server from the Server drop-down list. Based
                                          			 on the selected server and service, the service parameters appear. |
| Step 4 | From the
                                          			 Clusterwide Parameters (Device - General) section, choose True for Fail
                                             				Call If Trusted Relay Point Allocation Fails drop-down list. See
                                          			 the Related Topics section about the fields and their configuration options. |
| Step 5 | From the
                                          			 Clusterwide Parameters (Device - H323) section, choose True for Fail
                                             				Call If MTP Allocation Fails drop-down list. See the Related Topics
                                          			 section about the fields and their configuration options. |
| Step 6 | Click Save . |

| Fail
                                                						Call If TRP Allocation Fails | Fail
                                                						Call If MTP Allocation Fails | Fail
                                                						Call? |
|---|---|---|
| True | True | Yes |
| True | False | Yes |
| False | True | Yes, if
                                                						MTP is required for H.323 endpoint. No, if MTP is required for SIP endpoint. |
| False | False | No |

| MTP Required | Use TRP | Resource Allocation Status | Call Behavior |
|---|---|---|---|
| Y | Y | TRP allocated | Audio call only because no pass-through support exists. |
| Y | Y or N | MTP only | Audio call only. No TRP support. |
| Y | Y or N | None allocated | If MTP required is checked for H.323 endpoint, supplementary
                                                						services will be disabled. |
| N | Y | TRP allocated | Audio or video call depends on endpoint capabilities, and
                                                						call admission control (CAC). Supplementary services still work. |
| N | Y | None allocated | Audio or video call. Supplementary services still work, but
                                                						no TRP support exists. |

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

| Restriction | Description |
|---|---|
| Insertion of trusted relay point for an endpoint | Cisco Unified Communications
                                                						Manager must insert a TRP for the endpoint if you have checked the Use Trusted Relay Point check box for
                                             					 either the endpoint or the device pool that is associated with the device. The
                                             					 call may fail if Cisco Unified Communications
                                                						Manager fails to allocate a TRP while the Fail Call If Trusted Relay Point Allocation Fails service parameter is set to True . |
| Allocation of media termination point for an endpoint | If you check both the Media Termination Point Required check
                                             					 box and the Use Trusted Relay Point check box for an
                                             					 endpoint, Cisco Unified
                                                						Communications Manager should allocate an MTP that is also a TRP. If
                                             					 the administrator fails to allocate such an MTP or TRP, the call status
                                             					 appears. |
| Allocation of trusted relay point | In most instances, TRP is allocated after users answer the
                                             					 call, so if a call fails due to failure to allocate the TRP, users may receive
                                             					 fast-busy tone after answering the call. (The SIP outbound leg with MTP
                                             					 required, or H.323 outbound faststart, represents an exception.) |