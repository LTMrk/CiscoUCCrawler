---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-ed978a5f70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_security-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/encryption_support.html
retrieved_at: 2026-08-20T18:55:48.074470+00:00
---

Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Encryption Support

## Chapter: Encryption Support

# Encryption Support

## User and Agent
                        	 Passwords

When Single Sign-On (SSO) is enabled, it hands off the Agent and Supervisor authentications to a third party Identity Provider
                              (IDP). In such a case, the Agent and Supervisor passwords are not stored in the Unified CCE database.

When SSO is not enabled, the Agent
                              				and Supervisor passwords are stored in the configuration database with an MD5 hash.
                              				Unified CCE has mechanisms to protect data in transit, and options for protecting
                              				data at rest.

Administrator and Configuration user login uses credentials that are stored in Active Directory. These passwords are not stored
                              in the Unified CCE database. The exception is System Inventory, which allows centralized configuration and management of Unified
                              CCE services from a central location via CCE Administration web page. System Inventory requires credentials to manage and
                              get diagnostic information from other sub-systems in the Unified CCE Solution. These passwords are stored with AES 256-bit
                              encryption in the AW database.

CCE Admin web page users are authenticated using the Active Directory credentials.

CUIC reporting users can either use
                              				SSO or AD credentials to log on depending on whether SSO is enabled or not. If SSO
                              				is not enabled, then Supervisor reporting users use Active Directory authentication
                              				to gain access to reporting, and not the local MD5 password stored in the
                              				configuration database.

Unified CCE cannot read, set, or change user passwords in Active Directory. It is possible and likely that the Supervisor
                                          reporting users may use a password (their AD password) to login to CUIC that is different from their agent password set by
                                          the configuration administrator.

## Call Variables and Extended Call Variables

Call context variables in Unified CCE may contain sensitive data depending on how it is configured and scripted in your system
                              Peripheral. Variables between 1 to10 are stored in the Termination Call Detail records, and the Expanded Call Context (ECC)
                              variables are stored in the Termination Call Variable and Router Call Variable records on the Historical Data Server (HDS),
                              if the Persistent check box is checked.

These variables are neither encrypted in the memory nor when they are stored in the database. Therefore, be cautious about
                              the data you store in these variables. These variables are typically used for diagnostics and custom reporting only.

Unified CCE has strategies for encrypting the variables during transport and encrypting the drive where they are stored.

For more information, see About IPsec and Manage Secured PII in Transit .

## Internet Script
                        	 Editor

If you use Unified Contact Center Management Portal (Unified CCMP) or Unified Contact Center Domain Manager (Unified CCDM),
                                       you cannot use Transport Layer Security (TLS) v1.0 for Internet Script Editor.

The Internet Script Editor
                           		web application uses the TLS v1.2 protocol only which provides encryption using
                           		a cipher that the endpoints negotiate. All supervisor sign-ins, user sign-ins,
                           		and data exchanged is protected across the network.

For more information about enabling certain Cipher Suites in IIS, see the article https://docs.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings .

## Cisco Contact Center
                        	 SNMP Management Service

Unified ICM and Unified CCE include a Simple Network Management Protocol (SNMP v3) agent to support authentication and encryption
                              (privacy) provided by SNMP Research International. Our implementation exposes the configuration of the communication with a management station to be authenticated using the
                              SHA-256 digest algorithms. For all SNMP message encryption, our implementation uses one of the following protocols:

AES-192

AES-256

For more information, see the SNMP Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## TLS Encryption Support

External interfaces such as data center interfaces and external components such as Cisco Finesse, Customer Collaboration Platform , CVP, and Application Gateways support encryption using TLS.

### Supported TLS Cipher Suites

The following AES ciphers are used for encryption:

List of strongly recommeded ciphers

ECDHE-RSA-AES128-GCM-SHA256

ECDHE-ECDSA-AES128-GCM-SHA256

ECDHE-ECDSA-CHACHA20-POLY1305-SHA256

ECDHE-RSA-CHACHA20-POLY1305-SHA256

List of recommended ciphers

RSA-AES128-GCM-SHA256

ECDHE-ECDSA-AES256-GCM-SHA384

ECDHE-RSA-AES256-GCM-SHA384

RSA-AES256-GCM-SHA384

DHE-RSA-AES128-GCM-SHA256

DHE-RSA-AES256-GCM-SHA384

List of ciphers used for backward compatibility

DHE-RSA-AES128-CBC-SHA

DHE-RSA-AES128-CBC-SHA256

ECDHE-ECDSA-AES128-CBC-SHA256

ECDHE-ECDSA-AES128-CBC-SHA

ECDHE-RSA-AES128-CBC-SHA

ECDHE-RSA-AES128-CBC-SHA256

RSA-AES128-CBC-SHA256

RSA-AES128-CBC-SHA

ECDHE-ECDSA-AES256-CBC-SHA384

ECDHE-RSA-AES256-CBC-SHA384

RSA-AES256-CBC-SHA256

RSA-AES256-CBC-SHA

DHE-DSS-AES256-GCM-SHA384

DHE-RSA-AES256-CBC-SHA256

DHE-DSS-AES128-GCM-SHA256

DHE-DSS-AES128-CBC-SHA

DHE-DSS-AES128-CBC-SHA256

DHE-DSS-AES256-CBC-SHA256

ECDHE-RSA-AES256-CBC-SHA

ECDHE-RSA-AES128-GCM-SHA256

ECDHE-RSA-AES256-GCM-SHA384

ECDHE-RSA-AES128-SHA256

ECDHE-RSA-AES128-SHA

ECDHE-RSA-AES256-SHA384

AES128-GCM-SHA256

AES256-GCM-SHA384

AES128-SHA256

AES128-SHA

AES256-SHA256

DHE-RSA-AES128-GCM-SHA256

DHE-RSA-AES256-GCM-SHA384

DHE-RSA-AES128-SHA256

DHE-RSA-AES128-SHA

DHE-RSA-AES256-SHA256

TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

### TLS Cipher Suites Management

Ciphers are used to encrypt data to protect sensitive information. Ciphers enable secure communication over various networks.
                              Ciphers are part of the TLS handshake, which authenticates communication between a client and a webserver. Strong ciphers
                              are required to meet data protection regulations and industry standards. Ciphers are updated or replaced regularly to ensure
                              that the networks are not exposed to attacks and malicious actions. You can manage ciphers on both Windows and VOS systems.

#### Manage TLS Cipher Suites on Windows

You can add or remove the supported ciphers from the following registries for the server and client respectively:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\Cisco SSL Configuration\ServerCiphers

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\Cisco SSL Configuration\ClientCiphers

If the client and/or server cipher list was customized before the 15.0 upgrade, all the customised ciphers are retained post-upgrade.
                                                In such cases, manual configuration of the ciphers is needed to meet the Cisco recommended cipher list.

#### Manage TLS Cipher Suites on VOS systems

To keep the ciphers upto date, use the following commands that are applicable for VOS components Cisco VVB , Cisco Unified Intelligence Center , Cisco IdS , Finesse , and Cloud Connect :

The CLIs are node specific.

utils system tls_ciphers config list —Displays the current list of TLS ciphers.

utils system tls_ciphers config export —Exports the list of TLS ciphers that are configured in /usr/local/bin/base_scripts/tls_settings to an specified SFTP location.

utils system tls_ciphers config import —Imports the list of TLS ciphers from the specified SFTP server location and updates the configuration in /usr/local/bin/base_scripts/tls_settings .

utils system tls_ciphers config reset —Resets the TLS cipher configuration to the base version available with the product's standard release. This revokes any modifications
                                       made to the TLS cipher configuration by restoring it to the base version.

##### utils system tls_ciphers config list

Run this command to view the list of ciphers that are available. In a high availability (HA) deployment, run this CLI command
                                       on any one of the nodes in the cluster.

Command syntax

utils system tls_ciphers config list

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config list
 
TLS Cipher Configuration:

+----------------------+--------------------------------------------------+
| APR Cipher           | ALL:+HIGH:!ADH:!AECDH:!EXP:!PSK:!SRP:!LOW:!RC2     |
|                      | !3DES:!SEED:!RC4:!SSLv2:!IDEA:!CAMELLIA            |
|                      | !AES256-SHA:!ECDHE-RSA-AES256-SHA                  |
|                      | !DHE-RSA-AES256-SHA:!AES256-GCM-SHA384             |
|                      | !AES128-GCM-SHA256:!DHE-DSS-AES256-SHA:!AES128-SHA |
|                      | !RSA:!ARIA:!ECDHE-ECDSA-AES128-CCM                 |
|                      | !ECDHE-ECDSA-AES256-CCM:!ECDHE-ECDSA-AES128-CCM8   |
|                      | !ECDHE-ECDSA-AES256-CCM8                           |
|                      | !ECDHE-ECDSA-AES256-SHA384                         |
|                      | !ECDHE-ECDSA-AES128-SHA256:!ECDHE-ECDSA-AES256-SHA |
|                      | !ECDHE-ECDSA-AES128-SHA:!ECDHE-RSA-AES256-SHA384   |
|                      | !ECDHE-RSA-AES128-SHA256:!ECDHE-RSA-AES128-SHA     |
|                      | +ECDHE-RSA-CHACHA20-POLY1305                       |
|                      | +ECDHE-ECDSA-CHACHA20-POLY1305                     |
|                      | +ECDHE-RSA-AES128-GCM-SHA256                       |
|                      | +ECDHE-ECDSA-AES128-GCM-SHA256                     |
|                      | +ECDHE-RSA-AES256-GCM-SHA384                       |
|                      | +ECDHE-ECDSA-AES256-GCM-SHA384                     |
|                      | +DHE-RSA-AES128-GCM-SHA256                         |
|                      | +DHE-RSA-AES256-GCM-SHA384                         |
+----------------------+--------------------------------------------------+
+----------------------+--------------------------------------------------+
| JSSE RSA Cipher      | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256              |
|                      | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256        |
|                      | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384              |
|                      | TLS_DHE_RSA_WITH_AES_128_GCM_SHA256                |
|                      | TLS_DHE_RSA_WITH_AES_256_GCM_SHA384                |
+----------------------+--------------------------------------------------+
+----------------------+--------------------------------------------------+
| JSSE ECDSA Cipher    | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256            |
|                      | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256      |
|                      | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384            |
+----------------------+--------------------------------------------------+
```

##### utils system tls_ciphers config export

Run this command to export the TLS cipher list configured in the tls_settings file to a specified SFTP location. In a high availability (HA) deployment, run this CLI command on all the nodes of the cluster.

Command syntax

utils system tls_ciphers config export

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config export
 
You can export the TLS ciphers config data to an SFTP server location. Enter the details of the SFTP server:
 
Server:10.86.135.111
User:root
User's Password:********
Directory:/root
 
Successfully exported TLS cipher config data file: tls_settings_20240722104000
```

##### utils system tls_ciphers config import

Run this command to import the TLS cipher list from a specified SFTP server location and update the configuration in the tls_settings file. In a high availability (HA) deployment, run this CLI command on all the nodes of the cluster.

Command syntax

utils system tls_ciphers config import

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config import
Warning: This action will overwrite the current TLS cipher configuration.
Any changes to the TLS cipher settings can impact both the security and compatibility of the system.
Ensure that the new configuration meets all system security requirements without affecting functionality.
 
You can import the TLS ciphers config data from an SFTP server location. Enter the details of the SFTP server:
 
Server:10.86.135.111
User:root
User's Password:********
Directory:/root
Filename:tls_settings_update
 
Successfully imported TLS cipher config data file
 
Restart the system using the command 'utils system restart' for the changes to take effect
```

##### utils system tls_ciphers config reset

Run this command to reset the TLS cipher configuration to the base version available with the product's standard release.
                                       This will undo any modifications made to the TLS cipher configuration, restoring it to the base version. In a high availability
                                       (HA) deployment, run this CLI command on all the nodes of the cluster.

Command syntax

utils system tls_ciphers config reset

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config reset
 
Warning: Resetting the current TLS cipher configuration to the base version will impact security and compatibility.
Ensure the new configuration meets system security requirements and does not affect functionality.
 
TLS cipher configuration successfully reset to base version.
 
Restart the system using the command 'utils system restart' for the changes to take effect.
```

## SSH Encryption Support

The Windows registry key Cisco SSH configuration is available for SSH clients while establishing SSH connections.

This configuration is available only for Packaged CCE 2000 / 4000/ 12000 agent deployments and in lab mode. The configuration
                                          is used when a gateway is added in inventory. The client is Unified CCE Admin and the server is gateway.

You can update the following configurations from the registry, if required:

\HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ ClientKeyExchangeMethods

\HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ ClientBulkEncryptionAlgorithms

\HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ ClientMacAlgorithms

Registry

Default Value

Other supported algorithms

ClientKeyExchangeMethods

curve25519-sha256

ecdh-sha2-nistp256

ecdh-sha2-nistp384

curve25519-sha256@libssh.org

ecdh-sha2-nistp521

diffie-hellman-group14-sha256

diffie-hellman-group16-sha512

curve448-sha512

diffie-hellman-group15-sha512

diffie-hellman-group1-sha1

ClientBulkEncryptionAlgorithm

aes128-gcm@openssh.com

chacha20-poly1305@openssh.com

aes128-ctr,aes256-ctr

aes256-gcm@openssh.com

3des-cbc

aes192-ctr

aes192-cbc

aes128-cbc

aes256-cbc

ClientMacAlgorithms

hmac-sha2-256

AEAD_AES_128_GCM

AEAD_AES_256_GCM

hmac-sha2-512

hmac-sha2-512-etm@openssh.com

hmac-sha2-256-etm@openssh.com

ClientAuthenticationMethods

0

–

To update these configurations, modify the corresponding registries under the Cisco SSH configuration path. For example, to
                              update the ClientMacAlgorithms, you can add or remove algorithms from the registry path.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Note | Unified CCE cannot read, set, or change user passwords in Active Directory. It is possible and likely that the Supervisor
                                          reporting users may use a password (their AD password) to login to CUIC that is different from their agent password set by
                                          the configuration administrator. |
|---|---|

| Note | If you use Unified Contact Center Management Portal (Unified CCMP) or Unified Contact Center Domain Manager (Unified CCDM),
                                       you cannot use Transport Layer Security (TLS) v1.0 for Internet Script Editor. |
|---|---|

| Note | If the client and/or server cipher list was customized before the 15.0 upgrade, all the customised ciphers are retained post-upgrade.
                                                In such cases, manual configuration of the ciphers is needed to meet the Cisco recommended cipher list. |
|---|---|

| Note | The CLIs are node specific. |
|---|---|

| Note | This configuration is available only for Packaged CCE 2000 / 4000/ 12000 agent deployments and in lab mode. The configuration
                                          is used when a gateway is added in inventory. The client is Unified CCE Admin and the server is gateway. |
|---|---|

| Registry | Default Value | Other supported algorithms |
|---|---|---|
| ClientKeyExchangeMethods | curve25519-sha256 ecdh-sha2-nistp256 ecdh-sha2-nistp384 curve25519-sha256@libssh.org ecdh-sha2-nistp521 diffie-hellman-group14-sha256 diffie-hellman-group16-sha512 | curve448-sha512 diffie-hellman-group15-sha512 diffie-hellman-group1-sha1 |
| ClientBulkEncryptionAlgorithm | aes128-gcm@openssh.com chacha20-poly1305@openssh.com aes128-ctr,aes256-ctr aes256-gcm@openssh.com | 3des-cbc aes192-ctr aes192-cbc aes128-cbc aes256-cbc |
| ClientMacAlgorithms | hmac-sha2-256 AEAD_AES_128_GCM AEAD_AES_256_GCM hmac-sha2-512 | hmac-sha2-512-etm@openssh.com hmac-sha2-256-etm@openssh.com |
| ClientAuthenticationMethods | 0 | – |