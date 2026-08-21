---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-55cce01f7f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_010.html
retrieved_at: 2026-08-21T13:37:49.222357+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Cisco Unified IP
	 Phones and Telephony Networks

## Chapter: Cisco Unified IP
	 Phones and Telephony Networks

# Cisco Unified IP
                     	 Phones and Telephony Networks

## Phone and
                        	 Telephony Networks Overview

The Cisco Unified IP Conference Phone enables you to communicate by
                           		using voice over a data network. To provide this capability, the conference
                           		phones depend upon and interact with several other key Cisco Unified IP
                           		Telephony components, including DNS and DHCP servers, TFTP servers, and
                           		switches.

For related information about voice and IP communications, see this URL:

http://www.cisco.com/en/us/partner/products/sw/voicesw/index.html

This chapter provides an overview of the interaction between the
                           		conference phone and other key components of a Voice over IP (VoIP) network. It
                           		also describes options for powering conference phones.

## Cisco Unified IP
                        	 Communications Product Interactions

To function in the
                           		IP telephony network, the conference phone must be connected to a networking
                           		device, such as a Cisco Catalyst switch. You must also register the phone with
                           		a Cisco Unified Communications Manager system before sending and receiving
                           		calls.

### Interactions with
                           	 Other Cisco Unified IP Telephony Products

To function in the
                              		IP telephony network, the Cisco Unified IP Conference Phone must be connected
                              		to a networking device, such as a Cisco Catalyst switch. You must also register
                              		the conference phone with a Cisco Unified Communications Manager system before
                              		sending and receiving calls.

#### Cisco Unified IP
                              	 Conference Phone and Cisco Unified Communications Manager
                              	 Interaction

Cisco Unified
                                 		Communications Manager is an open and industry-standard call processing system.
                                 		Cisco Unified Communications Manager software sets up and tears down calls
                                 		between IP devices, integrating traditional private branch exchange (PBX)
                                 		functionality with the corporate IP network. Cisco Unified Communications
                                 		Manager manages the components of the IP telephony system—the conference
                                 		stations, the phones, the access gateways, and the resources necessary for
                                 		features such as, call conferencing and route planning. Cisco Unified
                                 		Communications Manager also provides:

Firmware for
                                       			 conference stations and phones

Authentication
                                       			 and encryption (if configured for the telephony system)

Configuration
                                       			 file using the TFTP service

Conference phone
                                       			 registration

Call
                                       			 preservation, so that a media session continues if signalling is lost between
                                       			 the primary Communications Manager and a conference phone

For information
                                 		about configuring Cisco Unified Communications Manager to work with the IP
                                 		devices described in this chapter, see Cisco Unified
                                    		  Communications Manager Administration Guide , Cisco Unified
                                    		  Communications Manager System Guide , and Cisco Unified
                                    		  Communications Manager Security Guide .

If the conference
                                             		  phone model that you want to configure does not appear in the Phone Type
                                             		  drop-down list in Cisco Unified Communications Manager Administration, go to
                                             		  the following URL and install the latest support patch for your version of
                                             		  Cisco Unified Communications Manager:

http://www.cisco.com/cisco/software/navigator.html?mdfid=282677102&i=rm

For more
                                 		information, see "Software
                                    		  Upgrades" , Cisco Unified
                                    		  Communications Operating System Administration Guide

#### Cisco Unified IP
                              	 Conference Phone and VLAN Interaction

When Voice VLAN
                                 		(VVLAN) is disabled, the egress SW port packets are not tagged and only
                                 		untagged packets are accepted on the ingress direction.

When VVLAN is
                                 		configured as 1-4094, the egress SW port packets are tagged with the VVLAN. For
                                 		ingress packets, if VLAN is different from VVLAN, only the packets that match
                                 		the VVLAN are accepted. If VLAN equals VVLAN then both packets that match the
                                 		VVLAN and untagged packets are accepted.

When VVLAN is set
                                 		to 0, 802.1p is enabled. The egress SW port packets will be tagged with 802.1p.
                                 		On the ingress side, both 802.1p tagged packets and untagged packets are
                                 		accepted.

For more
                                 		information, see the documentation included with a Cisco switch. You can also
                                 		access switch information at this URL: http://www.cisco.com/en/US/products/hw/switches/index.html

#### Cisco Unified IP
                              	 Conference Phone and Cisco Unified Communications Manager Express
                              	 Interaction

If supported, when
                                 		the phone works with the Cisco Unified Communications Manager Express (Unified
                                 		CME), the phone must go into CME mode.

When a user invokes
                                 		the conference feature, the tag allows the conference phone to use either a
                                 		local or network hardware conference bridge.

In CME mode, the
                                 		conference phones either only partially support, or do not support the
                                 		following actions:

## Conference Phone
                        	 Power

The Cisco Unified IP
                           		Conference Phone can be powered with external power or with Power over
                           		Ethernet (PoE). External power is provided through a separate power supply. PoE
                           		is provided by a switch through the Ethernet cable attached to a conference
                           		phone.

When you install a
                                       		  phone that is powered with external power, connect the power supply to the
                                       		  phone and to a power outlet before you connect the Ethernet cable to the phone.
                                       		  When you remove a phone that is powered with external power, disconnect the
                                       		  Ethernet cable from the phone before you disconnect the power supply.

### Power
                           	 Guidelines

The following
                                 		  table provides guidelines for powering the Cisco Unified IP Conference Phone.

External
                                             					 power: Provided by an external power supply.

The Cisco
                                             					 Unified IP Conference Phone uses the CP-PWR-CUBE-3 external power supply.

When using
                                             					 a sound base in Linked Mode, the primary sound base must be connected using the
                                             					 CP-PWR-CUBE-3 external power supply.

External
                                             					 power: Provided through the Cisco Unified IP Phone Power Injector.

The Cisco
                                             					 Unified IP Phone Power Injector may be used with any Cisco Unified IP Phone or
                                             					 Conference Phone. It functions as a mid-span device to deliver inline power to
                                             					 the attached phone. The Cisco Unified IP Phone Power Injector is connected
                                             					 between a switch port and the IP Conference Phone and supports a maximum cable
                                             					 length of 100m between the unpowered switch and the IP Phone.

External
                                             					 power: Provided through inline power patch panel WS-PWR-PANEL.

The inline
                                             					 power patch panel WS-PWR-PANEL is compatible with the Cisco Unified IP
                                             					 Conference Phone.

PoE power:
                                             					 Provided by a switch through the Ethernet cable attached to the conference
                                             					 phone.

The
                                                      						  Cisco Unified IP Conference Phone supports IEEE 802.3af Class 3 power on
                                                      						  signal pairs and spare pairs.

When
                                                      						  using a sound base in Linked Mode, the primary sound base must be connected
                                                      						  using the CP-PWR-CUBE-3 external power supply.

To
                                                      						  ensure uninterruptible operation of the conference phone, make sure that the
                                                      						  switch has a backup power supply.

Make
                                                      						  sure that the CatOS or IOS version running on your switch supports your
                                                      						  intended conference phone deployment. Refer to the documentation for your
                                                      						  switch for operating system version information.

### Power
                           	 Outage

Your access to
                              		emergency service through the phone requires the phone to receive power. If an
                              		interruption in the power supply occurs, Service and Emergency Calling Service
                              		dialling do not function until power is restored. In the case of a power
                              		failure or disruption, you may need to reset or reconfigure equipment before
                              		you can use the Service or Emergency Calling Service dialling.

### Power
                           	 Reduction

You can reduce the
                              		amount of energy that the phone consumes by using Power Save or EnergyWise
                              		(Power Save Plus) mode.

#### Power Save
                              	 Mode

In Power
                                 		Save mode, the backlight on the screen is not lit when the phone is not in use.
                                 		The phone remains in Power Save mode for the scheduled duration or until the
                                 		user interacts with the device. In the Device Configuration window on Cisco
                                 		Unified Communications Administration, configure the following parameters:

Specifies the
                                       				days that the backlight remains inactive.

Schedules the
                                       				time of day that the backlight automatically activates. on the days listed in
                                       				the off schedule.

Indicates the
                                       				length of time that the backlight is active after the backlight is enabled by
                                       				the programmed schedule.

Defines the
                                       				period of user inactivity on the phone before the backlight is turned off.

#### EnergyWise
                              	 Mode

The conference phone supports Cisco EnergyWise (Power Save Plus) mode. When your network contains an EnergyWise (EW) controller
                                 (for example, a Cisco switch with the EnergyWise feature enabled), you can configure these phones to sleep (power down) and
                                 wake (power up) on a schedule to further reduce power consumption.

Set up each phone to enable or disable the EnergyWise settings. If EnergyWise is enabled, configure a sleep and wake time,
                                 as well as other parameters. These parameters are sent to the phone as part of the phone configuration XML file.

### Additional Power
                           	 Information

For related
                                 		  information about power, see the documents listed in the following table. These
                                 		  documents provide information about these topics:

Cisco switches
                                       				that work with the conference phone

The Cisco IOS
                                       				releases that support bidirectional power negotiation

Other
                                       				requirements and restrictions regarding power

## Phone
                        	 Configuration Files

The TFTP server
                           		stores the conference phone configuration files that define parameters for
                           		connecting to Cisco Unified
                              				Communications Manager . In general, any time you make a
                           		change in Cisco Unified
                              				Communications Manager that requires the conference phone
                           		to be reset, a change is made to the conference phone configuration file
                           		automatically.

Configuration files
                           		also contain information about which image load the conference phone should be
                           		running. If this image load differs from the one currently loaded, the phone
                           		contacts the TFTP server to request the required load files.

A conference phone
                           		accesses a default configuration file named XmlDefault.cnf.xml from the TFTP server when these
                           		conditions exist:

You have enabled
                                 			 autoregistration in Cisco Unified
                                    				Communications Manager

The conference
                                 			 phone has not been added to the Cisco Unified
                                    				Communications Manager Database

The conference
                                 			 phone is registering for the first time

If autoregistration
                           		is not enabled and the phone has not been added to the Cisco Unified
                              				Communications Manager Database, the phone registration
                           		request will be rejected. In this case, the conference phone will reset and
                           		attempt to register repeatedly.

If the conference
                           		phone has registered before, the conference phone will access the configuration
                           		file named SEPmac_address.cnf.xml , where the mac_address portion of the filename is the Media
                           		Access Control (MAC) address of the conference phone.

## Phone Startup
                        	 Process

When connecting to
                           		the VoIP network, the conference phone goes through a standard startup process,
                           		as described in the following table. Depending on your specific network
                           		configuration, not all of these process steps may occur on your conference
                           		phone.

Obtain power
                                 			 from the switch. If a conference phone is not using external power, the switch
                                 			 provides in-line power through the Ethernet cable attached to the conference
                                 			 phone. For more information, see Conference Phone Power .

Load the stored
                                 			 conference phone image. The conference phone has non-volatile flash memory in
                                 			 which it stores firmware images and user-defined preferences. At startup, the
                                 			 conference phone runs a bootstrap loader that loads a conference phone image
                                 			 stored in flash memory. Using this image, the conference phone initializes its
                                 			 software and hardware. For more information, see .

Configure VLAN.
                                 			 If the Cisco Unified IP Conference Phone is connected to a Cisco switch, the
                                 			 switch next informs the phone of the voice VLAN defined on the switch port. The
                                 			 phone needs to know its VLAN membership before it can proceed with the Dynamic
                                 			 Host Configuration Protocol (DHCP) request for an IP address.

Obtain an IP
                                 			 address . If the Cisco Unified IP Conference Phone uses DHCP to obtain an IP
                                 			 address, the phone queries the DHCP server to obtain one. If you do not use
                                 			 DHCP in your network, you must assign static IP addresses to each phone
                                 			 locally.

Access a TFTP
                                 			 server. In addition to assigning an IP address, the DHCP server directs the
                                 			 Cisco Unified IP Conference Phone to a TFTP server. If the phone has a
                                 			 statically defined IP address, you must configure the TFTP server locally on
                                 			 the phone. The phone then contacts the TFTP server directly.

You can also
                                             				assign an alternative TFTP server to use instead of the one that DHCP assigns.

Request the
                                 			 configuration file. The TFTP server has configuration files, which define
                                 			 parameters for connecting to Cisco Unified Communications Manager and other
                                 			 information for the conference phone. For more information, see Phone Configuration Files .

Contact Cisco
                                 			 Unified Communications Manager. The configuration file defines how the
                                 			 conference phone communicates with Cisco Unified Communications Manager and
                                 			 provides a conference phone with its load ID. After obtaining the file from the
                                 			 TFTP server, the conference phone attempts to make a connection to the highest
                                 			 priority Cisco Unified Communications Manager on the list. The conference phone
                                 			 makes a non-secure TCP connection.

If the
                                 			 conference phone was manually added to the database, Cisco Unified
                                 			 Communications Manager identifies the conference phone. If the conference phone
                                 			 was not manually added to the database and auto-registration is enabled in
                                 			 Cisco Unified Communications Manager, the conference phone attempts to
                                 			 auto-register itself in Cisco Unified Communications Manager.

Auto-registration is disabled when security is enabled on Cisco
                                 			 Unified Communications Manager. In this case, the conference phone must be
                                 			 manually added to the Cisco Unified Communications Manager.

## Cisco Unified
                        	 Communications Manager IP Phone Addition Methods

Before installing
                              		  the conference phone, you must choose a method for adding conference phones to
                              		  Cisco Unified Communications Manager database. Be aware that each phone type
                              		  requires a fixed number of device license units and the number of unit licenses
                              		  that are available on the server may impact phone registration. For more
                              		  information about licensing, see "Licenses for
                                 			 Phones" section in the Cisco Unified
                                 			 Communications Manager System Guide .

The following
                              		  table provides an overview of these methods for adding conference phones to
                              		  Cisco Unified Communications Manager.

Not
                                          					 available when security or encryption is enabled. In this case, the conference
                                          					 phone must be manually added to the Cisco Unified Communications Manager
                                          					 database.

This
                                          					 method updates the Cisco Unified Communications Manager database with the MAC
                                          					 address and DNs for the device when user calls TAPS from the conference phone.

Allows for
                                          					 the simultaneous registration of multiple conference phones of the same model.

Allows you
                                          					 to schedule when conference phones are added to Cisco Unified Communications
                                          					 Manager.

### Autoregistration
                           	 IP Phone Addition

If you enable
                              		autoregistration before you begin installing conference phones, you can:

Automatically
                                    			 add a conference phone to the Cisco Unified Communications Manager database
                                    			 when you physically connect the conference phone to your IP telephony network.
                                    			 During autoregistration, Cisco Unified Communications Manager assigns the next
                                    			 available sequential directory number to the conference phone.

Add conference
                                    			 phones without first gathering MAC addresses from the conference phones.

Quickly enter
                                    			 conference phones into the Cisco Unified Communications Manager database and
                                    			 modify any settings, such as the directory numbers, from Cisco Unified
                                    			 Communications Manager.

Move
                                    			 autoregistered conference phones to new locations and assign them to different
                                    			 device pools without affecting their directory numbers.

Cisco recommends
                                          		  that you use autoregistration to add fewer than 100 conference phones to your
                                          		  network. To add more than 100 conference phones to your network, use the Bulk
                                          		  Administration Tool (BAT).

Autoregistration is
                              		disabled by default. In some cases, you might not want to use autoregistration;
                              		for example, if you want to assign a specific directory number to the phone, or
                              		if you plan to implement authentication or encryption. For information about
                              		enabling autoregistration, see "Enable
                                 		  Autoregistration" section in the Cisco Unified
                                 		  Communications Manager Administration Guide . For information about
                              		authentication or encryption as it pertains to autoregistration, refer to Cisco Unified
                                 		  Communications Manager Security Guide .

When you configure
                                          		  the client for mixed mode through the Cisco CTL client, autoregistration is
                                          		  automatically disabled. When you configure the cluster for nonsecure mode
                                          		  through the Cisco CTL client, autoregistation is automatically enabled.

### Autoregistration
                           	 and TAPS IP Phone Addition

You can add phones
                              		with autoregistration and TAPS, the Tool for Auto-Registered Phones Support,
                              		without first gathering MAC addresses from phones.

TAPS works with the
                              		Bulk Administration Tool (BAT) to update a batch of conference phones that were
                              		previously added to the Cisco Unified Communications Manager database with
                              		dummy MAC addresses. Use TAPS to update the MAC addresses and to download
                              		predefined configurations for conference phones.

Cisco recommends
                                          		  that you use autoregistration to add fewer than 100 conference phones to your
                                          		  network. To add more than 100 conference phones to your network, use the Bulk
                                          		  Administration Tool (BAT).

To implement TAPS,
                              		dial a TAPS directory number and follow voice prompts. When the process is
                              		complete, the conference phone has downloaded the directory number (DN) and
                              		other settings. The conference phone has also been updated in Cisco Unified
                              		Communications Manager Administration with the correct MAC address.

Autoregistration
                              		must be enabled in Cisco Unified Communications Manager Administration for TAPS
                              		to function. You can do this from System > Cisco Unified
                                    			 CM .

When you configure
                                          		  the client for mixed mode through the Cisco CTL client, autoregistration is
                                          		  automatically disabled. When you configure the cluster for nonsecure mode
                                          		  through the Cisco CTL client, autoregistation is automatically enabled.

For more
                              		information, see "Bulk
                                 		  Administration" , Cisco Unified
                                 		  Communications Manager Administration Guide and "Tool for
                                 		  Auto-Registered Phones Support" , Cisco Unified
                                 		  Communications Manager Bulk Administration Guide .

### Cisco Unified
                           	 Communications Manager Administration Conference Station Addition

You can add
                              		conference phones individually to the Cisco Unified Communications Manager
                              		database by using Cisco Unified Communications Manager Administration. To do
                              		so, you first need to obtain the MAC address for each conference phone.

After you collect
                              		MAC addresses, in Cisco Unified Communications Manager Administration, choose Device > Phone , and then click Add
                                 		  New to begin the addition process.

For complete
                              		instructions and conceptual information about Cisco Unified Communications
                              		Manager, see the Cisco Unified
                                 		  Communications Manager Administration Guide and the Cisco Unified
                                 		  Communications Manager System Guide .

### BAT IP Phone
                           	 Addition

Cisco Unified
                              		Communications Manager Bulk Administration Tool (BAT) enables you to perform
                              		batch operations, including registration, on multiple conference phones. To
                              		access BAT, choose the Bulk Administration drop-down menu in Cisco Unified
                              		Communications Manager Administration.

Before you can add
                              		conference phones using BAT only (not in conjunction with TAPS), you must
                              		obtain the MAC address for each conference phone. If you have a large number of
                              		conference phones to register you can use dummy MAC addresses and update them
                              		later via TAPS.

For detailed
                              		instructions about using BAT, see "Bulk
                                 		  Administration" , Cisco Unified
                                 		  Communications Manager Administration Guide .

## Conference Phone
                        	 MAC Address Determination

Several procedures
                           		described in this manual require you to determine the MAC address of a
                           		conference phone. You can determine the MAC address for a conference phone in
                           		any of these ways:

From the
                                 			 conference phone, press Apps , select Phone
                                    				Information , and look at the MAC Address field.

Look at the MAC
                                 			 label on the bottom of the conference phone.

Display the web
                                 			 page for the conference phone web page, and select Device
                                    				Information . For information about accessing the conference phone
                                 			 web page, see Access Web Page .

| Note | If the conference
                                             		  phone model that you want to configure does not appear in the Phone Type
                                             		  drop-down list in Cisco Unified Communications Manager Administration, go to
                                             		  the following URL and install the latest support patch for your version of
                                             		  Cisco Unified Communications Manager: http://www.cisco.com/cisco/software/navigator.html?mdfid=282677102&i=rm |
|---|---|

| Action | Support Level |
|---|---|
| Barge | Not supported. |
| Conference | Only supported in the connected call transfer scenario. |
| Direct Transfer | Not supported. |
| Hold | Supported using the Hold softkey. |
| Join | Supported using the Conference softkey. |
| Select | Not supported. |
| Transfer | Only supported in the connected call transfer scenario. |

| Note | When you install a
                                       		  phone that is powered with external power, connect the power supply to the
                                       		  phone and to a power outlet before you connect the Ethernet cable to the phone.
                                       		  When you remove a phone that is powered with external power, disconnect the
                                       		  Ethernet cable from the phone before you disconnect the power supply. |
|---|---|

| Power Type | Guidelines |
|---|---|
| External
                                             					 power: Provided by an external power supply. | The Cisco
                                             					 Unified IP Conference Phone uses the CP-PWR-CUBE-3 external power supply. When using
                                             					 a sound base in Linked Mode, the primary sound base must be connected using the
                                             					 CP-PWR-CUBE-3 external power supply. |
| External
                                             					 power: Provided through the Cisco Unified IP Phone Power Injector. | The Cisco
                                             					 Unified IP Phone Power Injector may be used with any Cisco Unified IP Phone or
                                             					 Conference Phone. It functions as a mid-span device to deliver inline power to
                                             					 the attached phone. The Cisco Unified IP Phone Power Injector is connected
                                             					 between a switch port and the IP Conference Phone and supports a maximum cable
                                             					 length of 100m between the unpowered switch and the IP Phone. |
| External
                                             					 power: Provided through inline power patch panel WS-PWR-PANEL. | The inline
                                             					 power patch panel WS-PWR-PANEL is compatible with the Cisco Unified IP
                                             					 Conference Phone. |
| PoE power:
                                             					 Provided by a switch through the Ethernet cable attached to the conference
                                             					 phone. | The
                                                      						  Cisco Unified IP Conference Phone supports IEEE 802.3af Class 3 power on
                                                      						  signal pairs and spare pairs. When
                                                      						  using a sound base in Linked Mode, the primary sound base must be connected
                                                      						  using the CP-PWR-CUBE-3 external power supply. To
                                                      						  ensure uninterruptible operation of the conference phone, make sure that the
                                                      						  switch has a backup power supply. Make
                                                      						  sure that the CatOS or IOS version running on your switch supports your
                                                      						  intended conference phone deployment. Refer to the documentation for your
                                                      						  switch for operating system version information. |

| Document Topics | URL |
|---|---|
| PoE Solutions | http://www.cisco.com/en/US/netsol/ns340/ns394/ns147/ns412/networking_solutions_package.html |
| Cisco Catalyst Switches | http://www.cisco.com/univercd/cc/td/doc/product/lan/index.htm |
| Integrated Service Routers | http://www.cisco.com/en/US/products/hw/routers/index.html |
| Cisco IOS Software | http://www.cisco.com/en/US/products/sw/iosswrel/products_ios_cisco_ios_software_category_home.html |

| Note | You can also
                                             				assign an alternative TFTP server to use instead of the one that DHCP assigns. |
|---|---|

| Method | Requires MAC Address? | Notes |
|---|---|---|
| Autoregistration | No | Results in the automatic
                                       				  assignment of a directory number to the conference phone, and provides no
                                       				  control over directory number assignment to conference phones. Not
                                          					 available when security or encryption is enabled. In this case, the conference
                                          					 phone must be manually added to the Cisco Unified Communications Manager
                                          					 database. |
| Autoregistration with the
                                       				  Tool for Auto-Registered Phones Support (TAPS) | No | Requires autoregistration
                                       				  and the Bulk Administration Tool (BAT). This
                                          					 method updates the Cisco Unified Communications Manager database with the MAC
                                          					 address and DNs for the device when user calls TAPS from the conference phone. |
| Using Cisco Unified
                                       				  Communications Manager Administration | Yes | Requires you to add
                                       				  conference phones individually. |
| Using BAT | Yes | Allows for
                                          					 the simultaneous registration of multiple conference phones of the same model. Allows you
                                          					 to schedule when conference phones are added to Cisco Unified Communications
                                          					 Manager. |

| Note | Cisco recommends
                                          		  that you use autoregistration to add fewer than 100 conference phones to your
                                          		  network. To add more than 100 conference phones to your network, use the Bulk
                                          		  Administration Tool (BAT). |
|---|---|

| Note | When you configure
                                          		  the client for mixed mode through the Cisco CTL client, autoregistration is
                                          		  automatically disabled. When you configure the cluster for nonsecure mode
                                          		  through the Cisco CTL client, autoregistation is automatically enabled. |
|---|---|

| Note | Cisco recommends
                                          		  that you use autoregistration to add fewer than 100 conference phones to your
                                          		  network. To add more than 100 conference phones to your network, use the Bulk
                                          		  Administration Tool (BAT). |
|---|---|

| Note | When you configure
                                          		  the client for mixed mode through the Cisco CTL client, autoregistration is
                                          		  automatically disabled. When you configure the cluster for nonsecure mode
                                          		  through the Cisco CTL client, autoregistation is automatically enabled. |
|---|---|