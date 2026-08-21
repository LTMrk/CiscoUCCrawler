---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-firmware-9-3-4-sr2-cs38-b-phone-8831-3pcc-release-934sr2-ht-ba35c9d628
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/firmware/9-3-4-sr2/cs38_b_phone-8831-3pcc-release-934sr2.html
retrieved_at: 2026-08-21T13:34:05.143528+00:00
---

Cisco Unified IP Conference Phone 8831 for Third Party Call Control Release Notes for Firmware Release 9.3(4)SR2

# Cisco Unified IP Conference Phone 8831 for Third Party Call Control Release Notes for Firmware Release 9.3(4)SR2

### Download Options

Updated: June 30, 2017

First Published: December 14, 2015

Last Updated: June 30, 2017

# Cisco Unified IP
	 Conference Phone 8831 for Third Party Call Control Release Notes for Firmware
	 Release 9.3(4)SR2

These Release Notes describe the Cisco Unified IP Conference Phone 8831
		for Third-Party Call Control running SIP Firmware Release 9.3(4)SR2.

As with any firmware release, read these release notes before the
		firmware upgrade. We also recommend that you back up the configuration before
		any firmware upgrade.

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to
		  publications that are specific to your language, phone model, and call control
		  system. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​tsd-products-support-series-home.html

The Deployment Guide is located at the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​products-implementation-design-guides-list.html

## New and Changed Features

This release contains no new or changed features.

## Installation

### Upgrade
	 Firmware

The Cisco Unified IP Conference Phone 8831 for Third-Party Call
		  Control supports a single image upgrade by TFTP, HTTP, or HTTPS.

After the conference phone is upgraded to Release 9.3(4)SR2, you cannot downgrade the firmware to a previous version.

Each region has a specific firmware load file. The following table
		  gives the region and the filename of the firmware load.

Region

Filename

North America

cp-8831-sip.9-3-4-SR2-3PCC.bin.sgn

Brazil

cp-8831-sip.9-3-4-SR2-3PCC-BR.bin.sgn

Europe and Australia

cp-8831-sip.9-3-4-SR2-3PCC-EU.bin.sgn

Japan

cp-8831-sip.9-3-4-SR2-3PCC-JP.bin.sgn

Latin America

cp-8831-sip.9-3-4-SR2-3PCC-LA.bin.sgn

North America

cp-8831-sip.9-3-4-SR2-3PCC-NA.bin.sgn

Taiwan

cp-8831-sip.9-3-4-SR2-3PCC-TW.bin.sgn

<schema>://<server[:port]>/filepath

The third-party call control can also upgrade via a URL in the web
				browser:

http://<phone_ip>/admin/upgrade?<schema>://<serv_ip[:port]>/filepath

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect Cisco IP Phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### Health-Care
	 Environment Use

This product is not a
		medical device and uses an unlicensed frequency band that is susceptible to
		interference from other devices or equipment.

## Caveats

### Access Cisco Bug
	 Search

Known problems
		  (bugs) are graded according to severity level. These release notes contain
		  descriptions of the following:

All severity
				level 1 or 2 bugs

Significant
				severity level 3 bugs

You can search for
		  problems by using Cisco Bug Search.

To access Cisco Bug
		  Search, you need the following items:

Internet
				connection

Web browser

Cisco.com user
				ID and password

https:/​/​tools.cisco.com/​bugsearch

### Open Caveats

There are no
severity 1, 2, and 3 defects open for the Cisco Unified IP
Conference Phone 8831 for Third-Party Call Control SIP Firmware
Release 9.3(4)SR2.

### Resolved Caveats

The following
table lists severity 1, 2, and 3 defects that are resolved for the
Cisco Unified IP Conference Phone 8831 for Third-Party Call Control
SIP Firmware Release 9.3(4)SR2.

For more
information about an individual defect, you can access the online
record for the defect by clicking the Identifier or going to the
URL that is shown. You must be a registered Cisco.com user to
access this online information.

Because defect
status continually changes, the table reflects a snapshot of the
defects that were open at the time this report was compiled. For an
updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Headline

CSCus31319

Oct 2014 OpenSSL Vulnerabilities

CSCus42757

JANUARY 2015 OpenSSL Vulnerabilities

CSCus69752

Evaluation of glibc GHOST vulnerability - CVE-2015-0235

CSCut46138

MARCH 2015 OpenSSL Vulnerabilities

CSCuu82519

Evaluation of 3pcc-beignet for OpenSSL June 2015

CSCuw96949

Show Wireless Region Code with debugSH command 'show emic'

CSCuw96967

remove the braces around the number on 8831 display

CSCux27616

8831 3PCC needs to prevent downgrading

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Note | After the conference phone is upgraded to Release 9.3(4)SR2, you cannot downgrade the firmware to a previous version. |
|---|---|

| Region | Filename |
|---|---|
| North America | cp-8831-sip.9-3-4-SR2-3PCC.bin.sgn |
| Brazil | cp-8831-sip.9-3-4-SR2-3PCC-BR.bin.sgn |
| Europe and Australia | cp-8831-sip.9-3-4-SR2-3PCC-EU.bin.sgn |
| Japan | cp-8831-sip.9-3-4-SR2-3PCC-JP.bin.sgn |
| Latin America | cp-8831-sip.9-3-4-SR2-3PCC-LA.bin.sgn |
| North America | cp-8831-sip.9-3-4-SR2-3PCC-NA.bin.sgn |
| Taiwan | cp-8831-sip.9-3-4-SR2-3PCC-TW.bin.sgn |

| Step 1 | Put the third-party call
			 control image (for example, cp-8831-sip.9-3-4-SR2-3PCC.bin.sgn ) on the
			 tftp/http/https download directory. |
|---|---|
| Step 2 | Configure the Upgrade Rule on the 'Provisioning' tab in the web
			 page with the valid URL format: <schema>://<server[:port]>/filepath The third-party call control can also upgrade via a URL in the web
				browser: http://<phone_ip>/admin/upgrade?<schema>://<serv_ip[:port]>/filepath After the firmware upgrade completes, the phone reboots
			 automatically. |

| Step 1 | To access Cisco Bug Search, go to: https:/​/​tools.cisco.com/​bugsearch |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCus31319 | Oct 2014 OpenSSL Vulnerabilities |
| CSCus42757 | JANUARY 2015 OpenSSL Vulnerabilities |
| CSCus69752 | Evaluation of glibc GHOST vulnerability - CVE-2015-0235 |
| CSCut46138 | MARCH 2015 OpenSSL Vulnerabilities |
| CSCuu82519 | Evaluation of 3pcc-beignet for OpenSSL June 2015 |
| CSCuw96949 | Show Wireless Region Code with debugSH command 'show emic' |
| CSCuw96967 | remove the braces around the number on 8831 display |
| CSCux27616 | 8831 3PCC needs to prevent downgrading |