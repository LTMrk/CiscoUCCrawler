---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212081-jabber-log-in-failure-due-to-proxy-setti-html-a1da9df9b8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212081-Jabber-Log-in-Failure-Due-To-Proxy-Setti.html
retrieved_at: 2026-08-21T07:06:06.289559+00:00
---

Jabber Log in Failure Due To Proxy Settings

# Jabber Log in Failure Due To Proxy Settings

### Download Options

Updated: January 23, 2018

Document ID: 212081

Contents

## Contents

## Introduction

This document describes the reasons for the Cisco Jabber log in failure which is due to a proxy defined on the workstation.

## Prerequisites

### Requirement

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Instant Messaging & Presence (IM&P)

- Cisco Unified Communications Manager (CUCM)

- Cisco Jabber clients

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Jabber for Windows 11.8

- Cisco Web Security Applicance (WSA) 9.1

- CUCM 11.5

- IM&P 11.5

## Problem

Cisco Jabber Log in fails when a system proxy is defined and does not allow traffic to reach the Call Managers to download it's configuration.

```
2017-04-19 16:30:30,565 INFO [0x000013b0] [etutils\src\http\CurlHttpUtils.cpp(1088)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - *-----* Configuring request #20 GET https://cucm.cisco.com:8443/cucm-uds/version 2017-04-19 16:30:30,565 DEBUG [0x000013b0] [etutils\src\http\CurlHttpUtils.cpp(1472)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - Request #20 configured with: connection timeout 10000 msec, transfer timeout 0 msec 2017-04-19 16:30:30,565 DEBUG [0x000013b0] [netutils\src\http\CurlHttpUtils.cpp(188)] [csf.httpclient] [csf::http::CurlHttpUtils::curlTraceCallback] - Request #20 pre connect phase: ' Trying ::1...' 2017-04-19 16:30:30,768 DEBUG [0x000013b0] [netutils\src\http\CurlHttpUtils.cpp(188)] [csf.httpclient] [csf::http::CurlHttpUtils::curlTraceCallback] - Request #20 pre connect phase: ' Trying 127.0.0.1...' 2017-04-19 16:30:30,770 DEBUG [0x000013b0] [netutils\src\http\CurlHttpUtils.cpp(192)] [csf.httpclient] [csf::http::CurlHttpUtils::curlTraceCallback] - Request #20 post connect phase: 'Connected to localhost (127.0.0.1) port 3128 (#1)' 2017-04-19 16:30:35,229 INFO [0x00000380] [lugin-runtime\impl\HangDetector.cpp(150)] [PluginRuntime-HangDetector] [HangDetector::hangDetectionCallback] - Enter - hangDetectionCallback() 2017-04-19 16:30:35,913 DEBUG [0x000013b0] [netutils\src\http\CurlHttpUtils.cpp(733)] [csf.httpclient] [csf::http::CurlHttpUtils::curlHeaderCallback] - Request #20 got status line: HTTP/1.1 503 Service Unavailable 2017-04-19 16:30:35,913 DEBUG [0x000013b0] [netutils\src\http\CurlHttpUtils.cpp(713)] [csf.httpclient] [csf::http::CurlHttpUtils::curlHeaderCallback] - Request #20 got CR-LF pair. Accumulated headers: Mime-Version: Redacted by client Date: Wed, 19 Apr 2017 16:30:35 AEST Via: 1.1 proxy-rtp-1.cisco.com:80 (Cisco-WSA/9.1.1-074) Content-Type: text/html Connection: keep-alive Proxy-Connection: keep-alive Content-Length: 2410 2017-04-19 16:30:35,913 INFO [0x000013b0] [ls\src\http\CurlAnswerEvaluator.cpp(115)] [csf.httpclient] [csf::http::CurlAnswerEvaluator::curlCodeToResult] - Request #20 got curlCode=[56] curl error message="[ Received HTTP code 503 from proxy after CONNECT ]" HttpClientResult=[UNKNOWN_ERROR] fips enabled=[false] 2017-04-19 16:30:35,913 INFO [0x000013b0] [ls\src\http\BasicHttpClientImpl.cpp(452)] [csf.httpclient] [csf::http::executeImpl] - *-----* HTTP response code 0 for request #20 to https://cucm.cisco.com:8443/cucm-uds/version 2017-04-19 16:30:35,913 ERROR [0x000013b0] [ls\src\http\BasicHttpClientImpl.cpp(457)] [csf.httpclient] [csf::http::executeImpl] - There was an issue performing the call to curl_easy_perform for request #20: UNKNOWN_ERROR
```

## Solution 1

You can configure the client to bypass the proxy and go directly to Call Manager in the exceptions section of proxy settings; naviagate to Control Panel > Network and Internet > Internet Options > Connection > LAN Settings > Advanced

You can define the exceptions by asterisk's (*) and then your domain, by an individual IP Address, or a range; e.g. *.MY.Domain; 192.168.1.1; 192.168.1.12-14.

## Solution 2

Configure the Proxy to redirect traffic sourced from the Jabber Client to redirect to the appropriate Call Manager.

## Solution 3

Remove the proxy configuration from the windows client, then have the HTTP GET method from Jabber bypass the proxy and all other traffic sourced from the PC. This is dependant on the network flow from the client to the Call Manager and would be nullified if the infrastructure inbetween is sends web traffic via Web Cache Communication Protocol (WCCP).

## Verify

Check the proxy settings on the workstation.

Step 1. You verify the proxy configuration from the command line; navigate to command prompt and run the command netsh winhttp show proxy

Step 2. You can navigate to Control Panel > Network and Internet > Internet Options > Connections > LAN Settings .

- When there is no proxy:

- When there is a proxy:

Step 3. Run the command " regedit " and navigate to HKEY_CURRENT_USER > Software > Microsoft > Windows > CurrentVersion > Internet Settings

- When a proxy is not defined:

- When a Proxy is defined:

### Contributed by Cisco Engineers

Aseem Anand

Cisco TAC Engineer

Edited by Harry Doyle and Jasmeet Sandhu

Cisco TAC Engineers

### This Document Applies to These Products

- Jabber