---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-maintain-and-operate-guide-uccx-04b932538f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/maintain_and_operate/guide/uccx_b_1501_admin-and-operations-guide/uccx_m_1501_applications-menu.html
retrieved_at: 2026-08-16T21:28:19.675513+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

Updated: April 30, 2025

Chapter: Applications Menu

## Chapter: Applications Menu

# Applications Menu

## Access Application Management Menu

The Application Management menu option in the Unified CCX
                              		  Administration web interface contains options for configuring and managing the
                              		  applications the Unified CCX system uses to interact with contacts and perform
                              		  a wide variety of functions.

To access the Application Management web pages, perform the
                              		  following steps:

Step 1

From the Unified CCXAdministration menu bar, choose Applications > Application
                                             				  Management .

The Applications Configuration web page opens, displaying a list of
                                          				applications that are currently configured on your Unified CCX server.

Step 2

Click 
                                       			 the Add New icon that displays in the toolbar in
                                       			 the upper left corner of the window or the Add New button that displays at the bottom of
                                       			 the window to add a new application. Add a New Application web page opens.

Step 3

Select the type of application that you want to create from the
                                       			 Application Type drop-down list.

## Manage Scripts

Use the Script Management web page to add a new script and to
                              		  rename, refresh, or delete an existing script. Unified CCX applications are
                              		  based on scripts created in the Unified CCX Editor.

To create a new subfolder under the default folder, perform the following steps:

Step 1

To access the Script Management web page, choose Applications > Script
                                             				  Management from the Unified CCX Administration menu
                                       			 bar.

The Script Management web page opens, displaying the default
                                          				directory that contains the scripts uploaded to the repository.

Step 2

Click 
                                       			 the Create New Folder icon that displays in the
                                       			 toolbar in the upper left corner of the window or the Create New Folder button that displays at the
                                       			 bottom of the window.

The Create New Folder dialog box opens.

Step 3

Enter a name of the new subfolder in the Folder Name field and
                                       			 click Create .

Once the folder is successfully created, the dialog box refreshes
                                          				with the following message:

Folder successfully created

Step 4

Click 
                                       			 the Return to Script Management button to return
                                       			 to the default folder's updated Script
                                       			 Management page. You can create any number of folders within the default folder.

## Prompt
                        	 Management

Several
                              		  system-level prompt files are loaded during Unified CCX installation. However,
                              		  any file you create
                              		  must be made available to the Unified CCXEngine before a Unified CCX
                              		  application can use them. This is done through the Unified CCX cluster's
                              		  Repository datastore, where the prompt files are created, stored, and updated.

You can use a
                                          			 custom script or the Unified CCX Administration to upload a prompt.

To access
                              		  the Prompt Management page, choose Applications > Prompt
                                    				Management from the Unified CCX Administration menu
                              		  bar.

The Prompt
                              		  Management web page contains the following icons and buttons:

Create
                                       				  Language —Click the Create
                                       				  Language icon that displays in the toolbar in the upper left corner
                                    				of the window or the Create
                                       				  Language button that displays at the bottom of the window to create
                                    				a new language folder.

Upload Zip
                                       				  Files —Click the Upload
                                       				  Zip Files icon that displays in the toolbar in the upper left
                                    				corner of the window or the Upload
                                       				  Zip Files button that displays at the bottom of the window to
                                    				upload a new prompt or zip file.

See Manage Prompt Files section to know more about the different
                              		  fields in this page and how to rename, refresh, or delete existing prompts.

## Grammar Management

Several system-level grammar files are loaded during Unified
                              		  CCX installation. However, any file you create must be made available to
                              		  the Unified CCX Engine before a Unified CCX application can use them. This is
                              		  done through the Unified CCX cluster's Repository datastore, where the
                              		  grammar files are created, stored, and updated.

To access the Grammar Management page, choose Applications > Grammar
                                    				Management from the Unified CCX Administration menu
                              		  bar.

The Grammar Management web page contains the following icons
                              		  and buttons:

Create Language —Click the Create Language icon that displays in the
                                    				toolbar in the upper left corner of the window or the Create Language button
                                    				that displays at the bottom of the window to create a new language folder.

Upload Zip Files —Click the Upload Zip Files icon that displays in the
                                    				toolbar in the upper left corner of the window or the Upload Zip Files button
                                    				that displays at the bottom of the window to upload a new grammar or zip file.

## Document Management

Several system-level document files are loaded during Unified CCX installation. However, any file you create must be made available to the Unified CCX Engine before a Unified CCX application can use them. This is done through
                              the Unified CCX cluster's Repository datastore, where the document files are created, stored, and updated.

To access the Document Management page, choose Applications > Document Management from the Unified CCX Administration menu bar.

The Document Management web page contains the following icons and buttons:

Create Language —Click the Create Language icon that displays in the toolbar in the upper left corner of the window or the Create Language button that displays at the bottom of the window to create a new language folder.

Upload Zip Files —Click the Upload Zip Files icon that displays in the toolbar in the upper left corner of the window or the Upload Zip Files button that displays at the bottom of the window to upload a new document or zip file.

Ensure that you do not upload any .jar files that are already used by Unified CCX. For the list of .jar files that are used,
                                          refer to the specific versions of the Open Source Used In UCCX document.

## AAR Management

Use the AAR Management web page to upload an AAR file to
                              		  Unified CCX.

To access the AAR Management web page, choose Applications > AAR
                                    				Management from the Unified CCXAdministration menu
                              		  bar. The AAR Management web page appears.

## Calendar Management

Use the Calendar Management section to create a new calendar. You can also configure and schedule business hours such as start
                              and end time for business days, special days, and holidays.

Step 1

From the Unified CCX Administration menu bar, choose Applications > Calendar Management .

The Calendar Management web page opens and displays the information for existing calendars, if any.

Step 2

To add a new calendar, click the Add New icon or the Add New button.

The Add New Calendar web page opens.

Step 3

In the Calendar Details section, specify the following information:

Field

Description

Name

Unique name of the calendar.

Description

Calendar description.

Time Zone

Time zone for the calendar.

The following information is available to view:

Field

Description

Associated with

Lists the names of applications and chats that are associated with the calendar.

Step 4

In the Business Hours section, select one of the following options to configure the Business Days.

- 24 hours x 7 days - The service is available 24 hours a day, 7 days a week.

- Fixed Hours - Administrator can configure a fixed time range for the entire week as per the business requirements.

- Flexible Hours - Administrator can configure a flexible time range for each of the business days as per the business requirements.

The Custom Business Hours Schedule Configuration is based on the Unified CCX server time zone.

During an upgrade of Unified CCX, by default the 24 hours x 7 days is selected as the Business Days .

Step 5

Click Next .

Step 6

In the Schedule Custom Business Days section, specify the name, date, and configure business hours for a custom business day.

Scheduling business hours for a custom business day overrides any previous schedule that was configured in Custom Business Hours for the same day.

To add more custom business days, click Add More . Click the delete icon to delete a custom business day.

Step 7

Click Next .

Step 8

In the Schedule Holidays section, configure holidays.

To add more holidays, click Add More . Click the delete icon to delete a configured holiday.

Step 9

Click Finish to save the configuration.

A maximum of 50 Calendars can be configured.

A maximum of 40 Custom Business Days and Holidays each can be configured.

### Calendar Flow

An example of the calendar step is as follows:

Step 1

Use the Calendar Step of Unified CCX Editor in any of the scripts.

Step 2

Create a new variable NewCalendar of type CCCalendar .

Step 3

Save the script in an appropriate location.

Step 4

Upload the script in Unified CCX Administration.

You can also modify and save the uploaded scripts.

Step 5

Navigate to Applications > Calendar Management .

Step 6

Create a new calendar HolidayCalendar .

Step 7

Navigate to Applications > Application Management .

Step 8

Select an application from the list or create an application.

Step 9

Select the script that has been uploaded.

Step 10

Select the calendar variable NewCalendar .

Step 11

Select HolidayCalendar from the list and save to associate the calendar with the application.

Step 12

Assign the HolidayCalendar to the appropriate supervisor.

You can assign one calendar to multiple supervisors.

The HolidayCalendar is now available in the Calendar Management tab of Advanced Supervisor Capabilities in Finesse Desktop, which can be edited by supervisors. If you have not associated HolidayCalendar in UCCX Administration, supervisors can associate it by using the Manage Application from the Application Management tab of Advanced Supervisor Capabilities in Finesse Desktop.

| Step 1 | From the Unified CCXAdministration menu bar, choose Applications > Application
                                             				  Management . The Applications Configuration web page opens, displaying a list of
                                          				applications that are currently configured on your Unified CCX server. |
|---|---|
| Step 2 | Click 
                                       			 the Add New icon that displays in the toolbar in
                                       			 the upper left corner of the window or the Add New button that displays at the bottom of
                                       			 the window to add a new application. Add a New Application web page opens. |
| Step 3 | Select the type of application that you want to create from the
                                       			 Application Type drop-down list. |

| Step 1 | To access the Script Management web page, choose Applications > Script
                                             				  Management from the Unified CCX Administration menu
                                       			 bar. The Script Management web page opens, displaying the default
                                          				directory that contains the scripts uploaded to the repository. |
|---|---|
| Step 2 | Click 
                                       			 the Create New Folder icon that displays in the
                                       			 toolbar in the upper left corner of the window or the Create New Folder button that displays at the
                                       			 bottom of the window. The Create New Folder dialog box opens. |
| Step 3 | Enter a name of the new subfolder in the Folder Name field and
                                       			 click Create . Once the folder is successfully created, the dialog box refreshes
                                          				with the following message: Folder successfully created |
| Step 4 | Click 
                                       			 the Return to Script Management button to return
                                       			 to the default folder's updated Script
                                       			 Management page. You can create any number of folders within the default folder. |

| Note | You can use a
                                          			 custom script or the Unified CCX Administration to upload a prompt. |
|---|---|

| Note | Ensure that you do not upload any .jar files that are already used by Unified CCX. For the list of .jar files that are used,
                                          refer to the specific versions of the Open Source Used In UCCX document. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Applications > Calendar Management . The Calendar Management web page opens and displays the information for existing calendars, if any. |
|---|---|
| Step 2 | To add a new calendar, click the Add New icon or the Add New button. The Add New Calendar web page opens. |
| Step 3 | In the Calendar Details section, specify the following information: Field Description Name Unique name of the calendar. Description Calendar description. Time Zone Time zone for the calendar. The following information is available to view: Table 1. Field Description Associated with Lists the names of applications and chats that are associated with the calendar. | Field | Description | Name | Unique name of the calendar. | Description | Calendar description. | Time Zone | Time zone for the calendar. | Field | Description | Associated with | Lists the names of applications and chats that are associated with the calendar. |
| Field | Description |
| Name | Unique name of the calendar. |
| Description | Calendar description. |
| Time Zone | Time zone for the calendar. |
| Field | Description |
| Associated with | Lists the names of applications and chats that are associated with the calendar. |
| Step 4 | In the Business Hours section, select one of the following options to configure the Business Days. 24 hours x 7 days - The service is available 24 hours a day, 7 days a week. Fixed Hours - Administrator can configure a fixed time range for the entire week as per the business requirements. Flexible Hours - Administrator can configure a flexible time range for each of the business days as per the business requirements. Note The Custom Business Hours Schedule Configuration is based on the Unified CCX server time zone. During an upgrade of Unified CCX, by default the 24 hours x 7 days is selected as the Business Days . | Note | The Custom Business Hours Schedule Configuration is based on the Unified CCX server time zone. During an upgrade of Unified CCX, by default the 24 hours x 7 days is selected as the Business Days . |
| Note | The Custom Business Hours Schedule Configuration is based on the Unified CCX server time zone. During an upgrade of Unified CCX, by default the 24 hours x 7 days is selected as the Business Days . |
| Step 5 | Click Next . |
| Step 6 | In the Schedule Custom Business Days section, specify the name, date, and configure business hours for a custom business day. Note Scheduling business hours for a custom business day overrides any previous schedule that was configured in Custom Business Hours for the same day. To add more custom business days, click Add More . Click the delete icon to delete a custom business day. | Note | Scheduling business hours for a custom business day overrides any previous schedule that was configured in Custom Business Hours for the same day. |
| Note | Scheduling business hours for a custom business day overrides any previous schedule that was configured in Custom Business Hours for the same day. |
| Step 7 | Click Next . |
| Step 8 | In the Schedule Holidays section, configure holidays. To add more holidays, click Add More . Click the delete icon to delete a configured holiday. |
| Step 9 | Click Finish to save the configuration. Note A maximum of 50 Calendars can be configured. A maximum of 40 Custom Business Days and Holidays each can be configured. | Note | A maximum of 50 Calendars can be configured. A maximum of 40 Custom Business Days and Holidays each can be configured. |
| Note | A maximum of 50 Calendars can be configured. A maximum of 40 Custom Business Days and Holidays each can be configured. |

| Field | Description |
|---|---|
| Name | Unique name of the calendar. |
| Description | Calendar description. |
| Time Zone | Time zone for the calendar. |

| Field | Description |
|---|---|
| Associated with | Lists the names of applications and chats that are associated with the calendar. |

| Note | The Custom Business Hours Schedule Configuration is based on the Unified CCX server time zone. During an upgrade of Unified CCX, by default the 24 hours x 7 days is selected as the Business Days . |
|---|---|

| Note | Scheduling business hours for a custom business day overrides any previous schedule that was configured in Custom Business Hours for the same day. |
|---|---|

| Note | A maximum of 50 Calendars can be configured. A maximum of 40 Custom Business Days and Holidays each can be configured. |
|---|---|

| Step 1 | Use the Calendar Step of Unified CCX Editor in any of the scripts. |
|---|---|
| Step 2 | Create a new variable NewCalendar of type CCCalendar . |
| Step 3 | Save the script in an appropriate location. |
| Step 4 | Upload the script in Unified CCX Administration. You can also modify and save the uploaded scripts. |
| Step 5 | Navigate to Applications > Calendar Management . |
| Step 6 | Create a new calendar HolidayCalendar . |
| Step 7 | Navigate to Applications > Application Management . |
| Step 8 | Select an application from the list or create an application. |
| Step 9 | Select the script that has been uploaded. |
| Step 10 | Select the calendar variable NewCalendar . |
| Step 11 | Select HolidayCalendar from the list and save to associate the calendar with the application. |
| Step 12 | Assign the HolidayCalendar to the appropriate supervisor. You can assign one calendar to multiple supervisors. The HolidayCalendar is now available in the Calendar Management tab of Advanced Supervisor Capabilities in Finesse Desktop, which can be edited by supervisors. If you have not associated HolidayCalendar in UCCX Administration, supervisors can associate it by using the Manage Application from the Application Management tab of Advanced Supervisor Capabilities in Finesse Desktop. |