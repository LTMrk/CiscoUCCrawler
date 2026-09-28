---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-1f9a5f1a24
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01001100.html
retrieved_at: 2026-08-21T09:15:28.522933+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Tool for Auto-Registered Phone Support (TAPs) User Locales

## Chapter: Tool for Auto-Registered Phone Support (TAPs) User Locales

# Tool for Auto-Registered Phone Support (TAPs) User Locales

The chapter provides information to add or remove languages for
                        		TAPS prompts.

You have to select at least one user locale for TAPS to work.
                        		Use the Locale Installer to install user locale support. For more information
                        		on the Cisco Unified Communications Manager Locale Installer, refer to the specific locale
                        		installer documentation.

## User Locales for Tool for Auto-Registered Phone Support

Administrators can specify the languages for TAPs voice
                              		  prompts by using the User Locales for TAPS option. You can configure user
                              		  prompts for TAPS in several languages.

You must run the Locale Installer to install user locale
                              		  support.

The  TAPS user locales installed  in Cisco Unified Communications Manager will automatically be copied to the Cisco Unified Contact Center Express when a TAPS call is made. The TAPS user locales
                                          are not available on the Prompt Management page of Cisco Unified Contact Center Express.

Using the locale installer ensures that you have the latest
                              		  translated text, translated voice prompts, country-specific phone tones, and
                              		  country-specific gateways tones that are available for the phones. For more
                              		  information on the Cisco Unified Communications Manager Locale Installer, refer to the specific locale
                              		  installer documentation.

You have to select at least one user locale for TAPS to work.

## Add Languages to Tool for Auto-Registered Phone Support Prompts

You can add languages for TAPS prompts.

Step 1

In the Cisco Unified Communications Manager Administration window, choose Bulk
                                             				  Administration > TAPS > User Locales
                                             				  for TAPS .

Step 2

In the User Locales list box, choose the languages
                                       			 that you want to use for user prompts. Click the arrow to move the chosen
                                       			 language to the Selected User Locales list box.

The User Locales list box is the list of
                                          				languages that are installed on Cisco Unified Communications Manager .

You can choose, a maximum of twenty, languages as you need
                                             				for user prompts and move them to the Selected User Locales list box.

If the language that you want does not appear, you must download the Locale Installer from cisco.com and install it on your
                                                      cluster nodes.

All the languages that you add to the Locales pane are offered
                                                      				  as options to the user. The order of the locales in the Locales pane does not
                                                      				  matter because users set the support prompt language preference on their phone.

Step 3

After you have chosen the languages for user prompts, click Save to create a job.

Step 4

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Remove Languages From Tool for Auto-Registered Phone Support Prompts

You can remove languages for TAPS prompts.

Step 1

Choose Bulk Administration > TAPS > User Locales for TAPS .

Step 2

In the Selected User Locales list box, choose the
                                       			 language that you want to remove. Click the arrow to move the chosen language
                                       			 to the User Locales list box.

The Selected User Locales list box is the list
                                          				of languages that is chosen for user prompts. You can choose one or many
                                          				languages from user prompts and move them to the User Locales list box.

Step 3

Click Save .

### What to do next

To return to the TAPS Options window, click Back .

## Select Language of TAPs Prompts on New Phone

End users can select the language of TAPs prompts for their
                              		  phones.

Step 1

Plug the phone into a port.

The phone automatically registers and displays a number.

It takes around 20-25 seconds for downloading phone profile and
                                                      				  making necessary updates in first node and directory.

Step 2

Dial the CTI Route Point number provided by your system
                                       			 administrator and follow the prompts.

Step 3

Dial the TAPS extension that your system administrator provided.

Step 4

A voice prompts you to choose the language that you want to use.
                                       			 Choose appropriately.

Step 5

Dial your personal extension number, that your system
                                       			 administrator provided, followed by #.

You may be instructed to enter the complete telephone number
                                                      				  (including area code).

Step 6

To confirm, enter your personal extension number again, followed
                                       			 by # .

Step 7

You will receive confirmation prompt.

Step 8

Hang up the phone.

The phone resets and displays your extension number.

### What to do next

If you experience any problems, contact your system
                              		  administrator.

## Topics Related to Tool for Auto-Registered Phone Support User Locales

| Note | The  TAPS user locales installed  in Cisco Unified Communications Manager will automatically be copied to the Cisco Unified Contact Center Express when a TAPS call is made. The TAPS user locales
                                          are not available on the Prompt Management page of Cisco Unified Contact Center Express. |
|---|---|

| Note | You have to select at least one user locale for TAPS to work. |
|---|---|

| Step 1 | In the Cisco Unified Communications Manager Administration window, choose Bulk
                                             				  Administration > TAPS > User Locales
                                             				  for TAPS . The User Locales Configuration window displays. |
|---|---|
| Step 2 | In the User Locales list box, choose the languages
                                       			 that you want to use for user prompts. Click the arrow to move the chosen
                                       			 language to the Selected User Locales list box. The User Locales list box is the list of
                                          				languages that are installed on Cisco Unified Communications Manager . You can choose, a maximum of twenty, languages as you need
                                             				for user prompts and move them to the Selected User Locales list box. Note If the language that you want does not appear, you must download the Locale Installer from cisco.com and install it on your
                                                      cluster nodes. Note All the languages that you add to the Locales pane are offered
                                                      				  as options to the user. The order of the locales in the Locales pane does not
                                                      				  matter because users set the support prompt language preference on their phone. | Note | If the language that you want does not appear, you must download the Locale Installer from cisco.com and install it on your
                                                      cluster nodes. | Note | All the languages that you add to the Locales pane are offered
                                                      				  as options to the user. The order of the locales in the Locales pane does not
                                                      				  matter because users set the support prompt language preference on their phone. |
| Note | If the language that you want does not appear, you must download the Locale Installer from cisco.com and install it on your
                                                      cluster nodes. |
| Note | All the languages that you add to the Locales pane are offered
                                                      				  as options to the user. The order of the locales in the Locales pane does not
                                                      				  matter because users set the support prompt language preference on their phone. |
| Step 3 | After you have chosen the languages for user prompts, click Save to create a job. |
| Step 4 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | If the language that you want does not appear, you must download the Locale Installer from cisco.com and install it on your
                                                      cluster nodes. |
|---|---|

| Note | All the languages that you add to the Locales pane are offered
                                                      				  as options to the user. The order of the locales in the Locales pane does not
                                                      				  matter because users set the support prompt language preference on their phone. |
|---|---|

| Step 1 | Choose Bulk Administration > TAPS > User Locales for TAPS . The Select User Locales window displays. |
|---|---|
| Step 2 | In the Selected User Locales list box, choose the
                                       			 language that you want to remove. Click the arrow to move the chosen language
                                       			 to the User Locales list box. The Selected User Locales list box is the list
                                          				of languages that is chosen for user prompts. You can choose one or many
                                          				languages from user prompts and move them to the User Locales list box. |
| Step 3 | Click Save . A status message indicates that the update is complete. |

| Step 1 | Plug the phone into a port. The phone automatically registers and displays a number. Note It takes around 20-25 seconds for downloading phone profile and
                                                      				  making necessary updates in first node and directory. | Note | It takes around 20-25 seconds for downloading phone profile and
                                                      				  making necessary updates in first node and directory. |
|---|---|---|---|
| Note | It takes around 20-25 seconds for downloading phone profile and
                                                      				  making necessary updates in first node and directory. |
| Step 2 | Dial the CTI Route Point number provided by your system
                                       			 administrator and follow the prompts. |
| Step 3 | Dial the TAPS extension that your system administrator provided. |
| Step 4 | A voice prompts you to choose the language that you want to use.
                                       			 Choose appropriately. |
| Step 5 | Dial your personal extension number, that your system
                                       			 administrator provided, followed by #. Note You may be instructed to enter the complete telephone number
                                                      				  (including area code). | Note | You may be instructed to enter the complete telephone number
                                                      				  (including area code). |
| Note | You may be instructed to enter the complete telephone number
                                                      				  (including area code). |
| Step 6 | To confirm, enter your personal extension number again, followed
                                       			 by # . |
| Step 7 | You will receive confirmation prompt. |
| Step 8 | Hang up the phone. The phone resets and displays your extension number. |

| Note | It takes around 20-25 seconds for downloading phone profile and
                                                      				  making necessary updates in first node and directory. |
|---|---|

| Note | You may be instructed to enter the complete telephone number
                                                      				  (including area code). |
|---|---|