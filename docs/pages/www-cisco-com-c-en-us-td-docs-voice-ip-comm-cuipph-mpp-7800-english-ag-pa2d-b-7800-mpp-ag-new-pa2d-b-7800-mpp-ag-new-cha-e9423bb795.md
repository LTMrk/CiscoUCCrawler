---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-ag-pa2d-b-7800-mpp-ag-new-pa2d-b-7800-mpp-ag-new-cha-e9423bb795
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/AG/pa2d_b_7800_mpp_ag_new/pa2d_b_7800_mpp_ag_new_chapter_010010.html
retrieved_at: 2026-08-21T23:21:37.276002+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Audio Configuration

## Chapter: Audio Configuration

# Audio Configuration

## Configure Different Audio Volume

You can configure the volume settings in the phone web interface.

You can also configure the parameters in the phone configuration file with XML (cfg.xml) code. To configure each parameter,
                              see the syntax of the string in the Parameters for Audio Volume table in Parameters for Audio Volume .

### Before you begin

Select Voice > User .

In the Audio Volume section, configure the volume level for audio parameters as described in the Parameters for Audio Volume table in Parameters for Audio Volume .

Click Submit All Changes .

### Parameters for Audio Volume

The following two tables describes the acoustic and audio settings.

The following table defines the function and usage of Audio Volume parameters in the Audio Volume section under the User tab
                                    in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                    code to configure a parameter.

Parameter

Description

Ringer Volume

Sets the default volume for the ringer.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Ringer_Volume ua="rw">8</Ringer_Volume>
```

In the phone web page, enter a valid value as the ringer volume.

Allowed values: an integer ranging between 0 and 15

Default: 9

Speaker Volume

Sets the default volume for the speakerphone.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Speaker_Volume ua="rw">11</Speaker_Volume>
```

In the phone web page, enter a valid value as the speaker volume.

Allowed values: an integer ranging between 0 and 15

Default: 11

Handset Volume

Sets the default volume for the handset.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Handset_Volume ua="rw">9</Handset_Volume>
```

In the phone web page, enter a valid value as the handset volume.

Allowed values: an integer ranging between 0 and 15

Default: 10

Headset Volume

Sets the default volume for the headset.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Headset_Volume ua="rw">9</Headset_Volume>
```

In the phone web page, enter a valid value as the headset volume.

Allowed values: an integer ranging between 0 and 15

Default: 10

Electronic Hookswitch Control

Enables or disables the Electronic HookSwitch (EHS) feature. After EHS is enabled, the AUX port does not output phone logs.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Ehook_Enable ua="na">Yes</Ehook_Enable>
```

In the phone web page, enter a valid value as the EHS volume.

Allowed values: Yes|No

Default: No

## Configure the Voice Codecs

A codec resource is considered allocated if it has been included in the SDP codec list of an active call, even though it eventually
                              might not be chosen for the connection. Negotiation of the optimal voice codec sometimes depends on the ability of the Cisco
                              IP Phone to match a codec name with the far-end device or gateway codec name. The phone allows the network administrator to
                              individually name the various codecs that are supported such that the correct codec successfully negotiates with the far-end
                              equipment.

The Cisco IP Phone supports voice codec priority. You can select up to three preferred codecs. The administrator can select
                              the low-bit-rate codec that is used for each line. G.711a and G.711u are always enabled.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter,
                              see the syntax of the string in Audio Codec Parameters .

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Ext(n) , where n is an extension number.

In the Audio Configuration section, configure the parameters as defined in the Audio Codec Parameters table.

Click Submit All Changes .

### Audio Codec Parameters

The following table defines the function and usage of the voice codec parameters in the Audio Configuration section under the Voice > Ext (n) tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml)
                                 with XML code to configure a parameter.

Parameter

Description

Preferred Codec

Preferred codec for all calls. The actual codec used in a call still depends on the outcome of the codec negotiation protocol.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select your preferred codec from the list.

Allowed values: G711u|G711a|G729a|G722|G722.2|iLBC|OPUS

Default: G711u

Use Pref Codec Only

Select No to use any code. Select Yes to use only the preferred codes. When you select Yes, calls fail if the far end does not support the preferred codecs.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format: <Use_Pref_Codec_Only_1_ ua="rw">No</Use_Pref_Codec_Only_1_>

In the phone web interface, set this field to Yes or No as needed.

Allowed values: Yes|No

Default: No

Second Preferred Codec

Codec to use if the codec specified in Preferred Codec fails.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select your preferred codec from the list.

Allowed values: Unspecified|G711u|G711a|G729a|G722|G722.2|iLBC|OPUS

Default: Unspecified

Third Preferred Codec

Codec to use if the codecs specified in Preferred Codec and Second Preferred Codec fail.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select your preferred codec from the list.

Allowed values: Unspecified|G711u|G711a|G729a|G722|G722.2|iLBC|OPUS

Default: Unspecified

G711u Enable

G711a Enable

G729a Enable

G722 Enable

G722.2 Enable

iLBC Enable

Enables the use of a specific codec.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<G711u_Enable_1_ ua="rw">Yes</G711u_Enable_1_>

<G711a_Enable_1_ ua="rw">Yes</G711a_Enable_1_>

<G729a_Enable_1_ ua="rw">Yes</G729a_Enable_1_>

<G722_Enable_1_ ua="rw">Yes</G722_Enable_1_>

<G722_Enable_1_ ua="rw">Yes</G722_Enable_1_>

<G722.2_Enable_1_ ua="rw">No</G722.2_Enable_1_>

<iLBC_Enable_1_ ua="rw">No</iLBC_Enable_1_>

<OPUS_Enable_1_ ua="rw">Yes</OPUS_Enable_1_>

In the phone web interface, set the corresponding field to Yes to enable the use of a specific codec, or No to disable it.

The transmit rate for the G.729a codec is at 8 kbps.

Silence Supp Enable

Enables or disables silence suppression. When set Yes , silent audio frames are not transmitted.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set this field to Yes to enable silence suppression, or No to disable it.

Allowed values: Yes|No

Default: No

DTMF Tx Method

The method for transmitting DTMF signals to the far end. The options are:

AVT—Audio video transport. Sends DTMF as AVT events.

InBand—Sends DTMF by using the audio path.

Auto—Uses InBand or AVT based on the outcome of codec negotiation.

INFO—Uses the SIP INFO method.

InBand+INFO—Uses both the audio path and the SIP INFO method.

AVT+INFO—Uses both the AVT and the SIP INFO method.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select your preferred transmitting method from the list.

Default: Auto

Codec Negotiation

When set to Default , the phone responds to an Invite with a 200 OK response advertising the preferred codec only. When set to List All , the phone responds listing all the codecs that the phone supports.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select the desired option from the list.

Allowed values: Default|List All

Default: Default

Encryption Method

Encryption method to be used during secured call. Options are AES 128 and AES 256 GCM

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select your preferred encryption method from the list.

Allowed values: AES 128 |AES 256 GCM

Default: AES 128.

## Voice Quality Reporting

You can capture voice quality metrics for Voice over Internet Protocol (VoIP) sessions with a Session Initiation Protocol
                           (SIP) event package. Voice call quality information derived from RTP and call information from SIP is conveyed from a User
                           Agent (UA) in a session (reporter) to a third party (collector).

The Cisco IP phone uses User Datagram Protocol (UDP) to send a SIP PUBLISH message to a collector server.

### Supported Scenarios for Voice Quality Reporting

Currently, only the basic call scenario supports voice quality reporting. A basic call can be a peer to peer incoming or
                              outgoing call. The phone supports periodic SIP publish message.

### Mean Opinion Scores and Codecs

The voice quality metrics use Mean Opinion Score (MOS) to rate the quality. A MOS rating of 1 is the lowest quality; a MOS
                              rating of 5 is the highest quality. The following table gives a description of some of the codecs and MOS scores. The phone
                              supports all codecs. For all codecs, the phone sends the SIP Publish message.

Codec

Complexity and Description

MOS

Minimum Call Duration for Valid MOS Value

G.711 (A-law and u-law)

Very low complexity. Supports uncompressed 64 kbps digitized voice transmission at one to ten 5 ms voice frames-per-packet.
                                          This codec provides the highest voice quality and uses the most bandwidth of any of the available codecs.

A minimum value of 4.1 indicates good voice quality.

10 seconds

G.729A

Low to medium complexity.

A minimum value of 3.5 indicates good voice quality.

30 seconds

G.729AB

Contains the same reduced complexity modifications present in the G.729A.

A minimum value of 3.5 indicates good voice quality.

30 seconds

### Configure Voice Quality Reporting

You can generate a voice quality report for each extension on the phone. The parameters for the Voice Quality Metrics (VQM)
                                 SIP Publish Message help you to:

Generate voice quality reports.

Name your reports.

Determine when your phone sends SIP Publish messages.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. See VQM SIP Publish Message Parameters

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Ext(n) , where (n) is the extension number.

In SIP Settings , enter a value for the Voice Quality Report Address parameter. You can enter either a domain name or an IP address.

You can also add a port number along with the domain name or an IP address for this parameter. If you do not enter a port
                                             number, the value of the SIP UDP Port (5060) is used by default. If the collector server URL parameter is blank, a SIP PUBLISH message is not sent out.

Enter your report name for the Voice Quality Report Group parameter.

Enter an interval, in seconds, for the Voice Quality Report Interval parameter. Example: 20 for 20-second interval reporting.

Click Submit All Changes .

#### VQM SIP Publish Message Parameters

Parameter Name

Description

Voice Quality Report Address

Allows you to enter one of the following options:

Domain Name

IP address

The SIP UDP port number along with the domain name

In the phone XML configuration file (cfg.xml), enter a string in this format:

```
<Voice_Quality_Report_Address_1_ ua="na">fake_vq_collector</Voice_Quality_Report_Address_1_>
```

Default parameter = empty (no report)

Default SIP UDP Port = 5060

Voice Quality Report Group

Allows you to enter a voice quality report name.

Your report name cannot begin with a:

hyphen (-)

semicolon (;)

space

In the phone XML configuration file (cfg.xml), enter a string in this format:

```
<Voice_Quality_Report_Group_1_ ua="na">test-group-1</Voice_Quality_Report_Group_1_>
```

Default parameter = empty (The report will use the canonical name in the form of identifier@ipAddress .)

Voice Quality Report Interval

Allows you to determine when the phones send SIP Publish messages.

If you have properly configured the Voice Quality Report Address , the SIP Publish messages can be sent:

When the call has ended or is placed on hold.

Periodically, when you enter an interval in seconds for this parameter. Example: 20 for 20-second intervals.

In the phone XML configuration file (cfg.xml), enter a string in this format:

```
<VQ_Report_Interval_1_ ua="na">20</VQ_Report_Interval_1_>
```

Default parameter = 0 (no periodic SIP Publish Message)

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Audio Volume section, configure the volume level for audio parameters as described in the Parameters for Audio Volume table in Parameters for Audio Volume . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Ringer Volume | Sets the default volume for the ringer. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Ringer_Volume ua="rw">8</Ringer_Volume> In the phone web page, enter a valid value as the ringer volume. Allowed values: an integer ranging between 0 and 15 Default: 9 |
| Speaker Volume | Sets the default volume for the speakerphone. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Speaker_Volume ua="rw">11</Speaker_Volume> In the phone web page, enter a valid value as the speaker volume. Allowed values: an integer ranging between 0 and 15 Default: 11 |
| Handset Volume | Sets the default volume for the handset. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Handset_Volume ua="rw">9</Handset_Volume> In the phone web page, enter a valid value as the handset volume. Allowed values: an integer ranging between 0 and 15 Default: 10 |
| Headset Volume | Sets the default volume for the headset. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Headset_Volume ua="rw">9</Headset_Volume> In the phone web page, enter a valid value as the headset volume. Allowed values: an integer ranging between 0 and 15 Default: 10 |
| Electronic Hookswitch Control | Enables or disables the Electronic HookSwitch (EHS) feature. After EHS is enabled, the AUX port does not output phone logs. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Ehook_Enable ua="na">Yes</Ehook_Enable> In the phone web page, enter a valid value as the EHS volume. Allowed values: Yes\|No Default: No |

| Step 1 | Select Voice > Ext(n) , where n is an extension number. |
|---|---|
| Step 2 | In the Audio Configuration section, configure the parameters as defined in the Audio Codec Parameters table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Preferred Codec | Preferred codec for all calls. The actual codec used in a call still depends on the outcome of the codec negotiation protocol. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Preferred_Codec_1_ ua="rw">G711u</Preferred_Codec_1_> In the phone web interface, select your preferred codec from the list. Allowed values: G711u\|G711a\|G729a\|G722\|G722.2\|iLBC\|OPUS Default: G711u |
| Use Pref Codec Only | Select No to use any code. Select Yes to use only the preferred codes. When you select Yes, calls fail if the far end does not support the preferred codecs. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Use_Pref_Codec_Only_1_ ua="rw">No</Use_Pref_Codec_Only_1_> In the phone web interface, set this field to Yes or No as needed. Allowed values: Yes\|No Default: No |
| Second Preferred Codec | Codec to use if the codec specified in Preferred Codec fails. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Second_Preferred_Codec_1_ ua="rw">Unspecified</Second_Preferred_Codec_1_> In the phone web interface, select your preferred codec from the list. Allowed values: Unspecified\|G711u\|G711a\|G729a\|G722\|G722.2\|iLBC\|OPUS Default: Unspecified |
| Third Preferred Codec | Codec to use if the codecs specified in Preferred Codec and Second Preferred Codec fail. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Third_Preferred_Codec_1_ ua="rw">Unspecified</Third_Preferred_Codec_1_> In the phone web interface, select your preferred codec from the list. Allowed values: Unspecified\|G711u\|G711a\|G729a\|G722\|G722.2\|iLBC\|OPUS Default: Unspecified |
| G711u Enable G711a Enable G729a Enable G722 Enable G722.2 Enable iLBC Enable | Enables the use of a specific codec. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <G711u_Enable_1_ ua="rw">Yes</G711u_Enable_1_> <G711a_Enable_1_ ua="rw">Yes</G711a_Enable_1_> <G729a_Enable_1_ ua="rw">Yes</G729a_Enable_1_> <G722_Enable_1_ ua="rw">Yes</G722_Enable_1_> <G722_Enable_1_ ua="rw">Yes</G722_Enable_1_> <G722.2_Enable_1_ ua="rw">No</G722.2_Enable_1_> <iLBC_Enable_1_ ua="rw">No</iLBC_Enable_1_> <OPUS_Enable_1_ ua="rw">Yes</OPUS_Enable_1_> In the phone web interface, set the corresponding field to Yes to enable the use of a specific codec, or No to disable it. Note The transmit rate for the G.729a codec is at 8 kbps. | Note | The transmit rate for the G.729a codec is at 8 kbps. |
| Note | The transmit rate for the G.729a codec is at 8 kbps. |
| Silence Supp Enable | Enables or disables silence suppression. When set Yes , silent audio frames are not transmitted. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Silence_Supp_Enable_1_ ua="rw">No</Silence_Supp_Enable_1_> In the phone web interface, set this field to Yes to enable silence suppression, or No to disable it. Allowed values: Yes\|No Default: No |
| DTMF Tx Method | The method for transmitting DTMF signals to the far end. The options are: AVT—Audio video transport. Sends DTMF as AVT events. InBand—Sends DTMF by using the audio path. Auto—Uses InBand or AVT based on the outcome of codec negotiation. INFO—Uses the SIP INFO method. InBand+INFO—Uses both the audio path and the SIP INFO method. AVT+INFO—Uses both the AVT and the SIP INFO method. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <DTMF_Tx_Method_1_ ua="rw">Auto</DTMF_Tx_Method_1_> In the phone web interface, select your preferred transmitting method from the list. Default: Auto |
| Codec Negotiation | When set to Default , the phone responds to an Invite with a 200 OK response advertising the preferred codec only. When set to List All , the phone responds listing all the codecs that the phone supports. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Codec_Negotiation_1_ ua="na">Default</Codec_Negotiation_1_> In the phone web interface, select the desired option from the list. Allowed values: Default\|List All Default: Default |
| Encryption Method | Encryption method to be used during secured call. Options are AES 128 and AES 256 GCM Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Encryption_Method_1_ ua="na">AES 128</Encryption_Method_1_> In the phone web interface, select your preferred encryption method from the list. Allowed values: AES 128 \|AES 256 GCM Default: AES 128. |

| Note | The transmit rate for the G.729a codec is at 8 kbps. |
|---|---|

| Codec | Complexity and Description | MOS | Minimum Call Duration for Valid MOS Value |
|---|---|---|---|
| G.711 (A-law and u-law) | Very low complexity. Supports uncompressed 64 kbps digitized voice transmission at one to ten 5 ms voice frames-per-packet.
                                          This codec provides the highest voice quality and uses the most bandwidth of any of the available codecs. | A minimum value of 4.1 indicates good voice quality. | 10 seconds |
| G.729A | Low to medium complexity. | A minimum value of 3.5 indicates good voice quality. | 30 seconds |
| G.729AB | Contains the same reduced complexity modifications present in the G.729A. | A minimum value of 3.5 indicates good voice quality. | 30 seconds |

| Step 1 | Select Voice > Ext(n) , where (n) is the extension number. |
|---|---|
| Step 2 | In SIP Settings , enter a value for the Voice Quality Report Address parameter. You can enter either a domain name or an IP address. You can also add a port number along with the domain name or an IP address for this parameter. If you do not enter a port
                                             number, the value of the SIP UDP Port (5060) is used by default. If the collector server URL parameter is blank, a SIP PUBLISH message is not sent out. |
| Step 3 | Enter your report name for the Voice Quality Report Group parameter. Your report name can't begin with a hyphen (-), semicolon (;), or a space. |
| Step 4 | Enter an interval, in seconds, for the Voice Quality Report Interval parameter. Example: 20 for 20-second interval reporting. |
| Step 5 | Click Submit All Changes . |

| Parameter Name | Description |
|---|---|
| Voice Quality Report Address | Allows you to enter one of the following options: Domain Name IP address The SIP UDP port number along with the domain name In the phone XML configuration file (cfg.xml), enter a string in this format: <Voice_Quality_Report_Address_1_ ua="na">fake_vq_collector</Voice_Quality_Report_Address_1_> Default parameter = empty (no report) Default SIP UDP Port = 5060 |
| Voice Quality Report Group | Allows you to enter a voice quality report name. Your report name cannot begin with a: hyphen (-) semicolon (;) space In the phone XML configuration file (cfg.xml), enter a string in this format: <Voice_Quality_Report_Group_1_ ua="na">test-group-1</Voice_Quality_Report_Group_1_> Default parameter = empty (The report will use the canonical name in the form of identifier@ipAddress .) |
| Voice Quality Report Interval | Allows you to determine when the phones send SIP Publish messages. If you have properly configured the Voice Quality Report Address , the SIP Publish messages can be sent: When the call has ended or is placed on hold. Periodically, when you enter an interval in seconds for this parameter. Example: 20 for 20-second intervals. In the phone XML configuration file (cfg.xml), enter a string in this format: <VQ_Report_Interval_1_ ua="na">20</VQ_Report_Interval_1_> Default parameter = 0 (no periodic SIP Publish Message) |