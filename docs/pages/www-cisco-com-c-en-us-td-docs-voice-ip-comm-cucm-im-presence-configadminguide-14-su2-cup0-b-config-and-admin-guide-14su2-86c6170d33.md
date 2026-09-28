---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-14-su2-cup0-b-config-and-admin-guide-14su2-86c6170d33
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/14_su2/cup0_b_config-and-admin-guide-14su2/cup0_b_config-and-admin-guide-1401_chapter_010.html
retrieved_at: 2026-08-16T16:16:56.955196+00:00
---

Configuration and Administration of the IM and Presence Service, Release 14 and SUs

# Configuration and Administration of the IM and Presence Service, Release 14 and SUs

Updated: May 8, 2025

Chapter: Configure IPv6

## Chapter: Configure IPv6

# Configure IPv6

## Configure IPv6 Overview

You can use IPv6 for your external interfaces on IM and Presence
                           Service even though the connection between IM and Presence Service
                           and Cisco Unified Communications Manager uses IPv4.

If you configure IPv6 for any of the following items on the IM and
                           Presence Service node, the node will not accept incoming IPv4
                           packets and will not automatically revert to using IPv4:

connection to an external database

connection to an LDAP server

connection to an Exchange server

federation deployments

For federation, you must enable IM and Presence Service for IPv6 if
                           you need to support federated links to a foreign Enterprise that is
                           IPv6 enabled. This is true even if there is an ASA installed
                           between the IM and Presence Service node and the federated
                           Enterprise. The ASA is transparent to the IM and Presence Service
                           node.

For more information about using the Command Line Interface to configure IPv6 parameters, see the Administration Guide for Cisco Unified Communications Manager and the Command Line Interface Guide for Cisco Unified Communications Solutions at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Configure IPv6 Task Flow

Step 1

Enable IPv6 on Eth0 for IM and Presence Service

Enable IPv6 on the Eth0 port of each IM and Presence Service node in the cluster. You must reboot each node to apply the changes.

Step 2

Enable IPv6 Enterprise Parameter

After you enable IPv6 on the Eth0 port, you must enable the IPv6 enterprise parameter for the IM and Presence Service cluster.

Step 3

Restart Services

You must restart IM and Presence services to apply the changes.

Step 4

Assign IPv6 Addresses to IM and Presence Nodes

Assign IPv6 addresses to your IM and Presence Service nodes.

### Enable IPv6 on Eth0 for IM and Presence Service

Use Cisco Unified IM and Presence Operating System Administration GUI to enable IPv6 on the Eth0 port of each IM and Presence
                                 Service node in the cluster.

Step 1

In Cisco Unified IM and Presence OS Administration , choose Settings > IP > Ethernet IPv6 .

Step 2

In the Ethernet IPv6 Configuration window, check the Enable IPv6 check box.

Step 3

Choose the Address Source :

- Router Advertisement

- DHCP

- Manual Entry

If you selected Manual Entry, enter the IPv6 Address , Subnet Mask , and the Default Gateway values.

Step 4

Check the Update with Reboot check box.

Tip

Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node.

Step 5

Click Save .

If you checked the Update with Reboot check box, the node reboots and the changes are applied.

#### What to do next

Enable IPv6 Enterprise Parameter

### Enable IPv6 Enterprise Parameter

Use Cisco Unified CM IM and Presence Administration to enable the IPv6 enterprise parameter for the IM and Presence Service
                                 cluster.

#### Before you begin

Enable IPv6 on Eth0 for IM and Presence Service

Step 1

In Cisco Unified CM IM and Presence Administration , choose System > Enterprise Parameters .

Step 2

In the Enterprise Parameters Configuration window, choose True in the IPv6 panel.

Step 3

Click Save .

#### What to do next

Restart Services to apply the changes.

### Restart Services

Use this procedure to restart IM and Presence services after you enable the IPv6 enterprise parameter for the cluster.

Tip

To monitor system restart notifications using Cisco Unified CM IM and Presence Administration, select System > Notifications .

#### Before you begin

Enable IPv6 Enterprise Parameter

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

Step 2

From the Server list, choose the node on which you want to reactivate services and click Go .

Step 3

In the IM and Presence Services area, select Cisco XCP Router .

Step 4

Click Restart .

Step 5

From the Related Links drop-down list, select Service Activation and click Go .

Step 6

In the IM and Presence Services area, select the following services:

Cisco SIP Proxy

Cisco Presence Engine

Step 7

Click Save .

### Assign IPv6 Addresses to IM and Presence Nodes

#### Before you begin

You must also enable the IPv6 Eth0 port in Cisco Unified OS Administration, and enable the IPv6 enterprise parameter.

Step 1

Log in to the Cisco Unified Communications Manager publisher node

Step 2

From Cisco Unified CM Administration, choose System > Server .

Step 3

Complete one of the following tasks:

- To add a new server, click Add New .

- To update an existing server, click on the server that you want to edit.

Step 4

If you are adding a new server, from the Server Type drop-down menu, select CUCM IM and Presence and click Next .

Step 5

Enter the IPv6 Address for the server.

Step 6

Click Save .

Step 7

Repeat for each IM and Presence Service cluster node.

### Disable IPv6 on Eth0 for IM and Presence Service

If you want to disable IPv6, use the Cisco Unified IM and Presence Operating System Administration GUI to disable IPv6 on the Eth0 port of each IM and Presence Service node in the cluster that you do not want to use IPv6.
                                 You must reboot the node to apply the changes.

If you do not want any of the nodes in the cluster to use IPv6, make sure the IPv6 enterprise parameter is disabled for the
                                             cluster.

Step 1

In Cisco Unified CM IM and Presence OS Administration , choose Settings > IP > Ethernet IPv6 .

Step 2

In the Ethernet IPv6 Configuration window, uncheck the Enable IPv6 check box.

Step 3

Check the Update with Reboot check box.

Tip

Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node.

Step 4

Click Save .

If you checked the Update with Reboot check box, the node reboots and the changes are applied.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable IPv6 on Eth0 for IM and Presence Service | Enable IPv6 on the Eth0 port of each IM and Presence Service node in the cluster. You must reboot each node to apply the changes. |
| Step 2 | Enable IPv6 Enterprise Parameter | After you enable IPv6 on the Eth0 port, you must enable the IPv6 enterprise parameter for the IM and Presence Service cluster. |
| Step 3 | Restart Services | You must restart IM and Presence services to apply the changes. |
| Step 4 | Assign IPv6 Addresses to IM and Presence Nodes | Assign IPv6 addresses to your IM and Presence Service nodes. |

| Step 1 | In Cisco Unified IM and Presence OS Administration , choose Settings > IP > Ethernet IPv6 . |
|---|---|
| Step 2 | In the Ethernet IPv6 Configuration window, check the Enable IPv6 check box. |
| Step 3 | Choose the Address Source : Router Advertisement DHCP Manual Entry If you selected Manual Entry, enter the IPv6 Address , Subnet Mask , and the Default Gateway values. |
| Step 4 | Check the Update with Reboot check box. Tip Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. | Tip | Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. |
| Tip | Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. |
| Step 5 | Click Save . If you checked the Update with Reboot check box, the node reboots and the changes are applied. |

| Tip | Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Enterprise Parameters Configuration window, choose True in the IPv6 panel. |
| Step 3 | Click Save . |

| Tip | To monitor system restart notifications using Cisco Unified CM IM and Presence Administration, select System > Notifications . |
|---|---|

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . |
|---|---|
| Step 2 | From the Server list, choose the node on which you want to reactivate services and click Go . |
| Step 3 | In the IM and Presence Services area, select Cisco XCP Router . |
| Step 4 | Click Restart . |
| Step 5 | From the Related Links drop-down list, select Service Activation and click Go . |
| Step 6 | In the IM and Presence Services area, select the following services: Cisco SIP Proxy Cisco Presence Engine |
| Step 7 | Click Save . |

| Step 1 | Log in to the Cisco Unified Communications Manager publisher node |
|---|---|
| Step 2 | From Cisco Unified CM Administration, choose System > Server . |
| Step 3 | Complete one of the following tasks: To add a new server, click Add New . To update an existing server, click on the server that you want to edit. |
| Step 4 | If you are adding a new server, from the Server Type drop-down menu, select CUCM IM and Presence and click Next . |
| Step 5 | Enter the IPv6 Address for the server. |
| Step 6 | Click Save . |
| Step 7 | Repeat for each IM and Presence Service cluster node. |

| Note | If you do not want any of the nodes in the cluster to use IPv6, make sure the IPv6 enterprise parameter is disabled for the
                                             cluster. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence OS Administration , choose Settings > IP > Ethernet IPv6 . |
|---|---|
| Step 2 | In the Ethernet IPv6 Configuration window, uncheck the Enable IPv6 check box. |
| Step 3 | Check the Update with Reboot check box. Tip Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. | Tip | Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. |
| Tip | Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. |
| Step 4 | Click Save . If you checked the Update with Reboot check box, the node reboots and the changes are applied. |

| Tip | Do not check the Update with Reboot check box if you want to manually reboot the node at a later time, such as during a scheduled maintenance window; however,
                                                         the changes you made do not take effect until you reboot the node. |
|---|---|