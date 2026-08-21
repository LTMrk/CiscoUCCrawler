---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-28aabbe4f0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_010.html
retrieved_at: 2026-08-21T14:27:19.568320+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Cisco Unified IP Phone and  Telephony Networks

## Chapter: Cisco Unified IP Phone and  Telephony Networks

# Cisco Unified IP Phone and  Telephony Networks

## Phone and Telephony Networks Overview

Cisco Unified IP Phones enable you to communicate by using voice over a data network. To provide this capability, the IP Phones
                           depend upon and interact with several other important Cisco Unified IP Telephony components, including Cisco Unified Communications
                           Manager.

This chapter focuses on the interactions between the Cisco Unified IP Phone 6901 and 6911,  Cisco Unified Communications Manager,
                           DNS and DHCP servers, TFTP servers, and switches. It also describes options for powering phones.

For related information about voice and IP communications, go to  this URL:

http://www.cisco.com/c/en/us/products/unified-communications/index.html

## Cisco Unified IP Communications Product Interactions

To function in the IP telephony network, the Cisco Unified IP
                           		Phone must be connected to a networking device, such as a Cisco Catalyst
                           		switch. You must also register the CiscoUnifiedIPPhone with a Cisco
                           		UnifiedCommunications Manager system before sending and receiving calls.

### Cisco Unified IP Phone and Cisco Unified Communications Manager Interactions

CiscoUnifiedCommunications Manager is an open and
                              		industry-standard call processing system. CiscoUnifiedCommunications Manager
                              		software sets up and tears down calls between phones, integrating traditional
                              		PBX functionality with the corporate IP network. CiscoUnifiedCommunications
                              		Manager manages the components of the IP telephony system: the phones, the
                              		access gateways, and the resources necessary for features such as call
                              		conferencing and route planning. CiscoUnified Communications Manager also
                              		provides:

Firmware for phones

Configuration file using the  TFTP service

Phone registration

Call preservation, so that a media session continues if signaling is
                                    			 lost between the primary Communications Manager and a phone

For information about configuring CiscoUnifiedCommunications
                              		Manager to work with the IPphones described in this chapter, see the "Cisco Unified IP Phone Configuration" chapter in the Cisco Communications Manager Administration Guide .

If the Cisco Unified IP Phone model that you want to configure does
                                          		  not appear in the Phone Type drop-down list in Cisco Unified Communications
                                          		  Manager, go to the following URL and install the latest support patch for your
                                          		  version of Cisco UnifiedCommunications Manager:

http://tools.cisco.com/support/downloads/go/Redirect.x?mdfid=278875240

For more information, see the "Software Upgrades" chapter in the Cisco Unified Communications Operating System Administration
                                 		  Guide .

### Cisco Unified IP Phone 6911 and VLAN Interaction

The Cisco Unified IP Phone 6911 has an internal Ethernet switch, enabling forwarding of packets to the phone, and to the access port and the network port
                              on the back of the phone.

The Cisco Unified IP Phone 6901 does not have a PC port.

If a computer is connected to the access port, the computer and the phone share the same physical link to the switch and share
                              the same port on the switch. This shared physical link has the following implications for the VLAN configuration on the network:

The current VLANs might be configured on an IP subnet basis. However, additional IP addresses might not be available to assign
                                    the phone to the same subnet as other devices connected to the same port.

Data traffic present on the VLAN supporting phones might reduce the quality of VoIP traffic.

Network security may require isolation of the VLAN voice traffic from the VLAN data traffic.

You can resolve these issues by isolating the voice traffic onto a separate VLAN. The switch port that the phone connects
                              to would be configured to have separate VLANs for carrying:

Voice traffic to and from the IP Phone (auxiliary VLAN on the Cisco Catalyst 6000 series, for example)

Data traffic to and from the PC connected to the switch through the access port of the IP Phone (native VLAN)

Isolating the phones on a separate, auxiliary VLAN increases the quality of the voice traffic and allows a large number of
                              phones to be added to an existing network when there are not enough IP addresses for each phone.

For more information, refer to the documentation included with a Cisco switch. You can also access switch information at this
                              URL:

http://cisco.com/en/US/products/hw/switches/index.html

### Cisco Unified IP Phone and Cisco Unified Communications Manager Express Interaction

When the Cisco Unified IP Phone works with the Cisco Unified Communications Manager Express (Unified CME), the phones must
                              go into CME mode.

When a user invokes the conference feature, the tag allows the phone to use either a local or network hardware conference
                              bridge.

The Cisco Unified IP Phones do not support the following actions:

Only supported in the connected call transfer scenario.

Only supported in the connected call transfer scenario.

Supported using the Conference button or Hookflash access.

Supported using the Hold button.

Not supported.

Not supported.

Not supported.

The users cannot create conference and transfer calls across different lines.

## Cisco Unified IP Phone Power

The Cisco Unified IP Phone 6901 and 6911 can be powered with external power or with Power over
                           		Ethernet (PoE). A separate power supply provides external power. A switch
                           		provides PoE through the Ethernet cable attached to a phone.

Caution

When you install an externally powered phone, connect the power supply
                                       		  to the phone and to a power outlet before you connect the Ethernet cable to the
                                       		  phone. When you remove an externally powered phone, disconnect the Ethernet
                                       		  cable from the phone before you disconnect the power supply.

### Power Guidelines

The following table provides guidelines for powering the Cisco Unified IP Phone 6901 and 6911 .

Type

Guidelines

External power,  provided through the CP-PWR-CUBE-3 external
                                             					 power supply.

The Cisco Unified IP Phone 6901 and 6911 use the CP-PWR-CUBE-3 power supply.

External power,  provided through the Cisco Unified IP Phone
                                             					 Power Injector.

The Cisco Unified IP Phone Power Injector may be used with any
                                             					 Cisco Unified IP Phone. Functioning as a midspan device, the injector delivers
                                             					 inline power to the attached phone. The Cisco Unified IP Phone Power Injector connects between a switch port and the
                                             IP Phone, and supports a maximum
                                             					 cable length of 100 meter (m) between the unpowered switch and the IP Phone.

PoE power, provided by a switch through the Ethernet cable
                                             					 attached to the phone.

The Cisco Unified IP Phone 6901 and 6911 support Cisco inline PoE.

The Cisco Unified IP Phone 6901 and 6911 support IEEE 802.3af Class 1 power on signal
                                             						pairs and spare pairs.

To ensure
                                             						uninterruptible operation of the phone, make sure that the switch has a backup
                                             						power supply.

Make sure that the
                                             						CatOS or IOS version running on your switch supports your intended phone
                                             						deployment. Refer to the documentation for your switch for operating system
                                             						version information.

External power, provided through inline power patch panel
                                             					 WS-PWR-PANEL

The inline power patch panel WS-PWR-PANEL is compatible with
                                             					 the Cisco Unified IP Phone 6901 and 6911 .

### Power Outage

Your access to emergency service through the phone requires the phone to receive power. If an interruption in the power supply
                              occurs, Service and Emergency Calling Service dialing do not function until power is restored. In the case of a power failure
                              or disruption, you may need to reset or reconfigure equipment before you can use the Service or Emergency Calling Service
                              dialing.

### Additional Information About Power

The documents in the following table provide more information on the following topics:

Cisco switches that work with Cisco Unified IP Phones

Cisco IOS releases that support bidirectional power negotiation

Other requirements and restrictions about power

Document topics

URL

Cisco Unified IP Phone Power Injector

http://www.cisco.com/en/US/products/ps6951/index.html

PoE Solutions

http://www.cisco.com/en/US/netsol/ns340/ns394/ns147/ns412/index.html

Cisco Catalyst Switches

http://www.cisco.com/en/US/products/hw/switches/index.html

Integrated Service Routers

http://www.cisco.com/en/US/products/hw/routers/index.html

Cisco IOS Software

http://www.cisco.com/en/US/products/sw/iosswrel/products_ios_cisco_ios_software_category_home.html

## Phone Configuration Files

The TFTP server stores the phone configuration files that
                           		define Cisco Unified Communications Manager connection parameters. In
                           		general, any time you make a change in Cisco Unified Communications Manager
                           		that requires the phone to be reset, a change is automatically made to the
                           		phone configuration file.

Configuration files also contain information about which image
                           		load the phone should be running. If this image load differs from the one
                           		currently loaded on a phone, the phone contacts the TFTP server to request the
                           		required load files.

In addition, if the device security mode in the configuration
                           		file is set to Authenticated and the CTL file on the phone has a valid
                           		certificate for CiscoUnifiedCommunications Manager, the phone establishes a
                           		TLS connection to CiscoUnifiedCommunications Manager. Otherwise, the phone
                           		establishes a TCP connection.

If the device security mode in the configuration file is set to
                                       		  Authenticated or Encrypted, but the phone has not received a CTL file, the
                                       		  phone tries four times to obtain a CTL file so it can register securely.

If you configure security-related settings in CiscoUnified
                           		Communications Manager, the phone configuration file contains sensitive
                           		information. To ensure the privacy of a configuration file, you must configure
                           		it for encryption. For detailed information, see the " Configuring
                              		  Encrypted Phone Configuration Files" chapter in Cisco Unified Communications Manager Security Guide . A phone
                           		requests a configuration file whenever it resets and registers with
                           		CiscoUnifiedCommunications Manager.

A phone accesses a default configuration file named
                           		XmlDefault.cnf.xml from the TFTP server when the following conditions exist:

You have enabled autoregistration in CiscoUnifiedCommunications
                                 			 Manager

The phone has not been added to the CiscoUnified Communications
                                 			 Manager database

The phone is registering for the first time

If autoregistration is not enabled and the phone is not added
                           		to the Cisco Unified Communications Manager database, the system rejects the phone registration request.

If the phone registers and works in encrypted mode, the phone
                           		accesses the configuration file named SEPmac_address.cnf.xml.enc.sgn. If the
                           		SEPmac_address.cnf.xml.enc.sgn does not exist on the TFTP server, the phone
                           		requests the file SEPmac_address.cnf.xml.sgn. That is, if the phone works in
                           		encrypted mode with TFTP Encrypted Config selected, the phone accesses the
                           		configuration file named SEPMac_addr.cnf.xml.enc.sgn. If the phone works in
                           		encrypted mode with TFTP Encrypted Config not selected, the phone accesses the
                           		file SEPMac_addr.cnf.xml.sgn. To enable TFTP Encrypted Configuration, select
                           		the TFTP Encrypted Config check box in the Phone
                           		Security Profile Configuration page. You can access this page from the Cisco
                           		Unified Communications Manager by selecting System > Security > Phone
                                 			 Security Profile and clicking Add New .

For SIP phones, the TFTP server generates these SIP
                           		configuration files:

SIP IP Phone:

For unsigned and unencrypted files - SEP<mac>.cnf.xml

For signed files - SEP<mac>.cnf.xml.sgn

For signed and encrypted files - SEP<mac>.cnf.xml.enc.sgn

Dial Plan - <dialplan>.xml

The filenames derive from the MAC address and description
                           		fields in the 
                           		Phone Configuration window of CiscoUnified
                           		Communications Manager. The MAC address uniquely identifies the phone.

For more information on phone configuration settings, see the "Cisco Unified IP Phone Configuration" chapter in the Cisco Communications Manager Administration Guide .

## Phone Startup Process

When connecting to the VoIP network, the Cisco Unified IP Phone 6901 and 6911 go through a standard startup process that is described in the following list. Depending on your specific network configuration,
                           not all these steps may occur on your CiscoUnifiedIPPhone.

Obtain power from the switch. If a phone does not use external power, the switch provides in-line power through the Ethernet
                                 cable attached to the phone. For more information, see Cisco Unified Communications Manager Phone Addition Methods and Startup Problems .

Configure VLAN. If the CiscoUnifiedIPPhone connects to a CiscoCatalyst switch, the switch informs the phone of the voice VLAN
                                 defined on the switch. The phone needs to know the VLAN membership before proceeding with the Dynamic Host Configuration Protocol
                                 (DHCP) request for an IP address.

For more information, see Cisco Unified IP Phone Network Settings Setup and Startup Problems .

Obtain an IP address. If the CiscoUnifiedIPPhone uses DHCP to obtain an IP address, the phone queries the DHCP server to obtainthe
                                 address. If you are not using DHCP in your network, you must assign static IP addresses to each phone locally.

For more information, see Cisco Unified IP Phone Network Settings Setup and Startup Problems .

Access a TFTP server. In addition to assigning an IP address, the DHCP server directs the CiscoUnifiedIPPhone to a TFTP Server.
                                 If the phone has a statically defined IP address, you must configure the TFTP server locally on the phone; the phone then
                                 contacts the TFTP server directly.

You can also assign an alternative TFTP server to use instead of the one assigned by DHCP.

For more information, see Cisco Unified IP Phone Network Settings Setup and Startup Problems .

Request the configuration file. The TFTP server stores configuration files that define parameters for connecting to Cisco
                                 UnifiedCommunications Manager and other information for the phone.

For more information, see Cisco Unified Communications Manager Phone Addition Methods and Startup Problems .

Load the stored phone image. The CiscoUnifiedIPPhone has nonvolatile flash memory to store firmware images and user-defined
                                 preferences. At startup, the phone runs a bootstrap loader that loads a phone image stored in flash memory. Using this image,
                                 the phone initializes the software and hardware.

For more information, see Startup Problems .

Contact Cisco Unified Communications Manager. The configuration file defines how the Cisco UnifiedIPPhone communicates with
                                 Cisco UnifiedCommunications Manager and provides a phone with the load ID. After obtaining the file from the TFTP server,
                                 the phone attempts to make a connection to the highest priority Cisco UnifiedCommunications Manager on the list.

If the phone was manually added to the database, Cisco UnifiedCommunications Manager identifies the phone. If the phone was
                                 not manually added to the database and autoregistration is enabled in Cisco UnifiedCommunications Manager, the phone attempts
                                 to autoregister in the Cisco UnifiedCommunications Manager database.

For more information, see Startup Problems

## Cisco Unified Communications Manager Phone Addition Methods

Before installing the CiscoUnifiedIPPhone, you must
                              		  choose a method for adding phones to the CiscoUnifiedCommunications Manager
                              		  database. Each phone type requires a fixed number of device
                              		  license units and the available  number of unit licenses on the server
                              		  may impact phone registration. For more information on licensing, see the "Licenses for Phones" section in the CiscoUnified Communications Manager System Guide .

The following table provides an overview of the Cisco Unified Communications Manager phone addition methods.

Method

Requires MAC address?

Notes

Autoregistration

No

Results in
                                          						automatic assignment of directory numbers.

Not available when
                                          						security or encryption is enabled.

Autoregistration with TAPS

No

Requires autoregistration and the Bulk Administration Tool
                                          					 (BAT); updates information in the Cisco Unified IP Phone and in Cisco
                                          					 UnifiedCommunications Manager Administration

Using the Cisco Unified Communications Manager Administration

Yes

Requires phones to be added individually

Using BAT

Yes

Allows for simultaneous registration of multiple phones

### Autoregistration Phone Addition

By enabling autoregistration before you begin installing
                              		phones, you can:

Add phones without first gathering MACaddresses from the phones.

Automatically add a CiscoUnified IP Phone to the CiscoUnified
                                    			 Communications Manager database when you physically connect the phone to your
                                    			 IP telephony network. During autoregistration, CiscoUnified Communications
                                    			 Manager assigns the next available sequential directory number to the phone.

Quickly enter phones into the CiscoUnifiedCommunications Manager
                                    			 database and modify any settings, such as the directory numbers, from
                                    			 CiscoUnifiedCommunications Manager.

Move autoregistered phones to new locations and assign them to
                                    			 different device pools without affecting their directory numbers.

Cisco recommends you use autoregistration to add less than 100 phones
                                          		  to your network. To add more than 100 phones to your network, use the Bulk
                                          		  Administration Tool (BAT). See Add Phones Using BAT Phone Template .

The system disables autoregistration by default. In some cases, you
                              		might not want to use autoregistration; for example, if you want to assign a
                              		specific directory number to the phone. For information about enabling
                              		autoregistration, see the "Enabling Autoregistration" section in
                              		the Cisco UnifiedCommunications Manager Administration Guide .

When you configure the cluster for mixed mode through the Cisco CTL
                                          		  client, autoregistration automatically disables. When you configure the
                                          		  cluster for nonsecure mode through the Cisco CTL client, autoregistration automatically enables.

### Autoregistration and TAPS Phone Addition

You can add phones with autoregistration the Tool for Auto-Registered Phones Support (TAPS), without first gathering MAC addresses
                              from
                              		phones.

TAPS works with the Bulk Administration Tool (BAT) to update a
                              		batch of phones that were already added to the CiscoUnifiedCommunications
                              		Manager database with dummy MAC addresses. Use TAPS to update MACaddresses and
                              		download predefined phone configuration files.

Cisco recommends you use autoregistration and TAPS to add less than
                                          		  100 phones to your network. To add more than 100 phones to your network, use
                                          		  the Bulk Administration Tool (BAT). See Add Phones Using BAT Phone Template .

To implement TAPS, you or the end user dial a TAPS directory
                              		number and follow the voice prompts. When the process completes, the phone has
                              		downloaded the directory number and other settings, and the
                              		CiscoUnifiedCommunications Manager database contains the correct MAC address
                              		for the phone.

Autoregistration must be enabled in CiscoUnified
                              		Communications Manager
                              		( System > Cisco Unified
                                    			 CM ) for TAPS to function.

When you configure the cluster for mixed mode through the Cisco CTL
                                          		  client, autoregistration is automatically disabled. When you configure the
                                          		  cluster for nonsecure mode through the Cisco CTL client, autoregistration is
                                          		  automatically enabled.

For more information, see the "Bulk Administration" chapter in CiscoUnified Communications Manager Administration Guide .

### Cisco Unified Communications Manager Phone Addition

You can add phones individually to the
                              		CiscoUnifiedCommunications Manager database using
                              		CiscoUnifiedCommunications Manager administration. To do so, you first obtain
                              		the MAC address for each phone.

For information about determining a MAC address, see Cisco Unified IP Phone MAC Address Determination .

After you have collected MAC addresses, in
                              		CiscoUnifiedCommunications Manager Administration, choose Device > Phone and click Add New to begin.

For complete instructions and conceptual information about
                              		CiscoUnified Communications Manager, see the "Cisco Unified Communications Manager Overview" chapter in the Cisco Unified Communications Manager System Guide .

### Add Phones Using BAT Phone Template

The Cisco Unified Communications Manager Bulk Administration
                                 		  Tool (BAT) enables you to perform batch operations, including registration, on
                                 		  multiple phones. To access BAT, choose Bulk Administration in
                                 		  CiscoUnifiedCommunications Manager Administration,

To add phones by using BAT only (not in conjunction with
                                 		  TAPS), you must obtain the appropriate MAC address for each phone.

For information about determining a MAC address, see Cisco Unified IP Phone MAC Address Determination .

For detailed instructions about adding phones using the Bulk
                                 		  Administration menu, see the Cisco Unified Communications Manager Bulk Administration
                                    			 Guide , chapter "Inserting Phones" .

To add a phone to the Cisco Unified Communications Manager
                                 		  using the BAT phone template, perform these steps:

Step 1

From Cisco Unified Communications Manager,
                                          			 choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template .

Step 2

Click Add New .

Step 3

Choose a Phone Type and click Next .

Step 4

Enter the details of phone specific parameters, including Device Pool,
                                          			 Phone Button Template, and  Device Security Profile.

Step 5

Click Save .

Step 6

From Cisco Unified Communications Manager, choose Device > Phone > Add
                                                				  New to add a phone using an existing BAT phone
                                          			 template.

## Cisco Unified IP Phones and Different Protocols

The Cisco Unified IP Phone can operate with SCCP (Skinny Client Control Protocol) or SIP (Session Initiation Protocol). You
                           can convert a phone that is using one protocol to use the other protocol.

### Convert New Phone from SCCP to SIP

A new, unused phone uses SCCP. To convert this phone to SIP,
                                 		  perform these steps:

Step 1

Take one of these actions:

To autoregister the phone, set the Auto Registration Phone
                                                   					 Protocol parameter in Cisco Unified Communications Manager to SIP.

To provision the phone using the Bulk Administration Tool
                                                   					 (BAT), choose the appropriate phone model and choose SIP from the BAT.

For more information, see Cisco Unified Communications Manager Bulk Administration Guide .

To provision the phone manually, make the appropriate changes
                                                   					 for SIP on the 
                                                   					 Phone configuration window in Cisco
                                                   					 Unified Communications Manager.

For more information, see Cisco Unified Commiunications Manager Administration Guide .

Step 2

If you are not using DHCP in your network, configure the network
                                          			 parameters for the phone. See Network Settings .

Step 3

To save the configuration updates,

Click Apply Config.

When the Apply Configuration Information window displays, click OK.

Tell the user to power cycle the phone.

### In-Use Phone Protocol to Protocol Conversion

Phones using SCCP can be upgraded to use SIP. To change from SCCP to SIP, the phone firmware must be updated to the recommended
                              SIP version before the phones can register. New Cisco Unified IP Phones ship from the factory with SCCP phone firmware. These
                              new phones must be upgraded to the recommended SIP version before they can complete registration.

For information about how to convert an in-use phone from one
                              		protocol to the other, see the Cisco Unified Communications Manager Administration Guide , 
                              		 chapter "Cisco Unified IP Phone Configuration" , section "Migration Existing Phone Configuration to a Different Phone" .

### Deploy Phone in SCCP and SIP Environment

To deploy Cisco Unified IP Phones in an environment that
                                 		  includes SCCP and SIP and in which the Cisco Unified Communications Manager
                                 		  autoregistration parameter specifies SCCP, perform these general steps:

Step 1

Set the Cisco Unified Communications Manager
                                          			 auto_registration_protocol parameter to SCCP.

Step 2

From Cisco Unified Communications Manager, choose System > Enterprise
                                                				  Parameters .

Step 3

Install the phones.

Step 4

Change the Auto Registration Protocol enterprise parameter to SIP.

Step 5

Autoregister the SIP phones.

## Cisco Unified IP Phone MAC Address Determination

Several procedures described in this manual require you to
                           		determine the MAC address of a CiscoUnified IP Phone. You can determine the MAC address of a phone in these ways:

Look at the MAC label on the back of the phone.

Display the web page for the phone and click the Device
                                    				Information hyperlink.

| Note | If the Cisco Unified IP Phone model that you want to configure does
                                          		  not appear in the Phone Type drop-down list in Cisco Unified Communications
                                          		  Manager, go to the following URL and install the latest support patch for your
                                          		  version of Cisco UnifiedCommunications Manager: http://tools.cisco.com/support/downloads/go/Redirect.x?mdfid=278875240 |
|---|---|

| Note | The Cisco Unified IP Phone 6901 does not have a PC port. |
|---|---|

| Caution | When you install an externally powered phone, connect the power supply
                                       		  to the phone and to a power outlet before you connect the Ethernet cable to the
                                       		  phone. When you remove an externally powered phone, disconnect the Ethernet
                                       		  cable from the phone before you disconnect the power supply. |
|---|---|

| Type | Guidelines |
|---|---|
| External power,  provided through the CP-PWR-CUBE-3 external
                                             					 power supply. | The Cisco Unified IP Phone 6901 and 6911 use the CP-PWR-CUBE-3 power supply. |
| External power,  provided through the Cisco Unified IP Phone
                                             					 Power Injector. | The Cisco Unified IP Phone Power Injector may be used with any
                                             					 Cisco Unified IP Phone. Functioning as a midspan device, the injector delivers
                                             					 inline power to the attached phone. The Cisco Unified IP Phone Power Injector connects between a switch port and the
                                             IP Phone, and supports a maximum
                                             					 cable length of 100 meter (m) between the unpowered switch and the IP Phone. |
| PoE power, provided by a switch through the Ethernet cable
                                             					 attached to the phone. | The Cisco Unified IP Phone 6901 and 6911 support Cisco inline PoE. The Cisco Unified IP Phone 6901 and 6911 support IEEE 802.3af Class 1 power on signal
                                             						pairs and spare pairs. To ensure
                                             						uninterruptible operation of the phone, make sure that the switch has a backup
                                             						power supply. Make sure that the
                                             						CatOS or IOS version running on your switch supports your intended phone
                                             						deployment. Refer to the documentation for your switch for operating system
                                             						version information. |
| External power, provided through inline power patch panel
                                             					 WS-PWR-PANEL | The inline power patch panel WS-PWR-PANEL is compatible with
                                             					 the Cisco Unified IP Phone 6901 and 6911 . |

| Document topics | URL |
|---|---|
| Cisco Unified IP Phone Power Injector | http://www.cisco.com/en/US/products/ps6951/index.html |
| PoE Solutions | http://www.cisco.com/en/US/netsol/ns340/ns394/ns147/ns412/index.html |
| Cisco Catalyst Switches | http://www.cisco.com/en/US/products/hw/switches/index.html |
| Integrated Service Routers | http://www.cisco.com/en/US/products/hw/routers/index.html |
| Cisco IOS Software | http://www.cisco.com/en/US/products/sw/iosswrel/products_ios_cisco_ios_software_category_home.html |

| Note | If the device security mode in the configuration file is set to
                                       		  Authenticated or Encrypted, but the phone has not received a CTL file, the
                                       		  phone tries four times to obtain a CTL file so it can register securely. |
|---|---|

| Note | You can also assign an alternative TFTP server to use instead of the one assigned by DHCP. For more information, see Cisco Unified IP Phone Network Settings Setup and Startup Problems . |
|---|---|

| Method | Requires MAC address? | Notes |
|---|---|---|
| Autoregistration | No | Results in
                                          						automatic assignment of directory numbers. Not available when
                                          						security or encryption is enabled. |
| Autoregistration with TAPS | No | Requires autoregistration and the Bulk Administration Tool
                                          					 (BAT); updates information in the Cisco Unified IP Phone and in Cisco
                                          					 UnifiedCommunications Manager Administration |
| Using the Cisco Unified Communications Manager Administration | Yes | Requires phones to be added individually |
| Using BAT | Yes | Allows for simultaneous registration of multiple phones |

| Note | Cisco recommends you use autoregistration to add less than 100 phones
                                          		  to your network. To add more than 100 phones to your network, use the Bulk
                                          		  Administration Tool (BAT). See Add Phones Using BAT Phone Template . |
|---|---|

| Note | When you configure the cluster for mixed mode through the Cisco CTL
                                          		  client, autoregistration automatically disables. When you configure the
                                          		  cluster for nonsecure mode through the Cisco CTL client, autoregistration automatically enables. |
|---|---|

| Note | Cisco recommends you use autoregistration and TAPS to add less than
                                          		  100 phones to your network. To add more than 100 phones to your network, use
                                          		  the Bulk Administration Tool (BAT). See Add Phones Using BAT Phone Template . |
|---|---|

| Note | When you configure the cluster for mixed mode through the Cisco CTL
                                          		  client, autoregistration is automatically disabled. When you configure the
                                          		  cluster for nonsecure mode through the Cisco CTL client, autoregistration is
                                          		  automatically enabled. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager,
                                          			 choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Choose a Phone Type and click Next . |
| Step 4 | Enter the details of phone specific parameters, including Device Pool,
                                          			 Phone Button Template, and  Device Security Profile. |
| Step 5 | Click Save . |
| Step 6 | From Cisco Unified Communications Manager, choose Device > Phone > Add
                                                				  New to add a phone using an existing BAT phone
                                          			 template. |

| Step 1 | Take one of these actions: To autoregister the phone, set the Auto Registration Phone
                                                   					 Protocol parameter in Cisco Unified Communications Manager to SIP. To provision the phone using the Bulk Administration Tool
                                                   					 (BAT), choose the appropriate phone model and choose SIP from the BAT. For more information, see Cisco Unified Communications Manager Bulk Administration Guide . To provision the phone manually, make the appropriate changes
                                                   					 for SIP on the 
                                                   					 Phone configuration window in Cisco
                                                   					 Unified Communications Manager. For more information, see Cisco Unified Commiunications Manager Administration Guide . |
|---|---|
| Step 2 | If you are not using DHCP in your network, configure the network
                                          			 parameters for the phone. See Network Settings . |
| Step 3 | To save the configuration updates, Click Apply Config. When the Apply Configuration Information window displays, click OK. Tell the user to power cycle the phone. |

| Step 1 | Set the Cisco Unified Communications Manager
                                          			 auto_registration_protocol parameter to SCCP. |
|---|---|
| Step 2 | From Cisco Unified Communications Manager, choose System > Enterprise
                                                				  Parameters . |
| Step 3 | Install the phones. |
| Step 4 | Change the Auto Registration Protocol enterprise parameter to SIP. |
| Step 5 | Autoregister the SIP phones. |