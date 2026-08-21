---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-user-1-0-1-ippmtrbl-html-12c1bd80c8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/user/1_0_1/ippmtrbl.html
retrieved_at: 2026-08-21T02:47:54.195044+00:00
---

Cisco Unified IP Phone Messenger User Guide, Release 1.0(1)

# Cisco Unified IP Phone Messenger User Guide, Release 1.0(1)

Updated: July 6, 2006

Chapter: Troubleshooting

## Chapter: Troubleshooting

- Resolving Error Messages

- Frequently Asked Questions

## Troubleshooting

If you experience an error message or other difficulty when using Cisco IP Phone Messenger, these tips can assist you.

## Resolving Error Messages

Cisco IP Phone Messenger will display error messages if it encounters a problem. Refer to the following table for tips on understanding and resolving these errors.

```
Send message failure
```

```
Your message to <user ID> 
could not be delivered. 
User may have logged off.
```

The contact likely logged off just as you were sending the message. Check the contact's availability and re-send the message.

See the "Displaying a Contact's Availability" section .

```
Presence status failure
```

```
Due to unavailability of 
presence services at this 
time, presence status may 
not be working correctly. 
Please notify your system 
administrator.
```

Contact your system administrator.

```
System configuration error
```

```
You were trying to access 
IP Phone Messenger service 
from a device not 
provisioned on Cisco 
CallManager server. Please 
work with your system 
administrator to get this 
device configured.
```

Contact your system administrator.

```
Add Contact Failure
```

```
No UserID matches the 
extension you entered. 
Press OK to enter another 
extension, or Cancel to 
contact list.
```

You must enter a valid extension number of a contact within your organization.

```
Adding Contact Failed
```

```
Invalid, duplicate, or 
non-existing contact name.
```

You must enter a valid extension number of a contact within your organization.

```
Host Not Found
```

Cisco IP Phone Messenger is not available. Contact your system administrator for assistance.

```
Invalid Message Identifier
```

```
You were trying to 
retrieve a message that 
had been deleted from the 
EPAS server. Press Ok or 
Exit to return to IP Phone 
Messenger main menu.
```

If you are logged into more than one phone at a time, Multi-login state. Was deleting messages on one phone and attempting to view one on another.

```
Invalid PIN
```

```
Your PIN is invalid. Press 
Retry to re-enter your 
PIN.
```

Your phone has PIN protection enabled, but you have not entered the correct PIN. If you need additional assistance, contact your system administrator to verify your PIN.

```
Login Failed
```

```
Login failed. Your UserID 
or PIN was invalid. Press 
Retry to re-enter your 
UserID and PIN.
```

Cisco IP Phone Messenger requires that you enter your PIN when logging in. You have entered an incorrect PIN. If you need additional assistance, contact your system administrator to verify your PIN.

```
Login Failed
```

```
Login failed due to server 
error. Please contact your 
system administrator.
```

When using an unassigned phone, Cisco IP Phone Messenger requires that you enter your user ID when logging in. You have entered an incorrect user ID. See the "Entering Text on the Phone" section to verify that you are entering your user ID correctly. If you need additional assistance, contact your system administrator to verify your user ID.

```
Multi-login Alert
```

```
You are currently logged 
in from other phones. 
Press Yes to log out of 
other phones (recommended 
for security reasons). 
Press No to leave other 
phones logged in.
```

```
Incoming messages will 
show on all your other 
logged-in phones in 
addition to this phone. 
Press OK to go to the main 
menu.
```

You are attempting to log into Cisco IP Phone Messenger on more than one phone. Although this is supported, you should be aware that all instant messages will appear on each phone. This might be a privacy concern.

```
Refresh Interval
```

```
Invalid refresh interval. 
Enter a number between 7 
and 3600.
```

You cannot enter an interval outside the given range (in seconds).

```
Session Timer
```

```
Invalid session timer. 
Enter a number between 1 
and 9999.
```

You cannot enter an interval outside the given range (in minutes).

## Frequently Asked Questions

The following table provides you with answers to some common questions about Cisco IP Phone Messenger.

Why is the Msg softkey unavailable when I am attempting to send a message to someone on my contact list?

The contact has selected a status that does not allow any incoming messages. Check the contact's status. See the "Displaying a Contact's Availability" section .

Why is the Dial softkey unavailable when I am attempting to call someone on my contact list?

The contact has selected a status that does not allow any incoming calls. Check the contact's status. See the "Displaying a Contact's Availability" section .

Why do I have to enter my PIN every time I try to access the Messages list or Settings?

You have enabled PIN Protection. See the "Protected messages" section .

I am accessing the User Options web page, but I do not see any of the options mentioned.

Verify that you are accessing the User Options web pages for Cisco IP Phone Messenger, not Cisco Unified CallManager. Contact your system administrator for assistance and see the "Logging into Cisco IP Phone Messenger" section .

Why do I have to re-enter my user name and password?

The User Options web pages automatically log you out after a period of inactivity for increased security.

| Error Title | Error Text | Explanation |
|---|---|---|
| Send message failure | Your message to <user ID> 
could not be delivered. 
User may have logged off. | The contact likely logged off just as you were sending the message. Check the contact's availability and re-send the message. See the "Displaying a Contact's Availability" section . |
| Presence status failure | Due to unavailability of 
presence services at this 
time, presence status may 
not be working correctly. 
Please notify your system 
administrator. | Contact your system administrator. |
| System configuration error | You were trying to access 
IP Phone Messenger service 
from a device not 
provisioned on Cisco 
CallManager server. Please 
work with your system 
administrator to get this 
device configured. | Contact your system administrator. |
| Add Contact Failure | No UserID matches the 
extension you entered. 
Press OK to enter another 
extension, or Cancel to 
contact list. | You must enter a valid extension number of a contact within your organization. |
| Adding Contact Failed | Invalid, duplicate, or 
non-existing contact name. | You must enter a valid extension number of a contact within your organization. |
| Host Not Found |  | Cisco IP Phone Messenger is not available. Contact your system administrator for assistance. |
| Invalid Message Identifier | You were trying to 
retrieve a message that 
had been deleted from the 
EPAS server. Press Ok or 
Exit to return to IP Phone 
Messenger main menu. | If you are logged into more than one phone at a time, Multi-login state. Was deleting messages on one phone and attempting to view one on another. |
| Invalid PIN | Your PIN is invalid. Press 
Retry to re-enter your 
PIN. | Your phone has PIN protection enabled, but you have not entered the correct PIN. If you need additional assistance, contact your system administrator to verify your PIN. |
| Login Failed | Login failed. Your UserID 
or PIN was invalid. Press 
Retry to re-enter your 
UserID and PIN. | Cisco IP Phone Messenger requires that you enter your PIN when logging in. You have entered an incorrect PIN. If you need additional assistance, contact your system administrator to verify your PIN. |
| Login Failed | Login failed due to server 
error. Please contact your 
system administrator. | When using an unassigned phone, Cisco IP Phone Messenger requires that you enter your user ID when logging in. You have entered an incorrect user ID. See the "Entering Text on the Phone" section to verify that you are entering your user ID correctly. If you need additional assistance, contact your system administrator to verify your user ID. |
| Multi-login Alert | You are currently logged 
in from other phones. 
Press Yes to log out of 
other phones (recommended 
for security reasons). 
Press No to leave other 
phones logged in. Incoming messages will 
show on all your other 
logged-in phones in 
addition to this phone. 
Press OK to go to the main 
menu. | You are attempting to log into Cisco IP Phone Messenger on more than one phone. Although this is supported, you should be aware that all instant messages will appear on each phone. This might be a privacy concern. |
| Refresh Interval | Invalid refresh interval. 
Enter a number between 7 
and 3600. | You cannot enter an interval outside the given range (in seconds). |
| Session Timer | Invalid session timer. 
Enter a number between 1 
and 9999. | You cannot enter an interval outside the given range (in minutes). |

| Question | Explanation |
|---|---|
| Cisco IP Phone Messenger Phone Service |
| Why is the Msg softkey unavailable when I am attempting to send a message to someone on my contact list? | The contact has selected a status that does not allow any incoming messages. Check the contact's status. See the "Displaying a Contact's Availability" section . |
| Why is the Dial softkey unavailable when I am attempting to call someone on my contact list? | The contact has selected a status that does not allow any incoming calls. Check the contact's status. See the "Displaying a Contact's Availability" section . |
| Why do I have to enter my PIN every time I try to access the Messages list or Settings? | You have enabled PIN Protection. See the "Protected messages" section . |
| Cisco IP Phone Messenger User Options |
| I am accessing the User Options web page, but I do not see any of the options mentioned. | Verify that you are accessing the User Options web pages for Cisco IP Phone Messenger, not Cisco Unified CallManager. Contact your system administrator for assistance and see the "Logging into Cisco IP Phone Messenger" section . |
| Why do I have to re-enter my user name and password? | The User Options web pages automatically log you out after a period of inactivity for increased security. |