---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-configuration-gui-f46adb1ef1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/configuration/guide/ccvp_b_configuration-guide-12-5-1/ccvp_b_configuration-guide-12-5-1_chapter_01110.html
retrieved_at: 2026-08-21T17:07:53.076924+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: SIP Proxy Server Configuration

## Chapter: SIP Proxy Server Configuration

# SIP Proxy Server Configuration

## Configure SIP Proxy Server

Step 1

Log in to  Operations Console and click Device Management > SIP Proxy Server .

Step 2

Click Add New to add a new SIP Proxy server or click Use As Template to use the existing  SIP Proxy server  from the list of available SIP Proxy servers.

Step 3

Click the following tabs and modify the default values of fields, if required:

General . See General Settings .

Device Pool . See Add or Remove Device From Device Pool . For information on Device Pool, see Device Pool .

Step 4

Click Save .

## SIP Proxy Server Settings

### General Settings

To configure the general settings of SIP Proxy server, on the General tab, enter or modify the field values, as listed in the following table:

Field

Description

Default

Range

Restart Required

General

IP Address

The IP address of a SIP Proxy server.

None

Valid IP address

Not Applicable

Hostname

The host name of the SIP Proxy server.

None

Valid DNS name includes uppercase and lowercase letters, the numbers 0 through 9, and a dash.

Not Applicable

Device Type

The type of proxy server.

Depending on the option selected, the Enable Serviceability fields change. See the Enable Serviceability options for details.

Cisco Unified SIP Proxy

Cisco Unified SIP Proxy
                                             						and Cisco Unified Presence.

Not Applicable

Description

The description of the SIP Proxy server.

None

Up to 1,024 characters.

Not Applicable

Device Admin URL

The Administration URL of SIP Proxy server.

None

A valid URL.

The user interface (UI) validates the URL for syntax
                                                         						  errors.  
                                                         						However, it cannot validate a URL for website existence.

Not Applicable

Enable Serviceability

Enable Serviceability

Check this check box to enable serviceability for SIP Proxy server.

Not Applicable

Unchecked

Not Applicable

Username

The username required to log in to the proxy server
                                             						  Serviceability.

Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore.

Not Applicable

Not Applicable

Port

The port on which Serviceability is configured on the SIP
                                             						  Proxy.

1 to 65535

8443

Not Applicable

(For Device Type: Cisco Unified SIP Proxy)

User Password

Enter a password. This is the first level of authentication for IOS.

Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore.

Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore.

Not Applicable

Enable Password

The password required to log in to SIP Proxy
                                             						  Serviceability. This is the second level of authentication for IOS.

Must be same as password on the SIP Proxy.

Not Applicable

Not Applicable

(For Device Type: Cisco Unified SIP Presence)

Password

Enter a password.

Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore.

Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore.

Not Applicable

Confirm Password

The password required to log in to SIP Proxy Serviceability.

Must be same as password on the SIP Proxy.

Not Applicable

Not Applicable

### Add SIP Proxy Server to Device Pool

See Add or Remove Device From Device Pool . For information on Device Pool, see Device Pool .

## Configuration

If only a
                           		single SIP Proxy Server is needed for outbound call routing from the Call
                           		Server, choose the SIP Proxy configuration when configuring the SIP Service. In
                           		the Unified CVP Operations Console Server, configure the following:

Add a SIP Proxy
                                 			 Server and specify the IP address of the server.

Under the
                           		Call Server SIP Service settings, configure the following:

Enable Outbound
                                 			 Proxy = True

Use DNS SRV type
                                 			 query = False

Outbound Proxy
                                 			 Host = SIP Proxy Server configured above

When using
                           		multiple SIP Proxy Servers for outbound redundancy from the Call Server,
                           		configure the SIP Proxy with a DNS name and configure DNS SRV records in order
                           		to reach the SIP Proxy Servers. The DNS SRV records can exist on an external
                           		DNS Server, or they can be configured in a local DNS SRV record on each CVP
                           		server. In the OAMP Console, configure the following:

Add a SIP Proxy
                                 			 Server and specify DNS name of the server.

Under SIP
                           		Service configuration, configure the following:

Enable Outbound
                                 			 Proxy = True

Use DNS SRV type
                                 			 query = True

The DNS SRV record should then be configured with the list of SIP
                                 			 Proxy Servers.

To
                           		configure the Local DNS SRV record on each server, under the SIP service
                           		configuration, check Resolve SRV
                              		  records locally .

To use a
                           		server group for redundant Proxy Servers:

Select resolve SRV
                                    				records locally and enter the name of the server group for the outbound
                                 			 proxy domain name.

Under System >
                                    				Server Groups , create a new server group with two proxy servers that have
                                 			 priority 1 and 2.

Deploy the
                                 			 server group configuration to the Call Server.

| Step 1 | Log in to  Operations Console and click Device Management > SIP Proxy Server . |
|---|---|
| Step 2 | Click Add New to add a new SIP Proxy server or click Use As Template to use the existing  SIP Proxy server  from the list of available SIP Proxy servers. |
| Step 3 | Click the following tabs and modify the default values of fields, if required: General . See General Settings . Device Pool . See Add or Remove Device From Device Pool . For information on Device Pool, see Device Pool . |
| Step 4 | Click Save . |

| Field | Description | Default | Range | Restart Required |
|---|---|---|---|---|
| General |
| IP Address | The IP address of a SIP Proxy server. | None | Valid IP address | Not Applicable |
| Hostname | The host name of the SIP Proxy server. | None | Valid DNS name includes uppercase and lowercase letters, the numbers 0 through 9, and a dash. | Not Applicable |
| Device Type | The type of proxy server. Note Depending on the option selected, the Enable Serviceability fields change. See the Enable Serviceability options for details. | Note | Depending on the option selected, the Enable Serviceability fields change. See the Enable Serviceability options for details. | Cisco Unified SIP Proxy | Cisco Unified SIP Proxy
                                             						and Cisco Unified Presence. | Not Applicable |
| Note | Depending on the option selected, the Enable Serviceability fields change. See the Enable Serviceability options for details. |
| Description | The description of the SIP Proxy server. | None | Up to 1,024 characters. | Not Applicable |
| Device Admin URL | The Administration URL of SIP Proxy server. | None | A valid URL. Note The user interface (UI) validates the URL for syntax
                                                         						  errors.  
                                                         						However, it cannot validate a URL for website existence. | Note | The user interface (UI) validates the URL for syntax
                                                         						  errors.  
                                                         						However, it cannot validate a URL for website existence. | Not Applicable |
| Note | The user interface (UI) validates the URL for syntax
                                                         						  errors.  
                                                         						However, it cannot validate a URL for website existence. |
| Enable Serviceability |
| Enable Serviceability | Check this check box to enable serviceability for SIP Proxy server. | Not Applicable | Unchecked | Not Applicable |
| Username | The username required to log in to the proxy server
                                             						  Serviceability. | Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore. | Not Applicable | Not Applicable |
| Port | The port on which Serviceability is configured on the SIP
                                             						  Proxy. | 1 to 65535 | 8443 | Not Applicable |
| (For Device Type: Cisco Unified SIP Proxy) |
| User Password | Enter a password. This is the first level of authentication for IOS. | Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore. | Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore. | Not Applicable |
| Enable Password | The password required to log in to SIP Proxy
                                             						  Serviceability. This is the second level of authentication for IOS. | Must be same as password on the SIP Proxy. | Not Applicable | Not Applicable |
| (For Device Type: Cisco Unified SIP Presence) |
| Password | Enter a password. | Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore. | Valid names containing uppercase and lowercase alphanumeric
                                             						  characters, period, dash and underscore. | Not Applicable |
| Confirm Password | The password required to log in to SIP Proxy Serviceability. | Must be same as password on the SIP Proxy. | Not Applicable | Not Applicable |

| Note | Depending on the option selected, the Enable Serviceability fields change. See the Enable Serviceability options for details. |
|---|---|

| Note | The user interface (UI) validates the URL for syntax
                                                         						  errors.  
                                                         						However, it cannot validate a URL for website existence. |
|---|---|