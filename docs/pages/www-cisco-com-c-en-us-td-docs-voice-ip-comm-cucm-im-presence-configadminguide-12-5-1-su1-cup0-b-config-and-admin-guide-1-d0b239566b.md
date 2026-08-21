---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su1-cup0-b-config-and-admin-guide-1-d0b239566b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su1/cup0_b_config-and-admin-guide-1251su1/cup0_b_config-and-admin-guide-1251su1_chapter_0101.html
retrieved_at: 2026-08-21T09:00:56.154306+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU1

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU1

Updated: November 27, 2024

Chapter: Configure User Settings

## Chapter: Configure User Settings

# Configure User Settings

## End User Settings  Overview

You can use user settings such as Service Profiles and Feature Group Templates to apply common settings to your end users
                           via an LDAP Directory sync.  When the LDAP Directory sync occurs the configured settings get applied to all synced users.

This chapter covers user settings that apply to the IM and Presence Service, specifically. For general UC user configurations,
                                       including UC services such as voicemail and conferencing, refer to the "Configure End Users" section of the System Configuration Guide for Cisco Unified Communications Manager . You can apply these configurations as a part of your LDAP sync.

### Service Profiles

A service profile contains common Unified Communications (UC) Services settings. You can configure different service profiles
                              for different groups of users so that each group of users has the appropriate services configured for their job. To enable
                              end users to access the IM and Presence Service configure the service profile so that it includes the  IM and Presence Service.

You can use the following methods to apply a service profile to an end user:

For LDAP Synchronized Users—If you have imported end users from an LDAP directory, you can assign the service profile to a
                                    feature group template and then apply that feature group template to your end users.  The settings in the template get applied
                                    to all synchronized users.

For Active Local Users (i.e. non-LDAP users)—To apply settings to a large number of users at once, use the Bulk Administration
                                    Tool to apply service profile settings via a csv file or spreadsheet. For details on how to use the Bulk Administration Tool
                                    at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Otherwise, you can configure user settings manually, on a user-by-user basis.

### Feature Group Template Overview

Feature group templates help you to quickly apply common settings to groups of end users via an LDAP directory sync. For
                              example, you can use the Feature Group Template to enable the IM and Presence Service for your end users. This is accomplished
                              by applying an IM and Presence-enabled Service Profile to the template. When you apply the feature group template to an LDAP
                              directory sync, when the sync occurs the settings from the template, including the configured Service Profile and User Profile
                              settings, get applied to all synced users.

Feature group template configuration includes the following profiles that you can assign to the feature group template:

User Profile—contains a set of common phone and phone line settings. You must configure the user profile with a universal
                                    line template, which assigns the common phone line settings, and a universal device template, which assigns the common phone
                                    settings. These templates assist users who are set up for self-provisioning to configure their own phones.

Service Profile—contains a group of common UC services, such as the IM and Presence Service, directory, or voicemail.

## User Settings Prerequisites

If you want to move users between IM and Presence
                                 Service clusters, you must do so before you
                              configure end users. For information about how to use Cisco
                                 Unified CM IM and Presence Administration to
                              migrate users, and export or import contact
                              lists.

Migrating users between clusters should not be confused with the User Migration Tool used for Partitioned Intra-domain Federation.

If you have Cisco Jabber connected over VPN, during the TLS handshake between the IM and Presence Service and the Cisco Jabber
                                          client, the IM and Presence server performs a reverse lookup for the client’s IP subnet. If the reverse lookup fails, the
                                          TLS handshake times out in the client machine.

## Configure User Settings Task Flow

Complete these tasks to configure user templates with common service  and feature settings, such as enabling end users for
                              the IM and Presence Service. When you complete an LDAP sync, your template settings will be applied to your end users.

This chapter task flow user settings that apply to the IM and Presence Service, specifically. For general UC user configurations,
                                          including UC services such as voicemail and conferencing, refer to the "Configure End Users" section of the System Configuration Guide for Cisco Unified Communications Manager . You can apply these configurations as a part of your LDAP sync.

Step 1

Configure the User Assignment Mode

Set the user assignment mode to balanced, active-stand-by, or none.

Step 2

Add an IM and Presence UC Service

Set up an IM and Presence UC service on Cisco Unified Communications Manager.

Step 3

Configure a Service Profile

Configure a service profile that contains the IM and Presence UC service that you added.

Step 4

Configure a Feature Group Template

Configure a feature group template that includes the service profile that you set up in addition to other common feature settings.

### What to do next

Complete an LDAP sync to apply the settings to LDAP-synchronized users.

### Configure the User Assignment Mode

Use this procedure to configure  the way in which the sync agent will
                                 distribute users to the nodes in the cluster.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

In the User Management Parameters Area, choose one of the following options for the User Assignment Mode for Presence Server parameter:

- Balanced —This mode assigns
                                             users equally to each node in each subcluster and attempts to
                                             balance the total number of users equally across each node. This is the default option.

- Active-Standby —This mode assigns all users to the first node of the
                                             subcluster, leaving the secondary server as a backup.

- None —This mode results in no assignment of the users to the nodes in the cluster
                                             by the sync agent.

Step 3

Click Save .

#### What to do next

Add an IM and Presence UC Service

### Add an IM and Presence UC Service

Use this procedure in Cisco Unified Communications Manager add a UC service for the IM and Presence Service.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose IM and Presence .

Step 4

From the Product Type drop-down list box, choose Unified CM (IM and Presence) .

Step 5

Enter a Name and Description for the IM and Presence service.

Step 6

In the Hostname/IP Address field, enter a hostname, IP address, or DNS SRV for the server that hosts the IM and Presence Service.

Step 7

Click Save .

#### What to do next

To enable users for the IM and Presence Service, assign the UC Service to a Service Profile and assign that profile to you
                                 users.

Configure a Service Profile .

### Configure a Service Profile

Use this procedure to configure a service profile that contains the IM and Presence Service .

#### Before you begin

Add an IM and Presence UC Service

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile .

Step 2

Do either of the following

- Click Find and select an existing profile

- Click Add New to create a new profile

Step 3

In the IM and Presence Profile section, select the Primary IM and Presence server.

Step 4

Complete the remaining fields in the Service Profile Configuration window. For help with the fields and their settings, see the online help

Step 5

Click Save .

#### What to do next

Configure a Feature Group Template

### Configure a Feature Group Template

Configure a feature group template that includes common feature settings as well as the IM and Presence-enabled service profile
                                 that you set up.

#### Before you begin

Configure a Service Profile

Step 1

In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > User/Phone Add > Feature Group
                                                				  Template .

Step 2

Click Add
                                             				New .

Step 3

Enter a Name and Description for the Feature Group Template.

Step 4

Check the Home Cluster check box if you want to use the local cluster as the home cluster for all users whom use this template.

Step 5

Check the Enable User for Unified CM IM and Presence check box to allow users whom use this template to exchange instant messaging and presence information.

Step 6

From the drop-down list, select a Services Profile and User Profile .

Step 7

Complete the
                                          			 remaining fields in the Feature
                                             				Group Template Configuration window. Refer to the online help for
                                          			 field descriptions.

Step 8

Click Save .

#### What to do next

Configure an LDAP Directory sync that includes this feature group template. When you complete the LDAP Sync, the IM and Presence
                                 settings in the  template get applied to synchronized users. See LDAP Synchronization Configuration Task Flow .

| Note | This chapter covers user settings that apply to the IM and Presence Service, specifically. For general UC user configurations,
                                       including UC services such as voicemail and conferencing, refer to the "Configure End Users" section of the System Configuration Guide for Cisco Unified Communications Manager . You can apply these configurations as a part of your LDAP sync. |
|---|---|

| Note | Migrating users between clusters should not be confused with the User Migration Tool used for Partitioned Intra-domain Federation. |
|---|---|

| Note | If you have Cisco Jabber connected over VPN, during the TLS handshake between the IM and Presence Service and the Cisco Jabber
                                          client, the IM and Presence server performs a reverse lookup for the client’s IP subnet. If the reverse lookup fails, the
                                          TLS handshake times out in the client machine. |
|---|---|

| Note | This chapter task flow user settings that apply to the IM and Presence Service, specifically. For general UC user configurations,
                                          including UC services such as voicemail and conferencing, refer to the "Configure End Users" section of the System Configuration Guide for Cisco Unified Communications Manager . You can apply these configurations as a part of your LDAP sync. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure the User Assignment Mode | Set the user assignment mode to balanced, active-stand-by, or none. |
| Step 2 | Add an IM and Presence UC Service | Set up an IM and Presence UC service on Cisco Unified Communications Manager. |
| Step 3 | Configure a Service Profile | Configure a service profile that contains the IM and Presence UC service that you added. |
| Step 4 | Configure a Feature Group Template | Configure a feature group template that includes the service profile that you set up in addition to other common feature settings. |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | In the User Management Parameters Area, choose one of the following options for the User Assignment Mode for Presence Server parameter: Balanced —This mode assigns
                                             users equally to each node in each subcluster and attempts to
                                             balance the total number of users equally across each node. This is the default option. Active-Standby —This mode assigns all users to the first node of the
                                             subcluster, leaving the secondary server as a backup. None —This mode results in no assignment of the users to the nodes in the cluster
                                             by the sync agent. |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose IM and Presence . |
| Step 4 | From the Product Type drop-down list box, choose Unified CM (IM and Presence) . |
| Step 5 | Enter a Name and Description for the IM and Presence service. |
| Step 6 | In the Hostname/IP Address field, enter a hostname, IP address, or DNS SRV for the server that hosts the IM and Presence Service. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile . |
|---|---|
| Step 2 | Do either of the following Click Find and select an existing profile Click Add New to create a new profile |
| Step 3 | In the IM and Presence Profile section, select the Primary IM and Presence server. |
| Step 4 | Complete the remaining fields in the Service Profile Configuration window. For help with the fields and their settings, see the online help |
| Step 5 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > User/Phone Add > Feature Group
                                                				  Template . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Enter a Name and Description for the Feature Group Template. |
| Step 4 | Check the Home Cluster check box if you want to use the local cluster as the home cluster for all users whom use this template. |
| Step 5 | Check the Enable User for Unified CM IM and Presence check box to allow users whom use this template to exchange instant messaging and presence information. |
| Step 6 | From the drop-down list, select a Services Profile and User Profile . |
| Step 7 | Complete the
                                          			 remaining fields in the Feature
                                             				Group Template Configuration window. Refer to the online help for
                                          			 field descriptions. |
| Step 8 | Click Save . |