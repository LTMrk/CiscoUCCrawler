---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-01000-h-093ceff93f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_01000.html
retrieved_at: 2026-08-17T02:28:52.826120+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting Non-Delivery Receipts

## Chapter: Troubleshooting Non-Delivery Receipts

# Troubleshooting Non-Delivery Receipts

Troubleshooting Non-Delivery Receipts

## Overview

Determine whether the fault lies with the sender, the
                           		recipient, or the Cisco Unity Connection server. To gather more information,
                           		send voice messages to the recipient from different users. In addition, send
                           		voice messages to different users from the original sender.

## Non-Delivery Receipt Status Codes

As you examine a nondelivery receipt (NDR), look for a three-digit code (for example, 4.2.2).

Note that in general, the first decimal place refers to the class of code: 4.x.x is a transient failure and resend attempts
                           may be successful, while 5.x.x is a permanent error.

A more detailed analysis and a list of standard errors for SMTP are available in RFC 1893—Enhanced Mail System Status Codes.

Status codes in Unity Connection have the following meanings:

4.0.0—An unknown error (for example, connectivity problems) prevented Unity Connection from communicating with another SMTP
                                 server.

4.0.1—Error connecting to the SMTP server.

4.0.2—An unknown error (for example, connectivity problems) prevented Unity Connection from communicating with another SMTP
                                 server.

4.2.1—The recipient mailbox has been dismounted.

4.2.2—The recipient mailbox is over the allotted quota set by the administrator.

4.2.4 —There is no valid recipient for the message.

4.3.2—The message store where the recipient is located has been dismounted.

5.1.1—The recipient mailbox cannot be resolved, possibly because the recipient address does not exist or is not correct.

5.2.0—An unknown error condition exists, and Unity Connection cannot process the message.

5.4.4—There are errors in the VPIM configuration in Unity Connection.

5.5.4—There was a permanent error in connecting to the SMTP server.

5.6.5—The conversion of a Unity Connection message to a VPIM message failed.

5.7.1—A user attempted to send a private message to a contact, which is not supported.

5.7.2—An error occurred during expansion of a distribution list.

5.7.3—A user attempted to send a secure message to a contact, which is not supported.

5.3.10—A fax message failed.

Code 2.0.0 indicates success. Delivery and read receipts contain this status code; NDRs do not.

| Note | Code 2.0.0 indicates success. Delivery and read receipts contain this status code; NDRs do not. |
|---|---|