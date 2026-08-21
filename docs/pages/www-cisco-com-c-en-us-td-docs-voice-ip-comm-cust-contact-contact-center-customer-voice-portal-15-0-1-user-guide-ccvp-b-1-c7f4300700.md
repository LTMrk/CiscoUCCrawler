---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-user-guide-ccvp-b-1-c7f4300700
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/user/guide/ccvp_b_1501_user-guide-for-unified-cvp-vxml-server-and-unified-cvp-call-studio-release/standalone_application_builder.html
retrieved_at: 2026-08-21T17:36:55.428614+00:00
---

User Guide for Unified CVP VXML Server and Unified CVP Call Studio, Release 15.0(1)

# User Guide for Unified CVP VXML Server and Unified CVP Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Standalone
	 Application Builder

## Chapter: Standalone
	 Application Builder

# Standalone
                     	 Application Builder

Generally a designer builds an application in Call Studio and then deploy to Call Services. Call Studio has the ability to
                        deploy an application locally as well as to a remote system via FTP. Deploying an application becomes more difficult in an
                        environment where many designers are working on a single application or when the enterprise follows a strict deployment policy
                        to the runtime servers. In the first scenario, multiple designers are adding content to a source repository system and no
                        single designer may have the full application in necessary to perform the deployment and even if possible, would require coordination
                        among all designers involved. In the second scenario, the production environments do not allow direct access via FTP and require
                        an automated system to place new content on to those environments, providing the flexibility to control exactly how and when
                        the content is deployed. The desire is to extract the ability to create a Call Services application from the Call Studio project
                        without requiring a person to launch Call Studio and deploy.

Universal Edition provides a tool to support this requirement named the Standalone Application Builder. It allows for the
                        deployment of an application through a command-line interface. By exposing this as a command-line tool, an administrator can
                        integrate this tool into any process that has the ability to run scripts. For example, the administrator can configure a crontab
                        to launch this utility every day with the latest content checked into a source repository. Another example is to modify existing
                        build and deploy Ant scripts to deploy the application once all other components such as elements, grammars, etc. are assembled.

This chapter
                        		explains what the Standalone Application Builder does and how to use it.

## Standalone
                        	 Application Builder Introduction

The Standalone
                           		Application Builder is a utility that deploys a Call Studio application project
                           		to a format that is required by VXML Server. It is launched via a batch script
                           		named buildApp.bat located in the Call Studio root directory.
                           		There is no license required to use this utility.

When launched, the
                           		Standalone Application Builder first validates the Call Studio project to
                           		ensure it is a valid application, and if successful, deploys the VXML Server
                           		version of the application to the destination folder. If there are validation
                           		errors, those errors are displayed in the output similar to validation errors
                           		that are displayed in Call Studio. The tool only deploys a single application
                           		at a time. To deploy multiple applications, the script can be called repeatedly
                           		pointing to different projects.

## Script Processing

The command-line usage of the Standalone Application Builder is as
                           		follows:

```
buildApp <project path> <deploy path> [-quiet <log file>] [-debug]
```

Where:

<project path> —The directory in which the Call Studio
                                 			 project to convert resides. This path should point to the location where Call
                                 			 Studio is configured to store application projects. By default, this path is
                                 			 the workspace folder within the eclipse folder.

<deploy path> —The directory to deploy the application
                                 			 to. If the Standalone Application Builder is installed on the same machine as
                                 			 VXML Server, you can pass the applications directory of %CVP_HOME%\VXMLServer so that the application is deployed
                                 			 directly to the VXML Server instance. To make the application live, you only
                                 			 need to call the deployApp VXML Server administration script.

-quiet <log file> - An optional parameter that is designed to pipe the output the script usually produces into a text file whose name is passed
                                 as <log file> . This parameter is useful for scenarios where the Standalone Application Builder is run through from an automated system
                                 that does not display data printed to the console. By piping the data to a file, any results can be analyzed later.

-debug —An optional parameter that produces additional output
                                 			 to use for debugging purposes should the deployment fail. This option should
                                 			 not be used unless directed to by customer support.

## Script Output

The following is how the output of the Standalone Application Builder will look for a successful deployment:

```
Cisco Unified Call Studio 6.0 (Standalone Application Build Mode)
© 1999-2007 Cisco Systems, Inc.
All rights reserved. Cisco, the Cisco logo, Cisco Systems, and the Cisco Systems
logo are trademarks or registered trademarks of Cisco Systems, Inc. and/or its
affiliates in the United States and certain other countries.
Start: Tue Jan 1 11:47:56 EDT 2000
*** Loading project.
*** Validating project ‘MyApp’.
*** Building project ‘MyApp’.
*** Unloading project ‘MyApp’.
*** Done.
End: Tue Jan 1 11:47:58 EDT 2000
```

The following is the output for a deployment that encounters validation errors:

```
Cisco Unified Call Studio 6.0 (Standalone Application Build Mode)
© 1999-2007 Cisco Systems, Inc.
All rights reserved. Cisco, the Cisco logo, Cisco Systems, and the Cisco Systems
logo are trademarks or registered trademarks of Cisco Systems, Inc. and/or its
affiliates in the United States and certain other countries.
Start: Tue Jan 1 11:47:56 EDT 2000
*** Loading project.
*** Validating project ‘MyApp’.
Error: Project is not valid. Aborting. See details below:
[Start Of Call] Exit States Error: Please connect all the exit states for this element.
```

## User Level Access Control for Call Studio

The administrator can set up access control for Call Studio application users by installing Call Studio in the Program Files
                           directory, thereby preventing users from having write access. Users can then use the created workspace in their user directory
                           to access the Call Studio application.

### Steps for the Administrator

Below are the steps to be done by an administrator to enable access control for users:

If you have uninstalled Call Studio application from the Program Files folder, ensure you also navigate to the system Environment Variables to locate and delete the path variable named CS_USER_HOME , as this step is crucial for completely removing all traces of the Call Studio application from your system.

Step 1

Install the Call Studio installer file (setup.exe).

Create the necessary folder structure and, during installation, change the default location from C:\Cisco\CallStudio to your desired folder location.

For example: C:\Program Files\Cisco\CallStudio .

Step 2

If Call Studio is installed in C:\Program Files\Cisco\CallStudio , it can be launched directly using the desktop shortcut. In case the Call Studio application is installed in any other location,
                                          create a shortcut for the startStudioUser.cmd file located in the %CallStudio% directory.

Ensure that this shortcut for startStudioUser.cmd is available to users so they can easily launch Call Studio.

### Steps for the Application Developer User

Below are the steps to be done by the user to launch Call Studio:

Step 1

If Call Studio is installed in C:\Program Files\Cisco\CallStudio , it can be launched directly using the desktop shortcut. In case the Call Studio application is installed in any other location,
                                          Launch Call Studio using the startStudioUser.cmd shortcut provided by the administrator, or directly launch startStudioUser.cmd file located in the %CallStudio% directory.

Ensure that this shortcut is available to users so they can easily launch Call Studio.

Step 2

The following workspace folder is created and selected by default for users (%user_directory%\Cisco\CallStudio\workspace) .

Step 3

To deploy CallStudio applications, change the default deployment location to a desired folder where the user has write privileges.

| Note | If you have uninstalled Call Studio application from the Program Files folder, ensure you also navigate to the system Environment Variables to locate and delete the path variable named CS_USER_HOME , as this step is crucial for completely removing all traces of the Call Studio application from your system. |
|---|---|

| Step 1 | Install the Call Studio installer file (setup.exe). Create the necessary folder structure and, during installation, change the default location from C:\Cisco\CallStudio to your desired folder location. For example: C:\Program Files\Cisco\CallStudio . |
|---|---|
| Step 2 | If Call Studio is installed in C:\Program Files\Cisco\CallStudio , it can be launched directly using the desktop shortcut. In case the Call Studio application is installed in any other location,
                                          create a shortcut for the startStudioUser.cmd file located in the %CallStudio% directory. Ensure that this shortcut for startStudioUser.cmd is available to users so they can easily launch Call Studio. |

| Step 1 | If Call Studio is installed in C:\Program Files\Cisco\CallStudio , it can be launched directly using the desktop shortcut. In case the Call Studio application is installed in any other location,
                                          Launch Call Studio using the startStudioUser.cmd shortcut provided by the administrator, or directly launch startStudioUser.cmd file located in the %CallStudio% directory. Ensure that this shortcut is available to users so they can easily launch Call Studio. |
|---|---|
| Step 2 | The following workspace folder is created and selected by default for users (%user_directory%\Cisco\CallStudio\workspace) . |
| Step 3 | To deploy CallStudio applications, change the default deployment location to a desired folder where the user has write privileges. |