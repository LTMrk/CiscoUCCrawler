---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-217558-configuring-http-2-for-broadworks-nps-wi-htm-7eb23ae6ea
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/217558-configuring-http-2-for-broadworks-nps-wi.html
retrieved_at: 2026-09-07T13:02:20.297493+00:00
---

Configuring HTTP/2 for BroadWorks NPS with Apple Push Notification Service

# Configuring HTTP/2 for BroadWorks NPS with Apple Push Notification Service

### Download Options

Updated: March 31, 2021

Document ID: 217558

Contents

## Contents

After March 31st 2021 the Notification Push Server (NPS) must use an HTTP/2 interface to communicate with the Apple Push Notification service (APNS). The HTTP/2 interface is available on BroadWorks Release 22.0 via the patch ap354313 and Release 23.0 supports only HTTP/2.

If running BroadWorks Release 22.0, HTTP/2 can be configured using the following instructions after applying ap354313. If upgrading to 23.0 or later the following steps will be needed to configure HTTP/2 for APNS.

## Requirements

You must be on 22.0+ or 23.0 XSP. A 22.0/23.0 XSP is compatible to run in parallel with an 21.sp1 stack if the XSP ONLY runs NPS and the AS is 21.sp1. See the BroadWorks Compatibility Matrix for more information.

You will need to know what clients are currently in use as the Auth Key ID, TeamID and Auth Key will be required to configure HTTP/2. The apps configured on 21.sp1 can be found here:

```
XSP_CLI/Applications/NotificationPushServer/APNS/Production/Certificate> get
```

- Any iOS apps Non-Cisco/BroadSoft apps must be configured to use the HTTP/2 APNS protocol.

- Add HTTP/2 Support to Notification Push Server for APNs

- For SaaS clients, login to the BAM portal → Configuration → BroadWorks, scroll down to section:  Notification Push Server, select the proper release in the drop-down, then follow the instructions.

- For Connect Eval Clients open a ticket with TAC to request the Auth Keys, Auth Key ID, and TeamID. Note that the App Id, Auth Key Id and Team Id listed below are for the unbranded client, if using a branded client, this information will need to be obtained for your clients from Apple.

Required tokens for other clients can be obtained from the Apple Developer portal, see the Apple documentation here:

https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/...

If upgrading to or deploying a new 22.0, 23.0 or ADP the necessary license will be required.

Please also refer to the relevant release notes available on Xchange for OS and upgrade requirements.

## Configuration

Ensure the URL in the Notification Push Server CLI is correct for HTTP/2 for both Production and Development.

#### Set the URL for HTTP/2

```
_CLI/Applications/NotificationPushServer/APNS/Production> get
   url = https://api.push.apple.com/3/device
   connectionPoolSize = 5
   connectionTimeout = 1000
   connectionIdleTimeoutInSeconds = 600 _CLI/Applications/NotificationPushServer/APNS/Development> get
   url = https://api.development.push.apple.com/3/device
   connectionPoolSize = 5
   connectionTimeout = 1000
   connectionIdleTimeoutInSeconds = 600
```

The above settings may need to be tuned for your specific system. The above example and following recommendations may provide a starting point.

- The 'ConnectionPoolSize' is the number of concurrent connections NPS can make to APNS servers. This will help throughput of NPS and may not directly help timeout issues. The ConnectionPoolSize should be increased above 2, note that without ap377409 the NPS may not properly register a value above 2.

- It is recommended to set the connectionTimeout to a value above 1000.

#### Configure the A uth Keys

```
_CLI/Applications/NotificationPushServer/APNS/AuthKey> add UTHPSAD667 Y2V5KSH586 /export/home/bwadmin/EVAL_Team-Y2V5KSH586-APNsAuthKey_ID-UTHPSAD667.p8
...Done

_CLI/Applications/NotificationPushServer/APNS/AuthKey> get
  Auth Key Id    Team Id     Auth Key
  ===================================
  64D9E5NY4S     D775LZJG9V  ********       <- SaaS
  L44B3C998K     698ZB8543V  ********       <- Connect Dev
  UTHPSAD667     Y2V5KSH586  ********       <- Connect Eval

3 entry found.
```

#### Add Tokens for Produ ction and Development Environments

```
_CLI/Applications/NotificationPushServer/APNS/Production/Tokens> add com.broadsoft.connect.eval authKeyId UTHPSAD667
...Done

_CLI/Applications/NotificationPushServer/APNS/Production/Tokens> get
                               App Id   Auth Key Id
===================================================
                 com.broadsoft.uc-one   64D9E5NY4S       <- SaaS
           com.broadsoft.connect.eval   UTHPSAD667       <- Connect Eval

2 entries found.
```

#### Enable HTTP/2 if using XSP 22.0

```
XSP_CLI/Applications/NotificationPushServer/APNS/GeneralSettings> set HTTP2Enabled true
```

Note: If on 23.0 or ADP this step is not required as HTTP/2 cannot be disabled.

#### R estart BroadWorks

```
restartbw
```

## Troubleshooting

The response to the HTTP/2 POST is processed by the Notification Push Server. A response code of “200” from the APNs means that the notification was successfully received by the APNs and it will try to push the notification to the device. Detailed error messages are captured in the Notification Push Server logs.

If Apple returns an error code the Apple error codes can be found in the Apple documentation here:

https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotifi...

If using the ADP the AS must be set to use TLSv1.2. To set this add the following container option on the AS:

```
AS_CLI/Maintenance/ContainerOptions> add platform bw.apache.sslenabledprotocols "-ALL +TLSv1.2"
```

Once the AS has been set to use TLSv1.2, stop BroadWorks, restart configd, and start BroadWorks again on the AS.

```
stopbw
configdctl restart
startbw
```

## Reference

HTTP/2 BroadWorks documentation: https://xchange.broadsoft.com/node/498995

Alert on Xchange in regards to the replacement of the previous binary APNS interface: https://xchange.broadsoft.com/node/1053230

UC-One Solutions Guide: https://xchange.broadsoft.com/node/1049202

See the patch notes on ap354313 for 22.0: https://xchange.broadsoft.com/node/496044

Please note that ap354313 exists for platform as well as for the AS, EMS, HZS, PS, NS, NFM, UMS, and XSP in order to update Java to 8.0_102b, this is a requirement for the XSP on 22.0 to work with HTTP/2, it does not mean that the UMS must also be on 22.0.

#### Connect Eval Client

https://apps.apple.com/in/app/uc-one-connect-evaluation/id1114743230

### Revision History

2.0

31-Mar-2021

Initial Release

1.0

11-Nov-2021

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 31-Mar-2021 | Initial Release |
| 1.0 | 11-Nov-2021 | Initial Release |