---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-serv-administration-b-12xcucservag-b-12xcucservag-chapter-00--a47cac48d0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag/b_12xcucservag_chapter_00.html
retrieved_at: 2026-08-21T00:22:17.091358+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 12.x

# Administration Guide for Cisco Unity Connection Serviceability Release 12.x

Updated: August 4, 2017

Chapter: Introduction to
	 Cisco Unity Connection Serviceability

## Chapter: Introduction to
	 Cisco Unity Connection Serviceability

# Introduction to
                     	 Cisco Unity Connection Serviceability

Introduction to Cisco Unity Connection Serviceability

## Understanding
                        	 Cisco Unity Connection Serviceability

Cisco Unity Connection Serviceability, a
                           		web-based troubleshooting tool for Unity Connection, provides the following
                           		functionality:

Displaying Unity Connection alarm definitions that you can use
                                 			 for troubleshooting.

Enabling Unity Connection traces. You can collect and view trace
                                 			 information in the Real-Time Monitoring Tool (RTMT).

Configuring the logs to which Unity Connection trace information
                                 			 is saved.

Managing a cluster and the servers, if a Unity Connection
                                 			 cluster is configured.

The Unity Connection cluster feature is not supported for use
                                             				with Cisco Business Edition.

Viewing the status of the Unity Connection feature services.

Activating, deactivating, starting, and stopping the Unity
                                 			 Connection services.

Generating reports that can be viewed in different file formats.

Depending on the service and component involved, you may perform
                           		serviceability-related tasks in both Cisco Unity Connection Serviceability and
                           		Cisco Unified Serviceability. For example, you may need to start and stop
                           		services, view alarms, and configure traces in both applications to
                           		troubleshoot a problem.

Cisco Unity Connection Serviceability supports the functionality
                           		that is described in the Administration Guide for Cisco Unity Connection
                           		Serviceability. For information on using Cisco Unified Serviceability, see the
                           		Cisco Unified Serviceability Administration Guide, Release 12.x, available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Configuring Browsers on Administrator Workstations

To access Cisco Unity Connection Serviceability, Cisco Unity Connection Administration, Cisco Unified Serviceability, Disaster
                           Recovery System, and other web applications on the Unity Connection or Cisco Business Edition server, the browser(s) must
                           be set up correctly on an administrator workstation.

### Firefox

Do the following tasks to set up Firefox
                                 		  for accessing the Unity Connection web applications.

Confirm that the software required for correct browser
                                          			 configuration is installed. See the "Software
                                             				Requirements-Administrator Workstations" section of the System
                                          			 Requirements for Cisco Unity Connection Release 12.x ,
                                          			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

Configure Firefox:

Enable Java.

Enable Java Script > Enable Change Images in Java Script
                                             				Advanced.

Allow sites to set cookies. (For security purposes, we recommend
                                             				that you set this to Allow Sites to Set Cookies for the Originating Website
                                             				Only.)

### Microsoft Internet
                           	 Explorer

Do the following tasks to
                                 		  set up Internet Explorer for accessing the Unity Connection web applications.

Confirm that the software required for correct browser
                                          			 configuration is installed. See the "Software
                                             				Requirements-Administrator Workstations" “Software
                                             				Requirements—Administrator Workstations” section of the System
                                          			 Requirements for Cisco Unity Connection Release 12.x ,
                                          			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

Configure Internet Explorer:

Enable Active scripting.

Download and run ActiveX controls.

Enable Java scripting.

Accept all cookies.

Automatically check for newer versions of temporary Internet
                                             				files.

Enable Medium-High privacy.

If you are running Microsoft Windows Server 2003 and using
                                             				Internet Explorer version 6.0 to access the Cisco Personal Communications
                                             				Assistant, add the Unity Connection server to the Trusted Sites list by doing
                                             				the following procedure

### Adding the Unity Connection or Cisco Business Edition Server to the
                           	 List of Trusted Sites (Windows Server 2003 with Internet Explorer 6.0
                           	 Only)

Open the Cisco Personal Communications
                                          			 Assistant Sign-In page.

On the Internet Explorer File menu, select Add This Site To > Trusted Sites Zone .

In the Trusted Sites dialog box, select Add .

Select Close to close the
                                          			 Trusted Sites dialog box.

Restart Internet Explorer.

## Accessing Cisco Unity Connection Serviceability

The first time that you sign
                              		  in to Cisco Unity Connection Serviceability, you use the username and password
                              		  for the default administrator account that the installer specified for the
                              		  account during installation. Later, you can use the username and password for
                              		  any additional administrator accounts that you create.

Using a supported web browser, open a
                                       			 browser session.

Go to https://<Cisco Unity Connection
                                             				  server IP address > /cuservice .

Enter an applicable username and password,
                                       			 and select Login .

After you have logged on to Cisco Unity
                                          				Connection Serviceability, you can access all applications that appear in the
                                          				Navigation drop-down box except for Cisco Unified Operating System
                                          				Administration and Disaster Recovery System without having to sign in to each
                                          				application.

You cannot access Cisco Unified Operating
                                          				System Administration or Disaster Recovery System using the Cisco Unity
                                          				Connection Serviceability username and password. To access these applications
                                          				from Cisco Unity Connection Serviceability, you must select the Logout link in
                                          				the upper-right corner of Cisco Unity Connection Serviceability, then select
                                          				the application from the Navigation drop-down box and select Go.

If you have already logged on to one of the
                                          				applications that display in the Navigation drop-down box (not Cisco Unified
                                          				Operating System Administration or Disaster Recovery System), you can access
                                          				Cisco Unity Connection Serviceability without logging in. From the Navigation
                                          				drop-down box, select Cisco Unity Connection Serviceability and select Go.

## Using Cisco Unity Connection Serviceability Interface

In addition to troubleshooting, generating reports, and doing service-related tasks in Cisco Unity Connection Serviceability,
                           you can do the following tasks:

To display documentation for a single window, select Help > This Page.

To display a list of documents that are available with this release of Unity Connection or Cisco Business Edition (or to access
                                 the Help index), select Help > Contents.

To verify the version of Cisco Unity Connection Serviceability running on the server, select Help > About or select the About
                                 link in the upper-right corner of the window.

To go directly to the home page in Cisco Unity Connection Serviceability from a configuration window, select Cisco Unity Connection
                                 Serviceability from the Navigation drop-down box.

To access Cisco Unity Connection Administration or other applications, select the applicable application from the Navigation
                                 drop-down box and select Go.

To sign out of Cisco Unity Connection Serviceability, select the Logout link in the upper-right corner of the window.

On each Cisco Unity Connection Serviceability configuration page, configuration icons appear that correspond to the configuration
                                 buttons at the bottom of the page. (For example, you can select either the Save icon or the Save button to complete the task.)

| Note | The Unity Connection cluster feature is not supported for use
                                             				with Cisco Business Edition. |
|---|---|

| Step 1 | Confirm that the software required for correct browser
                                          			 configuration is installed. See the "Software
                                             				Requirements-Administrator Workstations" section of the System
                                          			 Requirements for Cisco Unity Connection Release 12.x ,
                                          			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html . |
|---|---|
| Step 2 | Configure Firefox: Enable Java. Enable Java Script > Enable Change Images in Java Script
                                             				Advanced. Allow sites to set cookies. (For security purposes, we recommend
                                             				that you set this to Allow Sites to Set Cookies for the Originating Website
                                             				Only.) |

| Step 1 | Confirm that the software required for correct browser
                                          			 configuration is installed. See the "Software
                                             				Requirements-Administrator Workstations" “Software
                                             				Requirements—Administrator Workstations” section of the System
                                          			 Requirements for Cisco Unity Connection Release 12.x ,
                                          			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html . |
|---|---|
| Step 2 | Configure Internet Explorer: Enable Active scripting. Download and run ActiveX controls. Enable Java scripting. Accept all cookies. Automatically check for newer versions of temporary Internet
                                             				files. Enable Medium-High privacy. If you are running Microsoft Windows Server 2003 and using
                                             				Internet Explorer version 6.0 to access the Cisco Personal Communications
                                             				Assistant, add the Unity Connection server to the Trusted Sites list by doing
                                             				the following procedure |

| Step 1 | Open the Cisco Personal Communications
                                          			 Assistant Sign-In page. |
|---|---|
| Step 2 | On the Internet Explorer File menu, select Add This Site To > Trusted Sites Zone . |
| Step 3 | In the Trusted Sites dialog box, select Add . |
| Step 4 | Select Close to close the
                                          			 Trusted Sites dialog box. |
| Step 5 | Restart Internet Explorer. |

| Step 1 | Using a supported web browser, open a
                                       			 browser session. |
|---|---|
| Step 2 | Go to https://<Cisco Unity Connection
                                             				  server IP address > /cuservice . |
| Step 3 | Enter an applicable username and password,
                                       			 and select Login . After you have logged on to Cisco Unity
                                          				Connection Serviceability, you can access all applications that appear in the
                                          				Navigation drop-down box except for Cisco Unified Operating System
                                          				Administration and Disaster Recovery System without having to sign in to each
                                          				application. You cannot access Cisco Unified Operating
                                          				System Administration or Disaster Recovery System using the Cisco Unity
                                          				Connection Serviceability username and password. To access these applications
                                          				from Cisco Unity Connection Serviceability, you must select the Logout link in
                                          				the upper-right corner of Cisco Unity Connection Serviceability, then select
                                          				the application from the Navigation drop-down box and select Go. If you have already logged on to one of the
                                          				applications that display in the Navigation drop-down box (not Cisco Unified
                                          				Operating System Administration or Disaster Recovery System), you can access
                                          				Cisco Unity Connection Serviceability without logging in. From the Navigation
                                          				drop-down box, select Cisco Unity Connection Serviceability and select Go. |