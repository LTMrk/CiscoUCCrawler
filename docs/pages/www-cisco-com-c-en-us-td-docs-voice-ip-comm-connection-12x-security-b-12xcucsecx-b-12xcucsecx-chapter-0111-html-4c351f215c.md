---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-security-b-12xcucsecx-b-12xcucsecx-chapter-0111-html-4c351f215c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/b_12xcucsecx/b_12xcucsecx_chapter_0111.html
retrieved_at: 2026-08-17T02:36:37.914687+00:00
---

Security Guide for Cisco Unity Connection Release 12.x

# Security Guide for Cisco Unity Connection Release 12.x

Updated: August 7, 2017

Chapter: Cisco Unity Connection Security Password

## Chapter: Cisco Unity Connection Security Password

- Cisco Unity Connection Security Password

- About Security                              	 Password

# Cisco Unity Connection Security Password

Cisco Unity Connection Security Password

## About Security
                        	 Password

During Unity Connection installation, you specify a security
                           		password that is not associated with any user. The password has two purposes:

When a Unity Connection cluster is configured, the two servers
                                 			 in a cluster use the security password to authenticate with one another before
                                 			 replicating data. If you change the security password on one server in a
                                 			 cluster, you must also change the password on the other server, or the two
                                 			 servers cannnot replicate data or messages.

Regardless of whether a cluster is configured, the security
                                 			 password is used as the encryption key for the Disaster Recovery System. If you
                                 			 back up a Unity Connection server, change the security password, and then try
                                 			 to restore data from the backup, you must enter the security password that was
                                 			 in effect when you backed up the server. (If the current security password
                                 			 matches the security password with which the backup was made, you do not need
                                 			 to specify the password to restore data.)

To change the security password, use the set password user CLI command. For more information,
                           		including the sequence in which you change the password on the servers in a
                           		cluster, see the applicable version of the Command Line Interface Reference
                           		Guide for Cisco Unified Communications Solutions Release 12.x at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .