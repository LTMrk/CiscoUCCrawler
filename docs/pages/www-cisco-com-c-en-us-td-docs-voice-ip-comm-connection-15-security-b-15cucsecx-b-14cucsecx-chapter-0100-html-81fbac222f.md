---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-security-b-15cucsecx-b-14cucsecx-chapter-0100-html-81fbac222f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/b_15cucsecx/b_14cucsecx_chapter_0100.html
retrieved_at: 2026-08-21T08:00:26.511473+00:00
---

Security Guide for Cisco Unity Connection Release 15

# Security Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: FIPS Compliance in Cisco Unity Connection

## Chapter: FIPS Compliance in Cisco Unity Connection

# FIPS Compliance in Cisco Unity Connection

## FIPS Compliance in Cisco Unity Connection

## Introduction

FIPS, or Federal Information Processing Standard, is a U.S. and Canadian government certification standard that defines requirements
                           that cryptographic modules must follow.

Caution

FIPS mode is only supported on releases that have been through FIPS compliance. Be warned that FIPS mode should be disabled
                                       before you upgrade to a non-FIPS compliance version of Cisco Unity Connection.

For information about which releases are FIPS compliant and to view their certifications, see the FIPS 140 document at link
                                       : https://www.cisco.com/c/en/us/solutions/industries/government/global-government-certifications/fips-140.html

Certain versions of Unity Connection are FIPS 140-2 compliant, in accordance with the U.S. National Institute of Standards
                           (NIST). They can operate in FIPS mode, level 1 compliance. For more information on 'FIPS 140-2' setup, see Security Guide for Cisco Unified Communications Manager for release 15.

CiscoSSL 1.1.1n.7.2.390 with FIPS Module CiscoSSL FOM 7.2a

CiscoSSH -1.9.29

RSA CryptoJ 6_2_3

BC FIPS -1.0.2.3.jar

BCTLS FIPS - 1.0.12.3.jar

BCPKIX FIPS -1.0.5.jar

Strongswan - 5.9.8

NSS -3.67

For information on Unity Connection upgrades, see Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html

## Running CLI
                        	 Commands for FIPS

To enable the FIPS feature in Cisco Unity Connection, you use
                           		the utils fips enable CLI command. In addition to this, the following CLI
                           		commands are also available:

utils fips disable- Use to disable the FIPS feature.

utils fips status- Use to check the status of FIPS compliance.

For more
                           		information on the utils fips <option> CLI commands, see the applicable Command Line
                              		  Interface Reference Guide for Cisco Unified Communications Solutions at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .

Caution

Caution

Before enabling the FIPS mode on the Unity Connection server, ensure that the security password length is minimum of 14 characters.
                                       In case of upgrading Unity Connection, password needs to be updated if the prior version was FIPS enabled.

All the new certificates are signed using SHA-256 hashing algorithm in FIPS mode. When you generate a self-signed certificate
                           or Certificate Signing Request, you can choose only SHA-256 as the hashing algorithm.

## Regenerating
                        	 Certificates for FIPS

### Regenerating Root Certificates

Cisco Unity Connection servers with pre-existing telephony integrations must have the root certificate manually regenerated
                              after enabling or disabling the FIPS mode. If the telephony integration uses an Authenticated or Encrypted Security mode,
                              the regenerated root certificate must be re-uploaded to any corresponding Cisco Unified Communications Manager servers. For
                              fresh installations, regenerating the root certificate can be avoided by enabling FIPS mode before adding the telephony integration.

- Sign in to Cisco Unity Connection Administration.

- Select Telephony Integrations> Security> Root Certificate.

- On the View Root Certificate page, click Generate New.

- If the telephony integration uses an Authenticated or Encrypted Security mode, continue with steps 5-10, otherwise skip to
                                 step 12.

- On the View Root Certificate page, right-click the Right-click to Save the Root Certificate as a File link.

- On the Cisco Unified CM server, sign in to Cisco Unified Operating System Administration.

- Select the Certificate Management option from the Security menu.

- Select Upload Certificate/Certificate Chain on the Certificate List page.

- On the Upload Certificate/Certificate Chain page, select the CallManager-trust option from the Certificate Name drop-down.

- Enter Cisco Unity Connection Root Certificate in the Root Certificate field.

- Click Browse in the Upload File field to locate and select the Cisco Unity Connection root certificate that was saved in
                                       Step 5.

- Click Upload File.

- Click Close.

- On the Cisco Unified CM server, sign in to Cisco Unified Serviceability.

- Select Service Management from the Tools menu.

- On the Control Center - Feature Services page, restart the Cisco CallManager service.

- Repeat steps 5-10 on all remaining Cisco Unified CM servers in the Cisco Unified CM cluster.

- Sign in to Cisco Unity Connection Serviceability.

- Select Service Management from the Tools menu.

- Select Stop for the Unity Connection Conversation Manager service in the Critical Services section.

- When the Status area displays a message that the Unity Connection Conversation Manager service is successfully stopped, select
                                       Start for the service.

- New and pre-existing telephony integration ports are now correctly registered with Cisco Unified CM.

FIPS is supported for both SCCP and SIP integrations between Cisco Unified Communications Manager and Cisco Unity Connection.

For more information on managing certificates, see the " Manage Certificates and Certificate Trust Lists " section in the "Security" chapter of the Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html

### Regenerating Tomcat Certificates

Unity Connection supports only RSA key based Tomcat certificates to configure secure calls using SIP Integration.This allows
                              the use of self signed as well as third-party CA signed certificate for SIP secure call. Cisco Unity Connection servers with
                              pre-existing telephony integrations must have the Tomcat certificate manually regenerated after enabling or disabling the
                              FIPS mode. If the telephony integration uses an Authenticated or Encrypted Security mode, the regenerated tomcat certificate
                              must be re-uploaded to any corresponding Cisco Unified Communications Manager servers. For fresh installations, regenerating
                              the tomcat certificate can be avoided by enabling FIPS mode before adding the telephony integration.

Verify that the value entered in X.509 Subject Name field on SIP Trunk Security Profile Configuration page of Cisco Unified Communication Manager is the FQDN of the Unity Connection
                                             server.

## Configuring Additional Settings When Using FIPS Mode

In order to maintain FIPS compliance, additional
                           		configurations are mandatory for the following features:

- Networking: Intrasite,
                              		  Intersite, VPIM

- Unified Messaging: Unified
                              		  Messaging Services.

### Configure Networking When Using FIPS Mode

Networking from Cisco Unity Connection to another
                              		server must be secured by an IPsec policy. This includes intersite links,
                              		intrasite links, and VPIM locations. The remote server is responsible for
                              		assuring its own FIPS compliance.

### Configure Unified Messaging When Using FIPS Mode

Unified Messaging Services require the following
                              		configuration:

- Configure IPsec policy between Cisco Unity Connection and Microsoft Exchange.

Set the Web-Based Authentication Mode setting to Basic on the Edit Unified Messaging Service page in Unity Connection Administration.
                                    NTLM web authentication mode is not supported in FIPS mode.

Caution

### Configure IPsec
                           	 Policies Using FIPS Mode

For information on setting up IPsec policies, see the " IPSEC Management " section in the "Security" chapter of the Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx.html .

For information on the impact of IPsec policies with Unity Connection, see " Upgrading Cisco Unity Connection " chapter of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html

.

### Unsupported
                           	 Features When Using FIPS Mode

The following Cisco Unity Connection features are not supported
                              		when FIPS mode is enabled:

- SpeechView Transcription
                                 		  Service.

- SIP Digest Authentication
                                 		  (configured for SIP Telephony Integrations).

- SIP NTLM Authentication (configured for SIP Telephony Integration).

- Video Messaging.

## Configuring
                        	 Voicemail PIN For Touchtone Conversation Users To Sign-In

Enabling FIPS in Cisco Unity Connection prevents a touchtone
                           		conversation user from signing in to play or send voice messages or to change
                           		user settings if both of the following options are true:

- The user was created in
                              		  Cisco Unity 5.x or earlier, and migrated to Connection.

- The Unity Connection user
                              		  still has a voicemail PIN that was assigned in Cisco Unity 5.x or earlier.

A touchtone
                           		conversation user signs in by entering an ID (usually the user's extension) and
                           		a voicemail PIN. The ID and PIN are assigned when the user is created. Either
                           		an administrator or the user can change the PIN. To prevent administrators from
                           		accessing PINs in Connection Administration, PINs are hashed. In Cisco Unity
                           		5.x and earlier, Cisco Unity hashed the PIN by using an MD5 hashing algorithm,
                           		which is not FIPS compliant. In Cisco Unity 7.x and later, and in Unity
                           		Connection, the PIN is hashed by using an SHA-1 algorithm, which is much harder
                           		to decrypt and is FIPS compliant.

### Hashing All
                           	 Voicemail PIN with SHA-1 Algorithm in Unity Connection

When FIPS is enabled, Cisco Unity Connection no longer checks
                              		the database to determine whether the user's voicemail PIN was hashed with MD5
                              		or SHA-1 algorithm. Unity Connection hashes all the voicemail PINs with SHA-1
                              		and compares it with the hashed PIN in the Unity Connection database. The user
                              		is not allowed to sign in if the MD5 hashed voicemail PIN entered by user does
                              		not match with the SHA-1 hashed voicemail PIN in the database.

## FIPS Mode Restrictions

Feature

Restrictions

SNMP v3

FIPS mode does not support SNMP v3 with MD5 or DES. If you have SNMP v3 configured while FIPS mode is enabled, you must configure SHA as the Authentication Protocol and AES128 as the Privacy Protocol.

SFTP Server

FIPS mode only supports rsa-sha2-256.

Non-FIPS mode supports both ssh-rsa and rsa-sha2-256.

The rsa-sha2-256 (SHA256WithRSA) support is available only from OpenSSH 6.8 version onwards. In FIPS mode, only the SFTP servers
                                       running with OpenSSH 6.8 version onwards supports the rsa-sha2-256 (SHA256WithRSA).

SSH Host Key Algorithms

Deprecated Algorithm:

ssh-rsa (SHAlwithRSA)

New Supported Algorithm:

rsa-sha2-256

rsa-sha2-512

Before upgrading, we recommend you to refer the Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

IPSec Policy

Certificate based IPSec Policy will not work when moving from Non-FIPS to FIPS or vice-versa.

Perform the following when you  move from Non-FIPS mode to FIPS or vice-versa. If you have a certificate based IPSec policy
                                       and its in enabled state then:

Disable the IPSec policy before moving to FIPS or vice versa.

Re-certify the certificate and exchange the new certificate after moving to FIPS mode or vice versa.

Enable IPSec policy.

| Caution | FIPS mode is only supported on releases that have been through FIPS compliance. Be warned that FIPS mode should be disabled
                                       before you upgrade to a non-FIPS compliance version of Cisco Unity Connection. For information about which releases are FIPS compliant and to view their certifications, see the FIPS 140 document at link
                                       : https://www.cisco.com/c/en/us/solutions/industries/government/global-government-certifications/fips-140.html |
|---|---|

| Note | For information on Unity Connection upgrades, see Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html |
|---|---|

| Caution | After enabling or disabling the FIPS mode, the Cisco Unity Connection server
                                    		restart automatically. |
|---|---|

| Caution | If the Cisco Unity Connection server is in a cluster, do not change the FIPS
                                    		settings on any other node until the FIPS operation on the current node is
                                    		complete and the system is back up and running. |
|---|---|

| Note | Before enabling the FIPS mode on the Unity Connection server, ensure that the security password length is minimum of 14 characters.
                                       In case of upgrading Unity Connection, password needs to be updated if the prior version was FIPS enabled. |
|---|---|

| Note | In case of clusters, perform the following steps on all nodes. |
|---|---|

| Note | The certificate must be saved as a file with the extension.pem rather than.htm, else Cisco Unified CM will not recognize
                                             the certificate. |
|---|---|

| Note | Verify that the value entered in X.509 Subject Name field on SIP Trunk Security Profile Configuration page of Cisco Unified Communication Manager is the FQDN of the Unity Connection
                                             server. |
|---|---|

| Note | Secure Messages are not sent in a FIPS compliant manner unless an
                                       		IPsec Policy is configured. |
|---|---|

| Caution | The IPsec policy between servers is required to
                                       		protect the plain text nature of Basic web authentication. |
|---|---|

| Feature | Restrictions |
|---|---|
| SNMP v3 | FIPS mode does not support SNMP v3 with MD5 or DES. If you have SNMP v3 configured while FIPS mode is enabled, you must configure SHA as the Authentication Protocol and AES128 as the Privacy Protocol. |
| SFTP Server | By Default, the JSCH library was using ssh-rsa for SFTP connection but the FIPS mode doesn’t support ssh-rsa. Due to a recent
                                       update of CentOS, the JSCH library supports both ssh-rsa (SHA1withRSA) or rsa-sha2-256 (SHA256withRSA) depending on the FIPS
                                       value after modifications. That is, Note FIPS mode only supports rsa-sha2-256. Non-FIPS mode supports both ssh-rsa and rsa-sha2-256. The rsa-sha2-256 (SHA256WithRSA) support is available only from OpenSSH 6.8 version onwards. In FIPS mode, only the SFTP servers
                                       running with OpenSSH 6.8 version onwards supports the rsa-sha2-256 (SHA256WithRSA). | Note | FIPS mode only supports rsa-sha2-256. Non-FIPS mode supports both ssh-rsa and rsa-sha2-256. |
| Note | FIPS mode only supports rsa-sha2-256. Non-FIPS mode supports both ssh-rsa and rsa-sha2-256. |
| SSH Host Key Algorithms | Deprecated Algorithm: ssh-rsa (SHAlwithRSA) New Supported Algorithm: rsa-sha2-256 rsa-sha2-512 Note Before upgrading, we recommend you to refer the Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html . | Note | Before upgrading, we recommend you to refer the Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html . |
| Note | Before upgrading, we recommend you to refer the Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html . |
| IPSec Policy | Certificate based IPSec Policy will not work when moving from Non-FIPS to FIPS or vice-versa. Perform the following when you  move from Non-FIPS mode to FIPS or vice-versa. If you have a certificate based IPSec policy
                                       and its in enabled state then: Disable the IPSec policy before moving to FIPS or vice versa. Re-certify the certificate and exchange the new certificate after moving to FIPS mode or vice versa. Enable IPSec policy. |

| Note | FIPS mode only supports rsa-sha2-256. Non-FIPS mode supports both ssh-rsa and rsa-sha2-256. |
|---|---|

| Note | Before upgrading, we recommend you to refer the Upgrade Types section of the "Upgrading Cisco Unity Connection" chapter of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html . |
|---|---|