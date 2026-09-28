---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-wireless-ip-phone-8821-217219-troubleshoot-cp-8821-wireless-p-73e8f837b6
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/wireless-ip-phone-8821/217219-troubleshoot-cp-8821-wireless-phones.html
retrieved_at: 2026-08-17T01:16:05.467456+00:00
---

Troubleshoot CP-8821 Wireless Phones

# Troubleshoot CP-8821 Wireless Phones

### Download Options

Updated: July 19, 2021

Document ID: 217219

Contents

## Contents

## Introduction

This document describes high-level methods to troubleshoot various common issues with wireless phones such as the 8821 and 8821-EX.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on a CP-8821 on 11.0.5-SR1 firmware.

The information in this document was created from devices in a lab environment. All of the devices used in this document started with a cleared (default) configuration. If you are performing these tasks in a production environment, ensure that you understand the potential impact of any command.

## Wireless Terminology

Commonly used terminology and abbreviations that you need to know in order to troubleshoot various 8821 issues:

- Access Points (AP) - APs are the devices that wireless clients communicate with to receive connectivity. They contain the radios that broadcast the signals for the clients.

- Wireless LAN Controller (WLC) - the device that handles the association and/or authentication of wireless clients. All config for the Access Points is also done here.

Note : RSSI is measured in dBm so the measurement is logarithmic rather than linear. This means -3dBm is half the signal strength while +3dBm is double the signal strength.

- Roaming - this is when a device moves from one AP to another, usually due to a strong signal on the neighbor AP.

- Signal to Noise Ratio (SNR) -  this is a measurement of the strength of the wireless signal compared to the level of background noise (in positive dBm).

- Basic Service Set (BSS) - network topology that allows devices to communicate via an AP.

- Service Set Identifier (SSID) - friendly name of one or more BSS.

- Basic Service Set Identifier (BSSID) - identifier of the BSS MAC of an AP for a given radio.

- Over-the-air Capture (OTA Capture) - since packet captures cannot be taken from the 8821 directly, OTA captures are the only way to see the transmitted packets by the AP and phone.

- Call Admission Control (CAC) - a system by which an administrator can prevent calls that would negatively impact other calls on the network, usually due to bandwidth restrictions.

- Site Survey - A study of the environment to help plan and design the wireless network. The survey helps determine the optimal locations for APs in order to achieve the desired coverage, data rates, roaming capability, etc.

- Problem Reports (PRT) - a log bundle that can be generated on the phone to troubleshoot issues.

## Troubleshoot

### Deployment Guide and Wireless Configuration

The first step to troubleshoot 8821 connectivity issues is to ensure that the wireless config adheres to the 8821 deployment guide . You can use these tools to help accomplish this:

Wireless Config Analyzer Tool

More information about how to use the Wireless Config Analyzer tool can be found here:

https://community.cisco.com/t5/wireless-mobility-documents/how-to-use-the-wireless-lan-controller-co...

### Understand the Scope of the Problem

One of the first steps to troubleshoot wireless issues is to get a very detailed description of the problem. It is imperative that you understand the problem in detail so that you can troubleshoot the issue effectively. In order to narrow your focus down to the right area, knowledge of the expected behavior of the phone is vital. See the high-level steps that a phone takes from power on to the registration:

- Phone is powered on.

- Phone scans WiFi channels to look for SSIDs (Layer 1).

- Phone associates to an AP (Layer 1/2).

- Phone authenticates (PSK or 802.1x/EAP) (Layer 2).

- Phone acquires an IP address (either via DHCP or static assignment) (Layer 3).

- Phone attempts to establish a connection to the TFTP server in order to request files.

- Phone attempts to register to the primary CUCM node in the Unified CM Group applied to the phones Device Pool.

You need to isolate the step at which the failure occurs.

- Is the WiFi icon on the phone screen? If so, then the phone has successfully associated with an AP. If not, then you must review the phone and/or WLC logs to determine why the phone cannot connect to the AP.

- Does the phone acquire an IP?  If not, then review the phone logs, OTA capture, or packet capture from the AP wired interface to isolate where the DHCP process fails. Does the phone send a DHCP DISCOVER?  Does the DHCP server respond with a DHCP OFFER?

- If the WiFi icon is visible and the phone receives an IP, then expect the phone to attempt to connect to the TFTP server. The Status Messages page can be a quick place to check for this. Messages like "Trust list updated" or "SEPAAAABBBBCCCC.cnf.xml.sgn(HTTP)" indicate that the phone is able to acquire and validate the CTL/ITL files and config file. Ensure that you download a problem report from the phone to investigate any problematic errors on the Status Messages page.  More details on log collection are later in this document.

- Is the signal stronger (closer to 0) than -67dBm? A signal strength lower than -67dBm is considered unreliable.

### Connectivity Issues

If you experience intermittent call drops or audio issues, immediately look at the phone when the issue occurs. Does the WiFi icon disappear? If so, the phone disassociates from the AP and the failure is likely due to the loss of network connectivity.  If the WiFi icon remains, then it would make more sense to troubleshoot the problem from a Voice over IP (VoIP) perspective rather than connectivity. A quick and easy way to ensure that the phone remains associated to the AP and on the network is to run a continuous ping.

### Phone Roaming Information

When a wireless device roams, it switches to a new AP. There are a few reasons that this can occur but the most common reason to roam is the difference in RSSI between the current AP and a neighboring AP.

In addition to signal strength, there are a few other triggers for the 8821 to roam:

- Max Transmit (TX) retries - The phone is not able to successfully transmit packets.

- Traffic Specification Admission Control (TSpec) - TSpec was not granted from the AP. (This setting is related to CAC and QoS).

- BSS Loss - The AP does not send or the phone does not hear the beacons. (Weak RF or AP reboot, etc).

- Channel Switch - The phone is sent a Channel Switch Announcement (CSA).  The AP sends beacon probe responses to the phone to provide new channel information.

- Deauthentication - AP has sent a deauthentication to the phone. There could be many reasons for this - check the phone log or capture for the reason code. Reason codes can be found here, but are usually described in the capture:

### Scan Mode

The 8821 has 3 different options for Scan Mode which dictate how often the phone scans to determine the signal strength of all APs in the vicinity. This can be found at Cisco Unified CM Administration > Device > Phone > Select the 8821 .

- Continuous - This is the default setting. The phone scans every 2 seconds whether it is on an active call or idle. This setting utilizes the most battery power due since the phone constantly scans for APs.

- Auto - When the phone is on a call, it scans every 2 seconds.  When the phone is idle, it only scans when the RSSI on the current AP degrades beyond a certain point. This setting uses less battery than Continuous and can improve battery life on phones that are frequently inactive.

- Single AP - Scans only occur when the phone powers on or if connectivity is lost. When connectivity is lost, the phone scans every 45 seconds until it regains connectivity. This setting uses the least amount of battery.

Note : It is very important to understand that roaming can occur even if the phone is stationary. Most enterprise environments have a lot of variables that can cause RSSI to fluctuate even if the phone is stationary. If you suspect that your issue is due to roaming, setting the scan mode to Single AP can be very useful to prove that. Also, bear in mind that while RSSI fluctuation is the most common cause, there are other causes for roaming as well.

### Device Does Not Acquire an IP

Be aware of FN-70357 if you have an 8821 that cannot acquire an IP. This is usually seen in scenarios where ISE is upgraded to a version affected by CSCvm03681 .

### Data to Collect

#### Log Profile

The 8821 has various Log Profiles that are important to understand to troubleshoot issues. These are found on the device configuration page in CUCM:

Telephony is typically preferred over default due to the added debugs that it provides. When in doubt, change the profile to Telephony and additional debugs can be manually enabled in addition to that if needed.

#### Wireless Packet Capture (OTA Capture)

In cases where you need to troubleshoot 8821 connectivity, the text logs alone are not sufficient to isolate the cause of the problem.  Consider a scenario where the 8821 sends a SIP REGISTER to CUCM and CUCM never responds.  You need to determine a few things:

- Does CUCM receive this message?

- Does CUCM respond to this message?

- If CUCM responds, is the response lost between CUCM and the phone?

Since the text logs don't provide ample visibility into the cause of the problem, you need to collect packet captures from a few places:

- Over the air packet capture (to confirm that the phone sends the packet to the AP)

- Wired interface of the AP (to confirm the AP puts that packet on the wire)

- Devices between the AP and CUCM (to isolate if a specific device drops the packet)

- CUCM (to confirm that CUCM receives the message)

You must look for a point in the path of this packet where one device receives the packet but does not transmit it to the next device.  With that knowledge, you can pinpoint the problem to a specific device, or set of devices.

More information on how to collect an OTA capture can be found here: https://documentation.meraki.com/MR/Monitoring_and_Reporting/Capturing_Wireless_Traffic_from_a_Client_Machine

### Example Analysis

#### Log Review for a Successful DHCP Exchange

```
%%%%% Successful DHCP exchange
7241 ERR Oct 23 12:26:47.211445 DHCP-dhcpSendReq
... 7246 ERR Oct 23 12:26:47.218905 DHCP-dhcpSendReq(): Sending Discover... ...
7312 ERR Oct 23 12:26:48.395112 DHCP-dhcpRcvPkt
... 7322 ERR Oct 23 12:26:48.402401 DHCP-dhcpRcvPkt(): Sending Request...
... 7327 ERR Oct 23 12:26:48.500058 DHCP-dhcpRcvPkt
... 7330 NOT Oct 23 12:26:48.500112 DHCP-dhcpRcvPkt(): ACK received
... 7334 NOT Oct 23 12:26:48.500176 DHCP-dhcpRcvPkt(): DHCP Succeeded
7335 NOT Oct 23 12:26:48.500188 DHCP-dhcpRcvPkt(): new assigned IP addr: 0xaa401fac, configuredipaddr: 0x0
```

#### Log Review for a Failed DHCP Exchange

```
%%%%% DHCP Discover
2811 ERR Oct 23 12:33:17.229603 DHCP-dhcpSendReq(): Sending Discover...
2812 ERR Oct 23 12:33:17.229643 DHCP-dhcpDiscover
2813 ERR Oct 23 12:33:17.229659 DHCP-setSelectTimeout %%%%% No response to DHCP Discover
3253 ERR Oct 23 12:33:21.234227 DHCP-dhcpReadThrd(): response not received, try again...
... 3258 ERR Oct 23 12:33:21.234331 DHCP-dhcpTmrExp(): Max retries of discover %%%%% Phone does not acquire an IP so it cannot connect to the network
3638 ERR Oct 23 12:33:24.660465 NTP->>> Send pkt to 172.16.155.3 error: [101] Network is unreachable ... 3641 ERR Oct 23 12:33:25.350497 DHCP-dhcpReadThrd(): response not received, try again...
... 3646 ERR Oct 23 12:33:25.350606 DHCP-dhcpTmrExp(): Max retries of discover
...
3776 ERR Oct 23 12:33:29.465112 DHCP-dhcpReadThrd(): response not received, try again...
... 3785 ERR Oct 23 12:33:29.470765 DHCP-dhcpDiscover
```

#### Log Review for a Roaming Event

In order to search for roaming in 8821 logs, you need to ensure that the log profile is set to Telephony. Once you have done that, you can use this regex string:

```
wpa_supplicant\([0-9][0-9][0-9]\)-nl80211:\ Associated\ with
```

Be sure to paste this exactly as it is shown. Also, set your text editor to use the search string as regex.

```
%%%%% This phone is not roaming until the MAC Address of the AP changes on line 4121 2848 DEB Oct 25 09:49:37.303344 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 2897 DEB Oct 25 09:49:37.683084 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 3018 DEB Oct 25 09:49:39.680420 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 3600 DEB Oct 25 09:49:41.676275 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 3928 DEB Oct 25 09:49:43.669054 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 3983 DEB Oct 25 09:49:45.672203 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 4037 DEB Oct 25 09:49:47.674104 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 4085 DEB Oct 25 09:49:49.671717 wpa_supplicant(940)-nl80211: Associated with 70:10:5c:b0:2a:1c 4121 DEB Oct 25 09:49:49.766735 wpa_supplicant(940)-nl80211: Associated with b4:e9:b0:b5:05:59
```

#### Checking the Signal Strength (RSSI)

You want to ensure that the phone remains connected to an AP with a signal strength of -67dBm or better (closer to 0). You can easily scan the logs for this with this search string:

```
level=-
```

Example:

```
%%%%% The signal level is printed on the right end of each line.  If you see this approach or exceed -67, then jump to that line and investigate %%%%% In this example, the RSSI exceeded our acceptable threshhold starting on line 4008 and only came back within acceptable limits for one scan so I would start there 3550 DEB Oct 25 11:34:08.317669 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:73:6c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-66 3586 DEB Oct 25 11:34:08.681122 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:73:6c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-66 3692 DEB Oct 25 11:34:13.484584 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:75:ec ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-58 3902 DEB Oct 25 11:34:18.305574 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:75:ec ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-57 4008 DEB Oct 25 11:34:21.310674 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:75:ec ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-68 4047 DEB Oct 25 11:34:21.865534 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:75:ec ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-68 4144 DEB Oct 25 11:34:26.311028 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-66 4316 DEB Oct 25 11:34:32.063243 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:75:ec ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-68 4467 DEB Oct 25 11:34:39.191279 wpa_supplicant(940)-wlan0: 0: 74:a2:e6:71:75:ec ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-68 4642 DEB Oct 25 11:34:44.210987 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 4796 DEB Oct 25 11:34:50.064503 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 4911 DEB Oct 25 11:34:57.241813 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 4927 DEB Oct 25 11:34:57.453239 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 5502 DEB Oct 25 11:35:02.336313 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 5662 DEB Oct 25 11:35:10.671841 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 5673 DEB Oct 25 11:35:10.673330 wpa_supplicant(940)-wlan0: 0: e8:40:40:72:29:5c ssid='cisco-lab-voip' wpa_ie_len=0 rsn_ie_len=24 caps=0x1111 level=-77 %%%%% After jumping to line 4642, I scroll up to look for the previous scan %%%%% The scan shows that there is no other AP with a stronger signal within range.  Since -77dBm is unreliable, this needs to be addressed: 4628 DEB Oct 25 11:34:44.206227 wpa_supplicant(940)-nl80211: Drv Event 34 (NL80211_CMD_NEW_SCAN_RESULTS) received for wlan0 4629 DEB Oct 25 11:34:44.207867 kernel-[102016.581878] [wl_dump_bss_list]: SCAN COMPLETED: scanned AP count (1) 4630 DEB Oct 25 11:34:44.207952 kernel-[102016.581909] [wl_dump_bss_list]: SSID: "cisco-lab-voip" BSSID: e8:40:40:72:29:5c RSSI: -77 Channel: 48
```

## Related Information

- Cisco 8821 Wireless Phone Troubleshooting

- Capturing Wireless Traffic from a Client Machine - Meraki

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

19-Jul-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Jul-2021 | Initial Release |