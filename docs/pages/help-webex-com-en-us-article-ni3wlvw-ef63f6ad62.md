---
doc_id: help-webex-com-en-us-article-ni3wlvw-ef63f6ad62
source_url: https://help.webex.com/en-us/article/ni3wlvw
retrieved_at: 2026-11-02T13:02:19.844663+00:00
---

If you're a full customer administrator, read-only customer administrator, or customer support administrator, you can use the Troubleshooting information in Control Hub to help you determine the root cause of calls on the Call on Webex (non-PSTN) service, Webex Calling calls, or meeting-related issues your users experienced.

Diagnostics are also available. You can further investigate specific meetings or calls that are in progress or that have occurred within the past 21 days. Search for meetings by meeting number, the email address of the host or participants, conference ID, or the name of cloud-registered devices. Search for calls with the caller or callee's email address, MAC address, and phone number. You can then drill down into participant details, hop details, video quality, audio quality, and more.

For more information on media quality artifacts, troubleshooting methodology, and best
        practices, see Troubleshooting Webex Meetings and Calls .

Meetings in progress appear at the top of list with an In Progess status. Calls only appear after they've ended.

These are the minimum versions required for Webex services that you need in order to see rich troubleshooting data for Webex Meetings and calls using Call on Webex. If your devices don't meet these requirements, only packet loss and latency data are available.

Rich troubleshooting data for Webex Events is available for participants who join through the desktop app. Oherwise, only packet loss and latency data are available.

Only packet loss and latency data are available for Webex Training sessions.

## View troubleshooting data

Sign in to Control
            Hub .

Go to Troubleshooting .

Use the Search bar to search for:

- Meetings —by host email, participant email, meeting number,
            or conference ID.

- Webcasts —by host email, participant email, meeting number,
            or conference ID.

- Calls that used Call on Webex —by caller or callee's email
            address.

- Calls that used Webex Calling —by caller or callee's email
            address that's registered with Webex Calling, phone number, MAC address, or call
            ID.

By default, you can see meetings and calls from the last 7 days, but you can click the
            calendar icon  to specify a specific date. You
            can search for meetings and calls that happened up to 21 days ago.

The time zone is set according to your profile at the top right corner, but you can
            change the time zone anytime from the drop-down menu. For example, if a meeting host
            comes to you with an issue from a meeting that took place in a different time zone, you
            can switch to that time zone so that you don’t have to do the time conversion.

In the search results, select the meeting or call that you want more information about.

If someone reports an issue with:

- Meetings or calls using Call on Webex—You can search for the email of the host or participants, the 9-digit meeting number (also known as meeting access code), the conference ID, or the caller or callee's email address.

- Calls using Webex Calling—You can search for the caller or callee's email address that's registered with Webex Calling, MAC address of the phone, phone number, or call ID.

You have access to information such as what people were up to during the meeting or call (like hosting or sharing), how long it took them to join, and how long the meeting or call lasted.

By default, the table is sorted by the latest start date of meetings and calls, but you can sort the table to see either meetings or calls first by clicking on the Service column.

If you click on a meeting or call and then use the back button to go back into the search view, the last viewed meeting or call is highlighted in yellow.

The time zone is set according to your profile setting, but you can change it next to the date selector.

## Search by email address

Enter someone’s email address, including the
        domain, to find out more about meetings and calls that they attended, along with a
        high-level overview of their media quality metrics in those meetings and calls.

Calls using Call on Webex or Webex Calling only show up after the call has ended.

KPIs

The following KPIs help you see how often the user had poor quality meetings or
        calls:

- Poor Meeting Minutes —Number of Webex Meetings minutes where the user experienced
          poor media quality.

- Total Meeting Minutes —Total number of minutes that the user was in meetings using
          Webex Meetings.

- Poor Minutes of Call on Webex —Number of minutes using Call on Webex where the
          user experienced poor media quality.

- Total Minutes of Call on Webex —Total number of minutes that the user was in calls
          using Call on Webex.

- Poor Webex Calling Minutes —Number of Webex Calling minutes where the user
          experienced poor media quality.

- Total Webex Calling Minutes —Total number of minutes that the user was in calls
          using Webex Calling.

Meetings and calls list

This list organizes meetings and calls starting from the most recent. The information
        available in this list are:

- Overall —Overall media quality of the meeting or call across all
          participants.

- Personal —The user's personal media quality in the meeting or call.

- Service —The service used for the meeting or call.

- Start Time —The time that the meeting or call started. The timezone is based on
          what you selected.

- Meeting / Caller number —The 9-digit meeting access code used to join the meeting
          or the number that the user called.

- Name —Name of the meeting or call.

- Host / Caller —The user who hosted the meeting or the user who initiated the
          call.

- Participants —Number of participants in the meeting or call.

- Duration —The total duration of the meeting or call.

- Site / Location —The Webex Meetings site if it was a meeting or location assigned
          to the user if it was a call.

- Conference / Call ID —Unique identifier of the meeting or call.

Visualization view

The visualization view shows you a timeline view of the meetings and calls that the
        user attended. Each dot represents a meeting or call. Hover over a dot to see a short
        description of the meeting or call. You can click on the name of the meeting or call to open
        up a new tab that redirects you to its details page. Different devices are split into
        multiple rows so you can quickly glance and see if a user's poor quality is coming from a
        specific operating system or device.

## Search by user name

Enter someone’s user name to find out more about meetings and calls that they attended,
        along with a high-level overview of their media quality metrics in those meetings and
        calls.

You can also apply the following filters when searching for a user:

Device type

Location

Personal quality

Service type

## Search by meeting number

Meeting numbers are also known as the 9-digit access code. This number may not be
                unique across meetings. For example, a person's Cisco Webex Personal Room access
                code doesn't change from meeting to meeting.

Enter the 9-digit number without spaces or dashes. A list of meetings that match your
                search criteria display.

## Search by name of cloud-registered device

Enter a device name to find out more about meetings and calls that they were used in, along
        with a high-level overview of the media quality metrics of the device in those meetings and
        calls. If you search for a partial device name, a drop-down list shows you the closest match
        that you can select from.

Device summary and details

Once you select a device, the following summary information is available for you to
          see:

- Device name —Display name of the device. You can click on the name to go to the Devices section of Control Hub.

- Status —Current status of the device.

- Owner —If usageMode is set to personal, shows the name of the
            user that the device is assigned to.

- Workspace —If usageMode isn't set to personal, shows what
            platform the device is on, such as Microsoft Teams, Google Meet,etc.

- Product Name —Product name of the device.

- Device Platform —Platform that the device uses, such as Google Meet or Microsoft
            Teams.

In addition, the following details of the device are available at a glance:

- Network Connectivity —Network connectivity of the device, such as wired or
            wireless.

- MAC Address —MAC address of the device.

- Serial Number —Serial number of the device.

- Type —Type of the device, such as Room or Desk series.

- IP Address —IP address of the device.

- SIP Address —SIP address of the device.

- RoomOS Release —Release number of RoomOS that the device is on.

- Software version —Software version of RoomOS that the device is on.

- Software channel —Shows if the device is on stable or beta channel.

Device KPIs

The following KPIs help you see how often the device had poor quality meetings or
          calls:

- Meetings with poor quality —Number of meetings where the device experienced poor
            media quality out of the total number of meetings joined.

- Calls on Webex with poor quality —Number of calls using Call on Webex where the
            device experienced poor media quality out of the total number of Call on Webex
            calls.

- Webex callings with poor quality —Number of calls using Webex Calling where the
            device experienced poor media quality out of the total number of Webex Calling
            calls.

- WebRTC with poor quality —Number of calls using WebRTC where the device
            experienced poor quality out of the total number of WebRTC calls.

- Poor Meeting Minutes —Number of Webex Meetings minutes where the device
            experienced poor media quality.

- Poor Webex calling Minutes —Number of Webex Calling minutes where the device
            experienced poor media quality.

- Poor Minutes of Call on Webex —Number of Call on Webex minutes where the device
            experienced poor media quality.

- Poor WebRTC Minutes —Number of WebRTC minutes where the device experienced poor
            media quality.

Device meetings and calls list

This list organizes meetings and calls starting from the most recent. The information
          available in this list are:

- Overall —Overall media quality of the meeting or call across all
            participants.

- Quality —The device's personal quality during the meeting or call.

- Service —The service and platform of the device used for the meeting or
            call.

- Start Time —The time that the meeting or call started. The timezone is based on
            what you selected.

- Meeting / Caller number —The 9-digit meeting access code used to join the
            meeting or the number that the user called.

- Name —Name of the meeting or call.

- Host / Caller —The user who hosted the meeting or the user who initiated the
            call.

- Participants —Number of participants in the meeting or call.

- Duration —The total duration of the meeting or call.

- Site / Location —The Webex Meetings site if it was a meeting or location
            assigned to the user if it was a call.

- Conference / Call ID —Unique identifier of the meeting or call.

## Search by conference ID

Every meeting or call has a unique conference ID. The conference is an internal ID that isn't commonly available to users. You can locate this ID through Analytics .

Enter the conference ID in the search field. Conference IDs are 9 to 18 characters in length and can be alphanumeric. Once you enter an ID, you're taken straight to the details page for that meeting or call.

## Search by phone number

Calls made using Webex Calling usually have a caller and callee phone number. Enter the phone number in the search field for an exact string match. The listing view will show all calls that were either made to or received from that phone number.

## Search by call ID

Every call leg (or hop) has a call ID. The call ID is an internal ID that isn't commonly available to users. It's primarily used by the support team.

Enter the call ID in the search field, which is an alphanumeric string. Once you enter the call ID, the listing view shows the call in which the call ID occurred.

## Search for users or devices that joined external meetings

Enter a user's email address or device name to view their media quality metrics when they
        join a meeting outside of your organization. External meetings show up as calls with the
        following naming convention:

- User's email address— user name → Webex Meeting.

- Device— device name → Webex Meeting.

The user or device will also be the only participant shown when you drill down to see the
        meeting details.

## Limitations

- Wildcard searches, like searches that use special characters, are not supported.

- Data isn't available for audio-only meetings, where every participant in the meeting (including the host) dialed into the meeting and no one joined through a client or device.

- If the meeting was scheduled in a space, then use the meeting number to find the meeting if you can't find the meeting using the host's email address. You can find the meeting number by going to the space, selecting the activity menu and choosing Meetings , then Space meeting information .

Once you select a meeting from the search view, you see the details for that meeting. This view lists all the participants on the left side, participant usage and quality information in the middle, and a sliding right panel with specific meeting or call details.

## Key performance indicators (KPIs)

KPIs are available at the top to give you a quick view of the media quality experienced during the meeting. The KPIs available are:

Total participants —The number of participants who joined the meeting. When it's a meeting, the number of guests are shown at the bottom of this KPI. When it's an event, panelists are shown at the bottom. Click on the filter icon to only show guests or panelists.

Poor audio minutes —The percentage of audio minutes at or above the poor media quality threshold out of the total minutes in the meeting. Click on the filter icon to sort participants who had the most poor audio minutes at the top.

Poor video minutes —The percentage of video minutes at or above the poor media quality threshold out of the total minutes in the meeting. Click on the filter icon to sort participants who had the most poor video minutes at the top.

Poor sharing minutes —The percentage of sharing minutes at or above the poor media quality threshold out of the total minutes in the meeting. Click on the filter icon to sort participants who had the most poor sharing minutes at the top.

Unexpected drops —The percentage of participants who left the meeting early due to a connection, software, or hardware issue. Click on the filter icon to sort participants who had the most unexpected drops at the top.

## Join in-progress meetings

If you’re a full administrator with the Advanced Troubleshooting Access role, then you can join a meeting that’s in progress to help make sure the meeting runs smoothly. Click Join in the meeting view, and you’ll join the meeting as a guest.

In-progress meetings are shown with an icon. In-progress meetings don’t refresh automatically by default unless you enable it. Click the refresh button to update the meeting information that’s shown on the page.

Enable auto refresh for in-progress meetings

To enable auto refresh, click the Actions button when viewing an in-progress meeting and then select Enable auto refresh . The in-progress meeting information automatically updates every two minutes, or you can manually refresh the meeting information again.

## Participants list

The name of the participant or device, and the icon of the device used to join the meeting,
        shows up on the left. If someone joins a meeting using their Webex client and they connect
        audio with call back over PSTN, then two entries are shown. For example, when you call into
        a meeting and your Webex App is paired with a Cisco Room Device, there are two entries: Webex App and Room Device.

To speed up loading time, the default number of participants shown at one time is 25, and participants are divided into pages. You can increase the number of participants shown per page with the drop-down menu at the bottom of the list.

Search for specific participants

Enter the name of a participant that you want to look at the metrics for. You can add to the list by searching for another participant.

Filter participants list

Click on the search bar to bring up a list of filters that you can filter participants by. The available filters are:

Platform —Filters participants by the operating system of the device used to join the meeting.

Client —Filters participants by the type of application used to join the meeting.

Participant —Filters participants by an assigned role, such as as guest or host.

Quality —Filters participants by who experienced poor or fair quality thresholds.

Location —Filters participants by a certain location.

Media region —Filters participants by the data center or on-premises cluster that they connected to.

Reorganize participants list

Use the drop-drop menu to sort participants by alphabetical order, by poorest audio, video, or share quality first, or by locations.

View which participant paired with a device

When a participant uses a device or connects through PSTN to join a meeting, the name of the participant shows up under the device. This helps you see which participants paired with which device, making it easier for you to reach out to the correct participant to assist them.

Hover over a participant to see a short summary about the participant, such as the client type used to join the meeting. When someone calls into a meeting, you can see what time they joined the meeting and the amount of time that they were in the meeting.

## Submit feedback

Click on the announcement button next to the information available to let us hear your thoughts. If you think the information's helpful, you can give it a thumbs up. If you don't think an information's helpful, click on the edit button to write down your comments on how we can improve the information for you.

## Join meeting time (JMT)

The JMT for each client is captured with the exception of calls using PSTN. JMT is calculated in seconds as (the time from clicking the meeting link to loading the preview window) + (the time from clicking the Join Now button in the preview window to connecting into the meeting).

JMT doesn’t count the time the user spends browsing menus, making selections in the preview window, or waiting in the lobby.

A JMT of less than 10 seconds is shown in green, between 10 and 20 seconds is shown in yellow, and over 20 seconds is shown in red. Hover over the colored dot to see the JMT of a participant.

A participant’s join meeting time will always show the first time that the participant joined the meeting, even if the participant leaves and re-joins the meeting multiple times.

## Meeting Details

Meeting details are shown on the right-side sliding panel, and can be collapsed with the button.

Title

Description

Meeting No

The 9-digit meeting access code used to join the meeting.

Conference ID

The unique ID of the meeting.

Site Name

The Webex site used to host the meeting.

Meeting Date

Meeting Time

The time of when the meeting started and ended, shown in the time zone that you selected in the search view.

Schedule Timezone

The time zone that the meeting was scheduled in.

Meeting Type

The type of meeting that was scheduled. The meeting types available are:

Webex Meetings

Webex Events Webinar

Webex Events Webcast

Webex Events Classic

Webex Support

Webex Training

Participants

The number of participants who joined.

Host Name

The name of the host.

Host Email

The email address of the host.

Audio

The type of audio used.

Video

If video was enabled by a participant, it shows as yes. If video wasn't enabled at all, it shows as no.

Recording

The total duration of how long the meeting was recorded for.

Screen Share

The total duration of how long participants shared their screens for.

Apps

This field shows if an integrated app, like Slido , was used during the meeting.

AI Assistant

This field shows if the Cisco AI Assistant was used during the meeting.

End reason

This field shows how the meeting was ended. Possible values are:

- Ended by host—Name of the host who ended the meeting.

- No Participant—Meeting is ended by Webex because there are no participants
                    left.

- Max Duration—Meeting is ended by Webex due to meeting duration limit.

A legend is provided under the Meeting Details panel. Hover over the information icon to see how the thresholds are defined.

## Audio, video, and sharing tab

You can switch
        between the audio, video, and sharing tabs to see the detailed views of a meeting or call,
        which includes JMT, usage, and quality metric.

How media quality data is captured

Media quality data is captured every minute and visualized using green (good), yellow
        (fair), or red (poor). These colors are based on the end-to-end packet loss and average
        latency only. The types of packet loss captured are:

End to End —The speaker's sending packet loss from their Webex
            client to the participant's Webex client, captured after packet recovery.

Sending —Participant's Webex client to the Webex cloud.

Receiving —Webex cloud to the participant's Webex client.

If you see a dotted gray line, it means the audio, video, or sharing of the device is
        turned off. If you see a solid gray line, that indicates only minimal data is available,
        like usage and JMT. Solid gray lines mean the user joined the meeting with an application or
        device that is older than the minimum supported version or a Cisco on-premises
        device.

You can hover over a line to see a summary of the quality metric as a
        pop-up.

Host and panelist indicator

An H  icon indicates when a participant
        becomes the host of the meeting.

A P icon indicates who were the panelists during a
        Webex Events session.

Share indicator

A blue line shows who's sharing their screen and how long they shared their screen
        for.

Hardware and network change indicator

A purple diamond icon indicates when a participant changes their network
        connection, headset, microphone, or camera during a meeting. Hover over the icon to see the
        change details.

Mute indicator

The dotted line shows you how long a participant was muted for, and you can hover over
        the icon to see if the participant muted and unmuted multiple times within that
        duration.

End meeting indicator

If a participant joined a meeting using VoIP with the Webex Meetings app, Webex App app, or a device, then you can see how a meeting ended for that participant. A green line icon indicates when a participant left a meeting normally, while
        a red line icon indicates when a participant left a meeting unexpectedly,
        such as getting dropped from a meeting due to a system or network issue.

Host end
          meeting indicator

The X icon inside a circle shows how the host ended the
        meeting.

Initial mute and unmute
        indicator

You can hover over the join meeting indicator to see whether a
        participant initially joined the meeting with their audio muted or unmuted. This information
        helps you quickly determine whether audio issues may have started when the participant first
        joined.

Volume level indicator

Hover over a participant’s
        media quality line to see what their volume level was during the meeting. If they were
        experiencing audio issues, this can help you understand whether their device volume was set
        appropriately or if the issue may have been caused by something else.

Volume level is
        calculated based on the participant's device audio signal level and volume
          settings.

Simultaneous interpreter and language
        indicator

An I icon next to a participant's name indicates that the
        participant was assigned as an interpreter. You can hover over the icon to see the source
        language and the target language.

View individual breakout sessions

A blue line represents if a breakout session was started within a meeting. You can
        click on the blue line to see which participants joined the breakout session, and how long
        they were in there for. Use this information to help you isolate issues within a specific
        breakout session.

## Details tab

The details tab provides a table view of participants. You can see how long they were in the meeting or call for, the client and platform they used to join a meeting, their IP addresses, their hardware information, how they ended a meeting, the location they joined from, and if they were the host. You can use the scroll bar to see additional information, such as the participant's dialed #, audio, video and share transport and codec, microphone, speaker, and camera. This table can be exported to a CSV file using the Export Record button at the top right.

The meeting details shows values that are relevant to the meeting or call. If a feature or function wasn't used, like if no one shared their screen during the meeting, then the value is left blank.

The following table shows what details data is available.

Title

Description

Join Time

When the participant joined the meeting shown in the time zone you select.

Duration

Duration of the meeting.

Activity

If the participant was the host, was transferred the host role, or shared content during the meeting.

Client

The type and version of the application used to join the meeting.

Platform

The operating system and version of the device used to join the meeting. Possible values could be "windows", "mac", "android", "ios", and "linux”

Join From

If the participant joined the meeting by browser, this shows the browser type and version used to join the meeting.

Hardware

This hardware make and model of the device used to join a meeting. For computers, this might be "Lenovo Thinkpad p60". For phones, this might be "Samsung Galaxy S7". For room devices, this might be "Cisco Webex Room Kit".

Connection

The type of network connection that the client used to exchange media. Possible values could be "wifi", "ethernet", "cellular", or "unknown".

This is not tracked per media type. It it is possible (and relatively common) that this changes over the course of a meeting.

Local IP

The local IP address of the client for the network interface that it is using to transmit media. IP addresses are partially masked to preserve the personal identity of users.

Public IP

This is the public IP address of the client as seen by the media servers. IP addresses are partially masked to preserve the personal identity of users.

Media Server IP

The IP address of the media service that the client is exchanging media with. The
                  Media Server IP is the network address of the server responsible for storing and
                  delivering media files (such as audio prompts) to clients or applications during
                  media sessions.

Location

Geo lookup of Public IP address.

Media Node

The datacenter or region of the media node that the client is connected to. For cloud based media nodes this will be a general region name such as "San Jose, USA".

For video mesh based media nodes, this will have a more specific name that matches the video mesh cluster name that was provisioned by the customer.

System Code

What happened to the participant during a meeting. The system codes available are:

Host Hung Up —The host ended the meeting for everyone.

User Hung Up —The participant left the meeting early.

Time Out —The participant disconnected from the meeting due to a network connection error.

Leave Waiting Room —The participant was waiting in the lobby before the host started the meeting.

Fallback to PSTN —Callback with Edge Audio failed, so the callback goes through a PSTN connection.

Phone

The phone number of the participant.

Dialed #

The conference bridge PSTN number.

Audio Transport

The network type used to transport audio. Valid values could be "UDP", "TCP", "xTLS".

This can change over the course of a meeting, however, only the initial transport used is reported.

Video Transport

The network type used to transport video. Valid values could be "UDP", "TCP", "xTLS".

This can change over the course of a meeting, however, only the initial transport used is reported.

Share Transport

The network type used to transport a screen or application share. Valid values could be "UDP", "TCP", "xTLS".

This can change over the course of a meeting, however, only the initial transport used is reported.

Audio Codec

(Send) The media encoding and decoding format in use for the media transmitted by a client. Note that this can change over time during a call.

(Receive) The media encoding and decoding format in use for the media received by a client.

This can change over the course of a meeting, however, only the initial codec used is reported.

Video Codec

(Send) The media encoding and decoding format in use for the media transmitted by a client. Note that this can change over time during a call.

(Receive) The media encoding and decoding format in use for the media received by a client.

This can change over the course of a meeting, however, only the initial codec used is reported.

Share Codec

(Receive) The media encoding and decoding format in use for the media received by a client.

This can change over the course of a meeting, however, only the initial codec used is reported.

Microphone

The brand name and model information for the the microphone that was used during the meeting.

This can change over the course of a meeting, however, only the initial microphone used is reported.

Speaker

The brand name and model information for the the speaker that was used during the meeting.

This can change over the course of a meeting, however, only the initial speaker used is reported.

Camera

The brand name and model information for the the camera that was used during the meeting.

This can change over the course of a meeting, however, only the initial camera used is reported.

## Export

From the meeting or participant view, you can export meeting information in a JSON file. You can also export the participant list and details to a CSV file.

Presenter and host information in the data tab isn't included in the JSON file.

## Map tab

The map view gives you a visualization of the locations that participants joined the meeting from and the data centers that they connected to. With this information, you can determine if there's a pattern for participants who are experiencing media quality issues. Did certain areas have participants with poor media quality, or was it a specific data center? Are participants connecting to the most optimal data center closest to their area? Did a participant have poor media quality because they connected to a data center that's farther away from them? This map view can help you find possible answers to those questions so you can narrow down issues and proactively figure out if there's a problem before more users are affected.

The map view supports up to 500 participants and only shows participants that are on the current page. To see the other participants, you can click through the pages.

If the meeting has more than 500 participants, the map view won't be available.

The number in the circle shows how many participants joined from that area. Hover over a location to see the names of the participants in that area, what their media quality was like, and the data center that they connected to.

Participants with poor media quality

If a participant reaches the poor media quality threshold for three minutes continuously or for a total of five minutes, the circle becomes red. Media quality thresholds for this map are calculated as:

Poor —End-to-end receiving packet loss > 5% or latency > 400ms.

Good —Everything else.

You can click on a participant's name to see their media quality details during the meeting.

Participants with an unknown location

Participants whose locations are unknown are placed in a square at the bottom-left side of the map.

Currently, participants who join a meeting from video mesh clusters show as unknown.

For information on how to troubleshoot calls that use Webex Calling, see Troubleshoot Webex Calling Media Quality in Control Hub .

When you select a call from the list, you get information that's similar to the meeting view, such as media quality data for the participants and the audio, video, sharing, and details tab. The difference is that calls don't have the KPIs at the top and the Map tab. You can also find out the details about the call on the right-hand panel, like the calling session ID, the date and time of the call, and who initiated the call.

If you add another user to the Call on Webex session, the call changes to a meeting from a space. Troubleshooting data for meetings from a space are the same as calls using Call on Webex.

## Call Details

Title

Description

Calling Session ID

Unique ID of the call.

Calling Date

The date of when the call was started.

Calling Time

The time of when the call started and ended, shown in the time zone that you selected in the search view.

Session Type

The type of call that was made. The session types available are:

Call on Webex—When a caller calls someone using Call on Webex (non-PSTN).

Conference call—When a caller adds more people to a Call on Webex call, it becomes a conference call .

Participants

Number of participants in the call or meetings started from a space.

Caller Name

The name of the user who started the call.

Caller Email

The email of the user who started the call.

Audio

The type of audio used.

Video

If video was enabled by a participant, it shows as Yes. If video wasn't enabled at all, it shows as No.

Click a participant name to see the detailed metrics of their client and device. All information is updated every minute. Additional information about a participant's equipment and network can be found on the right side.

## Participant details

Click the down arrow on any of the charts to collapse them.

Filter between showing All, Sending, Receiving, or End to End details with the drop-down menu in the right corner.

Filter out the average or maximum latency of each chart by clicking the icons for them.

Audio Quality, Video Quality, Share Quality, CPU Usage, and Memory Usage data is updated every minute for meetings that are in progress.

Click the red or yellow line segments to highlight the selection with a vertical bar,  then hover over each of the line to show the pop-up with the actual value and timestamp of each chart.

Audio Quality —The network quality of the audio channel for that participant throughout the meeting.

Video Quality —The network quality of the video channel for that participant throughout the meeting.

Share Quality —The quality of any content shared during the meeting. The share quality includes information on how content was sent and received.

CPU Usage —The percentage of the CPU that was used by the machine that the participant joined the meeting with.

Memory Usage —The percentage of memory that was used by the machine of the participant during the meeting.

Mute indicator

A mute icon indicates when a participant was muted during a
                meeting. The mute indicator shows for participants who clicked the mute button on
                the Webex Meetings desktop and mobile app, the Webex App desktop and mobile app, and cloud-registered room devices. If a participant was
                muted through an external hardware, like a microphone, then the mute indicator
                doesn't show.

Mute on entry only shows for participants who join from the Webex App desktop and mobile app.

The following quality metrics are available.

Title

Description

Latency(ms)

Latency is a delay in the delivery of audio or video during a
                                    meeting.

Packet Loss (%)

Packet loss occurs when there's a problem transmitting data packets, and some packets are dropped before they're received by the participant. The types of packet loss captured are:

End to End —The speaker's sending packet loss from their Webex client to the participant's Webex client, captured after packet recovery.

Sending —Participant's Webex client to the Webex cloud.

Receiving —Webex cloud to the participant's Webex client.

Jitter(ms)

A variation in the delay of packets that are received.

Media Bitrate(kbps)

The number of bits processed per second.

Frame Rate(fps)

The number of frames that are shown every second of a meeting.

Resolution(p)

The number of pixels shown on user’s screen during a given amount of time.

System CPU(%)

The total percentage of CPU that is used by all applications. On
                                    a multi-core system, CPU usage is measured across all cores.

Webex App CPU(%)

The percentage of CPU that is taken by Webex Meetings or Webex App app during the meeting. On a multi-core system, CPU usage is measured across all cores.

System Memory(%)

The total percentage of memory that is used by all
                                    applications.

Webex App Memory(%)

The total percentage of memory that is taken by Webex Meetings or Webex App app during the meeting.

## Equipment and Networks details

The Equipment and Networks panel shows you information about a participant's
                configuration. You can collapse the panel with the button.

Similar information is available for the Webex Meetings Desktop application, Webex App Desktop application, Webex App for Android, Webex App for iPhone and iPad, and cloud-enabled devices. Webex Meetings for mobile, on-premises devices, and third-party SIP devices will be supported in the future.

Platform, microphone, speaker, and camera details aren't available for cloud-enabled devices.

Only phone number and conference bridge information is available for call in and
                    callback users.

For PSTN: Call In and Call Back, only phone numbers or conference bridge information
                is available.

The following table shows available equipment and network data.

Title

Description

Client

The type and version of the application used to join the meeting.

Location

Geo lookup of Public IP address.

Platform

The operating system and version of the device used to join the meeting. Possible
                  values could be "windows", "mac", "android", "ios", and "linux”.

Join From

If the user joined the meeting by browser, this shows the browser type and
                  version used to join the meeting.

Connection

The type of network connection that the client used to exchange media. Possible
                  values could be "wifi", "ethernet", "cellular", or "unknown".

This is not tracked per media type. It it is possible (and relatively common)
                    that this changes over the course of a meeting.

Media Node

The datacenter or region of the media node that the client is connected to. For
                  cloud based media nodes this will be a general region name such as "San Jose,
                  USA".

For video mesh based media nodes, this will have a more specific name that
                  matches the video mesh cluster name that was provisioned by the customer.

Local IP

The local IP address of the client for the network interface that it is using to
                  transmit media. IP addresses are partially masked to preserve the personal
                  identity of users.

Public IP

This is the public IP address of the client as seen by the media servers. IP
                  addresses are partially masked to preserve the personal identity of users.

Media Server IP

The IP address of the media service that the client is exchanging media with. The
                  Media Server IP is the network address of the server responsible for storing and
                  delivering media files (such as audio prompts) to clients or applications during
                  media sessions.

Audio Transport

The network type used to transport audio. Valid values could be "UDP", "TCP",
                  "xTLS".

This can change over the course of a meeting, however, only the initial
                    transport used is reported.

Video Transport

The network type used to transport video. Valid values could be "UDP", "TCP",
                  "xTLS".

This can change over the course of a meeting, however, only the initial
                    transport used is reported.

Share Transport

The network type used to transport a screen or application share. Valid values
                  could be "UDP", "TCP", "xTLS".

This can change over the course of a meeting, however, only the initial
                    transport used is reported.

Audio Codec

(Sending) The media encoding and decoding format in use for the media transmitted
                  by a client. Note that this can change over time during a call.

(Receiving) The media encoding and decoding format in use for the media received
                  by a client.

This can change over the course of a meeting, however, only the initial codec
                    used is reported.

Video Codec

(Sending) The media encoding and decoding format in use for the media transmitted
                  by a client. Note that this can change over time during a call.

(Receiving) The media encoding and decoding format in use for the media received
                  by a client.

This can change over the course of a meeting. Only the initial codec used is
                    reported.

Share Codec

(Receiving) The media encoding and decoding format in use for the media received
                  by a client.

This can change over the course of a meeting. Only the initial codec used is
                    reported.

Microphone

The brand name and model information for the the microphone that was used during
                  the meeting.

This can change over the course of a meeting. Only the initial codec used is
                    reported.

Speaker

The brand name and model information for the the speaker that was used during the
                  meeting.

This can change over the course of a meeting. Only the initial speaker used is
                    reported.

Camera

The brand name and model information for the the camera that was used during the
                  meeting.

This can change over the course of a meeting. Only the initial camera used is
                    reported.

Noise Removal

This field shows if the participant used the noise
                    removal feature. If noise removal was used, then you can see how long it
                  was enabled.

Virtual Background

This field shows if the participant used a virtual
                    background .

## Network infrastructure details

If the Allow Cisco to collect network details setting is enabled for
        the organization, the Equipment and Networks panel can show network
        infrastructure details that are reported by the participant's endpoint. Use these details
        with participant media-quality metrics to look for repeated issues tied to the same Wi-Fi
        access point, Ethernet switch or port, or cellular network.

To collect these details, turn on Allow Cisco to collect network
          details in Organization Settings > Collect client metrics . This setting is off by default.

The following network infrastructure details can appear when they're available for the
        selected interval.

Connection type

Title

Description

Wi-Fi

BSSID

The basic service set identifier of the Wi-Fi access point that the endpoint used
                  for the connection.

Wi-Fi

SSID

The service set identifier, or Wi-Fi network name, that the endpoint used for the
                  connection.

Ethernet

Switch Chassis

The identifier for the Ethernet switch chassis that the endpoint reported.

Ethernet

Switch Port

The identifier for the Ethernet switch port that the endpoint reported.

Cellular

PLMN

The public land mobile network identifier that the endpoint reported for the
                  cellular connection.

Cellular

Provider Name

The name of the cellular network provider, when available.

Cellular

Network Type

The cellular network type, such as 4G or 5G, when available.

When you troubleshoot a participant, compare these details across the affected intervals
        and other participants. Recurring values can help identify a network path, access point,
        switch port, or cellular provider for additional investigation.

Network infrastructure details only appear when the endpoint reports them for the
          selected interval. Availability varies by endpoint, operating system, app version, active
          network, and device permissions.

A missing value doesn't confirm a network fault. On macOS, iOS, and Android, location
          permissions can affect whether Wi-Fi or cellular details are available.

The Live Meetings tab shows all the meetings that are currently in progress in your
        organization. You can use the information here to proactively catch network issues before
        they become widespread, or to help diagnose the cause for any network issues. Data
        automatically updates every 10 minutes. You can see when the last time the data was updated
        next to the Export as JSON button.

By default, the page shows you the live meetings for all the sites in your Control Hub organization. If you have multiple sites, you can use the drop-down menu to select a
        specific site.

## Key performance indicators (KPIs)

KPIs are available at the top of the page to show you the number of live meetings and how many meetings and participants are experiencing good network. You can use these KPIs as measurable data to see if any network issues have been happening recently. The KPIs available are:

Total Live Meetings —The number of meetings that are in progress.

Total Live Participants —The number of participants that are currently in meetings.

Meetings with Good Network —The number of meetings that are at or above the good network quality threshold. Quality is counted as good if packet loss was less than or equal to 5% and latency was less than or equal to 400ms. Meetings are counted as poor quality if at least one participant had poor audio or video quality in the last 15 minutes.

Participants with Good Network —The number of participants that are at or above the good network quality threshold. Quality is counted as good if packet loss was less than or equal to 5% and latency was less than or equal to 400ms. Participants are counted as poor quality if they had three consecutive minutes or five accumulated minutes of poor audio or video quality during a meeting.

## Live meetings map

This map shows the overall geographic distribution of live meetings. You can hover over each circle to see more data about a location, such as the number of participants, meetings, and poor quality meetings. You can also select the data centers to which the participants in a location are connected. The names for the data centers are abbreviated. The size of the circle is based on how many participants there are, and the color is based on how many poor-quality meetings a location is experiencing.

If you have the Advanced Troubleshooting role, you can click on the number next to poor-quality meetings when you hover over a location to filter the live meetings table by poor-quality meetings from that location.

## Network performance

This chart shows a trend of the latency and packet loss experienced by participants during meetings that are in progress. You can switch between data for audio and video. You can also adjust the sliding bar to see what the 95th percentile was between a 24-hour period.

## IP by network performance

This chart shows a breakdown of IP addresses and the network quality of participants who connected to those IP addresses. IP addresses are partially masked to preserve the personal identity of users. You can use this chart to see if a specific location or service provider has a higher number of poor-quality meetings than average, and start troubleshooting from there.

Hover over the red bar to see the number, percentage, and location of poor-quality meetings from that IP address. Hover over the green bar to see the same breakdown of good-quality meetings from that IP address.

## Live meetings search table

If you're a full administrator, read-only administrator, or support administrator with the Advanced Troubleshooting Access role, you have access to a table that shows all the meetings that are in progress. Use the search bar to search for specific meetings or quickly filter participants by interacting with the other charts.

For example, if you notice a location with lots of poor-quality meetings in the Live Meetings Map, you can hover over that location and click on the number next to # of Poor Quality Meetings . This will filter the table to only show the meetings that those participants are in.

Another example is in the IP by Network Performance chart. If you hover hover a red bar and click the number of poor connections, this will filter the table to only show the meetings where participants connected to that IP address.

Selected filters show before the search box, which you can remove by clicking the X.

To have a good experience during a Webex Meeting or call, a key requirement is to have good
        video and audio quality. Several factors can degrade media quality during the meeting, such
        as environment, equipment, or the network. For a more in-depth explanation of how
        troubleshooting works, see Troubleshooting Webex Meetings and Calls , which
        highlights key considerations when troubleshooting poor meeting or call experiences and
        outlines the tools available to you to help resolve them.

| 1 | Sign in to Control
            Hub . |
|---|---|
| 2 | Go to Troubleshooting . |
| 3 | Use the Search bar to search for: Meetings —by host email, participant email, meeting number,
            or conference ID. Webcasts —by host email, participant email, meeting number,
            or conference ID. Calls that used Call on Webex —by caller or callee's email
            address. Calls that used Webex Calling —by caller or callee's email
            address that's registered with Webex Calling, phone number, MAC address, or call
            ID. By default, you can see meetings and calls from the last 7 days, but you can click the
            calendar icon  to specify a specific date. You
            can search for meetings and calls that happened up to 21 days ago. The time zone is set according to your profile at the top right corner, but you can
            change the time zone anytime from the drop-down menu. For example, if a meeting host
            comes to you with an issue from a meeting that took place in a different time zone, you
            can switch to that time zone so that you don’t have to do the time conversion. |
| 4 | In the search results, select the meeting or call that you want more information about. |

| Title | Description |
|---|---|
| Meeting No | The 9-digit meeting access code used to join the meeting. |
| Conference ID | The unique ID of the meeting. |
| Site Name | The Webex site used to host the meeting. |
| Meeting Date | The date of when the meeting started. |
| Meeting Time | The time of when the meeting started and ended, shown in the time zone that you selected in the search view. |
| Schedule Timezone | The time zone that the meeting was scheduled in. |
| Meeting Type | The type of meeting that was scheduled. The meeting types available are: Webex Meetings Webex Events Webinar Webex Events Webcast Webex Events Classic Webex Support Webex Training |
| Participants | The number of participants who joined. |
| Host Name | The name of the host. |
| Host Email | The email address of the host. |
| Audio | The type of audio used. |
| Video | If video was enabled by a participant, it shows as yes. If video wasn't enabled at all, it shows as no. |
| Recording | The total duration of how long the meeting was recorded for. |
| Screen Share | The total duration of how long participants shared their screens for. |
| Apps | This field shows if an integrated app, like Slido , was used during the meeting. |
| AI Assistant | This field shows if the Cisco AI Assistant was used during the meeting. |
| End reason | This field shows how the meeting was ended. Possible values are: Ended by host—Name of the host who ended the meeting. No Participant—Meeting is ended by Webex because there are no participants
                    left. Max Duration—Meeting is ended by Webex due to meeting duration limit. |

| Title | Description |
|---|---|
| Join Time | When the participant joined the meeting shown in the time zone you select. |
| Duration | Duration of the meeting. |
| Activity | If the participant was the host, was transferred the host role, or shared content during the meeting. |
| Client | The type and version of the application used to join the meeting. |
| Platform | The operating system and version of the device used to join the meeting. Possible values could be "windows", "mac", "android", "ios", and "linux” |
| Join From | If the participant joined the meeting by browser, this shows the browser type and version used to join the meeting. |
| Hardware | This hardware make and model of the device used to join a meeting. For computers, this might be "Lenovo Thinkpad p60". For phones, this might be "Samsung Galaxy S7". For room devices, this might be "Cisco Webex Room Kit". |
| Connection | The type of network connection that the client used to exchange media. Possible values could be "wifi", "ethernet", "cellular", or "unknown". This is not tracked per media type. It it is possible (and relatively common) that this changes over the course of a meeting. |
| Local IP | The local IP address of the client for the network interface that it is using to transmit media. IP addresses are partially masked to preserve the personal identity of users. |
| Public IP | This is the public IP address of the client as seen by the media servers. IP addresses are partially masked to preserve the personal identity of users. |
| Media Server IP | The IP address of the media service that the client is exchanging media with. The
                  Media Server IP is the network address of the server responsible for storing and
                  delivering media files (such as audio prompts) to clients or applications during
                  media sessions. |
| Location | Geo lookup of Public IP address. |
| Media Node | The datacenter or region of the media node that the client is connected to. For cloud based media nodes this will be a general region name such as "San Jose, USA". For video mesh based media nodes, this will have a more specific name that matches the video mesh cluster name that was provisioned by the customer. |
| System Code | What happened to the participant during a meeting. The system codes available are: Host Hung Up —The host ended the meeting for everyone. User Hung Up —The participant left the meeting early. Time Out —The participant disconnected from the meeting due to a network connection error. Leave Waiting Room —The participant was waiting in the lobby before the host started the meeting. Fallback to PSTN —Callback with Edge Audio failed, so the callback goes through a PSTN connection. |
| Phone | The phone number of the participant. |
| Dialed # | The conference bridge PSTN number. |
| Audio Transport | The network type used to transport audio. Valid values could be "UDP", "TCP", "xTLS". This can change over the course of a meeting, however, only the initial transport used is reported. |
| Video Transport | The network type used to transport video. Valid values could be "UDP", "TCP", "xTLS". This can change over the course of a meeting, however, only the initial transport used is reported. |
| Share Transport | The network type used to transport a screen or application share. Valid values could be "UDP", "TCP", "xTLS". This can change over the course of a meeting, however, only the initial transport used is reported. |
| Audio Codec | (Send) The media encoding and decoding format in use for the media transmitted by a client. Note that this can change over time during a call. (Receive) The media encoding and decoding format in use for the media received by a client. This can change over the course of a meeting, however, only the initial codec used is reported. |
| Video Codec | (Send) The media encoding and decoding format in use for the media transmitted by a client. Note that this can change over time during a call. (Receive) The media encoding and decoding format in use for the media received by a client. This can change over the course of a meeting, however, only the initial codec used is reported. |
| Share Codec | (Receive) The media encoding and decoding format in use for the media received by a client. This can change over the course of a meeting, however, only the initial codec used is reported. |
| Microphone | The brand name and model information for the the microphone that was used during the meeting. This can change over the course of a meeting, however, only the initial microphone used is reported. |
| Speaker | The brand name and model information for the the speaker that was used during the meeting. This can change over the course of a meeting, however, only the initial speaker used is reported. |
| Camera | The brand name and model information for the the camera that was used during the meeting. This can change over the course of a meeting, however, only the initial camera used is reported. |
|  |

| Title | Description |
|---|---|
| Calling Session ID | Unique ID of the call. |
| Calling Date | The date of when the call was started. |
| Calling Time | The time of when the call started and ended, shown in the time zone that you selected in the search view. |
| Session Type | The type of call that was made. The session types available are: Call on Webex—When a caller calls someone using Call on Webex (non-PSTN). Conference call—When a caller adds more people to a Call on Webex call, it becomes a conference call . |
| Participants | Number of participants in the call or meetings started from a space. |
| Caller Name | The name of the user who started the call. |
| Caller Email | The email of the user who started the call. |
| Audio | The type of audio used. |
| Video | If video was enabled by a participant, it shows as Yes. If video wasn't enabled at all, it shows as No. |
|  |

| Title | Description |
|---|---|
| Latency(ms) | Latency is a delay in the delivery of audio or video during a
                                    meeting. |
| Packet Loss (%) | Packet loss occurs when there's a problem transmitting data packets, and some packets are dropped before they're received by the participant. The types of packet loss captured are: End to End —The speaker's sending packet loss from their Webex client to the participant's Webex client, captured after packet recovery. Sending —Participant's Webex client to the Webex cloud. Receiving —Webex cloud to the participant's Webex client. |
| Jitter(ms) | A variation in the delay of packets that are received. |
| Media Bitrate(kbps) | The number of bits processed per second. |
| Frame Rate(fps) | The number of frames that are shown every second of a meeting. |
| Resolution(p) | The number of pixels shown on user’s screen during a given amount of time. |
| System CPU(%) | The total percentage of CPU that is used by all applications. On
                                    a multi-core system, CPU usage is measured across all cores. |
| Webex App CPU(%) | The percentage of CPU that is taken by Webex Meetings or Webex App app during the meeting. On a multi-core system, CPU usage is measured across all cores. |
| System Memory(%) | The total percentage of memory that is used by all
                                    applications. |
| Webex App Memory(%) | The total percentage of memory that is taken by Webex Meetings or Webex App app during the meeting. |
|  |

| Title | Description |
|---|---|
| Client | The type and version of the application used to join the meeting. |
| Location | Geo lookup of Public IP address. |
| Platform | The operating system and version of the device used to join the meeting. Possible
                  values could be "windows", "mac", "android", "ios", and "linux”. |
| Join From | If the user joined the meeting by browser, this shows the browser type and
                  version used to join the meeting. |
| Connection | The type of network connection that the client used to exchange media. Possible
                  values could be "wifi", "ethernet", "cellular", or "unknown". This is not tracked per media type. It it is possible (and relatively common)
                    that this changes over the course of a meeting. |
| Media Node | The datacenter or region of the media node that the client is connected to. For
                  cloud based media nodes this will be a general region name such as "San Jose,
                  USA". For video mesh based media nodes, this will have a more specific name that
                  matches the video mesh cluster name that was provisioned by the customer. |
| Local IP | The local IP address of the client for the network interface that it is using to
                  transmit media. IP addresses are partially masked to preserve the personal
                  identity of users. |
| Public IP | This is the public IP address of the client as seen by the media servers. IP
                  addresses are partially masked to preserve the personal identity of users. |
| Media Server IP | The IP address of the media service that the client is exchanging media with. The
                  Media Server IP is the network address of the server responsible for storing and
                  delivering media files (such as audio prompts) to clients or applications during
                  media sessions. |
| Audio Transport | The network type used to transport audio. Valid values could be "UDP", "TCP",
                  "xTLS". This can change over the course of a meeting, however, only the initial
                    transport used is reported. |
| Video Transport | The network type used to transport video. Valid values could be "UDP", "TCP",
                  "xTLS". This can change over the course of a meeting, however, only the initial
                    transport used is reported. |
| Share Transport | The network type used to transport a screen or application share. Valid values
                  could be "UDP", "TCP", "xTLS". This can change over the course of a meeting, however, only the initial
                    transport used is reported. |
| Audio Codec | (Sending) The media encoding and decoding format in use for the media transmitted
                  by a client. Note that this can change over time during a call. (Receiving) The media encoding and decoding format in use for the media received
                  by a client. This can change over the course of a meeting, however, only the initial codec
                    used is reported. |
| Video Codec | (Sending) The media encoding and decoding format in use for the media transmitted
                  by a client. Note that this can change over time during a call. (Receiving) The media encoding and decoding format in use for the media received
                  by a client. This can change over the course of a meeting. Only the initial codec used is
                    reported. |
| Share Codec | (Receiving) The media encoding and decoding format in use for the media received
                  by a client. This can change over the course of a meeting. Only the initial codec used is
                    reported. |
| Microphone | The brand name and model information for the the microphone that was used during
                  the meeting. This can change over the course of a meeting. Only the initial codec used is
                    reported. |
| Speaker | The brand name and model information for the the speaker that was used during the
                  meeting. This can change over the course of a meeting. Only the initial speaker used is
                    reported. |
| Camera | The brand name and model information for the the camera that was used during the
                  meeting. This can change over the course of a meeting. Only the initial camera used is
                    reported. |
| Noise Removal | This field shows if the participant used the noise
                    removal feature. If noise removal was used, then you can see how long it
                  was enabled. |
| Virtual Background | This field shows if the participant used a virtual
                    background . |
|  |

| Connection type | Title | Description |
|---|---|---|
| Wi-Fi | BSSID | The basic service set identifier of the Wi-Fi access point that the endpoint used
                  for the connection. |
| Wi-Fi | SSID | The service set identifier, or Wi-Fi network name, that the endpoint used for the
                  connection. |
| Ethernet | Switch Chassis | The identifier for the Ethernet switch chassis that the endpoint reported. |
| Ethernet | Switch Port | The identifier for the Ethernet switch port that the endpoint reported. |
| Cellular | PLMN | The public land mobile network identifier that the endpoint reported for the
                  cellular connection. |
| Cellular | Provider Name | The name of the cellular network provider, when available. |
| Cellular | Network Type | The cellular network type, such as 4G or 5G, when available. |

## Figuras

![Search view example in Troubleshooting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/463001-464000/463133.jpg)

![User-centric troubleshooting in Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/474001-475000/474970.jpg)

![Visualization view of user-centric troubleshooting in Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/474001-475000/474971.jpg)

![Meetings icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/410001-420000/417001-418000/417469.jpg)

![In Progress icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/439001-440000/439203.jpg)

![Refresh icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/439001-440000/439202.jpg)

![Enable auto refresh button for in-progress meetings in Troubleshooting.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469664.jpg)

![Image shows how to view which participant is paired with a device when connected through a PSTN](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/455001-456000/455267.jpg)

![Image shows hovering over a participant to view a short summary of their meeting details including client type used, join time, and duration](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438883.jpg)

![Submitting feedback in Troubleshooting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/468001-469000/468087.jpg)

![Image shows a short list of participants' join meeting time](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438910.jpg)

![Expand side menu icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438876.jpg)

![Meeting details tab for Troubleshooting in Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438880.jpg)

![Information icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/410001-420000/417001-418000/417358.jpg)

![Image of chart legend of thresholds](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438877.jpg)

![Panel showing participant media quality samples](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438881.jpg)

![Hardware and network change indicator icon (purple diamond)](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/441001-442000/441741.jpg)

![Green line icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/450001-451000/450895.jpg)

![Red line icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/450001-451000/450389.jpg)

![Host end meeting indicator for Troubleshooting in Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488913.jpg)

![Image shows the view of individual breakout sessions within a meeting](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/455001-456000/455266.jpg)

![Table of details tab which provides a table view of participants](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438878.jpg)

![Participant details record with equipment and networks data](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/439001-440000/439235.jpg)

![Mute icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/450001-451000/450388.jpg)

![Equipment and networks panel showing Webex App on Android 15, Wi-Fi connection details, media node and IP addresses, TLS audio/video/share transport, Opus audio codec, H.264 video codec, and built-in microphone and speaker information.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/438001-439000/438882.jpg)

![Image shows an overview of the Live Meetings tab in Control Hub.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461843.jpg)

![Image shows key performance indicators in Control Hub displaying the number of live meetings and the number of meetings and participants experiencing good network.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461844.jpg)

![Image shows a map in Control Hub of the geographical distribution of live meetings.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461845.jpg)

![Image displays a chart in Control Hub showing the trend of latency and packet loss experienced during in-progress meetings.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461846.jpg)

![Image displays a chart in Control Hub showing the breakdown of IP addresses and the network quality of participants connected to those IP addresses.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461847.jpg)

![Image shows a table displaying all in-progress meetings in Control Hub.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461848.jpg)