---
doc_id: help-webex-com-en-us-article-n5rdoxq-e162c22574
source_url: https://help.webex.com/en-us/article/n5rdoxq
retrieved_at: 2026-11-02T13:03:34.133720+00:00
---

The updates released for Webex Meetings just include some minor fixes and optimizations,
          we are no longer adding any new features.

## March 2025 (45.3)

There are no new features or bug fixes coming in 45.3.

## February 2025 (45.2)

There are no new features or bug fixes coming in 45.2.

## January 2025 (45.1)

Join a Webex Meetings meeting using the meeting link

When you are invited to a Webex Meetings, clicking the meeting link will open a browser
        window to the meeting join page. If you have Webex App installed, click open Webex to join
        the meeting from your app. If you don't have the app, choose 1 of 2 options to download and
        install Webex App or join from your browser directly.

For more information see, Join a Webex meeting using the meeting link .

## February 2025 (45.2)

There are no new features or bug fixes coming in 45.2.

## January 2025 (45.1)

Join a Webex Meetings meeting using the meeting link

When you are invited to a Webex Meetings, clicking the meeting link will open a browser window to the meeting join page. If you have
        Webex App installed, click open Webex to join the meeting from your app. If you don't have the app, choose 1 of 2 options to
      download and install Webex App or join from your browser directly.

For more information see, Join a Webex meeting using the meeting link .

October 2024 (44.10)

There are no new features or bug fixes coming in 44.10.

September 2024 (44.9)

You can find a summary of the latest features and improvements in Webex Meetings, helping you understand and utilize the new functionality effectively.

What's new for the latest channel of Webex Meetings - 44.9

July 2024 (44.7)

You can find a summary of the latest features and improvements in Webex Meetings, helping you understand and utilize the new functionality effectively.

What's new for the latest channel of Webex Meetings - 44.7

June 2024 (44.6)

You can find a summary of the latest features and improvements in Webex Meetings, helping you understand and utilize the new functionality effectively.

What's new for the latest channel of Webex Meetings - 44.6

April 2024 (44.4)

You can find a summary of the latest features and improvements in Webex Meetings, helping you understand and utilize the new functionality effectively.

What's new for the latest channel of Webex Meetings - 44.4

February 2024 (44.2)

You can find a summary of the latest features and improvements in Webex Meetings, helping you understand and utilize the new functionality effectively.

What's new for the latest channel of Webex Meetings - 44.2

Known Issues and Limitations for the Webex Meetings Desktop Application

See the Webex Meetings Web App Known Issues and Limitations for info on the web app.

### Mac Outlook Plugin in the Cisco Webex Desktop App Requires Upgrade to Version 39.5.1

The Webex Mac Outlook plugin doesn’t recognize Webex Meetings in Mac Outlook 16.23 or later for Microsoft Office 365, with the controls still
                showing Add Webex Meeting when users open an appointment and
                try to edit it.

To restore this interoperability between the Webex Mac Outlook plugin and Windows Outlook plugin, you must upgrade your Webex Outlook plugin to WBS39.5.1 or later.

For these changes:

The site administrator must check Automatically link users with
                            this Webex site if their Webex account email address matches their
                            Microsoft Office 365 email address in the Cisco Webex Site Administration’s Configuration > Common Site Settings > Third-Party Integration .

The administrator must authorize Webex access to Microsoft Office 365 in Webex Site Administration. Select Add New Authorization to start the process.

For more information on deploying and configuring the Cisco Webex Scheduler for Microsoft 365, see Deploy and
                            Configure the Cisco Webex Scheduler for Microsoft 365 .

Ensure the email address that's used in Webex is the same as the Microsoft 365 account, and that the email address is
                        verified in Webex.

For more information on email verification, see:

Cisco Webex Meetings Email Verification

Verify an Email Domain in Cisco Webex Site Administration

Known Issues with the Webex Outlook plugin WBS39.5.1

Interop issue on Personal Room meeting: The Webex Personal Room meeting information can't be deleted when selecting Cancel Webex Meeting Webex Meetings in Mac Outlook if the meeting is created or updated by the Webex Outlook plugin for windows. A workaround for this is to cancel the
                        Outlook appointment.

Interop issue on PCN meeting: The button still shows Add Webex
                            Meeting when users open the appointment in Mac Outlook if
                        the meeting is created or updated by Webex Windows Outlook plugin. There’s no workaround.

Schedule on behalf of the issue on MAC outlook version 16.25(19051201): A Mac
                        Outlook defect is identified and it impacts the Webex Scheduler. This Outlook defect was fixed in the Microsoft Office slow
                        channel 16.26 (19053000) and Microsoft Office fast channel 16.27(19060500).
                        This defect is that when an assistant opens another person’s calendar, and
                        tries to create an appointment for that person, the appointment is created
                        for the assistant. The workaround is to upgrade to Mac Outlook 16.26 or
                        later.

Dependencies

Sites that have upgraded to the new Webex Mac Outlook plugin 39.5.1, but don't meet the preconditions receive an error
                message when trying to update or edit a Webex meeting.

Backward compatibility

This new version doesn’t fix previous meetings that were scheduled by the old Webex Windows or Mac Outlook plugins. The same error message appears when users try to
                update or edit a Webex meeting.

Cisco Webex is redirecting the primary service to GSB for this change.

Without this upgrade, users are unable create and update Webex Meetings using the Webex Mac Outlook plugin.

Sites receive this update automatically only if the Auto Update is enabled.

### General Webex Meetings Desktop App Known Issues and Limitations

After the Webex desktop app is installed, there are two items in the Windows application
                        list. Selecting either for uninstallation removes both of them.

After users start a meeting from desktop app, there are two Webex icons on the task bar. These will be merged later.

The user interface display may appear distorted after DPI is change on Microsoft Windows. To correct it, sign out of Windows and sign in again.

Scheduling in Microsoft Outlook with an account set up from Google Calendar isn’t supported.

The desktop app can only read the meeting list when Microsoft Outlook is installed and logged in. Mac users must configure their Outlook account email address and password the first time they use the application.

For Windows 7 and Outlook 2016 users, the desktop app may not be able to scrape the meeting list from the Outlook calendar because Windows 7 doesn’t have some library files that Outlook 2016 needs. See the Microsoft website to download the Visual C++ Redistributable Packages. Windows 7 and Outlook 2013 don’t have this issue.

Windows users may receive a MAPI error when the desktop app attempts to read the meeting list from the Outlook calendar. Exit the Outlook application and restart.

When users try to start or join Webex Meetings which require authentication on a different site, the meeting application
                        will redirect user to the browser first. Cisco and Cisco Webex Events (classic)Webex Training users are also redirected to the browser first.

When users try to join a meeting on a Webex sites which is different from the site that signed in through the desktop app,
                        the start and join flows are redirected to the browser first instead of
                        launching the Webex Meetings application.

The proximity pairing function of the desktop app only uses exclusive mode to try to pair with Cisco video devices when users click Connect to a Device on Windows. This means that other applications running in exclusive mode blocks or impact the pairing.

The proximity pairing function may not work on Windows if the setting Enable Audio Enhancements is enabled. To prevent this, follow these steps:

From the Recording tab of your Windows Sound configuration screen, select Properties , then disable (uncheck) Enable audio enhancements .

If a PC has multiple screens, only the content on the main screen is shared to the paired Cisco video devices.

If the PC has a headset that's plugged in, Cisco video devices won't be detected through proximity.

When the endpoint is paired with desktop app, "Share On Device" means project
                        your desktop to the video system screen wirelessly without Webex Meetings.

The Webex Meetings desktop app does not show meeting information shared from the Hybrid
                        Calendar Service.

If you select Webex as the calendar that you use for your meetings list, meetings scheduled in Personal Rooms don't appear.

Webex Meetings Desktop app can't pair with a public IP address device using the
                        Proximity for the security reasons.

Known Issues and Limitations for Webex video platform version 2

This section applies only to Webex Meetings sites that have the Media Resource Type list available in the Cloud Collaboration Meeting Room site options. Contact your administrator for more information.

H.264 video codec required for content sharing

Content sharing is only supported using H.264 video codec. Older video systems that do not support H.264 codec will not be able to do content sharing.

In-meeting video thumbnail experience

Any cascades in Webex Meetings are limited to up to six streams at a time in either direction. For example, Webex Meetings participants only see up to six video streams of Webex Video Platform users connected through Webex Cisco Webex, Webex Room and Desk Devices, Skype for Business, and other SIP or H.323 devices connected to the meeting. Likewise, Webex Video Platform users only see up to six participants using Webex Meetings apps including apps for desktop, mobile, and web. Also, any participants that are connected through Webex Video Mesh nodes have the same limitation between their specific Webex Video Mesh node and devices or apps that are connected directly to the Webex cloud or other Webex Video Mesh nodes.

On-premises-registered video device roster

An on-premises-registered video device roster has a limitation for the number of
        participants displayed. Therefore, that roster may not show the total number of participants
        in the meeting, as reflected in the Webex Meetings desktop app.

Known Issues and Limitations for Webex Meetings

### Prompted to install Webex Meetings multiple times

If you clear your cookies in Google Chrome, Mozilla Firefox, or Safari, you may see the
        install screen again the next time you join a meeting from your web browser, even if you
        already installed the desktop app. If you click the install file, you launch the desktop
        app.

### Recording playback on mobile devices

You cannot play back a network-based recording on a mobile device.

### Default meeting templates

If the First attendee to join will be presenter option is enabled in
        Site Administration, this option is enabled by default in the meeting scheduler on your Webex sites. It is also enabled in the default meeting template that you use in Productivity Tools
        for scheduling Webex Meetings with Microsoft Outlook. Custom meeting templates that have been created by users are not
        impacted. If a host schedules meetings using custom templates and wants to have the first
        attendee to join the meetings automatically become the presenter, the host must manually
        enable the setting in the custom templates.

### Network-based recordings

Network-based recordings require a minimum bandwidth of 2.0 Mbps to play smoothly;
        otherwise, pausing might occur.

### MP4 Playback in non-Webex Meetings video meetings not supported for the Webex Meetings desktop app for Linux

Linux users on the Webex Meetings desktop app can't start or join a non-Webex video meeting that has enabled MP4 playback. They receive a warning message indicating
        their operating system is not supported for this meeting, because Linux only supports ARF
        recording format.

We recommend that Linux users use the Webex Meetings web app for MP4 playback support in non-Webex video meetings.

### Active audio-only meetings recycled

Audio-only meetings are recycled according to the 90-day meetings recycle period, or
        180-day recurring meetings recycle period, even if the meetings were hosted or joined within
        that time.

### Personal Rooms

Windows 8 phones and the Webex Meetings desktop app for Linux —You can't start or host
        a meeting in your Personal Room using a Windows Phone 8 device or the Webex Meetings desktop app for Linux.

We recommend that Linux users use the Webex Meetings web app to start or host meetings from their Personal Rooms.

Personal Room lobby —Users of the following devices or applications cannot wait in the
        lobby while a Personal Room is locked: Webex Meetings desktop app for Linux, TelePresence devices, and Windows Phone 8 devices. In addition
        users who join only the audio portion of the meeting cannot wait in the lobby while a
        Personal Room is locked. These users will receive a message that the room is locked, and
        will not be able to join until the room is unlocked.

We recommend that Linux users use the Webex Meetings web app to wait in a lobby while a Personal Room is locked.

For more issues that affect Personal Rooms and Webex Meetings video, see Cross-platform Features and Known Issues .

### Webex Meetings web app

Video Limitation

VoIP is not supported when the host account has Webex Meetings video conferencing disabled.

### Slow join times after a major upgrade

After a major Webex Meetings Suite upgrade containing more new features than
                                                  a regular service pack release, you may encounter
                                                  a long load time, as more files have to be
                                                  downloaded and installed. Loading times depend on
                                                  your network's bandwidth and the amount of traffic
                                                  at the time of the download. In general, load
                                                  times can range from 20 seconds to 3 minutes or
                                                  more.

### One meeting at a time

Mac users can join only one meeting at the same time.

### In-meeting experience

When the language is set to Korean, the meeting topic might sometimes show incorrect characters.

The video settings button does not appear for the Participants panel on a Mac when a participant is viewing shared content in full-screen mode.

Keyboard navigation and screen reader support:

Video thumbnail items in the Participant panel do not support navigation using the Tab key.

Some items in file sharing and in the Polling panel don't support navigation using the Tab key.

Items within the video full-screen view don't support navigation using the Tab key.

Elements inside the video user interface don't support screen readers.

Video thumbnail items don't support screen readers.

The participant list within the Participant panel doesn't support screen readers.

Some elements for file sharing and in the Polling panel don't support screen readers.

The Pan tool is not available when viewing a file that is shared using file sharing.

The new interface is not available for Linux users.

On Mac, when the presenter annotates during application sharing or screen sharing (formerly called desktop sharing ) and takes notes or creates a poll, the Notes and Poll information cannot be saved.

On Mac, when using annotation during sharing, if user moves from tab view to full-screen view, the annotation option that as last used is not remembered.

On some Windows machines as well as on Linux machines, if attendee screen saver comes on and then the presenter starts file sharing, the screen saver automatically quits.

Some custom Quick Start templates, created using older releases of Webex Meetings, may not work after upgrading to this release.

In a few cases, uploading a very large Microsoft PowerPoint file to share in the meeting may cause the meeting to get disconnected for the presenter.

### Initials in avatars

The first letter of a user's first name and the first letter of the user's last name are used in avatars when there is no image available. Users with second names comprised of more than one word will not be displayed correctly as three letters, for example, "Mary Van Buren" and "Robert Smith Jr." will display as "MB" and "RJ" respectively.

### Anyone can share feature

The Anyone Can Share feature is not available for Linux users on the Webex Meetings desktop app. It is also not available for mobile users who are using earlier versions
            of the Webex Meetings mobile app. This feature will be supported in the Webex Meetings app version 6.6 or later for iPhone and iPad and version 6.5 or later for Android
            devices. Mobile users who have earlier versions of the application can still be made
            presenters by passing the presenter role to them only if the mobile app has presenter
            capabilities.

We recommend that Linux users use the Webex Meetings web app to access the Anyone Can Share feature.

If a host starts a meeting on a desktop and then disables the Anyone Can Share feature
            while in a meeting, participants in that meeting who are using earlier versions of the
              Webex Meetings app for iPhone, iPad, and Android devices will still be able to share.

Users of the Webex Meetings mobile app will not be able to disable the Anyone Can Share feature within a meeting,
            but will follow the site administration settings for that feature.

### Host role taken over by a joining alternate host

In some circumstances, the host role may be taken over by an alternate host when joining a meeting or session, even if the host has already joined. If this occurs, we recommend the alternate host assigns the host role back to the host.

### Links generated by Webex Meetings and Webex recording services

As part of our continuing updates to improve security, Cisco is making changes to improve
        the management of cryptographic keys that are used to generate URLs used in the Webex Meetings Suite and Webex recording services. As a result, existing links that were generated by those services
        have been updated, and sometimes, users may need to request new links.

### Multi-monitor support in Windows 10

Shared content may get cut off or display partially when sharing from a secondary screen that has a higher resolution than your primary screen. To remedy this, we recommend that you set your largest display to be your main display in your Windows display settings.

### Shared documents display quality

Webex Meetings uses a printer driver interface to import documents that are not natively supported. The
        presentation quality of documents shared in Print Driver mode, such as Microsoft Word,
        Excel, and Adobe PDF documents, cannot be better than a hard-copy printout of the same
        document printed by a physical printer. This issue is pronounced when these documents
        contain images of text.

### Cropped, cut off, or misplaced drawing objects

Drawing objects partially or wholly outside the 15-bit twips (32768 x 32768 twips = 22.75 x
        22.75 inches) coordinate range are not displayed, cut off or misplaced. This includes
        regular PD drawing objects, images, UCF objects, and annotations. The actual size on pixels
        depends on the screen resolution and screen size.

To avoid this issue, we recommend you resize large documents to fit within the above
        coordinate range.

### Microsoft Office 2013 and later support

If you have Microsoft Office 2013 or later installed, the following features are not supported when sharing PowerPoint files:

Animations and transitions

Embedded video or audio files

UCF Toolkit

If you have
                                                  customized your Info Tab, some custom elements may
                                                  not be supported. We recommend that you validate
                                                  it to make sure it continues to display properly
                                                  in a Webex meeting.

In a few cases, the following problems may occur:

Text and fill colors may be slightly different from the actual colors in a slide.

Some graphic elements may be missing from a slide.

Fonts may appear blurry on a slide or may be different from the original.

The size of shapes may be different from the original.

If an object in a
                                                  PowerPoint presentation does not display correctly
                                                  in edit mode, it is automatically removed in Slide
                                                  Show view; however, the object may continue to
                                                  display when the file is shared in a Webex meeting.

You cannot share password-protected PowerPoint 2013 files using the file sharing feature. Use the application sharing or desktop sharing features instead.

You cannot share Excel 2013 files on Windows 8 using the file sharing feature. Use the application sharing or screen sharing (formerly called "desktop sharing") features instead.

You cannot share Word 2013 (64-bit) documents on Windows 8 (64-bit) using the file sharing feature. Use the application sharing or screen sharing features instead.

### Tagging internal participants

Tags for internal participants do not appear in the following cases:

When the participant joins from mobile device

When a participant using One-Touch TelePresence Plus is not using SAML single
            sign-on

In Personal Conference meetings

### File sharing

If you are a host using Windows and do not have a universal printer driver that is
        installed on your system, you will not be able to share any file types except Microsoft
        PowerPoint files during file sharing. In this case, the system will provide an option to
        move to application sharing instead of file sharing or to install a universal printer driver
        before you proceed. (Windows 7 systems come pre-installed with a universal printer driver.)

### Streaming media sharing

Attendee video resolution is optimized to 480p. Video files with higher resolution are
        resized to fit (640 X 480) resolution. The following media file formats are currently
        supported: WMV, WMA, WAV, MP3, ASF, AVI, MPG, MPEG, FLV, F4V, and MP4.

Recommended System requirements for video file sharing on Presenter side:

Core2-Duo E6750 @ 2.66GHz for VGA file is required

AMD 9650 2.3GHz (4 core) 8GB is preferred

Intel® Core™ 2 Duo -E7400 2.8GHz 2.79GHz is preferred

### Audio switching to internal speakers when file sharing

If you are using an external audio device such as headphone or external speakers, sharing a
        file with sound, such as a WRF file, forces the Webex Meetings application to switch to the internal speakers, even if you select an external source in
        the Webex Meetings sound settings. The application returns to the external device once you stop sharing the
        file.

### Unable to join meeting

Linux/Unix users might not able to join the meeting if NTLM authentication is enabled with
        ISA proxy. We recommend that Linux users use the Webex Meetings web app as a workaround.

### Viewing Office 2007 and later documents

Attendees who join a meeting from the Webex Meetings desktop app for Linux/Unix may have display issues when the presenter shares a Microsoft
        Office 2007 and later document. For example, some animations and pictures may not be
        displayed or become distorted. As a workaround, we recommend that attendees use the Webex Meetings web app.

### Microsoft Office PowerPoint

In Microsoft PowerPoint 2007 and later, text that is copied from a web page and pasted into
        the notes panel may not render properly. A workaround is to copy the text into Microsoft
        Word or Microsoft Notepad, then copy the text again from that editor in the notes panel.

### Importing contacts into Microsoft Outlook 2010

Importing your company address book into your Webex Meetings contacts is not supported with Microsoft Outlook 2010 64-bit.

### Closing a meeting

In Internet Explorer 7, if there are multiple tabs open in the browser, and the Webex Meetings "Meeting in Progress" page is not the tab in the foreground, the meeting manager cannot
        be closed. The reason is that the "Close meeting" confirmation dialog box becomes hidden if
        another tab is on top of the Webex Meetings page.

### Full-screen video view

When the presenter switches to full-screen video view while sharing his or her screen
        (formerly called "desktop sharing"), an application, or a document, sharing is paused on the
        attendee side (the last-shared screen freezes) if they have only one monitor. When the
        presenter exits full-screen video view, sharing automatically resumes.

Attendees stay in full-screen video view when the presenter stops sharing and automatically
        exits full-screen video view when the presenter starts sharing again.

If the presenter has two or more monitors, they can easily share content on one monitor and
        switch to full-screen video view on another monitor.

### Automatically restarting a meeting on a backup site

There is no automatic shared state recovery when a site becomes unavailable and
        automatically redirects to your backup site that was backed up with the Webex Global Site Backup (GSB) system. After the Meeting window reconnects to the meeting on a
        backup site, the shared state is lost and the presenter must start sharing content.

### End-to-end encryption using PKI

End-to-end encryption of in-meeting data using a public and private key pair that is
        provided by the site administrator is no longer supported. End-to-end encryption in a live
        meeting continues to be available using an automatically generated session key only.

### Denied access on iOS device after upgrade

You may be prevented from joining a meeting from your iOS device with the error message
        "The version of your Webex Meetings application is not compatible with the current Webex service. Upgrade the application now." This is because of a security option to enforce
        secure access after all mobile app upgrades.

### Overlapping meetings prematurely ending

Overlapping meetings may end at the first meeting's end time sometimes.

For example, if a host schedules a daily repeat meeting with 24 hours duration with a
        starting time of 8:00 a.m. and the meeting supports joining before host 15 minutes before
        the meeting start, and if the host is not present, the meeting ends at 8:00 a.m. and host
        and participants must join the meeting again.

### Limitations during screen sharing

You cannot interact with system applications on a remotely controlled computer, even if the
        presenter on that computer is sharing their screen.

### Unable to join before host when meeting has already been started

When hosts schedule a meeting in Microsoft Outlook and check Attendees can join
          meeting X minutes before starting time , if the meeting has already been
        started before on the same day, participants can connect to the meeting audio using their
        computer only after the hosts starts the meeting. This is a security feature.

### High frame rate content sharing

In Webex Meetings, there may be intermittent issues with some participants being able to see shared content
        when Optimized for motion and video is selected. A fix is planned for
        a future update. Until then, you may need to uncheck this option if the issue persists.

### Unable to pair with Proximity

Webex Meetings desktop app can't pair with a public IP address device using Proximity for security
        reasons.

### Remote Desktop Protocol

The Remote Desktop Protocol is not supported for Webex Meetings.

### Certain meetings don't appear in your calendar without Hybrid Calendar

If you don't have Hybrid Calendar , the following meetings don’t appear
        in your calendar on your Webex site or the Webex Meetings app:

- Personal Room meetings

- Meetings that you didn't receive a direct invite to (forwarded invites or invites sent
          to a distribution list)

- Meetings hosted on a different Webex site

Known Issues and Limitations for Remote
        Access

### Joining a Webex Meetings on Chrome and Firefox

With the Google and Mozilla policy changes, users need to manually enable the Webex plug-in when using Chrome and Firefox.

### Remote Access agents limitation

The Make Screen Blank command is
                disabled in Windows Safe mode.

Known issues and limitations for Webex Meetings Slack

Users in Slack (including meeting hosts) will not receive notifications about meetings starting and ending, participants joining and leaving, and recording ready events inside Slack because of changes to the structure of the join link.

Direct message limitations:

Meeting reminders and in-progress notifications for meetings don’t appear in direct messages.

Recording reminders for recorded meetings don’t appear in direct messages.

When you use the /webexschedule command in a direct message, the direct message participants aren't automatically added as meeting attendees.

The /invite [@botname] command doesn't work in direct messages.

When you schedule a Webex meeting or a Personal Room meeting that starts within 10 minutes, you'll see a Start Meeting button in the meeting notifications that appears in the conversation. Otherwise, you'll be sent a meeting reminder 10 minutes before the meeting is scheduled to start. It'll remind you to use the /webexschedule list command to show a list of your upcoming meetings. Hosts can start the meeting by selecting the Start button that appears next to the meeting in the list. Invitees can use the /webexschedule list command to show a list of their upcoming meetings and then select the Join button that appears next to the meeting in the list.

Meeting hosts must either login to the Webex App or the Webex site in a browser to start or join their meetings.

Personal Room meetings scheduled in Slack aren't shown in your meetings list on your Webex site. Also, invitation email messages aren't sent to invitees.

To see the " In a Webex meeting" status for all members of a workspace, including workspace administrations, the primary owner must install the Meetings app.

Known issues and limitations for Webex Meetings web app

The Meetings web app supports Meetings, Webex Events (classic), Webex Webinars, and Webex Training. The web app doesn’t support Webex Support.

For Events (classic) and Training, the web app supports attendees only. (Hosts and Panelists must use the desktop app.)

We recommend using Meetings or Webinars, so that hosts, cohosts, and panelists can join using web app.

The Meetings web app isn’t available in meetings that have end-to-end (E2E) encryption enabled.

If the UDP 9000 and TCP 5004 ports are blocked from your network, video isn't available for the Meetings web app.

The web app supports content sharing only in Chrome, Firefox, and Edge 77.0.235.20 and later.

To enable content sharing in Chrome version 71 or earlier, install the Webex app and Webex Content Sharing extension.

The web app supports only meetings that are enabled for Webex video or for MP4 recordings.

The Meetings web app doesn't have a whiteboard panel. Participants who use the web app can't see whiteboards that others share during Meetings, Events (classic), Webinars, and Training sessions.

Disabling application or desktop sharing in the session type doesn’t affect the ability to share content from the web app.

Sharing content is currently not available during a Breakout Session in meetings.

Known issues for Application Sharing:

Sometimes, when several applications are open on Windows 10, not all open application windows appear in the Share Application selection menu. We recommend closing unnecessary windows and trying again, or using the Share Screen option instead.

Sometimes, your edits to a document aren't visible during application sharing. For others to see your updates, you may need to stop and reshare the application. You can avoid this problem by using Share Screen, where users can see your edits in real time.

With macOS Catalina (10.15), Apple introduced new security and privacy features for Mac devices. In order to share your screen in the Meetings web app, ensure that your browser has the Screen Recording permission enabled.

In your device System Preferences, give your web browser privacy permissions, and restart your device for the changes to take effect:

If you don't grant permissions, you may see the following prompt when trying to share your screen:

- Web app doesn't support annotating on shared files in a
            meeting.

Presenters can’t pass keyboard and mouse control to attendees who join using the Meetings web app.

You can’t request control when a user is sharing from the Meetings web app.

The web app supports the “Call using computer” audio option, only on Chrome, Firefox, Safari, and Edge.

To enable the full “Call using computer” experience, disable the “block websites from automatically playing sound” option in Firefox.

The web app supports sending and receiving video on Chrome, Firefox, Safari, and Edge.

When using the Meetings web app in Safari, your webcam video automatically stops when you open a new browser tab. You can manually restart your video after returning to the tab running the web app.

If you’re behind a firewall that blocks UDP connections, you can't send and receive video in the Edge browser.

Attendees who join from Internet Explorer browsers can’t view other participants' videos, and can’t turn on their own video. To view other participants' video and turn on your own video at the same time, we recommend that you:

Use a Chrome, Firefox, Safari, or Edge browser.

Switch to the Meetings desktop app.

Grid View in the web app supports up to six videos, with a maximum resolution of 180p.

Sometimes, in Grid View, when several people are talking back to back, there’s delay in the active speaker video response. The delay can cause the video to look duplicated for a brief moment.

If you use Internet Explorer in Compatibility View for Webex sites, the Join using browser link doesn't appear. We recommend that you turn off Compatibility View for webex.com URLs.

When attendees disconnect from the network, the web app displays the audio connect status is incorrectly.

If the meeting name exceeds the maximum allowed length, it’s truncated.

When you remove the camera, the status of the send and stop video button is incorrect. It resets to the correct status after you reopen the video dialog.

To switch to the desktop app from the Edge browser, manually close the web app browser window, and then manually reconnect in the desktop app. The Edge browser can't automatically disconnect from the web app.

You can't switch seamlessly to the desktop app if you're using the web app in a private or incognito browser window. You're prompted to install the desktop app, even if you already have it installed. To avoid this issue, launch the desktop app manually.

Call using computer not supported when the host account has Webex video disabled.

Call using computer isn’t supported in meetings using the “Use VoIP Only” conference type.

When a participant using the desktop app shares video using Share > File , the video doesn’t display in the web app. When a participant using the desktop app shares a media file, attendees can’t see it using the web app. These users are prompted to switch to the desktop app.

Sometimes, there may be an issue sending and receiving video when joining back-to-back
          meetings in the Firefox browser. If you encounter this, simply close the Firefox browser
          and rejoin.

Meeting Options can not be managed from within the web app.

Gesture recognition is not supported in the web app.

Events (classic)

Events (classic) support is currently for attendees only. Hosts and panelists must use the desktop app. (Alternatively we recommend using Webex Webinars.)

The web app does not support entry and exit tones that are configured in an event.

When switching from the web app to the desktop app in an event, you must manually reconnect to
          audio in the  desktop app.

Audio broadcast is currently only available in Chrome, Firefox, and Safari.

The Mute or Unmute icon appears in the Participants list next to web app attendees connect to audio broadcast.

It will appear as if hosts are able to mute or unmute web app attendees who are connected to the audio broadcast, even those users who do not have the ability to speak.

When connected to audio broadcast in the web app, the “request to speak” feature will require you to switch to the desktop app.

Only Webex audio broadcast is supported. Events (classic) set to use audio broadcast by using the “ Other teleconference service ” audio type will require attendees to join through the desktop app.

The post-event survey web app does not pop up the Events (classic) feedback form after an attendee leaves an event.

Like all clients, photo avatars are not currently supported in Events (classic). It will display a user’s initials.

Participants joining an event on the Webex FedRAMP platform can only join the computer audio of a session that has scheduled with Audio Broadcasting enabled.

Training

Training support is currently for attendees only. Hosts and panelists must use the desktop app.

If a host in the desktop app tries to pass the host role to an attendee in the web app, the host role is automatically passed back to the host in the desktop app.

There is a rare case where, if the host unexpectedly gets dropped from the Training session, it may look like the host role was automatically assigned to a user in the web app, though they, in fact, do not have host privileges. In this case, the host role may be reclaimed by a participant in the desktop app.

Web app users can't view whiteboards or shared files in breakout Sessions.

You can't create breakout sessions from the web app. We recommend using Meetings instead.

You can't switch to the desktop app while in a breakout session. To switch to the desktop app, leave the breakout session first.

In training sessions scheduled with the setting “This session will have over 500 attendees” enabled, attendees in the web app are able to see the participant list, unlike in the desktop app.

Custom “Session Options” set in the Training scheduler are ignored in the web app, as all panels are available by default.

Known Limitations for Webex Meetings for Google

If a user who has more than one Webex account signs in to one Webex account (such as companyA.webex.com) in the Chrome browser, and then
                        signs in to the Webex Meetings for Google extension with the user’s Google account, and uses a different
                            Webex account (companyb.webex.com) with different credentials, that user will
                        not be able to sign in to Webex Meetings for Google. If this problem occurs, the user should sign out of the
                        Chrome browser and clear cookies, and then try to sign in again to Webex Meetings for Google.

If a user signs in to Google calendar with one Google account, and then signs
                        in to Webex Meetings for Google with a different Google account, when the user selects
                        Schedule Meeting in the Webex Meetings for Google window, the calendar won’t
                        open and won’t display the scheduled meeting, even though the meeting may
                        have been scheduled successfully.

If a user’s Personal Room meeting settings change, those changes won’t be
                        reflected in Webex Meetings for Google automatically. Personal Room meeting settings changes are
                        synchronized when the user restarts the Chrome browser, or signs in to Webex Meetings for Google again, or signs in to their Webex account through Webex Meetings for Google.

When the host adds Webex Personal Room meeting to a meeting in their Google Calendar, a
                        confirmation appears that includes the video address, but invitees do not
                        see this video address. However, invitees can see the video address and the
                        meeting link in the invitation.

Sometimes the Webex Meetings for Google window doesn’t display completely. If this happens, the user
                        can try double-clicking the Cisco Webex Meetings for Google icon in the Chrome browser.

Known Issues and Limitations for
        WebACD

Links generated by Webex applications and Webex recording services

As part of our continuing updates to improve security, Cisco is making changes to improve
        the management of cryptographic keys used to generate URLs used in Webex Meetings, Webex Training,Webex Training, Webex Events (classic), and Webex recording services. As a result, existing links that were generated by those services
        have been updated, and in some cases, users may need to request new links.

### Windows 8.1, and 10

- For file sharing, you must have Adobe Acrobat Reader to
                                                  share PDFs.

- When sharing Microsoft PowerPoint files in Print Driver
                                                  mode, some content may not appear. We recommend
                                                  that you use our standard Universal Communications
                                                  Format (UCF) mode or use application sharing
                                                  screen sharing instead.

- When connecting to a remote computer with Windows 10,
                                                  the local screen will not be able to be blacked
                                                  out.

- Webex Meetings attendees are able to save Universal
                                                  Communications Format Files (UCF) to their
                                                  computers, even when the host has canceled the
                                                  save privilege for them.

- Windows apps do not appear in the Access Anywhere or
                                                  Remote Access Add Application dialog box.

- When a Mac participant of a Webex meeting is sharing and annotating the
                                                  whiteboard, the annotation color is incorrect when
                                                  the square or oval shape is selected.

Known Issues and Limitations for Site Administration

### Branding and customization

The new Webex header does not allow branded headers to be less than 75 px. If a branded site has a header height that is less then 75 px and does not have customized header HTML code, the system automatically increases header height to 75 px.

The Log in and Log out links for the Site Administration tool are not visible if the header navigation color is blue or a dark color.

If you want to make branding changes, you should contact Cisco support.

### Safari browser support

The Safari browser is not supported for Site Administration on the Mac.

### CMR Hybrid (Webex-enabled TelePresence) meetings

The following issues apply for CMR Hybrid (Webex-enabled TelePresence) meetings:

To reduce the possibility of bandwidth issues for video, site administrators should make sure the following site administration options are set for CMR Hybrid users:

Make sure that for Webex VoIP and video connection, the Automatically encrypted UDP/TCP SSL option is always selected.

Select Site Settings > Site Options and check the maximum video bandwidth option. This sets the maximum video frame rate for in-meeting video. The default setting is 15 fps.

Under "OneTouch TelePresence Options," make sure Enable TelePresence bandwidth control is checked unless Webex Support recommends altering it.

Under "Meeting Options," make sure that Turn on high-definition video is turned on so that resolutions higher than 360 p can be sent.

For additional information about recommended bandwidth configuration settings for CMR Hybrid meetings, see "Prerequisites" in the Cisco Collaboration Meeting Rooms (CMR) Hybrid Configuration Guide on the Cisco TelePresence Management Suite (TMS) Configuration Guides page.

Site administrators should also make sure that Webex Meetings PRO TelePresence session type is enabled for your site:

Webex Meetings PRO TelePresence session type will give users a different user interface in the Webex Productivity Tools integration to Microsoft Outlook than the standard Webex integration with Outlook.

If you want existing users on your site to use CMR Hybrid, you need to batch-enable them for Webex Meetings Pro TelePresence session type-it is not enabled for them automatically.

When your site is enabled for CMR Hybrid, the Default for New Users checkbox is automatically checked next to Webex Meetings PRO TelePresence session type site administration option. If you do not want new users to be enabled for CMR Hybrid automatically, you should uncheck the Default for New Users checkbox.

You can also create additional custom session types based on Webex Meetings TelePresence session type.

Site administrators cannot make any changes to CMR Hybrid user interface for Webex Productivity Tools. For example, administrators cannot change the branding for the CMR Hybrid Meeting Options panel within the Outlook integration, cannot hide information in the Meeting Options panel or in the TelePresence or Webex Advanced Settings dialog boxes, and cannot limit the number of video call-in participants the user can enter.

Although screen sharing (formerly called "desktop sharing" and application sharing are supported in CMR Hybrid meetings, some standard sharing features, such as file sharing, annotation, and whiteboard sharing, are not supported in CMR Hybrid meetings.

Recording is supported for CMR Hybrid meetings; however, it has the following known issues and limitations:

CMR Hybrid meeting recordings will be in MP4 format. Video will be recorded at 360 p.

When users play back the recording, they can see screen sharing, application sharing, active speaker video camera feeds, the participant, list, chat, and polling. However, if users download the recordings, the screen sharing, application sharing, and audio portion is in one MP4 file, and does not contain active speaker video camera feeds, the participant list, chat, and polling.

If you do not have adequate bandwidth, your presentation and data sharing in Webex video conferencing and CMR Hybrid meetings can degrade to XGA (1024 x 768 resolution) and 5 fps. On TelePresence systems, users see a "letterbox" format. Up to 720 p resolution is supported as long as all Webex participants have at least 2 Mbps, and the data sharing can cover the whole TelePresence system screen on both 4:3 and 16:9 TelePresence systems without cropping. With TelePresence Server 4.1 and Conductor XC 3.0, 1080 p resolution is supported as long as all Webex participants have at least 3 Mbps. If any participants in the meeting do not have the minimum bandwidth, all participants will drop to the next lowest data sharing resolution level. For example, if 720 p resolution was used, but one participant has bandwidth that is below the threshold, the meeting resolution drops to 720 p for all participants. Or, if TelePresence Server 4.1 and Conductor XC 3.0 are used, 1080 p would normally be supported, but if one participant does not have least 3 Mbps, the data sharing resolution drops to 720 p for all participants. The presentation and data sharing quality from TelePresence system to TelePresence system does not change, and the resolution is based on TelePresence Server or Cisco TelePresence MCU series settings. The presentation and data sharing quality from Webex application to Webex application is good quality. These presentation and data sharing quality limitations do not apply to Webex-only meetings, which use a proprietary data rendering format.

For a list of compatible video systems and applications see Webex Meetings Video Compatibility and Support

Screen sharing (formerly called "desktop sharing") and application sharing are supported in CMR Hybrid meetings, but some standard content sharing features, such as file sharing, annotation, and whiteboard sharing, are not supported.

Starting with Cisco TelePresence Management Suite (Cisco TMS) version 14.4, administrators can configure Cisco TMS to allow TelePresence participants to join a CMR Hybrid meeting up to 5 minutes before the scheduled start time. TelePresence doesn't join the meeting until the first TelePresence participant dials in to the meeting. Cisco TMS does not dial out to Webex until the scheduled start time of the meeting. For more information, see "Configuring Allow Early Join" in the "Configuring Conference Settings in Cisco TMS" section of the Cisco Collaboration Meeting Rooms (CMR) Hybrid Configuration Guide on the Cisco TelePresence Management Suite (TMS) Configuration Guides page.

CMR Hybrid meetings do not support "VoIP Only" audio.

Scheduling large CMR Hybrid meetings requires that administrators set capacity limits. To mute everyone except the speaker, participants need to be muted in both Webex and TelePresence:

From the Webex application, the host can mute Webex participants.

On some TelePresence systems, the host can mute other TelePresence participants; otherwise, the administrator can mute TelePresence participants through TelePresence Server.

See Open
                    and Resolved Bugs for the Slow Channel Webex Meetings Updates for info on
                the slow channel updates.

We report open and resolved customer-found bugs of severity 1 to 3. When an update
                does not include customer-found bugs, there will not be a Resolved Bugs list shown
                for that update.

You can find details about listed bugs and search for other bugs impacting specific
                    Webex Meetings updates by using the Cisco Bug
                    Search Tool . For more info on using the Bug Search, see Bug Search Tool Help .

Open Bugs for Webex Meetings

The bugs listed in the following table describe unexpected behavior in this release. Refer to Bug Search Tool for further details.

Bug Number

Affected Product Area

Description

CSCvh90269

The Make Screen blank feature doesn't work on Windows 10 devices if User Account Control is enabled.

CSCvi72293

Webex Meetings (Mac)

If a user's Facebook account is locked, they can't stream Webex meetings on Facebook Live.

CSCvh63085

Webex Events (Windows)

During events, when a presenter shares their screen, participants can see chat
         notifications that appear to the presenter

Resolved Bugs for Webex (44.9.0)

For open and resolved bugs in 44.9.0 see What's new for the latest channel of Webex Meetings -
        44.9 .

Resolved Bugs for Webex (44.7.0)

For open and resolved bugs in 44.7.0 see What's new for the latest channel of Webex Meetings -
        44.7 .

Resolved Bugs for Webex (44.6.0)

For open and resolved bugs in 44.6.0 see What's new for the latest channel of Webex Meetings -
        44.6 .

Resolved Bugs for Webex (44.4.0)

For open and resolved bugs in 44.4.0 see What's new for the latest channel of Webex Meetings -
        44.4 .

Resolved Bugs for Webex (44.2.0)

For open and resolved bugs in 44.2.0 see What's new for the latest channel of Webex Meetings -
        44.2 .

45.6.1 is the last slow channel version for Webex Meetings sites.

## June 45.6.x slow channel

Slow Channel version

Updates

45.6.1

Maintenance release

No new features or bug fixes

45.6.0

Maintenance release

No new features or bug fixes

## February 45.2.x slow channel

Slow Channel version

Updates

45.2.3

Maintenance release

No new features or bug fixes

45.2.2

Maintenance release

No new features or bug fixes

45.2.1

Maintenance release

No new features or bug fixes

## October 44.10.x slow channel

Slow Channel version

Updates

44.10.3

Maintenance release

No new features or bug fixes

44.10.2

Maintenance release

No new features or bug fixes

## June 44.6.x slow channel

Slow Channel version

Updates

44.6.2

Maintenance release

No new features or bug fixes

## February 44.2.x slow channel

Slow Channel version

Updates

44.2.2

Maintenance release

No new features or bug fixes

## Slow Channel

Slow Channel of Webex Meetings

### Slow Channel of Webex Meetings

Cisco Webex Meetings Slow Channel Policy

#### Webex Slow Channel Announcements

#### Version Retirement Policy

For a given Webex release, when a newer slow channel version of the desktop application is available,
            Cisco will announce the end-of-support date of the previously available slow channel
            version of the desktop application. The end-of-support date will be one month after the
            availability of a new slow channel version. The announced retirement date of a desktop
            application version will be four months after the availability the new version of the
            application. For example, if your Webex site is on Slow Channel release 40.6.6, and on October 31, 2020 the new Slow Channel
            release 40.10 becomes available, then the 40.6.6 version would reach end of support on
            November 30, 2020 and would be retired on February 28, 2021.

After the end-of-support date, Cisco will no longer deliver bug fixes or software maintenance on the previous version.

Customers must upgrade their site to use the new available version before
            the version’s retirement date. After the announced retirement date, Cisco will
            automatically update the customers’ site to the new version. This change will
            automatically deliver the new version of the desktop application to the users who
            connect to the Webex site. If IT administrators prevent users from getting the new version, then users can
            use Webex Web App to join or start meetings from browser.

The approved supported versions are as follows:

Approved slow channel Versions of Desktop Applications and Productivity Tools

Availability

End of Support

Retirement Date

45.6.1

August 27, 2025

45.2.1

April 9, 2025

September 28, 2025

January 11, 2026

44.10.2

December 11, 2024

May 9, 2025

August 24, 2025

#### Webex Slow Channel Policy

Webex Video Conferencing is a highly secure and scalable video conferencing service delivered through 
    Cisco Collaboration Cloud. Being a cloud service helps 
    Webex to deliver new features, enhancements, and fixes automatically without any intervention from customers. For special business needs, many of our customers can choose to stay on specific supported versions of 
    Webex desktop applications, preventing them from getting regular updates and enhancements.

Cisco is publishing this version retirement policy for 
    Webex release versions to serve customers by keeping an effective balance between the need for minimizing change but receiving important updates and enhancements.

#### Webex Meetings is a cloud service. Why is it not always the latest version?

Webex Meetings requires users to join or start meetings using a meeting application. Users can use
        mobile apps, desktop apps, the browser-based web app, Webex App, Cisco Jabber, or a video device to join meetings. Using the desktop app requires
        users or IT administrators to install the desktop app on users’ desktops.

Customers who want to minimize changes in their 
    Webex service can keep their desktop applications on a supported slow channel version of the 
    Webex desktop application and prevent automatic updates of this application. Customers must then schedule updates of the desktop application at a preferred time. This causes older versions of 
    Webex Meetings to exist on customer premises.

However, customers can’t keep Webex Meetingscloud components on a specific version. Customers will automatically receive updates
        including major or minor enhancements and bug fixes on Webex components delivered by the cloud, such as Webex pages, APIs, mobile applications, the web app, and Webex Site Administration.

The 
     Webex Meetings Slow Channel Policy establishes the update cadence for slow channel versions.

Open and Resolved Bugs

See the Open and Resolved Bugs for the Latest Webex Meetings Updates for info on the latest updates.

We report open and resolved customer-found bugs of severity 1 to 3. When an
                    update does not include customer-found bugs, there will not be a Resolved Bugs
                    list shown for that update.

You can find details about listed bugs and search for other bugs impacting specific
                    Webex Meetings updates by using the Cisco Bug
                    Search Tool . For more info on using the Bug Search, see Bug Search Tool Help .

Open Bugs for Webex Meetings

The bugs listed in the following table describe unexpected behavior in this release. Refer to Bug Search Tool for further details.

Bug Number

Affected Product Area

Description

CSCvh90269

The Make Screen blank feature doesn't work on Windows 10 devices if User Account Control is enabled.

CSCvi72293

Webex Meetings (Mac)

If a user's Facebook account is locked, they can't stream Webex meetings on Facebook Live.

CSCvh63085

Webex Events (Windows)

During events, when a presenter shares their screen, participants can see chat
         notifications that appear to the presenter

Resolved Bugs for Webex (44.2.2)

For open and resolved bugs in 44.2.2 see What's new for the slow channel of Webex Meetings -
        44.2.2 .

| Bug Number | Affected Product Area | Description |
|---|---|---|
| CSCvh90269 | Webex Meetings | The Make Screen blank feature doesn't work on Windows 10 devices if User Account Control is enabled. |
| CSCvi72293 | Webex Meetings (Mac) | If a user's Facebook account is locked, they can't stream Webex meetings on Facebook Live. |
| CSCvh63085 | Webex Events (Windows) | During events, when a presenter shares their screen, participants can see chat
         notifications that appear to the presenter |

| Slow Channel version | Updates |
|---|---|
| 45.6.1 | Maintenance release No new features or bug fixes |
| 45.6.0 | Maintenance release No new features or bug fixes |

| Slow Channel version | Updates |
|---|---|
| 45.2.3 | Maintenance release No new features or bug fixes |
| 45.2.2 | Maintenance release No new features or bug fixes |
| 45.2.1 | Maintenance release No new features or bug fixes |

| Slow Channel version | Updates |
|---|---|
| 44.10.3 | Maintenance release No new features or bug fixes |
| 44.10.2 | Maintenance release No new features or bug fixes |

| Slow Channel version | Updates |
|---|---|
| 44.6.2 | Maintenance release No new features or bug fixes |

| Slow Channel version | Updates |
|---|---|
| 44.2.2 | Maintenance release No new features or bug fixes |

| Approved slow channel Versions of Desktop Applications and Productivity Tools | Availability | End of Support | Retirement Date |
|---|---|---|---|
| 45.6.1 | August 27, 2025 |  |  |
| 45.2.1 | April 9, 2025 | September 28, 2025 | January 11, 2026 |
| 44.10.2 | December 11, 2024 | May 9, 2025 | August 24, 2025 |

| Bug Number | Affected Product Area | Description |
|---|---|---|
| CSCvh90269 | Webex Meetings | The Make Screen blank feature doesn't work on Windows 10 devices if User Account Control is enabled. |
| CSCvi72293 | Webex Meetings (Mac) | If a user's Facebook account is locked, they can't stream Webex meetings on Facebook Live. |
| CSCvh63085 | Webex Events (Windows) | During events, when a presenter shares their screen, participants can see chat
         notifications that appear to the presenter |

## Figuras

![Third party integration window for Webex meetings displaying settings options](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/436001-437000/436600.jpg)

![Phone receiver icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/440001-441000/440499.jpg)

![Security and privacy settings window on MAC OS](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/441001-442000/441371.jpg)

![Screen recording permision screen for Google Chrome on MAC OS](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/441001-442000/441372.jpg)

![web browser URL field with icon selected displaying "you have blocked autoplay media with sound for this website"](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/436001-437000/436480.jpg)