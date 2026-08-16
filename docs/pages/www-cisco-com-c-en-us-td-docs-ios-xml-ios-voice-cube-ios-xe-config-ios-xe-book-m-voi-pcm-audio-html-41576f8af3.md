---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-pcm-audio-html-41576f8af3
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-pcm-audio.html
retrieved_at: 2026-08-16T15:52:05.497034+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Pulse Code Modulation (PCM) Audio Capture

## Chapter: Pulse Code Modulation (PCM) Audio Capture

# Pulse Code Modulation (PCM) Audio Capture

## Feature Information for Pulse Code Modulation (PCM) Audio Capture

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Pulse Code Modulation (PCM) Audio Capture

Baseline Functionality

The PCM Capture feature is used for debugging audio quality issues.

The following commands were introduced or modified: show voice pcm capture , voice pcm capture

## Information about PCM Audio Capture

### PCM Audio Capture

The following are the enhancements to the PCM Audio Capture feature:

Separate PCM capture and Banjo logger feature so that they do not share the same data (.dat) file; they have their own data
                                       file.

One PCM call per data file is generated dynamically. The filename contains information such as voice port type and number,
                                       call ID, calling and called number, GUID, DSP channel number, and time stamp.

A user on the TDM-TDM or TDM-VoIP call can dynamically enable and disable PCM capture by entering predefined start and stop
                                       Dual Tone Multi-Frequency (DTMF) digits.

More test points or streams can be captured.

PCM capture is a CPU-intensive feature, and you must not enable several PCM capture sessions while running heavy traffic.

## How to Configure PCM Audio Capture

### Configuring PCM Audio Capture

### SUMMARY STEPS

- enable

- configure terminal

- voice pcm capture buffer number

- voice pcm capture destination url

- voice pcm capture on-demand-trigger

- voice pcm capture user-trigger-string start-string stop-string stream bitmap duration call-duration

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

voice pcm capture buffer number

#### Example:

```
Router(config)# voice pcm capture buffer 10
```

Configures the number of PCM capture buffers. The Range is from 0 to 200000. To change the PCM capture buffer size, you must
                                             first configure it with 0 and then configure it with the desired number.

Step 4

voice pcm capture destination url

#### Example:

```
Router(config)# voice pcm capture destination tftp://10.10.1.2/acphan/
```

Configures or changes the destination URL for storing captured data.

Step 5

voice pcm capture on-demand-trigger

#### Example:

```
Router(config)# voice pcm capture on-demand-trigger
```

Configures user-triggered PCM capture.

Step 6

voice pcm capture user-trigger-string start-string stop-string stream bitmap duration call-duration

#### Example:

```
Router(config)# voice pcm capture #132 #543 stream ff duration 230
```

Changes the default user trigger PCM capture start and stop string, stream, and duration.

The start and stop string must have different values.

PCM stream bitmap is in hexadecimal. The range is from 1 to FFFFFFF.

- bit 0—Rin

- bit 1—Sin

- bit 2—Sout

- bit 3—nonNLP Sout

- bit 4—fax modem in

- bit 5—fax modem out

- bit 6—from IP network to TDM earpiece direction: ASP input

- bit 7—from IP network to TDM earpiece direction: ASP output

- bit 8—NR in

- bit 9—NR out

- bit 10—from TDM mic to IP network: ASP in

- bit 11—from TDM mic to IP network: ASP out

Step 7

end

#### Example:

```
Router(config)# end
```

Returns to privileged EXEC mode.

### Verifying PCM Audio Capture

Perform this task to verify the configuration for the PCM Audio Capture feature.

### SUMMARY STEPS

- enable

- show voice pcm capture

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Step 2

show voice pcm capture

#### Example:

```
Router# show voice pcm capture PCM Capture is on and is logging to URL tftp://10.10.1.2/acphan/
50198 messages sent to URL, 0 messages dropped
Message Buffer (total:inuse:free) 200000:0:200000
Buffer Memory: 68000000 bytes, Message size: 340 bytes
```

Displays the configured PCM capture buffer and destination, number of saved messages/packets, number of dropped messages/packets,
                                             and number of buffers allocated, both used and free.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Pulse Code Modulation (PCM) Audio Capture | Baseline Functionality | The PCM Capture feature is used for debugging audio quality issues. The following commands were introduced or modified: show voice pcm capture , voice pcm capture |

| Note | PCM capture is a CPU-intensive feature, and you must not enable several PCM capture sessions while running heavy traffic. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice pcm capture buffer number Example: Router(config)# voice pcm capture buffer 10 | Configures the number of PCM capture buffers. The Range is from 0 to 200000. To change the PCM capture buffer size, you must
                                             first configure it with 0 and then configure it with the desired number. |
| Step 4 | voice pcm capture destination url Example: Router(config)# voice pcm capture destination tftp://10.10.1.2/acphan/ | Configures or changes the destination URL for storing captured data. |
| Step 5 | voice pcm capture on-demand-trigger Example: Router(config)# voice pcm capture on-demand-trigger | Configures user-triggered PCM capture. |
| Step 6 | voice pcm capture user-trigger-string start-string stop-string stream bitmap duration call-duration Example: Router(config)# voice pcm capture #132 #543 stream ff duration 230 | Changes the default user trigger PCM capture start and stop string, stream, and duration. The start and stop string must have different values. PCM stream bitmap is in hexadecimal. The range is from 1 to FFFFFFF. The stream bitmap definitions are as follows: bit 0—Rin bit 1—Sin bit 2—Sout bit 3—nonNLP Sout bit 4—fax modem in bit 5—fax modem out bit 6—from IP network to TDM earpiece direction: ASP input bit 7—from IP network to TDM earpiece direction: ASP output bit 8—NR in bit 9—NR out bit 10—from TDM mic to IP network: ASP in bit 11—from TDM mic to IP network: ASP out |
| Step 7 | end Example: Router(config)# end | Returns to privileged EXEC mode. |

| Step 1 | enable Example: Router> enable Enables privileged EXEC mode. |
|---|---|
| Step 2 | show voice pcm capture Example: Router# show voice pcm capture PCM Capture is on and is logging to URL tftp://10.10.1.2/acphan/
50198 messages sent to URL, 0 messages dropped
Message Buffer (total:inuse:free) 200000:0:200000
Buffer Memory: 68000000 bytes, Message size: 340 bytes Displays the configured PCM capture buffer and destination, number of saved messages/packets, number of dropped messages/packets,
                                             and number of buffers allocated, both used and free. |