---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b05usgrp-html-87a4506814
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b05usgrp.html
retrieved_at: 2026-08-21T16:13:17.569537+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: User Group Configuration

## Chapter: User Group Configuration

## User Group Configuration

The role and user group menu options in the Cisco Unified Presence Server Administration User Management menu allow users with full access to configure different levels of window access for Cisco Unified Presence Server administrators. Users with full access configure roles, user groups, and access privileges for roles. In general, full-access users configure the access of other users to Cisco Unified Presence Server Administration.

User groups comprise lists of application users and end users. A user may belong to multiple user groups. After you add a user group, you then add users to a user group. Afterward, you may proceed to assign roles to a user group. If a user belongs to multiple user groups, the MLA permission enterprise parameter determines the effective privilege of the user.

Use the following topics to configure user groups, assign users to user groups, and view a user's roles, user groups, and permissions:

• Finding a User Group

• Configuring a User Group

• Deleting a User Group

• Adding Users to a User Group

• Deleting Users from a User Group

• Assigning Roles to a User Group

• Viewing a User's Roles, User Groups, and Permissions

## Finding a User Group

Because you might have several user groups in your network, Cisco Unified Presence Server lets you locate specific user groups on the basis of specific criteria. Use the following procedure to locate user groups.

Note During your work in a browser session, Cisco Unified Presence Server Administration retains your user group search preferences. If you navigate to other menu items and return to this menu item, Cisco Unified Presence Server Administration retains your user group search preferences until you modify your search or close the browser.

Step 1 Choose User Management > User Group .

The Find and List User Groups window displays. Use the two drop-down list boxes to search for a user group.

Step 2 From the first Find User Group where drop-down list box, choose the following criterion:

• Name

From the second Find User Group where drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find . You can also specify how many items per page to display.

Tip To find all user groups that are registered in the database, click Find without entering any search text.

A list of discovered user groups displays by

• Name

• Roles (icon)

Tip To search for user groups within the search results, click the Search Within Results check box and enter your search criteria as described in this step.

Note You can delete multiple user groups from the Find and List User Groups window by checking the check boxes next to the appropriate user groups and clicking Delete Selected . You can delete all user groups in the window by clicking Select All and then clicking Delete Selected .

Note You cannot delete the standard user groups.

Step 4 From the list of records, click the user group name that matches your search criteria.

The window displays the user group that you choose.

Additional Topics

See the "Related Topics" section .

## Configuring a User Group

This section describes how to add, copy and update a user group to and in the Cisco Unified Presence Server Administration.

Step 1 Choose User Management > User Group .

The Find and List User Groups window displays.

Step 2 Perform one of the followings tasks:

• To copy an existing user group, locate the appropriate user group as described in "Finding a User Group" section and click the Copy button next to the user group that you want to copy. In the popup window that displays, enter a name for the new user group and click OK . Continue with Step 3 .

• To add a new user group, click the Add New button. Enter a name for the new user group and click OK . Continue with Step 3 .

Note The user group name can contain up to 50 alphanumeric characters and can contain any combination of spaces, periods (.), hyphens (-), and underscore characters (_). Ensure that the user group name is unique.

• To update an existing user group, locate the appropriate user group as described in "Finding a User Group" section . Click the name of the user group that you want to update. The user group that you chose displays. Update the appropriate settings. Continue with Step 3 .

Note You cannot delete a standard user group, but you can update the user membership for a standard user group.

Step 3 Click Save .

Step 4 Proceed to add users to this user group. See Adding Users to a User Group .

Step 5 Proceed to assign roles to the user group. See Assigning Roles to a User Group .

Additional Topics

See the "Related Topics" section .

## Deleting a User Group

This section describes how to delete a user group from Cisco Unified Presence Server Administration. Use the following procedure to delete a user group entirely. If you want to delete only certain users from a user group, refer to the "Deleting Users from a User Group" section .

Before You Begin

When you delete a user group, Cisco Unified Presence Server removes all user group data from the database. To find out which roles are using the user group, in the User Group Configuration window, choose Dependency Records from the Related Links drop-down list box and click Go . If dependency records are not enabled for the system, the Dependency Records Summary window displays a message.

Step 1 Choose User Management > User Group .

The Find and List User Groups window displays.

Step 2 Find the user group that you want to delete by using the procedure in the "Finding a User Group" section .

Step 3 Click the name of the user group that you want to delete.

The user group that you chose displays. The list shows the users in this user group in alphabetical order.

Step 4 If you want to delete the group entirely, click Delete .

A dialog box displays to warn you that you cannot undo deletion of user groups.

Step 5 To delete the user group, click OK or to cancel the action, click Cance l. If you click OK , Cisco Unified Presence Server removes the user group from the database.

Additional Topics

See the "Related Topics" section .

## Adding Users to a User Group

This section describes how to add end users and application users to a user group in Cisco Unified Presence Server Administration.

Step 1 Choose User Management > User Group .

The Find and List User Groups window displays.

Step 2 Find the user group to which you want to add users. Use the procedure in the "Finding a User Group" section .

Step 3 Click the name of the user group that you want to update.

The user group that you chose displays. The Users in Group list shows the users that currently belong to the user group.

Step 4 To add end users, click Add Users to Group . To add application users, skip to Step 8 .

The Find and List Users window displays.

Step 5 Use the Find User drop-down list boxes to find the end users that you want to add and click Find .

Note You can perform the search for users in a variety of ways. You can enter the first name, middle name, last name, user ID, or department of a user. Alternatively, you can leave the field blank, which results in display of all users.

A list of end users that matches your search criteria displays.

Note The list of search results does not display end users that already belong to the user group.

Step 6 In the list of search results, click the check box next to the users that you want to add to this user group. If the list comprises multiple pages, use the links at the bottom to see more results.

Step 7 Click Add Selected .

The User Group Configuration window redisplays with the users that you added listed in the Users in Group pane.

Note After you add a user, you can view the user's roles by clicking the i icon in the Permission column for that user.

Step 8 To add application users, click Add Application Users to Group .

The Find and List Application Users window displays.

Step 9 Use the Find Application User drop-down list boxes to find the application users that you want to add and click Find .

Note You can perform the search for application users by searching for user ID. Alternatively, you can leave the field blank, which results in display of all application users.

A list of application users that matches your search criteria displays.

Step 10 In the list of search results, click the check box next to the application users that you want to add to this user group. If the list comprises multiple pages, use the links at the bottom to see more results.

Note The list of search results does not display application users that already belong to the user group.

Step 11 Click Add Selected .

The User Group Configuration window redisplays with the application users that you added listed in the Users in Group pane.

Note After you add an application user, you can view the user's roles by clicking the i icon in the Permission column for that user.

Step 12 To save your changes to this user group, click Save .

Additional Topics

See the "Related Topics" section .

## Deleting Users from a User Group

This section describes how to delete users from a user group in Cisco Unified Presence Server Administration.

Step 1 Choose User Management > User Group .

The Find and List User Groups window displays.

Step 2 Find the user group from which you want to delete users. Use the procedure in the "Finding a User Group" section .

Step 3 Click the name of the user group that you want to update.

The user group that you chose displays. The Users in Group list shows the users that currently belong to the user group.

Step 4 Click the check boxes next to the names of the users that you want to delete from this user group.

Step 5 Click Delete Selected .

A confirmation message asks you to confirm the deletion.

Step 6 To delete the selected user group members, click OK or click Cancel to exit this window.

The User Group redisplays with the deleted users removed from the Users in Group pane.

Additional Topics

See the "Related Topics" section .

## Assigning Roles to a User Group

Users with full access can assign roles to user groups. A user group that has assigned roles has access to the resources that the role comprises.

This section describes assigning roles to a user group in Cisco Unified Presence Server Administration.

Note When an administrator assigns roles to a user group, the administrator should assign the Standard CCM Admin Users role to the user group. This role enables the users to log into Cisco Unified Presence Server Administration.

Step 1 Choose User Management > User Group .

The Find and List User Groups windows displays.

Step 2 Find the user group to which you want to assign roles. Use the procedure in the "Finding a User Group" section .

Step 3 Click the name of the user group for which you want to assign roles.

The user group that you chose displays. The Users in Group list shows the users that currently belong to the user group.

Step 4 From the Related Links drop-down list box, choose Assign Role to User Group and click Go .

The User Group Configuration window changes to display the Role Assignment pane. For the user group that you chose, the list of assigned roles displays. Choose one of the following options:

• To assign roles to the user group, go to Step 5 .

• To delete roles from the user group, go to Step 9 .

Step 5 To assign additional roles to the user group, click Assign Role to Group .

The Find and List Roles popup window displays.

Step 6 If necessary, use the Find Role search criteria to narrow the list of roles.

Step 7 Choose the roles to assign to this user group by clicking the check boxes next to the role names. To close the Find and List Roles popup window without assigning roles to this user group, click Close .

Step 8 Click Add Selected .

The Find and List Roles popup window closes. The chosen roles get added to the Role Assignment pane for this user group. If you do not want to delete any assigned roles for this user group, skip to Step 10 .

Step 9 To delete an assigned role from the user group, select a role in the Role Assignment pane and click Delete Role Assignment . Repeat this step for each role that you want to delete from this user group.

Step 10 Click Save .

The system makes the added and deleted role assignments to the user group in the database.

Additional Topics

See the "Related Topics" section .

## Viewing a User's Roles, User Groups, and Permissions

This section describes how to view the roles, user groups, and permissions that are assigned to a user that belongs to a specified user group. Use the following procedure to view the roles, user groups, and permissions that are assigned to a user in a user group.

Note You can also view user roles by using User Management > Application User (for application users) or User Management > End User (for end users) to view a particular user and then display the user roles.

Step 1 Choose User Management > User Group .

The Find and List User Groups window displays.

Step 2 Find the user group that has the users for which you want to display assigned roles. Use the procedure in the "Finding a User Group" section .

Step 3 Click the name of the user group for which you want to view the roles that are assigned to the users.

The User Group Configuration window displays for the user group that you chose. The Users in Group pane shows the users that belong to the user group.

Step 4 For a particular user, click the i icon in the Permission column for the user.

The User Privilege window displays. For the user that you chose, the following information displays:

• User groups to which the user belongs

• Roles that are assigned to the user

• Resources to which the user has access. For each resource, the following information displays:

– Application

– Resource

– Permission ( read and/or update )

Step 5 To return to the user, choose Back to User in the Related Links drop-down list box and click Go .

Additional Topics

See the "Related Topics" section .

## Related Topics

• Finding a User Group

• Configuring a User Group

• Deleting a User Group

• Adding Users to a User Group

• Deleting Users from a User Group

• Assigning Roles to a User Group

• Viewing a User's Roles, User Groups, and Permissions

• Roles and User Groups, Cisco Unified CallManager System Guide

• End User Configuration, Cisco Unified CallManager System Guide

• Application User Configuration, Cisco Unified CallManager System Guide