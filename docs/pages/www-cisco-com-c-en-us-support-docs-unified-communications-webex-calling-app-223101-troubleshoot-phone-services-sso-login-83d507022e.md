---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-app-223101-troubleshoot-phone-services-sso-login-83d507022e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling-app/223101-troubleshoot-phone-services-sso-login.html
retrieved_at: 2026-08-21T07:16:06.377287+00:00
---

Troubleshoot Phone Services SSO Login Failure on iOS Webex App

# Troubleshoot Phone Services SSO Login Failure on iOS Webex App

### Download Options

Updated: June 16, 2025

Document ID: 223101

Contents

## Contents

## Introduction

This document describes troubleshooting Webex Phone Services SSO Login Failure on Webex application for iOS.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub

- Webex App

- Calling in Webex (Unified CM)

- Cisco Unified Communications Manager (CUCM)

### Components Used

The information in this document is based on these software and hardware versions:

- Webex App version 43.12

- CUCM version 14.0.1.10000-20

- IOS version 17.2.1

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document describes troubleshooting Webex Phone Services SSO Login Failure on Webex application for iOS. You are unable to log in to Phone services on Webex app running on iPhone (iOS), when Single Sign On (SSO) is enabled. Phone Services log in works fine when using an Android device, as well as while using a Windows system. Issue persists even after re-installing the mobile Webex application on iOS.

Mobile Remote Access (MRA) is not involved in the log in flow. All attempts to log in to phone services are being made on the corporate network. Single Sign On (SSO) is enabled on Webex as well as on the CUCM.

When you navigate to Phone services menu in the Webex app, it shows the error "Phone service is disconnected". Clicking Sign In just shows Connecting for about 10-15 seconds, followed by a blank page and it does not proceed further. Attempt is made to log in on another iPhone as well, however, the same result is observed. You are able to log in to CUCM Web GUI on Chrome (using SSO) from your iPhone.

Log in Flow:

Webex app on iPhone (iOS) > Corporate network > CUCM

## Troubleshooting Steps

- When the issue is reproduced, note the exact time stamp.

2. Proceed to collect the Webex app logs, including the Calling Environment Data (CED) file as well. The instructions are mentioned here .

3. Navigate to Control Hub > Services > Calling > Client Settings > Unified CM Settings .

Proceed to validate if the setting Allow Unified CM registration without trusted certificate is checked on Control Hub.

Allow Unified CM Registration Without Trusted Certificate Setting on Control Hub

Details are mentioned here .

4. If it is toggled off , ensure to toggle it on , save the settings and proceed to make a test again.

## Logs Analysis

When reviewing the logs, you can see log lines pointing to certificate related errors, navigation to secure URL failed errors, and an error pointing out that secure connection to the server cannot be made:

```
2024-02-01 05:48:33,461 ERROR [0x6d4ab000] [ls/src/cert/ios/iOSCertVerifier.cpp(189)] [csf.cert.ios] [verifyCertificatePolicy] - Policy verification failed, the urls of CRL Distribution Points and Authority Information Access might be unreachable, result=5 2024-02-01 05:48:33,461 ERROR [0x6d4ab000] [ls/src/cert/ios/iOSCertVerifier.cpp(189)] [csf.cert.ios] [verifyCertificatePolicy] - Policy verification failed, the urls of CRL Distribution Points and Authority Information Access might be unreachable, result=5 2024-02-01 05:48:33,461 INFO  [0x6d4ab000] [mmon/PlatformVerificationHandler.cpp(38)] [csf.cert] [handlePlatformVerificationResultSynchronously] - Verification result : FAILURE reason : [CN_NO_MATCH UNKNOWN] 2024-02-01 05:48:33,480 INFO  [0x6d4ab000] [vices/impl/DiscoveryHandlerImpl.cpp(668)] [service-discovery] [evaluateServiceDiscoveryResult] - ServiceDiscoveryHandlerResult return code FAILED_UCM90_CREDENTIALS_NOT_SET 2024-02-01T05:48:33.551Z <Error> [0x84953][]WebViewController.swift:358 webView(_:didFailProvisionalNavigation:withError:):Provisional Navigation failed: An SSL error has occurred and a secure connection to the server cannot be made. 2024-02-01 05:49:03,567 INFO  [0x6e36f000] [rvices/impl/BrowserListenerImpl.cpp(120)] [BrowserListener-Logger] [SecureOnNavigationCompleted] - OnNavigationCompleted( UnknownError ) 2024-02-01 05:49:03,567 INFO  [0x6e36f000] [rvices/impl/BrowserListenerImpl.cpp(120)] [BrowserListener-Logger] [SecureOnNavigationCompleted] - OnNavigationCompleted( UnknownError ) 2024-02-01 05:49:03,568 DEBUG [0x6e36f000] [vices/impl/system/SingleSignOn.cpp(1091)] [Single-Sign-On-Logger] [authorizeNext] - SsoAuthRequest #1 not finished 2024-02-01T05:49:04.711Z <Error> [0x84953][]WebViewController.swift:358 webView(_:didFailProvisionalNavigation:withError:):Provisional Navigation failed: An SSL error has occurred and a secure connection to the server cannot be made.
```

The above log lines are observed in the current_log.txt and uclogin files, present within the Webex app logs.

## Root Cause

The root cause behind the issue is the certificate validation failure (certificate not trusted by client) and also SSL error has occurred and a secure connection to the server cannot be made. You are using internal Certificate Authority (CA) signed CUCM Tomcat certificates (multi SAN) and not using public CA signed certificates. Tomcat certificates on CUCM include FQDNs in the name.

## Solution

Internal CA signed certificates are not supported by iOS. It is required that you use an enterprise root CA. You also need to ensure that the Certificate Revocation List (CRL) of custom root CA is reachable. More details are found here .

R e-doing the Tomcat certificate with CA signed, resolves the issue. You are now able to log in to Phone services on iOS Webex App.

## Related Information

- Deployment Guide For Calling in Webex App (Unified CM)

- Webex App Error Messages For Calling

### Revision History

1.0

16-Jun-2025

Initial Release

### Contributed by Cisco Engineers

Jagatbir Singh Jaijee

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Calling

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Jun-2025 | Initial Release |