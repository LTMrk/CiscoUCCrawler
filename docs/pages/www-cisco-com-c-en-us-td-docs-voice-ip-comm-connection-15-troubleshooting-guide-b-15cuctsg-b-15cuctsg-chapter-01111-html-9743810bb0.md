---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-01111-html-9743810bb0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_01111.html
retrieved_at: 2026-08-17T02:39:19.001677+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Audio Quality

## Chapter: Troubleshooting Audio Quality

# Troubleshooting Audio Quality

Troubleshooting Audio Quality

## Troubleshoot Audio Quality Using Check Telephony Configuration Test

The Check Telephony Configuration test does not test IPv6 connectivity. (IPv6 is supported in Cisco Unity Connection for Cisco
                                       Unified Communications Manager integrations.) The test confirms that Unity Connection can communicate with the phone system
                                       using IPv4 addressing.

### Using the Check
                           	 Telephony Configuration Test to Troubleshoot Audio Quality

Step 1

In Cisco Unity Connection Administration, in the Related Links
                                          			 box in the upper right corner of any Telephony Integrations page, select Check Telephony Configuration and select Go .

If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, run the test again.

Step 2

In the Task Execution Results window, select Close .

## Problem with Choppy Audio

Use the troubleshooting information in this section if the audio you hear from Unity Connection is choppy. Consider the following
                           possible causes:

The hard disk from which Unity Connection is playing a recording is full. To resolve the situation, eliminate unnecessary
                                 files from the hard disk.

The network Unity Connection to the Unity Connection server is not adequate. To resolve the situation, improve the network
                                 Unity Connection.

The Unity Connection platform has a malfunctioning component. To resolve the situation, identify the malfunctioning hardware
                                 component, then repair or replace it.

Another process is using too much CPU time. To resolve the situation, stop the process and run it when phone traffic is lighter.

You can check if there are any VMware snapshots. If yes, remove the snapshots.

Stratum of NTP should be less than 5. You can check the stratum using the utils ntp status command.

Toggle the settings for Audio Normalization for Recordings and Messages and Noise Reduction Settings on port group > Advanced
                                 Settings page.

## Problem with Garbled Recordings

Use the troubleshooting information in this section if recordings sound garbled. See the following possible scenarios:

The audio stream sounded garbled when Unity Connection created the recording. See the “Troubleshooting a Garbled Audio Stream in the Network” section on page 16-2 .

The audio stream did not sound garbled when Unity Connection created the recording, but became garbled later. See the “Troubleshooting How Unity Connection Makes Recordings” section on page 16-2 .

### Troubleshooting a Garbled Audio Stream in the Network

When the audio stream is garbled when Unity Connection created the recording, use the following task list to determine the
                              cause and to resolve the problem.

Follow the tasks to troubleshoot a garbled audio stream in the network:

Confirm that the Unity Connection to the caller is clear. Calls that have bad PSTN connections or calls from mobile phones
                                    may sometimes have garbled audio streams. Unity Connection cannot correct for a garbled audio stream.

Determine whether the garbled audio stream is caused by problems with the network. Use network analysis tools to do the following:

Check for latency, packet loss, and so on.

Search for devices on the network that are causing garbled audio streams. Some examples are routers, gateways, transcoders,
                                          and gateways that are configured for one packet size (such as G.711 30ms) while Unity Connection is configured for another
                                          packet size (such as G.711 20ms).

Determine whether the audio stream is garbled at the closest point to the Unity Connection server by obtaining a sniffer capture
                                    at that point. If the audio stream from the sniffer capture is not garbled, Unity Connection may not be handling the audio
                                    stream correctly. See the “Troubleshooting How Unity Connection Makes Recordings” section on page 16-2 .

### Troubleshooting
                           	 How Unity Connection Makes Recordings

When the audio stream did not sound garbled when Unity
                              		Connection created the recording, but became garbled later, use the following
                              		task list to determine the cause and to resolve the problem.

Follow the tasks to troubleshoot how Unity Connection makes
                              		recordings:

Enable the Media (Wave) Traces macro traces in Cisco Unity
                                    			 Connection Serviceability. For detailed instructions on enabling the macro
                                    			 trace and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting .

Obtain a snapshot of CPU usage on the Unity Connection server
                                    			 using the CPU and Memory display in the Real-Time Monitoring Tool (RTMT). For
                                    			 detailed information on using RTMT, see the applicable Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Contact Cisco TAC.

## Problem with
                        	 Garbled Prompts on Phone

When Unity Connection prompts sound garbled or
                           		jittery when heard on the phone, use the following task list to determine the
                           		cause and to resolve the problem.

Follow the tasks to troubleshoot garbled prompts on the phone:

Determine whether the audio stream is garbled at the closest
                                 			 point to the phone by obtaining a sniffer capture at that point. If the audio
                                 			 stream from the sniffer capture is not garbled, the cause may be in the network
                                 			 or with Unity Connection.

Determine whether the garbled audio stream is caused by problems
                                 			 with the network. Use network analysis tools to do the following:

Check for latency, packet loss, and so on.

Search for devices on the network that are causing garbled audio
                                       				  streams. Some examples are routers, gateways, transcoders, and gateways that
                                       				  are configured for one packet size (such as G.711 30ms) while Unity Connection
                                       				  is configured for another packet size (such as G.711 20ms).

Determine whether the audio stream is garbled at the closest
                                 			 point to the Unity Connection server by obtaining a sniffer capture at that
                                 			 point. If the audio stream from the sniffer capture is not garbled, Unity
                                 			 Connection may not be handling the audio stream correctly.

Enable the Media (Wave) Traces macro traces in Cisco Unity
                                 			 Connection Serviceability. For detailed instructions on enabling the macro
                                 			 trace and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting .

Obtain a snapshot of CPU usage on the Unity Connection server
                                 			 using the CPU and Memory display in the Real-Time Monitoring Tool (RTMT). For
                                 			 detailed information on using RTMT, see the applicable Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Contact Cisco TAC.

## Problem with
                        	 Volume of Recordings

Use the troubleshooting information in this
                           		section if the volume of recordings is too loud or too soft, or if the
                           		recordings do not have any sound. Consider the following:

Verify the audio level at each hardware point in the network by
                                 			 obtaining a sniffer capture at each point.

If the audio level from the sniffer capture at one point is too
                                       				  soft or too loud, the cause may be the configuration of the hardware (such as
                                       				  routers, gateways, transcoders) at that point. Check the automatic gain control
                                       				  (AGC) settings for the applicable hardware.

If the audio level from the sniffer capture at all points is too
                                       				  loud or too soft, see the “Changing
                                          					 the Volume for Unity Connection Recordings” section .

Disable automatic gain control (AGC) for Unity Connection so
                                 			 that Unity Connection does not automatically adjust the volume of recordings.
                                 			 See the “Disabling
                                    				Automatic Gain Control (AGC) for Unity Connection” section .

If the recordings do not have any sound, confirm that the
                                 			 advertised codec settings are correct. See the Confirming the Advertised Codec Settings .

### Changing the
                           	 Volume for Unity Connection Recordings

Step 1

In Cisco Unity Connection Administration, expand System Settings > and select General Configuration .

Step 2

On the Edit General Configuration page, in the Automatic Gain
                                          			 Control (AGC) Target Decibels field, enter the applicable number and select
                                          			 Save.

AGC decibel levels are set in negative numbers. For example, –26
                                                         				  db is louder than –45 db.

### Disabling
                           	 Automatic Gain Control (AGC) for Unity Connection

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations > and select Port Group . On the Search Port Groups page, select
                                          			 the name of the applicable port group.

Step 2

On the Port Group Basics page, in the Edit menu, select Advanced Settings .

Step 3

On the Edit Advanced Settings page, under Automatic Gain Control
                                          			 (AGC) Settings, uncheck the Enable AGC check box and select Save .

### Confirming the Advertised Codec Settings

#### Verifying the
                              	 Advertised Codec Settings

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group . On the Search Port Groups page, select
                                             			 the name of the applicable port group.

Step 2

On the Port Group Basics page, under Advertised Codec Settings,
                                             			 determine whether the list of codecs is correct.

Step 3

If the list is correct, skip to Step 7 . Otherwise,
                                             			 select Change Advertising .

Step 4

Select the Up and Down arrows to change the order of the codecs or to
                                             			 move codecs between the Advertised Codec box and the Unadvertised Codecs box.

If only one codec is in the Advertised Codecs box, Unity
                                                				Connection sends the audio stream in that audio format. If the phone system
                                                				does not use this audio format, the phone system drops the call.

If two or more codecs are in the Advertised Codecs box, Unity
                                                				Connection advertises its preference for the first codec in the list but sends
                                                				the audio stream in the audio format from the list that the phone system
                                                				selects.

Step 5

Select Save .

Step 6

On the Edit menu, select Port Group Basics .

Step 7

On the Search Port Groups page, if you want to change the packet
                                             			 size that is used by the advertised codecs, under Advertised Codec Settings,
                                             			 select the applicable packet setting for each codec and select Save .

## Using Traces to
                        	 Troubleshoot Audio Quality Issues

You can use traces to
                           		troubleshoot audio quality issues. For detailed instructions on enabling the
                           		applicable traces and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting .

| Note | The Check Telephony Configuration test does not test IPv6 connectivity. (IPv6 is supported in Cisco Unity Connection for Cisco
                                       Unified Communications Manager integrations.) The test confirms that Unity Connection can communicate with the phone system
                                       using IPv4 addressing. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, in the Related Links
                                          			 box in the upper right corner of any Telephony Integrations page, select Check Telephony Configuration and select Go . If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, run the test again. |
|---|---|
| Step 2 | In the Task Execution Results window, select Close . |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > and select General Configuration . |
|---|---|
| Step 2 | On the Edit General Configuration page, in the Automatic Gain
                                          			 Control (AGC) Target Decibels field, enter the applicable number and select
                                          			 Save. Note AGC decibel levels are set in negative numbers. For example, –26
                                                         				  db is louder than –45 db. | Note | AGC decibel levels are set in negative numbers. For example, –26
                                                         				  db is louder than –45 db. |
| Note | AGC decibel levels are set in negative numbers. For example, –26
                                                         				  db is louder than –45 db. |

| Note | AGC decibel levels are set in negative numbers. For example, –26
                                                         				  db is louder than –45 db. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations > and select Port Group . On the Search Port Groups page, select
                                          			 the name of the applicable port group. |
|---|---|
| Step 2 | On the Port Group Basics page, in the Edit menu, select Advanced Settings . |
| Step 3 | On the Edit Advanced Settings page, under Automatic Gain Control
                                          			 (AGC) Settings, uncheck the Enable AGC check box and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group . On the Search Port Groups page, select
                                             			 the name of the applicable port group. |
|---|---|
| Step 2 | On the Port Group Basics page, under Advertised Codec Settings,
                                             			 determine whether the list of codecs is correct. |
| Step 3 | If the list is correct, skip to Step 7 . Otherwise,
                                             			 select Change Advertising . |
| Step 4 | Select the Up and Down arrows to change the order of the codecs or to
                                             			 move codecs between the Advertised Codec box and the Unadvertised Codecs box. If only one codec is in the Advertised Codecs box, Unity
                                                				Connection sends the audio stream in that audio format. If the phone system
                                                				does not use this audio format, the phone system drops the call. If two or more codecs are in the Advertised Codecs box, Unity
                                                				Connection advertises its preference for the first codec in the list but sends
                                                				the audio stream in the audio format from the list that the phone system
                                                				selects. |
| Step 5 | Select Save . |
| Step 6 | On the Edit menu, select Port Group Basics . |
| Step 7 | On the Search Port Groups page, if you want to change the packet
                                             			 size that is used by the advertised codecs, under Advertised Codec Settings,
                                             			 select the applicable packet setting for each codec and select Save . |