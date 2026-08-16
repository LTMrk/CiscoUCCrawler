---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-device-packs-1401-devpack-for-feb-2026-html-19e06df637
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/device_packs/1401-devpack-for-feb-2026.html
retrieved_at: 2026-08-16T23:41:07.206741+00:00
---

Cisco Unified Communications Device Package 14.0(1.16076-1) Release Notes

# Cisco Unified Communications Device Package 14.0(1.16076-1) Release Notes

### Download Options

Updated: February 9, 2026

First Published: February 9, 2026

# Introduction

Cisco Unified
                     				Communications Manager Device Package Release 14.0(1.16076-1) provides database and firmware updates for Cisco Unified
                     				Communications Manager 14.

For information about all released Cisco Unified
                     				Communications Manager device packages, see the Cisco Unified Communications Manager Device Package Compatibility Matrix .

For information about how to install Cisco Unified
                     				Communications Manager device packages, see the Cisco Unified Communications Manager Device Package Installation Guide .

Caution

Installing the Device Package on the Publisher causes all of the device XML data to be reloaded into the database. This can
                              cause high CPU on the Subscribers while these changes are being processed. It is recommended that Device Package installations
                              occur during a maintenance window to minimize the impact of the database updates.

## Cisco Unified Communications Device Package 14

Caution

After applying the device package COP file, make sure that any future full upgrades are to a version that contains the device
                                 package fixes natively. Otherwise, some of the functionality added by the device package may be lost following the upgrade.
                                 If an upgrade to a version that does not contain the fixes natively is necessary, install the appropriate device package COP
                                 file to restore functionality.

The Cisco Unified
                        				Communications Manager Device Package 14.0(1.16076-1) filename and MD5 are in the following table.

File

MD5

cmterm-devicepack14.0.1.16076.cop.sha512

ed1af373b031c4da6a3fa3e8fadbe355

Use the information in the following table to determine if you must install this device package.

Device

Bug ID

Headline

Database Update

Firmware Upgrade

Notes

Analog Telephony Adapter 191

CSCwt02954

Commit 12‑0‑3‑0101‑142 ATA191 Load into UCM ISO and DevPack

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt02954 .

Desk Phone 9800 Series / Cisco Video Phone 8875

CSCws76199

Checkin PhoneOS 4.0(1) QED files to CUCM

Yes

No

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws76199 .

Desk Phone 9800 Series / Cisco Video Phone 8875

CSCws76200

Checkin PhoneOS 4.0(1) firmware to CUCM

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws76200 .

IP Phone 7800/8800 Series

CSCwt03065

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt03065 .

Cisco Desk Pro G2

CSCwo55959

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo55959 .

Cisco Codec Pro G2

CSCws04517

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws04517 .

## Firmware Table

The Cisco Unified
                        				Communications Manager Device Package Release 14.0(1.16076-1) contains loads for the following device releases.

The device package also contains configuration files for many Cisco Webex models. If there are any new configuration files
                                 for these models, they are listed in the previous table: Cisco Unified Communications Device Package 14 . You can get the latest firmware for these models from the Download Software page.

Starting with the PhoneOS 3.2(1) release, the Video Phone 8875 now shares the same firmware files as the Desk Phone 9800 Series
                                 endpoints. There is no longer a standalone 8875 firmware file included in the Device Packs.

The PhoneOS firmware is now included in the Device Packs. There is no longer a need to downlaod and install this firmware
                                 separately.

### Firmware Versions in this Release

```
Device type                               Load name                       Version
----------------------------------------  ------------------------------  ----------
3905                                      3905.9-4-1SR4-2                 9.4(1SR4.2)
6901-sccp                                 6901-sccp.9-3-1-SR3-2.k4        9.3(1.0)  
6901-sip                                  6901-sip.9-3-1-SR3-2.k4         9.3(1.0)  
7832-sip                                  7832-sip.14-4-1-0101-153.k4     14.4.1(0101.153)
78xx                                      78xx.14-4-1-0101-153.k4         14.4.1(0101.153)
8821-sip                                  8821-sip.11-0-6SR7-2.k4         11.0(6SR7.2)
8832-sip                                  8832-sip.14-4-1-0101-153.k4     14.4.1(0101.153)
8845_65-sip                               8845_65-sip.14-4-1-0001-36.k4   14.4.1(0001.36)
88xx-sip                                  88xx-sip.14-4-1-0101-153.k4     14.4.1(0101.153)
ATA191                                    ATA191.12-0-3-0101-142          12.0.3(0101.142)
headset-builtin                           headset-builtin.3-4-0001-1.k4   3.4(0001.1)
PHONEOS                                   PHONEOS.4-0-1-0002-64           4.0.1(0002.64)
```

| Caution | Installing the Device Package on the Publisher causes all of the device XML data to be reloaded into the database. This can
                              cause high CPU on the Subscribers while these changes are being processed. It is recommended that Device Package installations
                              occur during a maintenance window to minimize the impact of the database updates. |
|---|---|

| Caution | After applying the device package COP file, make sure that any future full upgrades are to a version that contains the device
                                 package fixes natively. Otherwise, some of the functionality added by the device package may be lost following the upgrade.
                                 If an upgrade to a version that does not contain the fixes natively is necessary, install the appropriate device package COP
                                 file to restore functionality. |
|---|---|

| File | MD5 |
|---|---|
| cmterm-devicepack14.0.1.16076.cop.sha512 | ed1af373b031c4da6a3fa3e8fadbe355 |

| Device | Bug ID | Headline | Database Update | Firmware Upgrade | Notes |
|---|---|---|---|---|---|
| Analog Telephony Adapter 191 | CSCwt02954 | Commit 12‑0‑3‑0101‑142 ATA191 Load into UCM ISO and DevPack | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt02954 . |
| Desk Phone 9800 Series / Cisco Video Phone 8875 | CSCws76199 | Checkin PhoneOS 4.0(1) QED files to CUCM | Yes | No | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws76199 . |
| Desk Phone 9800 Series / Cisco Video Phone 8875 | CSCws76200 | Checkin PhoneOS 4.0(1) firmware to CUCM | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws76200 . |
| IP Phone 7800/8800 Series | CSCwt03065 | 14.4(1)SR1 SIP phone firmware files for 7800 and 8800 IP Phones | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt03065 . |
| Cisco Desk Pro G2 | CSCwo55959 | Add support for Cisco Desk Pro G2 | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo55959 . |
| Cisco Codec Pro G2 | CSCws04517 | Add support for Cisco Codec Pro G2 | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws04517 . |

| Note | The device package also contains configuration files for many Cisco Webex models. If there are any new configuration files
                                 for these models, they are listed in the previous table: Cisco Unified Communications Device Package 14 . You can get the latest firmware for these models from the Download Software page. |
|---|---|

| Note | Starting with the PhoneOS 3.2(1) release, the Video Phone 8875 now shares the same firmware files as the Desk Phone 9800 Series
                                 endpoints. There is no longer a standalone 8875 firmware file included in the Device Packs. |
|---|---|

| Note | The PhoneOS firmware is now included in the Device Packs. There is no longer a need to downlaod and install this firmware
                                 separately. |
|---|---|