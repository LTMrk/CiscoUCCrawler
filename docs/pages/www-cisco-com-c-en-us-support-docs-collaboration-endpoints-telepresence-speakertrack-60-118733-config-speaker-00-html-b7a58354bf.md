---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-telepresence-speakertrack-60-118733-config-speaker-00-html-b7a58354bf
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/telepresence-speakertrack-60/118733-config-speaker-00.html
retrieved_at: 2026-09-08T01:56:20.742030+00:00
---

Configure Speaker Track with SX80 Codec

# Configure Speaker Track with SX80 Codec

### Download Options

Updated: October 6, 2021

Document ID: 118733

Contents

## Contents

## Introduction

This document describes how to install and configure Speaker Track with an SX80 setup.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- SX80 codec

- Precision 60 cameras

- Speaker Track unit

- High-Definition Multimedia Interface ( HDMI ) cables

- RJ45 cables

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Diagrams

Cable Diagram of Speaker Track Connected to an SX80 Codec

Complete these steps in order to install the equipment:

- Configure the SX80 codec.

- Connect an RJ45 cable from Network port 2,3 to the network port of the Speaker Track.

- Connect the HDMI cables from each camera to the HDMI Input port on the codec.

- Connect power to the Speaker Track.

- Connect an RJ45 cable from each camera to the respective network port on the Speaker Track .

- Connect power cables from each camera to the Speaker Track .

### Enable the Speaker Track

When the cabling is complete, ensure that the Speaker Track configuration is set correctly.

```
xConfiguration Cameras SpeakerTrack ConnectorDetection CameraLeft: 1 Configuration Cameras SpeakerTrack ConnectorDetection CameraRight: 2 xConfiguration Cameras SpeakerTrack ConnectorDetection Mode: Auto xConfiguration Cameras SpeakerTrack Mode: Auto xConfiguration Cameras SpeakerTrack TrackingMode: Default xCommand Cameras SpeakerTrack Activate
```

## Verify

Use this section in order to confirm that your configuration works properly.

- Codec - TC7.3.0

- Speaker Track- MT7.3.0

- Precision60- HC7.3.0

- Ensure the codec, Speaker Track, and camera use the same software version (numbers) suffix.

```
xstatus Camera *s Camera 1 HardwareID: "55000000" *s Camera 1 IpAddress: "169.254.1.43" *s Camera 1 MacAddress: "E4:C7:22:65:3F:D3" *s Camera 1 Manufacturer: "Cisco" *s Camera 1 Model: "Precision 60 Camera" *s Camera 1 Position Focus: 4200 *s Camera 1 Position Pan: 3600 *s Camera 1 Position Tilt: -650 *s Camera 1 Position Zoom: 4128 *s Camera 1 SerialNumber: " FTT181100R5 " *s Camera 1 SoftwareID: " HC7.3.0 .8cb420c, 2014-12-12" *s Camera 2 HardwareID: "55000000" *s Camera 2 IpAddress: "169.254.1.44" *s Camera 2 MacAddress: "E4:C7:22:65:3F:EE" *s Camera 2 Manufacturer: "Cisco" *s Camera 2 Model: "Precision 60 Camera" *s Camera 2 Position Focus: 0 *s Camera 2 Position Pan: 3600 *s Camera 2 Position Tilt: -650 *s Camera 2 Position Zoom: 0 *s Camera 2 SerialNumber: " FTT181100R1 " *s Camera 2 SoftwareID: " HC7.3.0 .8cb420c, 2014-12-12"
```

```
xstatus // speakerTrack *s Cameras SpeakerTrack Availability: Available *s Cameras SpeakerTrack LeftCamera VideoInputConnector: 1 *s Cameras SpeakerTrack RightCamera VideoInputConnector: 2 *s Cameras SpeakerTrack Status: Active
```

```
xstatus // Peripherals *s Peripherals ConnectedDevice 1045 Name: "SpeakerTrack 60" *s Peripherals ConnectedDevice 1045 SoftwareInfo: " MT7.3 .0.8cb420c" *s Peripherals ConnectedDevice 1045 Status: Connected *s Peripherals ConnectedDevice 1045 Type: SpeakerTracker
```

## Troubleshoot

This section provides the information you can use in order to troubleshoot your configuration.

Verify the Speaker Track status in order to ensure the cabling is set correctly.

```
xstatus // speakerTrack *s Cameras SpeakerTrack Availability: Available *s Cameras SpeakerTrack LeftCamera VideoInputConnector: 1 *s Cameras SpeakerTrack RightCamera VideoInputConnector: 2 *s Cameras SpeakerTrack Status: Active
```

Here is a brief description of the previous output:

*s Cameras SpeakerTrack Availability can have one of these states:

- Off

- Unavailable

- Available

Each of the states has a different meaning:

- *s Cameras SpeakerTrack Availability: Off - this means that the Speaker Track option is turned off from the configuration.

- *s Cameras SpeakerTrack Status: Unavailable - this means that the Control (Speaker Track/Camera) has an issue.

- * s Cameras SpeakerTrack Availability: Available - this means that the control cabling is set correctly.

*s Cameras SpeakerTrack LeftCamera VideoInputConnector: 1 *s Cameras SpeakerTrack RightCamera VideoInputConnector: 2

This status depicts the HDMI connection of the camera to the codec. The previous status is the expected output if the connection is correct.

If the HDMI cable from the Left camera is unplugged, the status changes to:

```
*s Cameras SpeakerTrack LeftCamera VideoInputConnector: 0 *s Cameras SpeakerTrack RightCamera VideoInputConnector: 2
```

If the HDMI cable from the Right camera is unplugged, the status changes to:

```
*s Cameras SpeakerTrack LeftCamera VideoInputConnector: 1 *s Cameras SpeakerTrack RightCamera VideoInputConnector: 0
```

This might cause the Speaker Track to not function.

*s Cameras SpeakerTrack Status: Inactive

The user has selected Manual Tracking and Auto Tracking has been disabled from the Touch Panel. This can be enabled with the xCommand Cameras SpeakerTrack Activate command.

### Diagnostics

In order to verify the functionality of the face detection mechanism, enter this command to start the Active speaker and face detection:

```
xCommand Experimental SpeakerTrack Diagnostics Start Tracking: On
```

The next command is valid for TC releases. As of CE8, the experimental command has been replaced with this command:

xCommand Cameras SpeakerTrack Diagnostics Start Tracking: <on, off=""></on,>

Here is the meaning of the parameters shown on the screen when the Speaker Tracker diagnostics is enabled:

F (local voice) – If you talk locally this is been closed to 100%.

T (local non-noise) – It is close to 100% - close to 0% means that a lot of noise (non-voice) has been picked up.

E (far end voice) – If the far end speaks, it is not tracked.

C (cameras moving) – a high number means a lot of switching.

U (ultrasound) – Needs to be low. Ultrasound can interfere. Ultrasound is been detected when Cisco Proximity is been used.

N (silence) - 100% means no audio was picked up.

S (audio sample) – number of samples from the sound algorithm. This needs to be somewhere around 177-182.

You can also check the video Enabling SpeakerTrack Diagnostics for more reference.

### Logs

View these logs at the time of Speaker Track installation.

Endpoint captures the logs at the time of the Camera and Speaker Track Pairing.

```
15342.61 CAMERA I: PairingStatus Starting: 1 Paired: 1 Connected : 1 15342.61 CAMERA I: PairingStatus MacAddr: 'E4:C7:22:65:3F:D3' Ipv4: '' Ipv6: '' Ipv6Global: 'fe80::e6c7:22ff:fe65:3fd3' 15342.78 CAMERA I: PairingStatus Starting: 1 Paired: 1 Connected : 1 15342.79 CAMERA I: PairingStatus MacAddr: 'E4:C7:22:65:3F:EE' Ipv4: '' Ipv6: '' Ipv6Global: 'fe80::e6c7:22ff:fe65:3fee' 15342.81 SpeakerTrack I: Peripheral C0:67:AF:58:B8:2D does not need SW upgrade 15342.90 CAMERA I: PairingStatus Starting: 0 Paired: 1 Connected : 1 15342.90 CAMERA I: PairingStatus MacAddr: 'E4:C7:22:65:3F:D3' Ipv4: '' Ipv6: '' Ipv6Global: 'fe80::e6c7:22ff:fe65:3fd3'
```

The connected status shows that the Speaker Track is successfully installed.

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

2.0

06-Oct-2021

Initial Release

1.0

16-Jan-2015

Initial Release

### Contributed by Cisco Engineers

Amrinder Singh

Cisco TAC Engineer

### This Document Applies to These Products

- SpeakerTrack 60

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 06-Oct-2021 | Initial Release |
| 1.0 | 16-Jan-2015 | Initial Release |