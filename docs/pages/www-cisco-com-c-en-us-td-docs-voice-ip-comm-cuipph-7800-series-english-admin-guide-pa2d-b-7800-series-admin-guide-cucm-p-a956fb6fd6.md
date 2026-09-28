---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-english-admin-guide-pa2d-b-7800-series-admin-guide-cucm-p-a956fb6fd6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/english/admin-guide/pa2d_b_7800-series-admin-guide-cucm/pa2d_b_7800-series-admin-guide-cucm_chapter_0100.html
retrieved_at: 2026-08-21T13:26:09.608315+00:00
---

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Updated: May 29, 2025

Chapter: Cisco IP Phone Installation

## Chapter: Cisco IP Phone Installation

# Cisco IP Phone Installation

## Verify the Network Setup

As they deploy a new IP telephony system, system administrators and network administrators must complete several initial configuration
                              tasks to prepare the network for IP telephony service. For information and a checklist for setting up and configuring a Cisco
                              IP telephony network, see the documentation for your particular Cisco Unified Communications Manager release.

For the phone to operate successfully as an endpoint in your network, your network must meet specific requirements. One requirement
                              is the appropriate bandwidth. The phones require more bandwidth than the recommended 32 kbps when they register to Cisco Unified
                              Communications Manager. Consider this higher bandwidth requirement when you configure your QoS bandwidth. For more information,
                              refer to Cisco Collaboration System 12.x Solution Reference Network Designs (SRND) or later ( https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/srnd/collab12/collab12.html ).

The phone displays the date and time from Cisco Unified
                                             				Communications Manager . The time displayed on the phone can differ from the Cisco Unified
                                             				Communications Manager time by up to 10 seconds.

Step 1

Configure a VoIP Network to meet the following requirements:

VoIP is configured on your routers and gateways.

Cisco Unified
                                                   				Communications Manager is installed in your network and is configured to handle call processing.

Step 2

Set up the network to support one of the following:

DHCP support

Manual assignment of IP address, gateway, and subnet mask

## Activation Code Onboarding for On-premises Phones

You can use Activation Code Onboarding to quickly set up new phones without autoregistration. With this approach, you control
                              the phone onboarding process using the one of the following:

Cisco Unified Communications Bulk Administration Tool (BAT)

Cisco Unified Communications Manager Administration interface

Administrative XML Web Service (AXL)

Enable this feature from the Device Information section of the Phone Configuration page. Select Require Activation Code for Onboarding if you want this feature to apply to a single on-premises phone.

Users must enter an activation code before their phones can register. Activation Code Onboarding can be applied to individual
                              phones, a group of phones, or across an entire network.

This is an easy way for users to onboard their phones because they only enter a 16-digit activation code. Codes are entered
                              either manually or with a QR code if a phone has a video camera. We recommend that you use a secure method to give users this
                              information. But if a user is assigned to a phone, then this information is available on the Self Care Portal. The audit log
                              records when a user accesses the code from the portal.

Activation codes can only be used once, and they expire after 1 week by default. If a code expires, you will have to provide
                              the user with a new one.

You will find this approach an easy way to keep your network secure because a phone cannot register until the Manufacturing
                              Installed Certificate (MIC) and activation code are verified. This method is also a convenient way to bulk onboard phones
                              because it doesn't use the Tool for Auto-registered Phone Support (TAPS) or autoregistration. The rate of onboarding is one
                              phone per second or about 3600 phones per hour. Phones can be added with the Cisco Unified Communications Manager Administrative,
                              with Administrative XML Web Service (AXL), or with BAT.

Existing phones reset after they are configured for Activation Code Onboarding. They don't register until the activation code
                              is entered and the phone MIC is verified. Inform current users that you are moving towards Activation Code Onboarding before
                              you implement it.

For more information, see Administration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.0(1) or later.

## Activation Code Onboarding and Mobile and Remote Access

You can use Activation Code Onboarding with Mobile and Remote Access when deploying Cisco IP phones for remote users. This
                              feature is a secure way to deploy off-premises phones when autoregistration is not required. But you can configure a phone
                              for autoregistration when on-premises, and activation codes when off-premises. This feature is similar to Activation Code
                              Onboarding for on-premises phones, but it makes activation code available for off-premises phones also.

Activation Code Onboarding for Mobile and Remote Access requires Cisco Unified Communications Manager 12.5(1)SU1 or later,
                              and Cisco Expressway X12.5 or later. Smart Licensing should be enabled also.

You enable this feature from the Cisco Unified Communications Manager Administration, but note the following:

Enable this feature from the Device Information section of the Phone Configuration page.

Select Require Activation Code for Onboarding if you want this feature to apply just to a single on-premises phone.

Select Allow Activation Code via MRA and Require Activation Code for Onboarding if you want to use Activation Onboarding for a single off-premises phone. If the phone is on-premises, it changes to Mobile
                                    and Remote Access mode and uses the Expressway. If the phone cannot reach the Expressway, it does not register until it is
                                    off premises.

For more information, see the following documents:

Administration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.0(1)

Mobile and Remote Access Through Cisco Expressway for Cisco Expressway X12.5 or later

## Enable Autoregistration for Phones

The Cisco IP Phone
                              		  requires Cisco Unified Communications Manager to handle call processing. See
                              		  the 
                              		  documentation for your particular Cisco Unified Communications Manager release or the context-sensitive
                              		  help in the Cisco Unified Communications Manager Administration to ensure that
                              		  Cisco Unified Communications Manager is set up properly to manage the phone and
                              		  to properly route and process calls.

Before you install
                              		  the Cisco IP Phone, you must choose a method for adding phones to the Cisco
                              		  Unified Communications Manager database.

By enabling
                              		  autoregistration before you install the phones, you can:

Add phones
                                    				without first gathering MAC addresses from the phones.

Automatically
                                    				add a Cisco IP Phone to the Cisco Unified Communications Manager database when
                                    				you physically connect the phone to your IP telephony network. During
                                    				autoregistration, Cisco Unified Communications Manager assigns the next
                                    				available sequential directory number to the phone.

Quickly enter
                                    				phones into the Cisco Unified Communications Manager database and modify any
                                    				settings, such as the directory numbers, from Cisco Unified Communications
                                    				Manager.

Move
                                    				autoregistered phones to new locations and assign them to different device
                                    				pools without affecting their directory numbers.

Autoregistration is disabled by default. In some cases, you might not want to use autoregistration; for example, if you want
                              to assign a specific directory number to the phone, or if you want to use a secure connection with Cisco Unified Communications
                              Manager. For information about enabling autoregistration, see the documentation for your particular Cisco Unified Communications
                              Manager release. When you configure the cluster for mixed mode through the Cisco CTL client, autoregistration is automatically
                              disabled, however you can enable it. When you configure the cluster for nonsecure mode through the Cisco CTL client, autoregistration
                              is not enabled automatically.

You can add phones with autoregistration and TAPS, the Tool for
                              		  AutoRegistered Phones Support, without first gathering MAC addresses from
                              		  phones.

TAPS works with the Bulk Administration Tool (BAT) to update a batch
                              		  of phones that were already added to the Cisco Unified Communications Manager
                              		  database with dummy MAC addresses. Use TAPS to update MAC addresses and to
                              		  download predefined configurations for phones.

Cisco recommends that you use autoregistration and TAPS to add fewer
                              		  than 100 phones to your network. To add more than 100 phones to your network,
                              		  use the Bulk Administration Tool (BAT).

To implement TAPS,
                              		  you or the end user dials a TAPS directory number and follows voice prompts.
                              		  After the process is complete, the phone contains the directory number and
                              		  other settings, and the phone is updated in Cisco Unified Communications
                              		  Manager Administration with the correct MAC address.

Verify that
                              		  autoregistration is enabled and is properly configured in Cisco Unified
                              		  Communications Manager Administration before you connect any Cisco IP Phone to
                              		  the network. For information about enabling and configuring autoregistration,
                              		  see the documentation for your particular Cisco Unified Communications Manager release.

Autoregistration must be enabled in Cisco Unified Communications
                              		Manager Administration for TAPS to function.

Step 1

In Cisco
                                       			 Unified Communications Manager Administration, click System > Cisco Unified CM .

Step 2

Click Find and select the required server.

Step 3

In Auto-registration Information , configure these fields.

Universal Device Template

Universal Line Template

Starting Directory Number

Ending Directory Number

Step 4

Uncheck the Auto-registration Disabled on this Cisco Unified Communications Manager check box.

Step 5

Click Save .

Step 6

Click Apply Config .

## Install the Cisco
                        	 IP Phone

After the phone connects to
                              		  the network, the phone startup process begins, and the phone registers with
                              		  CiscoUnified Communications Manager. To finish installing the phone, configure
                              		  the network settings on the phone depending on whether you enable or disable
                              		  DHCP service.

If you
                              		  used autoregistration, you need to update the specific configuration
                              		  information for the phone such as associating the phone with a user, changing
                              		  the button table, or directory number.

Before using
                                          			 external devices, read External Devices .

If you only have one LAN cable at your desk, you can plug your phone into the LAN with the SW port and then connect your computer
                              into the PC port. For more information, see Share a Network Connection with Your Phone and Computer .

You can also daisy chain two phones together.  Connect the PC port of the first phone to the SW port of the second phone.

Caution

Do not connect the SW and PC ports into the LAN.

Step 1

Choose the
                                       			 power source for the phone:

Power
                                                					 over Ethernet (PoE)

External
                                                					 power supply

For more
                                          				information, see Phone Power Requirements .

Step 2

Connect the handset to the handset port  and press the cable into the cable channel.

The wideband-capable handset is designed especially for use with a Cisco IP Phone. The handset includes a light strip that
                                          indicates incoming calls and waiting voice messages.

Caution

Failure to press the cable into the channel in the phone can lead to cable damage.

Step 3

Connect a headset to the headset port and press the cable into the cable channel. You can add a headset later if you do not
                                       connect one now.

The Cisco IP Phone 7811 does not have a headset port.

Caution

Failure to press the cable into the channel in the phone can lead to cable damage.

Step 4

Connect a wireless headset. You can add a wireless headset later
                                       			 if you do not want to connect one now. For more information, see your wireless
                                       			 headset documentation.

The Cisco IP Phone 7811 does not support a headset.

Step 5

Connect a
                                       			 straight-through Ethernet cable from the switch to the network port labeled
                                       			 10/100 SW on the Cisco IP Phone (10/100/1000 SW on 
                                       			 Cisco IP Phone
                                       				7841).
                                       			 Each Cisco IP Phone ships with one Ethernet cable in the box.

Use Category
                                          				3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for
                                          				100Mbps connections; and Category 5e or 6 for 1000 Mbps connections. For more
                                          				information, see Network and Computer Port Pinouts .

Step 6

Connect a straight-through Ethernet cable from another network
                                       			 device, such as a desktop computer, to the computer port on the Cisco IP Phone.
                                       			 You can connect another network device later if you do not connect one now.

Use Category
                                          				3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for
                                          				100Mbps connections; and Category 5e or 6 for 1000 Mbps connections. For more
                                          				information, see Network and Computer Port Pinouts for guidelines.

Step 7

If the phone is on a desk, adjust the footstand. With a wall-mounted phone, you might need to adjust the handset rest to ensure
                                       that the receiver cannot slip out of the cradle.

You cannot adjust the Cisco IP Phone 7811 footstand.

Step 8

Monitor the
                                       			 phone startup process. This step verifies that the phone is configured
                                       			 properly.

Step 9

If you are
                                       			 configuring the network settings on the phone, you can set up an IP address for
                                       			 the phone by either using DHCP or manually entering an IP address.

Step 10

Upgrade the
                                       			 phone to the current firmware image.

Step 11

Make calls
                                       			 with the Cisco IP Phone to verify that the phone and features work correctly.

See the Cisco IP Phone 7800 Series User Guide .

Step 12

Provide
                                       			 information to end users about how to use their phones and how to configure
                                       			 their phone options. This step ensures that users have adequate information to
                                       			 successfully use their Cisco IPPhones.

### Share a Network Connection with Your Phone and Computer

Both your phone and your computer must connect to your network to function. If you only have one Ethernet port, then your
                                 devices can share the network connection.

#### Before you begin

Your administrator must enable the PC port in Cisco Unified Communications Manager before you can use it.

Step 1

Connect the phone SW port to the LAN with an Ethernet cable.

Step 2

Connect your computer to the phone PC port with an Ethernet cable.

## Set Up the Phone from
                        	 the Setup Menus

The phone includes
                              		  many configurable network settings that you may need to modify before the phone
                              		  is functional for your users. You can access these settings, and change some of
                              		  them, through menus on the phone.

The phone
                              		  includes the following setup menus:

Network Setup:
                                    				Provides options for viewing and configuring a variety of network settings.

IPv4
                                          					 Setup: This submenu provides additional network options.

IPv6
                                          					 Setup: This submenu provides additional network options.

Security
                                    				Setup: Provides options for viewing and configuring a variety of security
                                    				settings.

You can control whether a phone has access to the Settings menu or to options on this menu. Use the Settings Access field in the Cisco Unified
                                             				Communications Manager Administration Phone Configuration window to control access. The Settings Access field accepts these values:

Enabled: Allows access to the Settings menu.

Disabled: Prevents access to most entries in the Settings menu. The user can still access Settings > Status .

Restricted: Allows access to the User Preferences and Status menu items and allows volume changes to be saved. Prevents access to other options on the Settings menu.

If you cannot access an option on the Admin Settings menu, check the Settings Access field.

You configure
                              		  settings that are display-only on the phone in Cisco Unified
                                 				Communications Manager Administration .

Step 1

Press Applications .

Step 2

Select Admin
                                          				Settings .

Step 3

Enter password if required, then click Sign-In .

Step 4

Select Network Setup or Security Setup .

Step 5

Perform one of
                                       			 these actions to display the desired menu:

- Use the navigation arrows
                                          				to select the desired menu and then press Select .

- Use the keypad on the phone
                                          				to enter the number that corresponds to the menu.

Step 6

To display a
                                       			 submenu, repeat step 5.

Step 7

To exit a menu, press Back .

### Apply a Phone Password

You can apply a password to the phone. If you do, no changes can be made to the administrative options on the phone without
                                 password entry on the Admin Settings phone screen.

Step 1

In Cisco Unified Communications Manager Administration, navigate
                                          			 to the Common Phone Profile Configuration window ( Device > Device
                                                				  Settings > Common Phone Profile ).

Step 2

Enter a password in the Local Phone Unlock Password option.

Step 3

Apply the password to the common phone profile that the phone
                                          			 uses.

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

Press Revert before pressing Apply to discard any changes that you made.

To enter a period (for example, in an IP address), press * on the keypad.

To enter a colon for an IPv6 address, press * on the keypad.

The Cisco IP
                                             			 Phone provides several methods to reset or restore option settings, if
                                             			 necessary.

## Configure Network Settings

Step 1

Press Applications .

Step 2

To access the Network Settings menu, select Admin settings > Network Setup .

Step 3

Set the fields as described in .

Step 4

After you have set the fields, select Apply and Save .

Step 5

Reboot the phone.

### Network Setup

The Network Setup menu contains fields and submenus for IPv4 and IPv6. To change some of the fields, first disable DHCP.

Entry

Type

Default

Description

IPv4 setup

Menu

See the IPv4 Fields section.

This option displays only when the phone is configured in IPv4-only mode or in IPv4 and IPv6 mode.

IPv6 setup

Menu

See the “IPv6 Fields” section.

Host Name

String

Host name that the DHCP server assigned to the phone.

Domain Name

String

Name of the Domain Name System (DNS) domain in which the phone resides.

To change this field, turn off DHCP.

Operational VLAN ID

Auxiliary Virtual Local Area Network (VLAN) configured on a Cisco Catalyst switch of which the phone is a member.

This setting is blank if the auxiliary VLAN or the Administrative VLAN are configured.

If the phone has not received an auxiliary VLAN, this option indicates the Administrative VLAN.

The phone doesn't inherit the Operational VLAN from Admin VLAN if Cisco Discovery Protocol or Link Level Discovery Protocol
                                                Media Endpoint Discovery is enabled.

To assign a VLAN ID manually, use the Admin VLAN ID option.

Admin VLAN ID

Auxiliary VLAN of which the phone is a member.

Used only if the phone does not receive an auxiliary VLAN from the switch; otherwise, this value is ignored.

PC VLAN

Allows the phone to interoperate with third-party switches that do not support a voice VLAN. The Admin VLAN ID option must
                                                be set before you can change this option.

SW Port Setup

Auto Negotiate

1000 Full

100 Half

10 Half

10 Full

Auto Negotiate

Speed and duplex of the network port. Valid values specify:

- Auto Negotiate

- 1000 Full:1000-BaseT/full duplex

- 100 Half: 100-BaseT/half duplex

- 100 Full: 100-BaseT/full duplex

- 10 Half: 10-BaseT/half duplex

- 10 Full: 10-BaseT/full duplex

If the phone is connected to a switch, configure the switch port to the same speed as the phone, or configure both to autonegotiate.

Unlock network configuration options if you want to edit this setting. If you change the setting of this option, you must
                                                change the PC Port Configuration option to the same setting.

PC Port Setup

Auto Negotiate

1000 Full

100 Half

10 Half

10 Full

Auto Negotiate

Speed and duplex of the Computer (access) port. Valid values:

- Auto Negotiate

- 1000 Full: 1000-BaseT/full duplex

- 100 Half: 100-BaseT/half duplex

- 100 Full: 100-BaseT/full duplex

- 10 Half: 10-BaseT/half duplex

- 10 Full: 10-BaseT/full duplex

If the phone is connected to a switch, configure the port on the switch to the same speed as the phone, or configure both
                                                to autonegotiate.

Unlock network configuration options if you want to change this field. If you change the setting, you must change the SW Port
                                                Configuration option to the same setting.

To configure the setting on multiple phones simultaneously, enable Remote Port Configuration in the Enterprise Phone Configuration
                                                window ( System > Enterprise Phone Configuration ).

If the ports are configured for Remote Port Configuration in Cisco Unified Communications Manager Administration, the data
                                                cannot be changed on the phone.

UDP-MED

### IPv4 Fields

Entry

Type

Default

Description

DHCP Enabled

Indicates whether the phone has DHCP enabled or disabled.

When DHCP is enabled, the DHCP server assigns the phone an IP address. When DHCP is disabled, the administrator must manually
                                                assign an IP address to the phone.

IP Address

Internet Protocol (IP) address of the phone.

If you assign an IP address with this option, you must also assign a subnet mask and default router. See the Subnet Mask and
                                                Default Router options in this table.

Subnet Mask

Subnet mask used by the phone.

Default Router

Default router used by the phone.

DNS Server 1

Primary Domain Name System (DNS) server (DNS Server 1) that the phone uses.

Alternate TFTP

Indicates whether the phone is using an alternate TFTP server.

TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server that the phone uses. If you are not using DHCP in your network and you
                                                want to change this server, you must use the TFTP Server 1 option.

If you set the Alternate TFTP option to On, you must enter a nonzero value for the TFTP Server 1 option.

If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock
                                                the file before you can save changes to the TFTP Server 1 option. In this case, the phone deletes the file when you save changes
                                                to the TFTP Server 1 option. A new CTL or ITL file downloads from the new TFTP Server 1 address.

When the phone looks for the TFTP server, the phone gives precedence to manually assigned TFTP servers, regardless of the
                                                protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for
                                                the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP
                                                server in this order:

Any manually assigned IPv4 TFTP servers

Any manually assigned IPv6 servers

DHCP assigned TFTP servers

DHCPv6 assigned TFTP servers

For information about the CTL and ITL files, see the Cisco Unified Communications Manager Security Guide .

TFTP Server 2

Optional backup TFTP server that the phone uses if the primary TFTP server is unavailable.

If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock
                                                either of the files before you can save changes to the TFTP Server 2 option. In this case, the phone deletes either of the
                                                files when you save changes to the TFTP Server 2 option. A new CTL or ITL file downloads from the new TFTP Server 2 address.

If you forget to unlock the CTL or ITL file, you can change the TFTP Server 2 address in either file, then erase them by pressing
                                                Erase from the Security Configuration menu. A new CTL or ITL file downloads from the new TFTP Server 2 address.

When the phone looks for the TFTP server, it gives precedence to manually assigned TFTP servers, regardless of the protocol.
                                                If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP
                                                server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server
                                                in the following order:

Any manually assigned IPv4 TFTP servers

Any manually assigned IPv6 servers

DHCP assigned TFTP servers

DHCPv6 assigned TFTP servers

For information about the CTL or ITL file, see Cisco Unified Communications Manager Security Guide.

DHCP Address Released

Releases the IP address that DHCP assigned.

This field is editable if DHCP is enabled. If you wish to remove the phone from the VLAN and release the IP address for reassignment,
                                                set this option to Yes and press Apply.

### IPv6 Fields

IP Addressing Mode

IP Addressing Mode Preference for Signalling

If IPv6 is enabled in the Unified cluster, the default setting for IP addressing mode is IPv4 and IPv6 . In this addressing mode, the phone acquires and uses one IPv4 address and one IPv6 address. It can use the IPv4 and the
                                 IPv6 address as required for media. The phone uses either the IPv4 or IPv6 address for call control signaling.

For more details about IPv6 deployment, see the IPv6 Deployment Guide for Cisco Collaboration Systems Release 12.0 .

When Wi-Fi is disabled: Ethernet Setup > IPv6 setup

When Wi-Fi is enabled: Wi-Fi Client Setup > IPv6 setup

Use the phone keypad to enter or edit an IPv6 address. To enter a colon, press the asterisk (*) on the keypad. To enter hexadecimal
                                 digits a, b, and c, press 2 on the keypad, scroll to select the required digit, and press Enter . To enter hexadecimal digits d, e, and f, press 3 on the keypad, scroll to select the required digit, and press Enter .

The following table describes the IPv6 related information found in the IPv6 menu.

Entry

Type

Default value

Description

DHCPv6 Enabled

Yes

Indicates the method that the phone uses to get the IPv6-only address.

When DHCPv6 is enabled, the phone gets the IPv6 address either from DHCPv6 server or from SLAAC by RA sent by the IPv6-enabled
                                             router. And if DHCPv6 is disabled, the phone will not have any stateful (from DHCPv6 server) or stateless (from SLAAC) IPv6
                                             address.

IPv6 Address

::

Displays the current IPv6-only address of the phone or allows the user to enter a new IPv6 address.

Eight sets of hexadecimal digits separated by colons X:X:X:X:X:X:X:X

Compressed format to collapse a single run of consecutive zero groups into a single group represented by a double colon.

If the IP address is assigned with this option, you must also assign the IPv6 prefix length and the default router.

IPv6 Prefix Length

0

Displays the current prefix length for the subnet or allows the user to enter a new prefix length.

The subnet prefix length is a decimal value from 1 to 128.

IPv6 Default Router

::

Displays the default router used by the phone or allows the user to enter a new IPv6-only default router.

IPv6 DNS Server 1

::

Displays the primary DNSv6 server used by the phone or allows the user to enter a new server.

IPv6 Alternate TFTP

No

Allows the user to enable the use of an alternate (secondary) IPv6 TFTP server.

IPv6 TFTP Server 1

::

Displays the primary IPv6 TFTP server used by the phone or allows the user to set a new primary TFTP server.

IPv6 TFTP Server 2

::

(Optional) Displays the secondary IPv6 TFTP server used if the primary IPv6 TFTP server is unavailable or allows the user
                                             to set a new secondary TFTP server.

IPv6 Address Released

No

Allows the user to release IPv6-related information.

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

For Cisco IP Phone 8861, if you are using a power cube but there is no Power over Ethernet available, then the wifi will be
                                                      enabled.

## Configure Phone Services for Users

You can
                              		  give users access to Cisco IP Phone Services on the IP phone. You can also
                              		  assign a button to different phone services. The IP phone manages
                              		  each service as a separate application.

Before a
                              		  user can access any service:

Use Cisco Unified
                                       				Communications Manager Administration to configure services that are not present by default.

The user must subscribe to services by using the Cisco Unified
                                       				Communications Self Care Portal . This web-based application provides a graphical user interface (GUI) for limited, end-user configuration of IP phone applications.
                                    However, a user cannot subscribe to any service that you configure as an enterprise subscription.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

Before
                              		  you set up services, gather the URLs for the sites that you want to set up and
                              		  verify that users can access those sites from your corporate IP telephony
                              		  network. This activity is not applicable for the default services that Cisco
                              		  provides.

Step 1

In Cisco Unified
                                          				Communications Manager Administration , choose Device > Device
                                             				  Settings > Phone Services .

Step 2

Verify that
                                       			 your users can access the Cisco Unified
                                          				Communications Self Care Portal , from which they can select and
                                       			 subscribe to configured services.

See Self Care Portal Overview for a summary of the information that you must provide to end users.

## Change a User's Phone Model

You or your user can change a user's phone model. The change can be required for a number of reasons, for example:

You have updated your Cisco Unified
                                       				Communications Manager (Unified CM) to a software version that doesn't support the phone model.

The user wants a different phone model from their current model.

The phone requires repair or replacement.

The Unified CM identifies the old phone and uses the old phone's MAC address to identify the old phone configuration. The
                              Unified CM copies the old phone configuration into the entry for the new phone. The new phone then has the same configuration
                              as the old phone.

Limitation : If the old phone has more lines or line buttons than the new phone, the new phone doesn't have the extra lines or line buttons
                              configured.

The phone reboots when the configuration is complete.

### Before you begin

Set up your Cisco Unified
                                 				Communications Manager according to the instructions in the Feature Configuration Guide for Cisco Unified Communications Manager .

You need a new, unused phone that comes preinstalled with Firmware Release 12.8(1) or later.

Step 1

Power off the old phone.

Step 2

Power on the new phone.

Step 3

On the new phone, select Replace an existing phone .

Step 4

Enter the primary extension of the old phone.

Step 5

If the old phone had a PIN assigned, enter the PIN.

Step 6

Press Submit .

Step 7

If there is more than one device for the user, select the device to replace and press Continue .

| Note | The phone displays the date and time from Cisco Unified
                                             				Communications Manager . The time displayed on the phone can differ from the Cisco Unified
                                             				Communications Manager time by up to 10 seconds. |
|---|---|

| Step 1 | Configure a VoIP Network to meet the following requirements: VoIP is configured on your routers and gateways. Cisco Unified
                                                   				Communications Manager is installed in your network and is configured to handle call processing. |
|---|---|
| Step 2 | Set up the network to support one of the following: DHCP support Manual assignment of IP address, gateway, and subnet mask |

| Step 1 | In Cisco
                                       			 Unified Communications Manager Administration, click System > Cisco Unified CM . |
|---|---|
| Step 2 | Click Find and select the required server. |
| Step 3 | In Auto-registration Information , configure these fields. Universal Device Template Universal Line Template Starting Directory Number Ending Directory Number |
| Step 4 | Uncheck the Auto-registration Disabled on this Cisco Unified Communications Manager check box. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config . |

| Note | Before using
                                          			 external devices, read External Devices . |
|---|---|

| Caution | Do not connect the SW and PC ports into the LAN. |
|---|---|

| Step 1 | Choose the
                                       			 power source for the phone: Power
                                                					 over Ethernet (PoE) External
                                                					 power supply For more
                                          				information, see Phone Power Requirements . |
|---|---|
| Step 2 | Connect the handset to the handset port  and press the cable into the cable channel. The wideband-capable handset is designed especially for use with a Cisco IP Phone. The handset includes a light strip that
                                          indicates incoming calls and waiting voice messages. Caution Failure to press the cable into the channel in the phone can lead to cable damage. | Caution | Failure to press the cable into the channel in the phone can lead to cable damage. |
| Caution | Failure to press the cable into the channel in the phone can lead to cable damage. |
| Step 3 | Connect a headset to the headset port and press the cable into the cable channel. You can add a headset later if you do not
                                       connect one now. Note The Cisco IP Phone 7811 does not have a headset port. Caution Failure to press the cable into the channel in the phone can lead to cable damage. | Note | The Cisco IP Phone 7811 does not have a headset port. | Caution | Failure to press the cable into the channel in the phone can lead to cable damage. |
| Note | The Cisco IP Phone 7811 does not have a headset port. |
| Caution | Failure to press the cable into the channel in the phone can lead to cable damage. |
| Step 4 | Connect a wireless headset. You can add a wireless headset later
                                       			 if you do not want to connect one now. For more information, see your wireless
                                       			 headset documentation. Note The Cisco IP Phone 7811 does not support a headset. | Note | The Cisco IP Phone 7811 does not support a headset. |
| Note | The Cisco IP Phone 7811 does not support a headset. |
| Step 5 | Connect a
                                       			 straight-through Ethernet cable from the switch to the network port labeled
                                       			 10/100 SW on the Cisco IP Phone (10/100/1000 SW on 
                                       			 Cisco IP Phone
                                       				7841).
                                       			 Each Cisco IP Phone ships with one Ethernet cable in the box. Use Category
                                          				3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for
                                          				100Mbps connections; and Category 5e or 6 for 1000 Mbps connections. For more
                                          				information, see Network and Computer Port Pinouts . |
| Step 6 | Connect a straight-through Ethernet cable from another network
                                       			 device, such as a desktop computer, to the computer port on the Cisco IP Phone.
                                       			 You can connect another network device later if you do not connect one now. Use Category
                                          				3, 5, 5e, or 6 cabling for 10 Mbps connections; Category 5, 5e, or 6 for
                                          				100Mbps connections; and Category 5e or 6 for 1000 Mbps connections. For more
                                          				information, see Network and Computer Port Pinouts for guidelines. |
| Step 7 | If the phone is on a desk, adjust the footstand. With a wall-mounted phone, you might need to adjust the handset rest to ensure
                                       that the receiver cannot slip out of the cradle. Note You cannot adjust the Cisco IP Phone 7811 footstand. | Note | You cannot adjust the Cisco IP Phone 7811 footstand. |
| Note | You cannot adjust the Cisco IP Phone 7811 footstand. |
| Step 8 | Monitor the
                                       			 phone startup process. This step verifies that the phone is configured
                                       			 properly. |
| Step 9 | If you are
                                       			 configuring the network settings on the phone, you can set up an IP address for
                                       			 the phone by either using DHCP or manually entering an IP address. |
| Step 10 | Upgrade the
                                       			 phone to the current firmware image. |
| Step 11 | Make calls
                                       			 with the Cisco IP Phone to verify that the phone and features work correctly. See the Cisco IP Phone 7800 Series User Guide . |
| Step 12 | Provide
                                       			 information to end users about how to use their phones and how to configure
                                       			 their phone options. This step ensures that users have adequate information to
                                       			 successfully use their Cisco IPPhones. |

| Caution | Failure to press the cable into the channel in the phone can lead to cable damage. |
|---|---|

| Note | The Cisco IP Phone 7811 does not have a headset port. |
|---|---|

| Caution | Failure to press the cable into the channel in the phone can lead to cable damage. |
|---|---|

| Note | The Cisco IP Phone 7811 does not support a headset. |
|---|---|

| Note | You cannot adjust the Cisco IP Phone 7811 footstand. |
|---|---|

| Step 1 | Connect the phone SW port to the LAN with an Ethernet cable. |
|---|---|
| Step 2 | Connect your computer to the phone PC port with an Ethernet cable. |

| Note | You can control whether a phone has access to the Settings menu or to options on this menu. Use the Settings Access field in the Cisco Unified
                                             				Communications Manager Administration Phone Configuration window to control access. The Settings Access field accepts these values: Enabled: Allows access to the Settings menu. Disabled: Prevents access to most entries in the Settings menu. The user can still access Settings > Status . Restricted: Allows access to the User Preferences and Status menu items and allows volume changes to be saved. Prevents access to other options on the Settings menu. If you cannot access an option on the Admin Settings menu, check the Settings Access field. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin
                                          				Settings . |
| Step 3 | Enter password if required, then click Sign-In . |
| Step 4 | Select Network Setup or Security Setup . |
| Step 5 | Perform one of
                                       			 these actions to display the desired menu: Use the navigation arrows
                                          				to select the desired menu and then press Select . Use the keypad on the phone
                                          				to enter the number that corresponds to the menu. |
| Step 6 | To display a
                                       			 submenu, repeat step 5. |
| Step 7 | To exit a menu, press Back . |

| Step 1 | In Cisco Unified Communications Manager Administration, navigate
                                          			 to the Common Phone Profile Configuration window ( Device > Device
                                                				  Settings > Common Phone Profile ). |
|---|---|
| Step 2 | Enter a password in the Local Phone Unlock Password option. |
| Step 3 | Apply the password to the common phone profile that the phone
                                          			 uses. |

| Note | The Cisco IP
                                             			 Phone provides several methods to reset or restore option settings, if
                                             			 necessary. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | To access the Network Settings menu, select Admin settings > Network Setup . |
| Step 3 | Set the fields as described in . |
| Step 4 | After you have set the fields, select Apply and Save . |
| Step 5 | Reboot the phone. |

| Entry | Type | Default | Description |
|---|---|---|---|
| IPv4 setup | Menu |  | See the IPv4 Fields section. This option displays only when the phone is configured in IPv4-only mode or in IPv4 and IPv6 mode. |
| IPv6 setup | Menu |  | See the “IPv6 Fields” section. |
| Host Name | String |  | Host name that the DHCP server assigned to the phone. |
| Domain Name | String |  | Name of the Domain Name System (DNS) domain in which the phone resides. To change this field, turn off DHCP. |
| Operational VLAN ID |  |  | Auxiliary Virtual Local Area Network (VLAN) configured on a Cisco Catalyst switch of which the phone is a member. This setting is blank if the auxiliary VLAN or the Administrative VLAN are configured. If the phone has not received an auxiliary VLAN, this option indicates the Administrative VLAN. The phone doesn't inherit the Operational VLAN from Admin VLAN if Cisco Discovery Protocol or Link Level Discovery Protocol
                                                Media Endpoint Discovery is enabled. To assign a VLAN ID manually, use the Admin VLAN ID option. |
| Admin VLAN ID |  |  | Auxiliary VLAN of which the phone is a member. Used only if the phone does not receive an auxiliary VLAN from the switch; otherwise, this value is ignored. |
| PC VLAN |  |  | Allows the phone to interoperate with third-party switches that do not support a voice VLAN. The Admin VLAN ID option must
                                                be set before you can change this option. |
| SW Port Setup | Auto Negotiate 1000 Full 100 Half 10 Half 10 Full | Auto Negotiate | Speed and duplex of the network port. Valid values specify: Auto Negotiate 1000 Full:1000-BaseT/full duplex 100 Half: 100-BaseT/half duplex 100 Full: 100-BaseT/full duplex 10 Half: 10-BaseT/half duplex 10 Full: 10-BaseT/full duplex If the phone is connected to a switch, configure the switch port to the same speed as the phone, or configure both to autonegotiate. Unlock network configuration options if you want to edit this setting. If you change the setting of this option, you must
                                                change the PC Port Configuration option to the same setting. |
| PC Port Setup | Auto Negotiate 1000 Full 100 Half 10 Half 10 Full | Auto Negotiate | Speed and duplex of the Computer (access) port. Valid values: Auto Negotiate 1000 Full: 1000-BaseT/full duplex 100 Half: 100-BaseT/half duplex 100 Full: 100-BaseT/full duplex 10 Half: 10-BaseT/half duplex 10 Full: 10-BaseT/full duplex If the phone is connected to a switch, configure the port on the switch to the same speed as the phone, or configure both
                                                to autonegotiate. Unlock network configuration options if you want to change this field. If you change the setting, you must change the SW Port
                                                Configuration option to the same setting. To configure the setting on multiple phones simultaneously, enable Remote Port Configuration in the Enterprise Phone Configuration
                                                window ( System > Enterprise Phone Configuration ). If the ports are configured for Remote Port Configuration in Cisco Unified Communications Manager Administration, the data
                                                cannot be changed on the phone. |
| UDP-MED |  |  |  |

| Entry | Type | Default | Description |
|---|---|---|---|
| DHCP Enabled |  |  | Indicates whether the phone has DHCP enabled or disabled. When DHCP is enabled, the DHCP server assigns the phone an IP address. When DHCP is disabled, the administrator must manually
                                                assign an IP address to the phone. |
| IP Address |  |  | Internet Protocol (IP) address of the phone. If you assign an IP address with this option, you must also assign a subnet mask and default router. See the Subnet Mask and
                                                Default Router options in this table. |
| Subnet Mask |  |  | Subnet mask used by the phone. |
| Default Router |  |  | Default router used by the phone. |
| DNS Server 1 |  |  | Primary Domain Name System (DNS) server (DNS Server 1) that the phone uses. |
| Alternate TFTP |  |  | Indicates whether the phone is using an alternate TFTP server. |
| TFTP Server 1 |  |  | Primary Trivial File Transfer Protocol (TFTP) server that the phone uses. If you are not using DHCP in your network and you
                                                want to change this server, you must use the TFTP Server 1 option. If you set the Alternate TFTP option to On, you must enter a nonzero value for the TFTP Server 1 option. If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock
                                                the file before you can save changes to the TFTP Server 1 option. In this case, the phone deletes the file when you save changes
                                                to the TFTP Server 1 option. A new CTL or ITL file downloads from the new TFTP Server 1 address. When the phone looks for the TFTP server, the phone gives precedence to manually assigned TFTP servers, regardless of the
                                                protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for
                                                the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP
                                                server in this order: Any manually assigned IPv4 TFTP servers Any manually assigned IPv6 servers DHCP assigned TFTP servers DHCPv6 assigned TFTP servers Note For information about the CTL and ITL files, see the Cisco Unified Communications Manager Security Guide . | Note | For information about the CTL and ITL files, see the Cisco Unified Communications Manager Security Guide . |
| Note | For information about the CTL and ITL files, see the Cisco Unified Communications Manager Security Guide . |
| TFTP Server 2 |  |  | Optional backup TFTP server that the phone uses if the primary TFTP server is unavailable. If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock
                                                either of the files before you can save changes to the TFTP Server 2 option. In this case, the phone deletes either of the
                                                files when you save changes to the TFTP Server 2 option. A new CTL or ITL file downloads from the new TFTP Server 2 address. If you forget to unlock the CTL or ITL file, you can change the TFTP Server 2 address in either file, then erase them by pressing
                                                Erase from the Security Configuration menu. A new CTL or ITL file downloads from the new TFTP Server 2 address. When the phone looks for the TFTP server, it gives precedence to manually assigned TFTP servers, regardless of the protocol.
                                                If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP
                                                server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server
                                                in the following order: Any manually assigned IPv4 TFTP servers Any manually assigned IPv6 servers DHCP assigned TFTP servers DHCPv6 assigned TFTP servers Note For information about the CTL or ITL file, see Cisco Unified Communications Manager Security Guide. | Note | For information about the CTL or ITL file, see Cisco Unified Communications Manager Security Guide. |
| Note | For information about the CTL or ITL file, see Cisco Unified Communications Manager Security Guide. |
| DHCP Address Released |  |  | Releases the IP address that DHCP assigned. This field is editable if DHCP is enabled. If you wish to remove the phone from the VLAN and release the IP address for reassignment,
                                                set this option to Yes and press Apply. |

| Note | For information about the CTL and ITL files, see the Cisco Unified Communications Manager Security Guide . |
|---|---|

| Note | For information about the CTL or ITL file, see Cisco Unified Communications Manager Security Guide. |
|---|---|

| Entry | Type | Default value | Description |
|---|---|---|---|
| DHCPv6 Enabled |  | Yes | Indicates the method that the phone uses to get the IPv6-only address. When DHCPv6 is enabled, the phone gets the IPv6 address either from DHCPv6 server or from SLAAC by RA sent by the IPv6-enabled
                                             router. And if DHCPv6 is disabled, the phone will not have any stateful (from DHCPv6 server) or stateless (from SLAAC) IPv6
                                             address. |
| IPv6 Address |  | :: | Displays the current IPv6-only address of the phone or allows the user to enter a new IPv6 address. A valid IPv6 address is 128 bits in length, including the subnet prefix. Two address formats are supported: Eight sets of hexadecimal digits separated by colons X:X:X:X:X:X:X:X Compressed format to collapse a single run of consecutive zero groups into a single group represented by a double colon. If the IP address is assigned with this option, you must also assign the IPv6 prefix length and the default router. |
| IPv6 Prefix Length |  | 0 | Displays the current prefix length for the subnet or allows the user to enter a new prefix length. The subnet prefix length is a decimal value from 1 to 128. |
| IPv6 Default Router |  | :: | Displays the default router used by the phone or allows the user to enter a new IPv6-only default router. |
| IPv6 DNS Server 1 |  | :: | Displays the primary DNSv6 server used by the phone or allows the user to enter a new server. |
| IPv6 Alternate TFTP |  | No | Allows the user to enable the use of an alternate (secondary) IPv6 TFTP server. |
| IPv6 TFTP Server 1 |  | :: | Displays the primary IPv6 TFTP server used by the phone or allows the user to set a new primary TFTP server. |
| IPv6 TFTP Server 2 |  | :: | (Optional) Displays the secondary IPv6 TFTP server used if the primary IPv6 TFTP server is unavailable or allows the user
                                             to set a new secondary TFTP server. |
| IPv6 Address Released |  | No | Allows the user to release IPv6-related information. |

| Step 1 | If you are using Power over Ethernet, plug the LAN cable into the Network port. |
|---|---|
| Step 2 | If you are using the power cube, connect the cube to the phone and plug the cube into an electrical outlet. The buttons flash amber and then
                                          			 green in sequence during the various stages of bootup as the phone checks the
                                          			 hardware. If the phone completes these stages successfully, it has
                                          		started up properly. Note For Cisco IP Phone 8861, if you are using a power cube but there is no Power over Ethernet available, then the wifi will be
                                                      enabled. | Note | For Cisco IP Phone 8861, if you are using a power cube but there is no Power over Ethernet available, then the wifi will be
                                                      enabled. |
| Note | For Cisco IP Phone 8861, if you are using a power cube but there is no Power over Ethernet available, then the wifi will be
                                                      enabled. |

| Note | For Cisco IP Phone 8861, if you are using a power cube but there is no Power over Ethernet available, then the wifi will be
                                                      enabled. |
|---|---|

| Step 1 | In Cisco Unified
                                          				Communications Manager Administration , choose Device > Device
                                             				  Settings > Phone Services . |
|---|---|
| Step 2 | Verify that
                                       			 your users can access the Cisco Unified
                                          				Communications Self Care Portal , from which they can select and
                                       			 subscribe to configured services. See Self Care Portal Overview for a summary of the information that you must provide to end users. |

| Step 1 | Power off the old phone. |
|---|---|
| Step 2 | Power on the new phone. |
| Step 3 | On the new phone, select Replace an existing phone . |
| Step 4 | Enter the primary extension of the old phone. |
| Step 5 | If the old phone had a PIN assigned, enter the PIN. |
| Step 6 | Press Submit . |
| Step 7 | If there is more than one device for the user, select the device to replace and press Continue . |