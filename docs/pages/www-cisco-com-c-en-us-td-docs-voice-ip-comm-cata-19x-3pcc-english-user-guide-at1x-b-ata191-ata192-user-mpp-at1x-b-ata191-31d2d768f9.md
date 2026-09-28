---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-user-guide-at1x-b-ata191-ata192-user-mpp-at1x-b-ata191-31d2d768f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/user-guide/at1x_b_ata191-ata192-user-mpp/at1x_b_ata191-ata192-user-mpp_chapter_00.html
retrieved_at: 2026-08-21T12:49:30.671838+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

Updated: April 10, 2025

Chapter: Your ATA

## Chapter: Your ATA

# Your ATA

## Your new ATA

Your analog telephone adapter (ATA) allows you to connect an analog device, such as an analog phone or fax machine, to your
                           network. The connected device can then function like the IP phones in your network.

Your new analog telephone adapter (ATA) has two interfaces:

Two RJ11 ports for analog devices

A RJ45 port for Ethernet

Light-emitting diodes (LEDs) on the ATA provide status.

Install your ATA with the components that are included in the box.

Install your ATA with the components in the box.

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

## Cisco ATA 191 and ATA 192 Hardware

The ATA 191 and ATA 192 are compact, easy to install devices.

The unit provides these connectors:

5V DC power connector.

Two RJ-11 FXS (Foreign Exchange Station) ports—Your ATA has two RJ-11 ports that work with any standard analog phone device.
                                    Each port supports either voice calls or fax sessions, and both ports can be used simultaneously.

One WAN network port—An RJ-45 10/100BASE-T data port to connect an Ethernet-capable device to the network.

The ATA 192 includes an extra LAN Ethernet port—An RJ-45 10/100BASE-T data port to connect to a device on your network, such
                                    as a computer, using an Ethernet cable.

The ATA network port performs autonegotiation for duplex and speed. It supports speeds of 10/100Mbps and full-duplex.

### ATA 191 and ATA 192 Top Panel

The following figure shows the different LEDs and buttons found on the top of your ATA.

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

This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator.

Problem Report Tool (PRT) LED

Flashing amber: The PRT is preparing the data for the problem report.

Fast Flashing amber: The PRT is sending the problem report log to the HTTP server.

Solid amber: The activation of the FIPS mode failed. Press the PRT button to turn off the PRT LED.

Solid green for five seconds, then off: The PRT report was sent successfully.

Fast flashing green: A factory reset is performed successfully.

Flashing red: The PRT report failed. Press the PRT button once to cancel the flashing, then press again to trigger a new PRT.

#### Problem Report Tool Button

The Problem Report Tool (PRT) button is on the ATA top panel. Press the PRT button, and a log file is prepared and uploaded
                                 to the server for troubleshooting your network.

You can instruct your analog phone users to press the PRT button on the ATA device to start the PRT log file process.

Set up the HTTP server to upload the PRT log file from the ATA.

Configure the customer support upload URL to best suit your needs, and apply it to the ATA.

### ATA 191 and ATA 192 Back Panel

The following figures shows the different ports and buttons found on the back of your ATA.

Item

Description

RESET

To restart the ATA, use a paper clip or similar object to press this button briefly.

To restore the factory default settings, press and hold for about 10 seconds.

The LED behaviour for the factory reset:

After you press and hold the button for about 10 seconds, the Power LED is fast flashing green.

After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds.

PHONE 1

Use an RJ-11 phone cable to connect an analog phone or fax machine.

PHONE 2

Use an RJ-11 phone cable to connect a second analog phone or fax machine.

ETHERNET (ATA 192 only)

Use an Ethernet cable to connect your ATA to a device on your network, such as a computer.

NETWORK

Use an Ethernet cable to connect to the network.

DC 5V POWER

Use the power adapter that was provided to connect to a power source.

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

## Phone Adapter Configuration Utility

You can configure or customize some phone features with the Phone Adapter Configuration Utility webpage. Your administrator
                              gives you the page URL, your user ID, and password.

In the Configuration Utility page, you can view some network and administration settings, as well as some basic information
                              about your ATA, such as firmware version, serial number, and memory use.

Most people use the Phone Adapter Configuration Utility page to set up a few basic features such as Speed dial or Call forward.
                              To set up these features, refer to the following table.

The following table describes the phone features that you configure from the Phone Adapter Configuration Utility webpage.

Feature

Description

Call forward and Selective call forward.

You specify the number that will receive calls when call forward is enabled on the phone. Use the Configuration Utility page
                                          to set up more complicated call forward functions, for example, when your line is busy.

For more information, see Call Forward Settings or Selective Call Forward Settings and Set Up Phone Features with Phone Adapter Configuration Utility .

Speed dial.

You assign phone numbers to a line so that you can quickly call that person.

For more information, see Speed Dial Settings and Set Up Phone Features with Phone Adapter Configuration Utility

Supplementary services.

Configure such features as Call waiting, Do not disturb, or Called ID.

For more information, see Supplementary Service Settings and Set Up Phone Features with Phone Adapter Configuration Utility

Distinctive ring

You can assign a specific ring to a phone number or line.

For more information, see Distinctive Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility .

Ring setting

You can assign a specific ring to a certain situation such as when a call is on hold or during a call back.

For more information, see Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility .

### View MIC Cert Refresh Status

#### Before you begin

Your administrator has given you the access to the Phone Adapter Configuration Utility.

Your administrator activates the Manufacture Installed Certificate (MIC) renewal on your ATA.

Step 1

Sign into Phone Adapter Configuration Utility as an user.

Step 2

Select Voice > Information .

Step 3

Navigate to the section MIC Cert Refresh Status , and check the information.

MIC Cert Provisioning Status : This field indicates that whether the certificate download is successful. If yes, the string is Download Successful . If no, this field shows the error message for your administrator's troubleshooting. By default, the field is empty.

MIC CA Info : This field indicates that whether the MIC certificate is renewed successfully. If yes, the string is Cisco Manufacturing CA III . If no, this filed shows Cisco Manufacturing CA or Cisco Manufacturing CA II . By default, the field is empty.

For more information about the MIC certificate renewal via a SUDI service, contact your administrator.

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
| Problem Report Tool (PRT) Button | Press this button to create a problem report using the Problem Report Tool. Note This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. | Note | This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. |
| Note | This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. |
| Problem Report Tool (PRT) LED | Flashing amber: The PRT is preparing the data for the problem report. Fast Flashing amber: The PRT is sending the problem report log to the HTTP server. Solid amber: The activation of the FIPS mode failed. Press the PRT button to turn off the PRT LED. Solid green for five seconds, then off: The PRT report was sent successfully. Fast flashing green: A factory reset is performed successfully. Flashing red: The PRT report failed. Press the PRT button once to cancel the flashing, then press again to trigger a new PRT. |

| Note | This button is not a power button. When you press this button, a problem report is generated and uploaded to a server for
                                                         the system administrator. |
|---|---|

| Item | Description |
|---|---|
| RESET | To restart the ATA, use a paper clip or similar object to press this button briefly. To restore the factory default settings, press and hold for about 10 seconds. The LED behaviour for the factory reset: After you press and hold the button for about 10 seconds, the Power LED is fast flashing green. After the factory reset is performed successfully, all LEDs are fast flashing green for about 5 seconds. |
| PHONE 1 | Use an RJ-11 phone cable to connect an analog phone or fax machine. |
| PHONE 2 | Use an RJ-11 phone cable to connect a second analog phone or fax machine. |
| ETHERNET (ATA 192 only) | Use an Ethernet cable to connect your ATA to a device on your network, such as a computer. |
| NETWORK | Use an Ethernet cable to connect to the network. |
| DC 5V POWER | Use the power adapter that was provided to connect to a power source. |

| Step 1 | Connect the network cable to your network and to the NETWORK port on the ATA. |
|---|---|
| Step 2 | Connect the phone cable to the PHONE 1 port on the ATA and to your analog device (phone or fax machine). If connecting a fax machine, connect it directly to the ATA. Do not connect an extension to a fax machine, and do not use
                                          a splitter. |
| Step 3 | (Optional) If you have a second analog device, connect the phone cable to the PHONE 2 port on the ATA and to your second analog device. |
| Step 4 | Connect the ATA power cable to the DC 5V POWER port on the ATA, and plug the power cable into your power source. |

| Feature | Description |
|---|---|
| Call forward and Selective call forward. | You specify the number that will receive calls when call forward is enabled on the phone. Use the Configuration Utility page
                                          to set up more complicated call forward functions, for example, when your line is busy. For more information, see Call Forward Settings or Selective Call Forward Settings and Set Up Phone Features with Phone Adapter Configuration Utility . |
| Speed dial. | You assign phone numbers to a line so that you can quickly call that person. For more information, see Speed Dial Settings and Set Up Phone Features with Phone Adapter Configuration Utility |
| Supplementary services. | Configure such features as Call waiting, Do not disturb, or Called ID. For more information, see Supplementary Service Settings and Set Up Phone Features with Phone Adapter Configuration Utility |
| Distinctive ring | You can assign a specific ring to a phone number or line. For more information, see Distinctive Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility . |
| Ring setting | You can assign a specific ring to a certain situation such as when a call is on hold or during a call back. For more information, see Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility . |

| Step 1 | Sign into Phone Adapter Configuration Utility as an user. |
|---|---|
| Step 2 | Select Voice > Information . |
| Step 3 | Navigate to the section MIC Cert Refresh Status , and check the information. MIC Cert Provisioning Status : This field indicates that whether the certificate download is successful. If yes, the string is Download Successful . If no, this field shows the error message for your administrator's troubleshooting. By default, the field is empty. MIC CA Info : This field indicates that whether the MIC certificate is renewed successfully. If yes, the string is Cisco Manufacturing CA III . If no, this filed shows Cisco Manufacturing CA or Cisco Manufacturing CA II . By default, the field is empty. For more information about the MIC certificate renewal via a SUDI service, contact your administrator. |