---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-firmware-1-9-0-w800-b-cisco-wireless-phone-840-and-860-190-1356c482b3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/firmware/1-9-0/w800_b_cisco-wireless-phone-840-and-860_190.html
retrieved_at: 2026-08-21T23:35:50.363004+00:00
---

Cisco Wireless Phone 840 and 860 Release Notes for Firmware Release 1.9(0)

# Cisco Wireless Phone 840 and 860 Release Notes for Firmware Release 1.9(0)

### Download Options

Updated: April 28, 2023

First Published: April 28, 2023

Last Updated: April 28, 2023

# Cisco Wireless Phone 840 and 860 Release Notes for Firmware Release 1.9(0)

These release notes support the Cisco Wireless Phone 840 and 860 software release 1.9(0). These wireless smartphones require:

Call Control

Cisco Unified Communications Manager

Minimum: 11.5(1)

Recommended: 12.5(1), 14.0(1), or higher)

Webex Calling

Wireless LAN Controller and Access Points

See the Cisco Wireless Phone 840 and 860 Deployment Guide for supported solutions.

## What’s new in this release?

The following sections describe the features that are new or have changed in this release.

Cisco Unified Survivable Remote Site Telephony

Cisco Wireless Phones 840 and 860 now support the Survivable Remote Site Telephony (SRST) .

Add Configuration File Dump to Cisco Apps and Log Bundles

The log bundle now includes a configuration .zip file.

CUCM Call Pickup

Cisco Unified Communications Manager Call Pickup allows you to pick up call from other phones when the phone is busy or in
                  a call queue or shared line group.

Report a Problem User Choice in Cisco Phone UI

Report any of the following issue types by filling out a brief comment, date, and time of issue occurred.

Telephony call (dropper, other)

Audio quality

Battery

Other

Diagnostics Application

Diagnostics application helps administrator to perform diagnostics tests quickly and efficiently to verify phone’s hardware
                  components.

NTP in Web Access Network Information

Displays NTP server address in Network Information tab of Phone Webpage and on Phone Status page.

CAC is Disabled by Default

Call Admission Control (CAC) is now disabled by default.

The following features require the latest device enabler QED installer and software COP files (Update QED to Version 1.9.0
                              and Firmware 1.9.0). Also, the 1.9.0 QED COP file must be applied. Just by applying the Firmware COP will not enable these
                              features.

Announced Caller ID

Provides an audible announcement of who is calling you.

Mute SIP Registration Notifications

A new option to mute SIP registration notifications.

Push Custom Ringtone, Notification, Alarm, and Wallpaper

Allows you to specify a custom ringtone, notification sound, alarm sound, and wallpaper per phone within CUCM.

### Where to Find More Information

Cisco Wireless Phone 840 and 860 User Guide

Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

## Installation

Refer to the following documents for installation instructions.

840 - https://www.cisco.com/web/software/282074288/164620/cmterm-840.1-9-0-1914-65593-readme.html

860 - https://www.cisco.com/web/software/282074288/164620/cmterm-860.1-9-0-2409-65593-readme.html

## Open bugs

Bug number

Description

CSCwc20252

860–840 Bluetooth Pairing Mode Confusion vulnerability.

CSCwd73349

Conference not recorded when user creates a conference with a call on hold.

CSCwe57179

Phone didn't reregister to Webex after network outage and initial reconnection attempt failed.

CSCwe98811

WebAPI Widget on 840 and 860 phones goes into "loading icons" state.

## Resolved bugs

Bug number

Description

CSCwe41696

Airplane mode remains enabled after exiting SAFE mode.

CSCwe57185

Call dropped by CUCM because phone did not reregister in time.

## Bug Search Tool

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for
                  other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

View All Caveats

View Open Caveats

View Resolved Caveats

Americas Headquarters

Cisco Systems, Inc.

San Jose, CA

Asia pacific Headquarters

Cisco Systems (USA) Pte. Ltd.

Singapore

Europe Headquarters

Cisco Systems International BV Amsterdam,

The Netharlands

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco Website at www.cisco.com/go/offices .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries.
                              To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply
                              a partnershiprelationship between Cisco and any other company. (1110R)

| Note | The following features require the latest device enabler QED installer and software COP files (Update QED to Version 1.9.0
                              and Firmware 1.9.0). Also, the 1.9.0 QED COP file must be applied. Just by applying the Firmware COP will not enable these
                              features. |
|---|---|

| Bug number | Description |
|---|---|
| CSCwc20252 | 860–840 Bluetooth Pairing Mode Confusion vulnerability. |
| CSCwd73349 | Conference not recorded when user creates a conference with a call on hold. |
| CSCwe57179 | Phone didn't reregister to Webex after network outage and initial reconnection attempt failed. |
| CSCwe98811 | WebAPI Widget on 840 and 860 phones goes into "loading icons" state. |

| Bug number | Description |
|---|---|
| CSCwe41696 | Airplane mode remains enabled after exiting SAFE mode. |
| CSCwe57185 | Call dropped by CUCM because phone did not reregister in time. |

|  |  |  |
|---|---|---|
| Americas Headquarters Cisco Systems, Inc. San Jose, CA | Asia pacific Headquarters Cisco Systems (USA) Pte. Ltd. Singapore | Europe Headquarters Cisco Systems International BV Amsterdam, The Netharlands |
| Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco Website at www.cisco.com/go/offices . |
| Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries.
                              To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply
                              a partnershiprelationship between Cisco and any other company. (1110R) |