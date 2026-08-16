---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-ce1400v-exwy-b-cisco-expressway-ce1400v-appliance-i-5206e5716e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/CE1400V/exwy_b_cisco-expressway-ce1400v-appliance-installation-guide/exwy_m_front-panel-layout.html
retrieved_at: 2026-08-16T22:09:20.352834+00:00
---

Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

# Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

Updated: September 1, 2025

Chapter: Front Panel Layout

## Chapter: Front Panel Layout

# Front Panel Layout

This section details the front panel layout, LEDs, and ports.

## Front Panel View

The CE1400V is shipped with fixed configuration of 6x SAS hard drives as a RAID5 volume.

The hardware loadout is fixed and should not be changed.

1

Drive bays 1 – 10 support SAS/SATA hard disk drives (HDDs) and solid-state drives (SSDs). As an option, drive bays 1-4 can
                                          contain up to 4 NVMe drives in any number up to 4. Drive bays 5 through 10 supports only SAS/SATA HDDs or SSDs.

NVMe drives are supported in a dual CPU server only.

Only 6 Drive bays are used.

2

Unit identification button/LED

3

Power button/power status LED

4

KVM connector

(used with KVM cable that provides one DB-15 VGA, one DB-9 serial, and two USB 2.0 connectors)

5

System LED cluster:

Fan status LED

System status LED

Power supply status LED

Network link activity LED

Temperature status LED

For definitions of LED states, see Front Panel LEDs .

-

For more information on the method to configure a Dedicated Management Interface (DMI), see Cisco Expressway Administrator Guide .

## Status LEDs and Buttons

This section contains information for interpreting front LED states.

### Front-Panel LEDs

The following illustration shows the LEDs on the server's front panel.

The table listss the various LEDs on the server's front panel and its definition of states.

LED Name

States

1

Power button/LED ( )

Off—There is no AC power to the server.

Amber—The server is in standby power mode. Power is supplied only to the Cisco IMC and some motherboard functions.

Green—The server is in main power mode. Power is supplied to all server components.

2

Unit identification (

Off—The unit identification function is not in use.

Blue, blinking—The unit identification function is activated.

3

System health ( )

Green—The server is running in normal operating condition.

Green, blinking—The server is performing system initialization and memory check.

Amber, steady—The server is in a degraded operational state (minor fault). For example:

Power supply redundancy is lost.

CPUs are mismatched.

At least one CPU is faulty.

At least one DIMM is faulty.

At least one drive in a RAID configuration failed.

Amber, 2 blinks—There is a major fault with the system board.

Amber, 3 blinks—There is a major fault with the memory DIMMs.

Amber, 4 blinks—There is a major fault with the CPUs.

4

Power supply status ( )

Green—All power supplies are operating normally.

Amber, steady—One or more power supplies are in a degraded operational state.

Amber, blinking—One or more power supplies are in a critical fault state.

5

Fan status ( )

Green—All fan modules are operating properly.

Amber, blinking—One or more fan modules breached the non-recoverable threshold.

6

Network link activity ( )

Off—The Ethernet LOM port link is idle.

Green—One or more Ethernet LOM ports are link-active, but there is no activity.

Green, blinking—One or more Ethernet LOM ports are link-active, with activity.

7

Temperature status ( )

Green—The server is operating at normal temperature.

Amber, steady—One or more temperature sensors breached the critical threshold.

Amber, blinking—One or more temperature sensors breached the non-recoverable threshold.

| Note | The CE1400V is shipped with fixed configuration of 6x SAS hard drives as a RAID5 volume. The hardware loadout is fixed and should not be changed. |
|---|---|

| 1 | Drive bays 1 – 10 support SAS/SATA hard disk drives (HDDs) and solid-state drives (SSDs). As an option, drive bays 1-4 can
                                          contain up to 4 NVMe drives in any number up to 4. Drive bays 5 through 10 supports only SAS/SATA HDDs or SSDs. NVMe drives are supported in a dual CPU server only. Note Only 6 Drive bays are used. | Note | Only 6 Drive bays are used. | 2 | Unit identification button/LED |
|---|---|---|---|---|---|
| Note | Only 6 Drive bays are used. |
| 3 | Power button/power status LED | 4 | KVM connector (used with KVM cable that provides one DB-15 VGA, one DB-9 serial, and two USB 2.0 connectors) |
| 5 | System LED cluster: Fan status LED System status LED Power supply status LED Network link activity LED Temperature status LED For definitions of LED states, see Front Panel LEDs . |  | - |

| Note | Only 6 Drive bays are used. |
|---|---|

|  | LED Name | States |
|---|---|---|
| 1 | Power button/LED ( ) | Off—There is no AC power to the server. Amber—The server is in standby power mode. Power is supplied only to the Cisco IMC and some motherboard functions. Green—The server is in main power mode. Power is supplied to all server components. |
| 2 | Unit identification ( | Off—The unit identification function is not in use. Blue, blinking—The unit identification function is activated. |
| 3 | System health ( ) | Green—The server is running in normal operating condition. Green, blinking—The server is performing system initialization and memory check. Amber, steady—The server is in a degraded operational state (minor fault). For example: Power supply redundancy is lost. CPUs are mismatched. At least one CPU is faulty. At least one DIMM is faulty. At least one drive in a RAID configuration failed. Amber, 2 blinks—There is a major fault with the system board. Amber, 3 blinks—There is a major fault with the memory DIMMs. Amber, 4 blinks—There is a major fault with the CPUs. |
| 4 | Power supply status ( ) | Green—All power supplies are operating normally. Amber, steady—One or more power supplies are in a degraded operational state. Amber, blinking—One or more power supplies are in a critical fault state. |
| 5 | Fan status ( ) | Green—All fan modules are operating properly. Amber, blinking—One or more fan modules breached the non-recoverable threshold. |
| 6 | Network link activity ( ) | Off—The Ethernet LOM port link is idle. Green—One or more Ethernet LOM ports are link-active, but there is no activity. Green, blinking—One or more Ethernet LOM ports are link-active, with activity. |
| 7 | Temperature status ( ) | Green—The server is operating at normal temperature. Amber, steady—One or more temperature sensors breached the critical threshold. Amber, blinking—One or more temperature sensors breached the non-recoverable threshold. |