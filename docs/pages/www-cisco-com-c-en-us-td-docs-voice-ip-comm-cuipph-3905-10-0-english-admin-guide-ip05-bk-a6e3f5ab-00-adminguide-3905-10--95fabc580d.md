---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--95fabc580d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_011.html
retrieved_at: 2026-08-21T14:35:00.510310+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Cisco Unified SIP Phone Installation

## Chapter: Cisco Unified SIP Phone Installation

# Cisco Unified SIP Phone Installation

## Verify Network Setup

Before you install a phone, you must decide how to configure the phone in your network. Then you can install the phone and
                              verify its functionality.

For the phone to successfully operate as an endpoint in your network, your network must meet specific requirements.

The phone displays the date and time from Cisco Unified
                                             				Communications Manager . 
                                          		The time displayed on the phone can differ from the Cisco Unified
                                             				Communications Manager time by up to 10 seconds.

Step 1

Configure a VoIP Network to meet  the
                                       		following requirements:

VoIP is configured on your Cisco routers and gateways.

Cisco Unified
                                                   				Communications Manager is installed in your network
                                                				  and is configured to handle call processing.

Step 2

Set up the network to support one of the following:

DHCP support

Manual assignment of IP address, gateway, and subnet mask

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

## Install Cisco
                        	 Unified SIP Phone

The
                              		  following steps provide an overview and checklist of installation tasks for the Cisco Unified SIP Phone 3905 . The list presents a suggested order
                              		  to guide you through the phone installation. Some tasks are optional, depending
                              		  on your system and user needs. For detailed procedures and information, refer
                              		  to the sources in the list.

Step 1

Choose the
                                       			 power source for the phone:

Power over
                                                					 Ethernet (PoE)

External
                                                					 power supply

Determines how
                                          				the phone receives power. For more information, see Phone Power Requirements .

Step 2

Connect the
                                       			 handset to the Handset port.

Step 3

(Optional)  Connect the power supply to the Cisco DC Adapter port. See Phone Addition Methods for guidelines.

Step 4

Connect a straight-through Ethernet cable from the switch to the network port labeled Network on the Cisco Unified SIP Phone 3905 . Each phone ships with one Ethernet cable in the box.

You can use either Category 3, 5, or 5e cabling for 10-Mbps connections, but you must use Category 5 or 5e for 100 Mbps connections.

Step 5

Connect a straight-through Ethernet cable from another network
                                       			 device, such as a desktop computer, to the access port labeled Computer. You
                                       			 can connect another network device later if you do not connect one now.

You can use
                                          				either Category 3, 5, or 5e cabling for 10-Mbps connections, but you must use
                                          				Category 5 or 5e for 100 Mbps connections.

Step 6

Monitor the
                                       			 phone startup process. This step associates directory numbers to the phone and
                                       			 verifies that phone is configured properly.

For more
                                          				information, see Verify Phone Startup .

Step 7

If you are
                                       			 configuring the network settings on the phone, you can set up an IP address for
                                       			 the phone by either using DHCP or manually entering an IP address.

Using
                                                					 DHCP: Verify that DHCP is enabled. You can set an alternate TFTP by entering
                                                					 the IP address for the TFTP.

Consult
                                                            						with the network administrator to determine whether you need to assign an
                                                            						alternative TFTP server instead of using the TFTP server assigned by DHCP.

Without
                                                					 DHCP: Verify that DHCP is disabled. You must then configure the IP address,
                                                					 subnet mask, TFTP server, and default router locally.

For more
                                          				information, see Configure Network Settings .

Step 8

Set up
                                       			 security on the phone. This step provides protection against data tampering
                                       			 threats and identity theft of phones.

For more
                                          				information, see Cisco Unified SIP Phone Security .

Step 9

Upgrade the
                                       			 phone to the current firmware image.

Step 10

Make calls
                                       			 with the phone. This step verifies that the phone and features work correctly.

For more
                                          				information, see the Cisco Unified SIP Phone 3905 User Guide for Cisco Unified
                                                				Communications Manager .

Step 11

Provide
                                       			 information to end users about how to use their phones and how to configure
                                       			 their phone options. This step ensures that users have adequate information to
                                       			 successfully use their phones.

For more
                                          				information, see Cisco IP Phone User Support .

## Set Up Phone from Setup Menus

The phone includes many configurable network settings that you may need to modify before the phone is functional for your
                              users. You can access these settings, and change some of them, through menus on the phone.

The phone includes the following setup
                              		menus:

Network Setup: Provides options for viewing and configuring a
                                    			 variety of network settings.

IPv4 Setup: This submenu provides additional network options.

Security Setup: Provides options for viewing and configuring a
                                    			 variety of security settings.

Before you can change option settings on the Network Setup
                              		menu, you must unlock options for editing.

You can control whether a phone has access to the Settings menu or
                                          			 to options on this menu by using the Settings Access field in the Cisco Unified
                                             				Communications Manager Administration Phone Configuration window. The Settings Access field accepts
                                          			 these values:

- Enabled: Allows
                                             				access to the Settings menu.

- Disabled:
                                             				Prevents access to the Settings menu.

- Restricted:
                                             				Allows access to the User Preferences menu and allows volume changes to be
                                             				saved. Prevents access to other options on the Settings menu.

If you cannot access an option on the Administrator Settings menu,
                                          			 check the Settings Access field.

You configure settings that are display-only on the phone in Cisco Unified
                                 				Communications Manager Administration .

To display a configuration menu, follow these steps:

Step 1

Press Applications .

Step 2

Select Admin Settings .

Step 3

Select Network or Security .

For information about the Reset Settings menu, see Maintenance .

Step 4

Enter your user ID and password, if required, then press Select .

Step 5

Perform one of these actions to display the desired menu:

- Use the
                                          				navigation arrows to select the desired menu and then press Select .

- Use the keypad
                                          				on the phone to enter the number that corresponds to the menu.

Step 6

To display a submenu, repeat step 5.

Step 7

To exit a menu, press Back .

### Apply a Phone Password

Step 1

In Cisco Unified Communications Manager Administration, navigate
                                          			 to the Common Phone Profile Configuration window ( Device > Device
                                                				  Settings > Common Phone Profile ).

Step 2

Enter a password in the Local Phone Unlock Password option.

Step 3

Apply the password to the common phone profile that the phone
                                          			 uses.

### Text and Menu Entry from Phone

When you edit the value of an option setting, follow these
                                 		  guidelines:

Use the arrows on the
                                       			 navigation pad to highlight the field that you wish to edit, then press Select in the navigation pad to activate that
                                       			 field. You can also double-tap on an editable field to activate it for editing.
                                       			 After the field is activated, you can enter values.

Use the keys on the keypad
                                       			to enter numbers and letters.

To enter letters by using
                                       			 the keypad, use a corresponding number key. Press the key one or more times to
                                       			 display a particular letter. For example, press the 2 key once for "a," twice quickly for "b," and three times quickly for "c." After you pause, the cursor automatically advances to allow
                                       			you to enter the next letter.

To delete a character to the left of the cursor, use the Hold/Resume button.

Press the arrow button to cancel or save your update.

To enter an IP address,
                                       		  	use the star (*) key to input:

the period (.) in IPv4 addresses

The Cisco IP Phone provides several methods to
                                             			 reset or restore option settings, if necessary.

## Configure Network Settings

If you are not using DHCP in your network, you must configure these network settings on the phone after installing the phone
                              on the network:

IP address

IP subnet information

Default Router

TFTP server IP address

The Network Setup menu provides options for viewing and making a variety of network settings. The following table describes
                              these options and, where applicable, explains how to change them.

Option

Description

To Change

IPv4

In the IPv4 Setup submenu, you can do the following:

- Enable or disable
                                             						the phone to use the IP address that is assigned by the DHCP server.

- Manually set the
                                             						IP Address, Subnet Mask, Default Routers, DNS Server, and Alternate TFTP
                                             						servers.

Scroll to IPv4 Setup and press Select.

MAC Address

Unique Media Access Control (MAC) address of the phone

Display only - Cannot configure.

Host Name

Unique host name that the DHCP server assigned to the phone.

Display only - Cannot configure.

Domain Name

Name of the Domain Name System (DNS) domain in which the phone
                                          					 resides.

See Set Domain Name Field .

Operational VLAN ID

Auxiliary Virtual Local Area Network (VLAN) configured on a
                                          					 Cisco Catalyst switch in which the phone is a member.

If the phone has not received an auxiliary VLAN, this option
                                          					 indicates the Administrative VLAN.

If neither the auxiliary VLAN nor the Administrative VLAN are
                                          					 configured, this option defaults to a VLAN ID of 4095.

Display only - Cannot configure.

The phone obtains its Operational VLAN ID via Cisco Discovery
                                          					 Protocol (CDP) from the switch to which the phone is attached. To assign a VLAN
                                          					 ID manually, use the Admin VLAN ID option.

Admin. VLAN ID

Auxiliary VLAN in which the phone is a member.

Used only if the phone does not receive an auxiliary VLAN from
                                          					 the switch; otherwise it is ignored.

See Set Admin VLAN ID Field .

PC VLAN

Allows the phone to interoperate with 3rd party switches that
                                          					 do not support a voice VLAN. The Admin VLAN ID option must be set before you
                                          					 can change this option.

See Set PC VLAN Field .

SW Port Setup

Speed and duplex of the network port. Valid values:

- Auto Negotiate

- 100 Half:
                                             						100-BaseT/half duplex

- 100 Full:
                                             						100-BaseT/full duplex

- 10 Half:
                                             						10-BaseT/half duplex

- 10 Full:
                                             						10-BaseT/full duplex

If the phone is connected to a switch, configure the port on
                                          					 the switch to the same speed/duplex as the phone, or configure both to
                                          					 auto-negotiate.

If you change the setting of this option, you must change the
                                          					 PC Port Configuration option to the same setting.

See Set SW Port Setup Field .

PC Port Setup

Speed and duplex of the access port. Valid values:

- Auto Negotiate

- 100 Half:
                                             						100-BaseT/half duplex

- 100 Full:
                                             						100-BaseT/full duplex

- 10 Half:
                                             						10-BaseT/half duplex

- 10 Full:
                                             						10-BaseT/full duplex

If the phone is connected to a switch, configure the port on
                                          					 the switch to the same speed/duplex as the phone, or configure both to
                                          					 auto-negotiate.

If you change the setting of this option, you must change the
                                          					 SW Port Configuration option to the same setting.

See Set PC Port Setup Field .

The IPv4 Setup menu is a submenu of the Network Setup menu.
                              		  To reach the IPv4 Setup menu, select the IPv4 option on the Network Setup menu.
                              		  
                              		The following table describes the IPv4 Setup menu options.

Option

Description

To Change

DHCP 
                                          				  Enabled

Indicates whether the phone has DHCP enabled or disabled.

When DHCP is enabled, the DHCP server assigns the phone an IP
                                          					 address. When DHCP is disabled, the administrator must manually assign an IP
                                          					 address to thephone.

See Set DHCP Enabled Field .

IP Address

Internet Protocol (IP) address of the phone.

If you assign an IP address with this option, you must also
                                          					 assign a subnet mask and default router. See the Subnet Mask and Default Router
                                          					 options in this table.

See Set IP Address Field .

Subnet Mask

Subnet mask used by the phone.

See Set Subnet Mask Field .

Default Router 1

Default router used by the phone (Default Router 1).

See Set Default Router Field .

DNS Server 1

Primary Domain Name System (DNS) server (DNS Server 1) used by the phone.

See Set DNS Server Field .

Alternate TFTP

Indicates whether the phone is using an alternative TFTP
                                          					 server.

See Set Alternate TFTP Field .

TFTP Server 1

Primary Trivial File Transfer Protocol (TFTP) server used by
                                          					 the phone. If you are not using DHCP in your network and you want to change
                                          					 this server, you must use the TFTP Server 1 option.

If you set the Alternate TFTP option to yes, you must enter a
                                          					 non-zero value for the TFTP Server 1 option.

See Set TFTP Server 1 Field .

TFTP Server 2

Optional backup TFTP server that the phone uses if the primary
                                          					 TFTP server is unavailable.

See Set TFTP Server 2 Field .

DHCP Address Released

Releases the IP address assigned by DHCP.

Scroll to the DHCP Address Released option and press Select,
                                          					 then select Yes to release the DHCP Address.

Step 1

On the phone, press Applications .

Step 2

Select Admin Settings and login if required.

Step 3

Select Network .

Step 4

To access the IPv4 setup fields, scroll to  IPv4 and press Select .

### Set Domain Name Field

Step 1

Set the DHCP Enabled option to No .

Step 2

Scroll to the Domain Name option, press Select , and enter a new domain name.

Step 3

Press Select .

### Set Admin VLAN ID Field

Step 1

Scroll to the Admin. VLAN ID option, press Select , and enter a new Admin VLAN
                                          			 setting.

Step 2

Press Select .

### Set PC VLAN Field

Step 1

Ensure that the Admin VLAN ID option is set.

Step 2

Scroll to the PC VLAN option, press Select , and then enter a new PC VLAN setting.

Step 3

Press Select .

### Set SW Port Setup Field

Step 1

Unlock network configuration options.

Step 2

Scroll to the SW Port Setup option and press Select .

Step 3

Scroll to the setting that you want and press Select .

### Set PC Port Setup Field

Step 1

Unlock network configuration options.

Step 2

Scroll to the PC Port Setup option and press Select .

Step 3

Scroll to the setting that you want and press Select .

### Set DHCP Enabled Field

Step 1

Scroll to the DHCP Enabled option.

Step 2

Press No to disable DHCP, or press Yes to enable DHCP.

### Set IP Address Field

Step 1

Set the DHCP Enabled option to No .

Step 2

Scroll to the IP Address option, press Select , and enter a new IP address.

Step 3

Press Select .

### Set Subnet Mask Field

Step 1

Set the DHCP Enabled option to No .

Step 2

Scroll to the Subnet Mask option, press Select , and enter a new subnet mask.

Step 3

Press Select .

### Set Default Router Field

Step 1

Set the DHCP Enabled option to No .

Step 2

Scroll to the appropriate Default Router option, press Select , and enter a new router IP
                                          			 address.

Step 3

Press Select .

### Set DNS Server Field

Step 1

Set the DHCP Enabled option to No .

Step 2

Scroll to the appropriate DNS Server option, press Select , and enter a new DNS server IP
                                          			 address.

Step 3

Press Select .

### Set Alternate TFTP Field

Step 1

Scroll to the Alternate TFTP option.

Step 2

Press Edit .

Step 3

Press Yes if the phone should use an alternative
                                          			 TFTP server.

Step 4

Press No if the phone should not use an alternative
                                          			 TFTP server.

### Set TFTP Server 1 Field

Step 1

If DHCP is enabled, set the Alternate TFTP option to Yes .

Step 2

Scroll to the TFTP Server 1 option, press Select , and enter a new TFTP server IP
                                          			 address.

Step 3

Press Select .

### Set TFTP Server 2 Field

Step 1

Unlock network configuration options.

Step 2

Enter an IP address for the TFTP Server 1 option.

Step 3

Scroll to the TFTP Server 2 option, press Select , and enter a new backup TFTP
                                          			 server IP address. If there is no secondary TFTP Server, you can use Delete to
                                          			 clear the field of a previous value.

Step 4

Press Select .

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

| Note | The phone displays the date and time from Cisco Unified
                                             				Communications Manager . 
                                          		The time displayed on the phone can differ from the Cisco Unified
                                             				Communications Manager time by up to 10 seconds. |
|---|---|

| Step 1 | Configure a VoIP Network to meet  the
                                       		following requirements: VoIP is configured on your Cisco routers and gateways. Cisco Unified
                                                   				Communications Manager is installed in your network
                                                				  and is configured to handle call processing. |
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

| Step 1 | Choose the
                                       			 power source for the phone: Power over
                                                					 Ethernet (PoE) External
                                                					 power supply Determines how
                                          				the phone receives power. For more information, see Phone Power Requirements . |
|---|---|
| Step 2 | Connect the
                                       			 handset to the Handset port. |
| Step 3 | (Optional)  Connect the power supply to the Cisco DC Adapter port. See Phone Addition Methods for guidelines. |
| Step 4 | Connect a straight-through Ethernet cable from the switch to the network port labeled Network on the Cisco Unified SIP Phone 3905 . Each phone ships with one Ethernet cable in the box. You can use either Category 3, 5, or 5e cabling for 10-Mbps connections, but you must use Category 5 or 5e for 100 Mbps connections. |
| Step 5 | Connect a straight-through Ethernet cable from another network
                                       			 device, such as a desktop computer, to the access port labeled Computer. You
                                       			 can connect another network device later if you do not connect one now. You can use
                                          				either Category 3, 5, or 5e cabling for 10-Mbps connections, but you must use
                                          				Category 5 or 5e for 100 Mbps connections. |
| Step 6 | Monitor the
                                       			 phone startup process. This step associates directory numbers to the phone and
                                       			 verifies that phone is configured properly. For more
                                          				information, see Verify Phone Startup . |
| Step 7 | If you are
                                       			 configuring the network settings on the phone, you can set up an IP address for
                                       			 the phone by either using DHCP or manually entering an IP address. Using
                                                					 DHCP: Verify that DHCP is enabled. You can set an alternate TFTP by entering
                                                					 the IP address for the TFTP. Note Consult
                                                            						with the network administrator to determine whether you need to assign an
                                                            						alternative TFTP server instead of using the TFTP server assigned by DHCP. Without
                                                					 DHCP: Verify that DHCP is disabled. You must then configure the IP address,
                                                					 subnet mask, TFTP server, and default router locally. For more
                                          				information, see Configure Network Settings . | Note | Consult
                                                            						with the network administrator to determine whether you need to assign an
                                                            						alternative TFTP server instead of using the TFTP server assigned by DHCP. |
| Note | Consult
                                                            						with the network administrator to determine whether you need to assign an
                                                            						alternative TFTP server instead of using the TFTP server assigned by DHCP. |
| Step 8 | Set up
                                       			 security on the phone. This step provides protection against data tampering
                                       			 threats and identity theft of phones. For more
                                          				information, see Cisco Unified SIP Phone Security . |
| Step 9 | Upgrade the
                                       			 phone to the current firmware image. |
| Step 10 | Make calls
                                       			 with the phone. This step verifies that the phone and features work correctly. For more
                                          				information, see the Cisco Unified SIP Phone 3905 User Guide for Cisco Unified
                                                				Communications Manager . |
| Step 11 | Provide
                                       			 information to end users about how to use their phones and how to configure
                                       			 their phone options. This step ensures that users have adequate information to
                                       			 successfully use their phones. For more
                                          				information, see Cisco IP Phone User Support . |

| Note | Consult
                                                            						with the network administrator to determine whether you need to assign an
                                                            						alternative TFTP server instead of using the TFTP server assigned by DHCP. |
|---|---|

| Note | You can control whether a phone has access to the Settings menu or
                                          			 to options on this menu by using the Settings Access field in the Cisco Unified
                                             				Communications Manager Administration Phone Configuration window. The Settings Access field accepts
                                          			 these values: Enabled: Allows
                                             				access to the Settings menu. Disabled:
                                             				Prevents access to the Settings menu. Restricted:
                                             				Allows access to the User Preferences menu and allows volume changes to be
                                             				saved. Prevents access to other options on the Settings menu. If you cannot access an option on the Administrator Settings menu,
                                          			 check the Settings Access field. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Admin Settings . |
| Step 3 | Select Network or Security . Note For information about the Reset Settings menu, see Maintenance . | Note | For information about the Reset Settings menu, see Maintenance . |
| Note | For information about the Reset Settings menu, see Maintenance . |
| Step 4 | Enter your user ID and password, if required, then press Select . |
| Step 5 | Perform one of these actions to display the desired menu: Use the
                                          				navigation arrows to select the desired menu and then press Select . Use the keypad
                                          				on the phone to enter the number that corresponds to the menu. |
| Step 6 | To display a submenu, repeat step 5. |
| Step 7 | To exit a menu, press Back . |

| Note | For information about the Reset Settings menu, see Maintenance . |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, navigate
                                          			 to the Common Phone Profile Configuration window ( Device > Device
                                                				  Settings > Common Phone Profile ). |
|---|---|
| Step 2 | Enter a password in the Local Phone Unlock Password option. |
| Step 3 | Apply the password to the common phone profile that the phone
                                          			 uses. |

| Note | The Cisco IP Phone provides several methods to
                                             			 reset or restore option settings, if necessary. |
|---|---|

| Option | Description | To Change |
|---|---|---|
| IPv4 | In the IPv4 Setup submenu, you can do the following: Enable or disable
                                             						the phone to use the IP address that is assigned by the DHCP server. Manually set the
                                             						IP Address, Subnet Mask, Default Routers, DNS Server, and Alternate TFTP
                                             						servers. | Scroll to IPv4 Setup and press Select. |
| MAC Address | Unique Media Access Control (MAC) address of the phone | Display only - Cannot configure. |
| Host Name | Unique host name that the DHCP server assigned to the phone. | Display only - Cannot configure. |
| Domain Name | Name of the Domain Name System (DNS) domain in which the phone
                                          					 resides. | See Set Domain Name Field . |
| Operational VLAN ID | Auxiliary Virtual Local Area Network (VLAN) configured on a
                                          					 Cisco Catalyst switch in which the phone is a member. If the phone has not received an auxiliary VLAN, this option
                                          					 indicates the Administrative VLAN. If neither the auxiliary VLAN nor the Administrative VLAN are
                                          					 configured, this option defaults to a VLAN ID of 4095. | Display only - Cannot configure. The phone obtains its Operational VLAN ID via Cisco Discovery
                                          					 Protocol (CDP) from the switch to which the phone is attached. To assign a VLAN
                                          					 ID manually, use the Admin VLAN ID option. |
| Admin. VLAN ID | Auxiliary VLAN in which the phone is a member. Used only if the phone does not receive an auxiliary VLAN from
                                          					 the switch; otherwise it is ignored. | See Set Admin VLAN ID Field . |
| PC VLAN | Allows the phone to interoperate with 3rd party switches that
                                          					 do not support a voice VLAN. The Admin VLAN ID option must be set before you
                                          					 can change this option. | See Set PC VLAN Field . |
| SW Port Setup | Speed and duplex of the network port. Valid values: Auto Negotiate 100 Half:
                                             						100-BaseT/half duplex 100 Full:
                                             						100-BaseT/full duplex 10 Half:
                                             						10-BaseT/half duplex 10 Full:
                                             						10-BaseT/full duplex If the phone is connected to a switch, configure the port on
                                          					 the switch to the same speed/duplex as the phone, or configure both to
                                          					 auto-negotiate. If you change the setting of this option, you must change the
                                          					 PC Port Configuration option to the same setting. | See Set SW Port Setup Field . |
| PC Port Setup | Speed and duplex of the access port. Valid values: Auto Negotiate 100 Half:
                                             						100-BaseT/half duplex 100 Full:
                                             						100-BaseT/full duplex 10 Half:
                                             						10-BaseT/half duplex 10 Full:
                                             						10-BaseT/full duplex If the phone is connected to a switch, configure the port on
                                          					 the switch to the same speed/duplex as the phone, or configure both to
                                          					 auto-negotiate. If you change the setting of this option, you must change the
                                          					 SW Port Configuration option to the same setting. | See Set PC Port Setup Field . |

| Option | Description | To Change |
|---|---|---|
| DHCP 
                                          				  Enabled | Indicates whether the phone has DHCP enabled or disabled. When DHCP is enabled, the DHCP server assigns the phone an IP
                                          					 address. When DHCP is disabled, the administrator must manually assign an IP
                                          					 address to thephone. | See Set DHCP Enabled Field . |
| IP Address | Internet Protocol (IP) address of the phone. If you assign an IP address with this option, you must also
                                          					 assign a subnet mask and default router. See the Subnet Mask and Default Router
                                          					 options in this table. | See Set IP Address Field . |
| Subnet Mask | Subnet mask used by the phone. | See Set Subnet Mask Field . |
| Default Router 1 | Default router used by the phone (Default Router 1). | See Set Default Router Field . |
| DNS Server 1 | Primary Domain Name System (DNS) server (DNS Server 1) used by the phone. | See Set DNS Server Field . |
| Alternate TFTP | Indicates whether the phone is using an alternative TFTP
                                          					 server. | See Set Alternate TFTP Field . |
| TFTP Server 1 | Primary Trivial File Transfer Protocol (TFTP) server used by
                                          					 the phone. If you are not using DHCP in your network and you want to change
                                          					 this server, you must use the TFTP Server 1 option. If you set the Alternate TFTP option to yes, you must enter a
                                          					 non-zero value for the TFTP Server 1 option. | See Set TFTP Server 1 Field . |
| TFTP Server 2 | Optional backup TFTP server that the phone uses if the primary
                                          					 TFTP server is unavailable. | See Set TFTP Server 2 Field . |
| DHCP Address Released | Releases the IP address assigned by DHCP. | Scroll to the DHCP Address Released option and press Select,
                                          					 then select Yes to release the DHCP Address. |

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Select Admin Settings and login if required. |
| Step 3 | Select Network . |
| Step 4 | To access the IPv4 setup fields, scroll to  IPv4 and press Select . |

| Step 1 | Set the DHCP Enabled option to No . |
|---|---|
| Step 2 | Scroll to the Domain Name option, press Select , and enter a new domain name. |
| Step 3 | Press Select . |

| Step 1 | Scroll to the Admin. VLAN ID option, press Select , and enter a new Admin VLAN
                                          			 setting. |
|---|---|
| Step 2 | Press Select . |

| Step 1 | Ensure that the Admin VLAN ID option is set. |
|---|---|
| Step 2 | Scroll to the PC VLAN option, press Select , and then enter a new PC VLAN setting. |
| Step 3 | Press Select . |

| Step 1 | Unlock network configuration options. |
|---|---|
| Step 2 | Scroll to the SW Port Setup option and press Select . |
| Step 3 | Scroll to the setting that you want and press Select . |

| Step 1 | Unlock network configuration options. |
|---|---|
| Step 2 | Scroll to the PC Port Setup option and press Select . |
| Step 3 | Scroll to the setting that you want and press Select . |

| Step 1 | Scroll to the DHCP Enabled option. |
|---|---|
| Step 2 | Press No to disable DHCP, or press Yes to enable DHCP. |

| Step 1 | Set the DHCP Enabled option to No . |
|---|---|
| Step 2 | Scroll to the IP Address option, press Select , and enter a new IP address. |
| Step 3 | Press Select . |

| Step 1 | Set the DHCP Enabled option to No . |
|---|---|
| Step 2 | Scroll to the Subnet Mask option, press Select , and enter a new subnet mask. |
| Step 3 | Press Select . |

| Step 1 | Set the DHCP Enabled option to No . |
|---|---|
| Step 2 | Scroll to the appropriate Default Router option, press Select , and enter a new router IP
                                          			 address. |
| Step 3 | Press Select . |

| Step 1 | Set the DHCP Enabled option to No . |
|---|---|
| Step 2 | Scroll to the appropriate DNS Server option, press Select , and enter a new DNS server IP
                                          			 address. |
| Step 3 | Press Select . |

| Step 1 | Scroll to the Alternate TFTP option. |
|---|---|
| Step 2 | Press Edit . |
| Step 3 | Press Yes if the phone should use an alternative
                                          			 TFTP server. |
| Step 4 | Press No if the phone should not use an alternative
                                          			 TFTP server. |

| Step 1 | If DHCP is enabled, set the Alternate TFTP option to Yes . |
|---|---|
| Step 2 | Scroll to the TFTP Server 1 option, press Select , and enter a new TFTP server IP
                                          			 address. |
| Step 3 | Press Select . |

| Step 1 | Unlock network configuration options. |
|---|---|
| Step 2 | Enter an IP address for the TFTP Server 1 option. |
| Step 3 | Scroll to the TFTP Server 2 option, press Select , and enter a new backup TFTP
                                          			 server IP address. If there is no secondary TFTP Server, you can use Delete to
                                          			 clear the field of a previous value. |
| Step 4 | Press Select . |

| Step 1 | If you are using Power over Ethernet, plug the LAN cable into the Network port. |
|---|---|
| Step 2 | If you are using the power cube, connect the cube to the phone and plug the cube into an electrical outlet. The buttons flash amber and then
                                          			 green in sequence during the various stages of bootup as the phone checks the
                                          			 hardware. If the phone completes these stages successfully, it has
                                          		started up properly. |