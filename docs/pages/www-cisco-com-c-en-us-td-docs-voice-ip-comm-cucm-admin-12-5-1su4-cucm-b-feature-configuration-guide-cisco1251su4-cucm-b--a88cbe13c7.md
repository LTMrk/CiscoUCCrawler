---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-b--a88cbe13c7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0111001.html
retrieved_at: 2026-08-16T17:01:36.680600+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Configure Call Queuing

## Chapter: Configure Call Queuing

# Configure Call Queuing

## Call Queuing Overview

Unified Communications Manager provides Call Queuing to place callers in a queue until hunt members are available to answer
                              them. An administrator can set the default so callers receive an initial greeting announcement before the call is extended
                              to an agent or the default can be changed so the initial announcement plays only after the caller is put in the queue followed
                              by Music On Hold or Tone On Hold. If the caller remains in queue for a specified period of time, a secondary announcement
                              is played at a configured interval until the call can be answered or until the maximum wait timer expires.

When an incoming call reaches the hunt pilot, the following functions are provided:

A caller may be connected to an initial customizable greeting announcement before proceeding.

If one or more line members are logged in to the hunt pilot and are in an idle state, and if no calls are queued, the call
                                    is extended to the line member that has been idle for the longest period of time.

If no line members answer a call, that caller is not placed in queue. The call is routed to a new destination or disconnected,
                                    based on the setting When no hunt members answer, are logged in, or registered.

If a line member does not answer a queue-enabled call, that line member is logged off the hunt group only if the setting Automatically Logout Hunt Member on No Answer is selected in the Line Group setting window.

Calls are placed in queue only if all members are busy.

A caller who is waiting in queue may hear Music On Hold and a repeating (customizable) periodic announcement.

After a line member becomes idle, the caller with the longest wait time across multiple hunt groups is extended to the idle
                                    line member. If the idle line member does not answer the call, the caller is returned to the previous position in the queue.

If a queued call exceeds its maximum wait time or the maximum number of callers allowed in queue is exceeded, the call can
                                    be routed to an alternate number or it can be disconnected, depending on how the hunt pilot is configured. The alternate number
                                    can be one of the following:

A hunt pilot DN with queuing either enabled or disabled

A voicemail DN

A line DN

A shared DN

Line members can display the queue status of their queue-enabled hunt pilots. The queue status display provides the following
                                    types of information:

Hunt pilot pattern

Number of queued callers on each hunt pilot

Longest waiting time

Call queuing works in conjunction with existing hunt pilots, but there are no changes in the behavior of the hunting operation
                              for either queuing or nonqueuing hunt pilots. Hunt pilots that have call queuing enabled provide the following features:

Queuing-enabled hunt pilot calls can only be received by line members one call at a time. Two queuing-enabled hunt pilot calls
                                    cannot be offered to a line member. A line member can receive calls directly to the DN or from non-queuing hunt pilots.

Line members who do not answer calls that are routed by hunt pilots are automatically logged out. A line member is automatically
                                    logged out of a device if the line member receives a queuing-enabled hunt pilot call and does not answer the call before timeout
                                    occurs. In the case of a shared-line deployment, all devices configured with the same shared line are logged out. You can
                                    configure this behavior from the Line Group setting window by selecting Automatically Logout Hunt Member on No Answer. Line
                                    members are logged out only if this check box is checked.

For information about Call Queuing monitoring or announcements monitoring, see Cisco Unified Real Time Monitoring Tool Administration Guide .

You can configure the inbound calls to change to the connected call state before playing the queuing announcement while the
                              call is extended to a hunt member in the queuing-enabled hunt pilot.

## Call Queuing Prerequisites

Cisco IP Voice Media Streaming (IPVMS) Application, which should be activated on at least one node in the cluster

Cisco CallManager service that is running on at least one server in the cluster

Cisco RIS Data Collector service that is running on the same server as the Cisco CallManager service

Cisco Unified Communications Manager Locale Installer, if you want to use non-English phone locales or country-specific tones

## Call Queuing Task Flow

Step 1

Configure Announcements

Configure announcements through uploading .wav files.

Step 2

Configure Music On Hold

Configure Music On Hold (MoH) audio source.

Step 3

Configure Hunt Pilot Queuing

Enables call queuing hold option for the calls in a queue until they are answered.

Step 4

Automatically Logout Hunt Member on No Answer

Allows line members to log off the hunt list automatically.

### Configure Announcements

Cisco Unified Communications Manager allows you to:

use the existing Cisco-provided announcements,

change the message or tone that you want an announcement to play,

insert custom announcement .wav files,

assign the locale for the announcement,

change the description for the announcement,

change the message or tone that you want an announcement to play.

Feature announcements are used by specific features such as Music On Hold (MoH) in association with Hunt Pilot call queuing
                                 or External Call Control.

There are up to 50 feature announcements available. These announcements can be Cisco-provided audio files or uploaded custom
                                 .wav files.

All custom announcement .wav files must be uploaded to all servers in the cluster.

Step 1

In Cisco Unified Communications Manager, select Media Resources > Announcements .

Step 2

Select a hyperlink to the announcement you want to use.

#### Example:

Step 3

To upload a .wav file to use as a custom announcement, click Upload File .

Step 4

In the Upload File window, choose the locale, enter the filename or browse to select the .wav file, and click Upload File .

The upload process begins, and may take a few minutes depending on the file. The Status is updated after processing is complete.

Step 5

Click Close to close the upload window.

Step 6

To play the customized announcement, ensure that the Enable check box is checked in the Announcement by Locale pane in the Announcements Configuration window.

Step 7

After you make the changes in the Announcements Configuration window, click Save .

#### What to do next

### Configure Music On Hold

You can configure Music On Hold (MoH) to play an optional initial greeting announcement when a caller is first put on hold
                                 and also to play a periodic repeating announcement. These announcements can use one of the Cisco-provided audio files or a
                                 file that is uploaded into the system.

Perform the following procedure to add or update a Music On Hold audio source, to associate an existing audio source with
                                 an audio stream number, or to upload a new custom audio source.

Step 1

From the Cisco Unified Communications Manager, choose Media Resources > Music On Hold Audio Source .

The Find and List Music On Hold Audio Sources window appears.

Step 2

To add a new Music On Hold audio source, click Add New . To update a Music On Hold audio source, locate a specific Music On Hold audio source. Based on the search criteria you specify,
                                          the system displays search results for the record that matches all the criteria.

Step 3

Enter the appropriate settings, as described in Audio Source Fields for Music On Hold .

Step 4

Click Save.

#### Audio Source Fields for Music On Hold

Field

Description

MOH Audio Stream Number

Use this field to choose the stream number for this MOH audio source. Click the drop-down list and choose a value from the
                                                list. For existing MOH audio sources, the value appears in the MOH Audio Source title.

MOH Audio Source File

Use this field to choose the file for this MOH audio source. Click the drop-down list and choose a value.

MOH Audio Source Name

Enter a unique name in this field for the MOH audio source. This name includes up to 50 valid characters, such as letters,
                                                numbers, spaces, dashes, dots (periods), and underscores.

Allow Multicasting

Check this check box to specify that the selected MOH audio source allows multicasting.

MOH Audio Source File Status

This pane displays the following information about the source file for the selected MOH audio source:

InputFileName

ErrorCode

ErrorText

DurationSeconds

DiskSpaceKB

LowDateTime

HighDateTime

OutputFileList

MOH Audio Translation completion date

Field

Description

Initial Announcement

Choose an initial announcement from the drop-down list.

To select MoH with no initial announcement, choose the Not Selected option.

Click the View Details link to view the following Initial Announcement information:

Announcement Identifier

Description

Default Announcement

Played by MOH server only when the Audio Source Allow Multi-casting is not checked and the Initial Announcement for queuing-enabled hunt pilot calls field is set to Play announcement if call is queued .

Played by ANN if Allow Multi-casting check box is checked or if Initial Announcement for queuing-enabled hunt pilot calls is set to Play announcement before routing to Hunt Member .

Initial Announcement for queuing-enabled hunt pilot calls

Choose one of the following to determine when to play the initial announcement:

Play announcement before routing to Hunt Member

Play announcement if call is queued

Periodic Announcement

Choose a periodic announcement from the drop-down list.

To select MoH with no periodic announcement, choose the Not Selected option.

Click the View Details link to view the following Periodic Announcement information:

Announcement Identifier

Description

Default Announcement

Periodic Announcement Interval

Enter a value (in seconds) that specifies the periodic announcement interval. Valid values are 10 to 300. The default value
                                                is 30.

Locale Announcement

Locale Announcement depends upon the locale installation package that has been installed.

Prompts played by MOH will use the setting for Locale Announcement.

Prompts played by ANN will use the User Locale of the calling party.

Field

Description

(list of MoH audio sources)

This list box shows the MOH audio source that you add. Select the audio stream number of an MOH audio source to configure
                                                that MoH audio source.

Audio source ID is an ID that represents an audio source in the Music On Hold server. The audio source can include either
                                                a file on a disk or a fixed device from which a source stream Music On Hold server obtains the streaming data. An MOH server
                                                can support up to 51 audio source IDs. Each audio source, represented by an audio source ID, can stream as unicast and multicast
                                                mode, if needed.

If you select <None> , the system default MoH audio source service parameter ( Default Network Hold MoH Audio Source ID ) is used for the MoH audio source.

Upload File

To upload an MOH audio source file that does not appear in the drop-down list, click Upload File . In the Upload File window, either enter the path of an audio source file or navigate to the file by clicking Browse . After you locate the audio source file, click the Upload File button to complete the upload. After the audio file gets uploaded, the Upload Result window displays the result of the upload.
                                                Click Close to close this window.

When you upload a file, the file is uploaded to the Unified Communications Manager server and performs audio conversions to
                                                            create codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes
                                                            to complete.

Uploading an audio source file to an MOH server uploads the file only to one MOH server. You must upload an audio source file
                                                            to each MOH server in a cluster by using Cisco Unified Communications Manager Administration on each server. MOH audio source files do not automatically propagate to other MOH servers in a cluster.

### Configure Hunt Pilot Queuing

When a hunt pilot has more calls distributed through the call distribution feature than its hunt members can handle at any
                                 given time, call queuing holds these calls in a queue until they can be answered.

When queuing is enabled, both Forward Hunt No Answer and Forward Hunt Busy are automatically disabled. Conversely, if Forward
                                 Hunt No Answer or Forward Hunt Busy is enabled, queuing is automatically disabled.

Step 1

In Cisco Unified Communications Manager Administration, select Call Routing > Route/Hunt > Hunt Pilot to configure hunt pilots.

Step 2

Select the hunt pilot that you need to configure for Queuing.

Step 3

Navigate to the Queuing section of the Hunt Pilot Configuration window.

Step 4

Check the Queue Calls check box to enable queuing.

Step 5

Choose a Music On Hold (MoH) source from the drop-down list box to be used to play announcements and provide queue hold treatments.

The MoH source can be configured as unicast or multicast. The caller-side Media Resource Group List (MRGL) takes precedence
                                             for multicast or unicast.

If you do not select a source, the default Network Hold MoH/MoH Source and Announcements is used.

The MoH source announcement locale is used to determine the language used for the announcement. Only one type of language
                                             announcement can be played per hunt pilot.

Step 6

In the Maximum Number of Callers Allowed in Queue field, enter an integer value for the number of callers allowed in the queue for this hunt pilot.

Step 7

Choose one of the following options when the maximum number of callers in the queue is reached:

- If you want subsequent calls to be disconnected, select Disconnect the call .

- If you want subsequent calls to be routed to a secondary destination, select Route the call to this destination . Provide a specific device DN, shared line DN, or another hunt pilot DN.

- (Optional) You may also select Full Queue Calling Search Space from the drop-down list. Used to determine which partition to search when attempting to complete a call.

Step 8

In the Maximum Wait Time in Queue field, enter an integer value to set the maximum wait time, in seconds, in a queue.

Step 9

Choose one of the following options when the maximum wait time is reached:

- If you want that call to be disconnected, select Disconnect the call .

- If you want that call to be routed to a secondary destination, select Route the call to this destination . Provide a specific device DN, shared line DN, or another hunt pilot DN.

- (Optional) You may also select Maximum Wait Time Calling Search Space from the drop-down list. Used to determine which partition to search when attempting to complete a call.

Step 10

When no line members are logged in or registered at the time of an incoming call, choose one of the following options:

- If you need that call to be disconnected, select Disconnect the call .

- If you need that call to be routed to a secondary destination, select Route the call to this destination . Provide a specific device DN, shared line DN, or another hunt pilot DN.

- (Optional) You may also select No hunt members logged in or registered Calling Search Space from the drop-down list. Used to determine which partition to search when attempting to complete a call.

Step 11

Click Save .

### Automatically Logout Hunt Member on No Answer

Allows line members to log off the hunt list automatically. If an agent does not answer a queuing-enabled hunt pilot call,
                                 that agent will be logged off of the hunt group and will not receive additional hunt pilot calls unless he presses the "HLOG"
                                 soft key on the phone to log into the hunt pilot.

Line members can log back in using the "HLOG" softkey or PLK.

Step 1

In Cisco Unified Communications Manager Administration, choose Call Routing > Route/Hunt > Line Group to configure line groups.

Step 2

Choose the line group that you need to configure from the Find and List Line Groups window.

Step 3

Navigate to the Hunt Options section of the Line Group Configuration window.

Step 4

Ensure that the Automatically Logout Hunt Member on No Answer check box is checked.

Step 5

Click Save .

## Call Queuing Interactions

SIP Rel1XX Options

If a call is routed to a queuing-enabled hunt pilot through SIP ICT, the SIP ICT uses the SIP profile that has SIP Rel1XX
                                          Options set to Send PRACK if 1XX contains SDP . As a result, the initial announcement is played to every call before the call is extended to the line member.

The above existing interaction for SIP ICT does not apply if Connect Inbound Call before Playing Queuing Announcement checkbox is checked under Device Device Settings SIP Profile > Trunk Specific Configuration in Cisco Unified CM Administration.

If Connect Inbound Call before Playing Queuing Announcement checkbox is not checked the interaction for SIP ICT remains the same. However, it does not guarantee the initial announcement
                                          can always be heard by a caller from the PSTN side. The initial announcement will not be heard by a caller from the PSTN side
                                          if the PSTN provider doesn't open the voice path until a Connect message is received on the call.

Hunt Pilots and Hunt Groups

The logoff notification functionality for hunt groups changes when Call Queuing is enabled for a hunt pilot. If Call Queuing
                                                is enabled for a hunt pilot, the Hunt Group Logoff Notification does not play when users log out of a hunt group or are logged
                                                off because they missed their turn in the queue.

If the hunt list has multiple line groups, these line groups must have the same setting for Automatically Logout Hunt Member on No Answer .

Hunt Pilot still queues calls, even when all hunt members are logged out.The line group members should not be added in more
                                                than one line group and even if they are added in second line groups, those second line groups should not be in the same Hunt
                                                list.

All hunt options must be set to Try Next Member, then Try Next Group in the hunt list.

## Call Queuing Restrictions

The following general restrictions apply to call queuing:

H.323 Fast Start does not support Call Queuing.

Queue status PLK is supported only with the following LCD display phones for both SCCP and SIP: 6921, 6941, 6945, 6961, 7911G,
                                    7931G, 7942G, 7945G, 7962G, 7965G, 7975G, 8961, 8945, 8941, 9951, 9971, 7800 and 8800 series.

Log Out of Hunt Groups (HLog) is not compatible with Cisco Extension Mobility Cross Cluster (EMCC); Call Queuing should not
                                    be deployed with EMCC.

Unified Communications Manager does not support Unified Mobility with Call Queuing.

In a H323 to
                                    				SIP interworking scenario, the user may not hear initial announcement, MoH,
                                    				periodic announcement or observe call failure in a native call queuing flow due
                                    				to interworking delays. In such a scenario it is advised to use only SIP
                                    				protocol.

## Performance and Scalability for Hunt Pilots with Call Queuing

The following performance and scalability restrictions apply:

A single Unified CM Cluster supports a maximum of
                                    15,000 hunt list devices.

A single Unified CM Subscriber supports a maximum of
                                    100 hunt pilots with call queuing enabled per node

Hunt list devices may be a combination of 1500 hunt
                                    lists with ten IP phones in each hunt list, 750 hunt lists with
                                    twenty IP phones in each hunt list, or similar combinations

When using the broadcast algorithm for call coverage, the number of
                                                hunt list devices is limited
                                                by the number of busy hour call attempts (BHCA). Note that a BHCA
                                                of 10 on a hunt pilot
                                                pointing to a hunt list or hunt group containing 10 phones and
                                                using the broadcast algorithm is
                                                equivalent to 10 phones with a BHCA of 10.

The maximum number of hunt pilots is 100 per Unified CM subscriber node with call queue enabled when configured with 32 callers
                                    which is allowed in the queue. The total number of queue slots per node (the value of "Maximum Number of Callers Allowed in
                                    Queue" for all Call Queuing Enabled Hunt Pilots on the node combined) is limited to 3200. The maximum number of simultaneous
                                    callers in a queue for each hunt pilot is 100, meaning 100 callers per hunt pilot is allowed in a queue and the maximum number
                                    of hunt pilots is reduced to 32. The maximum number of members across all hunt lists does not change when call queuing is
                                    enabled.

The maximum wait time in queue for each hunt pilot that you can
                                    configure ranges from 0 to 3600 seconds (default 900). An increase in the number of hunt lists can require you to
                                    increase the dial plan initialization timer that is specified in
                                    the Unified Communications Manager service parameters. We recommend
                                    that you set the dial plan initialization timer to 600 seconds if
                                    you have 1500 hunt lists configured.

We recommend having no more than 35 directory numbers for a
                                    single line group when using broadcast algorithms with call
                                    queuing. Additionally, the number
                                    of broadcast line groups depends
                                    on the busy hour call completion rate (BHCC). If there are multiple broadcast line groups in a
                                    Unified CM system, the number of
                                    maximum directory numbers in a line group must be less than 35. The
                                    number of busy hour call
                                    attempts (BHCA) for all the broadcast line groups should not exceed
                                    35 calls set up per second.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Announcements | Configure announcements through uploading .wav files. |
| Step 2 | Configure Music On Hold | Configure Music On Hold (MoH) audio source. |
| Step 3 | Configure Hunt Pilot Queuing | Enables call queuing hold option for the calls in a queue until they are answered. |
| Step 4 | Automatically Logout Hunt Member on No Answer | Allows line members to log off the hunt list automatically. |

| Step 1 | In Cisco Unified Communications Manager, select Media Resources > Announcements . The Find and List Announcements window displays. |
|---|---|
| Step 2 | Select a hyperlink to the announcement you want to use. Example: Hyperlink—Wait_In_Queue_Sample You can edit the announcement description or choose a customized announcement if uploaded. |
| Step 3 | To upload a .wav file to use as a custom announcement, click Upload File . The Upload File window opens. |
| Step 4 | In the Upload File window, choose the locale, enter the filename or browse to select the .wav file, and click Upload File . The upload process begins, and may take a few minutes depending on the file. The Status is updated after processing is complete. |
| Step 5 | Click Close to close the upload window. The Announcement Configuration window refreshes to update the uploaded file status. |
| Step 6 | To play the customized announcement, ensure that the Enable check box is checked in the Announcement by Locale pane in the Announcements Configuration window. |
| Step 7 | After you make the changes in the Announcements Configuration window, click Save . |

| Step 1 | From the Cisco Unified Communications Manager, choose Media Resources > Music On Hold Audio Source . The Find and List Music On Hold Audio Sources window appears. |
|---|---|
| Step 2 | To add a new Music On Hold audio source, click Add New . To update a Music On Hold audio source, locate a specific Music On Hold audio source. Based on the search criteria you specify,
                                          the system displays search results for the record that matches all the criteria. |
| Step 3 | Enter the appropriate settings, as described in Audio Source Fields for Music On Hold . |
| Step 4 | Click Save. The list box at the bottom of the window shows the new Music On Hold audio source. The MOH Audio Source File Status pane
                                          shows the MOH audio translation status for the added source. |

| Field | Description |
|---|---|
| MOH Audio Stream Number | Use this field to choose the stream number for this MOH audio source. Click the drop-down list and choose a value from the
                                                list. For existing MOH audio sources, the value appears in the MOH Audio Source title. |
| MOH Audio Source File | Use this field to choose the file for this MOH audio source. Click the drop-down list and choose a value. |
| MOH Audio Source Name | Enter a unique name in this field for the MOH audio source. This name includes up to 50 valid characters, such as letters,
                                                numbers, spaces, dashes, dots (periods), and underscores. |
| Allow Multicasting | Check this check box to specify that the selected MOH audio source allows multicasting. |
| MOH Audio Source File Status | This pane displays the following information about the source file for the selected MOH audio source: InputFileName ErrorCode ErrorText DurationSeconds DiskSpaceKB LowDateTime HighDateTime OutputFileList MOH Audio Translation completion date Note OutputFileList includes information on ULAW, ALAW, G.729, and Wideband wav files and status options. | Note | OutputFileList includes information on ULAW, ALAW, G.729, and Wideband wav files and status options. |
| Note | OutputFileList includes information on ULAW, ALAW, G.729, and Wideband wav files and status options. |

| Note | OutputFileList includes information on ULAW, ALAW, G.729, and Wideband wav files and status options. |
|---|---|

| Field | Description |
|---|---|
| Initial Announcement | Choose an initial announcement from the drop-down list. Note To select MoH with no initial announcement, choose the Not Selected option. Click the View Details link to view the following Initial Announcement information: Announcement Identifier Description Default Announcement Note Played by MOH server only when the Audio Source Allow Multi-casting is not checked and the Initial Announcement for queuing-enabled hunt pilot calls field is set to Play announcement if call is queued . Played by ANN if Allow Multi-casting check box is checked or if Initial Announcement for queuing-enabled hunt pilot calls is set to Play announcement before routing to Hunt Member . | Note | To select MoH with no initial announcement, choose the Not Selected option. | Note | Played by MOH server only when the Audio Source Allow Multi-casting is not checked and the Initial Announcement for queuing-enabled hunt pilot calls field is set to Play announcement if call is queued . Played by ANN if Allow Multi-casting check box is checked or if Initial Announcement for queuing-enabled hunt pilot calls is set to Play announcement before routing to Hunt Member . |
| Note | To select MoH with no initial announcement, choose the Not Selected option. |
| Note | Played by MOH server only when the Audio Source Allow Multi-casting is not checked and the Initial Announcement for queuing-enabled hunt pilot calls field is set to Play announcement if call is queued . Played by ANN if Allow Multi-casting check box is checked or if Initial Announcement for queuing-enabled hunt pilot calls is set to Play announcement before routing to Hunt Member . |
| Initial Announcement for queuing-enabled hunt pilot calls | Choose one of the following to determine when to play the initial announcement: Play announcement before routing to Hunt Member Play announcement if call is queued |
| Periodic Announcement | Choose a periodic announcement from the drop-down list. Note To select MoH with no periodic announcement, choose the Not Selected option. Click the View Details link to view the following Periodic Announcement information: Announcement Identifier Description Default Announcement Note The MOH server always plays the periodic announcement regardless of other settings. | Note | To select MoH with no periodic announcement, choose the Not Selected option. | Note | The MOH server always plays the periodic announcement regardless of other settings. |
| Note | To select MoH with no periodic announcement, choose the Not Selected option. |
| Note | The MOH server always plays the periodic announcement regardless of other settings. |
| Periodic Announcement Interval | Enter a value (in seconds) that specifies the periodic announcement interval. Valid values are 10 to 300. The default value
                                                is 30. |
| Locale Announcement | Locale Announcement depends upon the locale installation package that has been installed. Note Prompts played by MOH will use the setting for Locale Announcement. Prompts played by ANN will use the User Locale of the calling party. | Note | Prompts played by MOH will use the setting for Locale Announcement. Prompts played by ANN will use the User Locale of the calling party. |
| Note | Prompts played by MOH will use the setting for Locale Announcement. Prompts played by ANN will use the User Locale of the calling party. |

| Note | To select MoH with no initial announcement, choose the Not Selected option. |
|---|---|

| Note | Played by MOH server only when the Audio Source Allow Multi-casting is not checked and the Initial Announcement for queuing-enabled hunt pilot calls field is set to Play announcement if call is queued . Played by ANN if Allow Multi-casting check box is checked or if Initial Announcement for queuing-enabled hunt pilot calls is set to Play announcement before routing to Hunt Member . |
|---|---|

| Note | To select MoH with no periodic announcement, choose the Not Selected option. |
|---|---|

| Note | The MOH server always plays the periodic announcement regardless of other settings. |
|---|---|

| Note | Prompts played by MOH will use the setting for Locale Announcement. Prompts played by ANN will use the User Locale of the calling party. |
|---|---|

| Field | Description |
|---|---|
| (list of MoH audio sources) | This list box shows the MOH audio source that you add. Select the audio stream number of an MOH audio source to configure
                                                that MoH audio source. Audio source ID is an ID that represents an audio source in the Music On Hold server. The audio source can include either
                                                a file on a disk or a fixed device from which a source stream Music On Hold server obtains the streaming data. An MOH server
                                                can support up to 51 audio source IDs. Each audio source, represented by an audio source ID, can stream as unicast and multicast
                                                mode, if needed. Note If you select <None> , the system default MoH audio source service parameter ( Default Network Hold MoH Audio Source ID ) is used for the MoH audio source. | Note | If you select <None> , the system default MoH audio source service parameter ( Default Network Hold MoH Audio Source ID ) is used for the MoH audio source. |
| Note | If you select <None> , the system default MoH audio source service parameter ( Default Network Hold MoH Audio Source ID ) is used for the MoH audio source. |
| Upload File | To upload an MOH audio source file that does not appear in the drop-down list, click Upload File . In the Upload File window, either enter the path of an audio source file or navigate to the file by clicking Browse . After you locate the audio source file, click the Upload File button to complete the upload. After the audio file gets uploaded, the Upload Result window displays the result of the upload.
                                                Click Close to close this window. Note When you upload a file, the file is uploaded to the Unified Communications Manager server and performs audio conversions to
                                                            create codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes
                                                            to complete. Note Uploading an audio source file to an MOH server uploads the file only to one MOH server. You must upload an audio source file
                                                            to each MOH server in a cluster by using Cisco Unified Communications Manager Administration on each server. MOH audio source files do not automatically propagate to other MOH servers in a cluster. | Note | When you upload a file, the file is uploaded to the Unified Communications Manager server and performs audio conversions to
                                                            create codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes
                                                            to complete. | Note | Uploading an audio source file to an MOH server uploads the file only to one MOH server. You must upload an audio source file
                                                            to each MOH server in a cluster by using Cisco Unified Communications Manager Administration on each server. MOH audio source files do not automatically propagate to other MOH servers in a cluster. |
| Note | When you upload a file, the file is uploaded to the Unified Communications Manager server and performs audio conversions to
                                                            create codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes
                                                            to complete. |
| Note | Uploading an audio source file to an MOH server uploads the file only to one MOH server. You must upload an audio source file
                                                            to each MOH server in a cluster by using Cisco Unified Communications Manager Administration on each server. MOH audio source files do not automatically propagate to other MOH servers in a cluster. |

| Note | If you select <None> , the system default MoH audio source service parameter ( Default Network Hold MoH Audio Source ID ) is used for the MoH audio source. |
|---|---|

| Note | When you upload a file, the file is uploaded to the Unified Communications Manager server and performs audio conversions to
                                                            create codec-specific audio files for MOH. Depending on the size of the original file, processing may take several minutes
                                                            to complete. |
|---|---|

| Note | Uploading an audio source file to an MOH server uploads the file only to one MOH server. You must upload an audio source file
                                                            to each MOH server in a cluster by using Cisco Unified Communications Manager Administration on each server. MOH audio source files do not automatically propagate to other MOH servers in a cluster. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select Call Routing > Route/Hunt > Hunt Pilot to configure hunt pilots. |
|---|---|
| Step 2 | Select the hunt pilot that you need to configure for Queuing. |
| Step 3 | Navigate to the Queuing section of the Hunt Pilot Configuration window. |
| Step 4 | Check the Queue Calls check box to enable queuing. |
| Step 5 | Choose a Music On Hold (MoH) source from the drop-down list box to be used to play announcements and provide queue hold treatments. The MoH source can be configured as unicast or multicast. The caller-side Media Resource Group List (MRGL) takes precedence
                                             for multicast or unicast. If you do not select a source, the default Network Hold MoH/MoH Source and Announcements is used. The MoH source announcement locale is used to determine the language used for the announcement. Only one type of language
                                             announcement can be played per hunt pilot. |
| Step 6 | In the Maximum Number of Callers Allowed in Queue field, enter an integer value for the number of callers allowed in the queue for this hunt pilot. The default value is 32. The field range is from 1 to 100. |
| Step 7 | Choose one of the following options when the maximum number of callers in the queue is reached: If you want subsequent calls to be disconnected, select Disconnect the call . If you want subsequent calls to be routed to a secondary destination, select Route the call to this destination . Provide a specific device DN, shared line DN, or another hunt pilot DN. (Optional) You may also select Full Queue Calling Search Space from the drop-down list. Used to determine which partition to search when attempting to complete a call. |
| Step 8 | In the Maximum Wait Time in Queue field, enter an integer value to set the maximum wait time, in seconds, in a queue. The default value is 900 seconds. The field range is from 10 to 3600 seconds. |
| Step 9 | Choose one of the following options when the maximum wait time is reached: If you want that call to be disconnected, select Disconnect the call . If you want that call to be routed to a secondary destination, select Route the call to this destination . Provide a specific device DN, shared line DN, or another hunt pilot DN. (Optional) You may also select Maximum Wait Time Calling Search Space from the drop-down list. Used to determine which partition to search when attempting to complete a call. |
| Step 10 | When no line members are logged in or registered at the time of an incoming call, choose one of the following options: If you need that call to be disconnected, select Disconnect the call . If you need that call to be routed to a secondary destination, select Route the call to this destination . Provide a specific device DN, shared line DN, or another hunt pilot DN. (Optional) You may also select No hunt members logged in or registered Calling Search Space from the drop-down list. Used to determine which partition to search when attempting to complete a call. |
| Step 11 | Click Save . |

| Step 1 | In Cisco Unified Communications Manager Administration, choose Call Routing > Route/Hunt > Line Group to configure line groups. |
|---|---|
| Step 2 | Choose the line group that you need to configure from the Find and List Line Groups window. |
| Step 3 | Navigate to the Hunt Options section of the Line Group Configuration window. |
| Step 4 | Ensure that the Automatically Logout Hunt Member on No Answer check box is checked. |
| Step 5 | Click Save . |

| Feature | Interaction |
|---|---|
| SIP Rel1XX Options | If a call is routed to a queuing-enabled hunt pilot through SIP ICT, the SIP ICT uses the SIP profile that has SIP Rel1XX
                                          Options set to Send PRACK if 1XX contains SDP . As a result, the initial announcement is played to every call before the call is extended to the line member. The above existing interaction for SIP ICT does not apply if Connect Inbound Call before Playing Queuing Announcement checkbox is checked under Device Device Settings SIP Profile > Trunk Specific Configuration in Cisco Unified CM Administration. If Connect Inbound Call before Playing Queuing Announcement checkbox is not checked the interaction for SIP ICT remains the same. However, it does not guarantee the initial announcement
                                          can always be heard by a caller from the PSTN side. The initial announcement will not be heard by a caller from the PSTN side
                                          if the PSTN provider doesn't open the voice path until a Connect message is received on the call. |
| Hunt Pilots and Hunt Groups | The logoff notification functionality for hunt groups changes when Call Queuing is enabled for a hunt pilot. If Call Queuing
                                                is enabled for a hunt pilot, the Hunt Group Logoff Notification does not play when users log out of a hunt group or are logged
                                                off because they missed their turn in the queue. If the hunt list has multiple line groups, these line groups must have the same setting for Automatically Logout Hunt Member on No Answer . Hunt Pilot still queues calls, even when all hunt members are logged out.The line group members should not be added in more
                                                than one line group and even if they are added in second line groups, those second line groups should not be in the same Hunt
                                                list. All hunt options must be set to Try Next Member, then Try Next Group in the hunt list. |

| Note | When using the broadcast algorithm for call coverage, the number of
                                                hunt list devices is limited
                                                by the number of busy hour call attempts (BHCA). Note that a BHCA
                                                of 10 on a hunt pilot
                                                pointing to a hunt list or hunt group containing 10 phones and
                                                using the broadcast algorithm is
                                                equivalent to 10 phones with a BHCA of 10. |
|---|---|