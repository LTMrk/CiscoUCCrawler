---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b05role-html-d7e6f8c051
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b05role.html
retrieved_at: 2026-08-21T16:13:13.404975+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Role Configuration

## Chapter: Role Configuration

## Role Configuration

Roles allow Cisco Unified Presence Server administrators who have full administration privilege (access) to configure end users and application users with different levels of privilege. Administrators with full administration privilege configure roles and user groups. In general, full-access administration users configure the privilege of other administration users and end users to Cisco Unified Presence Server Administration and to other applications.

Different levels of privilege exist for each application. For the Cisco Unified CallManager Administration application, two levels of privilege exist: read privilege and update privilege. These privilege levels differ as follows:

• Users with update privilege can view and modify the Cisco Unified CallManager Administration windows to which the user's user group has update privilege.

• A user with read privilege can view the Cisco Unified CallManager Administration windows that belong to the roles to which the user's user group has read privilege. A user with read privilege for a window cannot, however, make any changes on those administration windows to which the user has only read privilege. For a user with read privilege, the Cisco Unified CallManager Administration application does not display any update buttons nor icons.

Roles comprise groups of resources for an application. At installation, default standard roles get created for various administrative functions. You may, however, create custom roles that comprise custom groupings of resources for an application.

Note Certain standard roles have no associated application nor resource. These roles provide login authentication for various applications.

Use the following topics to configure roles:

• Finding a Role

• Configuring a Role

• Deleting a Role

• Role Configuration Settings

Additional Information

See the "Related Topics" section .

## Finding a Role

Because you might have several roles in your network, Cisco Unified Presence Server lets you locate specific roles on the basis of specific criteria. Use the following procedure to locate roles.

Note During your work in a browser session, Cisco Unified Presence Server Administration retains your role search preferences. If you navigate to other menu items and return to this menu item, Cisco Unified Presence Server Administration retains your role search preferences until you modify your search or close the browser.

Step 1 Choose User Management > Role .

The Find and List Roles window displays. Use the two drop-down list boxes to search for a role.

Step 2 From the first Find Role where drop-down list box, choose one of the following criteria:

• Name

• Application

From the second Find Role where drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find . You can also specify how many items per page to display.

Tip To find all roles that are registered in the database, click Find without entering any search text.

A list of discovered roles displays by

• Name

• Application

• Description

Tip To search for roles within the search results, click the Search Within Results check box and enter your search criteria as described in this step.

Note You can delete multiple roles from the Find and List Roles window by checking the check boxes next to the appropriate roles and clicking Delete Selected . You can delete all roles in the window by clicking Select All and then clicking Delete Selected .

Note You cannot delete standard roles.

Step 4 From the list of records, click the role name that matches your search criteria.

The window displays the role that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Role

This section describes how to add a role to Cisco Unified Presence Server Administration.

Step 1 Choose User Management > Role .

The Find and List Roles window displays.

Step 2 Perform one of the following tasks:

• To copy an existing role, locate the appropriate role as described in the "Finding a Role" section and click the Copy button next to the role that you want to copy. In the popup window that displays, enter a name for the new role and click OK . Continue with Step 4 .

Note Copying a role also copies the privileges that are associated with that role.

• To add a new role, click the Add New button, and continue with Step 3 .

• To update an existing role, locate the appropriate role as described in the "Finding a Role" section and continue with Step 4 .

Step 3 If you are adding a new role, choose an application from the Application drop-down list box and click Next .

Step 4 In the Role Configuration window that displays, enter the appropriate settings as described in Table 37-1 .

Step 5 To add the role, click Save .

The new role gets added to the Cisco Unified Presence Server database.

Additional Information

See the "Related Topics" section .

## Deleting a Role

This section describes how to delete a role in Cisco Unified Presence Server Administration.

Step 1 Choose User Management > Role .

The Role Configuration window displays.

Step 2 In the list of Roles at left, click the name of the role that you want to delete.

Note You cannot delete a standard role.

The role that you chose displays.

Step 3 Click Delete .

You receive a message that asks you to confirm the deletion.

Step 4 Click OK .

The window refreshes, and the role gets deleted from the database.

Additional Information

See the "Related Topics" section .

## Role Configuration Settings

Table 37-1 describes the role configuration settings. For related procedures, see the "Related Topics" section .

Table 37-1 Role Configuration Settings

Application

From the drop-down list box, choose the application with which this role associates.

Name

Enter a name for the role. Names can have up to 50 characters.

Description

Enter a description for the role. Descriptions can have up to 50 characters.

(list of resource names for the chosen application)

In the Resource Access Information pane, click the check box(es) next to the resource(s) that you want this role to include.

Note In some applications, only one check box applies for each resource. In the Cisco Unified Presence Server Administration application, a read check box and an update check box apply to each resource.

Grant access to all

Click this button to grant privileges for all resources that display on this page for this role.

Note If the list of resources displays on more than one page, this button applies only to the resources that display on the current page. You must display other pages and use the button on those pages to change the access of the resources that are listed on those pages.

Deny access to all

Click this button to remove privileges for all resources that display on this page for this role.

Note If the list of resources displays on more than one page, this button applies only to the resources that display on the current page. You must display other pages and use the button on those pages to change the access of the resources that are listed on those pages.

## Related Topics

• Finding a Role

• Configuring a Role

• Deleting a Role

• Role Configuration Settings

• Roles and User Groups, Cisco Unified CallManager System Guide

| Field | Description |
|---|---|
| Role Information |
| Application | From the drop-down list box, choose the application with which this role associates. |
| Name | Enter a name for the role. Names can have up to 50 characters. |
| Description | Enter a description for the role. Descriptions can have up to 50 characters. |
| Resource Access Information |
| (list of resource names for the chosen application) | In the Resource Access Information pane, click the check box(es) next to the resource(s) that you want this role to include. Note In some applications, only one check box applies for each resource. In the Cisco Unified Presence Server Administration application, a read check box and an update check box apply to each resource. |
| Grant access to all | Click this button to grant privileges for all resources that display on this page for this role. Note If the list of resources displays on more than one page, this button applies only to the resources that display on the current page. You must display other pages and use the button on those pages to change the access of the resources that are listed on those pages. |
| Deny access to all | Click this button to remove privileges for all resources that display on this page for this role. Note If the list of resources displays on more than one page, this button applies only to the resources that display on the current page. You must display other pages and use the button on those pages to change the access of the resources that are listed on those pages. |