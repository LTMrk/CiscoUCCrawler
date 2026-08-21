---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-14-2-1-cisco-ip-phone-8800-release-notes-for-fir-99590f5776
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/14-2-1/Cisco-IP-Phone-8800-Release-Notes-for-Firmware-14-2-1.html
retrieved_at: 2026-08-21T13:29:25.478509+00:00
---

Cisco IP Phone 8800 Release Notes for Firmware Release 14.2(1)

# Cisco IP Phone 8800 Release Notes for Firmware Release 14.2(1)

### Download Options

Updated: January 20, 2023

Cisco IP Phone 8800 Series Release Notes for Firmware Release 14.2(1) 3

New and Changed Features . 3

Features Available with the Firmware Release . 3

External Phone Number Mask Display for Non-primary Line . 3

SIP OAuth support on SRST . 3

Simplify Extension Mobility Login with Cisco Headset 730 USB adapter 3

Bluetooth Mute Sync for Cisco Headset 700 Series . 4

New settings for Cisco Headset 500 Series . 4

New Cisco Headset 720 and 980 Support 4

Caveats . 5

Open Caveats . 5

Resolved Caveats . 5

View Caveats . 6

Cisco IP Phone Firmware Support Policy . 6

Cisco IP Phone 8800 Series Release Notes for Firmware Release 14.2(1)

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware Release 14.2(1).

New and Changed Features

Features Available with the Firmware Release

The following sections describe the features available with the Firmware Release.

External Phone Number Mask Display for Non-primary Line

Before this release, the External Phone Number Mask (EPNM) supported the primary line only. Now the external number can also be displayed for non-primary lines when EPNM is configured.

This feature requires:

· Cisco Unified Communication Manager Release: 14SU2 or later

Where to Find More Information

· Feature Configuration Guide for Cisco Unified Communications Manager

SIP OAuth support on SRST

The SIP OAuth feature that Cisco Unified Communications Manager (Unified CM) has supported since Release 14.0(1) is now also supported on SRST. If SIP OAuth is configured, phones can securely register to SRST using token-based authentication during a Unified CM outage.

This feature requires:

· Cisco Unified Communication Manager Release: 14 or later

· Cisco SRST Software Release: IOS XE 17.8.1a and later

· Cisco SRST Hardware Models: ISR1100, ISR43xx, ISR44xx, Catalyst 8200 or Catalyst 8300 platform

Where to Find More Information

· Cisco Unified SCCP and SIP SRST System Administrator Guide

· Feature Configuration Guide for Cisco Unified Communications Manager (Release 14 or later)

· Cisco IP Phone 8800 Series Release Notes for Firmware Release 14.0(1)

· Cisco IP Phone 8800 Series Administration Guide

Simplified Extension Mobility Login with Cisco Headset 730 USB Adapter

The Simplified Extension Mobility feature now supports Cisco Headset 730 USB adapter .

The phone triggers the Extension Mobility login process when Cisco Headset 730 is connected to the phone via the USB adapter. When the headset is disconnected, powered off, or out of range, the phone triggers the Extension Mobility logout process.

This feature requires:

· Cisco headset 730: 1-8-0-213 or later

· Cisco headset USB adapter: 1-3-20 or later

Where to Find More Information

· Cisco IP Phone 8800 Series User Guide

· Cisco IP Phone 8800 Series Administration Guide

· Feature Configuration Guide for Cisco Unified Communications Manager

· Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.8(1)

Bluetooth Mute Sync for Cisco Headset 700 Series

Bluetooth Mute Sync now is supported on Cisco IP Phone 8851/61/65 with Cisco Headset 700 Series.

Notes:

If the headset is paired with the phone running an earlier, unpair the headset and repair it again after you get the phone upgraded to 14.2(1).

New settings for Cisco Headset 500 Series

This firmware release introduces new settings on the phone UI for Cisco Headset 500 Series. For more information about the settings, see Always on mode and Dock event in Cisco Headset 500 Series Release Notes .

New Cisco Headset 720 and 980 Support

You can now use your phones with Cisco Headset 720 (Webex version) and 980. Headset 720 supports basic call control, local settings, and UCM serviceability. Headset 980 supports basic call control. For more details, see Cisco Headset Compatibility Guide .

Caveats

Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series for Firmware Release 14.2(1).

For more information about an individual defect, access the Bug Search Tool and search for the defect using the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Search Tool as described in View Caveats .

· CSCvq55980 Network name still displayed ssid when no wifi radio available

· CSCwa00308 fail to reject second incoming call on cisco 530 headset

· CSCvp34626 No wifi icon displayed at the upper right corner of LCD after wifi connection done

· CSCvq32455 ip phone reset/restart intermittently after disconnect of a call

· CSCvq89463 8845/8865 freezing randomly

· CSCvt18121 8865 Phones video freezing on CMS in side-by-side view

Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series for Firmware Release 14.2(1).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Tool. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Tool as described in View Caveats .

· CSCwb28354 Cisco IP Phone 7800 and 8800 Series Cisco Discovery Protocol Stack Overflow Vulnerability

· CSCwb71995 CIAM: busybox 1.21.0 CVE-2022-28391

· CSCwc86875 Vulnerabilities in curl 7.26.0 CVE-2018-1000121 and others

· CSCwc91435 Vulnerabilities in cjson 1.0.0 CVE-2019-11835 and others

· CSCwd38929 8861 stays unregistered after AP goes down and up when DHCP is disabled

· CSCwd79802 IP Phones fail to fallback to Active CUCM Nodes from SRST

· CSCwd80036 8861/8865 does not display 'Hold/Transfer' softkeys during call via WLAN

View Caveats

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

· Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.2(1),14.2(01)&sb=anfr&svr=3nH&bt=custV

· Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.2(1)&sb=afr&sts=open&svr=3nH&bt=custV

· Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.2(1),14.2(01)&sb=fr&sts=fd&svr=3nH&bt=custV

Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .