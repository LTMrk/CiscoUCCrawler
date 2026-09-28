---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-5-digcloud-cjab-b-cloud-hybrid-deploy-125-cjab-b-cloud-hybrid-depl-1c4a6014a1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_5/DIGCloud/cjab_b_cloud-hybrid-deploy-125/cjab_b_cloud-hybrid-deploy-125_chapter_010000.html
retrieved_at: 2026-08-21T21:13:20.098297+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.5

# Cloud and Hybrid Deployments for Cisco Jabber 12.5

Updated: April 1, 2024

Chapter: Configure Cisco Webex Control Hub

## Chapter: Configure Cisco Webex Control Hub

# Configure Cisco Webex Control Hub

## Bulk Configure Users in Cisco Webex Control Hub

You can configure up to 20,000 Jabber users in the Control Hub using a CSV file. When you add the user information in the
                              CSV file, you can also assign services to the users.

Step 1

From the customer view in https://admin.webex.com go to Users , click Manage Users and choose CSV Add or Modify Users .

You might see a message about sending welcome emails to the users. Click Next to proceed or cancel and change your account settings.

Step 2

Click Export to download a CSV file with the current configuration for your users. Click download CSV template to download a template without your current user information instead.

In the CSV file that you download, you can update the existing information or add a new user on an empty row. Enter the following
                                          information in the available columns:

To assign a service, add True in that service's column, and to exclude a service, add False .

User ID/Email (Required) —Enter the user information.

For your Jabber deployment enter information for each user in the following columns of the CSV file:

Jabber team messaging mode —Add True to assign team messaging mode to your Jabber users.

Jabber calling —Add True to assign Jabber calling to your users.

UC Manager Profile —Add your Cisco UC Manager profile name from Control Hub.

Contact Migration Required —Add True to migrate users' contacts from Webex Messenger or the Cisco Unified Communications Manager IM & Presence service to their
                                                      Jabber contacts.

ContactMigrationCompleted remains False by default, allowing an administrator to later perform contact migration for specific users.

Upgrade Profile —Add the profile name if you created one. This setting does not apply for mobile clients.

If you have an active license template, leave all the service columns blank. The Control Hub automatically assigns the template
                                                for the new user in that row.

Step 3

Click Import , select your file, and click Open .

Step 4

Choose either Add services only or Add and remove services .

If you have an active license template, choose Add services only .

Step 5

Click Submit .

Submitting the CSV file uploads it and creates your task. You can close the browser or this window and your task continues
                                          to run. You can review the progress of tasks. For more information, see Manage Tasks in Cisco Webex Control Hub .

## Set Up Calling for Team Messaging Mode Users

You can set up calling for your Jabber users on team messaging mode in Control Hub. You can either create a profile for your
                              Cisco UC Manager server settings in Control Hub, or choose from your existing deployment options. The Jabber client uses these
                              settings to connect to the Cisco UC Manager server for calling capabilities.

Step 1

From the customer view in https://admin.webex.com go to Services and then click Settings on the Message card, then toggle on Enable Jabber team messaging mode .

Step 2

Select Add Profile under UC Manager Profiles .

Step 3

Enter a profile name, then select one of the following options:

Voice Services Domain —Enter the domain for your voice services.

UDS Server —Enter the IP address or hostname for your UDS Server and your backup UDS server.

(Optional)—Click Allow users to edit server address to allow your users to change the server settings in their Jabber client.

Step 4

Save the profile.

## Enable Individual Jabber Users with Team Messaging Mode and Jabber Calling

Rather than using the bulk import method, you can set up individual Jabber users for team messaging mode in Control Hub.

Step 1

From the customer view in https://admin.webex.com go to Users .

Step 2

Select a user and under the Services section, select Cisco Webex Teams .

Step 3

Choose from the following options:

Enable Jabber team messaging mode —The Jabber user is assigned team messaging mode.

Contact Migration Required —The user is asked to migrate their contacts from Webex Messenger or the Cisco Unified Communications Manager IM & Presence
                                             service to Jabber.

Enable Jabber calling —The Jabber user is assigned Jabber calling.

(Optional) You can choose a Cisco UC Manager profile for the user. Or, if you don't choose a profile, then Jabber uses the
                                             services_domain, the voice services domain, the domain of the user name, or the UPN domain to query the DNS SRV records to
                                             connect to your Cisco UC Manager.

| Step 1 | From the customer view in https://admin.webex.com go to Users , click Manage Users and choose CSV Add or Modify Users . You might see a message about sending welcome emails to the users. Click Next to proceed or cancel and change your account settings. |
|---|---|
| Step 2 | Click Export to download a CSV file with the current configuration for your users. Click download CSV template to download a template without your current user information instead. In the CSV file that you download, you can update the existing information or add a new user on an empty row. Enter the following
                                          information in the available columns: To assign a service, add True in that service's column, and to exclude a service, add False . User ID/Email (Required) —Enter the user information. For your Jabber deployment enter information for each user in the following columns of the CSV file: Jabber team messaging mode —Add True to assign team messaging mode to your Jabber users. Jabber calling —Add True to assign Jabber calling to your users. UC Manager Profile —Add your Cisco UC Manager profile name from Control Hub. Contact Migration Required —Add True to migrate users' contacts from Webex Messenger or the Cisco Unified Communications Manager IM & Presence service to their
                                                      Jabber contacts. Note ContactMigrationCompleted remains False by default, allowing an administrator to later perform contact migration for specific users. Upgrade Profile —Add the profile name if you created one. This setting does not apply for mobile clients. If you have an active license template, leave all the service columns blank. The Control Hub automatically assigns the template
                                                for the new user in that row. | Note | ContactMigrationCompleted remains False by default, allowing an administrator to later perform contact migration for specific users. |
| Note | ContactMigrationCompleted remains False by default, allowing an administrator to later perform contact migration for specific users. |
| Step 3 | Click Import , select your file, and click Open . |
| Step 4 | Choose either Add services only or Add and remove services . If you have an active license template, choose Add services only . |
| Step 5 | Click Submit . Submitting the CSV file uploads it and creates your task. You can close the browser or this window and your task continues
                                          to run. You can review the progress of tasks. For more information, see Manage Tasks in Cisco Webex Control Hub . |

| Note | ContactMigrationCompleted remains False by default, allowing an administrator to later perform contact migration for specific users. |
|---|---|

| Step 1 | From the customer view in https://admin.webex.com go to Services and then click Settings on the Message card, then toggle on Enable Jabber team messaging mode . |
|---|---|
| Step 2 | Select Add Profile under UC Manager Profiles . |
| Step 3 | Enter a profile name, then select one of the following options: Voice Services Domain —Enter the domain for your voice services. UDS Server —Enter the IP address or hostname for your UDS Server and your backup UDS server. (Optional)—Click Allow users to edit server address to allow your users to change the server settings in their Jabber client. |
| Step 4 | Save the profile. |

| Step 1 | From the customer view in https://admin.webex.com go to Users . |
|---|---|
| Step 2 | Select a user and under the Services section, select Cisco Webex Teams . |
| Step 3 | Choose from the following options: Enable Jabber team messaging mode —The Jabber user is assigned team messaging mode. Contact Migration Required —The user is asked to migrate their contacts from Webex Messenger or the Cisco Unified Communications Manager IM & Presence
                                             service to Jabber. Enable Jabber calling —The Jabber user is assigned Jabber calling. (Optional) You can choose a Cisco UC Manager profile for the user. Or, if you don't choose a profile, then Jabber uses the
                                             services_domain, the voice services domain, the domain of the user name, or the UPN domain to query the DNS SRV records to
                                             connect to your Cisco UC Manager. |