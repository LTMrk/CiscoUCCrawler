---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-common-ag-desk-mpp-6800-7800-8800-tpcc-b-cisco-ip-desk-phone-mult-531bc697aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/common/ag_desk_mpp_6800_7800_8800/tpcc_b_cisco-ip-desk-phone-multiplatform/p881_m_vido-configuration-1131.html
retrieved_at: 2026-08-21T13:46:54.207197+00:00
---

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

# Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

Updated: November 19, 2025

Chapter: Video Configuration

## Chapter: Video Configuration

# Video Configuration

## Disable Video Services

You can disable or hide all video settings on the phone to disable the video capability of the phone. When you disable video
                              services, your user can't see any video settings menu on their phone and the Video and Camera Exposure parameters don't appear
                              on the phone web page. For information on camera exposure, see Adjust the Camera Exposure .

Step 1

On the phone web page, select Admin Login > Advanced > Voice > Phone .

Step 2

Under Supplementary Services section, from the Video Serv list, select Yes to enable video services or No to disable the service.

Step 3

Click Submit All Changes to save your settings.

## Control the Video Bandwidth

If you have a busy network or have limited network resources, users may complain about video issues; for example, the video
                              may lag or suddenly stop.

By default, the phone automatically selects a bandwidth setting that balances the audio and video network requirements.

You can configure a fixed bandwidth setting to override the automatic selection, if required for your network conditions.
                              If you configure a fixed bandwidth, select a setting and adjust downwards until there is no video lag.

You can also configure the parameters in the phone configuration file with XML (cfg.xml) code.

Step 1

On the phone web page, select Admin Login > Voice > Phone .

Step 2

In the Video Configuration section, choose a bandwidth from the Bandwidth Allowance parameter to restrict the maximum amount of information that the phone can transmit or receive. For more information.

Options: Auto

- Auto

- 2 Mbps

- 1 Mbps

- 750 Kbps

- 500 Kbps

- 250 Kbps

Default: Auto

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Bandwidth_Allowance ua="na">Auto</Bandwidth_Allowance>
```

Step 3

Click Submit All Changes .

## Adjust the Camera Exposure

You can adjust the camera exposure for the ambient light in your office. Adjust the exposure to change the brightness of the
                              transmitted video.

Your users can also adjust the exposure on the phone from Applications > User Preference > Video > Exposure menu.

### Before you begin

The camera shutter must be open.

Step 1

On the phone web page, select Admin Login > Advanced > Voice > User .

Step 2

In the Video Configuration section, enter a value in the Camera Exposure field.

The exposure range is 0 to 15, and the default value is 8.

Step 3

Click Submit All Changes .

## Video Transmit Resolution Setup

Cisco IP Phone 8845 and 8865 supports the following video formats:

720p (1280x720)

WVGA (800x480)

360p (640x360)

240p (432x240)

VGA (640x480)

CIF (352x288)

SIF (352x240)

QCIF (176x144)

Cisco IP Phones that support video negotiate the best bandwidth and resolution based on the phone configuration and phone
                              screen limitations.

The next table shows the resolutions, frames per second, and video bit rate range for each of the supported video types.

Video type

Video resolution

Frames per second (fps)

Video bit rate range

720p

1280 x 720

30

1360–2500 kbps

720p

1280 x 720

15

790–1359 kbps

WVGA

800 x 480

30

660–789 kbps

WVGA

800 x 480

15

350–399 kbps

360p

640 x 360

30

400–659 kbps

360p

640 x 360

15

210–349kbps

240p

432 x 240

30

180–209kbps

240p

432 x 240

15

64–179kbps

VGA

640 x 480

30

520–1500kbps

VGA

640 x 480

15

280–519kbps

CIF

352 x 288

30

200–279 kbps

CIF

352 x 288

15

120–199 kbps

SIF

352 x 240

30

200–279 kbps

SIF

352 x 240

15

120–199 kbps

QCIF

176 x 144

30

94–119 kbps

QCIF

176 x 144

15

64–93 kbps

## Configure the Video Codec

Video codecs enable compression or decompression of digital video. You can enable or disable video codecs from the phone web
                              page.

The Cisco IP Phone 8845 and 8865 supports the H.264 High Profile packetization mode 1, Base Profile Mode 0, and Base Profile
                              packetization mode 1 codecs.

For all codecs, the Real Time Protocol (RTP) payload type is dynamic and you can configure it on the phone web page from Admin Login > Advanced > Voice > SIP > SDP Payloads Type . For more information, see SDP Payload Types .

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter,
                              see the syntax of the string in Video Codec Parameters .

Step 1

On the phone web page, select Admin Login > Advanced > Voice > Ext(n) .

Step 2

In the Video Configuration section, set up the fields as described in Video Codec Parameters .

Step 3

Click Submit All Changes .

### Video Codec Parameters

The following table defines the function and usage of the video codec parameters in the Video Configuration section under the Voice > Ext (n) tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml)
                                 with XML code to configure a parameter.

Parameter

Description

H264 BP0 Enable

Enables the H264 Base Profile 0 codec when you select Yes and disables it when you select No .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set this field to Yes or No to enable or disable the H264 BP0 codec.

Allowed values: Yes|No

Default: Yes

H264 BP1 Enable

Enables the H264 Base Profile 1 codec when you select Yes and disables it when you select No .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set this field to Yes or No to enable or disable the H264 BP1 codec.

Allowed values: Yes|No

Default: Yes

H264 HP Enable

Enables the H264 High Profile codec when you select Yes and disables it when you select No .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set this field to Yes or No to enable or disable the H264 HP codec.

Allowed values: Yes|No

Default: Yes

Encryption Method

Encryption method to be used during secured call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select your preferred encryption method from the list.

Allowed values: AES 128|AES 256 GCM

Default: AES 128

| Step 1 | On the phone web page, select Admin Login > Advanced > Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary Services section, from the Video Serv list, select Yes to enable video services or No to disable the service. |
| Step 3 | Click Submit All Changes to save your settings. |

| Step 1 | On the phone web page, select Admin Login > Voice > Phone . |
|---|---|
| Step 2 | In the Video Configuration section, choose a bandwidth from the Bandwidth Allowance parameter to restrict the maximum amount of information that the phone can transmit or receive. For more information. Options: Auto Auto 2 Mbps 1 Mbps 750 Kbps 500 Kbps 250 Kbps Default: Auto You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Bandwidth_Allowance ua="na">Auto</Bandwidth_Allowance> |
| Step 3 | Click Submit All Changes . |

| Step 1 | On the phone web page, select Admin Login > Advanced > Voice > User . |
|---|---|
| Step 2 | In the Video Configuration section, enter a value in the Camera Exposure field. The exposure range is 0 to 15, and the default value is 8. |
| Step 3 | Click Submit All Changes . |

| Video type | Video resolution | Frames per second (fps) | Video bit rate range |
|---|---|---|---|
| 720p | 1280 x 720 | 30 | 1360–2500 kbps |
| 720p | 1280 x 720 | 15 | 790–1359 kbps |
| WVGA | 800 x 480 | 30 | 660–789 kbps |
| WVGA | 800 x 480 | 15 | 350–399 kbps |
| 360p | 640 x 360 | 30 | 400–659 kbps |
| 360p | 640 x 360 | 15 | 210–349kbps |
| 240p | 432 x 240 | 30 | 180–209kbps |
| 240p | 432 x 240 | 15 | 64–179kbps |
| VGA | 640 x 480 | 30 | 520–1500kbps |
| VGA | 640 x 480 | 15 | 280–519kbps |
| CIF | 352 x 288 | 30 | 200–279 kbps |
| CIF | 352 x 288 | 15 | 120–199 kbps |
| SIF | 352 x 240 | 30 | 200–279 kbps |
| SIF | 352 x 240 | 15 | 120–199 kbps |
| QCIF | 176 x 144 | 30 | 94–119 kbps |
| QCIF | 176 x 144 | 15 | 64–93 kbps |

| Step 1 | On the phone web page, select Admin Login > Advanced > Voice > Ext(n) . |
|---|---|
| Step 2 | In the Video Configuration section, set up the fields as described in Video Codec Parameters . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| H264 BP0 Enable | Enables the H264 Base Profile 0 codec when you select Yes and disables it when you select No . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <H264_BP0_Enable_1_ ua="na">Yes</H264_BP0_Enable_1_> In the phone web interface, set this field to Yes or No to enable or disable the H264 BP0 codec. Allowed values: Yes\|No Default: Yes |
| H264 BP1 Enable | Enables the H264 Base Profile 1 codec when you select Yes and disables it when you select No . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <H264_BP1_Enable_1_ ua="na">Yes</H264_BP1_Enable_1_> In the phone web interface, set this field to Yes or No to enable or disable the H264 BP1 codec. Allowed values: Yes\|No Default: Yes |
| H264 HP Enable | Enables the H264 High Profile codec when you select Yes and disables it when you select No . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <H264_HP_Enable_1_ ua="na">Yes</H264_HP_Enable_1_> In the phone web interface, set this field to Yes or No to enable or disable the H264 HP codec. Allowed values: Yes\|No Default: Yes |
| Encryption Method | Encryption method to be used during secured call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Viedo_Encryption_Method_1_ ua="na">AES 128</Viedo_Encryption_Method_1_> In the phone web interface, select your preferred encryption method from the list. Allowed values: AES 128\|AES 256 GCM Default: AES 128 |