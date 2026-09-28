---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-ce1400v-exwy-b-cisco-expressway-ce1400v-appliance-i-cc1019950b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/CE1400V/exwy_b_cisco-expressway-ce1400v-appliance-installation-guide/exwy_m_rear-panel-layout.html
retrieved_at: 2026-08-16T22:09:24.662266+00:00
---

Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

# Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

Updated: September 1, 2025

Chapter: Rear Panel Layout

## Chapter: Rear Panel Layout

# Rear Panel Layout

This section details the rear panel layout, LEDs, and ports.

## Rear Panel View

The CE1400V is shipped with a pair of PCIe Risers to accommodate a pair of network interface cards.

The hardware loadout is fixed and should not be changed.

For definitions of LED states, see . Status LEDs and Buttons .

1

PCIe slots, three

This configuration accepts three cards in riser slots 1, 2, and 3 as follows:

Riser 1, which is controlled by CPU 1:

Populated with UCSC-PCIEIQ10GF-D 4 port NIC

Riser 2, which is controlled by CPU 1:

Populated with UCSC-PCIEIQ10GF-D 4 port NIC

Riser 3, which is controlled by CPU 2:

Not populated

Only 2 Risers are installed.

2

Power supply units (PSUs), two which can be redundant when configured in 1+1 power mode.

3

Modular LAN-on-motherboard (mLOM) card or OCP card bay (x16 PCIe lane) populated with an Intel X710 OCP 3.0 card.

4

System identification button/LED

5

USB 3.0 ports (two)

6

1-Gb Ethernet dedicated management port

7

COM port (RJ-45 connector)

8

VGA video port (DB-15 connector)

For more information on the method to configure a Dedicated Management Interface (DMI), see Cisco Expressway Administrator Guide .

## Status LEDs and Buttons

This section contains information for interpreting rear LED states.

### Rear-Panel LEDs

The following illustration shows the LEDs on the server's rear panel.

The table listss the various LEDs on the server's rear panel and its definition of states.

LED Name

States

1

Rear Unit Identification

Off—The unit identification function is not in use.

Blue, blinking—The unit identification function is activated.

2

USB 3.0

3

USB 3.0

4

1-Gb Ethernet dedicated management link speed

Off—Link speed is 10 Mbps.

Amber—Link speed is 100 Mbps.

Green—Link speed is 1 Gbps.

5

1-Gb Ethernet dedicated management link status

Off—No link is present.

Green—Link is active.

Green, blinking—Traffic is present on the active link.

6

7

8

Power supply status (one LED each power supply unit)

AC power supplies:

Off—No AC input (12 V main power off, 12 V standby power off).

Green, blinking—12 V main power off; 12 V standby power on.

Green, solid—12 V main power on; 12 V standby power on.

Amber, blinking—Warning threshold detected but 12 V main power on.

Amber, solid—Critical error detected; 12 V main power off (for example, over-current, over-voltage, or over-temperature failure).

DC power supplies:

Off—No DC input (12 V main power off, 12 V standby power off).

Green, blinking—12 V main power off; 12 V standby power on.

Green, solid—12 V main power on; 12 V standby power on.

Amber, blinking—Warning threshold detected but 12 V main power on.

Amber, solid—Critical error detected; 12 V main power off (for example, over-current, over-voltage, or over-temperature failure).

| Note | The CE1400V is shipped with a pair of PCIe Risers to accommodate a pair of network interface cards. The hardware loadout is fixed and should not be changed. For definitions of LED states, see . Status LEDs and Buttons . |
|---|---|

| 1 | PCIe slots, three This configuration accepts three cards in riser slots 1, 2, and 3 as follows: Riser 1, which is controlled by CPU 1: Populated with UCSC-PCIEIQ10GF-D 4 port NIC Riser 2, which is controlled by CPU 1: Populated with UCSC-PCIEIQ10GF-D 4 port NIC Riser 3, which is controlled by CPU 2: Not populated Note Only 2 Risers are installed. | Note | Only 2 Risers are installed. | 2 | Power supply units (PSUs), two which can be redundant when configured in 1+1 power mode. |
|---|---|---|---|---|---|
| Note | Only 2 Risers are installed. |
| 3 | Modular LAN-on-motherboard (mLOM) card or OCP card bay (x16 PCIe lane) populated with an Intel X710 OCP 3.0 card. | 4 | System identification button/LED |
| 5 | USB 3.0 ports (two) | 6 | 1-Gb Ethernet dedicated management port |
| 7 | COM port (RJ-45 connector) | 8 | VGA video port (DB-15 connector) |

| Note | Only 2 Risers are installed. |
|---|---|

|  | LED Name | States |
|---|---|---|
| 1 | Rear Unit Identification | Off—The unit identification function is not in use. Blue, blinking—The unit identification function is activated. |
| 2 | USB 3.0 |  |
| 3 | USB 3.0 |  |
| 4 | 1-Gb Ethernet dedicated management link speed | Off—Link speed is 10 Mbps. Amber—Link speed is 100 Mbps. Green—Link speed is 1 Gbps. |
| 5 | 1-Gb Ethernet dedicated management link status | Off—No link is present. Green—Link is active. Green, blinking—Traffic is present on the active link. |
| 6 | RJ-45 COM port |  |
| 7 | RJ -45 COM port |  |
| 8 | Power supply status (one LED each power supply unit) | AC power supplies: Off—No AC input (12 V main power off, 12 V standby power off). Green, blinking—12 V main power off; 12 V standby power on. Green, solid—12 V main power on; 12 V standby power on. Amber, blinking—Warning threshold detected but 12 V main power on. Amber, solid—Critical error detected; 12 V main power off (for example, over-current, over-voltage, or over-temperature failure). DC power supplies: Off—No DC input (12 V main power off, 12 V standby power off). Green, blinking—12 V main power off; 12 V standby power on. Green, solid—12 V main power on; 12 V standby power on. Amber, blinking—Warning threshold detected but 12 V main power on. Amber, solid—Critical error detected; 12 V main power off (for example, over-current, over-voltage, or over-temperature failure). |