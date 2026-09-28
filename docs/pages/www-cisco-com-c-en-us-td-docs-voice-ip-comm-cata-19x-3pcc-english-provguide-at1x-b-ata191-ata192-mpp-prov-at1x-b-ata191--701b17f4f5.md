---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-provguide-at1x-b-ata191-ata192-mpp-prov-at1x-b-ata191--701b17f4f5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/provguide/at1x_b_ata191-ata192-mpp-prov/at1x_b_ata191-ata192-mpp-prov_chapter_0110.html
retrieved_at: 2026-08-22T01:05:32.337737+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Router Configuration Parameters

## Chapter: Router Configuration Parameters

# Router Configuration Parameters

## Nested Structure

All items in the <router_configuration> section of the XML file need to be nested under <router-configuration> and the section
                              headings as shown below.

• The </router-configuration> tag must appear at the end of the section.

• In the XML file, each section can be opened or closed by clicking the section heading. A + symbol indicates that a section
                              is closed, and a -symbol indicates that it is open.

• To enter a null value, enter a backslash at the end of the parameter name, as show in this example: <MAC_Address_Clone_Address
                              />

### Nested Sections

```
- <flat-profile>
   ...
   ...
- <router-configuration>
   + <WAN_Basic_Setting>
   + <WAN_Interface>
   + <WAN_IP6_Setting>
   + <PHY_Port_Setting>
   + <MAC_Address_Clone>
   + <Internet_Option>
   + <DHCP_Server_Pool>
   + <LAN_IP6_Setting>
   + <WAN_VLAN_Setting>
   + <CLDP_Setting>
   + <Single_Port_Forwarding>
   + <Port_Rang_Forwarding>
   + <SNMP>
   + <Time_Setup>
    <QoS_Bandwidth_Control>
   + <Software_DMZ>
     <Bonjour_Enable>1</Bonjour_Enable>
     <Reset_Button_Enable>1</Reset_Button_Enable>
     <Router_Mode>1</Router_Mode>
     <Monitor_WAN_Port_Only>0</Monitor_WAN_Port_Only>
   + <VPN_Passthrough>
   + <Web_Management>
   + <TR-069>
   + <Log_Configuration>
     <Web_Login_Admin_Name>admin</Web_Login_Admin_Name>
     <!--  <Web_Login_Admin_Password></Web_Login_Admin_Password  -->
     <Web_Login_Guest_Name>cisco</Web_Login_Guest_Name>
     <!--  <Web_Login_Guest_Password></Web_Login_Guest_Password  -->    
   + <SSH>
   </router-configuration>
</flat-profile>
```

## WAN_Basic_Setting Parameters

This section describes the parameters in the <x> section of the config.xml file.

TIP: You can click the <x> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

WAN_Stack_Mode

Description —IP stack mode

User Interface — Network Setup > Basic Settings page, Stack Mode field

Values

0: IPv4 Only

1: IPv6 Only

2: Dual Stack

Default —0

WAN_Signal_Preference

Description —Preference IP mode for SIP Signaling.

User Interface — Network Setup > Basic Settings page, Signaling Preference field.

Values

0: Prefer IPv4

1: Prefer IPv6

Default —0

WAN_Media_Preference

Description —Preference IP mode for RTP stream.

User Interface — Network Setup > Basic Settings page, Media Preference field.

Values

0: Prefer IPv4

1: Prefer IPv6

Default —0

## WAN_Interface Parameters

This section describes the parameters in the <WAN_Interface> section of the config.xml file.

TIP: You can click the <WAN_Interface> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

<WAN_Connection_Type>

Description —Defines the connection/addressing mode used for the INTERNET (WAN) port.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, Connection Type field

Values

dh: DHCP

st: Static

pp: PPPoE

Default —dh

Example —Static connection type

<WAN_Connection_Type>st</WAN_Connection_Type>

<WAN_DHCP_MTU_Mode>

<WAN_Static_MTU_Mode>

<WAN_PPPoE_MTU_Mode>

Description —MTU mode. Use the parameter corresponding to the configured connection type.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, MTU drop-down list

Values

0: Auto

1: Manual

Default —0

Example —Manual MTU mode for a static connection

<WAN_Static_MTU_Mode>1</WAN_Static_MTU_Mode>

<WAN_DHCP_MTU_Size>

<WAN_Static_MTU_Size>

<WAN_PPPoE_MTU_Size>

Description —MTU size. Use the parameter corresponding to the configured connection type.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, MTU text box

Values —576 to1492

Default —0

Example —Customized MTU size for PPPoE

<WAN_PPPoE_MTU_Size>1492</WAN_PPPoE_MTU_Size>

<WAN_Static_IP_NET>

Description —Specifies the IPv4 address for the Static IP connection.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, Internet IPv4 , Subnet Mark ,and Default Gateway text boxes (available when Static IP is the Connection Type)

Parameters —Internet_IP:Subnet_Mask:Default_Gateway [:DNS1[:DNS2[:DNS3]]]

Values

Internet_IP: IPv4 address

Subnet_Mask: IPv4 mask address

Default_Gateway: IPv4 address

DNS_1: IPv4 address

DNS_2: IPv4 address

DNS_3: IPv4 address

Default —0.0.0.0:0.0.0.0:0.0.0.0:0.0.0.0:0.0.0.0:0.0.0.0

Example

<WAN_Static_IP_NET>10.1.1.1:255.255.255.0:10.1.1.254:10.1.1.2:10.1.1.3</WAN_Static_IP_NET>

<WAN_PPPoE_User_Name>

Description —Username for PPTP session through the INTERNET (WAN) port.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, User Name field (available when PPPoE is the Connection Type)

Values —(up to 64 characters), Printable ASCII characters

Default —null

Example

<WAN_PPPoE_User_Name>test@example.net</WAN_PPPoE_User_Name>

<WAN_PPPoE_Password>

Description —Configures the interface settings for defined VLAN sub interfaces. VLAN ID n must be previously defined in the VLAN_ID_Index
                                          tag. This tag defines the password for PPPoE session configured over the sub interface. Note: the value of this field is hidden
                                          when reading the config.xml file from the device.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, Password field (available when PPPoE is the Connection Type)

Values —password (up to 64 characters)

Default —commented out, <!-- <WAN_PPPoE_Password></WAN_PPPoE_Password>-->

Example

<WAN_PPPoE_Password>my-password</WAN_PPPoE_Password>

<WAN_PPPoE_Service_Name>

Description —Descriptive service name (provided by the ISP), for a PPPoE session.

User Interface — Network Setup > Basic Setup > IPv4 Settings page, Service Name field (available when PPPoE is the Connection Type)

Parameter —Service name

Values —name (up to 64 characters)

Default —null

Example

<WAN_PPPoE_Service_Name>ServiceX_PPP</WAN_PPPoE_Service_Name>

<WAN_PPPoE_Keep_Alive>

User Interface — Network Setup > Basic Setup > IPv4 Settings page, Keep Alive field, Connect on Demand , and Max Idle fields (available when PPPoE is the Connection Type)

Description —Keep Alive or Connect on Demand settings for a PPPoE session configured.

Parameter —Type:Max_Idle_Time:30

Values

Type:

0 (Keep Alive)

1 (Connect on Demand)

Max_Idle_Time (Minutes)=1...9999 (for Connect on Demand)

30 is a static value

Default —0:0:30

Example

<WAN_PPPoE_Keep_Alive>1:5:30</WAN_PPPoE_Keep_Alive>

### WAN Example 1: DHCP with automatic MTU mode

```
<router-configuration>
<WAN_Interface>
<WAN_Connection_Type>dh</WAN_Connection_Type>
<WAN_DHCP_MTU_Mode>0</WAN_DHCP_MTU_Mode>
<WAN_DHCP_MTU_Size>0</WAN_DHCP_MTU_Size>
<WAN_Static_IP_NET>0.0.0.0:0.0.0.0:0.0.0.0</WAN_Static_IP_NET>
<WAN_Static_MTU_Mode>0</WAN_Static_MTU_Mode>
<WAN_Static_MTU_Size>0</WAN_Static_MTU_Size>
<WAN_PPPoE_User_Name />
<WAN_PPPoE_Service_Name />
<WAN_PPPoE_Password />
<WAN_PPPoE_Keep_Alive>0:0:30</WAN_PPPoE_Keep_Alive>
<WAN_PPPoE_MTU_Mode>0</WAN_PPPoE_MTU_Mode>
<WAN_PPPoE_MTU_Size>0</WAN_PPPoE_MTU_Size>
</WAN_Interface>
...
</router-configuration>
```

### WAN Example 2: Static IP with manual MTU mode

```
<router-configuration>
...
<WAN_Interface>
<WAN_Connection_Type>st</WAN_Connection_Type>
<WAN_DHCP_MTU_Mode>0</WAN_DHCP_MTU_Mode>
<WAN_DHCP_MTU_Size>0</WAN_DHCP_MTU_Size>
<WAN_Static_IP_NET>10.1.1.1:255.255.255.0:10.1.1.254:10.1.1.2:10.1.1.3</
WAN_Static_IP_NET>
<WAN_Static_MTU_Mode>1</WAN_Static_MTU_Mode>
<WAN_Static_MTU_Size>1492</WAN_Static_MTU_Size>
</WAN_Interface>
...
</router-configuration>
```

### WAN Example 3: PPPoE with Connect on Demand

```
<router-configuration>
...
<WAN_Interface>
<WAN_Connection_Type>pppoe</WAN_Connection_Type>
<WAN_DHCP_MTU_Mode>0</WAN_DHCP_MTU_Mode>
<WAN_DHCP_MTU_Size>0</WAN_DHCP_MTU_Size>
<WAN_Static_IP_NET>0.0.0.0:0.0.0.0:0.0.0.0</WAN_Static_IP_NET>
<WAN_Static_MTU_Mode>0</WAN_Static_MTU_Mode>
<WAN_Static_MTU_Size>0</WAN_Static_MTU_Size>
<WAN_PPPoE_User_Name>test@example.net</WAN_PPPoE_User_Name>
<WAN_PPPoE_Password>my-password</WAN_PPPoE_Password>
<WAN_PPPoE_Service_Name>ServiceX_PPP</WAN_PPPoE_Service_Name>
<WAN_PPPoE_Keep_Alive>1:5:30</WAN_PPPoE_Keep_Alive>
<WAN_PPPoE_MTU_Mode>0</WAN_PPPoE_MTU_Mode>
<WAN_PPPoE_MTU_Size>0</WAN_PPPoE_MTU_Size>
</WAN_Interface>
...
</router-configuration>
```

## WAN_IP6_Setting Parameters

This section describes the parameters in the <WAN_IP6_Setting> section of the config.xml file.

TIP: You can click the <WAN_IP6_Setting> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

WAN_IP6_Allow_AutoConfig

Description —Set enabled to allow stateless IPv6 adddress generation on receiving RA.

User Interface — Network Setup > IPv6 Settings page, Allow Auto Configuration field.

Values

0: Disabled

1: Enabled

Default —1

WAN_IP6_Connection_Type

Description —IPv6 connection type

User Interface — Network Setup > IPv6 Settings page, Connection Type field.

Values

0: DHCPv6

1: Static

2: PPPoE

Default —0

WAN_Static_IP6_Address

Description —Manually configured IP v6 address.

User Interface — Network Setup > IPv6 Settings page, Internet IPv6 Address field.

Values —address (up to 64 characters)

Default —null

WAN_Static_IP6_Prefix_Length

Description —Manually configured IP v6 prefix length.

User Interface — Network Setup > IPv6 Settings page, Prefix Length field.

Values —0 to 64

Default —64

WAN_Static_IP6_Gateway

Description —Manually configured IPv6 router address

User Interface — Network Setup > IPv6 Settings page, Default Gateway field.

Values —0-64

Default —null

## PHY_Port_Setting Parameters

This section describes the parameters in the <PHY_Port_Setting> section of the config.xml file.

TIP: You can click the <PHY_Port_Setting> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

<Flow_Control>

Description —Enables or disables flow control

User Interface — Interface Setup > Advanced Settings > Port Setting page, Flow Control field

Values

0: Disabled

1: Enabled

Default —1

Example —Flow control enabled

<Flow_Control>1</Flow_Control>

<Speed_Duplex>

Description —The port speed and duplex mode

User Interface — Interface Setup > Advanced Settings > Port Setting page, Speed Duplex field

Values

auto

10h

10f

100h

100f

Default —auto

Example —100 Mbps, half-duplex mode

<Speed_Duplex>100h</Speed_Duplex>

### <PHY_Port_Setting> Example: Flow control enabled with auto-negotiated duplex mode

```
<router-configuration>
...
<PHY_Port_Setting>
<Flow_Control>1</Flow_Control>
<Speed_Duplex>auto</Speed_Duplex>
</PHY_Port_Setting>
...
</router-configuration>
```

## MAC_Address_Clone Parameters

This section describes the parameters in the <MAC_Address_Clone> section of the config.xml file.

TIP: You can click the <MAC_Address_Clone> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

<MAC_Address_Clone_Enabled>

Description —Enables or disables MAC address cloning.

User Interface — Interface Setup > Advanced Settings > MAC Address Clone page, MAC Clone field

Values

0: Disabled

1: Enabled

Default —0

Example —MAC clone enabled

<MAC_Address_Clone_Enabled>1</MAC_Address_Clone_Enabled>

<MAC_Address_Clone_Address>

Description —MAC address to assign (clone) to this ATA

User Interface — Interface Setup > Advanced Settings > MAC Address Clone page, MAC Address field (available when MAC Clone is enabled)

Values —MAC address

Default —null

Example

<MAC_Address_Clone_Address>00:22:68:19:EF:83</MAC_Address_Clone_Address>

### <MAC_Address_Clone> Example: MAC Address Clone enabled

```
<router-configuration>
...
<MAC_Address_Clone>
<MAC_Address_Clone_Enabled>1</MAC_Address_Clone_Enabled>
<MAC_Address_Clone_Address>00:22:68:19:EF:83</MAC_Address_Clone_Address>
</MAC_Address_Clone>
...
</router-configuration>
```

## Internet_Option Parameters

This section describes the parameters in the <Internet_Option> section of the config.xml file.

TIP: You can click the <Internet_Option> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

<Host_Name>

Description —The name of the ATA

User Interface — Network Setup > Basic Setup > Basic Settings page, Host Name field

Values —name

Default —model number

Example

<Host_Name>ATA-192-MPP</Host_Name>

<Domain_Name>

Description —A domain name specified by the ISP, if applicable

User Interface — Network Setup > Basic Setup > Basic Settings page, Domain Name field

Values —name

Default —null

Example

<Domain_Name>My ISP</Domain_Name>

<DNS_Order>

Description —Method for choosing a DNS server

User Interface — Network Setup > Basic Setup > IPv4 Settings page, DNS Server Order field

Values

0:Manual

1:Manual-DHCP

2:DHCP-Manual

Default —2

Example —Manual-DHCP order

<DNS_Order>2</DNS_Order>

<DNS>

Description —For manual DNS server order, the IPv4 address of a DNS server; optionally, a secondary server can be specified

User Interface — Network Setup > Basic Setup > IPv4 Settings page, Primary DNS and Secondary DNS fields

Values —DNS1[:DNS2]

Default —null

Example —Primary and secondary DNS server

<DNS>209.165.201.1:209.165.201.2</DNS>

DNS6_Order

Description —IPv6 DNS server order

User Interface — Network Setup > IPv6 Settings page, DNS Server Order field

Values

0: only use manual DNS server

1: manual DNS server first, then dhcpv6 DNS server

2: dhcpv6 DNS serer first, then manual DNS server

Default —2

DNS6

Description —manual configured IPv6 DNS server, optionally a secondary server can be specified

User Interface — Network Setup > IPv6 Settings page, Primary DNS and Secondary DNS fields

Values —DNS6_1[:DNS6_2]

Default —null

### <Internet_Option> Example

```
<router-configuration>
...
<Internet_Option>
<Host_Name>ATA192-MPP</Host_Name>
<Domain_Name>My ISP</Domain_Name>
<DNS_Order>2</DNS_Order>
<DNS>209.165.201.1:209.165.201.2</DNS>
</Internet_Option>
...
</router-configuration>
```

## DHCP_Server_Pool Parameters

This section describes the parameters in the <DHCP_Server_Pool> section of the config.xml file.

### Rule

All parameters in the <DHCP_Server> section of the XML file are nested between <Rule> and </Rule>.

Parameter

Details

<DHCP_Server>

Description —Enables or disables the DHCP server

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, DHCP Server field

Values

0: Disabled

1: Enabled

Default —1

Example —DHCP server enabled

<DHCP_Server>1</DHCP_Server>

<Local_IP>

Description —The IPv4 address of the LAN interface

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Local IP address field

Values —IPv4 address

Default —192.168.15.1

Example:

<Local_IP>192.168.15.1</Local_IP>

<Subnet_Mask>

Description —The subnet mask for the local network

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Subnet Mask field

Values —Class C subnet mask

255.255.255.0

255.255.255.128

255.255.255.192

255.255.255.224

255.255.255.240

255.255.255.248

255.255.255.252

Default —255.255.255.0

Example:

<Subnet_Mask>255.255.255.0</Subnet_Mask>

<DHCP_Client_Table>

Description —Clients with reserved IPv4 addresses

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, IP Reservation list (available after clicking the Show DHCP Reservation button)

Values —Semi-colon separated list of client information in the following order: <MAC address> <ip_address> on <client_name>

Default —null

Example:

<DHCP_Client_Table>58:8D:09:72:73:DA 192.168.15.100 on Computer-1;00:22:68:19:EF:83 192.168.15.101 on Computer-2;</DHCP_Client_Table>

<Option_66>

Description —Method for specifying a TFTP server for remote configuration of the ATA

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 66 field

Values

0: None

2: Remote TFTP Server

3: Manual TFTP Server

Default —0

Example —Remote TFTP server

<Option_66>2</Option_66>

<TFTP_IP>

Description —IPv4 address of a TFTP server, if Option 66 is set to Manual

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, TFTP Server field

Values —IPv4 address

Default —0.0.0.0

Example

<TFTP_IP>209.165.202.129</TFTP_IP>

<Option_67>

Description —Provides a configuration/bootstrap filename to hosts that request this option

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 67 field

Values —filename

Default —null

Example

<Option_67>MyDirectory/MyFile.cfg</Option_67>

<Option_159 >

Description —Provides a configuration URL to hosts that request this option

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 159 field

Values —URL

Default —null

Example

<Option_159>http://MyDomain.com/MyDirectory/MyFile.cfg></Option_159>

<Option_160 >

Description —Provides a configuration URL to hosts that request this option

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 160 field

Values —filename

Default —null

Example

<Option_67>MyDirectory/MyFile.cfg</Option_67>

<DNS_Proxy>

Description —Enables or disables the DNS proxy, which relays DNS requests to the current public network DNS server for the proxy, and
                                             replies as a DNS resolver to the client device on the network

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, DNS Proxy field

Values

0: Disabled

1: Enabled

Default —1

Example —DNS proxy enabled

<DNS_Proxy>1</DNS_Proxy>

<Starting_IP>

Description —The first IPv4 address in the range of IPv4 addresses that are assigned by the DHCP server

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Starting IP address field

Values —IPv4 address

Default —192.168.15.100

Example

<Starting_IP>192.168.15.110</Starting_IP>

<Max_DHCP_User>

Description —The maximum number of devices that can receive DHCP addresses from the DHCP server

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Maximum DHCP Users field

Values —number

Default —50

Example —10-device maximum

<Max_DHCP_User>10</Max_DHCP_User>

<Client_Lease_Time>

Description —The number of minutes that a dynamically assigned IPv4 address can be in use, or "leased"

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Client Lease Time field

Values —number. Enter the number of minutes. Enter 0 to represent 1 day. Enter 9999 to never expire.

Default —0 (1 day)

Example —No expiration

<Client_Lease_Time>9999</Client_Lease_Time>

<Static_DNS>

Description —Defines a DNS server address that will be provided to DHCP clients. If DNS Proxy is enabled, clients will automatically be
                                             issued the Local IPv4 address to use for DNS.

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Static DNS field

Values —IPv4 address

Default —0.0.0.0

Example

<Static_DNS>209.165.202.129</Static_DNS>

<Default_Gateway>

Description —Enter the IPv4 address of the default gateway to be used by the DHCP clients.

User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Default Gateway field

Default —192.168.15.1

Example

<Default_Gateway>192.168.15.1</Default_Gateway>

#### <DHCP_Server_Pool> Example: DHCP enabled with two DHCP reservations <router-configuration>

```
...
<DHCP_Server_Pool>
<Rule>
<DHCP_Server>1</DHCP_Server>
<Local_IP>192.168.15.1</Local_IP>
<Subnet_Mask>255.255.255.0</Subnet_Mask>
<DHCP_Client_Table>58:8D:09:72:73:DA 192.168.15.100 on Computer-1;00:22:68:19:EF:83 192.168.15.101 on Computer-2;</DHCP_Client_Table>
<TFTP_IP>0.0.0.0</TFTP_IP>
<Starting_IP>192.168.15.100</Starting_IP>
<Max_DHCP_User>50</Max_DHCP_User>
<Client_Lease_Time>0</Client_Lease_Time>
<Default_Gateway>192.168.15.1</Default_Gateway>
</Rule>
</DHCP_Server_Pool>
...
</router-configuration>
```

## LAN_IP6_Setting Parameters

This section describes the parameters in the <LAN_IP6_Setting> section of the config.xml file.

TIP: You can click the <LAN_IP6_Setting> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

LAN_IP6_Address_Assign_Type

Description —Method for IPv6 assignment to LAN device..

User Interface — Network Setup > IPv6 LAN Settings page, Address Assign Type field

Values

0: SLACC

1: DHCP6s

Default —0

LAN_DHCP6_Delegation_Enable

Description —Set enabled to support DHCPv6 delegation which support to obtain LAN prefix via DHCPv6 client

User Interface — Network Setup > IPv6 LAN Settings page, DHCPv6 Delegation field.

Values

0: Disabled

1: Enabled

Default —0

LAN_IP6_Prefix

Description —Manual LAN prefix, editable only when DHCP delegation is disabled.

User Interface — Network Setup > IPv6 LAN Settings page, IPv6 Address Prefix field.

Values —0-64

Default —null

## WAN_VLAN_Setting Parameters

This section describes the parameters in the <WAN_VLAN_Setting> section of the config.xml file.

Parameter

Details

<WAN_VLAN_Enable>

Description —Enables or disables a VLAN on your network

User Interface — Network Setup > Advanced Settings > VLAN page, Enable VLAN field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example —VLAN enabled

<WAN_VLAN_Enable>1</WAN_VLAN_Enable>

<WAN_VLAN_ID>

Description —A number that identifies the VLAN

User Interface — Network Setup > Advanced Settings > VLAN page, VLAN ID field

Valid inputs —1~4094

Default —1

Example —VLAN ID 100

<WAN_VALN_ID>100</WAN_VALN_ID>

### <WAN_VLAN_Setting> Example: VLAN Enabled with ID 10

```
<router-configuration>
...
<WAN_VLAN_Setting>
<WAN_VLAN_Enable>1</WAN_VLAN_Enable>
<WAN_VALN_ID>100</WAN_VALN_ID>
</WAN_VLAN_Setting>
...
</router-configuration>
```

## CLDP_Setting Parameters

This section describes the parameters in the <CLDP_Setting> section of the config.xml file.

Parameter

Details

<CDP_ENABLE>

Description —Enables or disables Cisco Discovery Protocol (CDP)

User Interface — Network Setup > Advanced Settings > CDP & LLDP page, Enable CDP field

Valid inputs

0

1

0 means that the CDP is disabled. 1 means that the CDP is enabled.

Default —1

Example —CDP enabled

<CDP_ENABLE>1</CDP_ENABLE>

<LLDP_ENABLE>

Description —Enables or disables Link Layer Discovery Protocol (LLDP)

User Interface — Network Setup > Advanced Settings > CDP & LLDP page, Enable LLDP-MED field

Valid inputs

0

1

0 means that the LLDP is disabled. 1 means that the LLDP is enabled.

Default —1

Example —LLDP enabled

<LLDP_ENABLE>1</LLDP_ENABLE>

<LAYER2_LOGGING_ENABLE>

Description —Enables Layer 2 logging, which is used by CDP and LLDP for debugging purposes

User Interface — Network Setup > Advanced Settings > CDP & LLDP page, Layer 2 Logging field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example —Layer 2 logging enabled

<LAYER2_LOGGING_ENABLE>1</LAYER2_LOGGING_ENABLE>

### <CLDP_Setting> Example: CDP, LLDP, and Layer 2 logging enabled

```
<router-configuration>
...
<CLDP_Setting>
<CDP_ENABLE>1</CDP_ENABLE>
<LLDP_ENABLE>1</LLDP_ENABLE>
<LAYER2_LOGGING_ENABLE>1</LAYER2_LOGGING_ENABLE>
</CLDP_Setting>
...
</router-configuration>
```

## Single_Port_Forwarding Parameters

This section describes the parameters in the <Single_Port_Forwarding> section of the config.xml file.

TIP: You can click the <Single_Port_Forwarding> heading in the XML file to expand or collapse the nested parameters in this
                              section.

Parameter

Details

Single_Port_Forwarding_Index

Description —Index for single port forwarding. Should be listed in order with colon depending on the amount of entry added (Rule<index>).
                                          Index in order 0-9

User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Tupe page, Single Port Forwarding field

Values :

0: Disabled

1: Enabled

Default —null

Example

```
<Single_Port_Forwarding>
<Single_Port_Forwarding_Index>0:1:2</Single_Port_Forwarding_Index>
<Rule0>1:SNMP:br1:161:161:udp:192.168.15.30</Rule0>
<Rule1>0:Finger:br1:79:79:tcp:192.168.15.30</Rule1>
<Rule2>1:forward_rule:br1:25:27:both:192.168.15.15</Rule2>
</Single_Port_Forwarding>
```

Rule<index>

Description —Forwards traffic for a specified port to the same or an alternative port on the target server in the LAN. <index> can be
                                          0-9

User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Tupe page, Single Port Forwarding field.

Format : <Enabled>:<Name>:<Interface>:<External Port>:<Internal Port>:<Protocol>:<Target server IP>

Values

<Enabled>: 0-1

<Name>: String

<Interface>: br1

<External Port>: 1-65535

<Internal Port>: 1-65535

<Protocol>: tcp,udp,both

<Target server IP>: ipv4 address

Default —null

Example

```
<Rule0>1:SNMP:br1:161:161:udp:192.168.15.30</Rule0>
<Rule1>0:Finger:br1:79:79:tcp:192.168.15.30</Rule1>
<Rule2>1:forward_rule:br1:25:27:both:192.168.15.15</Rule2>
```

## Port_Range_Forwarding Parameters

This section describes the parameters in the <Port_Range_Forwarding> section of the config.xml file.

TIP: You can click the <Port_Range_Forwarding> heading in the XML file to expand or collapse the nested parameters in this
                              section.

Parameter

Details

Port_Range_Forwarding_Index

Description —Index for port range forwarding. Should be listed in order with colon depending on the amount of entry added (Rule<index>).

User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Type page, Port Range Forwarding field

Values : index in order: 0-9

Default —Null

Example

```
<Port_Range_Forwarding>
<Port_Range_Forwarding_Index>0:1</Port_Range_Forwarding_Index>
<Rule0>1:Rule_0:br1:50:60:tcp:192.198.15.22</Rule0>
<Rule1>0:Rule_1:br1:11:13:both:192.168.15.12</Rule1>
</Port_Range_Forwarding>
```

Rule<index>

Description —Forwards traffic to a range of ports to the same ports on the target server in the LAN. <index> can be 0-9.

User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Type page, Port Range Forwarding field.

Format : <Enabled>:<Name>:<Interface>:<Start Port>:<End Port>:<Protocol>:<Target server IP>

Values

<Enabled>: 0-1

<Name>: String

<Interface>: br1

<Start Port>: 1-65535

<End Port>: 1-65535

<Protocol>: tcp,udp,both

<Target server IP>: ipv4 address

Default —null

Example

```
<Rule0>1:Rule_0:br1:50:60:tcp:192.198.15.22</Rule0>
<Rule1>0:Rule_1:br1:11:13:both:192.168.15.12</Rule1>
```

## SNMP Parameters

This section describes the parameters in the <SNMP> section of the config.xml file.

Parameter

Details

<SNMP_Enabled>

Description —Enables or disables SNMP

User Interface — Administration > Management > SNMP page, SNMP section, Enabled and Disabled options

Valid inputs

0: Disabled

1: Enabled

Default —0

Example —SNMP enabled

<SNMP_Enabled>1</SNMP_Enabled>

<SNMP_Trusted_IP>

Description —trusted v4 IP address that can access the ATA through SNMP

User Interface — Administration > Management > SNMP page, SNMP section, Trusted IP field

Valid inputs —IPv4 address and subnet mask in this order: 0.0.0.0/0.0.0.0

Default —0.0.0.0/0.0.0.0 (Any IP address)

Example

<SNMP_Trusted_IP>209.165.202.129/255.255.255.0</SNMP_Trusted_IP>

SNMP_Trusted_IP6

Description —trusted v4 IP address that can access the ATA through SNMP

User Interface — Administration > SNMP page, Trusted IPv6 field

Valid inputs —IPv6 address

Default —::

SNMP_Trusted_IP6_Prefix_Length

Description —prefix of the trusted v6 IP that can access the ATA through SNMP

User Interface — Administration > SNMP page, Trusted IPv6 field

Valid inputs —0-128

Default —0

<Get_Community>

Description —A community string for authentication for SNMP GET commands.

User Interface —— Administration > Management > SNMP page, SNMP section, Get/Trap Community field

Valid inputs —string

Default —public

Example

<Get_Community>MyGet</Get_Community>

<Set_Community>

Description —A community string for authentication for SNMP GET commands.

User Interface — Administration > Management > SNMP page, SNMP section, Set Community field

Valid inputs —string

Default —private

Example

<Set_Community>MySet</Set_Community>

<SNMPV3>

User Interface — Administration > Management > SNMP page, SNMPV3 section, Enable and Disable fields

Valid inputs

0: Disabled

1: Enabled

Default —0

Example —SNMPv3 enabled

<SNMPV3>1</SNMPV3>

<RW_User>

Description —A username for SNMP authentication

User Interface — Administration > Management > SNMP page, SNMPV3 section, R/W User field

Valid inputs —username

Default —v3rwuser

Example

<RW_User>MyUsername</RW_User>

<Auth_Protocol>

Description —SNMPv3 authentication protocol

User Interface — Administration > Management > SNMP page, SNMPV3 section, Auth-Protocol field

Valid inputs

MD5

SHA

SHA256

SHA512

Default —MD5

Example—SHA enabled

<Auth_Protocol>SHA</Auth_Protocol>

<Auth_Password>

Description —Password for SNMPv3 authentication

User Interface — Administration > Management > SNMP page, Auth-Password field for SNMPv3

Valid inputs —string

Default —1111111111

Example

<Auth_Password>MyPassword</Auth_Password>

<Privacy_Protocol>

Description —Privacy authentication protocol for SNMPv3

User Interface — Administration > Management > SNMP page, SNMPV3 section, privprotocol field

Valid inputs

None

DES

Default —DES

Example —DES enabled

<Privacy_Protocol>DES</Privacy_Protocol>

<Privacy_Password>

Description —Privacy authentication password for SNMPv3

User Interface — Administration > Management > SNMP page, SNMPV3 section, Privacy Password field

Valid inputs —string

Default —1111111111

Example

<Privacy_Password>MyPrivacyPassword</Privacy_Password>

<TRAP_IP_Address>

Description —The IP Address of the SNMP manager or trap agent

User Interface — Administration > Management > SNMP page, Trap Configuration section, IP Address field

Valid inputs —IPv4 address

Default —192.168.15.100

Example

<TRAP_IP_Address>209.165.202.129</TRAP_IP_Address>

<TRAP_Port>

Description —The SNMP trap port used by the SNMP manager or trap agent to receive the trap messages

User Interface — Administration > Management > SNMP page, Trap Configuration section, Port field

Valid inputs —162 or 1025~65535

Default —162

Example

<TRAP_Port>162</TRAP_Port>

<TRAP_SNMP_Version>

Description —The SNMP version in use by the SNMP manager or trap agent

User Interface — Administration > Management > SNMP page, Trap Configuration section, SNMP Version field

Valid inputs —One of the SNMP version number listed below

v1

v2c

v3

Default —v1

Example

<TRAP_SNMP_Version>v3</TRAP_SNMP_Version>

### <SNMP> Example 1: SNMP Enabled from Any IP Address

```
<router-configuration>
...
<SNMP>
<SNMP_Enabled>1</SNMP_Enabled>
<SNMP_Trusted_IP>0.0.0.0/0.0.0.0</SNMP_Trusted_IP>
<Get_Community>MyGet</Get_Community>
<Set_Community>MySet</Set_Community>
<TRAP_IP_Address>209.165.202.129</TRAP_IP_Address>
<TRAP_Port>162</TRAP_Port>
<TRAP_SNMP_Version>v3</TRAP_SNMP_Version>
</SNMP>
...
</router-configuration>
```

### <SNMP> Example 2: SNMPv3 Enabled from Trusted IP Address

```
<router-configuration>
...
<SNMP>
<SNMP_Enabled>1</SNMP_Enabled>
<SNMP_Trusted_IP>209.165.202.129/255.255.255.0</SNMP_Trusted_IP>
<Get_Community>MyGet</Get_Community>
<Set_Community>MySet</Set_Community>
<SNMPV3>1</SNMPV3>
<RW_User>MyUsername</RW_User>
<Auth_Protocol>SHA</Auth_Protocol>
<Auth_Password>MyPassword</Auth_Password>
<Privacy_Protocol>DES</Privacy_Protocol>
<Privacy_Password>MyPrivacyPassword</Privacy_Password>
<TRAP_IP_Address>209.165.201.1</TRAP_IP_Address>
<TRAP_Port>162</TRAP_Port>
<TRAP_SNMP_Version>v3</TRAP_SNMP_Version>
</SNMP>
...
<router-configuration>
```

## Time_Setup Parameters

Parameter

Details

<Time_Zone>

Description —The time zone for the site where the ATA is in operation

User Interface — Network Setup > Basic Setup > Time Settings page, Time Zone field

Valid inputs —number identifying the time zone. See Time Zone Settings

Default —08 1 1

Example —Germany

<Time_Zone>+01 2 2</Time_Zone>

<Auto_Adjust_Clock>

Description —Enables or disables automatic time adjustments for daylight savings time

User Interface — Network Setup > Basic Setup > Time Settings page, Adjust Clock for Daylight Saving Changes field

Valid inputs

0: Disabled

1: Enabled

Default —1

Example —Automatic Daylight Saving adjustment enabled

<Auto_Adjust_Clock>1</Auto_Adjust_Clock>

<Daylight_Saving_Time_Rule>

Description —The method for specifying a time to start and end the daylight saving time

User Interface — Network Setup > Basic Setup > Time Settings page, Daylight Saving Time Rule field

Valid inputs — start=month/day/weekday/hh:mm:ss;end=month/day/weekday/hh:mm:ss;save=hours

Default —blank

Example —start=3/-1/7/2;end=11/-1/7/2;save=1

If you've configured this value and enabled <Auto_Adjust_Clock>, the <Daylight_Saving_Time_Rule> takes precedence.

<Time_Server_Mode>

Description —The method for specifying an NTP time server Time Server Address

User Interface — Network Setup > Basic Setup > Time Settings page, Time Server field

Valid inputs

manual

auto

Default —auto

Example —Manual mode

<Time_Server_Mode>manual</Time_Server_Mode>

<Time_Server>

Description —IPv4 address or domain name of an NTP server

User Interface— Network Setup > Basic Setup > Time Settings page, Time Server Address field

Valid inputs —IPv4 address or domain name

Default —0.ciscosb.pool.ntp.org

Example —European pool

<Time_Server>server 0.europe.pool.ntp.org </Time_Server>

<Resync_Timer>

Description —The interval, in seconds, at which the ATA resynchronizes with the NTP server

User Interface — Network Setup > Basic Setup > Time Settings page, Resync Timer field

Valid inputs —number

Default —3600

Example

<Resync_Timer>3600</Resync_Timer>

<Auto_Recovery_System_Time>

Description —When enabled, allows the ATA to automatically reconnect to the time server after a system reboot

User Interface — Network Setup > Basic Setup > Time Settings page, Auto Recovery After System Reboot field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example —Auto Recovery enabled

<Auto_Recovery_System_Time>1</Auto_Recovery_System_Time>

<Time_Mode>

Description —The method of specifying a time server

User Interface — Network Setup > Basic Setup > Time Settings page, Time Server field

Valid inputs

0: Manual

1: Auto

Default —1

Example —Automatic mode

<Time_Mode>1</Time_Mode>

### <Time_Setup> Example: Germany Time Zone with Daylight Savings and Auto-Recovery Enabled

```
<router-configuration>
...
<Time_Setup>
<Time_Zone>+01 2 2</Time_Zone>
<Auto_Adjust_Clock>1</Auto_Adjust_Clock>
<Time_Server_Mode>auto</Time_Server_Mode>
<Time_Server>0.ciscosb.pool.ntp.org</Time_Server>
<Resync_Timer>3600</Resync_Timer>
<Auto_Recovery_System_Time>1</Auto_Recovery_System_Time>
<Time_Mode>1</Time_Mode>
</Time_Setup>
...
<router-configuration>
```

## QoS_Bandwidth_Control Parameters

This section describes the parameters in the <QoS_Bandwidth_Control> section of the config.xml file.

### WAN

All parameters in the <Qos_Bandwidth_Control> section are nested between <WAN> and </WAN>.

Parameter

Details

<QoS_Always_ON>

Description —Determines whether QoS settings are enabled at all times or only when there is voice traffic

User Interface — Network Setup > Application > QoS page, QoS Policy field

Valid inputs

0: On When Phone In Use

1: Always On

Default —0

Example —On when phone is in use

<QoS_Always_ON>0</QoS_Always_ON>

<Upstream_Bandwidth>

Description —The maximum available upstream bandwidth, in kbps, as specified by the Internet Service Provider

User Interface — Network Setup > Application > QoS page, Upstream Bandwidth field

Valid inputs —number

Default —10000

Example

<Upstream_Bandwidth>20000</Upstream_Bandwidth>

#### <QoS_Bandwidth_Control> Example: QoS always on, maximum bandwidth of 20,000 kbps

```
<router-configuration>
...
<QoS_Bandwidth_Control>
<WAN>
<QoS_Always_ON>1</QoS_Always_ON>
<Upstream_Bandwidth>20000</Upstream_Bandwidth>
</WAN>
</QoS_Bandwidth_Control>
...
</router-configuration>
```

## HTTP_Proxy Parameters

This section describes the parameters in the <HTTP_Proxy> section of the config.xml file.

Parameter

Details

<Proxy_Mode>

Description —Specifies the HTTP proxy mode that the ATA uses, or disables the HTTP proxy feature.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Mode field.

Valid inputs

Off

Auto

Manual

Default —Off

Example —Auto proxy mode

<Proxy_Mode>Auto</Proxy_Mode>

<Use_Auto_Discovery__WPAD_>

Description —Determines whether the ATA uses the Web Proxy Auto-Discovery (WPAD) protocol to retrieve a PAC file.

If the parameter is set to No, you must configure the parameter <PAC_URL> .

The parameter configuration takes effect only when the <Proxy_Mode> is set to Auto.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Use Auto Discovery field.

Valid inputs

No

Yes

Default —Yes

Example —The WPAD protocol is not used.

<Use_Auto_Discovery__WPAD_>No</Use_Auto_Discovery__WPAD_>

<PAC_URL>

Description —The URL of a Proxy Auto-Configuration (PAC) file. This parameter configuration takes effect when the <Proxy_Mode> is set to Auto and <Use_Auto_Discovery__WPAD_> is set to No.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, PAC URL field.

Valid inputs— URL

Default —null

Example

http://proxy.department.branch.example.com

<Proxy_Server_Requires_Authentication>

Description —Select the option according to the actual behaviour of the proxy server. If the proxy server requires the user to provide
                                          authentication credentials, set it to Yes. Otherwise, select it to No.

If the parameter is set to Yes, you must further configure the parameters <Proxy_Username> and <Proxy_Password> .

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Server Requires Authentication field.

Valid inputs

No

Yes

Default —No

Example —The proxy server requires the user authentication.

<Proxy_Server_Requires_Authentication>1</Proxy_Server_Requires_Authentication>

<Proxy_Host>

Description —Specifies an IP address or hostname of the proxy host server that the ATA uses.

The parameter configuration is required if the <Proxy_Mode> is set to Manual.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Host field.

Valid inputs —A valid IP address or hostname of the proxy host server

Default —null

Example

<Proxy_Host>proxy.example.com</Proxy_Host>

<Proxy_Port>

Description —Specifies a port number of the proxy host server that the ATA uses.

The parameter configuration is required if the <Proxy_Mode> is set to Manual.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Port field.

Valid inputs —A valid port number from 2 to 65535.

Default —3128

Example

<Proxy_Port>3128</Proxy_Port>

<Proxy_Username>

Description —Enter a username for the authentication purpose of the proxy server.

The parameter configuration is required when <Proxy_Mode> is set to Manual and <Proxy_Server_Requires_Authentication> is set to Yes.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Username field.

Valid inputs —string

Default —null

Example

<Proxy_Username>Example</Proxy_Username>

<Proxy_Password>

Description —Enter the password of the specified username that the proxy server requires.

The parameter configuration is required when <Proxy_Mode> is set to Manual and <Proxy_Server_Requires_Authentication> is set to Yes.

User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Password field.

Valid inputs —string

Default —null

Example

<Proxy_Password>Example</Proxy_Password>

### <HTTP_Proxy> Example: Auto proxy mode with WPAD enabled

```
<router-configuration>
...
<HTTP_Proxy>
<Proxy_Mode>Auto</Proxy_Mode>
<Use_Auto_Discovery__WPAD_>Yes</Use_Auto_Discovery__WPAD_>
</HTTP_Proxy>
...
</router-configuration>
```

### <HTTP_Proxy> Example: Manual proxy mode with proxy authentication required

```
<router-configuration>
...
<HTTP_Proxy>
<Proxy_Mode>Manual</Proxy_Mode>
<Proxy_Host>proxy.example.com</Proxy_Host>
<Proxy_Host>3128</Proxy_Host>
<Proxy_Server_Requires_Authentication>Yes</Proxy_Server_Requires_Authentication>
<Proxy_Username>Username_Example</Proxy_Username>
<Proxy_Password>Password_Example</Proxy_Password>
</HTTP_Proxy>
...
</router-configuration>
```

## Software_DMZ Parameters

This section describes the parameters in the <Software_DMZ> section of the config.xml file.

### Rule1

All parameters in the <Software_DMZ> section are nested between <Rule1> and </Rule1>. Only one DMZ rule is allowed on this
                                 device.

Parameter

Details

<Status>

Description —Enables or disables exposing a local device to the Internet for a special purpose service

User Interface — Network Setup > Application > DMZ page, Status field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example —DMZ enabled

<Status>1</Status>

<Private_IP>

Description —The local IPv4 address of the device that can be accessed through the DMZ

User Interface — Network Setup > Application > DMZ page, Private IP field

Valid inputs —IPv4 address

Default —0.0.0.0

Example

<Private_IP>192.168.15.1</Private_IP>

<Rule_Number>

Description —A static setting used to define the DMZ rule

User Interface —not applicable

Valid inputs —1 (do not change this number)

Default —1

#### <Software_DMZ> Example: DMZ allowing Internet traffic to access

```
192.168.15.101
<router-configuration>
...
<Software_DMZ>
<Rule1>
<Status>1</Status>
<Private_IP>192.168.15.1</Private_IP>
</Rule1>
<Rule_Number>1</Rule_Number>
</Software_DMZ>
...
</router-configuration>
```

## Bonjour_Enable

Parameter

Details

<Bonjour_Enable>

Description —Enables or disables the Bonjour service discovery protocol, which may be required by network management systems that you
                                          use

User Interface — Administration > Management > Bonjour page, Enabled and Disabled fields

Valid inputs

0: Disabled

1: Enabled

Default —1

Example —Bonjour enabled

<Bonjour_Enable>1</Bonjour_Enable>

## Reset_Button_Enable

No other settings are nested below <Reset_Button_Enable>.

Parameter

Details

<Reset_Button_Enable>

Description —Enables or disables the RESET button

User Interface

Valid inputs

0: Disabled (button)

1: Enabled (button can be pressed for 1-2 seconds for reboot and 5-6 seconds for a factory reset)

Default —1

Example —Button disabled

<Reset_Button_Enable>0</<Reset_Button_Enable>

## Router_Mode

Parameter

Details

<Router_Mode>

Description —The operating mode of the router

User Interface — Network Setup > Basic Setup > Network Service page, Networking Service field

Valid inputs

0: Bridge

1: NAT

Default —1

Example —Bridge mode enabled

<Router_Mode>0<Router_Mode>

## Monitor_WAN_Port_Only Parameters

This section describes the parameters in the <Monitor_WAN_Port_Only> section of the config.xml file.

TIP: You can click the <Monitor_WAN_Port_Only> heading in the XML file to expand or collapse the nested parameters in this
                              section.

Parameter

Details

Monitor_WAN_Port_Only

Description —To monitor device link status base on wan port only. This configuration is only valid when <Router_Mode> is set to 0 (bridge).

User Interface — Network Setup > Basic Setup > Network Service page, Monitor Network Drop on Internet Port only field

Values

0: Off

1: On

Default —0

## VPN_Passthrough

This section describes the parameters in the <VPN_Passthrough> section of the config.xml file.

Parameter

Details

<IPSec_Passthrough>

Description —Enables or disables VPN passthrough for Internet Protocol Security (IPsec)

User Interface — Network Setup > Advanced Settings > VPN Passthrough page, IPsec Passthrough field

Valid inputs

0: Disabled

1: Enabled

Default —1

Example

<IPSec_Passthrough>1</IPSec_Passthrough>

<PPTP_Passthrough>

Description —Enables or disables VPN passthrough for Point-to-Point Tunneling Protocol (PPTP)

User Interface — Network Setup > Advanced Settings > VPN Passthrough page, PPTP Passthrough field

Valid inputs

0: Disabled

1: Enabled

Default —1

Example

<PPTP_Passthrough>1</PPTP_Passthrough>

<L2TP_Passthrough>

Description —Enables or disables VPN passthrough for Layer 2 Tunneling Protocol (L2TP)

User Interface — Network Setup > Advanced Settings > VPN Passthrough page, L2TP Passthrough field

Valid inputs

0: Disabled

1: Enabled

Default —1

Example

<L2TP_Passthrough>1</L2TP_Passthrough>

### <VPN_Passthrough> Example: All passthrough options enabled

```
<router-configuration>
...
<VPN_Passthrough>
<IPSec_Passthrough>1</IPSec_Passthrough>
<PPTP_Passthrough>1</PPTP_Passthrough>
<L2TP_Passthrough>1</L2TP_Passthrough>
</VPN_Passthrough>
...
</router-configuration>
```

## Web_Management

This section describes the parameters in the <Web_Management> section of the config.xml file.

Parameter

Details

<Web_Utility_Access_HTTP>

Description —Enables or disables access to the web-based configuration utility via HTTP, from a computer on the LAN

User Interface — Administration > Management > Web Access Management page, Web Utility Access field, HTTP option

Valid inputs

0: Disabled

1: Enabled

Default —0

Example

<Web_Utility_Access_HTTP>1</Web_Utility_Access_HTTP>

<Web_Utility_Access_HTTPS>

Description —Enables or disables access to the web-based configuration utility via HTTPS, from a computer on the LAN

User Interface — Administration > Management > Web Access Management page, Web Utility Access field, HTTPS option

Valid inputs

0: Disabled

1: Enabled

Default —1

Example

<Web_Utility_Access_HTTPS>1</Web_Utility_Access_HTTPS>

<Web_Remote_Management>

Description —Enables or disables access to the web-based configuration utility through the WAN interface (INTERNET port)

User Interface — Administration > Management > Web Access Management page, Remote Management field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example

<Web_Remote_Management>1</Web_Remote_Management>

<Remote_Web_Utility_Access>

Description —Specifies the protocol that can be used to access the web-based configuration utility through the WAN interface (INTERNET
                                          port), when Remote Management is enabled

User Interface — Administration > Management > Web Access Management page, Web Utility Access field

Valid inputs

0: HTTP

1: HTTPS

Default —1

Example

<Remote_Web_Utility_Access>1</Remote_Web_Utility_Access>

<Web_Remote_Upgrade>

Description —Enables or disables upgrading the firmware from a computer on the WAN, when Remote Management is enabled

User Interface — Administration > Management > Web Access Management page, Remote Upgrade field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example

<Web_Remote_Upgrade>1</Web_Remote_Upgrade>

<Allowed_Remote_IP_Type>

Description —Specifies a method for identifying remote devices that are allowed access to the web-based configuration utility, when Remote
                                          Management is enabled

User Interface — Administration > Management > Web Access Management page, Allowed Remote IPv4 Address field, Any IP Address option

Valid inputs :

0: Specified IP Address

1: Any IP Address

Default —1

Example

<Allowed_Remote_IP_Type>0</Allowed_Remote_IP_Type>

<Allowed_Remote_IP_Address>

Description —Specifies a remote IPv4 address that is allowed access to the web-based configuration utility, when Remote Management is
                                          enabled

User Interface — Administration > Management > Web Access Management page, Allowed Remote IPv4 Address field, unlabeled text box

Valid inputs —IPv4 address

Default —0.0.0.0

Example

<Allowed_Remote_IP_Address>209.165.201.129</Allowed_Remote_IP_Address>

<Remote_Management_Port>

Description —Specifies the port to use for access to the web-based configuration utility through the WAN interface (INTERNET port)

User Interface — Administration > Management > Web Access Management page, Remote Management Port field

Valid inputs —port number

Default —443

Example

<Remote_Management_Port>443</Remote_Management_Port>

### <Web_Management> Example: Remote Management and Remote Upgrade enabled

```
<router-configuration>
...
<Web_Management>
<Web_Utility_Access_HTTP>0</Web_Utility_Access_HTTP>
<Web_Utility_Access_HTTPS>1</Web_Utility_Access_HTTPS>
<Web_Remote_Management>1</Web_Remote_Management>
<Remote_Web_Utility_Access>1</Remote_Web_Utility_Access>
<Web_Remote_Upgrade>1</Web_Remote_Upgrade>
<Allowed_Remote_IP_Type>0</Allowed_Remote_IP_Type>
<Allowed_Remote_IP_Address>209.165.201.129 129</Allowed_Remote_IP_Address>
<Remote_Management_Port>443</Remote_Management_Port>
</Web_Management>
...
</router-configuration>
```

## TR-069 Parameters

This section describes the parameters in the <TR_069> section of the config.xml file.

Parameter

Details

<TR_069_Status>

Description —Enables or disables remote provisioning via TR-069 CPE WAN Management Protocol

User Interface —Administration > Management > TR-069 page, Status field

Valid inputs

0: Disabled

1: Enabled

Default —0

Example

<TR_069_Status>1</TR_069_Status>

<TR_069_ACS_URL>

Description —The URL of the Auto-Configuration Server (ACS)

User Interface —Administration > Management > TR-069 page, ACS URL field

Valid inputs —Domain name or IP address, starting with http:// or https://, and optionally ending with a port number

Default —null

Example

<TR_069_ACS_URL>http://ACS-example.com</TR_069_ACS_URL>

<TR_069_ACS_Username>

Description —The username for HTTP-based authentication to the ACS

User Interface —Administration > Management > TR-069 page, ACS Username field

Valid inputs —username

Default —null

Example

<TR_069_ACS_Username>MyUsername</TR_069_ACS_Username>

<TR_069_ACS_Password>

Description —The password for HTTP-based authentication to the ACS

User Interface —Administration > Management > TR-069 page, ACS Password field

Valid inputs —password

Default —commented out: <!-- <TR_069_ACS_Password></TR_069_ACS_Password> -->

Example

<TR_069_ACS_Password>MyACSPassword</TR_069_ACS_Password>

<TR_069_Connection_Request_URL>

Description —This field will be autofilled and does not need to be entered manually

User Interface —Administration > Management > TR-069 page, Connection Request URL field

Valid inputs —URL

Default —null

Example —not applicable, value is autofilled

<TR_069_Connection_Request_Username>

Description —This field will be autofilled and does not need to be entered manually

User Interface —Administration > Management > TR-069 page, Connection Request Username field

Valid inputs —username

Default —null

Example —not applicable, value is autofilled

<TR_069_Connection_Request_Password>

Description —This field will be autofilled and does not need to be entered manually

User Interface —Administration > Management > TR-069 page, Connection Request Password field

Valid inputs —password

Default —commented out, <!--<TR_069_Connection_Request_Password></TR_069_Connection_Request_Password>-->

Example

<TR_069_Connection_Request_Password> MyPassword</TR_069_Connection_Request_Password>

<TR_069_Periodic_Inform_Interval>

Description —When Periodic Information is enabled, the duration, in seconds, between CPE attempts to connect to the ACS

User Interface —Administration > Management > TR-069 page, Periodic Inform Interval field

Valid inputs —number

Default —86400

Example —Interval of 36000 seconds (10 minutes)

<TR_069_Periodic_Inform_Interval>36000</TR_069_Periodic_Inform_Interval>

<TR_069_Periodic_Inform_Enable>

Description —Enables or disables CPE connection requests to the ACS

User Interface —Administration > Management > TR-069 page, Periodic Inform Enable field

Valid inputs —

0: Disabled

1: Enabled

Default —1

Example —Periodic Inform enabled

<TR_069_Periodic_Inform_Enable>1</TR_069_Periodic_Inform_Enable>

## Log_Configuration Parameters

This section describes the parameters in the <Log_Configuration> section of the config.xml file.

Parameter

Details

<Log_Module>

Description —Value that indicates the debug flag of modules:

0: Default

1: Preset

2: Telephony

3: SIP

4: UI

5: Network

6: Media

7: System

8: Web

9: NTP

10: CDP/LLDP

11: Security

12: CSSD_RTP

13: CSSD_FAX

14: CSSD_ANY

User Interface — Administration > Debug Log Module page, Debug Log Module field

Valid inputs —0-14

Default —0

<RAM_Log_Size>

Description —The maximum size of the log file in kilobytes

User Interface — Administration > Debug Log Setting page, Debug Log Size field

Valid inputs —number from 128~1024

Default —200

Example

<RAM_Log_Size>200</RAM_Log_Size>

Syslog_Server_IP

Description —IPv4 address of debug log server

User Interface — Administration > Debug Log Setting page, Pv4 Address field

Valid inputs —Valid IPv4 address format

Default —null

Syslog_Server_IP6

Description —IPv6 address of debug log server

User Interface — Administration > Debug Log Setting page, Pv6 Address field

Valid inputs —Valid IPv6 address format

Default —null

Syslog_Server_Port

Description —debug log server port

User Interface — Administration > Debug Log Setting page, Port field

Valid inputs —0-65535

Default —514

Event_Log_Server

Description —Address of event log server, supports IPv4, IPv6, and FQDN

User Interface — Administration > Debug Log Setting page, Address field

Valid inputs —Valid IPv4, IPv6, or FQDN address format. Maximum length is 128 characters

Default —null

Event_Log_Port

Description —Port of event log server

User Interface — Administration > Debug Log Setting page, Port field

Valid inputs —0-65535

Default —514

Event_Log_Flag

Description —An bitwise value to turn on/off report of each event category (<DEV>: 1, <SYS>: 2 <CFG>: 4, <REG>: 8)

User Interface — Administration > Debug Log Setting page, Flag field

Valid inputs —0-65535

The available options are:

0: Disable

1: DEV

2: SYS

4: CFG

8: REG

15: DEV+SYS+CFG+REG

Default —15

PRT_Upload_Url

Description —Address of PRT upload server

User Interface — Administration > Debug Log Setting page, PRT Upload URL field

Valid inputs —Valid URL format. Maximum length is 256 characters.

Default —null

PRT_Upload_Method

Description —HTTP method to upload PRT

User Interface — Administration > Debug Log Setting page, Debug Log Size field

Valid inputs

0: POST

1: PUT)

Default —0

PRT_Max_Timer

Description —Value in minutes to specify interval of periodical PRT report.

User Interface — Administration > Debug Log Setting page, PRT Max Timer field

Valid inputs

0: Disable

15-1440

Default —0

## Web_Login_Admin_Name

Parameter

Details

<Web_Login_Admin_Name>

Description —The username for the administrator login, which has full read-write access to all parameters

User Interface — Administration > Management > User List page, Username field

Valid inputs —username

Default —admin

## Web_Login_Admin_Password

Parameter

Details

<Web_Login_Admin_Password>

Description—The password for the administrator login

User Interface — Administration > Management > User List page

Valid inputs —password (the minimum length of the characters is 8)

Default —commented out <!--<Web_Login_Admin_Password></Web_Login_Admin_Password>-->

Example

<Web_Login_Admin_Password>MyPassword</Web_Login_Admin_Password>

## Web_Login_Guest_Name

Parameter

Details

<Web_Login_Guest_Name>

Description —The username for the guest login, which has limited access to view or change parameters

User Interface — Administration > Management > User List page

Valid inputs —username

Default —cisco

Example

<Web_Login_Guest_Name>MyUsername</Web_Login_Guest_Name>

## Web_Login_Guest_Password

Parameter

Details

<Web_Login_Guest_Password>

User Interface — Administration > Management > User List Page

Valid inputs —password (the minimum length of the characters is 8)

Default —commented out,

Example —

<Web_Login_Guest_Password>MyPassword</Web_Login_Guest_Password>

## SSH Parameters

This section describes the parameters in the <SSH> section of the config.xml file.

TIP: You can click the <SSH> heading in the XML file to expand or collapse the nested parameters in this section.

Parameter

Details

SSH_ACCESS

Description —Set enabled to allow access to SSH service.

User Interface — Administration > SSH page, Access field

Values

0: Disabled

1: Enabled

Default —0

SSH_User_ID

Description —User name of SSH

User Interface — Administration > SSH page, User Name field

Values —0-50

Default —null

SSH_Password

Description —Password of SSH.

User Interface — Administration > SSH page, Password field

Values —0-50

Default —null

| Parameter | Details |
|---|---|
| WAN_Stack_Mode | Description —IP stack mode User Interface — Network Setup > Basic Settings page, Stack Mode field Values 0: IPv4 Only 1: IPv6 Only 2: Dual Stack Default —0 |
| WAN_Signal_Preference | Description —Preference IP mode for SIP Signaling. User Interface — Network Setup > Basic Settings page, Signaling Preference field. Values 0: Prefer IPv4 1: Prefer IPv6 Default —0 |
| WAN_Media_Preference | Description —Preference IP mode for RTP stream. User Interface — Network Setup > Basic Settings page, Media Preference field. Values 0: Prefer IPv4 1: Prefer IPv6 Default —0 |

| Parameter | Details |
|---|---|
| <WAN_Connection_Type> | Description —Defines the connection/addressing mode used for the INTERNET (WAN) port. User Interface — Network Setup > Basic Setup > IPv4 Settings page, Connection Type field Values dh: DHCP st: Static pp: PPPoE Default —dh Example —Static connection type <WAN_Connection_Type>st</WAN_Connection_Type> |
| <WAN_DHCP_MTU_Mode> <WAN_Static_MTU_Mode> <WAN_PPPoE_MTU_Mode> | Description —MTU mode. Use the parameter corresponding to the configured connection type. User Interface — Network Setup > Basic Setup > IPv4 Settings page, MTU drop-down list Values 0: Auto 1: Manual Default —0 Example —Manual MTU mode for a static connection <WAN_Static_MTU_Mode>1</WAN_Static_MTU_Mode> |
| <WAN_DHCP_MTU_Size> <WAN_Static_MTU_Size> <WAN_PPPoE_MTU_Size> | Description —MTU size. Use the parameter corresponding to the configured connection type. User Interface — Network Setup > Basic Setup > IPv4 Settings page, MTU text box Values —576 to1492 Default —0 Example —Customized MTU size for PPPoE <WAN_PPPoE_MTU_Size>1492</WAN_PPPoE_MTU_Size> |
| <WAN_Static_IP_NET> | Description —Specifies the IPv4 address for the Static IP connection. User Interface — Network Setup > Basic Setup > IPv4 Settings page, Internet IPv4 , Subnet Mark ,and Default Gateway text boxes (available when Static IP is the Connection Type) Parameters —Internet_IP:Subnet_Mask:Default_Gateway [:DNS1[:DNS2[:DNS3]]] Values Internet_IP: IPv4 address Subnet_Mask: IPv4 mask address Default_Gateway: IPv4 address DNS_1: IPv4 address DNS_2: IPv4 address DNS_3: IPv4 address Default —0.0.0.0:0.0.0.0:0.0.0.0:0.0.0.0:0.0.0.0:0.0.0.0 Example <WAN_Static_IP_NET>10.1.1.1:255.255.255.0:10.1.1.254:10.1.1.2:10.1.1.3</WAN_Static_IP_NET> |
| <WAN_PPPoE_User_Name> | Description —Username for PPTP session through the INTERNET (WAN) port. User Interface — Network Setup > Basic Setup > IPv4 Settings page, User Name field (available when PPPoE is the Connection Type) Values —(up to 64 characters), Printable ASCII characters Default —null Example <WAN_PPPoE_User_Name>test@example.net</WAN_PPPoE_User_Name> |
| <WAN_PPPoE_Password> | Description —Configures the interface settings for defined VLAN sub interfaces. VLAN ID n must be previously defined in the VLAN_ID_Index
                                          tag. This tag defines the password for PPPoE session configured over the sub interface. Note: the value of this field is hidden
                                          when reading the config.xml file from the device. User Interface — Network Setup > Basic Setup > IPv4 Settings page, Password field (available when PPPoE is the Connection Type) Values —password (up to 64 characters) Default —commented out, <!-- <WAN_PPPoE_Password></WAN_PPPoE_Password>--> Example <WAN_PPPoE_Password>my-password</WAN_PPPoE_Password> |
| <WAN_PPPoE_Service_Name> | Description —Descriptive service name (provided by the ISP), for a PPPoE session. User Interface — Network Setup > Basic Setup > IPv4 Settings page, Service Name field (available when PPPoE is the Connection Type) Parameter —Service name Values —name (up to 64 characters) Default —null Example <WAN_PPPoE_Service_Name>ServiceX_PPP</WAN_PPPoE_Service_Name> |
| <WAN_PPPoE_Keep_Alive> | User Interface — Network Setup > Basic Setup > IPv4 Settings page, Keep Alive field, Connect on Demand , and Max Idle fields (available when PPPoE is the Connection Type) Description —Keep Alive or Connect on Demand settings for a PPPoE session configured. Parameter —Type:Max_Idle_Time:30 Values Type: 0 (Keep Alive) 1 (Connect on Demand) Max_Idle_Time (Minutes)=1...9999 (for Connect on Demand) 30 is a static value Default —0:0:30 Example <WAN_PPPoE_Keep_Alive>1:5:30</WAN_PPPoE_Keep_Alive> |

| Parameter | Details |
|---|---|
| WAN_IP6_Allow_AutoConfig | Description —Set enabled to allow stateless IPv6 adddress generation on receiving RA. User Interface — Network Setup > IPv6 Settings page, Allow Auto Configuration field. Values 0: Disabled 1: Enabled Default —1 |
| WAN_IP6_Connection_Type | Description —IPv6 connection type User Interface — Network Setup > IPv6 Settings page, Connection Type field. Values 0: DHCPv6 1: Static 2: PPPoE Default —0 |
| WAN_Static_IP6_Address | Description —Manually configured IP v6 address. User Interface — Network Setup > IPv6 Settings page, Internet IPv6 Address field. Values —address (up to 64 characters) Default —null |
| WAN_Static_IP6_Prefix_Length | Description —Manually configured IP v6 prefix length. User Interface — Network Setup > IPv6 Settings page, Prefix Length field. Values —0 to 64 Default —64 |
| WAN_Static_IP6_Gateway | Description —Manually configured IPv6 router address User Interface — Network Setup > IPv6 Settings page, Default Gateway field. Values —0-64 Default —null |

| Parameter | Details |
|---|---|
| <Flow_Control> | Description —Enables or disables flow control User Interface — Interface Setup > Advanced Settings > Port Setting page, Flow Control field Values 0: Disabled 1: Enabled Default —1 Example —Flow control enabled <Flow_Control>1</Flow_Control> |
| <Speed_Duplex> | Description —The port speed and duplex mode User Interface — Interface Setup > Advanced Settings > Port Setting page, Speed Duplex field Values auto 10h 10f 100h 100f Default —auto Example —100 Mbps, half-duplex mode <Speed_Duplex>100h</Speed_Duplex> |

| Parameter | Details |
|---|---|
| <MAC_Address_Clone_Enabled> | Description —Enables or disables MAC address cloning. User Interface — Interface Setup > Advanced Settings > MAC Address Clone page, MAC Clone field Values 0: Disabled 1: Enabled Default —0 Example —MAC clone enabled <MAC_Address_Clone_Enabled>1</MAC_Address_Clone_Enabled> |
| <MAC_Address_Clone_Address> | Description —MAC address to assign (clone) to this ATA User Interface — Interface Setup > Advanced Settings > MAC Address Clone page, MAC Address field (available when MAC Clone is enabled) Values —MAC address Default —null Example <MAC_Address_Clone_Address>00:22:68:19:EF:83</MAC_Address_Clone_Address> |

| Parameter | Details |
|---|---|
| <Host_Name> | Description —The name of the ATA User Interface — Network Setup > Basic Setup > Basic Settings page, Host Name field Values —name Default —model number Example <Host_Name>ATA-192-MPP</Host_Name> |
| <Domain_Name> | Description —A domain name specified by the ISP, if applicable User Interface — Network Setup > Basic Setup > Basic Settings page, Domain Name field Values —name Default —null Example <Domain_Name>My ISP</Domain_Name> |
| <DNS_Order> | Description —Method for choosing a DNS server User Interface — Network Setup > Basic Setup > IPv4 Settings page, DNS Server Order field Values 0:Manual 1:Manual-DHCP 2:DHCP-Manual Default —2 Example —Manual-DHCP order <DNS_Order>2</DNS_Order> |
| <DNS> | Description —For manual DNS server order, the IPv4 address of a DNS server; optionally, a secondary server can be specified User Interface — Network Setup > Basic Setup > IPv4 Settings page, Primary DNS and Secondary DNS fields Values —DNS1[:DNS2] Default —null Example —Primary and secondary DNS server <DNS>209.165.201.1:209.165.201.2</DNS> |
| DNS6_Order | Description —IPv6 DNS server order User Interface — Network Setup > IPv6 Settings page, DNS Server Order field Values 0: only use manual DNS server 1: manual DNS server first, then dhcpv6 DNS server 2: dhcpv6 DNS serer first, then manual DNS server Default —2 |
| DNS6 | Description —manual configured IPv6 DNS server, optionally a secondary server can be specified User Interface — Network Setup > IPv6 Settings page, Primary DNS and Secondary DNS fields Values —DNS6_1[:DNS6_2] Default —null |

| Parameter | Details |
|---|---|
| <DHCP_Server> | Description —Enables or disables the DHCP server User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, DHCP Server field Values 0: Disabled 1: Enabled Default —1 Example —DHCP server enabled <DHCP_Server>1</DHCP_Server> |
| <Local_IP> | Description —The IPv4 address of the LAN interface User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Local IP address field Values —IPv4 address Default —192.168.15.1 Example: <Local_IP>192.168.15.1</Local_IP> |
| <Subnet_Mask> | Description —The subnet mask for the local network User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Subnet Mask field Values —Class C subnet mask 255.255.255.0 255.255.255.128 255.255.255.192 255.255.255.224 255.255.255.240 255.255.255.248 255.255.255.252 Default —255.255.255.0 Example: <Subnet_Mask>255.255.255.0</Subnet_Mask> |
| <DHCP_Client_Table> | Description —Clients with reserved IPv4 addresses User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, IP Reservation list (available after clicking the Show DHCP Reservation button) Values —Semi-colon separated list of client information in the following order: <MAC address> <ip_address> on <client_name> Default —null Example: <DHCP_Client_Table>58:8D:09:72:73:DA 192.168.15.100 on Computer-1;00:22:68:19:EF:83 192.168.15.101 on Computer-2;</DHCP_Client_Table> |
| <Option_66> | Description —Method for specifying a TFTP server for remote configuration of the ATA User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 66 field Values 0: None 2: Remote TFTP Server 3: Manual TFTP Server Default —0 Example —Remote TFTP server <Option_66>2</Option_66> |
| <TFTP_IP> | Description —IPv4 address of a TFTP server, if Option 66 is set to Manual User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, TFTP Server field Values —IPv4 address Default —0.0.0.0 Example <TFTP_IP>209.165.202.129</TFTP_IP> |
| <Option_67> | Description —Provides a configuration/bootstrap filename to hosts that request this option User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 67 field Values —filename Default —null Example <Option_67>MyDirectory/MyFile.cfg</Option_67> |
| <Option_159 > | Description —Provides a configuration URL to hosts that request this option User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 159 field Values —URL Default —null Example <Option_159>http://MyDomain.com/MyDirectory/MyFile.cfg></Option_159> |
| <Option_160 > | Description —Provides a configuration URL to hosts that request this option User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Option 160 field Values —filename Default —null Example <Option_67>MyDirectory/MyFile.cfg</Option_67> |
| <DNS_Proxy> | Description —Enables or disables the DNS proxy, which relays DNS requests to the current public network DNS server for the proxy, and
                                             replies as a DNS resolver to the client device on the network User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, DNS Proxy field Values 0: Disabled 1: Enabled Default —1 Example —DNS proxy enabled <DNS_Proxy>1</DNS_Proxy> |
| <Starting_IP> | Description —The first IPv4 address in the range of IPv4 addresses that are assigned by the DHCP server User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Starting IP address field Values —IPv4 address Default —192.168.15.100 Example <Starting_IP>192.168.15.110</Starting_IP> |
| <Max_DHCP_User> | Description —The maximum number of devices that can receive DHCP addresses from the DHCP server User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Maximum DHCP Users field Values —number Default —50 Example —10-device maximum <Max_DHCP_User>10</Max_DHCP_User> |
| <Client_Lease_Time> | Description —The number of minutes that a dynamically assigned IPv4 address can be in use, or "leased" User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Client Lease Time field Values —number. Enter the number of minutes. Enter 0 to represent 1 day. Enter 9999 to never expire. Default —0 (1 day) Example —No expiration <Client_Lease_Time>9999</Client_Lease_Time> |
| <Static_DNS> | Description —Defines a DNS server address that will be provided to DHCP clients. If DNS Proxy is enabled, clients will automatically be
                                             issued the Local IPv4 address to use for DNS. User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Static DNS field Values —IPv4 address Default —0.0.0.0 Example <Static_DNS>209.165.202.129</Static_DNS> |
| <Default_Gateway> | Description —Enter the IPv4 address of the default gateway to be used by the DHCP clients. User Interface — Network Setup > Basic Setup > IPv4 LAN Settings page, Default Gateway field Default —192.168.15.1 Example <Default_Gateway>192.168.15.1</Default_Gateway> |

| Parameter | Details |
|---|---|
| LAN_IP6_Address_Assign_Type | Description —Method for IPv6 assignment to LAN device.. User Interface — Network Setup > IPv6 LAN Settings page, Address Assign Type field Values 0: SLACC 1: DHCP6s Default —0 |
| LAN_DHCP6_Delegation_Enable | Description —Set enabled to support DHCPv6 delegation which support to obtain LAN prefix via DHCPv6 client User Interface — Network Setup > IPv6 LAN Settings page, DHCPv6 Delegation field. Values 0: Disabled 1: Enabled Default —0 |
| LAN_IP6_Prefix | Description —Manual LAN prefix, editable only when DHCP delegation is disabled. User Interface — Network Setup > IPv6 LAN Settings page, IPv6 Address Prefix field. Values —0-64 Default —null |

| Parameter | Details |
|---|---|
| <WAN_VLAN_Enable> | Description —Enables or disables a VLAN on your network User Interface — Network Setup > Advanced Settings > VLAN page, Enable VLAN field Valid inputs 0: Disabled 1: Enabled Default —0 Example —VLAN enabled <WAN_VLAN_Enable>1</WAN_VLAN_Enable> |
| <WAN_VLAN_ID> | Description —A number that identifies the VLAN User Interface — Network Setup > Advanced Settings > VLAN page, VLAN ID field Valid inputs —1~4094 Default —1 Example —VLAN ID 100 <WAN_VALN_ID>100</WAN_VALN_ID> |

| Parameter | Details |
|---|---|
| <CDP_ENABLE> | Description —Enables or disables Cisco Discovery Protocol (CDP) User Interface — Network Setup > Advanced Settings > CDP & LLDP page, Enable CDP field Valid inputs 0 1 0 means that the CDP is disabled. 1 means that the CDP is enabled. Default —1 Example —CDP enabled <CDP_ENABLE>1</CDP_ENABLE> |
| <LLDP_ENABLE> | Description —Enables or disables Link Layer Discovery Protocol (LLDP) User Interface — Network Setup > Advanced Settings > CDP & LLDP page, Enable LLDP-MED field Valid inputs 0 1 0 means that the LLDP is disabled. 1 means that the LLDP is enabled. Default —1 Example —LLDP enabled <LLDP_ENABLE>1</LLDP_ENABLE> |
| <LAYER2_LOGGING_ENABLE> | Description —Enables Layer 2 logging, which is used by CDP and LLDP for debugging purposes User Interface — Network Setup > Advanced Settings > CDP & LLDP page, Layer 2 Logging field Valid inputs 0: Disabled 1: Enabled Default —0 Example —Layer 2 logging enabled <LAYER2_LOGGING_ENABLE>1</LAYER2_LOGGING_ENABLE> |

| Parameter | Details |
|---|---|
| Single_Port_Forwarding_Index | Description —Index for single port forwarding. Should be listed in order with colon depending on the amount of entry added (Rule<index>).
                                          Index in order 0-9 User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Tupe page, Single Port Forwarding field Values : 0: Disabled 1: Enabled Default —null Example <Single_Port_Forwarding>
<Single_Port_Forwarding_Index>0:1:2</Single_Port_Forwarding_Index>
<Rule0>1:SNMP:br1:161:161:udp:192.168.15.30</Rule0>
<Rule1>0:Finger:br1:79:79:tcp:192.168.15.30</Rule1>
<Rule2>1:forward_rule:br1:25:27:both:192.168.15.15</Rule2>
</Single_Port_Forwarding> |
| Rule<index> | Description —Forwards traffic for a specified port to the same or an alternative port on the target server in the LAN. <index> can be
                                          0-9 User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Tupe page, Single Port Forwarding field. Format : <Enabled>:<Name>:<Interface>:<External Port>:<Internal Port>:<Protocol>:<Target server IP> Values <Enabled>: 0-1 <Name>: String <Interface>: br1 <External Port>: 1-65535 <Internal Port>: 1-65535 <Protocol>: tcp,udp,both <Target server IP>: ipv4 address Default —null Example <Rule0>1:SNMP:br1:161:161:udp:192.168.15.30</Rule0>
<Rule1>0:Finger:br1:79:79:tcp:192.168.15.30</Rule1>
<Rule2>1:forward_rule:br1:25:27:both:192.168.15.15</Rule2> |

| Parameter | Details |
|---|---|
| Port_Range_Forwarding_Index | Description —Index for port range forwarding. Should be listed in order with colon depending on the amount of entry added (Rule<index>). User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Type page, Port Range Forwarding field Values : index in order: 0-9 Default —Null Example <Port_Range_Forwarding>
<Port_Range_Forwarding_Index>0:1</Port_Range_Forwarding_Index>
<Rule0>1:Rule_0:br1:50:60:tcp:192.198.15.22</Rule0>
<Rule1>0:Rule_1:br1:11:13:both:192.168.15.12</Rule1>
</Port_Range_Forwarding> |
| Rule<index> | Description —Forwards traffic to a range of ports to the same ports on the target server in the LAN. <index> can be 0-9. User Interface — Network Setup > Application > Port Forwarding > Add Entry > Port Forwarding Type page, Port Range Forwarding field. Format : <Enabled>:<Name>:<Interface>:<Start Port>:<End Port>:<Protocol>:<Target server IP> Values <Enabled>: 0-1 <Name>: String <Interface>: br1 <Start Port>: 1-65535 <End Port>: 1-65535 <Protocol>: tcp,udp,both <Target server IP>: ipv4 address Default —null Example <Rule0>1:Rule_0:br1:50:60:tcp:192.198.15.22</Rule0>
<Rule1>0:Rule_1:br1:11:13:both:192.168.15.12</Rule1> |

| Parameter | Details |
|---|---|
| <SNMP_Enabled> | Description —Enables or disables SNMP User Interface — Administration > Management > SNMP page, SNMP section, Enabled and Disabled options Valid inputs 0: Disabled 1: Enabled Default —0 Example —SNMP enabled <SNMP_Enabled>1</SNMP_Enabled> |
| <SNMP_Trusted_IP> | Description —trusted v4 IP address that can access the ATA through SNMP User Interface — Administration > Management > SNMP page, SNMP section, Trusted IP field Valid inputs —IPv4 address and subnet mask in this order: 0.0.0.0/0.0.0.0 Default —0.0.0.0/0.0.0.0 (Any IP address) Example <SNMP_Trusted_IP>209.165.202.129/255.255.255.0</SNMP_Trusted_IP> |
| SNMP_Trusted_IP6 | Description —trusted v4 IP address that can access the ATA through SNMP User Interface — Administration > SNMP page, Trusted IPv6 field Valid inputs —IPv6 address Default —:: |
| SNMP_Trusted_IP6_Prefix_Length | Description —prefix of the trusted v6 IP that can access the ATA through SNMP User Interface — Administration > SNMP page, Trusted IPv6 field Valid inputs —0-128 Default —0 |
| <Get_Community> | Description —A community string for authentication for SNMP GET commands. User Interface —— Administration > Management > SNMP page, SNMP section, Get/Trap Community field Valid inputs —string Default —public Example <Get_Community>MyGet</Get_Community> |
| <Set_Community> | Description —A community string for authentication for SNMP GET commands. User Interface — Administration > Management > SNMP page, SNMP section, Set Community field Valid inputs —string Default —private Example <Set_Community>MySet</Set_Community> |
| <SNMPV3> | User Interface — Administration > Management > SNMP page, SNMPV3 section, Enable and Disable fields Valid inputs 0: Disabled 1: Enabled Default —0 Example —SNMPv3 enabled <SNMPV3>1</SNMPV3> |
| <RW_User> | Description —A username for SNMP authentication User Interface — Administration > Management > SNMP page, SNMPV3 section, R/W User field Valid inputs —username Default —v3rwuser Example <RW_User>MyUsername</RW_User> |
| <Auth_Protocol> | Description —SNMPv3 authentication protocol User Interface — Administration > Management > SNMP page, SNMPV3 section, Auth-Protocol field Valid inputs MD5 SHA SHA256 SHA512 Default —MD5 Example—SHA enabled <Auth_Protocol>SHA</Auth_Protocol> |
| <Auth_Password> | Description —Password for SNMPv3 authentication User Interface — Administration > Management > SNMP page, Auth-Password field for SNMPv3 Valid inputs —string Default —1111111111 Example <Auth_Password>MyPassword</Auth_Password> |
| <Privacy_Protocol> | Description —Privacy authentication protocol for SNMPv3 User Interface — Administration > Management > SNMP page, SNMPV3 section, privprotocol field Valid inputs None DES Default —DES Example —DES enabled <Privacy_Protocol>DES</Privacy_Protocol> |
| <Privacy_Password> | Description —Privacy authentication password for SNMPv3 User Interface — Administration > Management > SNMP page, SNMPV3 section, Privacy Password field Valid inputs —string Default —1111111111 Example <Privacy_Password>MyPrivacyPassword</Privacy_Password> |
| <TRAP_IP_Address> | Description —The IP Address of the SNMP manager or trap agent User Interface — Administration > Management > SNMP page, Trap Configuration section, IP Address field Valid inputs —IPv4 address Default —192.168.15.100 Example <TRAP_IP_Address>209.165.202.129</TRAP_IP_Address> |
| <TRAP_Port> | Description —The SNMP trap port used by the SNMP manager or trap agent to receive the trap messages User Interface — Administration > Management > SNMP page, Trap Configuration section, Port field Valid inputs —162 or 1025~65535 Default —162 Example <TRAP_Port>162</TRAP_Port> |
| <TRAP_SNMP_Version> | Description —The SNMP version in use by the SNMP manager or trap agent User Interface — Administration > Management > SNMP page, Trap Configuration section, SNMP Version field Valid inputs —One of the SNMP version number listed below v1 v2c v3 Default —v1 Example <TRAP_SNMP_Version>v3</TRAP_SNMP_Version> |

| Parameter | Details |
|---|---|
| <Time_Zone> | Description —The time zone for the site where the ATA is in operation User Interface — Network Setup > Basic Setup > Time Settings page, Time Zone field Valid inputs —number identifying the time zone. See Time Zone Settings Default —08 1 1 Example —Germany <Time_Zone>+01 2 2</Time_Zone> |
| <Auto_Adjust_Clock> | Description —Enables or disables automatic time adjustments for daylight savings time User Interface — Network Setup > Basic Setup > Time Settings page, Adjust Clock for Daylight Saving Changes field Valid inputs 0: Disabled 1: Enabled Default —1 Example —Automatic Daylight Saving adjustment enabled <Auto_Adjust_Clock>1</Auto_Adjust_Clock> |
| <Daylight_Saving_Time_Rule> | Description —The method for specifying a time to start and end the daylight saving time User Interface — Network Setup > Basic Setup > Time Settings page, Daylight Saving Time Rule field Valid inputs — start=month/day/weekday/hh:mm:ss;end=month/day/weekday/hh:mm:ss;save=hours Default —blank Example —start=3/-1/7/2;end=11/-1/7/2;save=1 Note If you've configured this value and enabled <Auto_Adjust_Clock>, the <Daylight_Saving_Time_Rule> takes precedence. | Note | If you've configured this value and enabled <Auto_Adjust_Clock>, the <Daylight_Saving_Time_Rule> takes precedence. |
| Note | If you've configured this value and enabled <Auto_Adjust_Clock>, the <Daylight_Saving_Time_Rule> takes precedence. |
| <Time_Server_Mode> | Description —The method for specifying an NTP time server Time Server Address User Interface — Network Setup > Basic Setup > Time Settings page, Time Server field Valid inputs manual auto Default —auto Example —Manual mode <Time_Server_Mode>manual</Time_Server_Mode> |
| <Time_Server> | Description —IPv4 address or domain name of an NTP server User Interface— Network Setup > Basic Setup > Time Settings page, Time Server Address field Valid inputs —IPv4 address or domain name Default —0.ciscosb.pool.ntp.org Example —European pool <Time_Server>server 0.europe.pool.ntp.org </Time_Server> |
| <Resync_Timer> | Description —The interval, in seconds, at which the ATA resynchronizes with the NTP server User Interface — Network Setup > Basic Setup > Time Settings page, Resync Timer field Valid inputs —number Default —3600 Example <Resync_Timer>3600</Resync_Timer> |
| <Auto_Recovery_System_Time> | Description —When enabled, allows the ATA to automatically reconnect to the time server after a system reboot User Interface — Network Setup > Basic Setup > Time Settings page, Auto Recovery After System Reboot field Valid inputs 0: Disabled 1: Enabled Default —0 Example —Auto Recovery enabled <Auto_Recovery_System_Time>1</Auto_Recovery_System_Time> |
| <Time_Mode> | Description —The method of specifying a time server User Interface — Network Setup > Basic Setup > Time Settings page, Time Server field Valid inputs 0: Manual 1: Auto Default —1 Example —Automatic mode <Time_Mode>1</Time_Mode> |

| Note | If you've configured this value and enabled <Auto_Adjust_Clock>, the <Daylight_Saving_Time_Rule> takes precedence. |
|---|---|

| Parameter | Details |
|---|---|
| <QoS_Always_ON> | Description —Determines whether QoS settings are enabled at all times or only when there is voice traffic User Interface — Network Setup > Application > QoS page, QoS Policy field Valid inputs 0: On When Phone In Use 1: Always On Default —0 Example —On when phone is in use <QoS_Always_ON>0</QoS_Always_ON> |
| <Upstream_Bandwidth> | Description —The maximum available upstream bandwidth, in kbps, as specified by the Internet Service Provider User Interface — Network Setup > Application > QoS page, Upstream Bandwidth field Valid inputs —number Default —10000 Example <Upstream_Bandwidth>20000</Upstream_Bandwidth> |

| Parameter | Details |
|---|---|
| <Proxy_Mode> | Description —Specifies the HTTP proxy mode that the ATA uses, or disables the HTTP proxy feature. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Mode field. Valid inputs Off Auto Manual Default —Off Example —Auto proxy mode <Proxy_Mode>Auto</Proxy_Mode> |
| <Use_Auto_Discovery__WPAD_> | Description —Determines whether the ATA uses the Web Proxy Auto-Discovery (WPAD) protocol to retrieve a PAC file. If the parameter is set to No, you must configure the parameter <PAC_URL> . The parameter configuration takes effect only when the <Proxy_Mode> is set to Auto. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Use Auto Discovery field. Valid inputs No Yes Default —Yes Example —The WPAD protocol is not used. <Use_Auto_Discovery__WPAD_>No</Use_Auto_Discovery__WPAD_> |
| <PAC_URL> | Description —The URL of a Proxy Auto-Configuration (PAC) file. This parameter configuration takes effect when the <Proxy_Mode> is set to Auto and <Use_Auto_Discovery__WPAD_> is set to No. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, PAC URL field. Valid inputs— URL Default —null Example http://proxy.department.branch.example.com |
| <Proxy_Server_Requires_Authentication> | Description —Select the option according to the actual behaviour of the proxy server. If the proxy server requires the user to provide
                                          authentication credentials, set it to Yes. Otherwise, select it to No. If the parameter is set to Yes, you must further configure the parameters <Proxy_Username> and <Proxy_Password> . User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Server Requires Authentication field. Valid inputs No Yes Default —No Example —The proxy server requires the user authentication. <Proxy_Server_Requires_Authentication>1</Proxy_Server_Requires_Authentication> |
| <Proxy_Host> | Description —Specifies an IP address or hostname of the proxy host server that the ATA uses. The parameter configuration is required if the <Proxy_Mode> is set to Manual. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Host field. Valid inputs —A valid IP address or hostname of the proxy host server Default —null Example <Proxy_Host>proxy.example.com</Proxy_Host> |
| <Proxy_Port> | Description —Specifies a port number of the proxy host server that the ATA uses. The parameter configuration is required if the <Proxy_Mode> is set to Manual. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Proxy Port field. Valid inputs —A valid port number from 2 to 65535. Default —3128 Example <Proxy_Port>3128</Proxy_Port> |
| <Proxy_Username> | Description —Enter a username for the authentication purpose of the proxy server. The parameter configuration is required when <Proxy_Mode> is set to Manual and <Proxy_Server_Requires_Authentication> is set to Yes. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Username field. Valid inputs —string Default —null Example <Proxy_Username>Example</Proxy_Username> |
| <Proxy_Password> | Description —Enter the password of the specified username that the proxy server requires. The parameter configuration is required when <Proxy_Mode> is set to Manual and <Proxy_Server_Requires_Authentication> is set to Yes. User Interface — Administration > Network Setup > Applications > HTTP Proxy page, Password field. Valid inputs —string Default —null Example <Proxy_Password>Example</Proxy_Password> |

| Parameter | Details |
|---|---|
| <Status> | Description —Enables or disables exposing a local device to the Internet for a special purpose service User Interface — Network Setup > Application > DMZ page, Status field Valid inputs 0: Disabled 1: Enabled Default —0 Example —DMZ enabled <Status>1</Status> |
| <Private_IP> | Description —The local IPv4 address of the device that can be accessed through the DMZ User Interface — Network Setup > Application > DMZ page, Private IP field Valid inputs —IPv4 address Default —0.0.0.0 Example <Private_IP>192.168.15.1</Private_IP> |
| <Rule_Number> | Description —A static setting used to define the DMZ rule User Interface —not applicable Valid inputs —1 (do not change this number) Default —1 |

| Parameter | Details |
|---|---|
| <Bonjour_Enable> | Description —Enables or disables the Bonjour service discovery protocol, which may be required by network management systems that you
                                          use User Interface — Administration > Management > Bonjour page, Enabled and Disabled fields Valid inputs 0: Disabled 1: Enabled Default —1 Example —Bonjour enabled <Bonjour_Enable>1</Bonjour_Enable> |

| Note | No other settings are nested below <Reset_Button_Enable>. |
|---|---|

| Parameter | Details |
|---|---|
| <Reset_Button_Enable> | Description —Enables or disables the RESET button User Interface Valid inputs 0: Disabled (button) 1: Enabled (button can be pressed for 1-2 seconds for reboot and 5-6 seconds for a factory reset) Default —1 Example —Button disabled <Reset_Button_Enable>0</<Reset_Button_Enable> |

| Parameter | Details |
|---|---|
| <Router_Mode> | Description —The operating mode of the router User Interface — Network Setup > Basic Setup > Network Service page, Networking Service field Valid inputs 0: Bridge 1: NAT Default —1 Example —Bridge mode enabled <Router_Mode>0<Router_Mode> |

| Parameter | Details |
|---|---|
| Monitor_WAN_Port_Only | Description —To monitor device link status base on wan port only. This configuration is only valid when <Router_Mode> is set to 0 (bridge). User Interface — Network Setup > Basic Setup > Network Service page, Monitor Network Drop on Internet Port only field Values 0: Off 1: On Default —0 |

| Parameter | Details |
|---|---|
| <IPSec_Passthrough> | Description —Enables or disables VPN passthrough for Internet Protocol Security (IPsec) User Interface — Network Setup > Advanced Settings > VPN Passthrough page, IPsec Passthrough field Valid inputs 0: Disabled 1: Enabled Default —1 Example <IPSec_Passthrough>1</IPSec_Passthrough> |
| <PPTP_Passthrough> | Description —Enables or disables VPN passthrough for Point-to-Point Tunneling Protocol (PPTP) User Interface — Network Setup > Advanced Settings > VPN Passthrough page, PPTP Passthrough field Valid inputs 0: Disabled 1: Enabled Default —1 Example <PPTP_Passthrough>1</PPTP_Passthrough> |
| <L2TP_Passthrough> | Description —Enables or disables VPN passthrough for Layer 2 Tunneling Protocol (L2TP) User Interface — Network Setup > Advanced Settings > VPN Passthrough page, L2TP Passthrough field Valid inputs 0: Disabled 1: Enabled Default —1 Example <L2TP_Passthrough>1</L2TP_Passthrough> |

| Parameter | Details |
|---|---|
| <Web_Utility_Access_HTTP> | Description —Enables or disables access to the web-based configuration utility via HTTP, from a computer on the LAN User Interface — Administration > Management > Web Access Management page, Web Utility Access field, HTTP option Valid inputs 0: Disabled 1: Enabled Default —0 Example <Web_Utility_Access_HTTP>1</Web_Utility_Access_HTTP> |
| <Web_Utility_Access_HTTPS> | Description —Enables or disables access to the web-based configuration utility via HTTPS, from a computer on the LAN User Interface — Administration > Management > Web Access Management page, Web Utility Access field, HTTPS option Valid inputs 0: Disabled 1: Enabled Default —1 Example <Web_Utility_Access_HTTPS>1</Web_Utility_Access_HTTPS> |
| <Web_Remote_Management> | Description —Enables or disables access to the web-based configuration utility through the WAN interface (INTERNET port) User Interface — Administration > Management > Web Access Management page, Remote Management field Valid inputs 0: Disabled 1: Enabled Default —0 Example <Web_Remote_Management>1</Web_Remote_Management> |
| <Remote_Web_Utility_Access> | Description —Specifies the protocol that can be used to access the web-based configuration utility through the WAN interface (INTERNET
                                          port), when Remote Management is enabled User Interface — Administration > Management > Web Access Management page, Web Utility Access field Valid inputs 0: HTTP 1: HTTPS Default —1 Example <Remote_Web_Utility_Access>1</Remote_Web_Utility_Access> |
| <Web_Remote_Upgrade> | Description —Enables or disables upgrading the firmware from a computer on the WAN, when Remote Management is enabled User Interface — Administration > Management > Web Access Management page, Remote Upgrade field Valid inputs 0: Disabled 1: Enabled Default —0 Example <Web_Remote_Upgrade>1</Web_Remote_Upgrade> |
| <Allowed_Remote_IP_Type> | Description —Specifies a method for identifying remote devices that are allowed access to the web-based configuration utility, when Remote
                                          Management is enabled User Interface — Administration > Management > Web Access Management page, Allowed Remote IPv4 Address field, Any IP Address option Valid inputs : 0: Specified IP Address 1: Any IP Address Default —1 Example <Allowed_Remote_IP_Type>0</Allowed_Remote_IP_Type> |
| <Allowed_Remote_IP_Address> | Description —Specifies a remote IPv4 address that is allowed access to the web-based configuration utility, when Remote Management is
                                          enabled User Interface — Administration > Management > Web Access Management page, Allowed Remote IPv4 Address field, unlabeled text box Valid inputs —IPv4 address Default —0.0.0.0 Example <Allowed_Remote_IP_Address>209.165.201.129</Allowed_Remote_IP_Address> |
| <Remote_Management_Port> | Description —Specifies the port to use for access to the web-based configuration utility through the WAN interface (INTERNET port) User Interface — Administration > Management > Web Access Management page, Remote Management Port field Valid inputs —port number Default —443 Example <Remote_Management_Port>443</Remote_Management_Port> |

| Parameter | Details |
|---|---|
| <TR_069_Status> | Description —Enables or disables remote provisioning via TR-069 CPE WAN Management Protocol User Interface —Administration > Management > TR-069 page, Status field Valid inputs 0: Disabled 1: Enabled Default —0 Example <TR_069_Status>1</TR_069_Status> |
| <TR_069_ACS_URL> | Description —The URL of the Auto-Configuration Server (ACS) User Interface —Administration > Management > TR-069 page, ACS URL field Valid inputs —Domain name or IP address, starting with http:// or https://, and optionally ending with a port number Default —null Example <TR_069_ACS_URL>http://ACS-example.com</TR_069_ACS_URL> |
| <TR_069_ACS_Username> | Description —The username for HTTP-based authentication to the ACS User Interface —Administration > Management > TR-069 page, ACS Username field Valid inputs —username Default —null Example <TR_069_ACS_Username>MyUsername</TR_069_ACS_Username> |
| <TR_069_ACS_Password> | Description —The password for HTTP-based authentication to the ACS User Interface —Administration > Management > TR-069 page, ACS Password field Valid inputs —password Default —commented out: <!-- <TR_069_ACS_Password></TR_069_ACS_Password> --> Example <TR_069_ACS_Password>MyACSPassword</TR_069_ACS_Password> |
| <TR_069_Connection_Request_URL> | Description —This field will be autofilled and does not need to be entered manually User Interface —Administration > Management > TR-069 page, Connection Request URL field Valid inputs —URL Default —null Example —not applicable, value is autofilled |
| <TR_069_Connection_Request_Username> | Description —This field will be autofilled and does not need to be entered manually User Interface —Administration > Management > TR-069 page, Connection Request Username field Valid inputs —username Default —null Example —not applicable, value is autofilled |
| <TR_069_Connection_Request_Password> | Description —This field will be autofilled and does not need to be entered manually User Interface —Administration > Management > TR-069 page, Connection Request Password field Valid inputs —password Default —commented out, <!--<TR_069_Connection_Request_Password></TR_069_Connection_Request_Password>--> Example <TR_069_Connection_Request_Password> MyPassword</TR_069_Connection_Request_Password> |
| <TR_069_Periodic_Inform_Interval> | Description —When Periodic Information is enabled, the duration, in seconds, between CPE attempts to connect to the ACS User Interface —Administration > Management > TR-069 page, Periodic Inform Interval field Valid inputs —number Default —86400 Example —Interval of 36000 seconds (10 minutes) <TR_069_Periodic_Inform_Interval>36000</TR_069_Periodic_Inform_Interval> |
| <TR_069_Periodic_Inform_Enable> | Description —Enables or disables CPE connection requests to the ACS User Interface —Administration > Management > TR-069 page, Periodic Inform Enable field Valid inputs — 0: Disabled 1: Enabled Default —1 Example —Periodic Inform enabled <TR_069_Periodic_Inform_Enable>1</TR_069_Periodic_Inform_Enable> |

| Parameter | Details |
|---|---|
| <Log_Module> | Description —Value that indicates the debug flag of modules: 0: Default 1: Preset 2: Telephony 3: SIP 4: UI 5: Network 6: Media 7: System 8: Web 9: NTP 10: CDP/LLDP 11: Security 12: CSSD_RTP 13: CSSD_FAX 14: CSSD_ANY User Interface — Administration > Debug Log Module page, Debug Log Module field Valid inputs —0-14 Default —0 |
| <RAM_Log_Size> | Description —The maximum size of the log file in kilobytes User Interface — Administration > Debug Log Setting page, Debug Log Size field Valid inputs —number from 128~1024 Default —200 Example <RAM_Log_Size>200</RAM_Log_Size> |
| Syslog_Server_IP | Description —IPv4 address of debug log server User Interface — Administration > Debug Log Setting page, Pv4 Address field Valid inputs —Valid IPv4 address format Default —null |
| Syslog_Server_IP6 | Description —IPv6 address of debug log server User Interface — Administration > Debug Log Setting page, Pv6 Address field Valid inputs —Valid IPv6 address format Default —null |
| Syslog_Server_Port | Description —debug log server port User Interface — Administration > Debug Log Setting page, Port field Valid inputs —0-65535 Default —514 |
| Event_Log_Server | Description —Address of event log server, supports IPv4, IPv6, and FQDN User Interface — Administration > Debug Log Setting page, Address field Valid inputs —Valid IPv4, IPv6, or FQDN address format. Maximum length is 128 characters Default —null |
| Event_Log_Port | Description —Port of event log server User Interface — Administration > Debug Log Setting page, Port field Valid inputs —0-65535 Default —514 |
| Event_Log_Flag | Description —An bitwise value to turn on/off report of each event category (<DEV>: 1, <SYS>: 2 <CFG>: 4, <REG>: 8) User Interface — Administration > Debug Log Setting page, Flag field Valid inputs —0-65535 The available options are: 0: Disable 1: DEV 2: SYS 4: CFG 8: REG 15: DEV+SYS+CFG+REG Default —15 |
| PRT_Upload_Url | Description —Address of PRT upload server User Interface — Administration > Debug Log Setting page, PRT Upload URL field Valid inputs —Valid URL format. Maximum length is 256 characters. Default —null |
| PRT_Upload_Method | Description —HTTP method to upload PRT User Interface — Administration > Debug Log Setting page, Debug Log Size field Valid inputs 0: POST 1: PUT) Default —0 |
| PRT_Max_Timer | Description —Value in minutes to specify interval of periodical PRT report. User Interface — Administration > Debug Log Setting page, PRT Max Timer field Valid inputs 0: Disable 15-1440 Default —0 |

| Parameter | Details |
|---|---|
| <Web_Login_Admin_Name> | Description —The username for the administrator login, which has full read-write access to all parameters User Interface — Administration > Management > User List page, Username field Valid inputs —username Default —admin |

| Parameter | Details |
|---|---|
| <Web_Login_Admin_Password> | Description—The password for the administrator login User Interface — Administration > Management > User List page Valid inputs —password (the minimum length of the characters is 8) Default —commented out <!--<Web_Login_Admin_Password></Web_Login_Admin_Password>--> Example <Web_Login_Admin_Password>MyPassword</Web_Login_Admin_Password> |

| Parameter | Details |
|---|---|
| <Web_Login_Guest_Name> | Description —The username for the guest login, which has limited access to view or change parameters User Interface — Administration > Management > User List page Valid inputs —username Default —cisco Example <Web_Login_Guest_Name>MyUsername</Web_Login_Guest_Name> |

| Parameter | Details |
|---|---|
| <Web_Login_Guest_Password> | User Interface — Administration > Management > User List Page Valid inputs —password (the minimum length of the characters is 8) Default —commented out, Example — <Web_Login_Guest_Password>MyPassword</Web_Login_Guest_Password> |

| Parameter | Details |
|---|---|
| SSH_ACCESS | Description —Set enabled to allow access to SSH service. User Interface — Administration > SSH page, Access field Values 0: Disabled 1: Enabled Default —0 |
| SSH_User_ID | Description —User name of SSH User Interface — Administration > SSH page, User Name field Values —0-50 Default —null |
| SSH_Password | Description —Password of SSH. User Interface — Administration > SSH page, Password field Values —0-50 Default —null |