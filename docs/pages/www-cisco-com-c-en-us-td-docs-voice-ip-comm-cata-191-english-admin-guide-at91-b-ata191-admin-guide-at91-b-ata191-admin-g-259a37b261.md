---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-259a37b261
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_01011.html
retrieved_at: 2026-08-22T01:12:14.532071+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: ATA 191 Country-Specific Tones and Cadences

## Chapter: ATA 191 Country-Specific Tones and Cadences

# ATA 191 Country-Specific Tones and Cadences

ATA 191 Country-Specific Tones and Cadences

## Mechanism

The administrator can upload an XML file named g3-tones.xml that describes the tones and cadences to the directory on the
                           Cisco Unified Communications Manager TFTP server. The directory name is actually a locale name, such as Australia .

During provisioning, the device knows the network locale setting and tries to download [locale name]/g3-tones.xml from the Cisco Unified CM TFTP server. For example, if the network locale is set to Australia , the path is Australia/g3-tones.xml .

## Link a Tone File with a Device

Use one of the following methods to link the tone file with the device.

Method 1: In Cisco Unified Communications Manager, navigate to System > Device Pool , and set the Network Locale value to specify the locale option.

Method 2: In Cisco Unified Communications Manager, navigate to Device > Phone . On the device window, set the value of Network Locale, which overwrites the value that is set in method 1.

For method 2, network locale from Device > Phone is not configurable currently because there are only two choices: none and United States. There is a known issue for Cisco
                                                         Unified Communications Manager that countries other than the United States cannot be selected from this menu. Method 2 has
                                                         a higher priority than method 1.

## Tone Configuration

Only the ATA 191 Line1 network locale setting is applied. The line2 network locale always applies the line1 option, even if
                                 the configured value of line2 network locale differs from the line1 value.

Only these tones can be configured:

Ringback tone

Reorder tone

Dialing tone

Outside dialing tone

Busy tone

Call waiting tone

Any tone specification that appears in the tone profile but is not supported or has invalid data fields (even if the tone
                           is supported) is ignored.

Example: A tone profile includes a valid reorder tone specification, an invalid busy tone specification (has invalid data fields),
                                 and a recording tone spec (not supported). Only the reorder tone spec would be applied.

The name of the XML file that describes tones and cadences is g3-tones.xml .

Each tone can specify at most four c/i pairs (about frequency and gain) and four cadence segments (each is an on/off pair).
                                 Any additional data gets discarded.

| Use one of the following methods to link the tone file with the device. Method 1: In Cisco Unified Communications Manager, navigate to System > Device Pool , and set the Network Locale value to specify the locale option. Method 2: In Cisco Unified Communications Manager, navigate to Device > Phone . On the device window, set the value of Network Locale, which overwrites the value that is set in method 1. Note For method 2, network locale from Device > Phone is not configurable currently because there are only two choices: none and United States. There is a known issue for Cisco
                                                         Unified Communications Manager that countries other than the United States cannot be selected from this menu. Method 2 has
                                                         a higher priority than method 1. | Note | For method 2, network locale from Device > Phone is not configurable currently because there are only two choices: none and United States. There is a known issue for Cisco
                                                         Unified Communications Manager that countries other than the United States cannot be selected from this menu. Method 2 has
                                                         a higher priority than method 1. |
|---|---|---|
| Note | For method 2, network locale from Device > Phone is not configurable currently because there are only two choices: none and United States. There is a known issue for Cisco
                                                         Unified Communications Manager that countries other than the United States cannot be selected from this menu. Method 2 has
                                                         a higher priority than method 1. |

| Note | For method 2, network locale from Device > Phone is not configurable currently because there are only two choices: none and United States. There is a known issue for Cisco
                                                         Unified Communications Manager that countries other than the United States cannot be selected from this menu. Method 2 has
                                                         a higher priority than method 1. |
|---|---|