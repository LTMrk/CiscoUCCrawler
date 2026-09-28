---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-14-cup0-b-rcc-lync-server-integration-14-c-fc277ff38f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/14/cup0_b_rcc-lync-server-integration-14/cup0_b_rcc-lync-server-integration-1251_chapter_01001.html
retrieved_at: 2026-08-16T16:34:53.191130+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

Updated: November 27, 2025

Chapter: Microsoft Lync Server and Microsoft Lync Client Logging

## Chapter: Microsoft Lync Server and Microsoft Lync Client Logging

- Microsoft Lync Server and Microsoft Lync Client Logging

- Initiate Trace and View Microsoft Lync Server Log

- Enable and View Microsoft Lync Client Logs

# Microsoft Lync Server and Microsoft Lync Client Logging

The Lync Server Logging Tool allows you to initiate traces of the Lync server and view message logs. The Microsoft Lync client also allows you to collect logging information for SIP messaging and other client-related logging information.

## Initiate Trace and View Microsoft Lync Server Log

Use the following procedure to initiate a trace of the Microsoft Lync server and view the message logs.

Step 1

Select Start > All Programs > Microsoft Lync Server > Lync Server Logging Tool .

Step 2

In the Components area, check the   SIPStack check box.

Step 3

In the Level area, choose the All option.

Step 4

In the Flags area, check all the flags.

Step 5

When you are ready to being the trace, select Start Logging .

Step 6

When you are ready to stop the trace, select Stop Logging .

Step 7

Select Analyze Log Files .

Step 8

Check the SIPStack and the SIPStackPerf check boxes.

Step 9

Select Analyze .

Step 10

Select the Messages tab and click on any message to view its contents.

## Enable and View Microsoft Lync Client Logs

Use the following procedure to enable client logging and view the resulting logs.

Step 1

Select Start > All Programs > Microsoft Lync > Microsoft Lync Server .

Step 2

Click on the drop-down arrow on the top right of the window.

Step 3

Select Tools > Options .

Step 4

Select General from the left pane.

Step 5

In the Logging area, check the Turn on logging in Lync and Turn on Windows Event logging for Lync check boxes.

Step 6

Select OK .

Step 7

Exit the Lync client. Do not just sign out of the Lync client.

Step 8

Go to C:\Users\Administrator.NE001B-LYNCAD\Tracing> on your client computer.

Step 9

Select all files in this directory and delete them.

Step 10

Sign in to the Lync client.

Tip

You will see new files being created in C:\Users\Administrator.NE001B-LYNCAD\Tracing> .

Step 11

Complete a sign in or call attempt from the Lync client.

Step 12

Exit the Lync client.

Step 13

Open the Communicator-uccapi-0 file in C:\Users\Administrator.NE001B-LYNCAD\Tracing> .

The Communicator-uccapi-0 file contains logs for SIP messaging and other client-related logging information.

| Step 1 | Select Start > All Programs > Microsoft Lync Server > Lync Server Logging Tool . |
|---|---|
| Step 2 | In the Components area, check the   SIPStack check box. |
| Step 3 | In the Level area, choose the All option. |
| Step 4 | In the Flags area, check all the flags. |
| Step 5 | When you are ready to being the trace, select Start Logging . |
| Step 6 | When you are ready to stop the trace, select Stop Logging . |
| Step 7 | Select Analyze Log Files . |
| Step 8 | Check the SIPStack and the SIPStackPerf check boxes. |
| Step 9 | Select Analyze . |
| Step 10 | Select the Messages tab and click on any message to view its contents. |

| Step 1 | Select Start > All Programs > Microsoft Lync > Microsoft Lync Server . |
|---|---|
| Step 2 | Click on the drop-down arrow on the top right of the window. |
| Step 3 | Select Tools > Options . |
| Step 4 | Select General from the left pane. |
| Step 5 | In the Logging area, check the Turn on logging in Lync and Turn on Windows Event logging for Lync check boxes. |
| Step 6 | Select OK . |
| Step 7 | Exit the Lync client. Do not just sign out of the Lync client. |
| Step 8 | Go to C:\Users\Administrator.NE001B-LYNCAD\Tracing> on your client computer. |
| Step 9 | Select all files in this directory and delete them. |
| Step 10 | Sign in to the Lync client. Tip You will see new files being created in C:\Users\Administrator.NE001B-LYNCAD\Tracing> . | Tip | You will see new files being created in C:\Users\Administrator.NE001B-LYNCAD\Tracing> . |
| Tip | You will see new files being created in C:\Users\Administrator.NE001B-LYNCAD\Tracing> . |
| Step 11 | Complete a sign in or call attempt from the Lync client. |
| Step 12 | Exit the Lync client. |
| Step 13 | Open the Communicator-uccapi-0 file in C:\Users\Administrator.NE001B-LYNCAD\Tracing> . Note The Communicator-uccapi-0 file contains logs for SIP messaging and other client-related logging information. | Note | The Communicator-uccapi-0 file contains logs for SIP messaging and other client-related logging information. |
| Note | The Communicator-uccapi-0 file contains logs for SIP messaging and other client-related logging information. |

| Tip | You will see new files being created in C:\Users\Administrator.NE001B-LYNCAD\Tracing> . |
|---|---|

| Note | The Communicator-uccapi-0 file contains logs for SIP messaging and other client-related logging information. |
|---|---|