---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-010111-htm-3ac9e3abf6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_010111.html
retrieved_at: 2026-08-17T02:18:06.807387+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting Fax

## Chapter: Troubleshooting Fax

# Troubleshooting Fax

### Troubleshooting Fax

## Problems with Fax
                        	 Delivery to Users

When faxes are not
                           		delivered to users, use the following task list to determine the cause and to
                           		resolve the problem. Do the tasks in the order presented until the problem is
                           		resolved.

Following are the tasks to troubleshoot fax delivery to users:

Determine whether the fax is being sent by enabling the MTA
                                 			 micro trace (all levels). For detailed instructions on enabling the micro trace
                                 			 and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting section.

If the trace logs show that the fax was sent, investigate how
                                 			 the SMTP server handles faxes by enabling the SMTP micro trace (all levels).
                                 			 For detailed instructions on enabling the micro trace and viewing the trace
                                 			 logs, see the Using Diagnostic Traces for Troubleshooting section.

Confirm that the SMTP server configuration lists the IP address
                                 			 of the Cisco Fax Server and allows a Unity Connection. See the “Confirm
                                    				that SMTP Server Configuration is Correct” section on page 24-1 .

Check for the fax in the POP3 mailbox by connecting an email
                                 			 client to the POP3 mailbox.

The email client must be configured to leave messages in the
                                             				POP3 mailbox.

In the RightFax Email Gateway, confirm that the POP3 mailbox
                                 			 name and password are correct. See the “Confirming
                                    				that POP3 Mailbox Name and Password are Correct” section on page 24-2 .

On the network, confirm that the account for the POP3 mailbox is
                                 			 set to never expire the password. An expired password prevents faxes from being
                                 			 routed.

Confirm that faxes are delivered to Unity Connection. See the “Confirming
                                    				Fax is Delivered to Unity Connection” section on page 24-2 .

### Confirming that
                           	 SMTP Server Configuration is Correct

Step 1

In Cisco Unity Connection Administration, expand System Settings > and select SMTP
                                                				  Configuration > Server .

Step 2

On the SMTP Server Configuration page, on the Edit menu, select Search IP Address Access List .

Step 3

On the Search IP Address Access List page, confirm that the IP
                                          			 address of the Cisco Fax Server appears in the list. If not, select Add New to add the IP address.

Step 4

Check the Allow Connections check box for the IP address of the Cisco Fax
                                          			 Server, if it is not already checked and select Save .

### Confirming that
                           	 POP3 Mailbox Name and Password are Correct

Step 1

On the Windows Start menu, select Control Panel > RightFax Email
                                                				  Gateway .

Step 2

In the Email Configuration window, select the General tab.

Step 3

In the POP3 Mailbox Name field, confirm that the entry matches
                                          			 the SMTP address for the Cisco Fax Server on the System Settings > Fax
                                          			 Server > Edit Fax Server Configuration page in Cisco Unity Connection
                                          			 Administration.

Step 4

In the Mailbox Password field, confirm that the password is
                                          			 correct.

Step 5

In the Email Deliver Direction field, confirm that Both is selected and select OK .

### Confirming Fax is
                           	 Delivered to Unity Connection

Step 1

On the Windows Start menu, select All
                                                				  Programs > RightFax
                                                				  FaxUtil .

Step 2

In the RightFax FaxUtil window, in the left pane, select the
                                          			 user who sends the test fax.

Step 3

On the Fax menu, select New .

Step 4

In the Fax Information dialog box, select the Main tab.

Step 5

Under the Name field, select the drop-down arrow and select Email Address .

Step 6

In the Email Address field, enter the email address of the user
                                          			 who has the fax delivery problem.

Step 7

Select Save .

Step 8

In the right pane, note the status of the test fax as it is
                                          			 being sent.

To refresh the status display of the fax progress, press F5 .

## Problems with Fax
                        	 Delivery to a Fax Machine

When faxes are
                           		not delivered to a fax machine, use the following task list to determine the
                           		cause and to resolve the problem. Do the tasks in the order presented until the
                           		problem is resolved.

Following are the tasks to troubleshoot fax delivery issues in a
                           		fax machine:

Determine the status of the fax that was sent to a fax machine.
                                 			 See the “Determine
                                    				the Status of a Fax Delivered to a Fax Machine” section on page 24-3 .

Confirm that the fax is in the POP3 mailbox by connecting an
                                 			 email client to the POP3 mailbox.

Note that the email client must be configured to leave messages
                                 			 in the POP3 mailbox.

In the RightFax Email Gateway, confirm that the POP3 mailbox
                                 			 name and password are correct. See the “Confirm
                                    				that POP3 Mailbox Name and Password are Correct” section on page 24-3 .

On the network, confirm that the account for the POP3 mailbox is
                                 			 set to never expire the password. An expired password prevents faxes from being
                                 			 routed.

Confirm that the SMTP server configuration lists the IP address
                                 			 of the Cisco Fax Server and allows a Unity Connection. See the “Confirming
                                    				that SMTP Server Configuration is Correct” section on page 24-4 .

Troubleshoot how the SMTP server handles faxes by enabling the
                                 			 SMTP micro trace (all levels). For detailed instructions on enabling the micro
                                 			 trace and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting section.

If the trace logs show that the SMTP message was not sent,
                                 			 investigate how the fax is sent by enabling the MTA micro trace (all levels).
                                 			 For detailed instructions on enabling the micro trace and viewing the trace
                                 			 logs, see the Using Diagnostic Traces for Troubleshooting section.

Confirm that the file extension of the file that the user
                                 			 attempted to fax is included in the list of faxable file types. See the “Confirming
                                    				that Faxable File Types List is Correct” section on page 24-4 .

### Determining the
                           	 Status of a Fax Delivered to a Fax Machine

Step 1

On the Windows Start menu, select All
                                                				  Programs > RightFax
                                                				  FaxUtil .

Step 2

In the RightFax FaxUtil window, in the left pane, select the
                                          			 user who sent the fax to the fax machine, then select All .

Step 3

In the right pane, note the status of the fax and any problems
                                          			 that are reported.

### Confirming that
                           	 POP3 Mailbox Name and Password are Correct

Step 1

On the Windows Start menu, select Control Panel > RightFax Email
                                                				  Gateway .

Step 2

In the Email Configuration window, select the General tab.

Step 3

In the POP3 Mailbox Name field, confirm that the entry matches
                                          			 the SMTP address for the Cisco Fax Server on the System Settings > Fax
                                          			 Server > Edit Fax Server Configuration page in Cisco Unity Connection
                                          			 Administration.

Step 4

In the Mailbox Password field, confirm that the password is
                                          			 correct.

Step 5

In the Email Deliver Direction field, confirm that Both is selected and select OK .

### Confirming that
                           	 SMTP Server Configuration is Correct

Step 1

In Cisco Unity Connection Administration, expand System Settings and select SMTP
                                                				  Configuration > Server .

Step 2

On the SMTP Server Configuration page, on the Edit menu, select Search IP Address Access List .

Step 3

On the Search IP Address Access List page, confirm that the IP
                                          			 address of the Cisco Fax Server appears in the list. If not, select Add New to add the IP address.

Step 4

Check the Allow Unity Connection check box for the IP address of the
                                          			 Cisco Fax Server, if it is not already checked and select Save .

### Confirming that
                           	 Faxable File Types List is Correct

Step 1

In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Fax .

Step 2

On the Fax Configuration page, in the Faxable File Types field,
                                          			 note the file extensions that are listed.

Step 3

If the file extension of the file that the user attempted to fax
                                          			 is not in the list, enter a comma followed by the file extension and select Save .

## Problems with Fax Notifications

Confirm that fax notification from Unity Connection is enabled for the user.

### Confirming that
                           	 Fax Notification is Enabled for the User

Step 1

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, select the alias of
                                          			 the user.

Step 2

On the Edit menu, select Notification Devices .

Step 3

On the Notification Devices page, select the name of the
                                          			 applicable notification device.

Step 4

On the Edit Notification Device page, under Notification Rule
                                          			 Events, check the Fax Messages check box and select Save .

## Problems with Fax Receipts

This section covers the troubleshooting steps of some fax receipt related problems.

### Fax Receipts Not Delivered

### Verifying Prefixes
                           	 for Delivery Receipts and Nondelivery Receipts on the Cisco Fax Server

Step 1

On the Windows Start menu, select Control Panel > RightFax Enterprise Fax
                                                				  Manager .

Step 2

In the Email Configuration window, select the General tab.

Step 3

In the left pane of the RightFax Enterprise Fax Manager window,
                                          			 select the name of the Cisco Fax Server.

Step 4

In the right pane, under Service Name, scroll down to RightFax eTransport Module .

Step 5

Right-click RightFax eTransport Module and select Configure Services .

Step 6

Select the Custom Messages tab.

Step 7

In the applicable fields, verify the fax failure prefix at the
                                          			 beginning of the text (the default fax failure prefix is [Fax Failure]). We
                                          			 recommend that the fax failure prefix appear at the beginning of the following
                                          			 fields:

Imaging Error

Bad Form Type

Bad Fax Phone Number

Too Many Retries

Sending Error

Incomplete Fax

Invalid Billing Code

Fax Needs Approval

Fax Number Blocked

Human Answered Fax

Fax Block by Do Not Dial

When the text at the beginning of the field matches the value
                                             				for the Subject Prefix for Notification of a Failed Fax field on the System
                                             				Settings > Advanced > Fax page of Cisco Unity Connection Administration,
                                             				Unity Connection notifies the user of the failed fax.

Step 8

In the Successful Send field, verify the fax success prefix at
                                          			 the beginning of the text (the default fax success prefix is [Fax Success]).

When the text at the beginning of the field matches the value
                                             				for the Subject Prefix for Notification of a Successful Fax field on the System
                                             				Settings > Advanced > Fax page of Connection Administration, Unity
                                             				Connection notifies the user of the successful fax.

Step 9

Select OK .

### Verifying Prefixes
                           	 for Delivery Receipts and Nondelivery Receipts on Cisco Unity
                           	 Connection

Step 1

In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Fax .

Step 2

On the Fax Configuration page, in the Subject Prefix for
                                          			 Notification of a Successful Fax field, confirm that the setting matches the
                                          			 prefix for the Successful Send field that is described in Step 8 of the “To
                                             				Verify Prefixes for Delivery Receipts and Nondelivery Receipts on the Cisco Fax
                                             				Server” procedure on page 24-5 .

Step 3

In the Subject Prefix for Notification of a Failed Fax field,
                                          			 confirm that the setting matches the prefix for the fields that are described
                                          			 in Step 7 of the “To
                                             				Verify Prefixes for Delivery Receipts and Nondelivery Receipts on the Cisco Fax
                                             				Server” procedure on page 24-5 .

Step 4

Select Save .

### User Mailbox is Filled with Fax Notifications

### Disabling Fax
                           	 Notifications

Step 1

In the RightFax Enterprise Fax Manager window, in the right
                                          			 pane, expand Users , right-click the user for whom you want to
                                          			 disable fax notifications, and select Edit .

Step 2

In the User Edit dialog box, select the Notifications tab.

Step 3

Under Notification About Received Faxes, uncheck the When Initially Received check box.

Step 4

Select OK .

Step 5

Repeat Step 1 through Step 4 for all
                                          			 remaining users for whom you want to disable fax notifications.

Step 6

Close the RightFax Enterprise Fax Manager window.

## Problems with
                        	 Printing Faxes

When you send a fax to a fax
                           		machine for printing but portions of the document are not printed, do the
                           		following:

Use the MTA micro trace to determine which files are not
                                 			 rendered into the fax. Then note the file types. For instructions for enabling
                                 			 the micro trace and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting section.

Confirm that the faxable file types include the file types that
                                 			 you sent to the fax machine for printing. See the “Confirming
                                    				that Faxable File Types List is Correct” section on page 24-6 .

### Confirming that
                           	 Faxable File Types List is Correct

Step 1

In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Fax .

Step 2

On the Fax Configuration page, in the Faxable File Types field,
                                          			 note the file extensions that are listed.

Step 3

If the file extension of the file that the user attempted to fax
                                          			 is not in the list, enter a comma followed by the file extension and select Save .

| Note | The email client must be configured to leave messages in the
                                             				POP3 mailbox. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > and select SMTP
                                                				  Configuration > Server . |
|---|---|
| Step 2 | On the SMTP Server Configuration page, on the Edit menu, select Search IP Address Access List . |
| Step 3 | On the Search IP Address Access List page, confirm that the IP
                                          			 address of the Cisco Fax Server appears in the list. If not, select Add New to add the IP address. |
| Step 4 | Check the Allow Connections check box for the IP address of the Cisco Fax
                                          			 Server, if it is not already checked and select Save . |

| Step 1 | On the Windows Start menu, select Control Panel > RightFax Email
                                                				  Gateway . |
|---|---|
| Step 2 | In the Email Configuration window, select the General tab. |
| Step 3 | In the POP3 Mailbox Name field, confirm that the entry matches
                                          			 the SMTP address for the Cisco Fax Server on the System Settings > Fax
                                          			 Server > Edit Fax Server Configuration page in Cisco Unity Connection
                                          			 Administration. |
| Step 4 | In the Mailbox Password field, confirm that the password is
                                          			 correct. |
| Step 5 | In the Email Deliver Direction field, confirm that Both is selected and select OK . |

| Step 1 | On the Windows Start menu, select All
                                                				  Programs > RightFax
                                                				  FaxUtil . |
|---|---|
| Step 2 | In the RightFax FaxUtil window, in the left pane, select the
                                          			 user who sends the test fax. |
| Step 3 | On the Fax menu, select New . |
| Step 4 | In the Fax Information dialog box, select the Main tab. |
| Step 5 | Under the Name field, select the drop-down arrow and select Email Address . |
| Step 6 | In the Email Address field, enter the email address of the user
                                          			 who has the fax delivery problem. |
| Step 7 | Select Save . |
| Step 8 | In the right pane, note the status of the test fax as it is
                                          			 being sent. Note To refresh the status display of the fax progress, press F5 . | Note | To refresh the status display of the fax progress, press F5 . |
| Note | To refresh the status display of the fax progress, press F5 . |

| Note | To refresh the status display of the fax progress, press F5 . |
|---|---|

| Step 1 | On the Windows Start menu, select All
                                                				  Programs > RightFax
                                                				  FaxUtil . |
|---|---|
| Step 2 | In the RightFax FaxUtil window, in the left pane, select the
                                          			 user who sent the fax to the fax machine, then select All . |
| Step 3 | In the right pane, note the status of the fax and any problems
                                          			 that are reported. |

| Step 1 | On the Windows Start menu, select Control Panel > RightFax Email
                                                				  Gateway . |
|---|---|
| Step 2 | In the Email Configuration window, select the General tab. |
| Step 3 | In the POP3 Mailbox Name field, confirm that the entry matches
                                          			 the SMTP address for the Cisco Fax Server on the System Settings > Fax
                                          			 Server > Edit Fax Server Configuration page in Cisco Unity Connection
                                          			 Administration. |
| Step 4 | In the Mailbox Password field, confirm that the password is
                                          			 correct. |
| Step 5 | In the Email Deliver Direction field, confirm that Both is selected and select OK . |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings and select SMTP
                                                				  Configuration > Server . |
|---|---|
| Step 2 | On the SMTP Server Configuration page, on the Edit menu, select Search IP Address Access List . |
| Step 3 | On the Search IP Address Access List page, confirm that the IP
                                          			 address of the Cisco Fax Server appears in the list. If not, select Add New to add the IP address. |
| Step 4 | Check the Allow Unity Connection check box for the IP address of the
                                          			 Cisco Fax Server, if it is not already checked and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Fax . |
|---|---|
| Step 2 | On the Fax Configuration page, in the Faxable File Types field,
                                          			 note the file extensions that are listed. |
| Step 3 | If the file extension of the file that the user attempted to fax
                                          			 is not in the list, enter a comma followed by the file extension and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, select the alias of
                                          			 the user. |
|---|---|
| Step 2 | On the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the name of the
                                          			 applicable notification device. |
| Step 4 | On the Edit Notification Device page, under Notification Rule
                                          			 Events, check the Fax Messages check box and select Save . |

| Step 1 | On the Windows Start menu, select Control Panel > RightFax Enterprise Fax
                                                				  Manager . |
|---|---|
| Step 2 | In the Email Configuration window, select the General tab. |
| Step 3 | In the left pane of the RightFax Enterprise Fax Manager window,
                                          			 select the name of the Cisco Fax Server. |
| Step 4 | In the right pane, under Service Name, scroll down to RightFax eTransport Module . |
| Step 5 | Right-click RightFax eTransport Module and select Configure Services . |
| Step 6 | Select the Custom Messages tab. |
| Step 7 | In the applicable fields, verify the fax failure prefix at the
                                          			 beginning of the text (the default fax failure prefix is [Fax Failure]). We
                                          			 recommend that the fax failure prefix appear at the beginning of the following
                                          			 fields: Imaging Error Bad Form Type Bad Fax Phone Number Too Many Retries Sending Error Incomplete Fax Invalid Billing Code Fax Needs Approval Fax Number Blocked Human Answered Fax Fax Block by Do Not Dial When the text at the beginning of the field matches the value
                                             				for the Subject Prefix for Notification of a Failed Fax field on the System
                                             				Settings > Advanced > Fax page of Cisco Unity Connection Administration,
                                             				Unity Connection notifies the user of the failed fax. |
| Step 8 | In the Successful Send field, verify the fax success prefix at
                                          			 the beginning of the text (the default fax success prefix is [Fax Success]). When the text at the beginning of the field matches the value
                                             				for the Subject Prefix for Notification of a Successful Fax field on the System
                                             				Settings > Advanced > Fax page of Connection Administration, Unity
                                             				Connection notifies the user of the successful fax. |
| Step 9 | Select OK . |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Fax . |
|---|---|
| Step 2 | On the Fax Configuration page, in the Subject Prefix for
                                          			 Notification of a Successful Fax field, confirm that the setting matches the
                                          			 prefix for the Successful Send field that is described in Step 8 of the “To
                                             				Verify Prefixes for Delivery Receipts and Nondelivery Receipts on the Cisco Fax
                                             				Server” procedure on page 24-5 . |
| Step 3 | In the Subject Prefix for Notification of a Failed Fax field,
                                          			 confirm that the setting matches the prefix for the fields that are described
                                          			 in Step 7 of the “To
                                             				Verify Prefixes for Delivery Receipts and Nondelivery Receipts on the Cisco Fax
                                             				Server” procedure on page 24-5 . |
| Step 4 | Select Save . |

| Step 1 | In the RightFax Enterprise Fax Manager window, in the right
                                          			 pane, expand Users , right-click the user for whom you want to
                                          			 disable fax notifications, and select Edit . |
|---|---|
| Step 2 | In the User Edit dialog box, select the Notifications tab. |
| Step 3 | Under Notification About Received Faxes, uncheck the When Initially Received check box. |
| Step 4 | Select OK . |
| Step 5 | Repeat Step 1 through Step 4 for all
                                          			 remaining users for whom you want to disable fax notifications. |
| Step 6 | Close the RightFax Enterprise Fax Manager window. |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Fax . |
|---|---|
| Step 2 | On the Fax Configuration page, in the Faxable File Types field,
                                          			 note the file extensions that are listed. |
| Step 3 | If the file extension of the file that the user attempted to fax
                                          			 is not in the list, enter a comma followed by the file extension and select Save . |