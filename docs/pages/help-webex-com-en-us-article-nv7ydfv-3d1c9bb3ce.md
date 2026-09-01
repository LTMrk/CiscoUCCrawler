---
doc_id: help-webex-com-en-us-article-nv7ydfv-3d1c9bb3ce
source_url: https://help.webex.com/en-us/article/nv7ydfv
retrieved_at: 2026-09-01T20:26:16.173020+00:00
---

- Overview

- Prerequisites

- Enable Groups integration

This integration enables your Webex users to create groups in Microsoft 365 when they create teams in Webex. When you've done the integration, this is how it works for your users .

You'll need admin access to your Microsoft tenant, the MS365 groups feature, and your users
      in Entra ID. Optionally you can sync users to Webex from your on-premises Active Directory, but first
      you must sync them to AD from Entra ID.

You'll also need admin access to your Webex organization, to check that users are synced, and
      to enable content management.

## Microsoft 365 requirements

A Global admin account on your Microsoft tenant.

Microsoft 365 groups feature.

Users in Entra ID.

## Webex requirements

A Webex organization and full administrator account.

Webex messaging entitlement for users (enabled free by default).

You can set up automatic license assignment to make sure that the users get
            this entitlement when you synchronize them from your directory.

Users synchronized with Webex in one of these ways:

Synchronize users from Entra ID to your Webex organization

Read https://help.webex.com/6ta3gz .

You automatically get Webex externalId populated with Entra objectId .

Synchronize users from Entra ID on-premises

With this option, you must first synchronize the objectId from Entra ID to your on-prem AD, then map the property to the externalId in
                Webex.

Read the Deployment guide for Directory Connector to learn how to
                map AD user attributes to Webex user attributes, then synchronize the groups.

If the user's externalId is successfully
            synchronized, you can see the External ID property and its value
            on the user's profile in Control Hub. Otherwise, the External ID property is not shown on the profile.

Webex user accounts must be Active (users have signed in to Webex).

Configure Enterprise Content Management settings for your organization, and enable it for all your users. Read https://help.webex.com/nfia8at . These are the settings that you need:

Select Microsoft content management.

Toggle Enable linked folders .

Enter your Entra ID Tenant Name .

If required, select the Microsoft Global instance.

You won't see the option to choose the Entra ID instance unless you are also a tenant in a special instance, like Microsoft
                Germany. This feature is only available for Webex organizations that are tenants in
                the Microsoft Global instance.

Before you begin

The essential prerequisite is that the Webex user's externalId property
          must match the Entra ID user's objectId property.

There are two ways to create this link on your Webex users:

- Option 1: Synchronize
              the users from Entra ID into Webex . This is the most direct option.

Option 2: Directory Connector synchronization. This requires two stages:

Synchronize the user objectId from Entra ID to your on-premises Active Directory.

The procedure for doing this sync is outside the scope of Webex documentation.
                  Have a read of Microsoft Entra Connect sync: Understanding the
                    architecture and Microsoft Entra Connect sync: Understand and
                    customize synchronization .

You may need to strip some prepended text from the objectId .
                  Entra adds it during the export.

Also, we recommend that you use a new target property in Active Directory, to
                  hold the Entra user's objectId , to avoid overwriting data in
                  existing properties.

Use the Directory Connector to synchronize the users from your
                    on-premises Active Directory into Webex .

Make sure to map the AD property that holds the Entra user objectId to the Webex externalId property. You
                  should do a "dry run" sync to test that the property comes into Webex as
                  expected.

Sign in to Control Hub at https://admin.webex.com and go to the Hybrid page.

Find the Groups integration card.

Click View prerequisites .

The list is active, and shows green ticks for the complete Content Management prerequisites. If the content management settings are incomplete, Control Hub guides you to the right place to get them done.

Click Next .

Read the note about permissions, and then click Authorize .

Enter your Microsoft admin credentials when prompted.

Read the list of permissions and click Accept .

You see a success message.

Click Go to settings .

Another way to get to the settings page is Hybrid > Groups integration > Edit settings .

Slide the switch to Enable Microsoft 365 Groups Integration .

What to do next

To edit these settings, go to the Hybrid page and find the Groups integration card.

| 1 | Sign in to Control Hub at https://admin.webex.com and go to the Hybrid page. |
|---|---|
| 2 | Find the Groups integration card. |
| 3 | Click View prerequisites . The list is active, and shows green ticks for the complete Content Management prerequisites. If the content management settings are incomplete, Control Hub guides you to the right place to get them done. |
| 4 | Click Next . |
| 5 | Read the note about permissions, and then click Authorize . |
| 6 | Enter your Microsoft admin credentials when prompted. |
| 7 | Read the list of permissions and click Accept . You see a success message. |
| 8 | Click Go to settings . Another way to get to the settings page is Hybrid > Groups integration > Edit settings . |
| 9 | Slide the switch to Enable Microsoft 365 Groups Integration . |