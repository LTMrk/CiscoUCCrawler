---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-ea733c26b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_12_6_1-install_upgrade_guide/ucce_b_12_6_1-install_upgrade_guide_appendix_010000.html
retrieved_at: 2026-08-16T20:01:57.616448+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: IPv6 Configuration

## Chapter: IPv6 Configuration

# IPv6 Configuration

## Configure NAT64
                        	 for IPv6-Enabled Deployment

NAT64 allows communication between IPv6 and IPv4 networks. For IPv6-enabled deployments, you must set up NAT64 so that supervisors
                              on an IPv6 network can access Unified CCE Administration web tools on an IPv4 network. You can use either Stateful and Stateless
                              NAT64.

NAT64 is NOT supported on M train IOS. T train is required.

For more information on Contact Center Enterprise Compatibility Matrix , see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

The following example network diagram and interface configuration demonstrates Stateful NAT64 translation between an IPv6
                              network and an IPv4 network.

```
interface GigabitEthernet0/0
description ipv4-only interface
 ip address 10.10.10.81 255.255.255.128
 duplex auto
 speed auto
 nat64 enable
 no mop enabled

interface GigabitEthernet0/1
description ipv6-only interface
 no ip address
 duplex auto
 speed auto
 nat64 enable
 ipv6 address 2001::1/64
 ipv6 enable

ipv6 unicast-routing
ipv6 cef
!
nat64 prefix stateful 3001::/96
nat64 v4 pool POOL1 10.10.10.129 10.10.10.250
nat64 v6v4 list V6ACL1 pool POOL1 overload
ipv6 router rip RIPv6
!
ipv6 router rip RIP

!
ipv6 access-list V6ACL1
 permit ipv6 2001::/64 any
```

### Configure DNS for IPv6

To meet the requirement that Unified CCE Administration
                                 		  be accessed by FQDN, a Forward lookup AAAA record for the AW must be created in
                                 		  DNS.

The steps in this
                                 		  procedure are for a Windows DNS server.

Step 1

In Windows,
                                          			 navigate to Administrative Tools > DNS . This opens the DNS
                                          			 Manager.

Step 2

In the Forward
                                          			 lookup zone, navigate to your deployment's domain name.

Step 3

Right-click
                                          			 the domain name and select New
                                             				Host (A or AAAA) .

Step 4

In the New
                                          			 Host dialog box, enter the computer name and IP address of the AW. Click Add Host .

#### Determine IPv6
                              	 Translation of IPv4 Address for DNS Entry

You can determine the IPv6 address needed for the AAAA DNS record by running a ping command on any Windows machine using mixed
                                 notation. Type “ping -6” followed by your IPv6 Nat64 Prefix, two colons, and then the IPv4 address.

In the ping
                                 		response, the IPv4 address is converted to the hexadecimal equivalent. Use this
                                 		address in your static AAAA record.

Optionally, DNS64
                                             		  can be used in place of static DNS entries. Use of DNS64 helps facilitate
                                             		  translation between IPv6 and IPv4 networks by synthesizing AAAA resource
                                             		  records from A resource records.

## Set Up IPv6 for
                        	 VOS-Based Contact Center Applications

By default, only IPv4 is enabled for Unified Communications Manager, Cisco Finesse, and Unified Intelligence Center.

If you choose to
                           		enable IPv6 on these applications, you must enable it on both the
                           		publisher/primary nodes and subscriber/secondary nodes for those applications.

You can use Cisco
                           		Unified Operating System Administration or the CLI to enable IPv6.

See the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html for more information about IPv6 support in Unified CCE.

### Set Up IPv6 Using
                           	 Cisco Unified Operating System Administration

Step 1

Sign into
                                          			 Cisco Unified Operating System Administration on the Publisher/Primary node:.

Unified
                                                   					 Communications Manager and Unified Intelligence Center: https:// <host or IP address of the Publisher or Primary
                                                         						  node> /cmplatform

Finesse: https:// FQDN of the Primary node :8443/cmplatform

Step 2

Navigate to Settings > IP > Ethernet
                                                				  IPv6 .

Step 3

Check
                                          			 the Enable
                                             				IPv6 check box.

Step 4

Enter values
                                          			 for IPv6Address , Prefix
                                             				Length , and Default Gateway .

Step 5

Check the Update with
                                             				Reboot check box.

Step 6

Click Save .

Step 7

Repeat this
                                          			 procedure on the subscriber/secondary node.

### Set Up IPv6 for
                           	 VOS-Based Applications Using the CLI

Step 1

Access the CLI on the VOS server.

Step 2

To enable or disable IPv6, enter:

Step 3

Set the IPv6 address and prefix length:

#### Example:

Step 4

Set the default gateway:

Step 5

Restart the system for the changes to take effect.

Step 6

To display the IPv6 settings, enter:

| Note | NAT64 is NOT supported on M train IOS. T train is required. For more information on Contact Center Enterprise Compatibility Matrix , see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . |
|---|---|

| Step 1 | In Windows,
                                          			 navigate to Administrative Tools > DNS . This opens the DNS
                                          			 Manager. |
|---|---|
| Step 2 | In the Forward
                                          			 lookup zone, navigate to your deployment's domain name. |
| Step 3 | Right-click
                                          			 the domain name and select New
                                             				Host (A or AAAA) . |
| Step 4 | In the New
                                          			 Host dialog box, enter the computer name and IP address of the AW. Click Add Host . |

| Note | Optionally, DNS64
                                             		  can be used in place of static DNS entries. Use of DNS64 helps facilitate
                                             		  translation between IPv6 and IPv4 networks by synthesizing AAAA resource
                                             		  records from A resource records. |
|---|---|

| Step 1 | Sign into
                                          			 Cisco Unified Operating System Administration on the Publisher/Primary node:. Unified
                                                   					 Communications Manager and Unified Intelligence Center: https:// <host or IP address of the Publisher or Primary
                                                         						  node> /cmplatform Finesse: https:// FQDN of the Primary node :8443/cmplatform |
|---|---|
| Step 2 | Navigate to Settings > IP > Ethernet
                                                				  IPv6 . |
| Step 3 | Check
                                          			 the Enable
                                             				IPv6 check box. |
| Step 4 | Enter values
                                          			 for IPv6Address , Prefix
                                             				Length , and Default Gateway . |
| Step 5 | Check the Update with
                                             				Reboot check box. |
| Step 6 | Click Save . The
                                          			 server restarts. |
| Step 7 | Repeat this
                                          			 procedure on the subscriber/secondary node. |

| Step 1 | Access the CLI on the VOS server. |
|---|---|
| Step 2 | To enable or disable IPv6, enter: set network ipv6 service {enable \| disable} |
| Step 3 | Set the IPv6 address and prefix length: set network ipv6 static_address addr mask Example: set network ipv6 static_address 2001:db8:2::a 64 |
| Step 4 | Set the default gateway: set network ipv6 gateway addr |
| Step 5 | Restart the system for the changes to take effect. utils system restart |
| Step 6 | To display the IPv6 settings, enter: show network ipv6 settings |