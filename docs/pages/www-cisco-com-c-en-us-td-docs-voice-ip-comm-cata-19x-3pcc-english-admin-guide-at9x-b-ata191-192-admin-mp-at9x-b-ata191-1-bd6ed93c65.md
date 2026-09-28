---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-bd6ed93c65
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_01001.html
retrieved_at: 2026-08-22T01:03:53.629677+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: IVR for Administration

## Chapter: IVR for Administration

# IVR for Administration

## Use IVR for Administration

An IVR system is available to help you to configure and manage your ATA. Use a telephone keypad to select options and to make
                              your entries.

Step 1

Connect an analog phone to a PHONE port of the ATA.

Step 2

Press the star (*) key four times: ****

Step 3

When challenged for a password:

- Log in as an administrator.

- Log in as the PHONE port's user.

Step 4

Enter the code for the desired action.

## IVR Tips

Enter the numbers slowly, listening for the audio confirmation before entering the next number.

After you select an option, press the # (pound) key.

To exit the menu, hang up the telephone or enter 3948# to exit.

After entering a value, such as an IP address, press the # (pound) key to indicate that you have finished your selection. Then proceed as needed:

To save a setting, press 1 .

To review a setting, press 2 .

To re-enter a setting, press 3 .

To cancel your entry and return to the main menu, press * (star).

While entering a value, you can cancel the changes by pressing the * (star) key twice within half a second. Be sure to press the key quickly, or the * will be treated as a decimal point entry.

If the menu is inactive for more than one minute, the IVR times out. You will need to re-enter the IVR menu by pressing the
                                    star key four times: **** . Your settings take effect after you hang up the telephone or exit the IVR. The ATA may reboot at this time.

To enter the decimal points in an IP address, press the * (star) key.

For example, to enter the IP address 191.168.1.105, perform the following tasks:

Press these keys: 191*168*1*105

Press the # (pound) key to indicate that you have finished entering the IP address.

Press 1 to save the IP address or press the * (star) key to cancel your entry and return to the main menu.

## IVR Actions

IVR Action

Menu Option

Choices and Instructions

Enter IVR Menu

****

Check Internet Addressing Method

100

Check Internet6 Addressing Method

600

Set Internet Addressing Method

101

0 —DHCP

1 —Static IP

2 —PPoE

Check Stack Mode

102

0 —IPv4

1 —IPv6

2 —Dual

Set Stack Mode

103

0 —IPv4

1 —IPv6

2 —Dual

Set Internet6 Addressing Method

601

0 —DHCP

1 —Static IP

2 —PPPoE

Check IPv6 Auto Configuration

607

0 —Disable

1 —Enable

Set IPv6 Auto Configuration

606

0 —Disable

1 —Enable

Check Internet IP Address (INTERNET port)

110

Check Internet6 Address (INTERNET port)

610

Set Static IP Address (INTERNET port)

111

Enter the IP address by using numbers on the telephone key pad. Use the * (star) key to a decimal point.

This option is available only after you choose Static IP as the Internet Connection Type, through option 101.

Set Static IPv6 Address (INTERNET port)

611

Available only in static IPv6 mode

Check Network Mask

120

Check IPv6 Prefix length

620

Set Network Mask

121

To enter the value, press numbers on the telephone key pad. Press the * (star) key to enter a decimal point.

This option is available only after you choose Static IP as the Internet Connection Type, through option 101.

Set Static IPv6 Prefix length

621

Available only in static IPv6 mode

Check Gateway IP Address

130

Check Gateway IPv6 Address

630

Set Gateway IP Address

131

To enter the value, press numbers on the telephone key pad. Press the * (star) key to enter a decimal point.

This option is available only after you choose Static IP as the Internet Connection Type, through option 101.

Set Gateway IPv6 Address

631

Available only in static IPv6 mode

Check MAC Address

140

Check Firmware Version

150

Check Primary DNS Server Setting

160

Check Primary IPv6 DNS Server Setting

660

Set Primary DNS Server

161

To enter the value, press numbers on the telephone key pad. Press the * (star) key to enter a decimal point.

This option is available only after you choose Static IP as the Internet Connection Type, through option 101.

Set Primary IPv6 DNS Server

661

Check INTRNET web server port

170

ATA 192 only: Check LAN IP address (ETHERNET port)

210

Announce Line 1 SIP Transport

1910

Set Line 1 SIP Transport

1911

0 —UDP

1 —TCP

2 —TLS

Check Line 2 SIP Transport

1920

Set Line 2 SIP Transport

1921

0 —UDP

1 —TCP

2 —TLS

Exit IVR

3948

(Spells EXIT on the phone keypad)

Reboot of Voice System

732668

(Spells REBOOT on the phone keypad)

After you hear “Option successful,” hang up the phone. The ATA reboots.

This action is equivalent to Pressing and immediately releasing the RESET button.

Factory Reset of Unit

Warning

All non-default settings will be lost. This includes network and service provider data.

73738

(Spells RESET on the phone keypad)

When prompted, press 1 to confirm, or press * (star) to cancel. After you hear “Option successful,” hang up the phone. The ATA reboots.

This action is equivalent to Pressing and holding the RESET button for 10 seconds.

User Factory Reset of Unit

Warning

All user-changeable non-default settings will be lost. This may include network and service provider data.

877778

When prompted, press 1 to confirm, or press * (star) to cancel. After you hear “Option successful,” hang up the phone. The ATA reboots.

| Step 1 | Connect an analog phone to a PHONE port of the ATA. |
|---|---|
| Step 2 | Press the star (*) key four times: **** |
| Step 3 | When challenged for a password: Log in as an administrator. Log in as the PHONE port's user. |
| Step 4 | Enter the code for the desired action. |

| IVR Action | Menu Option | Choices and Instructions |
|---|---|---|
| Enter IVR Menu | **** |  |
| Check Internet Addressing Method | 100 |  |
| Check Internet6 Addressing Method | 600 |  |
| Set Internet Addressing Method | 101 | 0 —DHCP 1 —Static IP 2 —PPoE |
| Check Stack Mode | 102 | 0 —IPv4 1 —IPv6 2 —Dual |
| Set Stack Mode | 103 | 0 —IPv4 1 —IPv6 2 —Dual |
| Set Internet6 Addressing Method | 601 | 0 —DHCP 1 —Static IP 2 —PPPoE |
| Check IPv6 Auto Configuration | 607 | 0 —Disable 1 —Enable |
| Set IPv6 Auto Configuration | 606 | 0 —Disable 1 —Enable |
| Check Internet IP Address (INTERNET port) | 110 |  |
| Check Internet6 Address (INTERNET port) | 610 |  |
| Set Static IP Address (INTERNET port) | 111 | Enter the IP address by using numbers on the telephone key pad. Use the * (star) key to a decimal point. Note This option is available only after you choose Static IP as the Internet Connection Type, through option 101. | Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Set Static IPv6 Address (INTERNET port) | 611 | Available only in static IPv6 mode |
| Check Network Mask | 120 |  |
| Check IPv6 Prefix length | 620 |  |
| Set Network Mask | 121 | To enter the value, press numbers on the telephone key pad. Press the * (star) key to enter a decimal point. Note This option is available only after you choose Static IP as the Internet Connection Type, through option 101. | Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Set Static IPv6 Prefix length | 621 | Available only in static IPv6 mode |
| Check Gateway IP Address | 130 |  |
| Check Gateway IPv6 Address | 630 |  |
| Set Gateway IP Address | 131 | To enter the value, press numbers on the telephone key pad. Press the * (star) key to enter a decimal point. Note This option is available only after you choose Static IP as the Internet Connection Type, through option 101. | Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Set Gateway IPv6 Address | 631 | Available only in static IPv6 mode |
| Check MAC Address | 140 |  |
| Check Firmware Version | 150 |  |
| Check Primary DNS Server Setting | 160 |  |
| Check Primary IPv6 DNS Server Setting | 660 |  |
| Set Primary DNS Server | 161 | To enter the value, press numbers on the telephone key pad. Press the * (star) key to enter a decimal point. Note This option is available only after you choose Static IP as the Internet Connection Type, through option 101. | Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
| Set Primary IPv6 DNS Server | 661 |  |
| Check INTRNET web server port | 170 |  |
| ATA 192 only: Check LAN IP address (ETHERNET port) | 210 |  |
| Announce Line 1 SIP Transport | 1910 |  |
| Set Line 1 SIP Transport | 1911 | 0 —UDP 1 —TCP 2 —TLS |
| Check Line 2 SIP Transport | 1920 |  |
| Set Line 2 SIP Transport | 1921 | 0 —UDP 1 —TCP 2 —TLS |
| Exit IVR | 3948 (Spells EXIT on the phone keypad) |  |
| Reboot of Voice System | 732668 (Spells REBOOT on the phone keypad) | After you hear “Option successful,” hang up the phone. The ATA reboots. Note This action is equivalent to Pressing and immediately releasing the RESET button. | Note | This action is equivalent to Pressing and immediately releasing the RESET button. |
| Note | This action is equivalent to Pressing and immediately releasing the RESET button. |
| Factory Reset of Unit Warning All non-default settings will be lost. This includes network and service provider data. | Warning | All non-default settings will be lost. This includes network and service provider data. | 73738 (Spells RESET on the phone keypad) | When prompted, press 1 to confirm, or press * (star) to cancel. After you hear “Option successful,” hang up the phone. The ATA reboots. Note This action is equivalent to Pressing and holding the RESET button for 10 seconds. | Note | This action is equivalent to Pressing and holding the RESET button for 10 seconds. |
| Warning | All non-default settings will be lost. This includes network and service provider data. |
| Note | This action is equivalent to Pressing and holding the RESET button for 10 seconds. |
| User Factory Reset of Unit Warning All user-changeable non-default settings will be lost. This may include network and service provider data. | Warning | All user-changeable non-default settings will be lost. This may include network and service provider data. | 877778 | When prompted, press 1 to confirm, or press * (star) to cancel. After you hear “Option successful,” hang up the phone. The ATA reboots. |
| Warning | All user-changeable non-default settings will be lost. This may include network and service provider data. |

| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
|---|---|

| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
|---|---|

| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
|---|---|

| Note | This option is available only after you choose Static IP as the Internet Connection Type, through option 101. |
|---|---|

| Note | This action is equivalent to Pressing and immediately releasing the RESET button. |
|---|---|

| Warning | All non-default settings will be lost. This includes network and service provider data. |
|---|---|

| Note | This action is equivalent to Pressing and holding the RESET button for 10 seconds. |
|---|---|

| Warning | All user-changeable non-default settings will be lost. This may include network and service provider data. |
|---|---|