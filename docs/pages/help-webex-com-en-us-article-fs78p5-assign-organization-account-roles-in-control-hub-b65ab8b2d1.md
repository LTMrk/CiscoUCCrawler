---
doc_id: help-webex-com-en-us-article-fs78p5-assign-organization-account-roles-in-control-hub-b65ab8b2d1
source_url: https://help.webex.com/en-us/article/fs78p5/Assign-organization-account-roles-in-Control-Hub
retrieved_at: 2026-11-02T13:02:07.477775+00:00
---

## Managing roles in Control Hub

We recommend that you share administrative responsibilities within your organization. Even in
      small organizations, we recommend having more than one person holding a full administrator
      role to ensure availability.

As a full administrator, you can assign various administrative roles to people in your organization, to streamline responsibilities and share accountability for managing the organization.

For example, a compliance officer can access user-generated content as necessary for legal/compliance purposes. This is likely to be a different person than a support administrator, who can access analytics and troubleshooting information.

This article describes how to manage administrative roles and lists the privileges associated
      with each role. Carefully plan out which roles your organization needs and how you want to
      divide responsibilities.

For other articles about administrative roles:

If you want to create a customized administrator role, see Custom roles in
            Control Hub .

If you're managing multiple Webex organizations for your customers, see administrator
            roles in Partner Hub .

If your organization is managed by a partner, you may also see delegated partner
          administrator access. To review or change partner access, see Assign external
            administrator roles in Control Hub .

### Assign roles to users

Assign roles to users to share administrative responsibilities and give each administrator the access they need in Control Hub. Review the role details before assigning roles so access matches each user's responsibilities.

Before you begin

Review the user's services roles before you change their organizational role. If you change the organizational role of a user who has an existing services role, you could affect their existing services roles.

The location administrator role is exclusive from other types of administrator roles. You can't assign a location administrator role to a user who is already assigned other administrator roles.

To assign locations to the user, check Location admin and add the
              locations .

If a user is assigned as user and device administrator or device administrator, they can't administer Webex Calling.

Sign in to Control Hub , go to Management > Users , and choose a user.

If you're a partner, open the customer organization where you want to assign roles, then access that organization's Users page.

In the Summary tab, go to Administrator roles .

If the user has roles assigned to them, they're listed here.

Click > , then select roles to assign to the user.

For meetings site administrator roles, click Edit next to Webex Site administrator roles . Select roles for each Webex site that you want the user to manage.

Click Save .

It may take up to 10 minutes for users to gain access to their new roles.

Want to see how it's done? Watch this video demonstration on how to assign organization account roles in Control Hub.

### Assign roles to a group

You can assign specific administrator roles to groups in your organization. This makes
        managing permissions more efficient and ensures consistent access control. Members assigned
        to a group all receive the same administrator permissions. When you remove a user from that
        group, they also lose the administrator permissions granted by the group. You can easily
        update administrator privileges simply by modifying group memberships.

Keep the following limitations in mind when assigning roles to a group:

Organizations can have up to 100 groups with assigned administrator roles.

You can assign up to 20 different roles to a single group.

A user may have incompatible roles from direct assignment and group membership. For
          example, a user with a directly assigned Read-only administrator or Location administrator
          role won't inherit an incompatible role from a group. To apply the group-assigned role,
          remove the incompatible role directly assigned to the user. Then, remove the user from the
          group and add them to the group again. Click here for more information on limitations between
          roles.

Sign in to Control Hub .

Go to Groups > Webex groups .

Select the group you want to assign roles to.

Click Assignments > Assign roles .

Select the roles you want to assign to your group.

Click Save .

### Find specific administrators

Sort and filter the list of users in your organization to see who is assigned to specific
        roles.

Sign in to Control
            Hub .

Go to Management > Users .

Click Filter and select the check box next to the roles you want to
          find.

### Export the administrator list as a CSV file

You can export a full or filtered list of administrators in your organization as a CSV
        file. The following table shows you the data that the CSV file exports.

You can't manage administrator roles through the CSV file.

Column name

Description

First / Last name

The names (First<space>Last) of the exported administrators.

User ID/Email

The unique IDs (email addresses) of the exported users.

Admin Role

Comma-separated lists of administrative roles held by the exported users.

Sign in to Control Hub , go to Management > Users .

Click Filter and select the check box next to the roles you want to
          find.

Click at the top right to export the list.

If you're exporting a filtered list, wait until the CSV file downloads before you
              change the filter. Otherwise, you get the updated filtered list in the current CSV
              file download.

## Role details

Each role determines the privilege level you have in Control Hub. If you have full administrator privileges, you can assign one or more roles to any user in your organization.

When you set up your account for the first time, the administrator from the partner
      organization becomes the full administrator for your organization, and can set up additional
      administrators.

Users that you add to your organization have no administrative privileges at first. Here's a
      list of the prebuilt roles in Control Hub and why you might want to assign them to a user:

Full administrator —Full administrators have access to every aspect
          of how an organization is run. They can add and remove users, distribute Webex licenses,
          create and modify company policy templates, and change organization settings.

Full administrators can’t simultenously hold the role of a location administrator .

Read-only administrator —Read-only administrators can view and
          monitor all areas of Control Hub, but don't have permission to make any organizational
          changes.

Read-only administrators can’t also be assigned a custom or location administrator
            role. If an administrator needs view-only access with specific additional permissions, create a
              custom role that includes the required access.

Support administrator —Support administrators are intended to
          provide logistical support to full administrators. They only have access to organization
          analytics and reports, in addition to troubleshooting tools. They may also view
          organization support cases.

User and device administrator —User and device administrators have
          access to the essential day-to-day workings of an organization. They can add and manage
          users, set up and manage devices, and assign the location administrator role to users. They can't
          assign other administrator roles.

Device administrator —Device administrators focus solely on device
          management. This includes registering or
            deregistering new devices and phone numbers , generating activation
            codes , and managing workspaces .

Compliance officer —Compliance officers moderate and oversee
          user-generated content. They can access the Events API and eDiscovery reports to see user-generated content in Webex App. They can also override the default content retention policy to support legal
          cases.

Security activity administrator —Security activity administrators
          assist full administrators in monitoring changes to organization settings and troubleshooting
          Calling and meeting logs.

Advanced troubleshooting access —The advanced troubleshooting
          access role allows full administrators, read-only administrators, and support
          administrators to access the Live Meeting page in the Troubleshooting tab. Full administrators with this permission can
          also join in-progress meetings to provide troubleshooting assistance.

### Organization roles

The following table displays a list of pre-built roles and what kind of Control Hub access
        each comes with.

Access

Full admin

Read-only admin

Support admin

User and device admin

Device admin

Compliance officers

Security activity admin

Advanced troubleshooting access

Add/Delete users and assign licenses

✔

Read-only

✔

Assign roles to users

✔

Read-only

Device management

✔

Read-only

✔

Company policy and templates

✔

Read-only

Analytics and reports

✔

Read-only

✔

Troubleshooting

✔

Read-only

✔

✔

Organization-based licenses

✔

Read-only

Group-based licenses

✔

Add or remove users from groups

✔

✔

Individual licenses

✔

✔

Organization settings

✔

Read-only

App integrations

✔

Read-only

Vidcast

✔

Read-only

Webex site management

✔

Read-only

Admin actions audit log

✔

✔

Access to user-generated content

✔

Legal hold

✔

Access to join in-progress meetings

✔

Access to live meetings

✔

Product email notifications

View organization support cases

✔

✔

✔

✔

✔

✔

This table only lists organization-wide administrative roles. For more information on
          service-specific administrator roles, such as Webex site administrator and Webex Contact
          Center administrator, you can read about them in the following sections.

Add/Delete users and assign licenses —The user can add and
              delete users , manage user status , and manage
              licenses for users.

Assign roles to users —The user can assign administrative roles to users .

Device management —The user can register or deregister
              new devices and phone numbers , generate activation
              codes , and manage workspaces .

Company policy and templates —The user can manage the Webex
              app content retention policy and configure security settings such as blocking
              file uploads and blocking external
              communications .

Analytics and reports —The user can access the Analytics tab
            to view Webex services usage data.

Troubleshooting —The user can only access the Troubleshooting tab to view recent Webex meetings details.

Organization-based licenses —The user can set up
            organization-based automatic license assignments .

Group-based license assignments —The user can set up automatic licensing for groups .

Add or remove users from groups —The user can create and manage
              groups of users.

Individual licenses —The user can view and
              manage individual license assignments.

Organization settings —The user can access and modify
            organization settings.

App integrations —The user can view and
              access Webex app integrations.

Vidcast —The user has access to Vidcast
              settings , templates, and recordings.

Webex site management —The user can add, modify, and
              delete Webex sites if the partner enabled Webex site management
              for customers .

Admin actions audit log —The user can view and export
              administrator activity logs .

Access to user-generated content —The user can access the Events
              API and eDiscovery reports to see user-generated content in Webex App.

Legal hold —The user can override Webex App's content retention policy to support legal
              cases .

Access to join in-progress meetings —The user can access
              in-progress meetings to troubleshoot issues.

Access to live meetings —The user can view and access live meetings in Control
            Hub.

View organization support cases —The user can access the Cisco
              Support Case Manager to see the status of the organization's support cases.

### Advanced Troubleshooting Access Role

This role allows full administrators, read-only administrators, and support administrators to access the Live Meeting page in the Troubleshooting tab, and lets full administrators join meetings that are in progress with just the click of a button. If participants are having issues during meetings, administrators with this role can quickly find those meetings to join and help sort out the issues.

For more information about the Live Meeting page and the Admin Join feature, see Advanced Diagnostics and Troubleshooting in Control Hub .

Full administrators can assign the Advanced Troubleshooting Access role to another full administrator, read-only administrator, or support administrator within their organization. Full administrators can’t assign the Advanced Troubleshooting Access role to themselves. Another full administrator must assign the role to them.

### Webex Site Administrator roles

You can only assign Webex site administrator roles to users in Control Hub-managed meeting sites. These roles can't be assigned in Control Hub to manage Site Administration-managed meeting sites.

Webex site administrators only have access to the users and settings for the Webex site that they're assigned to in Control Hub. You can assign a user as an administrator for more than one Webex site. Users that are assigned with the site administrator role must sign in to Control Hub once after being assigned the role before they can get admin access to the meeting sites.

Full administrators have Webex site administrator and Meeting content administrator privileges by default. These roles cannot be modified or revoked.

If your organization has a lot of Webex sites to manage, assign users as Webex site, Webex user, or Webex read-only administrators to define ownership and to split up administrative responsibilities for each Webex site.

Webex site administrators and Webex user administrators can only manage Webex Meetings-related settings for users in customer organizations to which they're assigned.

Webex site administrators don't use a Webex Meetings license for the Webex site that they're assigned to, but they won't have any host privileges. If you want a Webex site administrator to have hosting privileges, assign a host license to them.

#### Meeting Content Administrator role

If you want to allow Webex site administrators to also access, retrieve, and manage meeting artifacts, such as recordings and transcriptions, through APIs or a web interface, you can toggle a switch to assign them as a Meeting Content admin. This role allows you to assign users with granular access to specific Webex sites, instead of allowing them access to all sites.

To assign the Meeting Content admin role to a user:

- Sign in to Control Hub , then Management > Users and choose a user.

- In the user's Profile tab, find Administrator roles .

- In the Services section, click Edit next to Webex site administrator roles .

The user must be assigned one of the Webex site administrator roles for a site in order to have access to the Meeting Content admin role.

- Click Done .

- Click Save .

User Management

✔ (User Settings. Can't add or delete users to Control Hub org.)

✔ (User Settings. Can't add or delete users to Control Hub org.)

Read-only

✔ (User Settings. Can't add or delete users to Control Hub org.)

Analytics and Reports

Read-only

Read-only

Read-only

Read-only

Licenses*

✔

✔

Read-only

✔

Assign Roles*

✔

Read-only

Read-only

✔

Site Configuration*

✔

Read-only

Read-only

✔

Can download recordings and transcripts using https://developer.webex.com/meeting/docs/meetings .

* For their assigned Webex sites only.

### Webex Contact Center Administrator Role

Webex Contact Center provides a dedicated Contact Center Service Administrator role that allows users to administer and manage the contact center service and licenses. This role can be assigned to external administrators, and users within the customer organization. For more information about Contact Center administrator roles, see this article .

The following table describes the contact center-specific privileges of all Control Hub administrator roles:

Customer Organization

External Organization

Partner Organization

Any Other Organization

Full Administrator

Can administer all features of contact center.

Can perform all user management activities for contact center such as:

Add or remove users in the customer organization.

Assign, edit, or remove contact center licenses from users.

Add or revoke the Contact Center Service Administrator role from external administrators.

Can perform all administrative activities similar to full administrators from a customer organization, with the following exception:

The administrator cannot add or revoke the Contact Center Service Administrator role from other external administrators.

Contact Center Service Administrator

NA

Can perform all administrative activities similar to full administrators from a customer organization, with the following exception:

The administrator cannot add or revoke the Contact Center Service Administrator role from other external administrators.

Provisioning Administrator

NA

Can perform all contact center administrative activities that a partner full administrator can perform.

Cannot perform any user management activities, and can only view the list of other external administrators in the organization.

NA

Read-only Administrator

Cannot access the Webex Contact Center administrative interfaces (Control Hub and Management Portal).

Can access the Webex Contact Center administrative interfaces (Control Hub and Management Portal) in read-only mode only.

### Webex location administrator

You can distribute administration across the organization by delegating administration of certain services in locations . This enables you to efficiently handle location-level management without impacting the entire organization.

You can’t assign any other administrator role to a location administrator.

### Webex Calling Detailed Call History API access role

The earlier functional role named Webex Calling Detailed Call History API
            access is marked Obsolete in Control Hub. The role
          remains operational until December 31, 2026 .

Use the following Webex Calling Detailed Call History API access custom role for new assignments, and migrate users from the functional role before that
          date.

Full administrators can create a custom role to give users access to Webex Calling Detailed
        Call History CDR APIs, including the stream and feed APIs. See the Webex Calling Detailed Call History API documentation for details
        about the CDR APIs.

Once you've created the Webex Calling Detailed Call History API access custom role, you can assign the role to a user through the Users page.

For more details on consuming the CDR APIs using this custom role, you can watch this Vidcast .

Sign in to Control
            Hub .

Go to Users > Admin roles .

Select Create a custom role .

Enter a name and description for the custom role.

For example, use CDR API Access for the name, and describe which administrators should
            receive the permission.

In the permission list, go to Reporting > Webex Calling Detailed Call History API access .

Click the Add button next to Webex Calling Detailed
            Call History API access .

Select Save .

### Webex Events administrator

The Webex Events administrator role has access to Webex Events (formerly Socio) and can grant access to others.

When the user with this role signs in to Control Hub, they can:

- See the Services > Events page.

On that page, click the Launch Webex Events portal button to open Socio.

(Administrators who do not have this specific role see an inactive button)

## Known issues

The following is a list of known issues with assigning administrator roles in Control
        Hub.

Location administrator roles can't combine with other administrator roles, including
            custom roles.

Read-only administrator roles can't be combined with custom roles or Location
            administrator roles. If an administrator needs view-only access with specific additional
            permissions, create a custom role that includes the required access.

A user may have incompatible roles from direct assignment and group membership. To
            apply the group-assigned role, remove the incompatible role directly assigned to the
            user. Then, remove the user from the group and add them to the group again.

In some role-conflict scenarios, Inherited role badges from
            group assignments may not match the selected role check boxes on the user role details
            page.

| 1 | Sign in to Control Hub , go to Management > Users , and choose a user. If you're a partner, open the customer organization where you want to assign roles, then access that organization's Users page. |
|---|---|
| 2 | In the Summary tab, go to Administrator roles . If the user has roles assigned to them, they're listed here. |
| 3 | Click > , then select roles to assign to the user. For meetings site administrator roles, click Edit next to Webex Site administrator roles . Select roles for each Webex site that you want the user to manage. |
| 4 | Click Save . It may take up to 10 minutes for users to gain access to their new roles. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Groups > Webex groups . |
| 3 | Select the group you want to assign roles to. |
| 4 | Click Assignments > Assign roles . |
| 5 | Select the roles you want to assign to your group. |
| 6 | Click Save . |

| 1 | Sign in to Control
            Hub . |
|---|---|
| 2 | Go to Management > Users . |
| 3 | Click Filter and select the check box next to the roles you want to
          find. |

| Column name | Description |
|---|---|
| First / Last name | The names (First<space>Last) of the exported administrators. |
| User ID/Email | The unique IDs (email addresses) of the exported users. |
| Admin Role | Comma-separated lists of administrative roles held by the exported users. |
|  |

| 1 | Sign in to Control Hub , go to Management > Users . |
|---|---|
| 2 | Click Filter and select the check box next to the roles you want to
          find. |
| 3 | Click at the top right to export the list. The CSV file automatically downloads once it's ready. If you're exporting a filtered list, wait until the CSV file downloads before you
              change the filter. Otherwise, you get the updated filtered list in the current CSV
              file download. |

| Access | Full admin | Read-only admin | Support admin | User and device admin | Device admin | Compliance officers | Security activity admin | Advanced troubleshooting access |
|---|---|---|---|---|---|---|---|---|
| Add/Delete users and assign licenses | ✔ | Read-only |  | ✔ |  |  |  |  |
| Assign roles to users | ✔ | Read-only |  |  |  |  |  |  |
| Device management | ✔ | Read-only |  | ✔ | ✔ |  |  |  |
| Company policy and templates | ✔ | Read-only |  |  |  |  |  |  |
| Analytics and reports | ✔ | Read-only | ✔ |  |  |  |  |  |
| Troubleshooting | ✔ | Read-only | ✔ |  |  |  | ✔ |  |
| Organization-based licenses | ✔ | Read-only |  |  |  |  |  |  |
| Group-based licenses | ✔ | Read-only |  |  |  |  |  |  |
| Add or remove users from groups | ✔ | Read-only |  | ✔ |  |  |  |  |
| Individual licenses | ✔ | Read-only |  | ✔ |  |  |  |  |
| Organization settings | ✔ | Read-only |  |  |  |  |  |  |
| App integrations | ✔ | Read-only |  |  |  |  |  |  |
| Vidcast | ✔ | Read-only |  |  |  |  |  |  |
| Webex site management | ✔ | Read-only |  |  |  |  |  |  |
| Admin actions audit log | ✔ |  |  |  |  |  | ✔ |  |
| Access to user-generated content |  |  |  |  |  | ✔ |  |  |
| Legal hold |  |  |  |  |  | ✔ |  |  |
| Access to join in-progress meetings |  |  |  |  |  |  |  | ✔ |
| Access to live meetings |  |  |  |  |  |  |  | ✔ |
| Product email notifications | ✔ |  |  |  |  |  |  |  |
| View organization support cases | ✔ | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |

| Access | Webex Site Admin | Webex User Admin | Webex Read-only Admin | Meeting Content Admin |
|---|---|---|---|---|
| User Management | ✔ (User Settings. Can't add or delete users to Control Hub org.) | ✔ (User Settings. Can't add or delete users to Control Hub org.) | Read-only | ✔ (User Settings. Can't add or delete users to Control Hub org.) |
| Analytics and Reports | Read-only | Read-only | Read-only | Read-only |
| Licenses* | ✔ | ✔ | Read-only | ✔ |
| Assign Roles* | ✔ | Read-only | Read-only | ✔ |
| Site Configuration* | ✔ | Read-only | Read-only | ✔ |
| Recordings and transcripts* |  |  |  | Can download recordings and transcripts using https://developer.webex.com/meeting/docs/meetings . |
|  |

|  | Customer Organization | External Organization |
|---|---|---|
| Partner Organization | Any Other Organization |
| Full Administrator | Can administer all features of contact center. Can perform all user management activities for contact center such as: Add or remove users in the customer organization. Assign, edit, or remove contact center licenses from users. Add or revoke the Contact Center Service Administrator role from external administrators. | Can perform all administrative activities similar to full administrators from a customer organization, with the following exception: The administrator cannot add or revoke the Contact Center Service Administrator role from other external administrators. |
| Contact Center Service Administrator | NA | Can perform all administrative activities similar to full administrators from a customer organization, with the following exception: The administrator cannot add or revoke the Contact Center Service Administrator role from other external administrators. |
| Provisioning Administrator | NA | Can perform all contact center administrative activities that a partner full administrator can perform. Cannot perform any user management activities, and can only view the list of other external administrators in the organization. | NA |
| Read-only Administrator | Cannot access the Webex Contact Center administrative interfaces (Control Hub and Management Portal). | Can access the Webex Contact Center administrative interfaces (Control Hub and Management Portal) in read-only mode only. |

| 1 | Sign in to Control
            Hub . |
|---|---|
| 2 | Go to Users > Admin roles . |
| 3 | Select Create a custom role . |
| 4 | Enter a name and description for the custom role. For example, use CDR API Access for the name, and describe which administrators should
            receive the permission. |
| 5 | In the permission list, go to Reporting > Webex Calling Detailed Call History API access . |
| 6 | Click the Add button next to Webex Calling Detailed
            Call History API access . |
| 7 | Select Save . |

## Figuras

![filter button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487700.svg)

![What users with the Advanced Troubleshooting Access role can see, so they can help meeting participants with issues during meetings.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/451001-452000/451902.jpg)