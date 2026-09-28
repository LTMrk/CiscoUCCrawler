---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-12-5-1-su4-cucm-b-release-notes-for-cucm-imp-1251su4-cucm-m-n-c22577a287
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_5_1/SU4/cucm_b_release-notes-for-cucm-imp-1251su4/cucm_m_new-and-changed-features.html
retrieved_at: 2026-08-17T00:03:52.391539+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU4

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU4

## Results

Updated: February 22, 2021

Chapter: New and Changed Features

## Chapter: New and Changed Features

# New and Changed Features

## Headset and Accessories Inventory Download

The Headsets menu category is renamed to Headsets and Accessories in the Cisco Unified Communications Manager user interface.

This feature enables an administrator to download a detailed report of Headsets and Accessories in your deployment into a
                           CSV file from the Unified Communications Manager user interface.

For more information, see the “Headset and Accessories Management” chapter in the Feature Configuration Guide for Cisco Unified Communications Manager .

## Oracle JRE Removal from Manager Assistant

The Oracle Java Runtime Environment (JRE) is no longer included in the Cisco Unified Communications Manager Assistant plug-in.

Before you upgrade the Cisco Unified Communications Manager Assistant client to a newer version, perform the following:

Uninstall the Cisco Unified Communications Manager Assistant client that is currently installed on your machine.

Install JRE on 32-bit or 64-bit Windows platform.

For more information, see the Feature Configuration Guide for Cisco Unified Communications Manager .

## Smart Licensing Registration Through Authentication Based Proxy

This feature enables licensing component on Unified Communications Manager to communicate with the cloud-based Cisco Smart
                              Software Manager using an authenticated connection through the HTTP/HTTPS proxy.

## SSO Redirect URI for Webex Apps

The SSO Redirect URI feature allows soft clients (Cisco Jabber/Cisco Webex App) that use the external browser to perform SSO,
                              be cross launched by the browser using SSO Redirect URI so that the browser can sign in to the Cisco Jabber/Cisco Webex App
                              backend service.

Webex Client Embedded Browser Support

This feature enhances the security of Cisco Jabber/Webex Client Embedded Browser Support.

Enhancements include:

Protection against " Authorization Code Interception Attack ", as per RFC7636.

Improved calling experience prevents dual login when SSO is enabled while using Webex Client(s) or Unified Communications Manager .

## Performance Counters for Mobile and Remote Access Device Registrations

New performance counters are introduced in the Cisco Unified Real-Time Monitoring Tool to track registered Cisco Webex App
                           and Cisco Jabber devices registered to Unified Communication Manager in Mobile and Remote Access mode. This enables administrators
                           to get an insight into how many devices in Mobile and Remote Access mode are registered to Unified CM. When you enable troubleshooting
                           Perfmon data logging, system automatically collects statistics for these new counters and stores it in Perfmon logs.

For more information on the new counters, see the Cisco Unified Real-Time Monitoring Tool Administration Guide .

## UDS Enhancements

The following enhancements are introduced for UDS:

The UDS Bulk Search by Email enables Cisco Jabber to send requests in batches using the email attribute to prevent high CPU
                                 usage by UDS and Cisco Tomcat services.

UDS is enhanced to do a better discovery of the home cluster of a user across remote clusters. This helps in avoiding the
                                 Cisco Jabber login failures and ensures geo redundancy in the event of Data Center failure or shutdown.

## Certificate Sync and Intercluster Periodic Sync

The IM and Presence Service performs certificates sync as part of the intercluster sync process. This feature introduces a
                           new service parameter Certificate Sync during Inter-Cluster Periodic Sync and allows the administrator to disable or enable certificates synchronization as part of Intercluster periodic sync from
                           the Cisco Unified Communications Manager IM and Presence Administration user interface.

The Certificate Sync feature intoduces the following options:

Perform certificate sync —This is the default value of the Certificate Sync during Inter-Cluster Periodic Sync service parameter. When the Certificate Sync during Inter-Cluster Periodic Sync service parameter is set to Perform certificate sync and the certificates are not synchronized across the intercluster peers, it requires a Force Manual Sync operation to synchronize
                                 data and certificates.

Do not perform certificate sync —To disable the certificate sync during the ICSA sync, the administrator can set the Certificate Sync during Inter-Cluster Periodic Sync service parameter to Do not perform certificate sync .

For detailed information on how to disable or enable certificates sync as part of the intercluster sync process, see the "Configure
                           Intercluster Peers" chapter in the Configuration and Administration of the IM and Presence Service Guide .

## Improved IM and Presence Stream Features/Services Advertisement via Expressway

IM and Presence Service now supports the advertisement of XMPP stream features/services to the clients connecting over Cisco
                           Expressway's Mobile and Remote Access.

This new functionality enables deployments with mixed IM and Presence Service versions, for example some clusters on 11.5(1)SU8
                           and some other clusters on 12.5(1)SU3, to work with Cisco Expressway so that Cisco Jabber clients can discover the correct
                           capabilities applicable to it based on the IM and Presence Service home cluster it is assigned to.

For this mechanism to work, the minimum deployment requirement is to have Cisco Expressway running version X12.7 or higher
                           and have at least one IM and Presence cluster in the intercluster mesh running version 11.5(1)SU9 or 12.5(1)SU4 and above.

Depending on your current IM and Presence Service version mix, you may need to enable or disable push notifications feature
                           using FCM service flag on the Expressway as per the information given in the following table:

```
xConfiguration XCP Config FcmService: On/Off
```

Mixed Versions IM and Presence Clusters

Expected Status of FCM Flag on Expressway X12.7

Comment

Any 11.5(1)SU with

12.5(1)SU2 and lower

OFF

Android Push (FCM) NOT supported.

11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU3

OFF

Android push (FCM) NOT supported

11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU4 (and higher)

OFF

Android push (FCM) supported on 12.5(1)SU4 (or newer) versions

11.5(1)SU9 (and higher) or 12.5(1)SU4 (and higher) with 12.5(1)SU3

ON

Android push (FCM) supported on version 12.5(1)SU3 and higher

11.5(1)SU9 (and higher) with 12.5(1)SU4 (and higher)

Flag not required

(Expressway 12.7 relies fully on the new discovery mechanism)

Android push (FCM) supported on 12.5(1)SU4 (or newer) versions

| Note | If you encounter performance degradation or high CPU spikes in your deployment that is related to certificate sync during
                                    intercluster periodic sync, you can use this feature. |
|---|---|

| Note | Apple Push Notification Service (APNS) is not affected by the FCM service flag status. |
|---|---|

| Mixed Versions IM and Presence Clusters | Expected Status of FCM Flag on Expressway X12.7 | Comment |
|---|---|---|
| Any 11.5(1)SU with 12.5(1)SU2 and lower | OFF | Android Push (FCM) NOT supported. |
| 11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU3 | OFF | Android push (FCM) NOT supported |
| 11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU4 (and higher) | OFF | Android push (FCM) supported on 12.5(1)SU4 (or newer) versions |
| 11.5(1)SU9 (and higher) or 12.5(1)SU4 (and higher) with 12.5(1)SU3 | ON | Android push (FCM) supported on version 12.5(1)SU3 and higher |
| 11.5(1)SU9 (and higher) with 12.5(1)SU4 (and higher) | Flag not required (Expressway 12.7 relies fully on the new discovery mechanism) | Android push (FCM) supported on 12.5(1)SU4 (or newer) versions |