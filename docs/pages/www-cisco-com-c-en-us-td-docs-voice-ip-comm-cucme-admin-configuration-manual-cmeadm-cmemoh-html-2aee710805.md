---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmemoh-html-2aee710805
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmemoh.html
retrieved_at: 2026-08-21T04:22:16.656309+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Music on Hold

## Chapter: Music on Hold

# Music on Hold

## Prerequisites for
                        	 Music on Hold

For Unified CME
                                 			 Release 11.6 and previous releases, phones receiving Music on Hold (MOH) in a
                                 			 system using G.729 require transcoding between G.711 and G.729. From Unified
                                 			 CME Release 11.7 onwards, transcoding is not required if G.729 codec format MOH
                                 			 file is configured on Unfiied CME. For information about transcoding, see Configure Transcoding Resources .

Transcoding for MOH is supported on Cisco 4000 Series Integrated
                                 			 Services Router from Unified CME Release 11.7 onwards.

## Restrictions for
                        	 Music on Hold

IP phones do not
                                    			 support multicast at 224.x.x.x addresses.

Cisco Unified
                                    			 CME 3.3 and earlier versions do not support MOH for local Cisco Unified CME
                                    			 phones that are on hold with other Cisco Unified CME phones; these parties hear
                                    			 a periodic repeating tone instead.

Cisco Unified CME 4.0 and later versions support MOH for
                                    			 internal calls on SCCP Phones only if the multicast moh command is used to enable the flow of packets to the subnet on which the phones
                                    			 are located.

Internal
                                    			 extensions that are connected through a Cisco VG224 Analog Voice Gateway or
                                    			 through a WAN (remote extensions) do not hear MOH on internal calls.

Multicast MOH is
                                    			 not supported on a phone if the phone is configured with the mtp command
                                    			 or the paging-dn command with the unicast keyword.

For calls from
                                    			 SCCP to SCCP phones, Unicast MoH is not supported. Multicast MoH is supported
                                    			 if it is enabled. If Multicast MoH is not enabled, Tone on Hold is supported.

Multicast MOH is
                                    			 not supported on SIP Phones.

Multicast MOH does not support co-location of tunnels on the same device.

### Restrictions
                              		  for Music on Hold from a Live Feed on Cisco 4000 Series Integrated Services
                              		  Routers

MOH from a
                                       				live feed supports only G.711 codec. Transcoding is required if the MOH
                                       				playback party is on a codec other than g711ulaw or g711alaw.

E&M is not
                                       				supported on Cisco 4000 Series Integrated Services Routers. Only an FXO based
                                       				live feed is supported.

Unified CME 12.6 on Cisco IOS XE Gibraltar 16.11.1a Release is not a recommended release for call flows that include Multicast
                                          Music On Hold.

## Information About Music on Hold

### Music on Hold
                           	 Summary

MOH is an audio
                              		stream that is played to PSTN and VoIP G.711 or G.729 callers who are placed on
                              		hold by phones in a Cisco Unified CME system. This audio stream is intended to
                              		reassure callers that they are still connected to their calls.

Table 29-1 provides a summary of options for MOH for PSTN and multicast MOH for local IP
                              		phones.

Audio Source

Description

How to
                                             				  Configure

Flash memory

No external
                                             				  audio input is required.

Configuring
                                                					 Music on Hold from an Audio File

Live feed

The
                                             				  multicast audio stream has minimal delay for local IP phones. The MOH stream
                                             				  for PSTN callers is delayed by a few seconds. If the live feed audio input
                                             				  fails, callers on hold hear silence.

Configuring
                                                					 Music on Hold from a Live Feed

Live feed
                                             				  and flash memory

The live
                                             				  feed stream has a few seconds of delay for both PSTN and local IP phone
                                             				  callers. The flash MOH acts as backup for the live-feed MoH.

If MOH from
                                             				  a live feed is not found or fails, Unified CME swtiches to playback of MOH from
                                             				  the flash memory.

Configuring
                                                					 Music on Hold from an Audio File

and

Configuring
                                                					 Music on Hold from a Live Feed

### Music on
                           	 Hold

MOH is an audio
                              		stream that is played to PSTN and VoIP G.711 or G.729 callers who are placed on
                              		hold by phones in a Cisco Unified CME system. This audio stream is intended to
                              		reassure callers that they are still connected to their calls.

For Unified CME
                              		Release 11.6 and previous releases, when the phone receiving MOH is part of a
                              		system that uses a G.729 codec, transcoding is required between G.711 and
                              		G.729. The G.711 MOH must be translated to G.729. Note that because of
                              		compression, MOH using G.729 is of significantly lower fidelity than MOH using
                              		G.711. From Unified CME Release 11.7 onwards, transcoding is not required if
                              		G.711 and G.729 codec format MOH files are configured on Unified CME. For
                              		information about transcoding, see Transcoding
                                 		  Resources .

Audio file—A MOH
                                       			 audio stream from an audio file is supplied from a .au or .wav file held in
                                       			 router flash memory. For configuration information, see "Configuring
                                          				Music on Hold from an Audio File" .

E&M is
                                                      				  not supported on Cisco 4000 Series Integrated Services Routers for Unified CME.

### Music on Hold from
                           	 a Live Feed

The live-feed
                              		feature is typically used to connect to a CD jukebox player. To configure MOH
                              		from a live feed, you establish a voice port and dial peer for the call and
                              		also create a “dummy” ephone-dn. The ephone-dn must have a phone or extension
                              		number assigned to it so that it can make and receive calls, but the number is
                              		never assigned to a physical phone. Only one live MOH feed is supported per
                              		system.

Using an analog
                              		E&M port as the live-feed MOH interface requires the minimum number of
                              		external components. You connect a line-level audio feed (standard audio jack)
                              		directly to pins 3 and 6 of an E&M RJ-45 connector. The E&M voice
                              		interface card (VIC) has a built-in audio transformer that provides appropriate
                              		electrical isolation for the external audio source. An audio connection on an
                              		E&M port does not require loop-current. The signal
                                    			 immediate and auto-cut-through commands disable E&M
                              		signaling on this voice port. A G.711 audio packet stream is generated by a
                              		digital signal processor (DSP) on the E&M port.

E&M is not
                                          		  supported for MOH from a live feed on the Cisco 4000 Series Integrated Services
                                          		  Routers. Only an FXO based live MOH feed is supported.

If you use an FXO
                              		port as the live-feed MOH interface, connect the MOH source to the FXO port
                              		using a MOD-SC cable if the MOH source has a different connector than the FXO
                              		RJ-11 connector. MOH from a live feed is supported on the VIC2-2FXO, VIC2-4FXO,
                              		EM-HDA-3FXS/4FXO, EM-HDA-6FXO, and EM2-HDA-4FXO.

For Cisco 4000
                              		Series Integrated Services Routers, MOH from a live feed is supported on the
                              		following Cisco network interface modules (NIMs):

NIM-2FXO

NIM-4FXO

NIM-2FXS/4FXO

NIM-2FXS/4FXOP

You can directly
                              		connect a live-feed source to an FXO port if the signal loop-start
                                    			 live-feed command is configured on the voice port; otherwise, the
                              		port must connect through an external third-party adapter to provide a battery
                              		feed. An external adapter must supply normal telephone company (telco) battery
                              		voltage with the correct polarity to the tip and ring leads of the FXO port and
                              		it must provide transformer-based isolation between the external audio source
                              		and the tip and ring leads of the FXO port.

Music from a live
                              		feed is continuously fed into the MOH playout buffer instead of being read from
                              		a flash file, so there is typically a 2-second delay. An outbound call to a MOH
                              		live-feed source is attempted (or reattempted) every 30 seconds until the
                              		connection is made by the directory number that has been configured for MOH. If
                              		the live-feed source is shut down for any reason, the flash memory source will
                              		be automatically activated.

A live-feed MOH
                              		connection is established as an automatically connected voice call that is made
                              		by the Unified CME MOH system or by an external source directly calling in to
                              		the live-feed MOH port. An MOH call can be from or to the PSTN or can proceed
                              		via VoIP with voice activity detection (VAD) disabled. The call is assumed to
                              		be an incoming call unless the optional out-call keyword is used with the moh command
                              		during configuration.

The Unified CME
                              		router uses the audio stream from the call as the source for the MOH stream,
                              		displacing any audio stream that is available from a flash file. An example of
                              		an MOH stream received over an incoming call is an external H.323-based server
                              		device that calls the ephone-dn to deliver an audio stream to the
                              		Cisco Unified CME router.

For configuration
                              		information, see “Configuring
                                 		  Music on Hold from a Live Feed” .

For configuration
                              		example, see Examples .

#### Music on Hold from
                              	 a Live Feed on Cisco 4000 Series Integrated Services Routers

From Unified CME
                                 		Release 12.2 onwards, MOH from a live feed is supported on the Cisco 4000
                                 		Series Integrated Services Routers for all phone types (SIP, SCCP, PSTN, SIP
                                 		Trunk) . As part of the feature support introduced in Unified CME Release 12.2,
                                 		only FXO based live feed is supported. If the FXO based live feed is not
                                 		available, Unified CME switches to flash based MOH playback. If the MOH options
                                 		are disabled, the caller does not hear either the tone on hold or the MOH
                                 		playback.

If you configure
                                 		both live feed and flash-based audio file as the source for MOH, the router
                                 		seeks the live feed first. If the live feed is found, it displaces the audio
                                 		file source. If the live feed is not found or fails at any time, the router
                                 		falls back to the audio file source specified in the MOH audio file
                                 		configuration. This is the recommended configuration.

MOH from a live feed
                                 		supports only G.711 codec. If the MOH live feed over a SIP trunk has a codec
                                 		other than G.711, transcoder insertion is required to play MOH from the live
                                 		feed. TDM trunks support G.711 codecs. Hence, no transcoder insertion is
                                 		required to play MOH for calls from a TDM trunk.

When the SIP
                                          			 trunk or line side has G.729 codec and a DSP resource is not available for
                                          			 transcoding, MOH is played from the G.729 codec format file in the router flash
                                          			 memory.

When the SIP
                                          			 trunk or line side has G.729 codec and a DSP resource is available for
                                          			 transcoding, MOH from a live feed is played. If the MOH from live feed fails,
                                          			 MOH is played from the G.711 codec format file in the router flash memory using
                                          			 the DSP resource.

When the SIP
                                          			 trunk or line side has a codec other than G.729 or G.711 and a DSP resource is
                                          			 not available for transcoding, MOH is not played (dead air).

### Multicast
                           	 MOH

In Cisco CME 3.0 and
                              		later versions, you can configure the MOH audio stream as a multicast source. A
                              		Cisco Unified CME router that is configured for multicast MOH also transmits
                              		the audio stream on the physical IP interfaces of the specified router to
                              		permit access to the stream by external devices.

From Unified CME
                              		Release 12.2 (Cisco IOS XE Fuji 16.8.1 Release), you can configure MOH audio
                              		stream from a live feed as the multicast source. The live feed MoH is supported
                              		when a SCCP phone puts any remote party (SCCP phone, SIP phone, TDM trunk or
                              		SIP trunk) on hold. The MoH is sourced on multicast address, only if the remote
                              		party is SCCP phone. For other parties, it would be unicast address. The
                              		support is introduced on the Cisco 4000 Series Integrated Services Routers.

Certain IP phones do
                              		not support multicast MOH because they do not support IP multicast. In
                              		Cisco Unified CME 4.0 and later versions, you can disable multicast MOH to
                              		individual phones that do not support multicast. Callers hear a repeating tone
                              		when they are placed on hold.

### Music on Hold for
                           	 SIP Phones

In Cisco Unified CME 4.1 and later versions, the MOH feature is supported when a call is put on hold from a SIP phone and
                              when the user of a SIP phone is put on hold by a SIP, SCCP, or POTS endpoint. The holder (party that pressed the hold key)
                              or holdee (party who is put on hold) can be on the same Cisco Unified CME or a different Cisco Unified CME connected through
                              a SIP trunk. MOH is also supported for call transfers and conferencing, with or without a transcoding device.

When a call is placed on hold from an IP phone registered via SIP to CME, the party on hold will not hear Tone on Hold (ToH)
                                          if no MoH source is configured. Instead, the party experiences silence.

Configuring MOH for SIP phones is same as configuring MOH for SCCP phones. For configuration information, see “How to Configure Music on Hold” .

### Music On Hold
                           	 Enhancement

Cisco Unified CME
                              		8.0 and later versions enhance the MOH feature by playing different media
                              		streams to PSTN and VoIP callers who are placed on hold. The MOH enhancement
                              		allows you to configure up to five additional media streams supplied from
                              		multiple media files stored in a router’s flash memory and eliminates the need
                              		for separate routers for streaming MOH media files.

Cisco Unified CME
                              		8.0 MOH enhancement allows you to create MOH groups and assign ephone extension
                              		numbers to these MOH groups to receive different media streams. Callers to the
                              		extension numbers configured under the MOH groups can listen to different MOH
                              		media streams when they are placed on hold.

You can configure up
                              		to five MOH groups. The size of each media source file can range between 64KB
                              		to 10MB long on the Cisco Unified CME router for ephones in different
                              		departments in a branch. A MOH group is linked to an ephone using the extension
                              		number of that ephone. For configuration information, see “Configuring
                                 		  Music on Hold Groups to Support Different Media Sources” .

You can also
                              		configure individual directory numbers to select any MOH group as a MOH source
                              		on the Cisco Unified CME router. The extension number of a directory associates
                              		an ephone to a specific MOH group and callers to these extension numbers can
                              		listen to different media streams when placed on hold. For configuration
                              		information, see “Assigning
                                 		  a MOH Group to a Directory Number” .

Similarly, callers
                              		from internal directory numbers can listen to different media streams when a
                              		MOH group is assigned for an internal call. For configuration information, see “Assigning
                                 		  a MOH Group to all Internal Calls (SCCP Only)” .

Following precedence
                              		rules are applicable when an ephone caller is placed on hold:

MOH group defined for
                                    			 internal calls takes highest precedence.

MOH group defined in
                                    			 ephone-dn takes the second highest precedence.

MOH group defined in
                                    			 ephone-dn-template takes precedence if MOH group is not defined in ephone-dn or
                                    			 internal call.

Extension
                                    			 numbers defined in a MOH-group has the least precedence.

Phones not
                                    			 associated with any MOH groups default to the MOH parameters defined in the moh command
                                    			 under telephony-service configuration mode.

If a selected MOH
                                          		  group does not exist, the caller will hear tone on hold.

We recommend that
                                          		  departments in a branch must have mutually exclusive extension numbers and
                                          		  multicast destinations for configuring MOH groups.

### Caching MOH Files
                           	 for Enhanced System Performance

Caching MOH files helps enhance the system performance by reducing the CPU usage. However, caching requires memory buffer
                              to store a large MOH file. You can set up a buffer file size for caching MOH files that you might use in the future. The default
                              MOH file buffer size is 64 KB (8 seconds). The maximum buffer size (per file) can be configured anywhere between 64 KB (8
                              seconds) to 10000 KB (approximately 20 minutes), You can use the moh-file-buffer command to allocate MOH file buffer for future MOH files, see Configuring Buffer Size for MOH Files . To verify if a file is being cached and to update a cached moh-file, see Verifying MOH File Caching .

If the file size
                                          		  is too large, buffer size falls back to 64 KB.

### Configure G.711 and
                              	 G.729 Files for Music on Hold

From Cisco Unified CME 11.7 Release onwards, G.711 and G.729 codec
                              		format MOH files can be configured on Unified CME. For calls (line or trunk
                              		calls) that need to be placed on hold and MOH needs to be played, transcode
                              		insertion is not required if the codec used is G.729 or G.711. The new feature
                              		dynamically selects the matching codec (either G.729 or G.711) based on the
                              		codec used on phones or trunk. Transcode insertion is required only if the
                              		codec on the phone playing Music on Hold is neither G.729 nor G.711. For more
                              		information on configuration of MOH, see Configure Music on Hold .

If G.711 and G.729 codec format MOH files are configured on Unified CME,
                              		you will need transcoding only to support other codec format MOH files, such as
                              		iLBC. You need the G.711 codec format MOH file to be configured under
                              		telephony-service for MOH to be supported on Unified CME.

You have to configure the primary G.711 codec format MOH file before
                                          		  configuring the G.729 or G.729A codec format MOH file.

We recommend that G.711 and G.729 codec format MOH files are available
                                          		  on the flash memory of Unified CME router.

In a scenario where a call between an SCCP line and SIP trunk has a
                                          		  codec other than G.729 or G.711, then MOH is not played when the SCCP line
                                          		  places the SIP phone on hold.

In a scenario where a call is placed between an SCCP line and a SIP
                                          		  line, and the call is placed on hold from the SIP end, MOH is played only from
                                          		  the G.711 codec format MOH file.

## Configure Music on Hold

### Configure Music on
                           	 Hold from an Audio File to Supply Audio Stream

If you configure
                                             			 MOH from an audio file and from a live feed, the router seeks the live feed
                                             			 first. If a live feed is found, it displaces an audio file source. If the live
                                             			 feed is not found or fails at any time, the router falls back to the audio file
                                             			 source.

The MOH file
                                             			 packaged with the CME software is completely royalty free.

Restriction

To change
                                                      				  the audio file to a different file, you must remove the first file using the no moh command before specifying a second file. If you configure a second file without
                                                      				  removing the first file, the MOH mechanism stops working and may require a
                                                      				  router reboot to clear the problem.

The volume
                                                      				  level of a MOH file cannot be adjusted through Cisco IOS software, so it cannot
                                                      				  be changed when the file is loaded into the flash memory of the router. To
                                                      				  adjust the volume level of a MOH file, edit the file in an audio editor before
                                                      				  downloading the file to router flash memory.

#### Before you begin

SIP phones
                                          				require Cisco Unified CME 4.1 or a later version.

A music file
                                          				must be in stored in the router’s flash memory. This file should be in G.711
                                          				format. The file can be in .au or .wav file format, but the file format must
                                          				contain 8-bit 8-kHz data; for example, ITU-T A-law or mu-law data format.

From Cisco Unified CME Release 11.7 onwards, you can configure and
                                          				store an MOH file in G.729 codec format in the router's flash memory. The G.729
                                          				file can be used as MOH source.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- moh filename

- multicast moh ip-address port port-number [ route ip-address-list ]

- exit

- ephone phone-tag

- multicast-moh

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

moh filename

#### Example:

```
Router(config-telephony)# moh minuet.au
```

```
Router(config-telephony)# moh flash:moh_g711u_music.wav
```

```
Router(config-telephony)# moh g729 flash:SampleAudioSource.g729.wav
```

Enables music
                                             				on hold using the specified file.

If you
                                                   					 specify a file with this command and later want to use a different file, you
                                                   					 must disable use of the first file with the no moh command before configuring the second file.

G.729 MOH file can be configured along with the G.711 MOH
                                                   					 file. Unified CME would pick the MOH file to be played based on the negotiated
                                                   					 codec on line or trunk.

Step 5

multicast moh ip-address port port-number [ route ip-address-list ]

#### Example:

```
Router(config-telephony)# multicast moh 239.10.16.4 port 16384 route 10.10.29.17 10.10.29.33
```

Specifies that
                                             				this audio stream is to be used for multicast and also for MOH.

This command
                                                         				  is required to use MOH for internal calls and it must be configured after MOH
                                                         				  is enabled with the moh command.

ip-address —Destination IP address for multicast.

port port-number —Media port for multicast. Range is
                                                   					 2000 to 65535. We recommend port 2000 because it is already used for normal RTP
                                                   					 media transmissions between IP phones and the router.

Valid port
                                                         				  numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                         				  system reserves odd values.)

route —(Optional) List of explicit router
                                                   					 interfaces for the IP multicast packets.

ip-address-list —(Optional) List of up to four
                                                   					 explicit routes for multicast MOH. The default is that the MOH multicast stream
                                                   					 is automatically output on the interfaces that correspond to the address that
                                                   					 was configured with the ip
                                                         						  source-address command.

For MOH on
                                                         				  internal calls, packet flow must be enabled to the subnet on which the phones
                                                         				  are located.

Step 6

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 7

ephone phone-tag

#### Example:

```
Router(config)# ephone 28
```

Enters
                                             				ephone configuration mode.

Step 8

multicast-moh

#### Example:

```
Router(config-ephone)# no multicast-moh
```

(Optional)
                                             				Enables multicast MOH on a phone. This is the default.

This
                                                   					 command is supported in Cisco Unified CME 4.0 and later versions.

The no form of
                                                   					 this command disables MOH for phones that do not support multicast. Callers
                                                   					 hear a repeating tone when they are placed on hold.

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone configuration mode has priority over the value set in
                                                   					 ephone-template mode.

Step 9

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example enables music on hold and specifies the music file to use:

```
telephony-service  
		 moh minuet.wav
```

The following
                                 		  example enables MOH and specifies a multicast address for the audio stream:

```
telephony-service  
		 moh minuet.wav 
		 multicast moh 239.23.4.10 port 2000
```

### Configure Music on
                           	 Hold from a Live Feed

To configure music
                                 		  on hold from a live feed, perform the following steps.

If you configure
                                             			 MOH from an audio file and from a live feed, the router seeks the live feed
                                             			 first. If a live feed is found, it displaces an audio file source. If the live
                                             			 feed is not found or fails at any time, the router falls back to the audio file
                                             			 source.

Restriction

A foreign
                                                      				  exchange station (FXS) port cannot be used for a live feed.

#### Before you begin

SIP phones
                                          				require Cisco Unified CME 4.1 or a later version.

VIC2-2FXO,
                                          				VIC2-4FXO, EM-HDA-3FXS/4FXO, EM-HDA-6FXO, or EM2-HDA-4FXO on Cisco Integrated
                                          				Services Routers Generation 2 (ISR G2) family of routers.

NIM-2FXO,
                                          				NIM-4FXO, NIM-2FXS/4FXO, and NIM-2FXS/4FXOP are the Cisco network interface
                                          				modules (NIMs) supported on Cisco 4000 Series Integrated Services Routers.

For a live
                                          				feed from VoIP (over a SIP trunk), VAD must be disabled.

### SUMMARY STEPS

- enable

- configure terminal

- voice-port port

- input gain decibels

- auto-cut-through

- operation 4-wire

- signal immediate

- signal loop-start live-feed

- no shutdown

- exit

- dial peer voice tag pots

- destination-pattern string

- port port

- exit

- ephone-dn dn-tag

- number number

- moh [ out-call outcall-number ] [ ip ip-address port port-number [ route ip-address-list ]]

- exit

- ephone phone-tag

- multicast-moh

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

voice-port port

#### Example:

```
Router(config)# voice-port 1/1/0
```

Enters
                                             				voice-port configuration mode.

Port argument is platform-dependent; type ? to display
                                                   					 syntax.

Step 4

input gain decibels

#### Example:

```
Router(config-voice-port)# input gain 0
```

Specifies, in
                                             				decibels, the amount of gain to be inserted at the receiver side of the
                                             				interface.

decibels —Acceptable values are integers –6 to 14.

Step 5

auto-cut-through

#### Example:

```
Router(config-voice-port)# auto-cut-through
```

(E&M ports
                                             				only) Enables call completion when a PBX does not provide an M-lead response.

MOH
                                                   					 requires that you use this command with E&M ports.

Step 6

operation 4-wire

#### Example:

```
Router(config-voice-port)# operation 4-wire
```

(E&M ports
                                             				only) Selects the 4-wire cabling scheme.

MOH
                                                   					 requires that you specify 4-wire operation with this command for E&M ports.

Step 7

signal immediate

#### Example:

```
Router(config-voice-port)# signal immediate
```

(E&M ports
                                             				only) For E&M tie trunk interfaces, directs the calling side to seize a
                                             				line by going off-hook on its E-lead and to send address information as dual
                                             				tone multifrequency (DTMF) digits.

Step 8

signal loop-start live-feed

#### Example:

```
Router(config-voice-port)# signal loop-start live-feed
```

(FXO ports
                                             				only) Enables an MOH audio stream from a live feed to be directly connected to
                                             				the router through an FXO port.

This
                                                   					 command is supported in Cisco IOS Release 12.4(15)T and later releases.

Step 9

no shutdown

#### Example:

```
Router(config-voice-port)# no shutdown
```

Activates
                                             				the voice port.

To shut
                                                   					 the voice port down and disable MOH from a live feed, use the shutdown command.

Step 10

exit

#### Example:

```
Router(config-voice-port)# exit
```

Exits
                                             				voice-port configuration mode.

Step 11

dial peer voice tag pots

#### Example:

```
Router(config)# dial peer voice 7777 pots
```

Enters
                                             				dial-peer configuration mode.

Step 12

destination-pattern string

#### Example:

```
Router(config-dial-peer)# destination-pattern 7777
```

Specifies
                                             				either the prefix or the full E.164 telephone number to be used for a dial
                                             				peer.

Step 13

port port

#### Example:

```
Router(config-dial-peer)# port 1/1/0
```

Associates
                                             				the dial peer with the voice port that was specified in Step 3.

Step 14

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits
                                             				dial-peer configuration mode.

Step 15

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 55
```

Enters
                                             				ephone-dn configuration mode.

dn-tag —Unique sequence number that identifies this
                                                   					 ephone-dn during configuration tasks. Range is 1 to 288.

Step 16

number number

#### Example:

```
Router(config-ephone-dn)# number 5555
```

Configures a
                                             				valid extension number for this ephone-dn.

This
                                                   					 number is not assigned to any phone; it is only used to make and receive calls
                                                   					 that contain an audio stream to be used for MOH.

number —String of up to 16 digits that represents a
                                                   					 telephone or extension number to be associated with this ephone-dn.

Step 17

moh [ out-call outcall-number ] [ ip ip-address port port-number [ route ip-address-list ]]

#### Example:

```
Router(config-ephone-dn)# moh out-call 7777 ip 239.10.16.8 port 2311 route 10.10.29.3 10.10.29.45
```

or

```
Router(config-ephone-dn)# moh out-call 7777
```

Specifies
                                             				that this ephone-dn is to be used for an incoming or outgoing call that is the
                                             				source for an MOH stream.

(Optional) out-call outcall-number —Indicates that the router is
                                                   					 calling out for a live feed for MOH and specifies the number to be called.
                                                   					 Forces a connection to the local voice port that was specified in Step 3. If
                                                   					 this command is used without this keyword, the MOH stream is received from an
                                                   					 incoming call.

(Optional) ip ip-address —Destination IP address for multicast.

If you
                                                   					 are configuring MOH from a live feed and from an audio file for backup, do not
                                                   					 configure a multicast IP address for this command. If the live feed fails or is
                                                   					 not found, MOH will fall back to the ip address that you configured using the multicast
                                                         						  moh command in telephony-service configuration mode. See “Configuring
                                                      						Music on Hold from an Audio File” .

If you
                                                   					 specify an address for multicast with this command and a different address with
                                                   					 the multicast
                                                         						  moh command in telephony-service configuration mode, you can send
                                                   					 the MOH audio stream to two multicast addresses.

(Optional) port port-number —Media port for multicast. Range is
                                                   					 2000 to 65535. We recommend port 2000 because it is already used for RTP media
                                                   					 transmissions between IP phones and the router.

(Optional) route ip-address -list—Indicates specific router
                                                   					 interfaces on which to transmit the IP multicast packets. Up to four IP
                                                   					 addresses can be listed. Default: The MOH multicast stream is automatically
                                                   					 output on the interfaces that correspond to the address that was configured
                                                   					 with the ip
                                                         						  source-address command.

Step 18

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 19

ephone phone-tag

#### Example:

```
Router(config)# ephone 28
```

Enters
                                             				ephone configuration mode.

Step 20

multicast-moh

#### Example:

```
Router(config-ephone)# no multicast-moh
```

(Optional)
                                             				Enables multicast MOH on a phone. This is the default.

This
                                                   					 command is supported in Cisco Unified CME 4.0 and later versions.

The no form of
                                                   					 this command disables MOH for phones that do not support multicast. Callers
                                                   					 hear a repeating tone when they are placed on hold.

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone configuration mode has priority over the value set in
                                                   					 ephone-template mode.

Step 21

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example enables MOH from an outgoing call on voice port 1/1/0 and dial peer
                                 		  7777:

```
voice-port 1/1/0
 auto-cut-through
 operation 4-wire
 signal immediate
!
dial-peer voice 7777 pots
 destination-pattern 7777
 port 1/1/0
!
ephone-dn 55
 number 5555
 moh out-call 7777
```

The following
                                 		  example enables MOH from a live feed and if the live feed is not found or fails
                                 		  at any time, the router falls back to the music file (music-on-hold.au) and
                                 		  multicast address for the audio stream specified in the telephony-service
                                 		  configuration:

```
voice-port 0/1/0
 auto-cut-through
 operation 4-wire
 signal immediate
 timeouts call-disconnect 1
 description MOH Live Feed
!
dial-peer voice 7777 pots
 destination-pattern 7777
 port 0/1/0
!
telephony-service
 max-ephones 24
 max-dn 192
 ip source-address 10.232.222.30 port 2000
 moh music-on-hold.au
 multicast moh 239.1.1.1 port 2000
! 
ephone-dn  52
		 number 1
 moh out-call 7777
```

### Configure Music on
                           	 Hold Groups to Support Different Media Sources

Restriction

Media files
                                                   				  from live-feed source are not supported.

Each MOH
                                                   				  group must contain a unique flash media file name, extension numbers, and
                                                   				  multicast destination. If you enter any extension ranges, MOH filenames, and
                                                   				  multicast IP addresses that already exist in another MOH-group, an error
                                                   				  message is issued and the new input in the current voice MOH-group is
                                                   				  discarded.

Media file
                                                   				  CODEC format is limited to G.711 and G.729.

#### Before you begin

Cisco Unified
                                       				CME 8.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice moh-group moh-group-tag

- description string

- moh filename

- multicast moh ip-address port port-number route ip-address-list

- extension-range starting-extension to ending-extension

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

voice moh-group moh-group-tag

#### Example:

```
Router(config-telephony)# voice moh-group 1
```

Enters the
                                             				voice moh-group configuration mode. You can create up to five voice moh-groups
                                             				for ephones receiving music on hold audio files when placed on hold. Range for
                                             				the voice moh-groups is 1 to 5.

Step 4

description string

#### Example:

```
Router(config-voice-moh-group)# description moh group for sales
```

(Optional)
                                             				Allows you to add a brief description specific to a voice MOH group. You can
                                             				use up to 80 characters to describe the voice MOH group.

Step 5

moh filename

#### Example:

```
Router(config-voice-moh-group)# moh flash:/minuet.au
```

Enables music
                                             				on hold using the specified MOH source file. The MOH file must be in .au and
                                             				.wav format. MOH filename length should not exceed 128 characters. You must
                                             				provide the directory and filename of the MOH file in URL format. For example: moh
                                                				  flash:/minuet.au

If you
                                                   					 specify a file with this command and later want to use a different file, you
                                                   					 must disable use of the first file with the no moh command before configuring the second file.

Step 6

multicast moh ip-address port port-number route ip-address-list

#### Example:

```
Router((config-voice-moh-group)# multicast moh 239.10.16.4 port 16384 route 10.10.29.17 10.10.29.33
```

Specifies that
                                             				this audio stream is to be used for multicast and also for MOH.

ip-address —Destination IP address for multicast.

port port-number —Media port for multicast. Range is
                                                   					 2000 to 65535. We recommend port 2000 because it is already used for normal RTP
                                                   					 media transmissions between IP phones and the router.

route —(Optional) List of explicit router
                                                   					 interfaces for the IP multicast packets.

ip-address-list —(Optional) List of up to four
                                                   					 explicit routes for multicast MOH. The default is that the MOH multicast stream
                                                   					 is automatically output on the interfaces that correspond to the address that
                                                   					 was configured with the ip
                                                         						  source-address command.

Step 7

extension-range starting-extension to ending-extension

#### Example:

```
Router(config-voice-moh-group)#extension-range 1000 to 1999
```

```
Router(config-voice-moh-group)#extension-range 2000 to 2999
```

(Optional)
                                             				identifies MOH callers calling the extension numbers specified in a MOH group.
                                             				Extension number must be in hexadecimal digits (0-9) or (A-F). Both extension
                                             				numbers (starting extension and ending extension) must contain equal number of
                                             				digits. Repeat this command to add additional extension ranges.

starting-extension —(Optional) Lists the starting
                                                   					 extension number for a moh-group.

ending-extension —(Optional) Lists the ending
                                                   					 extension number for a moh-group.

Step 8

end

#### Example:

```
Router(config-voice-moh-group)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

In the following
                                 		  example, total six MOH groups are configured. MOH group 1 through 5 are
                                 		  configured under voice-moh-group configuration mode and MOH group 0 is the MOH
                                 		  source file configured under telephony-services.

```
router# show voice moh-group telephony-service
 moh alaska.wav
 Moh multicast 239.1.1.1 port 16384 route 10.1.4.31 10.1.1.2

voice moh-group 1
 description this moh group is for sales
 moh flash:/hello.au
 multicast moh 239.1.1.1 port 16386 route 239.1.1.3 239.1.1.3
 extension-range 1000 to 1999
 extension-range 2000 to 2999
 extension-range 3000 to 3999
 extension-range A1000 to A1999

voice moh-group 2
 description (not configured)
 moh flash1:/minuet.au
 multicast moh 239.23.4.10 port 2000
 extension-range 7000 to 7999
 extension-range 8000 to 8999

voice moh-group 3
 description This is for marketing
 moh flash2:/happy.au
 multicast moh 239.15.10.1 port 3000
 extension-range 9000 to 9999

voice moh-group 4
 description (not configured)
 moh flash:/audio/sun.au
 multicast moh 239.16.12.1 port 4000
 extension-range 10000 to 19999

voice moh-group 5
 description (not configured)
 moh flash:/flower.wav
 multicast moh 239.12.1.2 port 5000
 extension-range 0012 to 0024
 extension-range 0934 to 0964 === Total of 6 voice moh-groups ===
```

### Assign a MOH Group to a Directory Number

Restriction

Do not use same extension number for different MOH groups.

#### Before you begin

Cisco Unified CME 8.0 or a later version.

MOH groups must be configured under global configuration mode.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn tag

- number

- moh-group tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

ephone-dn tag

#### Example:

```
Router(config)# ephone-dn 1
```

Enters ephone-dn configuration mode.

In ephone-dn configuration mode, you assign an extension number
                                             				using the number command.

You can also configure a MOH group to an ephone-dn- template for
                                             				use across a range of ephone-dns. If two different MOH groups are configured as
                                             				a result of this command, the MOH group configured under the ephone-dn
                                             				configuration takes precedence.

MOH group configuration for ephone-template-dn configuration
                                                         				  command is temporarily prohibited when any directory number using that template
                                                         				  is on hold.

Step 4

number

#### Example:

```
Router(config)# ephone-dn 1
```

```
Router(config-ephone-dn)# number 1001
```

Allows you to define an extension number and associate this number to a telephone.

Step 5

moh-group tag

#### Example:

```
Router(config-telephony)#voice moh-group 1
```

```
Router(config-voice-moh-group)#
```

Allows you to assign a MOH group to a directory number.

MOH group tag — identifies the unique number
                                                   					 assigned to a MOH group for configuration tasks.

Step 6

end

#### Example:

```
Router(config-ephone)# end
```

Returns to privileged EXEC mode.

#### Examples

In the following example different moh groups are assigned to
                                 		  different directory numbers (ephone-dn) moh group1 is assigned to ephone-dn 1,
                                 		  moh-group 4 is assigned to ephone-dn 4, and moh-group 5 is assigned to
                                 		  ephone-dn 5.

```
ephone-dn  1  octo-line
 number 7001
 name DN7001
 moh-group 1
!
ephone-dn  2  dual-line
 number 7002
 name DN7002
 call-forward noan 6001 timeout 4
!
ephone-dn  3 
 number 7003
 name DN7003
 snr 7005 delay 3 timeout 10
 allow watch
 call-forward noan 8000 timeout 30
!
!
ephone-dn  4  dual-line
 number 7004
 allow watch
 call-forward noan 7001 timeout 10
 moh-group 4
 !
ephone-dn  5 
 number 7005
 name DN7005
 moh-group 5
 !
```

### Assign a MOH Group to all Internal Calls Only to SCCP Phones

Restriction

Do not use same extension number for different MOH groups.

#### Before you begin

Cisco Unified CME 8.0 or a later version.

MOH groups must be configured under global configuration mode.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- internal-call moh-group tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config-telephony)# ephone-dn 1
```

Enters telephony-service configuration mode.

In ephone-dn configuration mode, you assign an extension number
                                             				using the number command.

Step 4

internal-call moh-group tag

#### Example:

```
Router(config)#
```

```
Router(config-telephony)# internal call moh-group 4
```

Allows to assign a MOH-group for all internal directory numbers.

Moh group tag — identifies the unique number
                                                   					 assigned to a MOH group for configuration tasks, Range for the tag is from 0 to
                                                   					 5, where 0 represents MOH configuration in telephony service.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to privileged EXEC mode.

#### Examples

The following examples shows moh-group 4 configured for internal
                                 		  directory calls.

```
telephony-service
		sdspfarm conference mute-on *6 mute-off *8
		sdspfarm units 4
		sdspfarm transcode sessions 2
		sdspfarm tag 1 moto-HW-Conf moh flash1:/minuet.au Moh multicast 239.1.1.1 port 16384 route 10.1.4.31 10.1.1.2 internal-call moh-group 4 em logout 0:0 0:0 0:0 
		max-ephones 110
		max-dn 288
		ip source-address 15.2.0.5 port 2000
		auto assign 1 to 1
		caller-id block code *9999
		service phone settingsAccess 1
		service phone spanTOPCPort 0
		service dss
		timeouts transfer-recall 12
```

### Configure Buffer
                           	 Size for MOH Files

Restriction

MOH file
                                                      				  caching is prohibited if live-feed is enabled for MOH-group 0.

MOH file
                                                      				  buffer size must be larger than the MOH file (size) that needs to be cached.

Sufficient
                                                      				  system memory must be available for MOH file caching.

#### Before you begin

Cisco Unified
                                          				CME 8.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- moh-file-buffer file
                                       				  size

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

telephony-service

#### Example:

```
Router(config-telephony)# ephone-dn 1
```

Enters
                                             				telephony-service configuration mode.

In ephone-dn
                                             				configuration mode, you assign an extension number using the number command.

Step 4

moh-file-buffer file
                                                				  size

#### Example:

```
Router(config-telephony)# moh-file-buffer 2000
```

(Optional)
                                             				Allows to set a buffer for the MOH file size. You can configure a max file
                                             				buffer size (per file) anywhere between 64 KB (8 seconds) to 10000 KB
                                             				(approximately 20 minutes), Default moh-file-buffer size is 64 KB (8 seconds).

A large
                                                         				  buffer size is desirable to cache the largest MOH file and a better system
                                                         				  performance.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  examples shows 90 KB as the configured moh-file-buffer size.

```
telephony-service
 sdspfarm conference mute-on *6 mute-off *8
 sdspfarm units 4
 sdspfarm transcode sessions 2
 sdspfarm tag 1 moto-HW-Conf
 moh flash1:/minuet.au
 Moh multicast 239.1.1.1 port 16384 route 10.1.4.31 10.1.1.2 moh-file-buffer 90 em logout 0:0 0:0 0:0 
 max-ephones 110
 max-dn 288
 ip source-address 15.2.0.5 port 2000
 auto assign 1 to 1
 caller-id block code *9999
 service phone settingsAccess 1
 service phone spanTOPCPort 0
 service dss
 timeouts transfer-recall 12
```

### Verify MOH File
                           	 Caching

Use the show ephone
                                                				  moh command to verify if the MOH file is being cached.

#### Example:

```
Router #show ephone moh
Skinny Music On Hold Status (moh-group 1)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000
```

If the
                                                				  file is not cached as in MOH group 1 in the above example, then check file size
                                                				  in the flash.

#### Example:

```
Router#dir flash:/minuet.au
Directory of flash:/minuet.au 32  -rw- 1865696  Apr 25 2009 00:47:12 +00:00  moh1.au
```

Under
                                                				  telephony-service, configure “moh-file-buffer <file size>”. Default file
                                                				  size is 64 KB (8 seconds). Make sure you enter a larger file size to cache
                                                				  large MOH files that you may use in future.

#### Example:

```
Router(config)# telephony-service
Router(config-telephony)# moh-file-buffer 2000
```

Under
                                                				  voice moh-group <group tag>, configure “no moh”, and immediately
                                                				  configure “moh <filename>”. This allows the MOH server to read the file
                                                				  immediately from flash again.

#### Example:

```
Router(config-telephony)#voice moh-group 1
Router(config-voice-moh-group)#no moh
Router(config-voice-moh-group)#moh flash:/minuet.au
```

Depending
                                                				  on the size of the file, you should see the MOH file caching after a few
                                                				  minutes (approximately, 2 minutes).

#### Example:

```
Router #show ephone moh
Skinny Music On Hold Status - group 1
Active MOH clients 0 (max 830), Media Clients 0
File flash:/moh1.au (cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000
```

MOH file
                                                               						caching is prohibited under the following conditions: if live feed is
                                                               						configured in moh-group 0, If file buffer size smaller than file size, or
                                                               						insufficient system memory.

### Verify Music on Hold Group Configuration

Step 1

Use the show voice moh-group command to display one or the entire moh-group configuration.

The following example shows all six MOH groups with extension ranges, MOH files, and multicast destination addresses.

```
router# show voice moh-group telephony-service
 moh alaska.wav
 Moh multicast 239.1.1.1 port 16384 route 10.1.4.31 10.1.1.2
 
voice moh-group 1
 description this moh group is for sales
 moh flash:/audio?minuet.au
 multicast moh 239.1.1.1 port 16386 route 239.1.1.2 239.1.1.3
 extension-range 1000 to 1999
 extension-range 2000 to 2999
 extension-range 3000 to 3999
 extension-range 20000 to 22000
 extension-range A1000 to A1999
 
voice moh-group 2
 description (not configured)
 moh flash:/audio/hello.au
 multicast moh 239.23.4.10 port 2000
 extension-range 7000 to 7999
 extension-range 8000 to 8999
 
voice moh-group 3
 description This is for marketing
 moh flash:/happy.au
 multicast moh 239.15.10.1 port 3000
 extension-range 9000 to 9999
 
voice moh-group 4
 description (not configured)
 moh flash:/audio/sun.au
 multicast moh 239.16.12.1 port 4000
 extension-range 10000 to 19999
 
voice moh-group 5
 description (not configured)
 moh flash:/flower.wav
 multicast moh 239.12.1.2 port 5000
 extension-range 0012 to 0024
 extension-range 0934 to 0964
 
=== Total of 6 voice moh-groups ===
```

Step 2

Use the show ephone moh to display information about the different MOH group configured.

The following example displays information about five different MOH groups.

```
Router # show ephone moh Skinny Music On Hold Status (moh-group 1)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000
 
Skinny Music On Hold Status (moh-group 2)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/audio/hello.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.6 port 2000 via 0.0.0.0
 
Skinny Music On Hold Status (moh-group 3)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/bells.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.5 port 2000 via 0.0.0.0
 
Skinny Music On Hold Status (moh-group 4)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/3003.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.7 port 2000 via 0.0.0.0
 
Skinny Music On Hold Status (moh-group 5)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/4004.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.8 port 2000 via 0.0.0.0
```

Step 3

Use the show voice moh-group statistics command to display the MOH subsystem statistics information.

In the following example, the MOH Group Streaming Interval Timing Statistics shows the media packet counts during streaming
                                             intervals. Each packet counter is of 32 bit size and holds a count limit of 4294967296. This means that with 20 milliseconds
                                             packet interval (for G.711), the counters will restart from 0 any time after 2.72 years (2 years 8 months). Use the clear
                                             voice moh-group statistics once in every two years to reset the packet counters.

MOH Group Packet Transmission Timing Statistics shows the maximum and minimum amount of time (in microseconds) taken by the
                                             MOH groups to send out media packets. The MOH Group Loopback Interval Timing Statistics is available when loopback interface
                                             is configured as part of the multicast MOH routes as in the case of SRST. These counts are loopback packet counts within certain
                                             streaming timing intervals.

```
router# show voice moh-group statistics MOH Group Streaming Interval Timing Statistics:
Grp#  ~19 msec     20~39      40~59      60~99     100~199   200+ msec
==== ========== ========== ========== ========== ========== ==========
 0:       25835   17559966      45148          0          0          1
 1:       19766   17572103      39079          0          0          1
 2:       32374   17546886      51687          0          0          1
 3:       27976   17555681      47289          0          0          1
 4:       34346   17542940      53659          0          0          1
 5:       14971   17581689      34284          0          0          1
 
MOH Group Packet Transmission Timing Statistics:
Grp#  max(usec)  min(usec) 
==== ========== ========== 
 0:          97          7.
 1:          95          7.
 2:          97          7.
 3:          96          7.
 4:          94          7.
 5:          67          7.
 
 MOH Group Loopback Interval Timing Statistics:
 loopback event array: svc_index=1542, free_index=1549, max_q_depth=31
 Grp#  ~19 msec     20~39      40~59      60~99     100~199   200+ msec
 ==== ========== ========== ========== ========== ========== ==========
 0:     8918821    8721527      10023          0          1          1
 1:     9007373    8635813       7184          0          1          1
 2:     8864760    8772851      12758          0          1          1
 3:     8924447    8715457      10464          0          1          1
 4:     8858393    8778957      13017          0          1          1
 5:     9005511    8639936       4919          0          1          1
 
Statistics collect time: 4 days 2 hours 5 minutes 39 seconds.
```

Step 4

Use the clear voice moh-group statistics command to clear the display of MOH subsystem statistics information.

For Example:

```
router# clear voice moh-group statistics All moh group stats are cleared
```

## Feature
                        	 Information for Music on Hold

The following table
                           		provides release information about the feature or features described in this
                           		module. This table lists only the software release that introduced support for
                           		a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature
                                       				  Name

Cisco Unified CME Version

Feature
                                       				  Information

Music on
                                       				  Hold

12.2

Support
                                       				  for Music on Hold from a live feed on Unified CME is introduced on the Cisco
                                       				  4000 Series Integrated Services Routers.

12.2

Support
                                       				  for Multicast Music on Hold from a live feed is introduced for SCCP to SCCP
                                       				  calls on the Cisco 4000 Series Integrated Services Routers.

11.7

Support
                                       				  for configuration of G.711 and G.729 codec format MOH file on Unified CME is
                                       				  added.

8.0

Music on
                                       				  hold from different media sources is added.

4.1

Music on
                                       				  hold for SIP phones is supported.

4.0

Music
                                                						on hold is introduced for internal calls.

The
                                                						ability to disable multicast MOH per phone is introduced.

3.0

The
                                       				  ability to use a live audio feed as a multicast source is introduced.

2.1

Music on
                                       				  hold from a live audio feed is introduced for external calls.

2.0

Music on
                                       				  hold from an audio file is introduced for external calls.

| Note | Unified CME 12.6 on Cisco IOS XE Gibraltar 16.11.1a Release is not a recommended release for call flows that include Multicast
                                          Music On Hold. |
|---|---|

| Audio Source | Description | How to
                                             				  Configure |
|---|---|---|
| Flash memory | No external
                                             				  audio input is required. | Configuring
                                                					 Music on Hold from an Audio File |
| Live feed | The
                                             				  multicast audio stream has minimal delay for local IP phones. The MOH stream
                                             				  for PSTN callers is delayed by a few seconds. If the live feed audio input
                                             				  fails, callers on hold hear silence. | Configuring
                                                					 Music on Hold from a Live Feed |
| Live feed
                                             				  and flash memory | The live
                                             				  feed stream has a few seconds of delay for both PSTN and local IP phone
                                             				  callers. The flash MOH acts as backup for the live-feed MoH. If MOH from
                                             				  a live feed is not found or fails, Unified CME swtiches to playback of MOH from
                                             				  the flash memory. | Configuring
                                                					 Music on Hold from an Audio File and Configuring
                                                					 Music on Hold from a Live Feed |

| Note | E&M is
                                                      				  not supported on Cisco 4000 Series Integrated Services Routers for Unified CME. |
|---|---|

| Note | E&M is not
                                          		  supported for MOH from a live feed on the Cisco 4000 Series Integrated Services
                                          		  Routers. Only an FXO based live MOH feed is supported. |
|---|---|

| Note | When a call is placed on hold from an IP phone registered via SIP to CME, the party on hold will not hear Tone on Hold (ToH)
                                          if no MoH source is configured. Instead, the party experiences silence. |
|---|---|

| Note | If a selected MOH
                                          		  group does not exist, the caller will hear tone on hold. |
|---|---|

| Note | We recommend that
                                          		  departments in a branch must have mutually exclusive extension numbers and
                                          		  multicast destinations for configuring MOH groups. |
|---|---|

| Note | If the file size
                                          		  is too large, buffer size falls back to 64 KB. |
|---|---|

| Note | You have to configure the primary G.711 codec format MOH file before
                                          		  configuring the G.729 or G.729A codec format MOH file. We recommend that G.711 and G.729 codec format MOH files are available
                                          		  on the flash memory of Unified CME router. |
|---|---|

| Note | In a scenario where a call between an SCCP line and SIP trunk has a
                                          		  codec other than G.729 or G.711, then MOH is not played when the SCCP line
                                          		  places the SIP phone on hold. In a scenario where a call is placed between an SCCP line and a SIP
                                          		  line, and the call is placed on hold from the SIP end, MOH is played only from
                                          		  the G.711 codec format MOH file. |
|---|---|

| Note | If you configure
                                             			 MOH from an audio file and from a live feed, the router seeks the live feed
                                             			 first. If a live feed is found, it displaces an audio file source. If the live
                                             			 feed is not found or fails at any time, the router falls back to the audio file
                                             			 source. |
|---|---|

| Note | The MOH file
                                             			 packaged with the CME software is completely royalty free. |
|---|---|

| Restriction | To change
                                                      				  the audio file to a different file, you must remove the first file using the no moh command before specifying a second file. If you configure a second file without
                                                      				  removing the first file, the MOH mechanism stops working and may require a
                                                      				  router reboot to clear the problem. The volume
                                                      				  level of a MOH file cannot be adjusted through Cisco IOS software, so it cannot
                                                      				  be changed when the file is loaded into the flash memory of the router. To
                                                      				  adjust the volume level of a MOH file, edit the file in an audio editor before
                                                      				  downloading the file to router flash memory. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | moh filename Example: Router(config-telephony)# moh minuet.au OR Router(config-telephony)# moh flash:moh_g711u_music.wav Router(config-telephony)# moh g729 flash:SampleAudioSource.g729.wav | Enables music
                                             				on hold using the specified file. If you
                                                   					 specify a file with this command and later want to use a different file, you
                                                   					 must disable use of the first file with the no moh command before configuring the second file. G.729 MOH file can be configured along with the G.711 MOH
                                                   					 file. Unified CME would pick the MOH file to be played based on the negotiated
                                                   					 codec on line or trunk. |
| Step 5 | multicast moh ip-address port port-number [ route ip-address-list ] Example: Router(config-telephony)# multicast moh 239.10.16.4 port 16384 route 10.10.29.17 10.10.29.33 | Specifies that
                                             				this audio stream is to be used for multicast and also for MOH. Note This command
                                                         				  is required to use MOH for internal calls and it must be configured after MOH
                                                         				  is enabled with the moh command. ip-address —Destination IP address for multicast. port port-number —Media port for multicast. Range is
                                                   					 2000 to 65535. We recommend port 2000 because it is already used for normal RTP
                                                   					 media transmissions between IP phones and the router. Note Valid port
                                                         				  numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                         				  system reserves odd values.) route —(Optional) List of explicit router
                                                   					 interfaces for the IP multicast packets. ip-address-list —(Optional) List of up to four
                                                   					 explicit routes for multicast MOH. The default is that the MOH multicast stream
                                                   					 is automatically output on the interfaces that correspond to the address that
                                                   					 was configured with the ip
                                                         						  source-address command. Note For MOH on
                                                         				  internal calls, packet flow must be enabled to the subnet on which the phones
                                                         				  are located. | Note | This command
                                                         				  is required to use MOH for internal calls and it must be configured after MOH
                                                         				  is enabled with the moh command. | Note | Valid port
                                                         				  numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                         				  system reserves odd values.) | Note | For MOH on
                                                         				  internal calls, packet flow must be enabled to the subnet on which the phones
                                                         				  are located. |
| Note | This command
                                                         				  is required to use MOH for internal calls and it must be configured after MOH
                                                         				  is enabled with the moh command. |
| Note | Valid port
                                                         				  numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                         				  system reserves odd values.) |
| Note | For MOH on
                                                         				  internal calls, packet flow must be enabled to the subnet on which the phones
                                                         				  are located. |
| Step 6 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 7 | ephone phone-tag Example: Router(config)# ephone 28 | Enters
                                             				ephone configuration mode. |
| Step 8 | multicast-moh Example: Router(config-ephone)# no multicast-moh | (Optional)
                                             				Enables multicast MOH on a phone. This is the default. This
                                                   					 command is supported in Cisco Unified CME 4.0 and later versions. The no form of
                                                   					 this command disables MOH for phones that do not support multicast. Callers
                                                   					 hear a repeating tone when they are placed on hold. This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone configuration mode has priority over the value set in
                                                   					 ephone-template mode. |
| Step 9 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | This command
                                                         				  is required to use MOH for internal calls and it must be configured after MOH
                                                         				  is enabled with the moh command. |
|---|---|

| Note | Valid port
                                                         				  numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                         				  system reserves odd values.) |
|---|---|

| Note | For MOH on
                                                         				  internal calls, packet flow must be enabled to the subnet on which the phones
                                                         				  are located. |
|---|---|

| Note | If you configure
                                             			 MOH from an audio file and from a live feed, the router seeks the live feed
                                             			 first. If a live feed is found, it displaces an audio file source. If the live
                                             			 feed is not found or fails at any time, the router falls back to the audio file
                                             			 source. |
|---|---|

| Restriction | A foreign
                                                      				  exchange station (FXS) port cannot be used for a live feed. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice-port port Example: Router(config)# voice-port 1/1/0 | Enters
                                             				voice-port configuration mode. Port argument is platform-dependent; type ? to display
                                                   					 syntax. |
| Step 4 | input gain decibels Example: Router(config-voice-port)# input gain 0 | Specifies, in
                                             				decibels, the amount of gain to be inserted at the receiver side of the
                                             				interface. decibels —Acceptable values are integers –6 to 14. |
| Step 5 | auto-cut-through Example: Router(config-voice-port)# auto-cut-through | (E&M ports
                                             				only) Enables call completion when a PBX does not provide an M-lead response. MOH
                                                   					 requires that you use this command with E&M ports. |
| Step 6 | operation 4-wire Example: Router(config-voice-port)# operation 4-wire | (E&M ports
                                             				only) Selects the 4-wire cabling scheme. MOH
                                                   					 requires that you specify 4-wire operation with this command for E&M ports. |
| Step 7 | signal immediate Example: Router(config-voice-port)# signal immediate | (E&M ports
                                             				only) For E&M tie trunk interfaces, directs the calling side to seize a
                                             				line by going off-hook on its E-lead and to send address information as dual
                                             				tone multifrequency (DTMF) digits. |
| Step 8 | signal loop-start live-feed Example: Router(config-voice-port)# signal loop-start live-feed | (FXO ports
                                             				only) Enables an MOH audio stream from a live feed to be directly connected to
                                             				the router through an FXO port. This
                                                   					 command is supported in Cisco IOS Release 12.4(15)T and later releases. |
| Step 9 | no shutdown Example: Router(config-voice-port)# no shutdown | Activates
                                             				the voice port. To shut
                                                   					 the voice port down and disable MOH from a live feed, use the shutdown command. |
| Step 10 | exit Example: Router(config-voice-port)# exit | Exits
                                             				voice-port configuration mode. |
| Step 11 | dial peer voice tag pots Example: Router(config)# dial peer voice 7777 pots | Enters
                                             				dial-peer configuration mode. |
| Step 12 | destination-pattern string Example: Router(config-dial-peer)# destination-pattern 7777 | Specifies
                                             				either the prefix or the full E.164 telephone number to be used for a dial
                                             				peer. |
| Step 13 | port port Example: Router(config-dial-peer)# port 1/1/0 | Associates
                                             				the dial peer with the voice port that was specified in Step 3. |
| Step 14 | exit Example: Router(config-dial-peer)# exit | Exits
                                             				dial-peer configuration mode. |
| Step 15 | ephone-dn dn-tag Example: Router(config)# ephone-dn 55 | Enters
                                             				ephone-dn configuration mode. dn-tag —Unique sequence number that identifies this
                                                   					 ephone-dn during configuration tasks. Range is 1 to 288. |
| Step 16 | number number Example: Router(config-ephone-dn)# number 5555 | Configures a
                                             				valid extension number for this ephone-dn. This
                                                   					 number is not assigned to any phone; it is only used to make and receive calls
                                                   					 that contain an audio stream to be used for MOH. number —String of up to 16 digits that represents a
                                                   					 telephone or extension number to be associated with this ephone-dn. |
| Step 17 | moh [ out-call outcall-number ] [ ip ip-address port port-number [ route ip-address-list ]] Example: Router(config-ephone-dn)# moh out-call 7777 ip 239.10.16.8 port 2311 route 10.10.29.3 10.10.29.45 or Router(config-ephone-dn)# moh out-call 7777 | Specifies
                                             				that this ephone-dn is to be used for an incoming or outgoing call that is the
                                             				source for an MOH stream. (Optional) out-call outcall-number —Indicates that the router is
                                                   					 calling out for a live feed for MOH and specifies the number to be called.
                                                   					 Forces a connection to the local voice port that was specified in Step 3. If
                                                   					 this command is used without this keyword, the MOH stream is received from an
                                                   					 incoming call. (Optional) ip ip-address —Destination IP address for multicast. If you
                                                   					 are configuring MOH from a live feed and from an audio file for backup, do not
                                                   					 configure a multicast IP address for this command. If the live feed fails or is
                                                   					 not found, MOH will fall back to the ip address that you configured using the multicast
                                                         						  moh command in telephony-service configuration mode. See “Configuring
                                                      						Music on Hold from an Audio File” . If you
                                                   					 specify an address for multicast with this command and a different address with
                                                   					 the multicast
                                                         						  moh command in telephony-service configuration mode, you can send
                                                   					 the MOH audio stream to two multicast addresses. (Optional) port port-number —Media port for multicast. Range is
                                                   					 2000 to 65535. We recommend port 2000 because it is already used for RTP media
                                                   					 transmissions between IP phones and the router. (Optional) route ip-address -list—Indicates specific router
                                                   					 interfaces on which to transmit the IP multicast packets. Up to four IP
                                                   					 addresses can be listed. Default: The MOH multicast stream is automatically
                                                   					 output on the interfaces that correspond to the address that was configured
                                                   					 with the ip
                                                         						  source-address command. |
| Step 18 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 19 | ephone phone-tag Example: Router(config)# ephone 28 | Enters
                                             				ephone configuration mode. |
| Step 20 | multicast-moh Example: Router(config-ephone)# no multicast-moh | (Optional)
                                             				Enables multicast MOH on a phone. This is the default. This
                                                   					 command is supported in Cisco Unified CME 4.0 and later versions. The no form of
                                                   					 this command disables MOH for phones that do not support multicast. Callers
                                                   					 hear a repeating tone when they are placed on hold. This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone configuration mode has priority over the value set in
                                                   					 ephone-template mode. |
| Step 21 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Media files
                                                   				  from live-feed source are not supported. Each MOH
                                                   				  group must contain a unique flash media file name, extension numbers, and
                                                   				  multicast destination. If you enter any extension ranges, MOH filenames, and
                                                   				  multicast IP addresses that already exist in another MOH-group, an error
                                                   				  message is issued and the new input in the current voice MOH-group is
                                                   				  discarded. Media file
                                                   				  CODEC format is limited to G.711 and G.729. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice moh-group moh-group-tag Example: Router(config-telephony)# voice moh-group 1 | Enters the
                                             				voice moh-group configuration mode. You can create up to five voice moh-groups
                                             				for ephones receiving music on hold audio files when placed on hold. Range for
                                             				the voice moh-groups is 1 to 5. |
| Step 4 | description string Example: Router(config-voice-moh-group)# description moh group for sales | (Optional)
                                             				Allows you to add a brief description specific to a voice MOH group. You can
                                             				use up to 80 characters to describe the voice MOH group. |
| Step 5 | moh filename Example: Router(config-voice-moh-group)# moh flash:/minuet.au | Enables music
                                             				on hold using the specified MOH source file. The MOH file must be in .au and
                                             				.wav format. MOH filename length should not exceed 128 characters. You must
                                             				provide the directory and filename of the MOH file in URL format. For example: moh
                                                				  flash:/minuet.au If you
                                                   					 specify a file with this command and later want to use a different file, you
                                                   					 must disable use of the first file with the no moh command before configuring the second file. |
| Step 6 | multicast moh ip-address port port-number route ip-address-list Example: Router((config-voice-moh-group)# multicast moh 239.10.16.4 port 16384 route 10.10.29.17 10.10.29.33 | Specifies that
                                             				this audio stream is to be used for multicast and also for MOH. Note This
                                                      				command is required to use MOH for internal calls and it must be configured
                                                      				after MOH is enabled with the moh command. ip-address —Destination IP address for multicast. port port-number —Media port for multicast. Range is
                                                   					 2000 to 65535. We recommend port 2000 because it is already used for normal RTP
                                                   					 media transmissions between IP phones and the router. Note Valid port
                                                      				numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                      				system reserves odd values.) route —(Optional) List of explicit router
                                                   					 interfaces for the IP multicast packets. ip-address-list —(Optional) List of up to four
                                                   					 explicit routes for multicast MOH. The default is that the MOH multicast stream
                                                   					 is automatically output on the interfaces that correspond to the address that
                                                   					 was configured with the ip
                                                         						  source-address command. Note For MOH
                                                      				on internal calls, packet flow must be enabled to the subnet on which the
                                                      				phones are located. | Note | This
                                                      				command is required to use MOH for internal calls and it must be configured
                                                      				after MOH is enabled with the moh command. | Note | Valid port
                                                      				numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                      				system reserves odd values.) | Note | For MOH
                                                      				on internal calls, packet flow must be enabled to the subnet on which the
                                                      				phones are located. |
| Note | This
                                                      				command is required to use MOH for internal calls and it must be configured
                                                      				after MOH is enabled with the moh command. |
| Note | Valid port
                                                      				numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                      				system reserves odd values.) |
| Note | For MOH
                                                      				on internal calls, packet flow must be enabled to the subnet on which the
                                                      				phones are located. |
| Step 7 | extension-range starting-extension to ending-extension Example: Router(config-voice-moh-group)#extension-range 1000 to 1999 Router(config-voice-moh-group)#extension-range 2000 to 2999 | (Optional)
                                             				identifies MOH callers calling the extension numbers specified in a MOH group.
                                             				Extension number must be in hexadecimal digits (0-9) or (A-F). Both extension
                                             				numbers (starting extension and ending extension) must contain equal number of
                                             				digits. Repeat this command to add additional extension ranges. starting-extension —(Optional) Lists the starting
                                                   					 extension number for a moh-group. ending-extension —(Optional) Lists the ending
                                                   					 extension number for a moh-group. Note The
                                                      				ending extension number must be greater than or equal to the starting extension
                                                      				number. Extension-ranges must not overlap with any other extension-range
                                                      				configured in any other MOH group. Note If
                                                      				extension range is defined and a moh-group is also defined in an ephone-dn ,
                                                      				the ephone-dn parameters takes precedence. | Note | The
                                                      				ending extension number must be greater than or equal to the starting extension
                                                      				number. Extension-ranges must not overlap with any other extension-range
                                                      				configured in any other MOH group. | Note | If
                                                      				extension range is defined and a moh-group is also defined in an ephone-dn ,
                                                      				the ephone-dn parameters takes precedence. |
| Note | The
                                                      				ending extension number must be greater than or equal to the starting extension
                                                      				number. Extension-ranges must not overlap with any other extension-range
                                                      				configured in any other MOH group. |
| Note | If
                                                      				extension range is defined and a moh-group is also defined in an ephone-dn ,
                                                      				the ephone-dn parameters takes precedence. |
| Step 8 | end Example: Router(config-voice-moh-group)# end | Returns to
                                             				privileged EXEC mode. |

| Note | This
                                                      				command is required to use MOH for internal calls and it must be configured
                                                      				after MOH is enabled with the moh command. |
|---|---|

| Note | Valid port
                                                      				numbers for multicast include even numbers that range from 16384 to 32767. (The
                                                      				system reserves odd values.) |
|---|---|

| Note | For MOH
                                                      				on internal calls, packet flow must be enabled to the subnet on which the
                                                      				phones are located. |
|---|---|

| Note | The
                                                      				ending extension number must be greater than or equal to the starting extension
                                                      				number. Extension-ranges must not overlap with any other extension-range
                                                      				configured in any other MOH group. |
|---|---|

| Note | If
                                                      				extension range is defined and a moh-group is also defined in an ephone-dn ,
                                                      				the ephone-dn parameters takes precedence. |
|---|---|

| Restriction | Do not use same extension number for different MOH groups. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-dn tag Example: Router(config)# ephone-dn 1 | Enters ephone-dn configuration mode. In ephone-dn configuration mode, you assign an extension number
                                             				using the number command. You can also configure a MOH group to an ephone-dn- template for
                                             				use across a range of ephone-dns. If two different MOH groups are configured as
                                             				a result of this command, the MOH group configured under the ephone-dn
                                             				configuration takes precedence. Note MOH group configuration for ephone-template-dn configuration
                                                         				  command is temporarily prohibited when any directory number using that template
                                                         				  is on hold. | Note | MOH group configuration for ephone-template-dn configuration
                                                         				  command is temporarily prohibited when any directory number using that template
                                                         				  is on hold. |
| Note | MOH group configuration for ephone-template-dn configuration
                                                         				  command is temporarily prohibited when any directory number using that template
                                                         				  is on hold. |
| Step 4 | number Example: Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1001 | Allows you to define an extension number and associate this number to a telephone. |
| Step 5 | moh-group tag Example: Router(config-telephony)#voice moh-group 1 Router(config-voice-moh-group)# | Allows you to assign a MOH group to a directory number. MOH group tag — identifies the unique number
                                                   					 assigned to a MOH group for configuration tasks. |
| Step 6 | end Example: Router(config-ephone)# end | Returns to privileged EXEC mode. |

| Note | MOH group configuration for ephone-template-dn configuration
                                                         				  command is temporarily prohibited when any directory number using that template
                                                         				  is on hold. |
|---|---|

| Restriction | Do not use same extension number for different MOH groups. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config-telephony)# ephone-dn 1 | Enters telephony-service configuration mode. In ephone-dn configuration mode, you assign an extension number
                                             				using the number command. |
| Step 4 | internal-call moh-group tag Example: Router(config)# Router(config-telephony)# internal call moh-group 4 | Allows to assign a MOH-group for all internal directory numbers. Moh group tag — identifies the unique number
                                                   					 assigned to a MOH group for configuration tasks, Range for the tag is from 0 to
                                                   					 5, where 0 represents MOH configuration in telephony service. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to privileged EXEC mode. |

| Restriction | MOH file
                                                      				  caching is prohibited if live-feed is enabled for MOH-group 0. MOH file
                                                      				  buffer size must be larger than the MOH file (size) that needs to be cached. Sufficient
                                                      				  system memory must be available for MOH file caching. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config-telephony)# ephone-dn 1 | Enters
                                             				telephony-service configuration mode. In ephone-dn
                                             				configuration mode, you assign an extension number using the number command. |
| Step 4 | moh-file-buffer file
                                                				  size Example: Router(config-telephony)# moh-file-buffer 2000 | (Optional)
                                             				Allows to set a buffer for the MOH file size. You can configure a max file
                                             				buffer size (per file) anywhere between 64 KB (8 seconds) to 10000 KB
                                             				(approximately 20 minutes), Default moh-file-buffer size is 64 KB (8 seconds). Note A large
                                                         				  buffer size is desirable to cache the largest MOH file and a better system
                                                         				  performance. | Note | A large
                                                         				  buffer size is desirable to cache the largest MOH file and a better system
                                                         				  performance. |
| Note | A large
                                                         				  buffer size is desirable to cache the largest MOH file and a better system
                                                         				  performance. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | A large
                                                         				  buffer size is desirable to cache the largest MOH file and a better system
                                                         				  performance. |
|---|---|

| Use the show ephone
                                                				  moh command to verify if the MOH file is being cached. The
                                          			 following examples shows that the minuet.au music file in MOH group 1 is not
                                          			 cached. Follow steps a through d to verify the MOH file is being cached. Example: Router #show ephone moh
Skinny Music On Hold Status (moh-group 1)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000 If the
                                                				  file is not cached as in MOH group 1 in the above example, then check file size
                                                				  in the flash. Example: Router#dir flash:/minuet.au
Directory of flash:/minuet.au 32  -rw- 1865696  Apr 25 2009 00:47:12 +00:00  moh1.au Under
                                                				  telephony-service, configure “moh-file-buffer <file size>”. Default file
                                                				  size is 64 KB (8 seconds). Make sure you enter a larger file size to cache
                                                				  large MOH files that you may use in future. Example: Router(config)# telephony-service
Router(config-telephony)# moh-file-buffer 2000 Under
                                                				  voice moh-group <group tag>, configure “no moh”, and immediately
                                                				  configure “moh <filename>”. This allows the MOH server to read the file
                                                				  immediately from flash again. Example: Router(config-telephony)#voice moh-group 1
Router(config-voice-moh-group)#no moh
Router(config-voice-moh-group)#moh flash:/minuet.au Depending
                                                				  on the size of the file, you should see the MOH file caching after a few
                                                				  minutes (approximately, 2 minutes). Example: Router #show ephone moh
Skinny Music On Hold Status - group 1
Active MOH clients 0 (max 830), Media Clients 0
File flash:/moh1.au (cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000 Note MOH file
                                                               						caching is prohibited under the following conditions: if live feed is
                                                               						configured in moh-group 0, If file buffer size smaller than file size, or
                                                               						insufficient system memory. | Note | MOH file
                                                               						caching is prohibited under the following conditions: if live feed is
                                                               						configured in moh-group 0, If file buffer size smaller than file size, or
                                                               						insufficient system memory. |
|---|---|---|
| Note | MOH file
                                                               						caching is prohibited under the following conditions: if live feed is
                                                               						configured in moh-group 0, If file buffer size smaller than file size, or
                                                               						insufficient system memory. |

| Note | MOH file
                                                               						caching is prohibited under the following conditions: if live feed is
                                                               						configured in moh-group 0, If file buffer size smaller than file size, or
                                                               						insufficient system memory. |
|---|---|

| Step 1 | Use the show voice moh-group command to display one or the entire moh-group configuration. The following example shows all six MOH groups with extension ranges, MOH files, and multicast destination addresses. router# show voice moh-group telephony-service
 moh alaska.wav
 Moh multicast 239.1.1.1 port 16384 route 10.1.4.31 10.1.1.2
 
voice moh-group 1
 description this moh group is for sales
 moh flash:/audio?minuet.au
 multicast moh 239.1.1.1 port 16386 route 239.1.1.2 239.1.1.3
 extension-range 1000 to 1999
 extension-range 2000 to 2999
 extension-range 3000 to 3999
 extension-range 20000 to 22000
 extension-range A1000 to A1999
 
voice moh-group 2
 description (not configured)
 moh flash:/audio/hello.au
 multicast moh 239.23.4.10 port 2000
 extension-range 7000 to 7999
 extension-range 8000 to 8999
 
voice moh-group 3
 description This is for marketing
 moh flash:/happy.au
 multicast moh 239.15.10.1 port 3000
 extension-range 9000 to 9999
 
voice moh-group 4
 description (not configured)
 moh flash:/audio/sun.au
 multicast moh 239.16.12.1 port 4000
 extension-range 10000 to 19999
 
voice moh-group 5
 description (not configured)
 moh flash:/flower.wav
 multicast moh 239.12.1.2 port 5000
 extension-range 0012 to 0024
 extension-range 0934 to 0964
 
=== Total of 6 voice moh-groups === |
|---|---|
| Step 2 | Use the show ephone moh to display information about the different MOH group configured. The following example displays information about five different MOH groups. Router # show ephone moh Skinny Music On Hold Status (moh-group 1)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000
 
Skinny Music On Hold Status (moh-group 2)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/audio/hello.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.6 port 2000 via 0.0.0.0
 
Skinny Music On Hold Status (moh-group 3)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/bells.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.5 port 2000 via 0.0.0.0
 
Skinny Music On Hold Status (moh-group 4)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/3003.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.7 port 2000 via 0.0.0.0
 
Skinny Music On Hold Status (moh-group 5)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/4004.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.8 port 2000 via 0.0.0.0 |
| Step 3 | Use the show voice moh-group statistics command to display the MOH subsystem statistics information. In the following example, the MOH Group Streaming Interval Timing Statistics shows the media packet counts during streaming
                                             intervals. Each packet counter is of 32 bit size and holds a count limit of 4294967296. This means that with 20 milliseconds
                                             packet interval (for G.711), the counters will restart from 0 any time after 2.72 years (2 years 8 months). Use the clear
                                             voice moh-group statistics once in every two years to reset the packet counters. MOH Group Packet Transmission Timing Statistics shows the maximum and minimum amount of time (in microseconds) taken by the
                                             MOH groups to send out media packets. The MOH Group Loopback Interval Timing Statistics is available when loopback interface
                                             is configured as part of the multicast MOH routes as in the case of SRST. These counts are loopback packet counts within certain
                                             streaming timing intervals. router# show voice moh-group statistics MOH Group Streaming Interval Timing Statistics:
Grp#  ~19 msec     20~39      40~59      60~99     100~199   200+ msec
==== ========== ========== ========== ========== ========== ==========
 0:       25835   17559966      45148          0          0          1
 1:       19766   17572103      39079          0          0          1
 2:       32374   17546886      51687          0          0          1
 3:       27976   17555681      47289          0          0          1
 4:       34346   17542940      53659          0          0          1
 5:       14971   17581689      34284          0          0          1
 
MOH Group Packet Transmission Timing Statistics:
Grp#  max(usec)  min(usec) 
==== ========== ========== 
 0:          97          7.
 1:          95          7.
 2:          97          7.
 3:          96          7.
 4:          94          7.
 5:          67          7.
 
 MOH Group Loopback Interval Timing Statistics:
 loopback event array: svc_index=1542, free_index=1549, max_q_depth=31
 Grp#  ~19 msec     20~39      40~59      60~99     100~199   200+ msec
 ==== ========== ========== ========== ========== ========== ==========
 0:     8918821    8721527      10023          0          1          1
 1:     9007373    8635813       7184          0          1          1
 2:     8864760    8772851      12758          0          1          1
 3:     8924447    8715457      10464          0          1          1
 4:     8858393    8778957      13017          0          1          1
 5:     9005511    8639936       4919          0          1          1
 
Statistics collect time: 4 days 2 hours 5 minutes 39 seconds. |
| Step 4 | Use the clear voice moh-group statistics command to clear the display of MOH subsystem statistics information. For Example: router# clear voice moh-group statistics All moh group stats are cleared |

| Feature
                                       				  Name | Cisco Unified CME Version | Feature
                                       				  Information |
|---|---|---|
| Music on
                                       				  Hold | 12.2 | Support
                                       				  for Music on Hold from a live feed on Unified CME is introduced on the Cisco
                                       				  4000 Series Integrated Services Routers. |
| 12.2 | Support
                                       				  for Multicast Music on Hold from a live feed is introduced for SCCP to SCCP
                                       				  calls on the Cisco 4000 Series Integrated Services Routers. |
| 11.7 | Support
                                       				  for configuration of G.711 and G.729 codec format MOH file on Unified CME is
                                       				  added. |
| 8.0 | Music on
                                       				  hold from different media sources is added. |
| 4.1 | Music on
                                       				  hold for SIP phones is supported. |
| 4.0 | Music
                                                						on hold is introduced for internal calls. The
                                                						ability to disable multicast MOH per phone is introduced. |
| 3.0 | The
                                       				  ability to use a live audio feed as a multicast source is introduced. |
| 2.1 | Music on
                                       				  hold from a live audio feed is introduced for external calls. |
| 2.0 | Music on
                                       				  hold from an audio file is introduced for external calls. |