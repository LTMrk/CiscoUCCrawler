---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125install-3f24b1df2e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125install-and-upgrade-guide/uccx_b_125install-and-upgrade-guide_appendix_0101.html
retrieved_at: 2026-08-16T21:14:35.709521+00:00
---

Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Server Configuration Table

## Chapter: Server Configuration Table

- Server Configuration Table

- Server                              	 Configuration Information for Installation

# Server Configuration Table

## Server
                        	 Configuration Information for Installation

You can use the configuration table for saving your entries either on a printed paper or in the PDF document.

Be aware that the field values (namely hostname and passwords) that you enter while you are running the installation program
                                                are case-sensitive. Hostname must be in lower case and the character limit is 24 characters.

All the fields may not be applicable to your system and network configuration. Unless mentioned otherwise, you can change
                                                the values of most fields after the installation using CLI commands.

Attention

Parameter

Your Entry

Administrator ID

Attention

Caution

Administrator Password

Attention

This field specifies the password for the administrator account, which you use for secure shell access to the CLI, for logging
                                                      in to Cisco Unified Operating System Administration, and for logging in to the Disaster Recovery System. Ensure that the password
                                                      is at least six characters long; it can contain alphanumeric characters, hyphens, and underscores.

You can
                                                      						change the password after installation.

Application User Name

Application User
                                             						Password

Attention

Use the
                                                      						Application User password as the default password for applications that are
                                                      						installed on the system, including Unified CCX and Unified Communications
                                                      						Manager. Ensure that the password is at least six characters long; it can
                                                      						contain alphanumeric characters, hyphens, and underscores.

You can
                                                      						change the password after installation.

DNS Primary

DNS
                                             						Secondary (optional)

Domain

Gateway Address

Hostname

IP Address

IP Mask

MTU Size

NIC Duplex

NIC Speed

NTP Server

Attention

Enter the hostname or IP address of one or more Network Time Protocol (NTP) servers with which you want to synchronize.

You can enter up to five NTP servers.

You can change the NTP server after installation.

Security Password

Attention

Servers in the cluster use the Security password to communicate with one another. The password must contain at least six alphanumeric
                                                      characters. It can contain hyphens and underscores, but it must start with an alphanumeric character.

Save this password. You will be asked to enter the same Security password when you install the second node to form a cluster.

You can change the password after installation by using the following CLI command:

To avoid losing communications between nodes, you must change the Security password on both nodes in a cluster and reboot
                                                      both the nodes. For more information, see the description of this command in the Cisco Unified Operating
                                                               				  System Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

SMTP Location

Organization

Unit

Location

State

Country

Time Zone

| Note | You can use the configuration table for saving your entries either on a printed paper or in the PDF document. Be aware that the field values (namely hostname and passwords) that you enter while you are running the installation program
                                                are case-sensitive. Hostname must be in lower case and the character limit is 24 characters. All the fields may not be applicable to your system and network configuration. Unless mentioned otherwise, you can change
                                                the values of most fields after the installation using CLI commands. |
|---|---|

| Attention | Changes to some of the configuration parameters may result in changes to the licence MAC, and you may have to rehost the Unified
                                       CCX license. For information about the configuration parameters, see Unified CCX Licenses . |
|---|---|

| Parameter | Your Entry |
|---|---|
| Administrator ID Attention You cannot change the original administrator account user ID; you can create additional administrator accounts. Caution Do not create administrator IDs (for CLI access or Operating System administration) that start with "uccx" or "UCCX" because
                                                   such IDs conflict with system account names that are used internally within the Unified CCX server. | Attention | You cannot change the original administrator account user ID; you can create additional administrator accounts. | Caution | Do not create administrator IDs (for CLI access or Operating System administration) that start with "uccx" or "UCCX" because
                                                   such IDs conflict with system account names that are used internally within the Unified CCX server. |  |
| Attention | You cannot change the original administrator account user ID; you can create additional administrator accounts. |
| Caution | Do not create administrator IDs (for CLI access or Operating System administration) that start with "uccx" or "UCCX" because
                                                   such IDs conflict with system account names that are used internally within the Unified CCX server. |
| Administrator Password Attention This field specifies the password for the administrator account, which you use for secure shell access to the CLI, for logging
                                                      in to Cisco Unified Operating System Administration, and for logging in to the Disaster Recovery System. Ensure that the password
                                                      is at least six characters long; it can contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. | Attention | This field specifies the password for the administrator account, which you use for secure shell access to the CLI, for logging
                                                      in to Cisco Unified Operating System Administration, and for logging in to the Disaster Recovery System. Ensure that the password
                                                      is at least six characters long; it can contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. |  |
| Attention | This field specifies the password for the administrator account, which you use for secure shell access to the CLI, for logging
                                                      in to Cisco Unified Operating System Administration, and for logging in to the Disaster Recovery System. Ensure that the password
                                                      is at least six characters long; it can contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. |
| Application User Name |  |
| Application User
                                             						Password Attention Use the
                                                      						Application User password as the default password for applications that are
                                                      						installed on the system, including Unified CCX and Unified Communications
                                                      						Manager. Ensure that the password is at least six characters long; it can
                                                      						contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. | Attention | Use the
                                                      						Application User password as the default password for applications that are
                                                      						installed on the system, including Unified CCX and Unified Communications
                                                      						Manager. Ensure that the password is at least six characters long; it can
                                                      						contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. |  |
| Attention | Use the
                                                      						Application User password as the default password for applications that are
                                                      						installed on the system, including Unified CCX and Unified Communications
                                                      						Manager. Ensure that the password is at least six characters long; it can
                                                      						contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. |
| DNS Primary |  |
| DNS
                                             						Secondary (optional) |  |
| Domain |  |
| Gateway Address |  |
| Hostname |  |
| IP Address |  |
| IP Mask |  |
| MTU Size Note Use the same Maximum Transmission Unit (MTU) value for all servers in the cluster. | Note | Use the same Maximum Transmission Unit (MTU) value for all servers in the cluster. |  |
| Note | Use the same Maximum Transmission Unit (MTU) value for all servers in the cluster. |
| NIC Duplex Note This parameter is not displayed if automatic negotiation is used. | Note | This parameter is not displayed if automatic negotiation is used. |  |
| Note | This parameter is not displayed if automatic negotiation is used. |
| NIC Speed Note This parameter is not displayed if automatic negotiation is used. | Note | This parameter is not displayed if automatic negotiation is used. |  |
| Note | This parameter is not displayed if automatic negotiation is used. |
| NTP Server Attention Enter the hostname or IP address of one or more Network Time Protocol (NTP) servers with which you want to synchronize. You can enter up to five NTP servers. You can change the NTP server after installation. | Attention | Enter the hostname or IP address of one or more Network Time Protocol (NTP) servers with which you want to synchronize. You can enter up to five NTP servers. You can change the NTP server after installation. |  |
| Attention | Enter the hostname or IP address of one or more Network Time Protocol (NTP) servers with which you want to synchronize. You can enter up to five NTP servers. You can change the NTP server after installation. |
| Security Password Attention Servers in the cluster use the Security password to communicate with one another. The password must contain at least six alphanumeric
                                                      characters. It can contain hyphens and underscores, but it must start with an alphanumeric character. Save this password. You will be asked to enter the same Security password when you install the second node to form a cluster. You can change the password after installation by using the following CLI command: CLI > set password user security To avoid losing communications between nodes, you must change the Security password on both nodes in a cluster and reboot
                                                      both the nodes. For more information, see the description of this command in the Cisco Unified Operating
                                                               				  System Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . | Attention | Servers in the cluster use the Security password to communicate with one another. The password must contain at least six alphanumeric
                                                      characters. It can contain hyphens and underscores, but it must start with an alphanumeric character. Save this password. You will be asked to enter the same Security password when you install the second node to form a cluster. You can change the password after installation by using the following CLI command: CLI > set password user security To avoid losing communications between nodes, you must change the Security password on both nodes in a cluster and reboot
                                                      both the nodes. For more information, see the description of this command in the Cisco Unified Operating
                                                               				  System Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |  |
| Attention | Servers in the cluster use the Security password to communicate with one another. The password must contain at least six alphanumeric
                                                      characters. It can contain hyphens and underscores, but it must start with an alphanumeric character. Save this password. You will be asked to enter the same Security password when you install the second node to form a cluster. You can change the password after installation by using the following CLI command: CLI > set password user security To avoid losing communications between nodes, you must change the Security password on both nodes in a cluster and reboot
                                                      both the nodes. For more information, see the description of this command in the Cisco Unified Operating
                                                               				  System Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |
| SMTP Location Note You must populate this field if you plan to use electronic notification. | Note | You must populate this field if you plan to use electronic notification. |  |
| Note | You must populate this field if you plan to use electronic notification. |
| Organization Note The value you enter is used to generate a CSR. | Note | The value you enter is used to generate a CSR. |  |
| Note | The value you enter is used to generate a CSR. |
| Unit Note The value you enter is used to generate a CSR. | Note | The value you enter is used to generate a CSR. |  |
| Note | The value you enter is used to generate a CSR. |
| Location |  |
| State Note The value you enter is used to generate a CSR. | Note | The value you enter is used to generate a CSR. |  |
| Note | The value you enter is used to generate a CSR. |
| Country Note The value you enter is used to generate a CSR and self-signed certificates. | Note | The value you enter is used to generate a CSR and self-signed certificates. |  |
| Note | The value you enter is used to generate a CSR and self-signed certificates. |
| Time Zone Note Use the same Timezone for all nodes. | Note | Use the same Timezone for all nodes. |  |
| Note | Use the same Timezone for all nodes. |

| Attention | You cannot change the original administrator account user ID; you can create additional administrator accounts. |
|---|---|

| Caution | Do not create administrator IDs (for CLI access or Operating System administration) that start with "uccx" or "UCCX" because
                                                   such IDs conflict with system account names that are used internally within the Unified CCX server. |
|---|---|

| Attention | This field specifies the password for the administrator account, which you use for secure shell access to the CLI, for logging
                                                      in to Cisco Unified Operating System Administration, and for logging in to the Disaster Recovery System. Ensure that the password
                                                      is at least six characters long; it can contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. |
|---|---|

| Attention | Use the
                                                      						Application User password as the default password for applications that are
                                                      						installed on the system, including Unified CCX and Unified Communications
                                                      						Manager. Ensure that the password is at least six characters long; it can
                                                      						contain alphanumeric characters, hyphens, and underscores. You can
                                                      						change the password after installation. |
|---|---|

| Note | Use the same Maximum Transmission Unit (MTU) value for all servers in the cluster. |
|---|---|

| Note | This parameter is not displayed if automatic negotiation is used. |
|---|---|

| Note | This parameter is not displayed if automatic negotiation is used. |
|---|---|

| Attention | Enter the hostname or IP address of one or more Network Time Protocol (NTP) servers with which you want to synchronize. You can enter up to five NTP servers. You can change the NTP server after installation. |
|---|---|

| Attention | Servers in the cluster use the Security password to communicate with one another. The password must contain at least six alphanumeric
                                                      characters. It can contain hyphens and underscores, but it must start with an alphanumeric character. Save this password. You will be asked to enter the same Security password when you install the second node to form a cluster. You can change the password after installation by using the following CLI command: CLI > set password user security To avoid losing communications between nodes, you must change the Security password on both nodes in a cluster and reboot
                                                      both the nodes. For more information, see the description of this command in the Cisco Unified Operating
                                                               				  System Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |
|---|---|

| Note | You must populate this field if you plan to use electronic notification. |
|---|---|

| Note | The value you enter is used to generate a CSR. |
|---|---|

| Note | The value you enter is used to generate a CSR. |
|---|---|

| Note | The value you enter is used to generate a CSR. |
|---|---|

| Note | The value you enter is used to generate a CSR and self-signed certificates. |
|---|---|

| Note | Use the same Timezone for all nodes. |
|---|---|