---
doc_id: www-cisco-com-c-en-us-td-docs-collaboration-meeting-center-wvdi-wvdi-b-admin-guide-wvdi-b-admin-guide-chapter-01-html-edbc807013
source_url: https://www.cisco.com/c/en/us/td/docs/collaboration/meeting_center/wvdi/wvdi-b-admin-guide/wvdi-b-admin-guide_chapter_01.html
retrieved_at: 2026-09-01T20:32:26.488161+00:00
---

Administration Guide for the Cisco Webex Meetings Virtual Desktop Environments

# Administration Guide for the Cisco Webex Meetings Virtual Desktop Environments

Updated: August 8, 2019

Chapter: Installing and Configuring the Cisco Webex Meetings Web App for Virtual Desktop Environments

## Chapter: Installing and Configuring the Cisco Webex Meetings Web App for Virtual Desktop Environments

# Installing and Configuring the Cisco Webex Meetings Web App for Virtual Desktop Environments

## About the Cisco Webex Meetings Web App for Virtual Desktop Environments (Beta)

Cisco Webex Meetings Web App for Virtual Desktop Environments (Beta) now supports Browser Content Redirection (BCR) for Citrix
                           Visualization platforms. This allows users on virtual desktops to join meetings from the Web App and get amazing audio and
                           video depending on the local computer and network conditions. Users can join meetings using the Web App on virtual environments
                           without BCR, but if they join with BCR then the media traversal happens between user's local machine and Cisco Webex cloud
                           providing the optimization. Currently, BCR is supported on Citrix Virtual Desktops and App version 7.15, 7.18, and 7.19

Due to limitation of the Citrix's Browser Content Redirection protocol, user on Web App cannot share their screen, but can
                                       see the screen share from other users.

## Citrix Browser Content Redirection Set up

Citrix BCR for VDI only supports Windows in the current release as Webex Meeting web client is WebRTC based. For more information,
                                          see Citrix Virtual Apps and Desktops .

Set up the environment to make the client fetch and client rendering work with VDI 7.18.

Install Citrix VDI version is 7.18 or higher. Make sure that the virtual machine has Citrix Virtual Delivery Agent 1811.1
                                       or higher, as a lower version doesn't support Google Chrome.

Install the Citrix Workspace on a local machine with the version 18.12.0.12(1812) or higher.

Don't install the Citrix Receiver.

Install the BCR extension for Chrome on the remote virtual machine for Chrome. The extension is, Browser Content Redirection Extension .

Enable the policy, Browser Content Redirection > Policies in Citrix Studio. By default, the BCR is set to Allowed .

Edit the Browser Content Redirection ACL Configuration > Policies in Citrix Studio.

This is an allowed list which contains the sites that allow VDA to perform BCR. Add the meeting sites having the thin client
                                          BCR feature. For example, add https://go.webex.com/* . The wildcard '*' can't be used for protocol and domain names.

Optional, allow HTML5 Video redirection in Citrix Studio > Policies .

### Set up the Environment

The Citrix VDI version is 7.15 LTSR CU3 on both the Delivery Controller and VDA.

Install the Citrix Workspace on a local machine with the version 18.12.0.12(1812) or higher.

Don't install the Citrix Receiver.

Install 7.15 LTSR CU3 on VDA by using command line and disabling the HTML5 option, VDAWorkstationsSetup_7.15.exe /FEATURE_DISABLE_HTML5 .

Install BCR.msi that is available on the Citrix download page.

Download the group policy template from Citrix here . Edit the Group Policy using the admin account on VDA.

You can also edit the Group Policy in Windows Registry.

Adding other configurations, for example: the chrome extension, wss://127.0.0.1:9001 is the same as in VDI 7.18.

For more information about setting up the VDI 7.15 environment, see Compatible Components for VDI 7.15

### Verify that the Client Fetch and Client Render Work

Connect to a VDA system from the local machine. Currently Windows is the supported operating system.

Launch Chrome on VDA and join a Webex meeting using the thin client. You can send and receive audio and video.

Check that the network package works on a local machine using the server address. The packages are present on the local and
                                          MMP servers and few of the control package are present local and on the VDA servers.

## Notes in the Setup

### Before you begin

To ensure best resolution and performance:

Click Citrix Workspace in your task bar and select Advanced Preferences .

Select High DPI > Yes > Save .

Check the resolution and scale ratio of your local machine.

## Limitations of the Webex Meetings Web App for Virtual Desktop Environments

If you are using the Webex Meetings Web App for Virtual Desktop Environments client on a virtual desktop with BCR enabled,
                                    you can't switch to native client.

The Webex Meetings Web App for Virtual Desktop Environments only works with Google Chrome on Windows.

The Playback feature for recordings is not available for Webex Meetings Web App for Virtual Desktop Environments.

The share functionality in not available on Webex Meetings Web App for Virtual Desktop Environments  as Citrix has not implemented
                                    the related WebRTC interface.

| Note | Due to limitation of the Citrix's Browser Content Redirection protocol, user on Web App cannot share their screen, but can
                                       see the screen share from other users. |
|---|---|

| Note | Citrix BCR for VDI only supports Windows in the current release as Webex Meeting web client is WebRTC based. For more information,
                                          see Citrix Virtual Apps and Desktops . |
|---|---|

| Step 1 | Install Citrix VDI version is 7.18 or higher. Make sure that the virtual machine has Citrix Virtual Delivery Agent 1811.1
                                       or higher, as a lower version doesn't support Google Chrome. |
|---|---|
| Step 2 | Install the Citrix Workspace on a local machine with the version 18.12.0.12(1812) or higher. Note Don't install the Citrix Receiver. | Note | Don't install the Citrix Receiver. |
| Note | Don't install the Citrix Receiver. |
| Step 3 | Install the BCR extension for Chrome on the remote virtual machine for Chrome. The extension is, Browser Content Redirection Extension . |
| Step 4 | Enable the policy, Browser Content Redirection > Policies in Citrix Studio. By default, the BCR is set to Allowed . |
| Step 5 | Edit the Browser Content Redirection ACL Configuration > Policies in Citrix Studio. This is an allowed list which contains the sites that allow VDA to perform BCR. Add the meeting sites having the thin client
                                          BCR feature. For example, add https://go.webex.com/* . The wildcard '*' can't be used for protocol and domain names. |
| Step 6 | Optional, allow HTML5 Video redirection in Citrix Studio > Policies . |

| Note | Don't install the Citrix Receiver. |
|---|---|

| Step 1 | The Citrix VDI version is 7.15 LTSR CU3 on both the Delivery Controller and VDA. |
|---|---|
| Step 2 | Install the Citrix Workspace on a local machine with the version 18.12.0.12(1812) or higher. Note Don't install the Citrix Receiver. | Note | Don't install the Citrix Receiver. |
| Note | Don't install the Citrix Receiver. |
| Step 3 | Install 7.15 LTSR CU3 on VDA by using command line and disabling the HTML5 option, VDAWorkstationsSetup_7.15.exe /FEATURE_DISABLE_HTML5 . |
| Step 4 | Install BCR.msi that is available on the Citrix download page. |
| Step 5 | Download the group policy template from Citrix here . Edit the Group Policy using the admin account on VDA. Note You can also edit the Group Policy in Windows Registry. | Note | You can also edit the Group Policy in Windows Registry. |
| Note | You can also edit the Group Policy in Windows Registry. |
| Step 6 | Adding other configurations, for example: the chrome extension, wss://127.0.0.1:9001 is the same as in VDI 7.18. For more information about setting up the VDI 7.15 environment, see Compatible Components for VDI 7.15 |

| Note | Don't install the Citrix Receiver. |
|---|---|

| Note | You can also edit the Group Policy in Windows Registry. |
|---|---|

| Step 1 | Connect to a VDA system from the local machine. Currently Windows is the supported operating system. |
|---|---|
| Step 2 | Launch Chrome on VDA and join a Webex meeting using the thin client. You can send and receive audio and video. |
| Step 3 | Check that the network package works on a local machine using the server address. The packages are present on the local and
                                          MMP servers and few of the control package are present local and on the VDA servers. |

| Step 1 | Click Citrix Workspace in your task bar and select Advanced Preferences . |
|---|---|
| Step 2 | Select High DPI > Yes > Save . |
| Step 3 | Check the resolution and scale ratio of your local machine. |