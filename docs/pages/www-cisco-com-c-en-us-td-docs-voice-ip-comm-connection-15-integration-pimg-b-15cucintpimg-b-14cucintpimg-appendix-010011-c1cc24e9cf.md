---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-pimg-b-15cucintpimg-b-14cucintpimg-appendix-010011-c1cc24e9cf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/pimg/b_15cucintpimg/b_14cucintpimg_appendix_010011.html
retrieved_at: 2026-08-16T18:33:08.275915+00:00
---

PIMG Integration Guide for Cisco Unity Connection Release 15

# PIMG Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Adding a Secondary Master PIMG Unit

## Chapter: Adding a Secondary Master PIMG Unit

# Adding a Secondary Master PIMG Unit

Because the master PIMG unit processes all call information and MWI requests for the system, the integration loses important
                        functionality if the master PIMG unit stops working. If you want to minimize this risk, you can add a secondary master PIMG
                        unit to process call information and MWI requests when the primary master PIMG unit is no longer functioning.

During normal operation, the primary master PIMG unit is connected to power and is functioning, while the secondary master
                        PIMG unit is not connected to power and is not functioning. To activate the secondary master PIMG unit, you must disconnect
                        power to the primary master PIMG unit, then connect power to the secondary master PIMG unit.

The following task list describes the process for adding a secondary master PIMG unit.

## Adding a Secondary Master PIMG Unit

Because the master PIMG unit processes all call information and MWI requests for the system, the integration loses important
                           functionality if the master PIMG unit stops working. If you want to minimize this risk, you can add a secondary master PIMG
                           unit to process call information and MWI requests when the primary master PIMG unit is no longer functioning.

During normal operation, the primary master PIMG unit is connected to power and is functioning, while the secondary master
                           PIMG unit is not connected to power and is not functioning. To activate the secondary master PIMG unit, you must disconnect
                           power to the primary master PIMG unit, then connect power to the secondary master PIMG unit.

The following task list describes the process for adding a secondary master PIMG unit.

### Task List to Add a
                           	 Secondary Master PIMG Unit

Use the following task list to add a secondary master PIMG unit.

Set up the analog voice line connections to the master PIMG
                                    			 units. See the “Analog
                                       				Voice Line Connections for the Master PIMG Units” section .

Set up the serial data cable connections to the master PIMG
                                    			 units. See the “Serial
                                       				Data Cable Connections for the Master PIMG Units” section .

Configure the secondary master PIMG unit. See the “Configuring
                                       				the Secondary Master PIMG Unit” section .

### Analog Voice Line Connections for the Master PIMG Units

Circuit-switched phone systems typically have 25-pair or 32-pair cables to provide analog voice connections. It is common
                              that the cable is broken into individual lines that may attach to a punchdown cross-connect block (for example, 66-Type),
                              or the cable may terminate with RJ-11 or RJ-14 connectors to accept analog voice lines.

A punchdown cross-connect block or line splitters may be used to split the analog lines. It is possible to use these devices
                              in combination to manage and split the lines.

No devices other than those described in this appendix should be connected to the analog voice lines for any voice messaging
                                          port on the master PIMG units. Otherwise, the ring equivalency number (REN) may be exceeded and the primary and secondary
                                          servers may not receive sufficient ring current to answer calls.

#### Requirements

The following components are required for common configurations:

Two or three analog voice patch cables for each port on the
                                       			 phone system.

The applicable device to split the analog lines:

One or more punchdown cross-connect blocks (for example,
                                             				  66-Type), installed and ready to accept lines.

One line splitter for every one or two ports on the phone
                                             				  system. The line splitter accepts both RJ-11 and RJ-14 connectors.

The applicable connectors (RJ-11 and/or RJ-14) for the analog
                                       			 voice lines. Figure A-1 shows the pinout for the RJ-11 connector, and Figure
                                       			 A-2 shows the pinout for the RJ-14 connector.

#### Connections Using
                              	 RJ-11 Connectors

The following figures illustrate common configurations:

Figure A-3 shows the connections between a phone system and the
                                       			 primary and secondary master PIMG units, through a punchdown cross-connect
                                       			 block.

Figure A-4 shows the connections between a phone system with an
                                       			 RJ-11 connector and the primary and secondary master PIMG units.

Figure A-5 shows the connections between a phone system with an
                                       			 RJ-14 connector and the primary and secondary master PIMG units.

### Serial Data Cable Connections for the Master PIMG Units

Connecting the RS-232 serial cables between a circuit-switched phone system and the primary and secondary master PIMG varies
                              depending on the number of serial ports the phone system has.

#### Requirements

The following components are required for phone systems with only one serial port:

Three RS-232 serial cables

Data splitter unit

The following components are required for phone systems with multiple serial ports:

Two RS-232 serial cables

#### Connections for
                              	 the Serial Data Cables

Figure A-6 shows the connections between the serial port on a
                                 		phone system that has only one serial port to the serial ports on the primary
                                 		and secondary master PIMG units. Figure A-6 shows the connections between the
                                 		serial ports on a phone system that has two serial ports to the serial ports on
                                 		the master PIMG units.

Note that the following figures do not show the analog voice
                                 		lines, which are described in the “Analog
                                    		  Voice Line Connections for the Master PIMG Units” .

### Configuring the Secondary Master PIMG Unit

This procedure has the following requirements:

All analog lines and serial cables must be correctly connected.

The primary secondary master PIMG units must have the same firmware version installed.

The primary master PIMG unit is connected to power, while the secondary master PIMG unit is disconnected from power.

You have a Windows workstation that has access to the PIMG units.

Do the following procedure to make the configuration of the secondary master PIMG unit match the configuration of the primary
                              master PIMG unit.

#### Configuring the Secondary Master PIMG Unit

### SUMMARY STEPS

- On a Windows workstation, in a web browser, sign in to the primary master PIMG unit.

- On the Configuration menu, select Import/Export .

- On the Import/Export page, under Export Files, select Export All Settings .

- In the File Download dialog box, select Save .

- In the Save As dialog box, browse to the Windows workstation, browse to a directory where you want to save the file, and select Save .

- Exit the PIMG web interface.

- Disconnect power from the primary master PIMG unit.

- Connect power to the secondary master PIMG unit.

- On the Windows workstation, in a web browser, sign in the secondary master PIMG unit by entering the following case-sensitive
                                    settings.

- Select OK .

- On the Configuration menu of the secondary master PIMG unit, select Import/Export .

- On the Import/Export page, under Import File, select Browse .

- In the Choose File dialog box, browse to the file Config.ini that you saved from the primary master PIMG unit in Step 5 .

- Select Config.ini , and select Open .

- On the Import/Export page, select Import File .

- When prompted to restart the PIMG unit, select OK .

- Disconnect power from the secondary master PIMG unit.

- Connect power to the primary master PIMG unit.

### DETAILED STEPS

Step 1

On a Windows workstation, in a web browser, sign in to the primary master PIMG unit.

Step 2

On the Configuration menu, select Import/Export .

Step 3

On the Import/Export page, under Export Files, select Export All Settings .

Step 4

In the File Download dialog box, select Save .

Step 5

In the Save As dialog box, browse to the Windows workstation, browse to a directory where you want to save the file, and select Save .

Step 6

Exit the PIMG web interface.

Step 7

Disconnect power from the primary master PIMG unit.

Step 8

Connect power to the secondary master PIMG unit.

Step 9

On the Windows workstation, in a web browser, sign in the secondary master PIMG unit by entering the following case-sensitive
                                             settings.

Field

Setting

Username

Enter admin .

Password

Enter IpodAdmin .

Step 10

Select OK .

Step 11

On the Configuration menu of the secondary master PIMG unit, select Import/Export .

Step 12

On the Import/Export page, under Import File, select Browse .

Step 13

In the Choose File dialog box, browse to the file Config.ini that you saved from the primary master PIMG unit in Step 5 .

Step 14

Select Config.ini , and select Open .

Step 15

On the Import/Export page, select Import File .

Step 16

When prompted to restart the PIMG unit, select OK .

Step 17

Disconnect power from the secondary master PIMG unit.

Step 18

Connect power to the primary master PIMG unit.

| Note | No devices other than those described in this appendix should be connected to the analog voice lines for any voice messaging
                                          port on the master PIMG units. Otherwise, the ring equivalency number (REN) may be exceeded and the primary and secondary
                                          servers may not receive sufficient ring current to answer calls. |
|---|---|

| Step 1 | On a Windows workstation, in a web browser, sign in to the primary master PIMG unit. |
|---|---|
| Step 2 | On the Configuration menu, select Import/Export . |
| Step 3 | On the Import/Export page, under Export Files, select Export All Settings . |
| Step 4 | In the File Download dialog box, select Save . |
| Step 5 | In the Save As dialog box, browse to the Windows workstation, browse to a directory where you want to save the file, and select Save . |
| Step 6 | Exit the PIMG web interface. |
| Step 7 | Disconnect power from the primary master PIMG unit. |
| Step 8 | Connect power to the secondary master PIMG unit. |
| Step 9 | On the Windows workstation, in a web browser, sign in the secondary master PIMG unit by entering the following case-sensitive
                                             settings. Table 1. Default Sign-in Settings Field Setting Username Enter admin . Password Enter IpodAdmin . | Field | Setting | Username | Enter admin . | Password | Enter IpodAdmin . |
| Field | Setting |
| Username | Enter admin . |
| Password | Enter IpodAdmin . |
| Step 10 | Select OK . |
| Step 11 | On the Configuration menu of the secondary master PIMG unit, select Import/Export . |
| Step 12 | On the Import/Export page, under Import File, select Browse . |
| Step 13 | In the Choose File dialog box, browse to the file Config.ini that you saved from the primary master PIMG unit in Step 5 . |
| Step 14 | Select Config.ini , and select Open . |
| Step 15 | On the Import/Export page, select Import File . |
| Step 16 | When prompted to restart the PIMG unit, select OK . |
| Step 17 | Disconnect power from the secondary master PIMG unit. |
| Step 18 | Connect power to the primary master PIMG unit. |

| Field | Setting |
|---|---|
| Username | Enter admin . |
| Password | Enter IpodAdmin . |