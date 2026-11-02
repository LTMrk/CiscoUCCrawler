---
doc_id: help-webex-com-en-us-article-tb5ei1-23d5463da2
source_url: https://help.webex.com/en-us/article/tb5ei1
retrieved_at: 2026-11-02T13:12:49.936933+00:00
---

The directories on the phone are structured into Default directory and Custom directories .

The Default directory uses the End User data on Cisco Unified Communications Manager (Unified CM). The contacts in the directory are displayed in the Default
          directory on the phone. To allow your users to view and look up phone numbers
        for coworkers, you must configure the User Data Service on Cisco Unified CM.

The Custom directories retrieves contacts data through XSI service and can contain personal directory and corporate directory. For more information about how to subscribe XSI directory service, see XSI services configuration on your phone .

Contact search authentication is only supported in Custom
            directories .

If your corporate uses a Lightweight Directory Access Protocol (LDAP) directory that Cisco Unified CM syncs from an LDAP server, ensure that LDAP synchronization is configured on Cisco Unified CM. See more information about LDAP synchronization, see the Configure LDAP Synchronization chapter in System Configuration Guide for Cisco Unified
            Communications Manager, Release 15 and SUs .

## Configure User Data Service (UDS)

Follow these steps to set up your phone if your corporate uses Cisco User Data Service (UDS) to query Cisco Unified Communications Manager for directory.

On Cisco Unified CM Administration, go to System > Enterprise Parameters .

In the User Data Service Parameters section, configure the User Search Limit parameter to limit the number of users returned in a query. The default setting is 64.

Click Save to save the changes.

## Disable User Data Service (UDS)

By default, the User Data Service is enabled. If your corporate don't use UDS as directory service, you can disable the service either for all phones or for an individual phone. When disabled, users on the phone can't view the personal or corporate contacts provided by UDS.

Log in to Cisco Unified CM Administration.

Do one of the following actions as needed:

- To disable UDS for all deployed phones, go to System > Enterprise Phone Configuration .

- To disable UDS for phones sharing the same phone profile, go to Device > Phone Settings > Common Phone Profile .

- To disable UDS for an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

Set the UDS for Contacts parameter as Disabled .

Click Save to save the change.

Click Apply Config to apply the change.

| 1 | On Cisco Unified CM Administration, go to System > Enterprise Parameters . |
|---|---|
| 2 | In the User Data Service Parameters section, configure the User Search Limit parameter to limit the number of users returned in a query. The default setting is 64. |
| 3 | Click Save to save the changes. |

| 1 | Log in to Cisco Unified CM Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To disable UDS for all deployed phones, go to System > Enterprise Phone Configuration . To disable UDS for phones sharing the same phone profile, go to Device > Phone Settings > Common Phone Profile . To disable UDS for an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. |
| 3 | Set the UDS for Contacts parameter as Disabled . |
| 4 | Click Save to save the change. |
| 5 | Click Apply Config to apply the change. |