---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-cucm-b-feature-configuration-guide-for-cisco14su2-cucm-mp-m-90b838d0a6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/cucm_b_feature-configuration-guide-for-cisco14su2/cucm_mp_m7ca6519_00_music-on-hold-12-0.html
retrieved_at: 2026-08-16T16:25:23.969338+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: May 7, 2026

Chapter: Music On Hold

## Chapter: Music On Hold

# Music On Hold

## Music On Hold
                        	 Overview

Use the integrated
                           		Music On Hold (MOH) feature to place on-net and off-net users on hold
                           		with music from a streaming source. This source makes music
                           		available to any on-net or off-net device that you place on hold. On-net
                           		devices include station devices and applications that an interactive voice response (IVR) or call
                           		distributor places on hold,
                           		consult hold, or park hold. Off-net users include those users who are connected through Media
                           		Gateway Control Protocol (MGCP) or Skinny Call Control Protocol (SCCP) gateways,
                           		Cisco IOS H.323 gateways, and Cisco IOS Media Gateway Control Protocol gateways. The system
                           		also makes the Music On Hold feature available for Cisco IP POTS phones that
                           		connect to the Cisco IP network through Foreign Exchange Station (FXS) ports on
                           		Cisco IOS H.323 or MGCP and for Cisco MGCP or SCCP gateways.

Start Cisco Unified
                              		  Communications Manager to create a media resource manager. Music On Hold server registers to the media resource manager with its music on hold
                           		resources. Music On Hold server is a software application that provides music
                           		on hold audio sources and connects a music on hold audio source to multiple
                           		streams.

When an
                           		end device or feature places a call on hold, Cisco Unified
                              		  Communications Manager connects the held device to a music resource.
                           		When the held device is retrieved, it disconnects from the music on hold
                           		resource and resumes normal activity.

### Caller-Specific
                           	 Music On Hold

For SIP calls
                                 		  that a phone receives over the SIP trunk, Cisco Unified Communications Manager can use a
                                 		  different MOH audio source.

An external
                                 		  application, such as the Cisco Unified Customer Voice Portal (CVP) contact
                                 		  center solution, determines the most appropriate MOH audio source based on the
                                 		  caller ID, dialed number, or IVR interaction when a call is received from the
                                 		  public switched telephone network (PSTN).

For details, see the Cisco Unified Customer Voice Portal documentation
                                 		  at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

### Increased Capacity
                           	 of IP Voice Media Streaming Application and Expanded MOH Audio Source

Cisco IP Voice
                                 		  Media Streaming application is installed automatically when you install Cisco
                                 		  Unified Communications Manager. Activate this application to enable the Music
                                 		  On Hold (MOH) feature.

With this release,
                                 		  the capacity of Cisco Unified Communications Manager to support unique and
                                 		  concurrent MOH audio sources, while the Music On Hold service is running on the
                                 		  MOH server, is increased from 51 to 501. The MOH audio sources are numbered
                                 		  from 1 to 501 with the fixed MOH audio source remaining at the number 51.

The fixed MOH
                                 		  device cannot use an audio source that connects through a USB MOH device,
                                 		  because Cisco Unified Communications Manager does not support USB when running
                                 		  on VMware. Use of the fixed MOH USB device is not supported on VMware. However,
                                 		  provision the external sound device for use with deployments that utilize Cisco
                                 		  Unified Survivable Remote Site Telephony (SRST) multicast MOH.

You can configure
                                 		  each MOH audio source to use a custom announcement as an initial greeting
                                 		  and/or an announcement that is played periodically to callers who are hearing
                                 		  the music. Cisco Unified Communications Manager provides 500 custom
                                 		  announcements that you can use on one or multiple MOH audio sources. These
                                 		  announcements are not distributed between the Cisco Unified Communications
                                 		  Manager servers within a cluster. You have to upload these custom announcement
                                 		  files to each server that provides the MOH and announcement services. You must
                                 		  also upload each custom music file for MOH audio sources to each server.

#### Performance Impact of Media Devices with Services

The Cisco IP Voice Media Streaming application runs as a service for four media devices—annunciator (ANN), software conference
                                    bridge, Music On Hold (MOH), and software media termination point. Activate this service on a Cisco Unified Communications
                                    Manager server as coresident with call processing. When you activate this service, ensure that you configure these media devices
                                    for limited capacity to avoid any impact on the call processing. The default settings for the media devices are defined based
                                    on this
                                    coresident operation. You can adjust these settings by reducing the use of one or more media devices to increase other settings.

For example, if you are not using software media termination point devices, you can choose the Run Flag setting for the SW MTP to False , select System > Service Parameters > Cisco IP Voice Media Streaming App service > MTP Parameters , and add the MTP Call Count setting to Media Resource > MOH Server > Maximum Half Duplex Streams configuration. Depending on the call traffic, you can modify the default settings. However, monitor the server performance
                                    activity for CPU, memory,
                                    and IO wait. For higher capacity clusters, such as the ones using
                                    7500 user OVA configuration, it is possible to increase the default media device
                                    settings for Call Count by 25%.

For installations where you expect high usage of the media devices,
                                    such as Music On Hold, or where high call volumes require higher
                                    number of media connections, activate the Cisco IP Voice Media
                                    Streaming application service on one or more of the Cisco Unified
                                    Communications Manager servers which do not have call processing
                                    activated.
                                    Activating this service limits the impact of media device usage to other services, such as call processing. Then, you can
                                    increase the   configuration settings for maximum number of calls for the media devices.

When you activate Cisco IP Voice Media Streaming application as co-resident with Cisco Unified  Communications Manager service,
                                    it can impact call processing performance. To increase the capacity settings for Music On Hold or annunciator from the default
                                    settings, it is suggested to activate Cisco IP Voice Media Streaming application on a server without activating Cisco Unified
                                    Communications Manager.

The CPU performance is impacted by MOH when active callers are on hold or when multicast MOH audio streams are configured.

Configuration Notes

CPU Performance

Dedicated MOH server, 1000 held calls, 500 MOH sources with greeting and periodic announcements.

25–45% (7500 user OVA configuration)

Native call queuing with dedicated MOH server and annunciator server, 1000 queued calls, 500 MOH sources with greeting and
                                                periodic announcements. An annunciator can play up to 300 simultaneous greeting announcements.

25–45% (7500 user OVA configuration)

Dedicated MOH server, 500 held calls, 500 MOH sources with greeting and periodic announcements.

15–35% (7500 user OVA configuration)

Configuration

Recommendation Limit

When  Cisco IP Voice Media Streaming application is co-resident with Cisco Unified  Communications Manager on 2500 OVA (moderate
                                                call processing).

MOH: 500 held callers, 100 MOH sources, and 48 to 64 annunciator callers.

When  Cisco IP Voice Media Streaming application is a dedicated server on 2500 OVA.

MOH: 750 held callers, 250 MOH sources, and 250 annunciator callers.

When Cisco IP Voice Media Streaming application is co-resident with Cisco Unified  Communications Manager on 7500/10K OVA
                                                (moderate call processing).

MOH: 500 held callers, 250 MOH sources, and 128 annunciator callers.

When  Cisco IP Voice Media Streaming application is a  dedicated server on 7500/10K OVA.

Reduce annunciator to 300 for two MOH codecs.

These recommendations are specific to MOH/ANN devices. If you combine these devices  with the software media termination
                                                point (MTP) and call forward busy (CFB) devices, reduce the limits to provide streams.

#### Configuration Limitations for Capacity Planning

The Cisco IP Voice Media Streaming application and Self Provisioning IVR services use a media kernel driver to create and
                                    control Real-time Transfer Protocol (RTP) streams. This media kernel driver has a 	capacity of 6000 streams. These streams
                                    allow the media devices and IVR to make resource reservations.

These reservations are based on the following capacity calculations:

Media Device

Capacity

Annunciator

(Call Count service parameter) * 3

Where 3 indicates total of receiving (RX) and transmitting (TX) calls for endpoint and 1 for .wav file.

Software Conference Bridge

(Call Count service parameter) * 2

Where 2 indicates total streams of RX and TX endpoints.

Software Media Termination Point

(Call Count service parameter) * 2

Where 2 indicates total streams of RX and TX endpoints.

Music On Hold

((Maximum Half Duplex Streams) * 3) + (501 * 2 * [number of enabled
                                                MOH codecs])

(Maximum Half Duplex Streams) is a configuration setting on the MOH
                                                         device configuration administration web page.

3 indicates total steams of RX, TX, and greeting announcement .wav
                                                         file.

501 indicates the maximum number of Music On Hold (MOH) sources.

2 indicates music .wav stream and possible multicast TX stream.

[number of enabled MOH codecs] is based on how many MOH
                                                         codecs are enabled in the Cisco IP Voice Media Streaming application
                                                         service parameters.

Self Provisioning IVR Service

(500 * 2)

Where 500 indicates callers, and 2 indicates total streams from RX and TX
                                                streams.

Hence, to enable MOH to support a maximum of 1000 callers, use the following equation: 1000 * 3 + 501 * 2 * 1 = 4002 driver streams with one enabled codec and 1000 * 3 +501 * 2 * 2 = 5004 with two enabled codecs. Reduce the remaining devices and  deactivate the Self Provisioning IVR service to limit total reservations
                                    to 6000, which allows the MOH device to make these reservations. It may also require that you do not activate the Self Provisioning
                                    IVR service on the same server with Cisco IP Voice Media Streaming
                                    application.

If configuration settings of the media devices exceed the capacity
                                    of the media device driver, the media devices that register with
                                    the device driver first will be able to reserve their required
                                    stream resources. The media devices that register later are restricted to fewer than requested stream resources. The later
                                    registered media devices result in logging some
                                    alarm messages and automatically reducing the call count for
                                    the restricted media device.

A media kernel driver with a 	capacity of 6000 streams might not support that many simultaneous media device connections.

## Interwork External
                        	 Multicast MOH to Unicast MOH

With this release, you can configure a Cisco Unified Survivable Remote
                              		  Site Telephony (SRST) router as an audio source. This router provides multicast
                              		  MOH audio for devices that are capable of multicast reception. In this
                              		  approach, devices act as if Cisco Unified Communications Manager is sending the
                              		  multicast MOH audio. However, devices that are capable of only the unicast
                              		  reception cannot hear the MOH audio that an external MOH source (for example,
                              		  Cisco Unified SRST router) sends. Examples of devices that are capable of
                              		  unicast reception only can be public switched telephone network (PSTN) phones,
                              		  destination to session border controllers (SBC), and Session Initiation
                              		  Protocol (SIP) trunks.

In this release of Cisco Unified Communications Manager, this feature
                              		  is enhanced to receive multicast MOH audio from an external audio source and
                              		  send it as unicast MOH audio. Cisco Unified Communications Manager uses this
                              		  feature to play multicast MOH audio as unicast MOH for the devices that are
                              		  capable of unicast MOH reception only. Examples of an external MOH audio source
                              		  can be a Cisco Unified SRST router or software that can send multicast MOH
                              		  audio.

An administrator configures the fields for this feature from Cisco
                              		  Unified CM Administration Music On Hold Audio Source Configuration window.

This feature has no impact on existing functionality of playing
                                                				  multicast MOH audio using an external audio source for the devices that are
                                                				  capable of multicast reception.

For the unicast media connection, Cisco Unified Communications
                                                				  Manager MOH Server plays the initial announcement and periodic announcement
                                                				  even if you configure the MOH audio source with external multicast source.

### Configuration Tips for the Codec-Specific Inbound Audio
                              		  Stream

Configure an external multicast audio source, such as Cisco Unified
                              		  SRST router, to MOH server for streaming the required audio feed.

To configure an external multicast audio source, such as a Cisco
                              		  Unified SRST router, configure the Source IPv4 Multicast Address and Source Port Number fields in the MOH Audio Source Configuration window.

Cisco Unified Communications Manager listens to multicast G.711
                                       				mu-law stream on external multicast IP address and port that you configured on
                                       				the MOH Audio Source configuration window. An MOH server can transcode between the G.711
                                       				mu-law or a-law or L16 256K wideband MOH codecs. The external multicast RTP
                                       				stream uses G.711 mu-law codec for MOH as a source for G.711 mu-law or a-law or
                                       				L16 256K wideband MOH codecs. For G.711 a-law and wideband calls, Cisco Unified
                                       				Communications Manager MOH server transcodes the inbound G.711 mu-law stream to
                                       				outbound G.711 a-law or wideband stream before sending it to the device.

Cisco Unified Communications Manager listens to multicast G.729
                                       				stream on external multicast IP and port value added with four that is
                                       				configured on the MOH audio source configuration window. For
                                       				example, if you configure an MOH audio Source with 239.1.1.1:16384, Cisco
                                       				Unified Communications Manager listens to G.711 mu-law stream on
                                       				239.1.1.1:16384 and G.729 stream on 239.1.1.1:16388 (port value added with
                                       				four). An MOH server cannot transcode for G.729 codecs. Callers who are using
                                       				MOH G.729 codec require an external multicast RTP stream using G.729 or G.729a
                                       				codec.

## Music On Hold
                        	 Prerequisites

Before you configure multicast, ensure that you configure MOH
                                    				server and audio sources. If you want to use fixed audio source, configure it
                                    				before you configure multicast.

Make sure to decide whether you are going to do unicast or multicast Music On Hold

It is crucial to plan the capacity of the deployed and configured hardware and ensure that it can support the anticipated
                                    call volume of the network. You need to know the hardware capacity for MOH resources and consider the implications of multicast
                                    and unicast MOH in relation to this capacity. Ensure that network call volumes do not exceed these limits. When MOH sessions
                                    reach these limits, an additional load can result in poor MOH quality, erratic MOH operation, or loss of MOH functionality.

If you use multicast MOH and the devices that listen to multicast MOH streams are not in the same IP network, you must enable
                                    multicast routing in the IP network. Take care when you enable the multicast routing to avoid the potential flooding of parts
                                    of the network with wrongly sent multicast packets (specially, across WAN links). Disable multicasts on interfaces on which
                                    the multicast MOH packets are not required and use the Max Hops parameter.

For detailed information on planning your Music On Hold deployment, including server capacities, refer to the Music On Hold
                                    capacities topics in the Cisco Collaboration System  Solution Reference Network Design .

## Music On Hold Configuration Task Flow

Step 1

Activate Cisco IP Voice Media Streaming

Activate the Cisco IP Voice Media Streaming Service Application service to enable Music On Hold.

Step 2

Configure Music On Hold Server

Configure basic server settings for the MOH server.

Step 3

Upload Audio File for Music On Hold

Optional. Upload your own audio files to make them available as MOH audio streams.

Step 4

Configure Music On Hold Audio Source

Configure Music On Hold audio streams. You can also associate an uploaded audio files to an MOH audio stream.

Step 5

Configure Fixed Music On Hold Audio Source

Configure the fixed Music On Hold audio source. The system supports a single fixed MOH audio source (stream 51).

Step 6

Add MOH to Media Resource Group

Assign the Music On Hold service to a Media Resource Group. The group compiles the media resources that are available to an
                                          endpoint in a call.

Step 7

Configure Media Resource Group List

Assign your Media Resouce Groups to a prioritized Media Resource Group List.

Step 8

Add Media Resources to Device Pool

Make Music On Hold available to endpoints by assigning the Media Resource Group List to a device or device pool.

Step 9

Configure MOH Service Parameters

Optional. Configure optional Music On Hold parameters such as default codecs and default audio streams for calls on hold.

### Activate Cisco IP Voice Media Streaming

The Cisco IP Voice Media Streaming Application service must be Activated in order to use Music On Hold.

During installation, Unified Communications Manager installs and configures a default Music On Hold audio source. Music On Hold functionality can proceed by using the default
                                             audio source.

Step 1

From Cisco Unified CM Administration, choose Tools > Service Activation .

Step 2

Choose a server from the Server drop-down list.

Step 3

Under CM Services , make sure the Cisco IP Voice Media Streaming App service is Activated . If the service is deactivated, check the service and click Save .

### Configure Music On
                           	 Hold Server

#### Before you begin

The Cisco Unified Communications Manager MOH server is automatically added when the Cisco IP Voice Media Streaming Application service is activated.

Step 1

From Cisco Unified CM Administration, choose Media Resources > Music On Hold Server .

Step 2

Click Find and select the Music On Hold server that you want to update.

Step 3

Select the Host Server .

Step 4

Enter a descriptive Music On Hold Server Name along with a Description .

Step 5

Select the Device Pool you want to use for this server.

Step 6

Configure server capacity by configuring the following fields:

- Maximum Multi-cast Connections —Set this to a value that is greater than or equal to the number of devices that might be placed on multicast MOH at any given
                                             time.

Step 7

(Optional) To enable multi-casting, check the Enable Multi-cast Audio Sources on this MOH Server check box, and configure the multicast IP address ranges.

Step 8

Configure the additional fields in the Music On Hold Server Configuration window. For help with the fields and their settings, see the online help.

Step 9

Click Save .

### Upload Audio File for Music On Hold

Step 1

From Cisco Unified CM Administration, choose Media Resources > MOH Audio File Management .

Step 2

Click Upload
                                             				File .

Step 3

Click Choose File and browse to the file you want to upload. Once you've selected the file, click Open .

Step 4

Click Upload .

The Upload Result window shows the result of the upload. The uploading procedure uploads the file and performs audio conversions to create
                                             codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes to complete.

Step 5

Click Close to close the Upload Result window.

Step 6

Repeat this procedure if you want to upload additional audio files.

When you import an audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by the Music On Hold server. Following are examples
                                                         of valid input audio source files:

16-bit PCM .wav file

Stereo or mono

Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz

MOH audio source files do not automatically propagate to other MOH servers in a cluster. You must upload an audio source file
                                                         to each MOH server or each server in a cluster separately

### Configure Music On Hold Audio Source

Use this procedure to configure Music On Hold audio sources. You can configure audio streams and associate uploaded files
                                 to an audio stream. You can configure up to 500 audio streams.

If a new version
                                             			 of an audio source file is available, perform the update procedure to use the
                                             			 new version.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Music On Hold Audio Source .

Step 2

Do either of the following:

- Click Find and select an existing audio stream.

- Click Add New to configure a new stream.

Step 3

From the MOH Audio Stream Number , select an audio stream.

Step 4

Enter a unique name in the MOH Audio Source Name field.

Step 5

Optional. Check the Allow Multi-casting check box if you want to allow this file to be multi-casted.

Step 6

Configure the audio source:

- Check the Use MOH WAV file source radio button and from the MOH Audio Source File , select the file you want to assign.

- Check the Rebroadcast External Multicast Source radio button and enter the multicast source IP Address details.

Step 7

In the Announcement Settings for Held and Hunt Pilot Calls section, assign the announcements that you want to use for this audio source.

Step 8

Configure the remaining fields in the Music On Hold Audio Source Configuration window. For help with the fields and their settings, see the online help.

Step 9

Click Save .

### Configure Fixed
                           	 Music On Hold Audio Source

Step 1

From Cisco Unified CM Administration, choose Media Resources > Fixed MOH Audio Source .

Step 2

Optional. Check the Allow Multi-casting check box if you want to allow this audio source to be multi-casted.

Step 3

Check the Enable check box to enable the fixed audio source. When you check this check box, a Name is required.

Step 4

In the Announcement Settings for Held and Hunt Pilot Calls area, configure announcements for this audio source.

Step 5

Configure the fields in the Fixed MOH Audio Source Configuration window. For help with the fields and their settings, see the online help.

Step 6

Click Save .

### Add MOH to Media Resource Group

Step 1

From Cisco Unified CM Administration, choose Media Resources > Media Resource Group .

Step 2

Do either of the following:

- Click Find and select an existing group.

- Click Add New to create a new group.

Step 3

Enter a Name and Description .

Step 4

In the Available Media Resources list, select the Music On Hold resource and use the down arrow to add the resource to the Selected Media Resources . Repeat this step for the other media resources you want to assign to this group.

Step 5

(Optional) Check the Use Multi-cast for MOH Audio check box if you want to allow Music On Hold multi-casting.

Step 6

Click Save .

### Configure Media
                           	 Resource Group List

Media Resource
                                 		  Group List lists the  prioritized media resource groups. An
                                 		  application can select required media resources from among ones that are
                                 		  available according to the priority order that is defined in a media resource
                                 		  group list.

Step 1

From Cisco Unified CM Administration, choose Media Resources > Media Resource Group List .

Step 2

Do either of the following:

- Click Find and select an existing media resource group list.

- Click Add New to create a new media resource group list.

Step 3

Enter a Name for the list.

Step 4

From the Available Media Resource Groups list, select the groups you want to add to this list and use the down arrow to move them to Selected Media Resource Groups .

Step 5

In the Selected Media Resource Groups list use the up and down arrows to the right of the list to edit the prioritized order of groups.

Step 6

Click Save .

### Add Media Resources to Device Pool

The device in a call will use the media resource group list that is assigned to the device in the Phone Configuration window. If none is assigned, it will use the media resource group list for the device pool that is used for the call.

Step 1

From Cisco Unified CM Administration, do either of the following:

- Choose System > Device Pool .

- Choose Device > Phone .

Step 2

Click Find and select an existing phone or an existing device pool.

Step 3

From the Media Resource Group List drop-down list, select the media resource group list that contains the Music On Hold resource.

Step 4

Complete the remaining fields in the configuration window. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

### Configure MOH Service Parameters

Step 1

In Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters .

Step 2

From the Server drop-down list, select the server.

Step 3

From the Service drop-down list, select Cisco IP Voice Media Streaming .

Step 4

From the Clusterwide Parameters (Parameters that apply to all servers) area, configure optional MOH service parameters.

Step 5

Click Save .

Step 6

From the Service drop-down list, select Cisco CallManager .

Step 7

Configure optional MOH parameters. For example,  under Clusterwide Parameters (Service) , you can assign the default audio sources for Hold.

Step 8

Click Save .

All parameters apply only to the current server except parameters that are in the cluster-wide group.

### View Music on Hold
                           	 Audio File

View existing Music On Hold audio files that are stored on the system.

Step 1

In Cisco Unified CM
                                             				Administration , choose Media
                                                				  Resources > MOH Audio File Management .

Step 2

View the
                                          			 following information for each record:

Check box —If
                                                   					 the audio file can be deleted, a check box appears before the File Name column.

File Name —This column displays the audio file name.

Length —This
                                                   					 column displays the audio file length in minutes and seconds.

File Status —This column displays one of the following statuses of an audio file:

Translation Complete —This status appears after a
                                                         						  file is uploaded successfully and is available for use as audio files for a
                                                         						  music on hold audio source.

In Use —This status appears after you add a Music
                                                         						  On Hold audio source that uses this audio file as its MOH audio source file.

You
                                                                     							 cannot a delete a file with In Use status.

## Unicast and
                        	 Multicast Audio Sources

Unicast Music On
                              		  Hold is the system default option. However, you need to configure for
                              		  multicast, if required. Both multicast and unicast configurations present the
                              		  same audio-source behavior to held parties. Each audio source is used once,
                              		  and the stream is split internally and is sent to the held parties. The
                              		  only difference between multicast and unicast, in this case, is how the data is sent over the network.

Unicast
                                          					 Audio Source

Multicast
                                          					 Audio Source

Consists
                                          					 of streams that are sent directly from the MOH server to the endpoint that
                                          					 requests an MOH audio stream.

Consists
                                          					 of streams that are sent from the MOH server to a multicast group IP address.
                                          					 Endpoints that request an MOH audio stream can join multicast MOH, as needed.

A unicast
                                          					 MOH stream is a point-to-point, one-way audio RTP stream between the server and
                                          					 the endpoint device.

A
                                          					 multicast MOH stream is a point-to-multipoint, one-way audio RTP stream between
                                          					 the MOH server and the multicast group IP address.

Unicast
                                          					 MOH uses a separate source stream for each user or connection. As more endpoint
                                          					 devices go on hold through a user or network event, the number of MOH streams
                                          					 increases.

Enables
                                          					 multiple users to use the same audio source stream to provide MOH.

An MOH
                                          					 audio source may be configured with an initial (greeting) announcement, which
                                          					 will be played to unicast held parties. For unicast MOH users, this
                                          					 announcement is heard from the beginning.

For
                                          					 multicast users, this announcement is not heard.

The
                                          					 additional MOH streams can have a negative effect on network throughput and
                                          					 bandwidth.

Multicast
                                          					 MOH conserves system resources and bandwidth.

Extremely
                                          					 useful in networks in which multicast is not enabled or devices are incapable
                                          					 of multicast.

Can be
                                          					 problematic in situations in which a network is not enabled for multicast or
                                          					 the endpoint devices are incapable of processing multicast.

Includes
                                          					 managing devices only.

Includes
                                          					 managing devices, IP addresses, and ports.

No
                                          					 requirement to define the Music On Hold server.

Administrators must define at least one audio source to allow
                                          					 multicasting. To define Music On Hold servers for multicast, first define the
                                          					 server to allow multicasting.

Functions
                                          					 without configuring MOH audio source, MOH server, or media resource group list.

Functions
                                          					 only if both media resource groups and media resource group lists are defined
                                          					 to include a multicast Music On Hold server. For media resource groups, you
                                          					 must include a Music On Hold server that is set up for multicast. These servers
                                          					 are labeled as (MOH) [Multicast]. Also, check the Use Multicast for MOH Audio check box when you define a media resource group for multicast.

The
                                          			 Multicast MOH Direction Attribute for SIP service parameter determines whether Cisco Unified
                                             				Communications Manager sets the direction attribute of the Session
                                          			 Description Protocol (SDP) in its multicast Music On Hold (MOH) INVITE message
                                          			 to sendOnly or recvOnly.

If
                                          			 your deployment uses SIP phone uses Release 8.4 and earlier for Cisco Unified IP
                                             				Phone s 7940 and 7960, or SIP phone uses Release 8.1(x) and earlier for Cisco Unified IP
                                             				Phone s 7906, 7911, 7941, and 7961 , set this parameter to sendOnly . Otherwise, leave this parameter set to the
                                          			 default value, recvOnly .

## Music On Hold
                        	 Interactions

Feature

Interaction

Multicast Music On Hold over H.323 Intercluster Trunks

Using the multicast MOH over H.323 intercluster
                                          						trunk feature, you can multicast MOH to work over H.323 intercluster trunks
                                          						(ICT). When a call connects over an intercluster trunk and one of the parties
                                          						presses the Hold key, MOH streams over the intercluster trunk. If you have
                                          						turned on the multicast MOH and have configured the holding party and trunk to
                                          						use the multicast MOH server, MOH streams with multicast. Only one multicast
                                          						MOH stream streams over the trunk regardless of the number of calls that are
                                          						put on hold on this trunk.

Additional points regarding this feature:

This feature does not work if any middle box between Cisco Unified Communications Managers does not pass the new fields in
                                                Terminal Capability Set (TCS) and OLC message.

This feature requires no additional configuration for field up multicast MOH, and applies only between Cisco Unified Communications
                                                Managers that support single-transmitter multicast.

The feature is On by default, but can be turned off by setting the Send Multicast MOH in H.245 OLC Message service parameter to False . Setting this value can resolve interoperability issues that the feature might cause.

Music On Hold Failover and Fallback

The MOH server supports Cisco Unified
                                             						  Communications Manager lists and failover as implemented by the
                                          						software conference bridge and media termination point. Upon failover, the
                                          						system maintains connections to a backup Cisco Unified
                                             						  Communications Manager , if available.

When a Music On Hold server fails during an active
                                          						Music On Hold session, the held party hears no music from this point.
                                          						However, this situation does not affect normal call functions.

Call Park and Directed Call Park

Music On Hold allows users to place calls on hold with music that a streaming source provides. Music On Hold allows two types
                                          of hold:

User hold—The system invokes this type of hold when a user presses the Hold button or Hold softkey.

Network hold—This type of hold takes place when a user activates the Transfer, Conference, or Call Park feature, and the hold
                                                automatically gets invoked. This hold type applies to directed call park because directed call park is a transfer function.
                                                However, Directed Call Park uses the Cisco Call Manager service parameter, Default Network Hold MOH Audio Source, for the
                                                audio source.

Extension Mobility Cross Cluster—Media resources for the visiting phone

Examples include RSVP Agent, TRP, Music On Hold (MOH), MTP, transcoder,
                                          					 and conference bridge.

Media resources are local to the visiting phone (other than RSVP
                                          				  Agents).

Hold Reversion

Cisco
                                          					 Unified Communications Manager supports MOH on a reverted call if MOH is
                                          					 configured for a normal held call.

Media Resource Selection

Held parties determine the media resource group list that a Cisco Unified Communications Manager uses to allocate a Music
                                          On Hold resource.

Secured Music On Hold with SRTP

Cisco Unified Communications Manager enhances the Cisco IP Voice Media Streaming application service to support Secure Real-Time
                                          Protocol (SRTP). Hence, when you enable the Cisco Unified Communications Manager cluster or system for security, the MOH server
                                          registers with Cisco Unified Communications Manager as an SRTP capable device. If the receiving device is also SRTP-capable,
                                          the music media is encrypted before streaming to the receiving device.

Make sure of the following:

Cluster security should be mixed mode—Run the utils ctl set-cluster mixed-mode CLI command

SIP trunks in the path support SRTP—The SRTP Allowed check box must be checked in the Trunk Configuration window for SRTP to work over the trunk.

Devices support SRTP—In the Phone Security Profile used by the endpoint, the Device Security Mode must be Encrypted .

## Music On Hold Restrictions

Restriction

Description

Multicast Music On Hold Support

Computer Telephony Integration (CTI) and media termination point (MTP) devices do not support the multicast Music On Hold
                                          feature. If you configure  CTI or MTP devices with a multicast MoH device in the media resource group list of the CTI device,
                                          call control issues may result. CTI and MTP devices do not support multicast media streaming.

Internet Protocol Support

Multicast Music On Hold supports only IPv4. The Cisco IP Voice Media Streaming Application, which is a
                                          component of Music On Hold, supports both IPv4 and IPv6 audio media
                                          connections for unicast Music On Hold. Multicast Music On Hold
                                          supports IPv4 only. Devices with an IP addressing mode of IPv6
                                          only cannot support multicast.

Distribution of fixed-device audio sources

Cisco Unified Communications Manager does not support distribution of fixed-device (hardware) audio sources across Music On
                                          Hold servers within a media resource group.

Unacceptable Audio Quality with G.729a codec

Because the G.729a codec is designed for human speech, if you use it with Music On Hold for music, it  may not provide acceptable
                                          audio quality.

Cisco Unified Communications Manager System Support

A Cisco Unified Communications Manager cluster or system supports only virtualized deployments on Cisco Unified Computing
                                          System (UCS) servers or other Cisco-approved third-party server configurations. You cannot use the Music On Hold feature with
                                          an external source (USB audio dongle) for the nodes that provide MOH from an external source.

Multicast Support

The administrator can designate a Music On Hold server as either unicast or multicast, provided that resources exist to support
                                          multicast.

Caller-specific MOH Support

Caller-specific MOH is not supported when calls are received or transferred over QSIG tunneling-enabled SIP trunks.

MP3 Format Support

The Music On Hold feature does not support the MP3 format.

Interoperability between H.323 and SIP Protocols

Multicast MOH does not support interoperability between H.323 and SIP protocols.

SRTP Support

Multicast MoH audio streams are not encrypted and do not support SRTP.

Multicast Streams

MTPs do not support multicast streams.

Encryption of Multicast Music On Hold RTP Streams

Cisco Unified Communications Manager does not support encryption of multicast Music On Hold RTP streams. For secure MOH audio,
                                          you should not configure multicast audio sources.

Fixed Music On Hold Device

The fixed Music On Hold device cannot specify an audio source that connects through a USB, because Cisco Unified Communications
                                          Manager does not support USB when running on VMware. However, VMware supports internal Music On Hold.

MOH Server Failure

Cisco Unified Communications Manager takes no action when a Music On Hold server fails during an active Music On Hold session.

Multicast MOH

When an MTP resource gets invoked in a call leg at a site that is using multicast MOH, Cisco Unified Communications Manager
                                          falls back to unicast MOH instead of multicast MOH.

Provisioning

If you do not provision  the user and network MOH audio source identifiers, or if one or both values are invalid, the caller-specific
                                          MOH information in the SIP header is ignored.  The call reverts to
                                          tone on hold and an invalid MOH audio source alarm is raised.

Header Values

When both the  user and network MOH audio source identifiers are present in the header, any invalid value is replaced by the
                                                default value (0).

If both values are zero, or the only value is zero, the header in the incoming INVITE is ignored.

MOH Audio Source Identifier

If you provide only one MOH audio source identifier in the SIP header, including if a comma appears before or after the MOH
                                                audio source identifier value, the same MOH ID is used for both user and network MOH. The SIP trunk populates both the user
                                                and the network MOH audio source identifiers in the SIP header so that  Call Control always receive both values.

If there are more than two MOH audio source identifier values separated by a comma in the header, then the first two values
                                                are used. Subsequent values are ignored.

Administrators for Consistent Caller-specific MOH Configurations

Administrators are responsible to
                                          maintain consistent caller-specific MOH configurations when multiple Cisco Unified Communications Manager clusters
                                          are involved.

Original Incoming Caller

The original incoming caller to the
                                          call center cannot change during the course of the entire
                                          call.

MOH Information

The Music On Hold information is shared only across SIP trunks.

## Music On Hold Troubleshooting

### Music On Hold Does Not Play on Phone

Phone user cannot hear Music On Hold.

G.729a codec is used with MOH for music, which may not provide acceptable audio quality.

An MTP resource is invoked in a call leg at a site that is using multicast MoH.

When an MTP resource gets invoked in a call leg at a site that is using multicast MoH, the caller receives silence instead
                                       of Music On Hold. To avoid this scenario, configure unicast MoH or Tone on Hold instead of multicast MoH.

| Configuration Notes | CPU Performance |
|---|---|
| Dedicated MOH server, 1000 held calls, 500 MOH sources with greeting and periodic announcements. | 25–45% (7500 user OVA configuration) |
| Native call queuing with dedicated MOH server and annunciator server, 1000 queued calls, 500 MOH sources with greeting and
                                                periodic announcements. An annunciator can play up to 300 simultaneous greeting announcements. | 25–45% (7500 user OVA configuration) |
| Dedicated MOH server, 500 held calls, 500 MOH sources with greeting and periodic announcements. | 15–35% (7500 user OVA configuration) |

| Configuration | Recommendation Limit |
|---|---|
| When  Cisco IP Voice Media Streaming application is co-resident with Cisco Unified  Communications Manager on 2500 OVA (moderate
                                                call processing). | MOH: 500 held callers, 100 MOH sources, and 48 to 64 annunciator callers. |
| When  Cisco IP Voice Media Streaming application is a dedicated server on 2500 OVA. | MOH: 750 held callers, 250 MOH sources, and 250 annunciator callers. |
| When Cisco IP Voice Media Streaming application is co-resident with Cisco Unified  Communications Manager on 7500/10K OVA
                                                (moderate call processing). | MOH: 500 held callers, 250 MOH sources, and 128 annunciator callers. |
| When  Cisco IP Voice Media Streaming application is a  dedicated server on 7500/10K OVA. | MOH: 1000 held callers, 500 MOH sources, and 300-700 annunciator callers  (with 1 MOH codec). Note Reduce annunciator to 300 for two MOH codecs. | Note | Reduce annunciator to 300 for two MOH codecs. |
| Note | Reduce annunciator to 300 for two MOH codecs. |

| Note | Reduce annunciator to 300 for two MOH codecs. |
|---|---|

| Note | These recommendations are specific to MOH/ANN devices. If you combine these devices  with the software media termination
                                                point (MTP) and call forward busy (CFB) devices, reduce the limits to provide streams. |
|---|---|

| Media Device | Capacity |
|---|---|
| Annunciator | (Call Count service parameter) * 3 Where 3 indicates total of receiving (RX) and transmitting (TX) calls for endpoint and 1 for .wav file. |
| Software Conference Bridge | (Call Count service parameter) * 2 Where 2 indicates total streams of RX and TX endpoints. |
| Software Media Termination Point | (Call Count service parameter) * 2 Where 2 indicates total streams of RX and TX endpoints. |
| Music On Hold | ((Maximum Half Duplex Streams) * 3) + (501 * 2 * [number of enabled
                                                MOH codecs]) Where: (Maximum Half Duplex Streams) is a configuration setting on the MOH
                                                         device configuration administration web page. 3 indicates total steams of RX, TX, and greeting announcement .wav
                                                         file. 501 indicates the maximum number of Music On Hold (MOH) sources. 2 indicates music .wav stream and possible multicast TX stream. [number of enabled MOH codecs] is based on how many MOH
                                                         codecs are enabled in the Cisco IP Voice Media Streaming application
                                                         service parameters. |
| Self Provisioning IVR Service | (500 * 2) Where 500 indicates callers, and 2 indicates total streams from RX and TX
                                                streams. |

| Note | A media kernel driver with a 	capacity of 6000 streams might not support that many simultaneous media device connections. |
|---|---|

| Note | This feature has no impact on existing functionality of playing
                                                				  multicast MOH audio using an external audio source for the devices that are
                                                				  capable of multicast reception. For the unicast media connection, Cisco Unified Communications
                                                				  Manager MOH Server plays the initial announcement and periodic announcement
                                                				  even if you configure the MOH audio source with external multicast source. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Cisco IP Voice Media Streaming | Activate the Cisco IP Voice Media Streaming Service Application service to enable Music On Hold. |
| Step 2 | Configure Music On Hold Server | Configure basic server settings for the MOH server. |
| Step 3 | Upload Audio File for Music On Hold | Optional. Upload your own audio files to make them available as MOH audio streams. |
| Step 4 | Configure Music On Hold Audio Source | Configure Music On Hold audio streams. You can also associate an uploaded audio files to an MOH audio stream. |
| Step 5 | Configure Fixed Music On Hold Audio Source | Configure the fixed Music On Hold audio source. The system supports a single fixed MOH audio source (stream 51). |
| Step 6 | Add MOH to Media Resource Group | Assign the Music On Hold service to a Media Resource Group. The group compiles the media resources that are available to an
                                          endpoint in a call. |
| Step 7 | Configure Media Resource Group List | Assign your Media Resouce Groups to a prioritized Media Resource Group List. |
| Step 8 | Add Media Resources to Device Pool | Make Music On Hold available to endpoints by assigning the Media Resource Group List to a device or device pool. |
| Step 9 | Configure MOH Service Parameters | Optional. Configure optional Music On Hold parameters such as default codecs and default audio streams for calls on hold. |

| Note | During installation, Unified Communications Manager installs and configures a default Music On Hold audio source. Music On Hold functionality can proceed by using the default
                                             audio source. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Tools > Service Activation . |
|---|---|
| Step 2 | Choose a server from the Server drop-down list. |
| Step 3 | Under CM Services , make sure the Cisco IP Voice Media Streaming App service is Activated . If the service is deactivated, check the service and click Save . |

| Note | The Cisco Unified Communications Manager MOH server is automatically added when the Cisco IP Voice Media Streaming Application service is activated. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Music On Hold Server . |
|---|---|
| Step 2 | Click Find and select the Music On Hold server that you want to update. |
| Step 3 | Select the Host Server . |
| Step 4 | Enter a descriptive Music On Hold Server Name along with a Description . |
| Step 5 | Select the Device Pool you want to use for this server. |
| Step 6 | Configure server capacity by configuring the following fields: Maximum Half Duplex Stream —Set this to the maximum number of devices that can be on unicast music on hold that is streamed from this music on hold server
                                             at any given time. You can use the following formula to calculate the maximum: Note (Server and deployment capacity) – ([Number of multicast MOH sources] * [Number of enabled MOH codecs]) Maximum Multi-cast Connections —Set this to a value that is greater than or equal to the number of devices that might be placed on multicast MOH at any given
                                             time. | Note | (Server and deployment capacity) – ([Number of multicast MOH sources] * [Number of enabled MOH codecs]) |
| Note | (Server and deployment capacity) – ([Number of multicast MOH sources] * [Number of enabled MOH codecs]) |
| Step 7 | (Optional) To enable multi-casting, check the Enable Multi-cast Audio Sources on this MOH Server check box, and configure the multicast IP address ranges. |
| Step 8 | Configure the additional fields in the Music On Hold Server Configuration window. For help with the fields and their settings, see the online help. |
| Step 9 | Click Save . |

| Note | (Server and deployment capacity) – ([Number of multicast MOH sources] * [Number of enabled MOH codecs]) |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > MOH Audio File Management . |
|---|---|
| Step 2 | Click Upload
                                             				File . |
| Step 3 | Click Choose File and browse to the file you want to upload. Once you've selected the file, click Open . |
| Step 4 | Click Upload . The Upload Result window shows the result of the upload. The uploading procedure uploads the file and performs audio conversions to create
                                             codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes to complete. |
| Step 5 | Click Close to close the Upload Result window. |
| Step 6 | Repeat this procedure if you want to upload additional audio files. Note When you import an audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by the Music On Hold server. Following are examples
                                                         of valid input audio source files: 16-bit PCM .wav file Stereo or mono Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz Note MOH audio source files do not automatically propagate to other MOH servers in a cluster. You must upload an audio source file
                                                         to each MOH server or each server in a cluster separately | Note | When you import an audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by the Music On Hold server. Following are examples
                                                         of valid input audio source files: 16-bit PCM .wav file Stereo or mono Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz | Note | MOH audio source files do not automatically propagate to other MOH servers in a cluster. You must upload an audio source file
                                                         to each MOH server or each server in a cluster separately |
| Note | When you import an audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by the Music On Hold server. Following are examples
                                                         of valid input audio source files: 16-bit PCM .wav file Stereo or mono Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz |
| Note | MOH audio source files do not automatically propagate to other MOH servers in a cluster. You must upload an audio source file
                                                         to each MOH server or each server in a cluster separately |

| Note | When you import an audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by the Music On Hold server. Following are examples
                                                         of valid input audio source files: 16-bit PCM .wav file Stereo or mono Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz |
|---|---|

| Note | MOH audio source files do not automatically propagate to other MOH servers in a cluster. You must upload an audio source file
                                                         to each MOH server or each server in a cluster separately |
|---|---|

| Note | If a new version
                                             			 of an audio source file is available, perform the update procedure to use the
                                             			 new version. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Music On Hold Audio Source . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing audio stream. Click Add New to configure a new stream. |
| Step 3 | From the MOH Audio Stream Number , select an audio stream. |
| Step 4 | Enter a unique name in the MOH Audio Source Name field. |
| Step 5 | Optional. Check the Allow Multi-casting check box if you want to allow this file to be multi-casted. |
| Step 6 | Configure the audio source: Check the Use MOH WAV file source radio button and from the MOH Audio Source File , select the file you want to assign. Check the Rebroadcast External Multicast Source radio button and enter the multicast source IP Address details. |
| Step 7 | In the Announcement Settings for Held and Hunt Pilot Calls section, assign the announcements that you want to use for this audio source. |
| Step 8 | Configure the remaining fields in the Music On Hold Audio Source Configuration window. For help with the fields and their settings, see the online help. |
| Step 9 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Fixed MOH Audio Source . |
|---|---|
| Step 2 | Optional. Check the Allow Multi-casting check box if you want to allow this audio source to be multi-casted. |
| Step 3 | Check the Enable check box to enable the fixed audio source. When you check this check box, a Name is required. |
| Step 4 | In the Announcement Settings for Held and Hunt Pilot Calls area, configure announcements for this audio source. |
| Step 5 | Configure the fields in the Fixed MOH Audio Source Configuration window. For help with the fields and their settings, see the online help. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Media Resource Group . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing group. Click Add New to create a new group. |
| Step 3 | Enter a Name and Description . |
| Step 4 | In the Available Media Resources list, select the Music On Hold resource and use the down arrow to add the resource to the Selected Media Resources . Repeat this step for the other media resources you want to assign to this group. |
| Step 5 | (Optional) Check the Use Multi-cast for MOH Audio check box if you want to allow Music On Hold multi-casting. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Media Resource Group List . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing media resource group list. Click Add New to create a new media resource group list. |
| Step 3 | Enter a Name for the list. |
| Step 4 | From the Available Media Resource Groups list, select the groups you want to add to this list and use the down arrow to move them to Selected Media Resource Groups . |
| Step 5 | In the Selected Media Resource Groups list use the up and down arrows to the right of the list to edit the prioritized order of groups. |
| Step 6 | Click Save . |

| Note | The device in a call will use the media resource group list that is assigned to the device in the Phone Configuration window. If none is assigned, it will use the media resource group list for the device pool that is used for the call. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, do either of the following: Choose System > Device Pool . Choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select an existing phone or an existing device pool. |
| Step 3 | From the Media Resource Group List drop-down list, select the media resource group list that contains the Music On Hold resource. |
| Step 4 | Complete the remaining fields in the configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, select the server. |
| Step 3 | From the Service drop-down list, select Cisco IP Voice Media Streaming . |
| Step 4 | From the Clusterwide Parameters (Parameters that apply to all servers) area, configure optional MOH service parameters. |
| Step 5 | Click Save . |
| Step 6 | From the Service drop-down list, select Cisco CallManager . |
| Step 7 | Configure optional MOH parameters. For example,  under Clusterwide Parameters (Service) , you can assign the default audio sources for Hold. |
| Step 8 | Click Save . Note All parameters apply only to the current server except parameters that are in the cluster-wide group. | Note | All parameters apply only to the current server except parameters that are in the cluster-wide group. |
| Note | All parameters apply only to the current server except parameters that are in the cluster-wide group. |

| Note | All parameters apply only to the current server except parameters that are in the cluster-wide group. |
|---|---|

| Step 1 | In Cisco Unified CM
                                             				Administration , choose Media
                                                				  Resources > MOH Audio File Management . The Music
                                             				On Hold Audio File Management window appears. |
|---|---|
| Step 2 | View the
                                          			 following information for each record: Check box —If
                                                   					 the audio file can be deleted, a check box appears before the File Name column. File Name —This column displays the audio file name. Length —This
                                                   					 column displays the audio file length in minutes and seconds. File Status —This column displays one of the following statuses of an audio file: Translation Complete —This status appears after a
                                                         						  file is uploaded successfully and is available for use as audio files for a
                                                         						  music on hold audio source. In Use —This status appears after you add a Music
                                                         						  On Hold audio source that uses this audio file as its MOH audio source file. Note You
                                                                     							 cannot a delete a file with In Use status. | Note | You
                                                                     							 cannot a delete a file with In Use status. |
| Note | You
                                                                     							 cannot a delete a file with In Use status. |

| Note | You
                                                                     							 cannot a delete a file with In Use status. |
|---|---|

| Unicast
                                          					 Audio Source | Multicast
                                          					 Audio Source |
|---|---|
| Consists
                                          					 of streams that are sent directly from the MOH server to the endpoint that
                                          					 requests an MOH audio stream. | Consists
                                          					 of streams that are sent from the MOH server to a multicast group IP address.
                                          					 Endpoints that request an MOH audio stream can join multicast MOH, as needed. |
| A unicast
                                          					 MOH stream is a point-to-point, one-way audio RTP stream between the server and
                                          					 the endpoint device. | A
                                          					 multicast MOH stream is a point-to-multipoint, one-way audio RTP stream between
                                          					 the MOH server and the multicast group IP address. |
| Unicast
                                          					 MOH uses a separate source stream for each user or connection. As more endpoint
                                          					 devices go on hold through a user or network event, the number of MOH streams
                                          					 increases. | Enables
                                          					 multiple users to use the same audio source stream to provide MOH. |
| An MOH
                                          					 audio source may be configured with an initial (greeting) announcement, which
                                          					 will be played to unicast held parties. For unicast MOH users, this
                                          					 announcement is heard from the beginning. | For
                                          					 multicast users, this announcement is not heard. |
| The
                                          					 additional MOH streams can have a negative effect on network throughput and
                                          					 bandwidth. | Multicast
                                          					 MOH conserves system resources and bandwidth. |
| Extremely
                                          					 useful in networks in which multicast is not enabled or devices are incapable
                                          					 of multicast. | Can be
                                          					 problematic in situations in which a network is not enabled for multicast or
                                          					 the endpoint devices are incapable of processing multicast. |
| Includes
                                          					 managing devices only. | Includes
                                          					 managing devices, IP addresses, and ports. |
| No
                                          					 requirement to define the Music On Hold server. | Administrators must define at least one audio source to allow
                                          					 multicasting. To define Music On Hold servers for multicast, first define the
                                          					 server to allow multicasting. |
| Functions
                                          					 without configuring MOH audio source, MOH server, or media resource group list. | Functions
                                          					 only if both media resource groups and media resource group lists are defined
                                          					 to include a multicast Music On Hold server. For media resource groups, you
                                          					 must include a Music On Hold server that is set up for multicast. These servers
                                          					 are labeled as (MOH) [Multicast]. Also, check the Use Multicast for MOH Audio check box when you define a media resource group for multicast. |

| Note | The
                                          			 Multicast MOH Direction Attribute for SIP service parameter determines whether Cisco Unified
                                             				Communications Manager sets the direction attribute of the Session
                                          			 Description Protocol (SDP) in its multicast Music On Hold (MOH) INVITE message
                                          			 to sendOnly or recvOnly. If
                                          			 your deployment uses SIP phone uses Release 8.4 and earlier for Cisco Unified IP
                                             				Phone s 7940 and 7960, or SIP phone uses Release 8.1(x) and earlier for Cisco Unified IP
                                             				Phone s 7906, 7911, 7941, and 7961 , set this parameter to sendOnly . Otherwise, leave this parameter set to the
                                          			 default value, recvOnly . |
|---|---|

| Feature | Interaction |
|---|---|
| Multicast Music On Hold over H.323 Intercluster Trunks | Using the multicast MOH over H.323 intercluster
                                          						trunk feature, you can multicast MOH to work over H.323 intercluster trunks
                                          						(ICT). When a call connects over an intercluster trunk and one of the parties
                                          						presses the Hold key, MOH streams over the intercluster trunk. If you have
                                          						turned on the multicast MOH and have configured the holding party and trunk to
                                          						use the multicast MOH server, MOH streams with multicast. Only one multicast
                                          						MOH stream streams over the trunk regardless of the number of calls that are
                                          						put on hold on this trunk. Additional points regarding this feature: This feature does not work if any middle box between Cisco Unified Communications Managers does not pass the new fields in
                                                Terminal Capability Set (TCS) and OLC message. This feature requires no additional configuration for field up multicast MOH, and applies only between Cisco Unified Communications
                                                Managers that support single-transmitter multicast. The feature is On by default, but can be turned off by setting the Send Multicast MOH in H.245 OLC Message service parameter to False . Setting this value can resolve interoperability issues that the feature might cause. |
| Music On Hold Failover and Fallback | The MOH server supports Cisco Unified
                                             						  Communications Manager lists and failover as implemented by the
                                          						software conference bridge and media termination point. Upon failover, the
                                          						system maintains connections to a backup Cisco Unified
                                             						  Communications Manager , if available. When a Music On Hold server fails during an active
                                          						Music On Hold session, the held party hears no music from this point.
                                          						However, this situation does not affect normal call functions. |
| Call Park and Directed Call Park | Music On Hold allows users to place calls on hold with music that a streaming source provides. Music On Hold allows two types
                                          of hold: User hold—The system invokes this type of hold when a user presses the Hold button or Hold softkey. Network hold—This type of hold takes place when a user activates the Transfer, Conference, or Call Park feature, and the hold
                                                automatically gets invoked. This hold type applies to directed call park because directed call park is a transfer function.
                                                However, Directed Call Park uses the Cisco Call Manager service parameter, Default Network Hold MOH Audio Source, for the
                                                audio source. |
| Extension Mobility Cross Cluster—Media resources for the visiting phone | Examples include RSVP Agent, TRP, Music On Hold (MOH), MTP, transcoder,
                                          					 and conference bridge. Media resources are local to the visiting phone (other than RSVP
                                          				  Agents). |
| Hold Reversion | Cisco
                                          					 Unified Communications Manager supports MOH on a reverted call if MOH is
                                          					 configured for a normal held call. |
| Media Resource Selection | Held parties determine the media resource group list that a Cisco Unified Communications Manager uses to allocate a Music
                                          On Hold resource. |
| Secured Music On Hold with SRTP | Cisco Unified Communications Manager enhances the Cisco IP Voice Media Streaming application service to support Secure Real-Time
                                          Protocol (SRTP). Hence, when you enable the Cisco Unified Communications Manager cluster or system for security, the MOH server
                                          registers with Cisco Unified Communications Manager as an SRTP capable device. If the receiving device is also SRTP-capable,
                                          the music media is encrypted before streaming to the receiving device. Make sure of the following: Cluster security should be mixed mode—Run the utils ctl set-cluster mixed-mode CLI command SIP trunks in the path support SRTP—The SRTP Allowed check box must be checked in the Trunk Configuration window for SRTP to work over the trunk. Devices support SRTP—In the Phone Security Profile used by the endpoint, the Device Security Mode must be Encrypted . |

| Restriction | Description |
|---|---|
| Multicast Music On Hold Support | Computer Telephony Integration (CTI) and media termination point (MTP) devices do not support the multicast Music On Hold
                                          feature. If you configure  CTI or MTP devices with a multicast MoH device in the media resource group list of the CTI device,
                                          call control issues may result. CTI and MTP devices do not support multicast media streaming. |
| Internet Protocol Support | Multicast Music On Hold supports only IPv4. The Cisco IP Voice Media Streaming Application, which is a
                                          component of Music On Hold, supports both IPv4 and IPv6 audio media
                                          connections for unicast Music On Hold. Multicast Music On Hold
                                          supports IPv4 only. Devices with an IP addressing mode of IPv6
                                          only cannot support multicast. |
| Distribution of fixed-device audio sources | Cisco Unified Communications Manager does not support distribution of fixed-device (hardware) audio sources across Music On
                                          Hold servers within a media resource group. |
| Unacceptable Audio Quality with G.729a codec | Because the G.729a codec is designed for human speech, if you use it with Music On Hold for music, it  may not provide acceptable
                                          audio quality. |
| Cisco Unified Communications Manager System Support | A Cisco Unified Communications Manager cluster or system supports only virtualized deployments on Cisco Unified Computing
                                          System (UCS) servers or other Cisco-approved third-party server configurations. You cannot use the Music On Hold feature with
                                          an external source (USB audio dongle) for the nodes that provide MOH from an external source. |
| Multicast Support | The administrator can designate a Music On Hold server as either unicast or multicast, provided that resources exist to support
                                          multicast. |
| Caller-specific MOH Support | Caller-specific MOH is not supported when calls are received or transferred over QSIG tunneling-enabled SIP trunks. |
| MP3 Format Support | The Music On Hold feature does not support the MP3 format. |
| Interoperability between H.323 and SIP Protocols | Multicast MOH does not support interoperability between H.323 and SIP protocols. |
| SRTP Support | Multicast MoH audio streams are not encrypted and do not support SRTP. |
| Multicast Streams | MTPs do not support multicast streams. |
| Encryption of Multicast Music On Hold RTP Streams | Cisco Unified Communications Manager does not support encryption of multicast Music On Hold RTP streams. For secure MOH audio,
                                          you should not configure multicast audio sources. |
| Fixed Music On Hold Device | The fixed Music On Hold device cannot specify an audio source that connects through a USB, because Cisco Unified Communications
                                          Manager does not support USB when running on VMware. However, VMware supports internal Music On Hold. |
| MOH Server Failure | Cisco Unified Communications Manager takes no action when a Music On Hold server fails during an active Music On Hold session. |
| Multicast MOH | When an MTP resource gets invoked in a call leg at a site that is using multicast MOH, Cisco Unified Communications Manager
                                          falls back to unicast MOH instead of multicast MOH. |
| Provisioning | If you do not provision  the user and network MOH audio source identifiers, or if one or both values are invalid, the caller-specific
                                          MOH information in the SIP header is ignored.  The call reverts to
                                          tone on hold and an invalid MOH audio source alarm is raised. |
| Header Values | When both the  user and network MOH audio source identifiers are present in the header, any invalid value is replaced by the
                                                default value (0). If both values are zero, or the only value is zero, the header in the incoming INVITE is ignored. |
| MOH Audio Source Identifier | If you provide only one MOH audio source identifier in the SIP header, including if a comma appears before or after the MOH
                                                audio source identifier value, the same MOH ID is used for both user and network MOH. The SIP trunk populates both the user
                                                and the network MOH audio source identifiers in the SIP header so that  Call Control always receive both values. If there are more than two MOH audio source identifier values separated by a comma in the header, then the first two values
                                                are used. Subsequent values are ignored. |
| Administrators for Consistent Caller-specific MOH Configurations | Administrators are responsible to
                                          maintain consistent caller-specific MOH configurations when multiple Cisco Unified Communications Manager clusters
                                          are involved. |
| Original Incoming Caller | The original incoming caller to the
                                          call center cannot change during the course of the entire
                                          call. |
| MOH Information | The Music On Hold information is shared only across SIP trunks. |