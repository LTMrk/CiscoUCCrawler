---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-9-cjab-b-deploy-jabber-webex-messenger-129-cjab-b-deploy-jabber-we-82e164da9a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_9/cjab_b_deploy-jabber-webex-messenger-129/cjab_b_deploy-jabber-webex-messenger-129_chapter_0101.html
retrieved_at: 2026-08-21T21:03:52.245887+00:00
---

Webex Messenger Deployment for Cisco Jabber 12.9

# Webex Messenger Deployment for Cisco Jabber 12.9

Updated: April 1, 2024

Chapter: Create Users for Cloud Deployment

## Chapter: Create Users for Cloud Deployment

# Create Users for Cloud Deployment

## Create Users Workflow

Step 1

Create users in Webex Administration Tool using one of the following methods:

You can add users individually using the Webex Administration Tool.

You can generate an email invitation for users to self register for a Webex account. User Provisioning Information

Create and import a CSV file with your users information.

Step 2

Assign users to policy groups. Assign Users to Policies

## Create New Users

Step 1

To create a new user or administrator, select the User
                                             				  tab > Add .

Step 2

Enter information in each field. The default
                                       			 Role is User (non-administrator).

Step 3

(Optional) Select the Policy Group Assignment tab to assign a policy group
                                       			 to the user.

Step 4

If IM Archiving is enabled for your Webex Messenger Organization, the Archive IMs check box is displayed on the Add User dialog box. To log IMs for this user for archival, select the Archive IMs check box.

Step 5

To change the endpoint, select a different endpoint from the
                                       			 drop down list.

Step 6

To assign this user to an upgrade site, select a site from the Upgrade Site drop-down list.

Step 7

If your Webex Messenger Organization is enabled with Cisco Unified Communications, the Unified Communications tab is displayed on the Add
                                       User dialog box. Select the Unified Communications tab to view the settings available for Cisco Unified Communications.

Step 8

Under Cluster , select the applicable Cisco Unified
                                       			 Communications cluster to which you want to add this user.

Step 9

If your Webex Messenger Organization is enabled with Webex Meeting Center integration, the Add User dialog box is displayed. To assign the Organization Administrator role to the user,
                                       select the Organization Administrator check box.

If you have enabled Automatically enable Meeting account when creating a new user in the Meetings page, the Meeting Account check box is selected by default. In such a case, you cannot clear the Meeting Account check box.

When the Meeting Account check box is selected, it means a corresponding Webex Meeting Center account is created for this user.

Step 10

Select Save.

New users receive a welcome email based on the Welcome Email template in Webex Messenger Administration Tool.

Step 11

Repeat the previous steps to continue adding new users.

## User Provisioning
                        	 Information

User provisioning includes specifying user-provisioning information such as registration, and fields required when creating
                              a user's profile. The settings you make here impact when users are provisioned in your Webex Messenger Organization. For example, if you set specific fields as mandatory here, the user needs to compulsorily fill in those fields
                              when creating the user profile.

Webex Messenger customers can enable self-registration when there is no SAML or Directory Integration enabled. In such a case, the Organization
                              Administrator does not need to specify the registration URL. When registration is not enabled, customers can specify a custom
                              web page. Any user trying to register with an email address that matches with customer’s domain is redirected to the custom
                              web page. Customers can use this webpage to display information about their internal processes required for creating a new Webex Messenger account.

```
To obtain the Cisco Webex Messenger service, send an email to ithelpdesk@mycompany.com, or call +1 800 555 5555.
```

### Enter User
                           	 Provisioning Information

Step 1

To enter user provisioning information, under the Configuration tab select System
                                                				  Settings > User Provisioning .

Step 2

To enable users to self-register for an account with the Cisco Jabber application, select Enable user self-registration using Webex registration page .

The URL for the self-registration page is www.webex.com/go/wc. The Webex Messenger organization Administrator typically provides this URL.

If you do not select Enable user self-registration using Webex registration page, the Custom Registration URL field and the Custom Message box is displayed. In this case, you will need
                                                         to enter the URL for the custom user registration page.

Step 3

In the Custom Registration URL field, enter the URL of the
                                          			 customized self-registration page.

If you do not
                                             				enter a custom URL, the following self-registration page (default) URL is
                                             				displayed: www.webex.com/go/wc.

Step 4

In the Custom Message box, enter a description for the
                                          			 custom self-registration page.

Step 5

To notify the Organization Administrator via email each time a user registers using the self-registration page, select Send notification to Administrator when users self register using Cisco Webex registration page .

Step 6

Under Set mandatory fields for user profile , select the
                                          			 fields that are compulsorily displayed each time a user's profile is created or
                                          			 viewed. These fields always appear each time you:

create a new user

edit an existing user profile

import users from a CSV file

Step 7

Select Save .

## Create and Import a CSV File

You can easily import a large number of users from a comma separated values (CSV) file into your Webex Messenger organization. Similarly, you can export your users to a CSV file. Importing is a useful way of painlessly adding a large
                              number of users to your organization thereby saving the effort of manually adding each user.

After the import is complete, the Organization Administrator who
                              		  initiated the import receives an email with the status of the import. The email
                              		  states whether the import was a success, failure, or terminated.

The CSV file is imported and the users appear in the User tab.

### CSV Fields

Note: Organization Administrators and User Administrators cannot
                                 		  be created using the CSV Import process.

The following fields (in no specific order) should be included in the CSV file prior to importing users into Webex . Some fields are mandatory, you must enter information into them, and some are optional.

Note: If you do not want to enter information into a field, you
                                 		  can enter the character "-" and it is imported into the database as an empty
                                 		  field. You can only do this for optional fields. If you input "-" in a
                                 		  mandatory field, an error is reported on import. Do not use the value N/A.

Field Name

Description

employeeID

Mandatory
                                                						  (only SSO enabled) Enter the user's ID.

displayName

Optional Enter the user's display name.

firstName

Mandatory Enter the user's first name.

lastName

Mandatory Enter the user's last name.

email

Mandatory Enter the user's email address.

userName

Mandatory Enter the user's username in the user@email.com
                                             						format.

jobTitle

Optional Enter the user's job title or designation.

address1

Optional Enter the first line of the user's address. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users.

address2

Optional Enter the second line of the user's address. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users.

city

Optional Enter the city in which the user lives. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users.

state

Optional Enter the state in which the user lives. The Organization
                                             						Administrator can configure this field so that it is mandatory for users.

zipCode

Optional Enter the user's ZIP code. The Organization
                                             						Administrator can configure this field so that it is mandatory for users.

ISOcountry

Optional Enter the two letter country code, for example IN, US,
                                             						CN, in which the user lives. For more information see
                                             						http://www.iso.org/iso/country_codes/iso_3166_code_lists/
                                             						country_names_and_code_elements.htm. The Organization Administrator can
                                             						configure this field so that it is mandatory for users.

phoneBusinessISOCountry

Optional Enter the country code, for example IN, US, CN, for
                                             						the user's business phone number. The Organization Administrator can configure
                                             						this field so that it is mandatory for users.

phoneBusinessNumber

Optional Enter the user's business phone number. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users.

phoneMobileISOCountry

Optional Enter the country code, for example IN, US, CN, for the
                                             						user's mobile phone number. The Organization Administrator can configure this
                                             						field so that it is mandatory for users.

phoneMobileNumber

Optional Enter the user's mobile phone number. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users.

fax

Optional Enter the user's fax number.

policyGroupName

Optional Enter the default policy group to which the user
                                             						belongs.

userProfilePhotoURL

Optional Enter the URL where the user's profile picture can
                                             						be accessed.

activeConnect

Optional Indicate whether the user's status is active in Webex Enter Yes to indicate an active status and No to indicate an inactive status.

center

Optional Used to assign (Yes) or remove (No) the center
                                             						account for the Cisco Jabber application user. Only one center can be
                                             						specified.

storageAllocated

Optional Enter the storage allocated to the user in
                                             						Megabytes.

This must be a numerical value

CUCMClusterName

Optional Enter the name of the Cisco Unified Communications
                                             						Manager cluster that the user belongs to.

businessUnit

Optional Enter the business unit or department of the user.
                                             						The Organization Administrator can configure this field so that it is mandatory
                                             						for users.

IMLoggingEnable

Optional Indicate if IM logging is enabled for this user.
                                             						Enter True to indicate an enabled status and False to indicate a disabled status.

endpointName

Optional Enter the endpoint name configured for logging IMs.

autoUpgradeSiteName

Optional Enter the upgrade site name.

You can use tab,
                                             			 or comma-separated CSV files. Ensure that your CSV file is encoded in either
                                             			 UTF-8 or UTF16-LE formats.

### Select UTF-8 as the
                           	 Encoding Format

Step 1

In Microsoft Excel select File > Save As .

Step 2

In the Save As dialog box, select Tools and Web Options .

Step 3

In the Web Options dialog box, select the Encoding tab.

Step 4

From the Save this document as list, select UTF-8 .

Step 5

Select OK to return to the Save As dialog box.

Step 6

From the Save as type list, select CSV (Comma delimited) (*.csv) .

Step 7

In the File Name field, type a name for the CSV file
                                          			 and select Save .

### Import and Export
                           	 Users

Step 1

To import users from a CSV file, in the Webex Messenger Administration Tool, select the User tab > More Actions > Import/Export .

Step 2

Select Browse and select the CSV file that contains the
                                          			 list of users you want to import.

Step 3

Select Import to begin the import process.

Step 4

To export users, select Export in the Import/Export User dialog box.

A progress message indicates the progress of the export process.

Step 5

To view the CSV file that contains the exported users, select
                                          			 the time stamp of the export message.

Step 6

Select Open to view the CSV file containing your Messenger
                                          			 organization's users. Alternatively, select Save to save the CSV file to your local computer.

## Assign Users to Policies

Step 1

To assign users to policy groups, select the User tab .

Step 2

If you want to assign a policy group to a new user, create the
                                       			 new user first by selecting Add .

Step 3

If you want to assign a policy group to an existing user, search
                                       			 for the user.

Step 4

In the search result, double-click the appropriate user's name
                                       			 to open the Edit User dialog box.

Step 5

Select the Policy Group Assignment tab to open the Policy Group Assignment dialog box.

Step 6

In the Search field, enter at least one letter of the
                                       			 policy group that you want to search for and assign to this user.

Step 7

Select Search.

Step 8

In the Search Result window, select the appropriate policy
                                       			 group and select Assign to assign the policy to this user.

Step 9

Select Save to save the policy group assignment and return
                                       			 to the User tab.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create users in Webex Administration Tool using one of the following methods: You can add users individually using the Webex Administration Tool. Create New Users You can generate an email invitation for users to self register for a Webex account. User Provisioning Information Create and import a CSV file with your users information. Create and Import a CSV File |  |
| Step 2 | Assign users to policy groups. Assign Users to Policies |  |

| Step 1 | To create a new user or administrator, select the User
                                             				  tab > Add . |
|---|---|
| Step 2 | Enter information in each field. The default
                                       			 Role is User (non-administrator). Note The Business Email is the Username. You cannot edit the
                                                   				Username. | Note | The Business Email is the Username. You cannot edit the
                                                   				Username. |
| Note | The Business Email is the Username. You cannot edit the
                                                   				Username. |
| Step 3 | (Optional) Select the Policy Group Assignment tab to assign a policy group
                                       			 to the user. |
| Step 4 | If IM Archiving is enabled for your Webex Messenger Organization, the Archive IMs check box is displayed on the Add User dialog box. To log IMs for this user for archival, select the Archive IMs check box. |
| Step 5 | To change the endpoint, select a different endpoint from the
                                       			 drop down list. Selecting Default assigns the user to the endpoint preconfigured as the
                                       			 default endpoint in the IM Archiving screen. |
| Step 6 | To assign this user to an upgrade site, select a site from the Upgrade Site drop-down list. |
| Step 7 | If your Webex Messenger Organization is enabled with Cisco Unified Communications, the Unified Communications tab is displayed on the Add
                                       User dialog box. Select the Unified Communications tab to view the settings available for Cisco Unified Communications. |
| Step 8 | Under Cluster , select the applicable Cisco Unified
                                       			 Communications cluster to which you want to add this user. |
| Step 9 | If your Webex Messenger Organization is enabled with Webex Meeting Center integration, the Add User dialog box is displayed. To assign the Organization Administrator role to the user,
                                       select the Organization Administrator check box. Note If you have enabled Automatically enable Meeting account when creating a new user in the Meetings page, the Meeting Account check box is selected by default. In such a case, you cannot clear the Meeting Account check box. When the Meeting Account check box is selected, it means a corresponding Webex Meeting Center account is created for this user. | Note | If you have enabled Automatically enable Meeting account when creating a new user in the Meetings page, the Meeting Account check box is selected by default. In such a case, you cannot clear the Meeting Account check box. When the Meeting Account check box is selected, it means a corresponding Webex Meeting Center account is created for this user. |
| Note | If you have enabled Automatically enable Meeting account when creating a new user in the Meetings page, the Meeting Account check box is selected by default. In such a case, you cannot clear the Meeting Account check box. When the Meeting Account check box is selected, it means a corresponding Webex Meeting Center account is created for this user. |
| Step 10 | Select Save. New users receive a welcome email based on the Welcome Email template in Webex Messenger Administration Tool. |
| Step 11 | Repeat the previous steps to continue adding new users. |

| Note | The Business Email is the Username. You cannot edit the
                                                   				Username. |
|---|---|

| Note | If you have enabled Automatically enable Meeting account when creating a new user in the Meetings page, the Meeting Account check box is selected by default. In such a case, you cannot clear the Meeting Account check box. When the Meeting Account check box is selected, it means a corresponding Webex Meeting Center account is created for this user. |
|---|---|

| Step 1 | To enter user provisioning information, under the Configuration tab select System
                                                				  Settings > User Provisioning . |
|---|---|
| Step 2 | To enable users to self-register for an account with the Cisco Jabber application, select Enable user self-registration using Webex registration page . The URL for the self-registration page is www.webex.com/go/wc. The Webex Messenger organization Administrator typically provides this URL. Note If you do not select Enable user self-registration using Webex registration page, the Custom Registration URL field and the Custom Message box is displayed. In this case, you will need
                                                         to enter the URL for the custom user registration page. | Note | If you do not select Enable user self-registration using Webex registration page, the Custom Registration URL field and the Custom Message box is displayed. In this case, you will need
                                                         to enter the URL for the custom user registration page. |
| Note | If you do not select Enable user self-registration using Webex registration page, the Custom Registration URL field and the Custom Message box is displayed. In this case, you will need
                                                         to enter the URL for the custom user registration page. |
| Step 3 | In the Custom Registration URL field, enter the URL of the
                                          			 customized self-registration page. If you do not
                                             				enter a custom URL, the following self-registration page (default) URL is
                                             				displayed: www.webex.com/go/wc. |
| Step 4 | In the Custom Message box, enter a description for the
                                          			 custom self-registration page. |
| Step 5 | To notify the Organization Administrator via email each time a user registers using the self-registration page, select Send notification to Administrator when users self register using Cisco Webex registration page . |
| Step 6 | Under Set mandatory fields for user profile , select the
                                          			 fields that are compulsorily displayed each time a user's profile is created or
                                          			 viewed. These fields always appear each time you: create a new user edit an existing user profile import users from a CSV file |
| Step 7 | Select Save . |

| Note | If you do not select Enable user self-registration using Webex registration page, the Custom Registration URL field and the Custom Message box is displayed. In this case, you will need
                                                         to enter the URL for the custom user registration page. |
|---|---|

| Field Name | Description |
|---|---|
| employeeID | Mandatory
                                                						  (only SSO enabled) Enter the user's ID. |
| displayName | Optional Enter the user's display name. |
| firstName | Mandatory Enter the user's first name. |
| lastName | Mandatory Enter the user's last name. |
| email | Mandatory Enter the user's email address. |
| userName | Mandatory Enter the user's username in the user@email.com
                                             						format. |
| jobTitle | Optional Enter the user's job title or designation. |
| address1 | Optional Enter the first line of the user's address. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users. |
| address2 | Optional Enter the second line of the user's address. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users. |
| city | Optional Enter the city in which the user lives. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users. |
| state | Optional Enter the state in which the user lives. The Organization
                                             						Administrator can configure this field so that it is mandatory for users. |
| zipCode | Optional Enter the user's ZIP code. The Organization
                                             						Administrator can configure this field so that it is mandatory for users. |
| ISOcountry | Optional Enter the two letter country code, for example IN, US,
                                             						CN, in which the user lives. For more information see
                                             						http://www.iso.org/iso/country_codes/iso_3166_code_lists/
                                             						country_names_and_code_elements.htm. The Organization Administrator can
                                             						configure this field so that it is mandatory for users. |
| phoneBusinessISOCountry | Optional Enter the country code, for example IN, US, CN, for
                                             						the user's business phone number. The Organization Administrator can configure
                                             						this field so that it is mandatory for users. |
| phoneBusinessNumber | Optional Enter the user's business phone number. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users. |
| phoneMobileISOCountry | Optional Enter the country code, for example IN, US, CN, for the
                                             						user's mobile phone number. The Organization Administrator can configure this
                                             						field so that it is mandatory for users. |
| phoneMobileNumber | Optional Enter the user's mobile phone number. The
                                             						Organization Administrator can configure this field so that it is mandatory for
                                             						users. |
| fax | Optional Enter the user's fax number. |
| policyGroupName | Optional Enter the default policy group to which the user
                                             						belongs. |
| userProfilePhotoURL | Optional Enter the URL where the user's profile picture can
                                             						be accessed. |
| activeConnect | Optional Indicate whether the user's status is active in Webex Enter Yes to indicate an active status and No to indicate an inactive status. |
| center | Optional Used to assign (Yes) or remove (No) the center
                                             						account for the Cisco Jabber application user. Only one center can be
                                             						specified. |
| storageAllocated | Optional Enter the storage allocated to the user in
                                             						Megabytes. This must be a numerical value |
| CUCMClusterName | Optional Enter the name of the Cisco Unified Communications
                                             						Manager cluster that the user belongs to. |
| businessUnit | Optional Enter the business unit or department of the user.
                                             						The Organization Administrator can configure this field so that it is mandatory
                                             						for users. |
| IMLoggingEnable | Optional Indicate if IM logging is enabled for this user.
                                             						Enter True to indicate an enabled status and False to indicate a disabled status. |
| endpointName | Optional Enter the endpoint name configured for logging IMs. |
| autoUpgradeSiteName | Optional Enter the upgrade site name. |

| Note | You can use tab,
                                             			 or comma-separated CSV files. Ensure that your CSV file is encoded in either
                                             			 UTF-8 or UTF16-LE formats. |
|---|---|

| Step 1 | In Microsoft Excel select File > Save As . |
|---|---|
| Step 2 | In the Save As dialog box, select Tools and Web Options . |
| Step 3 | In the Web Options dialog box, select the Encoding tab. |
| Step 4 | From the Save this document as list, select UTF-8 . |
| Step 5 | Select OK to return to the Save As dialog box. |
| Step 6 | From the Save as type list, select CSV (Comma delimited) (*.csv) . |
| Step 7 | In the File Name field, type a name for the CSV file
                                          			 and select Save . |

| Step 1 | To import users from a CSV file, in the Webex Messenger Administration Tool, select the User tab > More Actions > Import/Export . |
|---|---|
| Step 2 | Select Browse and select the CSV file that contains the
                                          			 list of users you want to import. |
| Step 3 | Select Import to begin the import process. |
| Step 4 | To export users, select Export in the Import/Export User dialog box. A progress message indicates the progress of the export process. |
| Step 5 | To view the CSV file that contains the exported users, select
                                          			 the time stamp of the export message. A confirmation prompt appears. The message resembles the
                                          			 following example: Last export: 2009-06-24 09:02:01 . |
| Step 6 | Select Open to view the CSV file containing your Messenger
                                          			 organization's users. Alternatively, select Save to save the CSV file to your local computer. |

| Step 1 | To assign users to policy groups, select the User tab . |
|---|---|
| Step 2 | If you want to assign a policy group to a new user, create the
                                       			 new user first by selecting Add . |
| Step 3 | If you want to assign a policy group to an existing user, search
                                       			 for the user. |
| Step 4 | In the search result, double-click the appropriate user's name
                                       			 to open the Edit User dialog box. |
| Step 5 | Select the Policy Group Assignment tab to open the Policy Group Assignment dialog box. |
| Step 6 | In the Search field, enter at least one letter of the
                                       			 policy group that you want to search for and assign to this user. |
| Step 7 | Select Search. |
| Step 8 | In the Search Result window, select the appropriate policy
                                       			 group and select Assign to assign the policy to this user. |
| Step 9 | Select Save to save the policy group assignment and return
                                       			 to the User tab. |