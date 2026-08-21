---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-english-ag-cs88-b-8832-mpp-ag-new-cs88-b-8832-mpp-ag-new-cha-5752886a81
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/english/AG/cs88_b_8832-mpp-ag_new/cs88_b_8832-mpp-ag_new_chapter_010010.html
retrieved_at: 2026-08-21T13:49:35.206877+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Cisco IP Conference Phone Hardware

## Chapter: Cisco IP Conference Phone Hardware

# Cisco IP Conference Phone Hardware

## Cisco IP Conference Phone 8832

The Cisco IP Conference Phone 8832 enhances people-centric communications. It combines superior high‑definition (HD) audio
                              performance and 360-degree coverage for medium to large conference rooms and executive offices. It provides an audiophile
                              sound experience with a full-duplex two-way wideband (G.722) audio hands-free speaker. This phone is a simple solution that
                              meets the challenges of the most diverse rooms

The conference phone has sensitive microphones with 360-degree coverage. This coverage lets you speak in a normal voice and
                              be heard clearly from up to 10 feet (3 m) away. The phone also features technology that resists interference from mobile phones
                              and other wireless devices, which assures delivery of clear communications without distractions. The phone provides a color
                              screen and softkey buttons to access user functions. With the base unit alone, the phone provides coverage for a 20 x 20 ft.
                              (6.1 x 6.1 m) room and up to 10 people.

Two wired expansion microphones are available for use with the phone. Placing the expansion microphones away from the base
                              unit provides greater coverage in larger conference rooms. With the base unit and wired expansion microphones, the conference
                              phone provides coverage for a 20 x 34 ft. (6.1 x 10 m) room and up to 22 people.

The phone also supports an optional set of two wireless expansion microphones. With the base unit and wireless expansion microphones,
                              the conference phone provides coverage for a 20 x 40 ft. (6.1 x 12.2 m) room and up to 26 people. To cover a 20 x 40 ft. room,
                              we recommend that you place each microphone at a maximum distance of 10 ft. from the base.

Like other devices, a Cisco IP Phone must be configured and managed. These phones encode and decode the following codecs:

G.711 a-law

- G.711 mu-law

- G.722

- G722.2 AMR-WB

G729a

- iLBC

Opus

Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone might cause interference. For
                                          more information, see the manufacturer’s documentation of the interfering device.

Cisco IP Phones provide traditional telephony functionality, such as call forwarding and transferring, redialing, speed dialing,
                              conference calling, and voice messaging system access. Cisco IP Phones also provide a variety of other features.

As with other network devices, you must configure Cisco IP Phones to prepare them to access the third-party server and the
                              rest of the IP network. By using DHCP, you have fewer settings to configure on a phone. If your network requires it, however,
                              you can manually configure information such as: an IP address, TFTP server, and subnet information.

Cisco IP Phones can interact with other services and devices on your IP network to provide enhanced functionality. For example,
                              you can integrate the third-party server with the corporate Lightweight Directory Access Protocol 3 (LDAP3) standard directory
                              to enable users to search for coworker contact information directly from their IP phones.

Finally, because the Cisco IP Phone is a network device, you can obtain detailed status information from it directly. This
                              information can assist you with troubleshooting any problems users might encounter when using their IP phones. You can also
                              obtain statistics about an active call or firmware versions on the phone.

To function in the IP telephony network, the Cisco IP Phone must connect to a network device, such as a Cisco Catalyst switch.
                              You must also register the Cisco IP Phone with a third-party server before sending and receiving calls.

## Phones Supported in this Document

This document supports these phones:

Cisco IP Conference Phone 8832 Multiplatform Phones

In this document, the term phone or Cisco IP Phone refers to the above phones.

## Cisco IP Conference Phone 8832 Buttons and Hardware

The following figure shows the Cisco IP Conference Phone 8832.

1

Mute bar

Toggle the microphone on or off. When the microphone is muted, the LED bar is lit red.

2

LED bar

Indicates call states:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

3

Softkey buttons

Access functions and services.

4

Navigation bar and Select button

Scroll through menus, highlight items, and select the highlighted item.

When the phone is idle, press Up to access the recent calls list and press Down to access the favorites list.

5

Volume button

Adjust the speakerphone volume (off hook) and the ringer volume (on hook).

When you change the volume, the LED bar lights white to show the volume change.

### Conference Phone Softkeys

You can interact with the features on your phone with the softkeys. Softkeys, located below the screen, give you access to
                                 the function displayed on the screen above the softkey. The softkeys change depending on what you are doing at the time.

The and softkeys indicate more softkey functions are available.

### Wired Expansion Microphone

The Cisco IP Conference Phone 8832 supports two wired expansion microphones, available in an optional kit. Use the expansion microphones in larger rooms or
                                 in a crowded room. For best results, we recommend that you place the microphones between 3 feet (0.91 m) and 7 feet (2.1 m)
                                 away from the phone.

When you're in a call, the expansion microphone LED around the Mute button is green.

When you mute the microphone, the LED is red. When you press the Mute button, the phone and the expansion microphones are muted.

### Wireless Expansion Microphone

The Cisco IP Conference Phone 8832 supports two expansion wireless microphones, available with a charging cradle in an optional kit. When the wireless microphone
                                 is placed on the charging cradle for charging, the LED on the cradle is lit white.

When the conference phone is in a call, the expansion microphone LED around the Mute button is lit green.

When the microphone is muted, the LED is lit red. When you press the Mute button, the phone and the expansion microphones are muted.

If the phone is paired with a wireless microphone (for example, Wireless microphone 1) and you connect the wireless microphone
                                 to a charger, pressing the Show detail softkey indicates the charge level for that microphone.

When the phone is paired with a wireless microphone and you connect a wired microphone, the wireless microphone gets unpaired
                                 and the phone is paired with the wired microphone. A notification appears on the phone screen indicating that the wired microphone
                                 is connected.

## Cisco IP Conference Phone 8832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                              URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/tsd-products-support-series-home.html

## Terminology Differences

In this document, the term Cisco IP Phone includes the Cisco IP Conference Phone 8832 Multiplatform Phones.

The following table highlights some of the terminology differences in the Cisco IP Conference in the Cisco IP Conference Phone
                              8832 Multiplatform Phone User Guide, the Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide.

User Guide

Administration Guide

Message Indicators

Message Waiting Indicator (MWI)

Voicemail System

Voice Messaging System

| Note | Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone might cause interference. For
                                          more information, see the manufacturer’s documentation of the interfering device. |
|---|---|

| 1 | Mute bar | Toggle the microphone on or off. When the microphone is muted, the LED bar is lit red. |
|---|---|---|
| 2 | LED bar | Indicates call states: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 3 | Softkey buttons | Access functions and services. |
| 4 | Navigation bar and Select button | Scroll through menus, highlight items, and select the highlighted item. When the phone is idle, press Up to access the recent calls list and press Down to access the favorites list. |
| 5 | Volume button | Adjust the speakerphone volume (off hook) and the ringer volume (on hook). When you change the volume, the LED bar lights white to show the volume change. |

| User Guide | Administration Guide |
|---|---|
| Message Indicators | Message Waiting Indicator (MWI) |
| Voicemail System | Voice Messaging System |