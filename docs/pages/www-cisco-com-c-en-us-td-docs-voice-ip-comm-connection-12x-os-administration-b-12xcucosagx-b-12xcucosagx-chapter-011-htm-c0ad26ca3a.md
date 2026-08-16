---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-os-administration-b-12xcucosagx-b-12xcucosagx-chapter-011-htm-c0ad26ca3a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx/b_12xcucosagx_chapter_011.html
retrieved_at: 2026-08-16T18:58:25.885688+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x

Updated: August 4, 2017

Chapter: Settings

## Chapter: Settings

# Settings

## Overview

Use the Settings options to display and change IP settings, host settings, and Network Time Protocol (NTP) settings.

## IP Settings

The IP Settings options allow you to view and change IP and port setting for the Ethernet connection and, on subsequent nodes,
                           to set the IP address of the publisher.

### Ethernet
                           	 Settings

The IP Settings window indicates whether Dynamic Host
                                 		  Configuration Protocol (DHCP) is active and also provides the related Ethernet
                                 		  IP addresses, as well as the IP address for the network gateway.

All Ethernet settings apply only to Eth0. You cannot configure
                                 		  any settings for Eth1. The Maximum Transmission Unit (MTU) on Eth0 defaults to
                                 		  1500.

To view IP settings, do the following procedure.

Do not use the procedure to change IP settings for Cisco Unity
                                             			 Connection.

For information on changing the IP address of a Connection
                                             			 server, see the “Changing the IP Addresses of Cisco Unity Connection Servers” Upgrade Guide for Unity Connection at http://www.cisco.com/en/US/products/ps6509/prod_installation_guides_list.html .

For information on changing the host name of a Unity Connection
                                             			 12.x server refer, Install, Upgrade, and Maintenance Guide for Cisco Unity
                                                				Connection 12x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > IP > Ethernet .

The Ethernet Settings window displays.For a description of the
                                             				fields on the Ethernet Settings window, see Table 4-1 .

Field

Description

DHCP

Indicates whether DHCP is Enabled or Disabled.

Hostname

Displays the host name of the server.

IP Address

Displays the IP address of the system.

Subnet Mask

Displays the IP subnet mask address.

Default Gateway

Shows the IP address of the network gateway.

### Ethernet IPv6
                           	 Configuration Settings

The settings detailed below are applicable to Cisco Unity
                                             			 Connection release 9.0 and later. IPv6 is not supported in earlier versions of
                                             			 Cisco Unity Connection.

The Ethernet IPv6 Configuration Settings page allows you to
                                 		  enable IPv6, and to determine a method for obtaining the IP addresses.

To view or change the IPv6 settings, follow this procedure:

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > IP > Ethernet IPv6 Configuration .

To modify the ethernet IPv6 settings, enter the new values in
                                          			 the applicable fields. For a description of the fields on the Ethernet IPv6
                                          			 Configuration Settings window, see Table 4-2 .

To preserve your changes, select Save .

Field

Description

Enable IPv6

Check this check box to enable IPv6.

Address Source

Select one of the following:

- Router
                                                            							 Advertisement-Select this option if your network router is configured to
                                                            							 advertise the network prefix to servers on the network.

- DHCP-Select
                                                            							 this option to use the DHCPv6 protocol to assign addresses to your server (note
                                                            							 that you must be running a DHCPv6 server on the network to provide the
                                                            							 addresses).

- Manual
                                                            							 Entry-Select this option if you want to enter an address manually in the IPv6
                                                            							 Address field.

Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server.

IPv6 Address

If you chose Manual Entry as the Address Source, enter an
                                                         						  IPv6 address.

For example, enter:

2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345

Subnet Mask

If you chose Manual Entry as the Address Source, enter a
                                                         						  prefix length (from 0 through 128), indicating the number of bits in the
                                                         						  address that correspond to the prefix of the network.

For example, enter: 64

Update with Reboot

Check this check box if you want an immediate reboot of
                                                         						  the server to occur when you save the updated settings.

For the IPv6 settings to take effect, you must reboot
                                                                     							 the system.

### Publisher Settings

This feature is only applicable if Cisco Unified Communications Manager is installed alone on the server.

## NTP
                        	 Servers

Ensure that external NTP servers are stratum 9 or higher (1-9).
                              		  To add, delete, or modify an external NTP server, follow this procedure:

You can only configure the NTP server settings on the first node
                                          			 or publisher.

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > NTP
                                             				  Servers .

The NTP Server Settings window displays.

You can add, delete, or modify an NTP server:

To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node should
                                                      				  be NTP v4 (version 4). If you are usingIPv6 addressing, external NTP servers
                                                      				  must be NTP v4.

To delete an NTP server, check the check box in front of the
                                                            						appropriate server and click Delete .

To add an NTP server, click Add , enter the hostname or IP address, and then click Save .

To modify an NTP server, click the IP address, modify the
                                                            						hostname or IP address, and then click Save .

Any change that you make to the NTP servers can take up to 5
                                                            						minutes to complete. Whenever you make any change to the NTP servers, you must
                                                            						refresh the window to display the correct status.

To refresh the NTP Server Settings window and display the
                                       			 correct status, select Settings > NTP .

After deleting, modifying, or adding the NTP server, you must
                                                      				  restart all other nodes in the cluster for the changes to take affect.

## SMTP
                        	 Settings

The SMTP Settings window allows you to view or set the SMTP
                              		  hostname and indicates whether the SMTP host is active.

If you want the system to send you e-mail, you must configure an
                                          			 SMTP host.

To access the SMTP settings, follow this procedure:

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > SMTP .

The SMTP Settings window displays.

Enter or modify the SMTP hostname or IP address.

Click Save .

## Time
                        	 Settings

To manually configure the time, follow this procedure:

Before you can manually configure the server time, you must
                                          			 delete any NTP servers that you have configured. See the “NTP
                                             				Servers” section on page 4-3 for more information.

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > Time .

Enter the date and time for the system.

Click Save .

On a Cisco Unity Connection server, if you changed the date or
                                       			 if you changed the time by more than two minutes, use the CLI command utils system restart to restart the server.

| Caution | Do not use the procedure to change IP settings for Cisco Unity
                                             			 Connection. |
|---|---|

| Caution | For information on changing the IP address of a Connection
                                             			 server, see the “Changing the IP Addresses of Cisco Unity Connection Servers” Upgrade Guide for Unity Connection at http://www.cisco.com/en/US/products/ps6509/prod_installation_guides_list.html . |
|---|---|

| Caution | For information on changing the host name of a Unity Connection
                                             			 12.x server refer, Install, Upgrade, and Maintenance Guide for Cisco Unity
                                                				Connection 12x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html . |
|---|---|

| From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > IP > Ethernet . The Ethernet Settings window displays.For a description of the
                                             				fields on the Ethernet Settings window, see Table 4-1 . Table 1. Ethernet
                                                      				  Configuration Fields and Descriptions Field Description DHCP Indicates whether DHCP is Enabled or Disabled. Hostname Displays the host name of the server. IP Address Displays the IP address of the system. Subnet Mask Displays the IP subnet mask address. Default Gateway Shows the IP address of the network gateway. | Field | Description | DHCP | Indicates whether DHCP is Enabled or Disabled. | Hostname | Displays the host name of the server. | IP Address | Displays the IP address of the system. | Subnet Mask | Displays the IP subnet mask address. | Default Gateway | Shows the IP address of the network gateway. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| DHCP | Indicates whether DHCP is Enabled or Disabled. |
| Hostname | Displays the host name of the server. |
| IP Address | Displays the IP address of the system. |
| Subnet Mask | Displays the IP subnet mask address. |
| Default Gateway | Shows the IP address of the network gateway. |

| Field | Description |
|---|---|
| DHCP | Indicates whether DHCP is Enabled or Disabled. |
| Hostname | Displays the host name of the server. |
| IP Address | Displays the IP address of the system. |
| Subnet Mask | Displays the IP subnet mask address. |
| Default Gateway | Shows the IP address of the network gateway. |

| Note | The settings detailed below are applicable to Cisco Unity
                                             			 Connection release 9.0 and later. IPv6 is not supported in earlier versions of
                                             			 Cisco Unity Connection. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > IP > Ethernet IPv6 Configuration . |
|---|---|
| Step 2 | To modify the ethernet IPv6 settings, enter the new values in
                                          			 the applicable fields. For a description of the fields on the Ethernet IPv6
                                          			 Configuration Settings window, see Table 4-2 . |
| Step 3 | To preserve your changes, select Save . Table 2. Ethernet IPv6 Configuration Fields and Descriptions Field Description Enable IPv6 Check this check box to enable IPv6. Address Source Select one of the following: Router
                                                            							 Advertisement-Select this option if your network router is configured to
                                                            							 advertise the network prefix to servers on the network. DHCP-Select
                                                            							 this option to use the DHCPv6 protocol to assign addresses to your server (note
                                                            							 that you must be running a DHCPv6 server on the network to provide the
                                                            							 addresses). Manual
                                                            							 Entry-Select this option if you want to enter an address manually in the IPv6
                                                            							 Address field. Note Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. IPv6 Address If you chose Manual Entry as the Address Source, enter an
                                                         						  IPv6 address. For example, enter: 2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345 Subnet Mask If you chose Manual Entry as the Address Source, enter a
                                                         						  prefix length (from 0 through 128), indicating the number of bits in the
                                                         						  address that correspond to the prefix of the network. For example, enter: 64 Update with Reboot Check this check box if you want an immediate reboot of
                                                         						  the server to occur when you save the updated settings. Note For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. | Field | Description | Enable IPv6 | Check this check box to enable IPv6. | Address Source | Select one of the following: Router
                                                            							 Advertisement-Select this option if your network router is configured to
                                                            							 advertise the network prefix to servers on the network. DHCP-Select
                                                            							 this option to use the DHCPv6 protocol to assign addresses to your server (note
                                                            							 that you must be running a DHCPv6 server on the network to provide the
                                                            							 addresses). Manual
                                                            							 Entry-Select this option if you want to enter an address manually in the IPv6
                                                            							 Address field. Note Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. | Note | Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. | IPv6 Address | If you chose Manual Entry as the Address Source, enter an
                                                         						  IPv6 address. For example, enter: 2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345 | Subnet Mask | If you chose Manual Entry as the Address Source, enter a
                                                         						  prefix length (from 0 through 128), indicating the number of bits in the
                                                         						  address that correspond to the prefix of the network. For example, enter: 64 | Update with Reboot | Check this check box if you want an immediate reboot of
                                                         						  the server to occur when you save the updated settings. Note For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. | Note | For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. |
| Field | Description |
| Enable IPv6 | Check this check box to enable IPv6. |
| Address Source | Select one of the following: Router
                                                            							 Advertisement-Select this option if your network router is configured to
                                                            							 advertise the network prefix to servers on the network. DHCP-Select
                                                            							 this option to use the DHCPv6 protocol to assign addresses to your server (note
                                                            							 that you must be running a DHCPv6 server on the network to provide the
                                                            							 addresses). Manual
                                                            							 Entry-Select this option if you want to enter an address manually in the IPv6
                                                            							 Address field. Note Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. | Note | Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. |
| Note | Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. |
| IPv6 Address | If you chose Manual Entry as the Address Source, enter an
                                                         						  IPv6 address. For example, enter: 2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345 |
| Subnet Mask | If you chose Manual Entry as the Address Source, enter a
                                                         						  prefix length (from 0 through 128), indicating the number of bits in the
                                                         						  address that correspond to the prefix of the network. For example, enter: 64 |
| Update with Reboot | Check this check box if you want an immediate reboot of
                                                         						  the server to occur when you save the updated settings. Note For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. | Note | For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. |
| Note | For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. |

| Field | Description |
|---|---|
| Enable IPv6 | Check this check box to enable IPv6. |
| Address Source | Select one of the following: Router
                                                            							 Advertisement-Select this option if your network router is configured to
                                                            							 advertise the network prefix to servers on the network. DHCP-Select
                                                            							 this option to use the DHCPv6 protocol to assign addresses to your server (note
                                                            							 that you must be running a DHCPv6 server on the network to provide the
                                                            							 addresses). Manual
                                                            							 Entry-Select this option if you want to enter an address manually in the IPv6
                                                            							 Address field. Note Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. | Note | Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. |
| Note | Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. |
| IPv6 Address | If you chose Manual Entry as the Address Source, enter an
                                                         						  IPv6 address. For example, enter: 2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345 |
| Subnet Mask | If you chose Manual Entry as the Address Source, enter a
                                                         						  prefix length (from 0 through 128), indicating the number of bits in the
                                                         						  address that correspond to the prefix of the network. For example, enter: 64 |
| Update with Reboot | Check this check box if you want an immediate reboot of
                                                         						  the server to occur when you save the updated settings. Note For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. | Note | For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. |
| Note | For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. |

| Note | Cisco recommends that the Cisco Unity Connection server
                                                                     							 use a static non-link-local IPv6 address. If the server obtains the IPv6
                                                                     							 address from the DHCPv6 server or via stateless address autoconfiguration,
                                                                     							 ensure that the server only obtains one non-link-local IPv6 address from the
                                                                     							 DHCPv6 server. |
|---|---|

| Note | For the IPv6 settings to take effect, you must reboot
                                                                     							 the system. |
|---|---|

| Note | You can only configure the NTP server settings on the first node
                                          			 or publisher. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > NTP
                                             				  Servers . The NTP Server Settings window displays. |
|---|---|
| Step 2 | You can add, delete, or modify an NTP server: Note To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node should
                                                      				  be NTP v4 (version 4). If you are usingIPv6 addressing, external NTP servers
                                                      				  must be NTP v4. To delete an NTP server, check the check box in front of the
                                                            						appropriate server and click Delete . To add an NTP server, click Add , enter the hostname or IP address, and then click Save . To modify an NTP server, click the IP address, modify the
                                                            						hostname or IP address, and then click Save . Any change that you make to the NTP servers can take up to 5
                                                            						minutes to complete. Whenever you make any change to the NTP servers, you must
                                                            						refresh the window to display the correct status. | Note | To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node should
                                                      				  be NTP v4 (version 4). If you are usingIPv6 addressing, external NTP servers
                                                      				  must be NTP v4. To delete an NTP server, check the check box in front of the
                                                            						appropriate server and click Delete . To add an NTP server, click Add , enter the hostname or IP address, and then click Save . To modify an NTP server, click the IP address, modify the
                                                            						hostname or IP address, and then click Save . Any change that you make to the NTP servers can take up to 5
                                                            						minutes to complete. Whenever you make any change to the NTP servers, you must
                                                            						refresh the window to display the correct status. |
| Note | To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node should
                                                      				  be NTP v4 (version 4). If you are usingIPv6 addressing, external NTP servers
                                                      				  must be NTP v4. To delete an NTP server, check the check box in front of the
                                                            						appropriate server and click Delete . To add an NTP server, click Add , enter the hostname or IP address, and then click Save . To modify an NTP server, click the IP address, modify the
                                                            						hostname or IP address, and then click Save . Any change that you make to the NTP servers can take up to 5
                                                            						minutes to complete. Whenever you make any change to the NTP servers, you must
                                                            						refresh the window to display the correct status. |
| Step 3 | To refresh the NTP Server Settings window and display the
                                       			 correct status, select Settings > NTP . Note After deleting, modifying, or adding the NTP server, you must
                                                      				  restart all other nodes in the cluster for the changes to take affect. | Note | After deleting, modifying, or adding the NTP server, you must
                                                      				  restart all other nodes in the cluster for the changes to take affect. |
| Note | After deleting, modifying, or adding the NTP server, you must
                                                      				  restart all other nodes in the cluster for the changes to take affect. |

| Note | To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node should
                                                      				  be NTP v4 (version 4). If you are usingIPv6 addressing, external NTP servers
                                                      				  must be NTP v4. To delete an NTP server, check the check box in front of the
                                                            						appropriate server and click Delete . To add an NTP server, click Add , enter the hostname or IP address, and then click Save . To modify an NTP server, click the IP address, modify the
                                                            						hostname or IP address, and then click Save . Any change that you make to the NTP servers can take up to 5
                                                            						minutes to complete. Whenever you make any change to the NTP servers, you must
                                                            						refresh the window to display the correct status. |
|---|---|

| Note | After deleting, modifying, or adding the NTP server, you must
                                                      				  restart all other nodes in the cluster for the changes to take affect. |
|---|---|

| Tip | If you want the system to send you e-mail, you must configure an
                                          			 SMTP host. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > SMTP . The SMTP Settings window displays. |
|---|---|
| Step 2 | Enter or modify the SMTP hostname or IP address. |
| Step 3 | Click Save . |

| Note | Before you can manually configure the server time, you must
                                          			 delete any NTP servers that you have configured. See the “NTP
                                             				Servers” section on page 4-3 for more information. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > Time . |
|---|---|
| Step 2 | Enter the date and time for the system. |
| Step 3 | Click Save . |
| Step 4 | On a Cisco Unity Connection server, if you changed the date or
                                       			 if you changed the time by more than two minutes, use the CLI command utils system restart to restart the server. |