---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-firmware-2-1-0-new-w800-b-cisco-wireless-phone-860-rn-210--2a03f4abd2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/firmware/2_1_0-new/w800_b_cisco-wireless-phone-860_rn-210.html
retrieved_at: 2026-08-21T09:59:08.735450+00:00
---

Cisco Wireless Phone 860 Release Notes for Firmware Release 2.1(0)

# Cisco Wireless Phone 860 Release Notes for Firmware Release 2.1(0)

### Download Options

Updated: July 7, 2025

First Published: July 7, 2025

# Cisco Wireless Phone 860 Release Notes for Firmware Release 2.1(0)

These release notes support the Cisco Wireless Phone 860 software release 2.1(0). These wireless smartphone require:

Call Control

Cisco Unified Communications Manager

Minimum: 11.5(1)

Recommended: 12.5(1), 14.0(1), or higher

Webex Calling

Wireless LAN Controller and Access Points

See the Cisco Wireless Phone 840 and 860 Deployment Guide for supported solutions.

## What’s New in This Release?

The following sections describe the features that are new or have changed in this release.

### Android 13 Update

With the release, for the Cisco Wireless Phone 860 phones, Android 10 has been updated to Android 13.

We recommend to analyze the functionality and the operational readiness of any custom or third party applications downloaded
                     to the Cisco Wireless 860 and 860S, after the upgrade from Android 10 to Android 13.

### Updates to the Webex Wireless Phone Configuration Management Tool (v2.1.0.6)

Newly added application options to support Android 13 configuration options

Under Choose Application, select,

- Custom Settings > User Restrictions: Allow manage notification settings button and Use Location to set time zone

- Custom Settings > User Restrictions > Quick Settings Tiles: Alarm, Device control, Screen record, Extra dim, QR scan, Color
                        correction, Live caption, and Calculator.

- Custom Settings > Time: Allow location to set time

- Custom Settings > Device info: Display Device info and Device Info (1 to 4)

- Barcode > General: Allow scan on screen lock and Allow URL redirection to browser

Application options name changes to support Android 13

Under Choose Application, select,

- Custom Settings > User Restrictions: Allow WiFi toggle is updated to Allow Internet toggle

WiFi is updated to Internet

Rotation lock is updated to Auto rotate

Cast is updated to Screen cast

Invert colors is updated to Color inversion

Nearby share is updated to Quick share

- Custom Settings > Camera: Jump to camera is updated to Quickly open camera

### Updated Call Quality Settings App

With this release, Wi-Fi preferences for Cisco Wireless Phone 860 is updated to support Android 13. CCKM and CAC options are removed from Wi-Fi preferences and not supported in the Firmware release 2.1(0) and later.

### Removal of Webex Application

With this release, Webex Application is removed for Cisco Wireless Phone 860 . The Webex application must be downloaded from the Google Play Store.

## Installation

Refer to the following documents for installation instructions.

Upgrade phones configured with an Alternate TFTP to version 1.10.4 before upgrading to version 2.1.0. Directly upgrading phones
                                    from version 1.10.3 or earlier to 2.1.0 will result in the loss of the Alternate TFTP configuration. In such cases, you must
                                    manually reconfigure the Alternate TFTP or enable DHCP option 150 or 66 for the Wi-Fi network.

With firmware release 2.1(0) for Cisco Wireless Phone 860, the Android OS is upgraded from version 10 to 13. Since Android
                                    13 manages permissions differently, Cisco application permissions must be granted for the CP-860 software to function properly.

If the phone is managed by a Cisco Wireless Phone Configuration Management Utility configuration file, permissions are granted
                                    automatically. If the phone is managed by an EMM (Enterprise Mobility Management) solution, you must configure the EMM to
                                    grant all necessary permissions in the configuration profile or within the specific application settings. Additionally, location
                                    services must be enabled on the Android device.

If the phone is managed by an EMM (Enterprise Mobility Management) solution, after upgrading Cisco Wireless Phone 860 to Android
                                    13 with a firmware version 2.1, the EMM must reapply or push any custom configuration settings to the phone.

## Open Bug

Bug number

Description

CSCwc20252

860-840 Bluetooth Pairing Mode Confusion vulnerability.

CSCwn32012

860 Emergency App - Panic Button uses Secondary SIP Extension configured instead of lines on device

CSCwm87370

860 memory corruption vulnerability in DSP drivers software

## Resolved Bugs

Bug number

Description

CSCwm61819

Upon removing WiFi toggle from pull down of the Cisco Wireless Phone 860, it reappears upon a reboot.

## Bug Search Tool

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for
                     other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

View All Caveats

View Open Caveats

- View Resolved Caveats

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

| Note | Upgrade phones configured with an Alternate TFTP to version 1.10.4 before upgrading to version 2.1.0. Directly upgrading phones
                                    from version 1.10.3 or earlier to 2.1.0 will result in the loss of the Alternate TFTP configuration. In such cases, you must
                                    manually reconfigure the Alternate TFTP or enable DHCP option 150 or 66 for the Wi-Fi network. |
|---|---|

| Note | With firmware release 2.1(0) for Cisco Wireless Phone 860, the Android OS is upgraded from version 10 to 13. Since Android
                                    13 manages permissions differently, Cisco application permissions must be granted for the CP-860 software to function properly. If the phone is managed by a Cisco Wireless Phone Configuration Management Utility configuration file, permissions are granted
                                    automatically. If the phone is managed by an EMM (Enterprise Mobility Management) solution, you must configure the EMM to
                                    grant all necessary permissions in the configuration profile or within the specific application settings. Additionally, location
                                    services must be enabled on the Android device. |
|---|---|

| Note | If the phone is managed by an EMM (Enterprise Mobility Management) solution, after upgrading Cisco Wireless Phone 860 to Android
                                    13 with a firmware version 2.1, the EMM must reapply or push any custom configuration settings to the phone. |
|---|---|

| Bug number | Description |
|---|---|
| CSCwc20252 | 860-840 Bluetooth Pairing Mode Confusion vulnerability. |
| CSCwn32012 | 860 Emergency App - Panic Button uses Secondary SIP Extension configured instead of lines on device |
| CSCwm87370 | 860 memory corruption vulnerability in DSP drivers software |

| Bug number | Description |
|---|---|
| CSCwm61819 | Upon removing WiFi toggle from pull down of the Cisco Wireless Phone 860, it reappears upon a reboot. |

|  |  |  |
|---|---|---|
| Americas Headquarters Cisco Systems, Inc. San Jose, CA | Asia pacific Headquarters Cisco Systems (USA) Pte. Ltd. Singapore | Europe Headquarters Cisco Systems International BV Amsterdam, The Netharlands |
| Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco Website at www.cisco.com/go/offices . |
| Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries.
                                 To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply
                                 a partnershiprelationship between Cisco and any other company. (1110R) |