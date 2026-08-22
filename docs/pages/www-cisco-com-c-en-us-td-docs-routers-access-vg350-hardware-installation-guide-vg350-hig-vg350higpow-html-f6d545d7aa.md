---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg350-hardware-installation-guide-vg350-hig-vg350higpow-html-f6d545d7aa
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg350/hardware/installation/guide/vg350_hig/vg350higpow.html
retrieved_at: 2026-08-22T01:14:40.132721+00:00
---

Cisco VG350 Voice Gateway Hardware Installation Guide

# Cisco VG350 Voice Gateway Hardware Installation Guide

Updated: March 27, 2014

Chapter: Powering On the Cisco VG350 Voice Gateway

## Chapter: Powering On the Cisco VG350 Voice Gateway

- Checklist for Power-On

- Power-On Procedure

- Troubleshooting

To power on your Cisco VG350 Voice Gateway, perform the following tasks in the order listed, as required:

## Checklist for Power-On

You can power on a Cisco VG350 Voice Gateway if it meets the requirements described in Chapter 4, “Installing the Cisco VG350 Voice Gateway” :

- The chassis is securely mounted.

- Power cable is connected.

- Interface cables are connected.

## Power-On Procedure

Perform this procedure to power on your Cisco VG350 Voice Gateway, and verify that it goes through its initialization and self-test. When this is finished, the Cisco VG350 Voice Gateway is ready to configure.

Warning	This unit might have more than one power supply connection. All connections must be removed to de-energize the unit. Statement 1028

Warning	Installation of the equipment must comply with local and national electrical codes. Statement 1074

To power on the Cisco VG350 Voice Gateway, perform the following:

Step 1 Power on your terminal or PC, and configure it for 9600 bps, 8 data bits, 1 stop bit, and no parity.

Step 2 Move the Cisco VG350 Voice Gateway power switch to the ON position.

The green LED next to the auxiliary port should come on and the fan should operate. If this does not happen, see the “Troubleshooting” section .

The following message is displayed at the end of the boot-up messages:

--- System Configuration Dialog ---

Would you like to enter the initial configuration dialog? [yes/no]:

Step 3 Enter no to proceed with manual configuration using the CLI:

Would you like to enter the initial configuration dialog? [yes/no]: no

Would you like to terminate autoinstall? [yes]

Step 4 Press Return to terminate autoinstall and continue with manual configuration.

Several messages are displayed, ending with a line similar to the following:

...

Copyright (c) 1986-2003 by cisco Systems, Inc.

Compiled < date > < time > by < person >

Step 5 Press Return to bring up the Router> prompt:

...

flashfs[4]: Initialization complete.

Router>

Step 6 Enter privileged EXEC mode:

Router> enable

Router#

Step 7 Continue with the “Troubleshooting” section .

Note If the rommon 1> prompt appears, your system has booted in ROM monitor mode. For information on the ROM monitor, refer to the router rebooting and ROM monitor information in the Cisco IOS Configuration Fundamentals Configuration Guide for your Cisco IOS software release.

## Troubleshooting

This section describes possible mechanical problems and corrective actions.

Warning	Only trained and qualified personnel should be allowed to install, replace, or service this equipment. Statement 1030

Warning	No user-serviceable parts inside. Do not open. Statement 1073

If there appears to be a malfunction, first check all cables and connections. If these are in order, see Table 5-1 for specific troubles and solutions.

For problems with the configuration, refer to Cisco VG350 Voice Gateway Software Configuration Guide.

Table 5-1 Troubleshooting the Cisco VG350 Voice Gateway

Symptom

Possible Cause

Corrective Action

Power LED and fan are off

Power source switched off

Switch power source on

Faulty power cable

Check/replace power cable

Faulty power source

Check/correct input power

Faulty internal power supply

Contact Cisco 1 or your Cisco reseller

Power LED on; fan off

Faulty Cisco VG350

Contact Cisco 1 Technical Service Center or your Cisco reseller

Power LED off; fan on

Faulty Cisco VG350

Contact Cisco 1 or your Cisco reseller

No initialization response from Cisco VG350

Faulty modem console terminal

Check/replace modem/terminal

Faulty cabling to terminal

Check/replace cable

Faulty Cisco VG350

Contact Cisco 1 or your Cisco reseller

Unit shuts off after operating for some time

Overheating

Check ventilation

Faulty Cisco VG350

Contact Cisco 1 or your Cisco reseller

Console screen display freezes

Console fault

Reset/replace console

Software error

Repeat power-on procedure

Faulty Cisco VG350

Contact Cisco 1 or your Cisco reseller

1. See the “$paratext>” section .

| Symptom | Possible Cause | Corrective Action |
|---|---|---|
| Power LED and fan are off | Power source switched off | Switch power source on |
| Faulty power cable | Check/replace power cable |
| Faulty power source | Check/correct input power |
| Faulty internal power supply | Contact Cisco 1 or your Cisco reseller |
| Power LED on; fan off | Faulty Cisco VG350 | Contact Cisco 1 Technical Service Center or your Cisco reseller |
| Power LED off; fan on | Faulty Cisco VG350 | Contact Cisco 1 or your Cisco reseller |
| No initialization response from Cisco VG350 | Faulty modem console terminal | Check/replace modem/terminal |
| Faulty cabling to terminal | Check/replace cable |
| Faulty Cisco VG350 | Contact Cisco 1 or your Cisco reseller |
| Unit shuts off after operating for some time | Overheating | Check ventilation |
| Faulty Cisco VG350 | Contact Cisco 1 or your Cisco reseller |
| Console screen display freezes | Console fault | Reset/replace console |
| Software error | Repeat power-on procedure |
| Faulty Cisco VG350 | Contact Cisco 1 or your Cisco reseller |

| 1. See the “$paratext>” section . |
|---|