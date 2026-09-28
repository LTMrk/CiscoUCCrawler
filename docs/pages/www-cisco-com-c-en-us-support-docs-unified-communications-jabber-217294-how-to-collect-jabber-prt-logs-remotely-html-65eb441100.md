---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-217294-how-to-collect-jabber-prt-logs-remotely-html-65eb441100
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/217294-how-to-collect-jabber-prt-logs-remotely.html
retrieved_at: 2026-08-20T22:13:54.804529+00:00
---

How to collect Jabber PRT Logs Remotely

# How to collect Jabber PRT Logs Remotely

### Download Options

Updated: August 5, 2021

Document ID: 217294

Contents

## Contents

## Introduction

This document describes how to configure c ollection of Jabber Problem Report Tool (PRT) logs remotely.Instead of waiting for a user to upload the PRT logs, you can also generate the logs remotely in Unified CM Administration.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Platform: Windows/Mac

- Jabber 12.9 and later

- CUCM Requirements:12.5.1.SU1 and later

- Hyper Text Transfer Protocol (HTTP) Server

- Headset Requirements: sunkist and version greater than 1-3(if has headset)

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM 12.5SU4

- Jabber 12.9

- Jabber installed on windows 10

- HTTP Server (Apache server on linux)

## Configure

### Network Diagram

### Configurations

#### Before you begin

Complete the following steps to prepare your environment:

Install and configure an HTTP server. In this document we are using Apache server on Linux(CentOS)

Create a custom script to accept the HTTP POST request.

- $target_dir = "/var/www/html/JabberPRT/uploads/" this is the location where PRT will be saved , we can use any path & same path needs to be mentioned in code, make sure folder or directory which we are using can be accessed by Apache process & proper permission to write in that folder.

Create an HTML page that enables users to upload problem reports that are saved locally. Your HTML page should contain a form that accepts the problem report saved as a .ZIP archive and contains an action to post the problem report using your custom script. The following is an example form that accepts problem report

- action=" http://server_name/path_of_script " in this we are pointing to script which we have created in Step 2 to handle POST request.

- Once we have all in place we can test by uploading any file manually by accesing the HTTP server via. browser.

Step 1

Open Cisco Unified CM Administration> Select User Management > User Setting > UC Service.

Step 2

Add a new UC service with a UC Service Type of Jabber Client Configuration (jabber-config.xml).

Step 3

Add a Jabber Configuration Parameter with these values:

Section —Policies

Parameter —RemotePRTServer

Value —The URL for your upload script( http://10.106.120.10/upload.php )

## Verify

Step 1

Select Device > Phone. Step 2

Choose the devices for which you need logs. Step 3

Click Generate PRT for selected.

Step 4

To check the PRT collected access your HTTP server and check the directory (/var/www/html/JabberPRT/uploads/) which you have mentioned in your script

## Troubleshoot

Below are the basic troubleshooting checks

```
NOTIFY sip:0008@10.106.120.5:51038 SIP/2.0 Via: SIP/2.0/TCP 10.106.120.2:5060;branch=z9hG4bK1273e54f34755 From: <sip:10.106.120.2>;tag=1284645402 To: <sip:0008@10.106.120.5> Call-ID: e7fc3880-1ed10efb-12732-2786a0a@10.106.120.2 CSeq: 101 NOTIFY Max-Forwards: 70 Date: Fri, 30 Jul 2021 05:42:22 GMT User-Agent: Cisco-CUCM12.5 Event: service-control Subscription-State: active Contact: <sip:10.106.120.2:5060;transport=tcp> Content-Type: text/plain Content-Length: 86 action=prt-report RegisterCallId={005056bd-e9d90009-00000f98-000014d7@10.106.120.5}
```

- Log Example

```
2021-07-29 22:41:27,917 INFO [0x00001260] [ipcc\core\sipstack\ccsip_platform.c(250)] [csf.sip-call-control] [sip_platform_reset_req] - SIPCC-SIP_REG_STATE: sip_platform_reset_req: ***********DEVICE_PRT_REPORT, requested*********** 2021-07-29 22:41:27,917 DEBUG [0x000052c8] [ftphonewrapper\CC_SIPCCService.cpp(7463)] [csf.ecc] [csf::ecc::CC_SIPCCService::serviceRequest] - service = CC_DEVICE_PRT_REPORT 2021-07-29 22:41:27,917 INFO [0x000055dc] [control\CallControlManagerImpl.cpp(4553)] [csf.ecc] [csf::ecc::CallControlManagerImpl::onPRTReport] - notify prt report event 2021-07-29 22:41:27,917 DEBUG [0x000055dc] [ntrol\TelephonyCallControlImpl.cpp(6919)] [jcf.tel.callcontrol] [CSFUnified::TelephonyCallControlImpl::onPRTReport] - onPRTReport 2021-07-29 22:41:27,917 DEBUG [0x00004b9c] [ntrol\TelephonyCallControlImpl.cpp(6928)] [jcf.tel.callcontrol] [CSFUnified::TelephonyCallControlImpl::onPRTReportImpl] - onPRTReport 2021-07-29 22:41:27,917 DEBUG [0x00004b9c] [honyAdapterCallControlObserver.cpp(1284)] [jcf.tel.ccobserver] [CSFUnified::TelephonyAdapter::onPRTReportChange] - onPRTReportChange 2021-07-29 22:41:27,917 DEBUG [0x00004b9c] [src\framework\ServicesDispatcher.cpp(38)] [services-dispatcher] [CSFUnified::ServicesDispatcher::enqueue] - ServicesDispatcher.enqueue: TelephonyServiceImpl::notifyOnPRTStart 2021-07-29 22:41:27,917 DEBUG [0x00004968] [rc\framework\ServicesDispatcher.cpp(207)] [services-dispatcher] [CSFUnified::ServicesDispatcher::executeTask] - executing (TelephonyServiceImpl::notifyOnPRTStart) 2021-07-29 22:41:27,917 DEBUG [0x00004968] [ices\impl\TelephonyServiceImpl.cpp(5060)] [jcf.tel.service] [CSFUnified::TelephonyServiceImpl::notifyOnPRTStart] - TelephonyServiceImpl:: notifyOnPRTStart 2021-07-29 22:41:27,917 DEBUG [0x00004968] [c\plugin-runtime\impl\jabberprt.cpp(486)] [PluginRuntime] [JabberPrtImpl::setPRTConfig] - Setting Config:ProblemReportToolOnPrem to 0xTrue 2021-07-29 22:41:27,917 DEBUG [0x00004a88] [src\framework\ServicesDispatcher.cpp(38)] [services-dispatcher] [CSFUnified::ServicesDispatcher::enqueue] - ServicesDispatcher.enqueue: OnFlushCompleted 2021-07-29 22:41:27,917 DEBUG [0x00004968] [gins\hubwindowplugin\prtlistener.cpp(10)] [HubWindowPlugin] [CPrtListener:: onPRTStart ] - received remote amdin upload prt request
```

- Try uploading PRT directly from a web browser using the machine in question.

- Verify antivirus software or firewall isn’t preventing the request.

- We can verify the access request on Apache server as well & check the errors in case of CentOS path is /var/log/httpd/

- Make sure post-max-size of php is enough to accept large size of PRT as well we can modify the same from php.ini

## Related Information

Problem Reporting Feature Configuration for Cisco Jabber 12.9

### Revision History

1.0

05-Aug-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Aug-2021 | Initial Release |