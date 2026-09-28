---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-b-15cucdg-b-14cucdg-chapter-01100-html-ea04bd168b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/b_15cucdg/b_14cucdg_chapter_01100.html
retrieved_at: 2026-08-17T03:22:41.437765+00:00
---

Design Guide for Cisco Unity Connection 15

# Design Guide for Cisco Unity Connection 15

Updated: December 18, 2023

Chapter: Disaster Recovery System and COBRAS

## Chapter: Disaster Recovery System and COBRAS

# Disaster Recovery System and COBRAS

With any disaster recovery planning, it is imperative for customers to properly back up Cisco Unity Connection in case of
                        a disaster. There are two tools that you should use in backing up and restoring Unity Connection:

## Disaster Recovery System and COBRAS

With any disaster recovery planning, it is imperative for customers to properly back up Cisco Unity Connection in case of
                           a disaster. There are two tools that you should use in backing up and restoring Unity Connection:

### Disaster Recovery
                           	 System (DRS)

The
                              		Disaster Recovery System (DRS), which can be invoked from Cisco Unified
                              		Communications Manager Administration, provides full data backup and restore
                              		capabilities. The Disaster Recovery System allows you to perform manual or
                              		regularly scheduled automatic data backups.

The Disaster Recovery System includes the following
                              		capabilities:

A user interface for performing backup and restore tasks.

A distributed system architecture for performing backup and
                                    			 restore functions.

Scheduled backups.

Archived backups to a physical tape drive or remote SFTP server.

For more information on the Disaster Recovery System, see the ” Backing Up and Restoring Cisco Unity Connection Components ” chapter of the Install, Upgrade, Maintenance Guide for Cisco Unity Connection, Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### Cisco Object Backup and Restore Application Suite (COBRAS)

Cisco Objected Backup and Restore Application Suite (COBRAS) is a set of tools designed to allow administrators to back up
                              all user, call handler, interview handler, public distribution list, schedule and routing rule information and restore some
                              or all of that information onto another Cisco Unity Connection server. It is specifically designed to allow for partial restores,
                              restores onto different versions or products than was backed up, and for “merges” of data from multiple system backups.

For extensive information on using COBRAS, see the COBRAS Help at http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html .