---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-userguide-cjab-b-cisco-jabber-user-guide-cjab-m-troubleshooting-ug-ht-614e9dbb56
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/userguide/cjab_b_cisco-jabber-user-guide/cjab_m_troubleshooting-ug.html
retrieved_at: 2026-08-21T07:08:05.045720+00:00
---

Cisco Jabber User Guide

# Cisco Jabber User Guide

Updated: May 4, 2026

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Sign-In Issue Resolutions

Here are ways to resolve sign-in issues.

### iPhone and iPad

If you cannot sign in, try the following troubleshooting tips:

Check if you are using a supported device and operating system. Click here| Supported Device and Operating System

Check if you can access your corporate network from non-corporate Wi-Fi networks.

If you can access your corporate network from non-corporate Wi-Fi networks, contact your system administrator to check if
                                    your collaboration edge environment has been set up correctly.

If you have access rights to your corporate network from non-corporate Wi-Fi networks, check that your VPN is connected (if
                                    VPN is required). If your VPN is not connected, contact your system administrator.

If you are using Phone Services , check the network connection between your device and the corporate network as follows:

Open your Internet browser.

Try to access the administration pages for your corporate calling system by entering the following URL in your Internet browser:
                                          https://your company's Cisco Unified Communications Manager (CUCM) server address.

Example:https://209.165.200.224

Contact your system administrator if you need the address for your company's Cisco Unified Communications Manager server.

If you cannot access the administration pages for your corporate calling system, try again from a different network access
                                    point. If you still cannot access the administration pages for your corporate calling system, contact your system administrator
                                    to find out if there is a network issue.

If you are using Cisco Unified Communications Manager (CUCM) IM and Presence Service Release 9.1 or earlier, check that you
                                    can sign in with your user account as follows:

Enter the URL using the following format: https://presence server name/ccmuser .

If you cannot access the server, contact your system administrator to find out if there is a network issue.

Sign in with your username and password.

If the sign-in fails, please confirm your username and password with your system administrator.

Open a ping utility to ping the Cisco Unified Communications Manager IM and Presence Service server.

Enter the Fully Qualified Domain Name of the server in the following format: presence server name.domain.com.

If you cannot ping the server, contact your system administrator.

### Android

If you cannot sign in, try the following troubleshooting tips:

Check that you are using a supported device and operating system. For information about supported devices and operating systems,
                                    see the Cisco Jabber for Android Release Notes for your release.

Check that you are using the correct release of Cisco Jabber for Android.

You can download the latest release of Cisco Jabber for Android from the Google Play Store.

Check that your VPN is connected (if VPN is required). If your VPN is not connected, and you are not using Expressway Remote
                                    and Mobile Access, contact your system administrator for configuration details.

If you are using HTTP basic SAML SSO authentication and the sign-in fails when switching users with the Reset Jabber functionality:

Reset Cisco Jabber.

Force Quit the application fully in Android OS.

Log in.

If you are using Phone Services, check the network connection between your device and the corporate network as follows:

Open your web browser.

Try to access the administration pages for your corporate calling system by entering the following URL in your web browser:
                                          http://cisco_unified _communications_manager_node_name_or_ip_address/ucmuser.

Contact your system administrator if you do not have the address for your company's Cisco Unified Communications Manager node.

If you cannot access the administration pages for your corporate calling system, try again from a different network access
                                    point. If you still cannot access the administration pages for your corporate calling system, contact your system administrator
                                    to find out if there is a network issue.

If you are using Cisco Unified Communications Manager IM and Presence Service, check the network connection between your device
                                    and the node as follows:

Open a ping utility to ping the Cisco Unified Communications Manager IM and Presence Service node.

Enter the Fully Qualified Domain Name or IP address of the node in one of the following formats:

presence_node_name.domain.com

ip_address.domain.com

If you cannot ping the node, contact your system administrator.

If you are using a tablet, contact your system administrator to ensure that it is set up for use. Some tablet services require
                                    extra configuration that may not have been performed.

If you still cannot set up Cisco Jabber for Android, send a problem report to your system administrator.

## Jabber Configuration Refresh

Keep your Cisco Jabber client up-to-date by refreshing your Cisco Jabber configuration any time after you're signed in to
                              it. Refresh Cisco Jabber if your administrator has modified the parameter settings. Even if you don't update or refresh, Cisco
                              Jabber automatically checks with the servers every 8 hours to make sure it has the latest configuration.

### Refresh Your Windows Configuration

Step 1

From Cisco Jabber, click the gear icon , choose Help and choose Refresh Configuration .

Step 2

Click OK .

### Refresh Your Mac Configuration

Step 1

From the main menu, go to Help and choose Refresh Configuration .

Step 2

Click OK .

### Refresh Your Mobile Configuration

Step 1

Tap your contact picture, go to Settings , and scroll down to Help .

Step 2

Tap Configuration and then Refresh Configuration .

## Jabber Reset

You can reset Cisco Jabber when you want to change your account, clear your log files, clear your chat or call history, or
                              troubleshoot Jabber issues.

### Reset Your Windows App

Step 1

From Cisco Jabber, click the gear icon and choose Sign out .

Step 2

From the Sign In page, click Reset Jabber .

Step 3

Click Keep to retain the secure phone certificate.

Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it.

### Reset Your Mac App

Step 1

From the main menu, scroll down and choose Quit Jabber .

Step 2

From the Sign In page, click Reset Jabber .

Step 3

Click Keep to retain the secure phone certificate.

Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it.

### Reset Your Mobile App

Step 1

Tap on your profile picture and then tap Sign out .

Step 2

From the Sign In page, tap Reset Jabber .

Step 3

Tap Keep in Android or tap Keep Certificate in iPhone and iPad to retain the secure phone certificate.

Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it.

| Step 1 | From Cisco Jabber, click the gear icon , choose Help and choose Refresh Configuration . |
|---|---|
| Step 2 | Click OK . |

| Step 1 | From the main menu, go to Help and choose Refresh Configuration . |
|---|---|
| Step 2 | Click OK . |

| Step 1 | Tap your contact picture, go to Settings , and scroll down to Help . |
|---|---|
| Step 2 | Tap Configuration and then Refresh Configuration . |

| Step 1 | From Cisco Jabber, click the gear icon and choose Sign out . |
|---|---|
| Step 2 | From the Sign In page, click Reset Jabber . |
| Step 3 | Click Keep to retain the secure phone certificate. Note Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. | Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |
| Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |

| Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |
|---|---|

| Step 1 | From the main menu, scroll down and choose Quit Jabber . |
|---|---|
| Step 2 | From the Sign In page, click Reset Jabber . |
| Step 3 | Click Keep to retain the secure phone certificate. Note Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. | Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |
| Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |

| Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |
|---|---|

| Step 1 | Tap on your profile picture and then tap Sign out . |
|---|---|
| Step 2 | From the Sign In page, tap Reset Jabber . |
| Step 3 | Tap Keep in Android or tap Keep Certificate in iPhone and iPad to retain the secure phone certificate. Note Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. | Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |
| Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |

| Note | Don't remove the certificate or you won't be able to use any calling features until your administrator reconfigures it. |
|---|---|