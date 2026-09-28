---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-7f22d6c542
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_01000.html
retrieved_at: 2026-08-22T01:04:14.822834+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Voice Menu Codes

## Chapter: Voice Menu Codes

# Voice Menu Codes

## Access the IVR and Configure Your ATA Settings

### Before you begin

If you set the IP mode to static IP, you must go on-hook to make it effective. Then, you can configure the IP address, subnet
                              mask, and default gateway.

The network cable must be connected to set a static IP.

You can change the IVR password on the Device window of Cisco Unified Communications Manager.

Step 1

To access the IVR, go off-hook on the phone connected to PHONE1 or PHONE2.

Step 2

Press **** from the phone keypad.

The IVR prompts for a password.

The ATA 191 allows you to enter only numerical values for the password.

Step 3

Enter the IVR password by pressing the number keypad, followed by # .

You are at the IVR main configuration menu.

Step 4

Follow the voice prompts on the IVR. See IVR Configuration Menu Options for information on navigating the IVR.

Step 5

To return to the main configuration menu, press * .

Step 6

To exit the IVR, end the call.

### IVR Tips

When using the IVR to manage the ATA, note the following tips:

Enter the numbers slowly, listening for the audio confirmation before entering the next number.

After you select an option, press the # (pound) key.

To exit the menu, hang up the phone.

After entering a value such as an IP address, press the # (pound) key to indicate that you have finished your selection. Then proceed as needed:

To save a setting, press 1 .

To review a setting, press 2 .

To re-enter a setting, press 3 .

To cancel your entry and return to the main menu, press * (star).

When entering a value, you can cancel the changes by pressing the * (star) key twice within half a second. Be sure to press the key quickly, or the * is treated as a decimal point entry.

If the menu is inactive for more than one minute, the IVR times out. Re-enter the IVR menu by pressing **** . Your settings take effect after you hang up the phone or exit the IVR. The ATA may reboot now.

To enter special characters, use the following key combinations:

To enter a dot (.) or colon (:) that separates octets in the IP Address, press star (*).

To enter the hexadecimal A, press the 2 key two times quickly.

To enter the hexadecimal B, press the 2 key three times quickly.

To enter the hexadecimal C, press the 2 key four times quickly.

To enter the hexadecimal D, press the 3 key two times quickly.

To enter the hexadecimal E, press the 3 key three times quickly.

To enter the hexadecimal F, press the 3 key four times quickly.

For example, to enter the IP address 191.168.1.105, perform the following tasks:

Press these keys: 191*168*1*105

- Press the # (pound) key to indicate that you have finished entering the IP address.

Press 1 to save the IP address or press the * (star) key to cancel your entry and return to the main menu.

### IVR Configuration Menu Options

The following table describes the various options in the IVR Configuration Menu.

Menu Option

IVR Action

Notes

100

(IPv4) Check the Internet Addressing Method

Answers with 0, the default option (DHCP).

101

(IPv4) Set the Internet Addressing Method

0: DHCP; 1: Static IP

102

Check Stack Mode.

0: IPv4; 1:IPv6; 2: Dual

110

(IPv4) Show the ATA IP address

111

(IPv4) Configure the ATA's static IP address

Available in static IP mode only.

120

(IPv4) Show the subnet mask

121

(IPv4) Configure the subnet mask

Available in static IP mode only.

130

(IPv4) Check the gateway IP address

131

(IPv4) Configure the gateway IP address

Available in static IP mode only.

160

(IPv4) Check the primary DNS Server setting

161

(IPv4) Set the primary DNS Server

220

(IPv4) Show the TFTP server address

221

(IPv4) Configure the TFTP server address

230

Show the VLAN.

231

Configure a VLAN.

To enable a VLAN, set the VLAN ID from 1 to 4094.

To disable a VLAN, set the VLAN ID to 4095.

600

(IPv6) Check the IPv6 Internet addressing method

601

(IPv6) Set the IPv6 Internet Addressing Method

0: DHCP; 1: Static IP

606

Check IPv6 Auto Configuration.

0: Disabled; 1: Enabled.

610

(IPv6) Show the ATA IP address

611

(IPv6) Configure the ATA's static IP address

Available in IPv6 static IP mode only.

620

(IPv6) Check the IP address prefix length

621

(IPv6) Configure the static IP address prefix length

Available in IPv6 static IP mode only.

622

(IPv6) Check the TFTPv6 server address

623

(IPv6) Set the TFTPv6 server address

630

(IPv6) Check the gateway IP address

631

(IPv6) Configure the gateway IP address

Available in IPv6 static IP mode only.

660

(IPv6) Check the primary DNS Server setting

661

(IPv6) Set the primary DNS Server

73738

Factory Reset

802

Configure the 802.1x authentication

0: Disabled; 1: Enabled

803

Check the 802.1x   authentication configuration

Respond with a number: 0 or 1.

0: Disabled; 1: Enabled

| Note | You can change the IVR password on the Device window of Cisco Unified Communications Manager. |
|---|---|

| Step 1 | To access the IVR, go off-hook on the phone connected to PHONE1 or PHONE2. |
|---|---|
| Step 2 | Press **** from the phone keypad. The IVR prompts for a password. The ATA 191 allows you to enter only numerical values for the password. |
| Step 3 | Enter the IVR password by pressing the number keypad, followed by # . You are at the IVR main configuration menu. |
| Step 4 | Follow the voice prompts on the IVR. See IVR Configuration Menu Options for information on navigating the IVR. |
| Step 5 | To return to the main configuration menu, press * . |
| Step 6 | To exit the IVR, end the call. |

| Menu Option | IVR Action | Notes |
|---|---|---|
| 100 | (IPv4) Check the Internet Addressing Method | Answers with 0, the default option (DHCP). |
| 101 | (IPv4) Set the Internet Addressing Method | 0: DHCP; 1: Static IP |
| 102 | Check Stack Mode. | 0: IPv4; 1:IPv6; 2: Dual |
| 110 | (IPv4) Show the ATA IP address |  |
| 111 | (IPv4) Configure the ATA's static IP address | Available in static IP mode only. |
| 120 | (IPv4) Show the subnet mask |  |
| 121 | (IPv4) Configure the subnet mask | Available in static IP mode only. |
| 130 | (IPv4) Check the gateway IP address |  |
| 131 | (IPv4) Configure the gateway IP address | Available in static IP mode only. |
| 160 | (IPv4) Check the primary DNS Server setting |  |
| 161 | (IPv4) Set the primary DNS Server |  |
| 220 | (IPv4) Show the TFTP server address |  |
| 221 | (IPv4) Configure the TFTP server address |  |
| 230 | Show the VLAN. |  |
| 231 | Configure a VLAN. | To enable a VLAN, set the VLAN ID from 1 to 4094. To disable a VLAN, set the VLAN ID to 4095. |
| 600 | (IPv6) Check the IPv6 Internet addressing method |  |
| 601 | (IPv6) Set the IPv6 Internet Addressing Method | 0: DHCP; 1: Static IP |
| 606 | Check IPv6 Auto Configuration. | 0: Disabled; 1: Enabled. |
| 610 | (IPv6) Show the ATA IP address |  |
| 611 | (IPv6) Configure the ATA's static IP address | Available in IPv6 static IP mode only. |
| 620 | (IPv6) Check the IP address prefix length |  |
| 621 | (IPv6) Configure the static IP address prefix length | Available in IPv6 static IP mode only. |
| 622 | (IPv6) Check the TFTPv6 server address |  |
| 623 | (IPv6) Set the TFTPv6 server address |  |
| 630 | (IPv6) Check the gateway IP address |  |
| 631 | (IPv6) Configure the gateway IP address | Available in IPv6 static IP mode only. |
| 660 | (IPv6) Check the primary DNS Server setting |  |
| 661 | (IPv6) Set the primary DNS Server |  |
| 73738 | Factory Reset |  |
| 802 | Configure the 802.1x authentication | 0: Disabled; 1: Enabled |
| 803 | Check the 802.1x   authentication configuration | Respond with a number: 0 or 1. 0: Disabled; 1: Enabled |