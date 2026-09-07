---
doc_id: help-webex-com-en-us-article-36bjkdb-f90b67ed35
source_url: https://help.webex.com/en-us/article/36bjkdb
retrieved_at: 2026-09-07T13:03:56.987132+00:00
---

## Change the Internet protocol mode

If required, you may need to change the internet protocol mode on which the phone operates.

Press Settings .

Navigate to Network and service > Network settings > IP stack .

In the IP stack section, select one of the following internet protocol modes:

- IPv4 and IPv6

- IPv4

- IPv6

Select Apply .

## Change the IP address on your phone

As your network settings require, you may need to change or manually assign the IP address to your phone. You can set or change the IP address on your phone from the network connection menu.

Your phone supports IP version 4 (IPv4), IP version 6 (IPv6), and IPv4 and IPv6. IPv4 and IPv6 is the default setting. The IP parameters can be assigned automatically by the network, or you can set them manually.

Follow the steps in the following sections as needed to change your IPv4 or IPv6 address.

The available options in the settings vary with the network settings in your organization.

- Change IPv4 settings

- Change IPv6 settings

Follow these steps to change or set your IPv4 network.

If your network supports both IPv4 and IPv6, you may also need to set the IPv6 settings. For how to change IPv6 settings, see Change IPv6 settings .

Parameters

Options

Default

Description

DHCP

On

Off

On

Enable or disable DHCP on your phone.

Enable DHCP to allow your phone to get an IP address from the DHCP server. Otherwise, disable DHCP and manually assign an IP address to your phone.

On

Off

Off

Available only when DHCP is enabled.

To release the IP address that DHCP assigned for reassignment, turn on this switch. Otherwise, turn it Off.

On

Off

Available only when DHCP is enabled.

This parameter is only available on the phones registered to Unified CM.

Indicates whether the phone is using an alternate TFTP server.

IP address

IPv4 address

Available only when DHCP is disabled.

You must assign an IP address to the phone when DHCP is disabled. If you assign an IP address with this option, you must also assign a subnet mask and default router (gateway).

Subnet mask

Available only when DHCP is disabled.

You must specify the subset mask used by the phone when DHCP is disabled.

Available only when DHCP is disabled.

Identify the default router for the phone to use when DHCP is disabled.

IPv4 DNS address 1

Identify the primary Domain Name System (DNS) server that the phone uses.

Available only when DHCP is disabled.

Identify the secondary Domain Name System (DNS) server that the phone uses.

Available only when DHCP is disabled.

Identify the optional backup Domain Name System (DNS) server that the phone uses.

This parameter is only available on the phones registered to Unified CM.

Available only when DHCP is disabled.

Available only when Alternate TFTP is enabled.

This parameter is only available on the phones registered to Unified CM.

Primary Trivial File Transfer Protocol (TFTP) server that the phone uses. If you are not using DHCP in your network and you want to change this server, you must use the TFTP Server 1 option.

If Alternate TFTP is enabled, enter a non-zero value for the TFTP Server 1 option.

If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock the file before you can save changes to the TFTP Server 1 option. In this case, the phone deletes the file when you save changes to the TFTP Server 1 option. A new CTL or ITL file downloads from the new TFTP Server 1 address.

When the phone looks for the TFTP server, the phone gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in this order:

Any manually assigned IPv4 TFTP servers

Any manually assigned IPv6 servers

DHCP assigned TFTP servers

DHCPv6 assigned TFTP servers

Available only when Alternate TFTP is enabled.

This parameter is only available on the phones registered to Unified CM.

Optional backup TFTP server that the phone uses if the primary TFTP server is unavailable.

If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock either of the files before you can save changes to the TFTP Server 2 option. In this case, the phone deletes either of the files when you save changes to the TFTP Server 2 option. A new CTL or ITL file downloads from the new TFTP Server 2 address.

If you forget to unlock the CTL or ITL file, you can change the TFTP Server 2 address in either file, then erase them by pressing Erase from the Security Configuration menu. A new CTL or ITL file downloads from the new TFTP Server 2 address.

When the phone looks for the TFTP server, it gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in the following order:

Any manually assigned IPv4 TFTP servers

Any manually assigned IPv6 servers

DHCP assigned TFTP servers

DHCPv6 assigned TFTP servers

Specify the DHCPv4 options that can deliver configuration parameters from a DHCP server to the phone.

This parameter is only available on the phone registered to Webex Calling or BroadWorks.

Press Settings .

Navigate to Network and service > Network settings > IPv4 settings .

In the IPv4 settings screen, configure the settings as needed.

Select Apply when done.

The phone restarts to apply the changes.

You can change the IPv6 settings when your phone's IP stack is set to IPv6 or IPv4 and IPv6 .

Parameters

Options

Default

Description

DHCPv6

On

Off

On

Enable or disable DHCP on your phone.

Enable DHCP to allow your phone to get an IP address from the DHCP server. Otherwise, disable DHCP and manually assign an IP address to your phone.

IPv6 address

Available only when DHCPv6 is disabled.

You must assign an IP address to the phone when DHCP is disabled.

IPv6 prefix length

Available only when DHCPv6 is disabled.

Identify how many bits of a Global Unicast IPv6 Address are there in the network part.

Available only when DHCPv6 is disabled.

Identify the default router for the phone to use when DHCP is disabled.

IPv6 DNS address 1

Identify the primary Domain Name System (DNS) server that the phone uses.

Identify the secondary Domain Name System (DNS) server that the phone uses.

On

Off

Available only when DHCP is enabled.

This parameter is only available on the phones registered to Unified CM.

Indicates whether the phone is using an alternate TFTP server.

Available only when Alternate TFTP is enabled.

This parameter is only available on the phones registered to Unified CM.

Primary Trivial File Transfer Protocol (TFTP) server that the phone uses. If you are not using DHCP in your network and you want to change this server, you must use the TFTP Server 1 option.

If Alternate TFTP is enabled, enter a non-zero value for the TFTP Server 1 option.

If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock the file before you can save changes to the TFTP Server 1 option. In this case, the phone deletes the file when you save changes to the TFTP Server 1 option. A new CTL or ITL file downloads from the new TFTP Server 1 address.

When the phone looks for the TFTP server, the phone gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in this order:

Any manually assigned IPv4 TFTP servers

Any manually assigned IPv6 servers

DHCP assigned TFTP servers

DHCPv6 assigned TFTP servers

Available only when Alternate TFTP is enabled.

This parameter is only available on the phones registered to Unified CM.

Optional backup TFTP server that the phone uses if the primary TFTP server is unavailable.

If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock either of the files before you can save changes to the TFTP Server 2 option. In this case, the phone deletes either of the files when you save changes to the TFTP Server 2 option. A new CTL or ITL file downloads from the new TFTP Server 2 address.

If you forget to unlock the CTL or ITL file, you can change the TFTP Server 2 address in either file, then erase them by pressing Erase from the Security Configuration menu. A new CTL or ITL file downloads from the new TFTP Server 2 address.

When the phone looks for the TFTP server, it gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in the following order:

Any manually assigned IPv4 TFTP servers

Any manually assigned IPv6 servers

DHCP assigned TFTP servers

DHCPv6 assigned TFTP servers

On

Off

Available only when DHCP is enabled.

This parameter is only available on the phones registered to Unified CM.

To release the IP address that DHCP assigned for reassignment, turn on this switch. Otherwise, turn it Off.

Specify the DHCPv6 options that can deliver configuration parameters from a DHCP server to the phone.

This parameter is only available on the phone registered to Webex Calling or BroadWorks.

Press Settings .

Navigate to Network and service > Network settings > IPv6 settings .

In the IPv6 settings screen, configure the settings as needed.

Select Apply when done.

The phone restarts to apply the changes.

## Change VLAN settings on your phone

Determines which Virtual LAN (VLAN) your phone resides in. You phone uses CDP to communicate information such as auxiliary VLAN ID, per port power management details, and Quality of Service (QoS) configuration information with the Cisco Catalyst switch.

Parameters

Options

Default

Description

Admin VLAN ID

Valid values: 0 through 4095

1

Enter a VLAN ID for the IP phone when you use a VLAN without CDP (VLAN enabled, CDP disabled, and LLDP disabled).

Note that only voicepackets are tagged with the VLAN ID. Do not use the 1 value for the VLAN ID. If VLAN ID is 1, you cannot tag voice packets with the VLAN ID.

PC VLAN ID

Valid values: 0 through 4095

1

Enter a value of the VLAN ID that is used to tag communications from the PC port on the phone.

The phone tags all the untagged frames coming from the PC (it does not tag any frames with an existing tag).

Before you begin

Consult your administrator before you make changes to the VLAN settings.

Press Settings .

Navigate to Network and service > Network settings > VLAN .

In the VLAN screen, configure the settings as needed.

Select Apply when done.

The phone restarts to apply the changes.

## Connect to a VPN

- Currently, the VPN connection is only available on the phones registered to Cisco
            Unified CM.

- Cisco Desk Phone 9811 doesn't support VPN.

You can connect to a VPN in one of the following ways:

- With a certificate—If your administrator has installed a certificate on your phone, you can directly enable the VPN connection without a need to set up your phone.

- By entering credentials—Enter a user ID and password, or password only to for the VPN sign-in.

To connect to a VPN on your phone, do the following:

Press Settings

Navigate to Network and service > VPN .

The status for the menu item VPN indicates that whether the VPN connection is turned on or off.

Turn on the VPN connection.

Press On .

Toggle on VPN.

Your phone will try to connect to the VPN. If a required certificate is already installed on the phone, the VPN connection establishes directly. The job is finished, you can skip the following steps. Otherwise, you need to enter user credentials.

When your phone is trying to connect to the VPN, you can cancel the process by selecting Cancel . Then the VPN connection will be back to disabled.

When prompted for the VPN sign-in, enter your user ID and password, or just password, and then select Apply .

Your phone will try to establish the VPN connection. Once successful, you will receive the pop-up message and you can find the VPN icon on the top right corner of the home screen.

(Optional) To change the user credentials for an existing VPN connection, do the following:

Navigate to Network and service > VPN .

Select Credentials .

Enter a valid user ID and password, and then select Apply .

## HTTP proxy settings

HTTP proxy is only available on the phones registered to Webex Calling or BroadWorks.

You can set up an HTTP proxy on your phone or from the phone web page.

During the phone's registration, if the network connection to the server fails, you might be prompted to set up an HTTP proxy server on your phone. The HTTP proxy settings on the phone can still be kept after the phone's registration.

### Set up a proxy server with the auto proxy mode

You can choose the auto proxy mode to set up an HTTP proxy server on the phone.

Press Settings

Navigate to the HTTP proxy settings menu:

Select Network and service > Network settings > HTTP proxy .

Select Network connection > Network settings , and navigate to the HTTP proxy section.

Select the auto proxy mode:

Select Proxy Mode , and then select Auto .

Select Auto in the HTTP proxy section.

(Optional) Turn on Web Proxy Auto Discovery (WPAD) that is used to retrieve a PAC file automatically. By default, your phone uses WPAD in the auto proxy mode.

Highlight Web proxy auto discovery , and select On .

Toggle on Web proxy auto discovery .

If you want to manually enter a Proxy Auto Configuration (PAC) URL, turn off Web proxy auto discovery , and enter a PAC URL in PAC URL . For example:

If you don't have the PAC URL, contact your administrator.

Press Apply to apply the settings.

### Set up a proxy server with the manual proxy mode

You can choose the manual proxy mode to set up an HTTP proxy server on the phone.

Before you begin

Your administrator provides you the server address and port of the proxy server.

Press Settings

Do one of the following actions:

Select Network and service > Network settings > HTTP proxy .

Select Network connection > Network settings , and navigate to the HTTP proxy section.

Select the manual proxy mode:

Select Proxy Mode , and then select Manual .

Select Manual in the HTTP proxy section.

Enter a valid hostname or IP address of a proxy server in Proxy host .

Do not provide the scheme (http:// or https://) for the proxy host.

Enter a valid server port of the specified proxy server in Proxy port .

If the specified proxy server requires user's authentication, turn on Proxy authentication , and enter your username and password to access the proxy server.

If you don't have the username and password, contact your administrator.

Select Apply to apply the settings.

### Set up a proxy server from the phone web page

You can choose the auto or manual proxy mode to set up an HTTP proxy server from the phone web page.

On the phone web page, select Voice > System .

Under the section HTTP Proxy Settings , set the parameters, as described in the above table.

- Proxy Mode : Choose the proxy mode (Auto or Manual) for the HTTP proxy setting. If set to Off (default), the HTTP proxy is disabled. By default, the value is Off.

If the parameter is set to No , you must configure PAC URL .

- PAC URL : URL that locate the PAC file.

- Proxy Host : Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ).

- Proxy Port : Port number of the proxy server. The default port is 3128

If set to Yes , you must configure Username and Password for an authentication on the proxy server.

Click Submit All Changes .

| 1 | Press Settings . |
|---|---|
| 2 | Navigate to Network and service > Network settings > IP stack . |
| 3 | In the IP stack section, select one of the following internet protocol modes: IPv4 and IPv6 IPv4 IPv6 |
| 4 | Select Apply . |

| Parameters | Options | Default | Description |
|---|---|---|---|
| DHCP | On Off | On | Enable or disable DHCP on your phone. Enable DHCP to allow your phone to get an IP address from the DHCP server. Otherwise, disable DHCP and manually assign an IP address to your phone. |
| DHCP address released | On Off | Off | Available only when DHCP is enabled. To release the IP address that DHCP assigned for reassignment, turn on this switch. Otherwise, turn it Off. |
| Alternate TFTP | On Off | Off | Available only when DHCP is enabled. This parameter is only available on the phones registered to Unified CM. Indicates whether the phone is using an alternate TFTP server. |
| IP address IPv4 address |  |  | Available only when DHCP is disabled. You must assign an IP address to the phone when DHCP is disabled. If you assign an IP address with this option, you must also assign a subnet mask and default router (gateway). |
| Subnet mask | off |  | Available only when DHCP is disabled. You must specify the subset mask used by the phone when DHCP is disabled. |
| Gateway |  |  | Available only when DHCP is disabled. Identify the default router for the phone to use when DHCP is disabled. |
| IPv4 DNS address 1 |  |  | Identify the primary Domain Name System (DNS) server that the phone uses. Available only when DHCP is disabled. |
| IPv4 DNS address 2 |  |  | Identify the secondary Domain Name System (DNS) server that the phone uses. Available only when DHCP is disabled. |
| IPv4 DNS address 3 |  |  | Identify the optional backup Domain Name System (DNS) server that the phone uses. This parameter is only available on the phones registered to Unified CM. Available only when DHCP is disabled. |
| TFTP server 1 |  |  | Available only when Alternate TFTP is enabled. This parameter is only available on the phones registered to Unified CM. Primary Trivial File Transfer Protocol (TFTP) server that the phone uses. If you are not using DHCP in your network and you want to change this server, you must use the TFTP Server 1 option. If Alternate TFTP is enabled, enter a non-zero value for the TFTP Server 1 option. If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock the file before you can save changes to the TFTP Server 1 option. In this case, the phone deletes the file when you save changes to the TFTP Server 1 option. A new CTL or ITL file downloads from the new TFTP Server 1 address. When the phone looks for the TFTP server, the phone gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in this order: Any manually assigned IPv4 TFTP servers Any manually assigned IPv6 servers DHCP assigned TFTP servers DHCPv6 assigned TFTP servers |
| TFTP server 2 |  |  | Available only when Alternate TFTP is enabled. This parameter is only available on the phones registered to Unified CM. Optional backup TFTP server that the phone uses if the primary TFTP server is unavailable. If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock either of the files before you can save changes to the TFTP Server 2 option. In this case, the phone deletes either of the files when you save changes to the TFTP Server 2 option. A new CTL or ITL file downloads from the new TFTP Server 2 address. If you forget to unlock the CTL or ITL file, you can change the TFTP Server 2 address in either file, then erase them by pressing Erase from the Security Configuration menu. A new CTL or ITL file downloads from the new TFTP Server 2 address. When the phone looks for the TFTP server, it gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in the following order: Any manually assigned IPv4 TFTP servers Any manually assigned IPv6 servers DHCP assigned TFTP servers DHCPv6 assigned TFTP servers |
| DHCPv4 option to use |  | 66,160,159,150 | Specify the DHCPv4 options that can deliver configuration parameters from a DHCP server to the phone. This parameter is only available on the phone registered to Webex Calling or BroadWorks. |

| 1 | Press Settings . |
|---|---|
| 2 | Navigate to Network and service > Network settings > IPv4 settings . |
| 3 | In the IPv4 settings screen, configure the settings as needed. |
| 4 | Select Apply when done. The phone restarts to apply the changes. |

| Parameters | Options | Default | Description |
|---|---|---|---|
| DHCPv6 | On Off | On | Enable or disable DHCP on your phone. Enable DHCP to allow your phone to get an IP address from the DHCP server. Otherwise, disable DHCP and manually assign an IP address to your phone. |
| IPv6 address |  |  | Available only when DHCPv6 is disabled. You must assign an IP address to the phone when DHCP is disabled. |
| IPv6 prefix length |  | 0 | Available only when DHCPv6 is disabled. Identify how many bits of a Global Unicast IPv6 Address are there in the network part. |
| IPv6 Gateway |  |  | Available only when DHCPv6 is disabled. Identify the default router for the phone to use when DHCP is disabled. |
| IPv6 DNS address 1 |  |  | Identify the primary Domain Name System (DNS) server that the phone uses. |
| IPv6 DNS address 2 |  |  | Identify the secondary Domain Name System (DNS) server that the phone uses. |
| IPv6 alternate TFTP | On Off | Off | Available only when DHCP is enabled. This parameter is only available on the phones registered to Unified CM. Indicates whether the phone is using an alternate TFTP server. |
| IPv6 TFTP server 1 |  |  | Available only when Alternate TFTP is enabled. This parameter is only available on the phones registered to Unified CM. Primary Trivial File Transfer Protocol (TFTP) server that the phone uses. If you are not using DHCP in your network and you want to change this server, you must use the TFTP Server 1 option. If Alternate TFTP is enabled, enter a non-zero value for the TFTP Server 1 option. If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock the file before you can save changes to the TFTP Server 1 option. In this case, the phone deletes the file when you save changes to the TFTP Server 1 option. A new CTL or ITL file downloads from the new TFTP Server 1 address. When the phone looks for the TFTP server, the phone gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in this order: Any manually assigned IPv4 TFTP servers Any manually assigned IPv6 servers DHCP assigned TFTP servers DHCPv6 assigned TFTP servers |
| IPv6 TFTP server 2 |  |  | Available only when Alternate TFTP is enabled. This parameter is only available on the phones registered to Unified CM. Optional backup TFTP server that the phone uses if the primary TFTP server is unavailable. If neither the primary TFTP server nor the backup TFTP server is listed in the CTL or ITL file on the phone, you must unlock either of the files before you can save changes to the TFTP Server 2 option. In this case, the phone deletes either of the files when you save changes to the TFTP Server 2 option. A new CTL or ITL file downloads from the new TFTP Server 2 address. If you forget to unlock the CTL or ITL file, you can change the TFTP Server 2 address in either file, then erase them by pressing Erase from the Security Configuration menu. A new CTL or ITL file downloads from the new TFTP Server 2 address. When the phone looks for the TFTP server, it gives precedence to manually assigned TFTP servers, regardless of the protocol. If your configuration includes both IPv6 and IPv4 TFTP servers, the phone prioritizes the order that it looks for the TFTP server by giving priority to manually assigned IPv6 TFTP servers and IPv4 TFTP servers. The phone looks for the TFTP server in the following order: Any manually assigned IPv4 TFTP servers Any manually assigned IPv6 servers DHCP assigned TFTP servers DHCPv6 assigned TFTP servers |
| IPv6 address released | On Off | Off | Available only when DHCP is enabled. This parameter is only available on the phones registered to Unified CM. To release the IP address that DHCP assigned for reassignment, turn on this switch. Otherwise, turn it Off. |
| DHCPv6 option to use |  | 17,160,159 | Specify the DHCPv6 options that can deliver configuration parameters from a DHCP server to the phone. This parameter is only available on the phone registered to Webex Calling or BroadWorks. |

| 1 | Press Settings . |
|---|---|
| 2 | Navigate to Network and service > Network settings > IPv6 settings . |
| 3 | In the IPv6 settings screen, configure the settings as needed. |
| 4 | Select Apply when done. The phone restarts to apply the changes. |

| Parameters | Options | Default | Description |
|---|---|---|---|
| Admin VLAN ID | Valid values: 0 through 4095 | 1 | Enter a VLAN ID for the IP phone when you use a VLAN without CDP (VLAN enabled, CDP disabled, and LLDP disabled). Note that only voicepackets are tagged with the VLAN ID. Do not use the 1 value for the VLAN ID. If VLAN ID is 1, you cannot tag voice packets with the VLAN ID. |
| PC VLAN ID | Valid values: 0 through 4095 | 1 | Enter a value of the VLAN ID that is used to tag communications from the PC port on the phone. The phone tags all the untagged frames coming from the PC (it does not tag any frames with an existing tag). |

| 1 | Press Settings . |
|---|---|
| 2 | Navigate to Network and service > Network settings > VLAN . |
| 3 | In the VLAN screen, configure the settings as needed. |
| 4 | Select Apply when done. The phone restarts to apply the changes. |

| 1 | Press Settings |
|---|---|
| 2 | Navigate to Network and service > VPN . The status for the menu item VPN indicates that whether the VPN connection is turned on or off. |
| 3 | Turn on the VPN connection. Press On . Toggle on VPN. Your phone will try to connect to the VPN. If a required certificate is already installed on the phone, the VPN connection establishes directly. The job is finished, you can skip the following steps. Otherwise, you need to enter user credentials. When your phone is trying to connect to the VPN, you can cancel the process by selecting Cancel . Then the VPN connection will be back to disabled. |
| 4 | When prompted for the VPN sign-in, enter your user ID and password, or just password, and then select Apply . Your phone will try to establish the VPN connection. Once successful, you will receive the pop-up message and you can find the VPN icon on the top right corner of the home screen. |
| 5 | (Optional) To change the user credentials for an existing VPN connection, do the following: Navigate to Network and service > VPN . Select Credentials . Enter a valid user ID and password, and then select Apply . |

| 1 | Press Settings |
|---|---|
| 2 | Navigate to the HTTP proxy settings menu: Select Network and service > Network settings > HTTP proxy . Select Network connection > Network settings , and navigate to the HTTP proxy section. |
| 3 | Select the auto proxy mode: Select Proxy Mode , and then select Auto . Select Auto in the HTTP proxy section. |
| 4 | (Optional) Turn on Web Proxy Auto Discovery (WPAD) that is used to retrieve a PAC file automatically. By default, your phone uses WPAD in the auto proxy mode. Highlight Web proxy auto discovery , and select On . Toggle on Web proxy auto discovery . |
| 5 | If you want to manually enter a Proxy Auto Configuration (PAC) URL, turn off Web proxy auto discovery , and enter a PAC URL in PAC URL . For example: http://proxy.department.branch.example.com/pac If you don't have the PAC URL, contact your administrator. |
| 6 | Press Apply to apply the settings. |

| 1 | Press Settings |
|---|---|
| 2 | Do one of the following actions: Select Network and service > Network settings > HTTP proxy . Select Network connection > Network settings , and navigate to the HTTP proxy section. |
| 3 | Select the manual proxy mode: Select Proxy Mode , and then select Manual . Select Manual in the HTTP proxy section. |
| 4 | Enter a valid hostname or IP address of a proxy server in Proxy host . Do not provide the scheme (http:// or https://) for the proxy host. |
| 5 | Enter a valid server port of the specified proxy server in Proxy port . |
| 6 | If the specified proxy server requires user's authentication, turn on Proxy authentication , and enter your username and password to access the proxy server. If you don't have the username and password, contact your administrator. |
| 7 | Select Apply to apply the settings. |

| 1 | On the phone web page, select Voice > System . |
|---|---|
| 2 | Under the section HTTP Proxy Settings , set the parameters, as described in the above table. Proxy Mode : Choose the proxy mode (Auto or Manual) for the HTTP proxy setting. If set to Off (default), the HTTP proxy is disabled. By default, the value is Off. If Proxy Mode is set to Auto ,  set Web Proxy Auto Discovery to Yes (default) or No to determine whether to use the Web Proxy Auto Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . PAC URL : URL that locate the PAC file. If Proxy Mode is set to Manual , you must configure the following parameters: Proxy Host : Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). Proxy Port : Port number of the proxy server. The default port is 3128 Proxy Authentication : If your proxy server requires authentication, select Yes . Otherwise, select No (default). The configuration depends on the actual behavior of the proxy server. If set to Yes , you must configure Username and Password for an authentication on the proxy server. |
| 3 | Click Submit All Changes . |