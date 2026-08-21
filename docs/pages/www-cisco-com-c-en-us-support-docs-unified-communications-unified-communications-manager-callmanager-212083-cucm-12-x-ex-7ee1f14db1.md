---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-212083-cucm-12-x-ex-7ee1f14db1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/212083-CUCM-12-X-Extension-Mobility-EM-and-Ext.html
retrieved_at: 2026-08-21T13:56:32.753280+00:00
---

CUCM 12.X Extension Mobility(EM) and Extension Mobility Cross Cluster(EMCC) Log in service URL

# CUCM 12.X Extension Mobility(EM) and Extension Mobility Cross Cluster(EMCC) Log in service URL

### Download Options

Updated: September 14, 2017

Document ID: 212083

Contents

## Contents

## Introduction

This document describe the new service Uniform Resource Locator(URL) in Cisco Unified Communication Manager(CUCM) 12.X.

## Prerequisites

Cisco Extension Mobility allows users a temporarily access their Cisco Unified IP Phone configuration such as line appearances, services, and speed dials from other Cisco Unified IP Phones. Extension Mobility supports Cisco Unified IP Phones that run SCCP and SIP.

Extension mobility functionality extends on most Cisco Unified IP Phones. You can configure each Cisco Unified IP Phone in order to support Cisco Extension Mobility at the Default Device Profile window in Cisco Unified Communications Manager Administration. This allows users who do not have a user device profile for a particular Cisco Unified IP Phone in order to use Cisco Extension Mobility with that phone.

### Requirements

This feature was introduced in CUCM 12.X.

### Components Used

CUCM version: 12.0.0.99834-5

Phone Model - 88XX

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Network Diagram

### Configurations

### Extension Mobility Service URL Configuration(EM):

You are familiar with configure the extension mobilty URL for normal log in for "User ID".

Normal EM Log in URL:

http:// <ip>:8080/emapp/EMAppServlet?device=#DEVICENAME#

Based on parameter in the Phone service URL, Extension Mobility Application serves different types of log in page for the End User.

The EM log in is now available in three different types:

- User ID

- Primary DN

- Self-Service User ID

This table helps you identify the different log in types:

#### 1. User ID (UID):

This is the service URL thatallow user log in with their User ID.

Here, UID is the log in type.

http://<ip>:8080/emapp/EMAppServlet?device=#DEVICENAME# &loginType=UID

Navigate to Device > Device Setting > Phone Services > Add New

#### How it looks on actual phone:

#### 2. Primary DN

First you need understand about What its mean by Primary DN?

So on the End user configuration page you have the optio set the Primary DN.

If you dont set the primary DN for the user and tries log in, you recieve a failure with this error:

```
Error code : 23
Error message on phone: Login is unavailable(23) / Logout is unavailable(23
```

Occurs when entered User ID (UID) / Self-Service User ID (SP) or Primary Extension (DN) is not found in database

This is the service URL to allow users to log in with their Primay DN.

http://<ip>:8080/emapp/EMAppServlet?device=#DEVICENAME# &loginType=DN

Navigate to Device > Device Setting > Phone Services > Add New

#### How it looks on actual phone:

3.Self-Service User ID

This is the ID used that manage the self care portal.

If it is not configured on the end user page, you are not allowed log in on this service URL and gives this error:

```
Error code : 23
Error message on phone: Login is unavailable(23) / Logout is unavailable(23)
```

- Occurs when entered User ID (UID) / Self-Service User ID (SP) or Primary Extension (DN) is not found in database

Service URL for the self-service User ID:

http://<ip>:8080/emapp/EMAppServlet?device=#DEVICENAME# &loginType=SP

Navigate to Device > Device Setting > Phone Services > Add New

#### How it looks on actual phone:

### Extension Mobility Cross Cluster Service URL Configuration(EMCC):

Like EM service URL, we have three types for EMCC log in as well. Here are the service URL for respective log in types.

- User ID : This is the service URL for log in EMCC.

http://<ip>:8080/emapp/EMAppServlet?device=#DEVICENAME#&EMCC=#EMCC# &loginType=UID

- Primary DN:

http://<ip>:8080/emapp/EMAppServlet?device=#DEVICENAME#&EMCC=#EMCC# &loginType=DN

- Self-Service User ID:

http://<ip>:8080/emapp/EMAppServlet?device=#DEVICENAME#&EMCC=#EMCC #&loginType=SP

Error codes for EMCC:

Common error codes for EMCC log in issues:

- Error Code: 47 Error Message on Phone : DN has multiple users(47) Occurs on EMCC log in when the Extension (Primary Extension under the end user configuration page) used for log in is assigned for multiple users

- Error Code: 1 Error Message On Phone: Login is unavailable(1) / Logout is unavailable(1) Occurs when EM Service could not parse the XML request from EMApp/EMservice Or Because of mismatch in versions between home and visiting CUCM versions.

- Error code : 23 Error message on phone: Login is unavailable(23) / Logout is unavailable(23) Occurs when entered User ID (UID) / Self-Service User ID (SP) or Primary Extension (DN) is not found in database

Note : If EMCC is configured between 12.x and any pre 12.x CUCM, the log in process only works with user id (traditional way), not with DN or Selfcare ID.

## Verify

## Troubleshoot

Collect these logs for EM/EMCC issue:

- Cisco Extension Mobility

- Cisco Extension Mobility Application

- Phone Console logs

- Packet capture from the phone

- TVS logs in details

```
Snippet for EM APP logs.
========================================================================================
Sample Snippets for Login Type "DN"

2017-08-28 21:07:04,522 INFO  [http-bio-8080-exec-10] EMAppServlet              - EMApp Request# ----->1190
2017-08-28 21:07:04,523 INFO  [http-bio-8080-exec-10] EMAppServlet              - EMAppServlet: Request protocol is :http
2017-08-28 21:07:04,523 INFO  [http-bio-8080-exec-10] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=SEP74A02FC09CDF User Id=null Device Profile=null Refresh=null Remote Host IP Address = 10.106.99.235 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,;q=0.8 Emcc = true LoginType = DN
2017-08-28 21:07:04,523 INFO  [http-bio-8080-exec-10] CMDatabase                - CMDatabase:checkDeviceAllowsAlternateScript
2017-08-28 21:07:04,551 INFO  [http-bio-8080-exec-10] CMDatabase                - SEP74A02FC09CDF with model 36224 and locale 1 does not support alternate script
2017-08-28 21:07:04,551 INFO  [http-bio-8080-exec-10] EMAppServlet              - Alternate Script for device SEP74A02FC09CDF =
2017-08-28 21:07:04,552 DEBUG [http-bio-8080-exec-10] EMServiceCommunicator     - Posting to EM Service:<query>
  <appInfo>
      <appID>CCMSysUser</appID>
      <appEncryptedCertificate>xxxxxxx</appEncryptedCertificate>
  </appInfo>
  <deviceUserQuery>
      <deviceName>SEP74A02FC09CDF</deviceName>
<loginType>DN</loginType>
     <remoteIPAddr>10.106.99.235</remoteIPAddr>
  </deviceUserQuery>
</query>
```

```
==================================================================================

Sample Snippets for Login Type "SP"

2017-08-28 22:06:05,781 INFO  [http-bio-8080-exec-24] EMAppServlet              - EMApp Request# ----->1204
2017-08-28 22:06:05,782 INFO  [http-bio-8080-exec-24] EMAppServlet              - EMAppServlet: Request protocol is :http
2017-08-28 22:06:05,782 INFO  [http-bio-8080-exec-24] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=SEP74A02FC09CDF User Id=null Device Profile=null Refresh=null Remote Host IP Address = 10.106.99.235 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,;q=0.8 Emcc = true LoginType = SP
2017-08-28 22:06:05,782 DEBUG [http-bio-8080-exec-24] EMServiceCommunicator     - Posting to EM Service:<query>
  <appInfo>
      <appID>CCMSysUser</appID>
      <appEncryptedCertificate>xxxxxxx</appEncryptedCertificate>
  </appInfo>
  <deviceUserQuery>
      <deviceName>SEP74A02FC09CDF</deviceName>
<loginType>SP</loginType>
     <remoteIPAddr>10.106.99.235</remoteIPAddr>
  </deviceUserQuery>
</query>
```

```
====================================================================================

Sample Snippets for Login Type "UID"

2017-08-29 14:48:20,657 INFO  [http-bio-8080-exec-1167] EMAppServlet              - EMApp Request# ----->10
2017-08-29 14:48:20,657 INFO  [http-bio-8080-exec-1167] EMAppServlet              - EMAppServlet: Request protocol is :http
2017-08-29 14:48:20,658 INFO  [http-bio-8080-exec-1167] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=SEP402CF4915265 User Id=null Device Profile=null Refresh=null Remote Host IP Address = 10.77.22.225 Via Header Set = false getClusterInfo = null Lang = en Charset=utf-8,utf-8;q=0.8 Emcc = null LoginType = UID
2017-05-29 14:48:20,658 DEBUG [http-bio-8080-exec-1167] EMServiceCommunicator     - Posting to EM Service:<query>

<appInfo>   
    <appID>CCMSysUser</appID>  
    <appEncryptedCertificate>xxxxxxx</appEncryptedCertificate>
</appInfo>
<deviceUserQuery>
    <deviceName>SEP74A02FC09CDF </deviceName>
<loginType>UID</loginType>   
    <remoteIPAddr>10.106.99.235</remoteIPAddr>
</deviceUserQuery>
</query>

2017-08-29 14:48:20,658 INFO  [http-bio-8080-exec-1167] EMServiceCommunicator     - Posting to EM Query Service:https://localhost:8443/emservice/EMServiceServlet
```