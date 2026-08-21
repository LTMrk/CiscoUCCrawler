---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-15ebec5758
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_0100.html
retrieved_at: 2026-08-21T14:04:45.509599+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Cisco Unified IP Phone Settings

## Chapter: Cisco Unified IP Phone Settings

# Cisco Unified IP Phone Settings

## Phone Settings Overview

The Cisco Unified IP Phone includes configurable network settings that you may need to modify before the phone can be used.
                           You can access, view, and change the network settings on the phone by accessing the Interactive Voice Response (IVR) tool.
                           Other configuration settings may be configured in Cisco Unified Communications Manager.

## Cisco Unified IP Phone Network Settings Setup

Before the Cisco Unified IP Phone can function, you must configure the network setting on the phone. You can review the configuration
                           of a phone by accessing IVR on the phone. When the phone is connected to a network with a DHCP server, you can use the DHCP
                           server to configure the network settings. You can also manually configure the phone by accessing the IVR.

### Phone Settings Options

The following table describes the options that
                                 		  can be configured on the IVR.

Option

Description

DHCP

Indicates whether the phone has DHCP enabled or disabled.

When DHCP is enabled, the DHCP server assigns to the phone an IP
                                             					 address, subnet mask, default router, and TFTP Server. When DHCP is disabled,
                                             					 the administrator must manually assign the IP address, subnet mask, default
                                             					 router, and TFTP server on the phone.

IP Address

Internet Protocol version 4 (IPv4) address of the phone.

If you assign an IP address with this option, you must also
                                             					 assign a subnet mask and default router. See the Subnet Mask and Default Router
                                             					 options in this table.

Subnet Mask

Subnet mask used by the phone.

Default Router 1

Default router used by the phone (Default Router 1).

TFTP Server

Primary Trivial File Transfer Protocol (TFTP) server used by
                                             					 the phone. If you are not using DHCP in your network or you want to change this
                                             					 server, you must assign the TFTP Server.

802.1 xSecurity

Indicates whether the phone has 802.1x security enabled or
                                             					 disabled.

DHCPv6

Dynamic Host Configuration Protocol (DHCP) automatically
                                             					 assigns IPv6 addresses to phones when you connect them to the network. Cisco
                                             					 Unified IP Phones enable DHCP by default.

IPv6 Default Router 1

Default IPv6  router used by the phone (Default Router 1).

IPv6 Address

IPv6 address of the phone. The IPv6 address is a 128 bit
                                             					 address.

IPv6 Prefix Length

Subnet prefix length used by the phone. The subnet
                                             					 prefix length is a decimal value from 1 to 128 that specifies the portion of the
                                             					 IPv6 address that comprises the subnet.

IPv6 TFTP Server

Indicates whether the phone uses  the IPv6 Trivial File
                                             					 Transfer Protocol (TFTP) server.

## Access Phone Configuration Settings

You can change the PIN of the IVR from the Common Phone
                              		  Profile page.

When there is no User ID or PIN associated with a phone, the phone
                                          			 uses a default PIN of 24726.

Step 1

Access the Cisco Unified Communications Manager administration.

Step 2

Navigate to Device > Device
                                             				  Settings > Common Phone Profile .

Step 3

Specify a PIN for the Local Phone Unlock PIN
                                       			 field in the Common Phone Profile Configuration window.

Step 4

Click Save .

### Access IVR and Set Up Phone Settings

To access the IVR and configure the  phone settings, follow
                                 		  these steps on the phone:

You can change the PIN by using the 
                                             			 Local Phone Unlock Password in the Common Phone Profile
                                             			 Configuration page of the Cisco Unified CM Administration web page.

Step 1

Go off-hook and press 
                                          			 star (*), pound (#), and 
                                          			 0 keys simultaneously. On the Cisco Unified
                                          			 IP Phone 6911, you can also access IVR by pressing the speaker button followed by the  *, #, and
                                          			 
                                          			 0 keys simultaneously.

The IVR prompts for a password.

The Cisco Unified IP Phone 6901 and 6911 supports alphanumeric characters (A-F), and
                                                         				  colon (:) in IPv6 settings.

Step 2

Enter the PIN using the keypad, followed by #.

You are at the IVR main configuration menu.

Step 3

Follow the voice prompts on the IVR. For more information on navigating the IVR, see IVR Configuration Menu .

Step 4

To return to the main configuration menu, press #.

Step 5

To exit the IVR, end the call.

#### IVR Configuration Menu

When you input information in response to IVR prompts, use the following list for special character input:

To enter a period (.) or colon (:) that separates octets in the IP Address, press star (*).

To enter the hexadecimal A, press the 2 key two times quickly.

To enter the hexadecimal B, press the 2 key three times quickly

To enter the hexadecimal C, press the 2 key four times quickly.

To enter the hexadecimal D, press the 3 key two times quickly.

To enter the hexadecimal E, press the 3 key three times quickly.

To enter the hexadecimal F, press the 3 key four times quickly.

To delete a character in an entry, press Redial.

The following table describes the options in the IVR
                                    		  Configuration menu.

Action

IVR Code

Navigating Notes

Review or Set Network Settings

1

If DHCP is enabled, the IVR announces each network parameter.

If DHCP is disabled, the IVR announces each network parameter,
                                                					 pausing between each parameter to allow you to enter a new value.

IVR announces the IP Address. To change the IP address for
                                                      						  the phone, use the keypad to enter a new IP address, followed by #. To
                                                      						  retain the current IP address, press #.

IVR announces the subnet mask. To change the subnet mask,
                                                      						  use the keypad to enter a new IP address, followed by #. To retain the
                                                      						  current subnet mask, press #.

IVR announces the default gateway. To change the default
                                                      						  gateway, use the keypad to enter a new IP address, followed by #. To retain
                                                      						  the current default gateway, press #.

Review or Set TFTP Server

2

IVR announces the current TFTP setting.

To change the TFTP server, use the keypad to enter a new
                                                					 address, followed by #. To retain the current TFTP server, press #.

To reset a manually-configured TFTP server to the DHCP-configured server, press *.

Enable or Disable DHCP

3

Press 3 to enable or disable DHCP.

Enable or Disable 802.1X

4

Press 4 to enable or disable 802.1X security.

Review or Set IPv6 Network Settings

5

If DHCPv6 is enabled, the IVR announces each network parameter
                                                					 sequentially: IPv6 address, IPv6 prefix length, IPv6 subnet mask, and IPv6
                                                					 default gateway.

If DHCPv6 is disabled, the IVR announces each network
                                                					 parameter, pausing between each parameter to allow you to enter a new value.

IVR announces the IPv6 Address. To change the IPv6 address
                                                      						  for the phone, use the keypad to enter a new IPv6 address, followed by #.
                                                      						  To retain the current IPv6 address, press #.

IVR announces the subnet mask. To change the subnet mask, 
                                                      						  use the keypad to enter a new IPv6 address, followed by #. To retain the
                                                      						  current subnet mask, press #.

IVR announces the default gateway. To change the default
                                                      						  gateway, use the keypad to enter a new IPv6 address, followed by #. To
                                                      						  retain the current default gateway, press #.

Review or Set Ipv6 TFTP Server

6

IVR announces the current IPv6 TFTP setting.

To change the IPv6 TFTP server, use the keypad to enter a new
                                                					 IPv6 address, followed by #. To retain the current IPv6 TFTP server, press
                                                					 #.

To reset a manually-configured IPv6 TFTP server to the IPv6 DHCP-configured server, press *.

Enable or Disable DHCPv6

7

Press 7 to enable or disable DHCPv6.

Reset to factory settings

0

All configuration settings change to the default factory
                                                            						settings and the phone resets. It takes some time for the phone to
                                                            						reregister. Select this option only when needed.

| Option | Description |
|---|---|
| DHCP | Indicates whether the phone has DHCP enabled or disabled. When DHCP is enabled, the DHCP server assigns to the phone an IP
                                             					 address, subnet mask, default router, and TFTP Server. When DHCP is disabled,
                                             					 the administrator must manually assign the IP address, subnet mask, default
                                             					 router, and TFTP server on the phone. |
| IP Address | Internet Protocol version 4 (IPv4) address of the phone. If you assign an IP address with this option, you must also
                                             					 assign a subnet mask and default router. See the Subnet Mask and Default Router
                                             					 options in this table. |
| Subnet Mask | Subnet mask used by the phone. |
| Default Router 1 | Default router used by the phone (Default Router 1). |
| TFTP Server | Primary Trivial File Transfer Protocol (TFTP) server used by
                                             					 the phone. If you are not using DHCP in your network or you want to change this
                                             					 server, you must assign the TFTP Server. |
| 802.1 xSecurity | Indicates whether the phone has 802.1x security enabled or
                                             					 disabled. |
| IPv6 Network
                                             					 Settings |
| DHCPv6 | Dynamic Host Configuration Protocol (DHCP) automatically
                                             					 assigns IPv6 addresses to phones when you connect them to the network. Cisco
                                             					 Unified IP Phones enable DHCP by default. |
| IPv6 Default Router 1 | Default IPv6  router used by the phone (Default Router 1). |
| IPv6 Address | IPv6 address of the phone. The IPv6 address is a 128 bit
                                             					 address. |
| IPv6 Prefix Length | Subnet prefix length used by the phone. The subnet
                                             					 prefix length is a decimal value from 1 to 128 that specifies the portion of the
                                             					 IPv6 address that comprises the subnet. |
| IPv6 TFTP Server | Indicates whether the phone uses  the IPv6 Trivial File
                                             					 Transfer Protocol (TFTP) server. |

| Note | When there is no User ID or PIN associated with a phone, the phone
                                          			 uses a default PIN of 24726. |
|---|---|

| Step 1 | Access the Cisco Unified Communications Manager administration. |
|---|---|
| Step 2 | Navigate to Device > Device
                                             				  Settings > Common Phone Profile . |
| Step 3 | Specify a PIN for the Local Phone Unlock PIN
                                       			 field in the Common Phone Profile Configuration window. |
| Step 4 | Click Save . |

| Note | You can change the PIN by using the 
                                             			 Local Phone Unlock Password in the Common Phone Profile
                                             			 Configuration page of the Cisco Unified CM Administration web page. |
|---|---|

| Step 1 | Go off-hook and press 
                                          			 star (*), pound (#), and 
                                          			 0 keys simultaneously. On the Cisco Unified
                                          			 IP Phone 6911, you can also access IVR by pressing the speaker button followed by the  *, #, and
                                          			 
                                          			 0 keys simultaneously. The IVR prompts for a password. Note The Cisco Unified IP Phone 6901 and 6911 supports alphanumeric characters (A-F), and
                                                         				  colon (:) in IPv6 settings. | Note | The Cisco Unified IP Phone 6901 and 6911 supports alphanumeric characters (A-F), and
                                                         				  colon (:) in IPv6 settings. |
|---|---|---|---|
| Note | The Cisco Unified IP Phone 6901 and 6911 supports alphanumeric characters (A-F), and
                                                         				  colon (:) in IPv6 settings. |
| Step 2 | Enter the PIN using the keypad, followed by #. You are at the IVR main configuration menu. |
| Step 3 | Follow the voice prompts on the IVR. For more information on navigating the IVR, see IVR Configuration Menu . |
| Step 4 | To return to the main configuration menu, press #. |
| Step 5 | To exit the IVR, end the call. |

| Note | The Cisco Unified IP Phone 6901 and 6911 supports alphanumeric characters (A-F), and
                                                         				  colon (:) in IPv6 settings. |
|---|---|

| Action | IVR Code | Navigating Notes |
|---|---|---|
| Review or Set Network Settings | 1 | If DHCP is enabled, the IVR announces each network parameter. If DHCP is disabled, the IVR announces each network parameter,
                                                					 pausing between each parameter to allow you to enter a new value. IVR announces the IP Address. To change the IP address for
                                                      						  the phone, use the keypad to enter a new IP address, followed by #. To
                                                      						  retain the current IP address, press #. IVR announces the subnet mask. To change the subnet mask,
                                                      						  use the keypad to enter a new IP address, followed by #. To retain the
                                                      						  current subnet mask, press #. IVR announces the default gateway. To change the default
                                                      						  gateway, use the keypad to enter a new IP address, followed by #. To retain
                                                      						  the current default gateway, press #. |
| Review or Set TFTP Server | 2 | IVR announces the current TFTP setting. To change the TFTP server, use the keypad to enter a new
                                                					 address, followed by #. To retain the current TFTP server, press #. To reset a manually-configured TFTP server to the DHCP-configured server, press *. |
| Enable or Disable DHCP | 3 | Press 3 to enable or disable DHCP. |
| Enable or Disable 802.1X | 4 | Press 4 to enable or disable 802.1X security. |
| Review or Set IPv6 Network Settings | 5 | If DHCPv6 is enabled, the IVR announces each network parameter
                                                					 sequentially: IPv6 address, IPv6 prefix length, IPv6 subnet mask, and IPv6
                                                					 default gateway. If DHCPv6 is disabled, the IVR announces each network
                                                					 parameter, pausing between each parameter to allow you to enter a new value. IVR announces the IPv6 Address. To change the IPv6 address
                                                      						  for the phone, use the keypad to enter a new IPv6 address, followed by #.
                                                      						  To retain the current IPv6 address, press #. IVR announces the subnet mask. To change the subnet mask, 
                                                      						  use the keypad to enter a new IPv6 address, followed by #. To retain the
                                                      						  current subnet mask, press #. IVR announces the default gateway. To change the default
                                                      						  gateway, use the keypad to enter a new IPv6 address, followed by #. To
                                                      						  retain the current default gateway, press #. |
| Review or Set Ipv6 TFTP Server | 6 | IVR announces the current IPv6 TFTP setting. To change the IPv6 TFTP server, use the keypad to enter a new
                                                					 IPv6 address, followed by #. To retain the current IPv6 TFTP server, press
                                                					 #. To reset a manually-configured IPv6 TFTP server to the IPv6 DHCP-configured server, press *. |
| Enable or Disable DHCPv6 | 7 | Press 7 to enable or disable DHCPv6. |
| Reset to factory settings | 0 | Note All configuration settings change to the default factory
                                                            						settings and the phone resets. It takes some time for the phone to
                                                            						reregister. Select this option only when needed. | Note | All configuration settings change to the default factory
                                                            						settings and the phone resets. It takes some time for the phone to
                                                            						reregister. Select this option only when needed. |
| Note | All configuration settings change to the default factory
                                                            						settings and the phone resets. It takes some time for the phone to
                                                            						reregister. Select this option only when needed. |

| Note | All configuration settings change to the default factory
                                                            						settings and the phone resets. It takes some time for the phone to
                                                            						reregister. Select this option only when needed. |
|---|---|