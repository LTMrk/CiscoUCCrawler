---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-device-packs-1501-devpack-for-may-2026-html-0509b67c09
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/device_packs/1501-devpack-for-may-2026.html
retrieved_at: 2026-08-17T01:02:29.005097+00:00
---

Cisco Unified Communications Device Package 15.0(1.15031-2) Release Notes

# Cisco Unified Communications Device Package 15.0(1.15031-2) Release Notes

### Download Options

Updated: May 4, 2026

First Published: May 4, 2026

# Introduction

Cisco Unified
                     				Communications Manager Device Package Release 15.0(1.15031-2) provides database and firmware updates for Cisco Unified
                     				Communications Manager 15.

For information about all released Cisco Unified
                     				Communications Manager device packages, see the Cisco Unified Communications Manager Device Package Compatibility Matrix .

For information about how to install Cisco Unified
                     				Communications Manager device packages, see the Cisco Unified Communications Manager Device Package Installation Guide .

Caution

Installing the Device Package on the Publisher causes all of the device XML data to be reloaded into the database. This can
                              cause high CPU on the Subscribers while these changes are being processed. It is recommended that Device Package installations
                              occur during a maintenance window to minimize the impact of the database updates.

## Cisco Unified Communications Device Package 15

Caution

After applying the device package COP file, make sure that any future full upgrades are to a version that contains the device
                                 package fixes natively. Otherwise, some of the functionality added by the device package may be lost following the upgrade.
                                 If an upgrade to a version that does not contain the fixes natively is necessary, install the appropriate device package COP
                                 file to restore functionality.

The Cisco Unified
                        				Communications Manager Device Package 15.0(1.15031-2) filename and MD5 are in the following table.

File

MD5

cmterm-devicepack15.0.1.15031-2.cop.sha512

72496bd8630c346633cead61516c1b7a

Use the information in the following table to determine if you must install this device package.

Device

Bug ID

Headline

Database Update

Firmware Upgrade

Notes

Cisco Headsets

CSCwu02324

Checkin headset cop file 4-0-0001-1 to cucm

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwu02324 .

Desk Phone 9800 Series / Cisco Video Phone 8875

CSCws76199

Checkin PhoneOS 4.0(1) QED files to CUCM

Yes

No

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws76199 .

Desk Phone 9800 Series / Cisco Video Phone 8875

CSCwt39204

Checkin PhoneOS 4.1(1) firmware to CUCM

No

Yes

For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt39204 .

## Firmware Table

The Cisco Unified
                        				Communications Manager Device Package Release 15.0(1.15031-2) contains loads for the following device releases.

The device package also contains configuration files for many Cisco Webex models. If there are any new configuration files
                                 for these models, they are listed in the previous table: Cisco Unified Communications Device Package 15 . You can get the latest firmware for these models from the Download Software page.

Starting with the PhoneOS 3.2(1) release, the Video Phone 8875 now shares the same firmware files as the Desk Phone 9800 Series
                                 endpoints. There is no longer a standalone 8875 firmware file included in the Device Packs.

The PhoneOS firmware is now included in the Device Packs. There is no longer a need to downlaod and install this firmware
                                 separately.

### Firmware Versions in this Release

```
Device type                               Load name                       Version
----------------------------------------  ------------------------------  ----------
3905                                      3905.9-4-1SR4-2                 9.4(1SR4.2)
7832-sip.14                               7832-sip.14-4-1-0101-153.k4     4.1(0101.153)
78xx.14                                   78xx.14-4-1-0101-153.k4         4.1(0101.153)
8832-sip.14                               8832-sip.14-4-1-0101-153.k4     4.1(0101.153)
8845_65-sip.14                            8845_65-sip.14-4-1-0001-36.k4   4.1(0001.36)
88xx-sip.14                               88xx-sip.14-4-1-0101-153.k4     4.1(0101.153)
ATA191.12                                 ATA191.12-0-3-0101-142          0.3(0101.142)
headset-builtin                           headset-builtin.4-0-0001-1.k4   4.0(0001.1)
PHONEOS.4                                 PHONEOS.4-1-1-0001-74           1.1(0001.74)
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
| cmterm-devicepack15.0.1.15031-2.cop.sha512 | 72496bd8630c346633cead61516c1b7a |

| Device | Bug ID | Headline | Database Update | Firmware Upgrade | Notes |
|---|---|---|---|---|---|
| Cisco Headsets | CSCwu02324 | Checkin headset cop file 4-0-0001-1 to cucm | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwu02324 . |
| Desk Phone 9800 Series / Cisco Video Phone 8875 | CSCws76199 | Checkin PhoneOS 4.0(1) QED files to CUCM | Yes | No | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws76199 . |
| Desk Phone 9800 Series / Cisco Video Phone 8875 | CSCwt39204 | Checkin PhoneOS 4.1(1) firmware to CUCM | No | Yes | For more information, see https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt39204 . |

| Note | The device package also contains configuration files for many Cisco Webex models. If there are any new configuration files
                                 for these models, they are listed in the previous table: Cisco Unified Communications Device Package 15 . You can get the latest firmware for these models from the Download Software page. |
|---|---|

| Note | Starting with the PhoneOS 3.2(1) release, the Video Phone 8875 now shares the same firmware files as the Desk Phone 9800 Series
                                 endpoints. There is no longer a standalone 8875 firmware file included in the Device Packs. |
|---|---|

| Note | The PhoneOS firmware is now included in the Device Packs. There is no longer a need to downlaod and install this firmware
                                 separately. |
|---|---|