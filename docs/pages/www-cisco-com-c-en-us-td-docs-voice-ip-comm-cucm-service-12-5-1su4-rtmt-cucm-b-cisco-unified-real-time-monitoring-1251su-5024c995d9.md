---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1su4-rtmt-cucm-b-cisco-unified-real-time-monitoring-1251su-5024c995d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1SU4/rtmt/cucm_b_cisco-unified-real-time-monitoring-1251su4/cucm_b_cisco-unified-rtmt-administration-1251su2_chapter_0101.html
retrieved_at: 2026-08-21T01:41:29.362279+00:00
---

Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)SU4

# Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)SU4

Updated: January 9, 2023

Chapter: Profiles and Categories

## Chapter: Profiles and Categories

# Profiles and Categories

## Profiles

This section describes about how to add, restore, and delete the configuration profile.

### Add Configuration
                           	 Profile

With RTMT,
                                 		  you can customize your monitoring window by monitoring different performance
                                 		  counters and then create your own configuration profiles. You can restore these
                                 		  monitoring windows in a single step rather than opening each window again.

You can switch
                                 		  between different profiles during the same RTMT session or use the
                                 		  configuration profile in subsequent RTMT sessions.

Follow
                                 		  this procedure to create a profile.

Step 1

Choose File > Profile .

The Preferences
                                             				dialog box appears.

Step 2

Click Save .

The Save Current
                                             				Configuration dialog box appears.

Step 3

In the
                                          			 Configuration name field, enter a name for this particular configuration
                                          			 profile.

Step 4

In the
                                          			 Configuration description field, enter a description of this particular
                                          			 configuration profile.

Profiles apply
                                                         				  to all nodes within a cluster, but you cannot save and apply the profile to a
                                                         				  different cluster.

The system
                                             				creates the new configuration profile.

### Restore
                           	 Configuration Profile

Perform
                                 		  the following procedure to restore a profile that you configured:

Step 1

Choose File > Profile .

The Preferences
                                             				dialog box appears.

Step 2

Click the
                                          			 profile that you want to restore.

Step 3

Click Restore .

All windows with
                                             				precanned settings or performance monitoring counters for the restored
                                             				configuration open.

### Delete Configuration
                           	 Profile

Perform
                                 		  the following procedure to delete a profile that you configured:

Step 1

Choose File > Profile .

The Preferences
                                             				dialog box appears.

Step 2

Click the
                                          			 profile that you want to delete.

Step 3

Click Delete .

Step 4

Click Close .

## Categories

### Add Category

Follow this procedure to add a category.

Step 1

Go to the applicable window for your configuration:

Unified Communications Manager

Choose System > Performance > Open Performance Monitoring .

Unified Communications Manager IM and Presence Service

Choose System > Performance > Open Performance Monitoring .

Cisco Unity Connection

Choose System > Performance > Open Performance Monitoring .

Step 2

Choose Edit > Add New Category .

Step 3

Enter the name of the category; click OK .

The category tab appears at the bottom of the window.

### Rename
                           	 Category

To rename a
                                 		  category, perform the following procedure:

Step 1

Perform one of
                                          			 the following tasks:

Right-click
                                                				  the category tab that you want to rename and choose Rename Category .

Click the
                                                				  category tab that you want to rename and choose Edit > Rename
                                                      						Category .

Step 2

Enter the new
                                          			 name and click OK .

The renamed
                                             				category displays at the bottom of the window.

### Delete
                           	 Category

To delete a
                                 		  category, perform one of the following tasks:

Right-click the category tab that you want to delete and choose Remove Category .

Click the category tab that you want to delete and choose Edit > Remove Category .

| Step 1 | Choose File > Profile . The Preferences
                                             				dialog box appears. |
|---|---|
| Step 2 | Click Save . The Save Current
                                             				Configuration dialog box appears. |
| Step 3 | In the
                                          			 Configuration name field, enter a name for this particular configuration
                                          			 profile. |
| Step 4 | In the
                                          			 Configuration description field, enter a description of this particular
                                          			 configuration profile. Note Profiles apply
                                                         				  to all nodes within a cluster, but you cannot save and apply the profile to a
                                                         				  different cluster. The system
                                             				creates the new configuration profile. | Note | Profiles apply
                                                         				  to all nodes within a cluster, but you cannot save and apply the profile to a
                                                         				  different cluster. |
| Note | Profiles apply
                                                         				  to all nodes within a cluster, but you cannot save and apply the profile to a
                                                         				  different cluster. |

| Note | Profiles apply
                                                         				  to all nodes within a cluster, but you cannot save and apply the profile to a
                                                         				  different cluster. |
|---|---|

| Step 1 | Choose File > Profile . The Preferences
                                             				dialog box appears. |
|---|---|
| Step 2 | Click the
                                          			 profile that you want to restore. |
| Step 3 | Click Restore . All windows with
                                             				precanned settings or performance monitoring counters for the restored
                                             				configuration open. |

| Step 1 | Choose File > Profile . The Preferences
                                             				dialog box appears. |
|---|---|
| Step 2 | Click the
                                          			 profile that you want to delete. |
| Step 3 | Click Delete . |
| Step 4 | Click Close . |

| Step 1 | Go to the applicable window for your configuration: Unified Communications Manager Choose System > Performance > Open Performance Monitoring . Unified Communications Manager IM and Presence Service Choose System > Performance > Open Performance Monitoring . Cisco Unity Connection Choose System > Performance > Open Performance Monitoring . | Unified Communications Manager | Choose System > Performance > Open Performance Monitoring . | Unified Communications Manager IM and Presence Service | Choose System > Performance > Open Performance Monitoring . | Cisco Unity Connection | Choose System > Performance > Open Performance Monitoring . |
|---|---|---|---|---|---|---|---|
| Unified Communications Manager | Choose System > Performance > Open Performance Monitoring . |
| Unified Communications Manager IM and Presence Service | Choose System > Performance > Open Performance Monitoring . |
| Cisco Unity Connection | Choose System > Performance > Open Performance Monitoring . |
| Step 2 | Choose Edit > Add New Category . |
| Step 3 | Enter the name of the category; click OK . The category tab appears at the bottom of the window. |

| Unified Communications Manager | Choose System > Performance > Open Performance Monitoring . |
|---|---|
| Unified Communications Manager IM and Presence Service | Choose System > Performance > Open Performance Monitoring . |
| Cisco Unity Connection | Choose System > Performance > Open Performance Monitoring . |

| Step 1 | Perform one of
                                          			 the following tasks: Right-click
                                                				  the category tab that you want to rename and choose Rename Category . Click the
                                                				  category tab that you want to rename and choose Edit > Rename
                                                      						Category . |
|---|---|
| Step 2 | Enter the new
                                          			 name and click OK . The renamed
                                             				category displays at the bottom of the window. |