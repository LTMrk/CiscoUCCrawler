---
doc_id: help-webex-com-en-us-article-nikzbgy-4c15dda616
source_url: https://help.webex.com/en-us/article/nikzbgy
retrieved_at: 2026-09-01T20:21:31.227952+00:00
---

## Filter users

You can filter the list to focus on the types of users that you want to manage, such as by administrators or by users that are in a Webex Meetings site.

Sign in to Control Hub , then go to Management > Users .

Click Filter .

Select the filters that you want to apply to the list. You can filter by:

Host —User has a Webex Meetings license assigned to them.

Attendee —User can only join meetings, not host them.

Admin only —User has a Webex Site Administrator role.

Select multiple Webex sites to show every account type that users have in general, and not for a specific Webex site. To see what specific account type users have for a Webex site, we recommended filtering by a single Webex site.

The list automatically updates based on the filters that you select. Click Reset to remove all of the filters at once.

## User status details

The Status column tells you if there are users in your organization
      who are inactive or haven't been verified. Use this information to decide what action to take
      on a specific user account, such as resending the verification email or removing a user from
      your organization.

Service licenses are assigned to users, regardless of their status. For example, a pending
      user still uses a license. You can remove licenses from a user if they don't need the services
      anymore.

A user can have any of the following statuses:

Active —This is the ideal state for users to be in during normal
          use. The user is part of the organization (either linked from Site Administration or
          created by a Webex admin in Control Hub) and is using or ready to use their collaboration services. No further administrative
          action is required.

Pending —The user is part of the organization but their identity
          hasn’t yet been validated. They may still be verifying their identity when accessing Webex
          for the first time. This state can happen easily during onboarding.

Users can’t use their services when they are in this state.

You can nudge unverified users to activate their accounts with a bulk activation
            email .

Compliance —The Cisco compliance team has determined that this user
          is out of compliance.

Users in this state are locked out of their account.

Contact
            support for more information.

Fraud —Cisco's fraud detection team has determined that this
          account is engaging in suspecious activity.

Users in this state are locked out of their account.

Contact
            support for more information.

Suspended —The user's account has been suspended by an
          administrator.

Transient —The user has already created an account with the same
          domain and has been claimed by your organization. The next time the user signs in they
          will be presented with a choice to change their email or delete their
          account.

## Filter column headers

You can add or remove columns that show on the Users page and the Deleted users page. For example, you may want to sort users by when they were added to your organization, or alphabetically by department. Your changes are saved automatically and are shown when you log back in.

You must be a full administrator in this organization to make these changes. External administrators and read-only administrators do not see this feature.

You can't currently filter and sort users by Sync source .

Sign in to Control Hub .

Go to Management > Users and in the list of users, click .

Select the attributes you want to appear on the page.

The Display name attribute is always visible.

(Optional) Drag and drop the column headers to rearrange the order in which they appear.

## Download a list of users

You can export your list of users to a CSV file and download it to your desktop. The exported CSV file reflects any filters, search parameters, or customized attribute columns you've applied to the user list on your screen.

Depending on the size of your organization, it may take some time for Control Hub to compile and export the user list into a CSV file. The pop up window displays any exports currently in progress. You can click Start a new download in the window to initiate a fresh file that reflects any changes you may have made since the last export was initiated.

Sign in to Control Hub , then go to Management > Users .

Click Download .

The most recently exported CSV file is available to download up to seven days after it's initiated.

Click Download from task manager when the exported CSV is
          compiled.

## Actions column details

You can make changes to a user's status in the Actions column.

If you use Cisco Directory Connector for user synchronization, you can resend invitations to users in Control Hub, but you can't reactivate, deactivate, or delete users. You must perform those actions in Active Directory and then resync the changes to Control Hub.

Depending on the status, the actions that you can take are:

Resend Invitation —Resends the verification email to users.

Reactivate User —Reactivates users to their previous status.

Deactivate User —Deactivates users and changes their status to Inactive.

Delete User —Deletes users from your organization.

## Manage user status

You can manage user status in the Actions column in Control Hub.

Sign in to Control Hub , then go to Management > Users .

Click next to a user.

Select the action you want to perform.

If your organization uses directory synchronization (e.g. DirSync, Okta, Entra ID), you need to manage users in your directory and sync those changes to Webex.

## View restricted users

When Cisco's compliance and fraud detection teams determine that a user is engaging in
        suspicious activity, the user is marked as Fraud or Compliance in Control Hub. These users no longer have access to
        Webex services.

You can view the full list of users in your organization with a designation of Fraud , Compliance , or both. You can't select
        or remove these labels from a user. If you believe that a user has been incorrectly flagged, contact
          support .

Sign in to Control Hub .

Click Users > Restricted users .

## Manage pending users

Control Hub normally deletes pending users 30 days after they were deactivated. You can change this
        to make Control Hub wait up to 90 days before deleting pending users.

Webex retains user data for pending users. If you reactivate an pending user, they can find
        their old data (Spaces and Meetings), but only if that data is still within your retention
        period.

This setting does not apply to Active Directory users that are synchronized with Webex. When you sync Active Directory with Webex:

Any users that were deactivated in the directory become pending. Webex holds these users in the pending state indefinitely.

Any users that were deleted from the directory become pending in Webex. Webex holds these users in the pending state for 7 days and then deletes them. You can
              choose to delete them sooner to free up their user license. This 7-day window still
              applies to pending users even if Directory Connector is disabled in that time.

If users originally synchronized from Active Directory are marked as pending after
              synchronization is disabled, they will be retained for the normal 30 to 90-day
              window.

Sign into Control Hub , then go to Management > Organization settings .

Scroll down to Manage pending user .

Enter a number between 30 and 90 in the Delete pending user field.

Your changes save automatically.

| 1 | Sign in to Control Hub , then go to Management > Users . |
|---|---|
| 2 | Click Filter . |
| 3 | Select the filters that you want to apply to the list. You can filter by: Administrators —Filters the list based on the administrator roles
            assigned to users. Webex sites —Filters the list by the Webex site users are a part of. This filter only applies to Control Hub-managed sites and doesn't include linked sites. When you select this filter, an Account type column is added to the list to show if users have these accounts: Host —User has a Webex Meetings license assigned to them. Attendee —User can only join meetings, not host them. Admin only —User has a Webex Site Administrator role. If users have accounts or an administrator role on multiple sites, then the Webex site column will show ... for additional sites, and Account type can show as host, attendee, and admin only. Select multiple Webex sites to show every account type that users have in general, and not for a specific Webex site. To see what specific account type users have for a Webex site, we recommended filtering by a single Webex site. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Management > Users and in the list of users, click . |
| 3 | Select the attributes you want to appear on the page. The Display name attribute is always visible. |
| 4 | (Optional) Drag and drop the column headers to rearrange the order in which they appear. |

| 1 | Sign in to Control Hub , then go to Management > Users . |
|---|---|
| 2 | Click Download . The most recently exported CSV file is available to download up to seven days after it's initiated. |
| 3 | Click Download from task manager when the exported CSV is
          compiled. |

| 1 | Sign in to Control Hub , then go to Management > Users . |
|---|---|
| 2 | Click next to a user. |
| 3 | Select the action you want to perform. If your organization uses directory synchronization (e.g. DirSync, Okta, Entra ID), you need to manage users in your directory and sync those changes to Webex. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Click Users > Restricted users . |

| 1 | Sign into Control Hub , then go to Management > Organization settings . |
|---|---|
| 2 | Scroll down to Manage pending user . |
| 3 | Enter a number between 30 and 90 in the Delete pending user field. Your changes save automatically. |