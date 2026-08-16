---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-maintain-and-operate-guid-fd0ba1c51d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/maintain_and_operate/guide/uccx_b_1251su2_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_0110.html
retrieved_at: 2026-08-16T21:35:52.153714+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Cisco Applications Configuration

## Chapter: Cisco Applications Configuration

# Cisco Applications Configuration

## About Unified CCX
                        	 Applications

The Unified
                              		  CCX system uses applications to interact with contacts and perform a wide
                              		  variety of functions.

Unified CCX
                                          			 licenses you purchase and install determine the applications available on your
                                          			 system.

Unified CCX
                              		  provides the following application types:

Script

Busy

Ring-No-Answer

### Configure Script
                           	 Applications

The Unified CCX script applications are applications based on scripts created in the Unified CCXEditor. These applications come with every Unified
                                 CCX system and running scripts created in the Unified CCX Editor.

Use the
                                 		  Unified CCXEditor to create scripts that direct the Unified CCX system to
                                 		  automatically answer calls and other types of contacts, prompt callers for
                                 		  information, accept caller input, queue calls, distribute calls to available
                                 		  agents, place outbound calls, respond to HTTP requests, and send email
                                 		  messages.

Cisco
                                 		  script applications can make use of many components, such as scripts,
                                 		  prerecorded prompts, grammars, languages, locales, and custom Java classes.

Tip

Depending on your particular Unified CCX implementation, you may need to perform most or all of the following tasks to configure
                                 a Cisco script application:

Manage scripts—Cisco script applications are based on scripts that you must upload to the repository and make available to
                                       the Unified CCX system.

Manage prompts—Many applications make use of prerecorded prompts, stored as .wav files, which are played back to callers to
                                       provide information and elicit caller response. You must upload these .wav files to the repository and make them available
                                       to the Unified CCX system.

Install grammars—The Unified CCX system uses specific grammars to recognize and respond to caller response to prompts. You
                                       must store these grammars in a directory to make them available to the Unified CCX system.

Unified CCX support only W3C XML grammar for speech recognition with Nuance adapter. The following XML and regular expression
                                       (regex) grammars are supported:

Nuance extensions for XML grammar.

regex grammar for DTMF input.

Install customized Unified CCX languages—Language packs, such as American English, Canadian French, and so on, are installed
                                       with Unified CCX. You install language packs in a directory accessible by the Unified CCX system.

Install Java files—In addition to the Java files automatically installed as part of the Unified CCX installation process,
                                       you can install your own custom classes and Java Archive (JAR) files to customize the performance of your Unified CCX system.

Add a Cisco script application—Scripts created in the Unified CCXEditor are used as the basis for Cisco script applications.

Add an application trigger—Triggers are specified signals that invoke application scripts in response to incoming contacts.
                                       After adding a new Cisco script application, you need to add a trigger so that this application can respond to telephone calls
                                       and HTTP requests.

### Add New Cisco Script Application

To add a new Cisco script application, complete the following steps:

Step 1

From the Unified CCXAdministration menu bar, choose Applications > Application Management .

The Application Management web page opens, displaying the details of any existing applications.

Step 2

Click Add New icon that is displayed in the tool bar in the upper left corner of the window or the Add New button that is displayed at the bottom of the window.

The Add a New Application web page opens.

Step 3

From the Application Type drop-down menu, choose Cisco Script Application and click Next .

The Cisco Script Application configuration Web page opens.

Step 4

Specify the following fields:

Field

Description

Name

A name for the application. This is a mandatory field.

ID

Accept the automatically-generated ID, or enter a unique ID. This is a mandatory field.

The Historical Reporting feature uses this ID to identify this application.

Maximum Number Of Sessions

The maximum number of simultaneous sessions (instances) that the application can handle. This is a mandatory field.

Script

This field is available only for Cisco Script Application type. This is a mandatory field.

Perform one of the following actions:

Choose a script from the drop-down list to run the application. If the script contains parameters, the parameters are displayed
                                                               below the Script drop-down menu. Each parameter has a check box, which enables you to override the default value for that
                                                               parameter. If you want to override the value, check the check box for that parameter.

All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page.

Click Edit , enter the script name in the dialog box, and click OK . The User Prompt dialog box closes, and the name you entered appears in the Script field.

If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef

Description

Use the Tab key to automatically populate this field.

For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More .

Enabled

Click the required radio button to accept ( Yes = default) or reject ( No )

For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More .

Enable Cisco Webex Experience Management post-call survey

This field is not enabled by default. For the procedure to enable the Cisco Webex Experience Management post-call survey and information about the script variables required for Cisco Webex Experience Management post-call survey, see Cisco Unified Contact Center Express Features Guide .

After you select the Enable Cisco Webex Experience Management post-call survey check box:

If you want to play the inline survey to the customer, then select the IVR option and select the survey from the drop-down list.

If you want to provide an offline SMS/Email survey to the customer:

Select the SMS/Email option and select the survey from the drop-down list. After you select the survey, the associated questionnaire and associated
                                                                     channels are displayed. The associated channels can be sms, email, or both.

Ensure that the script selected for the application has all the variables required for SMS/Email survey to work. Select the
                                                                     check box All the variables required for the survey have been defined in the script .

Step 5

Click Add .

The Cisco Script Application page is refreshed, the Add New Trigger hyperlink appears in the left navigation bar, and the following message is displayed in the status bar on top:

The operation has been executed successfully.

Click Back to Application List icon or button to view the list of existing applications.

Step 6

Add a trigger for the application.

### Configure Busy
                           	 Application

#### Before you begin

To configure the Busy application, you will need to perform the following tasks:

Add the Busy application.

Add a Unified CM Telephony trigger to the Busy application. The Busy application is activated when it is triggered by a Unified CM Telephony trigger. The Busy application does not support HTTP triggers.

To configure the
                                 		  Unified CCX server with the Busy application, complete the following steps.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Applications > Application
                                                				  Management .

The Application
                                             				Management web page opens, displaying the details of existing applications, if
                                             				any.

Step 2

Click Add
                                             				New icon that displays in the tool bar in the upper, left corner of
                                          			 the window or the Add
                                             				New button that is displayed at the bottom of the window.

The Add a New
                                             				Application web page opens.

Step 3

From the
                                          			 Application Type drop-down menu, choose Busy , and then click Next .

The Busy
                                             				Application Configuration web page appears.

Step 4

Specify the
                                          			 following fields:

Field

Description

Name

A name
                                                         							 for the application. This is a mandatory field.

ID

Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field.

The
                                                                     								Historical Reporting feature uses this ID to identify this application.

Maximum Number Of Sessions

The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle.

The
                                                         							 following fields are displayed only on click of Show More button.

Description

Use
                                                         							 the Tab key to automatically populate this field.

Enabled

Click
                                                         							 the required radio button to accept - Yes (the default).

Step 5

Click Add .

The Busy web
                                             				page refreshes, the Add
                                                				  New Trigger hyperlink appears in the left navigation bar, and the
                                             				following message is displayed in the status bar on top:

Step 6

Add a trigger
                                          			 for the application.

### Configure
                           	 Ring-No-Answer Application

The Cisco
                                 		  Ring-No-Answer application comes with each Unified CCX system. This application
                                 		  returns a ring tone signal when a call reaches a CTI route point.

#### Before you begin

To configure the Ring-No-Answer application, you will need to perform the following tasks:

Add the Ring-No-Answer application.

Add a Unified CM Telephony trigger to the Ring-No-Answer application. The Ring-No-Answer application is activated when it is triggered by
                                       a Unified CM Telephony trigger.

To configure the Unified CCX server with the Ring-No-Answer application, complete the following steps:

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Applications > Application
                                                				  Management .

The Application
                                             				Management web page opens, displaying the details of existing applications, if
                                             				any.

Step 2

Click Add
                                             				New icon that is displayed in the tool bar in the upper, left
                                          			 corner of the window or the Add
                                             				New button that is displayed at the bottom of the window.

Step 3

From the
                                          			 Application Type drop-down menu, choose Ring-No-Answer , and then click Next .

The
                                             				Ring-No-Answer web page opens.

Step 4

Specify the
                                          			 following fields.

Field

Description

Name

A name
                                                         							 for the application. This is a mandatory field.

ID

Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field.

The
                                                                     								Historical Reporting feature uses this ID to identify this application.

Maximum Number Of Sessions

The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. This is a mandatory field.

The
                                                         							 following fields are displayed only when you click the Show More button:

Description

Use
                                                         							 the Tab key to automatically populate this field.

Enabled

Click
                                                         							 the required radio button to accept - Yes (the default).

Step 5

Click Add .

The
                                             				Ring-No-Answer web page refreshes, the Add
                                                				  New Trigger hyperlink appears in the left navigation bar, and the
                                             				following message is displayed in the status bar on top:

Step 6

Add a trigger
                                          			 for the application.

## Application
                        	 Triggers

After
                              		  adding a new Cisco application, you need to add one or more triggers so
                              		  that the application can respond to Unified CM Telephony calls and HTTP requests.

Triggers
                              		  are specified signals that invoke application scripts in response to incoming
                              		  contacts. The Unified CCX system uses Unified CM Telephony triggers to trigger responses to telephone calls and HTTP triggers to
                              		  respond to HTTP requests.

You can use either of the below two methods to add a trigger to an application:

Add the trigger from the Cisco Application web page or add the trigger from the Unified CM Telephony.

HTTP Triggers web pages available from the Subsystem menu.

### Unified CM Telephony Trigger

You must add Unified CM Telephony triggers to invoke Cisco
                                 		  applications in response to incoming contacts.

A Unified CM Telephony trigger responds to calls
                                 		  that arrive on a specific route point by selecting telephony and media
                                 		  resources to serve the call and invoking an application script to handle the
                                 		  call.

#### Add Unified CM
                              	 Telephony Triggers from Application Web Page

To add a Unified CM Telephony trigger directly from the Cisco Application Configuration web page,
                                    		  complete the following steps.

Step 1

From the
                                             			 configuration web page for the application you want to add a trigger for, click Add New
                                                				Trigger .

The Add a New
                                                				Trigger window opens.

Step 2

From the Trigger
                                             			 Type drop-down menu, choose Unified CM Telephony and click Next .

The Unified CM Telephony Trigger Configuration window opens.

Step 3

Follow the
                                             			 procedure described in Add Unified CM Telephony Trigger .

#### Add Unified CM
                              	 Telephony Triggers from Unified CCX

To add a Unified CM Telephony trigger to an application from the Unified CM Telephony subsystem, complete the following steps.

Step 1

From the Unified
                                             			 CCXAdministration menu bar, choose Subsystems > Unified CM Telephony > Triggers .

The Unified CM Telephony Trigger Configuration summary web page opens.

Step 2

Click the Add
                                                				New icon that is displayed in the tool bar in the upper, left
                                             			 corner of the window or the Add
                                                				New button that is displayed at the bottom of the window.

Step 3

The Cisco
                                             			 Unified CM Telephony Trigger Configuration web page opens. Follow the procedure
                                             			 described in Add Unified CM Telephony Trigger (Steps 3 and 4) for detailed instructions on adding and configuring a Unified
                                             			 CM Telephony trigger.

For triggers
                                                            				  created in Unified CCX, Unified CM will always show the IPv4 Address of the CTI
                                                            				  Route point, as the IP address is of the primary node or the first node in the
                                                            				  Unified CCX cluster.

### HTTP Trigger Provision

A Cisco application can be used to handle HTTP requests when
                                 		  the Unified CCX system is provisioned with an HTTP trigger.

HTTP/HTTPS triggers are available if your system has a license installed for one of the following Cisco product packages:
                                             Unified IP IVR or Unified CCX Premium.

An HTTP trigger is the relative URL a user enters into the
                                 		  client browser to start the application. You can upload either eXtensible Style
                                 		  Language Transformation (XSLT) templates or Java Server Pages (JSP) templates
                                 		  to serve as your HTTP trigger.

The following path is an example of an HTTP-triggered
                                 		  request (using the HTTP trigger name "/hello" ):

```
http://www.appserver.acme.com:9080/hello
```

In this example, the URL starts the application with the HTTP trigger "/hello" on a web server running on port 9080 with the hostname www.appserver.acme.com.

You can add the HTTP trigger from the Cisco Script
                                 		  Application web page or add the trigger from the HTTP subsystem.

#### Add HTTP Trigger from Application Web Page

To add an HTTP trigger directly from a Cisco Application
                                    		  Configuration web page, complete the following steps.

Step 1

From the configuration web page for the application you want to
                                             			 add a trigger for, click Add New Trigger hyperlink.

The Add a New Trigger window opens.

Step 2

From the Trigger Type drop-down menu, select HTTP and click Next .

The HTTP Trigger Configuration window opens.

Step 3

Specify the following fields.

Field

Description

URL

The relative URL

For example:

```
/hello
```

Language

Perform one of the following actions:

Choose a default language from the drop-down list.

Click Edit , specify a default language in the dialog box that appears, and click OK .

Maximum Number Of Sessions

The maximum amount of simultaneous sessions that can be
                                                            							 served by the HTTP subsystem for this trigger.

Idle Timeout (in ms)

Maximum amount of time (in milliseconds) that the system
                                                            							 will wait to invoke the application before rejecting a contact.

Enabled

Click the required radio button to accept - Yes (the default).

If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL.

Step 4

Click Add .

The Cisco Application Configuration web page appears, and the URL
                                                				of the HTTP trigger appears on the navigation bar.

Step 5

Test the trigger by entering the URL you just configured in the
                                             			 address bar of your browser.

For example,

```
/hello
```

The browser should display "hello" .

#### Add HTTP Trigger
                              	 from HTTP Subsystem

To
                                    		  configure a HTTP trigger from the HTTP subsystem, complete the following steps.

Step 1

From the Unified
                                             			 CCXAdministration menu bar, choose Subsystems > HTTP .

The HTTP Trigger
                                                				Configuration web page opens.

Step 2

Click the Add
                                                				New icon that is displayed in the tool bar in the upper, left
                                             			 corner of the window or the Add
                                                				New button that is displayed at the bottom of the window.

The HTTP Trigger
                                                				Configuration window opens.

Step 3

Specify the
                                             			 following mandatory fields.

Field

Description

URL

The
                                                            							 relative URL.

For
                                                            							 example:

```
/hello
```

Language

Perform one of the following actions:

Choose a default language from the drop-down list.

Click Edit , specify a default language in the dialog box that appears, and click OK .

Application Name

Choose
                                                            							 the name of the application from the drop-down list.

Maximum Number Of Sessions

The
                                                            							 maximum amount of simultaneous sessions that can be served by the HTTP
                                                            							 subsystem for this trigger.

Idle
                                                            							 Timeout (in ms)

Maximum amount of time (in milliseconds) that the system will
                                                            							 wait to invoke the application before rejecting a contact.

Enabled

Click
                                                            							 the required radio button to accept - Yes (the default)

If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL.

Step 4

Click Add .

The Cisco
                                                				Application Configuration web page appears, and the URL of the HTTP trigger
                                                				appears on the navigation bar.

Step 5

To test the
                                             			 trigger, enter the URL you just configured in the address bar of your browser.

For example,

```
/hello
```

The browser
                                                				should display "hello" .

## Script Management

Scripts are created with the Unified CCX Editor, and can perform a wide variety of functions. For example, scripts can prompt
                              callers for extension numbers to transfer calls, place callers in a queue, route calls to available agents, and place outbound
                              calls.

The Unified CCX Administration web interface contains options for managing the Unified CCX scripts. The options are available
                              at Applications > Script Management .

Your Unified CCX system includes sample scripts stored as .aef
                                          			 files.

Caution

If a large number of VRU scripts are configured for your system, the Upload a New Script and Refresh Scripts operations can take a long time to complete.
                                          			 These tasks can also result in high CPU utilization.

### Upload New
                           	 Scripts

To make a script available for use as a Unified CCX application, you must first upload the script to the repository. The Repository
                                 Datastore (RDS) database contains the uploaded scripts along with prompts, grammars, and files. The scripts are grouped into
                                 folders and subfolders. The uploaded user scripts get synchronized to the local disk and are accessible from there.

To upload
                                 		  a script to the repository, complete the following steps:

Step 1

Choose Applications > Script Management from the Unified CCX Administration menu.

The Script Management page opens.

The Script Management page allows you to only work with user scripts; it does not have language-based directories.

The following table describes the available columns on the Script Management web page.

Field

Description

Folder Path

The level of the directory in the folder drop-down list.

Name

The name of the script.

Click the icon in front of the script name to download the script file.

Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( |), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ).

Size

The size of the script file is prefixed with KB . The file size is in kilobytes.

This column is blank on the root page because the items on the page are usually folders.

Date Modified

The date, time, and time zone when the document was changed.

Modified by

The user ID of the person who modified the document.

Delete

To delete the corresponding folder.

Caution

When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system.

Rename

To rename the required subfolder within the default folder.

Refresh

To refresh the corresponding script.

Step 2

Click the Upload New Scripts icon. Alternatively, you can also click the Upload New Scripts button.

The Upload Script dialog box opens.

Step 3

In the File Name field, click Browse and navigate to the directory in which the scripts are located. Select a script, and click Open .

The script path for the profile appears in the File Name field.

Step 4

Click Upload to upload the script to the repository.

On successful upload of the license, a confirmation window appears.

You can now manage any existing scripts shown in the Script Management page. You can also add prompts to your applications.

### Download Script
                           	 File

To view or download a script file, complete the following steps:

Step 1

From the Unified CCX Administration menu bar, choose Applications > Script Management .

The Script Management page opens to display the contents of the default folder.

Step 2

Click the Download Script icon that appears before the name of the script file that you want to view or download.

The File Download dialog box opens.

Step 3

Perform one of
                                          			 the following tasks:

To view the
                                                				  script file, click Open .

The script
                                                   					 file opens in the Unified CCX Editor.

To download
                                                				  the script file, click Save , and then follow the prompts to choose a
                                                				  directory and file name for the script file.

The file is
                                                   					 saved to the specified directory.

### Refresh Scripts

Caution

The size of the script determines the loading time of script properties. Larger the size, longer the processing time. If a
                                             large number of VRU scripts are configured for your system, the Upload a New Script and Refresh Scripts operations can take a long time to complete. These tasks can also result in high CPU utilization.

The size of the script determines the loading time of script properties. Larger the size, longer the processing time.

When you make changes to a script, you must refresh the script to direct all the applications and subsystems that use this
                                 script to reload the new version. There are two script refresh options:

Refresh Scripts Individually

Refresh Bulk Scripts

#### Refresh Scripts Individually

To refresh an individual script on the Unified CCX server from the repository (RDS), complete the following steps:

Step 1

From the Unified CCXAdministration menu bar, choose Applications > Script
                                                   				  Management .

The Script Management page opens to display the contents of the default folder.

Step 2

In the row that contains the script, click Refresh .

The script information refreshes and the Script Management page reappears.

#### Refresh Bulk
                              	 Scripts

Support for high
                                                			 availability and remote servers is available only in multiple-server
                                                			 deployments.

Bulk
                                    		  scripts refers to multiple .aef script files within one .zip file.

This option is
                                                			 available only when you upload .zip files. You will see the option to refresh
                                                			 scripts after the selected file is uploaded successfully.

To refresh
                                    		  all scripts (within a zip file) with one command, complete the following steps.

Step 1

From the Unified
                                             			 CCXAdministration menu bar, choose Applications > Script
                                                   				  Management .

The Script
                                                				Management page opens to display the contents of the default folder.

Step 2

Click the Upload
                                                				New Scripts icon or button.

The Upload
                                                				Script dialog box opens.

Step 3

To locate the
                                             			 script, click the Browse button next to the File Name field, navigate
                                             			 to the directory in which the scripts are located, select a file, and click Open . The script path for the profile appears in the
                                             			 File Name field.

Tip

You can only
                                                            				  upload .zip files containing .aef files. The total size of the.zip file cannot
                                                            				  exceed 20 MB.

Step 4

Click Upload to upload the script to the repository.

A window opens,
                                                				informing you that the script upload succeeded.

Step 5

Click Refresh icon in the Script Management page.

The Script
                                                				Management web page opens, giving you the option of refreshing the script and
                                                				the applications that reference it, or just refreshing the script.

Step 6

Specify one of
                                             			 the following options:

If you want
                                                      					 all applications and subsystems that reference the script (in the repository)
                                                      					 to use the new version, click Yes .

If you only
                                                      					 want to refresh the scripts, click No .

If you want
                                                      					 to cancel the operation, click Cancel .

The script
                                                				information refreshes and the Script Management page reappears to display the
                                                				newly loaded .zip file.

### Rename Script or Folder

To rename a script or folder, complete the following steps:

Step 1

From the Unified CCXAdministration menu bar, choose Applications > Script
                                                				  Management .

The Script Management page opens to display the contents of the default folder.

Step 2

Click Rename icon for the folder or script that you
                                          			 want to rename. A dialog box opens displaying the name of the selected folder
                                          			 or script.

Step 3

Enter a new name for this folder or script in the text box.

Step 4

Click Rename button.

The dialog box refreshes to state that the folder was successfully
                                             				renamed.

Step 5

Click Return to Script Management button.

The dialog box closes and the default folder's updated Script
                                             				Management page displays the new script name.

### Delete Script or Folder

When you delete a script or a folder, you remove it
                                 		  permanently from the repository.

To delete a script or folder, complete the following steps:

Step 1

From the Unified CCXAdministration menu bar, choose Applications > Script
                                                				  Management .

The Script Management page opens to display the contents of the default folder.

Step 2

To delete a folder, click Delete icon for the folder or script that you
                                          			 want to delete.

A dialog box opens to confirm your action on the selected script
                                             			 or folder.

Step 3

Click OK .

The dialog box closes and the default folder's updated Script
                                             				Management page refreshes to display the updated list of folders and scripts.

### Sample
                           	 Scripts

Your
                                 		  Unified CCX system includes sample scripts stored as .aef files. These scripts
                                 		  have been built using Unified CCXEditor steps, including prerecorded prompts.
                                 		  You can use these scripts to create applications without performing any script
                                 		  development, or you can use these scripts as models for your own customized
                                 		  scripts.

The included
                                             			 scripts are bundled with the Unified CCX system only as samples; they are not
                                             			 supported by Cisco. For more information on these sample scripts, see the Cisco Unified Contact
                                                      				  Center Express Getting Started with Scripts .

| Note | Unified CCX
                                          			 licenses you purchase and install determine the applications available on your
                                          			 system. |
|---|---|

| Note | The Unified CCX system includes a number of sample scripts. For a description of these sample scripts, and for more information
                                          on creating scripts with the Unified CCX Editor, see the Cisco Unified Contact
                                                   				  Center Express Getting Started with Scripts . In addition, a script repository is available at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html. This repository provides some examples of scripting techniques that can leverage Unified CCX abilities. |
|---|---|

| Tip | Upload these components to the repository before you configure a Cisco script application that uses them. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Applications > Application Management . The Application Management web page opens, displaying the details of any existing applications. |
|---|---|
| Step 2 | Click Add New icon that is displayed in the tool bar in the upper left corner of the window or the Add New button that is displayed at the bottom of the window. The Add a New Application web page opens. |
| Step 3 | From the Application Type drop-down menu, choose Cisco Script Application and click Next . The Cisco Script Application configuration Web page opens. |
| Step 4 | Specify the following fields: Field Description Name A name for the application. This is a mandatory field. ID Accept the automatically-generated ID, or enter a unique ID. This is a mandatory field. Note The Historical Reporting feature uses this ID to identify this application. Maximum Number Of Sessions The maximum number of simultaneous sessions (instances) that the application can handle. This is a mandatory field. Script Note This field is available only for Cisco Script Application type. This is a mandatory field. Perform one of the following actions: Choose a script from the drop-down list to run the application. If the script contains parameters, the parameters are displayed
                                                               below the Script drop-down menu. Each parameter has a check box, which enables you to override the default value for that
                                                               parameter. If you want to override the value, check the check box for that parameter. Note All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. Click Edit , enter the script name in the dialog box, and click OK . The User Prompt dialog box closes, and the name you entered appears in the Script field. Note If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef Description Use the Tab key to automatically populate this field. Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . Enabled Click the required radio button to accept ( Yes = default) or reject ( No ) Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . Enable Cisco Webex Experience Management post-call survey This field is not enabled by default. For the procedure to enable the Cisco Webex Experience Management post-call survey and information about the script variables required for Cisco Webex Experience Management post-call survey, see Cisco Unified Contact Center Express Features Guide . After you select the Enable Cisco Webex Experience Management post-call survey check box: If you want to play the inline survey to the customer, then select the IVR option and select the survey from the drop-down list. If you want to provide an offline SMS/Email survey to the customer: Select the SMS/Email option and select the survey from the drop-down list. After you select the survey, the associated questionnaire and associated
                                                                     channels are displayed. The associated channels can be sms, email, or both. Ensure that the script selected for the application has all the variables required for SMS/Email survey to work. Select the
                                                                     check box All the variables required for the survey have been defined in the script . | Field | Description | Name | A name for the application. This is a mandatory field. | ID | Accept the automatically-generated ID, or enter a unique ID. This is a mandatory field. Note The Historical Reporting feature uses this ID to identify this application. | Note | The Historical Reporting feature uses this ID to identify this application. | Maximum Number Of Sessions | The maximum number of simultaneous sessions (instances) that the application can handle. This is a mandatory field. | Script | Note This field is available only for Cisco Script Application type. This is a mandatory field. Perform one of the following actions: Choose a script from the drop-down list to run the application. If the script contains parameters, the parameters are displayed
                                                               below the Script drop-down menu. Each parameter has a check box, which enables you to override the default value for that
                                                               parameter. If you want to override the value, check the check box for that parameter. Note All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. Click Edit , enter the script name in the dialog box, and click OK . The User Prompt dialog box closes, and the name you entered appears in the Script field. Note If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef | Note | This field is available only for Cisco Script Application type. This is a mandatory field. | Note | All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. | Note | If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef | Description | Use the Tab key to automatically populate this field. Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Enabled | Click the required radio button to accept ( Yes = default) or reject ( No ) Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Enable Cisco Webex Experience Management post-call survey | This field is not enabled by default. For the procedure to enable the Cisco Webex Experience Management post-call survey and information about the script variables required for Cisco Webex Experience Management post-call survey, see Cisco Unified Contact Center Express Features Guide . After you select the Enable Cisco Webex Experience Management post-call survey check box: If you want to play the inline survey to the customer, then select the IVR option and select the survey from the drop-down list. If you want to provide an offline SMS/Email survey to the customer: Select the SMS/Email option and select the survey from the drop-down list. After you select the survey, the associated questionnaire and associated
                                                                     channels are displayed. The associated channels can be sms, email, or both. Ensure that the script selected for the application has all the variables required for SMS/Email survey to work. Select the
                                                                     check box All the variables required for the survey have been defined in the script . |
| Field | Description |
| Name | A name for the application. This is a mandatory field. |
| ID | Accept the automatically-generated ID, or enter a unique ID. This is a mandatory field. Note The Historical Reporting feature uses this ID to identify this application. | Note | The Historical Reporting feature uses this ID to identify this application. |
| Note | The Historical Reporting feature uses this ID to identify this application. |
| Maximum Number Of Sessions | The maximum number of simultaneous sessions (instances) that the application can handle. This is a mandatory field. |
| Script | Note This field is available only for Cisco Script Application type. This is a mandatory field. Perform one of the following actions: Choose a script from the drop-down list to run the application. If the script contains parameters, the parameters are displayed
                                                               below the Script drop-down menu. Each parameter has a check box, which enables you to override the default value for that
                                                               parameter. If you want to override the value, check the check box for that parameter. Note All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. Click Edit , enter the script name in the dialog box, and click OK . The User Prompt dialog box closes, and the name you entered appears in the Script field. Note If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef | Note | This field is available only for Cisco Script Application type. This is a mandatory field. | Note | All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. | Note | If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef |
| Note | This field is available only for Cisco Script Application type. This is a mandatory field. |
| Note | All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. |
| Note | If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef |
| Description | Use the Tab key to automatically populate this field. Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Enabled | Click the required radio button to accept ( Yes = default) or reject ( No ) Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Enable Cisco Webex Experience Management post-call survey | This field is not enabled by default. For the procedure to enable the Cisco Webex Experience Management post-call survey and information about the script variables required for Cisco Webex Experience Management post-call survey, see Cisco Unified Contact Center Express Features Guide . After you select the Enable Cisco Webex Experience Management post-call survey check box: If you want to play the inline survey to the customer, then select the IVR option and select the survey from the drop-down list. If you want to provide an offline SMS/Email survey to the customer: Select the SMS/Email option and select the survey from the drop-down list. After you select the survey, the associated questionnaire and associated
                                                                     channels are displayed. The associated channels can be sms, email, or both. Ensure that the script selected for the application has all the variables required for SMS/Email survey to work. Select the
                                                                     check box All the variables required for the survey have been defined in the script . |
| Step 5 | Click Add . The Cisco Script Application page is refreshed, the Add New Trigger hyperlink appears in the left navigation bar, and the following message is displayed in the status bar on top: The operation has been executed successfully. Click Back to Application List icon or button to view the list of existing applications. |
| Step 6 | Add a trigger for the application. |

| Field | Description |
|---|---|
| Name | A name for the application. This is a mandatory field. |
| ID | Accept the automatically-generated ID, or enter a unique ID. This is a mandatory field. Note The Historical Reporting feature uses this ID to identify this application. | Note | The Historical Reporting feature uses this ID to identify this application. |
| Note | The Historical Reporting feature uses this ID to identify this application. |
| Maximum Number Of Sessions | The maximum number of simultaneous sessions (instances) that the application can handle. This is a mandatory field. |
| Script | Note This field is available only for Cisco Script Application type. This is a mandatory field. Perform one of the following actions: Choose a script from the drop-down list to run the application. If the script contains parameters, the parameters are displayed
                                                               below the Script drop-down menu. Each parameter has a check box, which enables you to override the default value for that
                                                               parameter. If you want to override the value, check the check box for that parameter. Note All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. Click Edit , enter the script name in the dialog box, and click OK . The User Prompt dialog box closes, and the name you entered appears in the Script field. Note If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef | Note | This field is available only for Cisco Script Application type. This is a mandatory field. | Note | All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. | Note | If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef |
| Note | This field is available only for Cisco Script Application type. This is a mandatory field. |
| Note | All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. |
| Note | If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef |
| Description | Use the Tab key to automatically populate this field. Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Enabled | Click the required radio button to accept ( Yes = default) or reject ( No ) Note For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . | Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
| Enable Cisco Webex Experience Management post-call survey | This field is not enabled by default. For the procedure to enable the Cisco Webex Experience Management post-call survey and information about the script variables required for Cisco Webex Experience Management post-call survey, see Cisco Unified Contact Center Express Features Guide . After you select the Enable Cisco Webex Experience Management post-call survey check box: If you want to play the inline survey to the customer, then select the IVR option and select the survey from the drop-down list. If you want to provide an offline SMS/Email survey to the customer: Select the SMS/Email option and select the survey from the drop-down list. After you select the survey, the associated questionnaire and associated
                                                                     channels are displayed. The associated channels can be sms, email, or both. Ensure that the script selected for the application has all the variables required for SMS/Email survey to work. Select the
                                                                     check box All the variables required for the survey have been defined in the script . |

| Note | The Historical Reporting feature uses this ID to identify this application. |
|---|---|

| Note | This field is available only for Cisco Script Application type. This is a mandatory field. |
|---|---|

| Note | All scripts under the default directory are listed in the drop-down list of the Script field in the Cisco Script Application
                                                                     Configuration web page. |
|---|---|

| Note | If you enter the script name as a file URL, enter the value with double backslashes (\\). For example, file://c:\\temp\\aa.aef |
|---|---|

| Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
|---|---|

| Note | For the Busy and Ring-No-Answer application types, this field is visible only when you click Show More . |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Applications > Application
                                                				  Management . The Application
                                             				Management web page opens, displaying the details of existing applications, if
                                             				any. |
|---|---|
| Step 2 | Click Add
                                             				New icon that displays in the tool bar in the upper, left corner of
                                          			 the window or the Add
                                             				New button that is displayed at the bottom of the window. The Add a New
                                             				Application web page opens. |
| Step 3 | From the
                                          			 Application Type drop-down menu, choose Busy , and then click Next . The Busy
                                             				Application Configuration web page appears. |
| Step 4 | Specify the
                                          			 following fields: Field Description Name A name
                                                         							 for the application. This is a mandatory field. ID Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. Maximum Number Of Sessions The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. The
                                                         							 following fields are displayed only on click of Show More button. Description Use
                                                         							 the Tab key to automatically populate this field. Enabled Click
                                                         							 the required radio button to accept - Yes (the default). | Field | Description | Name | A name
                                                         							 for the application. This is a mandatory field. | ID | Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Maximum Number Of Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. | The
                                                         							 following fields are displayed only on click of Show More button. | Description | Use
                                                         							 the Tab key to automatically populate this field. | Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). |
| Field | Description |
| Name | A name
                                                         							 for the application. This is a mandatory field. |
| ID | Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Maximum Number Of Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. |
| The
                                                         							 following fields are displayed only on click of Show More button. |
| Description | Use
                                                         							 the Tab key to automatically populate this field. |
| Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). |
| Step 5 | Click Add . The Busy web
                                             				page refreshes, the Add
                                                				  New Trigger hyperlink appears in the left navigation bar, and the
                                             				following message is displayed in the status bar on top: The
                                             				operation has been executed successfully |
| Step 6 | Add a trigger
                                          			 for the application. |

| Field | Description |
|---|---|
| Name | A name
                                                         							 for the application. This is a mandatory field. |
| ID | Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Maximum Number Of Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. |
| The
                                                         							 following fields are displayed only on click of Show More button. |
| Description | Use
                                                         							 the Tab key to automatically populate this field. |
| Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). |

| Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Applications > Application
                                                				  Management . The Application
                                             				Management web page opens, displaying the details of existing applications, if
                                             				any. |
|---|---|
| Step 2 | Click Add
                                             				New icon that is displayed in the tool bar in the upper, left
                                          			 corner of the window or the Add
                                             				New button that is displayed at the bottom of the window. |
| Step 3 | From the
                                          			 Application Type drop-down menu, choose Ring-No-Answer , and then click Next . The
                                             				Ring-No-Answer web page opens. |
| Step 4 | Specify the
                                          			 following fields. Field Description Name A name
                                                         							 for the application. This is a mandatory field. ID Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. Maximum Number Of Sessions The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. This is a mandatory field. The
                                                         							 following fields are displayed only when you click the Show More button: Description Use
                                                         							 the Tab key to automatically populate this field. Enabled Click
                                                         							 the required radio button to accept - Yes (the default). | Field | Description | Name | A name
                                                         							 for the application. This is a mandatory field. | ID | Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Maximum Number Of Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. This is a mandatory field. | The
                                                         							 following fields are displayed only when you click the Show More button: | Description | Use
                                                         							 the Tab key to automatically populate this field. | Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). |
| Field | Description |
| Name | A name
                                                         							 for the application. This is a mandatory field. |
| ID | Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Maximum Number Of Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. This is a mandatory field. |
| The
                                                         							 following fields are displayed only when you click the Show More button: |
| Description | Use
                                                         							 the Tab key to automatically populate this field. |
| Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). |
| Step 5 | Click Add . The
                                             				Ring-No-Answer web page refreshes, the Add
                                                				  New Trigger hyperlink appears in the left navigation bar, and the
                                             				following message is displayed in the status bar on top: The
                                             				operation has been executed successfully |
| Step 6 | Add a trigger
                                          			 for the application. |

| Field | Description |
|---|---|
| Name | A name
                                                         							 for the application. This is a mandatory field. |
| ID | Accept
                                                         							 the automatically-generated ID, or enter a unique ID. This is a mandatory
                                                         							 field. Note The
                                                                     								Historical Reporting feature uses this ID to identify this application. | Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
| Maximum Number Of Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. This is a mandatory field. |
| The
                                                         							 following fields are displayed only when you click the Show More button: |
| Description | Use
                                                         							 the Tab key to automatically populate this field. |
| Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). |

| Note | The
                                                                     								Historical Reporting feature uses this ID to identify this application. |
|---|---|

| Step 1 | From the
                                             			 configuration web page for the application you want to add a trigger for, click Add New
                                                				Trigger . The Add a New
                                                				Trigger window opens. |
|---|---|
| Step 2 | From the Trigger
                                             			 Type drop-down menu, choose Unified CM Telephony and click Next . The Unified CM Telephony Trigger Configuration window opens. |
| Step 3 | Follow the
                                             			 procedure described in Add Unified CM Telephony Trigger . |

| Step 1 | From the Unified
                                             			 CCXAdministration menu bar, choose Subsystems > Unified CM Telephony > Triggers . The Unified CM Telephony Trigger Configuration summary web page opens. |
|---|---|
| Step 2 | Click the Add
                                                				New icon that is displayed in the tool bar in the upper, left
                                             			 corner of the window or the Add
                                                				New button that is displayed at the bottom of the window. |
| Step 3 | The Cisco
                                             			 Unified CM Telephony Trigger Configuration web page opens. Follow the procedure
                                             			 described in Add Unified CM Telephony Trigger (Steps 3 and 4) for detailed instructions on adding and configuring a Unified
                                             			 CM Telephony trigger. Note For triggers
                                                            				  created in Unified CCX, Unified CM will always show the IPv4 Address of the CTI
                                                            				  Route point, as the IP address is of the primary node or the first node in the
                                                            				  Unified CCX cluster. | Note | For triggers
                                                            				  created in Unified CCX, Unified CM will always show the IPv4 Address of the CTI
                                                            				  Route point, as the IP address is of the primary node or the first node in the
                                                            				  Unified CCX cluster. |
| Note | For triggers
                                                            				  created in Unified CCX, Unified CM will always show the IPv4 Address of the CTI
                                                            				  Route point, as the IP address is of the primary node or the first node in the
                                                            				  Unified CCX cluster. |

| Note | For triggers
                                                            				  created in Unified CCX, Unified CM will always show the IPv4 Address of the CTI
                                                            				  Route point, as the IP address is of the primary node or the first node in the
                                                            				  Unified CCX cluster. |
|---|---|

| Note | HTTP/HTTPS triggers are available if your system has a license installed for one of the following Cisco product packages:
                                             Unified IP IVR or Unified CCX Premium. |
|---|---|

| Step 1 | From the configuration web page for the application you want to
                                             			 add a trigger for, click Add New Trigger hyperlink. The Add a New Trigger window opens. |
|---|---|
| Step 2 | From the Trigger Type drop-down menu, select HTTP and click Next . The HTTP Trigger Configuration window opens. |
| Step 3 | Specify the following fields. Field Description URL The relative URL For example: /hello Language Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . Maximum Number Of Sessions The maximum amount of simultaneous sessions that can be
                                                            							 served by the HTTP subsystem for this trigger. Idle Timeout (in ms) Maximum amount of time (in milliseconds) that the system
                                                            							 will wait to invoke the application before rejecting a contact. Enabled Click the required radio button to accept - Yes (the default). Note If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. | Field | Description | URL | The relative URL For example: /hello | Language | Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . | Maximum Number Of Sessions | The maximum amount of simultaneous sessions that can be
                                                            							 served by the HTTP subsystem for this trigger. | Idle Timeout (in ms) | Maximum amount of time (in milliseconds) that the system
                                                            							 will wait to invoke the application before rejecting a contact. | Enabled | Click the required radio button to accept - Yes (the default). Note If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. | Note | If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. |
| Field | Description |
| URL | The relative URL For example: /hello |
| Language | Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . |
| Maximum Number Of Sessions | The maximum amount of simultaneous sessions that can be
                                                            							 served by the HTTP subsystem for this trigger. |
| Idle Timeout (in ms) | Maximum amount of time (in milliseconds) that the system
                                                            							 will wait to invoke the application before rejecting a contact. |
| Enabled | Click the required radio button to accept - Yes (the default). Note If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. | Note | If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. |
| Note | If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. |
| Step 4 | Click Add . The Cisco Application Configuration web page appears, and the URL
                                                				of the HTTP trigger appears on the navigation bar. |
| Step 5 | Test the trigger by entering the URL you just configured in the
                                             			 address bar of your browser. For example, /hello The browser should display "hello" . |

| Field | Description |
|---|---|
| URL | The relative URL For example: /hello |
| Language | Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . |
| Maximum Number Of Sessions | The maximum amount of simultaneous sessions that can be
                                                            							 served by the HTTP subsystem for this trigger. |
| Idle Timeout (in ms) | Maximum amount of time (in milliseconds) that the system
                                                            							 will wait to invoke the application before rejecting a contact. |
| Enabled | Click the required radio button to accept - Yes (the default). Note If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. | Note | If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. |
| Note | If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. |

| Note | If you disable the trigger, the user receives an error
                                                                        								message when browsing to the defined trigger URL. |
|---|---|

| Step 1 | From the Unified
                                             			 CCXAdministration menu bar, choose Subsystems > HTTP . The HTTP Trigger
                                                				Configuration web page opens. |
|---|---|
| Step 2 | Click the Add
                                                				New icon that is displayed in the tool bar in the upper, left
                                             			 corner of the window or the Add
                                                				New button that is displayed at the bottom of the window. The HTTP Trigger
                                                				Configuration window opens. |
| Step 3 | Specify the
                                             			 following mandatory fields. Field Description URL The
                                                            							 relative URL. For
                                                            							 example: /hello Language Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . Application Name Choose
                                                            							 the name of the application from the drop-down list. Maximum Number Of Sessions The
                                                            							 maximum amount of simultaneous sessions that can be served by the HTTP
                                                            							 subsystem for this trigger. Idle
                                                            							 Timeout (in ms) Maximum amount of time (in milliseconds) that the system will
                                                            							 wait to invoke the application before rejecting a contact. Enabled Click
                                                            							 the required radio button to accept - Yes (the default) Note If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. | Field | Description | URL | The
                                                            							 relative URL. For
                                                            							 example: /hello | Language | Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . | Application Name | Choose
                                                            							 the name of the application from the drop-down list. | Maximum Number Of Sessions | The
                                                            							 maximum amount of simultaneous sessions that can be served by the HTTP
                                                            							 subsystem for this trigger. | Idle
                                                            							 Timeout (in ms) | Maximum amount of time (in milliseconds) that the system will
                                                            							 wait to invoke the application before rejecting a contact. | Enabled | Click
                                                            							 the required radio button to accept - Yes (the default) Note If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. | Note | If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. |
| Field | Description |
| URL | The
                                                            							 relative URL. For
                                                            							 example: /hello |
| Language | Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . |
| Application Name | Choose
                                                            							 the name of the application from the drop-down list. |
| Maximum Number Of Sessions | The
                                                            							 maximum amount of simultaneous sessions that can be served by the HTTP
                                                            							 subsystem for this trigger. |
| Idle
                                                            							 Timeout (in ms) | Maximum amount of time (in milliseconds) that the system will
                                                            							 wait to invoke the application before rejecting a contact. |
| Enabled | Click
                                                            							 the required radio button to accept - Yes (the default) Note If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. | Note | If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. |
| Note | If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. |
| Step 4 | Click Add . The Cisco
                                                				Application Configuration web page appears, and the URL of the HTTP trigger
                                                				appears on the navigation bar. |
| Step 5 | To test the
                                             			 trigger, enter the URL you just configured in the address bar of your browser. For example, /hello The browser
                                                				should display "hello" . |

| Field | Description |
|---|---|
| URL | The
                                                            							 relative URL. For
                                                            							 example: /hello |
| Language | Perform one of the following actions: Choose a default language from the drop-down list. Click Edit , specify a default language in the dialog box that appears, and click OK . |
| Application Name | Choose
                                                            							 the name of the application from the drop-down list. |
| Maximum Number Of Sessions | The
                                                            							 maximum amount of simultaneous sessions that can be served by the HTTP
                                                            							 subsystem for this trigger. |
| Idle
                                                            							 Timeout (in ms) | Maximum amount of time (in milliseconds) that the system will
                                                            							 wait to invoke the application before rejecting a contact. |
| Enabled | Click
                                                            							 the required radio button to accept - Yes (the default) Note If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. | Note | If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. |
| Note | If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. |

| Note | If
                                                                        								you disable the trigger, the user receives an error message when browsing to
                                                                        								the defined trigger URL. |
|---|---|

| Note | Your Unified CCX system includes sample scripts stored as .aef
                                          			 files. |
|---|---|

| Caution | If a large number of VRU scripts are configured for your system, the Upload a New Script and Refresh Scripts operations can take a long time to complete.
                                          			 These tasks can also result in high CPU utilization. |
|---|---|

| Step 1 | Choose Applications > Script Management from the Unified CCX Administration menu. The Script Management page opens. Note The Script Management page allows you to only work with user scripts; it does not have language-based directories. The following table describes the available columns on the Script Management web page. Field Description Folder Path The level of the directory in the folder drop-down list. Name The name of the script. Note Click the icon in front of the script name to download the script file. Note Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). Size The size of the script file is prefixed with KB . The file size is in kilobytes. Note This column is blank on the root page because the items on the page are usually folders. Date Modified The date, time, and time zone when the document was changed. Modified by The user ID of the person who modified the document. Delete To delete the corresponding folder. Caution When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. Rename To rename the required subfolder within the default folder. Refresh To refresh the corresponding script. | Note | The Script Management page allows you to only work with user scripts; it does not have language-based directories. | Field | Description | Folder Path | The level of the directory in the folder drop-down list. | Name | The name of the script. Note Click the icon in front of the script name to download the script file. Note Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). | Note | Click the icon in front of the script name to download the script file. | Note | Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). | Size | The size of the script file is prefixed with KB . The file size is in kilobytes. Note This column is blank on the root page because the items on the page are usually folders. | Note | This column is blank on the root page because the items on the page are usually folders. | Date Modified | The date, time, and time zone when the document was changed. | Modified by | The user ID of the person who modified the document. | Delete | To delete the corresponding folder. Caution When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. | Caution | When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. | Rename | To rename the required subfolder within the default folder. | Refresh | To refresh the corresponding script. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | The Script Management page allows you to only work with user scripts; it does not have language-based directories. |
| Field | Description |
| Folder Path | The level of the directory in the folder drop-down list. |
| Name | The name of the script. Note Click the icon in front of the script name to download the script file. Note Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). | Note | Click the icon in front of the script name to download the script file. | Note | Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). |
| Note | Click the icon in front of the script name to download the script file. |
| Note | Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). |
| Size | The size of the script file is prefixed with KB . The file size is in kilobytes. Note This column is blank on the root page because the items on the page are usually folders. | Note | This column is blank on the root page because the items on the page are usually folders. |
| Note | This column is blank on the root page because the items on the page are usually folders. |
| Date Modified | The date, time, and time zone when the document was changed. |
| Modified by | The user ID of the person who modified the document. |
| Delete | To delete the corresponding folder. Caution When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. | Caution | When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. |
| Caution | When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. |
| Rename | To rename the required subfolder within the default folder. |
| Refresh | To refresh the corresponding script. |
| Step 2 | Click the Upload New Scripts icon. Alternatively, you can also click the Upload New Scripts button. The Upload Script dialog box opens. |
| Step 3 | In the File Name field, click Browse and navigate to the directory in which the scripts are located. Select a script, and click Open . The script path for the profile appears in the File Name field. |
| Step 4 | Click Upload to upload the script to the repository. On successful upload of the license, a confirmation window appears. You can now manage any existing scripts shown in the Script Management page. You can also add prompts to your applications. |

| Note | The Script Management page allows you to only work with user scripts; it does not have language-based directories. |
|---|---|

| Field | Description |
|---|---|
| Folder Path | The level of the directory in the folder drop-down list. |
| Name | The name of the script. Note Click the icon in front of the script name to download the script file. Note Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). | Note | Click the icon in front of the script name to download the script file. | Note | Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). |
| Note | Click the icon in front of the script name to download the script file. |
| Note | Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). |
| Size | The size of the script file is prefixed with KB . The file size is in kilobytes. Note This column is blank on the root page because the items on the page are usually folders. | Note | This column is blank on the root page because the items on the page are usually folders. |
| Note | This column is blank on the root page because the items on the page are usually folders. |
| Date Modified | The date, time, and time zone when the document was changed. |
| Modified by | The user ID of the person who modified the document. |
| Delete | To delete the corresponding folder. Caution When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. | Caution | When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. |
| Caution | When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. |
| Rename | To rename the required subfolder within the default folder. |
| Refresh | To refresh the corresponding script. |

| Note | Click the icon in front of the script name to download the script file. |
|---|---|

| Note | Unified CCX does not support the use of special characters—Dollar ($), ampersand (&), percent (%), colon (:), asterisk (*),
                                                                     question mark (?), double quotes(" "), angle brackets( < >), pipe ( \|), single quotes (' '), forward slash (/), backward slash
                                                                     ( \), square brackets ([ ]), parentheses ( ( ) ). |
|---|---|---|

| Note | This column is blank on the root page because the items on the page are usually folders. |
|---|---|

| Caution | When you delete a folder, you permanently remove it from the repository and make it unavailable to the Unified CCX system. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Applications > Script Management . The Script Management page opens to display the contents of the default folder. |
|---|---|
| Step 2 | Click the Download Script icon that appears before the name of the script file that you want to view or download. The File Download dialog box opens. |
| Step 3 | Perform one of
                                          			 the following tasks: To view the
                                                				  script file, click Open . The script
                                                   					 file opens in the Unified CCX Editor. To download
                                                				  the script file, click Save , and then follow the prompts to choose a
                                                				  directory and file name for the script file. The file is
                                                   					 saved to the specified directory. |

| Caution | The size of the script determines the loading time of script properties. Larger the size, longer the processing time. If a
                                             large number of VRU scripts are configured for your system, the Upload a New Script and Refresh Scripts operations can take a long time to complete. These tasks can also result in high CPU utilization. The size of the script determines the loading time of script properties. Larger the size, longer the processing time. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Applications > Script
                                                   				  Management . The Script Management page opens to display the contents of the default folder. |
|---|---|
| Step 2 | In the row that contains the script, click Refresh . The script information refreshes and the Script Management page reappears. |

| Note | Support for high
                                                			 availability and remote servers is available only in multiple-server
                                                			 deployments. |
|---|---|

| Note | This option is
                                                			 available only when you upload .zip files. You will see the option to refresh
                                                			 scripts after the selected file is uploaded successfully. |
|---|---|

| Step 1 | From the Unified
                                             			 CCXAdministration menu bar, choose Applications > Script
                                                   				  Management . The Script
                                                				Management page opens to display the contents of the default folder. |
|---|---|
| Step 2 | Click the Upload
                                                				New Scripts icon or button. The Upload
                                                				Script dialog box opens. |
| Step 3 | To locate the
                                             			 script, click the Browse button next to the File Name field, navigate
                                             			 to the directory in which the scripts are located, select a file, and click Open . The script path for the profile appears in the
                                             			 File Name field. Tip You can only
                                                            				  upload .zip files containing .aef files. The total size of the.zip file cannot
                                                            				  exceed 20 MB. | Tip | You can only
                                                            				  upload .zip files containing .aef files. The total size of the.zip file cannot
                                                            				  exceed 20 MB. |
| Tip | You can only
                                                            				  upload .zip files containing .aef files. The total size of the.zip file cannot
                                                            				  exceed 20 MB. |
| Step 4 | Click Upload to upload the script to the repository. A window opens,
                                                				informing you that the script upload succeeded. |
| Step 5 | Click Refresh icon in the Script Management page. The Script
                                                				Management web page opens, giving you the option of refreshing the script and
                                                				the applications that reference it, or just refreshing the script. |
| Step 6 | Specify one of
                                             			 the following options: If you want
                                                      					 all applications and subsystems that reference the script (in the repository)
                                                      					 to use the new version, click Yes . If you only
                                                      					 want to refresh the scripts, click No . If you want
                                                      					 to cancel the operation, click Cancel . The script
                                                				information refreshes and the Script Management page reappears to display the
                                                				newly loaded .zip file. |

| Tip | You can only
                                                            				  upload .zip files containing .aef files. The total size of the.zip file cannot
                                                            				  exceed 20 MB. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Applications > Script
                                                				  Management . The Script Management page opens to display the contents of the default folder. |
|---|---|
| Step 2 | Click Rename icon for the folder or script that you
                                          			 want to rename. A dialog box opens displaying the name of the selected folder
                                          			 or script. |
| Step 3 | Enter a new name for this folder or script in the text box. |
| Step 4 | Click Rename button. The dialog box refreshes to state that the folder was successfully
                                             				renamed. |
| Step 5 | Click Return to Script Management button. The dialog box closes and the default folder's updated Script
                                             				Management page displays the new script name. |

| Step 1 | From the Unified CCXAdministration menu bar, choose Applications > Script
                                                				  Management . The Script Management page opens to display the contents of the default folder. |
|---|---|
| Step 2 | To delete a folder, click Delete icon for the folder or script that you
                                          			 want to delete. A dialog box opens to confirm your action on the selected script
                                             			 or folder. |
| Step 3 | Click OK . The dialog box closes and the default folder's updated Script
                                             				Management page refreshes to display the updated list of folders and scripts. |

| Note | The included
                                             			 scripts are bundled with the Unified CCX system only as samples; they are not
                                             			 supported by Cisco. For more information on these sample scripts, see the Cisco Unified Contact
                                                      				  Center Express Getting Started with Scripts . |
|---|---|