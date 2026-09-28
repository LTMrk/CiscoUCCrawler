---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-user-guide-email-b-12xcucugemail-b-12xcucugemail-chapter-0101-025b2044d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/email/b_12xcucugemail/b_12xcucugemail_chapter_0101.html
retrieved_at: 2026-08-21T07:57:00.194474+00:00
---

User Guide for Accessing Cisco Unity Connection Voice Messages in an Email Application (Release 12.x)

# User Guide for Accessing Cisco Unity Connection Voice Messages in an Email Application (Release 12.x)

Updated: August 17, 2017

Chapter: Managing
	 HTML-based Message Notification

## Chapter: Managing
	 HTML-based Message Notification

# Managing
                     	 HTML-based Message Notification

Cisco Unity Connection can be configured to send SMTP-based
                        		message notifications in the form of HTML to email addresses. All SMTP-based
                        		HTML notifications in Unity Connection require HTML-based notification
                        		templates. HTML-based templates can be selected and applied by the
                        		administrator to allow HTML notification for a device. The template selected
                        		can either be a default or custom template that the administrator has created.

For more information on how to create a template, refer to the System
                           		  Administration Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

To get the HTML notifications exactly as per the template
                        		defined by the administrator, the user’s email client must support the display
                        		of images and icons. For more information on this, refer to documentation of
                        		your email service provider.

HTML notifications are supported with the following email
                        		clients:

Microsoft Outlook 2010

Microsoft Outlook 2013

IBM Lotus Notes

Gmail (Web based access only)

The administrator selects the authentication or
                        		non-authentication mode as desired. In addition, make sure the signed SSL
                        		certificates are installed in order to access the voice message via Unity
                        		Connection Mini Web Inbox. See the Securing Cisco Unity Connection
                        		Administration, Cisco PCA, and IMAP Email Client Access to Unity Connection
                        		12.x section.

For more information on how to configure SSL on Unity
                        		Connection, refer to the System
                           		  Administration Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

## Configuring the Authentication Mode

The authentication mode allows the embedded images or icons to be displayed in the SMTP-based HTML notification using the
                           Unity Connection credentials. After the credentials get authenticated the images are displayed.

To know which mode is configured for you, contact your System Administrator.

By default, the system is configured for the authentication mode. The administrator can configure the authentication mode
                           using the Cisco Unity Connection Administration.

### Configuring the
                           	 Authentication Mode

In Cisco Unity Connection Administration, select System Settings
                                          			 > General Configuration.

On the Edit General Configuration page, select the Authenticate
                                          			 Graphics for HTML Notification option to turn on the authentication mode.

Click Save.

- The Unity Connection
                                                            					 credentials are required only once for each session of Outlook.

If the user clicks on the Cancel button and does not enter Unity
                                                               						Connection credentials when prompted at the first instance then no image will
                                                               						be displayed in the email notification. You must restart Outlook to enter the
                                                               						Unity Connection credentials and view the images.

If the user enters wrong password thrice then Unity Connection
                                                               						will not prompt again and the user must restart Outlook.

## Configuring the Non-Authentication Mode

The non-authentication mode does not prompt user for credentials and the embedded images or icons are displayed in the email
                           notification of its own. Make sure to confirm the mode configured for you from your System Administrator.

## Configuring
                        	 Microsoft Outlook to Display Images in an HTML Message Notification

In the authentication mode, to view all the custom graphics or
                              		  administrative replaceable images as per the HTML-based template, you must make
                              		  sure that your Outlook client has all the required hotfixes and registry
                              		  entries.

If the non-authentication mode is configured then your Outlook
                              		  client does not require any hotfixes or registry entries.

The user workstation must have the SSL certificates installed
                                          			 irrespective of the mode selected (authentication or non-authentication) by the
                                          			 administrator.

If you are using Internet Explorer version 8, refer to the
                              		  settings given in the Configuring Internet Explorer 8 for Unity Connection Mini
                              		  Web Inbox section.

Microsoft Outlook Version

Microsoft Outlook 2007

Microsoft Outlook 2010

Windows XP SP3, Windows 7 (32 and 64 bit), and Windows Vista (32
                                          						and 64 bit)

Outlook 2007

Registry entry for
                                                      								  AllowImageProxyAuth, where value=1.

Either Install 2007 Office
                                                      								  suite SP2. To install 2007 Office suite SP2, refer to http://support.microsoft.com/kb/953195 .
                                                      								  Then, install Outlook 2007 hotfix package. To install hotfix, refer to http://support.microsoft.com/kb/2596993 .
                                                      								  OR

Install 2007 Office suite
                                                      								  SP3. To install 2007 Office suite SP3, refer to http://support.microsoft.com/kb/2526086 .

Outlook 2007 with SP2

Install Outlook 2007 hotfix
                                                      								  package. To install hotfix, refer to http://support.microsoft.com/kb/2596993 .

Registry entry for
                                                      								  AllowImageProxyAuth, where value=1.

Outlook 2007 with SP3

Registry entry for
                                                      								  AllowImageProxyAuth, where value=1.

Install Outlook 2010 hotfix
                                                							 package. For more information, refer to http://support.microsoft.com/kb/2459116 .

Registry entry for
                                                							 AllowImageProxyAuth, where value=1.

### Creating the
                           	 registry entries for Microsoft Outlook

Go to Start > Run . Type regedit and press Enter .

Browse to the following path for Microsoft Outlook 2007:

Browse to the following path for Microsoft Outlook 2010:

Add “AllowImageProxyAuth = 1” as new DWORD value.

## Configuring Microsoft Outlook for Automatic Image Download

Even after updating your Microsoft Outlook with required hotfixes and registry entries, you need to right click on the image,
                           if any given in the template and select Show images. You can also right click on the prompt appearing at the above of message
                           window to show the images.

To download your images automatically without performing these steps with every session, you must select the required options
                           given under the Tools > Trust Center > Automatic Download section in your Outlook email client.

## Configuring Unity Connection to Send Voice Message as an Attachment

Starting with Unity Connection 10.0(1) release, the administrator can now configure Connection to send the voice message as
                           an attachment in the HTML notification to the user. Along with the link to access Connection Mini Web Inbox through the HTML
                           notification email, the user can now access the voice message attachment in the .wav format that can be played on PC or mobile
                           using any player. Prior to Unity Connection 10.0(1) version, the end user received only a link in the HTML notifications to
                           access Unity Connection Mini Web Inbox and listen to voice messages through Mini Web Inbox only.

In case of forwarded messages, the attachment is sent only for the latest voice message.

If a user tries to access the voice message attachment using mobile, the following mobile clients are

supported:

Supported versions of iPhone 4 and 4s

Supported versions of Android

The secure and private voice messages cannot be sent as an attachment.

By default, the system is configured for not to send the voice message as an attachment. The

administrator can configure to send voice message as an attachment using the Cisco Unity Connection Administration.

### Configuring Unity
                           	 Connection to Send Voice Message as an Attachment

In Cisco Unity Connection Administration, select Advanced >
                                          			 Messaging.

On the Messaging Configuration page, select the Allow voice mail
                                          			 as attachments to HTML notifications option to send the voice message as an
                                          			 attachment.

## Configuring the Size of Voice Messages Sent as an Attachment with HTML Notification

The administrator can configure the size of voice messages sent as an attachment with HTML notifications. The user can now
                           access the voice message attachment in the .wav format that can be played on PC or mobile using any player.

By default, the system is configured to send the voice message as an attachment upto 2048KB and maximum size can be 12288
                           KB. The administrator can configure the size of the voice message using the Cisco Unity Connection Administration.

### Configuring the
                           	 Size of Voice Message Sent as an Attachment

In Cisco Unity Connection Administration, select Advanced >
                                          			 Messaging.

On the Messaging Configuration page, enter the size of voice
                                          			 message in the Max size of voice mail as attachment to HTML notifications (KB)
                                          			 text box.

Click Save. Make sure to restart the Connection Notifier service
                                          			 for changes to take effect.

Configuring Unity Connection for Mini Web Inbox

## Configuring IBM Lotus Notes for Unity Connection Mini Web Inbox

Unity Connection Mini Inbox does not support the default IBM Lotus Notes supported browser. When a user receives a message
                           notification on his or her IBM Lotus Notes email client and clicks a link in the notification to open Connection Mini Inbox,
                           the Connection Mini Web Inbox must open in the default operating system browser.

### Configuring the
                           	 Web Browser as Operating System Default Browser in Lotus Notes Email
                           	 Client

In your Lotus Notes client, select File > Preferences >
                                          			 Web Browser.

Select the Use the browser I have set as the default for this
                                          			 operating system option.

Click Apply and then Ok.

## Configuring
                        	 Internet Explorer 8 for Unity Connection Mini Web Inbox

In your browser window, go to Tools > Intranet Options and
                                       			 select the Security tab.

Select the Local intranet option and click Sites.

Uncheck all the check boxes and click Ok.

Select the Trusted sites option and click Sites.

Add the website that you are using for Connection, for example,
                                       			 https://ucbu-cisco-vmxyz.cisco.com.

Click Close and then Ok.

## Configuring
                        	 Windows Vista and Windows 7 (32 bit and 64 bit) for Unity Connection Mini Web
                        	 Inbox

Select Start > Control Panel > Flash Player.

In the Flash Player Settings Manager window, select the Camera
                                       			 and Mic tab.

Click Camera and Microphone Settings by Site.

In the Camera and Microphone Settings by Site window, select the
                                       			 Ask me when a site wants to use the camera or microphone option.

Then, click Add.

Add the website that you are using for Unity Connection, for
                                       			 example, ucbu-cisco-vmxyz.cisco.com.

Click Allow and then Close.

## Configuring Gmail
                        	 to Display Images in an HTML Message Notification

If you have configured Gmail as your HTML notification device,
                           		then to view all the custom graphics or images into notification emails make
                           		sure that you login to the Gmail account as an administrator.

After login to Gmail admin account, you have to configure the
                           		image URL proxy whitelist settings. Below are the steps for the same:

Login to Google Admin Account.

Go to
                                    				Apps > Google Apps > Gmail > Advanced settings

In Advanced settings go to Organizations section.

Select the domain.

Go to Image URL proxy whitelist section.

Enter the patterns for image URL proxy whitelist (matching URLs
                                 			 will bypass image proxy protection).

Click Save.

| Step 1 | In Cisco Unity Connection Administration, select System Settings
                                          			 > General Configuration. |
|---|---|
| Step 2 | On the Edit General Configuration page, select the Authenticate
                                          			 Graphics for HTML Notification option to turn on the authentication mode. |
| Step 3 | Click Save. Note The Unity Connection
                                                            					 credentials are required only once for each session of Outlook. If the user clicks on the Cancel button and does not enter Unity
                                                               						Connection credentials when prompted at the first instance then no image will
                                                               						be displayed in the email notification. You must restart Outlook to enter the
                                                               						Unity Connection credentials and view the images. If the user enters wrong password thrice then Unity Connection
                                                               						will not prompt again and the user must restart Outlook. | Note | The Unity Connection
                                                            					 credentials are required only once for each session of Outlook. If the user clicks on the Cancel button and does not enter Unity
                                                               						Connection credentials when prompted at the first instance then no image will
                                                               						be displayed in the email notification. You must restart Outlook to enter the
                                                               						Unity Connection credentials and view the images. If the user enters wrong password thrice then Unity Connection
                                                               						will not prompt again and the user must restart Outlook. |
| Note | The Unity Connection
                                                            					 credentials are required only once for each session of Outlook. If the user clicks on the Cancel button and does not enter Unity
                                                               						Connection credentials when prompted at the first instance then no image will
                                                               						be displayed in the email notification. You must restart Outlook to enter the
                                                               						Unity Connection credentials and view the images. If the user enters wrong password thrice then Unity Connection
                                                               						will not prompt again and the user must restart Outlook. |

| Note | The Unity Connection
                                                            					 credentials are required only once for each session of Outlook. If the user clicks on the Cancel button and does not enter Unity
                                                               						Connection credentials when prompted at the first instance then no image will
                                                               						be displayed in the email notification. You must restart Outlook to enter the
                                                               						Unity Connection credentials and view the images. If the user enters wrong password thrice then Unity Connection
                                                               						will not prompt again and the user must restart Outlook. |
|---|---|

| Caution | The user workstation must have the SSL certificates installed
                                          			 irrespective of the mode selected (authentication or non-authentication) by the
                                          			 administrator. |
|---|---|

| Note | If due to certain
                                       		  security implications you are not allowed to install the required patches or
                                       		  update registry entries, then you can create the templates without images, MWI
                                       		  status, and message status. |
|---|---|

| Microsoft Outlook Version | Microsoft Outlook 2007 | Microsoft Outlook 2010 |
|---|---|---|
| Windows XP SP3, Windows 7 (32 and 64 bit), and Windows Vista (32
                                          						and 64 bit) | Outlook 2007 Registry entry for
                                                      								  AllowImageProxyAuth, where value=1. Either Install 2007 Office
                                                      								  suite SP2. To install 2007 Office suite SP2, refer to http://support.microsoft.com/kb/953195 .
                                                      								  Then, install Outlook 2007 hotfix package. To install hotfix, refer to http://support.microsoft.com/kb/2596993 .
                                                      								  OR Install 2007 Office suite
                                                      								  SP3. To install 2007 Office suite SP3, refer to http://support.microsoft.com/kb/2526086 . Outlook 2007 with SP2 Install Outlook 2007 hotfix
                                                      								  package. To install hotfix, refer to http://support.microsoft.com/kb/2596993 . Registry entry for
                                                      								  AllowImageProxyAuth, where value=1. Outlook 2007 with SP3 Registry entry for
                                                      								  AllowImageProxyAuth, where value=1. | Install Outlook 2010 hotfix
                                                							 package. For more information, refer to http://support.microsoft.com/kb/2459116 . Registry entry for
                                                							 AllowImageProxyAuth, where value=1. |

| Step 1 | Go to Start > Run . Type regedit and press Enter . |
|---|---|
| Step 2 | Browse to the following path for Microsoft Outlook 2007: HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\Common |
| Step 3 | Browse to the following path for Microsoft Outlook 2010: HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Common |
| Step 4 | Add “AllowImageProxyAuth = 1” as new DWORD value. |

| Note | In case of forwarded messages, the attachment is sent only for the latest voice message. |
|---|---|

| Note | The secure and private voice messages cannot be sent as an attachment. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, select Advanced >
                                          			 Messaging. |
|---|---|
| Step 2 | On the Messaging Configuration page, select the Allow voice mail
                                          			 as attachments to HTML notifications option to send the voice message as an
                                          			 attachment. Click Save. |

| Step 1 | In Cisco Unity Connection Administration, select Advanced >
                                          			 Messaging. |
|---|---|
| Step 2 | On the Messaging Configuration page, enter the size of voice
                                          			 message in the Max size of voice mail as attachment to HTML notifications (KB)
                                          			 text box. |
| Step 3 | Click Save. Make sure to restart the Connection Notifier service
                                          			 for changes to take effect. |

| Step 1 | In your Lotus Notes client, select File > Preferences >
                                          			 Web Browser. |
|---|---|
| Step 2 | Select the Use the browser I have set as the default for this
                                          			 operating system option. |
| Step 3 | Click Apply and then Ok. |

| Step 1 | In your browser window, go to Tools > Intranet Options and
                                       			 select the Security tab. |
|---|---|
| Step 2 | Select the Local intranet option and click Sites. |
| Step 3 | Uncheck all the check boxes and click Ok. |
| Step 4 | Select the Trusted sites option and click Sites. |
| Step 5 | Add the website that you are using for Connection, for example,
                                       			 https://ucbu-cisco-vmxyz.cisco.com. |
| Step 6 | Click Close and then Ok. |

| Step 1 | Select Start > Control Panel > Flash Player. |
|---|---|
| Step 2 | In the Flash Player Settings Manager window, select the Camera
                                       			 and Mic tab. |
| Step 3 | Click Camera and Microphone Settings by Site. |
| Step 4 | In the Camera and Microphone Settings by Site window, select the
                                       			 Ask me when a site wants to use the camera or microphone option. |
| Step 5 | Then, click Add. |
| Step 6 | Add the website that you are using for Unity Connection, for
                                       			 example, ucbu-cisco-vmxyz.cisco.com. |
| Step 7 | Click Allow and then Close. |