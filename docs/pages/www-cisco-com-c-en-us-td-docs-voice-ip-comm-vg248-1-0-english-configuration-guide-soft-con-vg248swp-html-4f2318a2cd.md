---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-0-english-configuration-guide-soft-con-vg248swp-html-4f2318a2cd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_0/english/configuration/guide/soft_con/vg248swp.html
retrieved_at: 2026-08-22T01:20:10.160091+00:00
---

Software Configuration Guide (Version 1.0)

# Software Configuration Guide (Version 1.0)

Updated: March 17, 2015

Chapter: Configuring Analog Phones Using Cisco CallManager

## Chapter: Configuring Analog Phones Using Cisco CallManager

## Configuring Analog Phones Using Cisco CallManager

The VG248 connects to Cisco CallManager to provide access from the analog phones to Cisco CallManager. To configure the analog phones using Cisco CallManager, you actually configure the ports on the VG248. The changes you make to a specific port (such as disabling call waiting or assigning speed dials) apply directly to the analog device connected to that port.

The following sections provide an overview of the configuration requirements for Cisco CallManager:

• Overview

• Adding the VG248 to Cisco CallManager

• Configuring the VG248 Ports

This guide does not contain details about configuring Cisco CallManager. Refer to the documentation and online help provided with Cisco CallManager for installation and configuration instructions.

## Overview

Cisco CallManager does not recognize the VG248 as a single IP telephony device. Instead, each of the 48 ports are identified as individual devices, similar to IP phones.

## Adding the VG248 to Cisco CallManager

You can add the VG248 ports to Cisco CallManager automatically or manually. These sections provide the details:

• Using Auto-Registration

• Manually Adding the VG248

### Using Auto-Registration

You can choose to have the VG248 automatically added to Cisco CallManager using auto-registration. To do this, you must

• Verify that auto-registration is enabled in Cisco CallManager. Refer to the documentation or online help included with the Cisco CallManager application for details.

• Verify that the VG248 port enable policy is set to "auto." See the "Setting the Port Enable Policy" section on page 3-7 for details.

When the VG248 connects to Cisco CallManager through auto-registration, each port connected to an analog device registers itself as a Cisco VGC phone.

Auto-registration automatically assigns phones a directory number. The directory number assigned is the next one available in sequential order within the device pool assigned to this phone type in Cisco CallManager. However, if you need to, you can modify this directory number for each emulated phone (see the "Configuring the VG248 Ports" section ).

During auto-registration, the host name assigned to the VG248 is entered in the Description field in the record for the emulated phone in Cisco CallManager. If you do not enter a host name, the following sequence applies for the device description: VGC + the last 10 digits of the MAC address.

Additionally, Cisco CallManager requires unique MAC addresses for all devices, but all 48 ports on the VG248 share the same MAC address. Therefore, auto-registration includes a process that converts the MAC addresses into this format:

1. The first two digits of the MAC address are dropped.

2. The number is shifted two places to the left.

3. The two-digit port number is added to the right.

For example, if the MAC address on the VG248 is 000039A44218

the MAC address registered for port 12 in CallManager is 0039A4421812

After adding each port, make configuration changes as described in the "Configuring the VG248 Ports" section .

### Manually Adding the VG248

If you want to assign specific directory numbers to the emulated IP phones on the VG248 without using auto-registration, you must manually add each phone to the Cisco CallManager database. Keep in mind several important facts:

• To add a VG248 port to Cisco CallManager,

a. From Cisco CallManager, choose Devices > Add a New Device.

b. Choose Cisco VGC Phone from the Phone type menu.

c. Click Next .

• Each port must have a unique MAC address. Use the auto-registration formula (see page 4-2) to calculate the MAC address for each port.

• Use the host name or other name for the Description for each port. For ease of administration, use a similar name for ports configured on the same VG248.

• Consider adding a descriptive line to the Display field, such as "Analog phone."

• Configure each port as described in the "Configuring the VG248 Ports" section .

## Configuring the VG248 Ports

Each port on the VG248 corresponds to an analog device in your IP telephony network. To manage these devices using Cisco CallManager you must add each port to the Cisco CallManager database. To Cisco CallManager, each port is recognized and handled as a phone.

For example, if you have 48 devices connected to the VG248, you must add and configure 48 ports to Cisco CallManager. Cisco CallManager recognizes 48 separate phones connected to it.

After these phones are added to Cisco CallManager, treat them as you would any other phone in your IP telephony network. You need to add directory numbers, calling search space, and so on.

Refer to the documentation and online help included with Cisco CallManager for details.