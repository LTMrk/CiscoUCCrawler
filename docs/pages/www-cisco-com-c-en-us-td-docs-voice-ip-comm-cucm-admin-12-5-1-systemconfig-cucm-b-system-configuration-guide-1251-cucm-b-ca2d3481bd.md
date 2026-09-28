---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-ca2d3481bd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011111.html
retrieved_at: 2026-08-16T17:31:31.811036+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: End User Configuration Overview

## Chapter: End User Configuration Overview

- End User Configuration Overview

- About End User Configuration

- End User Configuration

# End User Configuration Overview

## About End User Configuration

The chapters in this part describe how to provision and configure end users for your system.

End users are the main consumers of Cisco Unified Communications Manager features. End users can be assigned with phones and
                           directory numbers thereby allowing your end users to make calls and communicate with other users in the system as well as
                           placing calls to external networks such as the PSTN.

For provisioning large numbers of end users at once, Cisco Unified Communications Manager provides the following features:

LDAP Directory Integration—You can synchronize Cisco Unified Communications Manager with an external LDAP directory thereby
                                 allowing you to import end user data from the LDAP directory.

Bulk Administration Tool—You can use the Bulk Administration Tool to import and configure a large number of end users, and
                                 associated user data, from a CSV file in a single operation.

After your end users are provisioned, you can configure user settings such as user profiles that allow your users to provision
                           their own phones, in addition to phone services and  credential policies.

## End User Configuration

Complete the following task flows to configure end users for your system.

Step 1

User Access Configuration Task Flow

Plan the roles and access control groups for your end users. Decide whether the system-defined roles and access control groups
                                          have the access privileges that your deployment requires or if you need to create new roles and new access control groups.

Step 2

Credential Policy Configuration Task Flow

Configure credential policies for your end users.

Step 3

User Profile Configuration Task Flow

Configure user profiles for groups of users who meet the same access and functionality requirements. The user profile consists
                                          of common phone and phone line settings that can allow you to quickly configure new phones and phone lines for users who use
                                          this user profile. You can also enable self-provisioning for users who use this profile.

Step 4

Service Profile Configuration Task Flow

Configure a service profile with settings for Unified Communications (UC) services. You can apply the service profile to groups
                                          of users who have the same services requirements. The service profile allows you to configure UC services for any new phones
                                          provisioned for users who use this service profile.

Step 5

Configure a Feature Group Template

Optional. Configure a feature group template to your end users. A feature group template contains a set of common feature
                                          configurations as well as an assigned user profile and service profile. For LDAP synchronized users you can assign the feature
                                          group template during the LDAP sync thereby assigning a user profile, service profile, line and device templates, and self-provisioning
                                          capability to the user.

Step 6

LDAP Synchronization Configuration Task Flow

If your deployment includes a company LDAP directory, you can import your end users directly from the LDAP directory into
                                          the Cisco Unified Communications Manager database.

Step 7

LDAP Synchronization Configuration Task Flow

If you are not importing end users from an LDAP directory, you can use the Bulk Administration Tool to import the end user
                                          list, and end user configurations, from a CSV file into the Cisco Unified Communications Manager database.

For details on how to use the Bulk Administration Guide to perform bulk transactions to the database, see the Bulk Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 8

Manual End User Configuration Task Flow

Optional. Add new users to the database manually.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | User Access Configuration Task Flow | Plan the roles and access control groups for your end users. Decide whether the system-defined roles and access control groups
                                          have the access privileges that your deployment requires or if you need to create new roles and new access control groups. |
| Step 2 | Credential Policy Configuration Task Flow | Configure credential policies for your end users. |
| Step 3 | User Profile Configuration Task Flow | Configure user profiles for groups of users who meet the same access and functionality requirements. The user profile consists
                                          of common phone and phone line settings that can allow you to quickly configure new phones and phone lines for users who use
                                          this user profile. You can also enable self-provisioning for users who use this profile. |
| Step 4 | Service Profile Configuration Task Flow | Configure a service profile with settings for Unified Communications (UC) services. You can apply the service profile to groups
                                          of users who have the same services requirements. The service profile allows you to configure UC services for any new phones
                                          provisioned for users who use this service profile. |
| Step 5 | Configure a Feature Group Template | Optional. Configure a feature group template to your end users. A feature group template contains a set of common feature
                                          configurations as well as an assigned user profile and service profile. For LDAP synchronized users you can assign the feature
                                          group template during the LDAP sync thereby assigning a user profile, service profile, line and device templates, and self-provisioning
                                          capability to the user. |
| Step 6 | LDAP Synchronization Configuration Task Flow | If your deployment includes a company LDAP directory, you can import your end users directly from the LDAP directory into
                                          the Cisco Unified Communications Manager database. |
| Step 7 | LDAP Synchronization Configuration Task Flow | If you are not importing end users from an LDAP directory, you can use the Bulk Administration Tool to import the end user
                                          list, and end user configurations, from a CSV file into the Cisco Unified Communications Manager database. For details on how to use the Bulk Administration Guide to perform bulk transactions to the database, see the Bulk Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 8 | Manual End User Configuration Task Flow | Optional. Add new users to the database manually. |