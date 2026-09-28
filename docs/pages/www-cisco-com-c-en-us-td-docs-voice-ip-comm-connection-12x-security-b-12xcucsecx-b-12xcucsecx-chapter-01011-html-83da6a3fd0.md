---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-security-b-12xcucsecx-b-12xcucsecx-chapter-01011-html-83da6a3fd0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/b_12xcucsecx/b_12xcucsecx_chapter_01011.html
retrieved_at: 2026-08-16T18:58:56.099114+00:00
---

Security Guide for Cisco Unity Connection Release 12.x

# Security Guide for Cisco Unity Connection Release 12.x

Updated: August 7, 2017

Chapter: Cisco Unity
	 Connection- Restricted and Unrestricted Version

## Chapter: Cisco Unity
	 Connection- Restricted and Unrestricted Version

- Cisco Unity                              	 Connection- Restricted and Unrestricted Version

- Cisco Unity                              	 Connection - Restricted and Unrestricted Version

# Cisco Unity
                     	 Connection- Restricted and Unrestricted Version

## Cisco Unity
                        	 Connection - Restricted and Unrestricted Version

This product contains cryptographic features and is subject to United States and local country laws governing import, export,
                              transfer and use. Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute,
                              or use encryption. Importers, exporters, distributors and users are responsible for compliance with U.S. and local country
                              laws.

Cisco Unity Connection provides two versions of the Connection software - restricted and unrestricted that address import
                              requirements for some countries related to encryption of user data. Restricted version of the Cisco Unity Connection allows
                              you to enable the encryption on the product to use the below given security modules whereas in Unrestricted version, you are
                              not allowed to use the security modules

With Unity Connection 12.0(1) and later, by default the encryption is disabled for the Restricted version of the product in
                              Evaluation Mode. Hence you are not allowed to use the above security modules with Restricted version of Unity Connection until
                              the product is registered with Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite using a token
                              that allows Export-Controlled Functionality. The behavior of Restricted version of Unity Connection in Evaluation Mode is
                              similar to the behavior of Unrestricted version of Unity Connection.

When you are upgrading Cisco Unity Connection from any earlier releases to 12.0(1) and later, you get the following behavior
                              of encryption on Cisco Unity Connection:

Cisco Unity Connection continues to run in secure mode. If the product is not registered with CSSM or satellite through Export
                                             Controlled Functionality enabled token before Evaluation Period Expired, system will generate an alarm on RTMT after Evaluation
                                             Period Expired.

For more information on how to register the product with CSSM or satellite, see "Managing Licenses" chapter of Install, Upgrade
                              and Maintenance Guide for Cisco Unity Connection 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

To enable or disable the encryption on Cisco Unity Connection Restricted version, a new CLI command "utils cuc encryption
                              <enable/disable>" is introduced in Unity Connection 12.0(1) and later.

For more information on the CLI, see the Command Line Interface Reference Guide for Cisco Unified Solutions for the latest
                              release, available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

As per the United State Export Control law, Category C customers are not allowed to enable the encryption on the product.
                              The virtual account of Category C customers is export restricted.

With Unity Connection 12.5(1) SU1, the Category C customers can enable the encryption on the restricted version of Cisco Unity
                              Connection with both type of licensing – Cisco Smart Software Licensing and Specific License Reservation. To enable the encryption
                              for Category C customers, the product is registerd with Cisco Smart Software Manager using a token created on the virtual
                              account of the customer and must have CUC Export Restricted Authorization Key (PID: CUC-SL-EXRTKY-K9=) license in the virtual
                              account with Smart Licensing. For Specific License reservation, you must reserve that license to enable the encryption for
                              Category C customers.

For more information on how to enable the encryption for export restricted virtual account, see " Enabling Encryption in Cisco Unity Connection 12.5 SU1 and Later ".

| Functionality | Restricted Version of Connection | Unrestricted Version of Connection |
|---|---|---|
| SSL for IMAP connections used to access voice messages | Allowed | Disallowed |
| Secure SCCP, SIP, and SRTP for call signaling and media | Allowed | Disallowed |
| Communications among networked Connection servers or clusters (over secure MIME) | Allowed | Disallowed |
| SSL for Comet notification (Jetty SSL command) | Allowed | Disallowed |

| Caution | With restricted and unrestricted versions of Connection software available, download software or order a DVD. Upgrading a
                                          restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                          Upgrading an unrestricted version to a restricted version is not supported. |
|---|---|

| Upgrade Path | Cluster Mode before Upgrade | License Status before Upgrade | License Status after Upgrade | Action |
|---|---|---|---|---|
| Pre-12.0(1) to 12.0(1) | Secure | Demo or PLM Licensed | Evaluation Mode | Cisco Unity Connection continues to run in secure mode. If the product is not registered with CSSM or satellite through Export
                                             Controlled Functionality enabled token before Evaluation Period Expired, system will generate an alarm on RTMT after Evaluation
                                             Period Expired. |

| Caution | After deregistration, if any of the following services - "Connection Conversation Manager" or "Connection IMAP Server" is
                                          restarted, you will not be able to use security modules. For example IMAP in case IMAP Server restart and SCCP/SIP/SRTP in
                                          case Connection Conversation Manager in Cisco Unity Connection. |
|---|---|

| Note | With release 12.0(1) onwards, upgrade from 12.0(1) to 12.0(1) and later will have the existing encryption status of the system
                                          after upgrade. |
|---|---|

| Note | In case of upgrade, you must execute the CLI after successfully completed the switch version. |
|---|---|