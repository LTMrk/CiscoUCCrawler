---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-release-notes-8831-3pcc-934-rn-html-9de07fc071
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/release-notes/8831-3pcc-934-rn.html
retrieved_at: 2026-08-21T13:34:13.563776+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Release Notes for Firmware Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Release Notes for Firmware Release 9.3(4)

- 9.3(4)SR1

- 9.3(4)

### Download Options

Updated: June 30, 2017

## Table of Contents

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control  Release Notes for  Firmware Release 9.3(4)

Contents

Introduction

Sound Base

Display Control Unit (DCU)

Related Documentation

Cisco IP Phone 8800 Series Documentation

Firmware Upgrade

New and Changed Features

Features Available with Firmware Release

Wireless Microphone Frequency Lock

View Caveats

Cisco IP Phone Firmware Support Policy

Documentation, Service Requests, and Additional Information

Updated: June 2017

These Release Notes describe the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control.

As with any firmware release, read these release notes before upgrading the firmware. Cisco also recommends backing up configuration before any firmware upgrade.

## Introduction

These release notes support the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control running SIP Firmware Release 9.3(4).

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control supports third-party call control that provides support for 2 to 10 calls per line. The Call Appearances Per Line parameter controls the call appearance. The conference phone 8831 model comprises the following units:

- Sound Base (with built-in mic)

- Display Control Unit (DCU)

- (Optional) Wired microphone, or wireless microphone (with charger)

Note The conference phone system can support 2 wired or 2 wireless microphones at one time. When both the wired and wireless microphones are connected, only the wireless microphone functions.

### Sound Base

The bottom of the sound base comprises the following:

- Network port: 1

- USB port for DCU: 1

- Wired microphone ports: 2

- Daisy chain port: 1

- Wall power port: 1

### Display Control Unit (DCU)

- Comprises a keypad, LCD, and LED.

- Connects to a base unit via USB.

Note Connect the DCU only to the master unit of a daisy chain.

## Related Documentation

Use the following section to obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to publications that are specific to your language, phone model, and Cisco Unified Communications Manager release. Navigate from the following documentation URL:

http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd-products-support-series-home.html

## Firmware Upgrade

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control supports a single image upgrade by tftp/http/https.

Step 1	Put the 3PCC image (for example, cp-8831-sip.9-3-4-x-3PCC.bin.sgn) on the tftp/http/https download directory.

Step 2	Configure Upgrade Rule on the ‘Provisioning’ tab in the web page, with the valid URL format:

<schema>:// <server[:port]> /filepath

The 3PCC can also upgrade via URL on web browser:

http://<phone_ip>/admin/upgrade?<schema>://<serv_ip[:port]>/filepath

Step 3	After the firmware upgrade completes, the phone reboots automatically. After this, reboot the phone manually.

Note This step applies only for firmware upgrade to release 9.3(4).

## New and Changed Features

### Features Available with Firmware Release

The following sections describe the features that are available with the Firmware Release.

### Wireless Microphone Frequency Lock

The Wireless Microphone Frequency Lock enhancement provides a secure Digital Enhanced Cordless Telecommunications (DECT) frequency for wireless microphones by locking the Wireless Microphone Region setting. When the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control is shipped from the manufacturer, the mask and the Wireless Microphone Region setting are already configured for a particular region.

Note If your Cisco Unified IP Conference Phone 8831 for Third-Party Call Control is operating with an earlier firmware release, you must upgrade to Firmware release 9.3(4) so that the Wireless Microphone Region can be set.After you configure the Wireless Microphone Region setting, it cannot be updated. Further configuration of this setting requires an RMA.

Note Although you cannot change the value of the Wireless Microphone Region setting, you can check its value. To do so, execute Info > System Status > Product Information and check the Wireless Microphone Region value on the webpage.

Beginning with Release 9.3(4), new phones that are shipped from the factory are loaded with region-specific firmware:

Wireless Microphone Regions and Firmware Loads

Region

Region-Specific Firmware

North America

cp-8831-sip.9-3-4-4-3PCC.bin.sgn

cp-8831-sip.9-3-4-4-3PCC-NA.bin.sgn

Europe

cp-8831-sip.9-3-4-4-3PCC-EU.bin.sgn

Latin America

cp-8831-sip.9-3-4-4-3PCC-LA.bin.sgn

Brazil

cp-8831-sip.9-3-4-4-3PCC-BR.bin.sgn

Taiwan

cp-8831-sip.9-3-4-4-3PCC-TW.bin.sgn

Japan

cp-8831-sip.9-3-4-4-3PCC-JP.bin.sgn

The feature is supported on the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control.

Where to Find More Information

- Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before You Begin

To view caveats, you need the following items:

- Internet connection

- Web browser

- Cisco.com user ID and password

Step 1	Perform one of the following actions:

- To find all caveats for this release, use this URL:

https://tools.cisco.com/bugsearch/search?kw=customer%20visible%20bug%20for%208831%203PCC%209.3.%284%29&pf=prdNm&sb=anfr&srtBy=byRel&bt=custV

- To find all open caveats for this release, use this URL:

https://tools.cisco.com/bugsearch/search?kw=customer%20visible%20bug%20for%208831%203PCC%209.3.%284%29&pf=prdNm&sb=anfr&mDt=5&sts=open&svr=3nH&srtBy=byRel&bt=custV

- To find all resolved caveats for this release, use this URL:

https://tools.cisco.com/bugsearch/search?kw=customer%20visible%20bug%20for%208831%203PCC%209.3.%284%29&pf=prdNm&sb=anfr&mDt=5&sts=fd&svr=3nH&srtBy=byRel&bt=custV

Step 2	When prompted, log in with your Cisco.com user ID and password.

Step 3	To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter .

## Cisco IP Phone Firmware Support Policy

For information on the support policy for Cisco IP Phones, see http://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/unified-ip-phone-7900-series/116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

Copyright © 2009-2017 Cisco Systems, Inc. All rights reserved.

| Region | Region-Specific Firmware |
|---|---|
| North America | cp-8831-sip.9-3-4-4-3PCC.bin.sgn cp-8831-sip.9-3-4-4-3PCC-NA.bin.sgn |
| Europe | cp-8831-sip.9-3-4-4-3PCC-EU.bin.sgn |
| Latin America | cp-8831-sip.9-3-4-4-3PCC-LA.bin.sgn |
| Brazil | cp-8831-sip.9-3-4-4-3PCC-BR.bin.sgn |
| Taiwan | cp-8831-sip.9-3-4-4-3PCC-TW.bin.sgn |
| Japan | cp-8831-sip.9-3-4-4-3PCC-JP.bin.sgn |