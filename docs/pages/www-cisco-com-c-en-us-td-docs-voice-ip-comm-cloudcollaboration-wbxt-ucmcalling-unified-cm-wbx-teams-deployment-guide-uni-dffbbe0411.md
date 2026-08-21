---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-ucmcalling-unified-cm-wbx-teams-deployment-guide-uni-dffbbe0411
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_0101.html
retrieved_at: 2026-08-20T23:59:54.620572+00:00
---

Deployment guide for Calling in Webex App (Unified CM)

# Deployment guide for Calling in Webex App (Unified CM)

Updated: November 10, 2025

Chapter: Manage and troubleshoot Calling in Webex App (Unified CM)

## Chapter: Manage and troubleshoot Calling in Webex App (Unified CM)

# Manage and troubleshoot Calling in Webex App (Unified CM)

## Configure users to move Jabber contacts and common settings to Webex App

This feature is built into Cisco Jabber and provides a way to migrate contacts in the
                              buddy list and other common user preferences from Jabber to Webex. The data is
                              encrypted. You just need to configure some settings before users see this option pop
                              up automatically in Jabber.

Learn how
                                 to configure Jabber users to move to Webex App .

## Access call statistics for Calling in Webex App (Unified CM)

During a call, you can access call statistics such as video frame rate, audio codec, packet loss, jitter, and bandwidth usage.
                              An indicator also appears that shows the call environment that you're on (your administrator or support team may need this
                              information for troubleshooting purposes).

Follow the steps or have your users follow the steps in Access call statistics to access statistics for a
                              call in Webex App for desktop or mobile.

## Edit a UC manager profile

Step 1

From the customer view in https://admin.webex.com , go to Management > Organization Settings , and under UC Manager Profiles select the
                                       ellipsis ... .

Step 2

Choose Edit .

Step 3

Make the necessary edits, and then select Save .

## Diagnostics in the Webex App

The diagnostics available in the Webex App (desktop and VDI) help you and your users resolve connection issues, check media
                              quality, and collect important troubleshooting information.

When you set up Calling in Webex App (Unified CM) , you may encounter issues related to the connection or required settings (such as
                              voice domain and UC services). Using this tool, you can diagnose what services are
                              configured correctly and what is missing. This feature is useful for troubleshooting
                              scenarios and reducing support cases, whether you're migrating to Calling in Webex App (Unified CM) or setting up new users.

When user experience issues, they can access the diagnostics view and export the
                                 data to share with you or support.

Unified CM Settings —Critical settings (for Jabber migration as well as
                                    new user setup) for phone services to work correctly, such as:

Unified CM version

UC service domain

SSO

UC services such as voicemail

Expressway for MRA

Media quality —Quality for video, audio, and sharing in both
                                    directions

Devices —Device information, when users are connected to devices

For shortcut keys to show the diagnostics window, see Keyboard
                                 and navigation shortcuts .

## Manage Cisco headsets in Control Hub

In the Control Hub devices view, you can get a list of all the Cisco headsets that are registered in
                              your organization for tracking purposes. You can find further details and management
                              options for each headset entry. This information can help you make decisions on
                              whether headsets need to be replaced or troubleshooted.

For more information, see Manage Cisco headsets in Control Hub .

## Connection is lost to the Webex cloud

If https://status.webex.com or the health checker show a Webex App cloud full or partial outage, Calling in Webex App (Unified CM) still works for users who are already signed in, as long as the call
                              type is a Unified CM call and goes through Unified CM infrastructure.

Unified CM calling can't happen in the following scenarios when sign in is
                              blocked:

First day sign-in for the user

Sign out of Webex App then sign in again

Unified CM calling can happen in the following scenarios where the app remains signed
                              in:

Quit or exit Webex App and then relaunch—cached data remains (contacts, call history, messages).
                                    Unified CM registration and calling aren't affected, but presence when on a
                                    call is not sent to other users.

Reboot the device that Webex App is running on—cached data remains (contacts, call history, messages).
                                    Unified CM registration and calling aren't affected, but presence when on a
                                    call is not sent to other users.

### Single Number Reach (SNR) workaround

If Unified CM is not reachable from Webex App , users can use the Self Care Portal (a link is available in Webex App ) to set up Single Number Reach (SNR) so that calls get routed to mobile through
                              the PSTN. For administrative steps, see the Cisco Unified Mobility Features chapter
                              in the Feature Configuration Guide for Cisco Unified Communications
                                 Manager . For user self-care configuration, see the Self Care Portal User Guide .

## Troubleshoot issues with Calling in Webex App (Unified CM)

If you see registration issues when trying to use Calling in Webex App (Unified CM), go through these checklist items before you submit a ticket.

Step 1

Verify that any CTI-RD or Cisco Spark-RD was removed from Unified CM for the
                                       user; if not, delete any stray remote devices.

Step 2

If your organization is enabled for a different call behavior (such as a
                                       cross-launch to another calling app) in Control Hub, disable this feature and
                                       reselect Calling in Webex App (Unified CM) because Unified CM registration and cross-launch cannot
                                       be enabled together.

Step 3

Exit Jabber if it's installed on the same machine, because Jabber and Webex App cannot both be registered to Unified CM in softphone mode at the same time.

Step 4

Check other configuration on Unified CM. Some common culprits include the following:

- No Controlled Devices in the Unified CM end user account. Ensure that the soft phone device is added to the Controlled Devices.

- Missing SUBSCRIBE Calling Search Space for Extension Mobility users. Ensure that a value is selected for this setting.

- A missing Access Control Group permission on the end user account: Standard CTI Allow Control of Phones supporting Connected Xfer and conf . Ensure this box is checked.

### What to do next

If you addressed all of these steps and issues still persist, restart Webex App and then choose Help > Send Feedback to submit logs and open a case for the support team to investigate.

## Error messages in Webex App

A warning icon appear in the app if Webex App failed to register to Unified CM because of a sign in failure or other reason. A
                              summary of the reason appears next to the icon.

Tip

You can hover over the icon to show an error message that may give you clues
                                          about what to troubleshoot. You can also click the icon to see if there are any
                                          next steps that you have to take to resolve the issue (such as sign into phone
                                          services or start a new session).

See the Error messages documentation for more information on
                                          the errors that may appear in Webex App and how to resolve the problem.

| Step 1 | From the customer view in https://admin.webex.com , go to Management > Organization Settings , and under UC Manager Profiles select the
                                       ellipsis ... . |
|---|---|
| Step 2 | Choose Edit . |
| Step 3 | Make the necessary edits, and then select Save . |

| Step 1 | Verify that any CTI-RD or Cisco Spark-RD was removed from Unified CM for the
                                       user; if not, delete any stray remote devices. |
|---|---|
| Step 2 | If your organization is enabled for a different call behavior (such as a
                                       cross-launch to another calling app) in Control Hub, disable this feature and
                                       reselect Calling in Webex App (Unified CM) because Unified CM registration and cross-launch cannot
                                       be enabled together. |
| Step 3 | Exit Jabber if it's installed on the same machine, because Jabber and Webex App cannot both be registered to Unified CM in softphone mode at the same time. |
| Step 4 | Check other configuration on Unified CM. Some common culprits include the following: No Controlled Devices in the Unified CM end user account. Ensure that the soft phone device is added to the Controlled Devices. Missing SUBSCRIBE Calling Search Space for Extension Mobility users. Ensure that a value is selected for this setting. A missing Access Control Group permission on the end user account: Standard CTI Allow Control of Phones supporting Connected Xfer and conf . Ensure this box is checked. |

| Tip | You can hover over the icon to show an error message that may give you clues
                                          about what to troubleshoot. You can also click the icon to see if there are any
                                          next steps that you have to take to resolve the issue (such as sign into phone
                                          services or start a new session). See the Error messages documentation for more information on
                                          the errors that may appear in Webex App and how to resolve the problem. |
|---|---|