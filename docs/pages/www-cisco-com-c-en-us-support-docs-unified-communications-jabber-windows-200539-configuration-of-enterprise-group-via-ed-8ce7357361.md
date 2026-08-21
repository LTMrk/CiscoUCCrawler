---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-200539-configuration-of-enterprise-group-via-ed-8ce7357361
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/200539-Configuration-of-Enterprise-Group-via-ED.html
retrieved_at: 2026-08-21T06:57:23.267531+00:00
---

Configuration of Enterprise Group via EDI for Cisco Jabber in WIndows

# Configuration of Enterprise Group via EDI for Cisco Jabber in WIndows

### Download Options

Updated: June 27, 2016

Document ID: 200539

Contents

## Contents

## Introduction

This document describes enterprise group configuration via Cisco Enhanced Device Interfsce (EDI) for Cisco Jabber in Windows.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Call Manager

- Active Directory

### Components Used

The information in this document is based on these software and hardware versions:

- Jabber for windows 11.x and above

- IM and Presence 11.x

- Cisco Communications Manager (CUCM) 11.x

- MS Active Directory

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Current CUCM 11.0.1 only supports directory group with Microsoft Active Directory (MS AD). This is not supported on Microsoft Active Directory Lightweight Directory Services (ADLDS) or other corporate directories.

While AD group is created, two types of options are presented, security and distribution group, as shown in the preceding image. Currently, synchronization of security group is not supported so only distribution group stands supported.

### Configurations

Step 1. Enable Enterprise group.

On CUCM Admin page, navigate to System>Enterprise Parameter.

Under the user management section, search for Directory Group Operations on Cisco IM and Presence and select Enabled

(Optional) From the Synching Mode for Enterprise Groups drop-down list, choose one of these:

- None- If you choose this option, the Cisco Intercluster Sync Agent service does not synchronize the enterprise groups and the group membership records between IM and Presence Service clusters.

- Differential Sync- This is the default option. If you choose this option, after all the enterprise groups and group membership records from remote IM and Presence Service cluster are synchronized, the subsequent syncs synchronize only the records that were updated since the last sync occurred.

- Full Sync- If you choose this option, after all the enterprise groups and group membership records from the remote IM and Presence Service cluster are synchronized, all the records are synchronized during each subsequent sync.

Step 2. In the Lightweight Directory Access Protocol (LDAP) directory configuration section, ensure that the synchronization is enabled for the users and groups.

Navigate to CUCM Admin LDAP> LDAP Directory and then select the directory configuration.

Under Synchronize select Users and Groups , as shown in the image:

Step 3. Depending upon how the LDAP directory sync is configured you may click on Perform Full Sync now and the created directory group is listed in: cucm admin \ user management\ user settings\ user group\

In the current example only one user group was created in the LDAP directory.

Step 4. As you click the group name as listed in step 3, you can see the end user in the group.

Step 5. From jabber's perspective, you have two options. If you use EDI contact resolution then all that is needed here under jabber for windows is to navigate to Settings > File >New >Directory Group.

Search for the directory group, while jabber is connected to LDAP. It is able to query LDAP and give you a search result. In case of User Data Services (UDS) end user needs to know the complete name of the directory group, as shown in the image:

Step 6. If you have to add a new user in the already added directory group, follow these steps:

- Add the user in the AD distribution group.

- Ensure that this is updated in the CUCM user group section, as this can either be done with the LDAP sync cycle defined at the LDAP directory page.

- Or the administrator clicks on Perform Full Sync Now. The moment it is done, the end user pops up in jabber (in windows) automatically, no jabber (in windows) restart is needed as the update is dynamic from jabber's perspective. However, sync for CUCM to LDAP has to be completed before it pops up the new user (This is a tested method.)

As shown in the image test3 3 account is a new entry added in the already imported group1_distribution group.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

- Enterprise Group CUCM 11.x guide

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Amit Kumar

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Windows