---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-1-english-configuration-guide-sw-confg-vg248swc-html-8ebbb99507
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_1/english/configuration/guide/sw_confg/vg248swc.html
retrieved_at: 2026-08-22T01:19:29.300376+00:00
---

Software Configuration Guide (Version 1.1)

# Software Configuration Guide (Version 1.1)

Updated: March 17, 2015

Chapter: Getting Started with the VG248

## Chapter: Getting Started with the VG248

## Getting Started with the VG248

Before you can configure the telephony features on the VG248 to interact with the analog phones, you must first configure the basic network, SNMP, and password settings. These settings enable the VG248 to connect to the IP network and help you manage the device.

These sections provide details about configuring these settings on the VG248:

• Accessing Configuration Options

• Restarting the VG248

• Configuring Network Settings

• Configuring Passwords

• Configuring SNMP Settings

## Accessing Configuration Options

You can access the VG248 configuration options, after the device has started up, using a console terminal connected to the RJ-45 console port or through a Telnet session.

### Using the Console Port

You might want to use the console port to connect to the VG248 when you initially install the device. This enables you to observe the initial startup procedure and manually assign an IP address and host name if you are not using DHCP.

To access the VG248 through the console RJ-45 port, perform these steps.

Step 1

Connect the console terminal to the console port.

See the Cisco VG248 Analog Phone Gateway Hardware Installation Guide .

Step 2

At the prompt, enter the password.

The VG248 does not have a default password. If no password has been configured, the main menu displays.

< password >

Step 3

Choose the necessary options to complete your desired tasks.

Choose the desired option from the menus.

Step 4

When finished, exit the session.

—

### Using Telnet

To access the VG248 through a Telnet session, you must know its IP address or host name. By default, the device uses DHCP. If you want to assign a specific IP address or host name, you must first configure the network settings using the console port before connecting through a Telnet session.

To access the VG248 from a remote host with Telnet, perform these steps:

Step 1

From the remote host, enter the telnet command and the host name or IP address of the VG248 that you want to access.

telnet hostname | ip_addr

Step 2

At the prompt, enter the password, if you have configured one.

The VG248 does not have a default password. If no password has been configured, the main menu displays.

< password >

Step 3

Choose the necessary options to complete your desired tasks.

Choose the desired option from the menus.

Step 4

When finished, exit the Telnet session

—

### Displaying the Main Menu

After connecting to the VG248 through the console port or a Telnet session, the main menu appears (see Figure 2-1 ). Follow these guidelines to navigate the menus:

• Use the arrow keys or numeric keypad to navigate the available options.

• Press Enter to choose an option.

• Press Esc to return to the previous menu.

Figure 2-1 VG248 Main Menu

## Restarting the VG248

Certain configuration changes to the VG248 do not take effect until you restart the device. To restart the VG248, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Restart .

## Configuring Network Settings

You must configure the network settings on the VG248 to connect it to the IP network. After configuring any network settings, you must restart the VG248. See the "Restarting the VG248" section .

### Configuring Ethernet

The VG248 fully supports 10/100 Mbps half- and full-duplex Ethernet. If you choose auto-negotiation, the VG248 automatically adjusts to the speed and duplex mode of the switch to which it is attached. This is the default and recommended setting.

Follow these steps to configure the VG248 as your network requires:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Ethernet .

Step 4 Choose the option that matches the setting on the switch to which the VG248 is connected:

• auto-negotiation

• 100Mb/s half duplex

• 100Mb/s full duplex

• 10Mb/s half duplex

• 10Mb/s full duplex

Step 5 Restart the VG248.

### Using DHCP

If you are using Dynamic Host Configuration Protocol (DHCP) in your network, the VG248 automatically obtains an IP address when you connect it to the network. Although the VG248 uses DHCP by default, you can disable DHCP and manually assign an IP address to the VG248.

To use DHCP, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Use DHCP .

Step 4 Press Enter to toggle between yes (use DHCP) and no (do not use DHCP).

If you use DHCP, you can only modify the host name; you cannot modify the other network settings. See the "Setting the Host Name" section for details.

If you do not use DHCP, you must enter the additional network settings. See these sections for details:

• Setting the Host Name

• Setting the IP Address

• Setting the Subnet Mask

• Setting the Default Router

• Setting the DNS Server

• Setting the Domain Name

### Renewing IP Address from DHCP

You might need to renew the IP address automatically assigned to the VG248. For example, if you have changed the physical location of the VG248 from one subnet to another or if you need assistance troubleshooting a connectivity problem.

To renew an IP address assigned by DHCP, follow these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Renew DHCP .

### Setting the Host Name

The host name identifies each VG248 on your TCP/IP network, enabling you to access the device using this name rather than the IP address.

By default, this value is set to be the same as the device name registered in the Cisco CallManager database. This device name is a unique character string generated based on the MAC address for the VG248 (see the "Adding the VG248 to Cisco CallManager" section for details). However, you can use this setting to modify the host name.

To change the host name, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Host name .

Step 4 Enter the host name to be used by the VG248.

Step 5 Restart the VG248.

### Setting the IP Address

The IP address identifies each VG248 on your TCP/IP network. You must enter the IP address if you are not using DHCP. The VG248 automatically obtains an IP address if you are using DHCP.

To assign an IP address, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose IP address .

Step 4 Enter the IP address to be used by the VG248.

Step 5 Restart the VG248.

### Setting the Subnet Mask

You must enter the subnet mask if you are not using DHCP. The VG248 automatically obtains a subnet mask if you are using DHCP.

To set the subnet mask, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Subnet mask .

Step 4 Enter the subnet mask.

Step 5 Restart the VG248.

### Setting the Default Router

You must enter the default router if you are not using DHCP. The VG248 automatically obtains a default router if you are using DHCP.

To set the default router, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Default router .

Step 4 Enter the IP address of the default router.

Step 5 Restart the VG248.

### Setting the DNS Server

Domain Name System (DNS) allows users to specify remote computers by host names. The VG248 uses DNS to resolve the host name of TFTP servers and Cisco CallManager systems when the system is configured to use names rather than IP addresses.

To set the DNS server, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose DNS server .

Step 4 Enter the IP address of the DNS server.

Step 5 Restart the VG248.

Tips You can enter a secondary DNS server by choosing Network interface > DNS server 2 and entering the IP address.

### Setting the Domain Name

The domain name is the name of the Domain Name System (DNS) domain in which the VG248 is located.

To set the domain name, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Domain name .

Step 4 Enter the domain name.

Step 5 Restart the VG248.

### Enabling CDP

The VG248 can advertise itself to other network devices using Cisco Discovery Protocol (CDP). Many network management applications require that CDP is enabled.

To enable CDP, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose CDP .

Step 4 Press Enter to toggle between enabled and disabled .

### Setting DSCP Quality of Service Values

Differentiated Services Code Point (DSCP) is an IETF standard that uses 6 bits in the IPv4 header's ToS (Type of Service) field to specify the class of service for each packet. This enables you to apply differentiated grades of service to different packet types.

You can modify the assigned DSCP Quality of Service (QoS) value for certain types of traffic. This enables you to give priority to media traffic over control traffic.

To enable modify the DSCP QoS values, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Network interface .

Step 3 Choose Set DSCP QoS values .

Step 4 Choose one of the following options:

• Media traffic —RTP packets carrying voice, fax, and modem calls

• Control traffic —SCCP data packets carrying telephony control data

• All other traffic —such as FTP, HTTP, SNMP, and so on

Step 5 Enter the new value for Media traffic or Control traffic from 0 to 63, using decimal format.

By default, Media traffic is set to 46, and Control traffic is set to 26. You cannot change the value for All other traffic ; it is set to 0.

## Configuring Passwords

The VG248 ships without a set or enabled password. You should enable passwords to prevent unauthorized access to and control of the VG248. The VG248 does not support or use user names.

Once you set a password, however, the VG248 requires that you use it, whether you are accessing the device using the console port, telnet, HTTP, or FTP. When using the HTTP, you are required to enter the login password if one is set; you cannot modify any settings when accessing the VG248 using HTTP. When accessing the VG248 using FTP, the FTP server adopts the highest level of security currently set. For example, if you have set both a login and enable password, you must use the enable password to use FTP.

### Configuring the Login Password

The login password enables you or other users to view the current status of the VG248. To configure the login password, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Passwords .

Step 3 Choose Login password .

Step 4 Enter the new password.

### Configuring the Enable Password

The enable password allows you to view current settings and make changes to the VG248. Once set, you must use the enable password to make changes to the VG248.

To configure the enable password, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Passwords .

Step 3 Choose Enable passwor d .

Step 4 Enter the new password.

## Configuring SNMP Settings

The VG248 supports Simple Network Management Protocol (SNMP) by supporting standard MIBs. Modify the SNMP settings as appropriate for your network management needs. You need to configure the SNMP settings if you want to manage the VG248 remotely.

### Setting Community Strings

The community string settings enable network management systems to access the VG248 for remote management.

You can configure a read-only password, which restricts access to the device, allowing users to view information but not to make changes. You can also configure a read-write community string, which allows users to make changes to the device remotely.

By default, the read-only community string is set to public , which provides read-only access. If you do not set these community strings on the VG248, you cannot manage the device remotely using the Simple Network Management Protocol (SNMP).

To set the community strings, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose SNMP .

Step 3 To set the read-only community string, choose Read-only community string .

Step 4 To set the read-write community string, choose Read-write community string .

Step 5 Enter the community string value.

### Configuring Contact Information

You can enter the contact name of the person responsible for the VG248 and the location of the VG248 on your campus.

### Configuring Contact Name

The contact name on the VG248 corresponds to the sysContact variable defined in RFC 1213.

To add a contact name indicating the person responsible for the VG248, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose SNMP .

Step 3 Choose Contact name .

Step 4 Enter the name of the person responsible for the VG248.

### Configuring System Name

The system name on the VG248 corresponds to the sysName variable defined in RFC 1213.

To specify the system name of the VG248 to the network management system perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose SNMP .

Step 3 Choose System name .

Step 4 Enter the system name of the VG248.

### Configuring Location

The location on the VG248 corresponds to the sysLocation variable defined in RFC 1213.

To add the location of the VG248 in your network or on your site, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose SNMP .

Step 3 Choose Location .

Step 4 Enter the location of the VG248.

### Configuring Trap Settings

You can configure the VG248 to notify up to four network management systems when certain significant system events occur. You can also specify the IP address for the network management system that is acting as a trap receiver. See the "Understanding Trap Support" section on page 1-11 for information about supported trap types.

### Enabling Authentication Traps

To enable authentication traps, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose SNMP .

Step 3 Choose Generate authentication traps .

Step 4 Press Enter to toggle between yes and no .

### Configuring Trap Receiver Stations

To set up to four trap receiver stations, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose SNMP .

Step 3 Choose Trap receiver stations .

Step 4 Enter the IP address or host name of the network management system used to receive the traps.

|  | Task | Description |
|---|---|---|
| Step 1 | Connect the console terminal to the console port. | See the Cisco VG248 Analog Phone Gateway Hardware Installation Guide . |
| Step 2 | At the prompt, enter the password. The VG248 does not have a default password. If no password has been configured, the main menu displays. | < password > |
| Step 3 | Choose the necessary options to complete your desired tasks. | Choose the desired option from the menus. |
| Step 4 | When finished, exit the session. | — |

|  | Task | Command |
|---|---|---|
| Step 1 | From the remote host, enter the telnet command and the host name or IP address of the VG248 that you want to access. | telnet hostname \| ip_addr |
| Step 2 | At the prompt, enter the password, if you have configured one. The VG248 does not have a default password. If no password has been configured, the main menu displays. | < password > |
| Step 3 | Choose the necessary options to complete your desired tasks. | Choose the desired option from the menus. |
| Step 4 | When finished, exit the Telnet session | — |