---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-0-english-install-guide-hard-ins-vg248hwi-html-d06f81cb16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_0/english/install/guide/hard_ins/vg248hwi.html
retrieved_at: 2026-08-22T01:16:41.645231+00:00
---

Hardware Installation Guide (Version 1.0)

# Hardware Installation Guide (Version 1.0)

Updated: March 17, 2015

Chapter: Installing the VG248

## Chapter: Installing the VG248

## Installing the VG248

You must install the VG248 into your network, connecting it to both the IP network and the analog devices.

Before installing the VG248, review the important site and safety information in "Preparing to Install the VG248."

These sections provide instructions for safely installing the VG248:

• Installing the VG248

• Connecting the VG248 to the Network

• Verifying Installation

## Installing the VG248

You have the option of installing the VG248 in a 19-inch rack or setting it on a shelf or other flat surface. Refer to these sections for detailed instructions:

• Installing the VG248 in a Rack

• Setting the VG248 on a Shelf or Table

### Installing the VG248 in a Rack

The VG248 includes the brackets and screws required to install it in a 19-inch rack. Follow these instructions to install it safely and securely.

Warning To prevent bodily injury when mounting or servicing this unit in a rack, you must take special precautions to ensure that the system remains stable. The following guidelines are provided to ensure your safety:

• This unit should be mounted at the bottom of the rack if it is the only unit in the rack.

• When mounting this unit in a partially filled rack, load the rack from the bottom to the top with the heaviest component at the bottom of the rack.

• If the rack is provided with stabilizing devices, install the stabilizers before mounting or servicing the unit in the rack.

### Attaching the Brackets

The chassis comes with brackets for use with a 19-inch rack. To install the chassis in a rack, attach the brackets in one of the following ways:

• With the front panel forward (see Figure 3-1 )

• With the rear panel forward (see Figure 3-2 )

These figures ( Figure 3-1 and Figure 3-2 ) show how to connect the bracket to one side of the chassis. The second bracket connects to the opposite side of the chassis.

Figure 3-1 Bracket Installation—Front Panel Forward

Figure 3-2 Bracket Installation—Rear Panel Forward

### Putting the VG248 in a Rack

After the brackets are secured to the chassis, you can rack-mount it ( Figure 3-3 ).

Figure 3-3 Mounting the VG248 in a Rack

Step 1 Lift the VG248 and align the mounting holes in the L brackets with the mounting holes in the rack.

Step 2 Secure the chassis by inserting the mounting screws through the holes in the L brackets and into the threaded holes in the mounting posts.

### Setting the VG248 on a Shelf or Table

Before setting the VG248 on a desktop, shelf, or other flat, secure surface, adhere the rubber feet included with the VG248. To attach them to the chassis, peel the rubber feet from the adhesive strip and place them adhesive-side down onto the round, recessed areas on the bottom of the chassis. Place the VG248 right-side up on a flat, smooth, secure surface.

## Connecting the VG248 to the Network

You must connect the VG248 to the other IP telephony systems in the network, such as Cisco CallManager.

Review these sections before connecting the VG248:

• Connecting to the Ethernet Port

• Connecting to the Console Port

• Connecting to the FXS Telco Connectors

• Connecting Power

### Connecting to the Ethernet Port

Use the Ethernet port to connect the VG248 to the IP network to access Cisco CallManager (see Figure 3-4 ). The VG248 supports half- or full-duplex Ethernet operation.

Warning To avoid electric shock, do not connect safety extra-low voltage (SELV) circuits to telephone-network voltage (TNV) circuits. LAN ports contain SELV circuits, and WAN ports contain TNV circuits. Some LAN and WAN ports both use RJ-45 connectors. Use caution when connecting cables.

Figure 3-4 Connecting to the Ethernet Port

Ethernet cable

Ethernet port

### Connecting to the Console Port

Use the console port to connect the VG248 to a console terminal for configuration and management tasks (see Figure 3-5 ).

To connect the VG248 to a terminal, perform these steps:

Step 1 Connect the terminal using an RJ-45-to-RJ-45 rollover cable and an RJ-45-to-DB-9 adapter, included with the VG248.

Step 2 Configure your terminal or PC terminal emulation software for the following settings:

Baud

9600

Data bits

8

Parity

No

Stop bits

1

Figure 3-5 Connecting the VG248 to a Console Terminal

Console port (RJ-45)

RJ-45 to RJ-45 rollover cable

RJ-45 to DB-9 or RJ-45 to DB-25 adapter

Laptop computer or terminal

### Connecting to the FXS Telco Connectors

Use one of the two 24-port FXS telco connectors to connect the VG248 to the analog devices (see Figure 3-6 ).

Figure 3-6 Connecting to the Telco Connectors on the VG248

FXS telco connectors

### Connecting Power

Provide power to the VG248 by plugging the power cord (included) into the AC power adapter on the rear panel (see Figure 3-7 ).

Figure 3-7 Connecting Power

Power Cord

## Verifying Installation

After you complete installation of the VG248 and have connected power to it, connect a console terminal to observe its initial startup procedure. You can only observe these initial startup messages when connected to the console port. Initially, the device uses DHCP by default, but you can reconfigure this after startup.

The startup process proceeds as follows:

1. Loads boot loader software image and starts up the VG248.

2. Performs self tests on the hardware, indicating whether the component passed; for example:

Testing RAM......passed Testing FLASH....passed Testing EEPROM...passed Testing Ethernet..passed

3. Pauses for 10 seconds, allowing you to perform the following tasks:

• Initiate an FTP session to upgrade main software image before it loads, allowing recovery from a previous failed upgrade.

• Press Esc on the console terminal to access the boot loader menu.

4. Loads the main software image and displays the main menu (see Figure 3-8 ):

Figure 3-8 VG248 Main Menu

If the main software menu displays successfully, you can begin configuring the device as described in the Cisco VG248 Software Configuration Guide .

If the menu does not display properly, verify your connections and follow suggestions in the Cisco VG248 Software Configuration Guide

| 1 | Ethernet cable | 2 | Ethernet port |
|---|---|---|---|

| Setting | Value |
|---|---|
| Baud | 9600 |
| Data bits | 8 |
| Parity | No |
| Stop bits | 1 |

| 1 | Console port (RJ-45) | 2 | RJ-45 to RJ-45 rollover cable |
|---|---|---|---|
| 3 | RJ-45 to DB-9 or RJ-45 to DB-25 adapter | 4 | Laptop computer or terminal |

| 1 | FXS telco connectors |
|---|---|

| 1 | Power Cord |
|---|---|