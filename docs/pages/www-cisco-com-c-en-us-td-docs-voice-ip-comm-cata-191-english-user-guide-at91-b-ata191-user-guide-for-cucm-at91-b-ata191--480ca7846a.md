---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-user-guide-at91-b-ata191-user-guide-for-cucm-at91-b-ata191--480ca7846a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/user-guide/at91_b_ata191-user-guide-for-cucm/at91_b_ata191-user-guide-for-cucm_chapter_00.html
retrieved_at: 2026-08-21T12:49:21.744250+00:00
---

Cisco ATA 191 Analog Telephone Adapter User Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter User Guide for Cisco Unified Communications Manager

Updated: February 23, 2024

Chapter: Get Started with Your New ATA

## Chapter: Get Started with Your New ATA

# Get Started with Your New ATA

## Your new ATA

Your analog telephone adapter (ATA) allows you to connect an analog device, such as an analog phone or fax machine, to your
                           network. The connected device can then function like the IP phones in your network.

Your new analog telephone adapter (ATA) has two interfaces:

Two RJ11 ports for analog devices

A RJ45 port for Ethernet

Light-emitting diodes (LEDs) on the ATA provide status.

Install your ATA with the components that are included in the box.

Install your ATA with the components in the box.

### Cisco ATA 191  Hardware

The ATA 191 and ATA 192 are compact, easy to install devices.

The unit provides these connectors:

5V DC power connector.

Two RJ-11 FXS (Foreign Exchange Station) ports—Your ATA has two RJ-11 ports that work with any standard analog phone device.
                                       Each port supports either voice calls or fax sessions, and both ports can be used simultaneously.

One WAN network port—An RJ-45 10/100BASE-T data port to connect an Ethernet-capable device to the network.

The ATA network port performs autonegotiation for duplex and speed. It supports speeds of 10/100Mbps and full-duplex.

#### ATA 191 Top Panel

The top panel of your ATA has several LEDs that are used to show the device's status.

The following table describes the LEDs located on your ATA.

Item

Description

Power LED

Steady green: System booted up successfully and is ready for use.

Slow flashing green: System is booting up.

Fast flashing green three times, then repeats: System failed to boot up.

Fast flashing green: The LED behaviour occurs in the following situations:

System detects a factory reset.

A factory reset is performed successfully.

Off: Power is off.

Network LED

Flashing green: Data transmission or reception is in progress through the WAN port.

Off: No link.

Phone 1 LED

Phone 2 LED

Steady green: On hook.

Slow flashing green: Off hook.

Fast flashing green three times, then repeats: The analog device failed to register.

Fast flashing green: A factory reset is performed successfully.

Off: The port is not configured.

Problem Report Tool (PRT) Button

Press this button to create a problem report using the Problem Report Tool.

This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator.

Problem Report Tool (PRT) LED

Flashing amber: The PRT is preparing the data for the problem report.

Fast Flashing amber: The PRT is sending the problem report log to the PRT server.

Solid green for five seconds, then off: The PRT report was sent successfully.

Fast flashing green: A factory reset is performed successfully.

Flashing red: The PRT report failed. Press the PRT button to turn the LED off. Once it is off, another press triggers a new PRT report.

#### ATA 191 Back Panel

The back panel of your ATA has several ports used to connect your device and to power it. The back panel also has the reset
                                    button for resetting the device to the factory settings.

The following table describes the ports that are located on the back panel of your ATA.

Port or Button

Description

RESET

To restart the ATA, use a paper clip or similar object to press this button briefly.

To restore the factory default settings, press and hold for 10 seconds.

The LED behaviour for the factory reset:

After you press and hold the button for about 10 seconds, the Power LED is fast flashing green.

After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds.

PHONE 1

Use an RJ-11 phone cable to connect an analog phone or fax machine.

PHONE 2

Use an RJ-11 phone cable to connect a second analog phone or fax machine.

NETWORK

Use an Ethernet cable to connect to the network.

DC 5V POWER

Use the provided power adapter to connect to a power source.

## Devices associated with your ATA

Analog phones

Analog phones have no softkeys.

The information that analog phones display depends on the model you have.

You use the phone’s flash button for hold, resume, transfer, and conference.

Analog telephony voice devices

The ATA supports analog telephony voice devices, such as overhead paging adapters and answering machines, that emulate a regular
                                             phone.

Overhead paging systems

Overhead paging systems provide alarms and public-address announcements in buildings.

Fax machines

Use a fax machine directly with an ATA. Don’t connect an extension to a fax machine, and don’t use the fax machine with a
                                             splitter.

To reduce fax failures, use overseas mode, if available; if not, set the fax machine transmission speed to low.

Data devices, such as facsimile machines and modems, may not function optimally. For the best fax and modem performance, continue
                                             to use a dedicated PSTN line.

## Install your new ATA

### Before you begin

Before you begin the installation, make sure you have the following equipment:

Ethernet cable to connect to your network.

Analog phone or fax machine to connect to your ATA.

Phone cable to connect your phone.

Uninterruptible power supply (UPS) to provide backup power.

Step 1

Connect the network cable to your network and to the NETWORK port on the ATA.

Step 2

Connect the phone cable to the PHONE 1 port on the ATA and to your analog device (phone or fax machine).

If connecting a fax machine, connect it directly to the ATA. Do not connect an extension to a fax machine, and do not use
                                          a splitter.

Step 3

(Optional) If you have a second analog device, connect the phone cable to the PHONE 2 port on the ATA and to your second analog device.

Step 4

Connect the ATA power cable to the DC 5V POWER port on the ATA, and plug the power cable into your power source.

## Mount Your ATA

You can place the ATA on a desktop or mount it on a wall.

Caution

To prevent the ATA from overheating, do not operate it in an area that exceeds an ambient temperature of 104°F (40°C).

### Desktop Placement

Place the ATA on a flat surface near an electrical outlet.

Warning

Do not place anything on top of the ATA; excessive weight could damage it.

### Wall Mounting

The ATA has two wall-mounted slots on the bottom panel. To mount the ATA on a wall, you need mounting hardware (not included).
                                 Suggested hardware is illustrated (not true to scale).

Recommended hardware (not included): Two #6 pan head, 5/8 in., self-tapping screws with anchors for sheet rock installation.

Insecure mounting might damage the ATA or cause injury. Cisco is not responsible for damages incurred byinsecure wall-mounting.

Step 1

Determine where you want to mount the unit.  Verify that the surface is smooth, flat and dry.

Step 2

Drill two pilot holes into the surface 58 mm apart (about 2.28 in.).

Step 3

Insert a screw into each hole, leaving a gap of 5 mm (0.1968 in.) between the underside of each screw head and the surface
                                          of the wall.

Step 4

Place the unit wall-mount slots over the screws and slide the unit down until the screws fit snugly into the wall-mount slots.

## Supported ATA call features

Depending on your system configuration, your ATA supports some or all the following call features:

Transfer (attended or supervised)—In this type of transfer, you talk to the receiving party before you complete the transfer.

Transfer (unattended or unsupervised)—In this type of transfer, you complete the transfer and hang up before the receiving
                                    party answers.

Conference.

Hold and Resume.

Caller ID.

Call Waiting.

Call Pickup.

Speed Dial.

Music On Hold.

Shared Lines.

Voicemail—This feature has no visual indicator, but a message waiting tone when you go off-hook indicates that you have voice
                                    messages. Some analog phones with a large LCD screen may display a voicemail icon.

Call Forward.

Redial.

| Note | The ATA network port performs autonegotiation for duplex and speed. It supports speeds of 10/100Mbps and full-duplex. |
|---|---|

| Item | Description |
|---|---|
| Power LED | Steady green: System booted up successfully and is ready for use. Slow flashing green: System is booting up. Fast flashing green three times, then repeats: System failed to boot up. Fast flashing green: The LED behaviour occurs in the following situations: System detects a factory reset. To perform a factory reset, press and hold the RESET button for about 10 seconds. A factory reset is performed successfully. Off: Power is off. |
| Network LED | Flashing green: Data transmission or reception is in progress through the WAN port. Off: No link. |
| Phone 1 LED Phone 2 LED | Steady green: On hook. Slow flashing green: Off hook. Fast flashing green three times, then repeats: The analog device failed to register. Fast flashing green: A factory reset is performed successfully. Off: The port is not configured. |
| Problem Report Tool (PRT) Button | Press this button to create a problem report using the Problem Report Tool. Note This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. | Note | This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. |
| Note | This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. |
| Problem Report Tool (PRT) LED | Flashing amber: The PRT is preparing the data for the problem report. Fast Flashing amber: The PRT is sending the problem report log to the PRT server. Solid green for five seconds, then off: The PRT report was sent successfully. Fast flashing green: A factory reset is performed successfully. Flashing red: The PRT report failed. Press the PRT button to turn the LED off. Once it is off, another press triggers a new PRT report. |

| Note | This is not a power button. When you press this button, a problem report is generated and uploaded to a server for the system
                                                            administrator. |
|---|---|

| Port or Button | Description |
|---|---|
| RESET | To restart the ATA, use a paper clip or similar object to press this button briefly. To restore the factory default settings, press and hold for 10 seconds. The LED behaviour for the factory reset: After you press and hold the button for about 10 seconds, the Power LED is fast flashing green. After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds. |
| PHONE 1 | Use an RJ-11 phone cable to connect an analog phone or fax machine. |
| PHONE 2 | Use an RJ-11 phone cable to connect a second analog phone or fax machine. |
| NETWORK | Use an Ethernet cable to connect to the network. |
| DC 5V POWER | Use the provided power adapter to connect to a power source. |

| Step 1 | Connect the network cable to your network and to the NETWORK port on the ATA. |
|---|---|
| Step 2 | Connect the phone cable to the PHONE 1 port on the ATA and to your analog device (phone or fax machine). If connecting a fax machine, connect it directly to the ATA. Do not connect an extension to a fax machine, and do not use
                                          a splitter. |
| Step 3 | (Optional) If you have a second analog device, connect the phone cable to the PHONE 2 port on the ATA and to your second analog device. |
| Step 4 | Connect the ATA power cable to the DC 5V POWER port on the ATA, and plug the power cable into your power source. |

| Caution | To prevent the ATA from overheating, do not operate it in an area that exceeds an ambient temperature of 104°F (40°C). |
|---|---|

| Warning | Do not place anything on top of the ATA; excessive weight could damage it. |
|---|---|

| Note | Insecure mounting might damage the ATA or cause injury. Cisco is not responsible for damages incurred byinsecure wall-mounting. |
|---|---|

| Step 1 | Determine where you want to mount the unit.  Verify that the surface is smooth, flat and dry. |
|---|---|
| Step 2 | Drill two pilot holes into the surface 58 mm apart (about 2.28 in.). |
| Step 3 | Insert a screw into each hole, leaving a gap of 5 mm (0.1968 in.) between the underside of each screw head and the surface
                                          of the wall. |
| Step 4 | Place the unit wall-mount slots over the screws and slide the unit down until the screws fit snugly into the wall-mount slots. |