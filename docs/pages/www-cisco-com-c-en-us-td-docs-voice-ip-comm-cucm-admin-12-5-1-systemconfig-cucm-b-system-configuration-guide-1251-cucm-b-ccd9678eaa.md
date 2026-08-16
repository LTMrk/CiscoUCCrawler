---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-ccd9678eaa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111111.html
retrieved_at: 2026-08-16T17:33:57.646403+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Announcements

## Chapter: Configure Announcements

# Configure Announcements

## Announcements Overview

In Cisco Unified Communications Manager Administration, use the Menu Resources > Announcements menu path to configure announcements. There are two classifications of announcements:

- System Announcements—Pre-defined announcements that are used in normal call processing or provided as sample feature announcements.

- Feature Announcements—Used by features such as Music on Hold (MOH), Hunt Pilots with Call Queuing or External Call Control.
                                 You can customize your own feature announcements by uploading Cisco-provided audio files or uploading custom .wav files. Upload all custom announcement .wav files to all servers in the cluster.

You can hear custom announcements such as warning or reorder tones if you are connected through a trunk or gateway. However,
                                       you cannot hear custom announcements on calls between two IP phones or IP phones and Jabber clients.

### Formats

The recommended format for announcements includes the following specifications:

16-bit PCM wav file

Stereo or mono

Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz

### Default
                           	 Announcements

You can
                                 		  upload custom announcement .wav files or change the Cisco-provided file for a
                                 		  system announcement. However, you cannot change the announcement identifier.
                                 		  For example, the System announcement (VCA_00121) is played when a caller dials
                                 		  an invalid number. This is commonly known as the vacant call announcement.

Announcement Identifier

Description

Gone_00126

System:
                                             					 Gone

MLPP-BNEA_00123

System:
                                             					 MLPP Busy not equipped

MLPP-BPA_00122

System:
                                             					 MLPP Higher precedence

MLPP-ICA_00120

System:
                                             					 MLPP Service disruption

MLPP-PALA_00119

System:
                                             					 MLPP Precedence access limit

MLPP-UPA_00124

System:
                                             					 MLPP Unauthorized precedence

Mobility_VMA

Please
                                             					 press 1 to be connected

MonitoringWarning_00055

System:
                                             					 Monitoring or Recording

RecordingWarning_00038

System:
                                             					 Recording

TemporaryUnavailable_00125

System:
                                             					 Temporary unavailable

VCA_00121

System:
                                             					 Vacant number / invalid number dialed

Wait_In_Queue_Sample

Builtin:
                                             					 Sample queued caller periodic announcement

Welcome_Greeting_Sample

Builtin:
                                             					 Sample caller greeting

## Announcements
                        	 Configuration Task Flow

Step 1

Configure Announcement .

Configure an
                                          				announcement that you can use with features, such as Music On Hold (MoH) along
                                          				with Hunt Pilot call queuing or External Call Control.

Step 2

Upload a Customized Announcement .

Upload custom
                                          				announcement .wav files or change the Cisco-provided file for a system
                                          				announcement. However, you cannot change the announcement identifier. The
                                          				customized announcements are underlined with a hyperlink and appear in the Find
                                             				  and List Announcements window of Cisco Unified Communications
                                          				Manager.

### Configure
                           	 Announcement

You can configure
                                 		  an announcement that you can use as a system announcement or as a feature
                                 		  announcement. A system announcement is used for call processing or for the use
                                 		  of sample feature announcements whereas a feature announcement is used for
                                 		  specific features, such as music on hold (MOH) in association with hunt pilot
                                 		  call queuing or external call control.

You can modify an
                                 		  existing announcement or configure a new announcement in Cisco Unified
                                 		  Communications Manager.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Announcement .

Step 2

Do one of the following:

- Click Find and select an existing announcement to edit.

- Click Add New to add a new announcment.

Step 3

Configure the fields in the Announcement Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Upload a
                           	 Customized Announcement

You can modify a default announcement with an uploaded custom .wav file with a different announcement. When you import an
                                 audio source file, Unified Communications Manager processes the file and converts the file to the proper formats for use by
                                 the music on hold (MOH) server.

Announcements are specific to the locale (language). If your installation is using more than one language locale, you have
                                             to record each custom announcement each language as a separate .wav file and upload with the correct locale assignment. This
                                             task also requires that the correct locale package is installed on each server before uploading custom announcement .wav files
                                             for languages other than United States English.

Similar to MOH audio source files, the recommended format for announcements includes the following specifications:

16-bit PCM .wav file

Stereo or mono

Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz

You cannot update announcements that are not hyperlinked in the Find and List Announcements window in Unified Communications Manager. You can add customized announcements for Cisco-provided announcements that are
                                             underlined with a hyperlink in this window. For example, MLPP-ICA_00120 and MonitoringWarning_00055.

Step 1

From Cisco Unified CM
                                             				Administration , choose Media
                                                				  Resources > Announcement .

Step 2

From the Find
                                             				and List Announcements window, enter search criteria, click Find , and click the hyperlink for the announcement
                                          			 from the resulting list.

Step 3

From the Announcement Configuration window, click Upload File .

Step 4

From the Upload
                                             				File pop-up window, choose the locale, enter the filename and browse
                                          			 to select the .wav file, and click Upload
                                             				File .

The upload process begins and the status is updated after the processing is complete. Select Close to close the Upload File window.

Step 5

(Optional) If you want Unified Communications Manager to play the customized announcement instead of playing the Cisco-provided announcement, check the Enable check box appears in the Announcement by Locale pane in the Announcements Configuration window.

If the Enable check box is unchecked, Unified Communications Manager plays the Cisco-provided announcement.

Step 6

Click Save .

#### What to do next

Upload the
                                 		  announcement on each node in the cluster as the announcement files are not
                                 		  propagated between servers in a cluster. Browse for Cisco
                                    			 Unified Communications Manager Administration on each server in the
                                 		  cluster and repeat the upload process.

| Note | You can hear custom announcements such as warning or reorder tones if you are connected through a trunk or gateway. However,
                                       you cannot hear custom announcements on calls between two IP phones or IP phones and Jabber clients. |
|---|---|

| Announcement Identifier | Description |
|---|---|
| Gone_00126 | System:
                                             					 Gone |
| MLPP-BNEA_00123 | System:
                                             					 MLPP Busy not equipped |
| MLPP-BPA_00122 | System:
                                             					 MLPP Higher precedence |
| MLPP-ICA_00120 | System:
                                             					 MLPP Service disruption |
| MLPP-PALA_00119 | System:
                                             					 MLPP Precedence access limit |
| MLPP-UPA_00124 | System:
                                             					 MLPP Unauthorized precedence |
| Mobility_VMA | Please
                                             					 press 1 to be connected |
| MonitoringWarning_00055 | System:
                                             					 Monitoring or Recording |
| RecordingWarning_00038 | System:
                                             					 Recording |
| TemporaryUnavailable_00125 | System:
                                             					 Temporary unavailable |
| VCA_00121 | System:
                                             					 Vacant number / invalid number dialed |
| Wait_In_Queue_Sample | Builtin:
                                             					 Sample queued caller periodic announcement |
| Welcome_Greeting_Sample | Builtin:
                                             					 Sample caller greeting |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Announcement . | Configure an
                                          				announcement that you can use with features, such as Music On Hold (MoH) along
                                          				with Hunt Pilot call queuing or External Call Control. |
| Step 2 | Upload a Customized Announcement . | Upload custom
                                          				announcement .wav files or change the Cisco-provided file for a system
                                          				announcement. However, you cannot change the announcement identifier. The
                                          				customized announcements are underlined with a hyperlink and appear in the Find
                                             				  and List Announcements window of Cisco Unified Communications
                                          				Manager. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Announcement . |
|---|---|
| Step 2 | Do one of the following: Click Find and select an existing announcement to edit. Click Add New to add a new announcment. |
| Step 3 | Configure the fields in the Announcement Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Note | Announcements are specific to the locale (language). If your installation is using more than one language locale, you have
                                             to record each custom announcement each language as a separate .wav file and upload with the correct locale assignment. This
                                             task also requires that the correct locale package is installed on each server before uploading custom announcement .wav files
                                             for languages other than United States English. Similar to MOH audio source files, the recommended format for announcements includes the following specifications: 16-bit PCM .wav file Stereo or mono Sample rates of 48 kHz, 44.1 kHz, 32 kHz, 16 kHz, or 8 kHz You cannot update announcements that are not hyperlinked in the Find and List Announcements window in Unified Communications Manager. You can add customized announcements for Cisco-provided announcements that are
                                             underlined with a hyperlink in this window. For example, MLPP-ICA_00120 and MonitoringWarning_00055. |
|---|---|

| Step 1 | From Cisco Unified CM
                                             				Administration , choose Media
                                                				  Resources > Announcement . |
|---|---|
| Step 2 | From the Find
                                             				and List Announcements window, enter search criteria, click Find , and click the hyperlink for the announcement
                                          			 from the resulting list. |
| Step 3 | From the Announcement Configuration window, click Upload File . |
| Step 4 | From the Upload
                                             				File pop-up window, choose the locale, enter the filename and browse
                                          			 to select the .wav file, and click Upload
                                             				File . The upload process begins and the status is updated after the processing is complete. Select Close to close the Upload File window. |
| Step 5 | (Optional) If you want Unified Communications Manager to play the customized announcement instead of playing the Cisco-provided announcement, check the Enable check box appears in the Announcement by Locale pane in the Announcements Configuration window. If the Enable check box is unchecked, Unified Communications Manager plays the Cisco-provided announcement. |
| Step 6 | Click Save . |