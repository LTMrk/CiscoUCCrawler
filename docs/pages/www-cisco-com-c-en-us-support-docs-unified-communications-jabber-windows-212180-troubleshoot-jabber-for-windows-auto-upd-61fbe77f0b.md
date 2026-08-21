---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-212180-troubleshoot-jabber-for-windows-auto-upd-61fbe77f0b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/212180-Troubleshoot-Jabber-for-Windows-auto-upd.html
retrieved_at: 2026-08-21T06:59:58.244460+00:00
---

Troubleshoot Jabber for Windows auto-update over MRA

# Troubleshoot Jabber for Windows auto-update over MRA

### Download Options

Updated: October 4, 2017

Document ID: 212180

Contents

## Contents

## Introduction

This document describes how to troubleshoot auto-update failure of Jabber Windows over MRA from 11.7(x) to 11.8.

## Problem: Upgrade Issue over MRA from 11.7.0 to 11.8.x

You try to upgrade Jabber client automatically over MRA from 11.7.0 to 11.8.x. However, it fails even though an update window appears. Whereas, auto-upgrade of 11.6 to 11.8 works fine.

## Troubleshoot

### Log Analysis from the Non-Working Scenario:

- Transformed the autoupdate.xml file URL:

```
DEBUG [0x00001f14] [tutils\adapters\EdgeUtilsAdapter.cpp(39)] [csf.netutils.adapters] [csf::netutils::adapters::EdgeUtilsAdapter::transformRequest] - About to transformRequest with Url [http://10.106.108.146:6970/Autoupdate.xml]
DEBUG [0x00001f14] [ls\src\edge\GlobalEdgeStateImpl.cpp(780)] [csf.edge] [csf::edge::GlobalEdgeStateImpl::checkPrecondition] - Acquired scoped lock (visibilityMutex_)
```

- Updated transformed URL:

```
DEBUG [0x00001f14] [tutils\adapters\EdgeUtilsAdapter.cpp(63)] [csf.netutils.adapters] [csf::netutils::adapters::EdgeUtilsAdapter::transformRequest] - Transformed Urls:https://vcse-test.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/Autoupdate.xml https://vcse-mum.hpcl.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/Autoupdate.xml
```

```
DEBUG [0x000014e8] [ntrol\FeatureSetEventManagerImpl.cpp(87)] [IMPServices-PresenceAdapter.FeatureSetEventManager] [CSFUnified::FeatureSetEventManagerImpl::flushQueue] - Adding 0 deferred events to the service dispatcher
INFO  [0x0000162c] [onstabs\generaltab\src/AutoStart.cpp(34)] [AutoStart] [AutoStart::DetermineExecutablePath] - The executable path for the client is C:\Program Files\Cisco Systems\Cisco Jabber\CiscoJabber.exe
```

- Upgrade information with the download link:

```
DEBUG [0x0000162c] [erupgradeplugin\UpgradesListener.cpp(80)] [JabberUpgradePlugin] [UpgradesListener::OnUpdateChecked] - Received update information. Version number: 11.8.2 Build number: 50390 Download link: http://10.106.108.146:6970/CiscoJabberSetup.msi Upgrade rule:  UpgradeAvailable: 1 UpgradeMandatory: 0
INFO  [0x00000b20] [\cpve\src\main\connectionfactory.cpp(46)] [cpve] [CSF::media::rtp::ConnectionFactoryImpl::ConnectionFactoryImpl] - Created a new ConnectionFactory 0x099f7ef8.
```

- Upgrade dialog box:

```
DEBUG [0x0000162c] [gradeplugin\JabberUpgradeDialog.cpp(591)] [JabberUpgradePlugin] [JabberUpgradeDialog::OnUpdateInformationReceived] - Received update information. Version number: 11.8.2 Build number: 50390 Download link: http://10.106.108.146:6970/CiscoJabberSetup.msi Upgrade rule:  UpgradeMandatory: 0 AllowUpdatesOverEdge: 0

 
DEBUG [0x0000162c] [gradeplugin\JabberUpgradeDialog.cpp(314)] [JabberUpgradePlugin] [JabberUpgradeDialog::DownloadInstaller] - Temporary filename is: C:\Users\SACHIN~1\AppData\Local\Temp\CiscoJabberSetup.msi.temp
```

- Jabber is not transforming the download link for the msi installer:

```
DEBUG [0x00001b64] [ls\src\http\BasicHttpClientImpl.cpp(136)] [csf.httpclient] [csf::http::BasicHttpClientImpl::AsyncTask::execute] - Edge policy enforced successfully with transformed Url:http://10.106.108.146:6970/CiscoJabberSetup.msi for request #28
 
DEBUG [0x00001b64] [etutils\src\http\HttpRequestData.cpp(73)] [csf.httpclient] [csf::http::HttpRequestData::consumeEasyCURLConnection] - Acquired lock (_easyCurlConnectionMutex)
 
DEBUG [0x0000162c] [facade\IJabberToolbarEventsImpl.cpp(285)] [PluginRuntime] [IJabberToolbarEventsImpl::onToolbarContextChanged] - Enqueuing event - CallerPluginID=105
 
DEBUG [0x00001b64] [etutils\src\http\HttpRequestData.cpp(82)] [csf.httpclient] [csf::http::HttpRequestData::consumeEasyCURLConnection] - Releasing lock (_easyCurlConnectionMutex)
```

- Sending the MSI installer URL directly to the TFTP server and it fails.

INFO  [0x00001b64] [etutils\src\http\CurlHttpUtils.cpp(1088)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - *-----* Configuring request #28 GET http://10.106..108.146:6970/CiscoJabberSetup.msi

- Jabber client get HTTP response 0 for the request and host unreachable error:

```
INFO  [0x00001b64] [ls\src\http\BasicHttpClientImpl.cpp(452)] [csf.httpclient] [csf::http::executeImpl] - *-----* HTTP response code 0 for request #28 to http://10.106.108.146:6970/CiscoJabberSetup.msi
ERROR [0x00001b64] [ls\src\http\BasicHttpClientImpl.cpp(457)] [csf.httpclient] [csf::http::executeImpl] - There was an issue performing the call to curl_easy_perform for request #28: HOST_UNREACHABLE_ERROR
```

### Working Scenario:

- Downloading the jabber setup:

```
DEBUG [0x0000253c] [erupgradeplugin\UpgradesListener.cpp(43)] [JabberUpgradePlugin] [UpgradesListener::OnUpdateChecked] - Received update information. Version number: 11.8.2 Build number: 50390 Download link: http://10.106.108.146:6970/CiscoJabberSetup.msi Upgrade rule:  UpgradeAvailable: 1 UpgradeMandatory: 0
 
DEBUG [0x0000253c] [gradeplugin\JabberUpgradeDialog.cpp(554)] [JabberUpgradePlugin] [JabberUpgradeDialog::OnUpdateInformationReceived] - Received update information. Version number: 11.8.2 Build number: 50390 Download link: http://10.106.108.146:6970/CiscoJabberSetup.msi Upgrade rule:  UpgradeMandatory: 0
INFO  [0x0000253c] [win\src\ceb\src\trident/trident.cpp(218)] [ceb.trident] [trident::CTrident::stopNavigation] - Attempting to call stop on the browser - checking if the browser is navigating
 
DEBUG [0x0000253c] [gradeplugin\JabberUpgradeDialog.cpp(275)] [JabberUpgradePlugin] [JabberUpgradeDialog::DownloadInstaller] - Starting download
2017-03-27 15:53:31,554 DEBUG [0x0000253c] [gradeplugin\JabberUpgradeDialog.cpp(289)] [JabberUpgradePlugin] [JabberUpgradeDialog::DownloadInstaller] - Temporary filename is: C:\Users\Abhishek\AppData\Local\Temp\CiscoJabberSetup.msi.temp
 
 
DEBUG [0x00002540] [tutils\adapters\EdgeUtilsAdapter.cpp(39)] [csf.netutils.adapters] [csf::netutils::adapters::EdgeUtilsAdapter::transformRequest] - About to transformRequest with Url [http://10.106.108.146:6970/CiscoJabberSetup.msi]
2017-03-27 15:53:31,555 DEBUG [0x00002540] [ls\src\edge\GlobalEdgeStateImpl.cpp(774)] [csf.edge] [csf::edge::GlobalEdgeStateImpl::checkPrecondition] - Acquired scoped lock (visibilityMutex_
 
DEBUG [0x00002540] [tutils\adapters\EdgeUtilsAdapter.cpp(63)] [csf.netutils.adapters] [csf::netutils::adapters::EdgeUtilsAdapter::transformRequest] - Transformed Urls:https://vcse-test1.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi https://vcse-hyd.hpcl.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi
 
DEBUG [0x00002540] [tutils\adapters\EdgeUtilsAdapter.cpp(63)] [csf.netutils.adapters] [csf::netutils::adapters::EdgeUtilsAdapter::transformRequest] - Transformed Urls:https://vcse-test1.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi https://vcse-hyd.hpcl.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi
DEBUG [0x00002540] [\common\ScopedWinSockInitialiser.cpp(50)] [csf.netutils.common] [csf::ip::ScopedWinSockInitialiser::ScopedWinSockInitialiser] - Winsock.dll details - Description: WinSock 2.0, System Status: Running.
 
DEBUG [0x00002540] [ls\src\http\BasicHttpClientImpl.cpp(132)] [csf.httpclient] [csf::http::BasicHttpClientImpl::AsyncTask::execute] - Edge policy enforced successfully with transformed Url:https://vcse-test1.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi for request #101
 
DEBUG [0x00002540] [etutils\src\http\HttpRequestData.cpp(73)] [csf.httpclient] [csf::http::HttpRequestData::consumeEasyCURLConnection] - Acquired lock (_easyCurlConnectionMutex)
 
DEBUG [0x00002540] [etutils\src\http\HttpRequestData.cpp(82)] [csf.httpclient] [csf::http::HttpRequestData::consumeEasyCURLConnection] - Releasing lock (_easyCurlConnectionMutex)
INFO  [0x00002540] [etutils\src\http\CurlHttpUtils.cpp(1087)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - *-----* Configuring request #101 GET https://vcse-test1.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi
 
INFO  [0x00002540] [etutils\src\http\CurlHttpUtils.cpp(1732)] [csf.httpclient] [csf::http::CurlHeaders::CurlHeaders] - Number of Request Headers : 1
2017-03-27 15:53:31,556 DEBUG [0x00002540] [etutils\src\http\CurlHttpUtils.cpp(1143)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - Successfully test-opened file with write option C:\Users\Abhishek\AppData\Local\Temp\CiscoJabberSetup.msi.temp
 
DEBUG [0x00002540] [tutils\src\http\HttpRequestData.cpp(111)] [csf.httpclient] [csf::http::HttpRequestData::switchToNextUrl] - switching to next url: https://vcse-test.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi
```

- Sending the request for MSI installer.

```
INFO  [0x00002540] [etutils\src\http\CurlHttpUtils.cpp(1087)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - *-----* Configuring request #101 GET https://vcse-test.ucis.co.in:8443/aHBjbC5jby5pbi9odHRwLzEwLjE1LjAuMzMvNjk3MA/CiscoJabberSetup.msi
 
INFO  [0x00002540] [etutils\src\http\CurlHttpUtils.cpp(1732)] [csf.httpclient] [csf::http::CurlHeaders::CurlHeaders] - Number of Request Headers : 1
DEBUG [0x00002540] [etutils\src\http\CurlHttpUtils.cpp(1143)] [csf.httpclient] [csf::http::CurlHttpUtils::configureEasyRequest] - Successfully test-opened file with write option C:\Users\Abhishek\AppData\Local\Temp\CiscoJabberSetup.msi.temp
DEBUG [0x00002540] [netutils\src\http\CurlHttpUtils.cpp(986)] [csf.httpclient] [csf::http::CurlHttpUtils::closeFile] - Closing file
```

## Solution

This parameter should be added in the jabber update file under Jabberupdate parameter explicitly from jabber version 11.7 for a successful auto-upgrade over MRA. Until Jabber version 11.6, it is enabled by default:

<AllowUpdatesViaExpressway>true</AllowUpdatesViaExpressway>

This document defect is also opened here:

http://cdets.cisco.com/apps/dumpcr?content=summary&format=html&identifier=CSCvd85090

### Contributed by Cisco Engineers

Pooja Gupta

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Windows