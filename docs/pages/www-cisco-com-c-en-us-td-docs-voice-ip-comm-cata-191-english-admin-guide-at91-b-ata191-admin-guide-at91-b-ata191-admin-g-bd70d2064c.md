---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-bd70d2064c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_01.html
retrieved_at: 2026-08-22T01:04:10.840654+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Prepare to Install the ATA 191 on Your Network

## Chapter: Prepare to Install the ATA 191 on Your Network

# Prepare to Install the ATA 191 on Your Network

## Interactions with Other Cisco Unified IP Communications Products

The ATA 191 enables you to communicate using voice over a data network. To provide this capability, the ATA 191 depends upon
                              and interacts with several other key Cisco Unified IP Telephony and Network components, including Cisco Unified Communications
                              Manager, DNS and DHCP servers, TFTP servers, media resources, and so on.

To function in the IP telephony network, the ATA 191 must be connected to a networking device, such as a Cisco Catalyst switch.
                              You must also register the ATA 191 with a Cisco Unified Communications Manager system before you can send and receive calls.

For related information about voice and IP communications, see this URL:

https://www.cisco.com/c/en/us/products/unified-communications/index.html

### Interaction with Cisco Unified Communications Manager

Cisco Unified Communciations Manager is an open industry-standard call process system. Cisco Unified Communications Manager
                              software sets up and tears down calls between analog phones that are connected to the ATA, and thus integrates traditional
                              PBX functionality with the corporate IP network. Cisco Unified Communications Manager manages the components of the IP telephony
                              system: the phones, the access gateways, and the resources necessary for features such as call conferencing and route planning.
                              Cisco Unified Communications Manager also provides:

Firmware for devices

Authentication and encryption (if configured for the telephony system)

Configuration and CTL files via the TFTP service

Phone registration

Call preservation, so that a media session continues if signaling is lost between the primary Communications Manager

For information about configuring Cisco Unified Communications Manager to work with the IP devices described in this chapter,
                              see Administration Guide for Cisco Unified Communications Manager and IM and Presence Service , System Configuration Guide for Cisco Unified Communications Manager , and Security Guide for Cisco Unified Communications Manager .

## Power Guidelines

The ATA is powered with external power. External power is provided through a separate power supply.

The following power type and guideline applies to external power for the ATA:

Power Type—External power (provided through the Universal AC external power supply).

Guidelines—The ATA uses the Universal AC power supply 100/240V.

## Power Outage

Your accessibility to emergency service through the phone depends the phone being powered. If there is an interruption in
                              the power supply, Service and Emergency Calling Service dialing will not function until power is restored. In the case of
                              a power failure or disruption, you may need to reset or reconfigure equipment before using the Service or Emergency Calling
                              Service dialing.

## Phone Configuration Files

Configuration files for a phone are stored on the TFTP server and define parameters for connecting to Cisco UnifiedCommunications
                              Manager. When you make a change in Cisco UnifiedCommunications Manager that requires the ATA 191 line to be reset, the phone
                              configuration file is automatically updated. If a system reset or restart is required, both lines must reset or restart at
                              the same time.

Configuration files also contain information about which image load the ATA 191 should be running. If this image load differs
                              from the one currently loaded on an ATA 191, the phone contacts the TFTP server to request the required load files. These
                              files are digitally signed to ensure the authenticity of the file source.

If the device security mode in the configuration file is set to Authenticated and the CTL file on the ATA 191 has a valid
                              certificate for Cisco Unified Communications Manager, the phone establishes a TLS connection to Cisco Unified Communications
                              Manager. Otherwise, the ATA 191 establishes a TCP/UDP connection. You can go to Voice > Line > SIP Settings on the ATA 191 web GUI, where the SIP Transport should correspond to the transport type in the Phone Security Profile in
                              Cisco Unified Communications Manager.

If you configure security-related settings in Cisco Unified Communications Manager Administration, the phone configuration
                              file contains sensitive information. To ensure the privacy of a configuration file, configure it for encryption. For detailed
                              information, see the “Encrypted Phone Configuration Setup” chapter of the Security Guide for Cisco Unified Communications Manager at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

If the ATA 191 has registered before, the ATA 191 accesses the configuration file named ATA< mac_address >.cnf.xml, where mac_address is the MAC address of the phone. If the ATA 191 cannot access that configuration file, then it accesses the default XMLDefault.cnf.xml
                              configuration file.

If autoregistration is not enabled and you did not add the ATA 191 to the Cisco Unified Communications Manager database, the
                              ATA 191 does not attempt to register with Cisco Unified Communications Manager.

For the ATA 191, the TFTP server generates these SIP configuration files:

SIP IP Phone:

For unsigned and unencrypted files—ATA<mac>.cnf.xml

For signed files—ATA<mac>.cnf.xml.sgn

For signed and encrypted files—ATA<mac>.cnf.xml.enc.sgn

The filenames are derived from the MAC Address in the Phone Configuration window of CiscoUnified Communications Manager Administration.
                              The MAC address uniquely identifies the phone. For more information, see the Administration Guide for Cisco Unified Communications Manager and IM and Presence Service .

For more information about how the phone interacts with the TFTP server, see the “Configure TFTP Servers” chapter of the System Configuration Guide for Cisco Unified Communications Manager at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html

## ATA 191 Startup Process

When the ATA 191 connects to the VoIP network, it goes through a standard startup process. Depending on your specific network
                              configuration, not all these process steps may occur on your ATA.

Task

Related Topics

1

Obtaining power.

The ATA 191 uses external power.

See Power Guidelines .

2

Loading the Stored Image.

The Cisco ATA 191 has nonvolatile flash memory in which it stores firmware images and user-defined preferences. At startup,
                                          the ATA 191 runs a bootstrap loader that loads an ATA 191 image stored in flash memory. Using this image, the ATA 191 initializes
                                          its software and hardware.

3

Obtaining an IP Address.

If the Cisco ATA 191 is using DHCP to obtain an IP address, the device queries the DHCP server to obtain one. If you are not
                                          using DHCP in your network, assign static IP addresses to each device locally.

4

Requesting the CTL file.

The TFTP server stores the CTL file. This file contains the certificates necessary for establishing a secure connection between
                                          the device and Cisco UnifiedCommunications Manager.

See the “Cisco CTL Client Setup” chapter of the Security Guide for Cisco UnifiedCommunications Manager at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

5

Requesting the Configuration File.

The TFTP server has configuration files, which define parameters for connecting to Cisco Unified Communications Manager and
                                          other information for the ATA 191.

See Phone Configuration Files .

6

Contacting Cisco Unified Communications Manager.

The configuration file defines how the ATA 191 communicates with Cisco UnifiedCommunications Manager and provides a device
                                          with its load ID. After obtaining the file from the TFTP server, the device attempts to make a connection to the highest priority
                                          Cisco UnifiedCommunications Manager on the list. If the device is configured for secure signaling (encrypted or authenticated),
                                          and the Cisco Unified Communications Manager is set to Mixed (security) mode, the device makes a TLS connection. Otherwise,
                                          it makes a nonsecure TCP/UDP connection.

See Phone Configuration Files .

## Start up Process with Standby Image

The ATA 191 has two images or partitions in permanent storage. The second image allows the device to recover if the initial
                              image is corrupted.

Press the PRT button when the power is on, and you switch to the standby partition. Startup is similar to the normal process,
                              except that the LED for Phone 2 flashes amber indicating that the second partition is being used.

## Addition of the ATA 191 to the Cisco Unified CM Database

Before you install the ATA 191, choose a method for adding the devices to the Cisco Unified Communications Manager database.

The following table provides an overview of these methods for adding the ATA 191 to the Cisco Unified Communications Manager
                              database.

Method

Requires MAC Address?

Notes

Autoregistration

No

Results in automatic assignment of directory numbers.

Not available when mixed mode is enabled.

Using the Cisco Unified Communications Manager Administration

Yes

Requires phones to be added individually.

### Addition with Autoregistration

By enabling autoregistration before you begin installing the ATA 191, you can:

Automatically add devices without first gathering MAC addresses from the ATA 191.

Automatically add an ATA 191 to the Cisco Unified Communications Manager database when you physically connect the phone to
                                       your IP telephony network. During autoregistration, Cisco Unified Communications Manager assigns the next available sequential
                                       directory number to the phone.

To change any settings, quickly enter devices into the Cisco Unified Communications Manager database and modify settings,
                                       such as directory numbers, from Cisco Unified Communications Manager.

Move autoregistered devices to new locations and assign them to different device pools without affecting their directory numbers.

Support exists for autoregistration for several devices in the Unified CM at the same time.

Autoregistration is disabled by default. Sometimes, you may not want to use autoregistration. For example, if you want to
                                 assign a specific directory number to the phone or if you plan to use secure connection with Cisco Unified Communications
                                 Manager. For information about enabling autoregistration, see the Enabling Auto-Registration in the Cisco Unified Communications Manager Administration Guide.

For mixed mode, autoregistration is automatically disabled and cannot be changed. For nonsecure mode, autoregistration is
                                             disabled by default but can be enabled manually.

### Addition with Cisco Unified Communications Manager Administration

You can add the ATA 191 individually to the Cisco Unified Communications Manager database using Cisco Unified Communications
                                 Manager Administration. To do so, first obtain the MAC address for each device.

After you have collected MAC addresses, in Cisco Unified Communications Manager Administration, choose Device > Phone and click Add New to begin.

The ATA 191 has two FXS ports, and each port has its own MAC address. The first ATA 191 port uses the MAC address and the
                                             second ATA 191 port uses the shifted MAC address (example, AABBCCDDEEFF to BBCCDDEEFF01). You can add two devices (either
                                             an analog phone or a fax machine) from the Unified CM administration page.

For complete instructions and conceptual information about Cisco Unified Communications Manager, see the Cisco Unified Communications Manager Administration Guide and the Cisco Unified Communications Manager System Guide .

## Determine the MAC Address of the ATA

Choose one of the following methods to determine the MAC address:

Look at the MAC label on the back of the ATA.

Go to Voice > Information on the web page of the device and check the MAC address.

| Task |  | Related Topics |
|---|---|---|
| 1 | Obtaining power. The ATA 191 uses external power. | See Power Guidelines . |
| 2 | Loading the Stored Image. The Cisco ATA 191 has nonvolatile flash memory in which it stores firmware images and user-defined preferences. At startup,
                                          the ATA 191 runs a bootstrap loader that loads an ATA 191 image stored in flash memory. Using this image, the ATA 191 initializes
                                          its software and hardware. |  |
| 3 | Obtaining an IP Address. If the Cisco ATA 191 is using DHCP to obtain an IP address, the device queries the DHCP server to obtain one. If you are not
                                          using DHCP in your network, assign static IP addresses to each device locally. |  |
| 4 | Requesting the CTL file. The TFTP server stores the CTL file. This file contains the certificates necessary for establishing a secure connection between
                                          the device and Cisco UnifiedCommunications Manager. | See the “Cisco CTL Client Setup” chapter of the Security Guide for Cisco UnifiedCommunications Manager at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html |
| 5 | Requesting the Configuration File. The TFTP server has configuration files, which define parameters for connecting to Cisco Unified Communications Manager and
                                          other information for the ATA 191. | See Phone Configuration Files . |
| 6 | Contacting Cisco Unified Communications Manager. The configuration file defines how the ATA 191 communicates with Cisco UnifiedCommunications Manager and provides a device
                                          with its load ID. After obtaining the file from the TFTP server, the device attempts to make a connection to the highest priority
                                          Cisco UnifiedCommunications Manager on the list. If the device is configured for secure signaling (encrypted or authenticated),
                                          and the Cisco Unified Communications Manager is set to Mixed (security) mode, the device makes a TLS connection. Otherwise,
                                          it makes a nonsecure TCP/UDP connection. | See Phone Configuration Files . |

| Method | Requires MAC Address? | Notes |
|---|---|---|
| Autoregistration | No | Results in automatic assignment of directory numbers. Not available when mixed mode is enabled. |
| Using the Cisco Unified Communications Manager Administration | Yes | Requires phones to be added individually. |

| Note | Support exists for autoregistration for several devices in the Unified CM at the same time. |
|---|---|

| Note | For mixed mode, autoregistration is automatically disabled and cannot be changed. For nonsecure mode, autoregistration is
                                             disabled by default but can be enabled manually. |
|---|---|

| Note | The ATA 191 has two FXS ports, and each port has its own MAC address. The first ATA 191 port uses the MAC address and the
                                             second ATA 191 port uses the shifted MAC address (example, AABBCCDDEEFF to BBCCDDEEFF01). You can add two devices (either
                                             an analog phone or a fax machine) from the Unified CM administration page. |
|---|---|

| Choose one of the following methods to determine the MAC address: |
|---|