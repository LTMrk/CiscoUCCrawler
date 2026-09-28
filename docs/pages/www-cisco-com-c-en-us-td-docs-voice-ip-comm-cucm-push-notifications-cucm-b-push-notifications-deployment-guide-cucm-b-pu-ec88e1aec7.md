---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-push-notifications-cucm-b-push-notifications-deployment-guide-cucm-b-pu-ec88e1aec7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_011.html
retrieved_at: 2026-08-16T16:07:43.353205+00:00
---

Push Notifications Deployment Guide

# Push Notifications Deployment Guide

Updated: August 20, 2024

Chapter: Certificates and Performance Monitoring

## Chapter: Certificates and Performance Monitoring

# Certificates and Performance Monitoring

## Certificates for Cloud Connection

For on-premises deployments, you must obtain and upload certificates manually if you choose not to have Cisco manage cloud
                              certificates automatically, or if a new certificate requirement is added that was not included in your system installation
                              file. In these instances, you will have to download certificates manually from the CA site and upload them to Unified Communications Manager and IM and Presence Service. To choose this option, uncheck the I want Cisco to manage the Cisco Cloud Service CA Certificates required for this trust check box in the Cloud Onboarding Configuration window in Unified Communications Manager .

### Root Certificates for Cloud Connection

Refer to the below table for the root certificates that you must obtain if you are uploading certificates manually. For details
                              on how to upload certificates to Unified Communications Manager and IM and Presence Service, refer to the "Certificates" sections in the Security Guide for Cisco Unified Communications Manager . Make sure to select tomcat-trust as the Certificate Purpose .

Cloud hosts signed by this CA

Must be trusted by

For this purpose

Issuing CA

Fingerprint (Thumbprint) in SHA256

Common Identity (CI) service

Unified Communications Manager and IM and Presence Service

Cisco Unified Communications Manager requests a CI machine token to authenticate with Cisco Push REST service.

Secure https communication between Unified Communications Manager , IM and Presence Service, and the Cisco Push REST service.

O = IdenTrust

CN = IdenTrust Commercial Root CA 1

5D 56 49 9B E4 D2 E0 8B CF CA D0 8A 3E 38 72 3D 50 50 3B DE 70 69 48 E4 2F 55 60 30 19 E5 28 AE

Cisco Webex

Cisco Unified Communications Manager andIM and Presence Service

Unified Communications Manager communicates with Fusion Onboarding Service (FOS) to provision CI machine account.

O = The Go Daddy Group, Inc.

OU = Go Daddy Class 2 Certification Authority

C3 84 6B F2 4B 9E 93 CA 64 27 4C 0E C6 7C 1E CC 5E 02 4F FC AC D2 D7 40 19 35 0E 81 FE 54 6A E4

### Scenarios Where Cloud Certificates can be Uploaded Automatically

The following table shows whether onboarding will be successful with the I want Cisco
                                 to manage the Cisco Cloud Service CA certificates required for
                                 this trust check box selected in the Cisco Cloud Onboarding Configuration window,  or whether certificates need to be uploaded manually for onboarding to be successful.

Scenario

Installation iso file included the required certificates?

You have chosen to have Cisco manage certificate requirements

Onboarding is Successful?

Onboarding for first time

Yes

Yes

Yes

Onboarding for first time

No. The certificate requirements changed sometime after the installation iso was created

Yes

No. You must obtain and upload the new certificates manually. See the preceding table "Root Certificates for Cloud Connection".

You are already onboarded, but now a new certificate requirement has arisen

Your installation will not include the required certificates

Yes

Yes. The system can fetch and install new certificates automatically.

## Push Notifications Alarms

The following table highlights alarms that were added to support Push Notifications call support in Unified Communications Manager and IM and Presence Service Release 11.5(1)SU3.

Alarm

Description

Cisco CallManager Alarms

PushNotificationServiceUnavailable

Description : Unable to connect with Cisco Push Notification Service. The CallManager service requires a connection in order to send Push
                                          Notifications to the Cisco Cloud.

Severity : ALERT_ALARM

Action : In Cisco Unified Serviceability, check that the Cisco Push Notification Service status is running. If the service is stopped,
                                          start it. If the service is running, restart it.

PushNotificationInvalidDeviceTokenResponse

Description : Cloud returned Error code 410 for Push Notification sent from CallManager Service due to invalid device token. Push Notification
                                          for this iOS Cisco Jabber or Cisco Webex device will be stopped until valid device token is set by iOS Cisco Jabber and Webex
                                          device.

Severity : ERROR_ALARM

Action : User should log out and log back in to Cisco Jabber or Webex clients on that iOS device .

PushNotificationServiceAccessTokenUnavailable

Description: Cisco Push Notification Service (CPNS) does not have a valid Access Token. Unified Communications Manager requires valid Access Token to send Push Notifications to Cloud. This Access Token is not available from Cloud due to authentication
                                          or network error.

Severity: ALERT_ALARM

Action: Check the Cisco Cloud Onboarding Configuration window to confirm that the onboarding process has completed successfully. If the issue persists contact Cisco TAC for further
                                          assistance..

Cisco Push Notification Service Alarms

StartFailed

Description: This alarm indicates that an internal failure prevented the Cisco Push Notification Service from starting

Severity: CRITICAL_ALARM

Action: Try restarting the Cisco Push Notification Service. If the issue persists check the Cisco Push Notification Service application
                                          logs and contact Cisco TAC for further assistance.

AccessTokenInvalid

Description: This alarm indicates that current access token is expired and become invalid and new access token is unavailable.

Severity: ALERT_ALARM

Action: Check the Cisco Cloud Onboarding Configuration window to confirm that the onboarding process has completed successfully. If the issue persists, contact Cisco TAC for further
                                          assistance.

HttpClientPoolCreationError

Description: Indicates an error in creating the Http Client connection pool

Severity: ALERT_ALARM

Action: Check the Cisco Cloud Onboarding Configuration window and verify that the HTTP proxy settings are correct. In addition, verify that the on-boarding process has completed.

Cisco XCP Config Manager

PushNotificationFailed

Description: Cisco XCP Config Manager was not able to send Push Notification.

Severity: CRITICAL_ALARM

Action: Check the Error Code and follow the Error action that is directed.

PushNotificationFailedInvalidDeviceToken

Description: An attempt to send a Push Notification to the Cisco Cloud failed due to an invalid device token.

Severity: CRITICAL_ALARM

Action: User should re-login to Jabber.

PushNotificationFailedInvalidAccessToken

Description: An attempt to send a Push Notification to the Cisco Cloud failed due to an invalid access token.

Severity: CRITICAL_ALARM

Action: Look at the IM and Presence Service Cisco XCP Config Manager service logs to verify whether the AccessToken was fetched and
                                          refreshed on a timely basis. If the AccessToken was fetched and refreshed it on timely basis then do check the Cisco Cloud
                                          for further debugging.

AccessTokenFetchFailed

Description: Cisco XCP Config Manager was unable to fetch the Access Token.

Severity: CRITICAL_ALARM

Action: Check the Error Code and follow the Error action that is directed

XCPConfigMgrAccessTokenIsNull

Description: Cisco XCP Config Manager was unable to fetch the access token.

Severity:

Action: IM and Presence Service nodes must connect to the Cisco cloud to obtain the Access Token. Verify the following:

Verify that the access token URL and refresh token are valid.

Verify that the proxy details are correct on the Cisco Cloud Onboarding window.

Check connectivity to the Cisco cloud.

Cisco Jabber Alarms

APNSAlarm

Description: An iOS Jabber client was unable to process an Push Notification.

Severity: ALERT_ALARM

Action: Contact Cisco TAC for further assistance.

Unread Messages alert

This alert appears only in releases prior to 12.5(1). The issue is fixed as of 12.5(1).

Description : An iOS Jabber client gets the following message: Unread messages might be deleted from server due to timeout. Please sign
                                          in Jabber to check unread messages.

Severity: ALERT_ALARM

Conditions: Cisco Jabber for iPhone running in the background. The user did not sign out of Cisco Jabber prior to closing the application.

## Performance Counters for Push Notifications

### Performance Counters for Apple Push Notifications

The following table shows counters added to the Cisco Unified Real Time Monitoring Tool to support Push Notifications for
                              on-premises deployments of Unified Communications Manager and IM and Presence Service. Note that the counters increment only for specific APNS subscriber services (for example, APNS,
                              APNS:beta, APNS:dev, APNS:test, APNS:load). For example, if the subscriber service is 'APNS:beta' only the APNS:beta counters
                              increment, and none of the APNS:dev counters increment. The Cisco Jabber and Cisco Webex service type determines which subscriber
                              service is used.

Counter Description

Counter increments if the Subscriber service is set to...

Cisco CallManager Counters

NumberOfPushReqSent

The total number of Push Notification Requests sent by the Cisco CallManager Service.

Any APNS Subscriber Services.

NumberOfPushResReceived

The total number of Push Notification Responses received by the Cisco CallManager Service.

Any APNS Subscriber Services.

NumberOfPushErrorResReceived

The total number of Push Notification Responses received by Cisco CallManager Service with response code other than 200 OK.

In case of TLS handshake failure between Cisco Push Notification Service (CPNS) and Cloud PushRest, this counter will be incremented
                                          for push requests which could not be sent due to TLS handshake failure.

Any APNS Subscriber Services.

CustomRegionNumofMsgPushReqSent

The total number of Message Push Notification requests sent from CallManager Service, when call is made to Custom Region devices,
                                          where CallKit is disabled.

Any APNS Subscriber Services.

CustomRegionNumofMissedCallMsgPushReqSent

The total number of missed call Message Push Notification requests sent from CallManager Service to Custom Region devices,
                                          where CallKit is disabled.

Any APNS Subscriber Services.

CustomRegionNumofSharedCancelMsgPushReqSent

The total number cancel call Message Push Notification requests sent from CallManager Service in Shared Line scenario to Custom
                                          Region devices, where CallKit is disabled.

Any APNS Subscriber Services.

Cisco Mobility Manager Counters

MobilityPushNotificationCallsExtendedToMIDueToTimeout

This represents the total number of calls sent to the Mobility Identity destination where Cisco Jabber or Cisco Webex did
                                          not register after receiving push notification before the "Cisco Jabber Dual Mode (iPhone) Incoming Call Push Notification
                                          Wait Timer" expired.

Any APNS Subscriber Services.

MobilityPushNotificationCallsExtended ToJabber

This represents the total number of calls sent to Cisco Jabber where Cisco Jabber registers successfully after receiving
                                          push notification before the "Jabber Dual Mode (iPhone) Incoming Call Push Notification Wait Timer" expired.

Any APNS Subscriber Services.

NumberOfPushSuccess

Number of successful Push Notifications sent.

Any APNS Subscriber Services.

NumberOfPushFailure

Number of failed attempts to send Push Notifications.

Any APNS Subscriber Services.

TargetInvalid

Total number of Push Notification failures due to an invalid target.

Any APNS Subscriber Services.

TargetExpired

Total number of Push Notification failures due to an expired target.

Any APNS Subscriber Services.

PushEnabledSessionsApns

Number of push enabled sessions for APNS clients with APNS as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates.

APNS

PushEnableReqRcvdApns

Number of push enable requests received for clients with APNS as the subscriber service, during the 60 seconds interval. This
                                          counter resets to 0 every 60 seconds.

APNS

PushErrorsApns

Number of push errors received during the 60 secondsinterval. This counter resets to 0 every 60 seconds.

APNS

PushSentSilentApns

Number of messages sent to sessions in silent mode during the 60 secondsinterval. This counter resets to 0 every 60 seconds.

APNS

PushSentDisconnApns

Number of messages sent to sessions in suspended state during the 60 secondsinterval. This counter resets to 0 every 60 seconds.

APNS

PushEnabledSessionsApnsBeta

Number of push enabled sessions for clients with APNS:beta as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates.

APNS:beta

PushEnableReqRcvdApnsBeta

Number of push enable requests received for clients with APNS:beta as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds.

APNS:beta

PushErrorsApnsBeta

Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:beta. This counter resets
                                          to 0 every 60 seconds.

APNS:beta

PushSentSilentApnsBeta

Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:beta.
                                          This counter resets to 0 every 60 seconds.

APNS:beta

PushSentDisconnApnsBeta

Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:beta.
                                          This counter resets to 0 every 60 seconds.

APNS:beta

PushEnabledSessionsApnsDev

Number of push enabled sessions for clients with APNS:dev as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates.

APNS:dev

PushEnableReqRcvdApnsDev

Number of push enable requests received for clients with APNS:dev as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds.

APNS:dev

PushErrorsApnsDev

Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:dev. This counter resets
                                          to 0 every 60 seconds.

APNS:dev

PushSentSilentApnsDev

Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:dev.
                                          This counter resets to 0 every 60 seconds.

APNS:dev

PushSentDisconnApnsDev

Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:dev.
                                          This counter resets to 0 every 60 seconds.

APNS:dev

PushEnabledSessionsApnsLoad

Number of push enabled sessions for clients with APNS:load as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates;

APNS:load

PushEnableReqRcvdApnsLoad

Number of push enable requests received for clients with APNS:load as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds.

APNS:load

PushErrorsApnsLoad

Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:load. This counter resets
                                          to 0 every 60 seconds.

APNS:load

PushSentSilentApnsLoad

Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:load.
                                          This counter resets to 0 every 60 seconds.

APNS:load

PushSentDisconnApnsLoad

Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:load.
                                          This counter resets to 0 every 60 seconds.

APNS:load

PushEnabledSessionsApnsTest

Number of push enabled sessions for clients with APNS:test as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates.

APNS:test

PushEnableReqRcvdApnsTest

Number of push enable requests received for clients with APNS:test as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds.

APNS:test

PushErrorsApnsTest

Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:test. This counter resets
                                          to 0 every 60 seconds.

APNS:test

PushSentSilentApnsTest

Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:test.
                                          This counter resets to 0 every 60 seconds.

APNS:test

PushSentDisconnApnsTest

Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:test.
                                          This counter resets to 0 every 60 seconds.

APNS:test

### Performance Counters for Android Push Notifications

The following table shows counters added to the Cisco Unified Real Time Monitoring Tool to support Android Push Notifications
                              for Unified Communications Manager and IM and Presence Service from Release 12.5(1)SU3 onwards.

Messaging counters apply to Cisco Jabber only. Cisco Webex clients use the Cisco Webex cloud for messaging rather than the
                                          IM and Presence Service.

FCM (Firebase Cloud Messaging) and FCM:dev counters increment when a push enabled Cisco Jabber or Cisco Webex clients user
                                          logs in from Android device using FCM or FCM:dev as the subscriber service.

Counter Description

Counter increments if the Subscriber service is set to...

PushEnabledSessionsFcm

Number of push enabled sessions for clients with FCM as the subscriber service.

The counter is incremented when a push enabled Cisco Jabber or Cisco Webex user logs in on Android device using FCM as subscriber
                                          service and decrements when push notifications are disabled or a client session terminates.

FCM

PushEnableReqRcvdFcm

Number of push enable requests received by the IM and Presence server for clients with FCM as the subscriber service, during
                                          the 60 seconds interval. This counter resets to 0 every 60 seconds.

FCM

PushErrorsFcm

Number of push errors received during the 60 seconds interval where the subscriber service is FCM.

This counter resets to 0 every 60 seconds.

FCM

PushSentSilentFcm

Number of messages sent to sessions in silent mode during the 60 seconds interval where the subscriber service is FCM. This
                                          counter resets to 0 every 60 seconds.

A push-enabled client session moves to silent mode when the Cisco Jabber or Cisco Webex application on the Android device
                                          goes to background.

FCM

PushSentDisconnFcm

Number of messages sent to sessions in suspended state during the 60 seconds interval where the subscriber service is FCM.

This counter resets to 0 every 60 seconds.

A push enabled client session moves to suspended state when the Cisco Jabber or Cisco Webex  application on the Android device
                                          goes to background and the network connection is terminated.

FCM

PushEnabledSessionsFcmDev

Number of push enabled sessions for clients with FCM:dev as the subscriber service.

The counter is incremented when a push enabled Cisco Jabber or Cisco Webex user logs in on Android device using FCM:dev as
                                          subscriber service and decrements when push notifications are disabled or a client session terminates.

FCM:dev

PushEnableReqRcvdFcmDev

Number of push enable requests received by the IM and Presence server for clients with FCM:dev as the subscriber service,
                                          during the 60 seconds interval. This counter resets to 0 every 60 seconds.

FCM:dev

PushErrorFcmDev

Number of push errors received during the 60 seconds interval where the subscriber service is FCM:dev.

This counter resets to 0 every 60 seconds.

FCM:dev

PushSentSilentFcmDev

Number of messages sent to sessions in silent mode during the 60 seconds interval where the subscriber service is FCM:dev.
                                          This counter resets to 0 every 60 seconds.

A push-enabled client session moves to silent mode when the Cisco Jabber or Cisco Webex application on the Android device
                                          goes to background.

FCM:dev

PushSentDisconnFcmDev

Number of messages sent to sessions in suspended state during the 60 seconds interval where the subscriber service is FCM:dev.

This counter resets to 0 every 60 seconds.

A push enabled client session moves to suspended state when the Jabber application on the Android device goes to background
                                          and the network connection is terminated.

FCM:dev

## LPNS Alarms

Important

This section is applicable from Release 14SU3 onwards.

The following table gives details of the alarms that were added to support LPNS in Unified Communications Manager .

Cisco LPNS Alarms

Description

LocalPushNotificationInvalidOAuthToken

Description: Webex client responded with invalid / expired oAuth Token. CallManager will remove the connection and stop further sending
                                       of Local Push Notification to this client.

Severity: ALERT_ALARM

Action: Verify Webex App on Mobile connection with Cisco Unified CM for updating refresh / access token.

LocalPushNotificationServiceUnavailable

Description: Unable to connect with Cisco Local Push Notification Service. The CallManager service requires a connection in order to send
                                       Local Push Notifications to the Webex App on Mobile.

Severity: CRITICAL_ALARM

Action: Try restarting Cisco Push Notification service and Cisco Local Push Notification service. If the issue persists, check the
                                       application logs for the Cisco Local Push Notification service and contact Cisco TAC for further assistance.

LocalPushStartFailed

Description: This alarm indicates that an internal failure prevented the Cisco Local Push Notification Service from starting.

Severity: ALERT_ALARM

Action: Try restarting Cisco Local Push Notification service. If the issue persists, check the application logs for the Local Push
                                       Notification service and contact Cisco TAC for further assistance.

## Performance Counters for LPNS

Important

This section is applicable from Release 14SU3 onwards.

The following table gives details of the counters added to the Cisco Unified Real Time Monitoring Tool to support LPNS for
                              on-premises deployments of Unified Communications Manager .

RTMT Counter

Counter Description

Counter increments if the Subscriber service is set to...

Cisco CallManager Counters

NumberOfLocalPushReqSent

The total number of Local Push Notification requests sent by the Cisco CallManager service. This counter will be updated from
                                       the node where the Local Push request is sent.

Any LPNS Subscriber Services.

NumberOfLocalPushResReceived

The total number of Local Push Notification responses received by the Cisco CallManager service. This counter will be updated
                                       from the node where the Local Push response is received.

Any LPNS Subscriber Services.

NumberOfLocalPushTimout

The total number of Local Push Notification requests which were timed out.

Any LPNS Subscriber Services.

NumberOfLocalPushErrorResReceived

The total number of Local Push Notification responses received by Cisco CallManager Service with error response code.

Any LPNS Subscriber Services.

NumberofMissedCallLocalPushReqSent

The total number of missed call Local Push Notification requests sent from CallManager Service to devices.

Any LPNS Subscriber Services.

NumberofSharedCancelLocalPushReqSent

The total number of cancel call Local Push Notification requests sent from CallManager Service in Shared Line scenario to
                                       devices.

Any LPNS Subscriber Services.

| Cloud hosts signed by this CA | Must be trusted by | For this purpose | Issuing CA | Fingerprint (Thumbprint) in SHA256 |
|---|---|---|---|---|
| Common Identity (CI) service | Unified Communications Manager and IM and Presence Service | Cisco Unified Communications Manager requests a CI machine token to authenticate with Cisco Push REST service. Secure https communication between Unified Communications Manager , IM and Presence Service, and the Cisco Push REST service. | O = IdenTrust CN = IdenTrust Commercial Root CA 1 | 5D 56 49 9B E4 D2 E0 8B CF CA D0 8A 3E 38 72 3D 50 50 3B DE 70 69 48 E4 2F 55 60 30 19 E5 28 AE |
| Cisco Webex | Cisco Unified Communications Manager andIM and Presence Service | Unified Communications Manager communicates with Fusion Onboarding Service (FOS) to provision CI machine account. | O = The Go Daddy Group, Inc. OU = Go Daddy Class 2 Certification Authority | C3 84 6B F2 4B 9E 93 CA 64 27 4C 0E C6 7C 1E CC 5E 02 4F FC AC D2 D7 40 19 35 0E 81 FE 54 6A E4 |

| Scenario | Installation iso file included the required certificates? | You have chosen to have Cisco manage certificate requirements | Onboarding is Successful? |
|---|---|---|---|
| Onboarding for first time | Yes | Yes | Yes |
| Onboarding for first time | No. The certificate requirements changed sometime after the installation iso was created | Yes | No. You must obtain and upload the new certificates manually. See the preceding table "Root Certificates for Cloud Connection". |
| You are already onboarded, but now a new certificate requirement has arisen | Your installation will not include the required certificates | Yes | Yes. The system can fetch and install new certificates automatically. |

| Alarm | Description |
|---|---|
| Cisco CallManager Alarms |
| PushNotificationServiceUnavailable | Description : Unable to connect with Cisco Push Notification Service. The CallManager service requires a connection in order to send Push
                                          Notifications to the Cisco Cloud. Severity : ALERT_ALARM Action : In Cisco Unified Serviceability, check that the Cisco Push Notification Service status is running. If the service is stopped,
                                          start it. If the service is running, restart it. |
| PushNotificationInvalidDeviceTokenResponse | Description : Cloud returned Error code 410 for Push Notification sent from CallManager Service due to invalid device token. Push Notification
                                          for this iOS Cisco Jabber or Cisco Webex device will be stopped until valid device token is set by iOS Cisco Jabber and Webex
                                          device. Severity : ERROR_ALARM Action : User should log out and log back in to Cisco Jabber or Webex clients on that iOS device . |
| PushNotificationServiceAccessTokenUnavailable | Description: Cisco Push Notification Service (CPNS) does not have a valid Access Token. Unified Communications Manager requires valid Access Token to send Push Notifications to Cloud. This Access Token is not available from Cloud due to authentication
                                          or network error. Severity: ALERT_ALARM Action: Check the Cisco Cloud Onboarding Configuration window to confirm that the onboarding process has completed successfully. If the issue persists contact Cisco TAC for further
                                          assistance.. |
| Cisco Push Notification Service Alarms |
| StartFailed | Description: This alarm indicates that an internal failure prevented the Cisco Push Notification Service from starting Severity: CRITICAL_ALARM Action: Try restarting the Cisco Push Notification Service. If the issue persists check the Cisco Push Notification Service application
                                          logs and contact Cisco TAC for further assistance. |
| AccessTokenInvalid | Description: This alarm indicates that current access token is expired and become invalid and new access token is unavailable. Severity: ALERT_ALARM Action: Check the Cisco Cloud Onboarding Configuration window to confirm that the onboarding process has completed successfully. If the issue persists, contact Cisco TAC for further
                                          assistance. |
| HttpClientPoolCreationError | Description: Indicates an error in creating the Http Client connection pool Severity: ALERT_ALARM Action: Check the Cisco Cloud Onboarding Configuration window and verify that the HTTP proxy settings are correct. In addition, verify that the on-boarding process has completed. |
| Cisco XCP Config Manager |
| PushNotificationFailed | Description: Cisco XCP Config Manager was not able to send Push Notification. Severity: CRITICAL_ALARM Action: Check the Error Code and follow the Error action that is directed. |
| PushNotificationFailedInvalidDeviceToken | Description: An attempt to send a Push Notification to the Cisco Cloud failed due to an invalid device token. Severity: CRITICAL_ALARM Action: User should re-login to Jabber. |
| PushNotificationFailedInvalidAccessToken | Description: An attempt to send a Push Notification to the Cisco Cloud failed due to an invalid access token. Severity: CRITICAL_ALARM Action: Look at the IM and Presence Service Cisco XCP Config Manager service logs to verify whether the AccessToken was fetched and
                                          refreshed on a timely basis. If the AccessToken was fetched and refreshed it on timely basis then do check the Cisco Cloud
                                          for further debugging. |
| AccessTokenFetchFailed | Description: Cisco XCP Config Manager was unable to fetch the Access Token. Severity: CRITICAL_ALARM Action: Check the Error Code and follow the Error action that is directed |
| XCPConfigMgrAccessTokenIsNull | Description: Cisco XCP Config Manager was unable to fetch the access token. Severity: Action: IM and Presence Service nodes must connect to the Cisco cloud to obtain the Access Token. Verify the following: Verify that the access token URL and refresh token are valid. Verify that the proxy details are correct on the Cisco Cloud Onboarding window. Check connectivity to the Cisco cloud. |
| Cisco Jabber Alarms |
| APNSAlarm | Description: An iOS Jabber client was unable to process an Push Notification. Severity: ALERT_ALARM Action: Contact Cisco TAC for further assistance. |
| Unread Messages alert Note This alert appears only in releases prior to 12.5(1). The issue is fixed as of 12.5(1). | Note | This alert appears only in releases prior to 12.5(1). The issue is fixed as of 12.5(1). | Description : An iOS Jabber client gets the following message: Unread messages might be deleted from server due to timeout. Please sign
                                          in Jabber to check unread messages. Severity: ALERT_ALARM Conditions: Cisco Jabber for iPhone running in the background. The user did not sign out of Cisco Jabber prior to closing the application. |
| Note | This alert appears only in releases prior to 12.5(1). The issue is fixed as of 12.5(1). |

| Note | This alert appears only in releases prior to 12.5(1). The issue is fixed as of 12.5(1). |
|---|---|

| RTMT Counter | Counter Description | Counter increments if the Subscriber service is set to... |
|---|---|---|
| Cisco CallManager Counters |
| NumberOfPushReqSent | The total number of Push Notification Requests sent by the Cisco CallManager Service. | Any APNS Subscriber Services. |
| NumberOfPushResReceived | The total number of Push Notification Responses received by the Cisco CallManager Service. | Any APNS Subscriber Services. |
| NumberOfPushErrorResReceived | The total number of Push Notification Responses received by Cisco CallManager Service with response code other than 200 OK. In case of TLS handshake failure between Cisco Push Notification Service (CPNS) and Cloud PushRest, this counter will be incremented
                                          for push requests which could not be sent due to TLS handshake failure. | Any APNS Subscriber Services. |
| CustomRegionNumofMsgPushReqSent | The total number of Message Push Notification requests sent from CallManager Service, when call is made to Custom Region devices,
                                          where CallKit is disabled. | Any APNS Subscriber Services. |
| CustomRegionNumofMissedCallMsgPushReqSent | The total number of missed call Message Push Notification requests sent from CallManager Service to Custom Region devices,
                                          where CallKit is disabled. | Any APNS Subscriber Services. |
| CustomRegionNumofSharedCancelMsgPushReqSent | The total number cancel call Message Push Notification requests sent from CallManager Service in Shared Line scenario to Custom
                                          Region devices, where CallKit is disabled. | Any APNS Subscriber Services. |
| Cisco Mobility Manager Counters |
| MobilityPushNotificationCallsExtendedToMIDueToTimeout | This represents the total number of calls sent to the Mobility Identity destination where Cisco Jabber or Cisco Webex did
                                          not register after receiving push notification before the "Cisco Jabber Dual Mode (iPhone) Incoming Call Push Notification
                                          Wait Timer" expired. | Any APNS Subscriber Services. |
| MobilityPushNotificationCallsExtended ToJabber | This represents the total number of calls sent to Cisco Jabber where Cisco Jabber registers successfully after receiving
                                          push notification before the "Jabber Dual Mode (iPhone) Incoming Call Push Notification Wait Timer" expired. | Any APNS Subscriber Services. |
| Cisco XCP Config Manager Counters |
| NumberOfPushSuccess | Number of successful Push Notifications sent. | Any APNS Subscriber Services. |
| NumberOfPushFailure | Number of failed attempts to send Push Notifications. | Any APNS Subscriber Services. |
| TargetInvalid | Total number of Push Notification failures due to an invalid target. | Any APNS Subscriber Services. |
| TargetExpired | Total number of Push Notification failures due to an expired target. | Any APNS Subscriber Services. |
| Cisco XCP Push Counters |
| PushEnabledSessionsApns | Number of push enabled sessions for APNS clients with APNS as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates. | APNS |
| PushEnableReqRcvdApns | Number of push enable requests received for clients with APNS as the subscriber service, during the 60 seconds interval. This
                                          counter resets to 0 every 60 seconds. | APNS |
| PushErrorsApns | Number of push errors received during the 60 secondsinterval. This counter resets to 0 every 60 seconds. | APNS |
| PushSentSilentApns | Number of messages sent to sessions in silent mode during the 60 secondsinterval. This counter resets to 0 every 60 seconds. | APNS |
| PushSentDisconnApns | Number of messages sent to sessions in suspended state during the 60 secondsinterval. This counter resets to 0 every 60 seconds. | APNS |
| PushEnabledSessionsApnsBeta | Number of push enabled sessions for clients with APNS:beta as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates. | APNS:beta |
| PushEnableReqRcvdApnsBeta | Number of push enable requests received for clients with APNS:beta as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds. | APNS:beta |
| PushErrorsApnsBeta | Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:beta. This counter resets
                                          to 0 every 60 seconds. | APNS:beta |
| PushSentSilentApnsBeta | Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:beta.
                                          This counter resets to 0 every 60 seconds. | APNS:beta |
| PushSentDisconnApnsBeta | Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:beta.
                                          This counter resets to 0 every 60 seconds. | APNS:beta |
| PushEnabledSessionsApnsDev | Number of push enabled sessions for clients with APNS:dev as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates. | APNS:dev |
| PushEnableReqRcvdApnsDev | Number of push enable requests received for clients with APNS:dev as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds. | APNS:dev |
| PushErrorsApnsDev | Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:dev. This counter resets
                                          to 0 every 60 seconds. | APNS:dev |
| PushSentSilentApnsDev | Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:dev.
                                          This counter resets to 0 every 60 seconds. | APNS:dev |
| PushSentDisconnApnsDev | Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:dev.
                                          This counter resets to 0 every 60 seconds. | APNS:dev |
| PushEnabledSessionsApnsLoad | Number of push enabled sessions for clients with APNS:load as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates; | APNS:load |
| PushEnableReqRcvdApnsLoad | Number of push enable requests received for clients with APNS:load as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds. | APNS:load |
| PushErrorsApnsLoad | Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:load. This counter resets
                                          to 0 every 60 seconds. | APNS:load |
| PushSentSilentApnsLoad | Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:load.
                                          This counter resets to 0 every 60 seconds. | APNS:load |
| PushSentDisconnApnsLoad | Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:load.
                                          This counter resets to 0 every 60 seconds. | APNS:load |
| PushEnabledSessionsApnsTest | Number of push enabled sessions for clients with APNS:test as the subscriber service. The counter is incremented when push
                                          notifications is enabled and decrements when push notifications is disabled or a session terminates. | APNS:test |
| PushEnableReqRcvdApnsTest | Number of push enable requests received for clients with APNS:test as the subscriber service, during the 60 secondsinterval.
                                          This counter resets to 0 every 60 seconds. | APNS:test |
| PushErrorsApnsTest | Number of push errors received during the 60 secondsinterval where the subscriber service is APNS:test. This counter resets
                                          to 0 every 60 seconds. | APNS:test |
| PushSentSilentApnsTest | Number of messages sent to sessions in silent mode during the 60 secondsinterval where the subscriber service is APNS:test.
                                          This counter resets to 0 every 60 seconds. | APNS:test |
| PushSentDisconnApnsTest | Number of messages sent to sessions in suspended state during the 60 secondsinterval where the subscriber service is APNS:test.
                                          This counter resets to 0 every 60 seconds. | APNS:test |

| Note | Messaging counters apply to Cisco Jabber only. Cisco Webex clients use the Cisco Webex cloud for messaging rather than the
                                          IM and Presence Service. |
|---|---|

| Note | FCM (Firebase Cloud Messaging) and FCM:dev counters increment when a push enabled Cisco Jabber or Cisco Webex clients user
                                          logs in from Android device using FCM or FCM:dev as the subscriber service. |
|---|---|

| RTMT Counter | Counter Description | Counter increments if the Subscriber service is set to... |
|---|---|---|
| Cisco XCP Push Counters |
| PushEnabledSessionsFcm | Number of push enabled sessions for clients with FCM as the subscriber service. The counter is incremented when a push enabled Cisco Jabber or Cisco Webex user logs in on Android device using FCM as subscriber
                                          service and decrements when push notifications are disabled or a client session terminates. | FCM |
| PushEnableReqRcvdFcm | Number of push enable requests received by the IM and Presence server for clients with FCM as the subscriber service, during
                                          the 60 seconds interval. This counter resets to 0 every 60 seconds. | FCM |
| PushErrorsFcm | Number of push errors received during the 60 seconds interval where the subscriber service is FCM. This counter resets to 0 every 60 seconds. | FCM |
| PushSentSilentFcm | Number of messages sent to sessions in silent mode during the 60 seconds interval where the subscriber service is FCM. This
                                          counter resets to 0 every 60 seconds. A push-enabled client session moves to silent mode when the Cisco Jabber or Cisco Webex application on the Android device
                                          goes to background. | FCM |
| PushSentDisconnFcm | Number of messages sent to sessions in suspended state during the 60 seconds interval where the subscriber service is FCM. This counter resets to 0 every 60 seconds. A push enabled client session moves to suspended state when the Cisco Jabber or Cisco Webex  application on the Android device
                                          goes to background and the network connection is terminated. | FCM |
| PushEnabledSessionsFcmDev | Number of push enabled sessions for clients with FCM:dev as the subscriber service. The counter is incremented when a push enabled Cisco Jabber or Cisco Webex user logs in on Android device using FCM:dev as
                                          subscriber service and decrements when push notifications are disabled or a client session terminates. | FCM:dev |
| PushEnableReqRcvdFcmDev | Number of push enable requests received by the IM and Presence server for clients with FCM:dev as the subscriber service,
                                          during the 60 seconds interval. This counter resets to 0 every 60 seconds. | FCM:dev |
| PushErrorFcmDev | Number of push errors received during the 60 seconds interval where the subscriber service is FCM:dev. This counter resets to 0 every 60 seconds. | FCM:dev |
| PushSentSilentFcmDev | Number of messages sent to sessions in silent mode during the 60 seconds interval where the subscriber service is FCM:dev.
                                          This counter resets to 0 every 60 seconds. A push-enabled client session moves to silent mode when the Cisco Jabber or Cisco Webex application on the Android device
                                          goes to background. | FCM:dev |
| PushSentDisconnFcmDev | Number of messages sent to sessions in suspended state during the 60 seconds interval where the subscriber service is FCM:dev. This counter resets to 0 every 60 seconds. A push enabled client session moves to suspended state when the Jabber application on the Android device goes to background
                                          and the network connection is terminated. | FCM:dev |

| Important | This section is applicable from Release 14SU3 onwards. |
|---|---|

| Cisco LPNS Alarms | Description |
|---|---|
| LocalPushNotificationInvalidOAuthToken | Description: Webex client responded with invalid / expired oAuth Token. CallManager will remove the connection and stop further sending
                                       of Local Push Notification to this client. Severity: ALERT_ALARM Action: Verify Webex App on Mobile connection with Cisco Unified CM for updating refresh / access token. |
| LocalPushNotificationServiceUnavailable | Description: Unable to connect with Cisco Local Push Notification Service. The CallManager service requires a connection in order to send
                                       Local Push Notifications to the Webex App on Mobile. Severity: CRITICAL_ALARM Action: Try restarting Cisco Push Notification service and Cisco Local Push Notification service. If the issue persists, check the
                                       application logs for the Cisco Local Push Notification service and contact Cisco TAC for further assistance. |
| LocalPushStartFailed | Description: This alarm indicates that an internal failure prevented the Cisco Local Push Notification Service from starting. Severity: ALERT_ALARM Action: Try restarting Cisco Local Push Notification service. If the issue persists, check the application logs for the Local Push
                                       Notification service and contact Cisco TAC for further assistance. |

| Important | This section is applicable from Release 14SU3 onwards. |
|---|---|

| RTMT Counter | Counter Description | Counter increments if the Subscriber service is set to... |
|---|---|---|
| Cisco CallManager Counters |
| NumberOfLocalPushReqSent | The total number of Local Push Notification requests sent by the Cisco CallManager service. This counter will be updated from
                                       the node where the Local Push request is sent. | Any LPNS Subscriber Services. |
| NumberOfLocalPushResReceived | The total number of Local Push Notification responses received by the Cisco CallManager service. This counter will be updated
                                       from the node where the Local Push response is received. | Any LPNS Subscriber Services. |
| NumberOfLocalPushTimout | The total number of Local Push Notification requests which were timed out. | Any LPNS Subscriber Services. |
| NumberOfLocalPushErrorResReceived | The total number of Local Push Notification responses received by Cisco CallManager Service with error response code. | Any LPNS Subscriber Services. |
| NumberofMissedCallLocalPushReqSent | The total number of missed call Local Push Notification requests sent from CallManager Service to devices. | Any LPNS Subscriber Services. |
| NumberofSharedCancelLocalPushReqSent | The total number of cancel call Local Push Notification requests sent from CallManager Service in Shared Line scenario to
                                       devices. | Any LPNS Subscriber Services. |