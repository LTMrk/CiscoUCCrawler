---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-51ab1e1d19
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01000010.html
retrieved_at: 2026-08-16T17:34:10.200157+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Transcoders and Media Termination Points

## Chapter: Configure Transcoders and Media Termination Points

# Configure Transcoders and Media Termination Points

## Transcoders and Media Termination Points Overview

### Transcoders

A transcoder is a device that performs codec conversion, it converts an input stream from one codec into an output stream
                              that uses a different codec. For example, a transcoder can take a G.711 stream and convert it to a G.729 stream in real time.
                              During a call when the endpoints use different voice codecs, the Cisco Unified Communications Manager invokes a transcoder
                              into the media path. The transcoder converts the data streams between the two incompatible codecs to allow communication between
                              the devices. The transcoder is invisible to the user or the endpoints involved in a call.

Transcoder resources is managed by the Media Resource Manager (MRM).

The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                          providing MTP/TRP functionality.

#### Transcoders and the Media Resource Manager

All Cisco Unified Communications Manager nodes can access transcoders through the Media Resource Manager (MRM). The MRM manages
                                    access to transcoders.

The MRM makes use of Cisco Unified Communications Manager media resource groups and media resource group lists. The media
                                    resource group list allows transcoders to communicate with other devices in the assigned media resource group, which in turn,
                                    provides management of resources within a cluster.

A transcoder control process gets created for each transcoder device that is defined in the database. The MRM keeps track
                                    of the transcoder resources and advertises their availability throughout the cluster.

#### Transcoders as Media Termination Points

Hardware-based transcoder resources also support Media Termination Point ( MTP) and/or Trust Relay Point (TRP) functionality.
                                    In this capacity, when Cisco Unified Communications Manager determines that an endpoint in a call requires an MTP or TRP,
                                    it can allocate a transcoder resource and inserts it into the call, where it acts like an MTP transcoder.

Cisco Unified Communications Manager supports MTP and TRP and transcoding functionality simultaneously. For example, if a
                                    call originates from a Cisco Unified IP Phone (located in the G723 region) to NetMeeting (located in the G711 region), one
                                    transcoder resource supports MTP and transcoding functionality simultaneously.

If a software MTP resource is not available when it is needed, the call tries to connect without using an MTP resource and
                                    MTP/TRP services. If hardware transcoder functionality is required (to convert one codec to another) and a transcoder is not
                                    available, the call will fail.

The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                                providing MTP/TRP functionality.

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

#### Transcoder Failover and Fallback

The following items describe the transcoder device recovery
                                    		  methods when the transcoder is registered to a Cisco Unified Communications Manager node that goes inactive:

If the primary Cisco Unified Communications Manager node fails, the transcoder attempts to register
                                          				with the next available 
                                          				node in the Cisco Unified Communications Manager Group that is specified for the device pool to
                                          				which the transcoder belongs.

The transcoder device reregisters with the primary Cisco Unified Communications Manager node as soon as 
                                          				it becomes available.

A transcoder device unregisters with a Cisco Unified Communications Manager node that becomes unreachable. The calls that were
                                          				on that 
                                          				node will register with the next Cisco Unified Communications Manager node in the list.

If a transcoder attempts to register with a new Cisco Unified Communications Manager node and the register acknowledgment is never
                                          				received, the transcoder registers with the next 
                                          				node in the list.

Transcoder devices will unregister and then disconnect after a hard or soft reset. After the reset completes, the devices
                                    reregister with the primary Cisco Unified Communications Manager node.

### Media Termination
                           	 Points

Media Termination Points (MTP) allow Unified Communications Manager to relay calls that are routed through SIP or H.323 endpoints
                                 or gateways. Media Termination Points extend supplementary services, such as call hold, call transfer, call park, and conferencing,
                                 that are normally not available when a call is routed to an H.323 endpoint. For H.323 supplementary services, MTPs are only
                                 required for endpoints that do not support EmptyCapability Set (ECS) or FastStart. All Cisco and other third party other endpoints
                                 that support ECS and FastStart do not require an MTP.

An MTP device always registers with its primary Unified Communications Manager if that Unified Communications Manager is available
                                 and informs the Unified Communications Manager about the number of MTP resources it supports. You can register multiple MTPs
                                 with the same Unified Communications Manager. When more than one MTP is registered with a Unified Communications Manager,
                                 that Cisco Unified Communications Manager controls the set of resources for each MTP.

For example, consider MTP server 1 as configured for 48 MTP resources, and the MTP server 2 as configured for 24 resources.
                                 If both MTPs register with the same Unified Communications Manager, that Unified Communications Manager maintains both sets
                                 of resources for a total of 72 registered MTP resources.

When the Unified Communications Manager determines that a call endpoint requires an MTP, it allocates an MTP resource from
                                 the MTP that has the least active streams. That MTP resource gets inserted into the call on behalf of the endpoint. MTP resource
                                 use remains invisible to both the users of the system and to the endpoint on whose behalf it was inserted. If an MTP resource
                                 is not available when it is needed, the call connects without using an MTP resource, and that call does not have supplementary
                                 services.

#### MTP Failover and
                              	 Fallback

- If the primary Cisco
                                       			 Unified Communications Manager fails, the MTP attempts to register with the
                                       			 next available Cisco Unified Communications Manager in the Cisco Unified
                                       			 Communications Manager Group that is specified for the device pool to which the
                                       			 MTP belongs.

- The MTP device reregisters
                                       			 with the primary Cisco Unified Communications Manager as soon as it becomes
                                       			 available after a failure and is currently not in use.

- The system maintains the
                                       			 calls or conferences that were active in call preservation mode until all
                                       			 parties disconnect. The system does not make supplementary services available.

- If an MTP attempts to
                                       			 register with a new Cisco Unified Communications Manager and the register
                                       			 acknowledgment is never received, the MTP registers with the next Cisco Unified
                                       			 Communications Manager.

The MTP devices unregister and then disconnect after a hard or soft
                                    		  reset. After the reset completes, the devices reregister with the Cisco Unified
                                    		  Communications Manager.

#### Software Media
                              	 Termination Point Type

Software Media Termination Point type in Cisco Unified Communications
                                    		  Manager Administration is listed in the following table.

Software MTP Type

Description

Cisco Media Termination Point Software

A single MTP provides a default of 48 MTP (user
                                                						configurable) resources, depending on the speed of the network and the network
                                                						interface card (NIC). For example, a 100-MB Network/NIC card can support 48 MTP
                                                						resources, while a 10-MB NIC card cannot.

For a 10-MB Network/NIC card, approximately 24 MTP resources
                                                						can be provided; however, the exact number of MTP resources that are available
                                                						depends on the resources that other applications on that PC are consuming, the
                                                						speed of the processor, network loading, and various other factors.

## Transcoders and
                        	 MTPs Configuration Task Flow

Step 1

To Configure Transcoders ,complete
                                       			 the following sub tasks:

- Configure Transcoders

- Add Transcoder to Media Resource Group

If you need to configure a transcoder, follow this step.
                                          				Transcoders convert an input stream from one codec into an output stream that
                                          				uses a different codec.

Step 2

To Configure a Software MTP ,
                                       			 complete the following sub tasks:

- Configure Media Termination Points

- Add Software MTP to Media Resource Group

If you need to configure a software MTP, follow this step.
                                          				Software MTPs allow Cisco Unified Communications Manager to relay calls that
                                          				are routed through SIP or H.323 endpoints or gateways.

### Configure
                           	 Transcoders

Step 1

Determine the
                                          			 number of transcoder resources that are needed and the number of transcoder
                                          			 devices that are needed to provide these resources.

For a
                                             				multi-site deployment, Cisco recommends placing a transcoder local at each site
                                             				where it might be required. If multiple codecs are needed, it is necessary to
                                             				know how many endpoints do not support all codecs, where those endpoints are
                                             				located, what other groups will be accessing those resources, how many maximum
                                             				simultaneous calls these device must support, and where those resources are
                                             				located in the network.

Step 2

Configure Transcoders

Step 3

Add Transcoder to Media Resource Group

Step 4

Restart the
                                          			 transcoder devices.

#### Configure Transcoders

A transcoder is a
                                    		  device that converts an input stream from one codec into an output stream that
                                    		  uses a different codec.

##### Before you begin

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

#### Add Transcoder to
                              	 Media Resource Group

##### Before you begin

Configure Transcoders

Step 1

Choose Media
                                                   				  Resources > Media Resource Group .

Step 2

Click Find to display the list of configured Media
                                             			 Resource Groups.

Step 3

Click on the
                                             			 required Media Resource Group.

Step 4

Select the
                                             			 transcoder from the list of available media resources and add it to the
                                             			 Selected Media Resources list.

Step 5

Click Save .

Step 6

Navigate to Media Resources > Media
                                                   				  Resource Group .

Step 7

In the Find and List Transcoders window, check the
                                             			 check boxes next to the transcoders that you want to synchronize. To choose all
                                             			 transcoders in the window, check the check box in the matching records title
                                             			 bar.

Step 8

Click Apply Config to Selected .

Step 9

Click OK .

##### What to do next

Restart the
                                    		  transcoder device.

#### Synchronize Transcoder

To synchronize a transcoder with the most recent configuration changes, perform the following procedure, which applies any
                                    outstanding configuration settings in the least-intrusive manner possible. (For example, a reset/restart may not be required
                                    on some affected devices.).

Step 1

Choose Media Resources > Transcoder .

Step 2

Choose the search criteria to use.

Step 3

Click Find .

The window displays a list of transcoders that match the search criteria.

Step 4

Check the check boxes next to the transcoders that you want to synchronize. To choose all transcoders in the window, check
                                             the check box in the matching records title bar.

Step 5

Click Apply Config to Selected .

Step 6

Click OK .

### Configure a
                           	 Software MTP

This procedure describes the steps to configure a software MTP. For
                                 		  information about configuring a hardware MTP, see Configure Transcoders .

Step 1

Configure Media Termination Points

Configure a media termination point to relay calls that are routed
                                             				through SIP endpoints or gateways.

Step 2

Add Software MTP to Media Resource Group

Step 3

Restart the media termination point devices.

#### Configure Media Termination Points

##### Before you begin

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

#### Add Software MTP
                              	 to Media Resource Group

##### Before you begin

Configure Media Termination Points

Step 1

Choose Media Resources > Media
                                                   				  Resource Group .

Step 2

Click Find to display the list of configured Media
                                             			 Resource Groups.

Step 3

Click on the required Media Resource Group.

Step 4

Select the transcoder from the list of Available Media Resources and add it to the Selected Media Resources list.

Step 5

Click Save .

##### What to do next

Restart the media termination point device.

## Transcoders and MTPs Interactions and Restrictions

### Transcoder Interactions and Restrictions

#### Transcoder Interactions and Restrictions

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

### Media Termination Points Interactions and Restrictions

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

| Note | The transcoder supports transcoding between G.711 and all codecs, including G.711, when functioning as a transcoder and when
                                          providing MTP/TRP functionality. |
|---|---|

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

| Software MTP Type | Description |
|---|---|
| Cisco Media Termination Point Software | A single MTP provides a default of 48 MTP (user
                                                						configurable) resources, depending on the speed of the network and the network
                                                						interface card (NIC). For example, a 100-MB Network/NIC card can support 48 MTP
                                                						resources, while a 10-MB NIC card cannot. For a 10-MB Network/NIC card, approximately 24 MTP resources
                                                						can be provided; however, the exact number of MTP resources that are available
                                                						depends on the resources that other applications on that PC are consuming, the
                                                						speed of the processor, network loading, and various other factors. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To Configure Transcoders ,complete
                                       			 the following sub tasks: Configure Transcoders Add Transcoder to Media Resource Group | If you need to configure a transcoder, follow this step.
                                          				Transcoders convert an input stream from one codec into an output stream that
                                          				uses a different codec. |
| Step 2 | To Configure a Software MTP ,
                                       			 complete the following sub tasks: Configure Media Termination Points Add Software MTP to Media Resource Group | If you need to configure a software MTP, follow this step.
                                          				Software MTPs allow Cisco Unified Communications Manager to relay calls that
                                          				are routed through SIP or H.323 endpoints or gateways. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Determine the
                                          			 number of transcoder resources that are needed and the number of transcoder
                                          			 devices that are needed to provide these resources. | For a
                                             				multi-site deployment, Cisco recommends placing a transcoder local at each site
                                             				where it might be required. If multiple codecs are needed, it is necessary to
                                             				know how many endpoints do not support all codecs, where those endpoints are
                                             				located, what other groups will be accessing those resources, how many maximum
                                             				simultaneous calls these device must support, and where those resources are
                                             				located in the network. |
| Step 2 | Configure Transcoders | Configure transcoders to convert an input stream from one codec
                                          			 into an output stream that uses a different codec. |
| Step 3 | Add Transcoder to Media Resource Group | Add the
                                          			 new transcoders to the appropriate media resource groups. |
| Step 4 | Restart the
                                          			 transcoder devices. | See the
                                          			 transcoder documentation for details. |

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

| Step 1 | Choose Media
                                                   				  Resources > Media Resource Group . |
|---|---|
| Step 2 | Click Find to display the list of configured Media
                                             			 Resource Groups. |
| Step 3 | Click on the
                                             			 required Media Resource Group. The Media
                                                				Resource Group Configuration window displays. |
| Step 4 | Select the
                                             			 transcoder from the list of available media resources and add it to the
                                             			 Selected Media Resources list. |
| Step 5 | Click Save . |
| Step 6 | Navigate to Media Resources > Media
                                                   				  Resource Group . |
| Step 7 | In the Find and List Transcoders window, check the
                                             			 check boxes next to the transcoders that you want to synchronize. To choose all
                                             			 transcoders in the window, check the check box in the matching records title
                                             			 bar. |
| Step 8 | Click Apply Config to Selected . The Apply Configuration Information dialog box displays. |
| Step 9 | Click OK . |

| Step 1 | Choose Media Resources > Transcoder . The Find and List Transcoders window displays. |
|---|---|
| Step 2 | Choose the search criteria to use. |
| Step 3 | Click Find . The window displays a list of transcoders that match the search criteria. |
| Step 4 | Check the check boxes next to the transcoders that you want to synchronize. To choose all transcoders in the window, check
                                             the check box in the matching records title bar. |
| Step 5 | Click Apply Config to Selected . The Apply Configuration Information dialog box displays. |
| Step 6 | Click OK . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Media Termination Points | Configure a media termination point to relay calls that are routed
                                             				through SIP endpoints or gateways. |
| Step 2 | Add Software MTP to Media Resource Group | Add the new media termination point to the appropriate media
                                          			 resource groups. |
| Step 3 | Restart the media termination point devices. |  |

| Step 1 | From Cisco Unified CM
                                             			 Administration, choose Media Resources > Media
                                                   				  Termination Point . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing MTP. Click Add New to create a new MTP. |
| Step 3 | Assign a Media Termination Point Name . |
| Step 4 | Assign a Device Pool . |
| Step 5 | Check the Trusted Relay Point check box if you want to designate this MTP as a Trusted Relay Point (TRP). |
| Step 6 | Click Save . |

| Step 1 | Choose Media Resources > Media
                                                   				  Resource Group . |
|---|---|
| Step 2 | Click Find to display the list of configured Media
                                             			 Resource Groups. |
| Step 3 | Click on the required Media Resource Group. The Media Resource Group Configuration window
                                             			 displays. |
| Step 4 | Select the transcoder from the list of Available Media Resources and add it to the Selected Media Resources list. |
| Step 5 | Click Save . |

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