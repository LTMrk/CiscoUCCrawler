---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-011011-htm-7b6ad283e9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_011011.html
retrieved_at: 2026-08-17T02:40:14.213332+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter:  Troubleshooting Web Inbox

## Chapter:  Troubleshooting Web Inbox

# Troubleshooting Web Inbox

Troubleshooting Web Inbox

## Introduction

The Web Inbox application provides access to voice messages and receipts stored on the Cisco Unity Connection server. The
                           Web Inbox enables users to play, compose, reply to or forward, and manage Unity Connection voice messages using a web browser.
                           It is installed on the Unity Connection server during installation.

Following are the tasks to troubleshoot problems with Web Inbox:

If there is an error message associated with the problem, review the “Web Inbox Error Messages” section on page 28-1 .

Review the “Adobe Flash Player Settings Dialog Box Unresponsive (Mac OS X with Firefox Only)” section on page 28-4 to consider the most common reasons why users cannot access the Web Inbox pages, including use of an incorrect URL, incorrect
                                 browser settings, or the presence of unsupported software installed on the workstation.

If the problem is that the Adobe Flash Player Settings dialog box appears but no options on the dialog box can be selected,
                                 see the “Adobe Flash Player Settings Dialog Box Unresponsive (Mac OS X with Firefox Only)” section on page 28-4 .

If the problem is that no messages are displayed in the Web Inbox, see the “Messages Not Displayed in Web Inbox” section on page 28-5 .

If the problem is that users do not see any sent items in the Sent Folder, see the “Sent Messages Not Displayed in Web Inbox” section on page 28-5 .

Confirm that the Tomcat service is running. See the “Verifying that Tomcat Service is Running” section on page 28-5 .

If the problem is that the Web Inbox does not get open in Internet Explorer 9 with Windows 7 64 bit, see the “Web Inbox Not Working with Internet Explorer 9 on Windows 7 64 bit” section on page 28-6 .

If you cannot resolve the problem and plan to report the problem to Cisco TAC, you are asked to provide information about
                           your system and about the problem.

Cisco Unity Connection uses Flash Player for recording voice messages through Web Inbox. However, Adobe has announced end
                                       of life for Flash Player. Hence Cisco Unity Connection Release 15 and later, replaces Flash Player with Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in Web Inbox.

For more information on updates of the Flash Player refer https://www.adobe.com/products/flashplayer/end-of-life.html

## Web Inbox Error Messages

In addition to browser error messages (such as “File not found” or “Unauthorized access”), users may see Web Inbox-specific
                              error messages, Flash plugin error messages, Quicktime plugin error messages, and Tomcat error messages when signing in to
                              or using the Web Inbox.

The four types of error messages that users may encounter are described in the following table:

Browser error messages

Browser error messages may indicate that the Web Inbox failed to install, the user does not have network access to the Unity
                                          Connection server, the browser is not configured correctly, or the user does not have the required security certificate installed
                                          (if the Web Inbox uses SSL connections).

Web Inbox-specific error messages

Web Inbox-specific error messages are displayed on the Sign-In page or another Web Inbox page, and typically indicate problems
                                          with user credentials or actions within the Web Inbox.

Quicktime Plugin error messages

Quicktime Plugin-specific error or warning messages are pop-up alerts that occur on pages that load the Quicktime plugin recording
                                          and playback controls. These messages typically appear the first time that the Quicktime plugin is loaded when you navigate
                                          to a page that contains the controls.

Tomcat error messages

Tomcat errors occur when there is a system error, such as file corruption or insufficient memory on the Unity Connection server.
                                          A Tomcat error message usually lists the sequence of application errors. Each exception is followed by a description of what
                                          the Tomcat service was attempting to do when the error occurred, and for some exceptions, a message explaining the error is
                                          also offered. The “Exception” and “Root Cause” sections in the error message may offer additional information about the problem.

See the following sections for information about these specific error messages.

### Error Message: “Sign-In Status – Account Has Been Locked.”

When users encounter the error message “Sign-in status – account has been locked,” it is possible that the user exceeded the
                              number of failed sign-in attempts that is allowed. (This limit is set on the System Settings > Authentication Rules page in
                              Cisco Unity Connection Administration.) It may also be possible that the user forgot his or her credentials, or an unauthorized
                              user attempted to gain access.

Use the following task list to determine the source of the problem and correct it.

To confirm that the account is locked, in Cisco Unity Connection Administration, go to the Users > Edit Password Settings
                                    page for the individual user, and select Web Application from the Choose Password menu. Under Web Applications Password Settings,
                                    you can verify the status of the user credentials to determine whether the password was locked by an administrator, there
                                    were failed sign-in attempts, or the password was locked after an excessive number of failed sign-in attempts.

To unlock the user account, in Cisco Unity Connection Administration, go to the Users > Edit Password Settings page for the
                                    individual user, and select Web Application from the Choose Password menu. Under Web Applications Password Settings, select
                                    Unlock Password.

### Error Message: “Apache Tomcat/<Version> – HTTP Status 500 – Internal Server Error.”

File corruption at the time of installation or a Tomcat memory corruption can cause users to encounter the error message “Apache
                              Tomcat/<version> – HTTP status 500 – internal server error.” To confirm that this is the cause of the problem, check the Tomcat
                              error page for the indicated root cause for the exception. If an exception message similar to the one below exists, there
                              is a file or memory corruption:

java.lang.ClassFormatError: <classpath>/<classname> (Illegal constant pool index)

Contact Cisco TAC.

### Error Message: “Site Is Unavailable.”

If users encounter the error message “Site is unavailable,” confirm that the Apache Tomcat service is running. See the “Verifying that Tomcat Service is Running” section on page 28-5 .

### Error Message:
                           	 "This User Account Does Not Have a Mailbox and Cannot Sign In to the Web Inbox.
                           	 To Use the Web Inbox, You Must Have an Account with a Mailbox."

If a user with valid credentials
                              		but who does not have an associated Unity Connection mailbox attempts to sign
                              		in to the Web Inbox, the user receives the error "This user account does not
                              		have a mailbox and cannot sign in to the Web Inbox. To use the Web Inbox, you
                              		must have an account with a mailbox."

To correct the problem, create an account with a mailbox for the user.
                              		As a best practice, we recommend that Unity Connection administrators do not
                              		use the same user account to sign in to Cisco Unity Connection Administration
                              		that they use to sign in to the Web Inbox to manage their own Unity Connection
                              		account.

### Error Message: “Error While Uploading Message to Server”

If a user sign in to a Web Inbox using Mozilla Firefox and sends a voice message by uploading the .wav file, an error message
                              “Error while uploading message to server” gets displayed on the Web Inbox, However, the recipient still receives the voice
                              message.

#### Removing the Error Message Displayed on the Web Inbox

### SUMMARY STEPS

- Uninstall the Mozilla Firefox browser.

- Clear your data from Mozilla Firefox:

- Reinstall the Mozilla Firefox browser again.

### DETAILED STEPS

Step 1

Uninstall the Mozilla Firefox browser.

Uninstalling the Firefox does not remove any user data, such as cache or history. To completely remove the user data, you
                                                            must manually delete the Firefox folder that contains the user profile.

Step 2

Clear your data from Mozilla Firefox:

Select the Windows Start button and enter %APPDATA% in the search field.

Press Enter to open the hidden Roaming folder. The Mozilla folder gets displayed.

Open the Mozilla folder and delete the Firefox folder to manually delete the user profile.

Step 3

Reinstall the Mozilla Firefox browser again.

### Error Message: "HTML5 audio compatible browser or QuickTime Plug-in
                           	 not found. Select Phone option to play the message. Install Quick time plugin
                           	 or open web inbox into firefox"

If a user sign in to a Web Inbox using Internet Explorer 11 Mozilla
                              		Firefox and sends a voice message by uploading the.wav file, an error message
                              		"Error while uploading message to server" gets displayed on the Web Inbox,
                              		However, the recipient still receives the voice message.

## Send Option is
                        	 Disabled on MAC Operating System

On MAC operating system, if the Send option on Safari is not working
                              		  after uploading voice message, make sure that the most recent version of Flash
                              		  Player is installed on your machine. If the latest version of Flash Player is
                              		  installed on your system but still the Send option is not working, do the
                              		  following to resolve the issue:

Step 1

Navigate to Safari > Preferences and select Security tab.

Step 2

Check the Allow Plug-ins
                                       			 check box on the Security tab.

Step 3

Click Website Settings.

Step 4

In Configured Websites, select Allow Always for the Unity
                                       			 Connection server.

## Adobe Flash Player Settings Dialog Box Unresponsive (Mac OS X with Firefox Only)

When a user presses the record button to compose a message for the first time in the Web Inbox, an Adobe Flash Player Settings
                           dialog box is displayed, asking the user whether to allow the Web Inbox to access the microphone. In some cases, users who
                           see this dialog box are unable to select any of the options in the dialog box, and are therefore unable to record audio for
                           the message. To change the global Flash Player privacy settings so that the dialog box does not appear, do the following procedure.

In order to perform this procedure, the user must have access to the Internet to reach the Adobe Macromedia web site.

### Changing Global
                           	 Flash Player Privacy Settings to Allow the Web Inbox to Access the Computer
                           	 Microphone

Step 1

In the web browser that you use to access the Web Inbox,
                                          			 navigate to the Website Privacy Settings panel of the Adobe Flash Player
                                          			 Settings Manager at http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager06.html .

Step 2

In the Adobe Flash Player Settings Manager Website Privacy
                                          			 Settings panel, in the Visited Websites table, locate and select the website
                                          			 corresponding to the Web Inbox.

Step 3

While the Web Inbox site is selected, select Always Allow as the privacy setting. When this
                                          			 change is made, Web Inbox can access the computer microphone without prompting
                                          			 the user for permission.

## Messages Not Displayed in Web Inbox

If the Web Inbox does not display any messages for a user even though the user has messages in the folder being displayed,
                           clear the browser cache. (Refer to the browser documentation for instructions on how to clear the cache.)

## Sent Messages Not Displayed in Web Inbox

In order for sent messages to be available to users in the Sent folder in the Web Inbox, the Sent Messages feature must be
                           enabled. By default, the feature is not enabled. To enable the feature, change the Sent Messages: Retention Period (in Days)
                           setting on the System Settings > Advanced > Messaging page in Cisco Unity Connection Administration to a value greater than
                           zero. Note that because sent messages count toward user mailbox quotas, configuring a high value for this setting can cause
                           user mailboxes to fill with sent messages if users do not regularly manage them from the Web Inbox.

## Verifying that Tomcat Service is Running

Do the following tasks to confirm that the Tomcat service is running in Unity Connection and if necessary, to restart the
                           Tomcat service:

Confirm that the Tomcat service is running using either Real-Time Monitoring Tool (RTMT) or the Command Line Interface (CLI).
                                 Do the applicable procedure:

Confirming that the Tomcat Service is Running Using Real-Time Monitoring Tool (RTMT), page 28-5

Confirming that the Tomcat Service is Running Using the Command Line Interface (CLI), page 28-6

If necessary, restart the Tomcat service using the Command Line Interface (CLI). See the “Restarting the Tomcat Service Using the Command Line Interface (CLI)” procedure on page 28-6 .

### Confirming that
                           	 the Tomcat Service is Running Using Real-Time Monitoring Tool (RTMT)

Step 1

Launch Real-Time Monitoring Tool (RTMT).

For details on using RTMT, see the applicable Cisco Unified Real Time Monitoring Tool Administration Guide available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 2

On the System menu, select Server > Critical
                                                				  Services .

Step 3

On the System tab, locate Cisco Tomcat and view its status. The
                                          			 status is indicated by an icon.

### Confirming that
                           	 the Tomcat Service is Running Using the Command Line Interface (CLI)

Step 1

Use the Command Line Interface (CLI) command utils service list to list all of the services.

For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 2

Scan the CLI output for the Cisco Tomcat service and confirm
                                          			 that its status is Started .

### Restarting the
                           	 Tomcat Service Using the Command Line Interface (CLI)

To restart the Cisco Tomcat service, use the CLI command utils service restart Cisco Tomcat .

For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Web Inbox Not Working with Internet Explorer 9 on Windows 7 64 bit

If the Web Inbox is not working with Internet Explorer 9 on Windows 7 64 bit, make sure that the Media Feature Pack is installed
                           in your system.

| Note | Cisco Unity Connection uses Flash Player for recording voice messages through Web Inbox. However, Adobe has announced end
                                       of life for Flash Player. Hence Cisco Unity Connection Release 15 and later, replaces Flash Player with Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in Web Inbox. For more information on updates of the Flash Player refer https://www.adobe.com/products/flashplayer/end-of-life.html |
|---|---|

| Browser error messages | Browser error messages may indicate that the Web Inbox failed to install, the user does not have network access to the Unity
                                          Connection server, the browser is not configured correctly, or the user does not have the required security certificate installed
                                          (if the Web Inbox uses SSL connections). |
|---|---|
| Web Inbox-specific error messages | Web Inbox-specific error messages are displayed on the Sign-In page or another Web Inbox page, and typically indicate problems
                                          with user credentials or actions within the Web Inbox. |
| Quicktime Plugin error messages | Quicktime Plugin-specific error or warning messages are pop-up alerts that occur on pages that load the Quicktime plugin recording
                                          and playback controls. These messages typically appear the first time that the Quicktime plugin is loaded when you navigate
                                          to a page that contains the controls. |
| Tomcat error messages | Tomcat errors occur when there is a system error, such as file corruption or insufficient memory on the Unity Connection server.
                                          A Tomcat error message usually lists the sequence of application errors. Each exception is followed by a description of what
                                          the Tomcat service was attempting to do when the error occurred, and for some exceptions, a message explaining the error is
                                          also offered. The “Exception” and “Root Cause” sections in the error message may offer additional information about the problem. |

| Step 1 | Uninstall the Mozilla Firefox browser. Note Uninstalling the Firefox does not remove any user data, such as cache or history. To completely remove the user data, you
                                                            must manually delete the Firefox folder that contains the user profile. | Note | Uninstalling the Firefox does not remove any user data, such as cache or history. To completely remove the user data, you
                                                            must manually delete the Firefox folder that contains the user profile. |
|---|---|---|---|
| Note | Uninstalling the Firefox does not remove any user data, such as cache or history. To completely remove the user data, you
                                                            must manually delete the Firefox folder that contains the user profile. |
| Step 2 | Clear your data from Mozilla Firefox: Select the Windows Start button and enter %APPDATA% in the search field. Press Enter to open the hidden Roaming folder. The Mozilla folder gets displayed. Open the Mozilla folder and delete the Firefox folder to manually delete the user profile. |
| Step 3 | Reinstall the Mozilla Firefox browser again. |

| Note | Uninstalling the Firefox does not remove any user data, such as cache or history. To completely remove the user data, you
                                                            must manually delete the Firefox folder that contains the user profile. |
|---|---|

| Step 1 | Navigate to Safari > Preferences and select Security tab. |
|---|---|
| Step 2 | Check the Allow Plug-ins
                                       			 check box on the Security tab. |
| Step 3 | Click Website Settings. |
| Step 4 | In Configured Websites, select Allow Always for the Unity
                                       			 Connection server. |

| Note | In order to perform this procedure, the user must have access to the Internet to reach the Adobe Macromedia web site. |
|---|---|

| Step 1 | In the web browser that you use to access the Web Inbox,
                                          			 navigate to the Website Privacy Settings panel of the Adobe Flash Player
                                          			 Settings Manager at http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager06.html . |
|---|---|
| Step 2 | In the Adobe Flash Player Settings Manager Website Privacy
                                          			 Settings panel, in the Visited Websites table, locate and select the website
                                          			 corresponding to the Web Inbox. |
| Step 3 | While the Web Inbox site is selected, select Always Allow as the privacy setting. When this
                                          			 change is made, Web Inbox can access the computer microphone without prompting
                                          			 the user for permission. |

| Step 1 | Launch Real-Time Monitoring Tool (RTMT). Note For details on using RTMT, see the applicable Cisco Unified Real Time Monitoring Tool Administration Guide available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | For details on using RTMT, see the applicable Cisco Unified Real Time Monitoring Tool Administration Guide available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|---|---|
| Note | For details on using RTMT, see the applicable Cisco Unified Real Time Monitoring Tool Administration Guide available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 2 | On the System menu, select Server > Critical
                                                				  Services . |
| Step 3 | On the System tab, locate Cisco Tomcat and view its status. The
                                          			 status is indicated by an icon. |

| Note | For details on using RTMT, see the applicable Cisco Unified Real Time Monitoring Tool Administration Guide available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | Use the Command Line Interface (CLI) command utils service list to list all of the services. Note For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|---|---|
| Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 2 | Scan the CLI output for the Cisco Tomcat service and confirm
                                          			 that its status is Started . |

| Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| To restart the Cisco Tomcat service, use the CLI command utils service restart Cisco Tomcat . Note For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|---|
| Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |

| Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|