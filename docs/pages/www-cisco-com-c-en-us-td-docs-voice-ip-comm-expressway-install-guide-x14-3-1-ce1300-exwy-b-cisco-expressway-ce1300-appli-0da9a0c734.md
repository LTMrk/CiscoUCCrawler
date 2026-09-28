---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-3-1-ce1300-exwy-b-cisco-expressway-ce1300-appli-0da9a0c734
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-3-1/CE1300/exwy_b_cisco-expressway-ce1300-appliance-installation-guide-x1431/exwy_m_connect-to-expressway-console.html
retrieved_at: 2026-08-16T22:10:15.185611+00:00
---

Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

# Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

Updated: October 15, 2024

Chapter: Connect to Expressway Console

## Chapter: Connect to Expressway Console

# Connect to Expressway Console

Before you can use the Expressway, you need to configure some basic information by connecting to the Expressway console and
                        then completing the secure Install Wizard.

You can use either of these connection methods, as described below:

Direct cabled connection from a PC to the Cisco Expressway serial port.

Remote connection with the Cisco Integrated Management Controller (CIMC) tool using serial over LAN.

This chapter explains the following:

## Before You Begin

Connect an Ethernet LAN cable from the LAN1 port on the rear panel to your network.

Have the following information ready for when the Install Wizard runs:

IPv4 and/or IPv6 address, subnet mask and default gateway address for the Expressway. Consult your network administrator about
                                          which addresses to use. The Cisco Expressway must use a static IP address.

Suitable passwords for the predefined root and admin user accounts - use strong passwords for both accounts.

If you intend to use a CIMC connection these additional points apply:

You need an IP address for it, which can be static or DHCP-assigned.

You need a browser with the following minimum requirement: HTTP and HTTPS enabled

Caution

You cannot use a KVM or vKVM console for initial installation. This is because the secure Install Wizard is not exposed on the KVM console and does not show on the VGA output port. Hence
                                          the wizard will wait indefinitely for you to complete installation on the Expressway serial console. If you need to recover from this situation, connect to the serial console as described below and issue the Ctrl+D sequence to the console. The install wizard restarts so that you can continue.

## Connecting Using the Serial Port

Connect the supplied DB9-to-RJ-45 cable from your PC (DB9 end) to the serial port on the rear of the appliance (RJ-45 end).

To ensure compatibility, use the blue serial cable supplied in the accessory pack. This is a cross-over cable, with the following
                                    pin assignments:

Male RJ45 pin

Female DB9 pin

1

8

2

6

3 TXD

2

4 GND

5

5 GND

5

6 RXD

3

7

4

8

7

Start a terminal emulator program (for example PuTTY) on the PC and configure it to use the PC serial port as follows:

baud rate: 115200 bits per second

data bits: 8

parity: none

stop bits: 1

flow control (hardware and software): none

Once you are connected to the Expressway console, wait for the Install Wizard to appear and go to the next section Run the Install Wizard .

Close the terminal emulator session after use. An open session may cause issues during system restarts.

## Connecting Using CIMC Serial Over LAN

CIMC is the management interface for C-Series servers. It runs within the server to support remote administration, configuration,
                              and monitoring using web or SSH command line access. For detailed information, see the Cisco UCS C-Series Integrated Management Controller Configuration Guide on the CIMC Configuration Guides page.

### CIMC password requirements

The CIMC default password must be changed to a strong password, as described in this section. If you use DHCP addressing,
                              you do this when you first log into the CIMC web interface. If you use static IP addresses, you change the password during
                              the initial boot process.

CIMC passwords must contain characters from three of the following four categories:

English uppercase letters A through Z

English lowercase letters a through z

Digits 0 through 9

These non-alphabetic characters: ! @ # $ % ^ & * - _ = “

### Task 1: Configure the CIMC IP Address and Password (Once Only)

#### If you use DHCP addressing

Connect your network to the CIMC/dedicated management port (port 7 in Rear Panel Layout ).

Connect a USB keyboard and VGA monitor using one of the following methods:

If you ordered a KVM adapter (3-legged cable), connect it to the console port at the front of the CE1300 and connect the keyboard
                                             and monitor to the adapter.

If the appliance was ordered without a KVM adapter, connect the keyboard and monitor to the appropriate ports on the rear
                                             of the server.

Switch on the monitor.

Configure your DHCP server to deliver the correct address for the CIMC. For the MAC address, use the MGMT address on the pullout tab.

Switch on the CE1300.

Watch the boot process on the monitor.

During the initial Power On Self Test phase, you should see the CIMC address displayed in the bottom left of the screen.

CIMC is now enabled on this Expressway. You will be prompted to change the default CIMC password when you first log in to
                                                   the CIMC web interface.

Disconnect the peripherals and the adapter.

#### If you use Static addresses

Follow these steps if your deployment uses static IP addressing:

Connect your network to the CIMC/dedicated management port (port 7 in Rear Panel Layout ).

Connect a USB keyboard and VGA monitor using one of the following methods:

If you ordered a KVM adapter (3-legged cable), connect it to the console port at the front of the CE1300 and connect the keyboard
                                             and monitor to the adapter (see Front panel showing KVM connector ).

If the appliance was ordered without a KVM adapter, connect the keyboard and monitor to the appropriate ports on the rear
                                             of the server.

The KVM console is used to configure the CIMC, not to access Expressway.

Switch on the monitor.

Switch on the CE1300 appliance.

Watch the boot process on the monitor.

Press F8 to enter the CIMC configuration.

You are prompted to change the default CIMC password and configure the management interface IP address:

Set a strong password that matches the conditions in CIMC password requirements and press Enter .

At the password modified prompt, press Enter again to complete the password change.

Due to a known issue, the system fails to notify you if the new password does not match the password requirements . In this case, when you first try to access the CIMC web interface ( Task 2 ) you must use the supplied default CIMC password and will then be prompted to set a different, stronger, password before
                                                         you continue. (At that point the system will correctly prompt you if the password doesn't match the requirements.)

We recommend leaving the default NIC mode as Dedicated and the NIC redundancy settings as None .

Press F10 to save your changes and Esc to exit.

CIMC is now enabled on this Expressway.

Disconnect the peripherals and the adapter.

### Task 2: Run CIMC from a Remote Host and Enable Serial Over LAN (Once Only)

Step 1

In a web browser, go to the CIMC IP address you configured in the previous task. By default, the CIMC must be accessed by
                                          using https:// for security purposes, that is, enter https://x.x.x.x into your browser navigation bar, where x.x.x.x represents the IP address .

Step 2

Do one of the following:

If you use a static IP address, log in using the password you set in Task 1 .

If the new password you set in Task 1 was not strong enough, because of the known issue with the system failing to notify you at the time, you are now prompted
                                                               to enter the default password and then to set a different, strong, password before you can continue. The new password must match the conditions
                                                               in CIMC password requirements .

If you use DHCP, define a strong password to replace the supplied default. The new password must match the conditions in CIMC password requirements .

Step 3

Click the menu arrow in the top-left corner.

Step 4

Navigate to Compute > Remote Management > Serial over LAN

Step 5

In the Serial over LAN Properties , check Enabled and then click Save Changes . This step is necessary as serial over LAN is disabled by default.

### Task 3: Connect to the Expressway Console (Any Time You Need)

Step 1

In a terminal emulator, use SSH to connect to the CIMC IP address.

Step 2

Type the default username admin and your CIMC password, and press Enter .

Step 3

Type connect host and press Enter .

Step 4

You are now connected to the Expressway console using serial over LAN.

Wait for the Install Wizard to appear, and go to the section Run the Install Wizard

| Caution | You cannot use a KVM or vKVM console for initial installation. This is because the secure Install Wizard is not exposed on the KVM console and does not show on the VGA output port. Hence
                                          the wizard will wait indefinitely for you to complete installation on the Expressway serial console. If you need to recover from this situation, connect to the serial console as described below and issue the Ctrl+D sequence to the console. The install wizard restarts so that you can continue. |
|---|---|

| Male RJ45 pin | Female DB9 pin |
|---|---|
| 1 | 8 |
| 2 | 6 |
| 3 TXD | 2 |
| 4 GND | 5 |
| 5 GND | 5 |
| 6 RXD | 3 |
| 7 | 4 |
| 8 | 7 |

| Note | Close the terminal emulator session after use. An open session may cause issues during system restarts. |
|---|---|

| Note | CIMC is now enabled on this Expressway. You will be prompted to change the default CIMC password when you first log in to
                                                   the CIMC web interface. |
|---|---|

| Note | The KVM console is used to configure the CIMC, not to access Expressway. |
|---|---|

| Note | Due to a known issue, the system fails to notify you if the new password does not match the password requirements . In this case, when you first try to access the CIMC web interface ( Task 2 ) you must use the supplied default CIMC password and will then be prompted to set a different, stronger, password before
                                                         you continue. (At that point the system will correctly prompt you if the password doesn't match the requirements.) |
|---|---|

| Note | CIMC is now enabled on this Expressway. |
|---|---|

| Step 1 | In a web browser, go to the CIMC IP address you configured in the previous task. By default, the CIMC must be accessed by
                                          using https:// for security purposes, that is, enter https://x.x.x.x into your browser navigation bar, where x.x.x.x represents the IP address . |
|---|---|
| Step 2 | Do one of the following: If you use a static IP address, log in using the password you set in Task 1 . Note If the new password you set in Task 1 was not strong enough, because of the known issue with the system failing to notify you at the time, you are now prompted
                                                               to enter the default password and then to set a different, strong, password before you can continue. The new password must match the conditions
                                                               in CIMC password requirements . If you use DHCP, define a strong password to replace the supplied default. The new password must match the conditions in CIMC password requirements . | Note | If the new password you set in Task 1 was not strong enough, because of the known issue with the system failing to notify you at the time, you are now prompted
                                                               to enter the default password and then to set a different, strong, password before you can continue. The new password must match the conditions
                                                               in CIMC password requirements . |
| Note | If the new password you set in Task 1 was not strong enough, because of the known issue with the system failing to notify you at the time, you are now prompted
                                                               to enter the default password and then to set a different, strong, password before you can continue. The new password must match the conditions
                                                               in CIMC password requirements . |
| Step 3 | Click the menu arrow in the top-left corner. |
| Step 4 | Navigate to Compute > Remote Management > Serial over LAN |
| Step 5 | In the Serial over LAN Properties , check Enabled and then click Save Changes . This step is necessary as serial over LAN is disabled by default. |

| Note | If the new password you set in Task 1 was not strong enough, because of the known issue with the system failing to notify you at the time, you are now prompted
                                                               to enter the default password and then to set a different, strong, password before you can continue. The new password must match the conditions
                                                               in CIMC password requirements . |
|---|---|

| Step 1 | In a terminal emulator, use SSH to connect to the CIMC IP address. |
|---|---|
| Step 2 | Type the default username admin and your CIMC password, and press Enter . |
| Step 3 | Type connect host and press Enter . |
| Step 4 | You are now connected to the Expressway console using serial over LAN. Wait for the Install Wizard to appear, and go to the section Run the Install Wizard |