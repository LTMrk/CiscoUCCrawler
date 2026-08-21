---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-e472924aec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_010.html
retrieved_at: 2026-08-21T09:48:51.854589+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Cisco IP Phone Hardware

## Chapter: Cisco IP Phone Hardware

# Cisco IP Phone Hardware

## Phone
                        	 Overview

The Cisco IP Phones 8800 Series provides voice communication over an Internet Protocol (IP) network. The Cisco IP Phone functions
                           much like any digital business phone, allowing you to make phone calls and to access features such as mute, hold, transfer,
                           and more. In addition, because the phone connects to your data network, it offers enhanced IP telephony features, including
                           access to network information and services, and customizable features and services.

The Cisco IP Phone 8811 has a grayscale LCD screen. The Cisco IP Phones 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR have
                           a 24-bit color LCD screen.

When adding features to the phone line keys, you are limited by the number of line keys available. You cannot add more features
                           than the number of line keys on your phone.

The Cisco IP Phones have the following features:

Programmable feature buttons that support up to 5 lines in Session Line Mode or up to 10 lines with Enhanced Line Mode

Full video capabilities (Cisco IP Phones 8845, 8865, and 8865NR only)

Gigabit Ethernet connectivity

Bluetooth support for wireless headsets (Cisco IP Phone 8845, 8851, 8861, and 8865 only. This feature is not supported on
                                 Cisco IP Phone 8811, 8841, 8851NR, and 8865NR.)

Support for an external microphone and speakers (Cisco IP Phone 8861, 8865, and 8865NR only)

Network connectivity by Wi-Fi (Cisco IP Phone 8861 and 8865 only. Wi-Fi is not supported on Cisco IP Phone 8865NR.)

USB ports:

One USB port for Cisco IP Phone 8851 and 8851NR

Two USB ports for Cisco IP Phone 8861, 8865, and 8865NR

The Cisco IP Phone 8845, 8865, and 8865NR support video calls with a built-in video camera. Use this feature to collaborate
                           with friends and co-workers or to hold face-to-face meetings over the phone.

You should save the box and packaging for the Cisco IP Phone 8845, 8865, and 8865NR. The cameras on these phones are fragile.
                                       If you move the phone, we recommend that you pack the phone into the original box to protect the camera. For more information, see Protect Your Video Phone Camera .

A video call includes the following features:

PIP — Select from four positions: Right bottom, Right top, Left top, and Left bottom. You can also turn PIP off.

Swap — Toggles the views in the PIP view. The Swap softkey is disabled when PIP is off.

Self-view Video — Select Self-view Video to view your image as it appears on video.

Video UI and Conference/Transfer Initiation — Select to begin a conference.

For additional information on Video Calls, see Cisco IP Phone 8800 Series User Guide for Cisco Unified Communications Manager and the documentation for your particular Cisco Unified Communications Manager release.

Like other devices, a Cisco IP Phone must be configured and managed. These phones encode and decode the following codecs:

G.711 a-law

G.711 mu-law

G.722

G722.2 AMR-WB

G.729a/G.729ab

G.726

iLBC

Opus

iSAC

Caution

Using a cell,
                                       		  mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone
                                       		  might cause interference. For more information, see the manufacturer’s
                                       		  documentation of the interfering device.

Cisco IP Phones
                           		provide traditional telephony functionality, such as call forwarding and
                           		transferring, redialing, speed dialing, conference calling, and voice messaging
                           		system access. Cisco IP Phones also provide a variety of other features.

As with other
                           		network devices, you must configure Cisco IP Phones to prepare them to access
                           		Cisco Unified Communications Manager and the rest of the IP network. By using
                           		DHCP, you have fewer settings to configure on a phone. If your network requires
                           		it, however, you can manually configure information such as: an IP address,
                           		TFTP server, and subnet information.

Cisco IP Phones can
                           		interact with other services and devices on your IP network to provide enhanced
                           		functionality. For example, you can integrate Cisco Unified Communications
                           		Manager with the corporate Lightweight Directory Access Protocol 3 (LDAP3)
                           		standard directory to enable users to search for coworker contact information
                           		directly from their IP phones. You can also use XML to enable users to access
                           		information such as weather, stocks, quote of the day, and other web-based
                           		information.

Finally, because the Cisco IP Phone is a network device, you can obtain detailed status information from it directly. This
                           information can assist you with troubleshooting any problems users might encounter when using their IP phones. You can also
                           obtain statistics about an active call or firmware versions on the phone.

To function in the
                           		IP telephony network, the Cisco IP Phone must connect to a network device, such
                           		as a Cisco Catalyst switch. You must also register the Cisco IP Phone with a
                           		Cisco Unified Communications Manager system before sending and receiving calls.

## Cisco IP Phone 8811

The following section describe the Cisco IP Phone 8811 attributes.

### Phone Connections

Connect your phone to your organization's IP telephony network as shown in the following diagram.

1

DC adapter port (DC48V).

5

Access port (10/100/1000 PC) connection.

2

AC-to-DC power supply (optional).

6

Auxiliary port.

3

AC power wall plug (optional).

7

Handset connection.

4

Network port (10/100/1000 SW) connection. IEEE 802.3at power enabled.

8

Analog headset connection (optional).

In the EU and UK, your phone is shipped with a power switch cable that is required in order to provide power to your phone
                                             when using an AC-to-DC power supply. This cable only works with the power cube 4 power adapter that is shipped together (P/N
                                             341-100594-01 and above). Connect the power cord to the power switch cable and then connect the other end of the power switch
                                             cable to the DC adapter port.

The Cisco IP Phone 8811 does not support a key expansion module.

## Cisco IP Phones
                        	 8841 and 8845

The following section describe the attributes of the Cisco IP Phones 8841 and 8845.

### Phone
                           	 Connections

Connect
                                 		  your phone to the corporate IP telephony network, using the following diagram.

1

DC
                                             						adaptor port (DC48V).

5

Access
                                             						port (10/100/1000 PC) connection.

2

AC-to-DC
                                             						power supply (optional).

6

Auxiliary port.

3

AC power
                                             						wall plug (optional).

7

Handset
                                             						connection.

4

Network
                                             						port (10/100/1000 SW) connection. IEEE 802.3at power enabled.

8

Analog
                                             						headset connection (optional).

The Cisco IP Phone 8841 and 8845 does not support a key expansion module.

## Cisco IP Phones
                        	 8851 and 8851NR

The following section describe the attributes of the Cisco IP Phones 8851 and 8851NR.

The Cisco IP Phone
                                       		  8851NR does not support Bluetooth. Otherwise, the Cisco IP Phone 8851 and Cisco
                                       		  IP Phone 8851NR support the same features.

### Phone Connections

Connect
                              		your phone to the corporate IP telephony network as shown in the following
                              		diagram.

1

DC adaptor port (DC48V).

6

Auxiliary port.

2

AC-to-DC power supply (optional).

7

Handset connection.

3

AC power wall plug (optional).

8

Analog headset connection (optional).

4

Network port (10/100/1000 SW) connection. IEEE 802.3at power enabled.

9

USB port

5

Access port (10/100/1000 PC) connection.

In the EU and UK, your phone is shipped with a power switch cable that is required in order to provide power to your phone
                                          when using an AC-to-DC power supply. This cable only works with the power cube 4 power adapter that is shipped together (P/N
                                          341-100594-01 and above). Connect the power cord to the power switch cable and then connect the other end of the power switch
                                          cable to the DC adapter port.

Each USB port supports the connection of up to five supported and nonsupported devices. Each device connected to the phone
                                          is included in the maximum device count. For example, your phone can support five USB devices (such as two key expansion modules,
                                          one headset, one hub, and one other standard USB device) on the side port. Many third-party USB products count as multiple
                                          USB devices, for example, a device containing USB hub and headset can count as two USB devices. For more information, see
                                          the USB device documentation.

## Cisco IP Phones 8861, 8865, and 8865NR

The following section describe the attributes of the Cisco IP Phones 8861, 8865, and 8865NR.

### Phone
                           	 Connections

Connect
                              		your phone to the corporate IP telephony network as shown in the following
                              		diagram.

1

DC adaptor port (DC48V).

7

Handset connection.

2

AC-to-DC power supply (optional).

8

Analog headset connection (optional).

3

AC power wall plug (optional).

9

USB port

4

Network port (10/100/1000 SW) connection. IEEE 802.3at power enabled.

10

Audio In/Out ports

5

Access port (10/100/1000 PC) connection.

11

USB port

6

Auxiliary port.

Each USB port supports the connection of up to five supported and nonsupported devices. Each device connected to the phone
                                          is included in the maximum device count. For example, your phone can support five USB devices (such as three key expansion
                                          modules, one hub, and one other standard USB device) on the side port and five additional standard USB devices on the back
                                          port. Many third-party USB products count as multiple USB devices, for example, a device containing USB hub and headset can
                                          count as two USB devices. For more information, see the USB device documentation.

## Buttons and Hardware

The Cisco IP Phone 8800 Series has two distinct hardware types:

Cisco IP Phones 8811, 8841, 8851, 8851NR, and 8861—do not have a camera.

Cisco IP Phones 8845, 8865, and 8865NR—have a built-in camera.

The following figure shows the Cisco IP Phone 8845.

The following table describes the Cisco IP Phone 8800 Series Buttons.

1

Handset and Handset light strip

Indicates whether you have an incoming call (flashing red) or a new voice message (steady red).

2

Camera

Cisco IP Phone 8845, 8865, and 8865NR only

Use the camera for video calls.

3

Programmable feature buttons and line buttons

Access your phone lines, features, and call sessions.

When adding features to the phone line keys, you are limited by the number of line keys available. You cannot add more features
                                          than the number of line keys on your phone.

For more information, see the Softkey, Line, and Feature Buttons section in the "Cisco IP Phone Hardware" chapter.

4

Softkey buttons

Access to functions and services.

For more information, see the Softkey, Line, and Feature Buttons section in the "Cisco IP Phone Hardware" chapter.

5

Back , Navigation cluster, and Release

Back Return to the previous screen or menu.

Navigation cluster Navigation ring and Select button—Scroll through menus, highlight items and select the highlighted item.

Release End a connected call or session.

6

Hold/Resume , Conference , and Transfer

Hold/Resume Place an active call on hold and resume the held call.

Conference Create a conference call.

Transfer Transfer a call.

7

Speakerphone , Mute , and Headset

Speakerphone Toggle the speakerphone on or off. When the speakerphone is on, the button is lit.

Mute Toggle the microphone on or off. When the microphone is muted, the button is lit.

Headset Toggle the headset on. When the headset is on, the button islit. To leave headset mode, you pick up the handset or select Speakerphone .

8

Contacts , Applications , and Messages

Contacts Access personal and corporate directories.

Applications Access recent calls, user preferences, phone settings, and phone model information.

Messages Autodial your voice messaging system.

9

Volume button

Adjust the handset, headset, and speakerphone volume (off hook) and the ringer volume (on hook).

### Softkey, Line, and Feature Buttons

You can interact with the features on your phone in several ways:

Softkeys, located below the screen, give you access to the function displayed on the screen above the softkey. The softkeys
                                       change depending on what you are doing at the time. The More ... softkey shows you that more functions are available.

Feature and line buttons, located on either side of the screen, give you access to phone features and phone lines.

Feature buttons—Used for features such as Speed dial or Call pickup , and to view your status on another line.

Line buttons—Used to answer a call or resume a held call. When not used for an active call, used to initiate phone functions,
                                             such as the missed calls display.

Feature and line buttons illuminate to indicate status.

LED Color and State

Normal Line Mode: Line Buttons

Normal Line Mode: Feature Buttons

Enhanced Line Mode

Green, steady LED

Active call or two-way intercom call, held call, privacy in use

Active call or two-way intercom call, privacy in use

Green, flashing LED

Not applicable

Held call

Amber, steady LED

Incoming call, reverting call, one-way intercom call, logged into a Hunt Group

One-way intercom call, logged into a Hunt Group

Amber, flashing LED

Not applicable

Incoming call, reverting call

Red, steady LED

Remote line in use, Remote line on hold, Do Not Disturb active

Remote line in use, Do Not Disturb active

Red, flashing LED

Not applicable

Remote line on hold

Your administrator can set up some functions as softkeys or as feature buttons. You can also access some functions with softkeys
                                 or the associated hard button.

## Protect Your Video Phone Camera

The camera on your video phone is fragile and could break during transportation of the phone.

### Before you begin

You need one of these:

Original phone box and the packing material

Packaging material, such as foam or bubble wrap

Step 1

If you have the original box:

Place the foam on the camera in such a way that the lens is well-protected.

Place the phone in its original box.

Step 2

If you do not have the box, carefully wrap the phone with foam or bubble wrap to protect the camera. Ensure that the foam
                                       protects and surrounds the camera so that nothing can press against the camera from any direction or the camera may be damaged
                                       in transport.

| Note | You should save the box and packaging for the Cisco IP Phone 8845, 8865, and 8865NR. The cameras on these phones are fragile.
                                       If you move the phone, we recommend that you pack the phone into the original box to protect the camera. For more information, see Protect Your Video Phone Camera . |
|---|---|

| Caution | Using a cell,
                                       		  mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone
                                       		  might cause interference. For more information, see the manufacturer’s
                                       		  documentation of the interfering device. |
|---|---|

| 1 | DC adapter port (DC48V). | 5 | Access port (10/100/1000 PC) connection. |
|---|---|---|---|
| 2 | AC-to-DC power supply (optional). | 6 | Auxiliary port. |
| 3 | AC power wall plug (optional). | 7 | Handset connection. |
| 4 | Network port (10/100/1000 SW) connection. IEEE 802.3at power enabled. | 8 | Analog headset connection (optional). |

| Note | In the EU and UK, your phone is shipped with a power switch cable that is required in order to provide power to your phone
                                             when using an AC-to-DC power supply. This cable only works with the power cube 4 power adapter that is shipped together (P/N
                                             341-100594-01 and above). Connect the power cord to the power switch cable and then connect the other end of the power switch
                                             cable to the DC adapter port. |
|---|---|

| Note | The Cisco IP Phone 8811 does not support a key expansion module. |
|---|---|

| 1 | DC
                                             						adaptor port (DC48V). | 5 | Access
                                             						port (10/100/1000 PC) connection. |
|---|---|---|---|
| 2 | AC-to-DC
                                             						power supply (optional). | 6 | Auxiliary port. |
| 3 | AC power
                                             						wall plug (optional). | 7 | Handset
                                             						connection. |
| 4 | Network
                                             						port (10/100/1000 SW) connection. IEEE 802.3at power enabled. | 8 | Analog
                                             						headset connection (optional). |

| Note | The Cisco IP Phone 8841 and 8845 does not support a key expansion module. |
|---|---|

| Note | The Cisco IP Phone
                                       		  8851NR does not support Bluetooth. Otherwise, the Cisco IP Phone 8851 and Cisco
                                       		  IP Phone 8851NR support the same features. |
|---|---|

| 1 | DC adaptor port (DC48V). | 6 | Auxiliary port. |
|---|---|---|---|
| 2 | AC-to-DC power supply (optional). | 7 | Handset connection. |
| 3 | AC power wall plug (optional). | 8 | Analog headset connection (optional). |
| 4 | Network port (10/100/1000 SW) connection. IEEE 802.3at power enabled. | 9 | USB port |
| 5 | Access port (10/100/1000 PC) connection. |  |  |

| Note | In the EU and UK, your phone is shipped with a power switch cable that is required in order to provide power to your phone
                                          when using an AC-to-DC power supply. This cable only works with the power cube 4 power adapter that is shipped together (P/N
                                          341-100594-01 and above). Connect the power cord to the power switch cable and then connect the other end of the power switch
                                          cable to the DC adapter port. |
|---|---|

| Note | Each USB port supports the connection of up to five supported and nonsupported devices. Each device connected to the phone
                                          is included in the maximum device count. For example, your phone can support five USB devices (such as two key expansion modules,
                                          one headset, one hub, and one other standard USB device) on the side port. Many third-party USB products count as multiple
                                          USB devices, for example, a device containing USB hub and headset can count as two USB devices. For more information, see
                                          the USB device documentation. |
|---|---|

| 1 | DC adaptor port (DC48V). | 7 | Handset connection. |
|---|---|---|---|
| 2 | AC-to-DC power supply (optional). | 8 | Analog headset connection (optional). |
| 3 | AC power wall plug (optional). | 9 | USB port |
| 4 | Network port (10/100/1000 SW) connection. IEEE 802.3at power enabled. | 10 | Audio In/Out ports |
| 5 | Access port (10/100/1000 PC) connection. | 11 | USB port |
| 6 | Auxiliary port. |  |  |

| Note | Each USB port supports the connection of up to five supported and nonsupported devices. Each device connected to the phone
                                          is included in the maximum device count. For example, your phone can support five USB devices (such as three key expansion
                                          modules, one hub, and one other standard USB device) on the side port and five additional standard USB devices on the back
                                          port. Many third-party USB products count as multiple USB devices, for example, a device containing USB hub and headset can
                                          count as two USB devices. For more information, see the USB device documentation. |
|---|---|

| 1 | Handset and Handset light strip | Indicates whether you have an incoming call (flashing red) or a new voice message (steady red). |
|---|---|---|
| 2 | Camera Cisco IP Phone 8845, 8865, and 8865NR only | Use the camera for video calls. |
| 3 | Programmable feature buttons and line buttons | Access your phone lines, features, and call sessions. When adding features to the phone line keys, you are limited by the number of line keys available. You cannot add more features
                                          than the number of line keys on your phone. For more information, see the Softkey, Line, and Feature Buttons section in the "Cisco IP Phone Hardware" chapter. |
| 4 | Softkey buttons | Access to functions and services. For more information, see the Softkey, Line, and Feature Buttons section in the "Cisco IP Phone Hardware" chapter. |
| 5 | Back , Navigation cluster, and Release | Back Return to the previous screen or menu. Navigation cluster Navigation ring and Select button—Scroll through menus, highlight items and select the highlighted item. Release End a connected call or session. |
| 6 | Hold/Resume , Conference , and Transfer | Hold/Resume Place an active call on hold and resume the held call. Conference Create a conference call. Transfer Transfer a call. |
| 7 | Speakerphone , Mute , and Headset | Speakerphone Toggle the speakerphone on or off. When the speakerphone is on, the button is lit. Mute Toggle the microphone on or off. When the microphone is muted, the button is lit. Headset Toggle the headset on. When the headset is on, the button islit. To leave headset mode, you pick up the handset or select Speakerphone . |
| 8 | Contacts , Applications , and Messages | Contacts Access personal and corporate directories. Applications Access recent calls, user preferences, phone settings, and phone model information. Messages Autodial your voice messaging system. |
| 9 | Volume button | Adjust the handset, headset, and speakerphone volume (off hook) and the ringer volume (on hook). |

| LED Color and State | Normal Line Mode: Line Buttons | Normal Line Mode: Feature Buttons Enhanced Line Mode |
|---|---|---|
| Green, steady LED | Active call or two-way intercom call, held call, privacy in use | Active call or two-way intercom call, privacy in use |
| Green, flashing LED | Not applicable | Held call |
| Amber, steady LED | Incoming call, reverting call, one-way intercom call, logged into a Hunt Group | One-way intercom call, logged into a Hunt Group |
| Amber, flashing LED | Not applicable | Incoming call, reverting call |
| Red, steady LED | Remote line in use, Remote line on hold, Do Not Disturb active | Remote line in use, Do Not Disturb active |
| Red, flashing LED | Not applicable | Remote line on hold |

| Step 1 | If you have the original box: Place the foam on the camera in such a way that the lens is well-protected. Place the phone in its original box. |
|---|---|
| Step 2 | If you do not have the box, carefully wrap the phone with foam or bubble wrap to protect the camera. Ensure that the foam
                                       protects and surrounds the camera so that nothing can press against the camera from any direction or the camera may be damaged
                                       in transport. |