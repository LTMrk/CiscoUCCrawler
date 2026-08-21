---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--6ceb43dbd2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-cvvb-cuc-os-administration-guide/ccvp_b_1251-cvvb-cuc-os-administration-guide_chapter_011.html
retrieved_at: 2026-08-21T16:32:00.831423+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Updated: February 2, 2020

Chapter: Settings

## Chapter: Settings

# Settings

## IP and Port
                        	 Settings

Use the IP Settings option to view and change IP and port setting for the Ethernet connection on the subsequent node and configure the IP address of the publisher .

This section contains the following topics:

Change IP Settings

View Publisher IP Settings

Update the values in the fields only if you are changing the IP address. IP address and Host name change is not supported in Unified CCX 9.0(x) .

For detailed instructions about changing the IP address of servers in a cluster, see the Cisco Unified Communications Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR .

### Change IP
                           	 Settings

Use the IP
                                    			 Settings window to change or view the related Ethernet IP addresses,
                                 		  as well as the IP address for the network gateway.

All
                                 		  Ethernet settings apply to ethernet interface Eth0 or Eth1. You cannot
                                 		  configure any settings for Eth1. The Maximum Transmission Unit (MTU) on Eth0
                                 		  defaults to 1500.

For detailed instructions about changing the IP address of servers in a cluster, see the Cisco Unified Communications Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR , available here:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html

### IPv6
                           	 Configuration

Use the Ethernet
                                    			 Ipv6 Configuration page to enable or disable IPv6 address.

To enable
                                 		  or disable IPv6 address, follow this procedure:

From the Cisco Unified Communications Operating System Administration page, navigate to Settings > IP > Ethernet Ipv6 .

To enable or disable IPv6 address, check or uncheck the Enable IPv6 checkbox.

Enter the values for IPv6 Address , Subnet Mask , and the Default Gateway fields.

To reboot after you save the changes, check the Update with Reboot check box.

Click Save button to save the changes.

#### What to do next

If you have enabled IPv6 address, then add the IPv6 address in the Unified CCX Administration page immediately after server is restarted. If you have disabled IPv6 address, then remove the IPv6 address in the Unified CCX Administration page immediately after server is restarted.

For more information, see the Access Server Menu chapter in , available here:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html

### View Publisher IP
                           	 Settings

You can
                                 		  view the IP address of the first node or publisher for the node on the
                                 		  subsequent node.

Update the values in the fields only if you are changing the IP address. For detailed instructions about changing the IP address
                                             of servers in a cluster, see the Cisco Unified CCX Administration Guide .

To view the
                                 		  publisher IP settings, follow this procedure:

From the Cisco
                                          			 Unified Communications Operating System Administration window, navigate to Settings > IP > Publisher .

The Publisher Settings window appears.

You can view
                                                         				  the publisher IP address only on the subsequent node of the cluster, not on the
                                                         				  publisher itself.

## Configure NTP Servers

Ensure that external NTP servers are stratum 9 or higher
                              		  (1-9). To add, delete, or modify an external NTP server, follow this procedure:

You can only configure the NTP server settings on the first node or
                                          			 publisher.

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > NTP
                                             				  Servers .

Add, delete, or modify an NTP server:

To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node must 
                                                      				  be NTP v4 (version 4). If you are using IPv6 addressing, external NTP servers
                                                      				  must be NTP v4.

- To delete an NTP
                                          				server, select the check box in front of the appropriate server, and then click Delete .

- To add an NTP
                                          				server, click Add , enter the hostname or IP address, and
                                          				then click Save .

- To modify an NTP
                                          				server, click the IP address, modify the hostname or IP address, and then click Save .

Any change that you make to the NTP servers can take up to 5
                                                      				  minutes to complete. Whenever you make any change to the NTP servers, you must
                                                      				  refresh the window to view the correct status.

To refresh the NTP Server Settings window and view the
                                       			 correct status, choose Settings > NTP .
                                       			 After deleting, modifying, or adding the NTP server, you must restart the other
                                       			 node in the cluster for the changes to take effect.

## Set SMTP settings

Use the SMTP Settings window to view or set the
                              		  SMTP hostname and determine if the SMTP host is active.

If you want the system to send you e-mail, you must configure an SMTP
                                          			 host.

To access the SMTP settings, follow this procedure:

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > SMTP .

Enter or modify the SMTP hostname or IP address.

Click Save .

## Set Time

To manually
                              		  configure the time, follow this procedure:

The time cannot be
                                          			 set if NTP is currently enabled. Before you can manually configure the server
                                          			 time, you must delete any NTP servers that you configured.

If you enter a
                                          			 time that is before the time when Unified CCX was
                                          			 installed on the server, the digital certificates that the server uses for
                                          			 security become invalid, causing the webserver (Tomcat) to stop working. If
                                          			 this happens, you must regenerate the certificates.

From the Cisco
                                       			 Unified Communications Operating System Administration window, navigate to Settings > Time .

Enter the date
                                       			 and time for the system.

Click Save .

On a Unified CCX server, if you changed the date or if you changed the time by more than two
                                       			 minutes, use the CLI command utils
                                          				system restart to restart the server.

| Step 1 | From the Cisco Unified Communications Operating System Administration page, navigate to Settings > IP > Ethernet Ipv6 . |
|---|---|
| Step 2 | To enable or disable IPv6 address, check or uncheck the Enable IPv6 checkbox. |
| Step 3 | Enter the values for IPv6 Address , Subnet Mask , and the Default Gateway fields. |
| Step 4 | To reboot after you save the changes, check the Update with Reboot check box. |
| Step 5 | Click Save button to save the changes. |

| Note | Update the values in the fields only if you are changing the IP address. For detailed instructions about changing the IP address
                                             of servers in a cluster, see the Cisco Unified CCX Administration Guide . |
|---|---|

| From the Cisco
                                          			 Unified Communications Operating System Administration window, navigate to Settings > IP > Publisher . The Publisher Settings window appears. Note You can view
                                                         				  the publisher IP address only on the subsequent node of the cluster, not on the
                                                         				  publisher itself. | Note | You can view
                                                         				  the publisher IP address only on the subsequent node of the cluster, not on the
                                                         				  publisher itself. |
|---|---|---|
| Note | You can view
                                                         				  the publisher IP address only on the subsequent node of the cluster, not on the
                                                         				  publisher itself. |

| Note | You can view
                                                         				  the publisher IP address only on the subsequent node of the cluster, not on the
                                                         				  publisher itself. |
|---|---|

| Note | You can only configure the NTP server settings on the first node or
                                          			 publisher. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > NTP
                                             				  Servers . The NTP Server Settings window appears. |
|---|---|
| Step 2 | Add, delete, or modify an NTP server: Note To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node must 
                                                      				  be NTP v4 (version 4). If you are using IPv6 addressing, external NTP servers
                                                      				  must be NTP v4. To delete an NTP
                                          				server, select the check box in front of the appropriate server, and then click Delete . To add an NTP
                                          				server, click Add , enter the hostname or IP address, and
                                          				then click Save . To modify an NTP
                                          				server, click the IP address, modify the hostname or IP address, and then click Save . Note Any change that you make to the NTP servers can take up to 5
                                                      				  minutes to complete. Whenever you make any change to the NTP servers, you must
                                                      				  refresh the window to view the correct status. | Note | To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node must 
                                                      				  be NTP v4 (version 4). If you are using IPv6 addressing, external NTP servers
                                                      				  must be NTP v4. | Note | Any change that you make to the NTP servers can take up to 5
                                                      				  minutes to complete. Whenever you make any change to the NTP servers, you must
                                                      				  refresh the window to view the correct status. |
| Note | To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node must 
                                                      				  be NTP v4 (version 4). If you are using IPv6 addressing, external NTP servers
                                                      				  must be NTP v4. |
| Note | Any change that you make to the NTP servers can take up to 5
                                                      				  minutes to complete. Whenever you make any change to the NTP servers, you must
                                                      				  refresh the window to view the correct status. |
| Step 3 | To refresh the NTP Server Settings window and view the
                                       			 correct status, choose Settings > NTP .
                                       			 After deleting, modifying, or adding the NTP server, you must restart the other
                                       			 node in the cluster for the changes to take effect. |

| Note | To avoid potential compatibility, accuracy, and network jitter
                                                      				  problems, the external NTP servers that you specify for the primary node must 
                                                      				  be NTP v4 (version 4). If you are using IPv6 addressing, external NTP servers
                                                      				  must be NTP v4. |
|---|---|

| Note | Any change that you make to the NTP servers can take up to 5
                                                      				  minutes to complete. Whenever you make any change to the NTP servers, you must
                                                      				  refresh the window to view the correct status. |
|---|---|

| Tip | If you want the system to send you e-mail, you must configure an SMTP
                                          			 host. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Settings > SMTP . The SMTP Settings window appears. |
|---|---|
| Step 2 | Enter or modify the SMTP hostname or IP address. |
| Step 3 | Click Save . |

| Note | The time cannot be
                                          			 set if NTP is currently enabled. Before you can manually configure the server
                                          			 time, you must delete any NTP servers that you configured. |
|---|---|

| Caution | If you enter a
                                          			 time that is before the time when Unified CCX was
                                          			 installed on the server, the digital certificates that the server uses for
                                          			 security become invalid, causing the webserver (Tomcat) to stop working. If
                                          			 this happens, you must regenerate the certificates. |
|---|---|

| Step 1 | From the Cisco
                                       			 Unified Communications Operating System Administration window, navigate to Settings > Time . |
|---|---|
| Step 2 | Enter the date
                                       			 and time for the system. |
| Step 3 | Click Save . |
| Step 4 | On a Unified CCX server, if you changed the date or if you changed the time by more than two
                                       			 minutes, use the CLI command utils
                                          				system restart to restart the server. |