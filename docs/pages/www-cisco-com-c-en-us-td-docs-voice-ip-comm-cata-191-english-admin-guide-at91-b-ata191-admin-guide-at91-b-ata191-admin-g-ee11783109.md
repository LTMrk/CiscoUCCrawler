---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-ee11783109
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_010.html
retrieved_at: 2026-08-21T20:39:38.371837+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Install the ATA 191

## Chapter: Install the ATA 191

# Install the ATA 191

## ATA 191 Installation Information

You connect the ATA 191 hardware and configure the ATA 191 by loading the QED and firmware files. Install the QED file first,
                           then install the firmware file. For more information about loading the QED and firmware files, see the "Installation Notes"
                           section of the "Release Notes for Cisco ATA 191 Analog Telephone Adapter".

## Network Requirements

The ATA 191 acts as an endpoint on an IP telephony network. The following equipment is required:

Call Control system

Voice packet gateway—Required if you are connecting to the Public Switched Telephone Network (PSTN). A gateway is not required
                                 if an analog key system is in effect.

Ethernet connection

## Safety Recommendations

To ensure general safety, follow these guidelines:

Do not get this product wet or pour liquids into this device.

Do not open or disassemble this product.

Do not perform any action that creates a potential hazard to people or makes the equipment unsafe.

Use only the power supply that comes with the ATA.

Ultimate disposal of this product should be handled according to all national laws and regulations.

Read the installation instructions before you connect the system to its power source.

The plug-socket combination must always be accessible because it serves as the main disconnecting device.

Do not work on the system or connect or disconnect cables during periods of lightning activity.

To avoid electric shock, do not connect safety extra-low voltage (SELV) circuits to telephone-network voltage (TNV) circuits.
                                    LAN ports contain SELV circuits, and WAN ports contain TNV circuits. Some LAN and WAN ports both use RJ-45 connectors. Use
                                    caution when connecting cables.

For translated warnings, see the Regulatory Compliance and Safety Information for the Cisco ATA 191 document.

## Package Contents

The ATA 191 package contains the following items:

Cisco ATA 191 Analog Telephone Adapter

Regulatory Compliance and Safety Information for the ATA 191

5V power adapter with appropriate country clip

Ethernet cable

The ATA is intended for use only with the 5V DC power adapter that comes with the unit.

## Install Your Cisco ATA

You can use either Category 3/5/5e/6 cabling for 10-Mbps connections, but you must use Category 5/5e/6 for 100-Mbps connections.

Step 1

Connect the power supply to the Cisco DC Adapter port.

Step 2

Connect a straight-through Ethernet cable from the network to the network port on the ATA. Each ATA ships with one Ethernet
                                       cable in the box.

## Attach a Phone to the ATA 191

### Before you begin

You can attach one or two phones to an ATA 191.

Connect one or more phones to a phone port of the ATA with an RJ11 cable.

The PHONE1 and PHONE2 LEDs on the ATA light as solid green when there is activity on that port.

## Startup Process Verification

After your ATA has power connected to it, it begins the startup process by cycling through these steps:

The Power LED flashes during the startup process.

The Problem Report Tool (PRT) LED lights solid amber during initial bootup. The LED then flashes amber and then green while
                                 the application and kernel are booting.

If the PRT LED lights red during bootup, then either the MIC certificate failed, or the ATA failed to obtain a network address.

The LED for Phone 1 flashes while the Phone1 port boots, followed by the LED for Phone 2.

After the Phone1 and Phone2 ports register with Cisco Unified CM successfully, the corresponding LEDs are lit with solid green.
                                 If a phone port fails to register, the LED rapidly flashes in green three times, then repeats.

- When the ATA has successfully booted, the Power LED lights solid green and the PRT LED turns off. The Network LED flashes
                              as traffic is detected.

When you go offhook on the phone, the phone LED begins to flash, and you hear the dial tone. The ATA has completed the startup
                           process.

## Configure Startup Network Settings

### Before you begin

Perform this configuration if you are not using DHCP in your network.

Step 1

Configure these network settings on the ATA after you install the device on the network:

IP subnet information (subnet mask and gateway)

TFTP server IP address

Step 2

Configure these optional settings as necessary:

Administration VLAN ID

Step 3

Collect this information.

## Security on the ATA 191

Security features protect against several threats, including threats to the identity of the phone and to data. These features
                           establish and maintain authenticated communication streams between the phone and the Cisco Unified Communications Manager
                           server, and digitally sign files before they are delivered.

For more information about the security features, see the Security Guide for Cisco Unified Communications Manager.

You can start the installation of a Locally Significant Certificate (LSC) on the device profile from Cisco Unified Communications
                           Manager. Use the Device > Phone > Phone Configuration menu option. You can also use this menu option to update or remove an LSC.

Before you begin, make sure that the appropriate Cisco Unified Communications Manager and the CAPF security configurations
                           are complete:

On Cisco Unified Communications Operating System Administration, verify that the CAPF certificate has been installed.

The CAPF is running and configured.

See the Security Guide for Cisco Unified Communications Manager for more information.

### Disable Transport Layer Security Ciphers

You can disable Transport Layer Security (TLS) ciphers with the Disable TLS Ciphers parameter. This allows you to tailor your security for known vulnerabilities, and to align your network with your company's
                                 policies for ciphers.

None is the default setting.

You can disable more than one cipher suite. If you select all of the TLS ciphers, then ATA TLS service is impacted. ATA has
                                 the following choices:

None (default)

TLS_RSA_WITH_AES_128_CBC_SHA

TLS_RSA_WITH_AES_256_CBC_SHA

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

To disable one or more TLS ciphers on CUCM, do the following:

Sign into Cisco Unified Communications Manager Administration as an administrator.

Do one of the following actions as needed:

To configure all deployed ATAs, go to System > Enterprise Phone Configuration .

To configure ATAs sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

To configure an individual ATA, go to Device > Phone .

The precedence order:

Phone Configuration > Common Phone Profile > Enterprise Phone Configuration

Configure the parameter Disable TLS Ciphers to disable one or more TLS ciphers.

Click Save .

Click Apply Config .

The ATA will restart automatically.

### Set the Minimum TLS Version for Client and Server

You can set up the minimum version of TLS required for client and server respectively.

For more information about the TLS 1.3 compatibility for Cisco ATA 191, see TLS 1.3 Compatibility Matrix for Cisco Collaboration Products .

#### Before you begin

Step 1

Sign into Cisco Unified Communications Manager Administration as an administrator.

Step 2

Navigate to one of the following windows:

System > Enterprise Phone Configuration

Device > Device Settings > Common Phone Profile

Device > Phone > Phone Configuration

The precedence order:

Phone Configuration > Common Phone Profile > Enterprise Phone Configuration

Step 3

Set up the field TLS Client Min Version for the ATA that acts as the TLS client:

The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later.

TLS 1.0 : The TLS client supports the versions of TLS from 1.0 to 1.3.

TLS 1.1 : The TLS client supports the versions of TLS from 1.1 to 1.3.

If the TLS version in server is lower than 1.1, for example, 1.0, then the connection can't be established.

TLS 1.2 (default): The TLS client supports TLS 1.2 and 1.3.

If the TLS version in server is lower than 1.2, for example, 1.1 or 1.0, then the connection can't be established.

TLS 1.3 : The TLS client supports TLS 1.3 only.

If the TLS version in server is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the connection can't be established.

Step 4

Set up the field TLS Server Min Version for the ATA that acts as the TLS server (for example, an HTTPs web server):

TLS 1.0 : The TLS server supports the versions of TLS from 1.0 to 1.3.

TLS 1.1 : The TLS server supports the versions of TLS from 1.1 to 1.3.

If the TLS version in client is lower than 1.1, for example, 1.0, then the ATA rejects the connections.

TLS 1.2 (default): The TLS server supports TLS 1.2 and 1.3.

If the TLS version in client is lower than 1.2, for example, 1.1 or 1.0, then the ATA rejects the connections.

TLS 1.3 : The TLS server supports TLS 1.3 only.

If the TLS version in client is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the ATA rejects the connections.

Step 5

Click Save .

Step 6

Click Apply Config .

Step 7

Restart the ATA.

| Note | The ATA is intended for use only with the 5V DC power adapter that comes with the unit. |
|---|---|

| Step 1 | Connect the power supply to the Cisco DC Adapter port. |
|---|---|
| Step 2 | Connect a straight-through Ethernet cable from the network to the network port on the ATA. Each ATA ships with one Ethernet
                                       cable in the box. |

| Connect one or more phones to a phone port of the ATA with an RJ11 cable. The PHONE1 and PHONE2 LEDs on the ATA light as solid green when there is activity on that port. |
|---|

| Step 1 | Configure these network settings on the ATA after you install the device on the network: IP subnet information (subnet mask and gateway) TFTP server IP address |
|---|---|
| Step 2 | Configure these optional settings as necessary: Administration VLAN ID |
| Step 3 | Collect this information. |

| Step 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Navigate to one of the following windows: System > Enterprise Phone Configuration Device > Device Settings > Common Phone Profile Device > Phone > Phone Configuration The precedence order: Phone Configuration > Common Phone Profile > Enterprise Phone Configuration |
| Step 3 | Set up the field TLS Client Min Version for the ATA that acts as the TLS client: Note The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later. TLS 1.0 : The TLS client supports the versions of TLS from 1.0 to 1.3. TLS 1.1 : The TLS client supports the versions of TLS from 1.1 to 1.3. If the TLS version in server is lower than 1.1, for example, 1.0, then the connection can't be established. TLS 1.2 (default): The TLS client supports TLS 1.2 and 1.3. If the TLS version in server is lower than 1.2, for example, 1.1 or 1.0, then the connection can't be established. TLS 1.3 : The TLS client supports TLS 1.3 only. If the TLS version in server is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the connection can't be established. | Note | The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later. |
| Note | The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later. |
| Step 4 | Set up the field TLS Server Min Version for the ATA that acts as the TLS server (for example, an HTTPs web server): TLS 1.0 : The TLS server supports the versions of TLS from 1.0 to 1.3. TLS 1.1 : The TLS server supports the versions of TLS from 1.1 to 1.3. If the TLS version in client is lower than 1.1, for example, 1.0, then the ATA rejects the connections. TLS 1.2 (default): The TLS server supports TLS 1.2 and 1.3. If the TLS version in client is lower than 1.2, for example, 1.1 or 1.0, then the ATA rejects the connections. TLS 1.3 : The TLS server supports TLS 1.3 only. If the TLS version in client is lower than 1.3, for example, 1.2, 1.1 or 1.0, then the ATA rejects the connections. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config . |
| Step 7 | Restart the ATA. |

| Note | The "TLS 1.3" option is available on Cisco Unified CM 15SU2, or later. |
|---|---|