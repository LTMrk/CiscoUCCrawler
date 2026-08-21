---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-english-userguide-w88x-b-wireless-8821-8821ex-user-guide-w88x-b--283cd8271b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/english/userguide/w88x_b_wireless-8821-8821ex-user-guide/w88x_b_wireless-8821-8821ex-user-guide_chapter_01000.html
retrieved_at: 2026-08-21T01:57:29.588921+00:00
---

Cisco Wireless IP Phone 8821 and 8821-EX User Guide

# Cisco Wireless IP Phone 8821 and 8821-EX User Guide

Updated: June 28, 2016

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## General Troubleshooting

You can troubleshoot some general problems with your phone. If your problem is not discussed below, contact your administrator.

Symptom

Explanation

You cannot complete a call

One or more of the following factors might apply:

Your phone is out of the wireless network access point service area.

When roaming with your phone, a green blinking light indicates that the phone is still within the wireless service coverage
                                                            area.

You must log in to the Extension Mobility service.

You must enter a client matter code or forced authorization code after you dial a number.

Your phone has time-of-day restrictions that prevent you from using some features during certain hours of the day.

The main screen is not active

One of these messages appears on the status line:

Network busy : Not enough available bandwidth exists in wireless network to complete this call. Try again later.

Leaving service area : Phone is out of range of its associated access point and wireless network.

Locating network services : Phone is searching for a wireless network access point.

Authentication failed : Authentication server did not accept the security credentials.

Configuring IP : Phone is waiting for DHCP to assign an IP address.

The Settings menu is unresponsive

Your administrator might have disabled
                                          						access to the Settings app on your phone.

Conference fails

Conference requires multiple
                                          						selected calls. Be sure that you have selected at least one call in addition to
                                          						the active call, which is selected automatically. Conference also requires the selected calls
                                          						to be on the same line. If necessary, transfer calls to one line before joining
                                          						them.

The softkey that you want to use does not appear

One or more of the following factors might apply:

You must press More to reveal additional functions.

You must change the line state (for example, place a call or have a connected call).

Your phone is not configured to support the feature associated with that softkey.

Call back fails

The other party might have call forwarding enabled.

The phone shows an error message when you attempt
                                          						to set up Call Forward All

Your phone may reject your attempt to set up Call
                                          						Forward All directly on the phone if the target number that you enter would
                                          						create a Call Forward All loop or would exceed the maximum number of links
                                          						permitted in a Call Forward All chain (also known as a maximum hop count).

## Find Information About Your Phone

Your administrator may ask for information about your phone. This information uniquely identifies the phone for troubleshooting
                              purposes. 
                              		 The information in the menu is read-only. For more information about the menu, see the Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager .

Access the Settings app.

Select Phone information .

## Hardware Diagnostics

You can run some diagnostic tests on your phone.

### Perform Audio Diagnostics

You can check that the audio on your phone is working correctly.

Access the Settings app.

Select Admin settings > Diagnostics > Audio .

Listen to the tone on the handset speaker.

Press the Speaker button to turn on handsfree, and listen to the tone.

Plug in a wired headset and listen to the tone.

### Perform Keypad Diagnostics

You can check that the keypad on your phone is working correctly.

Access the Settings app.

Select Admin settings > Diagnostics > Keypad .

Press any key to check if it works correctly.

### Perform WLAN Diagnostics

You can check the Wi-Fi connection for your phone. The phone lists the access points in order, from the strongest signal to
                                 the weakest or offline access point. You can then view details of the wireless access point.

Access the Settings app.

Select Admin settings > Diagnostics > WLAN .

Press Continue .

Scroll to an access point and press Select to see detailed information about the access point.

#### WLAN Diagnostics Fields

The following table describes the fields in the WLAN Diagnostics screen.

Field

Description

AP name

Name of the access point (AP) to which the phone is associated

BSSID

The access point radio MAC address

SSID

The Service Set Identifier (SSID) that the phone uses

Frequency

The frequency that the phone uses

Current channel

The channel that the phone uses

Last RSSI

Last Received Signal Strength Indicator (RSSI) that the phone received.

Beacon interval

Number of time units between beacons. A time unit is 1.024 milliseconds.

Capability

802.11 capabilities

Basic rates

Data rates required by the AP at which the station must be capable of operating.

Optional rates

Data rates supported by the AP that are optional for the station to operate at.

Supported HT MCS

802.11n data rates

Supported VHT (rx) rates

802.11ac receive data rates

Supported VHT (tx) rates

802.11ac transmit data rates

DTIM period

Delivery Traffic Indication Map (DTIM) information

Country code

A two-digit country code. Country information might not be displayed if the country information element (IE) is not present
                                                in the beacon.

Channels

List of supported channels (from the country IE).

Power constraint

802.11h power constraint offset in dB

Power limit

Dynamic Transmit Power Control (DTCP) value advertised by the access point.

Channel utilization

Percentage of time, normalized to 255, in which the AP sensed the medium was busy, as indicated by the physical or virtual
                                                carrier sense (CS) mechanism.

Station count

Total number of spanning tree algorithms (STAs) currently associated with this BSS.

Admission capacity

An unsigned integer that specifies the remaining amount of medium time available through explicit admission control, in units
                                                of 32 microseconds per second.

WMM supported

Support for Wi-Fi Multimedia Extensions.

UAPSD supported

Unscheduled Automatic Power Save Delivery (UAPSD) is supported by the AP. May only be available if WMM is supported. This
                                                feature is critical to talk time and achieving maximum call density on the wireless IP phone.

Proxy ARP

CCX-compliant AP supports responding to IP ARP requests on behalf of the associated station. This feature is critical to standby
                                                time on the wireless IP phone.

CCX version

Version of CCX if the AP is CCX compliant.

AC: Best effort, AC: Background, AC: Video, and AC: Audio

Admission control

AIFSN

ECWMin

ECWMax

TXOpLimit

Information for each Access Category (AC). There is one set of data for best effort, background, video, and audio.

Admission control—If yes, admission control must be used prior to transmission using the access parameters specific for this
                                                      AC.

AIFSN—Number of slots after an SIFS duration a non-AP STA should defer before invoking a backoff or starting a transmission.

ECWMin—Encodes value of CWmin in an exponent form to provide the minimum amount of time in a random backoff.

ECWMax—Encodes value of CWmax in an exponent form to provide the maximum amount of time in a random backoff.

TXOpLimit—Interval of time in which a particular quality of service (QoS) station has the right to initiate

## Create a Problem Report from the Phone

If you encounter a problem with your phone, you can generate a problem report from the phone.

Access the Settings app.

Select Phone information > Report problem .

Press Submit .

When the success message is displayed, notify your administrator that a problem report is available.

| Symptom | Explanation |
|---|---|
| You cannot complete a call | One or more of the following factors might apply: Your phone is out of the wireless network access point service area. Note When roaming with your phone, a green blinking light indicates that the phone is still within the wireless service coverage
                                                            area. You must log in to the Extension Mobility service. You must enter a client matter code or forced authorization code after you dial a number. Your phone has time-of-day restrictions that prevent you from using some features during certain hours of the day. | Note | When roaming with your phone, a green blinking light indicates that the phone is still within the wireless service coverage
                                                            area. |
| Note | When roaming with your phone, a green blinking light indicates that the phone is still within the wireless service coverage
                                                            area. |
| The main screen is not active | One of these messages appears on the status line: Network busy : Not enough available bandwidth exists in wireless network to complete this call. Try again later. Leaving service area : Phone is out of range of its associated access point and wireless network. Locating network services : Phone is searching for a wireless network access point. Authentication failed : Authentication server did not accept the security credentials. Configuring IP : Phone is waiting for DHCP to assign an IP address. |
| The Settings menu is unresponsive | Your administrator might have disabled
                                          						access to the Settings app on your phone. |
| Conference fails | Conference requires multiple
                                          						selected calls. Be sure that you have selected at least one call in addition to
                                          						the active call, which is selected automatically. Conference also requires the selected calls
                                          						to be on the same line. If necessary, transfer calls to one line before joining
                                          						them. |
| The softkey that you want to use does not appear | One or more of the following factors might apply: You must press More to reveal additional functions. You must change the line state (for example, place a call or have a connected call). Your phone is not configured to support the feature associated with that softkey. |
| Call back fails | The other party might have call forwarding enabled. |
| The phone shows an error message when you attempt
                                          						to set up Call Forward All | Your phone may reject your attempt to set up Call
                                          						Forward All directly on the phone if the target number that you enter would
                                          						create a Call Forward All loop or would exceed the maximum number of links
                                          						permitted in a Call Forward All chain (also known as a maximum hop count). |

| Note | When roaming with your phone, a green blinking light indicates that the phone is still within the wireless service coverage
                                                            area. |
|---|---|

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Phone information . |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Diagnostics > Audio . |
| Step 3 | Listen to the tone on the handset speaker. |
| Step 4 | Press the Speaker button to turn on handsfree, and listen to the tone. |
| Step 5 | Plug in a wired headset and listen to the tone. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Diagnostics > Keypad . |
| Step 3 | Press any key to check if it works correctly. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Diagnostics > WLAN . |
| Step 3 | Press Continue . |
| Step 4 | Scroll to an access point and press Select to see detailed information about the access point. |

| Field | Description |
|---|---|
| AP name | Name of the access point (AP) to which the phone is associated |
| BSSID | The access point radio MAC address |
| SSID | The Service Set Identifier (SSID) that the phone uses |
| Frequency | The frequency that the phone uses |
| Current channel | The channel that the phone uses |
| Last RSSI | Last Received Signal Strength Indicator (RSSI) that the phone received. |
| Beacon interval | Number of time units between beacons. A time unit is 1.024 milliseconds. |
| Capability | 802.11 capabilities |
| Basic rates | Data rates required by the AP at which the station must be capable of operating. |
| Optional rates | Data rates supported by the AP that are optional for the station to operate at. |
| Supported HT MCS | 802.11n data rates |
| Supported VHT (rx) rates | 802.11ac receive data rates |
| Supported VHT (tx) rates | 802.11ac transmit data rates |
| DTIM period | Delivery Traffic Indication Map (DTIM) information |
| Country code | A two-digit country code. Country information might not be displayed if the country information element (IE) is not present
                                                in the beacon. |
| Channels | List of supported channels (from the country IE). |
| Power constraint | 802.11h power constraint offset in dB |
| Power limit | Dynamic Transmit Power Control (DTCP) value advertised by the access point. |
| Channel utilization | Percentage of time, normalized to 255, in which the AP sensed the medium was busy, as indicated by the physical or virtual
                                                carrier sense (CS) mechanism. |
| Station count | Total number of spanning tree algorithms (STAs) currently associated with this BSS. |
| Admission capacity | An unsigned integer that specifies the remaining amount of medium time available through explicit admission control, in units
                                                of 32 microseconds per second. |
| WMM supported | Support for Wi-Fi Multimedia Extensions. |
| UAPSD supported | Unscheduled Automatic Power Save Delivery (UAPSD) is supported by the AP. May only be available if WMM is supported. This
                                                feature is critical to talk time and achieving maximum call density on the wireless IP phone. |
| Proxy ARP | CCX-compliant AP supports responding to IP ARP requests on behalf of the associated station. This feature is critical to standby
                                                time on the wireless IP phone. |
| CCX version | Version of CCX if the AP is CCX compliant. |
| AC: Best effort, AC: Background, AC: Video, and AC: Audio Admission control AIFSN ECWMin ECWMax TXOpLimit | Information for each Access Category (AC). There is one set of data for best effort, background, video, and audio. Admission control—If yes, admission control must be used prior to transmission using the access parameters specific for this
                                                      AC. AIFSN—Number of slots after an SIFS duration a non-AP STA should defer before invoking a backoff or starting a transmission. ECWMin—Encodes value of CWmin in an exponent form to provide the minimum amount of time in a random backoff. ECWMax—Encodes value of CWmax in an exponent form to provide the maximum amount of time in a random backoff. TXOpLimit—Interval of time in which a particular quality of service (QoS) station has the right to initiate |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Phone information > Report problem . |
| Step 3 | Press Submit . |
| Step 4 | When the success message is displayed, notify your administrator that a problem report is available. |