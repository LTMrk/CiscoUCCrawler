---
doc_id: help-webex-com-en-us-article-ndl247o-580c1e512b
source_url: https://help.webex.com/en-us/article/ndl247o
retrieved_at: 2026-09-01T20:21:38.407219+00:00
---

## Configure organization-based automatic licensing for users

With automatic licensing, you can automatically grant Webex licenses to new users without needing to manually assign individual licenses.

Sign in to Control Hub , then under Management , select Users > Licenses .

Do one of the following:

- If you are setting up an organizational license assignment for the first time,
            click Set up .

- If you are modifying your organizational license assignment, click Edit .

Select from the available services (Calling, Meetings, Messaging, Contact
          Center).

If you select a Webex Meetings license, the wizard will display another page. Click Next to choose the account type:

- Host —Users governed by this license assignment automatically gain host privileges, and your meetings license count decreases by one.

- Attendee —Users governed by this license assignment automatically gain attendee privileges. Your meetings license count does not decrease.

The Attendee account type isn't available for users with the Webex Site Administrator role. If you want to assign these users with an attendee account, you must remove their administrative privileges for that Webex Meetings site.

In the Apply scope section, you can determine the scope of how you want to apply the license change by selecting one of the following:

Future users —Select this option if you want to apply licenses to future users only.

Existing users —Select this option if you also want to apply license assignment changes to existing users. When you select Existing users , we select Preserve licenses for existing users for you. This means that if you remove licenses from the organization assignment, users who already have those licenses are not affected. Uncheck the box if you want to use the assignment to remove licenses from users.

If you select Existing users , the license modifications
                apply to all the existing users of the organization after you click Save .

Selecting Existing users does not persist between sessions. After you save and leave this page, the next time you come back to this page, the Existing users setting is unselected again.

Review the licenses in your license assignment and click Save .

License assignments don't apply to users who are added to the organization with a
              specific license assigned at the time of user creation. Make sure that you don't
              manually assign licenses to new users if you want the license assignments to
              automatically assign licenses.

## Configure automatic licensing for users at the group level

When you synchronize your Webex organization with Active Directory, any new users are granted the licenses that you selected on that group's license assignment. You should only synchronize those Active Directory groups with a Group Policy. Webex does not support auto-assignment to Active Directory distribution groups.

If you assign licenses to an inactive user from an unverified domain, then the licenses aren’t activated until the user signs in for the first time and becomes active.

If you verified or claimed domains and want new users to use Webex services before signing in, configure Single Sign-On (SSO) and suppress automated emails before synchronizing users to the Webex cloud with the Cisco Directory Connector.

Before you begin

You may need to select groups-based automatic license management. See Select license
          assignment scope .

If users are in multiple groups, then those users are assigned licenses from all the
          license assigments applied to the groups they’re in (unless there are duplicate
          licenses).

If users are in multiple groups that assign host licenses and attendee roles for the same
          Meetings site, then users are only assigned host licenses for that Meetings site. If there
          aren’t enough host licenses, then users are assigned attendee roles.

Sign in to Control Hub and under Management , select Groups .

Select the group that you want to manage.

In the Assignments tab, do one of the following:

- If you are setting up a group license assignment for the first time, click Set up .

- If you are modifying a group license assignment, click Edit .

Select from the available services (Calling, Meetings, Messaging, Contact Center) to
          assign to this group's new users.

If you select a Webex Meetings license, the wizard has another page. Click Next to choose the account type:

- Host —A new user governed by this license assignment automatically gains host privilege, and your meetings license count decreases by one.

- Attendee —A new user governed by this license assignment automatically gains attendee privilege. Your meetings license count does not decrease.

The attendee account type isn't available for users with the Webex Site Administrator role. If you want to assign these users with an attendee account, you must remove their administrative privileges for that Webex Meetings site.

In the Apply Scope section, you can determine the scope of how you want to apply the license change by selecting one of the following:

- Future users —Select this option if you want to apply licenses to future users only.

If you select Existing users , the license modifications apply to all the existing users of the organization after you click Save .

Click Save .

Your license assignment is active. Webex automatically assigns the licenses, so that group members can use those services when they become Active.

## Delete your automatic license assignment

To delete a license assignment, follow the same steps for an organization license
        assignment or for a group license assignment; there's just a different path. If you're
        changing the license assignment mode, the assignments from the mode you're moving away from
        are automatically deleted.

Sign in to Control
            Hub and open the Users page.

Go the Licenses tab:

- For group-based management, click Groups list and select
            the group whose assignments you want to change. You see the license assignments on the Assignments tab.

- For organization-based management, the current assignment appears in the License assignment section.

Click the trashcan icon.

Acknowledge the warning.

Click Delete to confirm that you're removing the license assignment.

This action does not remove any licenses that were previously assigned to users. It
          means that Webex doesn't automatically assign licenses to future members of the group or
          organization. You can assign these licenses manually if you prefer, or set up a new
          license assignment before you add new users.

## Frequently asked questions about license assignments

### Should I use group license assignment or organization license assignment?

Yes, you can configure license assignments for the whole organization.

Yes, you can configure license assignments for specific groups within the organization.

This feature requires that you are using groups in Webex. See Group management for details about group creation in Control Hub and Cisco Directory Connector for information about how to synchronize your groups from Active Directory with Webex.

Organization-based assignments always apply to new users as you add them to your
              organization. This is shown by the (always checked) Future
                users check box on the organization licenses assignment page.

You can also choose to have the assignment apply to Existing users . This option changes the licenses assigned to all users who are already in your organization when you save the change.

If you choose Existing users , you can also Preserve
                licenses for existing users . For example, if some users already have Advanced Messaging , then you change the assignment to exclude that license,
              those users keep their advanced messaging features. Without the box checked, the
              existing users would lose those features.

Group-based assignments always apply to new users who join the group. This is shown
              by the (always checked) Future users check box on the group
              licenses assignment page.

You can also choose to have the assignment apply to Existing users . This option changes the licenses assigned to all users who are already in that group. It happens when you save the change.

If you choose Existing users , you can also decide to Preserve licenses for existing users . For example, if some
              users in the group already have Advanced Messaging , then you change the
              assignment to exclude that license, those users keep their advanced Messaging
              features. Without the box checked, the existing users in that group would lose those
              features.

Users that change groups always get the licenses from the new group. You can choose
              whether they also keep the licensing they had before the move, or if they lose their
              old assignments when they move. You control this with the Users > Licenses > Preserve licenses toggle.

Users will also lose any manually assigned licenses if the Preserve licenses toggle is deselected.

Users will always receive a union of licenses assigned at the organization level and
              the group level. This means that licenses granted by both templates are combined for
              the user.

If one template adds a license and another removes the same license, the user still
                recieves the license when both templates are applied. For example if an organization
                template adds Webex License A and a group template removes Webex License A and adds
                Webex License B, the user recieves both Webex License A and Webex License
                B.

### How do license assignments work?

Yes, you can add licenses for existing users by checking the Existing
                users option when you add or modify the license assignment. If you want
              to remove licenses with this feature, you must also uncheck Preserve
                licenses for existing users (checked by default).

Yes, you can assign or remove services for existing users if you check the Existing users box.

You should disable the preserve licenses option if you want to remove licenses from users who already had them. This applies to both organization and group assignments.

When you remove a service from a license assignment, or delete the license assignment, you get two options with license preservation. You can either enable license preservation or disable it. When you keep license preservation on, the users who were originally licensed by the license assignment keep all the services they were originally assigned. When it’s off, the licenses are removed.

New users who are licensed by a modified license assignment do not get the service that you removed. If you removed the whole license assignment, then new users do not automatically receive any licenses.

No. A group's license assignment only assigns licenses to new users who are direct members of the group. Users in nested groups don't get the licenses from the parent group's license assignment. In Control Hub, the groups hierarchy is flat.

However, if you assign or change licenses for a nested group, the user's effective
              licenses are treated as a combination of all group assignments they are part of,
              including the parent group. This means that licenses from both the nested group and
              the parent group will be added to the user.

Whenever license assignments change, for either parent or nested groups, Control Hub
              reprocesses all rules affecting the user, ensuring that the user receives the combined
              set of licenses from all relevant groups.

When you move a user from one group into another, you get two options of preserving licenses or not preserving them. On the License assignment page, there is a separate setting to choose license preservation for group transitions. That setting controls the license preservation options for asynchronous operations such as group transitions.

If a user is in multiple groups, the user gains licenses from the assignments applied to all their groups (unless there would be a duplicate assignment).

An exception to this is if users are in multiple license assignments that assign host licenses and attendee roles for the same Meetings site, then those users are only assigned host licenses for those Meetings sites. However, if there aren’t enough host licenses, then users get attendee roles.*

* Previously, the assignment would assign users with attendee roles even if licenses were available. This has been updated so that users now get assigned host licenses.

New users belonging to group license assignments that assign both attendee roles and host licenses  make sure that those users at least get attendee roles even if host licenses aren’t available. If host licenses are available, then those users get host licenses.

No, users cannot be assigned the same service more than once.

However, if you have multiple meetings sites, you can potentially grant users
              multiple meetings licenses (one for each site).

Yes, you can use license assignments to assign Webex Calling licenses to users. See Set up
                automatic license assignment templates for Webex Calling users for more
              information.

### What about Meetings licenses in Control Hub?

Yes. Users linked from Site Administration are subject to automatic licensing.

So, if you have organization based assignment, newly linked users automatically receive the licenses specified in the assignment as they come into your Control Hub organization.

Licenses are distinct in different meetings sites. So, if you have two sites with different group assignments for each, then when you move users from one group into another, the result is those users get licenses for both meetings sites.

Yes. If your assignment has a Meetings license on it, then you get an option to assign Attendee role using the license assignment.

You must have the Attendee account feature enabled for your Webex site to assign users as attendees. If you don't see the Attendee account column in the CSV file, contact the Cisco Technical Assistance Center (TAC) to enable this feature for your Webex site.

By default, Control Hub will apply three different licenses to a user(s) if you have not explicitly stated otherwise:

- Basic messaging

- Free Webex Meetings

- Call on Webex (1:1 call, non-PSTN)

You can uncheck the Basic Meetings option so that users aren't automatically assigned with Basic Meetings licenses.

To confirm that your users aren't assigned any Basic licenses (Messaging, Meeting, or
              Calling), remove those from the org-based templates.

### How does Webex allocate licenses from multiple subscriptions?

You can apply licenses from multiple subscriptions to the same assignment. This could be the case if you originally bought a subscription for 100 messaging licenses, then bought another subscription for 50 when more of your users wanted Webex.

In such cases, Webex assigns the licenses from the oldest subscription until they are all used, and then moves on to the next oldest subscription. You can see subscription creation dates in Control Hub.

### Which Contact Center license takes priority if a user is a member of different groups?

If a user is a member to two groups with different Contact Center licenses, that user will be assigned the Premium agent license.

### If I add a new user through API or CSV and assign them with a specific license, will the organization-based auto license assignment be applied to that user?

No. If you assign a license to a new user at the same time of creation, then the organization-based auto license assignment won’t apply to that user.

## Known issues

Change to Preserve licenses toggle persists on Cancel If you disable the Preserve licenses toggle in Control Hub,
            there's a warning that requires an extra click to disable. If you cancel the warning
            dialog, the toggle doesn't return to its original (enabled) state.

| 1 | Sign in to Control Hub , then under Management , select Users > Licenses . |
|---|---|
| 2 | Do one of the following: If you are setting up an organizational license assignment for the first time,
            click Set up . If you are modifying your organizational license assignment, click Edit . |
| 3 | Select from the available services (Calling, Meetings, Messaging, Contact
          Center). If you select a Webex Meetings license, the wizard will display another page. Click Next to choose the account type: Host —Users governed by this license assignment automatically gain host privileges, and your meetings license count decreases by one. Attendee —Users governed by this license assignment automatically gain attendee privileges. Your meetings license count does not decrease. The Attendee account type isn't available for users with the Webex Site Administrator role. If you want to assign these users with an attendee account, you must remove their administrative privileges for that Webex Meetings site. |
| 4 | In the Apply scope section, you can determine the scope of how you want to apply the license change by selecting one of the following: Future users —Select this option if you want to apply licenses to future users only. Existing users —Select this option if you also want to apply license assignment changes to existing users. When you select Existing users , we select Preserve licenses for existing users for you. This means that if you remove licenses from the organization assignment, users who already have those licenses are not affected. Uncheck the box if you want to use the assignment to remove licenses from users. If you select Existing users , the license modifications
                apply to all the existing users of the organization after you click Save . Selecting Existing users does not persist between sessions. After you save and leave this page, the next time you come back to this page, the Existing users setting is unselected again. |
| 5 | Review the licenses in your license assignment and click Save . Your license assignment is active. Webex automatically assigns the selected licenses to users when you add them to the
          organization. People can use the associated services when they become Active (when they
          sign in to Webex for the first time). License assignments don't apply to users who are added to the organization with a
              specific license assigned at the time of user creation. Make sure that you don't
              manually assign licenses to new users if you want the license assignments to
              automatically assign licenses. |

| 1 | Sign in to Control Hub and under Management , select Groups . |
|---|---|
| 2 | Select the group that you want to manage. |
| 3 | In the Assignments tab, do one of the following: If you are setting up a group license assignment for the first time, click Set up . If you are modifying a group license assignment, click Edit . |
| 4 | Select from the available services (Calling, Meetings, Messaging, Contact Center) to
          assign to this group's new users. If you select a Webex Meetings license, the wizard has another page. Click Next to choose the account type: Host —A new user governed by this license assignment automatically gains host privilege, and your meetings license count decreases by one. Attendee —A new user governed by this license assignment automatically gains attendee privilege. Your meetings license count does not decrease. The attendee account type isn't available for users with the Webex Site Administrator role. If you want to assign these users with an attendee account, you must remove their administrative privileges for that Webex Meetings site. |
| 5 | In the Apply Scope section, you can determine the scope of how you want to apply the license change by selecting one of the following: Future users —Select this option if you want to apply licenses to future users only. Existing users —Select this option if you also want to apply license assignment changes to existing users. When you select Existing users, we select Preserve licenses for existing users for you. This means that if you remove licenses from the group assignment, users who already have those licenses are not affected. Clear the box if you want to use the assignment to remove licenses from users. If you select Existing users , the license modifications apply to all the existing users of the organization after you click Save . |
| 6 | Click Save . Your license assignment is active. Webex automatically assigns the licenses, so that group members can use those services when they become Active. |

| 1 | Sign in to Control
            Hub and open the Users page. |
|---|---|
| 2 | Go the Licenses tab: For group-based management, click Groups list and select
            the group whose assignments you want to change. You see the license assignments on the Assignments tab. For organization-based management, the current assignment appears in the License assignment section. |
| 3 | Click the trashcan icon. Acknowledge the warning. |
| 4 | Click Delete to confirm that you're removing the license assignment. This action does not remove any licenses that were previously assigned to users. It
          means that Webex doesn't automatically assign licenses to future members of the group or
          organization. You can assign these licenses manually if you prefer, or set up a new
          license assignment before you add new users. |