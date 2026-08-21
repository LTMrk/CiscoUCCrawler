---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-user-guide-email-b-12xcucugemail-b-12xcucugemail-chapter-011--269ffc5092
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/email/b_12xcucugemail/b_12xcucugemail_chapter_011.html
retrieved_at: 2026-08-21T07:56:51.808097+00:00
---

User Guide for Accessing Cisco Unity Connection Voice Messages in an Email Application (Release 12.x)

# User Guide for Accessing Cisco Unity Connection Voice Messages in an Email Application (Release 12.x)

Updated: August 17, 2017

Chapter: Changing Settings for ViewMail for Outlook (Version 8.0 Only)

## Chapter: Changing Settings for ViewMail for Outlook (Version 8.0 Only)

# Changing Settings for ViewMail for Outlook (Version 8.0 Only)

## Changing Settings for ViewMail for Outlook (Version 8.0 Only)

### Changing the Sound
                           	 That Notifies You of New Voice Messages (Version 8.0 Only)

You can choose the computer sound that notifies you when new
                              		messages arrive in the Outlook folder that contains your voice messages. This
                              		option is available only if your computer has multimedia speakers.

#### Changing the Sound
                              	 That Notifies You of New Voice Messages

From the Outlook Tools menu, click ViewMail Options .

In the ViewMail Options dialog box, click the Notification tab.

Choose your notification options.

To preview the sound for an option, click the Speaker icon.

If applicable, change the default sound for an option:

Click the Browse button.

In the Browse Files dialog box, choose a sound (WAV) file, then
                                                   				  click Open .

When the ViewMail Options dialog box reappears, click OK to save your changes.

### Changing the Automatic Voice Message Playback Setting (Version 8.0
                           	 Only)

With automatic playback, your voice messages begin playing as soon as
                              		you open them in the Outlook folder that contains your voice messages. Without
                              		automatic playback, you use the Media Master to play voice messages.

#### Changing the
                              	 Automatic Voice Message Playback Setting

From the Outlook Tools menu, click ViewMail Options .

Click the General tab.

Check or uncheck the Play Voice Automatically check box.

Click OK .

### Changing Your Preference for Saving Sent Voice Messages (Version 8.0
                           	 Only)

When you configure Outlook to save copies of sent messages in the Sent
                              		Items folder, a copy of each voice message that you send by using ViewMail for
                              		Outlook is also saved. To save space on your hard disk, you can set ViewMail to
                              		save only the message headers and not save the message recordings. (A message
                              		header contains the message recipient(s), when the message was sent, the
                              		subject, the importance and sensitivity, and the size.)

#### Saving Only Voice
                              	 Message Headers

From the Outlook Tools menu, click ViewMail Options .

Click the General tab.

Check the Keep Only Message Header in the Sent Items Folder check box.

Click OK .

### Changing Recording
                           	 and Playback Devices (Version 8.0 Only)

Do the following
                                 		  procedure to change the recording or playback device

From the
                                          			 Outlook Tools menu, click ViewMail
                                             				Options .

Click the Record or Playback tab.

In the Device
                                          			 list, select the device that you want to use.

If you did not
                                          			 choose Phone for your playback or recording device, skip to Step
                                             				13 .

If you select
                                             				Phone for your playback or recording device, click the Server tab.

In the Cisco
                                          			 Unity Connection Server Name box, enter the name of your Unity Connection
                                          			 server. (If you do not know the server name, contact your Unity Connection
                                          			 administrator.)

In the User
                                          			 Name box, enter your Unity Connection username.

In the
                                          			 Password box, enter your Cisco PCA password.

Check the
                                          			 Remember Password check box if you want ViewMail for Outlook to remember your
                                          			 password so that you do not have to re-enter it each time you restart Outlook.

If your
                                          			 organization uses a proxy server, in the Proxy Server Address box, enter the IP
                                          			 address of the proxy server.

If your
                                          			 organization uses a proxy server, in the Proxy Server Port box, enter the
                                          			 server port number ViewMail for Outlook must use when connecting to the proxy
                                          			 server.

If your Unity
                                          			 Connection administrator tells you to, check the Validate HTTPS Certificate
                                          			 check box. Otherwise, leave it unchecked.

In the
                                          			 Extension box, enter your extension.

Click OK .

### Configuring Your Secure Messaging Settings (Version 8.0 Only)

#### Configuring Your
                              	 Secure Messaging Settings

From the Outlook Tools menu, click ViewMail Options .

Click the Server tab.

In the Cisco Unity Connection Server Name box, enter the name of
                                             			 your Unity Connection server. (If you do not know the server name, contact your
                                             			 Unity Connection administrator.)

In the User Name box, enter your Unity Connection username.

In the Password box, enter your Cisco PCA password.

Check the Remember Password check box if you want ViewMail for
                                             			 Outlook to remember your password so that you do not have to re-enter it each
                                             			 time you restart Outlook.

If your organization uses a proxy server, in the Proxy Server
                                             			 Address box, enter the IP address of the proxy server.

If your organization uses a proxy server, in the Proxy Server
                                             			 Port box, enter the server port number that ViewMail for Outlook must use when
                                             			 connecting to the proxy server.

If your Unity Connection administrator tells you to, check the
                                             			 Validate HTTPS Certificate check box. Otherwise, leave it unchecked.

Click OK .

### Changing Your IMAP Account Setting (Version 8.0 Only)

If you have more than one IMAP account configured in Outlook, you need
                              		to identify the one that is associated with Cisco Unity Connection.

#### Changing Your IMAP
                              	 Account Setting

From the Outlook Tools menu, click ViewMail Options .

Click the Accounts tab.

In the Select the Accounts to Access Cisco Unity Connection With
                                             			 list, select the IMAP account that is used to access Unity Connection.

Click OK .

### Updating the Password in ViewMail for Outlook to Match Your Cisco PCA
                           	 Password (Version 8.0 Only)

ViewMail for Outlook uses your Cisco Unity Connection username and Cisco
                              		PCA password to access your Unity Connection account to retrieve voice
                              		messages. You must update the password in ViewMail when you change your Cisco
                              		PCA password in the Messaging Assistant web tool. This ensures that ViewMail
                              		for Outlook can continue to access your Unity Connection account.

If you are having trouble sending or receiving voice messages in
                              		ViewMail for Outlook, consider the following tips:

If Microsoft Outlook prompts you for a password but does not accept
                                    			 it, your Cisco PCA password may have expired or changed, or it may be locked.
                                    			 Change your Cisco PCA password in the Messaging Assistant first, then update
                                    			 the password in ViewMail for Outlook.

If you receive an error when you attempt to play or record messages
                                    			 in ViewMail for Outlook by using the phone, your Cisco PCA password may have
                                    			 expired or changed, or it may be locked. Change your Cisco PCA password in the
                                    			 Messaging Assistant first, then update it in ViewMail.

If you receive an error when you attempt to play or record secure
                                    			 messages, your Cisco PCA password may have expired or changed, or it may be
                                    			 locked. Change your Cisco PCA password in the Messaging Assistant first, then
                                    			 update it in ViewMail for Outlook.

#### Updating the
                              	 Password in ViewMail for Outlook to Match Your Cisco PCA Password

From the Outlook Tools menu, click ViewMail Options .

Click the Server tab.

In the Password box, enter the new Cisco PCA password that you
                                             			 changed in the Messaging Assistant.

Click OK.

From the Outlook Tools menu, click Email Accounts.

Select View or Change Existing Email Accounts and click Next.

Select the IMAP account that is used to access Cisco Unity
                                             			 Connection and click Change.

In the Password box, enter the new Cisco PCA password that you
                                             			 changed in the Messaging Assistant.

Click Next, then click Finish.

| Note | This content applies to ViewMail for Outlook version 8.0 only. For
                                    		  later ViewMail versions, see the Quick Start Guide for Cisco ViewMail for
                                       			 Microsoft Outlook (Release 8.5 and Later) at http://www.cisco.com/en/US/docs/voice_ip_comm/connection/vmo/quick_start/guide/85xcucqsgvmo.html |
|---|---|

| Note | This content applies to ViewMail for Outlook version 8.0 only. For
                                       		  later ViewMail versions, see the Quick Start Guide for Cisco ViewMail for
                                          			 Microsoft Outlook (Release 8.5 and Later) at http://www.cisco.com/en/US/docs/voice_ip_comm/connection/vmo/quick_start/guide/85xcucqsgvmo.html |
|---|---|

| Step 1 | From the Outlook Tools menu, click ViewMail Options . |
|---|---|
| Step 2 | In the ViewMail Options dialog box, click the Notification tab. |
| Step 3 | Choose your notification options. To preview the sound for an option, click the Speaker icon. |
| Step 4 | If applicable, change the default sound for an option: Click the Browse button. In the Browse Files dialog box, choose a sound (WAV) file, then
                                                   				  click Open . |
| Step 5 | When the ViewMail Options dialog box reappears, click OK to save your changes. |

| Step 1 | From the Outlook Tools menu, click ViewMail Options . |
|---|---|
| Step 2 | Click the General tab. |
| Step 3 | Check or uncheck the Play Voice Automatically check box. |
| Step 4 | Click OK . |

| Step 1 | From the Outlook Tools menu, click ViewMail Options . |
|---|---|
| Step 2 | Click the General tab. |
| Step 3 | Check the Keep Only Message Header in the Sent Items Folder check box. |
| Step 4 | Click OK . |

| Step 1 | From the
                                          			 Outlook Tools menu, click ViewMail
                                             				Options . |
|---|---|
| Step 2 | Click the Record or Playback tab. |
| Step 3 | In the Device
                                          			 list, select the device that you want to use. |
| Step 4 | If you did not
                                          			 choose Phone for your playback or recording device, skip to Step
                                             				13 . If you select
                                             				Phone for your playback or recording device, click the Server tab. |
| Step 5 | In the Cisco
                                          			 Unity Connection Server Name box, enter the name of your Unity Connection
                                          			 server. (If you do not know the server name, contact your Unity Connection
                                          			 administrator.) |
| Step 6 | In the User
                                          			 Name box, enter your Unity Connection username. |
| Step 7 | In the
                                          			 Password box, enter your Cisco PCA password. |
| Step 8 | Check the
                                          			 Remember Password check box if you want ViewMail for Outlook to remember your
                                          			 password so that you do not have to re-enter it each time you restart Outlook. |
| Step 9 | If your
                                          			 organization uses a proxy server, in the Proxy Server Address box, enter the IP
                                          			 address of the proxy server. |
| Step 10 | If your
                                          			 organization uses a proxy server, in the Proxy Server Port box, enter the
                                          			 server port number ViewMail for Outlook must use when connecting to the proxy
                                          			 server. |
| Step 11 | If your Unity
                                          			 Connection administrator tells you to, check the Validate HTTPS Certificate
                                          			 check box. Otherwise, leave it unchecked. |
| Step 12 | In the
                                          			 Extension box, enter your extension. |
| Step 13 | Click OK . |

| Step 1 | From the Outlook Tools menu, click ViewMail Options . |
|---|---|
| Step 2 | Click the Server tab. |
| Step 3 | In the Cisco Unity Connection Server Name box, enter the name of
                                             			 your Unity Connection server. (If you do not know the server name, contact your
                                             			 Unity Connection administrator.) |
| Step 4 | In the User Name box, enter your Unity Connection username. |
| Step 5 | In the Password box, enter your Cisco PCA password. |
| Step 6 | Check the Remember Password check box if you want ViewMail for
                                             			 Outlook to remember your password so that you do not have to re-enter it each
                                             			 time you restart Outlook. |
| Step 7 | If your organization uses a proxy server, in the Proxy Server
                                             			 Address box, enter the IP address of the proxy server. |
| Step 8 | If your organization uses a proxy server, in the Proxy Server
                                             			 Port box, enter the server port number that ViewMail for Outlook must use when
                                             			 connecting to the proxy server. |
| Step 9 | If your Unity Connection administrator tells you to, check the
                                             			 Validate HTTPS Certificate check box. Otherwise, leave it unchecked. |
| Step 10 | Click OK . |

| Step 1 | From the Outlook Tools menu, click ViewMail Options . |
|---|---|
| Step 2 | Click the Accounts tab. |
| Step 3 | In the Select the Accounts to Access Cisco Unity Connection With
                                             			 list, select the IMAP account that is used to access Unity Connection. |
| Step 4 | Click OK . |

| Step 1 | From the Outlook Tools menu, click ViewMail Options . |
|---|---|
| Step 2 | Click the Server tab. |
| Step 3 | In the Password box, enter the new Cisco PCA password that you
                                             			 changed in the Messaging Assistant. |
| Step 4 | Click OK. |
| Step 5 | From the Outlook Tools menu, click Email Accounts. |
| Step 6 | Select View or Change Existing Email Accounts and click Next. |
| Step 7 | Select the IMAP account that is used to access Cisco Unity
                                             			 Connection and click Change. |
| Step 8 | In the Password box, enter the new Cisco PCA password that you
                                             			 changed in the Messaging Assistant. |
| Step 9 | Click Next, then click Finish. |