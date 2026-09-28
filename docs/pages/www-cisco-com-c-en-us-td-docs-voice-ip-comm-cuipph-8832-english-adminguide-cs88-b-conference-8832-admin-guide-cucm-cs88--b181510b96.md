---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-english-adminguide-cs88-b-conference-8832-admin-guide-cucm-cs88--b181510b96
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/english/adminguide/cs88_b_conference-8832-admin-guide-cucm/cs88_b_conference-8832-admin-guide-cucm_chapter_00.html
retrieved_at: 2026-08-21T13:36:38.033763+00:00
---

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

# Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Cisco IP Conference Phone Hardware

## Chapter: Cisco IP Conference Phone Hardware

# Cisco IP Conference Phone Hardware

## Cisco IP Conference Phone 8832

The Cisco IP Conference Phone 8832 and 8832NR enhance people-centric communications. It combines superior high‑definition (HD) audio performance and 360-degree
                              coverage for medium to large conference rooms and executive offices. It provides an audiophile sound experience with a full-duplex
                              two-way wideband (G.722) audio hands-free speaker. This phone is a simple solution that meets the challenges of the most diverse
                              rooms.

The conference phone has four built-in sensitive microphones with 360-degree coverage. This coverage lets you speak in a normal
                              voice and be heard clearly from up to 10 feet (3 m) away. The phone also features technology that resists interference from
                              mobile phones and other wireless devices, which assures delivery of clear communications without distractions. The phone provides
                              a color screen and softkey buttons to access user functions. With the base unit alone, the phone provides coverage for a 20
                              x 20 ft. (6.1 x 6.1 m) room and up to 10 people.

Two wired expansion microphones are available for use with the phone. Placing the expansion microphones away from the base
                              unit provides greater coverage in larger conference rooms. With the base unit and wired expansion microphones, the conference
                              phone provides coverage for a 20 x 34 ft. (6.1 x 10 m) room and up to 22 people.

The phone also supports an optional set of two wireless expansion microphones. With the base unit and wireless expansion microphones,
                              the conference phone provides coverage for a 20 x 40 ft. (6.1 x 12.2 m) room and up to 26 people. To cover a 20 x 40 ft. room,
                              we recommend that you place each microphone at a maximum distance of 10 ft. from the base.

You can connect two base units to increase the coverage for a room. This configuration requires the optional Daisy Chain kit
                              and can support two expansion microphones (either wired or wireless, but not a mixed combination). If you are using wired
                              microphones with the Daisy Chain kit, the configuration provides coverage for a room up to 20 x 50 feet (6.1 x 15.2 m) and
                              up to 38 people. If you are using wireless microphones with the Daisy Chain kit, the configuration provides coverage for a
                              room up to 20 x 57 feet (6.1 x 17.4 m) and up to 42 people.

The Cisco IP Conference Phone 8832NR (non-radio) version does not support Wi-Fi, wireless expansion microphones, or Bluetooth.

Like other devices, a Cisco IP Phone must be configured and managed. These phones encode and decode the following codecs:

G.711 a-law

G.711 mu-law

G.722

G722.2 AMR-WB

G.729a/G.729ab

G.726

iLBC

Opus

Caution

Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone might cause interference. For
                                          more information, see the manufacturer’s documentation of the interfering device.

Cisco IP Phones provide traditional telephony functionality, such as call forwarding and transferring, redialing, speed dialing,
                              conference calling, and voice messaging system access. Cisco IP Phones also provide a variety of other features.

As with other network devices, you must configure Cisco IP Phones to prepare them to access Cisco Unified Communications Manager
                              and the rest of the IP network. By using DHCP, you have fewer settings to configure on a phone. If your network requires it,
                              however, you can manually configure information such as: an IP address, TFTP server, and subnet information.

Cisco IP Phones can interact with other services and devices on your IP network to provide enhanced functionality. For example,
                              you can integrate Cisco Unified Communications Manager with the corporate Lightweight Directory Access Protocol 3 (LDAP3)
                              standard directory to enable users to search for coworker contact information directly from their IP phones. You can also
                              use XML to enable users to access information such as weather, stocks, quote of the day, and other web-based information.

Finally, because the Cisco IP Phone is a network device, you can obtain detailed status information from it directly. This
                              information can assist you with troubleshooting any problems users might encounter when using their IP phones. You can also
                              obtain statistics about an active call or firmware versions on the phone.

To function in the IP telephony network, the Cisco IP Phone must connect to a network device, such as a Cisco Catalyst switch.
                              You must also register the Cisco IP Phone with a Cisco Unified Communications Manager system before sending and receiving
                              calls.

## Cisco IP Conference Phone 8832 Buttons and Hardware

The following figure shows the Cisco IP Conference Phone 8832.

The following table describes the buttons on the Cisco IP Conference Phone 8832.

1

LED bar

Indicates call states:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

2

Expansion microphone port

The wired expansion microphone cable plugs into the port.

3

Mute bar

Toggles the microphone on or off. When you mute the microphone, the LED bar lights red.

4

Softkey buttons

Access functions and services.

5

Navigation bar and Select button

Scroll through menus, highlight items, and select the highlighted item.

6

Volume button

Adjusts the speakerphone volume (off hook) and the ringer volume (on hook).

When you change the volume, the LED bar lights white to show the volume change.

### Wired Expansion Microphone (8832 0nly)

The Cisco IP Conference Phone 8832 supports two wired expansion microphones, available in an optional kit. Use the expansion microphones in larger rooms or
                                 in a crowded room. For best results, we recommend that you place the microphones between 3 feet (0.91 m) and 7 feet (2.1 m)
                                 away from the phone.

When you're in a call, the expansion microphone LED around the Mute button is green.

When you mute the microphone, the LED is red. When you press the Mute button, the phone and the expansion microphones are muted.

### Wireless Expansion Microphone (8832 Only)

The Cisco IP Conference Phone 8832 supports two expansion wireless microphones, available with a charging cradle in an optional kit. When the wireless microphone
                                 is placed on the charging cradle for charging, the LED on the cradle is lit white.

When the conference phone is in a call, the expansion microphone LED around the Mute button is lit green.

When the microphone is muted, the LED is lit red. When you press the Mute button, the phone and the expansion microphones are muted.

If the phone is paired with a wireless microphone (for example, Wireless microphone 1) and you connect the wireless microphone
                                 to a charger, pressing the Show detail softkey indicates the charge level for that microphone.

When the phone is paired with a wireless microphone and you connect a wired microphone, the wireless microphone gets unpaired
                                 and the phone is paired with the wired microphone. A notification appears on the phone screen indicating that the wired microphone
                                 is connected.

## Related
                        	 Documentation

### Cisco IP Conference Phone 8832 Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Conference Phone 8832.

### Cisco Unified
                              				Communications Manager Documentation

See the Cisco Unified
                                       				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                                    				Communications Manager release on the product support page.

### Cisco Unified
                              				Communications Manager Express Documentation

See the publications that are specific to your language, phone model, and release on the product support page for Cisco Unified
                                       				Communications Manager Express .

### Cisco Hosted Collaboration Service Documentation

See the Cisco Hosted Collaboration
                                       				Solution Documentation Guide and other publications that are specific to your Cisco Hosted Collaboration
                                    				Solution release. Navigate from the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html

### Cisco Business Edition 4000 Documentation

See the Cisco Business Edition 4000 Documentation Guide and other publications that are specific to your Cisco Business Edition 4000 release. Navigate from the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-4000/tsd-products-support-series-home.html

## Documentation, Support, and Security Guidelines

For information on obtaining documentation, obtaining support,
                           		providing documentation feedback, reviewing security guidelines, and also recommended
                           		aliases and general Cisco documents, see the monthly What’s New in Cisco
                              		  Product Documentation , which also lists all new and revised Cisco
                           		technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product
                              		  Documentation as a Really Simple Syndication (RSS) feed and set content
                           		to be delivered directly to your desktop using a reader application. The RSS
                           		feeds are a free service and Cisco currently supports RSS Version 2.0.

### Cisco Product Security Overview

This product contains cryptographic features and is subject to U.S. and local country laws that govern import, export, transfer,
                              and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute, or use
                              encryption. Importers, exporters, distributors, and users are responsible for compliance with U.S. and local country laws.
                              By using this product, you agree to comply with applicable laws and regulations. If you are unable to comply with U.S. and
                              local laws, return this product immediately.

Further information regarding U.S. export regulations can be found at https://www.bis.gov/ear .

## Terminology Differences

In this document, the term Cisco IP Phone includes the Cisco IP Conference Phone 8832.

The following table highlights some of the terminology differences in the Cisco IP Conference Phone 8832 User Guide , the Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager , and the Cisco Unified Communications Manager documentation.

User Guide

Administration Guide

Message Indicators

Message Waiting Indicator (MWI)

Voicemail System

Voice Messaging System

| Caution | Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone might cause interference. For
                                          more information, see the manufacturer’s documentation of the interfering device. |
|---|---|

| 1 | LED bar | Indicates call states: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
|---|---|---|
| 2 | Expansion microphone port | The wired expansion microphone cable plugs into the port. |
| 3 | Mute bar | Toggles the microphone on or off. When you mute the microphone, the LED bar lights red. |
| 4 | Softkey buttons | Access functions and services. |
| 5 | Navigation bar and Select button | Scroll through menus, highlight items, and select the highlighted item. |
| 6 | Volume button | Adjusts the speakerphone volume (off hook) and the ringer volume (on hook). When you change the volume, the LED bar lights white to show the volume change. |

| User Guide | Administration Guide |
|---|---|
| Message Indicators | Message Waiting Indicator (MWI) |
| Voicemail System | Voice Messaging System |