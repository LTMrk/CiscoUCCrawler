---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-operating-system-guide-1-0-1-iptpch4-html-d3c4449845
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/operating_system/guide/1_0_1/iptpch4.html
retrieved_at: 2026-08-21T02:47:06.973812+00:00
---

Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

# Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Settings

## Chapter: Settings

## Settings

Use the Settings options to display and change IP settings, host settings, and Network Time Protocol (NTP) settings.

## IP Settings

The IP Settings options allow you to view and change IP and port setting for the Ethernet connection and, on subsequent nodes, to set the IP address of the publisher.

### Ethernet Settings

The IP Settings window indicates whether Dynamic Host Configuration Protocol (DHCP) is active and also provides the related Ethernet IP addresses, as well as the IP address for the network gateway.

To view or change the IP settings, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Settings>IP>Ethernet .

The Ethernet Settings window displays.

Step 2 To modify the Ethernet settings, enter the new values in the appropriate fields. For a description of the fields on the Ethernet Settings window, see Table 4-1 .

Note If you enable DHCP, then the Port and Gateway setting get disabled and cannot be changed.

Step 3 To preserve your changes, click Save .

Table 4-1 Ethernet Settings Fields and Descriptions

DHCP

Indicates whether DHCP is Enabled or Disabled.

Port Settings IP Address

Shows the IP address of the system.

Mask

Shows the IP subnet mask address.

Gateway IP Address

Shows the IP address of the network gateway.

### Publisher Settings

On subsequent or subscriber nodes, you can view or change the IP address of the first node or publisher for the node.

To view or change the publisher IP settings, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Settings>IP>Publisher .

The Publisher Settings window displays.

Note You can only view and change the publisher IP address on subsequent nodes of the cluster, not on the publisher itself.

Step 2 Enter the new publisher IP address.

Step 3 Click Save .

### Changing IP Address on a Subsequent Cisco Unified Presence Server Node

If the IP address of the first Cisco Unified Presence Server node gets changed while a subsequent node is offline, you may not be able to log in to Cisco Unified Presence Server Administration on the subsequent node. If this occurs, follow this procedure:

Step 1 Log in directly to operating system administration on the subsequent node by using the following IP address:

http:// server-name /iptplatform

where server-name specifies the host name or IP address of the subsequent node.

Step 2 Enter your Administrator user name and password and click Submit .

Step 3 Navigate to Settings>IP>Publisher .

Step 4 Enter the new IP address for the publisher and click Save .

Step 5 Restart the subsequent node.

## NTP Servers

To add, delete, or modify an external NTP server, follow this procedure:

Note You can only configure the NTP server settings on the first node or publisher.

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Settings>NTP Servers .

The NTP Server Settings window displays.

Step 2 You can add, delete, or modify an NTP server:

– To delete an NTP server, check the check box in front of the appropriate server and click Delete .

– To add an NTP server, click Add , enter the hostname or IP address, and then click Save .

– To modify an NTP server, click the IP address, modify the hostname or IP address, and then click Save .

Note Any change you make to the NTP servers can take up to five minutes to complete. Whenever you make any change to the NTP servers, you must refresh the window to display the correct status.

Step 3 To refresh the NTP Server Settings window and display the correct status, choose Settings>NTP .

Note After deleting, modifying, or adding NTP server, you must restart all the other nodes in the cluster for the changes to take affect.

## SMTP Settings

The SMTP Settings window allows you to view or set the SMTP hostname and indicates whether the SMTP host is active.

Tip If you want the system to send you e-mail, from the Certificate Expiry Monitor, for example, you must configure an SMTP host.

To access the SMTP settings, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Settings>SMTP .

The SMTP Settings window displays.

Step 2 Enter or modify the SMTP hostname or IP address.

Step 3 Click Save .

## Time Settings

To manually configure the time, follow this procedure:

Note Before you can manually configure the server time, you must delete any NTP servers that you have configured. See NTP Servers for more information.

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Settings>Time .

Step 2 Enter the date and time for the system.

Step 3 Click Save .

| Field | Description |
|---|---|
| DHCP | Indicates whether DHCP is Enabled or Disabled. |
| Port Settings IP Address | Shows the IP address of the system. |
| Mask | Shows the IP subnet mask address. |
| Gateway IP Address | Shows the IP address of the network gateway. |