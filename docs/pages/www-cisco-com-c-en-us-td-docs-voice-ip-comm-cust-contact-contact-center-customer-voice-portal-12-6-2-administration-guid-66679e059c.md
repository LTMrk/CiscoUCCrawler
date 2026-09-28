---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-administration-guid-66679e059c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/administration/guide/ccvp_b_1262-admin-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-admin-guide-for-cisco-unified-customer-voice-portal_chapter_011.html
retrieved_at: 2026-08-21T02:56:00.249899+00:00
---

Administration Guide for Cisco Unified Customer Voice Portal 12.6(2)

# Administration Guide for Cisco Unified Customer Voice Portal 12.6(2)

Updated: April 28, 2023

Chapter: Managing Unified CVP Users

## Chapter: Managing Unified CVP Users

# Managing Unified CVP Users

From the User Management menu, Users option, you can create one user account
                        at a time. Unified CVP includes the Super User, Administrator, Read
                        Only, and Serviceability Administration roles. You can assign users to any of these
                        roles. The Unified CVP installation creates an Administrator account, which is
                        assigned to the Super User role and a "wsmadmin" account which is assigned a
                        Serviceability Administration role.

User groups are provided so that you can group users together. Assigning users
                        to groups limits the operations users can perform from the Operations Console
                        menus. For example, administrators for San Jose devices can belong to a user
                        group called SanJose_Admins with Administrator privilege.

Device pools are logical groupings of devices, for example, SanJose-Gateways.
                        If a user is configured with SanJose-Gateways as the device pool, then that user
                        can operate only on devices in this device pool. The types of allowed
                        operations also depends on which user group the user belongs to. For example, if
                        a user belongs to SanJose_Admins, a group with Administrator privilege, then
                        this user has Administrator privilege for devices in the
                        SanJose-Gateways device pool.

Unified CVP includes four categories of access criteria:

Super User - Allows any operation in the Operations Console. Only the
                              Super User can create and delete Administrator accounts and assign
                              device pools to any user. The Super User can view all devices because
                              this account is associated with the "default" device
                              pool.

Administrator - Allows any operation in the Operations Console except
                              deleting Administrator accounts. Administrators can only view devices in
                              the device pools to which they have been associated. Administrators can
                              disassociate themselves from a device pool, but cannot associate
                              themselves to a device pool.

Read Only- Allows read-only access to the Operation Console.

Serviceability Administration - Allows Web Services authentication
                              through the Unified System CLI tool and does not provide any
                              privileges for the Operations Console. Only the Administrator can create
                              and delete Web Services users. Whenever Web Services user information is
                              changed or whenever a Unified CVP device is deployed successfully, the
                              configured Web Services users are pushed to all deployed Unified CVP
                              devices (see Web Services ).

Users roles that have Serviceability Administration applied cannot
                              have any roles assigned that contain Super User, Administrator, or Read
                              Only privileges.

Serviceability users such as wsmadmin (CLI/some REST APIs) and Readonly users (OAMP/NOAMP) cannot access their respective
                                          services after installing or upgrading to CVP 12.6, until an Administrator user resets their password through the Operations
                                          Console (OAMP).

## User Role Management

A user role is a logical group of privileges, also called access criteria, that determine the operations a user can perform.
                              For example, you might create a role that grants an operator read-only access to the Reporting Server, but grants write access
                              to the Unified CVP VXML Servers. You can do this by creating an operator user group and assigning that group the default Administrator
                              privilege, which allows any operation except deleting accounts with superuser privilege. Then, create a device pool that contains
                              all Unified CVP VXML Servers. Finally, assign the Unified CVP VXML Server device pool to the operator user group.

### Add User Role

To add a user role:

Step 1

Select User Management > User
                                                   				  Roles from the Main menu.

The Find, Add, Delete, Edit window opens.

Step 2

Select Add New .

Step 3

On the General tab, fill in the name of the role in the Role Name
                                             			 field.

Step 4

Fill in descriptive text in the Description field, if desired.

Step 5

Select the Access Criteria tab and assign 
                                             			 access criteria to
                                             			 the user role. 
                                             		  See Assign User Role Access Criteria .

A default Access Criteria of Administrator is applied to every new
                                                				user role you create.

Step 6

When you finish configuring the user role, click Save to save the configuration.

### Edit User Role

You can change the access criteria, which are privileges, assigned to
                                    		  a user role that has been added to the Operations Console.

Step 1

Select User Management > User
                                                   				  Roles from the Main menu.

The Find, Add, Delete, Edit Application User Roles window opens.

Step 2

Select the desired Role Name link or select the user role from the
                                             			 list and click Edit . If you have a long list of user roles,
                                             			 see Find User Role .

The Edit Application User Role window opens to the General tab.

Step 3

Change the description for the user role, if desired.

Step 4

Select the Access Criteria tab and change the 
                                             			 access criteria assigned to the user role. 
                                             		  See Assign User Role Access Criteria .

Step 5

When you finish configuring the user role, select Save .

### Assign User Role Access Criteria

Add User Role

Edit User Role

To assign access criteria to a user role:

Step 1

Select Access Criteria tab.

Step 2

Select the desired access criteria.

Step 3

Click Save to save the user role with assigned
                                             access criteria to the Operations Console database.

### Find User Role

To find a user role:

Step 1

Select User Management > User
                                                   				  Roles .

The Find, Add, Delete, Edit window opens.

Step 2

If the list is long, you can click the first page, previous page,
                                             			 next page, and last page icons on the bottom right of the window to page
                                             			 through the list. Or, you can enter a page number in the Page field and press 
                                             			 Enter to go to the numbered page.

Step 3

Filter the list by selecting an attribute such as Role Name . Select a modifier, such as begins with . Enter your search term and click Find .

### Delete User Roles

To delete a user role:

Step 1

Select User Management > User
                                                   				  Roles .

The Find, Add, Delete, Edit Application User Roles window opens.

Step 2

Find the user roles using the procedure shown in Find User Role .

Step 3

From the list of matching records, select the user roles that you
                                             			 want to delete.

Step 4

Select Delete .

Step 5

When prompted to confirm the delete operation, perform one of the following steps:.

- Select OK to delete the operation.

- Select Cancel to cancel the operation.

### Service Types User Roles and User Group Associations

In Unified CVP,  the Operations Console allows you
                                 to add a new type of user role: a Web Services (Serviceability
                                 Administration) user role.

The Operation Console does not support a mix-and-match of various user
                                 roles. The existing Operations Console service type user roles (Super User,
                                 Administrator, and Read-only users) cannot co-exist with the Web service
                                 type user roles (Web Services users) within a single user group.

Whenever you add/modify/delete a Web Services user role, a current list of
                                 Web Services users is pushed to all deployed Unified CVP devices.

The end user receives a validation error in the following
                                 situations:

When you edit any user role, the list of user groups associated
                                       with this user role are retrieved. If the user role changes and
                                       causes a mismatch of user role service types within any of its
                                       associated user groups.

A role changes and causes a mismatch of user role service
                                       types within any of its associated users.

Users assigned a Web Services user role cannot log into the Operations
                                 Console.

## User Group Management

A user group is a collection of users to which you can assign one or more user
                              roles. These groups limit the operations that users can perform
                              to the Operations Console.

### Add User Group

To add a User Group:

Step 1

Select User Management > User
                                                   				  Groups .

The Find, Add, Delete, Edit Application User Groups window opens.

Step 2

Select Add New .

Step 3

Fill in the name of the group in the Group Name field.

Step 4

Fill in descriptive text in the Description field, if desired.

Step 5

Select the User Roles tab and assign a user role to the
                                             			 user group. See Assign Role to User Group for details.

You must assign at least one user role to each user group you
                                                				create.

Step 6

When you finish configuring the user group, select Save .

### Edit User Groups

To edit a User Group:

Step 1

Select User Management > User
                                                   				  Groups .

The Find, Add, Delete, Edit User Groups window opens.

Step 2

If you have a long list of user groups, see Find User Group to narrow the list of choices.

Step 3

Select the radio button next to the User Group name and click Edit or click the Group Name. See Assign Role to User Group for details.

The User Group Configuration window opens to the General tab.

Step 4

You can change the description for the group by editing the
                                             			 Description field.

Step 5

Select the User Roles tab and edit the assigned roles for
                                             			 this user group.

Step 6

When you finish configuring the user group, click Save .

### Assign Role to User Group

Add User Group

Edit User Groups

To assign a user role to a user group:

Step 1

If you want to add a user role to a user group, select the user
                                             role from the Available pane, and then click the
                                             right arrow to move the user role to the Selected pane.

Step 2

To remove a user role from a user group, select the user role
                                             from the Selected pane, and then click the left
                                             arrow to move the user role to the Available pane.

Step 3

Click Save .

### Delete User Group

To delete a user
                                    		  group from the Operations Console:

Step 1

Select User Management > User Groups .

The Find, Add,
                                                				Delete, Edit Application User Groups window opens.

Step 2

Find the groups
                                             			 by using the procedure in Find User Group .

Step 3

From the list of
                                             			 matching records, select the user groups that you want to delete.

Step 4

Select Delete .

Step 5

When prompted to
                                             			 confirm the delete operation, perform one of the following steps:

- Select OK to delete the operation

- Select Cancel to cancel the delete operation

### Find User Group

To find a user group:

Step 1

Select User Management > User Groups User Management .

The Find, Add, Delete, Edit Application User Groups Window lists
                                                				the available user groups.

Step 2

If the list is long, you can perform one of the following steps:

- Select the first page, previous page,
                                                			 next page, and last page icons on the bottom right of the window to page
                                                			 through the list, or

- Enter a page number in the Page field and press Enter to go to the numbered page.

Step 3

To filter the list, perform the following steps:

Select an attribute,  such as Group Name

Select a modified, such as begins with

Enter your search term

Select Find

## Unified CVP User Setup

From the User Management menu, Users option, you can create one user account at a time. Unified CVP includes four roles: Super
                              User, Administrator, and Read Only in the Operations Console Server type of role, and Serviceability Administration in the
                              Web Services type of role. You can assign users to any of these roles; however, you cannot assign users to roles that include
                              both the Operations Console type and the web services type. See Assign User Role Access Criteria for information about this restriction.

### General User Information Settings

Configure general
                                 information about a Unified CVP user when you:

Adding a user account

Editing a user account

Field

Description

Default

Range

Restart Required

User Information

Username

Name of the user account. The user logs in to the
                                             Operations Console using this name. After logging in,
                                             the username is displayed in the upper right portion of
                                             the screen. You cannot change the username when editing
                                             a user account.

None

Valid names include uppercase and lowercase letters in
                                             the alphabet, the numbers 0 through 9, a dash, and an
                                             underscore.

No

Password

New password for the user account. User must type this password to log into the Operations Console.

None

Any text that follows the guidelines for choosing secure passwords

No

Reconfirm Password

Retype the password for this user account to verify
                                             that you typed the password correctly.

None

Text must match the text entered in the Password
                                             field.

No

Firstname

(Optional) First name of the user.

None

Valid names include uppercase and lowercase letters in
                                             the alphabet, the numbers 0 through 9, a dash, and an
                                             underscore.

No

Lastname

(Optional) Last name of the user.

None

Valid names include uppercase and lowercase letters in
                                             the alphabet, the numbers 0 through 9, a dash, and an
                                             underscore.

No

E-mail

(Optional) e-mail address of the user.

None

Valid e-mail address

No

Signed in User Password

The password used to log into the user account.

None

Valid e-mail address

No

#### Secure Password
                              	 Requirements

Passwords must meet all the following criteria.

Passwords must only
                                    		  contain the following ASCII characters:

Maximum password
                                          				length is 80 characters.

Minimum
                                          				password length is 12 characters

The password
                                          				must contain characters from at least three of the following classes: lowercase
                                          				characters, uppercase characters, digits, and special characters.

Lowercase
                                                					 letters (abcdefghijklmnopqrstuvwxyz)

Uppercase
                                                					 letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ)

Digits
                                                					 (012345689)

Special characters: !#$&()*+-./ :<?@ [\]_` {}~

No character in
                                          				the password can be repeated more than three (3) times consecutively.

Password must
                                          				not repeat or reverse username. Password is not cisco , ocsic , or any variant obtained by changing the
                                          				capitalization of letters therein.

### Add User Account

Before You Begin

When you are adding
                                    		  a new user for the first time after installing Unified CVP software, you must
                                    		  create at least one user role and user group before creating the user account.
                                    		  For information on performing these tasks, see Add User Role , Add User Group .

You must create Device Pools to further limit access to devices.
                                                			 See Add Device Pool to Operations Console .

To add a user
                                    		  account:

Step 1

Select User
                                                   				  Management > Users .

The Find, Add,
                                                				Delete, Edit Application Users window opens.

Step 2

Select Add
                                                				New .

Step 3

Fill in the
                                             			 appropriate configuration settings on the General tab.

Step 4

Select the Device
                                                				Pools tab and assign a Device Pool to the user. Each user must be
                                             			 assigned to at least one device pool. See Add or Remove User From Device Pool .

Step 5

Select the User
                                                				Group tab and add the user to one or more user groups. See Add User Group .

Step 6

When you finish
                                             			 configuring the user, click Save .

### Edit User Account

You can change one or more settings for a user account that has been
                                    		  added to the Operations Console.

Step 1

Select User Management > Users .

The Find, Add, Delete, Edit Users window opens.

Step 2

Select the desired Username link or select radio button next to the
                                             			 username from and select Edit . You can reduce the list of users
                                             			 displayed. See Find User Account .

The Edit User page opens to the General tab.

Step 3

Fill in the appropriate configuration settings on the General tab
                                             			 as described in General User Information Settings .

Step 4

Select the Device Pools tab and assign a device pool to the user.
                                             			 See Add or Remove User From Device Pool .

Step 5

Select the User Groups tab and add/remove the user to/from one or
                                             			 more user groups. See Add User Group .

Step 6

When you finish configuring the user, select Save .

### Delete User Account

To delete a user account:

Step 1

Select User
                                                   				  Management > User .

The Find, Add, Delete, Edit Application Users window opens.

Step 2

From the list of users, select the user that you want to delete.
                                             			 You can reduce the list of users displayed. See Find User Account

Step 3

Select Delete .

Step 4

When prompted to confirm the delete operation, perform one of the following steps:

- Select OK to delete.

- Select Cancel to cancel the delete operation.

### Find User Account

To find a user:

Step 1

Select User
                                                   				  Management > User .

The Find, Add, Delete, Edit Application Users window opens.

Step 2

Perform one of the following steps:

- If the list is long, select the first page, previous page,
                                                			 next page, and last page icons on the bottom right of the window to page
                                                			 through the list.

- Enter a page number in the Page field and press 
                                                			 Enter to go directly to the numbered page.

Step 3

Filter the list by performing the following steps:

Select an attribute, such as Username .

Select a modifier,  such as begins with .

Enter your search term.

Select Find .

### Add or Remove User From Device Pool

To add a user to or remove a user from a device pool:

Step 1

Select User
                                                   				  Management > User .

The Find, Add, Delete, Edit Users window opens.

Step 2

Perform one of the following steps:

- Select a user by clicking on the name in the Username list.

- Select the radio button preceding the name.

Step 3

Select Edit

The Edit User window opens to the General tab.

Step 4

Select  the Device Pools tab.

Step 5

Select the device pool from the Available pane, and then click the right arrow
                                             			 to move the pool to the Selected pane.

Step 6

To remove a user from a device pool, perform the following steps:

Select the device pool from
                                                   			 the Selected pane.

Select the left arrow
                                                   			 to move the device pool to the Available pane.

Step 7

Select Save .

### Assign User to User Group

- Super User - a role with superuser privileges that allow any operation in the
                                    Operations Console.

- Administrator - can perform any operation in the Operations Console except
                                    deleting user accounts.

- Serviceability Administration - Allows Web Services authentication through the
                                    "Unified System CLI" tool and does not allow any privileges for the Operations
                                    Console.

- Read Only - Has Read-only access to the Operations console.

- Add User Account

- Edit User Account

To add/remove a user to/from a user group:

Step 1

To add a user to a group, select the user group from the Available pane, and then click the right arrow
                                             to move the user group to the Selected pane.

Step 2

To remove a user from a group, select the user from the Selected pane, and then click the left arrow to
                                             move the user group to the Available pane.

Step 3

Click Save .

| Note | Serviceability users such as wsmadmin (CLI/some REST APIs) and Readonly users (OAMP/NOAMP) cannot access their respective
                                          services after installing or upgrading to CVP 12.6, until an Administrator user resets their password through the Operations
                                          Console (OAMP). |
|---|---|

| Step 1 | Select User Management > User
                                                   				  Roles from the Main menu. The Find, Add, Delete, Edit window opens. |
|---|---|
| Step 2 | Select Add New . |
| Step 3 | On the General tab, fill in the name of the role in the Role Name
                                             			 field. |
| Step 4 | Fill in descriptive text in the Description field, if desired. |
| Step 5 | Select the Access Criteria tab and assign 
                                             			 access criteria to
                                             			 the user role. 
                                             		  See Assign User Role Access Criteria . A default Access Criteria of Administrator is applied to every new
                                                				user role you create. |
| Step 6 | When you finish configuring the user role, click Save to save the configuration. |

| Step 1 | Select User Management > User
                                                   				  Roles from the Main menu. The Find, Add, Delete, Edit Application User Roles window opens. |
|---|---|
| Step 2 | Select the desired Role Name link or select the user role from the
                                             			 list and click Edit . If you have a long list of user roles,
                                             			 see Find User Role . The Edit Application User Role window opens to the General tab. |
| Step 3 | Change the description for the user role, if desired. |
| Step 4 | Select the Access Criteria tab and change the 
                                             			 access criteria assigned to the user role. 
                                             		  See Assign User Role Access Criteria . |
| Step 5 | When you finish configuring the user role, select Save . |

| Step 1 | Select Access Criteria tab. |
|---|---|
| Step 2 | Select the desired access criteria. |
| Step 3 | Click Save to save the user role with assigned
                                             access criteria to the Operations Console database. |

| Step 1 | Select User Management > User
                                                   				  Roles . The Find, Add, Delete, Edit window opens. |
|---|---|
| Step 2 | If the list is long, you can click the first page, previous page,
                                             			 next page, and last page icons on the bottom right of the window to page
                                             			 through the list. Or, you can enter a page number in the Page field and press 
                                             			 Enter to go to the numbered page. |
| Step 3 | Filter the list by selecting an attribute such as Role Name . Select a modifier, such as begins with . Enter your search term and click Find . Note The filter is not case-sensitive, and wildcard characters are not allowed. | Note | The filter is not case-sensitive, and wildcard characters are not allowed. |
| Note | The filter is not case-sensitive, and wildcard characters are not allowed. |

| Note | The filter is not case-sensitive, and wildcard characters are not allowed. |
|---|---|

| Step 1 | Select User Management > User
                                                   				  Roles . The Find, Add, Delete, Edit Application User Roles window opens. |
|---|---|
| Step 2 | Find the user roles using the procedure shown in Find User Role . |
| Step 3 | From the list of matching records, select the user roles that you
                                             			 want to delete. |
| Step 4 | Select Delete . |
| Step 5 | When prompted to confirm the delete operation, perform one of the following steps:. Select OK to delete the operation. Select Cancel to cancel the operation. |

| Step 1 | Select User Management > User
                                                   				  Groups . The Find, Add, Delete, Edit Application User Groups window opens. |
|---|---|
| Step 2 | Select Add New . |
| Step 3 | Fill in the name of the group in the Group Name field. |
| Step 4 | Fill in descriptive text in the Description field, if desired. |
| Step 5 | Select the User Roles tab and assign a user role to the
                                             			 user group. See Assign Role to User Group for details. You must assign at least one user role to each user group you
                                                				create. Note You cannot add a Web Service Role and an Operations Console
                                                         				user role to the same user group. Note Users assigned a Web Service Role cannot log in to the
                                                         				Operations Console. | Note | You cannot add a Web Service Role and an Operations Console
                                                         				user role to the same user group. | Note | Users assigned a Web Service Role cannot log in to the
                                                         				Operations Console. |
| Note | You cannot add a Web Service Role and an Operations Console
                                                         				user role to the same user group. |
| Note | Users assigned a Web Service Role cannot log in to the
                                                         				Operations Console. |
| Step 6 | When you finish configuring the user group, select Save . |

| Note | You cannot add a Web Service Role and an Operations Console
                                                         				user role to the same user group. |
|---|---|

| Note | Users assigned a Web Service Role cannot log in to the
                                                         				Operations Console. |
|---|---|

| Step 1 | Select User Management > User
                                                   				  Groups . The Find, Add, Delete, Edit User Groups window opens. |
|---|---|
| Step 2 | If you have a long list of user groups, see Find User Group to narrow the list of choices. |
| Step 3 | Select the radio button next to the User Group name and click Edit or click the Group Name. See Assign Role to User Group for details. The User Group Configuration window opens to the General tab. |
| Step 4 | You can change the description for the group by editing the
                                             			 Description field. |
| Step 5 | Select the User Roles tab and edit the assigned roles for
                                             			 this user group. |
| Step 6 | When you finish configuring the user group, click Save . |

| Step 1 | If you want to add a user role to a user group, select the user
                                             role from the Available pane, and then click the
                                             right arrow to move the user role to the Selected pane. |
|---|---|
| Step 2 | To remove a user role from a user group, select the user role
                                             from the Selected pane, and then click the left
                                             arrow to move the user role to the Available pane. |
| Step 3 | Click Save . |

| Step 1 | Select User Management > User Groups . The Find, Add,
                                                				Delete, Edit Application User Groups window opens. |
|---|---|
| Step 2 | Find the groups
                                             			 by using the procedure in Find User Group . |
| Step 3 | From the list of
                                             			 matching records, select the user groups that you want to delete. |
| Step 4 | Select Delete . |
| Step 5 | When prompted to
                                             			 confirm the delete operation, perform one of the following steps: Select OK to delete the operation Select Cancel to cancel the delete operation |

| Step 1 | Select User Management > User Groups User Management . The Find, Add, Delete, Edit Application User Groups Window lists
                                                				the available user groups. |
|---|---|
| Step 2 | If the list is long, you can perform one of the following steps: Select the first page, previous page,
                                                			 next page, and last page icons on the bottom right of the window to page
                                                			 through the list, or Enter a page number in the Page field and press Enter to go to the numbered page. |
| Step 3 | To filter the list, perform the following steps: Select an attribute,  such as Group Name Select a modified, such as begins with Enter your search term Select Find Note The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. | Note | The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. |
| Note | The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. |

| Note | The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. |
|---|---|

| Field | Description | Default | Range | Restart Required |
|---|---|---|---|---|
| User Information |  |
| Username | Name of the user account. The user logs in to the
                                             Operations Console using this name. After logging in,
                                             the username is displayed in the upper right portion of
                                             the screen. You cannot change the username when editing
                                             a user account. | None | Valid names include uppercase and lowercase letters in
                                             the alphabet, the numbers 0 through 9, a dash, and an
                                             underscore. | No |
| Password | New password for the user account. User must type this password to log into the Operations Console. | None | Any text that follows the guidelines for choosing secure passwords | No |
| Reconfirm Password | Retype the password for this user account to verify
                                             that you typed the password correctly. | None | Text must match the text entered in the Password
                                             field. | No |
| Firstname | (Optional) First name of the user. | None | Valid names include uppercase and lowercase letters in
                                             the alphabet, the numbers 0 through 9, a dash, and an
                                             underscore. | No |
| Lastname | (Optional) Last name of the user. | None | Valid names include uppercase and lowercase letters in
                                             the alphabet, the numbers 0 through 9, a dash, and an
                                             underscore. | No |
| E-mail | (Optional) e-mail address of the user. | None | Valid e-mail address | No |
| Signed in User Password | The password used to log into the user account. | None | Valid e-mail address | No |

| Note | Passwords must meet all the following criteria. |
|---|---|

| Note | You must create Device Pools to further limit access to devices.
                                                			 See Add Device Pool to Operations Console . |
|---|---|

| Step 1 | Select User
                                                   				  Management > Users . The Find, Add,
                                                				Delete, Edit Application Users window opens. |
|---|---|
| Step 2 | Select Add
                                                				New . |
| Step 3 | Fill in the
                                             			 appropriate configuration settings on the General tab. |
| Step 4 | Select the Device
                                                				Pools tab and assign a Device Pool to the user. Each user must be
                                             			 assigned to at least one device pool. See Add or Remove User From Device Pool . |
| Step 5 | Select the User
                                                				Group tab and add the user to one or more user groups. See Add User Group . |
| Step 6 | When you finish
                                             			 configuring the user, click Save . |

| Step 1 | Select User Management > Users . The Find, Add, Delete, Edit Users window opens. |
|---|---|
| Step 2 | Select the desired Username link or select radio button next to the
                                             			 username from and select Edit . You can reduce the list of users
                                             			 displayed. See Find User Account . The Edit User page opens to the General tab. |
| Step 3 | Fill in the appropriate configuration settings on the General tab
                                             			 as described in General User Information Settings . |
| Step 4 | Select the Device Pools tab and assign a device pool to the user.
                                             			 See Add or Remove User From Device Pool . |
| Step 5 | Select the User Groups tab and add/remove the user to/from one or
                                             			 more user groups. See Add User Group . |
| Step 6 | When you finish configuring the user, select Save . |

| Step 1 | Select User
                                                   				  Management > User . The Find, Add, Delete, Edit Application Users window opens. |
|---|---|
| Step 2 | From the list of users, select the user that you want to delete.
                                             			 You can reduce the list of users displayed. See Find User Account |
| Step 3 | Select Delete . |
| Step 4 | When prompted to confirm the delete operation, perform one of the following steps: Select OK to delete. Select Cancel to cancel the delete operation. |

| Step 1 | Select User
                                                   				  Management > User . The Find, Add, Delete, Edit Application Users window opens. |
|---|---|
| Step 2 | Perform one of the following steps: If the list is long, select the first page, previous page,
                                                			 next page, and last page icons on the bottom right of the window to page
                                                			 through the list. Enter a page number in the Page field and press 
                                                			 Enter to go directly to the numbered page. |
| Step 3 | Filter the list by performing the following steps: Select an attribute, such as Username . Select a modifier,  such as begins with . Enter your search term. Select Find . Note The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. | Note | The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. |
| Note | The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. |

| Note | The filter is not case-sensitive, and wildcard characters are
                                                         				not allowed. |
|---|---|

| Step 1 | Select User
                                                   				  Management > User . The Find, Add, Delete, Edit Users window opens. |
|---|---|
| Step 2 | Perform one of the following steps: Select a user by clicking on the name in the Username list. Select the radio button preceding the name. |
| Step 3 | Select Edit The Edit User window opens to the General tab. |
| Step 4 | Select  the Device Pools tab. |
| Step 5 | Select the device pool from the Available pane, and then click the right arrow
                                             			 to move the pool to the Selected pane. |
| Step 6 | To remove a user from a device pool, perform the following steps: Select the device pool from
                                                   			 the Selected pane. Select the left arrow
                                                   			 to move the device pool to the Available pane. Note A user must always be associated with at least one device pool. | Note | A user must always be associated with at least one device pool. |
| Note | A user must always be associated with at least one device pool. |
| Step 7 | Select Save . |

| Note | A user must always be associated with at least one device pool. |
|---|---|

| Step 1 | To add a user to a group, select the user group from the Available pane, and then click the right arrow
                                             to move the user group to the Selected pane. |
|---|---|
| Step 2 | To remove a user from a group, select the user from the Selected pane, and then click the left arrow to
                                             move the user group to the Available pane. |
| Step 3 | Click Save . |