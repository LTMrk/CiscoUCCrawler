---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-77e0221a13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_0100.html
retrieved_at: 2026-08-21T13:38:01.844292+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Cisco Unified IP
	 Conference Phone Settings

## Chapter: Cisco Unified IP
	 Conference Phone Settings

# Cisco Unified IP
                     	 Conference Phone Settings

## Cisco Unified IP Conference Phone Configuration Menus

The conference phone
                           		includes the following configuration menus:

Network Setup:
                                 			 Provides options for viewing and for configuring network settings.

IPv4
                                 			 Configuration: A submenu of the Network Setup menu, the IPv4 menu items provide
                                 			 additional network options field that can be viewed or set.

Before you can
                           		change or edit option settings on the Network Setup menu, you must unlock the
                           		options.

You can control
                           		whether a conference phone user has access to conference phone settings by
                           		using the Settings Access field on the Phone Configuration page in Cisco Unified
                              				Communications Manager Administration . For more information, see the Cisco Unified
                                 				Communications Manager Administration Guide .

### Display the Configuration Menu

You can control whether a conference phone has access to the Settings menu, or to options on this menu, by using the Settings
                                             Access field in the Cisco Unified Communications Manager Administration Phone Configuration page. The Settings Access field
                                             accepts these values:

Enabled: Allow access to the Settings menu.

Disabled: Prevent access to the Settings menu.

Restricted: Allow access to the User Preferences menu, but prevent access to other options on the Settings menu.

If you cannot access an option on the Administrator Settings menu, check the Settings Access field. For more information,
                                             see the Cisco Unified Communications Manager Administration Guide .

To display a configuration menu, perform these steps:

Press Apps .

Select Admin Settings .

For information about the Status menu, see Model Information, Status, and Statistics .
                                                         				  For information about the Reset Settings menu, see Troubleshooting and Maintenance .

Enter the password and then press Enter . The Admin Settings password is
                                          			 configured in the Local Phone Unlock Password parameter in the Common Phone
                                          			 Profile Configuration on Cisco Unified Communications Manager Administration.

Users can access the Admin Settings without entering a password
                                                         				  when the Local Phone Unlock Password parameter is not configured

Perform one of these actions to display the desired menu:

- Use the
                                             				navigation bar to select the desired menu and then press Select.

- Use the keypad
                                             				on the phone to enter the number that corresponds to the menu.

To display a submenu, repeat Step 4.

To exit a menu, press Exit .

### Password
                           	 Protection

You can apply a
                              		password to the phone so that no changes can be made to the administrative
                              		options on the conference phone unless the password is entered on the Admin
                              		Settings phone screen.

#### Apply
                              	 Password

To apply
                                    		  a password to the conference phone, perform these steps:

In Cisco
                                             			 Unified Communications Manager Administration, navigate to the Common Phone
                                             			 Profile Configuration window using Device > Device
                                                   				  Settings > Common Phone Profile .

In the Local
                                             			 Phone Unlock Password option, enter a password.

Apply the
                                             			 password to the common phone profile used by the phone.

### Value Input and
                           	 Editing Guidelines

When you edit the
                              		value of an option setting, follow these guidelines:

- Use the keys on the keypad
                                 		  to enter numbers and letters.

- To enter letters by using
                                 		  the keypad, use the corresponding number key. Press the key one or more times
                                 		  to display a particular letter. For example, press 2 once for "a" , twice
                                 		  quickly for "b" , and three
                                 		  times quickly for "c" . After you
                                 		  pause, the cursor automatically advances to allow you to enter the next letter.

- To enter a period (for
                                 		  example, in an IP address), press * on the keypad.

To enter a plus
                                    			 (+), for international dialling, press and hold the * key for at least 1 second.

- Press the up arrow on the
                                 		  navigation bar to move the cursor to the left most character, and press the
                                 		  down arrow on the navigation bar to move the cursor to the right most
                                 		  character.

- Press if you make a mistake. This softkey
                                 		  deletes the character to the left of the cursor.

- Press Cancel before pressing Save to discard any changes that you have made.

The Cisco Unified
                                          		  IP Conference Phone provides several methods you can use to reset or restore
                                          		  option settings, if necessary. For more information, see Reset or Restore.

## User Interface Menus

## Network Setup
                        	 Menu

The Network Setup
                           		menu provides options for viewing and configuring a variety of network
                           		settings. The following table describes these options and, where applicable,
                           		explains how to change them.

For
                           		information about how to access the Network Setup menu, see Display
                           		Configuration menu.

Option

Description

To Change

IPv4 Setup

In the IPv4
                                       				Setup submenu, you can do the following:

- Enable or disable the
                                          				  phone to use the IP address that is assign by the DHCP server.

- Manually set the IP
                                          				  Address, Subnet Mask, Default Routers, DNS Server, and Alternate TFTP servers.

For more
                                       				information on the IPv4 address fields, see IPv4 Setup Menu Items.

Scroll to
                                       				IPv4 Setup and press Select .

Host Name

Unique host
                                       				name that the DHCP server assigned to the phone.

Display
                                       				only—Cannot configure.

Domain Name

Name of the
                                       				Domain Name System (DNS) domain in which the phone resides.

See Set Domain Name .

Operational
                                       				VLAN ID

Auxiliary
                                       				Virtual Local Area Network (VLAN) configured on a Cisco Catalyst switch in
                                       				which the phone is a member.

If the phone
                                       				has not received an auxiliary VLAN, this option indicates the Administrative
                                       				VLAN.

If neither
                                       				the auxiliary VLAN nor the Administrative VLAN are configured, this option
                                       				defaults to a VLAN ID of 4095.

Display
                                       				only—Cannot configure.

The phone
                                       				obtains its Operational VLAN ID via Cisco Discovery Protocol (CDP) from the
                                       				switch to which the phone is attached. To assign a VLAN ID manually, use the
                                       				Admin VLAN ID option.

Admin. VLAN
                                       				ID

Auxiliary
                                       				VLAN in which the phone is a member.

Used only if
                                       				the phone does not receive an auxiliary VLAN from the switch; otherwise it is
                                       				ignored.

See Set Admin VLAN ID .

Network (SW)
                                       				Port Setup

Speed and
                                       				duplex of the network port. Valid values:

- Auto Negotiate

- 100 Half: 100-BaseT/half
                                          				  duplex

- 100 Full: 100-BaseT/full
                                          				  duplex

- 10 Half: 10-BaseT/half
                                          				  duplex

- 10 Full: 10-BaseT/full
                                          				  duplex

If the phone
                                       				is connected to a switch, configure the port on the switch to the same
                                       				speed/duplex as the phone, or configure both to auto-negotiate.

### Set Domain Name

Set the DHCP Enabled option to No .

Choose Apps > Admin Settings > Network Configuration > Domain Name .

Enter a new domain name.

Press Validate , and then press Save .

### Set Admin VLAN ID

Choose Apps > Admin Settings > Network Configuration > Admin VLAN ID .

Enter your password at the prompt.

Enter a new Admin VLAN ID.

Press Apply , and then Save .

## IPv4 Setup Menu
                        	 Options

The IPv4
                              		  Setup menu is a submenu of the Network Setup menu. To reach the IPv4 Setup
                              		  menu, select the IPv4 option on the Network Setup menu.

The
                              		  following table describes the IPv4 Setup menu options.

For
                              		  information about the keys you can use to edit options, see Value Input and Editing Guidelines .

Option

Description

To Change

DHCP

Indicates
                                          					 whether the conference phone has DHCP enabled or disabled.

When DHCP
                                          					 is enabled, the DHCP server assigns the conference phone an IP address. When
                                          					 DHCP is disabled, the administrator must manually assign an IP address to
                                          					 the phone.

For more
                                          					 information, see DHCP Usage .

Set DHCP

IP Address

Internet
                                          					 Protocol (IP) address of the conference phone.

If you
                                          					 assign an IP address with this option, you must also assign a subnet mask and
                                          					 default router. See the Subnet Mask and Default Router options in this table.

Set IP Address

Subnet
                                          					 Mask

Subnet
                                          					 mask used by the phone.

Set Subnet Mask

Default
                                          					 Router 1

Default
                                          					 router used by the phone (Default Router 1).

Set Default Router

DNS Server
                                          					 1

Primary
                                          					 Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers
                                          					 (DNS Server 2–5) used by the phone.

Set DNS Server

Alternate
                                          					 TFTP

Indicates
                                          					 whether the phone is using an alternative TFTP server.

Set Alternate TFTP

TFTP
                                          					 Server 1

Primary
                                          					 Trivial File Transfer Protocol (TFTP) server used by the phone. If you are not
                                          					 using DHCP in your network and you want to change this server, you must use the
                                          					 TFTP Server 1 option.

If you set
                                          					 the Alternate TFTP option to yes, you must enter a nonzero value for the TFTP
                                          					 Server 1 option.

Set TFTP Server 1

TFTP
                                          					 Server 2

Optional
                                          					 backup TFTP server that the phone uses if the primary TFTP server is
                                          					 unavailable.

Set TFTP Server 2

DHCP
                                          					 Address Released

Releases
                                          					 the IP address assigned by DHCP.

### Set DHCP

Unlock network configuration options.

Choose Apps > Admin Settings > Network Configuration > DHCP Enabled .

Set Enable to Yes.  To disable DHCP, set Enable to No.

Press Select , and then press Save .

### Set IP
                           	 Address

Set the DHCP
                                          			 Enabled option to No .

Choose Apps > Admin
                                                				  Settings > Network Configuration > IP
                                                				  Address .

Enter a new IP
                                          			 Address.

Press Validate , and then press Save .

### Set Subnet
                           	 Mask

Set the DHCP
                                          			 Enabled option to No .

Choose Apps > Admin
                                                				  Settings > Network Configuration > IP Subnet
                                                				  Mask .

Enter a new IP
                                          			 address for the subnet mask.

Press Validate , and then press Save .

### Set Default
                           	 Router

Unlock network
                                          			 configuration options.

Set the DHCP
                                          			 Enable option to No .

Choose Apps > Admin
                                                				  Settings > Network Configuration > Default
                                                				  Router1 .

Enter a new
                                          			 router IP address.

Press Apply , and then press Save .

### Set DNS
                           	 Server

Unlock network
                                          			 configuration options.

Set the DHCP
                                          			 Enable option to No.

Choose Apps > Admin
                                                				  Settings > Network Configuration > DNS
                                                				  Server1 .

Enter a new
                                          			 DNS server address.

Press Apply and then Save .

Repeat as
                                          			 needed to assign backup DNS servers

### Set Alternate TFTP

Choose Apps > Admin Settings > Network Configuration > Alternate TFTP .

Press Yes if the conference station should use an alternate TFTP server, or No if the conference station should not use an alternate TFTP server.

Press Select , and then press Save .

### Set TFTP Server 1

If DHCP is enabled, set the Alternate TFTP option to Yes .

Choose Apps > Admin Settings > Network Configuration > TFTP Server 1 .

Press Edit .

Enter a new TFTP server IP address.

Press Apply , and then press Save .

### Set TFTP Server 2

Choose Apps > Admin Settings > Network Configuration > TFTP Server 1 .

Press Edit and enter an IP address for the TFTP Server 1 option.

Press Apply , and then press Save .

Choose Apps > Admin Settings > Network Configuration > TFTP Server 2 .

Choose the TFTP Server 2 option, and then press Edit .

Enter a new backup TFTP server IP address.

Press Apply , and then press Save .

### DHCP Usage

Dynamic Host
                              		Configuration Protocol (DHCP) automatically assigns IP addresses to devices
                              		when you connect them to the network. Conference stations enable DHCP by
                              		default.

If you are
                              		configuring the Ethernet network settings on the phone for an IP network, you
                              		can set up an IP address for the phone by either using DHCP to assign it for
                              		you or by manually entering an IP address.

You must also
                                          		  enter the domain name for the phone in the Ethernet Setup page.

#### Set Up IP Phone to
                              	 Use DHCP

To
                                    		  enable DHCP and allow the DHCP server to automatically assign an IP address to
                                    		  the Cisco Unified IP Phone and direct the phone to a TFTP server, perform these
                                    		  steps:

Press Apps and choose Admin
                                                   				  Settings > Network Setup > Ethernet
                                                   				  Setup > IPv4 Setup .

To enable
                                             			 DHCP, set DHCP Enabled to Yes. DHCP is enabled by default.

To use an
                                             			 alternate TFTP server, set Alternate TFTP Server to Yes, and enter the IP
                                             			 address for the TFTP Server.

Consult with
                                                            				  the network administrator to determine whether you need to assign an
                                                            				  alternative TFTP server instead of using the TFTP server that DHCP assigns.

Press Apply , and then press Save .

#### Set Up IP Phone to
                              	 Not Use DHCP

When not
                                    		  using DHCP, you must configure the IP address, subnet mask, TFTP server, and
                                    		  default router locally on the conference station.

Press Apps and choose Admin
                                                   				  Settings > Network Setup > Ethernet
                                                   				  Setup > IPv4 Setup .

To disable
                                             			 DHCP and manually set an IP address:

Set DHCP
                                                   				  Enabled to No.

Enter the
                                                   				  static IP address for the conference station.

Enter the
                                                   				  subnet mask.

Enter the
                                                   				  default router IP addresses.

Set
                                                   				  Alternate TFTP Server to Yes, and enter the IP address for TFTP Server 1.

Press Apply , and then press Save .

## Security Setup
                        	 Menu

The
                              		  Security Setup menu provides information about various security settings. It
                              		  provides access to the Trust List File screen and the 802.1x authentication.

Access the
                              		  Security Configuration menu from Apps > Admin
                                    				Settings > Security Setup

The
                              		  following table describes the options in this menu.

Option

Description

To Change

Security
                                          					 Mode

Displays
                                          					 the security mode that is set for the phone.

From Cisco
                                          					 Unified Communications Manager Administration, choose Device > Phone > Phone
                                                						  Configuration .

LSC

Indicates
                                          					 if a locally significant certificate (used for the security features) is
                                          					 installed on the phone (Installed) or is not installed on the phone (Not
                                          					 Installed).

For
                                          					 information about how to manage the LSC for your phone, see "Using
                                             						the Certificate Authority Proxy Function" chapter in Cisco
                                             						Unified Communications Manager Security Guide .

Trust List

The Trust
                                          					 List provides submenus for CTL signature and Call Manager/TFTP Server.

For more
                                          					 information, see the Trust List Menu .

802.1X
                                          					 Authentication

Displays
                                          					 the device authentication, EAP/MD5, and transaction status.

See 802.1X Authentication and Status Menus .

### Trust List
                           	 Menu

The Trust List
                                 		  menu displays information about all the servers that the conference phone
                                 		  trusts, and includes the options described in the following table.

The Trust List is
                                 		  accessed via the Apps > Admin
                                       				Settings > Security Setup > Trust
                                       				List

To exit the Trust
                                 		  List Menu, press Back .

Option

Description

To Change

CTL
                                             					 Signature

Displays
                                             					 the MD5 hash of the CTL file.

For more
                                             					 information about this file, see "Configuring the Cisco CTL Client" chapter in Cisco
                                                						Unified Communications Manager Security Guide .

ITL File

Displays a
                                             					 submenu of options. Select an option to view its ITL setting information:

ITL
                                                   						  Signature: MD5 hash of the ITL file.

Unified CM/TFTP Server

CAPF
                                                   						  Server

TVS

For more
                                             					 information about this file, see "Configuring the Cisco ITL Client" chapter in the Cisco
                                                						Unified Communications Manager Security Guide .

Call
                                             					 Manager/TFTP Server

Displays
                                             					 the call manager/TFTP certificate information.

### 802.1X
                           	 Authentication and Status Menus

The
                                 		  802.1X Authentication and 802.1X Authentication Status menus allow you to
                                 		  enable 802.1X authentication and view transaction status. These options are
                                 		  described in the following tables.

To exit
                                 		  these menus, press Exit.

Option

Description

To
                                             					 Change

Device
                                             					 Authentication

Determines whether 802.1X authentication is enabled:

- Enabled: Phone uses
                                                						802.1X authentication to request network access.

- Disabled: Default setting
                                                						in which the phone uses CDP to acquire VLAN and network access.

Set 802.1X Device Authentication

802.1X
                                             					 Authentication Status

Real-time
                                             					 progress of the 802.1X authentication status, displaying one of the following
                                             					 states:

Disabled: 802.1X is disabled and the transaction was not
                                                   						  attempted

Disconnected: Physical link is down or disconnected

Connecting: Trying to discover or acquire the authenticator

Acquired: Authenticator acquired, awaiting authentication to
                                                   						  begin

Authenticating: Authentication in progress

Authenticated: Authentication successful or implicit
                                                   						  authentication due to timeouts

Held: Authentication failed, waiting before next attempt
                                                   						  (approximately 60 seconds)

Display
                                             					 only—Cannot configure.

To view
                                             					 the transaction status of your 802.1X Authentication, choose Applications > Admin
                                                   						  Settings > Security Configuration > 802.1X Authentication
                                                   						  Status .

#### Set 802.1X Device Authentication

Choose Apps > Admin Settings > Security Config > 802.1X Authentication > Device Authentication .

Press Edit .

Set the Device Authentication option to Enabled or Disabled .

The default value is Disabled.

Press Save .

| Note | You can control whether a conference phone has access to the Settings menu, or to options on this menu, by using the Settings
                                             Access field in the Cisco Unified Communications Manager Administration Phone Configuration page. The Settings Access field
                                             accepts these values: Enabled: Allow access to the Settings menu. Disabled: Prevent access to the Settings menu. Restricted: Allow access to the User Preferences menu, but prevent access to other options on the Settings menu. If you cannot access an option on the Administrator Settings menu, check the Settings Access field. For more information,
                                             see the Cisco Unified Communications Manager Administration Guide . |
|---|---|

| Step 1 | Press Apps . |
|---|---|
| Step 2 | Select Admin Settings . Note For information about the Status menu, see Model Information, Status, and Statistics .
                                                         				  For information about the Reset Settings menu, see Troubleshooting and Maintenance . | Note | For information about the Status menu, see Model Information, Status, and Statistics .
                                                         				  For information about the Reset Settings menu, see Troubleshooting and Maintenance . |
| Note | For information about the Status menu, see Model Information, Status, and Statistics .
                                                         				  For information about the Reset Settings menu, see Troubleshooting and Maintenance . |
| Step 3 | Enter the password and then press Enter . The Admin Settings password is
                                          			 configured in the Local Phone Unlock Password parameter in the Common Phone
                                          			 Profile Configuration on Cisco Unified Communications Manager Administration. Note Users can access the Admin Settings without entering a password
                                                         				  when the Local Phone Unlock Password parameter is not configured | Note | Users can access the Admin Settings without entering a password
                                                         				  when the Local Phone Unlock Password parameter is not configured |
| Note | Users can access the Admin Settings without entering a password
                                                         				  when the Local Phone Unlock Password parameter is not configured |
| Step 4 | Perform one of these actions to display the desired menu: Use the
                                             				navigation bar to select the desired menu and then press Select. Use the keypad
                                             				on the phone to enter the number that corresponds to the menu. |
| Step 5 | To display a submenu, repeat Step 4. |
| Step 6 | To exit a menu, press Exit . |

| Note | For information about the Status menu, see Model Information, Status, and Statistics .
                                                         				  For information about the Reset Settings menu, see Troubleshooting and Maintenance . |
|---|---|

| Note | Users can access the Admin Settings without entering a password
                                                         				  when the Local Phone Unlock Password parameter is not configured |
|---|---|

| Step 1 | In Cisco
                                             			 Unified Communications Manager Administration, navigate to the Common Phone
                                             			 Profile Configuration window using Device > Device
                                                   				  Settings > Common Phone Profile . |
|---|---|
| Step 2 | In the Local
                                             			 Phone Unlock Password option, enter a password. |
| Step 3 | Apply the
                                             			 password to the common phone profile used by the phone. |

| Note | The Cisco Unified
                                          		  IP Conference Phone provides several methods you can use to reset or restore
                                          		  option settings, if necessary. For more information, see Reset or Restore. |
|---|---|

| Option | Description | To Change |
|---|---|---|
| IPv4 Setup | In the IPv4
                                       				Setup submenu, you can do the following: Enable or disable the
                                          				  phone to use the IP address that is assign by the DHCP server. Manually set the IP
                                          				  Address, Subnet Mask, Default Routers, DNS Server, and Alternate TFTP servers. For more
                                       				information on the IPv4 address fields, see IPv4 Setup Menu Items. | Scroll to
                                       				IPv4 Setup and press Select . |
| Host Name | Unique host
                                       				name that the DHCP server assigned to the phone. | Display
                                       				only—Cannot configure. |
| Domain Name | Name of the
                                       				Domain Name System (DNS) domain in which the phone resides. | See Set Domain Name . |
| Operational
                                       				VLAN ID | Auxiliary
                                       				Virtual Local Area Network (VLAN) configured on a Cisco Catalyst switch in
                                       				which the phone is a member. If the phone
                                       				has not received an auxiliary VLAN, this option indicates the Administrative
                                       				VLAN. If neither
                                       				the auxiliary VLAN nor the Administrative VLAN are configured, this option
                                       				defaults to a VLAN ID of 4095. | Display
                                       				only—Cannot configure. The phone
                                       				obtains its Operational VLAN ID via Cisco Discovery Protocol (CDP) from the
                                       				switch to which the phone is attached. To assign a VLAN ID manually, use the
                                       				Admin VLAN ID option. |
| Admin. VLAN
                                       				ID | Auxiliary
                                       				VLAN in which the phone is a member. Used only if
                                       				the phone does not receive an auxiliary VLAN from the switch; otherwise it is
                                       				ignored. | See Set Admin VLAN ID . |
| Network (SW)
                                       				Port Setup | Speed and
                                       				duplex of the network port. Valid values: Auto Negotiate 100 Half: 100-BaseT/half
                                          				  duplex 100 Full: 100-BaseT/full
                                          				  duplex 10 Half: 10-BaseT/half
                                          				  duplex 10 Full: 10-BaseT/full
                                          				  duplex If the phone
                                       				is connected to a switch, configure the port on the switch to the same
                                       				speed/duplex as the phone, or configure both to auto-negotiate. |  |

| Step 1 | Set the DHCP Enabled option to No . |
|---|---|
| Step 2 | Choose Apps > Admin Settings > Network Configuration > Domain Name . |
| Step 3 | Enter a new domain name. |
| Step 4 | Press Validate , and then press Save . |

| Step 1 | Choose Apps > Admin Settings > Network Configuration > Admin VLAN ID . Enter your password at the prompt. |
|---|---|
| Step 2 | Enter a new Admin VLAN ID. |
| Step 3 | Press Apply , and then Save . |

| Option | Description | To Change |
|---|---|---|
| DHCP | Indicates
                                          					 whether the conference phone has DHCP enabled or disabled. When DHCP
                                          					 is enabled, the DHCP server assigns the conference phone an IP address. When
                                          					 DHCP is disabled, the administrator must manually assign an IP address to
                                          					 the phone. For more
                                          					 information, see DHCP Usage . | Set DHCP |
| IP Address | Internet
                                          					 Protocol (IP) address of the conference phone. If you
                                          					 assign an IP address with this option, you must also assign a subnet mask and
                                          					 default router. See the Subnet Mask and Default Router options in this table. | Set IP Address |
| Subnet
                                          					 Mask | Subnet
                                          					 mask used by the phone. | Set Subnet Mask |
| Default
                                          					 Router 1 | Default
                                          					 router used by the phone (Default Router 1). | Set Default Router |
| DNS Server
                                          					 1 | Primary
                                          					 Domain Name System (DNS) server (DNS Server 1) and optional backup DNS servers
                                          					 (DNS Server 2–5) used by the phone. | Set DNS Server |
| Alternate
                                          					 TFTP | Indicates
                                          					 whether the phone is using an alternative TFTP server. | Set Alternate TFTP |
| TFTP
                                          					 Server 1 | Primary
                                          					 Trivial File Transfer Protocol (TFTP) server used by the phone. If you are not
                                          					 using DHCP in your network and you want to change this server, you must use the
                                          					 TFTP Server 1 option. If you set
                                          					 the Alternate TFTP option to yes, you must enter a nonzero value for the TFTP
                                          					 Server 1 option. | Set TFTP Server 1 |
| TFTP
                                          					 Server 2 | Optional
                                          					 backup TFTP server that the phone uses if the primary TFTP server is
                                          					 unavailable. | Set TFTP Server 2 |
| DHCP
                                          					 Address Released | Releases
                                          					 the IP address assigned by DHCP. |  |

| Step 1 | Unlock network configuration options. |
|---|---|
| Step 2 | Choose Apps > Admin Settings > Network Configuration > DHCP Enabled . |
| Step 3 | Set Enable to Yes.  To disable DHCP, set Enable to No. |
| Step 4 | Press Select , and then press Save . |

| Step 1 | Set the DHCP
                                          			 Enabled option to No . |
|---|---|
| Step 2 | Choose Apps > Admin
                                                				  Settings > Network Configuration > IP
                                                				  Address . |
| Step 3 | Enter a new IP
                                          			 Address. |
| Step 4 | Press Validate , and then press Save . |

| Step 1 | Set the DHCP
                                          			 Enabled option to No . |
|---|---|
| Step 2 | Choose Apps > Admin
                                                				  Settings > Network Configuration > IP Subnet
                                                				  Mask . |
| Step 3 | Enter a new IP
                                          			 address for the subnet mask. |
| Step 4 | Press Validate , and then press Save . |

| Step 1 | Unlock network
                                          			 configuration options. |
|---|---|
| Step 2 | Set the DHCP
                                          			 Enable option to No . |
| Step 3 | Choose Apps > Admin
                                                				  Settings > Network Configuration > Default
                                                				  Router1 . |
| Step 4 | Enter a new
                                          			 router IP address. |
| Step 5 | Press Apply , and then press Save . |

| Step 1 | Unlock network
                                          			 configuration options. |
|---|---|
| Step 2 | Set the DHCP
                                          			 Enable option to No. |
| Step 3 | Choose Apps > Admin
                                                				  Settings > Network Configuration > DNS
                                                				  Server1 . |
| Step 4 | Enter a new
                                          			 DNS server address. |
| Step 5 | Press Apply and then Save . |
| Step 6 | Repeat as
                                          			 needed to assign backup DNS servers |

| Step 1 | Choose Apps > Admin Settings > Network Configuration > Alternate TFTP . |
|---|---|
| Step 2 | Press Yes if the conference station should use an alternate TFTP server, or No if the conference station should not use an alternate TFTP server. |
| Step 3 | Press Select , and then press Save . |

| Step 1 | If DHCP is enabled, set the Alternate TFTP option to Yes . |
|---|---|
| Step 2 | Choose Apps > Admin Settings > Network Configuration > TFTP Server 1 . |
| Step 3 | Press Edit . |
| Step 4 | Enter a new TFTP server IP address. |
| Step 5 | Press Apply , and then press Save . |

| Step 1 | Choose Apps > Admin Settings > Network Configuration > TFTP Server 1 . |
|---|---|
| Step 2 | Press Edit and enter an IP address for the TFTP Server 1 option. |
| Step 3 | Press Apply , and then press Save . |
| Step 4 | Choose Apps > Admin Settings > Network Configuration > TFTP Server 2 . |
| Step 5 | Choose the TFTP Server 2 option, and then press Edit . |
| Step 6 | Enter a new backup TFTP server IP address. |
| Step 7 | Press Apply , and then press Save . |

| Note | You must also
                                          		  enter the domain name for the phone in the Ethernet Setup page. |
|---|---|

| Step 1 | Press Apps and choose Admin
                                                   				  Settings > Network Setup > Ethernet
                                                   				  Setup > IPv4 Setup . |
|---|---|
| Step 2 | To enable
                                             			 DHCP, set DHCP Enabled to Yes. DHCP is enabled by default. |
| Step 3 | To use an
                                             			 alternate TFTP server, set Alternate TFTP Server to Yes, and enter the IP
                                             			 address for the TFTP Server. Note Consult with
                                                            				  the network administrator to determine whether you need to assign an
                                                            				  alternative TFTP server instead of using the TFTP server that DHCP assigns. | Note | Consult with
                                                            				  the network administrator to determine whether you need to assign an
                                                            				  alternative TFTP server instead of using the TFTP server that DHCP assigns. |
| Note | Consult with
                                                            				  the network administrator to determine whether you need to assign an
                                                            				  alternative TFTP server instead of using the TFTP server that DHCP assigns. |
| Step 4 | Press Apply , and then press Save . |

| Note | Consult with
                                                            				  the network administrator to determine whether you need to assign an
                                                            				  alternative TFTP server instead of using the TFTP server that DHCP assigns. |
|---|---|

| Step 1 | Press Apps and choose Admin
                                                   				  Settings > Network Setup > Ethernet
                                                   				  Setup > IPv4 Setup . |
|---|---|
| Step 2 | To disable
                                             			 DHCP and manually set an IP address: Set DHCP
                                                   				  Enabled to No. Enter the
                                                   				  static IP address for the conference station. Enter the
                                                   				  subnet mask. Enter the
                                                   				  default router IP addresses. Set
                                                   				  Alternate TFTP Server to Yes, and enter the IP address for TFTP Server 1. |
| Step 3 | Press Apply , and then press Save . |

| Option | Description | To Change |
|---|---|---|
| Security
                                          					 Mode | Displays
                                          					 the security mode that is set for the phone. | From Cisco
                                          					 Unified Communications Manager Administration, choose Device > Phone > Phone
                                                						  Configuration . |
| LSC | Indicates
                                          					 if a locally significant certificate (used for the security features) is
                                          					 installed on the phone (Installed) or is not installed on the phone (Not
                                          					 Installed). | For
                                          					 information about how to manage the LSC for your phone, see "Using
                                             						the Certificate Authority Proxy Function" chapter in Cisco
                                             						Unified Communications Manager Security Guide . |
| Trust List | The Trust
                                          					 List provides submenus for CTL signature and Call Manager/TFTP Server. | For more
                                          					 information, see the Trust List Menu . |
| 802.1X
                                          					 Authentication | Displays
                                          					 the device authentication, EAP/MD5, and transaction status. | See 802.1X Authentication and Status Menus . |

| Option | Description | To Change |
|---|---|---|
| CTL
                                             					 Signature | Displays
                                             					 the MD5 hash of the CTL file. | For more
                                             					 information about this file, see "Configuring the Cisco CTL Client" chapter in Cisco
                                                						Unified Communications Manager Security Guide . |
| ITL File | Displays a
                                             					 submenu of options. Select an option to view its ITL setting information: ITL
                                                   						  Signature: MD5 hash of the ITL file. Unified CM/TFTP Server CAPF
                                                   						  Server TVS | For more
                                             					 information about this file, see "Configuring the Cisco ITL Client" chapter in the Cisco
                                                						Unified Communications Manager Security Guide . |
| Call
                                             					 Manager/TFTP Server | Displays
                                             					 the call manager/TFTP certificate information. |  |

| Option | Description | To
                                             					 Change |
|---|---|---|
| Device
                                             					 Authentication | Determines whether 802.1X authentication is enabled: Enabled: Phone uses
                                                						802.1X authentication to request network access. Disabled: Default setting
                                                						in which the phone uses CDP to acquire VLAN and network access. | Set 802.1X Device Authentication |

| Option | Description | To Change |
|---|---|---|
| 802.1X
                                             					 Authentication Status | Real-time
                                             					 progress of the 802.1X authentication status, displaying one of the following
                                             					 states: Disabled: 802.1X is disabled and the transaction was not
                                                   						  attempted Disconnected: Physical link is down or disconnected Connecting: Trying to discover or acquire the authenticator Acquired: Authenticator acquired, awaiting authentication to
                                                   						  begin Authenticating: Authentication in progress Authenticated: Authentication successful or implicit
                                                   						  authentication due to timeouts Held: Authentication failed, waiting before next attempt
                                                   						  (approximately 60 seconds) | Display
                                             					 only—Cannot configure. To view
                                             					 the transaction status of your 802.1X Authentication, choose Applications > Admin
                                                   						  Settings > Security Configuration > 802.1X Authentication
                                                   						  Status . |

| Step 1 | Choose Apps > Admin Settings > Security Config > 802.1X Authentication > Device Authentication . |
|---|---|
| Step 2 | Press Edit . |
| Step 3 | Set the Device Authentication option to Enabled or Disabled . The default value is Disabled. |
| Step 4 | Press Save . |