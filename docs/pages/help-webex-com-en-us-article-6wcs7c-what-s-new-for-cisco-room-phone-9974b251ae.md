---
doc_id: help-webex-com-en-us-article-6wcs7c-what-s-new-for-cisco-room-phone-9974b251ae
source_url: https://help.webex.com/en-us/article/6wcs7c/What's-New-for-Cisco-Room-Phone
retrieved_at: 2026-09-07T15:42:37.959881+00:00
---

Use the information in the following article to learn
                        about new features and planned releases. We update the article whenever we
                        have news to announce.

You can subscribe to this article to get updates on any
                        changes.

- What's New

- Coming Soon

- Earlier Releases

## December 14, 2022

Firmware Release 1.2(0)SR3 applies to Cisco Unified Communications Manager (Unified CM) Calling and Unified CM Calling with Control Hub.

This release addresses caveat fixes. It doesn't contain any new or updated features.

Download and install the firmware from the Software Download page . Follow the prompts for cmterm-RoomPhone.1.2.0301-6205418351.k4.cop.sgn or cmterm-RoomPhone.1.2.0301-6205418351.zip .

For firmware installation instructions, see the Administration Guide for Cisco Unified Communications Manager for your Unified CM version.

Caveats

The following list contains the snapshot of severity 1, 2, and 3 caveats that are resolved for the Cisco Room Phone:

CSCwb22136 Webex Room Phone Memory Leak Issue

CSCwb20807 Webex Room Phone Contrast and Color-space issues during content sharing

CSCwd50973 Vulnerabilities that affect the third-party software components (CVE-2022-0563)

- CSCwd50971 Vulnerabilities that affect the third-party software components (CVE-2022-25255)

- CSCwb77790 Upgrade libexpat (CVE-2022-23852 and CVE-2022-23990)

- CSCwa74714 Webex Room Phone pick 1080p resolution with 60Hz only

- CSCwa68293 Change URL from devices.webex.com to share.webex.com

- CSCwd51118 CIAM c-ares 1.16.1 (CVE-2021-3672)

We'll update this article whenever we have news about
                        features that are coming out soon. Keep in mind that we might need to make
                        changes to release dates and the features themselves.

You can subscribe to this article to get updates on any
                        changes.

## January 7, 2022

Firmware Release 1.2(0)SR2 applies to Cisco Unified Communications Manager (Unified CM) Calling and Unified CM Calling with Control Hub.

This release addresses caveat fixes. It doesn't contain any new or updated features.

Download and install the firmware from the Software Download page . Follow the prompts for cmterm-RoomPhone.1.2.0201-4c142f8f2f.k4.cop.sha512 or cmterm-RoomPhone.1.2.0201-4c142f8f2f.zip.

For firmware installation instructions, see the Administration Guide for Cisco Unified Communications Manager for your Unified CM version.

Caveats

The following list contains the snapshot of severity 1, 2, and 3 caveats that are open for the Cisco Room Phone:

CSCvw99372 - Webex Room Phone: Calls Drop Randomly When On-Prem User Shares High Frame Rate Presentation.

The following list contains the snapshot of severity 1, 2, and 3 caveats that are resolved for the Cisco Room Phone:

CSCwa24255 - Update CA bundles Trusted Root Release for the Webex Room Phone.

## August 25, 2021

Firmware Release 1.2(0)SR1 applies to Cisco Unified Communications Manager (Unified CM) Calling and Unified CM Calling with Control Hub.

This release improves security on the Cisco Room Phone. For more information, see the following Cisco Security Advisories:

CSCvx89821: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-wifi-faf-22epcEWu.html

CSCvx84328: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-openssl-2021-GHY28dJd.html

CSCvv87082: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-dnsmasq-dns-2021-c5mrdf3g.html

Download and install Firmware Release 1.2(0) from the Software Download page . Follow the prompts for cmterm-RoomPhone.1.2.0-9d78b5079a.k4.cop.sha512 or RoomPhone.1.2.0-9d78b5079a.zip.

For firmware installation instructions, see the Administration Guide for Cisco Unified Communications Manager for your Unified CM version.

## January 15, 2021

The following sections describe the features that are new or have changed in Firmware Release 1.2(0) for Cisco Unified Communications Manager (Unified CM) Calling and Unified CM Calling with Control Hub.

Download and install Firmware Release 1.2(0) from the Software Download page . Follow the prompts for cmterm-RoomPhone.1.2.0-0f6c2a1678.k3.cop.sgn.

For firmware installation instructions, see the Administration Guide for Cisco Unified Communications Manager for your Unified CM version.

Support for Cable Sharing on Cisco Unified Communications Manager

Cable sharing is now available during calls and Webex meetings on Cisco Unified Communications Manager (Unified CM) Calling and Unified CM Calling with Control Hub. Previously, Unified CM Calling with Control Hub only supported Cable sharing during meetings.

Users connect the Cisco Room Phone to their computer and HDMI screen with the included HDMI cables. For more information, see Share Information and the Webex Room Phone .

This feature doesn't require any configuration. But you need the appropriate routing to Webex.

Support for Join Webex on Cisco Unified Communications Manager

Join Webex is now available for Cisco Unified Communications Manager (Unified CM) Calling. This feature makes it easier for Unified CM Calling users to collaborate with their colleagues.

You don't configure any parameters for this feature. But confirm that the routing is in place so the call goes to Webex. To join a meeting, users tap Join Webex and enter the meeting number, which is in the meeting invitation.

For more information, see Join Meetings from Your Webex Room Phone .

Caveats

The following list contains severity 1-3 defects that are open for the Cisco Room Phone for Firmware Release 1.2(0):

CSCvw99372 Webex Room Phone: Calls Drop Randomly When On-Prem User Shares High Frame Rate Presentation

The following list contains the severity 1-3 defects that are resolved for the Cisco Room Phone for Firmware Release 1.2(0):

CSCvw99378 Webex Room Phone: Fails To Register with UCM If Elliptical Curve Security Enabled

CSCvw99379 Webex Room Phone: “TFTP Encrypted Config” in the Device Security Profile should Not Be Shown

## December 15, 2020

The following sections describe the features that are new or have changed for Webex Calling with Control Hub.

Standby Mode

Your phone now enters Standby mode when you haven't used it for several minutes. This feature reduces your energy
				consumption.

Configure this feature with the Standby mode parameters on Control Hub.

For more information, see the following articles:

"Phone Modes" tab on the Your Cisco Webex Room Phone article at https://help.webex.com/en-us/1ois7l/Your-Cisco-Webex-Room-Phone .

"Cisco Webex Control Hub Parameters" tab on the Add Features to Cisco
							Webex Room Phone article at https://help.webex.com/en-us/nz3l3sm/Add-Features-to-Cisco-Webex-Room-Phone .

Lock Device Settings

Administrators can lock the following phone settings so that users can't modify
				them:

Language

Time zone

Device activation

Network connection

Reset

Parameters lock as a group. You cannot lock individual settings. A hard factory reset unlocks the phone settings.

For more information, see the "Lock Your Device Settings" tab on the Add Features
					to Cisco Webex Room Phone article at https://help.webex.com/en-us/nz3l3sm/Add-Features-to-Cisco-Webex-Room-Phone .

Cisco Webex Connectivity

You can now view information on your Cisco Webex connection from your phone.
				Administrators can use this information to troubleshoot an issue.

Information is available on the following items:

Calendar

Configuration

Credentials

Encryption

Geo location

Metrics

Notifications

Phonebook

Registration

Software upgrade

For more information, see the "View Webex Connectivity Information" tab on the Troubleshoot Your Cisco Webex Room Phone article at https://help.webex.com/en-us/nx0rg15/Troubleshoot-Your-Cisco-Webex-Room-Phone .

Support for Personal Mode

With Personal mode, users access their personal calendar instead of the room calendar for their meetings. Users can also collaborate with coworkers in a personal meeting space. Users also see their name in the top-left corner of the phone.

Turn on Personal mode from Cisco Webex Settings at https://settings.webex.com/ .

For more information, see the "Set Up Your Phone as a Personal Device" tab on the Customize Your Cisco Webex Room Phone article at https://help.webex.com/en-us/nk04cfc/Customize-Your-Cisco-Webex-Room-Phone .

Cisco Webex Video Integration for Microsoft Teams

Microsoft Teams meeting is now available for the Cisco Room Phone. For more information, see the "Cisco Webex Video Integration for Microsoft Teams" tab on the Join Meetings from Your Cisco Webex Room Phone at https://help.webex.com/en-us/guipj0/Join-Meetings-from-Your-Cisco-Webex-Room-Phone .

Meeting Participant List Enhancement

Users now see the following information when in a Webex meeting:

A list of people in attendance.

The status of each displayed participate, including the active speaker, the
						muted participants, and the participant who is screen sharing.

A notification if a participant joins or leaves the meeting.

This feature doesn't require any configuration.

For more information, see the "View the Meeting Participant Information" tab on the Join Meetings from Your Cisco Webex Room Phone at https://help.webex.com/en-us/guipj0/Join-Meetings-from-Your-Cisco-Webex-Room-Phone .

## September 11, 2020

The following sections describe the features that are new or have changed for Webex Calling with Control Hub.

Firmware Upgrade Enhancement

You can now postpone a phone firmware upgrade by 6 hours. This is a convenient way to
				reschedule an upgrade if you are busy, in a meeting, or on a call.

You can't postpone critical upgrades.

You can also upgrade your phone from Settings , if you want the latest release. This is a convenient way to make sure you have the latest features.

For more information, see https://help.webex.com/en-us/1ois7l/Your-Cisco-Webex-Room-Phone#task_EF2C02582CB977BC16C24FED699F71BE .

Support for Manual Factory Reset

You can now do a manual factory reset on your phone if you can't access the Settings menu. A factory reset returns the phone to the original factory settings.

For more information, see https://help.webex.com/en-us/nx0rg15/Troubleshoot-Your-Cisco-Webex-Room-Phone .