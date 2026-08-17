---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-wireless-ip-phone-8821-214215-how-to-get-your-8821-792x-wirel-c3180d39f1
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/wireless-ip-phone-8821/214215-how-to-get-your-8821-792x-wireless-phone.html
retrieved_at: 2026-08-17T01:16:09.679589+00:00
---

How to get your 8821/792x wireless phones performing reliably

# How to get your 8821/792x wireless phones performing reliably

### Download Options

Updated: April 22, 2021

Document ID: 214215

Contents

## Contents

## Introduction

This document explains how to get Cisco 8821 and 792x wireless phones (7921G, 7925G, 7926G) to work well in a Cisco Unified Wireless Network.

Important note: Cisco no longer supports the 792x phones. See the following End of Life announcements:

- 7921G: Retirement Notification End-of-Sale and End-of-Life Announcement

- 7925G, 7925G:-EX and 7926G: End-of-Sale and End-of-Life Announcement for the Cisco Unified Wireless IP Phones 7925G, 7925G-EX, and 7926G

In particular, the 792x phones have not been tested with AP-COS (802.11ac Wave 2 / 802.11ax) APs, nor with 9800 series controllers, and Cisco TAC will not assist with any such deployments.  Information on the 792x phones is provided below for historical reference.

## Voice over WLAN - a challenging technology

Voice over WLAN (VoWLAN) is one of the most challenging technologies that Cisco provides.  For VoWLAN to work satisfactorily - especially in the high-stress environments in which it is deployed, such as healthcare - the network, and the phone, must be able consistently to transport a real-time, bidirectional, securely encrypted audio stream, with almost no dropouts, while the endpoint moves across four dimensions (space and frequency).

## Seven basic guidelines to making VoWLAN work well

Though delivering a reliable VoWLAN service is difficult, it is possible, provided that the network provider adheres to the following basic design guidelines.

#### 1. Have solid coverage in 5GHz - and lock 802.11 mode on phones to 5GHz

Your network's ability to perform is fundamentally dependent on a solid physical layer.  VoWLAN uses both the 2.4GHz and 5GHz bands.  Of these, the 2.4GHz band's lower frequency signals carry further - however, the constrained bandwidth (only three non-overlapping channels) and ever-increasing interference, render 2.4GHz, in most cases, unsuitable for reliable voice.  Network providers who want to deliver a reliable VoWLAN service will ensure that their design adheres to the following standard:

Every spot in the coverage area is serviced by at least two viable 5GHz access points, at -67dBm or stronger.

You can easily validate the necessary coverage by setting your phone into site survey mode, and walking throughout your coverage area.

Additionally, AP placement, antenna selection, building construction, etc. must be such that multipath distortion is kept to a minumum .  To ensure gap-free roaming, a moving phone must be able to hear each roamed-to AP at least 5 seconds before it needs to roam to it - so place all APs in the middle of halls, at corridor junctions, etc., rather than in blind spots.

#### 2. Run current phone firmware

##### On the 792x: run 1.4.7 - nothing earlier

1.4.7 firmware or above is strongly recommended, due to the CSCut25250 (Phones stops sending SCCP messages) fix.

##### On the 8821: run  11.0(6)SR2 -- nothing earlier

The latest image has fixes to several phone related issues like: poor roaming, one way audio, phone freeze/hang/crash and phone deregistration issues. If you encounter any new issues, troubleshooting from the latest firmware will be the best path forward. If any problems with the latest firmware, contact TAC.

Please refer TAC Recommended AireOS for AireOS WLC side code recommendations.

Please refer TAC Recommended IOS-XE for 9800 WLC side code recommendations.

#### 3. If using FlexConnect local switching, enable ARP caching

If using FlexConnect local switching, make sure to enable ARP caching (i.e. the AP ARPing on behalf of the wireless client), for the sake of reliability and phone battery lifetime.

#### 4. Optimize Security for Fast Secure Roaming

##### WPA2/AES Enterprise with CCKM and/or FT-802.1X is recommended.

WPA2/AES Enterprise provides for the greatest security, and - with a Fast Secure Roaming method - also provides for the best roam times.

For 8821: use WPA2/AES Enterprise with 802.11r (FT over the air)

For 792x: use WPA2/AES Enterprise with CCKM.

Can have both CCKM and FT-802.1X enabled on the WLAN - 792x uses CCKM and 8821 will use FT-802.1X

Note : The phones(882 and 792x) do not support 802.11k and 802.11v and should be disabled.

##### WPA2/AES-PSK can also be used

- Although WPA2/AES Enterprise is the preferred security method, in some cases WPA2/AES-Preshared Key (PSK) will be used.  For example, if FlexConnect APs have only a high latency, unreliable WAN path to a RADIUS server, then PSK with FlexConnect Local Authentication may be the best choice.

- Enable FT over the air with FT-PSK for the fastest roaming with 8821 phones

- This bug does not affect 7921G or 7926G phones.

- The problem can be mitigated to some extent with: config advanced eap eapol-key-timeout 250 on the WLC, and by disabling Java on the 7925 (if using 1.4.6.3 firmware or above)

- Can have both FT-PSK and regular PSK on an SSID

Notes:

- Special considerations for using CCKM:

- use the WLC command "config wlan security wpa akm cckm timestamp-tolerance 5000" to increase the likelihood of performing a fast roam

- See the CCKM Client Disconnect Bugs in 7.0/7.2 tip

- If using CCKM with AP1131/1242 in 8.0, beware CSCuu49291 (7925 decrypt errors with AP1131 running 8.0 code), fixed in 8.0.132.0.

- For WPA2/AES Enterprise, you may use Local Authentication on the WLC, for small deployments (<100 phones), if you do not want to use an external RADIUS server.  (Note: Local Authentication with EAP-FAST does not work with the 792x in 8.0.140.0 or 8.3 - track CSCvb44979 [WLC Local EAP with 7925 Handshake Failure] for the fix.)

- Avoid TKIP which is less secure, and is susceptible to MIC error triggered service interruptions.  TKIP unicast ciphers are not supported with the 8821.

#### 5. Optimize channels, power, and data rates

- use at least 8 channels (if available in your regulatory domain)

- in the US, use channels from UNII-1 (36-48), UNII-2 (52-64), UNII-2 Extended (100-116; 132-140, but not 120-128 or 144), and/or UNII-3 (149-161 but not 165)

- if coverage is weak, avoid channels with lower power limits

- if radar detection is frequent, avoid the DFS channels (UNII-2, UNII-2 extended)

- in 5GHz, use a minimum power level of at least 11dBm

- although Cisco phones do not have a problem when the AP Tx level exceeds the phone's, other vendors' devices may, in such a case, stick to a suboptimal AP.  So you may want to set a maximum power level in the 14 - 17dBm range.

- the Deployment Guide (see below) recommends a minimum data rate of 12Mbps

- if there is significant multipath in the environment, or if the 5GHz coverage is marginal, set 6Mbps as the lowest mandatory rate, and be sure that 12 and 24Mbps are enabled

Note:

1. Remember to make any changes on all WLCs in the RF group

#### 6. Enable continuous scan mode (in CUCM)

For 8821: continuous scan mode is enabled by default.  Do not change this setting

. 7. Configure all QoS, and everything else, exactly as documented in the Deployment Guides Go through the entire 7925G Deployment Guide , and/or 8821 Deployment Guide , and configure the phones and the wireless network as per its recommendations.  In particular, make sure that all QoS configurations are set as per best practice, throughout your wireless and wired network. Conclusion With strict adherence to every single one of the above guidelines, there is a high probability that your VoWLAN service will meet your clients' performance expectations.

#### 7. Configure all QoS, and everything else, exactly as documented in the Deployment Guides

## Conclusion

## Related Information

### Revision History

1.0

13-Mar-2019

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Mar-2019 | Initial Release |