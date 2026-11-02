---
doc_id: help-webex-com-en-us-article-nffx8kj-deploy-the-webex-video-integration-for-microsoft-teams-efe166ca75
source_url: https://help.webex.com/en-us/article/nffx8kj/Deploy-the-Webex-video-integration-for-Microsoft-Teams
retrieved_at: 2026-11-02T13:03:54.569088+00:00
---

What's New with Webex Video Integration for Microsoft Teams

## Overview

Here's how the integration enhances the device user's experience when they join Microsoft Teams meetings hosted in your organization:

Webex meeting experience—multi-screen with flexible layout options

Participant list showing both Microsoft and video integration participants

Bi-directional content sharing between the device and Microsoft Teams

Meeting status indicators on the device, including recording,
          transcription, and participant waiting in lobby

### Deployment types and differences

Webex
      Video Integration for Microsoft Teams is available in two forms–as part of commercial Webex deployments, and as part of Webex for Government deployments. Webex for Government is a separate FedRAMP-authorized deployment of Webex for authorized US government entities and contractors.

The Webex for Government deployment of VIMT is offered only to Webex for Government customers. Each Webex environment automatically uses its corresponding Video Integration deployment when provisioning the Video Integration feature.

This guide covers both deployments combined, but there are particular changes and references that are specific to Webex for Government deployments that must be identified throughout the document.

- The SIP URI used to call into the service differs— m.webexgov.us for Webex for Government, m.webex.com for commercial.

- The Microsoft application name differs—for Webex for Government, it is Webex Video Integration for MS Teams (GCC) .

- The network ranges for Media with specialized media clusters are different. See Ports and protocols for video integration traffic section for details.

- There are cross-boundary calling impacts for both commercial Webex and Webex for Government. See Cross-boundary calling for more information.

### Video device join experience, from the meeting invitation

A standard email invitation to a Microsoft Teams meeting has meeting join details that include a clickable link to join the meeting from the Microsoft Teams client. The section may also include audio dial-in information with an audio conference ID and phone numbers to join as an audio-only participant. When you enable the video integration, the invitation join details section expands to include a block of video conferencing device join details.

When it is time to join the meeting, video device users can call the SIP video address "Tenant Key" under the Join on a video conferencing device section. The Tenant key calls the Webex interactive voice response (IVR) system, which asks the caller to provide the "Video ID". (This was previously called "VTC ID").

The Video ID is specifically for video devices and is different from the audio conference ID, if one is included for the meeting.

The SIP IVR video address is specific to your organization and is formed from your organization's Webex SIP subdomain in the format <subdomain>@m.webex.com .

Below the Video ID, the invitation links to a web page of "More info" dialing instructions,
      which shows how to join the meeting by dialing directly (in the following section).

### Alternative video device join method—direct dial

Video callers can join the meeting directly, bypassing the IVR, by using a SIP address in the format <VideoID>.<TenantKey>@m.webex.com . This method is listed at the top of the "More info" dialing instructions web page linked to in the invitation. The web page also repeats the IVR prompt join details from the meeting invitation.

### Alternative video device join method—Join button

If you also enable the Webex
       Hybrid Calendar Service, devices can receive One Button to Push (OBTP) when schedulers invite them to Microsoft Teams meetings. An attendee using the device then simply presses the Join button when it's time to connect the device to the meeting. The meeting's entry shows the Microsoft Teams logo to indicate the type of meeting the attendee is joining.

### Alternative video device join method—Microsoft Teams button

Cisco devices have a Microsoft Teams button to help users join Microsoft Teams meetings.

The Microsoft Teams button isn’t shown on the devices by default. To enable it directly on the device or in Control Hub, see Enable WebRTC and CVI to Join a Microsoft Teams Meeting from Board, Desk, and Room Series .

Device users can then join Microsoft Teams meetings by tapping the Microsoft Teams button and entering the video conference ID and address. See Join Microsoft Teams Meetings on Board, Desk, and Room Series .

You can make joining easier for users by setting the default CVI meeting address on the device with

```
xConfiguration UserInterface MeetingJoin CVITenants: address
```

See https://roomos.cisco.com/xapi/Configuration.UserInterface.MeetingJoin.CVITenants/ .

### Alternative video device join method—Cross-tenant join

Device users can join Microsoft Teams meetings hosted outside your company (in a different Microsoft Teams tenant) using VIMT's "cross-tenant join" feature, even if the meeting invite has no Video ID or Tenant key in the meeting invite.

Devices can use cross-tenant join using the OBTP Join button if Hybrid Calendar is configured, or by using the Teams button in RoomOS, then entering the meeting ID and passcode from the meeting invite.

When VIMT is deployed, cross-tenant join is automatically available on your devices that are Webex cloud-registered, or that use Webex Edge with JoinProtocol=Webex .

RoomOS SIP devices can optionally enable cross-tenant join. See Calendars and cross-organization invitations in this document.

## Requirements for Video Integration for Microsoft Teams

Requirement

Notes

An active Webex organization

If you do not yet have an active Webex organization, we will provision one for you when you purchase the video integration.

A Microsoft 365 tenant with Microsoft Teams accounts for users in the organization

The setup process requires an account that can sign in as a Global administrator for the tenant to grant application permissions, and a Microsoft Teams administrator account for the tenant that can execute PowerShell commands.

Webex video integration licenses, one for each of the video devices that you plan to use with this integration.

The subscription for this service must be provisioned to your Webex organization in Control Hub and set up as described in this article.

Cisco devices registered to your Webex organization, or other SIP video devices that can make internet calls.

Your network call control must allow business-to-business (B2B) calling to Webex, and meet the Webex certificate requirements. For help, see How Do I Allow Webex Meetings Traffic on My Network?

Video devices must have the signaling and media network access defined in Ports and protocols for video integration traffic .

Webex Hybrid Calendar Service (Optional, but highly recommended)

Required to provide One Button to Push (OBTP) to video devices.

For the best experience using  Hybrid Calendar, all meeting organizers and shared room mailboxes should be  Hybrid Calendar-enabled.

The  Hybrid Calendar Service has additional requirements. For instructions, see Deployment Guide for Hybrid Calendar .

### Microsoft tenant types

You can use a Microsoft GCC tenant with a commercial Webex organization, but if you need a FedRAMP-authorized version of the Video Integration, you must be using a Webex for Government organization linked to your Microsoft GCC tenant. Linking a Webex for Government organization to a worldwide Microsoft O365 tenant is not explicitly blocked, but is not supported as a FedRAMP-authorized offer.

### Ports and protocols for video integration traffic

#### Signaling

Video devices connect to the Webex data centers for signaling.

Video Device

Protocol

Port Number(s)

Cisco device registered to your organization

TCP

443

For requirements, see Network requirements for Webex services or Network requirements for Webex for Government .

Other SIP video device

TCP

5060/5061

#### Media

The media path for video integration calls differs from other Webex Meetings call flows, because specialized media clusters hosted by Azure handle this call type.

These specialized media clusters aren’t part of the standard Webex Meetings address
          ranges. You must ensure that traffic can reach these additional IP networks.

Failure to open access to any of the media cluster IP ranges can lead to call failures. The integration attempts to use the optimal media cluster for each call based on where the caller originates. However, you must allow access to all media clusters because the media cluster used can vary based on run-time conditions.

Video device

Protocol

Port number(s)

Media cluster regions and IP ranges

Cisco device registered to your organization

TCP

443

5004

We only use these TCP ports as a fall back option for the preferred (UDP) media ports

Australia East:

20.53.87.0/24

Southeast Asia:

40.119.234.0/24

4.144.190.0/24

US East 2:

52.232.210.0/24

20.57.87.0/24

4.152.214.0/24

4.152.180.0/24

US West 2:

48.202.19.0/24

172.194.164.0/24

20.120.238.0/23

UK South:

20.68.154.0/24

20.108.99.0/24

4.158.208.0/24

West Europe:

20.50.235.0/24

20.76.127.0/24

4.175.120.0/24

Webex for Government:

48.200.105.0/24*

48.221.124.0/24*

UDP

5004 (Devices & Webex clients)

9000 (Webex clients)

Other SIP video device

UDP

36000-59999

* These IP ranges are used exclusively for calls to meetings created using the Webex for Government version of the Video Integration.

Network requirements for SIP calls follow the network requirements of the deployment type used by the meeting organizer (Commercial or Webex for Government).

See the following network requirements documents for other Webex services, including device registration and more:

- Network requirements for Webex services

- Network requirements for Webex for Government

## Create the video integration from Control Hub

Follow these steps to register Microsoft Teams to the Webex cloud, authorize service permissions with Microsoft, and enable Cisco video devices to join Microsoft Teams meetings. The setup wizard in Control Hub guides you through the process.

The Microsoft user has to authenticate at least two separate times during the setup. We recommend that the steps be done by a Microsoft administrator whose account has been given full administrator access to Control Hub.

Before you begin

Make sure that you've met all of the Requirements for Video Integration with
              Microsoft Teams (in this
            document).

If you haven't already done so, set up your Webex organization .

If you haven't already done so, add a subdomain for Webex SIP addresses in your organization.

You need the following administrator access:

Microsoft Tenant Global Administrator privileges in your organization

Microsoft Teams administration privileges within the tenant

Full administrator privileges for your own Webex organization, and a web browser that can access Control Hub. (See System requirements for Webex services for browser compatibility.)

Users from any other organization that may have access to your Control Hub (such as Partner Admins) do not qualify. Use a full administrator account in the Webex organization that you are configuring.

You also need access to run Microsoft PowerShell commands.

Latest Microsoft Teams PowerShell module installed. See Install Microsoft Teams PowerShell Module for more information.

At the time of this writing, Microsoft recommends PowerShell version 5.1 or higher when using the Microsoft Teams module, so we recommend using PowerShell on a Windows machine. See PowerShell 5.1 system requirements for more information.

Sign in to Control Hub .

Go to Organization Settings > SIP Address for Cisco Webex Calling to check if you've set the subdomain for Webex SIP addresses. If the subdomain is not set, see Change your Webex SIP address .

Go to Services > Hybrid . On the Video Integration card for Microsoft Teams, click Set Up .

If the card doesn't show the Set Up option, make sure that your license is active.

On the Video Integration Setup screen, click Authorize .

You’re redirected to a Microsoft sign-in window.

Sign in with a Global Administrator account.

The application asks you to consent to the permissions it needs to check your role in the Microsoft tenant and get details of the tenant.

For Webex for Government deployments, the app includes (GCC) in the name.

Review the requested permissions and click Accept . You don’t
          need to check Consent on behalf of your organization , as it’s not
          required.

The application checks your authorization to continue the setup. If you're
            authorized, you're redirected to another Microsoft consent request for permissions. You
            may be prompted to sign in again. If so, use your Global Administrator
            account.

Review the requested permissions, then click Accept to grant the Webex Video Integration application the required permissions.

Open a PowerShell window on your computer, and install the Microsoft Teams PowerShell module if it's not already installed:

At the PowerShell command prompt, type the following command:

```
Install-Module MicrosoftTeams -AllowClobber
```

If you are prompted to trust the PSGallery repo, acknowledge with Y to trust, and proceed with the download and installation.

Import the Microsoft Teams module and connect to your Teams tenant:

Use the existing window or open a new PowerShell window on your computer.

At the PowerShell prompt, type the following command:

```
Import-Module MicrosoftTeams
```

At the PowerShell prompt, type the following command:

```
Connect-MicrosoftTeams
```

A Microsoft sign-in page appears.

Enter the credentials for the user with Microsoft Teams administration privileges for the tenant.

If successful, you get feedback on which account and tenant you successfully signed into. If you get an error, repeat the command and refer to the Microsoft PowerShell documentation for additional assistance.

You must successfully sign in to your Teams tenant before proceeding to the remaining steps.

From the Video Integration Setup screen in Control Hub, click to copy the text of the New-CsVideoInteropServiceProvider command from the first text box and paste it into the PowerShell session. Then run the command.

This command is specific to your tenant. The command will not work unless you have imported the Microsoft Teams PowerShell module and successfully signed in to your tenant as described in the previous step.

Take special care when copying the command to PowerShell, so that the copied text is not modified in any way when handling the text. Sending the command through email, messaging clients, or other handling may result in added formatting, character substitutions, or additional characters, which will break the configuration. PowerShell will not necessarily reject the malformed text. We recommend you directly copy and paste the command from Control Hub to PowerShell when possible, or verify the text using a plain text editor before pasting to PowerShell.

- The tenantKey assigned by Webex

- The Exchange invite Alternate Instructions URL provided by Webex

Choose how you want to enable the integration for your users.

For help, see Grant-CsTeamsVideoInteropServicePolicy .

To enable the integration for all users in your organization, copy the text of the Grant-CsTeamsVideoInteropServicePolicy command from the second text box.

```
Grant-CsTeamsVideoInteropServicePolicy -PolicyName CiscoServiceProviderEnabled -Global
```

To enable the integration for an individual user, copy the text of the Grant-CsTeamsVideoInteropServicePolicy command from the second text box. Replace -Global with -Identity , and add the user's email address after it.

```
Grant-CsTeamsVideoInteropServicePolicy -PolicyName CiscoServiceProviderEnabled -Identity jamie.smith@company.com
```

Paste the command into your PowerShell session and run it.

When you are done with the PowerShell commands, click Ok on the Video Integration Setup screen in Control Hub to complete the setup.

The PowerShell changes to the Microsoft tenant can take time to propagate in the Microsoft
        365 environment. Microsoft warns this can take up to 72 hours, although it typically takes
        less than two hours.

You can test if the changes for a user have become active by having the user create test meetings in Microsoft Outlook or Microsoft Teams. If the changes have successfully propagated, you should see the video integration join details in the meeting invitation. If the join details are not present, wait longer and repeat the test again.

What to do next

- In the Control Hub left navigation menu, under Services , select Hybrid .

- Find the Video Integration for Microsoft Teams card, and click Edit settings .

To take full advantage of the calendar and OBTP Join features of the  Hybrid Calendar Service, make sure your Cisco devices are either registered to the Webex cloud or linked to the cloud using Edge for devices .

Set up the  Hybrid Calendar Service if you want OBTP for devices. See Make it easier for video devices to join meetings with OBTP .

## Join button and Hybrid Calendar considerations

As mentioned in Alternative video device join method—Join button , if you enable the  Hybrid Calendar Service, you can further enhance the calling experience for your organization using One Button to Push (OBTP).

With OBTP, Cisco devices in your organization automatically show a Join button shortly before the Microsoft Teams meeting starts, when they're included in the meeting:

Personal mode devices show the button if the user associated with the device accepts the meeting invitation. (The user must be enabled for the calendar service in Control Hub.)

Shared mode devices show the button if the room mailbox email address associated with the device accepts the meeting invitation. (The device's workspace must be enabled for the calendar service in Control Hub.)

### Exchange mailbox requirements for OBTP

The  Hybrid Calendar Service will only process a meeting invitation (to add the details needed for OBTP) if the meeting scheduler or at least one of the invitees has the service enabled. If your organization doesn't have many calendar service-enabled users, it may be common for a device invitation to trigger the processing, rather than the scheduler or a user. When this happens, it's critical that your Exchange configuration retain all of the details that the service needs in the invitation.

You can enable users without Webex licenses for the  Hybrid Calendar Service.

By default, the Exchange Online settings delete the meeting details from invitations sent to room mailboxes. Apply the following PowerShell commands to the room mailboxes of all shared mode devices that you enable for the  Hybrid Calendar Service, so that the body of the meeting invitation is preserved. This is needed by VIMT.

```
Set-CalendarProcessing -identity "room" -DeleteComments $false
```

These two additional commands are optional and recommended:

```
Set-CalendarProcessing -identity "room" -DeleteSubject $false
```

```
Set-CalendarProcessing -identity "room" -AddOrganizerToSubject $false
```

If you want to be able to forward invitations scheduled from outside of your Microsoft organization to the device, add the following command:

```
Set-CalendarProcessing -identity "room" -ProcessExternalMeetingMessages $True
```

### URL rewriting and OBTP

You may be using the Safe Links feature from Microsoft Defender for Office 365 (or similar
      security software) to rewrite URLs in email to protect users from malicious links.

This software interferes with OBTP, so you need to configure exceptions for Microsoft Teams meeting invitations that include Webex URLs.

Specifically, you must configure your security software to not rewrite the "More info" instruction hyperlink. Otherwise, the Cisco
       Hybrid Calendar Service fails to create the Join button for those meetings.

For Microsoft Defender, you can add the URL pattern to the Do not rewrite the
        following URLs portion of your Safe Links policy.

For more information about Microsoft Defender’s Safe Links policies and configuration, see Set up Safe Links policies in Microsoft Defender for Office 365 .

### Supported device types for OBTP

The following devices and clients support OBTP for Microsoft Teams meetings using the video integration and the  Hybrid Calendar Service:

Cisco Board, Room, and Desk devices

Cisco Room Kit and Room Phone

Cisco MX, SX, and DX series

The devices must be either registered to the Webex cloud or linked to the cloud using Edge for devices .

If your devices are getting the Join button from Cisco TMS or Cisco TMSXE, they cannot get the Join button for Microsoft Teams meetings.

As an alternative, you can simplify joining for the affected devices by adding the SIP IVR video address of the Microsoft Teams meeting as a speed dial or macro.

## Features and limitations

This section explains limitations and feature behavior for the Video Integration for Microsoft Teams.

### Relationship between organizations and tenants

We currently support a 1:1 relationship between Webex organizations and Microsoft 365 tenants:

A single Webex organization can interoperate with only one Microsoft 365 tenant.

Your Microsoft tenant can support multiple different video integrations; for example, the tenant can simultaneously interoperate with Cisco and Pexip. However, the tenant can only have one integration of each type; so, one from Cisco, and one from Pexip.

If you have multiple Webex organizations, choose one to interoperate with your Microsoft tenant using the Webex video integration.

### Availability

We only support the Worldwide and GCC instances of Microsoft 365. Other instances which we do not support include USGovDoD, USGovGCCHigh, China, and Germany.

We do not recommend linking between a Commercial Webex organization and a GCC Microsoft tenant (or vise versa). Only the Webex for Government version of VIMT is FedRAMP-authorized for Webex for Government.

We only support Webex for Government and paid Webex organizations in countries and regions where Webex paid subscriptions are available .

### Video interoperability

The integration supports Cisco devices as follows:

- Registered to Webex

- Registered on-premises and using Webex Edge for Devices

- Registered on-premises making SIP calls

The integration also supports third-party devices making SIP calls.

The video quality of VIMT participants, as seen by other participants, can be impacted when Teams clients with limited bandwidth or impaired connectivity are present. Both the likelihood and severity of this issue increase with meeting size.

We recommend using Microsoft town hall meetings instead of Teams meetings when presenting from a small group of presenters to a large audience — for example, 50 or more participants.

VIMT can be used to join Microsoft Teams Meetings and Microsoft live events or town halls as a presenter. See Webex Video Integration for Microsoft Teams live events and Webex Video Integration for Microsoft town halls .

You can't cross-tenant join to Teams
          live events or town halls in other Microsoft tenants.

The integration does not support H.323 or IP address dialing.

You can interwork these legacy protocols to SIP calls using a Cisco Expressway deployment.

- For interoperability with other Cisco and third-party equipment, see Webex video compatibility and support .

You can use One Button to Push (OBTP) from Webex App to join a paired device to a Microsoft Teams meeting.

(No cross-tenant join from Webex App.)

You can't join a Microsoft Teams meeting using only Webex App.

The integration only supports devices paired with Webex App for OBTP, or wireless share, to join a Teams meeting on the video device. Other device pairing features, including dialing from Webex App, and device controls from Webex App, are not available.

Interactive whiteboarding from Cisco devices is not available for meetings on Microsoft Teams. Users can share whiteboards from the device as video content (BFCP support).

The integration doesn’t support audio-only devices such as IP phones or PSTN phones.

Audio-only devices should call in using the Microsoft Teams PSTN gateway functionality.

IP phones, like the Cisco Video Phone 8875, can use this solution.

- Webex Video Integration for Microsoft Teams meetings are not supported on devices setup in companion mode.

### Layouts

#### Layouts on single screen devices

Participants using a single participant screen, including Cisco devices and third-party devices, see the Grid layout by default.

Single screen participants can use layout controls to change the layout between the following:

- Grid (default)

- Prominent

- Focus

- Stack

- Overlay

- Teams Large Gallery

During content sharing, single screen devices see the Stack layout by default.

Cisco devices that are Webex-registered, Webex Edge using the Webex join protocol, or calling SIP with ActiveControl enabled will have individual panels for each participant stream in the Stack layout, while other device types will only see a single participant panel.

#### Layouts on dual screen devices

Dual screen layouts are used for Cisco devices that have two participant screens and are Webex-registered, Webex Edge using Webex for join protocol, or calling SIP with ActiveControl enabled.

Dual screen participants see the Grid layout on each screen by default.

Dual screen participants can use layout controls to change the layout between the following:

Prominent –Focused/Active speaker on primary screen, Grid layout (3x3) on second screen.

Focus –Active speaker full screen on each screen, voice switched.

Grid layout (Default)–Dual people screen, 2x2 max on each screen.

Large Gallery –Microsoft Teams Large Gallery layout on second screen (up to 7x7), Focused/active speaker on first screen.

The Overlay and Stack layouts are not available when two participant screens are active.

Content on dual screen devices will be shown on a dedicated third screen if it has one. Otherwise, the content replaces the layout on one of the two screens, and you can use layout controls to change the layout on the other screen.

#### Microsoft Teams Large Gallery layout

When participants use layout controls to select the Large Gallery layout, they see the Microsoft Teams Large Gallery composite view. This layout shows up to 49 remote participants in a 7x7 grid.

#### Spotlight

Teams hosts and presenters via Teams clients can mark up to seven meeting participant(s) to be spotlighted, which forces that participant to be visible in all participant’s layouts. For VIMT participants, spotlighted participants will be prioritized in your currently selected layout and will have a spotlight icon after their name in the layout. Spotlighted participants are not assigned to fixed locations in the layout, but rather they get the highest priority positions in the layout, and other non-spotlighted participants fill in the rest of the screen, if room allows.

#### Layout controls

VIMT participants can use a device’s local meeting controls or DTMF tones to change the layout they are viewing.

Controlling your layout via a device’s meeting controls is available for Cisco devices that meet any of the following requirements:

- Are registered to Webex.

- Using Webex Edge for Devices with Webex as the join protocol.

- CE and Room OS devices registered on-premises to CUCM or Expressway, and using SIP with ActiveControl (iX protocol enabled).

All other video integration participants can cycle through layout options by sending DTMF tones 2 and 8 from the device. Icons to assist will be shown in the video image when using DTMF to cycle through layout choices. DTMF controls for layouts are available to all devices that can send in-band DTMF tones.

#### Change the VIMT default layout for your meetings

You can customize the default layout used for callers to your VIMT deployment. To set the default layouts for your organization:

- Sign in to Control Hub .

- Go to Services > Hybrid , then click the Video Integration for Microsoft Teams card.

- Click Edit Settings , then click the table row for the Tenant to edit.

- Edit the choices in the dropdown list for single and/or dual screen devices, then click Save .

#### General layout features and limitations

Participants can see up to nine video streams at the same time (as counted across all people screens), unless they are using the Large Gallery layout.

The number of visible streams depends on the selected layout and the device type.

All participants beyond that limit are shown with Webex-generated name labels instead of a video stream of the remote participant.

The Grid layout is limited to a maximum of 3x3 panels for a single screen participant, and 2x2 when showing two participant screens. This is in order to maximize the video size of each participant by preventing the grid from expanding beyond the limit of nine visible participants.

If a VIMT participant is not sending video (for example, camera off), then Webex substitutes a white name label on a black background for that participant’s video stream. This is what's seen by other meeting participants.

That participant is treated as a video participant by Microsoft Teams (not an audio-only participant in Teams clients), and will not display in layouts like an audio-only participant.

Cisco devices using three people screen configurations, with dedicated content screens, automatically use the Overlay layout on all people screens.

Room switching and Panoramic experience features are not supported.

- Spotlighting does not force a VIMT participant’s layout to change. If the number of spotlighted participants exceeds the number of video windows in the VIMT participant’s current layout, a spotlighted participant may be off-screen. If a spotlighted participant is off-screen and becomes the main speaker, it will automatically swap into the active layout, displacing a inactive speaker.

Microsoft Teams Large Gallery limitations

- The Gallery view shows all video-enabled participants, including yourself and the active speaker. You may see duplicate streams.

- There is no option to view a second page of the Gallery view for VIMT participants. When a participant who is not shown in the grid becomes the active speaker, they will be switched into the current grid view.

- Teams client meeting participants with their cameras off are not shown in Large Gallery layout.

- Other VIMT participants with their cameras off are seen in the grid with the Webex-generated white text avatar for their video image.

### Calendars and cross-organization invitations

Participants from outside your organization can join your Microsoft Teams meetings from their video devices by dialing your IVR video address ( <yoursubdomain>@m.webex.com ) and entering the Video meeting ID for the meeting at the prompt, or by using your direct dial alternative ( <VideoMeetingID>.<yoursubdomain>@m.webex.com ).

This video integration allows joining meetings hosted by other Microsoft tenants if the invite has CVI join details, or if not, using cross-tenant join.

To join a Teams meeting that is hosted by a different Microsoft tenant with a Video ID, you can:

Use the video address of the CVI video integration that is enabled for that tenant.

If you are using OBTP, tap Join . Otherwise, you can manually dial the SIP address in the meeting invite.

Alternatively, if no Video ID is shown in the invite, use the RoomOS Teams button (or custom macro) to join by providing the Teams Meeting ID and passcode from the invite.

See Enable
                WebRTC and CVI to Join a Microsoft Teams Meeting from Board, Desk, and Room
                Series .

RoomOS devices using SIP (including Edge with JoinProtocol=SIP ) can optionally enable the cross-tenant join feature as follows:

Set xConfiguration MicrosoftTeams Cvi CrossTenant: Enabled. (Default is Auto)

Auto=Enabled is configured for Cloud-registered devices and VIMT.

Auto=Disabled is configured for on-prem SIP-registered devices.

RoomOS SIP devices also need to set VIMT per customers TenantKey (on the left side of @m.webex.com):

Set xConfiguration UserInterface MeetingJoin CVITenants:<example>

Issues arising from missing comments/body details or organizer-based processing also apply when processing OBTP for Microsoft Teams meetings.

RoomOS uses meeting ID and passcode from the Teams meeting invite to prepare the Join button for cross-tenant meetings. If these details are not present, or difficult to parse from the invite, then the Join button may not work as expected. In this case, OBTP with direct guest join using WebRTC will be used.

See Known
            Issues with Hybrid Calendar Service .

### Meeting features

#### Joining

Cisco devices connecting through the video integration have the Webex IVR and splash screens localized to the language set in the device. US English is the default for all other scenarios. Localization is supported for Cisco devices using cloud calling or SIP calling (requires CE9.14.3 or newer.)

#### Recording

Video integration participants don't have controls to start or stop meeting recordings. Microsoft Teams users must manage meeting recording.

#### Sharing

- Up to 1080p 30fps is supported.

- Other participants will see the content as a Share screen session.

- Video integration participants can see and hear content from other participants who use the Share screen , Share window , Content from camera , or Powerpoint Live features. Up to 1080p 30fps is supported. Other forms of content, such as Excel Live and Whiteboard , are not supported and will not be seen by video integration participants.

- Presenter mode features, such as Standout , Side by Side , and Reporter , are not seen by video integration participants. If used, the content and presenter will be seen separately—the same as if the Presenter mode feature was not used.

- The video integration does not support the Take Control feature with other participants during sharing.

If meeting policies or a meeting organizer limits who can share content in a Teams meeting using the Who Can Present? meeting option, then video integration participants must have the Presenter role to share content in the meeting. When joining through the video integration, a caller is an attendee by default. Callers who join as trusted callers will have the Presenter role assigned automatically, regardless of the value set in Who Can Present? Meeting organizers can toggle a participant's role as needed using the participant list in their Teams client.

If meeting policies or a meeting organizer limits who can share content in the Teams meeting using the Who Can Present? meeting option, sharing content will not work as expected for video integration participants who only have the attendee role in the meeting. The caller will be able to start sharing on their device, but their content will not be seen by other participants in the meeting. Sharing may also interfere with receiving content from another user.

#### PowerPoint Live support

When a meeting participant shares content using PowerPoint Live, video integration participants will see the shared slides as static images in their content channel. The slides automatically update as the presenter changes slides. Slide changes may take several seconds to update.

Because the VIMT participant sees the slide as static content, some features that Teams clients offer are not available:

- No Private View—You cannot advance or switch between slides on your own. The VIMT participant will always see the presenter's current slide.

- No Animations—The static slide shows all animated elements as visible and static. Slides that have elements that appear or disappear will all appear at the same time and may overlap or clash.

- No embedded video or audio playback—Embedded videos will appear as a static preview image without playback or audio.

- No Annotations—Annotations added by a presenter are not seen by the VIMT participant.

- Cameo mode—VIMT will see the placeholder for cameo video in a slide, but the presenter video will not be shown in the slide. The presenter's video will stay in the people monitor layout.

- No Magnified View—VIMT participants cannot change the zoom level of the content seen.

- No High Contrast View—This feature is not available.

- No Translations—This feature is not available.

#### On-screen notifications

We show notifications to video integration participants when:

Recording starts or stops. A recording icon stays on screen while recording is active. Devices with Webex cloud registration or ActiveControl get localized text and locally rendered icons.

A Teams participant raises their hand. The notification includes their screen name and the hand icon. The participant list also shows the raised hand icon.

VIMT participants can’t raise their hands, or lower the hands of others.

Participants are waiting in the Teams meeting lobby (a Teams client participant must admit them).

Transcription starts or stops in the meeting. A transcription icon stays on the screen while transcription is active.

#### In-meeting chat

Microsoft Teams chat isn't available to video integration participants.

#### Whiteboarding

Microsoft Teams whiteboarding isn't available to video integration participants.

Interactive white boarding from Cisco devices is not available for meetings on Microsoft Teams. Users can share whiteboards from the device as video content (BFCP support).

#### Mute controls and indicators

There are two types of mutes for VIMT participants that users must be aware of:

- The device's local mute feature.

- The Teams mute status—the server side mute state for the participant in the Teams meeting.

Devices have audio from microphones' sources, as well as potentially having audio from content sharing sources. For Cisco devices, the local mute feature has a light indicator and blocks the local microphones from transmitting, but does not block content audio when sharing content.

A Teams mute blocks all audio from the participant to the meeting. The mute indicator seen in the Teams participant list always reflects the Teams mute status of the participant, but this does not necessarily match the local device’s mute state.

How these two types of mutes interact in a VIMT call, and the status seen by users, differs depending on the device and type of call placed.

Calls by cloud-optimized/cloud-registered devices

When not sharing content, the device's local mute and Teams mute status are kept synchronized. The device’s local mute lights follow the device’s local mute status. Muting and unmuting locally will update the Teams mute state and the icons seen in the Teams participant list. If you are muted by another Teams participant, your local mute will also be enabled and light up. Due to privacy restrictions, you cannot be unmuted by a remote participant.

When sharing content, enabling the device's local mute will not turn on the Teams mute. This allows you to mute your local microphones, while still having your content's audio heard in the meeting.

Because the Teams mute is not enabled, the Teams participant list will not show you as muted.

If you are muted in the meeting by another Teams participant, both content audio and local microphones will be blocked from the meeting and your local mute indicator will turn on and display. You can unmute yourself using your device's unmute feature, and this will clear both the Teams mute and the local microphone mute.

DTMF mute commands for cloud-optimized/cloud-registered devices

For cloud-optimized/cloud-registered devices, you should always use the device's local mute feature and avoid use of DTMF commands for mute.

- When not sharing content, DTMF *6 can only be used to enable the Teams mute. When not sharing content, DTMF *6 will not toggle the Teams mute off.

- When sharing content, DTMF *6 will toggle the Teams mute on and off, but will not unmute the device's local mute status or indicator.

SIP Calls with ActiveControl

For SIP calls with ActiveControl (iX protocol) negotiated, the local and Teams mutes behave the same as on cloud-optimized/cloud-registered devices as described above.

DTMF mute commands for SIP with ActiveControl

For SIP Calls with ActiveControl, use the device's local mute feature. Do not use DTMF commands to mute and unmute.

- When not sharing content, DTMF *6 can only be used for Teams mute. DTMF *6 will not toggle the Teams mute off when not sharing content.

- When sharing content, DTMF *6 will toggle the Teams mute on and off, but will not unmute the device's local mute status or indicator. You may also see a You are being asked to unmute prompt on-screen when a Teams mute is cleared.

SIP calls without ActiveControl

When using SIP calls without ActiveControl, the device’s local mute feature and the Teams mute are not synchronized.

When a device locally mutes or unmutes, it is not seen in the Teams participant list.

If sharing content from a Cisco device, the device’s local mute will block microphones, but not the content audio. Third-party device behavior may differ.

If the participant is muted by another Teams participant using the participant list, all audio from the participant will be blocked in the meeting, but the device’s local mute feature is not toggled on. Due to privacy restrictions, you cannot be unmuted by a remote participant—the participant must clear the Teams mute themselves using DTMF commands. Webex provides on-screen message prompts to let the participant know if the Teams mute has been toggled on or off, and instructs them to use the DTMF *6 command to unmute.

DTMF mute commands for SIP without ActiveControl

SIP participants without ActiveControl can use the DTMF sequence *6 to toggle their Teams mute on or off for their call. On-screen text prompts indicate You have been muted or You have been requested to unmute when the Teams mute is enabled or cleared.

The following table summarizes VIMT mute behavior depending on the call type, when sharing content, and when not sharing content.

Local mute only mutes microphones; content audio is still sent to meeting.

If a participant has muted themselves locally, they are not shown as muted in the Teams roster.

Muting in the Teams roster blocks all audio and turns on local mute and indicators.

Local mute only mutes microphones; content audio is still sent to meeting.

If a participant has muted themselves locally, they are not shown as muted in the Teams roster.

Muting in the Teams roster blocks all audio and turns on local mute and indicators.

- Mute lights/indicators on Cisco devices follow the device’s local mute state.

- When sharing content on Cisco devices, content audio is still played to the meeting, even if the local mute is enabled and the light/indicators are on.

### Cross-boundary calling warnings

- You cannot use the Video ID from another customer's invites in your own VIMT gateway. When receiving an invite for a meeting outside your own organziation that has CVI defails included, you must use the Video ID and Video Address specified in the invite. If you enter the Meeting ID and password, the join will be made as a Cross-Tenant Join using your own VIMT gateway.

- Hybrid Calendar will always use the CVI provider included in the meeting invite for One Button to Push (OBTP) joins. If you get an invite from another organization that includes CVI join details, OBTP join dials the host's CVI gateway, not your own.

- When devices using the Webex protocol call a third-party CVI address or VIMT domain for a Webex Cloud other than the Webex Cloud where the device is registered, the call will exit that Webex Cloud as a SIP call without ActiveControl. This call path reduces the VIMT-supported features for the call to the level of a SIP call rather than a direct Webex call.

- Example 1: A commercial Webex-registered device with Hybrid Calendar enabled receives an invite from another company that has Pexip CVI join instructions in the invite. Joining via OBTP will result in a SIP call from Webex to the Pexip CVI gateway. The call will not have the normal VIMT in meeting controls or features.

- Example 2: A commercial Webex-registered device receives a Teams invite from a Webex for Government user that includes the VIMT address m.webex.gov.us . When the commercial Webex device calls the m.webexgov.us address, it will use a SIP call without ActiveControl between the two Webex clouds. The call will not have the normal VIMT in meeting controls or features.

### Microsoft Teams lobby

Trusted devices from your own organization can streamline how they join meetings by automatically bypassing the Microsoft Teams lobby. A device is considered trusted in either of the following cases:

It is a Cisco device registered to the Webex organization where VIMT is deployed using cloud calling, or Webex Edge using the Webex join protocol.

It is a device using on-prem SIP calling, which uses SIP TLS and presents a
              certificate that has a Subject Alternate Name matching one of your verified SIP
                domains .

If you enable TLS verification on your SIP calling to Webex, your TLS verification should check for the Subject Alternate Name (SAN) sip.webex.com (not m.webex.com).

If a meeting organizer sets the Who can bypass the lobby? meeting option to People who were invited or Only organizers and co-organizers , callers attempting to join as trusted callers will be placed into the lobby of the Teams meeting. The caller will see the Waiting for others to join splash screen instead of the expected lobby splash screen.

If you disable Anonymous users can join a meeting in the Microsoft Teams tenant settings, then video integration participants cannot join through the lobby. Video integration participants who would normally bypass the lobby will still be able to join Microsoft Teams meetings.

Cross-tenant join requires the device to be trusted and does not offer lobby bypass into another Teams tenant. The Teams meeting host(s) must admit those devices from the lobby.

### Networking

Calls to the video integration do not use Webex Video Mesh nodes; traffic is direct from the device to the cloud.

The specialized media clusters used by the video integration for Microsoft Teams are not part of the reachability tests that Webex-registered devices perform. Failure to open access to any of the media cluster IP ranges can lead to call failures. The integration attempts to use the optimal media cluster for each call based on where the caller originates. However, you must allow access to all media clusters because the media cluster used can vary based on run-time conditions.

| Requirement | Notes |
|---|---|
| An active Webex organization | If you do not yet have an active Webex organization, we will provision one for you when you purchase the video integration. |
| A Microsoft 365 tenant with Microsoft Teams accounts for users in the organization | The setup process requires an account that can sign in as a Global administrator for the tenant to grant application permissions, and a Microsoft Teams administrator account for the tenant that can execute PowerShell commands. |
| Webex video integration licenses, one for each of the video devices that you plan to use with this integration. | The subscription for this service must be provisioned to your Webex organization in Control Hub and set up as described in this article. |
| Cisco devices registered to your Webex organization, or other SIP video devices that can make internet calls. | Your network call control must allow business-to-business (B2B) calling to Webex, and meet the Webex certificate requirements. For help, see How Do I Allow Webex Meetings Traffic on My Network? Video devices must have the signaling and media network access defined in Ports and protocols for video integration traffic . |
| Webex Hybrid Calendar Service (Optional, but highly recommended) | Required to provide One Button to Push (OBTP) to video devices. For the best experience using  Hybrid Calendar, all meeting organizers and shared room mailboxes should be  Hybrid Calendar-enabled. The  Hybrid Calendar Service has additional requirements. For instructions, see Deployment Guide for Hybrid Calendar . |

| Video Device | Protocol | Port Number(s) | Comments |
|---|---|---|---|
| Cisco device registered to your organization | TCP | 443 | For requirements, see Network requirements for Webex services or Network requirements for Webex for Government . |
| Other SIP video device | TCP | 5060/5061 | For requirements, see How do I allow Webex Meetings traffic on my network? |

| Video device | Protocol | Port number(s) | Media cluster regions and IP ranges |
|---|---|---|---|
| Cisco device registered to your organization | TCP | 443 5004 We only use these TCP ports as a fall back option for the preferred (UDP) media ports | Australia East: 20.53.87.0/24 Southeast Asia: 40.119.234.0/24 4.144.190.0/24 US East 2: 52.232.210.0/24 20.57.87.0/24 4.152.214.0/24 4.152.180.0/24 US West 2: 48.202.19.0/24 172.194.164.0/24 20.120.238.0/23 UK South: 20.68.154.0/24 20.108.99.0/24 4.158.208.0/24 West Europe: 20.50.235.0/24 20.76.127.0/24 4.175.120.0/24 Webex for Government: 48.200.105.0/24* 48.221.124.0/24* |
| UDP | 5004 (Devices & Webex clients) 9000 (Webex clients) |
| Other SIP video device | UDP | 36000-59999 |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Organization Settings > SIP Address for Cisco Webex Calling to check if you've set the subdomain for Webex SIP addresses. If the subdomain is not set, see Change your Webex SIP address . |
| 3 | Go to Services > Hybrid . On the Video Integration card for Microsoft Teams, click Set Up . If the card doesn't show the Set Up option, make sure that your license is active. |
| 4 | On the Video Integration Setup screen, click Authorize . You’re redirected to a Microsoft sign-in window. |
| 5 | Sign in with a Global Administrator account. The application asks you to consent to the permissions it needs to check your role in the Microsoft tenant and get details of the tenant. For Webex for Government deployments, the app includes (GCC) in the name. |
| 6 | Review the requested permissions and click Accept . You don’t
          need to check Consent on behalf of your organization , as it’s not
          required. The application checks your authorization to continue the setup. If you're
            authorized, you're redirected to another Microsoft consent request for permissions. You
            may be prompted to sign in again. If so, use your Global Administrator
            account. |
| 7 | Review the requested permissions, then click Accept to grant the Webex Video Integration application the required permissions. The browser should redirect you to the Control Hub Video Integration Setup screen when you've finished the authorization steps. If not, note the error message, correct the concerns, and restart the setup process. |
| 8 | Open a PowerShell window on your computer, and install the Microsoft Teams PowerShell module if it's not already installed: At the PowerShell command prompt, type the following command: Install-Module MicrosoftTeams -AllowClobber If you are prompted to trust the PSGallery repo, acknowledge with Y to trust, and proceed with the download and installation. |
| 9 | Import the Microsoft Teams module and connect to your Teams tenant: Use the existing window or open a new PowerShell window on your computer. At the PowerShell prompt, type the following command: Import-Module MicrosoftTeams At the PowerShell prompt, type the following command: Connect-MicrosoftTeams A Microsoft sign-in page appears. Enter the credentials for the user with Microsoft Teams administration privileges for the tenant. If successful, you get feedback on which account and tenant you successfully signed into. If you get an error, repeat the command and refer to the Microsoft PowerShell documentation for additional assistance. You must successfully sign in to your Teams tenant before proceeding to the remaining steps. |
| 10 | From the Video Integration Setup screen in Control Hub, click to copy the text of the New-CsVideoInteropServiceProvider command from the first text box and paste it into the PowerShell session. Then run the command. This command is specific to your tenant. The command will not work unless you have imported the Microsoft Teams PowerShell module and successfully signed in to your tenant as described in the previous step. Take special care when copying the command to PowerShell, so that the copied text is not modified in any way when handling the text. Sending the command through email, messaging clients, or other handling may result in added formatting, character substitutions, or additional characters, which will break the configuration. PowerShell will not necessarily reject the malformed text. We recommend you directly copy and paste the command from Control Hub to PowerShell when possible, or verify the text using a plain text editor before pasting to PowerShell. This command creates a new CVI provider of type Cisco and sets the following: The tenantKey assigned by Webex The Exchange invite Alternate Instructions URL provided by Webex |
| 11 | Choose how you want to enable the integration for your users. For help, see Grant-CsTeamsVideoInteropServicePolicy . To enable the integration for all users in your organization, copy the text of the Grant-CsTeamsVideoInteropServicePolicy command from the second text box. To enable all users: Grant-CsTeamsVideoInteropServicePolicy -PolicyName CiscoServiceProviderEnabled -Global To enable the integration for an individual user, copy the text of the Grant-CsTeamsVideoInteropServicePolicy command from the second text box. Replace -Global with -Identity , and add the user's email address after it. To enable user jamie.smith@company.com: Grant-CsTeamsVideoInteropServicePolicy -PolicyName CiscoServiceProviderEnabled -Identity jamie.smith@company.com Paste the command into your PowerShell session and run it. |
| 12 | When you are done with the PowerShell commands, click Ok on the Video Integration Setup screen in Control Hub to complete the setup. |

| Usage | URL pattern |
|---|---|
| More info Instruction link | https://www.webex.com/* |

| Call type | When not sharing content | When sharing content | DTMF mute commands |
|---|---|---|---|
| Cloud-registered /cloud-optimized devices | Local mute and indicators are synchronized with Teams mute and roster. | Local mute only mutes microphones; content audio is still sent to meeting. If a participant has muted themselves locally, they are not shown as muted in the Teams roster. Muting in the Teams roster blocks all audio and turns on local mute and indicators. | Do not use DTMF mute controls—use the device's mute feature. |
| SIP with ActiveControl | Local mute and indicators are synchronized with Teams mute and roster. | Local mute only mutes microphones; content audio is still sent to meeting. If a participant has muted themselves locally, they are not shown as muted in the Teams roster. Muting in the Teams roster blocks all audio and turns on local mute and indicators. | Do not use DTMF mute controls—use the device's mute feature. |
| SIP without ActiveControl | Local mute and indicators are not linked to Teams mute. A local mute does not show in the Teams roster. | Local mute and indicators are not linked to Teams mute. A local mute does not show in the Teams roster. | Use DTMF *6 to enable or clear Teams mute. On-screen messages are shown when Teams mute changes. |

## Figuras

![Video join details in Microsoft Teams meeting invitation](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/447001-448000/447713.jpg)

![Alternate "More info" dialing instructions (hyperlinked meeting-specific web
        page)](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/447001-448000/447714.jpg)

![Create the video integration for Microsoft teams from Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/450001-451000/450221.jpg)

![Authorize video integration setup for Microsoft teams from Control Hub](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/450001-451000/450222.jpg)

![Microsoft sign-in window for video integration](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/484001-485000/484704.jpg)

![List of permissions requested for Webex video integration for MS Teams](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/440001-450000/449001-450000/449221.jpg)

![Control Hub Video Integration Setup screen](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/450001-451000/450224.jpg)

![an icon depicting the copy action](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483842.svg)