---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-design-guide-b-12xcucdg-b-12xcucdg-chapter-01100-html-1a55e4471e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg/b_12xcucdg_chapter_01100.html
retrieved_at: 2026-08-17T02:35:21.253634+00:00
---

Design Guide for Cisco Unity Connection 12.x

# Design Guide for Cisco Unity Connection 12.x

Updated: August 17, 2017

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

For more information on the Disaster Recovery System, see the
                              		” Backing Up and Restoring
                                 		  Cisco Unity Connection Components ” chapter of the Install, Upgrade,
                              		Maintenance Guide for Cisco Unity Connection, Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

### Cisco Object Backup and Restore Application Suite (COBRAS)

Cisco Objected Backup and Restore Application Suite (COBRAS) is a set of tools designed to allow administrators to back up
                              all user, call handler, interview handler, public distribution list, schedule and routing rule information and restore some
                              or all of that information onto another Cisco Unity Connection server. It is specifically designed to allow for partial restores,
                              restores onto different versions or products than was backed up, and for “merges” of data from multiple system backups.

For extensive information on using COBRAS, see the COBRAS Help at http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html .