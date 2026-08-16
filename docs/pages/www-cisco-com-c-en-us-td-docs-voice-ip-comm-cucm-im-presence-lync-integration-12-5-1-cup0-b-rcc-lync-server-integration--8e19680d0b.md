---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-12-5-1-cup0-b-rcc-lync-server-integration--8e19680d0b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/12_5_1/cup0_b_rcc-lync-server-integration-1251/cup0_b_rcc-lync-server-integration-1251_chapter_01001.html
retrieved_at: 2026-08-16T17:29:12.689774+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

Chapter: Microsoft Lync Server and Microsoft Lync Client Logging

## Chapter: Microsoft Lync Server and Microsoft Lync Client Logging

- Microsoft Lync Server and Microsoft Lync Client Logging

- Initiate Trace and View Microsoft Lync Server Log

- Enable and View Microsoft Lync Client Logs

# Microsoft Lync Server and Microsoft Lync Client Logging

The Lync Server Logging Tool allows you to initiate traces of the Lync server and view message logs. The Microsoft Lync client also allows you to collect logging information for SIP messaging and other client-related logging information.

## Initiate Trace and View Microsoft Lync Server Log

Use the following procedure to initiate a trace of the Microsoft Lync server and view the message logs.

Select Start > All Programs > Microsoft Lync Server > Lync Server Logging Tool .

In the Components area, check the   SIPStack check box.

In the Level area, choose the All option.

In the Flags area, check all the flags.

When you are ready to being the trace, select Start Logging .

When you are ready to stop the trace, select Stop Logging .

Select Analyze Log Files .

Check the SIPStack and the SIPStackPerf check boxes.

Select Analyze .

Select the Messages tab and click on any message to view its contents.

## Enable and View Microsoft Lync Client Logs

Use the following procedure to enable client logging and view the resulting logs.

Select Start > All Programs > Microsoft Lync > Microsoft Lync Server .

Click on the drop-down arrow on the top right of the window.

Select Tools > Options .

Select General from the left pane.

In the Logging area, check the Turn on logging in Lync and Turn on Windows Event logging for Lync check boxes.

Select OK .

Exit the Lync client. Do not just sign out of the Lync client.

Go to C:\Users\Administrator.NE001B-LYNCAD\Tracing> on your client computer.

Select all files in this directory and delete them.

Sign in to the Lync client.

You will see new files being created in C:\Users\Administrator.NE001B-LYNCAD\Tracing> .

Complete a sign in or call attempt from the Lync client.

Exit the Lync client.

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