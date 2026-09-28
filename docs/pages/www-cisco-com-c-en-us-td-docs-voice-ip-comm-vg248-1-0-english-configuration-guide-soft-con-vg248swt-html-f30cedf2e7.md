---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-0-english-configuration-guide-soft-con-vg248swt-html-f30cedf2e7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_0/english/configuration/guide/soft_con/vg248swt.html
retrieved_at: 2026-08-22T01:20:14.798561+00:00
---

Software Configuration Guide (Version 1.0)

# Software Configuration Guide (Version 1.0)

Updated: March 17, 2015

Chapter: Troubleshooting the VG248

## Chapter: Troubleshooting the VG248

## Troubleshooting the VG248

The VG248 includes several built-in troubleshooting and diagnostic features. Use these sections for details about troubleshooting:

• Troubleshooting Hardware Errors

• Troubleshooting Software Errors

• Upgrading Software Images

• Verifying Network Connectivity

• Displaying Status and Configuration Settings

• Monitoring System Status Remotely

• Working with the Event Log

## Troubleshooting Hardware Errors

The VG248 can identify some potential hardware problems with the fans, power supplies, the operating temperature, and other hardware systems.

These sections provide information about how the VG248 identifies these potential problems and how to resolve them:

• Displaying Hardware Status

• Identifying Fan Faults

• Identifying Power Supply Faults

• Monitoring Internal Operating Temperature

• Connecting Too Many Phones to the VG248

• Resolving Additional Hardware Errors

### Displaying Hardware Status

If potential hardware failures are detected, warning messages appear on the main interface window. However, you can also proactively monitor the current operating environment on the VG248. To do this, follow these steps:

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Show environment .

The following information about the VG248 displays:

• Internal temperature

• 1.8 volts supply

• 3.3 volts supply

• 5.0 volts supply

• 12.0 volts supply

• 48.0 volts supply

• 96.0 volts supply

• Chassis fan state

The voltages and temperatures are indicated with the actual values and "okay", "too high", or "too low" annotating the values. The fan status is identified as "okay" or "faulty".

### Identifying Fan Faults

If a fan fault is reported, it indicates that one (or more) of the fans is not functioning. You should verify that nothing is lodged in the holes in the rear of the device, but do not make any attempt to open the device or move the fans. You should contact a technical support representative from Cisco Systems for assistance.

### Identifying Power Supply Faults

The internal DC supply voltages are measured continuously (+1.8v, +3.3v, +5.0v, +12.0v, -48v, -96v).

The 1.8v and 3.3v voltages must be within +/- 6% of nominal, and the others must be within +/- 10%. If any of these values are outside this range, then the VG248 reports a power supply fault.

If the phone power supplies (-48v and -96v) fail, it might indicate that the VG248 is overloaded. Verify that you have not exceeded the maximum ringer equivalency number (REN) load for each line. You should only have a maximum of three (3) phones per line.

If one of the other power supplies fails, you should contact a Cisco technical representative for assistance.

### Monitoring Internal Operating Temperature

The VG248 monitors its internal temperature to ensure that it is operating within the specified limits (the ambient operating environment should be 0° to 40° C or 32° to 104° F). If the VG248 identifies internal temperatures too low or too high, it generates warning messages. Continuing to operate at ranges exceeding these limits (either too low or too high) can damage the VG248.

If the operating temperature of the VG248 is too low, there is a risk of condensation forming inside the device. You should move the device to a warmer location to prevent this.

If the operating temperature of the VG248 is too high, you should move the device to a cooler location with improved ventilation. The internal fans on the VG248 maintain the internal temperature consistent with the ambient environment. Therefore, if the device is in a location that is too warm, its internal temperature is more likely to exceed the limits. There are two levels of high temperature alert:

• yellow alert—generates and logs an error, but enables the device to continue functioning

• red alert—causes all the phones to be immediately shut down, causing calls to drop and preventing calls from being made. You must manually restart the VG248 either by selecting Configure > Restar t or by disconnecting power to the device.

### Connecting Too Many Phones to the VG248

The VG248 has a maximum ringer equivalency number (REN) load of three (3) analog devices per line (using a shared directory number), and only two of these devices can be off-hook at any one time. If these requirements are ignored, you might experience reduced quality on these analog phones, including:

• Difficulty hearing caller—Users have too many phones off-hook. Do not have more than two phones per line off-hook simultaneously.

• Dialing or caller ID are not working properly—Users have too many phones off-hook. Do not have more than two phones per line off-hook simultaneously.

• Phones not ringing properly or at all—REN load has been exceeded. Do not connect more than three analog devices per line.

• Phone power supplies (-48v and -96v) fail—REN load has been exceeded. Do not connect more than three analog devices per line. See the "Identifying Power Supply Faults" section for additional information.

### Resolving Additional Hardware Errors

Table 5-1 describes errors and warnings that might appear on the VG248 either on-screen or in the event log (see the "Working with the Event Log" section for details on accessing the event log) which are caused by a hardware fault. Use this information to resolve these errors.

Table 5-1 Hardware Errors and Warnings Explanation

DSP

DSP X on SIM Y has failed

One of the Digital Signal Processor (DSP) chips inside the VG248 has failed.

Contact a Cisco technical representative for assistance.

DSP

DSP X, SIM Y failed to boot

OS

Ethernet has gone down

Ethernet has gone down at the physical level.

Verify that the Ethernet cable is properly connected to the VG248 and that the hub or switch to which it is connected is up and running properly.

SCCP

Failed to update real-time clock

The on-board real-time clock in the VG248 has failed to set the time from Cisco CallManager.

Contact a Cisco technical representative for assistance.

SLIC

EDSP failure warning received

A transient fault has been detected in the SLICs (the hardware that drives the analog telephony interfaces).

If these messages persist, contact a Cisco technical representative for assistance.

SLIC

over-temperature warning received

## Troubleshooting Software Errors

The VG248 displays informational messages and errors on-screen or in the event log ((see the "Working with the Event Log" section for details on accessing the event log), which indicate potential software problems, such as misconfiguration, time-outs, unreachable servers, and so on.

The following sections provide details about resolving these errors:

• Resolving Network and System Errors

• Resolving Analog Errors

• Resolving Cisco CallManager Errors

### Resolving Network and System Errors

Table 5-2 describes errors and warnings that might appear on the VG248 either on-screen or in the event log (see the "Working with the Event Log" section for details on accessing the event log), which are caused by a misconfiguration or miscommunication with the network or system settings. Use this information to resolve these errors.

Table 5-2 Network and System Errors and Warnings Explanation

DHCP

IP address refused

The DHCP server rejected the VG248's request for an IP address.

Check configuration of DHCP server. If errors persist, assign a static IP address. Refer to the "Configuring Network Settings" section for details on assigning a static IP address.

DHCP

IP address cannot be allocated

No DHCP server responded to the request.

Check configuration of DHCP server. If errors persist, assign a static IP address. Refer to the "Configuring Network Settings" section for details on assigning a static IP address.

DHCP

Static IP address conflict with device <address>

The VG248 has a static IP address that is already assigned to another device on the network.

Assign a different static IP address for either the VG248 or the conflicting device. Refer to the "Configuring Network Settings" section for details on assigning a static IP address.

DHCP

IP address conflict with device <address>

The DHCP server allocated an IP address to the VG248 that is already in use by another device on the network.

1. Check your DHCP server configuration to ensure that addresses allocated are not reserved for static IP use.

2. Check your network for misconfigured devices.

DHCP

Network interface will be shut down

A previous error caused the network interface to be shut down.

Check the event log for errors.

DHCP

Invalid TFTP information received from DHCP server

Although the VG248 received TFTP information from the DHCP server, it was not valid.

The VG248 might not have enough information to retrieve telephony port configuration or register with Cisco CallManager.

Check configuration of DHCP server. If errors persist, assign a static IP address and manually enter settings for the TFTP server. Refer to the "Configuring Network Settings" section for details on assigning a static IP address.

DNS

No response from primary server

The DNS server failed to respond to one or more requests from the VG248.

1. If the VG248 has a static IP address, verify the DNS server has been configured. Refer to the "Setting the DNS Server" section for details.

2. Verify that the DNS server is working properly.

DNS

Server address not configured

A DNS query has been attempted, but no DNS server has been configured.

1. If the VG248 has a static IP address, verify the DNS server has been configured. Refer to the "Setting the DNS Server" section for details.

2. If you are using DHCP, the DHCP server has not provided a DNS server. Check the DHCP server configuration.

FTP

Invalid password entered

An attempt was made to connect to the VG248 via FTP with the wrong password.

Verify that you have entered the password for the highest level of security currently set. When using FTP, if you have both a login and an enable password set, you must use the enable password.

Refer to the "Configuring Passwords" section for details.

FTP

Required password absent

An attempt was made to connect to the VG248 via FTP without a password when one was required.

When using FTP, if you have both a login and an enable password set, you must use the enable password.

Refer to the "Configuring Passwords" section for details.

FTP

Partial download aborted

An attempt to download a file onto the VG248 was interrupted before the entire file was transferred.

The resulting partial file has been deleted from the filing system on the VG248.

Reattempt the file transfer.

OS

Ethernet failed to start

The Ethernet cable is not properly connected to the VG248 or to the hub or switch.

Check the Ethernet cable and reconnect it to the VG248 and the hub or switch. If error persists, replace cable.

OS

Incorrect password entered

A user attempted to use a telnet, console, or FTP connection to the VG248 but entered an incorrect password.

Check the passwords and verify that you are using the correct one.

Change the password if you suspect an unauthorized login attempt. Refer to the "Configuring Passwords" section for details.

SNMP

Attempt to use Get with invalid community name " <name> "

The VG248 received an SNMP request with an invalid read-only community name (password).

Check the community string setting on the VG248 and ensure that your network management system has the correct password.

Refer to the "Configuring SNMP Settings" section for details.

SNMP

Attempt to use Set with invalid community name " <name> "

The VG248 received an SNMP request with an invalid read-write community name (password).

Check the community string setting on the VG248 and ensure that your network management system has the correct password.

Refer to the "Configuring SNMP Settings" section for details.

SNMP

Received invalid packet

The SNMP server received an invalid SNMP request.

Verify that your network management system is set up properly.

TFTP

Timeout

The VG248 is unable to retrieve a file using TFTP.

These errors might occur if the network is busy. The errors should resolve themselves when the network load reduces.

TFTP

TFTP: Rx error

### Resolving Analog Errors

Table 5-3 describes errors and warnings that might appear on the VG248 either on-screen or in the event log (see the "Working with the Event Log" section for details on accessing the event log), which are caused by a misconfiguration or miscommunication with the analog phones or features. Use this information to resolve these errors.

Table 5-3 Analog Errors and Warnings Explanation

POTS

Feature codes: X same as Y

You have configured the telephone feature codes such that the code for one operation (such as speed dial) is the same as for another (such as call forward).

Users will not be able to use one of these operations. You must set unique feature codes for each operation.

To prohibit users from performing an operation, leave the feature code setting empty. See the "Assigning Feature Codes" section for details.

POTS

Feature codes: X precludes Y

You have configured the telephone feature codes in such a way that the code for one operation completely masks that for a second operation.

For example, if the feature code for speed dial 1 is*** and the code for speed dial 2 is ****, you could never use speed dial 2. Instead, as soon you dial the third *, speed dial 1 activates.

Do not assign features codes that might mask other operations.

See the "Assigning Feature Codes" section for details.

### Resolving Cisco CallManager Errors

Table 5-4 describes errors and warnings that might appear on the VG248 either on-screen or in the event log (see the "Working with the Event Log" section for details on accessing the event log), which are caused by a misconfiguration or miscommunication with the Cisco CallManager system. Use this information to resolve these errors.

Table 5-4 Cisco CallManager Errors and Warnings Explanation

SCCP

Registration failed: X

This message, associated with a particular port (1 - 48), indicates that the port had difficulty registering itself with Cisco CallManager.

If a port is not properly registered, then you cannot make phone calls using it.

The reason that registration with Cisco CallManager failed is indicated in the message.

If the port cannot successfully register, verify that the port is properly configured in Cisco CallManager.

See "Configuring the VG248 Ports" section for details.

SCCP

Registration failures; last reason X

SCCP

Attempt to use; currently disabled

A user has attempted to use a telephone handset attached to a VG248 port, which is currently disabled.

To allow the user to make and receive calls, you must enable the port so it can register with Cisco CallManager.

See "Setting the Port Enable Policy" section for details.

SCCP

TFTP failed; using last known good configuration

A port on the VG248 has failed to retrieve its configuration using TFTP. Instead, the VG248 is using the configuration stored last time the port successfully registered with Cisco CallManager.

No action is required. However, this message might indicate a potential problem with connectivity to the TFTP server. Verify that the TFTP server is up and running.

SCCP

No TFTP server address

The TFTP server has not been set.

1. If using DHCP to obtain TFTP server, check your DHCP server configuration.

2. If you want to use a fixed TFTP server, you must configure it on the VG248 Refer to the "Identifying the Cisco CallManager TFTP Server" section to assign a TFTP server for details.

SCCP

Unable to resolve TFTP server name

The VG248 was not able to locate the TFTP server.

Verify the name of the TFTP server the VG248 is attempting to locate using Display > System Status .

• If using DHCP, check the configuration on the DHCP server to verify that it is returning a valid TFTP server name to the VG248.

• If you are using a fixed TFTP server, verify the configured server name using Configure -> Telephony > CallManager TFTP server .

## Upgrading Software Images

The VG248 has two software images: a main software image and a boot loader. If necessary, you can upgrade these software images.

### Upgrading the Main Image

The main software image might need to be updated if a new release is available on CCO as a bug update or feature enhancement.

To upgrade the main software image, perform these steps:

Step 1 Obtain a configuration file whose name is in the following format: vgc-main. <version> .tar , where <version> indicates the release number, such as 1-0-1.

Step 2 Connect to the VG248 using FTP.

Step 3 Send the configuration file to the VG248 using FTP.

Step 4 Restart the VG248 for the new image to take effect.

Step 5 From the main menu on the VG248, choose Display .

Step 6 Choose Version to verify the updated version has been installed.

### Upgrading the Boot Loader

The boot loader is the initial startup image. You should not upgrade this image unless instructed to do so by a Cisco technical representative.

To upgrade the boot loader image, perform these steps:

Step 1 Obtain a configuration file whose name is in the following format: vgc-load. <version> .bin , where <version> indicates the release number, such as 1-0-1.

Step 2 Connect to the VG248 using FTP.

Step 3 Send the configuration file to the VG248 using FTP.

You must use a destination name that begins with "boot:". For example:

```
put vgc-load.< version >.bin boot:loader
```

Step 4 After the FTP command has completed successfully, restart the VG248 for the changes to take effect.

Step 5 Once the VG248 has restarted, choose Display > Version to verify that the updated version has been installed.

### Resolving an Incomplete Upgrade

If you initiated an upgrade to the main software image, but terminated it before the FTP transfer of the new image completed, the VG248 might not start up properly.

If this occurred, the next time the VG248 starts up, one of the following occurs:

• The boot loader loads, but the VG248 waits indefinitely at the Pausing for FTP prompt.

• The VG248 partially loads the main image, pauses, and then restarts.

To resolve either of these errors (while connected to the VG248 boot loader), use the console port to establish an FTP session and transfer the main image file again, following the steps in the "Upgrading the Main Image" section .

## Verifying Network Connectivity

To verify that the VG248 is connected to and communicating with your network, you can attempt to ping another device on the network. Follow these steps to ping another device from the VG248:

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Ping network host .

Step 3 Enter the IP address or host name of the device.

The VG248 makes an attempt to reach the device once every second.

Step 4 Press Esc to exit.

## Displaying Status and Configuration Settings

Use these sections to obtain information about the current status and settings of the VG248 and its connections:

• Displaying System Status

• Displaying Network Statistics

• Displaying Port Status

• Displaying Detailed Port Status

• Displaying Port Statistics

• Displaying Current Configuration

• Displaying Software Version

### Displaying System Status

The system status provides an overview of the current network settings on the VG248. Use this procedure to quickly check your network settings and connectivity information.

To display system status, perform these steps:

Step 1 From the main screen, choose Display .

Step 2 Choose System status .

The system status displays:

• Up time

• Real time clock

• Serial number

• Ethernet MAC address

• IP address

• Subnet mask

• Default router

• DNS server

• TFTP server

• Syslog server

• Domain

• Ethernet speed and duplex

### Displaying Network Statistics

Use the network statistics to observe the network traffic and packet errors through the IP connection on the VG248.

To display network statistics, perform these steps:

Step 1 From the main screen, choose Display .

Step 2 Choose Network statistics .

These statistics display:

• Octets

• Unicast packets

• Nonunicast packets

• Discarded packets

Tips Press the Tab key to reset the network statistics while viewing.

### Displaying Port Status

The port status provides detailed information about each port on the VG248. This is useful when determining the current state of and activity on a particular port.

To display port status, perform these steps:

Step 1 From the main screen, choose Display .

Step 2 Choose Port status .

The Port status indicates information about the status of the handset of the analog device connected to the port and about the link to Cisco CallManager.

Step 3 Use the information in Table 5-5 to interpret the port status.

Table 5-5 Port Status

OnHook

Not currently in use.

OffHook

User has lifted the handset.

Ringing

Incoming call to this port.

OnCall

A call has been established and voice packets are moving across the network.

Down

Link is not up (either because the port is not enabled or because of a temporary failure).

Register

Port is registering with Cisco CallManager

<directory number>

Directory number for the port displays indicating that the port is up and available for use.

Unregister

Unregistering from Cisco CallManager. Displays if port is being disabled or reset.

PeerInUse

The port's directory number is in use by another phone that shares the directory number. The port is not available for use while a call is active on the other phone.

KeepCall

The Cisco CallManager link has gone down, but the call that was in progress is being maintained.

### Displaying Detailed Port Status

Step 1 From the main screen, choose Display .

Step 2 Choose Port status .

Step 3 Use the arrow keys to select one of the ports and press Enter.

Step 4 Use the information in Table 5-6 to interpret the port status.

Table 5-6 Cisco CallManager Port Status

CallManager link

Status of the connection to Cisco CallManager

TFTP server

Host name or IP address of the TFTP server

Device name

Device name of the port as it appears in Cisco CallManager

Directory number

Extension number assigned to the analog device connected to this port

Forwarded to

Directory number to which calls are being forwarded

Call state

Status of the port from a user's viewpoint.

Remote party

Directory name and number of caller

Remote address

IP address and port of caller

Codec in use

Codec being used by Cisco CallManager:

• G.729A

• G.711 mu-law

• G.711 a-law.

MWI

Whether the message waiting indicator for this port is on or off

CallManager name

DNS name of the Cisco CallManager host

CallManager IP address

IP address of Cisco CallManager

CallManager state

Status of connection to Cisco CallManager:

• Active—connected to this Cisco CallManager and using this connection for SCCP communication.

• Connecting—in the process of connecting to this Cisco CallManager

• Idle—this Cisco CallManager is not being used

• Standby—connected to this Cisco CallManager but not currently using the connection. Can use connection if active connection fails.

• Pending—attempting to make this Cisco CallManager the active connection as soon as possible.

CallManager type

Type of Cisco CallManager system:

• Normal—typical Cisco CallManager system

• Failover—Cisco CallManager system reserved for failover situations

### Displaying Port Statistics

Step 1 From the main screen, choose Display .

Step 2 Choose Port status .

Step 3 Use the arrow keys to select one of the ports and press Enter.

Step 4 Press the space bar.

These statistics display for the current call:

• Tx packets

• Rx packets

• Call time

• Rx bad sequence

• Rx bad headers

• Rx packets late

• Rx packets early

These statistics display for the call history:

• Incoming calls

• Outgoing calls

• Connected calls

### Displaying Current Configuration

You can quickly display all the settings you have configured on the VG248.

To display the configured settings, perform these steps:

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Show configuration .

### Displaying Software Version

Step 1 From the main screen, choose Display .

Step 2 Choose Version .

## Monitoring System Status Remotely

The VG248 includes a web server allowing you to monitor system status remotely using a web browser application. These options are identical to the settings accessible via the VG248 user interface directly.

Follow these steps to monitor the system status remotely:

Step 1 From a web browser window, enter the IP address or host name of the VG248.

Step 2 Do one of the following:

a. Click a phone icon to display status for the port. See the "Displaying Port Status" section for details.

b. Choose these options to display system status:

• Network configuration—See the "Displaying Current Configuration" section for details.

• Network statistics—See the "Displaying Network Statistics" section for details.

• Port status—See the "Displaying Port Status" section for details.

• Port statistics—See the "Displaying Port Statistics" section for details.

• Version information—See the "Displaying Software Version" section for details.

• Event log—See the "Working with the Event Log" section for details.

## Working with the Event Log

The event log enables you to capture errors, warnings, and other informational messages from the VG248. Typically, you use these options only when troubleshooting a complex issue, perhaps while working with a Cisco technical representative.

However, using the default settings and these options, you can resolve many errors on your own:

• Identifying a Syslog Server

• Selecting Logging Levels and Logged Ports

• Displaying Recent Messages

• Understanding Sub-Systems on the VG248

• Resolving Incorrect Date and Time in Event Log

### Identifying a Syslog Server

You can identify a syslog server to automatically capture and receive event logs for remote network management.

### Enabling Syslog

You can assign a syslog server to the VG248 using DHCP or by identifying a specific syslog server.

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Event log .

Step 3 Choose Syslog .

Step 4 Choose from the following options:

• inactive —syslog disabled

• use server from DHCP —syslog server determined by DHCP

• use specified server —syslog server must be specified (see the "Identifying a Specific Syslog Server" section )

### Identifying a Specific Syslog Server

If you want to use a specific syslog server, you must enter its IP address by performing these steps:

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Event log .

Step 3 Choose Syslog server .

Step 4 Enter the IP address or host name of the network management system you want to designate as the syslog server.

### Selecting Logging Levels and Logged Ports

You can set the VG248 to log progressively more detail (information, errors, or warnings), or you can restrict logging to specific ports.

Typically, you should configure these options only when working with a Cisco technical representative because the nature of the problem determines the amount of information required to resolve it.

To set logging levels or select ports, perform these steps:

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Event log .

Step 3 Choose Set logging levels or Set logged ports .

Step 4 Work with a Cisco technical representative to determine the best options to select and enter.

### Displaying Recent Messages

You can obtain a list of recent messages from the VG248 to help you resolve some configuration issues.

To display recent messages, perform these steps:

Step 1 From the main screen, choose Diagnostics .

Step 2 Choose Event log .

Step 3 Choose View recent to display recent messages.

Step 4 See "Understanding Sub-Systems on the VG248" section for information on resolving these errors.

Tips You can also select View all to display all errors, or View new to display new errors only.

### Understanding Sub-Systems on the VG248

The VG248 generates informational and warning messages and errors from different sub-systems in its software. Many of these messages do not require any intervention on your part; the device simply notifies you of changes or update. Other errors and warnings require additional troubleshooting or configuration.

Table 5-7 provides an overview of the different sub-systems on the VG248 that might generate informational or warning messages.

Table 5-7 VG248 Sub-Systems

DHCP

Communicates with DHCP server.

Ethernet

Concerned with low-level network link integrity.

OS

Runs the low-level services of the VG248.

FTP

Used to send new software images to the VG248.

DNS

Resolves host names to IP addresses.

TFTP

Handles retrieval of Cisco CallManager port configuration.

SLIC

Detects events from analog handsets.

DSP

Provides digital signal processing.

POTS

Bridges between analog and IP telephony.

SCCP

Transmits and receives telephony events over the IP network; communicates with Cisco CallManager.

SNMP

Coordinates SNMP communication.

### Resolving Incorrect Date and Time in Event Log

The VG248 has a built-in real time clock that synchronizes itself periodically with Cisco CallManager to obtain the correct date and time.

The VG248 must have at least one port enabled and registered with Cisco CallManager. You should also verify that the time settings on the Cisco CallManager system are correct.

See the "Enabling a Specific Port" section for assistance on enabling and registering ports in Cisco CallManager.

| System | Error | Explanation | Action |
|---|---|---|---|
| DSP | DSP X on SIM Y has failed | One of the Digital Signal Processor (DSP) chips inside the VG248 has failed. | Contact a Cisco technical representative for assistance. |
| DSP | DSP X, SIM Y failed to boot |
| OS | Ethernet has gone down | Ethernet has gone down at the physical level. | Verify that the Ethernet cable is properly connected to the VG248 and that the hub or switch to which it is connected is up and running properly. |
| SCCP | Failed to update real-time clock | The on-board real-time clock in the VG248 has failed to set the time from Cisco CallManager. | Contact a Cisco technical representative for assistance. |
| SLIC | EDSP failure warning received | A transient fault has been detected in the SLICs (the hardware that drives the analog telephony interfaces). | If these messages persist, contact a Cisco technical representative for assistance. |
| SLIC | over-temperature warning received |

| System | Error | Explanation | Action |
|---|---|---|---|
| DHCP | IP address refused | The DHCP server rejected the VG248's request for an IP address. | Check configuration of DHCP server. If errors persist, assign a static IP address. Refer to the "Configuring Network Settings" section for details on assigning a static IP address. |
| DHCP | IP address cannot be allocated | No DHCP server responded to the request. | Check configuration of DHCP server. If errors persist, assign a static IP address. Refer to the "Configuring Network Settings" section for details on assigning a static IP address. |
| DHCP | Static IP address conflict with device <address> | The VG248 has a static IP address that is already assigned to another device on the network. | Assign a different static IP address for either the VG248 or the conflicting device. Refer to the "Configuring Network Settings" section for details on assigning a static IP address. |
| DHCP | IP address conflict with device <address> | The DHCP server allocated an IP address to the VG248 that is already in use by another device on the network. | 1. Check your DHCP server configuration to ensure that addresses allocated are not reserved for static IP use. 2. Check your network for misconfigured devices. |
| DHCP | Network interface will be shut down | A previous error caused the network interface to be shut down. | Check the event log for errors. |
| DHCP | Invalid TFTP information received from DHCP server | Although the VG248 received TFTP information from the DHCP server, it was not valid. The VG248 might not have enough information to retrieve telephony port configuration or register with Cisco CallManager. | Check configuration of DHCP server. If errors persist, assign a static IP address and manually enter settings for the TFTP server. Refer to the "Configuring Network Settings" section for details on assigning a static IP address. |
| DNS | No response from primary server | The DNS server failed to respond to one or more requests from the VG248. | 1. If the VG248 has a static IP address, verify the DNS server has been configured. Refer to the "Setting the DNS Server" section for details. 2. Verify that the DNS server is working properly. |
| DNS | Server address not configured | A DNS query has been attempted, but no DNS server has been configured. | 1. If the VG248 has a static IP address, verify the DNS server has been configured. Refer to the "Setting the DNS Server" section for details. 2. If you are using DHCP, the DHCP server has not provided a DNS server. Check the DHCP server configuration. |
| FTP | Invalid password entered | An attempt was made to connect to the VG248 via FTP with the wrong password. | Verify that you have entered the password for the highest level of security currently set. When using FTP, if you have both a login and an enable password set, you must use the enable password. Refer to the "Configuring Passwords" section for details. |
| FTP | Required password absent | An attempt was made to connect to the VG248 via FTP without a password when one was required. | When using FTP, if you have both a login and an enable password set, you must use the enable password. Refer to the "Configuring Passwords" section for details. |
| FTP | Partial download aborted | An attempt to download a file onto the VG248 was interrupted before the entire file was transferred. The resulting partial file has been deleted from the filing system on the VG248. | Reattempt the file transfer. |
| OS | Ethernet failed to start | The Ethernet cable is not properly connected to the VG248 or to the hub or switch. | Check the Ethernet cable and reconnect it to the VG248 and the hub or switch. If error persists, replace cable. |
| OS | Incorrect password entered | A user attempted to use a telnet, console, or FTP connection to the VG248 but entered an incorrect password. | Check the passwords and verify that you are using the correct one. Change the password if you suspect an unauthorized login attempt. Refer to the "Configuring Passwords" section for details. |
| SNMP | Attempt to use Get with invalid community name " <name> " | The VG248 received an SNMP request with an invalid read-only community name (password). | Check the community string setting on the VG248 and ensure that your network management system has the correct password. Refer to the "Configuring SNMP Settings" section for details. |
| SNMP | Attempt to use Set with invalid community name " <name> " | The VG248 received an SNMP request with an invalid read-write community name (password). | Check the community string setting on the VG248 and ensure that your network management system has the correct password. Refer to the "Configuring SNMP Settings" section for details. |
| SNMP | Received invalid packet | The SNMP server received an invalid SNMP request. | Verify that your network management system is set up properly. |
| TFTP | Timeout | The VG248 is unable to retrieve a file using TFTP. | These errors might occur if the network is busy. The errors should resolve themselves when the network load reduces. |
| TFTP | TFTP: Rx error |

| System | Error | Explanation | Action |
|---|---|---|---|
| POTS | Feature codes: X same as Y | You have configured the telephone feature codes such that the code for one operation (such as speed dial) is the same as for another (such as call forward). | Users will not be able to use one of these operations. You must set unique feature codes for each operation. To prohibit users from performing an operation, leave the feature code setting empty. See the "Assigning Feature Codes" section for details. |
| POTS | Feature codes: X precludes Y | You have configured the telephone feature codes in such a way that the code for one operation completely masks that for a second operation. For example, if the feature code for speed dial 1 is*** and the code for speed dial 2 is ****, you could never use speed dial 2. Instead, as soon you dial the third *, speed dial 1 activates. | Do not assign features codes that might mask other operations. See the "Assigning Feature Codes" section for details. |

| System | Error | Explanation | Action |
|---|---|---|---|
| SCCP | Registration failed: X | This message, associated with a particular port (1 - 48), indicates that the port had difficulty registering itself with Cisco CallManager. | If a port is not properly registered, then you cannot make phone calls using it. The reason that registration with Cisco CallManager failed is indicated in the message. If the port cannot successfully register, verify that the port is properly configured in Cisco CallManager. See "Configuring the VG248 Ports" section for details. |
| SCCP | Registration failures; last reason X |
| SCCP | Attempt to use; currently disabled | A user has attempted to use a telephone handset attached to a VG248 port, which is currently disabled. | To allow the user to make and receive calls, you must enable the port so it can register with Cisco CallManager. See "Setting the Port Enable Policy" section for details. |
| SCCP | TFTP failed; using last known good configuration | A port on the VG248 has failed to retrieve its configuration using TFTP. Instead, the VG248 is using the configuration stored last time the port successfully registered with Cisco CallManager. | No action is required. However, this message might indicate a potential problem with connectivity to the TFTP server. Verify that the TFTP server is up and running. |
| SCCP | No TFTP server address | The TFTP server has not been set. | 1. If using DHCP to obtain TFTP server, check your DHCP server configuration. 2. If you want to use a fixed TFTP server, you must configure it on the VG248 Refer to the "Identifying the Cisco CallManager TFTP Server" section to assign a TFTP server for details. |
| SCCP | Unable to resolve TFTP server name | The VG248 was not able to locate the TFTP server. | Verify the name of the TFTP server the VG248 is attempting to locate using Display > System Status . • If using DHCP, check the configuration on the DHCP server to verify that it is returning a valid TFTP server name to the VG248. • If you are using a fixed TFTP server, verify the configured server name using Configure -> Telephony > CallManager TFTP server . |

| Status | Description |
|---|---|
| Handset Status |
| OnHook | Not currently in use. |
| OffHook | User has lifted the handset. |
| Ringing | Incoming call to this port. |
| OnCall | A call has been established and voice packets are moving across the network. |
| Cisco CallManager Link Status |
| Down | Link is not up (either because the port is not enabled or because of a temporary failure). |
| Register | Port is registering with Cisco CallManager |
| <directory number> | Directory number for the port displays indicating that the port is up and available for use. |
| Unregister | Unregistering from Cisco CallManager. Displays if port is being disabled or reset. |
| PeerInUse | The port's directory number is in use by another phone that shares the directory number. The port is not available for use while a call is active on the other phone. |
| KeepCall | The Cisco CallManager link has gone down, but the call that was in progress is being maintained. |

| Type | Description |
|---|---|
| CallManager link | Status of the connection to Cisco CallManager |
| TFTP server | Host name or IP address of the TFTP server |
| Device name | Device name of the port as it appears in Cisco CallManager |
| Directory number | Extension number assigned to the analog device connected to this port |
| Forwarded to | Directory number to which calls are being forwarded |
| Call state | Status of the port from a user's viewpoint. |
| Remote party | Directory name and number of caller |
| Remote address | IP address and port of caller |
| Codec in use | Codec being used by Cisco CallManager: • G.729A • G.711 mu-law • G.711 a-law. |
| MWI | Whether the message waiting indicator for this port is on or off |
| CallManager name | DNS name of the Cisco CallManager host |
| CallManager IP address | IP address of Cisco CallManager |
| CallManager state | Status of connection to Cisco CallManager: • Active—connected to this Cisco CallManager and using this connection for SCCP communication. • Connecting—in the process of connecting to this Cisco CallManager • Idle—this Cisco CallManager is not being used • Standby—connected to this Cisco CallManager but not currently using the connection. Can use connection if active connection fails. • Pending—attempting to make this Cisco CallManager the active connection as soon as possible. |
| CallManager type | Type of Cisco CallManager system: • Normal—typical Cisco CallManager system • Failover—Cisco CallManager system reserved for failover situations |

| System | Description |
|---|---|
| DHCP | Communicates with DHCP server. |
| Ethernet | Concerned with low-level network link integrity. |
| OS | Runs the low-level services of the VG248. |
| FTP | Used to send new software images to the VG248. |
| DNS | Resolves host names to IP addresses. |
| TFTP | Handles retrieval of Cisco CallManager port configuration. |
| SLIC | Detects events from analog handsets. |
| DSP | Provides digital signal processing. |
| POTS | Bridges between analog and IP telephony. |
| SCCP | Transmits and receives telephony events over the IP network; communicates with Cisco CallManager. |
| SNMP | Coordinates SNMP communication. |