---
doc_id: help-webex-com-en-us-article-n1trwjh-release-notes-for-cisco-phoneos-phones-9800-and-8875-8bb6829588
source_url: https://help.webex.com/en-us/article/n1trwjh/Release-Notes-for-Cisco-PhoneOS-Phones-9800-and-8875
retrieved_at: 2026-09-07T13:04:16.361831+00:00
---

Check these release notes for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 running PhoneOS.

The following table describes the individual phone requirements.

Phone

Platform

Support requirements

Cisco Desk Phone 9800 Series

Cisco Video Phone 8875

Cisco BroadWorks 24.0 or later

Cisco Unified Communications Manager 12.5(1) or later

Note :  On PhoneOS 3.2 and later, features delivered in UCM Device
                  Packages require UCM 14 or 15. On PhoneOS 5.0, they require UCM 15.

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) or later

Cisco Expressway 12.5.4 or later

Make sure that the following Manufacture Installed Certificate (MIC) Certificate
              Authorities (CAs) are correctly installed on your platforms:

- High Assurance SUDI CA: https://www.cisco.com/security/pki/certs/hasudi.pem

- Cisco Root CA 2099: https://www.cisco.com/security/pki/certs/crca2099.pem

- Device Identity Basic Assurance Sub CA 2099: https://www.cisco.com/security/pki/certs/dibasca2099.pem

- Device Identity Basic Assurance Root CA 2099: https://www.cisco.com/security/pki/certs/dibarca2099.pem

The enhanced Webex Calling activation code onboarding process requires PhoneOS 4.0 or
              later. Automatic firmware upgrades will be rolled out to phones gradually. For the
              detailed schedule, see PhoneOS auto-upgrade rollout schedule .

For 9841NR and 9851NR with hardware VID V07 or later, the deployment process to UCM
              has been enhanced since PhoneOS 5.0. See Update for 9841NR and 9851NR deployment for details.

## August 19, 2026—PhoneOS 5.0(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875:

(since 3.0)

(since 3.0)

(since 4.1)

(since 4.1)

## Support more line keys on 8875 and 9871

On Cisco Desk Phone 9871 and Cisco Video Phone 8875 registered with Webex Calling or Cisco
        BroadWorks, the number of programmable virtual line keys has increased from 16 to 32. Line
        keys 17 through 32 support the same key assignments as keys 1 through 16, including primary
        lines, shared lines, BLF, speed dial, and other line key features.

Please note that the maximum number of extension SIP line remains 16. Additionally, when
        one or more Key Expansion Modules (KEMs) are connected, only 4 or 8 line keys will be kept
        on the phone and the remaining line keys appear on the KEMs.

For more information, see Configure layouts for Cisco phones in Control
            Hub .

## Custom ringtones

The following updates for ringtones are available on phones registered with Webex Calling
        or Cisco BroadWorks:

- For phones on Webex Calling: Incoming_EQ and Vibes

- For phones on BroadWorks: Chirp 1 and Vibes

- The phones also support up to 10 custom ringtones. New custom ringtones display (Not installed) next to the ringtone name until they are played
            or applied to a line.

For more information about ringtones, see the following links:

- Set
                phone ringtone and volume on 9800/8875

- Configure
                ringtones for 9800 Series and 8875 phones (Control
            Hub)

- Ringtone settings (BroadWorks)

## Quick access to speed dials during conference and
        transfer

With the new Speed dial on Cisco Desk Phone 9811, 9841, 9851, and
        9861, you can transfer calls to speed dial contacts or add speed dial contacts to a
        conference.

If Programmable Softkey is enabled on phones registered with Webex Calling or Cisco
        BroadWorks , make sure that speeddial is included in the Off Hook Key List.
        Otherwise, the Speed dial softkey isn't available. No additional
        setup is required for phones on Cisco Unified Communications Manager.

For more details, see the following links:

## Conference participants list

The Participants softkey is now available during conference calls, allowing you to view and
        manage participants.

For more details, see the following links:

- Make
                a conference call on 9800/8875 (Multiplatform)

- Make
                a conference call on 9800/8875 (Unified CM)

## Updates for programmable softkeys

We have updated the default programmable softkeys for the following key lists on phones
        registered with Webex Calling or Cisco BroadWorks:

- Idle Key List

- Off Hook Key List

- Dialing Input Key List

- Connected Key List

- Conferencing Key List

- Hold Key List

- Shared Active Key List

- Shared Held Key List

- Connected Video Key List

For the updated key lists, see to the following links:

- Configure the programmable softkeys on 9800/8875 (Control
            Hub)

- Configure the programmable softkeys on 9800/8875
            (BroadWorks)

## Enhancements for the Select key

On Cisco Desk Phone 9811, 9841, 9851, and 9861 registered with Cisco Unified CM, you can
        now use the Select key to make calls directly from the Dial screen, the Recents detail page,
        and the Contacts detail page. Additionally, you can also place a call using the Select key
        after editing a dialed number from the Recents detail page and the Contacts detail page.
        This feature has been supported on Cisco Desk Phone 9811, 9841, 9851, and 9861 registered
        with Webex Calling or Cisco BroadWorks since PhoneOS 4.1.

## Acoustic shock protection

On Cisco Desk Phone 9861, 9871 and Cisco Video Phone 8875, administrators can enable the Acoustic shock protection feature that detects and eliminates
        abnormal or unexpected sound from remote incoming audio. This feature helps to protect users
        from sudden loud impulses or distorted signals.

For more information, see the following links:

## Enhancement for E.164 number display

On 9841, 9851 and 9861 phones, incoming call display has been enhanced to show the full
        E.164 numbers in the incoming call window. Previously, long numbers could be truncated,
        especially in large font.

## ThousandEyes integration on Cisco Video Phone 8875

ThousandEyes enables you to monitor and troubleshoot your devices and network. Endpoint
        Agent has been integrated into the phone firmware. But you need to enable ThousandEyes on
        your phones to get the agent registered to the ThousandEyes platform.

See the configurations in the following links:

- ThousandEyes integration for 9800 Series and 8875 phones (Control
            Hub)

- Enable
              ThousandEyes integration for 9800 Series and 8875 phones (Unified
          CM)

## Update for 9841NR and 9851NR deployment on UCM

When you deploy the 9841NR or 9851NR with hardware VID V07
          or later to Cisco Unified Communications Manager (UCM), choose Cisco 9841NR or Cisco 9851NR accordingly, as the new Phone Type. To deploy these models with an
        earlier hardware VID, use Cisco 9841 or Cisco 9851 as the Phone Type. The new
        phone types are available only when your UCM has the device package cmterm-devicepack15.0.1.15036-1 or
        later installed.

To deploy 9841NR or 9851NR with any hardware version to Webex Calling or Cisco BroadWorks,
        use Cisco 9841 or Cisco 9851 as the Phone Type. The system automatically
        identifies the model name based on the product information.

PhoneOS 4.1(1) release

### May 26, 2026—PhoneOS 4.1(1)SR1 release

This maintenance release doesn't include any new or enhanced features.

To view the resolved bugs for this release, see Resolved bugs .

### March 26, 2026—PhoneOS 4.1(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875:

(since 3.0)

(since 3.0)

(since 3.0)

(since 3.0)

(since 3.0)

(since 3.0)

### Abbreviated dials

Abbreviated dials are now supported, enabling users to quickly and easily reach frequently
        dialed numbers by a single numeric key. This functionality enhances efficiency by reducing
        the steps required to place calls to frequent contacts, making communication faster and more
        streamlined.

For more information about this feature, see the following links:

### Private Line Automatic Ringdown (PLAR)

PLAR is now supported on Cisco phones registered with Cisco Unified Communications
        Manager.

PLAR is a feature that automatically dials a predefined number when the user lifts the
        handset or presses the speaker or headset button. The user doesn’t need to manually enter a
        phone number—the call is placed immediately to the configured destination.

For information about PLAR configurations, see Feature Configuration Guide for Cisco Unified
            Communications Manager .

### Minimum ringer volume enforcement

You can now define a minimum ringer volume for phones in Cisco Unified Communications
        Manager to help ensure incoming calls are not missed. When configured, attempts to reduce
        the ringer volume below the minimum are blocked.

For more information about this feature, see the following links:

- Set
                phone ringtone and volume on 9800/8875

- Set minimum ringer volume

### Manage phone with TR-069 settings

You can use the protocols and standards defined in Technical Report 069 (TR-069) to manage
        phones registered in Cisco BroadWorks and other platforms. TR-069 explains the common
        platform for management of all phones and other customer-premises equipment (CPE) in
        large-scale deployments. The platform is independent of phone types and manufacturers.

For more information about this feature, see the following link: Manage phones
            with TR-069 .

### More configurations available in Control Hub

You can now configure the screen brightness and voice feedback settings for your phones in
        Control Hub.

For more information, see Parameters for phone settings on Control
          Hub .

### MARI and FEC for media quality

Media Adaptation and Resilience Implementation(MARI) and Forward Error Correction (FEC) are
        now supported on your phones to dynamically maintain optimal media quality in lossy
        networks. By default, the features are enabled. Because FEC increases bandwidth usage, it
        may negatively impact media quality in congested or bandwidth-constrained networks. You can
        decide whether to disable it based on your network conditions.

For more information about MARI and FEC configurations, see Configure MARI and FEC for media
          quality .

### Option to postpone software upgrades

This release introduces support for postponing firmware upgrades on phones registered with
        Webex Calling or Cisco BroadWorks. After the firmware image is downloaded, the phone
        displays a timed prompt that allows the user to either upgrade immediately or postpone the
        reboot. Users can postpone the upgrade up to 10 times at one‑hour intervals. After the
        postponement limit is reached, the phone automatically reboots and completes the
        upgrade.

### Out-of-Box setup process enhancement

Phones now automatically retry registration in the background when connected to Ethernet,
        even before the MAC address is added to UCM. Once the MAC address is provisioned in UCM, the
        phone registers successfully without any user action or reboot. This enhancement streamlines
        the Out of Box (OOB) setup process for Cisco phones, providing a smoother registration
        experience.

### Quick access with Up and Down navigation keys

On Cisco Desk Phone 9811, 9841, 9851, and 9861, you can press the Up navigation key to
        access the Recents page and the Down navigation key to access the speed dials list.

### Enhancements for the Select key

On Cisco Desk Phone 9811, 9841, 9851, and 9861, you can now use the select key to make
        calls directly from the Dial screen, the Recents detail page, and the Contacts detail page.

### Enhanced LED notifications in Display Off mode

By default, all LEDs are off when the phone is in Display Off mode. You can now customize
        LED behavior in Display Off mode using new parameters introduced in this release. Enabling
        LED indicators helps users stay aware of phone status, such as BLF, voicemail, missed calls,
        and shared‑line status.

The parameter that controls the LEDs varies by phone model:

- Cisco Desk Phone 9841, 9851, 9861, and 9871: Line Key and Top 360 LED in
              Display Off Mode

- Video Phone 8875: Handset LED in Display Off Mode

For more information about this feature, see the following links:

- Office Hours (Unified CM)

- Configure Office Hours for 9800/8875 (Control
                Hub)

### Ringtone per line

The following updates for ringtones are available on phones registered with Webex Calling
        or Cisco BroadWorks:

- Added a new ringtone, Chirp 2.

- In Control Hub, you can now assign a distinct ringtone to each line on phones
            registered with Webex Calling.

For more information about the updates, see the following links:

- Ringtone list in Configure
                9800 Series and 8875 Phones on Control Hub

- Ringtone settings (BroadWorks)

### Visual notification for Group Call Pickup

Users can now receive visual notification for Group Call Pickup once you enable the
        notification type in Control Hub. This enhancement offers a more intuitive and interactive
        way for users to manage Group Call Pickup directly from the notification.

To enable the visual notification, set Notification type to Audio and visual or Visual only .

For more details about the instructions, see Configure call pickup group .

### Device status visibility in Control Hub

You can now access and monitor the live operational state of your phones directly through
        Webex Control Hub. This update provides a centralized and efficient way to perform health
        checks and technical troubleshooting for devices.

For more information about this feature, see View
            device statuses on Control Hub .

PhoneOS 4.0(1) release

### January 20, 2026—PhoneOS 4.0(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875:

(since 3.1.1)

### Cisco Desk Phone 9811

Cisco Desk Phone 9811, a new addition to the 9800 Series, is an essential business phone line, ideal for
        calling users in branch offices, small and medium businesses, or lobby spaces. This
        cost-effective phone provides the core features you need, including 2 lines and a
        customizable action button for quick access to key functions. With intuitive PhoneOS
        software, it makes everyday calling simple and reliable.

For the features available on the phone, see Features on Cisco Desk Phone 9811 .

Make sure that the following Manufacturing Installed Certificate (MIC) and Certificate
          Authorities (CAs) are properly installed on your call control system:

Device Identity Basic Assurance Sub CA 2099

https://www.cisco.com/security/pki/certs/dibasca2099.pem

Device Identity Basic Assurance Root CA 2099

https://www.cisco.com/security/pki/certs/dibarca2099.pem

### Feature Line keys improvement

An administrator can now list Call park , Call
          pickup , Group pickup , and Other
          pickup as feature line keys on Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Cisco Unified CM.

For more information about the feature, go to the following link:

- Feature keys and BLF on 9800/8875 (Unified CM)

### Report a malicious call

You can report troublesome or threatening calls as malicious by using a
        softkey or a line key. Cisco Unified CM can identify and register the source of the reported calls in the network.

For more information about the feature, go to the following links:

### Conference/transfer with on-hold calls

You can now transfer a call to an on-hold call or add it to a conference. If there are
          on-hold calls on the phone, the Calls tab appears, allowing you to select one
          during the transfer or conference.

For more details about this feature, see the following links:

- Use
                  your phone 9800/8875 for an ad-hoc conference (Multiplatform)

- Transfer a call on 9800/8875 (Multiplatform)

### User access improvement to the Settings menu

This release includes the following user access improvement to the Settings menu on Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Cisco Unified CM.

- The EM (or EMCC ) menu is now out of
          hierarchies. If extension mobility is configured, a user can directly access this menu
          under Settings .

- When the Settings access is disabled, a user can access the EM (or EMCC ) and Network and
            service menus.

- When the Settings access is restricted, a user can access the EM (or EMCC ), Network and
            service , and Accessibility menus.

For more information about the feature, go to the following links:

- Sign in to a shared phone (Extension
            Mobility)

- Configure 9800 and 8875 phones on Unified CM

### E911 service control

In PhoneOS firmware versions earlier than 4.0.1, phones sent HELD requests to third-party
        E911 service providers when the CUCM Location URL was configured in the Emergency
          Calling Profile section of the Service Profile .

In this release, a new parameter, HELD Support for Third-Party E911 ,
        is introduced. This parameter allows you to enable or disable the E911 service on phones
        based on your business needs. By default, this setting is disabled.

For phones running earlier firmware versions, the E911 service is disabled after upgrading
        to PhoneOS 4.0.1. If you choose to enable this parameter, be aware that it does not work
        with CER and requires appropriate licensing and provisioning from the third-party E911
        service provider.

For more details about E911 configurations, see Configure your phones for emergency calls
            (E911) .

PhoneOS 3.6(1) release

### November 17, 2025—PhoneOS 3.6(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875:

(since 3.2.1)

(for 9800 Series only)

(for 9851, 9861, 9871, and
                  8875)

(since 3.2.1)

(since 3.2.1)

(for
                  9861, 9871, and 8875)

### Display LLDP-MED TLV location information on your phone

After an administrator enabled the E911 geolocation feature on any line and set LLDP-MED as
        the location source, you can now select About this device > Location from the Settings menu on your phone to view the
        location information.

For more information about the feature, go to the following link:

- Use LLDP-MED protocol for emergency calls on 9800/8875

### Disable speakerphone

An administrator can now disable the speakerphone functionality and prevent you from
        re-enabling the speakerphone. However, disabling speakerphone functionality will not affect
        the handset or headset. You can change the audio path to headset or handset to use lines,
        speed dials, and softkeys for calling features.

For more information about the feature, go to the following links:

- Configure 9800 Series and 8875 Phones on Control Hub

- Configure calling features on 9800/8875 (BroadWorks)

### Cloud-assisted transcription in calls

Real-time translation and transcription improves accessibility and allows you to have more
        inclusive communication. Now you can turn on captions and view live transcripts during phone
        calling on Cisco Desk Phone 9861, Cisco Desk Phone 9871, and Cisco Video Phone 8875.

For more information about the feature, go to the following link:

- Use closed captions in phone calls and Webex meetings on 9800/8875 (Webex
              Calling)

### Reverse name lookup for Webex Personal Contacts

When reverse name lookup searches the phone's external directories, it also searches the
        Webex Personal Contacts dirctory and resolves self-defined contacts in Webex. When a search
        succeeds, the caller's name is displayed in the incoming call notifications, the call
        session and the call history.

For more information about the feature, see Configure 9800 Series and 8875 Phones on Control
            Hub .

### User experience improvement on Webex Meeting PIN challenge

Users may be prompted for the host key or the meeting password when joining a scheduled
        Webex meeting from the phone. This feature enhances security by ensuring that only
        authorized participants can join the session.

The prompt appears under any of the following conditions:

- The administrator has configured the conference system to require a meeting password to
          join.

- The meeting host didn't include the password in the invitation while scheduling the
          meeting.

- The user isn't a direct invitee and received the meeting link through forwarding or a
          mailing list.

For more information about this feature, see Check
            and join a meeting on 9800/8875 (Webex Calling) .

### xAPI updates

In this release, we enhance xAPI capabilities by introducing expanded network statistics,
        LED status monitoring, detailed per-call metrics, and device operational status. This update
        offers deeper insights into phone performance and call quality metrics. we added new xStatus
        and enhanced the xCommand for device booking. For details about the supported xAPIs and the
        related documentation, see https://phoneos.cisco.com .

Administrators can manage devices registered with Webex Calling using the Run
          xCommand feature in Control Hub. For more information, see Run
            xCommands from Control Hub .

### Support for CiscoIPPhoneStatus XML object

Since PhoneOS 3.6 release, the following phones support the CiscoIPPhoneStatus XML object:

- Cisco Desk Phone 9851, 9861, and 9871

- Cisco Video Phone 8875

For more information, see the following links:

Cisco
                Unified IP Phone Services Application Development Notes

XML
              applications configuration for 9800 and 8875 phones (BroadWorks)

XML
              applications and services configuration for 9800 and 8875 phones (Unified
            CM)

### Webex companion on 9800 Series

The Companion mode allows the phone to participate in video calls and Webex meetings by
        using the Webex App for video. Users can send and receive video or share content through the
        Webex App while keeping audio on the phone.

For more information, see the following links:

- Video calls and meetings on Desk Phone 9800 Series (Unified
            CM)

- Enable your phone to use the video capability on
                Webex

### 802.1x Custom Device Certificate (CDC) enhancement

When Security Mode parameter is set to EAP-TLS and Certificate Select parameter is
        set to Custom installed , the User ID becomes available for
        configuration on the phone. The Wi-Fi User ID configuration determines the 802.1x EAP-TLS
        Identity with the following behavior:

- If a user ID is configured : The phone will use the specified value as its 802.1x
          EAP-TLS Identity.

- If the user ID field is left blank : The phone will always default to using the
          MIC (Manufacturer Installed Certificate) or SUDI (Secure Unique Device Identity) Common
          Name as its 802.1x EAP-TLS Identity. This behavior occurs even if a Common Name has been
          selected via CDC (Certificate Device Configuration).

For more information on new parameters to support the feature, see Parameters for
          SCEP configuration section and Parameters for phone settings on Control
          Hub section in Configure 9800 Series and 8875 Phones on Control
        Hub .

### Move call to phone

Users can now use the Call Pull softkey to move an active call from
        the Webex App or another device directly to their desk phone. This ensures a seamless
        transition and uninterrupted conversation.

For more information on how to use the feature on the phone, see Move a
            call to your desk phone .

To configure the softkey, see Configure call pull on a programmable
          softkey .

### XSI call logs

You can configure phone to display associated XSI call logs or unassociated XSI call logs.
        To enable this feature, select an associated line and configure the Display
          Recents From parameter to XSI Server .

For more information on how to enable the parameter, see Configure call logs to display
          on the phone section in Configure calling features on 9800/8875
            (BroadWorks) .

### Enhancements for Hot Desking

The following enhancements are available in this release:

Beyond ad-hoc booking, the Cisco Desk Phone 9800 Series now supports Hot Desking
            reservations via Cisco Spaces or third-party booking apps. Reserved phones display
            reservation details and allow sign-in only by the user who reserved it.

The Desk Phone Control (DPC) feature is now supported on phones in Hot Desking mode.
            After signed in, users can control their desk phone from the Webex app, including
            placing calls, transferring or holding/resuming calls, and joining meetings.

For more information, see Sign in to a shared phone (Hot Desking) .

### Optimized directory search performance

In this release, we optimized connection handling to speed up Cisco BroadWorks directory
        searches and enable directory lookups during mid-call actions like transfers and
        conferences, improving overall call-handling efficiency.

PhoneOS 3.5(1) release

### September 16, 2025—PhoneOS 3.5(1)SR1 release

This maintenance release doesn't include any new or enhanced features.

To view the resolved bugs for this release, see Resolved bugs .

### July 31, 2025—PhoneOS 3.5(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875:

User ID configuration for wired 802.1X

### Customizable New call softkey for connected call state

Before the release, the New call softkey is always positioned in the third place when the phone is in the connected call state.

Now you can choose to show or hide the softkey when the phone is in the connected call state. By default, the softkey doesn't display in the state.

For more information about the feature, go to the following links:

- Make and answer calls on 9800/8875 (Unified CM)

- Feature keys and BLF on 9800/8875 (Unified CM)

### Dialog-based shared line appearance (SLA)

You can now enable dialog-based shared line, so that the phones in the shared line can subscribe to the dialog event package.

For more information see Dialog-based shared line appearance (SLA) .

### Individual Queue Login

Phone now can join or leave the call queue for Webex Calling. It supports two types of call queues: Call queues and Customer assist.

For more information, see Join status of a call queue .

### Multiple appearances support for line key labels

You can configure multiple appearances of the same line on the phone. So the phone can display the same line multiple times with a suffix (like -1, -2), based on the number of the appearances configured.

The multiple appearances feature is also applicable for the line key labels on KEM.

For more information about the feature, go to the following links:

- Configure line key labels for 9800/8875 (Control Hub)

- Cisco Desk Phone 9800 Key Expansion Module

- Configure and manage Webex Calling devices

### Diagnostics info on Control Hub

You can check the reported issues from the Devices > Issues & Information section on Control Hub. For all alerts reported by the phones, you can check them in Alerts center on Control Hub.

For more information about the feature, see Alerts center in Control Hub .

### Cisco Smart Power Framework

The smart power feature allows Cisco Smart Switches to manage the phone's power modes via
        Power over Ethernet (PoE). You can choose whether to allow the switch to follow or override
        the office hours and deep sleep settings configured in the phone's calling system.

For more information about the feature, see the following links:

- Configure Office Hours for 9800/8875 (Control Hub)

- Configure 9800 and 8875 phones on Unified
              CM

- Configure phone features for 9800 Series
                (BroadWorks)

### LLDP-MED TLV location support for emergency calls

Now the phone can support the LLDP-MED protocol to share its location information with the responders during emergency calls.

This feature is only available for the phones on call controllers that support LLDP MED TLV Location Identification Support.

For more information about the feature, see the following links:

- Use LLDP-MED protocol for emergency calls on 9800/8875

- Configure calling features on 9800/8875 (BroadWorks)

### Settings menu customization

The menu customization feature allows you to enhance usability by displaying only relevant
        settings to users, and to improve control and security by restricting access to sensitive
        settings.

By default, all Settings menu items are visible to phone users. You can now customize the
        Settings menu of your phone by hiding items that you don't want users to access.

This feature is available on phones registered to Webex Calling or Cisco BroadWorks.

For more information about the feature, see the following links:

- Customize
              the Settings menu for 9800 Series and 8875 phones (Control Hub)

- Manage the Settings menu visibility
            (BroadWorks)

### Accessibility voice feedback for multi-languages

When the phone is enabled with voice feedback, it supports multiple languages. Voice feedback is aligned with the configured language if the language is supported for voice feedback. People with vision problem can hear the voice feedback in their own language. It helps them to navigate and use the phone easily. The supported languages for voice feedback are:

- French (Canada, France)

- Italian

- German

- Spanish (Columbia, Spain)

- English (UK, US)

For more information, see the following links:

- Accessibility features

- Enable voice feedback with multi-languages (Control Hub)

### Always use the multi-line layout

This feature is only available on Cisco Desk Phone 9841, 9851, and 9861. It ensures a
        consistent user experience by forcing the phone to always display the multi-line layout.

By default, the phone displays the multi-line interface only when multiple lines or other
        line key features are configured. When Always Use Multi-line Mode is enabled, the phone uses
        the multi-line layout even if only a single line is configured.

For more information about the feature, see the following links:

- Prameters for phone settings on Control
          Hub

- Set the phone to always display the multi-line
              interface (Unified CM)

- Set the phone to always display the multi-line
              interface (BroadWorks)

### Factory reset from Unified CM

Starting with this release, you can perform a factory reset of your phones remotely through
        Cisco Unified CM, without needing physical access. This features helps simplify large-scale
        device reassignments and streamlines troubleshooting.

For more information about the feature, see Remotely
          factory reset 9800 and 8875 phones on Unified CM .

### xAPI

xAPI is a set of APIs used to monitor, manage, and control PhoneOS-based devices. In this
        release, we are introducing xAPI as a new option for customers and partners to manage phones
        and build custom solutions. Customers and partners can access xAPI through HTTP or HTTPS.

The following features are now supported on phones registered to Webex Calling, Cisco
        Unified CM, or Cisco BroadWorks:

Retrieve basic device information and status, and subscribe to phone events

Perform device reboot and factory reset

Simulate hard key presses and screen touch operations

Capture device screens

Initiate calls

To use xAPI on the phone, administrators need to

- Enable web access on the phone

- Enable the xAPI account on the server

- Prepare an HTTP client and HTTP server for feedback collection

For information about the supported xAPIs and the related documentation, see https://phoneos.cisco.com .

For information about how to enable xAPI on your phone, see the following links:

- Parameters for phone settings on Control
              Hub

- Enable xAPI on your phone (Unified
            CM)

- Enable xAPI on your phone
            (BroadWorks)

### Common Name configuration for CDC and User ID configuration for wired 802.1X

You can configure the Common Name (CN) for a Custom Device Certificate (CDC) installed by Simple Certificate Enrollment Protocol (SCEP). The CN will be used in the Certificate Signing Request (CSR) in the SCEP process.

If the custom certificate is selected for 802.1X authentication, you can configure the User ID that will be used as the identity for the wired 802.1X.

The configuration of CN and User ID supports the macro expansion variables.

During the SCEP provisioning via DHCP option 43, you can also utilize DHCP option 15 to provide a domain name. The phone can retrieve the domain name to construct the Common Name and User ID.

From this release, you can configure the SCEP parameters on Control Hub. Besides, the new parameters Certificate Select and User ID are added for 802.1X configuration.

For more information about the feature, see the following links:

### FIPS 140-3 compliance

Federal Information Processing Standards (FIPS) 140-3 is now available on the Desk Phone 9800 Series and Video Phone 8875 to further enhance the security.

PhoneOS 3.4(1) release

### April 29, 2025—PhoneOS 3.4(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875:

(for 9800 only)

(for 9800 only)

(for 9861/9871/8875 only)

(for 9800 only)

(for 9841/9851/9861 only)

(since 3.2.1)

(for 9861/9871/8875 only)

(for 8875 only)

### New and changed features

The PhoneOS Release 3.4(1) delivers the following new features and enhancements:

For the phones (except for 9861NR and 9871NR) that support NFC, the NFC onboarding now can support more configurable items in the predefined NFC data payload. Before this release, you can only configure onboarding method and the related onboarding details. Now you can further configure the following:

- MAC address of the phone (only applicable when the NFC data is signed)

- Wi-Fi network access configurations (such as, SSID, user ID, password)

- Custom Certificate Authority (CA) rule

To secure the NFC onboarding info (Wi-Fi configurations and Custom CA rule) that is transmitted between NFC device and phone, only the following security levels are permitted:

- Signing

- Encryption + Signing

In addition to the configurations in the NFC data payload, users can receive the notification messages that indicate the phone is ready to scan during the onboarding process.

For more information about the feature, go to the following links:

- Prepare NFC onboarding data for Desk Phone 9800 Series

- Register your Cisco Desk Phone 9800 Series (with NFC)

The phone now can keep the user settings that are applied before the phone's Out-Of-Box (OOB) registration. Before this release, the user settings are cleared and reset to their factory settings automatically after the phone is registered.

Currently, this feature can preserve the following user settings:

- HTTP proxy settings

- 802.1X authentication state (Enabled or Disabled)

For more information about the feature, go to the following links:

If your administrator has
          made you a member of a pickup group, you can answer calls for your group members when they
          are busy or absent. If there are multiple calls queuing in a group, you can answer calls
          for any of your group members or for a specific coworker as per the configuration. If
          multiple calls are available for pickup, you'll answer the call that has been ringing for
          the longest time. You see alerts in both the front arc LED and top LED if your
          administrator configures the notification alert for both the LEDs.

For configuring
          the LED alert type on Control Hub, see Configure the LED alert type for group call
              pickup .

The Hot Desking feature now supports
          sign-in via voice portal. Users can use the softkey or dial the Feature Access Code *30 to
          sign in to a workspace phone through voice portal authentication. By default, the Hot
          Desking sign in using voice portal option is enabled in the location-level and user-level
          configurations.

For more information, go to the following links:

- Sign in to a shared phone (Hot Desking)

- Configure Hot Desking on Control Hub

You can scan a QR code displayed on the phone screen to sign in to a Webex cloud calendar service with a Webex account. After a successful sign-in, you can join a calendar meeting on the phone. The supported meeting types include Webex and Teams.

For more information about the feature, go to the following links:

- Check and join a meeting on 9800/8875 (Unified CM)

- Enable calendar meetings on 9800/8875 (Unified CM)

During a Webex meeting in companion mode, your phone and Webex App work together as a combined system. When you pair your phone with Webex App, you can join a meeting either from your phone or from Webex App.

During this Webex meeting in companion mode, you can enjoy the following advantages:

- Send and receive a video, view or share content using Webex App, and keep the audio on the phone.

- Mute or unmute the phone audio, or adjust the phone volume using Webex App.

For more information on Webex meeting in companion mode, see Webex Companion with Desk Phone 9800 Series (Webex Calling) .

Now the phone supports to generate the Webex meeting summaries by using Cisco AI Assistant. The AI Assistant can analyze the discussion during the meeting in order to provide the meeting minutes and action items.

On the phone, the meeting hosts or participants (if granted the permission) can start or stop the meeting summary.

Currently, only the hosts using the Webex App can grant the permission to the participants.

For more information about the feature, go to the following links:

You can configure the display format (number or name) of lines that display on the phone screen by using Control Hub.

The configured display format can be applied to the following:

- The primary line that displays at the top left corner of the phone screen

- All lines if the phone has multiple lines

- The secondary line label if it's enabled

- All lines on Key Expansion Module (KEM)

For more information about the feature, go to the following link:

The following
          enhancements have been introduced with this release:

Silent emergency call retrieval

A new parameter, Allow Silent Emergency Call Retrieval, is now available to control
              whether users can regain phone functionality during a silent emergency call.
              Previously, users has to wait for the call recipient to end the call. If this
              parameter is enabled, users can press any key to restore normal phone operation while
              maintaining the emergency call. The call audio remains silent unless the user
              increases the speaker volume using the Volume key.

A single trigger for multiple events

Administrators can specify multiple service destinations for the Action button to
              allow users to initiate multiple events with a single trigger. For example, if
              configured, pressing the button will not only place an emergency call but also send an
              alert message to other phones within the organization. This feature streamlines
              critical workflows, making it easier to respond quickly in certain situations.

For more information, go to the following links:

On Desk Phone 9841, 9851, and 9861 with multiple lines, you can enable the feature to minimize the call window (including incoming call, single call, calls list, new call, etc.) automatically to the inline call label. The inline call label includes the call session information, such as caller/callee name, number, call duration, call state, and call state relevant icons. When the feature is enabled, the status of other lines won't be blocked by the call window. Therefore, you can view the status of all lines on the phone when you have active calls.

This feature is also applicable for the lines on Key Expansion Module (KEM).

For more information about the feature, go to the following links:

A new parameter,
          Display Off During Office Hours, has been added to control whether the phone display turns
          off when the phone is inactive during office hours. This helps reduce power
          consumption.

For more information, go to the following links:

Multilevel Precedence and Preemption (MLPP) improvement

From this release, the phone that initiates the priority call with a router or translation pattern can also show the special notifications (flag icon + precedence level) on the phone screen. At the same time, the phone plays the precedence ringback tone.

For more information about the feature, go to the following links:

- Make and answer priority calls on 9800/8875 (Unified CM)

- Multilevel Precedence and Preemption

The phones registered to Webex Calling or BroadWorks now support the TLS up to the 1.3 version. Before this release, the maximum supported version of TLS is 1.2.

For more information about the feature, go to the following links:

- Set the minimum TLS version for client and server

- Network Requirements for Webex Services

You can enable the backward compatibility for the oldest version of Wi-Fi Protected Access (WPA). If enabled, the phone can connect to the wireless networks or access points that only support WPA. By default, the feature is disabled.

For more information about the feature, go to the following links:

- View information about security settings on phone (Unified CM)

- View information about security settings on phone (Multiplatform)

The device-level configuration has
          been moved from Devices > {device} > Device Settings to Devices > {device} > All configurations . The device settings in Organization-level, Location-level configuration,
          and Templates have been also moved.

After the initial upgrade from PhoneOS 3.3.1 to 3.4.1, any subsequent upgrades or
            downgrades won't migrate any changes made to Device Settings.

For more information about how to configure 8875 phone settings on Control Hub,
          see Configure 9800 Series and 8875 Phones on Control Hub .

Cisco Unified Mobility offers a set of
          mobility-related features that allow users to interact with Unified Communications
          applications no matter where they may be, or which device they are using. Whether the
          device you are using is a home office phone, a dual-mode Cisco Jabber on iPhone or Android
          client over a Wi-Fi connection, or a mobile phone from another cellular provider, you can
          still access Unified Communications features and have the call be anchored in the
          enterprise.

For more information about the feature, see Cisco
              Unified Mobility .

PhoneOS 3.3(1) release

### January 23, 2025—PhoneOS 3.3(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series:

### New and changed features

The PhoneOS Release 3.3(1) delivers the following new features and enhancements:

Now the phone (except for none-radio model) supports the onboarding process via its NFC tag. By scanning the NFC tag with an app (for example, NFC Tools) running on a mobile phone, the onboarding information can be written to the phone in advance even before it boots up. When the phone boots up and connects to a network, the onboarding process starts automatically and chooses the path depending on the written information. In this way, the phones can be onboarded easily with zero touch for the phone users.

During the onboarding process, you can also scan the NFC tag to fill in the required information (for example, activation code or TFTP server address) if you don't want to manually enter the information on the phone.

For more information about the feature, go to the following links:

The Cisco IP
          Manager Assistant (Cisco IPMA) feature enables managers and their assistants to work
          together more effectively. Cisco IPMA supports two modes of operation: proxy line support
          and shared line support. Both modes support multiple calls per line for the
          manager.

For more information, go to the following links:

- Use Cisco IP Manager Assistant (IPMA) on phones

- Configure and Troubleshoot Cisco IP Manager Assistant (IPMA)

This feature allows you to manage the mode-based forwarding of the specified features on a line key. You can manually switch the operating mode of call queues on your phone. Hence, the incoming calls are effectively routed to different destinations based on the operating mode you've selected.

For more information, go to the following links:

- Switching operating mode

- Call routing based on operating modes in Webex Calling

The Hot Desking sign-in process has been optimized to reduce the processing time and remove the need for a device reboot.

The phone users now can open the closed
          captions to display the transcription of the dialogue during a Webex hybrid
          meeting.

For more information about the feature, go to the following links:

The Microsoft Teams meeting now is supported on the phone that is registered to Webex Calling. The Teams meetings can display in the Upcoming meeting and Calendar screens on the phone. Also, users can check details of the Teams meetings. Similar to the Webex meeting, users can directly join a Teams meeting by pressing or tapping the Join softkey or soft button (depending on the phone model).

For more information, go to the following links:

- Check and join a meeting on your phone

- Return to a meeting

The Action button can now be configured to
          trigger up to three distinct services, each with its own unique trigger configuration.
          When configured with custom services, the Action button can also trigger actions through
          HTTP Post requests.

For more information, go to the following links:

- Configure the Action button for 9800 (Control Hub)

- Configure the Action button on 9800 (Unified CM)

- Configure the Action button on 9800 (Multiplatform)

Users can add their own speed dials on the phone. The user-added speed dials can be edited and removed from the speed dial list. However, users can't update or remove the speed dials added remotely through Self Care Portal or by administrators in Cisco Unified Communications Manager.

For more information, see Manage speed dials .

The users
          can change the custom wallpaper or logo, or both, on the phone. As the administrator, you
          can customize or set up the wallpaper and logo from the Control Hub or phone web page.

For more information about the feature, go to the following links:

As the administrator, you can send an HTTP file that contains an XML body to apply the custom wallpaper on the target phones.

For more information about the feature, see Customize wallpaper by sending XML to the phone .

Phone now supports the following languages:

- Bulgarian

- Croatian

- Estonian

- Latvian

- Lithuanian

- Slovenian

- Welsh

For more information, see Change language for your phone .

Screen pagination increases the capacity of the phone and allows to add more extension lines and features on line keys, than the number of physical line keys.

For more information, see Pagination on Cisco Desk Phone 9851 and 9861 .

User Preference Attribute

The user-pref attribute allows you to set some user preferred value to provide a seamless experience for your user. Users can make further changes from the phone or from the phone administration web page. Any parameter changed by user is marked as user modified with an attribute um. Any changes made by the user are preserved.

The user-pref attribute can be updated during provisioning using XML configurations delivered with the Profile Rule parameter.

For more information, see User Preference Attribute .

Your phone now support updating Cisco headsets. When you connect a Cisco headset to the phone, the phone automatically check for updates.

For Cisco Headset 520 and 530, the phone starts the upgrading process automatically.

For Cisco Headset 300 Series, 560, and 700 Series, you are prompted to start updating or postpone it.

For more information, see Upgrade Cisco headset firmware on phones .

Reports for phones are available in the Monitoring section in Control Hub that you can use to help track usage or solve issues for your devices in your organization.

For more information, see Reports for Your Cloud Collaboration Portfolio .

Now the phone supports to provide information about the security issues. If any security issues occur on the phone, you can view the detailed information from the Issues and diagnostics screen.

For more information about the feature, see Check device security status on the phone .

You can set up the phone to
          connect the Internet through a specified HTTP proxy server for security purposes or
          resovle some HTTP connection issues. The users can either set up a proxy server on the
          phone or from the phone web page.

For more information about the feature, go to the
          following links:

You can enable a VPN connection on the phone
          from the Settings > Network and service . The established VPN connection doesn't require you to restart your
          phone.

For troubleshooting purpose, you can view the VPN statistics from the Issues and diagnostics screen which includes detailed information
          about current, closed, and failed VPN connections.

For more information about the
          feature, go to the following links:

- Connect to a VPN

- Check VPN statistics

- VPN configuration

PhoneOS 3.2(1) release

### October 31, 2024—PhoneOS 3.2(1) release

This release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series:

Multicast Paging with XML Application Support

Survivability

### New and changed features

The PhoneOS Release 3.2(1) delivers the following new features and enhancements:

You can use the service domain onboarding with Mobile and Remote Access (MRA) when deploying your phones for remote users. When users choose and enter a valid service domain, they will be prompted to enter their user credentials for the MRA authentication.

For more information about the feature, go to the following links:

- Register Cisco Desk Phone 9800 Series

- Get
                phones onboard to Cisco Unified Communications Manager

User login credentials can be stored on the phone
          after the user signs into the Expressway server for Mobile and Remote Access (MRA). If
          enabled, the users don't need to enter the credentials again even though the phone
          restarts.

This feature requires UCM 14 or later with Device Packages.

For more information about the feature, see Configure user credentials persistent for
              Expressway sign-in .

You can configure the phone to require the users to enter FAC or CMC, or both before they dial out a specific phone number. By using FAC and CMC, you can effectively manage call access and accounting. FAC regulates the types of calls that certain users can place, CMC assists with call accounting and billing for clients.

For more information about the feature, go to the following links:

- Calls that require authorization code or client
                matter code

- Configure speed dial numbers with Self Care Portal

- Feature Configuration Guide for Cisco Unified Communications Manager

You can set up multicast paging to allow the users to page to phones. The page can go to all phones or a group of phones in the same network. Any phone in the group can initiate a multicast paging session. Only the phones that listen for the paging group can receive the page.

In addition, you can configure the phones to receive pages from an XML server to optionally display an image or other UI elements. With this feature, you can invoke the XML service from multicast paging.

For more information about the feature, go to the following links:

Phone can now be enabled with Automatic Call Distribution (ACD) features. This phone acts as a call center agent's phone and can be used to trace a customer call, to escalate any customer call to a supervisor in emergency, to categorize contact numbers using disposition codes, and to view customer call details.

For more information, see Configure call center agent phone .

The User Data Service (UDS) is used as the default directory service for phone on Unified CM. You can disable the service either for all phones or for an individual phone if you don't use it. When disabled, users on the phone can't view the personal or corporate contacts provided by UDS.

This feature requires UCM 14 or later with Device Packages.

For more details, see Configure directory services for phones on Unified CM .

From this release, only the Top 360 LED lights up for the voicemails and missed calls. The Front Arc LED doesn't light up any more for the voicemails and missed calls.

By default, the Top 360 LED doesn't light up for the missed calls. You can enable the LED indication from the call control system.

For more information, go to the following links:

The enhancements for the Hot Desking feature include the following:

Hybrid working users can sign in to Hot Desking enabled phones through either Webex App or a web browser on their mobile devices.

Administrators can extend user bookings or terminate them on Control Hub.

The phones can be provisioned as hot-desk-only mode. Only emergency calls are supported on these phones. Users are required to sign in with their Webex account to use the full features.

For more information, go to the following links: .

- Sign in to a shared phone (Hot Desking)

- Configure Hot Desking on Control Hub

In this release, we deliver the following meeting related features:

- Mute status sync in hybrid meeting : The audio mute status is now synchronized across multiple devices, including the phone, connected headset, and Webex App. This ensures that the user's audio status remains consistent across all devices when they join a meeting with the phone.

- Recoding indication in meeting : When a meeting is being recorded, a recording indication pops up on the phone screen to notify the users that the meeting is being recording. Also, the users will receive a notification when the recording is paused, resumed, or stopped.

- Participant list : The participant list shows the participants with their roles and the video and audio status. The invitees that aren't present are listed in the lower part of the list.

For more information about the feature, go to the following links:

- Check and join a meeting on your phone

- Programmable softkeys configuration on 9800/8875
              (Multiplatform)

- Configure the Programmable Softkeys for 9800/8875 (Control
            Hub)

The Action button can be configured to either make an emergency call or trigger a custom service. Administrators can customize the service name, which appears in a popup when the button is pressed, helping users identify which service they'll access.

This feature requires UCM 14 or later with Device Packages.

For more information, go to the following links:

- Configure the Action button for 9800 (Control Hub)

- Configure the Action button on 9800 (Unified CM)

- Configure the Action button on 9800 (BroadWorks)

The Cisco Desk Phone 9800 Series now support Thai, Romanian, Serbian, Slovak, Arabic, and Hebrew as display languages.

For phones on BroadWorks, administrators can add XML applications and assign softkeys or line keys with XML applications for easy access.

For the supported XML objects, URIs, and configurations, see the following links:

- Cisco Unified IP Phone Services Application Development Note

- XML applications configuration for phones on BroadWorks

Voice feedback helps people with vision problems to use their phone. When enabled, a voice prompt helps you navigate the phone screen and use or configure phone features.

The voice also reads out incoming caller IDs, touchable area information, screen summary, virtual keyboard keys,hard keys, and softkey information.

To have a better visual experience, you can customize the font size when the phone is taken out-of-box. The customization of the font size does not change few of the texts, such as the texts on the phone header, some descriptional small texts, large text on the phone Home screen, texts in the softkey bar. If key expansion module is connected to a phone, font size of the text in KEM also changes during this customization.

For more information on configuring voice feedback on the phones registered to Cisco BroadWorks or Webex Calling, see Configure voice feedback .

For more information on configuring from phone, see Voice feedback (accessibility) .

For information on font change, see Customize font size on your phone .

The phones now support Cisco Headset USB-C Adapter for the connection with Cisco wireless headsets.

For more information, see Cisco Headset USB Adapter .

ThousandEyes enables you to monitor and troubleshoot your devices and network. Endpoint Agent has been integrated into the phone firmware. But you need to enable ThousandEyes on your phones to get the agent registered to the ThousandEyes platform.

Only Cisco Desk Phone 9861 and 9871 support this feature.

This feature requires UCM 14 or later with Device Packages.

See the configurations and limitations in the following links:

- ThousandEyes integration for 9800 (Control Hub)

- Enable ThousandEyes integration for 9800 (Unified CM)

For phones on BroadWorks, administrators can
          configure random timer for the phone to enter deep sleep and wake up around the schedule.
          This feature help distribute the load of network and power system when a large number of
          phones power on and off simultaneously.

You can control whether to light up the
          Front Arc LED indicator when the phone enters the Display-Off mode. By default, the LED
          will turns off. You can change the setting with the LED Indicator in "Display Off Mode"
          parameter.

This feature requires UCM 14 or later with Device Packages.

See the configurations in the following links:

- Configure Office Hours for 9800 (Control Hub)

- Phone features and setup on Unified CM

- Configure phone features on the phone administration
          page

Phone now has the ability to automatically register to the Site Survivability Gateway (SGW) nodes when the network connection to Webex Calling breaks. When the phone connects to the SGW nodes, phone supports only limited set of calling features. When this feature is enabled, user can see the "Limited features available" notification on the phone.

See the configurations in the following links:

- Limited features available notification

- Configure calling features

- Site survivability for Webex Calling

Assured Services SIP(AS-SIP) is a collection of features and protocols that offer a highly secure call flow for Cisco IP Phones and third-party phones. AS-SIP is often used with Multilevel Precedence and Preemption (MLPP) to prioritize calls during an emergency.

For more information, see Assured Services SIP .

In the previous release, only the RSA key is supported in CAPF. Now, the EC key is also supported. To use the EC key, make sure that the parameter "Endpoint Advanced Encryption Algorithms Support" (from System > Enterprise Parameter ) is enabled.

See the configurations in the following links:

- Security Guide for Cisco Unified Communications Manager

- CUCM Third-Party CA-Signed LSCs Generation and Import Configuration Example

- Configure Automatic Certificate Enrollment and Renewal Via CAPF Online CA

You can install a Custom Device Certificate (CDC) by using one of the following methods:

The certificate typically contains a private key and password associated with it.

You can configure the SCEP parameters by using one of the following methods:

- Phone web page

- XML provisioning

- DHCP option 43

The certificate can be installed for the wired and wireless network with 802.1x authentication.

On the phone web page, you can check the installation status of the certificate, view details of the installed certificate, and remove the installed certificate.

On the phone or phone web page, you can select the certificate type (Manufacturing or Custom) for the 802.1x authentication in wired/wireless network environment.

For more information about the feature, go to the following links:

You have the options to permanently turn off the speakerphone, headset, and handset on a phone for your user.

This feature requires UCM 14 or later with Device Packages.

For more information, see Turn off speakerphone, headset, and handset on a phone .

Multilevel Precedence and Preemption (MLPP) allows users to prioritize calls during emergencies or other crisis situations. A priority call takes precedence over a normal call or a lower-priority call.

The user can assign a priority to the outgoing calls that range from 1 to 5. Incoming calls display a precedence level icon and the receiver will hear a special ring that is faster than usual.

For more information about the feature, go to the following links:

- Make and answer priority calls

- Use Do Not Disturb (DND)

- Multilevel Precedence and Preemption

The phone supports Cisco UCM with Multi-server (SAN) Tomcat Certificates configured. The correct TFTP server address can be found in the phone ITL file for phone's registration.

For more information about the feature, go to the following links:

- How To Configure Multi-server (SAN) Tomcat certificate with Cisco UCM

- Security Guide for Cisco Unified Communications Manager

If you don't configure the user/admin password on the phone, the phone UI and phone web page will display the no password warning. For security concerns, we recommend to set up the password after the phone's first registration or a factory reset.

In addition, you can't submit the changes from the phone web page until the password is configured.

For more information about the feature, go to the following links:

- Set the user and admin password

You can set up the minimum version required for TLS client and TLS server respectively.

This feature requires UCM 14 or later with Device Packages.

For more information, see Set up the supported versions of TLS .

PhoneOS 3.1(1) release

### August 13, 2024—PhoneOS 3.1(1)SR1 release

This release is a maintenance release and doesn't contain any new or enhanced features.

To view the resolved and open bugs for this release, see Open and resolved bugs .

### July 15, 2024—PhoneOS 3.1(1) release

This release firmware introduces Cisco Desk Phone 9861, 9861NR, 9871, and 9871NR. Basically, these phone models support the features for Cisco Desk Phone 9841 and 9851 in the PhoneOS 3.0.1 release. For details, see PhoneOS 3.0(1) release . In addition, this release firmware provides the following new and enhanced features for Cisco Desk Phone 9800 Series:

Activation code onboarding

Narrowband-to-wideband audio enhancement by AI (for 9861/9871)

PhoneOS 3.0(1) release

### April 9, 2024—PhoneOS 3.0(1)

Cisco Desk Phone 9841 and 9851 running PhoneOS 3.0(1) delivers the following features:

Privacy call

Barge

This page includes the features delivered in PhoneOS 4.0 and 4.1 releases. For new and
          enhanced features delivered in PhoneOS 5.0 or later, see the relevant sections in the PhoneOS
            release notes .

See the following table for the features that Cisco Desk Phone 9811 supports on each calling system.

(since 4.0)

(since 4.0)

(since 4.0)

(since 4.0)

- Voice feedback in multiple languages

- Adjustable font size

Known problems (bugs) are graded according to severity. This article contains descriptions of the following:

Open bugs of severity 1 to 3

Resolved bugs of severity 1 to 3

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time new firmware is released.

Before you begin

You need the following to access the Bug Search Tool:

An internet connection

A web browser

A Cisco.com username and password

Open the Bug Search Tool .

Sign in with your Cisco.com username and password.

Enter the bug ID number in the Search for field and press Enter .

What to do next

For information on how to search for bugs, create saved searches, and create bug groups, select Help on the Bug Search Tool page.

Open bugs

### Webex Calling or BroadWorks

The following list contains the severity 1, 2, and 3 defects that are open for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

CSCwv82343, CSCwv82342, CSCwv82344, CSCwv82349: HTTP Proxy Screen Items Cannot Be
            Selected by Pressing Number Key

CSCwv82352, CSCwv82356: Wi-Fi UI Appears Briefly and Disappears During OOB After
            Factory Reset with 802.1X Switch Connection

CSCwv82361: Layout Item Remains Under More Button During Screen Sharing in Meeting

### Unified CM

The following list contains the severity 1, 2, and 3 defects that are open for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

CSCwi76138: Onprem OBTP: Cannot display unicode supplementary characters
              correctly

CSCwq44009: Occasionally phone can‘t recognize the input number or read volume is
              high when voice feedback is enabled

CSCwt58506: The front arc LED and top 360 LED continue to flash even when disabled
              in ring settings or DND scenarios

Resolved bugs

### August 19, 2026 (PhoneOS 5.0.1)

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

Webex Calling or BroadWorks

CSCwt59601: Some language text is truncated on factory reset UI after device
              deletion

CSCwt60046, CSCwt60051: Call icon remains enabled for abbreviated dial when speaker
              is disabled

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

CSCwu65606: 9861 can't show speeddial items beyond phone max lines number

CSCws71475: A beep tone played when making first silent emergency call after phone
              restart

CSCwu65472: 9861/9871 does not refresh MRA token after local router outage for an
              extended period

CSCwu26171: Cisco IP Phone CP-8875 device intermittently drop active call and then
              restart local services due to a crash of the phone media service.

CSCwu49019: 8875 Phone rebooting when making a video call with Third-party SIP
              Device

### May 26, 2026 (PhoneOS 4.1.1SR1)

We resolved the following issue in this release:

CSCwu31461 Video pixelation in MPP 8875 after SSRC change in the received stream

### March 26, 2026 (PhoneOS 4.1.1)

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

Webex Calling or BroadWorks

- CSCwt59601: Some language text is truncated on factory reset UI after device
            deletion

- CSCwt59602, CSCwt59950, CSCwt59969, CSCwt59977: AM/PM indicator is displayed on the
            incorrect side of time for Arabic locale on single-line models

- CSCws74795, CSCws74794, CSCws74793: Join button missing after canceling host PIN
            challenge when joining a calendar meeting

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

CSCws76185: The count of missed calls can be a bit confusing when phone has over 60
            missed calls across multiple lines

### January 20, 2026 (PhoneOS 4.0.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

- CSCws74743, CSCws74747, CSCws74750: Dial assist matches outdated display name in new
            call window, inconsistent with Recents menu

- CSCws74756, CSCws74760, CSCws74786: Booked time slot displays incorrect time after
            reboot due to timezone being ignored

- CSCwr75381, CSCwr75385, CSCwr75389: Voice feedback does not announce "All Lines
            selected" when accessing 'Lines' from the 'Recents' screen

- CSCwr75407, CSCwr75412: Scrolling in "About this device" and "Location" is not smooth;
            right slider size fluctuates

- CSCwr76314, CSCwr76315: Call icon remains green when speakerphone is disabled and
            phone is on-hook

- CSCwr76778, CSCwr76779: Missed call icon does not display when Agent status is
            available

- CSCwr76605, CSCwr76609: Blind transfer via speed dial on page 2 fails with pagination
            enabled

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

- CSCws74539: 98xx phones play beep tone on Call Waiting when using third party headset
            (CFD bug)

- CSCwr96909: Cannot enter phone admin web page if "apply config" from CUCM after
            changing some configuration options

### November 17, 2025 (PhoneOS 3.6.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

- CSCwq49671: Update "LineKeyLabel" only via WxC CH does not take effect for SCA

- CSCwq49676: Status descriptions during meetings are truncated for some languages

- CSCwq49899, CSCwq49905, and CSCwq49911: Voice feedback feature reads theme names in
            English instead of localized language

- CSCwq49927 and CSCwq49933: Voice feedback feature reads UI elements in English instead
            of localized language

- CSCwq49939: "Desk available" string is slightly truncated on DP-9861 device

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

CSCwq44002: Touch phones like 8875, 9871 are unable to hear voice feedback for
              meeting item in Calendar window when meeting backend is Webex

CSCwq44029: Touch phones like 8875/9871 are unable to enter letters in local speed
              dial window

### September 16, 2025 (PhoneOS 3.5.1SR1)

We resolved the following issue in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

CSCwr11741 Phone resyncs multiple times and shows incorrect download status when it
            tries to upgrade to the same image

We resolved the following issue in this release for Cisco Desk Phone 9841 and 9851:

CSCwq96873 Very low possibility, instruction corrupted during loading from DDR

### July 31, 2025 (PhoneOS 3.5.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

- CSCwo89969, CSCwo89972, and CSCwo89973: Line Label Display Incorrect After Phone Bootup When Changes the line label in offline status

- CSCwo90127: The DTMF tone isn't always heard when pressing keys in the IVR

- CSCwo90136, CSCwo90142, and CSCwo90149: The meeting mutes and unmutes several times after pressing the mute hard key to mute it

- CSCwo90378: Softkey Flashing When Dialing with Full Register Setup in SCA

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

- CSCwe04756: Shall not keep in 'Configuring...' page during OOB when phone can't get config files

- CSCwn78309: MRA phone not retry to refresh access token if DNS resolve failed, make phone unregistered

- CSCwo88467: phone not apply the new backgraound image if push with same name as the previous image

- CSCwo88475: Failed to establish Wired / Wireless 802.1x TLS Connection when LSC key size is 512 Bits

### April 29, 2025 (PhoneOS 3.4.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Webex Calling or BroadWorks:

CSCwn78165 and CSCwn78169: Pressing the "Hoteling" causes the phone to reboot if more than 10 lines are enabled with hoteling

- CSCwn78210, CSCwn79724, and CSCwn78218: XSI Failure on DND and Call Forward

- CSCwn78233, CSCwn78236, and CSCwn79725: Call Establishment Failure about 10 minutes after IP Stack Switches to IPv6-Only Mode

- CSCwn78244, CSCwn78249, and CSCwn79726: Setting "Switch Manually" with Long Operation Names in Certain Languages Triggers Reboot Loop

- CSCwn78322 and CSCwn78325: Line Key Unresponsive with Pagination Enabled and KEM Configured but not Attached

- CSCwo66615: Prevent Cisco 8875 phone from crashing when it receives corrupted or faulty H264 RTP packets

- CSCwo27009: 8875 default wallpaper issue after upgrade

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 that are registered to Unified CM:

- CSCwn02578: No Voicefeedback about authentication info on FAC/CMC page

- CSCwn79745: XSI command 'setBackground' execute failed if the 'kem' tag is missed in the xml body

### January 23, 2025 (PhoneOS 3.3.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series that
          are registered to Webex Calling or BroadWorks:

CSCwn04550 and  CSCwn05728: Countdown number briefly changes size and color after pressing action button with voice feedback

CSCwn04797 and CSCwn04794: The "Personal contact" is not fully displayed when font size is set to large

CSCwn04803: No scan list displayed after phone connection failed due to incorrect password input

CSCwn58672: Webui does not display properly from dojo 1.17.3

CSCwn44305: 98xx Webui does not display properly on Touch supported devices

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series that
          are registered to Unified CM:

- CSCwn02762: Phone asks Username/Password again after FIPS is enabled

- CSCwk55531: KEM line and Phone 360 LED are not blinking synchronized

- CSCwk49653: Line 127~130 of KEM cannot dial out or receive a call due to UCM limitation

### October 31, 2024 (PhoneOS 3.2.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series that are
        registered to Webex Calling or BroadWorks:

CSCwk62594: The long email address with long name for the XSI contact is being truncated

CSCwk63378: Meeting counter fails to update when receiving list outside home page

CSCwk62759: WiFi page title updates when switching security mode from 'Auto' to another after selecting an SSID

CSCwk63714 and CSCwk63367: Update Voice VLAN while DHCPv6 service disabled; phone still unregistered after reactivating DHCPv6

CSCwk63695 and CSCwk62828: Pressing 'navigate down' on the last item of the Recents Details page will read the first item

CSCwk63702 and CSCwk62847: Voice feedback does not announce "page 1" or "page 2" as expected on KEM

CSCwk63719 and CSCwk63376: Incorrect pronunciation of "d" and "e" in Voice Feedback

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series that are
        registered to Unified CM:

CSCwk49735：Need to press ’Select’ to wakeup phone since phone back into deep sleep near configured wake up time

CSCwk55555: After Activation Code onboarding, the activated flag in LCD is still white in light mode

CSCwk55576: The line key LED for Hunt group is not cleared when phone is unregistered

CSCwk55583: Voice feedback can't read out the content of Action button guide after Action button config change

CSCwk67177: Cipher Suites and Signature algs should comply with ECC configuration of UCM

CSCwk67185: ECC crypto suites not in TLS client-hello msg when register to SRST

CSCwn00908: Action Button - Long Press+Delay0+SilentEmergencyCall caused Call Looping on receiver phone

CSCwe04762: User cannot connect EAP-TLS from wifi scan list since the security mode always displayed EAP

CSCwf11899: Phone Mute LED is not red after changing audio path from usb-headset to 721 BT headset

CSCwf11900: Sync mute-unmute between MUTE LED and 721 BT headset failed

CSCwi76174: Bluetooth headset will not sync mute status when mute phone via CMS web client

CSCwi76224: "Speed dials" quick access screen overlaps "Upcoming meetings" screen

CSCwn00908: Action Button - Long Press+Delay0+SilentEmergencyCall caused Call Looping on receiver phone

### August 13, 2024 (PhoneOS 3.1.1SR1)

We resolved the following issue in this release for Cisco Desk Phone 9800 Series that are
        registered to Webex Calling, BroadWorks, or Unified CM:

- CSCwm00114 DHCP6: do not send RS during the IPv6 startup phase

### July 15, 2024 (PhoneOS 3.1.1)

Webex Calling or BroadWorks

We resolved the following issues in this release for Cisco Desk Phone 9800 Series that are
        registered to Webex Calling or BroadWorks:

- CSCwj54629 For some call records, unable to favorite it under details window after adding to contact

- CSCwj54635 The speaker LED turns green and the dial tone plays after several off-hook/on-hook cycles

- CSCwj54643 The phrase "All lines" displayed in the 'Recents' is not localized

- CSCwj54585 The prompt toast should be "Upgrade in progress"

- CSCwj66661 The softkey list displays incorrectly after the last contact item is deleted

- CSCwj66706 Missed call notifications display on lines mapped to same extension

- CSCwj66709 The start time and end time for a Webinar meeting are incorrectly displaying as identical

- CSCwj66934 BLF (Busy Lamp Field) names are displayed as language unicode characters

- CSCwj66940 Unable to select the first meeting in the calendar list by pressing the '1' key on the phone

- CSCwj66954 Transaction status is Authenticated when 802.1x is enabled on phone but the authentication times out

- CSCwj66984 "Return to call" string is truncated in certain languages

- CSCwj67105 The resync tag value of Line_label can't be assigned correctly

Unified CM

We resolved the following issues in this release for Cisco Desk Phone 9800 Series that are
        registered to Unified CM:

- CSCwj55473 Phone still shows the IP in network status after power cycle if Disable 802.1x

- CSCwj55483 Incoming call list flashes for a while if end the last hunt group call when another one is waiting

- CSCwj55485 The distance of call sessions on huntgroup with caller name is too close

- CSCwj55490 Phone can't navigate down after subscribing two services

- CSCwj55491 Phone Informacast paging server auth failed

- CSCwj55493 Phone popups an overcurrent toast when connecting 980/700 series to side USB port

- CSCwj55495 The incoming call in call list displays abnormal for single line

### April 9, 2024 (PhoneOS 3.0.1)

This version PHONEOS.3-0-1-0001 is the initial release and has no resolved bugs.

## Installation requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device package. For more information about how to install a Unified CM device package, see Cisco Unified Communications Manager Device Package Installation Guide .

If your Cisco Unified Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

Install the firmware on Cisco Unified Communications Manager

Before using the phone firmware release, you must install the latest Cisco Unified Communications Manager on all Cisco Unified CM servers in the cluster.

Go to the Software Download for IP Phones .

Do one of the following actions:

- Choose Desk Phone 9800 Series , and then choose your phone model.

- Choose IP Phone 8800 Series > Video Phone 8875 .

Choose Session Initiation Protocol (SIP) Software , if prompted.

In the Latest Release folder, choose 5.0(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts:

The firmware filename is cmterm-PHONEOS.5-0-1-0005-62.cop.sha512

If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All .

Click the + next to the firmware file name in the Download Cart section to access more information about this file.

Click the Readme link to open the installation instructions for the firmware.

Follow the instructions in the readme file to install the firmware.

Install the firmware Zip files

If a Cisco Unified Communications Manager is not available to load the installer program,
        the following .zip files are available to load the firmware: cmterm-PHONEOS.5-0-1-0005-62.zip.

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the Software Download for IP Phones .

Do one of the following actions:

- Choose Desk Phone 9800 Series , and then choose your phone model.

- Choose IP Phone 8800 Series > Video Phone 8875 .

Choose Session Initiation Protocol (SIP) Software , if prompted.

In the Latest Release folder, choose 5.0(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts:

The firmware filename is cmterm-PHONEOS.5-0-1-0005-62.zip

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server.

Unified Communications Manager Endpoints Locale Installer

By default, your phones are set up for the English (United States) locale. To use the phones in other locales, you must install the locale-specific version of the Unified Communications Manager Endpoints Locale Installer on every Cisco Unified Communications Manager server in the cluster. The Locale Installer installs the latest translated text for the phone user interface and country-specific phone tones on your system so that they are available for the Phones.

To access the Locale Installer required for a release, access the Software Download page, navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

The latest Locale Installer may not be immediately available; continue to check the website for updates.

Download the firmware file from cisco.com and then install the firmware with the phone administration web page or using the command in your web browser.

Download the firmware file

Before you begin

Obtain your username and password for cisco.com. Firmware downloading requires you to log in to cisco.com.

Do one of the following actions:

- For Desk Phone 9800 Series, go to https://software.cisco.com/download/home/286037605 , choose Desk Phone 9800 Series , and then your phone model.

- For Video Phone 8875, go to https://software.cisco.com/download/home/284729655 , and then choose Video Phone 8875 .

Choose Session Initiation Protocol (SIP) Software , if prompted.

In the Latest Release folder, choose 5.0(1) .

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the firmware file PHONEOS.5-0-1-0005-62.zip.

What to do next

Unzip the .zip file that you downloaded from cisco.com and place the files in the appropriate location on your upgrade server.

Upgrade the firmware on the phone web page

Before you begin

Unzip the .zip file that you downloaded from cisco.com and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade.

Log in to the phone administration web page.

Example: http://10.74.10.225/admin/advanced

Go to Voice > Provisioning .

In the Firmware Upgrade section, enter the load URL in the Upgrade Rule .

Follow this format when you enter the load file URL:

```
<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads
```

Examples:

Click Submit All Changes .

Upgrade the firmware with your web browser

Before you begin

Unzip the .zip file that you downloaded from cisco.com and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade.

In the address bar of your web browser, enter the phone upgrade URL in the following format:

```
<phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL>
```

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/ PHONEOS.5-0-1-0005-62 .loads

Specify the .loads file in the URL. The .zip file contains other files.

Phone behavior during times of network congestion

Anything that degrades network performance can affect phone audio and video quality, and in
        some cases, can cause a call to drop. Sources of network degradation can include, but are
        not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

Health-care environment use

This product is not a medical device and uses an unlicensed frequency band that is susceptible to interference from other devices or equipment.

On-hook transfer limitation in SIP phones

When the Cisco Unified Communications Manager Transfer On-Hook Enabled field is enabled, users might report a problem with direct call transfer in SIP phones. If the user transfers the call and immediately goes on hook before they hear the ring signal, the call may drop instead of being transferred.

The user needs to hear the ring signal so that they can be sure that the call is being routed.

Use the following sections to obtain related information.

## Cisco PhoneOS Phones (9800/8875) documentation

See the help information for Cisco Desk Phone 9800 Series on the help page .

See the help information for Cisco Video Phone 8875 on the help page .

## Cisco Unified Communications Manager Documentation

See the Cisco Unified Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified Communications Manager release on the product support page.

## Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Phone | Platform | Support requirements |
|---|---|---|
| Cisco Desk Phone 9800 Series Cisco Video Phone 8875 | Cisco BroadWorks | Cisco BroadWorks 24.0 or later |
| Cisco Unified Communications Manager | Cisco Unified Communications Manager 12.5(1) or later Note :  On PhoneOS 3.2 and later, features delivered in UCM Device
                  Packages require UCM 14 or 15. On PhoneOS 5.0, they require UCM 15. Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) or later Cisco Expressway 12.5.4 or later |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Calling |
| Support more line keys on 8875 and 9871 | ✓ | ✓ |  |
| Customization |
| Custom ringtones | ✓ | ✓ | ✓ (since 3.0) |
| User experience
                enhancements |
| Quick access to speed dials during conference and transfer | ✓ | ✓ | ✓ |
| Updates for programmable softkeys | ✓ | ✓ |  |
| Conference participants list | ✓ | ✓ | ✓ (since 3.0) |
| Enhancements for the Select key | ✓ (since 4.1) | ✓ (since 4.1) | ✓ |
| Acoustic shock protection | ✓ | ✓ | ✓ |
| Serviceability |
| ThousandEyes integration on Cisco Video Phone 8875 | ✓ |  | ✓ |
| Deployment |
| Update for 9841NR and 9851NR deployment on UCM |  |  | ✓ |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Calling features |
| Abbreviated dials | ✓ | ✓ | ✓ |
| Private Line Automatic Ringdown (PLAR) | ✓ (since 3.0) | ✓ (since 3.0) | ✓ |
| Customization features |
| Minimum ringer volume enforcement |  |  | ✓ |
| Manage phone with TR-069 settings |  | ✓ |  |
| More configurations available in Control Hub | ✓ |  |  |
| Media quality |
| MARI and FEC for media quality | ✓ (since 3.0) | ✓ (since 3.0) | ✓ |
| User experience
                enhancements |
| Option to postpone software upgrades | ✓ (since 3.0) | ✓ (since 3.0) | ✓ |
| Out-of-Box setup process enhancement |  |  | ✓ |
| Quick access with Up and Down navigation keys | ✓ | ✓ | ✓ |
| Enhancements for the Select key | ✓ | ✓ |  |
| Enhanced LED notifications in Display Off mode | ✓ | ✓ | ✓ |
| Visual notification for Group Call Pickup | ✓ |  |  |
| Serviceability |
| Device status visibility in Control Hub | ✓ |  |  |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| New device |
| Cisco Desk Phone 9811 | ✓ | ✓ | ✓ |
| Calling features |
| Feature Line keys improvement |  |  | ✓ |
| Report a malicious
                  call |  |  | ✓ |
| Conference/transfer with on-hold calls | ✓ | ✓ | ✓ (since 3.1.1) |
| User experience enhancements |
| User access improvement to the Settings menu |  |  | ✓ |
| Security |
| E911 service control |  |  | ✓ |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Calling features |
| Disable speakerphone | ✓ | ✓ | ✓ (since 3.2.1) |
| Reverse name lookup for Webex Personal Contacts | ✓ |  |  |
| Webex companion (Unified CM) (for 9800 Series only) |  |  | ✓ |
| Move call to phone | ✓ | ✓ |  |
| Customization features |
| Support for CiscoIPPhoneStatus XML object (for 9851, 9861, 9871, and
                  8875) | ✓ (since 3.2.1) | ✓ (since 3.2.1) | ✓ |
| XSI call logs |  | ✓ |  |
| Accessibility features |
| Cloud-assisted transcription in calls (for
                  9861, 9871, and 8875) | ✓ |  |  |
| User experience enhancements |
| User experience improvement on Webex Meeting PIN challenge | ✓ |  |  |
| Optimized directory search performance |  | ✓ |  |
| Enhancements for Hot Desking | ✓ |  |  |
| Serviceability |
| xAPI updates | ✓ | ✓ | ✓ |
| Security |
| Display LLDP-MED TLV location information on your phone |  |  |  |
| 802.1x Custom Device Certificate (CDC) enhancement | ✓ | ✓ |  |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Calling features |
| Customizable New call softkey for connected call state |  |  | ✓ |
| Individual Queue Login | ✓ |  |  |
| Customization features |
| Multiple appearances support for line key labels | ✓ |  |  |
| Cisco Smart Power Framework | ✓ | ✓ | ✓ |
| Settings menu customization | ✓ | ✓ |  |
| Accessibility features |
| Accessibility voice feedback for multi-languages | ✓ | ✓ | ✓ |
| User experience enhancements |
| Always use multi-line mode | ✓ | ✓ | ✓ |
| Serviceability |
| Diagnostics info on Control Hub | ✓ |  |  |
| Remote factory reset | ✓ (since 3.0.1) | ✓ (since 3.0.1) | ✓ |
| xAPI | ✓ | ✓ | ✓ |
| Security |
| Common Name configuration for CDC User ID configuration for wired 802.1X | ✓ | ✓ |  |
| ✓ | ✓ |  |
| FIPS 140-3 compliance | ✓ | ✓ | ✓ |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Onboarding |
| NFC onboarding enhancements (for 9800 only) | ✓ | ✓ | ✓ |
| User settings preservation | ✓ | ✓ |  |
| Calling features |
| Group call pickup notifications | ✓ |  |  |
| Cloud feature |
| Hot Desking enhancements | ✓ |  |  |
| Meeting features |
| Webex account login for calendar meeting |  |  | ✓ |
| Webex companion meeting (for 9800 only) | ✓ |  |  |
| Webex in-meeting summary (for 9861/9871/8875 only) | ✓ |  |  |
| Customization features |
| Configurable line key labels | ✓ |  |  |
| New settings for the Action button (for 9800 only) | ✓ | ✓ | ✓ |
| User experience enhancements |
| Inline call label or session (for 9841/9851/9861 only) | ✓ | ✓ |  |
| Sustainability |
| A new parameter for power saving (Office Hours) | ✓ | ✓ | ✓ |
| Security |
| Multilevel Precedence and Preemption (MLPP) improvement |  |  | ✓ |
| TLS 1.3 support | ✓ | ✓ | ✓ (since 3.2.1) |
| Backward compatibility with WPA (for 9861/9871/8875 only) | ✓ | ✓ | ✓ |
| Configuration management |
| Migration of 8875 settings (for 8875 only) | ✓ |  |  |
| Unified Communications (UC) |
| Cisco Unified Mobility |  |  | ✓ |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Onboarding |
| NFC onboarding | Yes | Yes | Yes |
| Call features |
| Cisco IP Manager Assistant | No | No | Yes |
| Switch the operating mode | Yes | No | No |
| Cloud feature |
| Faster Hot Desking sign-in | Yes | No | No |
| Meeting features |
| In-meeting transcription (for 9861/9871) | Yes | No | No |
| Teams meeting support | Yes | No | Yes (already supported in 3.1.1) |
| Customization features |
| Action button (multiple triggers and HTTP post) | Yes | Yes | Yes |
| Add speed dials locally (for 9871) | No | No | Yes |
| Custom wallpaper and logo (for 9851/9861/9871) | Yes | Yes | Yes (already supported in 3.0.1) |
| Custom wallpaper setting by XML files | No | No | Yes |
| New supported languages | Yes | Yes | Yes |
| User experience enhancements |
| Pagination on Cisco Desk Phone (for 9851/9861) | Yes | Yes | No |
| User Preference Attribute | Yes | Yes | NA |
| Serviceability |
| Headset upgrade on phone | Yes | Yes | Yes |
| Phone reports in Control Hub | Yes | No | No |
| Security |
| Device security insights | Yes | Yes | No |
| HTTP proxy | Yes | Yes | No |
| VPN | No | No | Yes |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Onboarding |
| MRA onboarding with domain service | No | No | Yes |
| User credentials persistent for Expressway sign-in | No | No | Yes |
| Calling features |
| Forced Authorization Code (FAC) and Client Matter Code (CMC) | No | No | Yes |
| Multicast Paging Multicast Paging with XML Application Support | Yes | Yes | No |
| Support for Call center agent's phone | Yes | Yes | No |
| Switch for UDS directory service on Unified CM | No | No | Yes |
| Top 360 and Front Arc LED for voicemails and missed calls | Yes | Yes | Yes |
| Cloud features |
| Hot Desking sign-in and booking management | Yes | No | No |
| Meeting features |
| Mute status sync in hybrid meeting | Yes | No | No |
| Recoding indication in meeting | Yes | No | No |
| Participant list | Yes | No | No |
| Customization features |
| Action button supports for custom services | Yes | Yes | Yes |
| More display languages on the phone | Yes | Yes | Yes |
| Support for XML applications on phones on BroadWorks | No | Yes | No |
| Accessibility features |
| Voice feedback (in English) | Yes | Yes | Yes |
| Adjustable font size on phone screen | Yes | Yes | Yes |
| Accessories supports |
| Cisco Headset USB-C Adapter support | Yes | Yes | Yes |
| Serviceability |
| ThousandEyes integration | Yes | No | Yes |
| Sustainability |
| New parameters for Office Hours | Yes | Yes | Yes |
| Survivability |
| WxC outbound proxy survivability support | Yes | Yes | No |
| Security |
| Assured Services SIP (AS-SIP) | No | No | Yes |
| Certificate Authority Proxy Function (CAPF) with Elliptical Curve (EC) key
                support | No | No | Yes |
| Custom Device Certificate on 802.1x | Yes | Yes | No |
| Disabling speakerphone, headset, and handset | No | No | Yes |
| Multilevel Precedence and Preemption (MLPP) | No | No | Yes |
| Multi-server (SAN) Tomcat Certificate with Cisco UCM | No | No | Yes |
| No password warning | Yes | Yes | No |
| TLS client/server min version | No | No | Yes |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Onboarding |
| Activation code onboarding | Yes | Yes | Yes |
| Calling features |
| Conference/transfer with on-hold calls | No | No | Yes |
| Call back | No | No | Yes |
| Noise removal support for incoming audio (for 9861/9871) | Yes | Yes | Yes |
| Narrowband-to-wideband audio enhancement by AI (for 9861/9871) | Yes | Yes | Yes |
| Cloud features |
| Calendar | Yes | No | Yes |
| One button to push (OBTP) | Yes | No | Yes |
| Accessibility feature |
| Voice feedback (for 9841/9851/9861) | Yes | Yes | Yes |
| Wireless supports |
| Bluetooth (for 9861/9871) | Yes | Yes | Yes |
| Wi-Fi (for 9861/9871) | Yes | Yes | Yes |
| Accessories supports |
| Bluetooth headset (for 9861/9871) | Yes | Yes | Yes |
| Key Expansion Module (for 9851/9861/9871) | Yes | Yes | Yes |
| KEM firmware upgrade | Yes | Yes | Yes |
| KEM intercom | No | No | Yes |
| KEM PLK | Yes | Yes | Yes |
| KEM brightness | Yes | Yes | Yes |
| KEM wallpaper | Yes | Yes | Yes |
| KEM PRT | Yes | Yes | Yes |
| Security |
| TLS 1.3 for UCM | No | No | Yes |

| Feature name | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Activation code onboarding | No | No | Yes |
| Action button | Yes | Yes | Yes |
| Adjustable display brightness | Yes | Yes | Yes |
| Adjustable ringtones and volume levels | Yes | Yes | Yes |
| SRST/MRA | No | No | Yes |
| Calendar button (for 9851/9861) | Yes | Yes | Yes |
| Custom wallpaper and logo (for 9851/9861/9871) | No | No | Yes |
| E911 | Yes | Yes | Yes |
| Extension mobility | No | No | Yes |
| Help desk (Favorite button) | Yes | Yes | Yes |
| Local factory reset, restart | Yes | Yes | Yes |
| Multiple languages support | Yes | Yes | Yes |
| Native phone migration | No | No | Yes |
| Password lock for settings menu | No | No | Yes |
| Peer firmware sharing | Yes | Yes | Yes |
| Problem report tool (local and remote) | Yes | Yes | Yes |
| System wallpaper (for 9851/9861/9871) | Yes | Yes | Yes |
| Time and date display | Yes | Yes | Yes |
| Network |
| Network traverse ICE | Yes | Yes | No |
| Network traverse NAT | Yes | Yes | No |
| Network traverse STUN | Yes | Yes | No |
| 802.1x | Yes | Yes | Yes |
| Calling features |
| Ad-hoc conference | Yes | Yes | Yes |
| Audio mute/unmute | Yes | Yes | Yes |
| Noise removal for microphone audio | Yes | Yes | Yes |
| Basic call | Yes | Yes | Yes |
| BLF call park | Yes | Yes | No |
| BLF with call pickup | Yes | Yes | No |
| BLF with speed dial | Yes | Yes | Yes |
| BLF with speed dial and call pickup | Yes | Yes | Yes |
| CBarge | No | No | Yes |
| Caller ID | Yes | Yes | Yes |
| Call forward | Yes | Yes | Yes |
| Call hold/resume | Yes | Yes | Yes |
| Call park | Yes | Yes | Yes |
| Call pickup | Yes | Yes | Yes |
| Call preservation mode | No | No | Yes |
| Call recording | Yes | Yes | Yes |
| Call waiting | Yes | Yes | Yes |
| Cisco meeting server mute sync | No | No | Yes |
| Conference participant list | No | No | Yes |
| Confidential access level (CAL) | No | No | Yes |
| Contacts | Yes | Yes | Yes |
| Dial rules | Yes | Yes | Yes |
| Directory search | Yes | Yes | Yes |
| Do not disturb | Yes | Yes | Yes |
| E.164/Plus Dialing | Yes | Yes | Yes |
| Feature access code | Yes | Yes | No |
| Flexible seating | No | Yes | No |
| Group pickup | Yes | Yes | Yes |
| Hold/Park Reversion | No | No | Yes |
| Hotline | Yes | Yes | No |
| Hoteling | Yes | Yes | No |
| Hunt group | Yes | Yes | Yes |
| Intercom | No | No | Yes |
| Meet me | No | Yes | Yes |
| Multiple calls | Yes | Yes | Yes |
| Native call queue status | No | No | Yes |
| Other pickup | No | No | Yes |
| Private Line Automatic Ringdown (PLAR) | Yes | Yes | No |
| Programmable line key (PLK) and softkey | Yes | Yes | Yes |
| Programmable Softkey (PSK) customization | Yes | Yes | No |
| Recents (call history) | Yes | Yes | Yes |
| Redial | Yes | Yes | Yes |
| Reverse phone lookup service | Yes | Yes | No |
| Shared line Privacy call Barge | Yes | Yes | Yes |
| Speed dial | Yes | Yes | Yes |
| Transfer | Yes | Yes | Yes |
| Uniform Resources Identifier (URI) dialing | Yes | Yes | Yes |
| Voicemail | Yes | Yes | Yes |
| Cloud features |
| Call log | Yes | No | No |
| Hot desking | Yes | No | No |
| MARI and FEC for media quality | Yes | Yes | No |
| Meeting calendar | Yes | No | No |
| One button to push (OBTP) | Yes | No | No |
| Remote reboot and factory reset | Yes | Yes | No |
| Webex hybrid meeting | Yes | No | No |
| Serviceability maintenance |
| Firmware upgrade | Yes | Yes | Yes |
| Sustainability |
| Carbon emissions insights | Yes | No | No |
| EnergyStar | Yes | Yes | Yes |
| Office hour (display off and deep sleep) | Yes | Yes | Yes |
| Security |
| Media plane security negotiations | Yes | Yes | No |

| Feature | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| Abbreviated dials | ✓ | ✓ | ✓ |
| Private Line Automatic Ringdown (PLAR) | ✓ (since 4.0) | ✓ (since 4.0) | ✓ |
| Minimum ringer volume |  |  | ✓ |
| Manage phone with TR-069 settings |  | ✓ |  |
| More configurations in Control Hub | ✓ |  |  |
| MARI and FEC for media quality | ✓ | ✓ | ✓ |
| Option to postpone software upgrades | ✓ | ✓ | ✓ (since 4.0) |
| Out-of-Box setup process enhancement |  |  | ✓ |
| Quick access with Up and Down navigation keys | ✓ | ✓ | ✓ |
| Enhancements for the Select key | ✓ | ✓ |  |
| Enhanced LED notifications in Display Off mode | ✓ | ✓ | ✓ |
| Visual notification for group call pickup | ✓ | ✓ |  |
| Device status display in Control Hub | ✓ |  |  |
| Disable speakerphone | ✓ | ✓ | ✓ (since 4.0) |
| Individual call queue | ✓ |  |  |
| LLDP-MED TLV location information on phone | ✓ | ✓ |  |
| Move call between devices | ✓ |  |  |
| Silent monitoring for the Contact Center solution |  |  | ✓ |
| xAPI support | ✓ | ✓ | ✓ |

| Feature | Webex Calling | BroadWorks | Unified CM |
|---|---|---|---|
| 802.1x | ✓ | ✓ | ✓ |
| Accessibility features Voice feedback in multiple languages Adjustable font size | ✓ | ✓ | ✓ |
| Action button | ✓ | ✓ | ✓ |
| Activation code onboarding | ✓ | ✓ | ✓ |
| Ad-hoc conference | ✓ | ✓ | ✓ |
| Adjustable ringtones and volume levels | ✓ | ✓ | ✓ |
| Always use multi-line mode | ✓ | ✓ | ✓ |
| Assured Services SIP (AS-SIP) |  |  | ✓ |
| Audio mute/unmute | ✓ | ✓ | ✓ |
| Barge | ✓ | ✓ | ✓ |
| Basic call | ✓ | ✓ | ✓ |
| BLF call park | ✓ | ✓ | ✓ |
| BLF with call pickup | ✓ | ✓ | ✓ |
| BLF with speed dial | ✓ | ✓ | ✓ |
| BLF with speed dial and call pickup | ✓ | ✓ | ✓ |
| Call back |  |  | ✓ |
| Call forward | ✓ | ✓ | ✓ |
| Call hold/resume | ✓ | ✓ | ✓ |
| Call index enhancement | ✓ | ✓ | ✓ |
| Call park | ✓ | ✓ | ✓ |
| Call pickup | ✓ | ✓ | ✓ |
| Call preservation mode |  |  | ✓ |
| Call recording | ✓ | ✓ | ✓ |
| Call waiting | ✓ | ✓ | ✓ |
| Caller ID | ✓ | ✓ | ✓ |
| Carbon emissions insights | ✓ |  |  |
| CBarge |  |  | ✓ |
| Certificate Authority Proxy Function (CAPF) with Elliptical Curve (EC) key
                support |  |  | ✓ |
| Cisco IP Manager Assistant |  |  | ✓ |
| Cisco meeting server mute sync |  |  | ✓ |
| Cisco Smart Power Framework | ✓ | ✓ | ✓ |
| Cisco Unified Mobility |  |  | ✓ |
| Cloud call log | ✓ |  |  |
| Conference participant list |  |  | ✓ |
| Conference/Transfer with active calls | ✓ | ✓ | ✓ |
| Confidential access level (CAL) |  |  | ✓ |
| Configurable line key labels | ✓ | ✓ | ✓ |
| Contacts | ✓ | ✓ | ✓ |
| Custom Device Certificate on 802.1x | ✓ | ✓ |  |
| Customizable New call softkey for connected call state |  |  | ✓ |
| Device security insights | ✓ | ✓ |  |
| Dial rules | ✓ | ✓ | ✓ |
| Directory search | ✓ | ✓ | ✓ |
| Disabling speakerphone, headset, and handset |  |  | ✓ |
| Do not disturb | ✓ | ✓ | ✓ |
| E.164/Plus Dialing | ✓ | ✓ | ✓ |
| E911 | ✓ | ✓ | ✓ |
| EnergyStar | ✓ | ✓ | ✓ |
| Extension mobility |  |  | ✓ |
| Feature access code | ✓ | ✓ |  |
| Firmware upgrade | ✓ | ✓ | ✓ |
| Flexible seating |  | ✓ |  |
| Forced Authorization Code (FAC) and Client Matter Code (CMC) |  |  | ✓ |
| Front Arc LED for voicemails and missed calls | ✓ | ✓ | ✓ |
| Group pickup | ✓ | ✓ | ✓ |
| Help desk (Favorite button) | ✓ | ✓ | ✓ |
| Hold/Park Reversion |  |  | ✓ |
| Hoteling | ✓ | ✓ |  |
| Hotline | ✓ | ✓ |  |
| HTTP proxy | ✓ | ✓ |  |
| Hunt group | ✓ | ✓ | ✓ |
| Inline call label or session | ✓ | ✓ |  |
| Intercom |  |  | ✓ |
| Local factory reset, restart | ✓ | ✓ | ✓ |
| Media plane security negotiations | ✓ | ✓ |  |
| Meet me |  | ✓ | ✓ |
| MRA onboarding with domain service |  |  | ✓ |
| Multiple appearances support for line key labels | ✓ |  |  |
| Multicast Paging | ✓ | ✓ | ✓ |
| Multilevel Precedence and Preemption (MLPP) |  |  | ✓ |
| Multiple calls | ✓ | ✓ | ✓ |
| Multiple languages support | ✓ | ✓ | ✓ |
| Multi-server (SAN) Tomcat Certificate with Cisco UCM |  |  | ✓ |
| Native call queue status |  |  | ✓ |
| Native phone migration |  |  | ✓ |
| Network traverse ICE/NAT/STUN | ✓ | ✓ |  |
| Option to postpone software upgrades |  |  | ✓ |
| Other pickup |  |  | ✓ |
| Password warning | ✓ | ✓ |  |
| Password lock for settings menu |  |  | ✓ |
| Peer firmware sharing | ✓ | ✓ | ✓ |
| Phone reports and analytics in Control Hub | ✓ |  |  |
| Private Line Automatic Ringdown (PLAR) | ✓ | ✓ |  |
| Privacy call |  |  | ✓ |
| Problem report tool (local and remote) | ✓ | ✓ | ✓ |
| Programmable line key (PLK) and softkey | ✓ | ✓ | ✓ |
| Programmable Softkey (PSK) customization | ✓ | ✓ |  |
| Recents (call history) | ✓ | ✓ | ✓ |
| Redial | ✓ | ✓ | ✓ |
| Remote factory reset | ✓ | ✓ | ✓ |
| Remote reboot and factory reset | ✓ | ✓ |  |
| Reverse phone lookup service | ✓ | ✓ |  |
| RJ-9 headset | ✓ | ✓ | ✓ |
| Settings menu customization | ✓ | ✓ |  |
| Shared line | ✓ | ✓ | ✓ |
| Speed dial | ✓ | ✓ | ✓ |
| SRST/CME |  |  | ✓ |
| Support for Call center agent's phone | ✓ | ✓ |  |
| Switch for UDS directory service on Unified CM |  |  | ✓ |
| Time and date display | ✓ | ✓ | ✓ |
| TLS 1.3 support | ✓ | ✓ | ✓ |
| TLS client/server min version |  |  | ✓ |
| Transfer | ✓ | ✓ | ✓ |
| Uniform Resources Identifier (URI) dialing | ✓ | ✓ | ✓ |
| User credentials persistent for Expressway sign-in |  |  | ✓ |
| Voicemail | ✓ | ✓ | ✓ |
| WxC outbound proxy survivability support | ✓ | ✓ |  |
| XML applications | ✓ | ✓ | ✓ |
| XSI call log | ✓ | ✓ |  |

| 1 | Open the Bug Search Tool . |
|---|---|
| 2 | Sign in with your Cisco.com username and password. |
| 3 | Enter the bug ID number in the Search for field and press Enter . |

| 1 | Go to the Software Download for IP Phones . |
|---|---|
| 2 | Do one of the following actions: Choose Desk Phone 9800 Series , and then choose your phone model. Choose IP Phone 8800 Series > Video Phone 8875 . |
| 3 | Choose Session Initiation Protocol (SIP) Software , if prompted. |
| 4 | In the Latest Release folder, choose 5.0(1) . |
| 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: The firmware filename is cmterm-PHONEOS.5-0-1-0005-62.cop.sha512 If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| 6 | Click the + next to the firmware file name in the Download Cart section to access more information about this file. |
| 7 | Click the Readme link to open the installation instructions for the firmware. |
| 8 | Follow the instructions in the readme file to install the firmware. |

| 1 | Go to the Software Download for IP Phones . |
|---|---|
| 2 | Do one of the following actions: Choose Desk Phone 9800 Series , and then choose your phone model. Choose IP Phone 8800 Series > Video Phone 8875 . |
| 3 | Choose Session Initiation Protocol (SIP) Software , if prompted. |
| 4 | In the Latest Release folder, choose 5.0(1) . |
| 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: The firmware filename is cmterm-PHONEOS.5-0-1-0005-62.zip |
| 6 | Unzip the files. |
| 7 | Manually copy the unzipped files to the directory on the TFTP server. |

| 1 | Do one of the following actions: For Desk Phone 9800 Series, go to https://software.cisco.com/download/home/286037605 , choose Desk Phone 9800 Series , and then your phone model. For Video Phone 8875, go to https://software.cisco.com/download/home/284729655 , and then choose Video Phone 8875 . |
|---|---|
| 2 | Choose Session Initiation Protocol (SIP) Software , if prompted. |
| 3 | In the Latest Release folder, choose 5.0(1) . |
| 4 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| 5 | Download the firmware file PHONEOS.5-0-1-0005-62.zip. |

| 1 | Log in to the phone administration web page. The URL for your phone web page is http://<phone IP address>/admin/advanced . Example: http://10.74.10.225/admin/advanced |
|---|---|
| 2 | Go to Voice > Provisioning . |
| 3 | In the Firmware Upgrade section, enter the load URL in the Upgrade Rule . Follow this format when you enter the load file URL: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/ PHONEOS.5-0-1-0005-62 .loads |
| 4 | Click Submit All Changes . |

| In the address bar of your web browser, enter the phone upgrade URL in the following format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/ PHONEOS.5-0-1-0005-62 .loads Specify the .loads file in the URL. The .zip file contains other files. |
|---|