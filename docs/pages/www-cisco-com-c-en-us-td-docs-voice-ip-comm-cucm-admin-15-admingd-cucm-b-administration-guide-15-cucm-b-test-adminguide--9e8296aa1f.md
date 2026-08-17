---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-admingd-cucm-b-administration-guide-15-cucm-b-test-adminguide--9e8296aa1f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/adminGd/cucm_b_administration-guide-15/cucm_b_test-adminguide_chapter_0100.html
retrieved_at: 2026-08-17T00:36:33.594961+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 31, 2025

Chapter: Manage Application Users

## Chapter: Manage Application Users

# Manage Application Users

## Application Users Overview

The Application User Configuration window in Cisco Unified CM Administration allows the administrator to add, search, display, and maintain information about Cisco Unified Communications Manager application users.

CCMAdministrator

CCMSysUser

CCMQRTSecureSysUser

CCMQRTSysUser

IPMASecureSysUser

IPMASysUser

WDSecureSysUser

WDSysUser

TabSyncSysUser

CUCService

Administrator users in the Standard CCM Super Users group can access Cisco Unified Communications Manager Administration,
                                             Cisco Unified Serviceability, and Cisco Unified Reporting with a single sign-on to one of the applications.

## Application Users
                        	 Task Flow

Step 1

Add New Application User

Add a new
                                          				application user.

Step 2

Associate Devices with Application Users

Assign devices
                                          				to associate with an application user.

Step 3

Add Administrator User to Cisco Unity or Cisco Unity Connection

Add a user as
                                          				an administrator user to Cisco Unity or Cisco Unity Connection. You configure
                                          				the application user in Cisco Unified CM Administration; then, configure any
                                          				additional settings for the user in Cisco
                                             				  Unity or Cisco
                                             				  Unity Connection Administration .

Step 4

Change Application User Password

Change an
                                          				application user password.

Step 5

Manage Application User Password Credential Information

Change or view
                                          				credential information, such as the associated authentication rules, the
                                          				associated credential policy, or the time of last password change for an
                                          				application user.

### Add New
                           	 Application User

Step 1

In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User .

Step 2

Click Add
                                             				New .

Step 3

Configure the
                                          			 fields in the Application User Configuration window. See the online
                                          			 help for information about the fields and their configuration options.

Step 4

Click Save .

#### What to do next

Associate Devices with Application Users

### Associate Devices
                           	 with Application Users

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User .

Step 2

To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, select Find to retrieve a list of users, and then select
                                          			 the user from the list.

Step 3

In the Available Devices list, choose a device that you
                                          			 want to associate with the application user and click the Down
                                             				arrow below the list. The selected device moves to the Controlled Devices list.

To limit the
                                                         				  list of available devices, click the Find more Phones or Find more Route Points button.

Step 4

If you click
                                          			 the Find
                                             				more Phones button, the Find and List
                                             				Phones window displays. Perform a search to find the phones to
                                          			 associate with this application user.

Repeat the
                                             				preceding steps for each device that you want to assign to the application
                                             				user.

Step 5

If you click
                                          			 the Find
                                             				more Route Points button, the Find
                                             				and List CTI Route Points window displays. Perform a search to find
                                          			 the CTI route points to associate with this application user.

Repeat the
                                             				preceding steps for each device that you want to assign to the application
                                             				user.

Step 6

Click Save .

### Add Administrator
                           	 User to Cisco Unity or Cisco Unity Connection

If you are
                                 		  integrating Cisco
                                    			 Unified Communications Manager with Cisco
                                    			 Unity Connection 7.x or later, you can use the import feature that is
                                 		  available in Cisco
                                    			 Unity Connection 7.x or later instead of performing the procedure
                                 		  that is described in the this section. For information on how to use the import
                                 		  feature, see the User Moves,
                                    			 Adds, and Changes Guide for Cisco
                                    			 Unity Connection 7.x or later at

http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .

When the Cisco
                                    			 Unity or Cisco
                                    			 Unity Connection user is integrated with the Cisco
                                    			 Unified CM Application User, you cannot edit the fields. You can only
                                 		  update these fields in Cisco Unified Communications Manager Administration.

Cisco Unity and Cisco
                                    			 Unity Connection monitor the synchronization of data from Cisco
                                    			 Unified Communications Manager . You can configure the sync time in Cisco
                                    			 Unity Administration or Cisco
                                    			 Unity Connection Administration on the tools menu.

#### Before you begin

Ensure that you
                                 		  have defined an appropriate template for the user that you plan to push to Cisco
                                    			 Unity or Cisco
                                    			 Unity Connection

The Create
                                    			 Cisco Unity User link displays only if you install and configure
                                 		  the appropriate Cisco
                                    			 Unity or Cisco
                                    			 Unity Connection software. See the applicable Cisco Unified
                                    			 Communications Manager Integration Guide for Cisco Unity or the
                                 		  applicable Cisco Unified
                                    			 Communications Manager SCCP Integration Guide for Cisco Unity Connection
                                 		  at

http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User .

Step 2

To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, select Find to retrieve a list of users, and then select
                                          			 the user from the list.

Step 3

From the Related Links drop-down list, choose the Create Cisco Unity
                                             				Application User link and click Go .

Step 4

From the Application Server drop-down list, choose the Cisco
                                          			 Unity or Cisco Unity Connection server on which you want to create a Cisco
                                          			 Unity or Cisco Unity Connection user and click Next .

Step 5

From
                                          			 the Application
                                             				User Template drop-down list, choose the template that you want to
                                          			 use.

Step 6

Click Save .

### Change Application User Password

Step 1

From Cisco Unified CM Administration, choose User Management > Application User .

Step 2

To select an existing user, specify the appropriate filters in the Find User Where field, select Find to retrieve a list of users, and then select the user from the list.

Step 3

In the Password field, double click the existing, encrypted password and enter the new password.

Step 4

In the Confirm Password field, double click the existing, encrypted password and enter the new password again.

Step 5

Click Save .

### Manage Application
                           	 User Password Credential Information

Perform the
                                 		  following procedure to manage credential information for an application user
                                 		  password. This allows you to perform administrative duties such as locking a
                                 		  password, applying a credential policy to a password, or viewing information
                                 		  such as the time of the last failed login attempt.

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User .

Step 2

To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, select Find to retrieve a list of users, and then select
                                          			 the user from the list.

Step 3

To change or
                                          			 view password information, click the Edit
                                             				Credential button next to the Password field.

Step 4

Configure the fields on the Credential Configuration window. See the online
                                          			 help for more information about the fields and their configuration options.

Step 5

If you have
                                          			 changed any settings, click Save .

| Note | Administrator users in the Standard CCM Super Users group can access Cisco Unified Communications Manager Administration,
                                             Cisco Unified Serviceability, and Cisco Unified Reporting with a single sign-on to one of the applications. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add New Application User | Add a new
                                          				application user. |
| Step 2 | Associate Devices with Application Users | Assign devices
                                          				to associate with an application user. |
| Step 3 | Add Administrator User to Cisco Unity or Cisco Unity Connection | Add a user as
                                          				an administrator user to Cisco Unity or Cisco Unity Connection. You configure
                                          				the application user in Cisco Unified CM Administration; then, configure any
                                          				additional settings for the user in Cisco
                                             				  Unity or Cisco
                                             				  Unity Connection Administration . |
| Step 4 | Change Application User Password | Change an
                                          				application user password. |
| Step 5 | Manage Application User Password Credential Information | Change or view
                                          				credential information, such as the associated authentication rules, the
                                          				associated credential policy, or the time of last password change for an
                                          				application user. |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Configure the
                                          			 fields in the Application User Configuration window. See the online
                                          			 help for information about the fields and their configuration options. |
| Step 4 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User . The Find
                                             				and List Users window appears. |
|---|---|
| Step 2 | To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, select Find to retrieve a list of users, and then select
                                          			 the user from the list. |
| Step 3 | In the Available Devices list, choose a device that you
                                          			 want to associate with the application user and click the Down
                                             				arrow below the list. The selected device moves to the Controlled Devices list. Note To limit the
                                                         				  list of available devices, click the Find more Phones or Find more Route Points button. | Note | To limit the
                                                         				  list of available devices, click the Find more Phones or Find more Route Points button. |
| Note | To limit the
                                                         				  list of available devices, click the Find more Phones or Find more Route Points button. |
| Step 4 | If you click
                                          			 the Find
                                             				more Phones button, the Find and List
                                             				Phones window displays. Perform a search to find the phones to
                                          			 associate with this application user. Repeat the
                                             				preceding steps for each device that you want to assign to the application
                                             				user. |
| Step 5 | If you click
                                          			 the Find
                                             				more Route Points button, the Find
                                             				and List CTI Route Points window displays. Perform a search to find
                                          			 the CTI route points to associate with this application user. Repeat the
                                             				preceding steps for each device that you want to assign to the application
                                             				user. |
| Step 6 | Click Save . |

| Note | To limit the
                                                         				  list of available devices, click the Find more Phones or Find more Route Points button. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User . |
|---|---|
| Step 2 | To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, select Find to retrieve a list of users, and then select
                                          			 the user from the list. |
| Step 3 | From the Related Links drop-down list, choose the Create Cisco Unity
                                             				Application User link and click Go . The Add Cisco
                                             				Unity User dialog displays. |
| Step 4 | From the Application Server drop-down list, choose the Cisco
                                          			 Unity or Cisco Unity Connection server on which you want to create a Cisco
                                          			 Unity or Cisco Unity Connection user and click Next . |
| Step 5 | From
                                          			 the Application
                                             				User Template drop-down list, choose the template that you want to
                                          			 use. |
| Step 6 | Click Save . The
                                          			 administrator account gets created in Cisco
                                             				Unity or Cisco
                                             				Unity Connection . The link in Related Links changes to Edit
                                             				Cisco Unity User in the Application User Configuration window. You can now view the user that you created in Cisco
                                             				Unity Administration or Cisco
                                             				Unity Connection Administration . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > Application User . The Find and List Users window appears. |
|---|---|
| Step 2 | To select an existing user, specify the appropriate filters in the Find User Where field, select Find to retrieve a list of users, and then select the user from the list. The Application User Configuration window displays information about the chosen application user. |
| Step 3 | In the Password field, double click the existing, encrypted password and enter the new password. |
| Step 4 | In the Confirm Password field, double click the existing, encrypted password and enter the new password again. |
| Step 5 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User . The Find
                                             				and List Users window appears. |
|---|---|
| Step 2 | To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, select Find to retrieve a list of users, and then select
                                          			 the user from the list. The Application User Configuration window displays
                                          			 information about the chosen application user. |
| Step 3 | To change or
                                          			 view password information, click the Edit
                                             				Credential button next to the Password field. The
                                          			 user Credential Configuration is displayed. |
| Step 4 | Configure the fields on the Credential Configuration window. See the online
                                          			 help for more information about the fields and their configuration options. |
| Step 5 | If you have
                                          			 changed any settings, click Save . |