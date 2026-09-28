---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-011100-htm-169d770fb4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_011100.html
retrieved_at: 2026-08-17T02:18:27.022900+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting
	 the HTML Notifications

## Chapter: Troubleshooting
	 the HTML Notifications

# Troubleshooting
                     	 the HTML Notifications

Cisco Unity
                        		Connection allows you to deliver the SMTP-based HTML notifications for a new
                        		voice message to the end users. These notifications can be sent as an HTML
                        		format embedded in the email via SMTP. The users get the flexibility to receive
                        		the HTML notifications that can include customized icons, header, and footer
                        		along with the link to access Mini Web Inbox. Mini Web Inbox is a player that
                        		allows user to play the voice messages over computer or mobile devices.

Ensure that you have taken care of all the requirements and checklist while creating the HTML templates. For more information
                        on the checklist while creating and rendering a template, see the "Configuring User Templates" section of the "User Attributes"
                        chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html

For more information on 'Must Haves' for Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox (Release 14) , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/quick_start/guide/b_14cucqsginbox.html .

## HTML Notifications
                        	 Not Received By the Users

If the users are not
                           		receiving the HTML notifications, ensure the following steps:

Confirm that the smart host hostname is configured from Cisco Unity Connection Administration. For more information, see the
                                 "Integrated Messaging" section of the "Messaging" chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

- Ping the smart host from
                              		  Unity Connection server. If the ping fails, there is a possibility that network
                              		  Unity Connection is not functional and you must restore the network Unity
                              		  Connection.

- Confirm that the 'Unity
                              		  Connection Notifier' service is up and running.

- Confirm that the HTML notification device is enabled. For more information on how to setup the HTML notification device, see
                              the "Notifications" chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

- Confirm that a valid email address is specified while configuring HTML notifications for a user. For more information on how
                              to setup the HTML notification device, see the "Notifications" chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

## Images Not
                        	 Displayed on Microsoft Outlook

If the user is using
                           		Microsoft Outlook client for checking the email notifications and is unable to
                           		view the images in the notification, do the following steps:

- If the images are not
                              		  displayed, right click the image and select the Show Images options.

- Make sure the minimum requirements for images to be displayed on Microsoft Outlook are met. To check the settings for Microsoft
                              Outlook, see the " Configuring Microsoft Outlook to Display Images in an HTML Message Notification " section of the "Configuring an Email Account to Access Unity Connection Voice Messages" chapter of the User Workstation Setup Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user_setup/guide/b_14cucuwsx.html

- If the authentication mode
                              		  is selected, then make sure you are giving the correct credentials.

- If the user enters wrong
                              		  password thrice continuously then Unity Connection does not prompt the user
                              		  again and the user must restart the Outlook. To enter the credentials and
                              		  display the images in the notification you must restart the Outlook.

- When prompted for
                              		  credentials at the first instance, if the user clicks on the Cancel button and
                              		  does not enter Unity Connection credentials then no image is displayed in the
                              		  email notification. You must restart the Outlook to enter the Unity Connection
                              		  credential and view the images.

1. Check the
                                 			 version of MSO.DLL from the path C:\Program Files\Common Files\Microsoft
                                 			 Shared\MSORUN on the Windows machine. Ensure that the version of MSO must
                                 			 include the fix. For more information on version, see the Outlook 2007 and Outlook 2010 hotfix.

2. After
                                 			 restarting Outlook, you must ensure that it is no longer running by ending any
                                 			 running process of Outlook.exe from the Task Manager window. The changes to
                                 			 MSO.DLL take affect only after proper shutdown and restart of the Outlook.

- Make sure that the registry
                              		  entry for AllowImageProxyAuth was made for DWORD only.

- If the user is not able to
                              		  see any images even after all the recommended settings, check the network
                              		  connectivity of the Unity Connection Server with Internet Explorer by copying
                              		  the link of the images and manually opening it over the browser. You can check
                              		  the connectivity via wireshark captures and filtering over SSL packet flow over
                              		  443 or 8443 port for the communication.

## Images Not
                        	 Displayed on IBM Lotus Notes

If the user is using
                           		IBM Lotus Notes for checking the email notification and unable to view the
                           		images, do the following steps

- If the images are not
                              		  displayed, right click the image and select show images options.

- If the authentication mode is selected, then make sure you are giving the correct credentials. For more information on how
                              to select the authentication mode, see the "Configuring the Authentication Mode" section of the "Configuring an Email Account
                              to Access Cisco Unity Connection Voice Messages" chapter of the User Workstation Setup Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user_setup/guide/b_14cucuwsx.html

## Hyperlinks Not
                        	 Visible in the Email Notification

If the hyperlinks
                           		given in the notification template are not visible in the notification, then
                           		you need to make sure that the HTML notification template in Cisco Unity
                           		Connection Administration has the valid HTML tags and all items (static,
                           		action, and status items) are given correctly.

For more information on how to define the tags and the items, see the "Configuring Notification Templates" section of the
                           "Notifications" chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

## Unable to Launch
                        	 Mini Web Inbox

If the user is unable to launch the
                           		Mini Web Inbox, ensure the following settings:

- Confirm that under COS assigned to the
                              		  user, Web Inbox is enabled.

- Confirm that the message for
                              		  which you are opening the Unity Connection Mini Web Inbox is not deleted.

- Confirm that the user is
                              		  logged in with the valid user name.

## Unable to View the
                        	 Updated Mini Web Inbox Interface in Internet Explorer

To View the Updated Interface of
                              		  Unity Connection Mini Web Inbox

Step 1

Open Internet Explorer and
                                       			 then go to Tools.

Step 2

In the Internet Options
                                       			 window under the Browsing History section, click Settings.

Step 3

In the Temporary Internet
                                       			 Files and History Settings window, select the Every time I visit the webpage
                                       			 option to check the newer version of stored pages option.

Step 4

Click Ok.

## Unable to Play and
                        	 Record Voice Messages on Computer Using Mini Web Inbox

If the user is
                           		unable to play and record voice messages on computer using Unity Connection
                           		Mini Web Inbox, confirm the following:

Confirm that the outdial number is configured. For more information on how to setup the outdial number and other fields for
                                 the HTML notification device, see the "Configuring Notification Devices" section of the "Notifications" chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

- Confirm that the callback
                              		  number is configured.

- Confirm that the end user
                              		  answers the phone.

| Note | It is
                                 		recommended, that the Mini Web Inbox must always be opened from the
                                 		notification email as it requires certain URL parameters. |
|---|---|

| Step 1 | Open Internet Explorer and
                                       			 then go to Tools. |
|---|---|
| Step 2 | In the Internet Options
                                       			 window under the Browsing History section, click Settings. |
| Step 3 | In the Temporary Internet
                                       			 Files and History Settings window, select the Every time I visit the webpage
                                       			 option to check the newer version of stored pages option. |
| Step 4 | Click Ok. |