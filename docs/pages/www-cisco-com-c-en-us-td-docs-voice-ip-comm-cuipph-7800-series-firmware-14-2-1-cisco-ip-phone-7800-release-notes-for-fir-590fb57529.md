---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-firmware-14-2-1-cisco-ip-phone-7800-release-notes-for-fir-590fb57529
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/firmware/14_2_1/Cisco-IP-Phone-7800-Release-Notes-for-Firmware-14-2-1.html
retrieved_at: 2026-08-21T13:23:21.115423+00:00
---

Cisco IP Phone 7800 Release Notes for Firmware Release 14.2(1)

# Cisco IP Phone 7800 Release Notes for Firmware Release 14.2(1)

Cisco IP Phone 7800 Series Release Notes for Firmware Release 14.2(1) 3

New and Changed Features . 3

Features Available with the Firmware Release . 3

SIP OAuth support on SRST . 3

New settings for Cisco Headset 500 Series . 3

Caveats . 3

Open Caveats . 3

Resolved Caveats . 4

View Caveats . 4

Cisco IP Phone Firmware Support Policy . 4

Cisco IP Phone 7800 Series Release Notes for Firmware Release 14.2(1)

These release notes support the Cisco IP Phone 7811, 7821, 7841, and 7861 running SIP Firmware Release 14.2(1).

New and Changed Features

Features Available with the Firmware Release

The following sections describe the features available with the Firmware Release.

SIP OAuth support on SRST

The SIP OAuth feature that Cisco Unified Communications Manager (Unified CM) has supported since Release 14.0(1) is now also supported on SRST. If SIP OAuth is configured, phone can securely register to SRST using token-based authentication during a Unified CM outage.

This feature requires:

· Cisco Unified Communication Manager Release: 14 or later

· Cisco SRST Software Release: IOS XE 17.8.1a and later

· Cisco SRST Hardware Models: ISR1100, ISR43xx, ISR44xx, Catalyst 8200 or Catalyst 8300 platform

Where to Find More Information

· Cisco Unified SCCP and SIP SRST System Administrator Guide

· Feature Configuration Guide for Cisco Unified Communications Manager (Release 14 or later)

· Cisco IP Phone 7800 Series Release Notes for Firmware Release 14.0(1)

· Cisco IP Phone 7800 Series Administration Guide

New settings for Cisco Headset 500 Series

This firmware release introduces new settings on the phone UI for Cisco Headset 500 Series. For more information about the settings, see Always on mode and Dock event in Cisco Headset 500 Series Release Notes .

Caveats

Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series for Firmware Release 14.2(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

· CSCvi99439 CME service URL throws XML error in 78xx

· CSCvs26183 78xx phone aux port upgrade 56x without headset need 22mins

· CSCwa12226 Sometimes the DN will remain or disappear after login/logout the EMCC service.

Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware Release 14.2(1).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

· CCSCwb28354 Cisco IP Phone 7800 and 8800 Series Cisco Discovery Protocol Stack Overflow Vulnerability

· CSCwb71995 CIAM: busybox 1.21.0 CVE-2022-28391

· CSCwc86875 Vulnerabilities in curl 7.26.0 CVE-2018-1000121 and others

· CSCwc91435 Vulnerabilities in cjson 1.0.0 CVE-2019-11835 and others

· CSCwd79802 IP Phones fail to fallback to Active CUCM Nodes from SRST

View Caveats

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

· Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.2(1),14.2(01)&sb=anfr&svr=3nH&bt=custV

· Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.2(1)&sb=afr&sts=open&svr=3nH&bt=custV

· Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.2(1),14.2(01)&sb=fr&svr=3nH&bt=custV

Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .