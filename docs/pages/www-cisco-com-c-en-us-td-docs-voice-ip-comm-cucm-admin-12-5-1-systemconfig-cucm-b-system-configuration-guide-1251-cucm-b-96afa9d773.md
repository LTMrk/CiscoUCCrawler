---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-96afa9d773
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011.html
retrieved_at: 2026-08-16T17:29:38.588315+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Server Information

## Chapter: Configure Server Information

# Configure Server Information

## System Information
                        	 Overview

This chapter describes how to configure the properties of the Unified Communications Manager node.

All Unified Communications products such as Unified Communications Manager, Cisco Unity Connections, and Cisco IM and Presence,
                                          and so on, have only one interface. Thus, you can assign only one IP address for each of these products.

## Server Configuration Task Flow

Step 1

Configure Server Information

Specify a name for the Unified Communications Manager node, and add a description.

Step 2

Configure Ports

Configure
                                          		  the following ports:

Ethernet Phone
                                                				Port

MGCP Listen
                                                				Port

MGCP
                                                				Keep-alive Port

SIP Phone Port

SIP Phone
                                                				Secure Port

### Configure Server Information

Specify a name for the Unified Communications Manager node, and add a description. You can also use this procedure to view the following read-only information:

The computer telephony integration identification (CTI ID).

The server where this Unified Communications Manager is installed.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, select System > Cisco Unified CM .

Step 2

Enter the
                                          			 appropriate search criteria and click Find .

Step 3

Select the Cisco
                                             				Unified CM that you want to view.

Step 4

In the Name field, enter the name that you want to assign to this Cisco Unified Communications Manager .

Step 5

In the Description field, enter a description for the node.

The description can include up to 50 characters in any language, but it cannot include double-quotes ("), percentage sign
                                             (%), ampersand (&), back-slash (\), or angle brackets (<>).

Step 6

Click Save .

### Configure Ports

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, select System > Cisco Unified CM .

Step 2

Enter the
                                          			 appropriate search criteria and click Find .

Step 3

Select the Cisco
                                             				Unified CM that you want to view.

Step 4

Navigate to
                                          			 the Cisco
                                             				Unified Communications Manager TCP Port Settings for this Server section.

Step 5

Click Save .

Step 6

Click Apply
                                             				Config .

Step 7

Click OK .

#### Port
                              	 Settings

Field

Description

Ethernet
                                                						Phone Port

The system uses this TCP port to communicate with the Cisco Unified IP Phone s (SCCP only) on the network.

Accept the default port value of 2000 unless this port is already in use on your system. Choosing 2000 identifies this port
                                                      as non-secure.

Ensure all port entries are unique.

Valid port numbers range from 1024 to 49151.

MGCP
                                                						Listen Port

The
                                                						system uses this TCP port to detect messages from its associated MGCP gateway.

Accept the default port of 2427 unless this port is already in use on your system.

Ensure all port entries are unique.

Valid port numbers range from 1024 to 49151.

MGCP
                                                						Keep-alive Port

The
                                                						system uses this TCP port to exchange keepalive messages with its associated
                                                						MGCP gateway.

Accept the default port of 2428 unless this port is already in use on your system.

Ensure all port entries are unique.

Valid port numbers range from 1024 to 49151.

SIP
                                                						Phone Port

This field specifies the port number that Unified Communications Manager uses to listen for SIP line registrations over TCP and UDP.

SIP
                                                						Phone Secure Port

This field specifies the port number that the system uses to listen for SIP line registrations over TLS.

SIP Phone OAuth Port

This field specifies the port number that Cisco Unified Communications Manager uses to listen for SIP line registrations from
                                                Jabber On-Premise devices over TLS (Transport Layer Security). The default value is 5090. Range is 1024 to 49151.

SIP Mobile and Remote Access OAuth Port

This field specifies the port number that Cisco Unified Communications Manager uses to listen for SIP line registrations from
                                                Jabber over Expressway through MTLS (Mutual Transport Layer Security). The default value is 5091. Range is 1024 to 49151.

## Hostname Configuration

Table5-2 lists the locations where you can configure a host name for the Unified Communications Manager server, the allowed
                              number of characters for the host name, and the recommended first and last characters for the host name. Be aware that if
                              you do not configure the host name correctly, some components in Unified Communications Manager, such as the operating system,
                              database, installation, and so on, may not work as expected.

Caution

Before you change the host name or IP address for any locations that are listed in Table5-2, see Changing the IP Address and
                                          Host Name for Unified Communications Manager 8.5(1). Failing to update the host name or IP address correctly after it is configured
                                          may cause problems for Unified Communications Manager.

Host Name Location

Allowed Configuration

Allowed Number of Characters

Recommended First Character for Host Name

Recommended Last Character for Host Name

Host Name/ IP Address field

System > Server in Cisco Unified Communications Manager Administration

You can add or change the host name for a server.

2-63

alphabetic

alphanumeric

Hostname field

Cisco Unified Communications Manager installation

You can add the host name for a server.

1-63

alphabetic

alphanumeric

Hostname field

Settings > IP > Ethernet in Cisco Unified Communications Operating System

You can change, not add, the host name for a server.

1-63

alphabetic

alphanumeric

set network hostname hostname

Command Line Interface

You can change, not add, the host name for a server.

1-63

alphabetic

alphanumeric

Tip

The host name must follow the rules for ARPANET host names. Between
                                          			 the first and last character of the host name, you can enter alphanumeric
                                          			 characters and hyphens.

Before you configure the host name in any location in
                              		  Table5-2, review the following information:

In this field, only configure a host name if  Unified Communications Manager can access the DNS server to resolve host names
                                    to IP addresses; make sure that you configure the Unified Communications Manager name and address information on the DNS server.

Tip

In addition to configuring Unified Communications Manager information on the DNS server, you enter DNS information during
                                          the Unified Communications Manager installation.

| Note | All Unified Communications products such as Unified Communications Manager, Cisco Unity Connections, and Cisco IM and Presence,
                                          and so on, have only one interface. Thus, you can assign only one IP address for each of these products. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Server Information | Specify a name for the Unified Communications Manager node, and add a description. |
| Step 2 | Configure Ports | Configure
                                          		  the following ports: Ethernet Phone
                                                				Port MGCP Listen
                                                				Port MGCP
                                                				Keep-alive Port SIP Phone Port SIP Phone
                                                				Secure Port |

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, select System > Cisco Unified CM . The Find
                                             				and List Cisco Unified CMs window appears. |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria and click Find . All
                                          			 matching Cisco Unified Communications Managers are displayed. |
| Step 3 | Select the Cisco
                                             				Unified CM that you want to view. The Cisco
                                             				Unified CM Configuration window appears. |
| Step 4 | In the Name field, enter the name that you want to assign to this Cisco Unified Communications Manager . |
| Step 5 | In the Description field, enter a description for the node. The description can include up to 50 characters in any language, but it cannot include double-quotes ("), percentage sign
                                             (%), ampersand (&), back-slash (\), or angle brackets (<>). |
| Step 6 | Click Save . |

| Note | Normally, you need not change the default port settings. Use this procedure only if you really want to change the defaults. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, select System > Cisco Unified CM . The Find
                                             				and List Cisco Unified CMs window appears. |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria and click Find . All
                                          			 matching Cisco Unified Communications Managers are displayed. |
| Step 3 | Select the Cisco
                                             				Unified CM that you want to view. The Cisco
                                             				Unified CM Configuration window appears. |
| Step 4 | Navigate to
                                          			 the Cisco
                                             				Unified Communications Manager TCP Port Settings for this Server section. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                             				Config . |
| Step 7 | Click OK . |

| Field | Description |
|---|---|
| Ethernet
                                                						Phone Port | The system uses this TCP port to communicate with the Cisco Unified IP Phone s (SCCP only) on the network. Accept the default port value of 2000 unless this port is already in use on your system. Choosing 2000 identifies this port
                                                      as non-secure. Ensure all port entries are unique. Valid port numbers range from 1024 to 49151. |
| MGCP
                                                						Listen Port | The
                                                						system uses this TCP port to detect messages from its associated MGCP gateway. Accept the default port of 2427 unless this port is already in use on your system. Ensure all port entries are unique. Valid port numbers range from 1024 to 49151. |
| MGCP
                                                						Keep-alive Port | The
                                                						system uses this TCP port to exchange keepalive messages with its associated
                                                						MGCP gateway. Accept the default port of 2428 unless this port is already in use on your system. Ensure all port entries are unique. Valid port numbers range from 1024 to 49151. |
| SIP
                                                						Phone Port | This field specifies the port number that Unified Communications Manager uses to listen for SIP line registrations over TCP and UDP. |
| SIP
                                                						Phone Secure Port | This field specifies the port number that the system uses to listen for SIP line registrations over TLS. |
| SIP Phone OAuth Port | This field specifies the port number that Cisco Unified Communications Manager uses to listen for SIP line registrations from
                                                Jabber On-Premise devices over TLS (Transport Layer Security). The default value is 5090. Range is 1024 to 49151. |
| SIP Mobile and Remote Access OAuth Port | This field specifies the port number that Cisco Unified Communications Manager uses to listen for SIP line registrations from
                                                Jabber over Expressway through MTLS (Mutual Transport Layer Security). The default value is 5091. Range is 1024 to 49151. |

| Caution | Before you change the host name or IP address for any locations that are listed in Table5-2, see Changing the IP Address and
                                          Host Name for Unified Communications Manager 8.5(1). Failing to update the host name or IP address correctly after it is configured
                                          may cause problems for Unified Communications Manager. |
|---|---|

| Host Name Location | Allowed Configuration | Allowed Number of Characters | Recommended First Character for Host Name | Recommended Last Character for Host Name |
|---|---|---|---|---|
| Host Name/ IP Address field System > Server in Cisco Unified Communications Manager Administration | You can add or change the host name for a server. | 2-63 | alphabetic | alphanumeric |
| Hostname field Cisco Unified Communications Manager installation | You can add the host name for a server. | 1-63 | alphabetic | alphanumeric |
| Hostname field Settings > IP > Ethernet in Cisco Unified Communications Operating System | You can change, not add, the host name for a server. | 1-63 | alphabetic | alphanumeric |
| set network hostname hostname Command Line Interface | You can change, not add, the host name for a server. | 1-63 | alphabetic | alphanumeric |

| Tip | The host name must follow the rules for ARPANET host names. Between
                                          			 the first and last character of the host name, you can enter alphanumeric
                                          			 characters and hyphens. |
|---|---|

| Tip | In addition to configuring Unified Communications Manager information on the DNS server, you enter DNS information during
                                          the Unified Communications Manager installation. |
|---|---|