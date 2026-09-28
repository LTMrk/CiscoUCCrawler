---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-010101--36bfe566e7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_010101.html
retrieved_at: 2026-08-17T02:29:48.081517+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting the Conversation

## Chapter: Troubleshooting the Conversation

# Troubleshooting the Conversation

Troubleshooting the Conversation

## Custom Keypad Mapping Not Taking Effect

When you use the Custom Key Map tool to customize the key mappings for the Cisco Unity Connection conversation, you must also
                           assign the Custom Keypad Mapping conversation to a user or group of users.

### Changing the
                           	 Conversation Style for a Single User

In Cisco Unity Connection Administration, expand Users and then select Users . On the Search Users page, select the alias of
                                          			 the user.

On the Edit menu, select Phone Menu .

In the Touchtone Conversation Menu Style list, select the
                                          			 applicable Custom Keypad Mapping and select Save .

### Specifying a
                           	 Custom Keypad Mapping Conversation for Multiple User Accounts at Once

In Cisco Unity Connection Administration, on the Search Users
                                          			 page, check the applicable user check boxes, and select Bulk Edit .

If the users that you want to edit in bulk do not all appear on
                                             				one Search page, check all applicable check boxes on the first page, then go to
                                             				the next page and check all applicable check boxes, and so on, until you have
                                             				selected all applicable users. Then select Bulk Edit .

On the Edit menu, select Phone Menu .

In the Touchtone Conversation Menu Style list, select the
                                          			 applicable Custom Keypad Mapping.

If applicable, set the Bulk Edit Task Scheduling fields to
                                          			 schedule the Bulk Edit operation for a later date and/or time and select Submit .

## Long Pauses After Listening to Help Menu

After playing a Help menu, Unity Connection waits for a key press. Users can press a key for the command they want, or press
                           0 to hear the Help menu of command options again.

## Determine the WAV File Played

To determine which WAV file is being played off from the hard disk, do the following procedures in the order given.

### Downloading the
                           	 Remote Port Status Monitor

In a web browser, go to the Cisco Unity Tools website at http://www.ciscounitytools.com .

In the Tool Update Log section, select Port Status Monitor .

On the Cisco Unified Communication Tools page for the Port
                                          			 Status Monitor, select Download Now .

Follow the on-screen instructions to download the Remote Port
                                          			 Status Monitor tool.

### Configuring Unity
                           	 Connection for the Remote Port Status Monitor

In Cisco Unity Connection Administration, expand System Settings > and then select Advanced > Conversations .

On the Conversation Configuration page, check the Enable Remote Port Status Monitor Output check box.

In the IP Addresses Allowed To Connect For Port Status Monitor
                                          			 Output field, enter the IP addresses of your workstations and select Save.

You can enter up to 70 IP addresses, separated by commas.

### Enabling the
                           	 PhraseServerToMonitor Micro Trace and View the WAV Filename

In Cisco Unity Connection Serviceability, on the Trace menu,
                                          			 select Micro Traces .

On the Micro Traces page, in the Server field, select the name
                                          			 of the Unity Connection server and select Go .

In the Micro Trace field, select PhraseServerToMonitor and select Go .

Check the check boxes for all levels and select Save .

On your workstation, start Remote Port Status Monitor.

Make a call to Unity Connection so that the WAV file is played.

The full path of the WAV files being played appears in the
                                             				Remote Port Status Monitor window.

In Cisco Unity Connection Serviceability, disable the traces
                                          			 that you enabled in Step 3 and Step 4 , then select Save .

| Step 1 | In Cisco Unity Connection Administration, expand Users and then select Users . On the Search Users page, select the alias of
                                          			 the user. |
|---|---|
| Step 2 | On the Edit menu, select Phone Menu . |
| Step 3 | In the Touchtone Conversation Menu Style list, select the
                                          			 applicable Custom Keypad Mapping and select Save . |

| Step 1 | In Cisco Unity Connection Administration, on the Search Users
                                          			 page, check the applicable user check boxes, and select Bulk Edit . If the users that you want to edit in bulk do not all appear on
                                             				one Search page, check all applicable check boxes on the first page, then go to
                                             				the next page and check all applicable check boxes, and so on, until you have
                                             				selected all applicable users. Then select Bulk Edit . |
|---|---|
| Step 2 | On the Edit menu, select Phone Menu . |
| Step 3 | In the Touchtone Conversation Menu Style list, select the
                                          			 applicable Custom Keypad Mapping. |
| Step 4 | If applicable, set the Bulk Edit Task Scheduling fields to
                                          			 schedule the Bulk Edit operation for a later date and/or time and select Submit . |

| Step 1 | In a web browser, go to the Cisco Unity Tools website at http://www.ciscounitytools.com . |
|---|---|
| Step 2 | In the Tool Update Log section, select Port Status Monitor . |
| Step 3 | On the Cisco Unified Communication Tools page for the Port
                                          			 Status Monitor, select Download Now . |
| Step 4 | Follow the on-screen instructions to download the Remote Port
                                          			 Status Monitor tool. |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > and then select Advanced > Conversations . |
|---|---|
| Step 2 | On the Conversation Configuration page, check the Enable Remote Port Status Monitor Output check box. |
| Step 3 | In the IP Addresses Allowed To Connect For Port Status Monitor
                                          			 Output field, enter the IP addresses of your workstations and select Save. Note You can enter up to 70 IP addresses, separated by commas. | Note | You can enter up to 70 IP addresses, separated by commas. |
| Note | You can enter up to 70 IP addresses, separated by commas. |

| Note | You can enter up to 70 IP addresses, separated by commas. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, on the Trace menu,
                                          			 select Micro Traces . |
|---|---|
| Step 2 | On the Micro Traces page, in the Server field, select the name
                                          			 of the Unity Connection server and select Go . |
| Step 3 | In the Micro Trace field, select PhraseServerToMonitor and select Go . |
| Step 4 | Check the check boxes for all levels and select Save . |
| Step 5 | On your workstation, start Remote Port Status Monitor. |
| Step 6 | Make a call to Unity Connection so that the WAV file is played. The full path of the WAV files being played appears in the
                                             				Remote Port Status Monitor window. |
| Step 7 | In Cisco Unity Connection Serviceability, disable the traces
                                          			 that you enabled in Step 3 and Step 4 , then select Save . |