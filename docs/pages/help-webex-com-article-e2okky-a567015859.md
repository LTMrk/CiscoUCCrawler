---
doc_id: help-webex-com-article-e2okky-a567015859
source_url: https://help.webex.com/article/e2okky
retrieved_at: 2026-09-01T21:38:38.370789+00:00
---

## Add a list of users

For a list of available CSV fields and its details, see Control Hub user
          management CSV file reference .

Before you begin

If you have more than one CSV file for your organization, upload and import each file
        separately. Wait for each task to complete before proceeding to the next CSV file.

For customers in the Asia-Pacific region (including Japan, China, and Hong Kong), the
        Caller ID automatically populates from the First Name and Last Name fields.

Here are some recommendations:

Some spreadsheet editors remove the + sign from cells when they open the CSV file.
                We recommend that you use a text editor to make CSV updates. If you use a
                spreadsheet editor, ensure that you set the cell format to text and restore removed
                + signs.

Export a new CSV to capture the latest information for the fields and avoid errors
                during the import of changes.

Sign in to Control
            Hub .

Go to Management > Users .

Click the downward arrow next to Add users , then select Manage users by CSV .

Select the data you want included in the CSV file.

Select User attributes to include user attributes.

Select User licenses to include user license assignments.

Choose how to manage users.

Generate a new CSV

Download CSV template

You can also choose to include User attributes, User licenses, or both when
          downloading the CSV file.

Enter the new users' information on new lines in the CSV file.

The User ID/Email (Required) column is the only mandatory
              field.

If you have a specific directory and external numbers for each new user, then include
              the leading + for external numbers without other characters.

To assign a service, add TRUE in that service's column. To
              exclude a service, add FALSE .

If you’re using automatic license assignments , leave the service columns empty when creating users with the CSV import. Webex automatically assigns the licenses for those services to the new users.

Any suspended services appears as (Suspended) in the
                respective column header within the CSV file. Control Hub won't upload a CSV file
                with a suspended service marked TRUE .

To assign a location, enter the name in the Location column.
              If you don’t specify the location in the CSV, user onboarding fails.

If you’re adding users as supervisors for Webex Contact Center, add users
                manually . You can only assign Standard and Premium roles using a CSV.

While entering a user's name, enter both the first and last name.

The user CSV no longer includes the columns for UC Manager Profile, Calling Behavior,
              and Calling Behavior UC Manager Profile. Use the Calling template to manage the Call
              Behavior and UCM Profile in bulk. For more information, see Set up calling
                behavior .

Click Select a user list and add the updated CSV file.

Choose one of the following:

Add services only —This is the best option when adding new
              users, especially if you’re using automatic license assignment.

Add and remove services —This is the best option for adding new
              users when you want to assign or disable specific licenses.

Click Upload .

The CSV file uploads and creates your task. You can close the browser or this window.
            However, your task continues to run. To review the progress of your task, see Manage
              tasks in Webex Control Hub .

## Download a list of users

We're progressively rolling out this feature, so it may not yet be available to all
          customers.

There are two distinct ways to export user data in Control Hub, each providing different sets of fields in the export file.

- Use the download button under Management > Users to export a CSV file
            containing basic user information, such as display name, role, account status, and
            email.

- Use the downward arrow next to Add users , select Manage users by CSV to export a comprehensive
            user data file with 40+ fields and all attributes documented in this article.

Generate a report of all users in your organization by starting an export. Once the export
        is complete, you can download the CSV file from the task
          manager , where you can also track the report's progress, errors, and completion
        percentage.

Sign in to Control
            Hub .

Go to Management > Users .

Click to download all users data.

Click Start a new report .

The time needed to complete the report may vary depending on the size of your
          organization.

Click View report progress to monitor the report progress.

Starting a new report cancels the current one when a report is already in progress.

When complete, click Download to access the report.

| 1 | Sign in to Control
            Hub . |
|---|---|
| 2 | Go to Management > Users . |
| 3 | Click the downward arrow next to Add users , then select Manage users by CSV . |
| 4 | Select the data you want included in the CSV file. Select User attributes to include user attributes. Select User licenses to include user license assignments. |
| 5 | Choose how to manage users. Generate a new CSV Download CSV template You can also choose to include User attributes, User licenses, or both when
          downloading the CSV file. |
| 6 | Enter the new users' information on new lines in the CSV file. The User ID/Email (Required) column is the only mandatory
              field. If you have a specific directory and external numbers for each new user, then include
              the leading + for external numbers without other characters. To assign a service, add TRUE in that service's column. To
              exclude a service, add FALSE . If you’re using automatic license assignments , leave the service columns empty when creating users with the CSV import. Webex automatically assigns the licenses for those services to the new users. Any suspended services appears as (Suspended) in the
                respective column header within the CSV file. Control Hub won't upload a CSV file
                with a suspended service marked TRUE . To assign a location, enter the name in the Location column.
              If you don’t specify the location in the CSV, user onboarding fails. If you’re adding users as supervisors for Webex Contact Center, add users
                manually . You can only assign Standard and Premium roles using a CSV. While entering a user's name, enter both the first and last name. The user CSV no longer includes the columns for UC Manager Profile, Calling Behavior,
              and Calling Behavior UC Manager Profile. Use the Calling template to manage the Call
              Behavior and UCM Profile in bulk. For more information, see Set up calling
                behavior . |
| 7 | Click Select a user list and add the updated CSV file. |
| 8 | Choose one of the following: Add services only —This is the best option when adding new
              users, especially if you’re using automatic license assignment. Add and remove services —This is the best option for adding new
              users when you want to assign or disable specific licenses. |
| 9 | Click Upload . The CSV file uploads and creates your task. You can close the browser or this window.
            However, your task continues to run. To review the progress of your task, see Manage
              tasks in Webex Control Hub . |

| 1 | Sign in to Control
            Hub . |
|---|---|
| 2 | Go to Management > Users . |
| 3 | Click to download all users data. |
| 4 | Click Start a new report . The time needed to complete the report may vary depending on the size of your
          organization. |
| 5 | Click View report progress to monitor the report progress. Starting a new report cancels the current one when a report is already in progress. |
| 6 | When complete, click Download to access the report. |