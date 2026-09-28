---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-firmware-14-2-1-cisco-ip-conference-phone-7832-release-notes-for-4620876433
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/firmware/14_2_1/Cisco-IP-Conference-Phone-7832-Release-Notes-for-Firmware-14-2-1.html
retrieved_at: 2026-08-21T13:22:05.278362+00:00
---

Cisco IP Conference Phone 7832 Release Notes for Firmware Release 14.2(1)

# Cisco IP Conference Phone 7832 Release Notes for Firmware Release 14.2(1)

Cisco IP Conference Phone 7832 Release Notes for Firmware Release 14.2(1) 3

New and Changed Features . 3

Features Available with the Firmware Release . 3

SIP OAuth support on SRST . 3

Features Available with the Latest Cisco Unified Communications Manager Device Pack . 3

4096-bit RSA Key Support 3

Caveats . 4

Resolved Caveats . 4

View Caveats . 4

Cisco IP Phone Firmware Support Policy . 5

Cisco IP Conference Phone 7832 Release Notes for Firmware Release 14.2(1)

These release notes support the Cisco IP Phone 7832 running SIP Firmware Release 14.2(1).

New and Changed Features

Features Available with the Firmware Release

The following sections describe the features available with the Firmware Release.

SIP OAuth support on SRST

The SIP OAuth feature that Cisco Unified Communications Manager (Unified CM) has supported since Release 14.0(1) is now also supported on SRST. If SIP OAuth is configured, phones can securely register to SRST using token-based authentication during a Unified CM outage.

This feature requires:

· Cisco Unified Communication Manager Release: 14 or later

· Cisco SRST Software Release: IOS XE 17.8.1a and later

· Cisco SRST Hardware Models: ISR1100, ISR43xx, ISR44xx, Catalyst 8200 or Catalyst 8300 platform

Where to Find More Information

· Cisco Unified SCCP and SIP SRST System Administrator Guide

· Feature Configuration Guide for Cisco Unified Communications Manager (Release 14 or later)

· Cisco IP Conference Phone 7832 Release Notes for Firmware Release 14.0(1)

· Cisco IP Conference Phone 7832 Administration Guide

Features Available with the Latest Cisco Unified Communications Manager Device Pack age

The following sections describe features in the release which require the new firmware and the latest Cisco Unified Communications Manager Device Package. The applicable device packs are released after the firmware release.

For information about the Cisco Unified IP Phones and the required Cisco Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

4096-bit RSA Key Support

With the latest Cisco Unified Communications Manager Device Package installed, the Conference Phone 7832 can support 4096-bit RSA key.

On Cisco Unified CM Administration , navigate to Device > Phone > Certification Authority Proxy Function (CAPF) Information . Select 4096 for RSA Key Size (Bits) .

Where to Find More Information

· Cisco System Configuration Guide for Cisco Unified Communications Manager

· Configure LSC on Cisco IP Phone with CUCM

Caveats

Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7832 running Firmware Release 14.2(1).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Tool. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Search Tool as described in View Caveats .

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