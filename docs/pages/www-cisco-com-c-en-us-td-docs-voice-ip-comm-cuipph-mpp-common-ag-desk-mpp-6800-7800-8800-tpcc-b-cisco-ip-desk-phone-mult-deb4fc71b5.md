---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-common-ag-desk-mpp-6800-7800-8800-tpcc-b-cisco-ip-desk-phone-mult-deb4fc71b5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/common/ag_desk_mpp_6800_7800_8800/tpcc_b_cisco-ip-desk-phone-multiplatform/tpcc_m_ip-phone-installation-mpp.html
retrieved_at: 2026-08-21T13:47:14.493954+00:00
---

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

# Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

Updated: November 19, 2025

Chapter: Cisco IP Phone Installation

## Chapter: Cisco IP Phone Installation

# Cisco IP Phone Installation

## Verify the Network Setup

For the phone to operate successfully as an endpoint in your network, your network must meet specific requirements.

Step 1

Configure a VoIP Network to meet the following requirements:

VoIP is configured on your routers and gateways.

Step 2

Set up the network to support one of the following:

DHCP support

Manual assignment of IP address, gateway, and subnet mask

## Install the Cisco IP Phone

After the phone connects
                              		  to the network, the phone startup process begins, and the phone registers with
                              		  Third-Party Call Control system. To finish installing the phone, configure the
                              		  network settings on the phone depending on whether you enable or disable DHCP
                              		  service.

If you
                              		  used autoregistration, you need to update the specific configuration
                              		  information for the phone such as associating the phone with a user, changing
                              		  the button table, or directory number.

Step 1

Choose the
                                       			 power source for the phone:

Power
                                                					 over Ethernet (PoE)

External
                                                					 power supply

Step 2

Connect the
                                       			 handset to the handset port.

The
                                          				wideband-capable handset is designed especially for use with a Cisco IP Phone.
                                          				The handset includes a light strip that indicates incoming calls and waiting
                                          				voice messages.

Step 3

Connect a headset to the headset port. You can add a headset
                                       			 later if you do not connect one now.

Step 4

Connect a wireless headset. You can add a wireless headset later
                                       			 if you do not want to connect one now. For more information, see your wireless
                                       			 headset documentation.

Step 5

Connect a
                                       			 straight-through Ethernet cable from the switch to the network port labeled
                                       			 10/100/1000 SW on the Cisco IP Phone.
                                       			 Each Cisco IP Phone ships with one Ethernet cable in the box.

Use Category 3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for 100Mbps connections; and Category 5e
                                          or 6 for 1000 Mbps connections. For more information, see Network and Computer Port Pinouts .

Step 6

Connect a straight-through Ethernet cable from another network
                                       			 device, such as a desktop computer, to the computer port on the Cisco IP Phone.
                                       			 You can connect another network device later if you do not connect one now.

Use Category 3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for 100Mbps connections; and Category 5e
                                          or 6 for 1000 Mbps connections. For more information, see Network and Computer Port Pinouts for guidelines.

Step 7

If the phone is on a desk, adjust the footstand. With a wall-mounted phone, you might need to adjust the handset rest to ensure
                                       that the receiver cannot slip out of the cradle.

Step 8

Monitor the
                                       			 phone startup process. This step verifies that the phone is configured
                                       			 properly.

Step 9

If you are
                                       			 configuring the network settings on the phone, you can set up an IP address for
                                       			 the phone by either using DHCP or manually entering an IP address.

See Configure the Network from the Phone .

Step 10

Upgrade the
                                       			 phone to the current firmware image.

Firmware
                                          				upgrades over the WLAN interface may take longer than upgrading over the wired
                                          				interface, depending on the quality and bandwidth of the wireless connection.
                                          				Some upgrades may take more than one hour.

Step 11

Make calls
                                       			 with the Cisco IP Phone to verify that the phone and features work correctly.

Step 12

Provide
                                       			 information to end users about how to use their phones and how to configure
                                       			 their phone options. This step ensures that users have adequate information to
                                       			 successfully use their Cisco IPPhones.

### Network and Computer Port Pinouts

Although both the network and computer (access) ports are used for network connectivity, they serve different purposes and
                                 have different port pinouts.

The network port is the 10/100/1000 SW port on the Cisco IP Phone.

The computer (access) port is the 10/100/1000 PC port on the Cisco IP Phone.

## Configure the Network from the Phone

The phone includes many configurable network settings that you may need to modify before it is functional for your users.
                              You can access these setting through the phone menus.

The Network configuration menu provides you with options to view and configure a variety of network settings.

You can configure settings that are display-only on the phone in your Third-Party Call Control system.

Step 1

Press Applications .

Step 2

Select Network configuration .

Step 3

Use the navigation arrows to select the desired menu and edit.

Step 4

To display a submenu, repeat step 3.

Step 5

To exit a menu, press .

Step 6

To exit a menu, press Back .

### Network Configuration Fields

Field

Field Type or Choices

Default

Description

Ethernet configuration

See the following Ethernet configuration submenu table.

IP mode

Dual mode

IPv4 only

IPv6 only

Dual mode

Select the Internet Protocol mode for which the phone operates.

In dual mode, the phone can have both IPv4 and IPv6 addresses.

Wi-Fi configuration

See Set Up a Wi-Fi Profile from the Phone

For Cisco IP Phone 8861 Multiplatform Phones only.

For Cisco IP Phone 6861 Multiplatform Phones only.

IPv4 address settings

DHCP

Static IP

Release DHCP IP

DHCP

See the IPv4 address submenu table in the following tables.

IPv6 address settings

DHCP

Static IP

DHCP

See the IPv6 address submenu table in the following tables.

DHCPv6 option to use

17, 160, 159

Indicates the order in which the phone uses the IPv6 addresses provided by DHCP server.

HTTP proxy settings

See the following HTTP proxy settings submenu table.

VPN settings

See the following VPN settings submenu table.

Web server

On

Off

On

Indicates whether the phone has web server enabled or disabled.

Field

Field Type

or Choices

Default

Description

802.1x authentication

Device authentication

Off

Enables or disables the 802.1x authentication. Valid options are:

On

Off

Transaction status

Disabled

Transaction status—Indicates different authentication status when you turn on 802.1x in the Device authentication field.

Connecting : Indicates that the authentication process is in progress.

Authenticated : Indicates that the phone is authenticated.

Disabled : Indicates that 802.1x authentication is disabled on the phone.

Protocol—Displays the protocol of the server.

User certificate type

Manufacturing installed

Choose the certificate for the 802.1X authentication during the initial enrollment and certificate renewal.

Manufacturing installed—The Manufacturing Installed Certificate (MIC) and Secure Unique Device Identifier (SUDI) is used.

Custom installed—The Custom Device Certificate (CDC) is used. This type of certificate can be installed either by manual uploading
                                                   on the phone web page or by installation from a Simple Certificate Enrollment Protocol (SCEP) server.

This parameter appears on the phone only when Device authentication is enabled.

Switch port config

Auto

10MB half

10MB full

100MB half

100MB full

1000 full

1000 full (except for 7811 and 7821)

Auto

Select speed and duplex of the network port.

If the phone is connected to a switch, configure the port on the switch to the same speed/duplex as the phone, or configure
                                             both to autonegotiate.

If you change the setting of this option, you must change the PC Port config option to the same setting.

PC port config

Auto

10MB half

10MB full

100 MB half

100MB full

100 half

1000 full (except for 6821)

1000 full (except for 7811 and 7821)

1000 full

Auto

Select Speed and duplex of the Computer (access) port.

If the phone is connected to a switch, configure the port on the switch to the same speed/duplex as the phone, or configure
                                             both to autonegotiate.

If you change the setting of this option, you must change the Switch Port config option to the same setting.

CDP

On

Off

On

Enable or disable Cisco Discovery Protocol (CDP).

CDP is a device-discovery protocol that runs on all Cisco manufactured equipment.

Using CDP, a device can advertise its existence to other devices and receive information about other devices in the network.

LLDP-MED

On

Off

On

Enable or disable LLDP-MED.

LLDP-MED enables the phone to advertise itself to devices that use the discovery protocol.

Startup delay

3 seconds

Set a value that causes a delay for the switch to get to the forwarding state before the phone sends out the first LLDP-MED
                                             packet. For configuration of some switches, you might need to increase this value to a higher value for LLDP-MED to work.
                                             Configuring a delay can be important for networks that use the Spanning Tree Protocol.

Default delay is 3 seconds.

VLAN

On

Off

Off

Enable or disable VLAN.

Permits you to enter a VLAN ID when you use VLAN without CDP or LLDP. When you use a VLAN with CDP or LLDP, that associated
                                             VLAN takes precedent over the VLAN ID you manually entered.

VLAN ID

1

Enter a VLAN ID for the IP phone when you use a VLAN without CDP (VLAN enabled and CDP disabled). Note that only voice packets
                                             are tagged with the VLAN ID. Do not use the 1 value for the VLAN ID. If VLAN ID is 1, you cannot tag voice packets with the
                                             VLAN ID.

PC port VLAN ID

1

Enter a value of the VLAN ID that is used to tag communications from the PC port on the phone.

The phone tags all the untagged frames coming from the PC (it does not tag any frames with an existing tag).

Valid values: 0 through 4095

Default: 0

PC port mirror

On

Off

Off

Adds the ability to port mirror on the PC port. When enabled, you can see the packets on the phone. Select On to enable PC port mirroring and select Off to disable it.

DHCP VLAN option

Enter a predefined DHCP VLAN option to learn the voice VLAN ID.

When you use a VLAN ID with CDP, LLDP, or manually select a VLAN ID, that VLAN ID takes precedent over the selected DHCP VLAN
                                             option.

Valid values are:

Null

128 to 149

151 to 158

161 to 254

Default value is null.

Cisco recommends that you use DHCP Option 132.

Field

Field Type

or Choices

Default

Description

Connection type

DHCP

Indicates whether the phone has DHCP enabled.

DNS1—Identifies the primary Domain Name System (DNS) server that the phone uses.

DNS2—Identifies the secondary Domain Name System (DNS) server that the phone uses.

DHCP address released—Releases the IP address that DHCP assigned. You can edit this field if DHCP is enabled. To remove the
                                                   phone from the VLAN and release the IP address for reassignment, set this field to Yes and press Set .

Static IP

When DHCP is disabled, you must set the Internet Protocol (IP) address of the phone.

Static IP address—Identifies the IP that you assign to the phone. The phone uses this IP address instead of acquiring an IP
                                                   from the DHCP server on the network.

Subnet Mask—Identifies the subnet mask used by the phone. When DHCP is disabled, you must set the subnet mask.

Gateway address—Identifies the default router used by the phone.

DNS1—Identifies the primary Domain Name System (DNS) server that the phone uses. When DHCP is disabled, you must set this
                                                   field manually.

DNS2—Identifies the primary Domain Name System (DNS) server that the phone uses. When DHCP is disabled, you must set this
                                                   field manually.

When you assign an IP address using this field, you must also assign a subnet mask and a gateway address. See the Subnet Mask
                                             and Default Router fields in this table.

Field

Field Type

or Choices

Default

Description

Connection type

DHCP

Indicates whether the phone has Dynamic Host Configuration Protocol (DHCP) enabled.

DNS1—Identifies the primary DNS server that the phone uses.

DNS2—Identifies the secondary DNS server that the phone uses.

Broadcast Echo—Identifies if the phone responses to multicast ICMPv6 message with destination address of ff02::1.

Auto config— Identifies if the phone uses automatic configuration for the address.

Static IP

When DHCP is disabled, you must set the Internet Protocol (IP) address of the phone and must set the values of the fields:

Static IP—Identifies the IP that you assign to the phone. The phone uses this IP address instead of acquiring an IP from the
                                                   DHCP server on the network.

Prefix length—Identifies how many bits of a Global Unicast IPv6 Address are there in the network part.

Gateway—Identifies the default router used by the phone.

Primary DNS—Identifies the primary DNS server that the phone uses. When DHCP is disabled, you must set this field manually.

Secondary DNS—Identifies the primary DNS server that the phone uses. When DHCP is disabled, you must set this field manually.

Broadcast Echo—Identifies if the phone responses to multicast ICMPv6 message with destination address of ff02::1.

Field

Field Type or Choices

Description

VPN server

Enter an IP address or FQDN of the VPN server that the phone uses for the VPN connection.

Username

Enter a VPN username to access the VPN server.

Password

Enter a valid password of the username to access the VPN server.

Tunnel group

Enter a VPN tunnel group for the VPN connection.

Connect to VPN on bootup

On

Off

Determines whether the phone connects to the VPN server automatically after the phone reboots.

Default value is Off

Enable VPN connection

On

Off

Enables or disables the VPN connection.

When you enable or disable the VPN connection, the phone reboots automatically.

Default value is Off

Field

Field Type or Choices

Description

Proxy mode

Auto

Auto discovery (WPAD)—Enables or disables the Web Proxy Auto-Discovery protocol to retrieve a Proxy Auto-Configuration (PAC)
                                             file. Valid options are:

On

Off

If the value is set to Off, you need to further set the following field:

PAC URL—Specifies the URL address for the PAC file that you want to retrieve. For example:

http://proxy.department.branch.example.com

The default value of Auto discovery (WPAD) is On.

Manual

Proxy host—Specifies an IP address or hostname of the proxy server for the phone. The scheme ( http:// or https:// ) is not required.

Proxy port—Specifies a port number of the proxy server.

Proxy authentication—Selects an option according to the actual situation of the proxy server. If the server requires authentication
                                                   credentials to grant access to the phone, then select On. Otherwise, select Off. Options are:

Off

On

If the value is set to On, you need to further set the following fields:

Username—Specifies the username of a credential user on the proxy server.

Password—Provides the specified user's password to pass the authentication of the proxy server.

The default value of Proxy authentication is Off.

Off

Disables the HTTP proxy feature on the phone.

### Text and Menu
                           	 Entry From the Phone

When you
                                 		  edit the value of an option setting, follow these guidelines:

Use the arrows on the navigation pad to highlight the field that
                                       				you wish to edit. Press Select in the navigation pad to activate the field.
                                       				After the field is activated, you can enter values.

Use the keys on the keypad to enter numbers and letters.

To enter letters by using the keypad, use a corresponding number
                                       				key. Press the key one or more times to display a particular letter. For
                                       				example, press the 2 key once for "a," twice
                                       				quickly for "b," and
                                       				three times quickly for "c." After
                                       				you pause, the cursor automatically advances to allow you to enter the next
                                       				letter.

Press the softkey if you make a mistake. This softkey
                                       				deletes the character to the left of the cursor.

Press Back before pressing Set to discard any changes that you made.

To enter a period (for example, in an IP address), press * on the keypad.

The Cisco IP
                                             			 Phone provides several methods to reset or restore option settings, if
                                             			 necessary.

## Set up wireless LAN from the phone

Only the Cisco IP Phone 6861 Multiplatform Phones support wireless LAN connections.

Ensure that the phone is not connected to Ethernet. It requires a separate power supply.

The Cisco IP Phone 6861 Wireless LAN Deployment Guide includes the following configuration information:

http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-6800-series/products-implementation-design-guides-list.html

The Cisco IP Phone 6861 Wireless LAN Deployment Guide includes the following configuration information:

Wireless network configuration

Wireless network configuration on the Cisco IP Phone

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration .

Step 3

Select Wi-Fi Type and press the Select button to choose from WLAN and WPS .

Step 4

In the Wi-Fi Profile screen, click Scan to get a list of available wireless networks (SSIDs).

You can also click Cancel to stop the scan process.

If your phone is associated with an SSID, the associated SSID appears at the top of scanned list with a check mark in front
                                          of it.

Step 5

Select an SSID when the scan is complete, and set up the fields for your phone to connect to that network as described in
                                       the following table.

Field

Field Type or Choices

Default

Description

Security mode

Auto

EAP-FAST

PEP-GCT

PEAP-MSCHAPV2

PSK

WEP

None

PSK

Allows you to select the type of authentication that the phone uses to access the WLAN.

The security mode depends on the settings on your access point.

Network name

Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

Password

WEP Key

Passphrase

Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected.

Password: Security mode is Auto.

Passphrase: Security mode is PSK.

WEP Key: Security mode is WEP.

Frequency band

Auto

2.4 GHz

5 GHz

Auto

Allows you to select the wireless signal standard that the WLAN uses.

### Scan list menus

Field

Field Type or Choices

Default

Description

Security mode

Auto

None

WEP

PSK

None

Allows you to select the type of authentication that the phone uses to access the WLAN.

User ID

Allows you to enter a user ID for the network profile.

Password

WEP Key

Passphrase

Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                          you have selected.

Password: Security mode is Auto.

Passphrase: Security mode is PSK.

WEP Key: Security mode is WEP.

802.11 mode

Auto

2.4 GHz

5 GHz

Auto

Allows you to select the wireless signal standard that is used in the WLAN.

### Wi-Fi other menu

Field

Field Type or Choices

Default

Description

Security mode

EAP-FAST

PEAP-GTC

PEAP (MSCHAPV2)

PSK

WEP

None

None

Allows you to select the type of authentication that the phone uses to access the WLAN.

Network name

Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

Password

Allows you to enter a password for the network profile.

802.11 mode

Auto

2.4 GHz

5 GHz

Auto

Allows you to select the wireless signal standard that is used in the WLAN.

### Turn the Wi-Fi On or Off from Your phone

You can enable or disable the wireless LAN of your phone from the Wi-Fi configuration menu. By default, the wireless LAN on your phone is enabled.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi .

Step 3

Press the Select button, to turn the Wi-Fi on or off. You can also press the Navigation cluster, left or right, to turn the Wi-Fi on or off.

Step 4

Press the Select button, to turn the Wi-Fi on or off.

Step 5

Press Set to save the changes.

### Turn the Wi-Fi On or Off from the Phone Web Page

You can enable or disable the wireless LAN of your phone from the phone web page. You turn on the Wi-Fi so that the phone
                                 connects to a wireless network automatically or manually. By default, the wireless LAN on your phone is enabled.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > System .

Step 2

On the phone web page, select User Login > Advanced > Voice > System .

Step 3

Set the Wi-Fi Settings fields as described in the Parameters for Wi-Fi Settings table.

Step 4

Go to the Wi-Fi Settings section and set the Phone-wifi-on field to Yes .

Step 5

Click Submit All Changes .

#### Parameters for Wi-Fi Settings

The following table defines the function and usage of each parameter in the Wi-Fi Settings section under the System tab in the phone web page. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                    code to configure a parameter.

Parameter

Description

Phone-wifi-on

Turns Wi-Fi on or off  on your phone.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to turn on the Wi-Fi or set to No to turn it off.

Default: Yes

Phone-wifi-type

Only supported by Cisco IP Phone 6861

Controls which method the phone will connect to a wireless network.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, select one of the methods:

WLAN : This option requires the user to enter the credentials on the phone to connect to a protected wireless network.

WPS : The user can connect the phone to a wireless network using either the WPS button on the access point or the PIN code.

Allowed values: WLAN|WPS

Default: WLAN

### Connect the Phone to a Wi-Fi Manually

When you set up a Wi-Fi profile, it provides you the options to connect the phone manually to a wireless network. You can
                                 establish the connection from the Wi-Fi profile screen or from the Setup Wi-Fi screen.

The top most Wi-Fi profile in the Wi-Fi profile screen gets connected automatically when the phone provisions.

#### Before you begin

Turn on the Wi-Fi of your phone.

Disconnect your phone with the wired network.

Turn on the Wi-Fi of your phone.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, do any of the actions to connect to Wi-Fi.

- Select any of the configured Wi-Fi profile and click Connect .

- Press Scan and select one wireless in the Connect to Wi-Fi screen. In the Setup Wi-Fi screen, enter values in the fields and press Connect .

See the Profile Parameter table in the Set Up a Wi-Fi Profile from the Phone for the field values.

You can also configure the Wi-Fi settings using the configuration file.

### View the Wi-Fi Status

You may experience issues related to Wi-Fi connection. You can gather information from the Wi-Fi status page to help your administrator troubleshoot.

You may experience issues related to Wi-Fi connection. You can gather information from the Wi-Fi status page to help you troubleshoot.

You can also view the status from the phone web page by selecting User Login > Advanced > Info > Status > System Information .

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi status .

You see the information:

Wi-Fi status : Displays if the Wi-Fi is connected or disconnected.

Network name : Indicates the name of the SSID.

Signal strength : Indicates strength of the network signal.

MAC address : Indicates MAC address of the phone.

AP MAC address : Indicates MAC address of the access point (SSID).

Channel : Indicated the channel on which the Wi-Fi network transmits and receives data.

Frequency : Indicates the wireless signal frequency band that is used in the Wireless LAN.

Security mode : Indicates the security mode that is set for the wireless LAN.

### View Wi-Fi Status Messages on the Phone

You can view messages about the Wi-Fi connection status of your phone. The messages can help you diagnose Wi-Fi connection
                                 problems. The messages contain:

connection time and MAC address of the AP

disconnection time and diagnostic code

connection failure time

time that weak signal of the AP continues over 12 seconds

the status of firmware memory when the free memory is less than 50K

the status of losing AP beacon when the phone can't receive signal from the AP

the status of no response for Wi-Fi authentication or association requests

the status of TX failure

the status of WPS connection failure

Step 1

Press Applications .

Step 2

Select Status > Wi-Fi messages .

Step 3

Use the outer ring of the navigation cluster to scroll through the messages.

Step 4

Press Details to view more details of the selected message.

Step 5

(Optional) Press Clear to delete all the messages.

## Verify Phone Startup

After the Cisco IP Phone has power connected to it,
                              		the phone automatically cycles through a startup diagnostic process.

Step 1

If you are using Power over Ethernet, plug the LAN cable into the Network port.

Step 2

If you are using the power cube, connect the cube to the phone and plug the cube into an electrical outlet.

The buttons flash amber and then
                                          			 green in sequence during the various stages of bootup as the phone checks the
                                          			 hardware.

If the phone completes these stages successfully, it has
                                          		started up properly.

## Disable or Enable DF Bit

### Before you begin

Step 1

Select Voice > System .

Step 2

In the Network Settings section, configure the parameter Disable DF .

If you set the Disable DF to Yes , the Don't Fragment (DF) bit is disabled. In this case, the network can fragment an IP packet. This is the default behaviour.

If you set the Disable DF to No , the Don't Fragment (DF) bit is enabled. In this case, the network can't fragment an IP packet. This setting doesn't allow
                                                fragmentation in cases where the receiving host doesn't have sufficient resources to reassemble internet fragments.

Step 3

Click Submit All Changes .

You can also configure the parameter in the phone configuration file (cfg.xml) with the following XML string:

```
<Disable_DF ua="na">Yes</Disable_DF>
```

Allowed values: Yes and No

Default: Yes

## Configure Internet Connection Type

You can choose how your phone receives an IP address. Set the connection type to one of the following:

Static IP—A static IP address for the phone.

Dynamic Host Configuration Protocol (DHCP)—Enables the phone to receive an IP address from the network DHCP server.

The Cisco IP phone typically operates in a network where a DHCP server assigns IP addresses to devices. Because IP addresses
                              are a limited resource, the DHCP server periodically renews the phone lease on the IP address. If a phone loses the IP address,
                              or if the IP address is assigned to another device on the network, the following occurs:

Communication between the SIP proxy and the phone is severed or degraded.

The DHCP Timeout on Renewal parameter causes the phone to request renewal of its IP address if the following occurs:

The phone doesn't receive an expected SIP response within programmable length of time after it sends a SIP command.

If the DHCP server returns the IP address that it originally assigned to the phone, the DHCP assignment is presumed to be
                              operating correctly. Otherwise, the phone resets to try to fix the issue.

### Before you begin

Access the Phone Web Interface .

Step 1

Select Voice > System .

Step 2

In the Internet Connection Type section, use the Connection Type drop-down list to choose the connection type:

Dynamic Host Configuration Protocol (DHCP)

Static IP

Step 3

In the IPv6 Settings section, use the Connection Type drop-down list to choose the connection type:

Dynamic Host Configuration Protocol (DHCP)

Static IP

Step 4

If you choose Static IP, configure these settings in the Static IP Settings section:

Static IP —Static IP address of the phone

NetMask —Netmask of the phone (IPv4, only)

Gateway —Gateway IP address

Step 5

Click Submit All Changes .

```
<Connection_Type ua="rw">DHCP</Connection_Type>
<!-- available options: DHCP|Static IP -->
<Static_IP ua="rw"/>
<NetMask ua="rw"/>
<Gateway ua="rw"/>
```

## Configure VLAN Settings

The software tags your phone voice packets with the VLAN ID when you use a virtual LAN (VLAN).

In the VLAN Settings section of the Voice > System window, you can configure the different settings:

LLDP-MED

Cisco Discovery Protocol (CDP)

Network Startup Delay

VLAN ID (manual)

DHCP VLAN Option

The multiplatform phones support these four methods to obtain VLAN ID information. The phone attempts to obtain the VLAN ID
                              information in this order:

LLDP-MED

Cisco Discovery Protocol (CDP)

VLAN ID (manual)

DHCP VLAN Option

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Disable CDP/LLDP and manual VLAN.

Step 1

Select Voice > System .

Step 2

In the VLAN Settings section, configure the parameters as defined in the VLAN Settings Parameters table.

Step 3

Click Submit All Changes .

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure  each parameter,
                                          see the syntax of the string in the VLAN Settings Parameters table.

### VLAN Settings Parameters

The following table defines the function and usage of each parameter in the VLAN Settings Parameters section under the System tab in the phone web page. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                 code to configure a parameter.

Parameter Name

Description and Default Value

Enable VLAN

Controls the VLAN feature.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to enable VLAN.

The default value is Yes .

VLAN ID

If you use a VLAN without CDP (VLAN enabled and CDP disabled), enter a VLAN ID for the IP phone. Note that only voice packets
                                             are tagged with the VLAN ID. Do not use 1 for the VLAN ID.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, enter an appropriate value.

Valid values: An integer ranging from 0 through 4095

Default: 1

Enable CDP

Enable CDP only if you are using a switch that has Cisco Discovery Protocol. CDP is negotiation based and determines which
                                             VLAN the IP phone resides in.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page: set to Yes to enable CDP.

Valid values: Yes/No

Default: Yes

Enable LLDP-MED

Choose Yes to enable LLDP-MED for the phone to advertise itself to devices that use that discovery protocol.

When the LLDP-MED feature is enabled, after the phone has initialized and Layer 2 connectivity is established, the phone sends
                                             out LLDP-MED PDU frames. If the phone receives no acknowledgment, the manually configured VLAN or default VLAN will be used
                                             if applicable. If the CDP is used concurrently, the waiting period of 6 seconds is used. The waiting period will increase
                                             the overall startup time for the phone.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to enable LLDP-MED.

Valid values: Yes/No

Default: Yes

Network Startup Delay

Setting this value causes a delay for the switch to get to the forwarding state before the phone will send out the first LLDP-MED
                                             packet. The default delay is 3 seconds. For configuration of some switches, you might need to increase this value to a higher
                                             value for LLDP-MED to work. Configuring a delay can be important for networks that use Spanning Tree Protocol.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, enter the delay in seconds.

Valid values: An integer ranging from 1 through 300

Default: 3

DHCP VLAN Option

A predefined DHCP VLAN option to learn the voice VLAN ID. You can use the feature only when no voice VLAN information is available
                                             by CDP/LLDP and manual VLAN methods. CDP/LLDP and manual VLAN are all disabled.

Set the value to Null to disable DHCP VLAN option.

Cisco recommends that you use DHCP Option 132.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page: specify the DHCP VLAN option.

## Set Up a Wi-Fi Profile from the Phone

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, move to a row in the list on which you want to set up the profile.

Step 4

Press the Select button.

You can also press Options and then select Edit .

Step 5

In the Edit profile screen, set the parameters as mentioned in the Profile Parameters table.

Parameter

Description

Security mode

Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are:

Auto

EAP-FAST

PEAP-GTC

PEAP-MSCHAPV2

PSK

WEP

None

Default: PSK

Network name

Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters.

Password

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters.

WEP key

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters.

Passphrase

Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK.

Frequency band

Allows you to select the wireless signal frequency band that is used in the WLAN. Options are:

Auto

2.4 GHz

5 GHz

Default: Auto

Step 6

Press Save .

## Set Up a Wi-Fi Profile

You can configure a Wi-Fi profile from the phone web page or from remote device profile resync and then associate the profile
                              to the available Wi-Fi networks. You can use this Wi-Fi profile to connect to a Wi-Fi. You can configure maximum of four profiles.

The profile contains the parameters required for phones to connect to the phone server with Wi-Fi. When you create and use
                                 a Wi-Fi profile, you or your users do not need to configure the wireless network for individual phones.

A Wi-Fi profile enables you to prevent or limit changes to the Wi-Fi configuration on the phone by the user.

We recommend that you use a secure profile with TFTP encryption enabled to protect keys and passwords when you use a Wi-Fi
                                 profile.

When you set up the phones to use EAP-FAST, PEAP-MSCHAPV, or PEAP-GTC authentication or security mode, your users need individual
                                 credentials to connect to an access point.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > System .

Step 2

On the phone web page, select User Login > Advanced > Voice > System .

Step 3

Set the Wi-Fi Profile fields as described in the following table.

Field

Field Type or Choices

Default

Description

Security mode

Auto

EAP-FAST

PEP-GCT

PEAP-MSCHAPV2

PSK

WEP

None

PSK

Allows you to select the type of authentication that the phone uses to access the WLAN.

The security mode depends on the settings on your access point.

Network name

Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

Password

WEP Key

Passphrase

Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected.

Password: Security mode is Auto.

Passphrase: Security mode is PSK.

WEP Key: Security mode is WEP.

Frequency band

Auto

2.4 GHz

5 GHz

Auto

Allows you to select the wireless signal standard that the WLAN uses.

Step 4

Set the Wi-Fi Profile fields as described in the Wi-Fi Profile (n) table.

Step 5

Set the Wi-Fi Profile fields with the information that your administrator provided.

Step 6

Click Submit All Changes .

If the phone has an active call, you can not save the changes.

### Wi-Fi Profile (n)

The following table defines the function and usage of each parameter in the Wi-Fi Profile(n) section under the System tab in the phone web page. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                 code to configure a parameter.

Parameter

Description

Network Name

Allows you to enter a name for the SSID that will display on the phone. Multiple profiles can have the same network name with
                                             different security mode.

In the phone configuration file with XML(cfg.xml) , enter a string in this format:

In the phone web page: , enter a name for the SSID.

Security Mode

Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                             you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                             this Wi-Fi network.

In the phone configuration file with XML(cfg.xml) , enter a string in this format:

In the phone web page: , select one of the methods.

Auto

EAP-FAST

PEAP-GTC

PEAP-MSCHAPV2

PSK

WEP

None

Default: PSK

Wi-Fi User ID

Allows you to enter a user ID for the network profile.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, or PEAP (MSCHAPV2). This is a mandatory
                                             field and it allows maximum length of 32 alphanumeric characters.

In the phone configuration file with XML(cfg.xml) , enter a string in this format:

In the phone web page: , enter a user ID for the network profile.

Wi-Fi Password

Allows you to enter the password for the specified Wi-Fi User ID.

In the phone configuration file with XML(cfg.xml) , enter a string in this format:

In the phone web page: , enter a password for the user ID that you have added.

WEP Key

Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                             is WEP.

In the phone configuration file with XML(cfg.xml) , enter a string in this format:

In the phone web page: , enter a password for the network profile that you have created.

PSK Passphrase

Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                             is PSK.

Frequency Band

Allows you to select the wireless signal frequency band that is the WLAN uses.

In the phone configuration file with XML(cfg.xml) , enter a string in this format:

In the phone web page: , select one of the options:

Auto

2.4 GHz

5 GHz

Default: Auto

## Delete a Wi-Fi Profile

You can remove a Wi-Fi profile from the list when the profile is no more required.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, select the Wi-Fi profile that you want to remove.

Step 4

Press Options .

Step 5

Select Delete and then confirm the deletion.

## Change the Order of a Wi-Fi Profile

You can determine the position of a Wi-Fi profile in the list. The Wi-Fi profile at the top of the list has the highest priority.
                              When the Wi-Fi is turned on, the phone uses the Wi-Fi profile on the top of the list to connect automatically to a wirless
                              network while provisioning.

Step 1

If you change the Wi-Fi profile order from the phone, follow these steps:

Press Applications .

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

In the Wi-Fi profile screen , select a Wi-Fi of which you want to change the order.

Press Options .

Select Move up or Move down to move the Wi-Fi profile one level up or one level down respectively in the list.

Step 2

If you change the Wi-Fi profile order from the phone web page, follow these steps:

On the phone web page, select User Login > Advanced > Voice > System .

Select Voice > System .

In the Wi-Fi Profile (n) section, set the Wi-Fi Profile Order field to the desired order.

Click Submit All Changes .

## Scan and Save a Wi-Fi Network

You can scan a Wi-Fi profile to get the list of available wireless networks (SSID). The security mode and the network name
                              have the same value of the scanned SSID. You can then edit the fields of any of the wireless networks. When you save the changes,
                              it saves as a Wi-Fi profile in the phone Wi-Fi profile list. You can then use this new Wi-Fi profile to connect the phone
                              to a wireless network.

When the security mode of a wireless network is None, PSK, and WEP, you can't modify the security mode. On the Security mode screen, you only see the security mode that is set for the network. For example, if the security mode of a network is PSK,
                                                you see only PSK in the Security mode screen.

When you scan a wireless network (SSID) which is the current connected wireless, you can't edit the Network name of this SSID.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, press Scan to get all available wireless networks.

Step 4

(Optional) In the Connect to Wi-Fi screen, press Scan again to rescan the list.

Step 5

Select a wireless and press Select or the Select button.

Step 6

In the Setup Wi-Fi screen, set the parameters as mentioned in the Profile Parameters table.

Parameter

Description

Security mode

Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are:

Auto

EAP-FAST

PEAP-GTC

PEAP-MSCHAPV2

PSK

WEP

None

Default: PSK

Network name

Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters.

Password

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters.

WEP key

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters.

Passphrase

Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK.

Frequency band

Allows you to select the wireless signal frequency band that is used in the WLAN. Options are:

Auto

2.4 GHz

5 GHz

Default: Auto

Step 7

Press Save .

## SIP Configuration

SIP settings for the Cisco IP Phone are configured for the phone in general and for the extensions.

### Configure the Basic SIP Parameters

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the SIP Parameters section, set the parameters as described in the SIP Parameters table.

Step 3

Click Submit All Changes .

#### SIP Parameters

Parameter

Description

Max Forward

Specifies SIP Max Forward value.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Value range: 1 to 255

Default: 70

Max Redirection

Specifies number of times an invite can be redirected to avoid an infinite loop.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Default: 5

Max Auth

Specifies the maximum number of times (from 0 to 255) a request can be challenged.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Allowed value: 0 to 255

Default: 2

SIP User Agent Name

Used in outbound requests.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate name.

Default: $VERSION

If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed

SIP Server Name

Server header used in responses to inbound responses.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate name.

Default: $VERSION

SIP Reg User Agent Name

User-Agent name to be used in a REGISTER request. If this is not specified, the SIP User Agent Name is also used for the REGISTER
                                                request.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<SIP_Reg_User_Agent_Name ua="na">agent name</SIP_Reg_User_Agent_Name>
```

In the phone web page, enter an appropriate name.

Default: Blank

SIP Accept Language

Accept-Language header used.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate language.

There is no default. If empty, the header is not included.

DTMF Relay MIME Type

MIME Type used in a SIP INFO message to signal a DTMF event. This field must match that of the Service Provider.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate MIME type.

Default: application/dtmf-relay

Hook Flash MIME Type

MIME Type used in a SIPINFO message to signal a hook flash event.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate MIME type for a SIPINFO message.

Default:

Remove Last Reg

Enables you to remove the last registration before registering a new one if the value is different.

Set to Yes to remove the last registration.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, Select Yes or No.

Allowed values: Yes or No

Default: No

Use Compact Header

If set to yes, the phone uses compact SIP headers in outbound SIP messages. If inbound SIP requests contain normal headers,
                                                the phone substitutes incoming headers with compact headers. If set to no, the phones use normal SIP headers. If inbound SIP
                                                requests contain compact headers, the phones reuse the same compact headers when generating the response, regardless of this
                                                setting.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No.

Allowed values: Yes or No

Default: No

Talk Package

Enables support for the BroadSoft Talk Package that lets users answer or resume a call by clicking a button in an external
                                                application.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the Talk Package.

Allowed values: Yes or No

Default: No

Hold Package

Enables support for the BroadSoft Hold Package, which lets users place a call on hold by clicking a button in an external
                                                application.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable support for the Hold Package.

Allowed values: Yes or No

Default: No

Conference Package

Enables support for the BroadSoft Conference Package that enables users to start a conference call by clicking a button in
                                                an external application.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No.

Allowed values: Yes or No

Default: No

RFC 2543 Call Hold

If set to yes, unit includes c=0.0.0.0 syntax in SDP when sending a SIP re-INVITE to the peer to hold the call. If set to
                                                no, unit will not include the c=0.0.0.0 syntax in the SDP. The unit will always include a=sendonly syntax in the SDP in either
                                                case.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, Yes or No.

Allowed values: Yes or No

Default: Yes

SIP TCP Port Min

Specifies the lowest TCP port number that can be used for SIP sessions.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Default: 5060

SIP TCP Port Max

Specifies the highest TCP port number that can be used for SIP sessions.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Default: 5080

Caller ID Header

Provides the option to take the caller ID from PAID-RPID-FROM, PAID-FROM, RPID-PAID-FROM, RPID-FROM, or FROM header.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select an option.

Allowed values: PAID-RPID-FROM, AID-FROM, RPID-PAID-FROM, RPID-FROM, and FROM

Default: PAID-RPID-FROM

Dialog SDP Enable

When enabled and the Notify message body is too big causing fragmentation, the Notify message xml dialog is simplified; Session
                                                Description Protocol (SDP) is not included in the dialog xml content.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No .

Allowed values: Yes or No

Default: No

Keep Referee When Refer Failed

If set to yes, it configures the phone to immediately handle NOTIFY sipfrag messages.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No .

Allowed values: Yes or No

Default: No

Display Diversion Info

Display the Diversion info included in SIP message on LCD or not.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No .

Allowed values: Yes or No

Display Anonymous From Header

Show the caller ID from the SIP INVITE message “From” header when set to Yes, even if the call is an anonymous call. When
                                                the parameter is set to no, the phone displays "Anonymous Caller" as the caller ID.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No .

Allowed values: Yes or No

Default: No

Sip Accept Encoding

Supports the content-encoding gzip feature.

If gzip is selected, the SIP message header contains the string “Accept-Encoding: gzip”, and the phone is able to process
                                                the SIP message body, which is encoded with the gzip format.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate MIME type for a SIPINFO message.

Allowed values: none and gzip

Default: none

SIP IP Preference

Sets if the phone uses IPv4 or IPv6.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select IPv4 or IPv6.

Allowed values: IPv4/IPv6

Default: IPv4.

Disable Local Name To Header

Controls the display name in “Directory”, “Call History”, and in the “To” header during an outgoing call.

Perform one of the following.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to disable the display name.

Allowed values: Yes/No

Default: No

Forced NAT64

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes .

Allowed values: Yes/No

Default: No

### Configure the SIP Timer Values

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the SIP Timer Values section, set the SIP timer values in seconds as described in SIP Timer Values (sec) .

Step 3

Click Submit All Changes .

#### SIP Timer Values (sec)

Parameter

Description

SIP T1

RFC 3261 T1 value (RTT estimate) that can range from 0 to 64 seconds.

Default: 0.5 seconds

SIP T2

RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses) that can range from 0 to 64 seconds.

Default: 4 seconds

SIP T4

RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds.

Default: 5 seconds.

INVITE Expires

INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000.

Default: 240 seconds

ReINVITE Expires

ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to
                                                2000000.

Default: 30

Reg Retry Intv

Interval to wait before the Cisco IP Phone retries registration after failing during the last registration.The range is from
                                                1 to 2147483647

Default: 30

See the note below for additional details.

Reg Retry Long Intvl

When registration fails with a SIP response code that does not match<Retry Reg RSC>, the Cisco IP Phone waits for the specified
                                                length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg
                                                Retry Intvl value, which should not be 0.

Default: 1200

See the note below for additional details.

Reg Retry Random Delay

Random delay range (in seconds) to add to <Register Retry Intvl> when retrying REGISTER after a failure. Minimum and maximum
                                                random delay to be added to the short timer. The range is from 0 to 2147483647.

Default: 0

Reg Retry Long Random Delay

Random delay range (in seconds) to add to <Register Retry Long Intvl> when retrying REGISTER after a failure.

Default: 0

Reg Retry Intvl Cap

Maximum value of the exponential delay. The maximum value to cap the exponential backoff retry delay (which starts at the
                                                Register Retry Intvl and doubles every retry). Defaults to 0, which disables the exponential backoff (that is, the error retry
                                                interval is always at the Register Retry Intvl). When this feature is enabled, the Reg Retry Random Delay is added to the
                                                exponential backoff delay value. The range is from 0 to 2147483647.

Default: 0

Sub Retry Intvl

This value (in seconds) determines the retry interval when the last Subscribe request fails.

Default: 10.

The phone can use a RETRY-AFTER value when it is received from a SIP proxy server that is too busy to process a request (503
                                                Service Unavailable message). If the response message includes a RETRY-AFTER header, the phone waits for the specified length
                                                of time before to REGISTER again. If a RETRY-AFTER header is not present, the phone waits for the value specified in the Reg
                                                Retry Interval or the Reg Retry Long Interval.

### Configure the Response Status Code Handling

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the Response Status Code Handling section, set the values as specified in the Response Status Code Handling Paramters table.

Step 3

Click Submit All Changes .

#### Response Status Code Handling Paramters

The following table defines the function and usage of  the parameters in the Response Status Code Handling section under the
                                       SIP tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file
                                       with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Try Backup RSC

This parameter may be set to invoke failover upon receiving specified response codes.

For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6??

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Default: Blank

Retry Reg RSC

Interval to wait before the phone retries registration after failing during the last registration.

For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6??

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Default: Blank

### Configure NTP Server

You can configure NTP servers with IPv4 and IPv6. You can also configure NTP server with DHCPv4 option 42 or DHCPv6 option
                                 56. Configuring NTP with Primary NTP Server and Secondary NTP server parameters has higher priority over configuring NTP with
                                 DHCPv4 option 42 or DHCPv6 option 56.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Systems .

Step 2

In the Optional Network Configuration section, set the IPv4 or IPv6 address as described in the NTP Server Parameters table.

Step 3

Click Submit All Changes .

#### NTP Server Parameters

The following table defines the function and usage of NTP server parameters in the Optional Network Configuration section
                                       under the System tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration
                                       file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Primary NTP Server

IP address or name of the primary NTP server used to synchronize its time.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the IP address of the priamry NTP server.

Default: Blank

Secondary NTP Server

IP address or name of the secondary NTP server used to synchronize its time.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the IP address of the secondary NTP server.

Default: Blank

### Configure the RTP Parameters

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the RTP Parameters section, set the Real-Time Transport Protocol (RTP) parameter values as described in RTP Parameters .

Step 3

Click Submit All Changes .

#### RTP Parameters

The following table defines the function and usage of  the parameters in the RTP Parameters section under the SIP tab in the
                                       phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                       code to configure a parameter.

Parameter

Description

RTP Port Min

Minimum port number for RTP transmission and reception.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate port number.

Allowed values: 2048 to 49151

If the value range ( RTP Port Max - RTP Port Min ) is less than 16 or you configure the parameter incorrectly, the RTP port range (16382 to 32766) is used instead.

Default: 16384

RTP Port Max

Maximum port number for RTP transmission and reception.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate port number.

Allowed values: 2048 to 49151

If the value range ( RTP Port Max - RTP Port Min ) is less than 16 or you configure the parameter incorrectly, the RTP port range (16382 to 32766) is used instead.

Default: 16482

RTP Packet Size

Specifies packet size in seconds.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value to specify the packet size.

Allowed values: Ranges from 0.01 to 0.13. Valid values must be a multiple of 0.01 seconds.

Default: 0.02

Max RTP ICMP Err

Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the phone terminates the call. If
                                                value is set to 0, the phone ignores the limit on ICMP errors.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Default: 0

RTCP Tx Interval

Interval for sending out RTCP sender reports on an active connection.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Allowed values: 0 to 255 seconds

Default: 0

Call Statistics

Specifies whether the phone sends end-of-call statistics within SIP messages when a call terminates or is put on hold.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature.

Allowed values: Yes and No

Default: No

SDP IP Preferences

Select the preferred IP that the phone uses as RTP address.

If the phone is in dual-mode and has both ipv4 and ipv6 addresses, it will always include both addresses in SDP by attributes
                                                "a=altc …

If  IPv4 address is selected, then ipv4 address has higher priority than ipv6 address in SDP and indicates that phone prefers
                                                using ipv4 RTP address.

If the phone has only ipv4 address or ipv6 address,  SDP does not have ALTC attributes and RTP address is specified in “c=”
                                                line.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select the preferred IP .

Allowed values: IPv4 and IPv6

Default: IPv4

RTP Before ACK

Allows you to specify whether an RTP session starts before or after an ACK is received from the calling party.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page select:

Yes : An RTP session doesn't await an ACK, but starts after a 200 OK message is sent.

No : An RTP session doesn't start until an ACK is received from the calling party.

Allowed values: Yes and No

Default: No

SSRC Reset on Rx RE-INVITE

Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on incoming RE-INVITE.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page select:

Yes : the phone can avoid the call transfer error, where only one person on the call hears the audio. This occurs on calls of
                                                            30 minutes or longer, and often on three-way calls.

No :  the SSRC still remains during a long duration call. In this case, this error might occur.

Allowed values: Yes and No

Default: No

SSRC Reset on Tx RE-INVITE

Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on outgoing RE-INVITE.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page select:

Yes : the phone can avoid the one-way audio issue on a long duration call followed by a hold-resume action in certain Webex Calling
                                                            environments where the SRTP is end-to-end encrypted.

No : the SSRC still remains during a long duration call. In this case, this error might occur.

Allowed values: Yes and No

Default: No

#### Enable SSRC Reset for the New RTP and SRTP Sessions

You can enable SSRC Reset on Rx RE-INVITE to avoid a call transfer error, where only one person on the call hears the audio. This error occurs on calls of 30 minutes
                                    or longer, and often on three-way calls. Meanwhile, you can also enable SSRC Reset on Tx RE-INVITE to avoid the one-way audio issue on a long duration call followed by a hold-resume action in certain Webex Calling environments
                                    where the SRTP is end-to-end encrypted.

##### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the RTP Parameters section, set the parameter SSRC Reset on Rx RE-INVITE to Yes .

You can also configure this parameter in the configuration file:

```
<SSRC_Reset_on_Rx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Rx_RE-INVITE>
```

Allowed values: Yes and No.

Default: No

If you set the parameter to No , the SSRC remains for the new outgoing RTP and SRTP sessions (SIP re-INVITEs). The call transfer error might occur during
                                                            a long duration call.

Step 3

In the RTP Parameters section, set the parameter SSRC Reset on Tx RE-INVITE to Yes .

You can also configure this parameter in the configuration file:

```
<SSRC_Reset_on_Tx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Tx_RE-INVITE>
```

Allowed values: Yes and No.

Default: No

If you set the parameter to No , the SSRC remains for the outgoing RTP and SRTP sessions on outgoing SIP RE-INVITEs. The one-way audio might occur on a hold-resume
                                                            action on a long duration call.

Step 4

Click Submit All Changes .

### Control SIP and RTP Behaviour in Dual Mode

You can control SIP and RTP parameters with SIP IP Preference and SDP IP Preference fields when phone is in dual mode.

SIP IP Preference parameter defines which IP address phone tries first when it is in dual mode.

IP Mode

SIP IP Preference

Address List from DNS, Priority, Result

P1 - First Priority Address

P2 - Second Priority Address

Failover Sequence

Dual Mode

IPv4

P1- 1.1.1.1, 2009:1:1:1::1

P2 - 2.2.2.2, 2009:2:2:2::2

Result : Phone will send the SIP messages to 1.1.1.1 first.

1.1.1.1 ->2009:1:1:1:1 ->

2.2.2.2 -> 2009:2:2:2:2

Dual Mode

IPv6

P1- 1.1.1.1, 2009:1:1:1::1

P2 - 2.2.2.2, 2009:2:2:2::2

Result : Phone will send the SIP messages to 2009:1:1:1::1 first.

2009:1:1:1:1 ->

1.1.1.1 -> 2009:2:2:2:2 ->

2.2.2.2

Dual Mode

IPv4

P1- 2009:1:1:1::1

P2 - 2.2.2.2, 2009:2:2:2::2

Result : Phone will send the SIP messages to 2009:1:1:1::1 first.

2009:1:1:1:1 -> 2.2.2.2 -> 2009:2:2:2:2

Dual Mode

IPv6

P1- 2009:1:1:1::1

P2 - 2.2.2.2, 2009:2:2:2::2

Result : Phone will send the SIP messages to 1.1.1.1 first.

2009:1:1:1:1 -> 2009:2:2:2:2

->2.2.2.2

IPv4 Only

IPv4

or

IPv6

P1 - 1.1.1.1, 2009:1:1:1::1

P2 -  2.2.2.2, 2009:2:2:2::2

Result : Phone will send the SIP messages to 1.1.1.1 first.

1.1.1.1 -> 2.2.2.2

IPv6 Only

IPv4

or

IPv6

P1 - 1.1.1.1, 2009:1:1:1::1

P2 -  2.2.2.2, 2009:2:2:2::2

Result : Phone will send the SIP messages to 2009:1:1:1::1 first.

2009:1:1:1:1 ->  2009:2:2:2::2

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the SIP Parameters section, select IPv4 or IPv6 in the SIP IP Preference field.

For details, see SDP IP Preference field in the SIP Parameters table.

Step 3

In the RTP Parameters section, select IPv4 or IPv6 in the SDP IP Preference field.

For details, see SDP IP Preference in the RTP Parameters table.

### Configure RTP IP and SIP IP Alignment

You can configure the phone so that the RTP IP always aligns with SIP IP. SIP INVITE packet will fill the SDP IP with the
                                 phone's registration IP (the IP used by the phone for SIP communication), regardless of whether it's IPv4 or IPv6. When the
                                 auto selection is enabled, SIP INVITE packet fills the SDP IP with the phone's registration IP that the phone uses for SIP
                                 communication.

#### Before you begin

Phone onboards to Cisco Webex cloud successfully.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the RTP Parameters section, select Auto in the SDP IP Preference field.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<SDP_IP_Preference ua="na">Auto</SDP_IP_Preference>
```

Options: IPv4 | IPv6 | Auto

Default: IPv4

Step 3

Click Submit All Changes .

### Configure the SDP Payload Types

Your Cisco IP Phone supports RFC4733. You can choose from three audio-video transport (AVT) options to send DTMF pulses to
                                 the server.

Configured dynamic payloads are used for outbound calls only when the Cisco IP Phone presents a Session Description Protocol
                                 (SDP) offer. For inbound calls with an SDP offer, the phone follows the caller’s assigned dynamic payload type.

The Cisco IP Phone uses the configured codec names in outbound SDP. For incoming SDP with standard payload types of 0-95,
                                 the phone ignores the codec names. For dynamic payload types, the phone identifies the codec by the configured codec names.
                                 The comparison is case-sensitive, so you need to set the name correctly.

You can also configure the parameters in the phone configuration file (cfg.xml). To configure each of the parameters, see
                                 the syntax of the string in SDP Payload Types .

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the SDP Payload Types section, set the value as specified in SDP Payload Types .

AVT Dynamic Payload —is any nonstandard data. Both sender and receiver must agree on a number. The range is from 96 to 127. The default is 101.

AVT 16kHz Dynamic Payload —is any nonstandard data. Both sender and receiver must agree on a number. The range is from 96 to 127. The default is 107.

AVT 48kHz Dynamic Payload —is any nonstandard data. Both sender and receiver must agree on a number. The range is from 96 to 127. The default is 108.

Step 3

Click Submit All Changes .

#### SDP Payload Types

Parameter

Description

G722.2 Dynamic Payload

G722 Dynamic Payload type.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Allowed values:

Default: 96

iLBC Dynamic Payload

iLBC Dynamic Payload type.

Default: 97

iSAC Dynamic Payload

iSAC Dynamic Payload type.

Default: 98

OPUS Dynamic Payload

OPUS Dynamic Payload type.

Default: 99

AVT Dynamic Payload

AVT dynamic payload type. Ranges from 96-127.

Default: 101

INFOREQ Dynamic Payload

INFOREQ Dynamic Payload type.

H264 BP0 Dynamic Payload

H264 BPO Dynamic Payload type.

Default: 110

H264 HP Dynamic Payload

H264 HP Dynamic Payload type.

Default: 110

iSAC Codec Name

iSAC codec name used in SDP.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate codec name.

Allowed values:

Default: iSAC

AVT 16 kHz Dynamic Payload

AVT dynamic payload type for the 16 kHz clock rate.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the payload.

Range: 96-127

Default: 107

AVT 48 kHz Dynamic Payload

AVT dynamic payload type for the 48 kHz clock rate.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the payload.

Range: 96-127

Default: 108

### Configure the SIP Settings for Extensions

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) , where n is an extension number.

Step 2

In the SIP Settings section, set the parameter values as described in the Parameters for SIP Settings on Extensions table.

Step 3

Click Submit All Changes .

#### Parameters for SIP Settings on Extensions

The following table defines the function and usage of  the parameters in the SIP Settings section under the Ext(n) tab in
                                       the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                       code to configure a parameter.

Parameter

Description

SIP Transport

Specifies the transport protocol for SIP messages.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select the transport protocol type.

UDP

TCP

TLS

AUTO

AUTO allows the phone to select the appropriate protocol automatically, based on the NAPTR records on the DNS server. See Configure the SIP Transport for more details.

Default: UDP

SIP Port

The phone's port number for SIP message listening and transmission.

Specify the port number here only when you are using UDP as the SIP transport protocol.

If you are using TCP, the system uses a random port within the range specified in SIP TCP Port Min and SIP TCP Port Max on the Voice > SIP tab.

If you need to specify a port of SIP proxy server, you can specify it using the Proxy field  or the XSI Host Server field.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate port number.

Default: 5060

SIP 100REL Enable

Individually enables the SIP 100REL feature.

When enabled, the phone supports the 100REL SIP extension for reliable transmission of provisional responses (18x) and uses
                                                the PRACK requests.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the feature.

Allowed values: Yes and No

Default: No

Precondition Support

Determines whether the phone includes the precondition tag (defined in RFC 3312) in the Supported header field.

Disabled : The phone doesn't include the precondition tag in the Supported header filed. And the phone doesn't return the 183 response
                                                      when it receives the INVITE request that contains the QoS precondition in the SDP description.

Enabled : The phone includes the precondition tag in the Supported header field.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Enabled to enable the feature.

Allowed values: Disabled and Enabled

Default: Disabled

EXT SIP Port

The external SIP port number.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a port number.

Allowed values:

Default: 5060

Auth Resync-Reboot

The Cisco IP Phone authenticates the sender when it receives a NOTIFY message with the following requests:

resync

reboot

report

restart

XML-service

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the feature.

Allowed values: Yes and No

Default: Yes

SIP Proxy-Require

The SIP proxy can support a specific extension or behavior when it receives the Proxy-Require header from the user agent.
                                                If this field is configured and the proxy does not support it, it responds with the message, unsupported.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, enter the appropriate header in the field provided.

Default: Blank

SIP Remote-Party-ID

The Remote-Party-ID header to use instead of the From header. Select Yes to enable.

Default: Yes

Referor Bye Delay

Controls when the phone sends BYE to terminate stale call legs upon completion of call transfers. Multiple delay settings
                                                (Referor, Refer Target, Referee, and Refer-To Target) are configured on this screen.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the appropriate period of time in seconds.

Allowed values: An integer from 0 through 65535

Default: 4

Refer-To Target Contact

Indicates the refer-to target.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to send the SIP Refer to the contact.

Allowed values: Yes and No

Default: No

Referee Bye Delay

Specifies the Referee Bye Delay time in seconds.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the appropriate period of time in seconds.

Allowed values: An integer from 0 through 65535

Default: 0

Refer Target Bye Delay

Specifies the Refer Target Bye Delay time in seconds.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page,  enter the appropriate period of time in seconds.

Allowed values: An integer from 0 through 65535

Default: 0

Sticky 183

Controls the first 183 SIP response for an outbound INVITE. To enable this feature,

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page,  select Yes to enable this feature.

When enabled, the IP telephony ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                                      INVITE.

Allowed values: Yes and No

Default: No

Auth INVITE

Controls if authorization is required for initial incoming INVITE requests from the SIP proxy.  To enable this feature.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page,  select Yes to enable this feature.

When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy.

Allowed values: Yes and No

Default: No

Ntfy Refer On 1xx-To-Inv

If set to Yes , as a transferee, the phone will send a NOTIFY with Event:Refer to the transferor for any 1xx response returned by the transfer
                                                target, on the transfer call leg.

If set to No , the phone will only send a NOTIFY for final responses (200 and higher).

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page,  select Yes to enable this feature.

Allowed values: Yes and No

Default: Yes

Set G729 annexb

Configure G.729 Annex B settings.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page,  select Yes to enable this feature.

Allowed values:

None

No

Yes

Follow silence supp setting

Default: Yes

User Equal Phone

When a tel URL is converted to a SIP URL and the phone number is represented by the user portion of the URL, the SIP URL includes
                                                the optional: user=phone parameter (RFC3261). For example:

To: sip:+12325551234@example.com; user=phone

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature.

Allowed values: Yes and No

Default: No

Call Recording Protocol

Determines the type of recording protocol that the phone uses. Options are:

SIPINFO

SIPREC

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select a protocol from the list.

Allowed values: SIPREC|SIPINFO

Default: SIPREC

Privacy Header

Sets user privacy in the SIP message in the trusted network.

The privacy header options are:

Disabled (default)

none—The user requests that a privacy service applies no privacy functions to this SIP message.

header—The user needs a privacy service to obscure headers which cannot be purged of identifying information.

session—The user requests that a privacy service provide anonymity for the sessions.

user—The user requests a privacy level only by intermediaries.

id—The user requests that the system substitute an id that doesn't reveal the IP address or host name.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select an option from the list.

Allowed values: Disabled|none|header|session|user|id

Default: Disabled

P-Early-Media Support

Controls whether the P-Early-Media header is included in the SIP message for an outgoing call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, to include the P-Early-Media header, select Yes .

Allowed values: Yes and No

Default: No

### Configure the SIP Proxy Server

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) , where n is an extension number.

Step 2

In the Proxy and Registration section, set the parameter values as described in the SIP Proxy and Registration for Extension Parameters table.

Step 3

Click Submit All Changes .

#### SIP Proxy and Registration for Extension Parameters

The following table defines the function and usage of  the parameters in the Proxy and Registration section under the Ext(n)
                                       tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with
                                       XML(cfg.xml) code to configure a parameter.

Parameter

Description

Proxy

SIP proxy server and port number set by the service provider for all outbound requests. For example: 192.168.2.100:6060.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

<RTP_Port_Max ua="na">16482</RTP_Port_Max>

In the phone web page, enter SIP proxy server and port number.

When you need to refer to this proxy in another setting, for example, the speed dial line key configuration, use the $PROXY macro variable.

Default: The port number is optional. If you don't specify a port, the default port 5060 is used for UDP, and the default
                                                port 5061 is used for TLS.

Outbound Proxy

Specifies an IP address or domain name. All outbound requests are sent as the first hop.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an IP address and a domain name.

Default: Empty

Proxy

Outbound Proxy

For Survivable Remote Site Telephony (SRST) support

These parameters can be configured with an extension that includes a statically-configured DNS SRV record or DNS A record.
                                                This allows for failover and fallback functionality with a secondary proxy server.

The format for the parameter value is as follows:

Where:

host-list: srv[|srv[|srv...]]

srv: hostname[:port][:p=priority][:weight][:A=ip-list]

ip-list: ip-addr[,ip-addr[,ip-addr...]]

Default:

Priority is 0.

Weight is 1.

Port is 5060 and 5061 for UDP and TLS respectively.

Alternate Proxy

Alternate Outbound Proxy

This feature provides fast fall back when there is network partition at the Internet or when the primary proxy (or primary
                                                outbound proxy) is not responsive or available. The feature works well in a Verizon deployment environment as the alternate
                                                proxy is the Integrated Service Router (ISR) with analog outbound phone connection.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the proxy server addresses and port numbers in these fields.

After the phone is registered to the primary proxy and the alternate proxy (or primary outbound proxy and alternate outbound
                                                proxy), the phone always sends out INVITE and Non-INVITE SIP messages (except registration) via the primary proxy. The phone
                                                always registers to both the primary and alternate proxies. If there is no response from the primary proxy after timeout (per
                                                the SIP RFC spec) for a new INVITE, the phone attempts to connect with the alternate proxy. The phone always tries the primary
                                                proxy first, and immediately tries the alternate proxy if the primary is unreachable.

Active transactions (calls) never fall back between the primary and alternate proxies. If there is fall back for a new INVITE,
                                                the subscribe/notify transaction will fall back accordingly so that the phone's state can be maintained properly. You must
                                                also set Dual Registration in the Proxy and Registration section to Yes.

Default: Empty

Use OB Proxy In Dialog

Determines whether to force SIP requests to be sent to the outbound proxy within a dialog.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes or No . The request is ignored if the Use Outbound Proxy field is set to No or if the Outbound Proxy field is empty.

Valid values: Yes and No

Default: Yes

Register

Enables periodic registration with the proxy. This parameter is ignored if a proxy is not specified.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, To enable this feature, select Yes .

Valid values: Yes and No

Default: Yes

Make Call Without Reg

Enables making outbound calls without successful (dynamic) registration by the phone.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, To enable this feature, select Yes . If set to No , the dial tone plays only when registration is successful.

Valid values: Yes and No

Default: No

Register Expires

Defines how often the phone renews registration with the proxy. If the proxy responds to a REGISTER with a lower expires value,
                                                the phone renews registration based on that lower value instead of the configured value.

If registration fails with an “Expires too brief” error response, the phone retries with the value specified in the Min-Expires
                                                header of the error.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a value in seconds to define how often the phone renews registration with the proxy.

Valid values: Numeric. The range is from 32 seconds to 2000000 seconds.

Default: 3600 seconds

Ans Call Without Reg

If enabled, the user does not have to be registered with the proxy to answer calls.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, To enable this feature, select Yes .

Valid values: Yes and No

Default: No

Use DNS SRV

Enables DNS SRV lookup for the proxy and outbound proxy.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, To enable this feature, select Yes .

Valid values: Yes and No

Default: No

DNS SRV Auto Prefix

Enables the phone to automatically append a prefix to the proxy or outbound proxy name when performing a DNS SRV lookup on
                                                that name. The prefix to be appended varies with SIP transport protocols.

_sip._udp. for UDP protocol

_sip._tcp. for TCP protocol

_sips._tcp. for TLS protocol

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, to enable this feature, select Yes .

Valid values: Yes and No

Default: No

Proxy Fallback Intvl

Sets the delay after which the phone retries from the highest priority proxy (or outbound proxy) after it has failed over
                                                to a lower priority server.

The phone should have the primary and backup proxy server list from a DNS SRV record lookup on the server name. It needs to
                                                know the proxy priority; otherwise, it does not retry.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a value in seconds to set the duration in seconds after which the phone retries.

Valid values: Numeric. The range is from 0 seconds to 65535 seconds.

Default: 3600 seconds

Proxy Redundancy Method

The phone creates an internal list of proxies returned in the DNS SRV records.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Normal and Based on SRV Port .

If you set to Normal , the list contains proxies ranked by weight and priority.

If you set to Based on SRV Port , the phone uses normal, then inspects the port number based on the first-listed proxy port.

Valid values: Normal|Based on SRV Port

Default: Normal

Dual Registration

Controls both the dual registration and the fast fall back feature.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes to enable the Dual registration/Fast Fall back feature. To enable the feature you must also configure the alternate proxy/alternate
                                                      outbound proxy fields in the Proxy and Registration section.

Valid values: Yes and No

Default: No

Auto Register When Failover

Controls the fallback duration.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, If set to No, the fallback happens immediately and automatically. If the Proxy Fallback Intvl is exceeded,
                                                      all the new SIP messages go to the primary proxy.

If set to Yes, the fallback happens only when current registration expires, which means only a REGISTER message can trigger
                                                      fallback.

For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is
                                                triggered 3600 seconds later and not 600 seconds later. When the value for Register Expires is 600 seconds and Proxy Fallback
                                                Intvl is 1000 seconds, the fallback is triggered at 1200 seconds. After successfully registering back to primary server, all
                                                the SIP messages go to primary server.

Valid values: Yes and No

Default: Yes

TLS Name Validate

This field works only when SIP Transport is set to TLS for the phone line.

Specifies whether hostname verification is required when the phone line uses SIP over TLS. The options are:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes when hostname verification is required.

Select No to bypass the hostname verification.

Valid values: Yes and No

Default: Yes

### Add Outbound Proxy Survivability Support

You can configure a phone with the ability to register to the Site Survivability Gateway (SGW) nodes when WxC SSE nodes are
                                 unreachable.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) .

Step 2

In the Proxy and Registration section, set up Survivability Proxy and Survivability Proxy Fallback Intvl fields as described in Parameters for Outbound Proxy Survivability Support .

Step 3

Select Voice > System .

Step 4

In the System Configuration section, set up Survivability Test Mode field as described in Parameters for Outbound Proxy Survivability Support .

Step 5

Click Submit All Changes .

#### Parameters for Outbound Proxy Survivability Support

The following table defines the function and usage of WxC Outbound Proxy Survivability Support parameters in the Proxy and Registration section under the Ext(n) tab and the System Configuration section under the System tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with
                                    XML(cfg.xml) code to configure a parameter.

Parameter

Description

Survivability Proxy

The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform
                                                   a failover to a survivability gateway.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Survivability_Proxy_n_>hostname[:port][:A=ip-list] [| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_>
```

In the phone web interface, enter the proxy server address as follows:

Where: ip-list: ip-addr[,ip-addr[,ip-addr…]]

Default: port=0

Example: wxclsg.example.com:8933:A=192.169.10.1

where,

wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes.

8933=SGW port

192.169.10.1=Provisioned SGW address

Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other.

Allowed values: String

Default: Blank

Survivability Proxy Fallback Intvl

The interval in seconds after which the phone will attempt to fallback to the SSE nodes

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_>
```

in the phone web interface, specify the time interval in seconds.

Default: 30 secs

Survivability Test Mode

If set it to Yes, phone will always register to SGW nodes.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Survivability_Test_Mode>No</Survivability_Test_Mode>
```

in the phone web interface, select the test mode.

Options: Yes|No

Default: No

### Configure the Subscriber Information Parameters

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) , where n is an extension number.

Step 2

In the Subscriber Information section, set the parameter values as described in the Subscriber Information Parameters table.

Step 3

Click Submit All Changes .

#### Subscriber Information Parameters

The following table defines the function and usage of the parameters in the RTP Parameters section under the SIP tab in the
                                    phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml)
                                    code to configure a parameter.

Parameter

Description

Display Name

Name displayed as the caller ID.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a name that represents the caller ID.

User ID

Extension number for this line.

When you need to refer to this user ID in another setting, for example, the short name for a line key, use the $USER macro variable.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an extension number

Password

Password for this line.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a value to add password for the line.

Default: Blank (no password required)

Auth ID

Authentication ID for SIP authentication.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a value for an authentication ID.

Default: Blank

SIP URI

The parameter by which the user agent will identify itself for this line. If this field is blank, the actual URI used in the
                                             SIP signaling should be automatically formed as:

sip:UserName@Domain

where UserName is the username given for this line in the User ID, and Domain is the domain given for this profile in the
                                             User Agent Domain. If the User Agent Domain is an empty string, then the IP address of the phone should be used for the domain.

If the URI field is not empty, but if a SIP or SIPS URI contains no @ character, the actual URI used in the SIP signaling
                                             should be automatically formed by appending this parameter with an @ character followed by the IP address of the device.

### Set Up Your Phone to Use OPUS Codec Narrowband

#### Before you begin

Step 1

Select Voice > Ext <n> where (n) is the number of the extension to configure.

Step 2

In the SIP Settings section, set Use low-bandwidth OPUS to Yes .

Step 3

Click Submit All Changes .

## NAT Transversal with Phones

Network Address
                              Translation (NAT) allows multiple devices to share a single,
                              public, routable, IP address to establish connections over the
                              Internet. NAT is present in many broadband access devices to translate public and
                              private IP addresses. For VoIP to coexist with NAT, NAT traversal
                              is required.

Not all service providers provide NAT traversal. If your service provider does not provide NAT traversal, you have several
                              options:

NAT Mapping with Session Border Controller : We recommend that you choose an service provider that supports NAT mapping through a Session Border Controller. With NAT
                                    mapping provided by the service provider, you have more choices in selecting a router.

NAT Mapping with SIP-ALG Router : NAT mapping can be achieved by using a router that has a SIP Application Layer Gateway (ALG). By using a SIP-ALG router,
                                    you have more choices in selecting an service provider.

NAT Mapping with a Static IP Address : NAT mapping with an external (public) static IP address can be acheived to ensure interoperability with the service provider.
                                    The NAT mechanism used in the router must be symmetric. For more information, see Determine Symmetric or Asymmetric NAT .

Use NAT mapping only if the service provider network does not provide a Session Border Controller functionality. For more
                                    information on how to configure NAT mapping with a static IP, see Configure NAT Mapping with the Static IP Address .

NAT Mapping with STUN : If the service provider network does not provide a Session Border Controller functionality and if the other requirements
                                    are met, it is possible to use Session Traversal Utilities for NAT (STUN) to discover the NAT mapping. For information on
                                    how to configure NAT mapping with STUN, see Configure NAT mapping with STUN .

### Configure NAT Mapping with the Static IP Address

You can configure NAT mapping on the phone to ensure interoperability with the service provider.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

You must have an external (public) IP address that is static.

The NAT mechanism used in the router must be symmetric.

Step 1

Select Voice > SIP .

Step 2

In the NAT Support Parameters section, set the parameters as described in the NAT Mapping with Static IP Parameters table.

Step 3

Click the Ext(n) tab.

Step 4

In the NAT Settings section, set the parameters as described in the NAT Mapping from Ext Tab with Static IP Parameters table.

Step 5

Click Submit All Changes .

#### What to do next

Configure the firewall settings on your router to allow SIP traffic.

#### NAT Mapping with Static IP Parameters

The following table defines the function and usage of NAT mapping with Static IP parameters in the NAT Support Parameters
                                       section under the Voice>SIP tab in the phone web interface. It also defines the syntax of the string that is added in the
                                       phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Handle VIA received

Enables the phone to process the received parameter in the VIA header.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes .

Default: No

Handle VIA rport

Enables the phone to process the rport parameter in the VIA header.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes .

Default: No

Insert VIA received

Enables to insert the received parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes .

Default: No

Insert VIA rport

Enables to insert the rport parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes .

Default: No

Substitute VIA Addr

Enables the user to use NAT-mapped IP:port values in the VIA header.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes .

Default: No

Send Resp To Src Port

Enables to send responses to the request source port instead of the VIA sent-by port.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes .

Default: No

NAT Keep Alive Intvl

Interval between NAT-mapping keep alive messages.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an appropriate value.

Allowed values: Numeric ranges from 0 through 65535

Default: 15

EXT IP

External IP address to substitute for the actual IP address of phone in all outgoing SIP messages. If 0.0.0.0 is specified,
                                                no IP address substitution is performed.

If this parameter is specified, phone assumes this IP address when generating SIP messages and SDP (if NAT Mapping is enabled
                                                for that line).

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an external static IP address.

Default: Blank

The following table defines the function and usage of NAT mapping with Static IP parameters in the NAT Support Parameters
                                       section under the Voice>Ext tab in the phone web interface. It also defines the syntax of the string that is added in the
                                       phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

NAT Mapping Enable

Controls the use of externally mapped IP addresses and SIP/ RTP ports in SIP messages.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes to use externally mapped IP addresses.

Allowed values: Yes and No.

Default: No

NAT Keep Alive Enable

(Optional)

Configured NAT keep alive message periodically.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes to configure periodic NAT keep alive messages.

The service provider might require the phone to send NAT keep alive messages to keep the NAT ports open.

Check with your service provider to determine the requirements.

Allowed values: Yes and No.

Default: No

### Configure NAT mapping with STUN

The router must use asymmetric NAT. See Determine Symmetric or Asymmetric NAT .

A computer running
                                          STUN server software is available on the network. You can also use
                                          a public STUN server or set up your own STUN server.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > SIP .

Step 2

In the NAT Support Parameters section, set the Handle VIA received , Insert VIA received , Substitute VIA Addr , Handle VIA rport , Insert VIA rport , and Send Resp To Src Port parameters as described in the NAT Mapping with Static IP Parameters table.

Step 3

Set the parameters as described in the NAT Mapping with STUN Parameters table.

Step 4

Click the Ext(n) tab.

Step 5

In the NAT Settings section, set the parameters as described in the NAT Mapping from Ext Tab with Static IP Parameters table.

Step 6

Click Submit All Changes .

#### What to do next

Configure the firewall settings on your router to allow SIP traffic.

#### NAT Mapping with STUN Parameters

The following table defines the function and usage of NAT mapping with STUN parameters in the NAT Support Parameters section
                                       under the Voice>SIP tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration
                                       file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

STUN Enable

Enables the use of STUN to discover NAT mapping.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set to Yes to enable the feature.

Allowed values: Yes and No.

Default: No

STUN Server

IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery. You can use a public STUN
                                                server or set up your own STUN server.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter an IP address or fully-qualified domain name of the STUN server.

Allowed values:

Default: Blank

#### Determine Symmetric or Asymmetric NAT

STUN does not work
                                    on routers with symmetric NAT. With symmetric NAT, IP addresses are
                                    mapped from one internal IP address and port to one external, routable destination IP address and port. If another packet
                                    is sent
                                    from the same source IP address and port to a different
                                    destination, a different IP
                                    address and port number combination is used. This method is
                                    restrictive because an external host can send a packet to a
                                    particular port on the internal
                                    host only if the internal host first
                                    sent a packet from that port to the external host.

This procedure
                                    assumes that a syslog server is configured and is ready to receive
                                    syslog messages.

To Determine Whether
                                    the Router Uses Symmetric or Asymmetric NAT:

##### Before you begin

Verify that the firewall is not running on your PC. (It can block the syslog port.) By default, the syslog port is 514.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > System and navigate to Optional Network Configuration section.

Step 2

Enter the IP address for the Syslog Server , if the port number is anything
                                             other than the default, 514. It is not necessary to include the port number if it is the
                                             default.

The address and port
                                                number must be reachable from the Cisco IP phone. The port number
                                                appears on the output log file name. The default output
                                                file is syslog.514.log (if port
                                                number was not specified).

Step 3

Set the Debug Level to Error , Notice , or Debug .

Step 4

To capture SIP signaling messages, click the Ext tab and navigate to SIP Settings . Set the SIP Debug Option to Full .

Step 5

To collect information about what type of NAT your router uses
                                             click the SIP tab and navigate to NAT Support Parameters .

Step 6

Click Voice > SIP and navigate to NAT Support Parameters .

Step 7

Set STUN Test Enable to Yes .

Step 8

Determine the type of NAT by viewing the debug messages in the log
                                             file. If the messages indicate that the device is using symmetric
                                             NAT, you cannot use STUN.

Step 9

Click Submit All Changes .

## Configure Phone with DNS64/NAT64 Deployment

You can configure the phone to utilize DNS64 and NAT64 for IPv6 deployments. This configuration allows MPP phones to handle
                              IPv4 addresses and connect to IPv4-only services via NAT64.

For more information on SIP parameters, see SIP Parameters .

### Before you begin

Phone onboards to Cisco Webex cloud successfully.

Set up NAT64 gateway for IPv4 to IPv6 transitions and co-existence of IPv4 and IPv6.

SIP Application Layer Gateway (ALG) or Session Border Controller (SBC) that co-exist with NAT64 gateway to translate SIP at
                                    the application layer.

Set up DNS64 to handle IPv6 DNS queries from the phone.

Step 1

Select Voice > SIP .

Step 2

In the SIP Parameters section, select Yes in the Forced NAT64 field.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Forced_NAT64>Yes</Forced_NAT64>
```

Options: Yes and No

Default: No

Step 3

Click Submit All Changes .

## Dial Plan

### Dial Plan Overview

Dial plans determine how digits are interpreted and transmitted. They also determine whether the dialed number is accepted
                              or rejected. You can use a dial plan to facilitate dialing or to block certain types of calls such as long distance or international.

Use the phone web user interface to configure dial plans on the IP phone.

This section includes information that you must understand about dial plans, and procedures to configure your own dial plans.

The Cisco IP Phone has various levels of dial plans and processes the digits sequence.

When a user presses the speaker button on the phone, the following sequence of events begins:

The phone begins to collect the dialed digits. The interdigit timer starts to  track the time that elapses between digits.

If the interdigit timer value is reached, or if another terminating event occurs, the phone compares the dialed digits with
                                    the IP phone dial plan. This dial plan is configured in the phone web user interface in Voice > Ext(n) under the Dial Plan section.

#### Digit Sequences

A dial plan contains a series of digit sequences, separated by the | character. The entire collection of sequences is enclosed within parentheses. Each digit sequence within the dial plan consists
                                    of a series of elements that are individually matched to the keys that the user presses.

Dial plan is processed in conjunction with the Vertical Service Activation Codes (VSACs), hence, the digit analysis is done
                                    on both at the same time. Also, after a VSAC is processed, the dial plan rules then apply to the digits entered.

The minimum length specified in the dial plan and VSACs is not enforced, only the maximum length is enforced, which means
                                    the partial matches are processed and dialled out. For example,  if the dial plan is xxxx, then x, xx, xxx and xxxx are allowed.

White space is ignored, but can be used for readability.

Digit Sequence

Function

0 1 2 3 4 5 6 7 8 9 0 * #

Characters that represent a key that the user must press on the phone keypad.

x

Numeric digit 0 to 9 on the phone keypad.

[sequence]

Characters within square brackets create a list of accepted key presses. The user can press any one of the keys in the list.

A numeric range, for example, [2-9] allows a user to press any one digit from 2 through 9 .

A numeric range can include other characters. For example, [35-8*] allows a user to press 3, 5, 6, 7, 8, or *.

.  (period)

A period indicates element repetition. The dial plan accepts 0 or more entries of the digit. For example, 01. allows users to enter 0, 01, 011, 0111, and so forth.

<dialed:substituted>

This format indicates that certain dialed digits are replaced by the substituted characters when the sequence is transmitted. The dialed digits can be zero to 9. For example:

```
<8:1650>xxxxxxx
```

When the user presses 8 followed by a seven-digit number, the system automatically replaces the dialed 8 with the sequence 1650 . If the user dials 85550112 , the system transmits 16505550112 .

If the dialed parameter is empty and there is a value in the substituted field, no digits are replaced and the substituted value is always prepended to the transmitted string. For example:

```
<:1>xxxxxxxxxx
```

When the user dials 9725550112 , the number 1 is added at the beginning of the sequence; the system transmits 19725550112 .

,  (comma)

An intersequence tone played (and placed) between digits plays an outside line dial tone. For example:

```
9, 1xxxxxxxxxx
```

An outside line dial tone plays after the user presses 9 . The tone continues until the user presses 1 .

!  (exclamation point)

Prohibits a dial sequence pattern. For example:

```
1900xxxxxxx!
```

Rejects any 11-digit sequence that begins with 1900.

*xx

Allows a user to enter a 2-digit star code.

S0 or L0

For Interdigit Timer Master Override, enter S0 to reduce the short interdigit timer to 0 seconds, or enter L0 to reduce the long interdigit timer to 0 seconds.

P

To pause, enter P , the number of seconds to pause, and a space. This feature is typically used for implementation of a hotline and warm line,
                                                with a 0 delay for the hot line, and a nonzero delay for a warm line. For example:

```
P5
```

A pause of 5 seconds is introduced.

#### Digit Sequence Examples

The following examples show digit sequences that you can enter in a dial plan.

In a complete dial plan entry, sequences are separated by a pipe character (|), and the entire set of sequences is enclosed
                                    within parentheses:

For the Cisco IP Phone 6871 MPP Phones:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 
9, 011xxxxxx. | 0 | [49]11 ) | [*#]xx[*#] | #xx+xxxxxxxxxxx*xxxxxxxxxx
```

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 
9, 011xxxxxx. | 0 | [49]11 ) | [*#]xx[*#] | #xx+xxxxxxxxxxx*xxxxxxxxxx
```

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

[1-8]xx Allows a user to dial any three-digit number that starts with the digits 1 to 8. If your system uses four-digit extensions,
                                          enter the following string: [1-8]xxx

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]111)
```

9, xxxxxxx After a user presses 9, an external dial tone sounds. The user can enter any seven-digit number, as in a local call.

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

9, <:1>[2-9]xxxxxxxxx This example is useful where a local area code is required. After a user presses 9, an external dial tone sounds. The user
                                          must enter a 10-digit number that begins with a digit 2 through 9. The system automatically inserts the 1 prefix before it
                                          transmits the number to the carrier.

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

8, <:1212>xxxxxxx This example is useful where a local area code is required by the carrier but most calls go to one area code. After the user
                                          presses 8, an external dial tone sounds. The user can enter any seven-digit number. The system automatically inserts the 1
                                          prefix and the 212 area code before it transmits the number to the carrier.

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

9, 1 [2-9] xxxxxxxxx After the user presses 9, an external dial tone sounds. The user can enter any 11-digit number that starts with 1 and is
                                          followed by a digit 2 through 9.

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

9, 1 900 xxxxxxx ! This digit sequence is useful if you want to prevent users from dialing numbers that are associated with high tolls or inappropriate
                                          content, such as 1-900 numbers in the U.S. After the user presses 9, an external dial tone sounds. If the user enters an 11-digit
                                          number that starts with the digits 1900, the call is rejected.

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

9, 011xxxxxx After the user presses 9, an external dial tone sounds. The user can enter any number that starts with 011, as in an international
                                          call from the U.S.

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx | 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

0 | [49]11 This example includes two-digit sequences, separated by the pipe character. The first sequence allows a user to dial 0 for
                                          an operator. The second sequence allows the user to enter 411 for local information or 911 for emergency services.

Service activation codes (Cisco IP Phone 6871 only) :

[*#]xx[*#] Allows the user to dial # codes and * codes to access functions.

Service activation codes with additional parameters (Cisco IP Phone 6871 only) :

#xx+xxxxxxxxxxx*xxxxxxxxxx Allows the user to dial a # code, followed by two 10-digit numbers.

An executive assistant can use this pattern to initiate a call on behalf of an executive. The assistant dials the service
                                          activation code for call initiation, followed by the executive's number, then the number that he or she wants to call.

#### Acceptance and Transmission of the Dialed Digits

When a user dials a series of digits, each sequence in the dial plan is tested as a possible match. The matching sequences
                                    form a set of candidate digit sequences. As the user enters more digits, the set of candidates diminishes until only one or
                                    none is valid. When a terminating event occurs, the IP PBX either accepts the user-dialed sequence and initiates a call, or
                                    else rejects the sequence as invalid. The user hears the reorder (fast busy) tone if the dialed sequence is invalid.

The following table explains how terminating events are processed.

Terminating Event

Processing

Dialed digits have not matched any sequence in the dial plan.

The number is rejected.

Dialed digits exactly match one sequence in the dial plan.

If the dial plan allows the sequence, the number is accepted and is transmitted according to the dial plan.

If the dial plan blocks the sequence, the number is rejected.

A timeout occurs.

The number is rejected if the dialed digits are not matched to a digit sequence in the dial plan within the time that the
                                                applicable interdigit timer specifies.

The Interdigit Long Timer applies when the dialed digits do not match any digit sequence in the dial plan.

Default: 10 seconds.

The Interdigit Short Timer applies when the dialed digits match one or more candidate sequences in the dial plan. Default:
                                                3 seconds.

A user presses the # key or the dial softkey on the IP phone screen.

If the sequence is complete and is allowed by the dial plan, the number is accepted and is transmitted according to the dial
                                                plan.

If the sequence is incomplete or is blocked by the dial plan, the number is rejected.

#### Dial Plan Timer (Off-Hook Timer)

You can think of the Dial Plan Timer as the off-hook timer. This timer starts when the phone goes off hook. If no digits are
                                    dialed within the specified number of seconds, the timer expires and the null entry is evaluated. Unless you have a special
                                    dial plan string to allow a null entry, the call is rejected.

The timer before a number is dialed is whichever shorter of the dial plan default timer and the dial tone timer set in the Dial Tone field on the Regional tab.

##### Syntax for the Dial Plan Timer

SYNTAX: (P s <:n> | dial plan)

s: The number of seconds; The timer before a number is dialed is whichever shorter of the dial plan default timer and the dial
                                             tone timer set in the Dial Tone field. With the timer set to 0 seconds, the call transmits automatically to the specified extension when the phone goes off
                                             hook.

n: (optional): The number to transmit automatically when the timer expires; you can enter an extension number or a DID number.
                                             No wildcard characters are allowed because the number is transmitted as shown. If you omit the number substitution, <:n>,
                                             the user hears a reorder (fast busy) tone after the specified number of seconds.

##### Examples for the Dial Plan Timer

The actual timer before a number is dialed is whichever shorter of the dial plan default timer and the dial tone timer set
                                                   in the Dial Tone field. In the following examples, the dial tone timer is assumed to be longer than the dial plan timer.

Allow more time for users to start dialing after taking a phone off hook:

```
(P9 | (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

P9 means that after taking a phone off hook, a user has 9 seconds to begin dialing. If no digits are pressed within 9 seconds,
                                       the user hears a reorder (fast busy) tone. By setting a longer timer, you allow more time for users to enter digits.

To create a hotline for all sequences on the System Dial Plan:

```
(P9<:23> | (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

P9<:23> means that after taking the phone off hook, a user has 9 seconds to begin dialing. If no digits are pressed within
                                       9 seconds, the call is transmitted automatically to extension 23.

To create a hotline on a line button for an extension:

```
(P0 <:1000>)
```

With the timer set to 0 seconds, the call is transmitted automatically to the specified extension when the phone goes off
                                       hook. Enter this sequence in the Phone Dial Plan for Ext 2 or higher on a client phone.

#### Interdigit Long Timer (Incomplete Entry Timer)

You can think of this timer as the incomplete entry timer. This timer measures the interval between dialed digits. It applies
                                    as long as the dialed digits do not match any digit sequences in the dial plan. Unless the user enters another digit within
                                    the specified number of seconds, the entry is evaluated as incomplete, and the call is rejected. The default value is 10 seconds.

This section explains how to edit a timer as part of a dial plan. Alternatively, you can modify the Control Timer that controls
                                    the default interdigit timers for all calls.

##### Syntax for the Interdigit Long Timer

SYNTAX: L:s, (dial plan)

s: The number of seconds; if no number is entered after L:, the default timer is 5 seconds. With the timer set to 0 seconds,
                                             the call is transmitted automatically to the specified extension when the phone goes off hook.

Note that the timer sequence appears to the left of the initial parenthesis for the dial plan.

##### Example for the Interdigit Long Timer

```
L:15, (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

L:15 means that this dial plan allows the user to pause for up to 15 seconds between digits before the Interdigit Long Timer
                                       expires. This setting is especially helpful to users such as sales people, who are reading the numbers from business cards
                                       and other printed materials while dialing.

#### Interdigit Short Timer (Complete Entry Timer)

You can think of this timer as the complete entry timer. This timer measures the interval between dialed digits. The timer
                                    applies when the dialed digits match at least one digit sequence in the dial plan. Unless the user enters another digit within
                                    the specified number of seconds, the entry is evaluated. If the entry is valid, the call proceeds. If the entry is invalid,
                                    the call is rejected.

Default: 3 seconds.

##### Syntax for the Interdigit Short Timer

SYNTAX 1: S:s, (dial plan)

Use this syntax to apply the new setting to the entire dial plan within the parentheses.

SYNTAX 2: sequence Ss

Use this syntax to apply the new setting to a particular dialing sequence.

s: The number of seconds; if no number is entered after S, the default timer of 5 seconds applies.

##### Examples for the Interdigit Short Timer

To set the timer for the entire dial plan:

```
S:6, (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

S:6 means that while the user enters a number with the phone off hook, the user can pause for up to 15 seconds between digits
                                       before the Interdigit Short Timer expires. This setting is especially helpful to users such as sales people, who are reading
                                       the numbers from business cards and other printed materials while dialing.

Set an instant timer for a particular sequence within the dial plan:

```
(9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxxS0 | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

9,8,1[2-9]xxxxxxxxxS0 means that with the timer set to 0, the call is transmitted automatically when the user dials the final
                                       digit in the sequence.

### Edit the Dial Plan on the IP Phone

You can edit the dial plan in the XML configuration file. Locate the Dial_Plan_n_ parameter in the XML configuration file, where n denotes the extension number. Edit the value of this parameter. The value
                                             must be specified in the same format as in the Dial Plan field on the phone administration web page, described below.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) , where n is an extension number.

Step 2

Scroll to the Dial Plan section.

Step 3

Enter the digit sequences in the Dial Plan field.

The default (US-based) systemwide dial plan appears automatically in the field.

Step 4

You can delete digit sequences, add digit sequences, or replace the entire dial plan with a new dial plan.

Separate each digit sequence with a pipe character, and enclose the entire set of digit sequences within parentheses. Example:

(9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)

Step 5

Click Submit All Changes .

The phone reboots.

Step 6

Verify that you can successfully complete a call with each digit sequence that you entered in the dial plan.

If you hear a reorder (fast busy) tone, review your entries and modify the dial plan appropriately.

## Regional Parameters Configuration

### Regional Parameters

In the phone web user interface, use the Regional tab to configure regional and local settings, such as control timer values, dictionary server script, language selection,
                                 and locale to change localization. The Regional tab includes these sections:

Call Progress Tones—Displays values of all ringtones.

Distinctive Ring Patterns—Ring cadence defines the ringing pattern that announces a telephone call.

Control Timer Values—Displays all values in seconds.

Vertical Service Activation Codes (VSACs)—Includes Call Back Act Code and Call Back Deact Code. They are processed in conjunction
                                       with the dial plan rules, hence, the digit analysis is done on both at the same time. Also, after a VSAC is processed, the
                                       dial plan rules then apply to the digits entered.

The minimum length specified in the dial plan and VSACs is not enforced, only the maximum length is enforced, which means
                                       the partial matches are processed and dialled out. For example,  if the dial plan is xxxx, then x, xx, xxx and xxxx are allowed.

Outbound Call Codec Selection Codes—Defines the voice quality.

Time—Includes local date, local time, time zone, and Daylight Saving Time.

Language—Includes Dictionary Server Script, Language Selection, and Locale.

Localization—Includes Dictionary Server Script, Language Selection, and Locale.

### Set the Control Timer Values

If you need to edit a timer setting only for a particular digit sequence or type of call, you can edit the dial plan.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Regional .

Step 2

Set the Reorder Delay , Interdigit Long Timer , and Interdigit Short Timer parameters as described in the Control Timer Values (sec) table.

Step 3

Click Submit All Changes .

#### Parameters for Control Timer Values (sec)

### Localize Your Cisco IP Phone

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Regional .

Step 2

Configure the values in the fields in the Time and Language sections.

Step 3

Click Submit All Changes .

#### Configure Time and Date on Phone Web Page

##### Before you begin

Step 1

Select Voice > Regional .

Step 2

In the Time section, enter the time and date information.

Step 3

Select Voice > User .

Step 4

In the Supplementary Services , choose 12h or 24hr from the Time Format drop down list.

Default: 12hr

Step 5

Choose the date format from the Date Format drop down list.

Step 6

Click Submit All Changes

#### Configure Time and Date on the Phone

##### Before you begin

Step 1

Press Applications .

Step 2

Select Device administration > Date/Time .

Step 3

Select Set current time manually .

Step 4

Set the date and time in the format requested on the screen:

YYYY MM DD HH MM

Step 5

Select the OK softkey.

Step 6

Select the Save softkey.

#### Time and Date Settings

The Cisco IP Phone obtains the time settings in one of two ways:

NTP Server— NTP 24-hour time format takes priority over the time you set using the menu options on the phone or web page.

When the phone boots up, it tries to contact the first Network Time Protocol (NTP) server to get and update the time. The
                                          phone periodically synchronizes its time with the NTP server, and between updates, it tracks time with its internal clock.
                                          The synchronization period is fixed at 64 seconds .

If you manually enter a time, this setting takes effect for now, but on the next NTP synchronization, the NTP time is displayed.

Manual Setup—You can manually configure the local date and time by using one of the following methods:

On the phone web interface

On the phone itself

The default format is 12-hour which is overwritten with the 24-hour format as soon as the phone synchronizes with the NTP
                                          server.

Parameter

Description

Set Local Date (mm/dd/yyyy)

Sets the local date (mm represents the month and dd represents the day). The year is optional and uses two or four digits.

Default: Blank

Set Local Time (HH/mm)

Sets the local time (hh represents hours and mm represents minutes). Seconds are optional.

Default: Blank

Time Zone

Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…,
                                                GMT, GMT+01:00, GMT+02:00, …, GMT+13:00.

The time of the log messages and status messages are in UTC time and are not affected by the time zone setting.

Default: GMT-08:00

Time Offset (HH/mm)

This specifies the offset in 24-hour format from GMT to use for the local system time.

The NTP Server time is expressed in GMT time. The local time is obtained by offsetting the GMT according to the time zone
                                                of the region.

Default: 00/00

Ignore DHCP Time Offset

When used with some routers that have DHCP with time offset values configured, the IP phone uses the router settings and ignores
                                                the IP phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset
                                                settings, choose yes for this option. If you choose no , the IP phone uses the router's DHCP time offset value.

Default: Yes.

Daylight Saving Time Rule

Enter the rule for calculating daylight saving time. This rule is comprised of three fields. Each field is separated by a
                                                semicolon (;). Optional values inside brackets [ ] are assumed to be 0 if they are not specified. Midnight is represented
                                                by colons. For example,  0:0:0 of the given date.

This is the format of the rule: Start = <start-time>; end=<end-time>; save = <save-time>.

The <start-time> and <end-time> values specify the start and end dates and times of daylight saving time. Each value is in
                                                this format: <month> /<day> / <weekday>[/HH:[mm[:ss]]]

The <save-time> value is the number of hours, minutes, and/or seconds to add to the current time during daylight saving time.
                                                The <save-time> value can be preceded by a negative (-) sign if subtraction is desired instead of addition. The <save-time>
                                                value is in this format: [/[+|-]HH:[mm[:ss]]]

The <month> value equals any value in the range 1-12 (January-December).

The <day> value equals [+|-] any value in the range 1-31.

If <day> is -1, it means the <weekday> on or before the end of the month (in other words the last occurrence of < weekday>
                                                in that month).

Daylight Saving Time Rule (continued)

The <weekday> value equals any value in the range 1-7 (Monday-Sunday). It can also equal 0. If the <weekday> value is 0, this
                                                means that the date to start or end daylight saving is exactly the date given. In that case, the <day> value must not be negative.
                                                If the <weekday> value is not 0 and the <day> value is positive, then daylight saving starts or ends on the <weekday> value
                                                on or after the date given. If the <weekday> value is not 0 and the <day> value is negative, then daylight saving starts or
                                                ends on the <weekday> value on or before the date given. Where:

HH stands for hours (0-23).

mm stands for minutes (0-59).

ss stands for seconds (0-59).

Default: 3/-1/7/2;end=10/-1/7/2;save=1.

Daylight Saving Time Enable

Enables Daylight Saving Time.

Default: Yes

Time Format

Choose the time format for the phone (12-hour or 24-hour).

Default: 12hr

Date Format

Choose the date format for the phone (month/day or day/month).

Default: month/day

In the phone configuration XML file (cfg.xml), enter a string in this format:

#### Configure Daylight Saving Time

The phone supports automatic adjustment for daylight saving time.

The time of the log messages and status messages are in UTC time. The time zone setting does not affect them.

##### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Regional .

Step 2

Set the Daylight Saving Time Enable drop-down list box to Yes .

Step 3

In the Daylight Saving Time Rule field, enter the DST rule. This value affects the time stamp on the CallerID.

Step 4

Click Submit All Changes .

##### Daylight Saving Time Examples

The following example configures daylight saving time for the U.S, adding one hour starting at midnight on the second Sunday
                                       in March and ending at midnight on the first Sunday in November; add 1 hour (USA, North America):

```
start=3/8/7/02:0:0;end=11/1/7/02:0:0;save=1
```

The following example configures daylight saving time for Finland, starting at midnight on the last Sunday in March and ending
                                       at midnight on the last Sunday in October:

```
start=3/-1/7/03:0:0;end=10/-1/7/03:0:0;save=1 (Finland)
```

The following example configures daylight saving time for New Zealand (in version 7.5.1 and higher), starting at midnight
                                       on the last Sunday in September and ending at midnight on the first Sunday of April.

```
start=9/-1/7/02:0:0;end=4/1/7/02:0:0;save=1 (New Zealand)
```

The following example configures the daylight saving time starting on the last Monday (on or before April 8) and ending on
                                       the first Wednesday (on or after May 8).

```
start=4/-8/1;end=5/8/3;save=1
```

#### Phone Display Language

The Cisco IP Phone supports multiple languages for the phone display.

By default, the phone is set up for English. To enable the use of another language, you must set up the dictionary for the
                                 language. For some languages, you must also set up the font for the language.

After the setup is complete, you or your users can specify the desired language for the phone display.

##### Supported Languages for the Phone Display

On the phone administration web page, go to Admin Login > Advanced > Voice > Regional . In the Language section, click the Locale drop-down list box to see the supported languages for the phone display.

ar-SA (Arabic)

bg-BG (Bulgarian)

ca-ES (Catalan)

cs-CZ (Czech)

da-DK (Danish)

de-DE (German)

el-GR (Greek)

en-GB (English-Great Britain)

en-US (English-United States)

es-CO (Spanish-Colombia)

es-ES (Spanish-Spain)

fi-FI (Finnish)

fr-CA (French-Canada)

fr-FR (French)

he-IL (Hebrew)

hr-HR (Croatian)

hu-HU (Hungarian)

it-IT (Italian)

ja-JP (Japanese)

ko-KR (Korean)

nl-NL (Dutch)

nn-NO (Norwegian)

pl-PL (Polish)

pt-PT (Portuguese)

ru-RU (Russian)

sk-SK (Slovak)

sl-SI (Slovenian)

sv-SE (Swedish)

tr-TR (Turkish)

zh-CN (Chinese)

zh-HK (Chinese-Hong Kong SAR)

##### Set Up Dictionaries and Fonts

Languages other than English require dictionaries. Some languages also require a font.

To enable Latin and Cyrillic languages, you must not add a font file.

Step 1

Download the locale zip file for your firmware version, from cisco.com. Place the file on your server, and unzip the file.

Dictionaries and fonts for all the supported languages are included in the zip file. Dictionaries are XML scripts. Fonts are
                                                   standard TTF files.

Step 2

On the phone administration web page, go to Admin Login > Advanced > Voice > Regional . In the Language section, specify the necessary parameters and values in the Dictionary Server Script field as described below. Use a semicolon (;) to separate multiple parameter and value pairs.

Specify the location of the dictionary and font files with the serv parameter.

For example: serv=http://server.example.com/Locales/

Make sure to include the IP address of the server, the path, and folder name.

Example: serv=http://10.74.128.101/Locales/

For each language that you want to set up, specify a set of parameters as described below.

In these parameter specifications, n denotes a serial number. This number determines the sequential order in which the language options are displayed in the Settings menu of the phone.

0 is reserved for US-English, which has a default dictionary. You can use it optionally, to specify your own dictionary.

Use numbers starting with 1 for other languages.

Specify the language name with the d n parameter.

Example for language name for Asian language: d1=Chinese-Simplified

Example for language name for German (Latin and Cyrillic): d2=German

Example for language name for French (Latin and Cyrillic): d1=French

Example for language name for French (Canada) (Latin and Cyrillic) language: d1=French-Canada

Example for language name for Hebrew (RTL language): d1=Hebrew

Example for language name for Arabic (RTL language): d1=Arabic

This name is displayed as a language option in the Settings menu of the phone.

Specify the name of the dictionary file with the x n parameter.

Example for Asian language: x1=zh-CN_78xx_68xx-11.2.1.1004.xml;

x1=zh-CN_88xx-11.2.1.1004.xml;

Example for French (Latin and Cyrillic) languages: x1=fr-FR_78xx_68xx-11.2.1.1004.xml;

x1=fr-FR_88xx-11.2.1.1004.xml;

Example for Arabic (RTL language) language: x1=ar-SA_78xx_68xx-11.2.1.1004.xml;

x1=ar-SA_88xx-11.2.1.1004.xml;

Example for French (Canada) language: x1=fr-CA_78xx_68xx-11.3.6.0006.xml;

x1=fr-CA_88xx-11.3.6.0006.xml;

Ensure to specify the correct file for the language and phone model that you use.

If a font is required for the language, specify the name of the font file with the f n parameter.

For example: f1=zh-CN_78xx_68xx-11.2.1.1004.ttf;

f1=zh-CN_88xx-11.2.1.1004.ttf;

Make sure to specify the correct file for the language and phone model that you use.

Font files with 'BMP' in the file name are for the Cisco IP Phone 7811.

See Setup for Latin and Cyrillic Languages for specific details on setting up Latin languages.

See Setup for an Asian Language for specific details on setting up an Asian language.

See Setup for RTL Languages for specific details on setting up RTL languages.

Step 3

Click Submit All Changes .

##### Setup for Latin and Cyrillic Languages

If you use Latin and Cyrillic languages such as French or German, you can configure up to four language options for the phone.
                                       List of Latin and Cyrillic languages:

Bulgarian

Catalan

Croatian

Czech

Danish

Dutch

English (UK)

Finnish

French (France)

French (Canada)

German

Greek

Hungarian

Italian

Portuguese (Portugal)

Norwegian

Polish

Russian

Slovak

Slovenian

Spanish (Columbia)

Spanish (Spain)

Swedish

Turkish

Ukraine

To enable the options, set up a dictionary for each language that you want to include. To enable the language, specify a pair
                                       of d n and x n parameters and values in the Dictionary Server Script field, for each language that you want to include.

Example for including French and German:

```
serv=http://10.74.128.101/Locales/;d1=French;x1=fr-FR_78xx_68xx-11.2.1.1004.xml;
d2=German;x2=de-DE_78xx_68xx-11.2.1.1004.xml
```

```
serv=http://10.74.128.101/Locales/;d1=French;x1=fr-FR_88xx-11.2.1.1004.xml;
d2=German;x2=de-DE_88xx-11.2.1.1004.xml
```

Example for including French (Canada):

```
serv=http://10.74.128.101/Locales/;d1=French-Canada;x1=fr-CA_78xx_68xx-11.3.6.0006xml;
```

```
serv=http://10.74.128.101/Locales/;d1=French-Canada;x1=fr-CA_88xx-11.3.6.0006xml;
```

In the above examples http://10.74.128.101/Locales/ is a web folder. The dictionary files are extracted in this web folder and are used in the examples.

To configure this option in the phone configuration XML file (cfg.xml), enter a string in this format:

```
<Dictionary_Server_Script ua="na">serv=http://10.74.10.215/lcdapi/resync_files/;d1=French-Canada;x1=fr-CA_88xx-11.3.6.0006.xml;</Dictionary_Server_Script>
```

```
<Language_Selection ua="na">French-Canada</Language_Selection>
```

```
<Locale ua="na">fr-CA</Locale>
```

Add values for:

Language Selection Parameter as appropriate

For French: French

For French (Canada): French-Canada

For German: German

Locale parameter list as appropriate

For French: fr-FR

For French (Canada): fr-CA

For German: de-DE

After the successful configuration, the user can see the configured language option on the phone under the Language menu. User can access the Language menu from Applications > Device administration .

##### Setup for an Asian Language

If you use an Asian language such as Chinese, Japanese, or Korean, you can only set up one language option for the phone.

You must set up the dictionary and the font for the language. To do this, specify the d1 , x1 and f1 parameters and values in the Dictionary Server Script field.

Example for setting up Chinese-Simplified:

```
serv=http://10.74.128.101/Locales/;d1=Chinese-Simplified;
x1=zh-CN_78xx_68xx-11.2.1.1004.xml;f1=zh-CN_78xx_68xx-11.2.1.1004.ttf
```

```
serv=http://10.74.128.101/Locales/;d1=Chinese-Simplified;
x1=zh-CN_88xx-11.2.1.1004.xml;f1=zh-CN_88xx-11.2.1.1004.ttf
```

##### Setup for RTL Languages

If you use a Right-to-Left (RTL) language such as Arabic and Hebrew, you can only set up one language option for the phone.

You must set up the dictionary and the font for the language. To do this, specify the d1, x1, and f1 parameters and values
                                       in the Dictionary Server Script field.

```
serv=http://server.example.com/Locales;d1=Arabic;x1=ar-SA_88xx-11.3.4.xml;f1=ar-SA_88xx-11.3.4.ttf
```

```
serv=http://server.example.com/Locales;d1=Hebrew;x1=he-IL_88xx-11.3.4.xml;f1=he-IL_88xx-11.3.4.ttf
```

Values for Language Selection parameter must be Arabic or Hebrew as appropriate.

Values for Locale parameter must be ar-SA for Arabic and he-IL for Hebrew.

##### Specify a Language for the Phone Display

Your users can select the language on the phone, from Settings > Device Administration > Language .

###### Before you begin

Step 1

On the phone administration web page, go to Admin Login > Advanced > Voice > Regional , Language section. In the Language Selection field, specify the value of the appropriate d n parameter value from the Dictionary Server Script field, for the language of your choice.

Step 2

Click Submit All Changes .

### Vertical Service Activation Codes

Parameter

Description

Call Return Code

This code calls the last caller.

Defaults to *69.

Blind Transfer Code

Begins a blind transfer of the current call to the extension specified after the activation code.

Defaults to *95.

Cfwd All Act Code

Forwards all calls to the extension specified after the activation code.

Defaults to *72.

Cfwd All Deact Code

Cancels call forward of all calls.

Defaults to *73.

Cfwd Busy Act Code

Forwards busy calls to the extension specified after the activation code.

Defaults to *90.

Cfwd Busy Deact Code

Cancels call forward of busy calls.

Defaults to *91.

Cfwd No Ans Act Code

Forwards no-answer calls to the extension specified after the activation code.

Defaults to *92.

Cfwd No Ans Deact Code

Cancels call forward of no-answer calls.

Defaults to *93.

CW Act Code

Enables call waiting on all calls.

Defaults to *56.

CW Deact Code

Disables call waiting on all calls.

Defaults to *57.

CW Per Call Act Code

Enables call waiting for the next call.

Defaults to *71.

CW Per Call Deact Code

Disables call waiting for the next call.

Defaults to *70.

Block CID Act Code

Blocks caller ID on all outbound calls.

Defaults to *61.

Block CID Deact Code

Removes caller ID blocking on all outbound calls.

Defaults to *62.

Block CID Per Call Act Code

Removes caller ID blocking on the next inbound call.

Defaults to *81.

Block CID Per Call Deact Code

Removes caller ID blocking on the next inbound call.

Defaults to *82.

Block ANC Act Code

Blocks all anonymous calls.

Defaults to *77.

Block ANC Deact Code

Removes blocking of all anonymous calls.

Defaults to *87.

DND Act Code

Enables the do not disturb feature.

Defaults to *78.

DND Deact Code

Disables the do not disturb feature.

Defaults to *79.

Secure All Call Act Code

Makes all outbound calls secure.

Defaults to *16.

Secure No Call Act Code

Makes all outbound calls not secure.

Defaults to *17.

Secure One Call Act Code

Makes a secure call.

Default: *18.

Secure One Call Deact Code

Disables secure call feature.

Default: *19.

Paging Code

The star code used for paging the other clients in the group.

Defaults to *96.

Call Park Code

The star code used for parking the current call.

Defaults to *68.

Call Pickup Code

The star code used for picking up a ringing call.

Defaults to *97.

Call Unpark Code

The star code used for picking up a call from the call park.

Defaults to *88.

Group Call Pickup Code

The star code used for picking up a group call.

Defaults to *98.

Exec Assistant Call Initiate Code

For executive assistants: Initiates a call on behalf of an executive from the user's (assistant's) extension.

Default: #64

Applicable to Cisco IP Phone 6871 Multiplatform Phones only.

Exec Call Filter Act Code

For executives who have assistants: Activates call filtering. When call filtering is on, assistants receive incoming calls
                                             for executives.

Default: #61

Applicable to Cisco IP Phone 6871 Multiplatform Phones only.

Exec Call Filter Deact Code

For executives who have assistants: Deactivates call filtering.

Default: #62

Applicable to Cisco IP Phone 6871 Multiplatform Phones only.

Exec Assistant Call Push Code

For executive assistants: Transfers an ongoing call from the user (assistant) to the executive.

Default: #63

Applicable to Cisco IP Phone 6871 Multiplatform Phones only.

Exec Call Retrieve Code

For executives who have assistants: Transfers an ongoing call from an assistant to the user (executive).

For executive assistants: Transfers an ongoing call from the executive to the user (assistant).

Default: *11

Applicable to Cisco IP Phone 6871 Multiplatform Phones only.

Exec Call Bridge Code

For executives who have assistants: Joins the user (executive) to an ongoing call with an assistant.

For executive assistants: Joins the user (assistant) to an ongoing call with an executive.

Default: *15

Applicable to Cisco IP Phone 6871 Multiplatform Phones only.

Important

If you change any of the service activation codes used by executives or assistants, you must update the corresponding settings
                                                         in BroadWorks.

Referral Services Codes

These codes tell the IP phone what to do when the user places the current call on hold and is listening to the second dial
                                             tone.

One or more *code can be configured into this parameter, such as *98, or *97|*98|*123, and so on. Max total length is 79 chars.
                                             This parameter applies when the user places the current call on hold (by Hook Flash) and is listening to second dial tone.
                                             Each *code (and the following valid target number according to current dial plan) entered on the second dial-tone triggers
                                             the phone to perform a blind transfer to a target number that is prepended by the service *code.

For example, after the user dials *98, the IP phone plays a special dial tone called the Prompt Tone while waiting for the
                                             user the enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered,
                                             the phone sends a blind REFER to the holding party with the Refer-To target equals to *98<target_number>. This feature allows
                                             the phone to hand off a call to an application server to perform further processing, such as call park.

The *codes should not conflict with any of the other vertical service codes internally processed by the IP phone. You can
                                             empty the corresponding *code that you do not want to the phone to process.

Feature Dial Services Codes

These codes tell the phone what to do when the user is listening to the first or second dial tone.

One or more *code can be configured into this parameter, such as *72, or *72|*74|*67|*82, and so forth. The maximum total
                                             length is 79 characters. This parameter applies when the user has a dial tone (first or second dial tone). Enter *code (and
                                             the following target number according to current dial plan) entered at the dial tone triggers the phone to call the target
                                             number prepended by the *code. For example, after user dials *72, the phone plays a prompt tone awaiting the user to enter
                                             a valid target number. When a complete number is entered, the phone sends a INVITE to *72<target_number> as in a normal call.
                                             This feature allows the proxy to process features like call forward (*72) or BLock Caller ID (*67).

The *codes should not conflict with any of the other vertical service codes internally processed by the phone. You can empty
                                             the corresponding *code that you do not want to the phone to process.

You can add a parameter to each *code in Features Dial Services Codes to indicate what tone to play after the *code is entered,
                                             such as *72‘c‘|*67‘p‘. Below are a list of allowed tone parameters (note the use of back quotes surrounding the parameter
                                             without spaces)

• c = Cfwd Dial Tone

• d = Dial Tone

• m = MWI Dial Tone

• o = Outside Dial Tone

• p = Prompt Dial Tone

• s = Second Dial Tone

• x = No tones are place, x is any digit not used above

If no tone parameter is specified, the phone plays Prompt tone by default.

If the *code is not to be followed by a phone number, such as *73 to cancel call forward, do not include it in this parameter.
                                             In that case, simple add that *code in the dial plan and the phone sends INVITE *73@..... as usual when user dials *73.

## Cisco IP Phone 8800 Series Documentation

Refer to publications that are specific to your language and
                              		  phone model, and phone firmware release. Navigate from the following
                              		  documentation URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/tsd-products-support-series-home.html

| Step 1 | Configure a VoIP Network to meet the following requirements: VoIP is configured on your routers and gateways. |
|---|---|
| Step 2 | Set up the network to support one of the following: DHCP support Manual assignment of IP address, gateway, and subnet mask |

| Step 1 | Choose the
                                       			 power source for the phone: Power
                                                					 over Ethernet (PoE) External
                                                					 power supply |
|---|---|
| Step 2 | Connect the
                                       			 handset to the handset port. The
                                          				wideband-capable handset is designed especially for use with a Cisco IP Phone.
                                          				The handset includes a light strip that indicates incoming calls and waiting
                                          				voice messages. |
| Step 3 | Connect a headset to the headset port. You can add a headset
                                       			 later if you do not connect one now. |
| Step 4 | Connect a wireless headset. You can add a wireless headset later
                                       			 if you do not want to connect one now. For more information, see your wireless
                                       			 headset documentation. |
| Step 5 | Connect a
                                       			 straight-through Ethernet cable from the switch to the network port labeled
                                       			 10/100/1000 SW on the Cisco IP Phone.
                                       			 Each Cisco IP Phone ships with one Ethernet cable in the box. Use Category 3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for 100Mbps connections; and Category 5e
                                          or 6 for 1000 Mbps connections. For more information, see Network and Computer Port Pinouts . |
| Step 6 | Connect a straight-through Ethernet cable from another network
                                       			 device, such as a desktop computer, to the computer port on the Cisco IP Phone.
                                       			 You can connect another network device later if you do not connect one now. Use Category 3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for 100Mbps connections; and Category 5e
                                          or 6 for 1000 Mbps connections. For more information, see Network and Computer Port Pinouts for guidelines. |
| Step 7 | If the phone is on a desk, adjust the footstand. With a wall-mounted phone, you might need to adjust the handset rest to ensure
                                       that the receiver cannot slip out of the cradle. |
| Step 8 | Monitor the
                                       			 phone startup process. This step verifies that the phone is configured
                                       			 properly. |
| Step 9 | If you are
                                       			 configuring the network settings on the phone, you can set up an IP address for
                                       			 the phone by either using DHCP or manually entering an IP address. See Configure the Network from the Phone . |
| Step 10 | Upgrade the
                                       			 phone to the current firmware image. Firmware
                                          				upgrades over the WLAN interface may take longer than upgrading over the wired
                                          				interface, depending on the quality and bandwidth of the wireless connection.
                                          				Some upgrades may take more than one hour. |
| Step 11 | Make calls
                                       			 with the Cisco IP Phone to verify that the phone and features work correctly. |
| Step 12 | Provide
                                       			 information to end users about how to use their phones and how to configure
                                       			 their phone options. This step ensures that users have adequate information to
                                       			 successfully use their Cisco IPPhones. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration . |
| Step 3 | Use the navigation arrows to select the desired menu and edit. |
| Step 4 | To display a submenu, repeat step 3. |
| Step 5 | To exit a menu, press . |
| Step 6 | To exit a menu, press Back . |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Ethernet configuration |  |  | See the following Ethernet configuration submenu table. |
| IP mode | Dual mode IPv4 only IPv6 only | Dual mode | Select the Internet Protocol mode for which the phone operates. In dual mode, the phone can have both IPv4 and IPv6 addresses. |
| Wi-Fi configuration |  |  | See Set Up a Wi-Fi Profile from the Phone For Cisco IP Phone 8861 Multiplatform Phones only. For Cisco IP Phone 6861 Multiplatform Phones only. |
| IPv4 address settings | DHCP Static IP Release DHCP IP | DHCP | See the IPv4 address submenu table in the following tables. |
| IPv6 address settings | DHCP Static IP | DHCP | See the IPv6 address submenu table in the following tables. |
| DHCPv6 option to use |  | 17, 160, 159 | Indicates the order in which the phone uses the IPv6 addresses provided by DHCP server. |
| HTTP proxy settings |  |  | See the following HTTP proxy settings submenu table. |
| VPN settings |  |  | See the following VPN settings submenu table. |
| Web server | On Off | On | Indicates whether the phone has web server enabled or disabled. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| 802.1x authentication | Device authentication | Off | Enables or disables the 802.1x authentication. Valid options are: On Off |
| Transaction status | Disabled | Transaction status—Indicates different authentication status when you turn on 802.1x in the Device authentication field. Connecting : Indicates that the authentication process is in progress. Authenticated : Indicates that the phone is authenticated. Disabled : Indicates that 802.1x authentication is disabled on the phone. Protocol—Displays the protocol of the server. |
| User certificate type | Manufacturing installed | Choose the certificate for the 802.1X authentication during the initial enrollment and certificate renewal. Manufacturing installed—The Manufacturing Installed Certificate (MIC) and Secure Unique Device Identifier (SUDI) is used. Custom installed—The Custom Device Certificate (CDC) is used. This type of certificate can be installed either by manual uploading
                                                   on the phone web page or by installation from a Simple Certificate Enrollment Protocol (SCEP) server. This parameter appears on the phone only when Device authentication is enabled. |
| Switch port config | Auto 10MB half 10MB full 100MB half 100MB full 1000 full 1000 full (except for 7811 and 7821) | Auto | Select speed and duplex of the network port. If the phone is connected to a switch, configure the port on the switch to the same speed/duplex as the phone, or configure
                                             both to autonegotiate. If you change the setting of this option, you must change the PC Port config option to the same setting. |
| PC port config | Auto 10MB half 10MB full 100 MB half 100MB full 100 half 1000 full (except for 6821) 1000 full (except for 7811 and 7821) 1000 full | Auto | Select Speed and duplex of the Computer (access) port. If the phone is connected to a switch, configure the port on the switch to the same speed/duplex as the phone, or configure
                                             both to autonegotiate. If you change the setting of this option, you must change the Switch Port config option to the same setting. |
| CDP | On Off | On | Enable or disable Cisco Discovery Protocol (CDP). CDP is a device-discovery protocol that runs on all Cisco manufactured equipment. Using CDP, a device can advertise its existence to other devices and receive information about other devices in the network. |
| LLDP-MED | On Off | On | Enable or disable LLDP-MED. LLDP-MED enables the phone to advertise itself to devices that use the discovery protocol. |
| Startup delay |  | 3 seconds | Set a value that causes a delay for the switch to get to the forwarding state before the phone sends out the first LLDP-MED
                                             packet. For configuration of some switches, you might need to increase this value to a higher value for LLDP-MED to work.
                                             Configuring a delay can be important for networks that use the Spanning Tree Protocol. Default delay is 3 seconds. |
| VLAN | On Off | Off | Enable or disable VLAN. Permits you to enter a VLAN ID when you use VLAN without CDP or LLDP. When you use a VLAN with CDP or LLDP, that associated
                                             VLAN takes precedent over the VLAN ID you manually entered. |
| VLAN ID |  | 1 | Enter a VLAN ID for the IP phone when you use a VLAN without CDP (VLAN enabled and CDP disabled). Note that only voice packets
                                             are tagged with the VLAN ID. Do not use the 1 value for the VLAN ID. If VLAN ID is 1, you cannot tag voice packets with the
                                             VLAN ID. |
| PC port VLAN ID |  | 1 | Enter a value of the VLAN ID that is used to tag communications from the PC port on the phone. The phone tags all the untagged frames coming from the PC (it does not tag any frames with an existing tag). Valid values: 0 through 4095 Default: 0 |
| PC port mirror | On Off | Off | Adds the ability to port mirror on the PC port. When enabled, you can see the packets on the phone. Select On to enable PC port mirroring and select Off to disable it. |
| DHCP VLAN option |  |  | Enter a predefined DHCP VLAN option to learn the voice VLAN ID. When you use a VLAN ID with CDP, LLDP, or manually select a VLAN ID, that VLAN ID takes precedent over the selected DHCP VLAN
                                             option. Valid values are: Null 128 to 149 151 to 158 161 to 254 Default value is null. Cisco recommends that you use DHCP Option 132. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Connection type | DHCP |  | Indicates whether the phone has DHCP enabled. DNS1—Identifies the primary Domain Name System (DNS) server that the phone uses. DNS2—Identifies the secondary Domain Name System (DNS) server that the phone uses. DHCP address released—Releases the IP address that DHCP assigned. You can edit this field if DHCP is enabled. To remove the
                                                   phone from the VLAN and release the IP address for reassignment, set this field to Yes and press Set . |
| Static IP |  | When DHCP is disabled, you must set the Internet Protocol (IP) address of the phone. Static IP address—Identifies the IP that you assign to the phone. The phone uses this IP address instead of acquiring an IP
                                                   from the DHCP server on the network. Subnet Mask—Identifies the subnet mask used by the phone. When DHCP is disabled, you must set the subnet mask. Gateway address—Identifies the default router used by the phone. DNS1—Identifies the primary Domain Name System (DNS) server that the phone uses. When DHCP is disabled, you must set this
                                                   field manually. DNS2—Identifies the primary Domain Name System (DNS) server that the phone uses. When DHCP is disabled, you must set this
                                                   field manually. When you assign an IP address using this field, you must also assign a subnet mask and a gateway address. See the Subnet Mask
                                             and Default Router fields in this table. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Connection type | DHCP |  | Indicates whether the phone has Dynamic Host Configuration Protocol (DHCP) enabled. DNS1—Identifies the primary DNS server that the phone uses. DNS2—Identifies the secondary DNS server that the phone uses. Broadcast Echo—Identifies if the phone responses to multicast ICMPv6 message with destination address of ff02::1. Auto config— Identifies if the phone uses automatic configuration for the address. |
| Static IP |  | When DHCP is disabled, you must set the Internet Protocol (IP) address of the phone and must set the values of the fields: Static IP—Identifies the IP that you assign to the phone. The phone uses this IP address instead of acquiring an IP from the
                                                   DHCP server on the network. Prefix length—Identifies how many bits of a Global Unicast IPv6 Address are there in the network part. Gateway—Identifies the default router used by the phone. Primary DNS—Identifies the primary DNS server that the phone uses. When DHCP is disabled, you must set this field manually. Secondary DNS—Identifies the primary DNS server that the phone uses. When DHCP is disabled, you must set this field manually. Broadcast Echo—Identifies if the phone responses to multicast ICMPv6 message with destination address of ff02::1. |

| Field | Field Type or Choices | Description |
|---|---|---|
| VPN server |  | Enter an IP address or FQDN of the VPN server that the phone uses for the VPN connection. |
| Username |  | Enter a VPN username to access the VPN server. |
| Password |  | Enter a valid password of the username to access the VPN server. |
| Tunnel group |  | Enter a VPN tunnel group for the VPN connection. |
| Connect to VPN on bootup | On Off | Determines whether the phone connects to the VPN server automatically after the phone reboots. Default value is Off |
| Enable VPN connection | On Off | Enables or disables the VPN connection. When you enable or disable the VPN connection, the phone reboots automatically. Default value is Off |

| Field | Field Type or Choices | Description |
|---|---|---|
| Proxy mode | Auto | Auto discovery (WPAD)—Enables or disables the Web Proxy Auto-Discovery protocol to retrieve a Proxy Auto-Configuration (PAC)
                                             file. Valid options are: On Off If the value is set to Off, you need to further set the following field: PAC URL—Specifies the URL address for the PAC file that you want to retrieve. For example: http://proxy.department.branch.example.com The default value of Auto discovery (WPAD) is On. |
| Manual | Proxy host—Specifies an IP address or hostname of the proxy server for the phone. The scheme ( http:// or https:// ) is not required. Proxy port—Specifies a port number of the proxy server. Proxy authentication—Selects an option according to the actual situation of the proxy server. If the server requires authentication
                                                   credentials to grant access to the phone, then select On. Otherwise, select Off. Options are: Off On If the value is set to On, you need to further set the following fields: Username—Specifies the username of a credential user on the proxy server. Password—Provides the specified user's password to pass the authentication of the proxy server. The default value of Proxy authentication is Off. |
| Off | Disables the HTTP proxy feature on the phone. |

| Note | The Cisco IP
                                             			 Phone provides several methods to reset or restore option settings, if
                                             			 necessary. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration . |
| Step 3 | Select Wi-Fi Type and press the Select button to choose from WLAN and WPS . |
| Step 4 | In the Wi-Fi Profile screen, click Scan to get a list of available wireless networks (SSIDs). You can also click Cancel to stop the scan process. If your phone is associated with an SSID, the associated SSID appears at the top of scanned list with a check mark in front
                                          of it. |
| Step 5 | Select an SSID when the scan is complete, and set up the fields for your phone to connect to that network as described in
                                       the following table. Field Field Type or Choices Default Description Security mode Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None PSK Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. Network name Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. User ID Allows you to enter a user ID for the network profile. Password WEP Key Passphrase Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. Frequency band Auto 2.4 GHz 5 GHz Auto Allows you to select the wireless signal standard that the WLAN uses. | Field | Field Type or Choices | Default | Description | Security mode | Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None | PSK | Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. | Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. | User ID |  |  | Allows you to enter a user ID for the network profile. | Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. | Frequency band | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that the WLAN uses. |
| Field | Field Type or Choices | Default | Description |
| Security mode | Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None | PSK | Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. |
| Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. |
| User ID |  |  | Allows you to enter a user ID for the network profile. |
| Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. |
| Frequency band | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that the WLAN uses. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Security mode | Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None | PSK | Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. |
| Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. |
| User ID |  |  | Allows you to enter a user ID for the network profile. |
| Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. |
| Frequency band | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that the WLAN uses. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Security mode | Auto None WEP PSK | None | Allows you to select the type of authentication that the phone uses to access the WLAN. |
| User ID |  |  | Allows you to enter a user ID for the network profile. |
| Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                          you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. |
| 802.11 mode | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that is used in the WLAN. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Security mode | EAP-FAST PEAP-GTC PEAP (MSCHAPV2) PSK WEP None | None | Allows you to select the type of authentication that the phone uses to access the WLAN. |
| Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. |
| User ID |  |  | Allows you to enter a user ID for the network profile. |
| Password |  |  | Allows you to enter a password for the network profile. |
| 802.11 mode | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that is used in the WLAN. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi . |
| Step 3 | Press the Select button, to turn the Wi-Fi on or off. You can also press the Navigation cluster, left or right, to turn the Wi-Fi on or off. |
| Step 4 | Press the Select button, to turn the Wi-Fi on or off. |
| Step 5 | Press Set to save the changes. |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | On the phone web page, select User Login > Advanced > Voice > System . |
| Step 3 | Set the Wi-Fi Settings fields as described in the Parameters for Wi-Fi Settings table. |
| Step 4 | Go to the Wi-Fi Settings section and set the Phone-wifi-on field to Yes . |
| Step 5 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Phone-wifi-on | Turns Wi-Fi on or off  on your phone. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Phone-wifi-on ua="rw">No</Phone-wifi-on> In the phone web interface, set to Yes to turn on the Wi-Fi or set to No to turn it off. Default: Yes |
| Phone-wifi-type | Only supported by Cisco IP Phone 6861 Controls which method the phone will connect to a wireless network. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Phone-wifi-type ua="na">WLAN</Phone-wifi-type> In the phone web interface, select one of the methods: WLAN : This option requires the user to enter the credentials on the phone to connect to a protected wireless network. WPS : The user can connect the phone to a wireless network using either the WPS button on the access point or the PIN code. Allowed values: WLAN\|WPS Default: WLAN |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, do any of the actions to connect to Wi-Fi. Select any of the configured Wi-Fi profile and click Connect . Press Scan and select one wireless in the Connect to Wi-Fi screen. In the Setup Wi-Fi screen, enter values in the fields and press Connect . See the Profile Parameter table in the Set Up a Wi-Fi Profile from the Phone for the field values. You can also configure the Wi-Fi settings using the configuration file. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi status . You see the information: Wi-Fi status : Displays if the Wi-Fi is connected or disconnected. Network name : Indicates the name of the SSID. Signal strength : Indicates strength of the network signal. MAC address : Indicates MAC address of the phone. AP MAC address : Indicates MAC address of the access point (SSID). Channel : Indicated the channel on which the Wi-Fi network transmits and receives data. Frequency : Indicates the wireless signal frequency band that is used in the Wireless LAN. Security mode : Indicates the security mode that is set for the wireless LAN. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Wi-Fi messages . |
| Step 3 | Use the outer ring of the navigation cluster to scroll through the messages. |
| Step 4 | Press Details to view more details of the selected message. |
| Step 5 | (Optional) Press Clear to delete all the messages. |

| Step 1 | If you are using Power over Ethernet, plug the LAN cable into the Network port. |
|---|---|
| Step 2 | If you are using the power cube, connect the cube to the phone and plug the cube into an electrical outlet. The buttons flash amber and then
                                          			 green in sequence during the various stages of bootup as the phone checks the
                                          			 hardware. If the phone completes these stages successfully, it has
                                          		started up properly. |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | In the Network Settings section, configure the parameter Disable DF . If you set the Disable DF to Yes , the Don't Fragment (DF) bit is disabled. In this case, the network can fragment an IP packet. This is the default behaviour. If you set the Disable DF to No , the Don't Fragment (DF) bit is enabled. In this case, the network can't fragment an IP packet. This setting doesn't allow
                                                fragmentation in cases where the receiving host doesn't have sufficient resources to reassemble internet fragments. |
| Step 3 | Click Submit All Changes . You can also configure the parameter in the phone configuration file (cfg.xml) with the following XML string: <Disable_DF ua="na">Yes</Disable_DF> Allowed values: Yes and No Default: Yes |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | In the Internet Connection Type section, use the Connection Type drop-down list to choose the connection type: Dynamic Host Configuration Protocol (DHCP) Static IP |
| Step 3 | In the IPv6 Settings section, use the Connection Type drop-down list to choose the connection type: Dynamic Host Configuration Protocol (DHCP) Static IP |
| Step 4 | If you choose Static IP, configure these settings in the Static IP Settings section: Static IP —Static IP address of the phone NetMask —Netmask of the phone (IPv4, only) Gateway —Gateway IP address |
| Step 5 | Click Submit All Changes . In the phone configuration XML file (cfg.xml), enter a string in this format: <Connection_Type ua="rw">DHCP</Connection_Type>
<!-- available options: DHCP\|Static IP -->
<Static_IP ua="rw"/>
<NetMask ua="rw"/>
<Gateway ua="rw"/> |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | In the VLAN Settings section, configure the parameters as defined in the VLAN Settings Parameters table. |
| Step 3 | Click Submit All Changes . You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure  each parameter,
                                          see the syntax of the string in the VLAN Settings Parameters table. |

| Parameter Name | Description and Default Value |
|---|---|
| Enable VLAN | Controls the VLAN feature. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Enable_VLAN ua="rw">No</Enable_VLAN> In the phone web interface, set to Yes to enable VLAN. The default value is Yes . |
| VLAN ID | If you use a VLAN without CDP (VLAN enabled and CDP disabled), enter a VLAN ID for the IP phone. Note that only voice packets
                                             are tagged with the VLAN ID. Do not use 1 for the VLAN ID. In the phone configuration file with XML(cfg.xml), enter a string in this format: <VLAN_ID ua="rw">1</VLAN_ID> In the phone web interface, enter an appropriate value. Valid values: An integer ranging from 0 through 4095 Default: 1 |
| Enable CDP | Enable CDP only if you are using a switch that has Cisco Discovery Protocol. CDP is negotiation based and determines which
                                             VLAN the IP phone resides in. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Enable_CDP ua="na">Yes</Enable_CDP> In the phone web page: set to Yes to enable CDP. Valid values: Yes/No Default: Yes |
| Enable LLDP-MED | Choose Yes to enable LLDP-MED for the phone to advertise itself to devices that use that discovery protocol. When the LLDP-MED feature is enabled, after the phone has initialized and Layer 2 connectivity is established, the phone sends
                                             out LLDP-MED PDU frames. If the phone receives no acknowledgment, the manually configured VLAN or default VLAN will be used
                                             if applicable. If the CDP is used concurrently, the waiting period of 6 seconds is used. The waiting period will increase
                                             the overall startup time for the phone. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Enable_LLDP-MED ua="na">Yes</Enable_LLDP-MED> In the phone web interface, set to Yes to enable LLDP-MED. Valid values: Yes/No Default: Yes |
| Network Startup Delay | Setting this value causes a delay for the switch to get to the forwarding state before the phone will send out the first LLDP-MED
                                             packet. The default delay is 3 seconds. For configuration of some switches, you might need to increase this value to a higher
                                             value for LLDP-MED to work. Configuring a delay can be important for networks that use Spanning Tree Protocol. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Network_Startup_Delay ua="na">3</Network_Startup_Delay> In the phone web interface, enter the delay in seconds. Valid values: An integer ranging from 1 through 300 Default: 3 |
| DHCP VLAN Option | A predefined DHCP VLAN option to learn the voice VLAN ID. You can use the feature only when no voice VLAN information is available
                                             by CDP/LLDP and manual VLAN methods. CDP/LLDP and manual VLAN are all disabled. Set the value to Null to disable DHCP VLAN option. Cisco recommends that you use DHCP Option 132. In the phone configuration file with XML(cfg.xml), enter a string in this format: <DHCP_VLAN_Option ua="na">132</DHCP_VLAN_Option> In the phone web page: specify the DHCP VLAN option. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, move to a row in the list on which you want to set up the profile. |
| Step 4 | Press the Select button. You can also press Options and then select Edit . |
| Step 5 | In the Edit profile screen, set the parameters as mentioned in the Profile Parameters table. Table 8. Profile Parameters Parameter Description Security mode Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK Network name Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. User ID Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. Password Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. WEP key Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. Passphrase Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. Frequency band Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto | Parameter | Description | Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK | Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. | User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. | Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. | WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. | Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. | Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Parameter | Description |
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Step 6 | Press Save . |

| Parameter | Description |
|---|---|
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | On the phone web page, select User Login > Advanced > Voice > System . |
| Step 3 | Set the Wi-Fi Profile fields as described in the following table. Field Field Type or Choices Default Description Security mode Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None PSK Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. Network name Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. User ID Allows you to enter a user ID for the network profile. Password WEP Key Passphrase Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. Frequency band Auto 2.4 GHz 5 GHz Auto Allows you to select the wireless signal standard that the WLAN uses. | Field | Field Type or Choices | Default | Description | Security mode | Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None | PSK | Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. | Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. | User ID |  |  | Allows you to enter a user ID for the network profile. | Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. | Frequency band | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that the WLAN uses. |
| Field | Field Type or Choices | Default | Description |
| Security mode | Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None | PSK | Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. |
| Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. |
| User ID |  |  | Allows you to enter a user ID for the network profile. |
| Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. |
| Frequency band | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that the WLAN uses. |
| Step 4 | Set the Wi-Fi Profile fields as described in the Wi-Fi Profile (n) table. |
| Step 5 | Set the Wi-Fi Profile fields with the information that your administrator provided. |
| Step 6 | Click Submit All Changes . If the phone has an active call, you can not save the changes. |

| Field | Field Type or Choices | Default | Description |
|---|---|---|---|
| Security mode | Auto EAP-FAST PEP-GCT PEAP-MSCHAPV2 PSK WEP None | PSK | Allows you to select the type of authentication that the phone uses to access the WLAN. The security mode depends on the settings on your access point. |
| Network name |  |  | Allows you to enter a unique name for the Wi-Fi profile. This name displays on the phone. |
| User ID |  |  | Allows you to enter a user ID for the network profile. |
| Password WEP Key Passphrase |  |  | Allows you to enter password for the network profile that you create. The type of password depends on the security mode that
                                                      you have selected. Password: Security mode is Auto. Passphrase: Security mode is PSK. WEP Key: Security mode is WEP. |
| Frequency band | Auto 2.4 GHz 5 GHz | Auto | Allows you to select the wireless signal standard that the WLAN uses. |

| Parameter | Description |
|---|---|
| Network Name | Allows you to enter a name for the SSID that will display on the phone. Multiple profiles can have the same network name with
                                             different security mode. In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Network_Name_1_ua="rw">cisco</Network_Name_1_> In the phone web page: , enter a name for the SSID. |
| Security Mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                             you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                             this Wi-Fi network. In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Security_Mode_1_ua="rw">Auto</Security_Mode_1_><!-- available options: Auto\|EAP-FAST\|PEAP-GTC\|PEAP-MSCHAPV2\|PSK\|WEP\|None
                                                   --> In the phone web page: , select one of the methods. Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Wi-Fi User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, or PEAP (MSCHAPV2). This is a mandatory
                                             field and it allows maximum length of 32 alphanumeric characters. In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Wi-Fi_User_ID_1_ua="rw"></Wi-Fi_User_ID_1_> In the phone web page: , enter a user ID for the network profile. |
| Wi-Fi Password | Allows you to enter the password for the specified Wi-Fi User ID. In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Wi-Fi_Password_1_ ua="rw"></Wi-Fi_Password_1_> In the phone web page: , enter a password for the user ID that you have added. |
| WEP Key | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                             is WEP. In the phone configuration file with XML(cfg.xml) , enter a string in this format: <WEP_Key_1_ ua="rw"/> In the phone web page: , enter a password for the network profile that you have created. |
| PSK Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                             is PSK. |
| Frequency Band | Allows you to select the wireless signal frequency band that is the WLAN uses. In the phone configuration file with XML(cfg.xml) , enter a string in this format: <PSK_Passphrase_1_ ua="rw"/> In the phone web page: , select one of the options: Auto 2.4 GHz 5 GHz Default: Auto |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, select the Wi-Fi profile that you want to remove. |
| Step 4 | Press Options . |
| Step 5 | Select Delete and then confirm the deletion. |

| Step 1 | If you change the Wi-Fi profile order from the phone, follow these steps: Press Applications . Select Network configuration > Wi-Fi configuration > Wi-Fi profile . In the Wi-Fi profile screen , select a Wi-Fi of which you want to change the order. Press Options . Select Move up or Move down to move the Wi-Fi profile one level up or one level down respectively in the list. |
|---|---|
| Step 2 | If you change the Wi-Fi profile order from the phone web page, follow these steps: On the phone web page, select User Login > Advanced > Voice > System . Select Voice > System . In the Wi-Fi Profile (n) section, set the Wi-Fi Profile Order field to the desired order. Click Submit All Changes . |

| Note | When the security mode of a wireless network is None, PSK, and WEP, you can't modify the security mode. On the Security mode screen, you only see the security mode that is set for the network. For example, if the security mode of a network is PSK,
                                                you see only PSK in the Security mode screen. When you scan a wireless network (SSID) which is the current connected wireless, you can't edit the Network name of this SSID. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, press Scan to get all available wireless networks. |
| Step 4 | (Optional) In the Connect to Wi-Fi screen, press Scan again to rescan the list. |
| Step 5 | Select a wireless and press Select or the Select button. |
| Step 6 | In the Setup Wi-Fi screen, set the parameters as mentioned in the Profile Parameters table. Table 10. Profile Parameters Parameter Description Security mode Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK Network name Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. User ID Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. Password Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. WEP key Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. Passphrase Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. Frequency band Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto | Parameter | Description | Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK | Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. | User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. | Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. | WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. | Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. | Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Parameter | Description |
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Step 7 | Press Save . |

| Parameter | Description |
|---|---|
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                      you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                      this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                      with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                      and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                      alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                      is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the SIP Parameters section, set the parameters as described in the SIP Parameters table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Max Forward | Specifies SIP Max Forward value. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Max_Forward ua="na">70</Max_Forward> In the phone web page, enter an appropriate value. Value range: 1 to 255 Default: 70 |
| Max Redirection | Specifies number of times an invite can be redirected to avoid an infinite loop. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Max_Redirection ua="na">5</Max_Redirection> In the phone web page, enter an appropriate value. Default: 5 |
| Max Auth | Specifies the maximum number of times (from 0 to 255) a request can be challenged. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Max_Auth ua="na">2</Max_Auth> In the phone web page, enter an appropriate value. Allowed value: 0 to 255 Default: 2 |
| SIP User Agent Name | Used in outbound requests. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_User_Agent_Name ua="na">$VERSION</SIP_User_Agent_Name> In the phone web page, enter an appropriate name. Default: $VERSION If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed |
| SIP Server Name | Server header used in responses to inbound responses. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_Server_Name ua="na">$VERSION</SIP_Server_Name> In the phone web page, enter an appropriate name. Default: $VERSION |
| SIP Reg User Agent Name | User-Agent name to be used in a REGISTER request. If this is not specified, the SIP User Agent Name is also used for the REGISTER
                                                request. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_Reg_User_Agent_Name ua="na">agent name</SIP_Reg_User_Agent_Name> In the phone web page, enter an appropriate name. Default: Blank |
| SIP Accept Language | Accept-Language header used. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_Accept_Language ua="na">en</SIP_Accept_Language> In the phone web page, enter an appropriate language. There is no default. If empty, the header is not included. |
| DTMF Relay MIME Type | MIME Type used in a SIP INFO message to signal a DTMF event. This field must match that of the Service Provider. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <DTMF_Relay_MIME_Type ua="na">application/dtmf-relay</DTMF_Relay_MIME_Type> In the phone web page, enter an appropriate MIME type. Default: application/dtmf-relay |
| Hook Flash MIME Type | MIME Type used in a SIPINFO message to signal a hook flash event. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Hook_Flash_MIME_Type ua="na">application/hook-flash</Hook_Flash_MIME_Type> In the phone web page, enter an appropriate MIME type for a SIPINFO message. Default: |
| Remove Last Reg | Enables you to remove the last registration before registering a new one if the value is different. Set to Yes to remove the last registration. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Remove_Last_Reg ua="na">No</Remove_Last_Reg> In the phone web page, Select Yes or No. Allowed values: Yes or No Default: No |
| Use Compact Header | If set to yes, the phone uses compact SIP headers in outbound SIP messages. If inbound SIP requests contain normal headers,
                                                the phone substitutes incoming headers with compact headers. If set to no, the phones use normal SIP headers. If inbound SIP
                                                requests contain compact headers, the phones reuse the same compact headers when generating the response, regardless of this
                                                setting. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Use_Compact_Header ua="na">No</Use_Compact_Header> In the phone web page, select Yes or No. Allowed values: Yes or No Default: No |
| Talk Package | Enables support for the BroadSoft Talk Package that lets users answer or resume a call by clicking a button in an external
                                                application. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Talk_Package ua="na">No</Talk_Package> In the phone web page, select Yes to enable the Talk Package. Allowed values: Yes or No Default: No |
| Hold Package | Enables support for the BroadSoft Hold Package, which lets users place a call on hold by clicking a button in an external
                                                application. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Hold_Package ua="na">No</Hold_Package> In the phone web page, select Yes to enable support for the Hold Package. Allowed values: Yes or No Default: No |
| Conference Package | Enables support for the BroadSoft Conference Package that enables users to start a conference call by clicking a button in
                                                an external application. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Conference_Package ua="na">No</Conference_Package> In the phone web page, select Yes or No. Allowed values: Yes or No Default: No |
| RFC 2543 Call Hold | If set to yes, unit includes c=0.0.0.0 syntax in SDP when sending a SIP re-INVITE to the peer to hold the call. If set to
                                                no, unit will not include the c=0.0.0.0 syntax in the SDP. The unit will always include a=sendonly syntax in the SDP in either
                                                case. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <RFC_2543_Call_Hold ua="na">Yes</RFC_2543_Call_Hold> In the phone web page, Yes or No. Allowed values: Yes or No Default: Yes |
| SIP TCP Port Min | Specifies the lowest TCP port number that can be used for SIP sessions. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_TCP_Port_Min ua="na">5060</SIP_TCP_Port_Min> In the phone web page, enter an appropriate value. Default: 5060 |
| SIP TCP Port Max | Specifies the highest TCP port number that can be used for SIP sessions. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_TCP_Port_Max ua="na">5080</SIP_TCP_Port_Max> In the phone web page, enter an appropriate value. Default: 5080 |
| Caller ID Header | Provides the option to take the caller ID from PAID-RPID-FROM, PAID-FROM, RPID-PAID-FROM, RPID-FROM, or FROM header. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Caller_ID_Header ua="na">PAID-RPID-FROM</Caller_ID_Header> In the phone web page, select an option. Allowed values: PAID-RPID-FROM, AID-FROM, RPID-PAID-FROM, RPID-FROM, and FROM Default: PAID-RPID-FROM |
| Dialog SDP Enable | When enabled and the Notify message body is too big causing fragmentation, the Notify message xml dialog is simplified; Session
                                                Description Protocol (SDP) is not included in the dialog xml content. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Dialog_SDP_Enable ua="na">No</Dialog_SDP_Enable> In the phone web page, select Yes or No . Allowed values: Yes or No Default: No |
| Keep Referee When Refer Failed | If set to yes, it configures the phone to immediately handle NOTIFY sipfrag messages. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Keep_Referee_When_Refer_Failed ua="na">No</Keep_Referee_When_Refer_Failed> In the phone web page, select Yes or No . Allowed values: Yes or No Default: No |
| Display Diversion Info | Display the Diversion info included in SIP message on LCD or not. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Display_Diversion_Info ua="na">No</Display_Diversion_Info> In the phone web page, select Yes or No . Allowed values: Yes or No |
| Display Anonymous From Header | Show the caller ID from the SIP INVITE message “From” header when set to Yes, even if the call is an anonymous call. When
                                                the parameter is set to no, the phone displays "Anonymous Caller" as the caller ID. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Display_Anonymous_From_Header ua="na">No</Display_Anonymous_From_Header> In the phone web page, select Yes or No . Allowed values: Yes or No Default: No |
| Sip Accept Encoding | Supports the content-encoding gzip feature. If gzip is selected, the SIP message header contains the string “Accept-Encoding: gzip”, and the phone is able to process
                                                the SIP message body, which is encoded with the gzip format. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Sip_Accept_Encoding ua="na">none</Sip_Accept_Encoding> In the phone web page, enter an appropriate MIME type for a SIPINFO message. Allowed values: none and gzip Default: none |
| SIP IP Preference | Sets if the phone uses IPv4 or IPv6. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_IP_Preference ua="na">IPv4</SIP_IP_Preference> In the phone web page, select IPv4 or IPv6. Allowed values: IPv4/IPv6 Default: IPv4. |
| Disable Local Name To Header | Controls the display name in “Directory”, “Call History”, and in the “To” header during an outgoing call. Perform one of the following. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Disable_Local_Name_To_Header ua="na">No</Disable_Local_Name_To_Header> In the phone web page, select Yes to disable the display name. Allowed values: Yes/No Default: No |
| Forced NAT64 | Sets the web parameter for Forced NAT64. Takes effect after a warm reboot. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Forced_NAT64 ua="na">Yes</Forced_NAT64> In the phone web page, select Yes . Allowed values: Yes/No Default: No |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the SIP Timer Values section, set the SIP timer values in seconds as described in SIP Timer Values (sec) . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| SIP T1 | RFC 3261 T1 value (RTT estimate) that can range from 0 to 64 seconds. Default: 0.5 seconds |
| SIP T2 | RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses) that can range from 0 to 64 seconds. Default: 4 seconds |
| SIP T4 | RFC 3261 T4 value (maximum duration a message remains in the network), which can range from 0 to 64 seconds. Default: 5 seconds. |
| INVITE Expires | INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Default: 240 seconds |
| ReINVITE Expires | ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to
                                                2000000. Default: 30 |
| Reg Retry Intv | Interval to wait before the Cisco IP Phone retries registration after failing during the last registration.The range is from
                                                1 to 2147483647 Default: 30 See the note below for additional details. |
| Reg Retry Long Intvl | When registration fails with a SIP response code that does not match<Retry Reg RSC>, the Cisco IP Phone waits for the specified
                                                length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg
                                                Retry Intvl value, which should not be 0. Default: 1200 See the note below for additional details. |
| Reg Retry Random Delay | Random delay range (in seconds) to add to <Register Retry Intvl> when retrying REGISTER after a failure. Minimum and maximum
                                                random delay to be added to the short timer. The range is from 0 to 2147483647. Default: 0 |
| Reg Retry Long Random Delay | Random delay range (in seconds) to add to <Register Retry Long Intvl> when retrying REGISTER after a failure. Default: 0 |
| Reg Retry Intvl Cap | Maximum value of the exponential delay. The maximum value to cap the exponential backoff retry delay (which starts at the
                                                Register Retry Intvl and doubles every retry). Defaults to 0, which disables the exponential backoff (that is, the error retry
                                                interval is always at the Register Retry Intvl). When this feature is enabled, the Reg Retry Random Delay is added to the
                                                exponential backoff delay value. The range is from 0 to 2147483647. Default: 0 |
| Sub Retry Intvl | This value (in seconds) determines the retry interval when the last Subscribe request fails. Default: 10. |

| Note | The phone can use a RETRY-AFTER value when it is received from a SIP proxy server that is too busy to process a request (503
                                                Service Unavailable message). If the response message includes a RETRY-AFTER header, the phone waits for the specified length
                                                of time before to REGISTER again. If a RETRY-AFTER header is not present, the phone waits for the value specified in the Reg
                                                Retry Interval or the Reg Retry Long Interval. |
|---|---|

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the Response Status Code Handling section, set the values as specified in the Response Status Code Handling Paramters table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Try Backup RSC | This parameter may be set to invoke failover upon receiving specified response codes. For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6?? Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Try_Backup_RSC ua="na"/> In the phone web page, enter an appropriate value. Default: Blank |
| Retry Reg RSC | Interval to wait before the phone retries registration after failing during the last registration. For example, you can enter numeric values 500 or a combination of numeric values plus wild cards if multiple values are possible.
                                                For the later, you can use 5?? to represent all SIP Response messages within the 500 range. If you want to use multiple ranges,
                                                you can add a comma "," to delimit values of 5?? and 6?? Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Retry_Reg_RSC ua="na"/> In the phone web page, enter an appropriate value. Default: Blank |

| Step 1 | Select Voice > Systems . |
|---|---|
| Step 2 | In the Optional Network Configuration section, set the IPv4 or IPv6 address as described in the NTP Server Parameters table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Primary NTP Server | IP address or name of the primary NTP server used to synchronize its time. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Primary_NTP_Server ua="rw"/> In the phone web page, enter the IP address of the priamry NTP server. Default: Blank |
| Secondary NTP Server | IP address or name of the secondary NTP server used to synchronize its time. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Secondary_NTP_Server ua="rw"/> In the phone web page, enter the IP address of the secondary NTP server. Default: Blank |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the RTP Parameters section, set the Real-Time Transport Protocol (RTP) parameter values as described in RTP Parameters . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| RTP Port Min | Minimum port number for RTP transmission and reception. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <RTP_Port_Min ua="na">16384</RTP_Port_Min> In the phone web page, enter an appropriate port number. Allowed values: 2048 to 49151 If the value range ( RTP Port Max - RTP Port Min ) is less than 16 or you configure the parameter incorrectly, the RTP port range (16382 to 32766) is used instead. Default: 16384 |
| RTP Port Max | Maximum port number for RTP transmission and reception. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <RTP_Port_Max ua="na">16482</RTP_Port_Max> In the phone web page, enter an appropriate port number. Allowed values: 2048 to 49151 If the value range ( RTP Port Max - RTP Port Min ) is less than 16 or you configure the parameter incorrectly, the RTP port range (16382 to 32766) is used instead. Default: 16482 |
| RTP Packet Size | Specifies packet size in seconds. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <RTP_Packet_Size ua="na">0.02</RTP_Packet_Size> In the phone web page, enter an appropriate value to specify the packet size. Allowed values: Ranges from 0.01 to 0.13. Valid values must be a multiple of 0.01 seconds. Default: 0.02 |
| Max RTP ICMP Err | Number of successive ICMP errors allowed when transmitting RTP packets to the peer before the phone terminates the call. If
                                                value is set to 0, the phone ignores the limit on ICMP errors. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Max_RTP_ICMP_Err ua="na">0</Max_RTP_ICMP_Err> In the phone web page, enter an appropriate value. Default: 0 |
| RTCP Tx Interval | Interval for sending out RTCP sender reports on an active connection. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <RTCP_Tx_Interval ua="na">5</RTCP_Tx_Interval> In the phone web page, enter an appropriate value. Allowed values: 0 to 255 seconds Default: 0 |
| Call Statistics | Specifies whether the phone sends end-of-call statistics within SIP messages when a call terminates or is put on hold. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Call_Statistics ua="na">No</Call_Statistics> In the phone web page, select Yes to enable this feature. Allowed values: Yes and No Default: No |
| SDP IP Preferences | Select the preferred IP that the phone uses as RTP address. If the phone is in dual-mode and has both ipv4 and ipv6 addresses, it will always include both addresses in SDP by attributes
                                                "a=altc … If  IPv4 address is selected, then ipv4 address has higher priority than ipv6 address in SDP and indicates that phone prefers
                                                using ipv4 RTP address. If the phone has only ipv4 address or ipv6 address,  SDP does not have ALTC attributes and RTP address is specified in “c=”
                                                line. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SDP_IP_Preference ua="na">IPv4</SDP_IP_Preference> In the phone web page, select the preferred IP . Allowed values: IPv4 and IPv6 Default: IPv4 |
| RTP Before ACK | Allows you to specify whether an RTP session starts before or after an ACK is received from the calling party. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <RTP_Before_ACK ua="na">No</RTP_Before_ACK> In the phone web page select: Yes : An RTP session doesn't await an ACK, but starts after a 200 OK message is sent. No : An RTP session doesn't start until an ACK is received from the calling party. Allowed values: Yes and No Default: No |
| SSRC Reset on Rx RE-INVITE | Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on incoming RE-INVITE. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SSRC_Reset_on_Rx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Rx_RE-INVITE> In the phone web page select: Yes : the phone can avoid the call transfer error, where only one person on the call hears the audio. This occurs on calls of
                                                            30 minutes or longer, and often on three-way calls. No :  the SSRC still remains during a long duration call. In this case, this error might occur. Allowed values: Yes and No Default: No |
| SSRC Reset on Tx RE-INVITE | Controls whether to reset the Synchronization Source (SSRC) for the outgoing RTP and SRTP sessions on outgoing RE-INVITE. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SSRC_Reset_on_Tx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Tx_RE-INVITE> In the phone web page select: Yes : the phone can avoid the one-way audio issue on a long duration call followed by a hold-resume action in certain Webex Calling
                                                            environments where the SRTP is end-to-end encrypted. No : the SSRC still remains during a long duration call. In this case, this error might occur. Allowed values: Yes and No Default: No |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the RTP Parameters section, set the parameter SSRC Reset on Rx RE-INVITE to Yes . You can also configure this parameter in the configuration file: <SSRC_Reset_on_Rx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Rx_RE-INVITE> Allowed values: Yes and No. Default: No Note If you set the parameter to No , the SSRC remains for the new outgoing RTP and SRTP sessions (SIP re-INVITEs). The call transfer error might occur during
                                                            a long duration call. | Note | If you set the parameter to No , the SSRC remains for the new outgoing RTP and SRTP sessions (SIP re-INVITEs). The call transfer error might occur during
                                                            a long duration call. |
| Note | If you set the parameter to No , the SSRC remains for the new outgoing RTP and SRTP sessions (SIP re-INVITEs). The call transfer error might occur during
                                                            a long duration call. |
| Step 3 | In the RTP Parameters section, set the parameter SSRC Reset on Tx RE-INVITE to Yes . You can also configure this parameter in the configuration file: <SSRC_Reset_on_Tx_RE-INVITE ua="na">Yes</SSRC_Reset_on_Tx_RE-INVITE> Allowed values: Yes and No. Default: No Note If you set the parameter to No , the SSRC remains for the outgoing RTP and SRTP sessions on outgoing SIP RE-INVITEs. The one-way audio might occur on a hold-resume
                                                            action on a long duration call. | Note | If you set the parameter to No , the SSRC remains for the outgoing RTP and SRTP sessions on outgoing SIP RE-INVITEs. The one-way audio might occur on a hold-resume
                                                            action on a long duration call. |
| Note | If you set the parameter to No , the SSRC remains for the outgoing RTP and SRTP sessions on outgoing SIP RE-INVITEs. The one-way audio might occur on a hold-resume
                                                            action on a long duration call. |
| Step 4 | Click Submit All Changes . |

| Note | If you set the parameter to No , the SSRC remains for the new outgoing RTP and SRTP sessions (SIP re-INVITEs). The call transfer error might occur during
                                                            a long duration call. |
|---|---|

| Note | If you set the parameter to No , the SSRC remains for the outgoing RTP and SRTP sessions on outgoing SIP RE-INVITEs. The one-way audio might occur on a hold-resume
                                                            action on a long duration call. |
|---|---|

| IP Mode | SIP IP Preference | Address List from DNS, Priority, Result P1 - First Priority Address P2 - Second Priority Address | Failover Sequence |
|---|---|---|---|
| Dual Mode | IPv4 | P1- 1.1.1.1, 2009:1:1:1::1 P2 - 2.2.2.2, 2009:2:2:2::2 Result : Phone will send the SIP messages to 1.1.1.1 first. | 1.1.1.1 ->2009:1:1:1:1 -> 2.2.2.2 -> 2009:2:2:2:2 |
| Dual Mode | IPv6 | P1- 1.1.1.1, 2009:1:1:1::1 P2 - 2.2.2.2, 2009:2:2:2::2 Result : Phone will send the SIP messages to 2009:1:1:1::1 first. | 2009:1:1:1:1 -> 1.1.1.1 -> 2009:2:2:2:2 -> 2.2.2.2 |
| Dual Mode | IPv4 | P1- 2009:1:1:1::1 P2 - 2.2.2.2, 2009:2:2:2::2 Result : Phone will send the SIP messages to 2009:1:1:1::1 first. | 2009:1:1:1:1 -> 2.2.2.2 -> 2009:2:2:2:2 |
| Dual Mode | IPv6 | P1- 2009:1:1:1::1 P2 - 2.2.2.2, 2009:2:2:2::2 Result : Phone will send the SIP messages to 1.1.1.1 first. | 2009:1:1:1:1 -> 2009:2:2:2:2 ->2.2.2.2 |
| IPv4 Only | IPv4 or IPv6 | P1 - 1.1.1.1, 2009:1:1:1::1 P2 -  2.2.2.2, 2009:2:2:2::2 Result : Phone will send the SIP messages to 1.1.1.1 first. | 1.1.1.1 -> 2.2.2.2 |
| IPv6 Only | IPv4 or IPv6 | P1 - 1.1.1.1, 2009:1:1:1::1 P2 -  2.2.2.2, 2009:2:2:2::2 Result : Phone will send the SIP messages to 2009:1:1:1::1 first. | 2009:1:1:1:1 ->  2009:2:2:2::2 |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the SIP Parameters section, select IPv4 or IPv6 in the SIP IP Preference field. For details, see SDP IP Preference field in the SIP Parameters table. |
| Step 3 | In the RTP Parameters section, select IPv4 or IPv6 in the SDP IP Preference field. For details, see SDP IP Preference in the RTP Parameters table. |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the RTP Parameters section, select Auto in the SDP IP Preference field. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <SDP_IP_Preference ua="na">Auto</SDP_IP_Preference> Options: IPv4 \| IPv6 \| Auto Default: IPv4 |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the SDP Payload Types section, set the value as specified in SDP Payload Types . AVT Dynamic Payload —is any nonstandard data. Both sender and receiver must agree on a number. The range is from 96 to 127. The default is 101. AVT 16kHz Dynamic Payload —is any nonstandard data. Both sender and receiver must agree on a number. The range is from 96 to 127. The default is 107. AVT 48kHz Dynamic Payload —is any nonstandard data. Both sender and receiver must agree on a number. The range is from 96 to 127. The default is 108. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| G722.2 Dynamic Payload | G722 Dynamic Payload type. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Try_Backup_RSC ua="na"/> In the phone web page, enter an appropriate value. Allowed values: Default: 96 |
| iLBC Dynamic Payload | iLBC Dynamic Payload type. Default: 97 |
| iSAC Dynamic Payload | iSAC Dynamic Payload type. Default: 98 |
| OPUS Dynamic Payload | OPUS Dynamic Payload type. Default: 99 |
| AVT Dynamic Payload | AVT dynamic payload type. Ranges from 96-127. Default: 101 |
| INFOREQ Dynamic Payload | INFOREQ Dynamic Payload type. |
| H264 BP0 Dynamic Payload | H264 BPO Dynamic Payload type. Default: 110 |
| H264 HP Dynamic Payload | H264 HP Dynamic Payload type. Default: 110 |
| iSAC Codec Name | iSAC codec name used in SDP. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <iSAC_Codec_Name ua="na">iSAC</iSAC_Codec_Name> In the phone web page, enter an appropriate codec name. Allowed values: Default: iSAC |
| AVT 16 kHz Dynamic Payload | AVT dynamic payload type for the 16 kHz clock rate. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <AVT_16kHz_Dynamic_Payload ua="na">107</AVT_16kHz_Dynamic_Payload> In the phone web page, enter the payload. Range: 96-127 Default: 107 |
| AVT 48 kHz Dynamic Payload | AVT dynamic payload type for the 48 kHz clock rate. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <AVT_48kHz_Dynamic_Payload ua="na">108</AVT_48kHz_Dynamic_Payload> In the phone web page, enter the payload. Range: 96-127 Default: 108 |

| Step 1 | Select Voice > Ext(n) , where n is an extension number. |
|---|---|
| Step 2 | In the SIP Settings section, set the parameter values as described in the Parameters for SIP Settings on Extensions table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| SIP Transport | Specifies the transport protocol for SIP messages. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_Transport_1_ ua="na">UDP</SIP_Transport_1_> In the phone web page, select the transport protocol type. UDP TCP TLS AUTO AUTO allows the phone to select the appropriate protocol automatically, based on the NAPTR records on the DNS server. See Configure the SIP Transport for more details. Default: UDP |
| SIP Port | The phone's port number for SIP message listening and transmission. Note Specify the port number here only when you are using UDP as the SIP transport protocol. If you are using TCP, the system uses a random port within the range specified in SIP TCP Port Min and SIP TCP Port Max on the Voice > SIP tab. If you need to specify a port of SIP proxy server, you can specify it using the Proxy field  or the XSI Host Server field. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_Port_1_ ua="na">5060</SIP_Port_1_> In the phone web page, enter an appropriate port number. Default: 5060 | Note | Specify the port number here only when you are using UDP as the SIP transport protocol. |
| Note | Specify the port number here only when you are using UDP as the SIP transport protocol. |
| SIP 100REL Enable | Individually enables the SIP 100REL feature. When enabled, the phone supports the 100REL SIP extension for reliable transmission of provisional responses (18x) and uses
                                                the PRACK requests. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_100REL_Enable_1_ ua="na">Yes</SIP_100REL_Enable_1_> In the phone web page, select Yes to enable the feature. Allowed values: Yes and No Default: No |
| Precondition Support | Determines whether the phone includes the precondition tag (defined in RFC 3312) in the Supported header field. Disabled : The phone doesn't include the precondition tag in the Supported header filed. And the phone doesn't return the 183 response
                                                      when it receives the INVITE request that contains the QoS precondition in the SDP description. Enabled : The phone includes the precondition tag in the Supported header field. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Precondition_Support_1_ ua="na">Enabled</Precondition_Support_1_> In the phone web page, select Enabled to enable the feature. Allowed values: Disabled and Enabled Default: Disabled |
| EXT SIP Port | The external SIP port number. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <EXT_SIP_Port_1_ ua="na">5060</EXT_SIP_Port_1_> In the phone web page, enter a port number. Allowed values: Default: 5060 |
| Auth Resync-Reboot | The Cisco IP Phone authenticates the sender when it receives a NOTIFY message with the following requests: resync reboot report restart XML-service Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Auth_Resync-Reboot_1_ ua="na">No</Auth_Resync-Reboot_1_> In the phone web page, select Yes to enable the feature. Allowed values: Yes and No Default: Yes |
| SIP Proxy-Require | The SIP proxy can support a specific extension or behavior when it receives the Proxy-Require header from the user agent.
                                                If this field is configured and the proxy does not support it, it responds with the message, unsupported. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <SIP_Proxy-Require_1_ ua="na">header<SIP_Proxy-Require_1_> In the phone web interface, enter the appropriate header in the field provided. Default: Blank |
| SIP Remote-Party-ID | The Remote-Party-ID header to use instead of the From header. Select Yes to enable. Default: Yes |
| Referor Bye Delay | Controls when the phone sends BYE to terminate stale call legs upon completion of call transfers. Multiple delay settings
                                                (Referor, Refer Target, Referee, and Refer-To Target) are configured on this screen. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Referor_Bye_Delay_1_ ua="na">4</Referor_Bye_Delay_1_> In the phone web page, enter the appropriate period of time in seconds. Allowed values: An integer from 0 through 65535 Default: 4 |
| Refer-To Target Contact | Indicates the refer-to target. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Refer-To_Target_Contact_1_ ua="na">No</Refer-To_Target_Contact_1_> In the phone web page, select Yes to send the SIP Refer to the contact. Allowed values: Yes and No Default: No |
| Referee Bye Delay | Specifies the Referee Bye Delay time in seconds. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Referee_Bye_Delay_1_ ua="na">0</Referee_Bye_Delay_1_> In the phone web page, enter the appropriate period of time in seconds. Allowed values: An integer from 0 through 65535 Default: 0 |
| Refer Target Bye Delay | Specifies the Refer Target Bye Delay time in seconds. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Refer_Target_Bye_Delay_1_ ua="na">0</Refer_Target_Bye_Delay_1_> In the phone web page,  enter the appropriate period of time in seconds. Allowed values: An integer from 0 through 65535 Default: 0 |
| Sticky 183 | Controls the first 183 SIP response for an outbound INVITE. To enable this feature, Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Sticky_183_1_ ua="na">No</Sticky_183_1_> In the phone web page,  select Yes to enable this feature. When enabled, the IP telephony ignores further 180 SIP responses after receiving the first 183 SIP response for an outbound
                                                      INVITE. Allowed values: Yes and No Default: No |
| Auth INVITE | Controls if authorization is required for initial incoming INVITE requests from the SIP proxy.  To enable this feature. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Auth_INVITE_1_ ua="na">No</Auth_INVITE_1_> In the phone web page,  select Yes to enable this feature. When enabled, authorization is required for initial incoming INVITE requests from the SIP proxy. Allowed values: Yes and No Default: No |
| Ntfy Refer On 1xx-To-Inv | If set to Yes , as a transferee, the phone will send a NOTIFY with Event:Refer to the transferor for any 1xx response returned by the transfer
                                                target, on the transfer call leg. If set to No , the phone will only send a NOTIFY for final responses (200 and higher). Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Ntfy_Refer_On_1xx-To-Inv_1_ ua="na">Yes</Ntfy_Refer_On_1xx-To-Inv_1_> In the phone web page,  select Yes to enable this feature. Allowed values: Yes and No Default: Yes |
| Set G729 annexb | Configure G.729 Annex B settings. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Set_G729_annexb_1_ ua="na">Yes</Set_G729_annexb_1_> In the phone web page,  select Yes to enable this feature. Allowed values: None No Yes Follow silence supp setting Default: Yes |
| User Equal Phone | When a tel URL is converted to a SIP URL and the phone number is represented by the user portion of the URL, the SIP URL includes
                                                the optional: user=phone parameter (RFC3261). For example: To: sip:+12325551234@example.com; user=phone Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <User_Equal_Phone_1_ ua="na">Yes</User_Equal_Phone_1_> In the phone web page, select Yes to enable this feature. Allowed values: Yes and No Default: No |
| Call Recording Protocol | Determines the type of recording protocol that the phone uses. Options are: SIPINFO SIPREC Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Call_Recording_Protocol_1_ ua="na">SIPREC</Call_Recording_Protocol_1_> In the phone web page, select a protocol from the list. Allowed values: SIPREC\|SIPINFO Default: SIPREC |
| Privacy Header | Sets user privacy in the SIP message in the trusted network. The privacy header options are: Disabled (default) none—The user requests that a privacy service applies no privacy functions to this SIP message. header—The user needs a privacy service to obscure headers which cannot be purged of identifying information. session—The user requests that a privacy service provide anonymity for the sessions. user—The user requests a privacy level only by intermediaries. id—The user requests that the system substitute an id that doesn't reveal the IP address or host name. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Privacy_Header_1_ ua="na">Disabled</Privacy_Header_1_> In the phone web page, select an option from the list. Allowed values: Disabled\|none\|header\|session\|user\|id Default: Disabled |
| P-Early-Media Support | Controls whether the P-Early-Media header is included in the SIP message for an outgoing call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <P-Early-Media_Support_1_ ua="na">No</P-Early-Media_Support_1_> In the phone web interface, to include the P-Early-Media header, select Yes . Allowed values: Yes and No Default: No |

| Note | Specify the port number here only when you are using UDP as the SIP transport protocol. |
|---|---|

| Step 1 | Select Voice > Ext(n) , where n is an extension number. |
|---|---|
| Step 2 | In the Proxy and Registration section, set the parameter values as described in the SIP Proxy and Registration for Extension Parameters table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Proxy | SIP proxy server and port number set by the service provider for all outbound requests. For example: 192.168.2.100:6060. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_1_ ua="na">64.101.154.134</Proxy_1_> <RTP_Port_Max ua="na">16482</RTP_Port_Max> In the phone web page, enter SIP proxy server and port number. When you need to refer to this proxy in another setting, for example, the speed dial line key configuration, use the $PROXY macro variable. Default: The port number is optional. If you don't specify a port, the default port 5060 is used for UDP, and the default
                                                port 5061 is used for TLS. |
| Outbound Proxy | Specifies an IP address or domain name. All outbound requests are sent as the first hop. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Outbound_Proxy_1_ ua="na">10.79.78.45</Outbound_Proxy_1_> In the phone web page, enter an IP address and a domain name. Default: Empty |
| Proxy Outbound Proxy For Survivable Remote Site Telephony (SRST) support | These parameters can be configured with an extension that includes a statically-configured DNS SRV record or DNS A record.
                                                This allows for failover and fallback functionality with a secondary proxy server. The format for the parameter value is as follows: FQDN format: hostname[:port][:SRV=host-list OR :A=ip-list] Where: host-list: srv[\|srv[\|srv...]] srv: hostname[:port][:p=priority][:weight][:A=ip-list] ip-list: ip-addr[,ip-addr[,ip-addr...]] Default: Priority is 0. Weight is 1. Port is 5060 and 5061 for UDP and TLS respectively. |
| Alternate Proxy Alternate Outbound Proxy | This feature provides fast fall back when there is network partition at the Internet or when the primary proxy (or primary
                                                outbound proxy) is not responsive or available. The feature works well in a Verizon deployment environment as the alternate
                                                proxy is the Integrated Service Router (ISR) with analog outbound phone connection. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Alternate_Proxy_1_ ua="na">10.74.23.43</Alternate_Proxy_1_> <Alternate_Outbound_Proxy_1_ ua="na">10.74.23.44</<Alternate_Outbound_Proxy_1_> In the phone web page, enter the proxy server addresses and port numbers in these fields. After the phone is registered to the primary proxy and the alternate proxy (or primary outbound proxy and alternate outbound
                                                proxy), the phone always sends out INVITE and Non-INVITE SIP messages (except registration) via the primary proxy. The phone
                                                always registers to both the primary and alternate proxies. If there is no response from the primary proxy after timeout (per
                                                the SIP RFC spec) for a new INVITE, the phone attempts to connect with the alternate proxy. The phone always tries the primary
                                                proxy first, and immediately tries the alternate proxy if the primary is unreachable. Active transactions (calls) never fall back between the primary and alternate proxies. If there is fall back for a new INVITE,
                                                the subscribe/notify transaction will fall back accordingly so that the phone's state can be maintained properly. You must
                                                also set Dual Registration in the Proxy and Registration section to Yes. Default: Empty |
| Use OB Proxy In Dialog | Determines whether to force SIP requests to be sent to the outbound proxy within a dialog. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Use_OB_Proxy_In_Dialog_1_ ua="na">Yes</Use_OB_Proxy_In_Dialog_1_> In the phone web page, select Yes or No . The request is ignored if the Use Outbound Proxy field is set to No or if the Outbound Proxy field is empty. Valid values: Yes and No Default: Yes |
| Register | Enables periodic registration with the proxy. This parameter is ignored if a proxy is not specified. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Register_1_ ua="na">Yes</Register_1_> In the phone web page, To enable this feature, select Yes . Valid values: Yes and No Default: Yes |
| Make Call Without Reg | Enables making outbound calls without successful (dynamic) registration by the phone. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Make_Call_Without_Reg_1_ ua="na">No</Make_Call_Without_Reg_1_> In the phone web page, To enable this feature, select Yes . If set to No , the dial tone plays only when registration is successful. Valid values: Yes and No Default: No |
| Register Expires | Defines how often the phone renews registration with the proxy. If the proxy responds to a REGISTER with a lower expires value,
                                                the phone renews registration based on that lower value instead of the configured value. If registration fails with an “Expires too brief” error response, the phone retries with the value specified in the Min-Expires
                                                header of the error. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Register_Expires_1_ ua="na">3600</Register_Expires_1_> In the phone web page, enter a value in seconds to define how often the phone renews registration with the proxy. Valid values: Numeric. The range is from 32 seconds to 2000000 seconds. Default: 3600 seconds |
| Ans Call Without Reg | If enabled, the user does not have to be registered with the proxy to answer calls. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Ans_Call_Without_Reg_1_ ua="na">No</Ans_Call_Without_Reg_1_> In the phone web page, To enable this feature, select Yes . Valid values: Yes and No Default: No |
| Use DNS SRV | Enables DNS SRV lookup for the proxy and outbound proxy. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Use_DNS_SRV_1_ ua="na">Yes</Use_DNS_SRV_1_> In the phone web page, To enable this feature, select Yes . Valid values: Yes and No Default: No |
| DNS SRV Auto Prefix | Enables the phone to automatically append a prefix to the proxy or outbound proxy name when performing a DNS SRV lookup on
                                                that name. The prefix to be appended varies with SIP transport protocols. _sip._udp. for UDP protocol _sip._tcp. for TCP protocol _sips._tcp. for TLS protocol Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <DNS_SRV_Auto_Prefix_1_ ua="na">Yes</DNS_SRV_Auto_Prefix_1_> In the phone web page, to enable this feature, select Yes . Valid values: Yes and No Default: No |
| Proxy Fallback Intvl | Sets the delay after which the phone retries from the highest priority proxy (or outbound proxy) after it has failed over
                                                to a lower priority server. The phone should have the primary and backup proxy server list from a DNS SRV record lookup on the server name. It needs to
                                                know the proxy priority; otherwise, it does not retry. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Fallback_Intvl_1_ ua="na">3600</Proxy_Fallback_Intvl_1_> In the phone web page, enter a value in seconds to set the duration in seconds after which the phone retries. Valid values: Numeric. The range is from 0 seconds to 65535 seconds. Default: 3600 seconds |
| Proxy Redundancy Method | The phone creates an internal list of proxies returned in the DNS SRV records. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Proxy_Redundancy_Method_1_ ua="na">Normal</Proxy_Redundancy_Method_1_> In the phone web page, select Normal and Based on SRV Port . If you set to Normal , the list contains proxies ranked by weight and priority. If you set to Based on SRV Port , the phone uses normal, then inspects the port number based on the first-listed proxy port. Valid values: Normal\|Based on SRV Port Default: Normal |
| Dual Registration | Controls both the dual registration and the fast fall back feature. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Dual_Registration_1_ ua="na">No</Dual_Registration_1_> In the phone web page, set to Yes to enable the Dual registration/Fast Fall back feature. To enable the feature you must also configure the alternate proxy/alternate
                                                      outbound proxy fields in the Proxy and Registration section. Valid values: Yes and No Default: No |
| Auto Register When Failover | Controls the fallback duration. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Auto_Register_When_Failover_1_ ua="na">Yes</Auto_Register_When_Failover_1_> In the phone web page, If set to No, the fallback happens immediately and automatically. If the Proxy Fallback Intvl is exceeded,
                                                      all the new SIP messages go to the primary proxy. If set to Yes, the fallback happens only when current registration expires, which means only a REGISTER message can trigger
                                                      fallback. For example, when the value for Register Expires is 3600 seconds and Proxy Fallback Intvl is 600 seconds, the fallback is
                                                triggered 3600 seconds later and not 600 seconds later. When the value for Register Expires is 600 seconds and Proxy Fallback
                                                Intvl is 1000 seconds, the fallback is triggered at 1200 seconds. After successfully registering back to primary server, all
                                                the SIP messages go to primary server. Valid values: Yes and No Default: Yes |
| TLS Name Validate | This field works only when SIP Transport is set to TLS for the phone line. Specifies whether hostname verification is required when the phone line uses SIP over TLS. The options are: In the phone configuration file with XML(cfg.xml), enter a string in this format: <TLS_Name_Validate_1_ ua="na">Yes</TLS_Name_Validate_1_> In the phone web page, select Yes when hostname verification is required. Select No to bypass the hostname verification. Valid values: Yes and No Default: Yes |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the Proxy and Registration section, set up Survivability Proxy and Survivability Proxy Fallback Intvl fields as described in Parameters for Outbound Proxy Survivability Support . |
| Step 3 | Select Voice > System . |
| Step 4 | In the System Configuration section, set up Survivability Test Mode field as described in Parameters for Outbound Proxy Survivability Support . |
| Step 5 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Survivability Proxy | The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform
                                                   a failover to a survivability gateway. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_n_>hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_> In the phone web interface, enter the proxy server address as follows: hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default: port=0 Example: wxclsg.example.com:8933:A=192.169.10.1 where, wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes. 8933=SGW port 192.169.10.1=Provisioned SGW address Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other. Allowed values: String Default: Blank |
| Survivability Proxy Fallback Intvl | The interval in seconds after which the phone will attempt to fallback to the SSE nodes In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_> in the phone web interface, specify the time interval in seconds. Default: 30 secs |
| Survivability Test Mode | If set it to Yes, phone will always register to SGW nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Test_Mode>No</Survivability_Test_Mode> in the phone web interface, select the test mode. Options: Yes\|No Default: No |

| Step 1 | Select Voice > Ext(n) , where n is an extension number. |
|---|---|
| Step 2 | In the Subscriber Information section, set the parameter values as described in the Subscriber Information Parameters table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Display Name | Name displayed as the caller ID. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Display_Name_1_ ua="na"/> In the phone web page, enter a name that represents the caller ID. |
| User ID | Extension number for this line. When you need to refer to this user ID in another setting, for example, the short name for a line key, use the $USER macro variable. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <User_ID_1_ ua="na">7001</User_ID_1_> In the phone web page, enter an extension number |
| Password | Password for this line. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Password_1_ ua="na">*************</Password_1_> In the phone web page, enter a value to add password for the line. Default: Blank (no password required) |
| Auth ID | Authentication ID for SIP authentication. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Auth_ID_1_ ua="na"/> In the phone web page, enter a value for an authentication ID. Default: Blank |
| SIP URI | The parameter by which the user agent will identify itself for this line. If this field is blank, the actual URI used in the
                                             SIP signaling should be automatically formed as: sip:UserName@Domain where UserName is the username given for this line in the User ID, and Domain is the domain given for this profile in the
                                             User Agent Domain. If the User Agent Domain is an empty string, then the IP address of the phone should be used for the domain. If the URI field is not empty, but if a SIP or SIPS URI contains no @ character, the actual URI used in the SIP signaling
                                             should be automatically formed by appending this parameter with an @ character followed by the IP address of the device. |

| Step 1 | Select Voice > Ext <n> where (n) is the number of the extension to configure. |
|---|---|
| Step 2 | In the SIP Settings section, set Use low-bandwidth OPUS to Yes . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the NAT Support Parameters section, set the parameters as described in the NAT Mapping with Static IP Parameters table. |
| Step 3 | Click the Ext(n) tab. |
| Step 4 | In the NAT Settings section, set the parameters as described in the NAT Mapping from Ext Tab with Static IP Parameters table. |
| Step 5 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Handle VIA received | Enables the phone to process the received parameter in the VIA header. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Handle_VIA_received ua="na">Yes</Handle_VIA_received> In the phone web page, set to Yes . Default: No |
| Handle VIA rport | Enables the phone to process the rport parameter in the VIA header. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Handle_VIA_rport ua="na">Yes</Handle_VIA_rport> In the phone web page, set to Yes . Default: No |
| Insert VIA received | Enables to insert the received parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Insert_VIA_received ua="na">Yes</Insert_VIA_received> In the phone web page, set to Yes . Default: No |
| Insert VIA rport | Enables to insert the rport parameter into the VIA header of SIP responses if the received-from IP and VIA sent-by IP values
                                                differ. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Insert_VIA_rport ua="na">Yes</Insert_VIA_rport> In the phone web page, set to Yes . Default: No |
| Substitute VIA Addr | Enables the user to use NAT-mapped IP:port values in the VIA header. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Substitute_VIA_Addr ua="na">Yes</Substitute_VIA_Addr> In the phone web page, set to Yes . Default: No |
| Send Resp To Src Port | Enables to send responses to the request source port instead of the VIA sent-by port. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Send_Resp_To_Src_Port ua="na">Yes</Send_Resp_To_Src_Port> In the phone web page, set to Yes . Default: No |
| NAT Keep Alive Intvl | Interval between NAT-mapping keep alive messages. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <NAT_Keep_Alive_Intvl ua="na">15</NAT_Keep_Alive_Intvl> In the phone web page, enter an appropriate value. Allowed values: Numeric ranges from 0 through 65535 Default: 15 |
| EXT IP | External IP address to substitute for the actual IP address of phone in all outgoing SIP messages. If 0.0.0.0 is specified,
                                                no IP address substitution is performed. If this parameter is specified, phone assumes this IP address when generating SIP messages and SDP (if NAT Mapping is enabled
                                                for that line). Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <EXT_IP ua="na">10.23.31.43</EXT_IP> In the phone web page, enter an external static IP address. Default: Blank |

| Parameter | Description |
|---|---|
| NAT Mapping Enable | Controls the use of externally mapped IP addresses and SIP/ RTP ports in SIP messages. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <NAT_Mapping_Enable_1_ ua="na">Yes</NAT_Mapping_Enable_1_> In the phone web page, set to Yes to use externally mapped IP addresses. Allowed values: Yes and No. Default: No |
| NAT Keep Alive Enable (Optional) | Configured NAT keep alive message periodically. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <NAT_Keep_Alive_Enable_1_ ua="na">Yes</NAT_Keep_Alive_Enable_1_> In the phone web page, set to Yes to configure periodic NAT keep alive messages. Note The service provider might require the phone to send NAT keep alive messages to keep the NAT ports open. Check with your service provider to determine the requirements. Allowed values: Yes and No. Default: No | Note | The service provider might require the phone to send NAT keep alive messages to keep the NAT ports open. Check with your service provider to determine the requirements. |
| Note | The service provider might require the phone to send NAT keep alive messages to keep the NAT ports open. Check with your service provider to determine the requirements. |

| Note | The service provider might require the phone to send NAT keep alive messages to keep the NAT ports open. Check with your service provider to determine the requirements. |
|---|---|

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the NAT Support Parameters section, set the Handle VIA received , Insert VIA received , Substitute VIA Addr , Handle VIA rport , Insert VIA rport , and Send Resp To Src Port parameters as described in the NAT Mapping with Static IP Parameters table. |
| Step 3 | Set the parameters as described in the NAT Mapping with STUN Parameters table. |
| Step 4 | Click the Ext(n) tab. |
| Step 5 | In the NAT Settings section, set the parameters as described in the NAT Mapping from Ext Tab with Static IP Parameters table. |
| Step 6 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| STUN Enable | Enables the use of STUN to discover NAT mapping. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <STUN_Enable ua="na">Yes</STUN_Enable> In the phone web page, set to Yes to enable the feature. Allowed values: Yes and No. Default: No |
| STUN Server | IP address or fully-qualified domain name of the STUN server to contact for NAT mapping discovery. You can use a public STUN
                                                server or set up your own STUN server. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <STUN_Server ua="na"/> In the phone web page, enter an IP address or fully-qualified domain name of the STUN server. Allowed values: Default: Blank |

| Step 1 | Select Voice > System and navigate to Optional Network Configuration section. |
|---|---|
| Step 2 | Enter the IP address for the Syslog Server , if the port number is anything
                                             other than the default, 514. It is not necessary to include the port number if it is the
                                             default. The address and port
                                                number must be reachable from the Cisco IP phone. The port number
                                                appears on the output log file name. The default output
                                                file is syslog.514.log (if port
                                                number was not specified). |
| Step 3 | Set the Debug Level to Error , Notice , or Debug . |
| Step 4 | To capture SIP signaling messages, click the Ext tab and navigate to SIP Settings . Set the SIP Debug Option to Full . |
| Step 5 | To collect information about what type of NAT your router uses
                                             click the SIP tab and navigate to NAT Support Parameters . |
| Step 6 | Click Voice > SIP and navigate to NAT Support Parameters . |
| Step 7 | Set STUN Test Enable to Yes . |
| Step 8 | Determine the type of NAT by viewing the debug messages in the log
                                             file. If the messages indicate that the device is using symmetric
                                             NAT, you cannot use STUN. |
| Step 9 | Click Submit All Changes . |

| Note | For more information on SIP parameters, see SIP Parameters . |
|---|---|

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the SIP Parameters section, select Yes in the Forced NAT64 field. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Forced_NAT64>Yes</Forced_NAT64> Options: Yes and No Default: No |
| Step 3 | Click Submit All Changes . |

| Digit Sequence | Function |
|---|---|
| 0 1 2 3 4 5 6 7 8 9 0 * # | Characters that represent a key that the user must press on the phone keypad. |
| x | Numeric digit 0 to 9 on the phone keypad. |
| [sequence] | Characters within square brackets create a list of accepted key presses. The user can press any one of the keys in the list. A numeric range, for example, [2-9] allows a user to press any one digit from 2 through 9 . A numeric range can include other characters. For example, [35-8*] allows a user to press 3, 5, 6, 7, 8, or *. |
| .  (period) | A period indicates element repetition. The dial plan accepts 0 or more entries of the digit. For example, 01. allows users to enter 0, 01, 011, 0111, and so forth. |
| <dialed:substituted> | This format indicates that certain dialed digits are replaced by the substituted characters when the sequence is transmitted. The dialed digits can be zero to 9. For example: <8:1650>xxxxxxx When the user presses 8 followed by a seven-digit number, the system automatically replaces the dialed 8 with the sequence 1650 . If the user dials 85550112 , the system transmits 16505550112 . If the dialed parameter is empty and there is a value in the substituted field, no digits are replaced and the substituted value is always prepended to the transmitted string. For example: <:1>xxxxxxxxxx When the user dials 9725550112 , the number 1 is added at the beginning of the sequence; the system transmits 19725550112 . |
| ,  (comma) | An intersequence tone played (and placed) between digits plays an outside line dial tone. For example: 9, 1xxxxxxxxxx An outside line dial tone plays after the user presses 9 . The tone continues until the user presses 1 . |
| !  (exclamation point) | Prohibits a dial sequence pattern. For example: 1900xxxxxxx! Rejects any 11-digit sequence that begins with 1900. |
| *xx | Allows a user to enter a 2-digit star code. |
| S0 or L0 | For Interdigit Timer Master Override, enter S0 to reduce the short interdigit timer to 0 seconds, or enter L0 to reduce the long interdigit timer to 0 seconds. |
| P | To pause, enter P , the number of seconds to pause, and a space. This feature is typically used for implementation of a hotline and warm line,
                                                with a 0 delay for the hot line, and a nonzero delay for a warm line. For example: P5 A pause of 5 seconds is introduced. |

| Terminating Event | Processing |
|---|---|
| Dialed digits have not matched any sequence in the dial plan. | The number is rejected. |
| Dialed digits exactly match one sequence in the dial plan. | If the dial plan allows the sequence, the number is accepted and is transmitted according to the dial plan. If the dial plan blocks the sequence, the number is rejected. |
| A timeout occurs. | The number is rejected if the dialed digits are not matched to a digit sequence in the dial plan within the time that the
                                                applicable interdigit timer specifies. The Interdigit Long Timer applies when the dialed digits do not match any digit sequence in the dial plan. Default: 10 seconds. The Interdigit Short Timer applies when the dialed digits match one or more candidate sequences in the dial plan. Default:
                                                3 seconds. |
| A user presses the # key or the dial softkey on the IP phone screen. | If the sequence is complete and is allowed by the dial plan, the number is accepted and is transmitted according to the dial
                                                plan. If the sequence is incomplete or is blocked by the dial plan, the number is rejected. |

| Note | The timer before a number is dialed is whichever shorter of the dial plan default timer and the dial tone timer set in the Dial Tone field on the Regional tab. |
|---|---|

| Note | The actual timer before a number is dialed is whichever shorter of the dial plan default timer and the dial tone timer set
                                                   in the Dial Tone field. In the following examples, the dial tone timer is assumed to be longer than the dial plan timer. |
|---|---|

| Note | You can edit the dial plan in the XML configuration file. Locate the Dial_Plan_n_ parameter in the XML configuration file, where n denotes the extension number. Edit the value of this parameter. The value
                                             must be specified in the same format as in the Dial Plan field on the phone administration web page, described below. |
|---|---|

| Step 1 | Select Voice > Ext(n) , where n is an extension number. |
|---|---|
| Step 2 | Scroll to the Dial Plan section. |
| Step 3 | Enter the digit sequences in the Dial Plan field. The default (US-based) systemwide dial plan appears automatically in the field. |
| Step 4 | You can delete digit sequences, add digit sequences, or replace the entire dial plan with a new dial plan. Separate each digit sequence with a pipe character, and enclose the entire set of digit sequences within parentheses. Example: (9,8<:1408>[2-9]xxxxxx \| 9,8,1[2-9]xxxxxxxxx \| 9,8,011xx. \| 9,8,xx.\|[1-8]xx) |
| Step 5 | Click Submit All Changes . The phone reboots. |
| Step 6 | Verify that you can successfully complete a call with each digit sequence that you entered in the dial plan. Note If you hear a reorder (fast busy) tone, review your entries and modify the dial plan appropriately. | Note | If you hear a reorder (fast busy) tone, review your entries and modify the dial plan appropriately. |
| Note | If you hear a reorder (fast busy) tone, review your entries and modify the dial plan appropriately. |

| Note | If you hear a reorder (fast busy) tone, review your entries and modify the dial plan appropriately. |
|---|---|

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | Set the Reorder Delay , Interdigit Long Timer , and Interdigit Short Timer parameters as described in the Control Timer Values (sec) table. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | Configure the values in the fields in the Time and Language sections. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | In the Time section, enter the time and date information. |
| Step 3 | Select Voice > User . |
| Step 4 | In the Supplementary Services , choose 12h or 24hr from the Time Format drop down list. Default: 12hr |
| Step 5 | Choose the date format from the Date Format drop down list. |
| Step 6 | Click Submit All Changes |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Date/Time . |
| Step 3 | Select Set current time manually . |
| Step 4 | Set the date and time in the format requested on the screen: YYYY MM DD HH MM |
| Step 5 | Select the OK softkey. |
| Step 6 | Select the Save softkey. |

| Parameter | Description |
|---|---|
| Set Local Date (mm/dd/yyyy) | Sets the local date (mm represents the month and dd represents the day). The year is optional and uses two or four digits. Default: Blank |
| Set Local Time (HH/mm) | Sets the local time (hh represents hours and mm represents minutes). Seconds are optional. Default: Blank |
| Time Zone | Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…,
                                                GMT, GMT+01:00, GMT+02:00, …, GMT+13:00. The time of the log messages and status messages are in UTC time and are not affected by the time zone setting. Default: GMT-08:00 |
| Time Offset (HH/mm) | This specifies the offset in 24-hour format from GMT to use for the local system time. The NTP Server time is expressed in GMT time. The local time is obtained by offsetting the GMT according to the time zone
                                                of the region. Default: 00/00 |
| Ignore DHCP Time Offset | When used with some routers that have DHCP with time offset values configured, the IP phone uses the router settings and ignores
                                                the IP phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset
                                                settings, choose yes for this option. If you choose no , the IP phone uses the router's DHCP time offset value. Default: Yes. |
| Daylight Saving Time Rule | Enter the rule for calculating daylight saving time. This rule is comprised of three fields. Each field is separated by a
                                                semicolon (;). Optional values inside brackets [ ] are assumed to be 0 if they are not specified. Midnight is represented
                                                by colons. For example,  0:0:0 of the given date. This is the format of the rule: Start = <start-time>; end=<end-time>; save = <save-time>. The <start-time> and <end-time> values specify the start and end dates and times of daylight saving time. Each value is in
                                                this format: <month> /<day> / <weekday>[/HH:[mm[:ss]]] The <save-time> value is the number of hours, minutes, and/or seconds to add to the current time during daylight saving time.
                                                The <save-time> value can be preceded by a negative (-) sign if subtraction is desired instead of addition. The <save-time>
                                                value is in this format: [/[+\|-]HH:[mm[:ss]]] The <month> value equals any value in the range 1-12 (January-December). The <day> value equals [+\|-] any value in the range 1-31. If <day> is -1, it means the <weekday> on or before the end of the month (in other words the last occurrence of < weekday>
                                                in that month). |
| Daylight Saving Time Rule (continued) | The <weekday> value equals any value in the range 1-7 (Monday-Sunday). It can also equal 0. If the <weekday> value is 0, this
                                                means that the date to start or end daylight saving is exactly the date given. In that case, the <day> value must not be negative.
                                                If the <weekday> value is not 0 and the <day> value is positive, then daylight saving starts or ends on the <weekday> value
                                                on or after the date given. If the <weekday> value is not 0 and the <day> value is negative, then daylight saving starts or
                                                ends on the <weekday> value on or before the date given. Where: HH stands for hours (0-23). mm stands for minutes (0-59). ss stands for seconds (0-59). Default: 3/-1/7/2;end=10/-1/7/2;save=1. |
| Daylight Saving Time Enable | Enables Daylight Saving Time. Default: Yes |
| Time Format | Choose the time format for the phone (12-hour or 24-hour). Default: 12hr |
| Date Format | Choose the date format for the phone (month/day or day/month). Default: month/day In the phone configuration XML file (cfg.xml), enter a string in this format: |

| Note | The time of the log messages and status messages are in UTC time. The time zone setting does not affect them. |
|---|---|

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | Set the Daylight Saving Time Enable drop-down list box to Yes . |
| Step 3 | In the Daylight Saving Time Rule field, enter the DST rule. This value affects the time stamp on the CallerID. |
| Step 4 | Click Submit All Changes . |

| ar-SA (Arabic) bg-BG (Bulgarian) ca-ES (Catalan) cs-CZ (Czech) da-DK (Danish) de-DE (German) el-GR (Greek) en-GB (English-Great Britain) en-US (English-United States) es-CO (Spanish-Colombia) es-ES (Spanish-Spain) fi-FI (Finnish) fr-CA (French-Canada) fr-FR (French) he-IL (Hebrew) hr-HR (Croatian) hu-HU (Hungarian) | it-IT (Italian) ja-JP (Japanese) ko-KR (Korean) nl-NL (Dutch) nn-NO (Norwegian) pl-PL (Polish) pt-PT (Portuguese) ru-RU (Russian) sk-SK (Slovak) sl-SI (Slovenian) sv-SE (Swedish) tr-TR (Turkish) zh-CN (Chinese) zh-HK (Chinese-Hong Kong SAR) |
|---|---|

| Note | To enable Latin and Cyrillic languages, you must not add a font file. |
|---|---|

| Step 1 | Download the locale zip file for your firmware version, from cisco.com. Place the file on your server, and unzip the file. Dictionaries and fonts for all the supported languages are included in the zip file. Dictionaries are XML scripts. Fonts are
                                                   standard TTF files. |
|---|---|
| Step 2 | On the phone administration web page, go to Admin Login > Advanced > Voice > Regional . In the Language section, specify the necessary parameters and values in the Dictionary Server Script field as described below. Use a semicolon (;) to separate multiple parameter and value pairs. Specify the location of the dictionary and font files with the serv parameter. For example: serv=http://server.example.com/Locales/ Make sure to include the IP address of the server, the path, and folder name. Example: serv=http://10.74.128.101/Locales/ For each language that you want to set up, specify a set of parameters as described below. Note In these parameter specifications, n denotes a serial number. This number determines the sequential order in which the language options are displayed in the Settings menu of the phone. 0 is reserved for US-English, which has a default dictionary. You can use it optionally, to specify your own dictionary. Use numbers starting with 1 for other languages. Specify the language name with the d n parameter. Example for language name for Asian language: d1=Chinese-Simplified Example for language name for German (Latin and Cyrillic): d2=German Example for language name for French (Latin and Cyrillic): d1=French Example for language name for French (Canada) (Latin and Cyrillic) language: d1=French-Canada Example for language name for Hebrew (RTL language): d1=Hebrew Example for language name for Arabic (RTL language): d1=Arabic This name is displayed as a language option in the Settings menu of the phone. Specify the name of the dictionary file with the x n parameter. Example for Asian language: x1=zh-CN_78xx_68xx-11.2.1.1004.xml; x1=zh-CN_88xx-11.2.1.1004.xml; Example for French (Latin and Cyrillic) languages: x1=fr-FR_78xx_68xx-11.2.1.1004.xml; x1=fr-FR_88xx-11.2.1.1004.xml; Example for Arabic (RTL language) language: x1=ar-SA_78xx_68xx-11.2.1.1004.xml; x1=ar-SA_88xx-11.2.1.1004.xml; Example for French (Canada) language: x1=fr-CA_78xx_68xx-11.3.6.0006.xml; x1=fr-CA_88xx-11.3.6.0006.xml; Ensure to specify the correct file for the language and phone model that you use. If a font is required for the language, specify the name of the font file with the f n parameter. For example: f1=zh-CN_78xx_68xx-11.2.1.1004.ttf; f1=zh-CN_88xx-11.2.1.1004.ttf; Make sure to specify the correct file for the language and phone model that you use. Note Font files with 'BMP' in the file name are for the Cisco IP Phone 7811. See Setup for Latin and Cyrillic Languages for specific details on setting up Latin languages. See Setup for an Asian Language for specific details on setting up an Asian language. See Setup for RTL Languages for specific details on setting up RTL languages. | Note | In these parameter specifications, n denotes a serial number. This number determines the sequential order in which the language options are displayed in the Settings menu of the phone. 0 is reserved for US-English, which has a default dictionary. You can use it optionally, to specify your own dictionary. Use numbers starting with 1 for other languages. | Note | Font files with 'BMP' in the file name are for the Cisco IP Phone 7811. |
| Note | In these parameter specifications, n denotes a serial number. This number determines the sequential order in which the language options are displayed in the Settings menu of the phone. 0 is reserved for US-English, which has a default dictionary. You can use it optionally, to specify your own dictionary. Use numbers starting with 1 for other languages. |
| Note | Font files with 'BMP' in the file name are for the Cisco IP Phone 7811. |
| Step 3 | Click Submit All Changes . |

| Note | In these parameter specifications, n denotes a serial number. This number determines the sequential order in which the language options are displayed in the Settings menu of the phone. 0 is reserved for US-English, which has a default dictionary. You can use it optionally, to specify your own dictionary. Use numbers starting with 1 for other languages. |
|---|---|

| Note | Font files with 'BMP' in the file name are for the Cisco IP Phone 7811. |
|---|---|

| Bulgarian Catalan Croatian Czech Danish Dutch English (UK) Finnish French (France) French (Canada) German Greek | Hungarian Italian Portuguese (Portugal) Norwegian Polish Russian Slovak Slovenian Spanish (Columbia) Spanish (Spain) Swedish Turkish Ukraine |
|---|---|

| Note | In the above examples http://10.74.128.101/Locales/ is a web folder. The dictionary files are extracted in this web folder and are used in the examples. |
|---|---|

| Note | Your users can select the language on the phone, from Settings > Device Administration > Language . |
|---|---|

| Step 1 | On the phone administration web page, go to Admin Login > Advanced > Voice > Regional , Language section. In the Language Selection field, specify the value of the appropriate d n parameter value from the Dictionary Server Script field, for the language of your choice. |
|---|---|
| Step 2 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Call Return Code | This code calls the last caller. Defaults to *69. |
| Blind Transfer Code | Begins a blind transfer of the current call to the extension specified after the activation code. Defaults to *95. |
| Cfwd All Act Code | Forwards all calls to the extension specified after the activation code. Defaults to *72. |
| Cfwd All Deact Code | Cancels call forward of all calls. Defaults to *73. |
| Cfwd Busy Act Code | Forwards busy calls to the extension specified after the activation code. Defaults to *90. |
| Cfwd Busy Deact Code | Cancels call forward of busy calls. Defaults to *91. |
| Cfwd No Ans Act Code | Forwards no-answer calls to the extension specified after the activation code. Defaults to *92. |
| Cfwd No Ans Deact Code | Cancels call forward of no-answer calls. Defaults to *93. |
| CW Act Code | Enables call waiting on all calls. Defaults to *56. |
| CW Deact Code | Disables call waiting on all calls. Defaults to *57. |
| CW Per Call Act Code | Enables call waiting for the next call. Defaults to *71. |
| CW Per Call Deact Code | Disables call waiting for the next call. Defaults to *70. |
| Block CID Act Code | Blocks caller ID on all outbound calls. Defaults to *61. |
| Block CID Deact Code | Removes caller ID blocking on all outbound calls. Defaults to *62. |
| Block CID Per Call Act Code | Removes caller ID blocking on the next inbound call. Defaults to *81. |
| Block CID Per Call Deact Code | Removes caller ID blocking on the next inbound call. Defaults to *82. |
| Block ANC Act Code | Blocks all anonymous calls. Defaults to *77. |
| Block ANC Deact Code | Removes blocking of all anonymous calls. Defaults to *87. |
| DND Act Code | Enables the do not disturb feature. Defaults to *78. |
| DND Deact Code | Disables the do not disturb feature. Defaults to *79. |
| Secure All Call Act Code | Makes all outbound calls secure. Defaults to *16. |
| Secure No Call Act Code | Makes all outbound calls not secure. Defaults to *17. |
| Secure One Call Act Code | Makes a secure call. Default: *18. |
| Secure One Call Deact Code | Disables secure call feature. Default: *19. |
| Paging Code | The star code used for paging the other clients in the group. Defaults to *96. |
| Call Park Code | The star code used for parking the current call. Defaults to *68. |
| Call Pickup Code | The star code used for picking up a ringing call. Defaults to *97. |
| Call Unpark Code | The star code used for picking up a call from the call park. Defaults to *88. |
| Group Call Pickup Code | The star code used for picking up a group call. Defaults to *98. |
| Exec Assistant Call Initiate Code | For executive assistants: Initiates a call on behalf of an executive from the user's (assistant's) extension. Default: #64 Applicable to Cisco IP Phone 6871 Multiplatform Phones only. |
| Exec Call Filter Act Code | For executives who have assistants: Activates call filtering. When call filtering is on, assistants receive incoming calls
                                             for executives. Default: #61 Applicable to Cisco IP Phone 6871 Multiplatform Phones only. |
| Exec Call Filter Deact Code | For executives who have assistants: Deactivates call filtering. Default: #62 Applicable to Cisco IP Phone 6871 Multiplatform Phones only. |
| Exec Assistant Call Push Code | For executive assistants: Transfers an ongoing call from the user (assistant) to the executive. Default: #63 Applicable to Cisco IP Phone 6871 Multiplatform Phones only. |
| Exec Call Retrieve Code | For executives who have assistants: Transfers an ongoing call from an assistant to the user (executive). For executive assistants: Transfers an ongoing call from the executive to the user (assistant). Default: *11 Applicable to Cisco IP Phone 6871 Multiplatform Phones only. |
| Exec Call Bridge Code | For executives who have assistants: Joins the user (executive) to an ongoing call with an assistant. For executive assistants: Joins the user (assistant) to an ongoing call with an executive. Default: *15 Applicable to Cisco IP Phone 6871 Multiplatform Phones only. |
| Important If you change any of the service activation codes used by executives or assistants, you must update the corresponding settings
                                                         in BroadWorks. | Important | If you change any of the service activation codes used by executives or assistants, you must update the corresponding settings
                                                         in BroadWorks. |
| Important | If you change any of the service activation codes used by executives or assistants, you must update the corresponding settings
                                                         in BroadWorks. |
| Referral Services Codes | These codes tell the IP phone what to do when the user places the current call on hold and is listening to the second dial
                                             tone. One or more *code can be configured into this parameter, such as *98, or *97\|*98\|*123, and so on. Max total length is 79 chars.
                                             This parameter applies when the user places the current call on hold (by Hook Flash) and is listening to second dial tone.
                                             Each *code (and the following valid target number according to current dial plan) entered on the second dial-tone triggers
                                             the phone to perform a blind transfer to a target number that is prepended by the service *code. For example, after the user dials *98, the IP phone plays a special dial tone called the Prompt Tone while waiting for the
                                             user the enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered,
                                             the phone sends a blind REFER to the holding party with the Refer-To target equals to *98<target_number>. This feature allows
                                             the phone to hand off a call to an application server to perform further processing, such as call park. The *codes should not conflict with any of the other vertical service codes internally processed by the IP phone. You can
                                             empty the corresponding *code that you do not want to the phone to process. |
| Feature Dial Services Codes | These codes tell the phone what to do when the user is listening to the first or second dial tone. One or more *code can be configured into this parameter, such as *72, or *72\|*74\|*67\|*82, and so forth. The maximum total
                                             length is 79 characters. This parameter applies when the user has a dial tone (first or second dial tone). Enter *code (and
                                             the following target number according to current dial plan) entered at the dial tone triggers the phone to call the target
                                             number prepended by the *code. For example, after user dials *72, the phone plays a prompt tone awaiting the user to enter
                                             a valid target number. When a complete number is entered, the phone sends a INVITE to *72<target_number> as in a normal call.
                                             This feature allows the proxy to process features like call forward (*72) or BLock Caller ID (*67). The *codes should not conflict with any of the other vertical service codes internally processed by the phone. You can empty
                                             the corresponding *code that you do not want to the phone to process. You can add a parameter to each *code in Features Dial Services Codes to indicate what tone to play after the *code is entered,
                                             such as *72‘c‘\|*67‘p‘. Below are a list of allowed tone parameters (note the use of back quotes surrounding the parameter
                                             without spaces) • c = Cfwd Dial Tone • d = Dial Tone • m = MWI Dial Tone • o = Outside Dial Tone • p = Prompt Dial Tone • s = Second Dial Tone • x = No tones are place, x is any digit not used above If no tone parameter is specified, the phone plays Prompt tone by default. If the *code is not to be followed by a phone number, such as *73 to cancel call forward, do not include it in this parameter.
                                             In that case, simple add that *code in the dial plan and the phone sends INVITE *73@..... as usual when user dials *73. |

| Important | If you change any of the service activation codes used by executives or assistants, you must update the corresponding settings
                                                         in BroadWorks. |
|---|---|