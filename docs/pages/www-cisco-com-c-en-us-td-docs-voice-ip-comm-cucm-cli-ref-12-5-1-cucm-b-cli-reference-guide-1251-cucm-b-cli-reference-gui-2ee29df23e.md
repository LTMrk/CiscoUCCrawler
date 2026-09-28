---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1-cucm-b-cli-reference-guide-1251-cucm-b-cli-reference-gui-2ee29df23e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1/cucm_b_cli-reference-guide-1251/cucm_b_cli-reference-guide-1251_chapter_0100.html
retrieved_at: 2026-08-16T23:54:47.652283+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)

Updated: August 26, 2025

Chapter: License
	 Commands

## Chapter: License
	 Commands

# License
                     	 Commands

## license smart
                        	 deregister

Use this command to unregister smart licensing on Unified Communications Manager and remove the product from Cisco Smart Software Manager.

license smart deregister

### Command Modes

Administrator (admin)

### Requirements

Command privilege
                              		  level: 4

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart
                        	 register idtoken <token> [force]

Use this command to register Unified Communications Manager with Cisco Smart Software Manager using an ID token.

license smart register idtoken <token>
                                 				  [force]

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 4

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart
                        	 renew auth

Use this command
                              		  to manually renew the license usage information .

license smart renew auth

### Command Modes

Administrator (admin)

### Requirements

Command privilege
                              		  level: 4

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart
                        	 renew ID

Use this command
                              		  to manually renew the license registration.

license smart renew ID

### Command Modes

Administrator (admin)

### Requirements

Command privilege
                              		  level: 4

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart transport direct

Use the following command to configure the Smart Licensing feature to send license usage information directly to Cisco Smart
                              Software Manager. This is a default setting.

license smart transport direct

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager

The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                          satellite.

## license smart transport gateway <URL> (Applicable Until Release 14SU4 and 15SU2)

Use the following command to configure the Smart Licensing feature to send license usage information to Cisco Smart Software
                              Manager through an on-premise Transport Gateway or Smart Software Manager satellite . The setting is used when the product does not have internet access.

license smart transport gateway <URL>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager

## license smart transport gateway <URL> (Applicable From Release 14SU4 and 15SU2 Onwards)

Use the following command to configure the Smart Licensing feature to send license usage information to Cisco Smart Software
                              Manager through an on-premise Transport Gateway. The setting is used when the product does not have internet access.

license smart transport gateway <URL>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager

## license smart transport proxy  <proxy-server> <proxy-port>

Use the following command to configure the Smart Licensing feature to communicate with Cisco Smart Software Manager through
                              an HTTP or HTTPS Proxy:

<proxy-server> - Proxy Server IP Address/HostName

<proxy-port> - Proxy Server Port

license smart transport proxy <proxy-server> <proxy-port>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager

The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager.

## license smart reservation enable

Use this command to enable the license reservation feature.

license smart reservation enable

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart reservation disable

Use this command to disable the license reservation feature.

license smart reservation disable

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart reservation request

Use this command to generate reservation request code from Unified Communications Manager product.

license smart reservation request

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart reservation cancel

Use this command to cancel the reservation process before the authorization code obtained from Cisco Smart Software Manager
                              against the Product request code is installed.

license smart reservation cancel

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart reservation install "<authorization-code>"

Use this command to install the license reservation authorization-code generated on the Cisco Smart Software Manager.

license smart reservation install "<authorization-code>"

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart reservation install-file <url>

Use this command to install the license reservation authorization-code file generated on the Cisco Smart Software Manager.

license smart reservation install-file <url>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

url is mandatory Path to the authorization-code file on SFTP server in below format:

sftp://<HostName/IP>:<port>/<Path to Authorization-Code file>

## license smart reservation return

Use this command to generate a return code that must be entered into the Cisco Smart Software Manager to return the licenses
                              to the virtual account pool.

license smart reservation return

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## license smart reservation return authorization "<authorization-code>"

Use this command to generate a return code using the authorization code specified on the command line. The return code must
                              be entered into the Cisco Smart Software Manager to return the licenses to the virtual account pool.

license smart reservation return authorization "<authorization-code>"

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                          satellite. |
|---|---|

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                       satellite. |
|---|---|

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                       satellite. |
|---|---|

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager. |
|---|---|

| Note | url is mandatory Path to the authorization-code file on SFTP server in below format: sftp://<HostName/IP>:<port>/<Path to Authorization-Code file> |
|---|---|