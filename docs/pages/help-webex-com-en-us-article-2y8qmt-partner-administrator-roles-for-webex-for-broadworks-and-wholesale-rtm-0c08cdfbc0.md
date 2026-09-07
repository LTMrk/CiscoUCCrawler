---
doc_id: help-webex-com-en-us-article-2y8qmt-partner-administrator-roles-for-webex-for-broadworks-and-wholesale-rtm-0c08cdfbc0
source_url: https://help.webex.com/en-us/article/2y8qmt/Partner-Administrator-Roles-for-Webex-for-BroadWorks-and-Wholesale-RTM
retrieved_at: 2026-09-07T12:42:49.768939+00:00
---

Roles are used to assign administration access to settings in Partner Hub and Control Hub. There are multiple roles available, which can provide access to required administrative settings while limiting access to non-required settings. You can assign multiple roles to a single administrator or multiple administrators with varying roles and access privileges, all according to the organization needs.

Within a partner organization (Service Provider or reseller), roles can be assigned for two main administration purposes:

Partner Management—Manage settings that apply to the partner organization.

Customer Management—Manage settings that apply to customer organizations that the partner manages.

## Partner Management Roles

The following organizational and functional roles grant administrative privileges to manage settings for the partner organization itself (the organization titled “My Organization” in Partner Hub).

Full administrator —Has access to view and administer settings for partner organization. Can assign administration roles, including roles for Customer management.

Read-only administrator —Has access to view partner organization’s settings, but cannot edit settings.

Support administrator —Has access to Analytics and Troubleshooting.

User and device administrator —Has access to manage users, devices and licensing.

Device administrator —Has access to manage devices.

Compliance officer —Has access to user-generated and legal content.

Advanced troubleshooting —Access to join in-progress and live meetings.

The following table displays the level of access the above administrators have to manage settings for the partner organization.

Full administrator

Read-only administrator

Support administrator

User and device administrator

Device administrator

Compliance officer

Advanced troubleshooting

Partner Organization Settings

Assign administrator roles

✔

Read-only

Add/Delete users and assign licenses

✔

Read-only

✔

Device management

✔

Read-only

✔

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

Licenses and upgrades

✔

Read-only

✔

Organization settings

✔

Read-only

App integrations

✔

Read-only

Webex site management

✔

Read-only

Administrator actions audit log

✔

Read-only

Access to user generated content

✔

✔

Legal hold

✔

✔

Access to join in-progress meetings

✔

✔

## Customer Management Roles

The following Customer Management roles can be assigned to users in the partner organization. These roles provide access to manage settings in Partner Hub or Control Hub for customer organizations that the partner manages.

Partner full administrator —Can manage settings for all customers that the partner manages. Can also assign administrator roles to existing users in the organization and assign specific customers to be managed by partner administrators.

Partner administrator —Can manage settings for customers that the administrator provisioned or who have been assigned to the user.

Partner read-only administrator —Can view settings for all customers that the partner manages. Does not have edit access.

Help desk administrator (Basic) — Can access Help Desk view (from Partner Hub’s Troubleshooting page). Can conduct cross-organization searches of all customers under the partner for troubleshooting and support. This role provides temporary read access to customer organizations under the partner.

Help desk administrator (Advanced) —This role provides everything that the above Basic role provides, but also lets the administrator request full administrator access from a customer administrator in order to fix problems.

The following table displays access privileges that the above administrators have to manage settings in Partner Hub and Control Hub on behalf of customer organizations that the partner manages.

Partner full administrator

Partner administrator

Partner read-only administrator

Help desk administrator (Basic)

Help desk administrator (Advanced)

Partner Hub Settings

Assign administrator roles

✔

Partner analytics and reporting

✔

Read-only

Branding

✔

Read-only

Company policy and templates

✔

Create customers

✔

Customer Organization Settings

Customer List

See all

See partial

See all

See all

See all

Assign Customer Admin Roles

✔

✔

Add / Delete users and assign licenses

✔

Read-only

Read-only

Temporary when approved

Device management

✔

✔

Read-only

Read-only

Temporary when approved

Company policy and templates

✔

✔

Read-only

Read-only

Temporary when approved

Analytics and reports

✔

✔

Read-only

Read-only

Temporary when approved

Troubleshooting

✔

✔

Read-only

✔

✔

Licenses and upgrades

✔

✔

Read-only

Read-only

Temporary when approved

Organization settings

✔

✔

Read-only

Read-only

Temporary when approved

App integrations

✔

✔

Read-only

Read-only

Temporary when approved

Webex site management

✔

✔

Read-only

Read-only

Temporary when approved

Admin actions audit log

✔

✔

Read-only

Read-only

Temporary when approved

Access to user-generated content

✔

✔

Legal hold

Access to join in-progress meetings

✔

Retrieve logs

✔

✔

Provisioning administrator is a derived role rather than an assigned role. It can occur if an administrator sets up Webex services for an organization that exists already in Control Hub and which has an existing relationship to a partner and partner admin. The Provisioning administrator has similar access to a Partner administrator. However, do not have access to begin and manage Webex Trials.

## Assign Roles

The first user provisioned to the partner organization gets assigned both of the above roles automatically and can assign roles to other users in the partner organization.

Sign in to Partner Hub at http://admin.webex.com .

Select Customers and launch the view for My Organization .

In Control Hub, click Users and select the appropriate user.

If the user does not exist in your My Organization, you can add additional administrators by clicking on the manage users button and following the prompts in the wizard. Once the user is created you can go into the users section of My Organization, click on the appropriate user, and assign administrative roles. If users already have an established Common Identity for services, you will need to set up an alias for Partner Hub.

Under the Profile tab, go to Administrator roles and click the arrow > to expand the view.

Select the appropriate roles and click Save .

A full administrator in a partner organization can also assign the Partner full administrator, Partner administrator and Partner read-only administrator roles via the Partner Hub Administrators view.

## Restricted Administrator Mode

Restricted administrator mode is an organization-level setting that partner administrators can enable for customer organizations (the default setting is enabled). When a partner administrator enables Restricted mode for a customer organization, all customer administrators for that organization are restricted from editing a list of partner-defined settings in Control Hub—only a partner administrator can reset the restricted settings. For customer administrators, the level of Control Hub access is determined as follows:

(Control Hub access) = (Role entitlements) - (Restrictions)

When Restricted mode is enabled, the following items are restricted for customer administrators in that organization:

In the Users view, the following settings are not available:

Manually Add or Modify Users—No option to add or modify users, either manually or via CSV.

Claim Users—not available

Auto-assign Licenses—not available

Directory Synchronization—Unable to edit directory sync settings (this setting is available to Partner-level administrators only).

User details—No option to edit User primary Email address. However, settings such as First name, Last name and Display name are editable.

Reset Package—No option to reset the package type.

Edit Services—No option to edit the services that are enabled for a user (e.g., Messages, Meetings, Calling)

View Services status—Unable to see full status of Hybrid Services or Software Upgrade Channel

Primary Work Number—This field is read-only.

In the Account view, the following settings are not available:

Company Name is read-only.

In the Organization Settings view, the following settings are not available:

Domain—Access is read-only.

Email—The Suppress Admin Invite Email and Email Locale Selection settings are read-only.

Authentication—No option to edit Authentication and SSO settings.

In the Calling menu, the following settings are not available:

Call Settings—The App Options Call Priority settings are read-only.

Calling Behavior—Settings are read-only.

Location > PSTN—The Local Gateway and Cisco PSTN options are hidden.

Under SERVICES , the Migrations and Connected UC service options are suppressed.

Restricted mode gets applied to customer organizations, rather than to individual administrators. When this setting is on, customer administrators at that organization see a banner at the top of the Control Hub screen that lets them know that this setting is applied.

Manage Users button will be greyed out for all customer administrators.

If the partner removes the restricted administrator mode for a customer administrator, the customer administrator will be able to perform the following:

Add Webex for Wholesale users (with the button)

Change packages for a user

### Configure Restricted Administrator Mode

Partner administrators can use the below procedure to enable or disable this mode for given customer organizations (the default setting is enabled).

Sign in to Partner Hub and select Customers .

Select the applicable customer organization.

In the right-hand settings view, turn Restricted Administrator Mode on or off by enabling or disabling the following toggles:

Disable the toggle if you want to remove Restricted Mode for the customer organization.

## Related Articles

The following articles contain additional information on roles:

Assign organization roles in Control Hub —If you grant Control Hub access to customer administrators, use this article to configure role access for customer administrators.

Approve External Administrator Request —Customer administrators can use this procedure to grant a partner administrator external administrator access to their organization. An example of where this may be required is if an existing Webex organization purchases Webex services from a partner organization with whom they do not have an existing relationship. The customer administrator must approve external administrator access to the new partner administrator.

## Change History

Date of Change

Description of Change

10 February 2025

First name, Last name, and Display name are editable in Restricted Administrator mode.

06 March 2024

Removed Begin and manage Webex trials from Customer
                                            Management table.

08 August 2023

No change to the content, regular update.

31 March 2023

Created new article for Partner Administrator Roles for Wholesale RTM

08 March 2023

Partner administrators can not Add / Delete users and assign licenses.

01 February 2022

Updated the note in Assign Roles section.

|  | Full administrator | Read-only administrator | Support administrator | User and device administrator | Device administrator | Compliance officer | Advanced troubleshooting |
|---|---|---|---|---|---|---|---|
| Partner Organization Settings |
| Assign administrator roles | ✔ | Read-only |  |  |  |  |  |
| Add/Delete users and assign licenses | ✔ | Read-only |  | ✔ |  |  |  |
| Device management | ✔ | Read-only |  | ✔ | ✔ |  |  |
| Company policy and templates | ✔ | Read-only |  |  |  |  |  |
| Analytics and reports | ✔ | Read-only | ✔ |  |  |  |  |
| Troubleshooting | ✔ | Read-only | ✔ |  |  |  |  |
| Licenses and upgrades | ✔ | Read-only |  | ✔ |  |  |  |
| Organization settings | ✔ | Read-only |  |  |  |  |  |
| App integrations | ✔ | Read-only |  |  |  |  |  |
| Webex site management | ✔ | Read-only |  |  |  |  |  |
| Administrator actions audit log | ✔ | Read-only |  |  |  |  |  |
| Access to user generated content | ✔ |  |  |  |  | ✔ |  |
| Legal hold | ✔ |  |  |  |  | ✔ |  |
| Access to join in-progress meetings | ✔ |  |  |  |  |  | ✔ |

|  | Partner full administrator | Partner administrator | Partner read-only administrator | Help desk administrator (Basic) | Help desk administrator (Advanced) |
|---|---|---|---|---|---|
| Partner Hub Settings |
| Assign administrator roles | ✔ |  |  |  |  |
| Partner analytics and reporting | ✔ |  | Read-only |  |  |
| Branding | ✔ |  | Read-only |  |  |
| Company policy and templates | ✔ |  |  |  |  |
| Create customers | ✔ |  |  |  |  |
| Customer Organization Settings |
| Customer List | See all | See partial | See all | See all | See all |
| Assign Customer Admin Roles | ✔ | ✔ |  |  |  |
| Add / Delete users and assign licenses | ✔ |  | Read-only | Read-only | Temporary when approved |
| Device management | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Company policy and templates | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Analytics and reports | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Troubleshooting | ✔ | ✔ | Read-only | ✔ | ✔ |
| Licenses and upgrades | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Organization settings | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| App integrations | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Webex site management | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Admin actions audit log | ✔ | ✔ | Read-only | Read-only | Temporary when approved |
| Access to user-generated content |  |  |  | ✔ | ✔ |
| Legal hold |  |  |  |  |  |
| Access to join in-progress meetings |  |  |  |  | ✔ |
| Retrieve logs |  |  |  | ✔ | ✔ |

| 1 | Sign in to Partner Hub at http://admin.webex.com . |
|---|---|
| 2 | Select Customers and launch the view for My Organization . |
| 3 | In Control Hub, click Users and select the appropriate user. If the user does not exist in your My Organization, you can add additional administrators by clicking on the manage users button and following the prompts in the wizard. Once the user is created you can go into the users section of My Organization, click on the appropriate user, and assign administrative roles. If users already have an established Common Identity for services, you will need to set up an alias for Partner Hub. |
| 4 | Under the Profile tab, go to Administrator roles and click the arrow > to expand the view. |
| 5 | Select the appropriate roles and click Save . Partner Hub login access is assigned automatically when administrator roles are assigned. For help desk, administrators can log in to https://admin.webex.com/helpdesk . A full administrator in a partner organization can also assign the Partner full administrator, Partner administrator and Partner read-only administrator roles via the Partner Hub Administrators view. |

| Date of Change | Description of Change |
|---|---|
| 10 February 2025 | First name, Last name, and Display name are editable in Restricted Administrator mode. |
| 06 March 2024 | Removed Begin and manage Webex trials from Customer
                                            Management table. |
| 08 August 2023 | No change to the content, regular update. |
| 31 March 2023 | Created new article for Partner Administrator Roles for Wholesale RTM |
| 08 March 2023 | Partner administrators can not Add / Delete users and assign licenses. |
| 01 February 2022 | Updated the note in Assign Roles section. |