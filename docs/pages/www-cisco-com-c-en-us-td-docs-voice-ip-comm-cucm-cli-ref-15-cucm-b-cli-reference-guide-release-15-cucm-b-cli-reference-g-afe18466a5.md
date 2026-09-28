---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-15-cucm-b-cli-reference-guide-release-15-cucm-b-cli-reference-g-afe18466a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/15/cucm_b_cli_reference_guide_release_15/cucm_b_cli_reference_guide_release_1401_chapter_0100.html
retrieved_at: 2026-08-16T23:52:58.251249+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 15 and SUs

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 15 and SUs

Updated: April 6, 2026

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

When user gets the prompt Do you want to enable Authentication based proxy? Yes/No

Enter "Yes" if you want to register Unified Communication Manager with Cisco Smart Software Manager using authentication based
                                          proxy server.

### Example

```
admin:license smart transport proxy <proxy-server> <proxy-port>

Do you want to enable Authentication based proxy ? y/n y
User Name : xyz
Password: *********
```

Result: Transport settings updated successfully.

## license smart transport ssm-satellite <URL> (Release 14SU4 and 15SU2 onwards)

Use the following command to configure the Smart Licensing feature to send license usage information to an on-premise Smart
                              Software Manager satellite. This setting is used when the product does not have any access to the Internet.

license smart transport ssm-satellite <URL>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager

## license smart factory reset

Use this command to clear all licensing information from the trusted store and memory, except the evaluation period count
                              down and the Specific License Reservation (SLR) sequence number.

license smart factory reset

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Cisco Unified Communications Manager

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

## license smart reservation set license_count

Use this command to configure or update the license count for the system to operate within when Permanent License Reservation
                              is enabled. License count configured using this CLI does not affect compliance status and is for administrator reference only.
                              The license count set by admin using the CLI will be displayed on the Unified Communications Manager License Management UI
                              screen.

license smart reservation set license_count

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Emergency Responder, and Cisco Unity Connection

## license smart export request local <exportfeaturename>

Use this command to allow user with Smart Account for whom Export Restrictions apply, to request a regulatory export license
                              from Cisco Smart Software Manager or satellite.

The command returns an export authorization key if regulatory Export License is available from Cisco Smart Software Manager
                              or satellite and enable export-controlled functionality on the product.

license smart export request local <exportfeaturename>

Export restricted feature name for Unified Communications Manager is <CUCM_Export_Restricted_Authorization_Key>

Export restricted feature name for Cisco Unity Connection is <CUC_Export_Restricted_Authorization_Key>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Cisco Unified Communications Manager, Cisco Unity Connection.

## license smart export return local <exportfeaturename>

Use this command to allow a return, previously requested export restricted license to Cisco Smart Software Manager or satellite.
                              The export authorization key for the export restricted feature is removed from the system.

license smart export return local <exportfeaturename>

Export restricted feature name for Unified Communications Manager is <CUCM_Export_Restricted_Authorization_Key>

Export restricted feature name for Cisco Unity Connection is <CUC_Export_Restricted_Authorization_Key>

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Cisco Unified Communications Manager, Cisco Unity Connection.

## license smart export cancel

Use this command to allow user with Smart Account for whom Export Restrictions apply, to cancel the automatic retry of previously
                              failed export request or return from Cisco Smart Software Manager or satellite.

license smart export cancel

### Command Modes

Administrator (admin)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Cisco Unified Communications Manager, Cisco Unity Connection.

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                          satellite. |
|---|---|

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                       satellite. |
|---|---|

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager or
                                       satellite. |
|---|---|

| Note | This command is executed to configure the Transport Gateway URL. This command cannot be executed on Unified Communications
                                       Manager using the Smart Transport mode for communication as Transport Gateway is not supported. Use the ‘license smart transport
                                       ssm-satellite <URL>’ CLI command to configure the satellite URL. Smart Transport gateway is not supported for freshly deployed
                                       Unified Communications Manager systems. |
|---|---|

| Note | You must use this command in case there are any issues with Smart Transport mode and wants to fall back to the Call Home mode
                                       post deregister. |
|---|---|

| Note | The following command is executed when Unified Communications Manager is unregistered with Cisco Smart Software Manager. |
|---|---|

| Note | When user gets the prompt Do you want to enable Authentication based proxy? Yes/No Enter "Yes" if you want to register Unified Communication Manager with Cisco Smart Software Manager using authentication based
                                          proxy server. |
|---|---|

| Note | url is mandatory Path to the authorization-code file on SFTP server in below format: sftp://<HostName/IP>:<port>/<Path to Authorization-Code file> |
|---|---|

| Note | Export restricted feature name for Unified Communications Manager is <CUCM_Export_Restricted_Authorization_Key> Export restricted feature name for Cisco Unity Connection is <CUC_Export_Restricted_Authorization_Key> |
|---|---|

| Note | Export restricted feature name for Unified Communications Manager is <CUCM_Export_Restricted_Authorization_Key> Export restricted feature name for Cisco Unity Connection is <CUC_Export_Restricted_Authorization_Key> |
|---|---|