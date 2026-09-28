---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-features-guide-uccx-b-125-3c64103dbb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/features/guide/uccx_b_1251su3_features-guide/uccx_m_1251su2_team-message.html
retrieved_at: 2026-08-16T21:17:23.387133+00:00
---

Cisco Unified Contact Center Express Features Guide, Release 12.5(1) SU3

# Cisco Unified Contact Center Express Features Guide, Release 12.5(1) SU3

Updated: May 7, 2023

Chapter: Team Message

## Chapter: Team Message

# Team Message

## Overview

Team Message is introduced in Finesse for enabling quick communication within the organization. It enables supervisors to
                              broadcast short messages, which are displayed on agents desktop.

Customers who upgrade with existing layouts, need to add this component manually from the Default Desktop Layout.

### Key Features

Key features of Team Message are as follows:

Role

Features

Administrator

Enable/Disable Team Message on supervisor desktop.

Supervisor

Send messages to a single team, multiple teams or all the teams that they manage.

View and delete broadcasted messages.

Set a time frame for a message to be displayed. After expiry of the set time, the message is not displayed.

Agent

View Team Message banner in real time to stay up-to-date with the latest broadcasts.

Scroll through the list of broadcasted messages.

During failover, team message and failover banners are displayed together.

## Use Team Message

### Send Team Message

The Team Message feature allows you to create and send a broadcast message to one or multiple teams. The message appears as
                                 a banner across the Finesse desktop and agents can view these messages in real-time. Team Message will be available on your
                                 Finesse desktop only if the administrator has configured this feature for you.

Step 1

In the Finesse desktop, click the Team Message icon.

Step 2

In the Compose Message box, enter the broadcast message (maximum number of characters allowed is 255).

Step 3

Select the team or teams to send the message by checking the check box next to the team name.

You can send multiple messages to a single team, multiple teams, or all teams.

Step 4

From the drop-down, you can set an expiry time for the composed messages: starting at 5 minutes and ending at 23:55 hours.
                                          The time is displayed in hours and minutes. However, this time frame can be edited.

Step 5

Click Send .

You can view the latest messages sent by clicking Show recent messages . If you wish to delete any or all messages, check the check box next to the message. Click Delete and confirm the deletion.

The message is removed from active display and the previous non-expired team message will become the active message for the
                                             agent.

Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message .

The rate at which messages (create/delete) are published to the teams involved, is capped at 100 per hour and the maximum number of active messages allowed is 1600 . If the limit of active messages is reached, supervisors will not be able to broadcast new messages until an existing team
                                             message is deleted or it expires.

As there are no individual limitations on supervisors, either one or all supervisors can broadcast messages up to the maximum
                                             active messages limit.

### View Team Message

On logging in to the Finesse desktop, you can view the Team Message banner which broadcasts the active team updates sent by
                                 your supervisor in real-time. The total number of active messages sent by your supervisor is displayed in the banner. By clicking
                                 the number, you can view the latest message with the name of the supervisor and the timestamp being displayed against each
                                 message.

You can toggle between the active messages (note that messages expire after a time frame, as set by the Supervisor).

If the Finesse desktop is inactive, a toaster notification appears when a new team message is sent by the Supervisor. You
                                 can click the notification to view the message.

During failover, the team message banner and the failover banner will be displayed together.

| Note | Customers who upgrade with existing layouts, need to add this component manually from the Default Desktop Layout. |
|---|---|

| Role | Features |
|---|---|
| Administrator | Enable/Disable Team Message on supervisor desktop. |
| Supervisor | Send messages to a single team, multiple teams or all the teams that they manage. View and delete broadcasted messages. Set a time frame for a message to be displayed. After expiry of the set time, the message is not displayed. |
| Agent | View Team Message banner in real time to stay up-to-date with the latest broadcasts. Scroll through the list of broadcasted messages. |

| Note | During failover, team message and failover banners are displayed together. |
|---|---|

| Step 1 | In the Finesse desktop, click the Team Message icon. |
|---|---|
| Step 2 | In the Compose Message box, enter the broadcast message (maximum number of characters allowed is 255). |
| Step 3 | Select the team or teams to send the message by checking the check box next to the team name. Note You can send multiple messages to a single team, multiple teams, or all teams. | Note | You can send multiple messages to a single team, multiple teams, or all teams. |
| Note | You can send multiple messages to a single team, multiple teams, or all teams. |
| Step 4 | From the drop-down, you can set an expiry time for the composed messages: starting at 5 minutes and ending at 23:55 hours.
                                          The time is displayed in hours and minutes. However, this time frame can be edited. |
| Step 5 | Click Send . You can view the latest messages sent by clicking Show recent messages . If you wish to delete any or all messages, check the check box next to the message. Click Delete and confirm the deletion. The message is removed from active display and the previous non-expired team message will become the active message for the
                                             agent. Note Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . | Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |
| Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |

| Note | You can send multiple messages to a single team, multiple teams, or all teams. |
|---|---|

| Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |
|---|---|

| Note | The rate at which messages (create/delete) are published to the teams involved, is capped at 100 per hour and the maximum number of active messages allowed is 1600 . If the limit of active messages is reached, supervisors will not be able to broadcast new messages until an existing team
                                             message is deleted or it expires. As there are no individual limitations on supervisors, either one or all supervisors can broadcast messages up to the maximum
                                             active messages limit. |
|---|---|

| Note | During failover, the team message banner and the failover banner will be displayed together. |
|---|---|