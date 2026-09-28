---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-1175f1580e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0100110.html
retrieved_at: 2026-08-16T17:32:01.487799+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure End Users Manually

## Chapter: Configure End Users Manually

# Configure End Users Manually

## Manual End User Provision Overview

Import using Bulk Administration Tool

Manually add new users

## Manual End User Provisioning Prerequisites

Before importing your end users, plan and configure the roles, access aontrol groups, and credential policies for your end
                           users.

User Access Configuration Task Flow

Credential Policy Configuration Task Flow

## Import End Users using Bulk Administration

Using the Bulk Administration Tool, you can perform bulk transactions to the Cisco Unified Communications Manager database,
                           including importing and updating large numbers of end users, phones, and ports, in a single process. The Bulk Administration
                           Tool allows you to  import the end user list, and end user configurations, from a CSV file into the database.

For details on how to use the Bulk Administration Tool to import end users, see the Bulk Administration Guide for Cisco Unified Communications Manager .

## Manual End User Configuration Task Flow

Step 1

Add a New End User

Add a new end user to the database manually.

Step 2

Assign End Users to an Access Control Group

Assign any local end users that you provision to an access control group with the required role permissions. Local users include
                                          any manually provisioned end users and any end users whom you import using the Bulk Administration Tool. Local users have
                                          a User Status of 'Active Local User' in End User Configuration .

Step 3

Apply Credential Policy to End User

(Optional). Confirm if the default credential policy can be applied to this end user. If not, apply a credential policy to
                                          the end user PIN or password.

Step 4

Assign Feature Group Template to Local End Users

Assign a feature group template for the end user. When you assign the feature group template, the system assigns to the end
                                          user the user profile, service profile, universal line and device templates, and self-provisioning settings that are associated
                                          to that feature group template.

### Add a New End
                           	 User

Use this procedure to add a new end user to the Unified Communications Manager database manually.

Step 1

In Cisco Unified CM
                                          			 Administration, choose User Management > End
                                                				  User .

Step 2

Click Add New .

Step 3

Enter the User ID and Last name .

Step 4

Choose the User Rank from the drop-down list.

Step 5

Complete the fields in the End User Configuration window. For field descriptions, see the online help.

Step 6

Click Save .

#### What to do next

Assign End Users to an Access Control Group

### Assign End Users
                           	 to an Access Control Group

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Access Control Group .

Step 2

Click Find and select an access control group.

Step 3

Click Add End Users to Group .

Step 4

In the Find and List Users window, select the end users whom you want to add to the group.

Step 5

Click Add Selected .

Step 6

Click Save .

### Apply Credential Policy to End User

Apply a configured credential policy to a specific end user password or end user PIN. You may need to do this if you need
                                 to make an update from the default credential policy.

You can also apply a credential policy to an application user password. For details, see the Administration Guide for Cisco Unified Communications Manager .

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find and select the end user.

Step 3

Click the Edit Credential button that corresponds to the password or PIN, depending on the credential to which you want to apply the credential policy.

Step 4

From the Authentication Rule drop-down list, choose the credential policy that you want to apply.

Step 5

Complete any additional fields in the Credential Configuration window. For help with the fields and their settings, see the online help.

Step 6

Click Save .

### Assign Feature
                           	 Group Template to Local End Users

Assign a feature group template to a local
                                 		  end user. A local end user is an end user who has been either added to the database manually, or imported using the Bulk
                                 Administration Tool. Local end users are not synchronized with an external LDAP directory.

Step 1

In Cisco Unified CM
                                          			 Administration, choose User
                                                				  Management > User/Phone Add > Quick
                                                				  User/Phone Add .

Step 2

Click Find and select an end user.

Step 3

From the Feature Group Template drop-down list, select the feature group template that you have configured for this end user.

Step 4

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a New End User | Add a new end user to the database manually. |
| Step 2 | Assign End Users to an Access Control Group | Assign any local end users that you provision to an access control group with the required role permissions. Local users include
                                          any manually provisioned end users and any end users whom you import using the Bulk Administration Tool. Local users have
                                          a User Status of 'Active Local User' in End User Configuration . |
| Step 3 | Apply Credential Policy to End User | (Optional). Confirm if the default credential policy can be applied to this end user. If not, apply a credential policy to
                                          the end user PIN or password. |
| Step 4 | Assign Feature Group Template to Local End Users | Assign a feature group template for the end user. When you assign the feature group template, the system assigns to the end
                                          user the user profile, service profile, universal line and device templates, and self-provisioning settings that are associated
                                          to that feature group template. |

| Step 1 | In Cisco Unified CM
                                          			 Administration, choose User Management > End
                                                				  User . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter the User ID and Last name . |
| Step 4 | Choose the User Rank from the drop-down list. |
| Step 5 | Complete the fields in the End User Configuration window. For field descriptions, see the online help. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | Click Find and select an access control group. |
| Step 3 | Click Add End Users to Group . |
| Step 4 | In the Find and List Users window, select the end users whom you want to add to the group. |
| Step 5 | Click Add Selected . |
| Step 6 | Click Save . |

| Note | You can also apply a credential policy to an application user password. For details, see the Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find and select the end user. |
| Step 3 | Click the Edit Credential button that corresponds to the password or PIN, depending on the credential to which you want to apply the credential policy. |
| Step 4 | From the Authentication Rule drop-down list, choose the credential policy that you want to apply. |
| Step 5 | Complete any additional fields in the Credential Configuration window. For help with the fields and their settings, see the online help. |
| Step 6 | Click Save . |

| Step 1 | In Cisco Unified CM
                                          			 Administration, choose User
                                                				  Management > User/Phone Add > Quick
                                                				  User/Phone Add . |
|---|---|
| Step 2 | Click Find and select an end user. |
| Step 3 | From the Feature Group Template drop-down list, select the feature group template that you have configured for this end user. |
| Step 4 | Click Save . |