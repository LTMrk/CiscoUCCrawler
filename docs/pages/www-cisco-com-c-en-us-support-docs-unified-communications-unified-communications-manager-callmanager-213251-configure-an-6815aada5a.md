---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213251-configure-an-6815aada5a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213251-configure-and-troubleshoot-extension-mob.html
retrieved_at: 2026-08-21T13:57:22.485419+00:00
---

Configure and Troubleshoot Extension Mobility for Log Analysis

# Configure and Troubleshoot Extension Mobility for Log Analysis

Updated: April 26, 2018

Document ID: 213251

Contents

## Contents

## Introduction

This document describes how to troubleshoot and be able to do log analysis for Cisco Extension Mobility.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM version: 12.0.0.99834-4

- Phone Model : CIPC 8.6.6.1

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When users roam between sites and do not have their phone with them, they might want to use any available phone at the site in order to which they have travelled. Most common issues that arise includes wrong extension numbers, calling privileges, etc as shown in the image.

## Cisco EM Operation

When a user wants to log in to a phone, this sequence of events occur:

- The user presses the Services button on the phone and chooses the Cisco EM Mobility service from the list of phone services that are available on the phone

- The Cisco EM service requires the user to log in by using a user ID and PIN. The user enters the required data.

- If the entered user ID and PIN are correct, Cisco EM chooses the device profile that is associated with that user. If a user is associated with multiple device profiles, the user must choose which device profile to use.

- CUCM updates the phone configuration with the settings of the chosen device profile. User-specific device-level parameters, lines, and other phone buttons are updated with user-specific settings

- The IP Phone is reset and loads the updated configuration

Users can log out of Cisco EM by pressing the Services button and choosing Logout in the Cisco EM service. If the users do not logout themselves, the system automatically logs them out after the expiration of the maximum login time (if appropriate service parameter has been configured accordingly)

## Configure

- Activate the Cisco Extension Mobility service.

- Set Cisco Extension Mobility service parameters.

- Add the Cisco EM phone service.

- Create default device profile for all the phone models used (optional).

- Create device profiles and subscribe them to the Cisco EM phone service.

- Create end users and associate them with device profiles.

- Enable Cisco EM for phones and subscribe phones to the Cisco EM service.

For detailed configuration steps, refer this link:

https://supportforums.cisco.com/t5/collaboration-voice-and-video/configuring-extension-mobility-on-cucm-10-x/ta-p/3137666

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

Collect these debug level logs:

- Call manager logs (debug level)

- Extension Mobility (debug level)

- Extension Mobility Application (debug level)

- Tomcat logs

- Tomcat Security logs

- Event Viewer System logs

- Event Viewer Application logs

- Phone console logs

Along with these logs, make a note of the details as follows:

- MAC address of the phone on which issue occurred

- IP address of the phone on which issue occurred

- User ID

- Time of login

### Log Analysis

```
Details:

User ID:EMuser

Normal DN: 7777

Device profile DN: 8888

Phone Name: test_secure (CIPC)

Time of login: 19:10

Phone IP: 192.168.0.105

PC IP on which CIPC running: 10.65.40.61

Publisher IP: 10.106.111.182
```

This section describes what all events need to be seen in the traces mentioned:

#### In Tomcat Security Logs

```
### Login Constructor

 

2018-04-14 19:10:51,961 DEBUG [http-bio-8080-exec-23] authentication.AuthenticationImpl - successfully read propertyfile - classname is com.cisco.security.ims.impl.CUCMUtil

2018-04-14 19:10:51,962 DEBUG [http-bio-8080-exec-23] authentication.AuthenticationImpl - login: Entering login

2018-04-14 19:10:51,962 DEBUG [http-bio-8080-exec-23] authentication.AuthenticationImpl - loginUtil: Authenticating against DB.

2018-04-14 19:10:51,962 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - Constructor:

 

### Authenticate user

2018-04-14 19:10:51,962 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - authenticateUser: userId=EM**** isLogin true

2018-04-14 19:10:51,962 DEBUG [http-bio-8080-exec-23] security.Log4jEncLogger - Entering HashTextSHA

 

### Authentication for the user is TRUE and CUCM checks that EMuser is a valid end user. Authentication complete with result =0; 0 means successful and 1 means not successful

2018-04-14 19:10:51,992 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - authenticateUser: Authentication Match.

2018-04-14 19:10:51,992 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - authenticateUser:Resetting last login time and Hack count..

2018-04-14 19:10:51,992 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - Calling combined API End user

2018-04-14 19:10:52,007 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - Authentication Sucessful .. Returning true

2018-04-14 19:10:52,007 DEBUG [http-bio-8080-exec-23] impl.AuthenticationDB - authenticateUser: userId=EMuser is a valid END user.

2018-04-14 19:10:52,009 DEBUG [http-bio-8080-exec-23] authentication.AuthenticationImpl - loginUtil: Authentication complete with result=0
```

#### In EM Service Logs

```
### Request for device (here name of phone is test_secure; otherwise it will be the MAC address here)

 

2018-04-14 19:09:45,772 INFO  [http-bio-8443-exec-23] DBRequestor               - 5:Querying device user for device test_secure

2018-04-14 19:09:45,772 INFO  [http-bio-8443-exec-23] DBRequestor               - 5:Getting device object - three params

2018-04-14 19:09:45,772 INFO  [http-bio-8443-exec-23] DBRequestor               - 5: DBRequestor.queryDeviceUser: Dev: 'test_secure' - Getting device object

2018-04-14 19:09:45,793 DEBUG [http-bio-8443-exec-23] CMDatabase                - CMDatabase:getDeviceInfo(): SELECT COUNT(pkid) as count from emccdynamic where my_lower(devicename) = my_lower(?) :: Parameter ('test_secure')

2018-04-14 19:09:45,795 DEBUG [http-bio-8443-exec-23] CMDatabase                - CMDatabase:getDeviceInfo(): SELECT device.pkid, loginduration,decode(emremotedynamic.logintime, null, extensionmobilitydynamic.logintime, emremotedynamic.logintime) logintime, allowhotelingflag, decode(remoteuserid, null, e2.userid, remoteuserid) currentuserid, decode(lastremoteuserid, null, e1.userid, lastremoteuserid) lastuserid, extensionmobilitydynamic.tkuserlocale, fkdevicepool, tkdeviceprotocol, tkproduct, tkmodel FROM Device left outer join extensionmobilitydynamic on device.pkid=extensionmobilitydynamic.fkdevice left outer join emremotedynamic on (extensionmobilitydynamic.fkdevice=emremotedynamic.fkdevice) left outer join enduser e1 on (extensionmobilitydynamic.fkenduser_lastlogin=e1.pkid) left outer join enduser e2 on (extensionmobilitydynamic.fkenduser=e2.pkid) where my_lower(device.name) = my_lower(?) :: Parameter ('test_secure')

2018-04-14 19:09:45,798 INFO  [http-bio-8443-exec-23] CMDatabase                - getDeviceInfo:Result of the query: {tkproduct=30041, loginduration=, lastuserid=, tkdeviceprotocol=11, pkid=d72b2e5f-5dd2-51fc-ec50-c9daf98aab66, tkmodel=30016, logintime=, currentuserid=, allowhotelingflag=t, fkdevicepool=1b1b9eb6-7803-11d3-bdf0-00108302ead1, tkuserlocale=}

2018-04-14 19:09:45,798 INFO  [http-bio-8443-exec-23] DBRequestor               - 5: DBRequestor.queryDeviceUser: Dev: 'test_secure' - Device object returned

2018-04-14 19:09:45,798 INFO  [http-bio-8443-exec-23] DBRequestor               - 5: QueryDeviceUser: Device Logged out

2018-04-14 19:09:45,799 INFO  [http-bio-8443-exec-23] DBRequestor               - 5:Device query info contains userid=

2018-04-14 19:09:45,799 INFO  [http-bio-8443-exec-23] DBRequestor               - 5:Device query info contains last login userid=

2018-04-14 19:09:45,800 DEBUG [http-bio-8443-exec-23] EMServiceServlet          - 5: executeQuery complete.

2018-04-14 19:09:45,800 DEBUG [http-bio-8443-exec-23] EMServiceServlet          - 5:Query completed, returning<response>

<deviceUserResults>

<device name="test_secure">

<none/>

<none/>

<emccDevice>no</emccDevice>

</device>

</deviceUserResults>

</response>

<!DOCTYPE query SYSTEM "http://10.106.111.182:8080/emservice/jsp/LoginQuery.dtd">

<query><appInfo><appID>CCMSysUser</appID><appEncryptedCertificate>***** </appInfo><checkUser><userID>EMuser</userID><remoteIPAddr>10.65.40.61</remoteIPAddr><isViaHeaderSet>false</isViaHeaderSet></checkUser></query>

 

### CUCM sends that EMuser is a local user

 

2018-04-14 19:10:51,940 DEBUG [http-bio-8443-exec-4] CMDatabase                - Userid being passed to the query is EMuser

2018-04-14 19:10:51,941 DEBUG [http-bio-8443-exec-4] CMDatabase                - CMDatabase.isLocalUser() : SELECT islocaluser FROM EndUser WHERE my_lower(userid)= my_lower(?) : parameter ( 'EMuser' )

2018-04-14 19:10:51,947 DEBUG [http-bio-8443-exec-4] CMDatabase                -  PKID for the ROW is

2018-04-14 19:10:51,948 DEBUG [http-bio-8443-exec-4] CMDatabase                -  CMDatabase.isLocalUser() : isLocaluser : true

2018-04-14 19:10:51,949 DEBUG [http-bio-8443-exec-4] EMServiceServlet          - 6:Query completed, returning<response>

<checkUserResults>

<user id="EMuser">

<exists>EMuser</exists>

</user>

</checkUserResults>

</response>

 

### Login request

 

2018-04-14 19:10:52,061 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7:EM Service: Request type=Login/Logout

2018-04-14 19:10:52,062 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7: LoginService.processRequest: Received Request

2018-04-14 19:10:52,062 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7:Parsing Request...

2018-04-14 19:10:52,063 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7:Request-><?xml version="1.0"?>

 

### Login process

 

2018-04-14 19:10:52,095 DEBUG [http-bio-8443-exec-21] EMServiceServlet          - 7: processXMLRequest: EMuser: EM2

2018-04-14 19:10:52,095 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7:Finished Parsing XML request

2018-04-14 19:10:52,095 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7:Executing Login...

 

2018-04-14 19:10:52,133 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7: LoginService.executeLogin: Dev: test_secure- Sending request to DB

2018-04-14 19:10:52,133 DEBUG [http-bio-8443-exec-21] DBRequestor               - 7: LoginInfo.profile is NULL

2018-04-14 19:10:52,133 INFO  [http-bio-8443-exec-21] DBRequestor               - 7: 'DBRequestor.login': Dev: 'test_secure' - Getting device profile object

2018-04-14 19:10:52,134 INFO  [http-bio-8443-exec-21] CMDatabase                - CMDatabase:getProfileInfo: ###: SELECT pkid from Device WHERE my_lower(name) = my_lower(?) : parameter ( 'EM2' )

2018-04-14 19:10:52,135 DEBUG [http-bio-8443-exec-21] CMDatabase                - CMDatabase:getProfileInfo: PKID for device : 0bff3cfd-13c1-5352-1a39-9188bdd855d8

2018-04-14 19:10:52,136 INFO  [http-bio-8443-exec-21] DBRequestor               - 7: DBRequestor.login: Dev: test_secure- Device profile object returned

2018-04-14 19:10:52,136 INFO  [http-bio-8443-exec-21] DBRequestor               - 7: DBRequestor.login: Dev: test_secure- Calling deviceLogin(d72b2e5f-5dd2-51fc-ec50-c9daf98aab66, 0bff3cfd-13c1-5352-1a39-9188bdd855d8, EMuser, 0, false, 0)

2018-04-14 19:10:52,136 INFO  [http-bio-8443-exec-21] CMDatabase                - CMDatabase:deviceLogin()

 

### Login successful

 

2018-04-14 19:10:52,137 DEBUG [http-bio-8443-exec-21] CMDatabase                - Userid being passed to the query is EMuser

2018-04-14 19:10:52,139 INFO  [http-bio-8443-exec-21] CMDatabase                - CMDatabase:deviceLogin: execute function DeviceLogin ('d72b2e5f-5dd2-51fc-ec50-c9daf98aab66','0bff3cfd-13c1-5352-1a39-9188bdd855d8','181a09dd-9e03-2acb-c107-c1156e171e88','0','0','f')

2018-04-14 19:10:52,466 INFO  [http-bio-8443-exec-21] DBRequestor               - 7: DBRequestor.login: Dev: test_secure- deviceLogin returned

2018-04-14 19:10:52,467 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7: LoginService.executeLogin: Dev: test_secure- Login Successful

2018-04-14 19:10:52,467 INFO  [http-bio-8443-exec-21] EMServiceServlet          - 7:Request succeeded returning<?xml version="1.0"?>

<response>

<success/>

</response>

 

### Logout request

 

2018-04-14 19:11:23,919 INFO  [http-bio-8443-exec-3] EMServiceServlet          - EMService Request# ----> : 9

2018-04-14 19:11:23,920 DEBUG [http-bio-8443-exec-3] EMServiceServlet          - 9: Conn. Via Header= null

2018-04-14 19:11:23,920 DEBUG [http-bio-8443-exec-3] EMServiceServlet          - 9: osHost is localHostAddress = 10.106.111.182

2018-04-14 19:11:23,920 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9:EM Service: Request type=Login/Logout

2018-04-14 19:11:23,920 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9: LoginService.processRequest: Received Request

2018-04-14 19:11:23,920 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9:Parsing Request...

 

### Logout process

 

2018-04-14 19:11:23,925 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9:Executing Logout...

2018-04-14 19:11:23,925 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9:Executing Logout for device=test_secure

2018-04-14 19:11:23,925 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9: Executing authenticate2...

 

### Logout successful

 

2018-04-14 19:11:23,936 INFO  [http-bio-8443-exec-3] CMDatabase                - CMDatabase:deviceLogout()

2018-04-14 19:11:23,936 INFO  [http-bio-8443-exec-3] CMDatabase                - CMDatabase:deviceLogout: execute function DeviceLogout ('d72b2e5f-5dd2-51fc-ec50-c9daf98aab66')

2018-04-14 19:11:24,122 INFO  [http-bio-8443-exec-3] DBRequestor               - 9: DBRequestor.logout: Dev: test_secure- deviceLogout returned

2018-04-14 19:11:24,122 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9: LoginService.executeLogout: Dev: test_secure- Logout Successful

2018-04-14 19:11:24,122 INFO  [http-bio-8443-exec-3] EMServiceServlet          - 9:Request succeeded returning<?xml version="1.0"?>

<response>

<success/>

</response>
```

#### In EmApp Logs

```
2018-04-14 19:09:45,566 INFO  [http-bio-8080-exec-10] EMAppServlet              - EMApp Request# ----->5

2018-04-14 19:09:45,567 INFO  [http-bio-8080-exec-10] EMAppServlet              - EMAppServlet: Request protocol is :http

2018-04-14 19:09:45,567 INFO  [http-bio-8080-exec-10] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=test_secure User Id=null Device Profile=null Refresh=null Remote Host IP Address = 10.65.40.61 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,iso-8859-1;q=0.8 Emcc = null LoginType = null

2018-04-14 19:09:45,568 INFO  [http-bio-8080-exec-10] CMDatabase                - CMDatabase:checkDeviceAllowsAlternateScript

2018-04-14 19:09:45,580 INFO  [http-bio-8080-exec-10] CMDatabase                - test_secure with model 30016 and locale 1 does not support alternate script

2018-04-14 19:09:45,580 INFO  [http-bio-8080-exec-10] EMAppServlet              - Alternate Script for device test_secure =

2018-04-14 19:09:45,581 DEBUG [http-bio-8080-exec-10] EMServiceCommunicator     - Posting to EM Service:<query>

  <appInfo>

      <appID>CCMSysUser</appID>

      <appEncryptedCertificate>xxxxxxx</appEncryptedCertificate>

  </appInfo>

  <deviceUserQuery>

      <deviceName>test_secure</deviceName>

     <remoteIPAddr>10.65.40.61</remoteIPAddr>

  </deviceUserQuery>

</query>

2018-04-14 19:09:45,581 INFO  [http-bio-8080-exec-10] EMServiceCommunicator     - Posting to EM Query Service: https://localhost:8443/emservice/EMServiceServlet

2018-04-14 19:09:45,581 DEBUG [http-bio-8080-exec-10] EMServiceCommunicator     - postMsg: EMService URL is :

https://localhost:8443/emservice/EMServiceServlet

2018-04-14 19:09:45,808 INFO  [http-bio-8080-exec-10] EMAppServlet              - The login status result for :test_secure:null:null:null:no

2018-04-14 19:09:45,809 INFO  [http-bio-8080-exec-10] CMDatabase                - CMDatabase:checkDeviceAllowsAlternateScript

2018-04-14 19:09:45,811 INFO  [http-bio-8080-exec-10] CMDatabase                - test_secure with model 30016 and locale 1 does not support alternate script

 

 

2018-04-14 19:09:45,812 INFO  [http-bio-8080-exec-10] EMAppServlet              - Sent login page for device test_secure

2018-04-14 19:09:45,812 INFO  [http-bio-8080-exec-10] EMAppServlet              - findPreferredCharSet on utf-8,iso-8859-1;q=0.8

2018-04-14 19:09:45,812 INFO  [http-bio-8080-exec-10] EMAppServlet              - token1 = utf-8

2018-04-14 19:09:45,812 INFO  [http-bio-8080-exec-10] EMAppServlet              -  token2 = utf-8

2018-04-14 19:09:45,813 INFO  [http-bio-8080-exec-10] EMAppServlet              -  charset with q value is 1 utf-8

2018-04-14 19:09:45,813 INFO  [http-bio-8080-exec-10] EMAppServlet              -  returning charset as q value is 1 utf-8

2018-04-14 19:09:45,813 INFO  [http-bio-8080-exec-10] EMAppServlet              -  my charset =utf-8

2018-04-14 19:10:51,885 INFO  [http-bio-8080-exec-23] EMAppServlet              - EMApp Request# ----->6

2018-04-14 19:10:51,886 INFO  [http-bio-8080-exec-23] EMAppServlet              - EMAppServlet: Request protocol is :http

2018-04-14 19:10:51,886 INFO  [http-bio-8080-exec-23] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=test_secure User Id=EMuser Device Profile=null Refresh=null Remote Host IP Address = 10.65.40.61 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,iso-8859-1;q=0.8 Emcc = null LoginType = null

2018-04-14 19:10:51,894 DEBUG [http-bio-8080-exec-23] EMAppServlet              - isUserLocal: userid = EMuser

2018-04-14 19:10:51,895 DEBUG [http-bio-8080-exec-23] EMServiceCommunicator     - Posting to EM Service:<query><appInfo><appID>CCMSysUser</appID><appEncryptedCertificate>xxxxxxx </appEncryptedCertificate></appInfo><checkUser><userID>EMuser</userID><remoteIPAddr>10.65.40.61</remoteIPAddr><isViaHeaderSet>false</isViaHeaderSet></checkUser></query>

2018-04-14 19:10:51,895 INFO  [http-bio-8080-exec-23] EMServiceCommunicator     - Posting to EM Query Service:https://localhost:8443/emservice/EMServiceServlet

2018-04-14 19:10:51,896 DEBUG [http-bio-8080-exec-23] EMServiceCommunicator     - postMsg: EMService URL is :

https://localhost:8443/emservice/EMServiceServlet

 

 

 

2018-04-14 19:10:51,957 DEBUG [http-bio-8080-exec-23] XMLGenParser              - XMLUtil.getDocumentFromStream

2018-04-14 19:10:51,957 DEBUG [http-bio-8080-exec-23] XMLGenParser              - XMLUtil.getValueFromDocument

2018-04-14 19:10:51,958 INFO  [http-bio-8080-exec-23] EMAppServlet              - User 'EMuser' exists locally

2018-04-14 19:10:51,958 INFO  [http-bio-8080-exec-23] EMAppServlet              - EM Request for EMuser

2018-04-14 19:10:52,010 INFO  [http-bio-8080-exec-23] EMAppServlet              - User authentication complete for user EMuser

2018-04-14 19:10:52,011 DEBUG [http-bio-8080-exec-23] CMDatabase                - Userid being passed to the query is EMuser

2018-04-14 19:10:52,011 DEBUG [http-bio-8080-exec-23] CMDatabase                - CMDatabase.getEndUserInfo - Query is - SELECT Device.name, Device.tkDeviceProfile, EndUserDeviceMap.defaultprofile FROM Device INNER JOIN EndUserDeviceMap ON Device.pkid = EndUserDeviceMap.fkDevice WHERE EndUserDeviceMap.fkEndUser = (SELECT pkid FROM EndUser WHERE my_lower(userid)=my_lower(?)) and device.tkDeviceProfile=1 AND EndUserDeviceMap.tkuserassociation = ? : parameter ( 'EMuser' )

2018-04-14 19:10:52,014 DEBUG [http-bio-8080-exec-23] CMDatabase                - CMDatabase.getEndUserInfo - name : EM2

2018-04-14 19:10:52,025 INFO  [http-bio-8080-exec-23] EMAppServlet              - Device profiles for user:EMuser=UserInfo:  UserID: EMuser Password:  Locale: 1 Authentication proxy rights: falseDevice Profiles:  EM2

2018-04-14 19:10:52,026 DEBUG [http-bio-8080-exec-23] EMServiceCommunicator     - Posting to EM Service:<request>

 

 

2018-04-14 19:10:52,471 INFO  [http-bio-8080-exec-23] EMAppServlet              - Successfully performed Login for user EMuser at test_secure

2018-04-14 19:10:52,472 INFO  [http-bio-8080-exec-23] EMAppServlet              - findPreferredCharSet on utf-8,iso-8859-1;q=0.8

 

 

2018-04-14 19:11:23,896 INFO  [http-bio-8080-exec-13] EMAppServlet              - EMApp Request# ----->9

2018-04-14 19:11:23,897 INFO  [http-bio-8080-exec-13] EMAppServlet              - EMAppServlet: Request protocol is :http

2018-04-14 19:11:23,897 INFO  [http-bio-8080-exec-13] EMAppServlet              - EMApp Request parameters: Logout=true Device Name=test_secure User Id=null Device Profile=null Refresh=null Remote Host IP Address = 10.65.40.61 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,iso-8859-1;q=0.8 Emcc = true LoginType = null

2018-04-14 19:11:23,899 DEBUG [http-bio-8080-exec-13] EMServiceCommunicator     - Posting to EM Service:<request>

  <appInfo>

      <appID>CCMSysUser</appID>

      <appEncryptedCertificate>xxxxxxx</appEncryptedCertificate>

  </appInfo>

  <logout>

      <deviceName>test_secure</deviceName>

      <remoteIPAddr>10.65.40.61</remoteIPAddr>

      <isViaHeaderSet>false</isViaHeaderSet>

  </logout>

</request>

2018-04-14 19:11:23,900 INFO  [http-bio-8080-exec-13] EMServiceCommunicator     - postMsgToLoginService: Service URL :https://localhost:8443/emservice/EMServiceServlet

2018-04-14 19:11:23,900 DEBUG [http-bio-8080-exec-13] EMServiceCommunicator     - postMsg: EMService URL is :

https://localhost:8443/emservice/EMServiceServlet

2018-04-14 19:11:24,126 INFO  [http-bio-8080-exec-13] EMAppServlet              - Successfully performed Logout for user null at test_secure

2018-04-14 19:11:24,127 DEBUG [http-bio-8080-exec-13] EMAppServlet              - EMCC: true
```

#### In Call Manager Logs

```
### The device profile DN (here 8888)

 

02760565.000 |19:11:08.329 |SdlSig   |CtiDeviceRegisterNotifyWithLineInfo    |wait                           |CTIRegistrar(1,100,237,1)        |SIPStationD(1,100,76,128)        |1,100,14,8722.2^10.65.40.61^test_secure  |[R:N-H:0,N:1,L:2,V:0,Z:0,D:0]  deviceName=test_secure EventContent=14 DeviceConfigInfo= Locale=1 AltScrpt= DNDOption=0 ConfigIpAddrMode=3 Hotelling=T Restricted=F OutboundRO=0 BIB=F DNDStatus=F LoginStatus=1 DeviceRegistrationInfo= TerminateMedia=5 ActiveIPAddrMode=0 IPv4=1761650880 IPv6= LoginUser=EMuser ProfilePkid=0bff3cfd-13c1-5352-1a39-9188bdd855d8 Encoding=3 CtiControllable=1 AppCapability=52 UserCapability=20Protocol=2 MultiMediaCapabilityBitMask=3 DeviceMultiMediaInfo= DeviceVideoCapability=0 TelepresenceInfo=0 ScreenCount=0 HuntLogStatus=1 TotalLines=1 LineCount=1 MoreLines=F DN = 8888 Part =  PkGpDN =  PkGpPart =  num RD = 0 StationPid(1,100,76,128) CTIHandlerId(0) LoginStatus=1

 

### Request for registering the phone for DN mentioned in the device profile

 

02760551.004 |19:11:08.219 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.65.40.61 on port 57378 index 12386 with 2203 bytes:

[101339,NET]

REGISTER sip:10.106.111.182 SIP/2.0

Via: SIP/2.0/TCP 192.168.0.105:57378;branch=z9hG4bK00007806

From: <sip:8888@10.106.111.182>;tag=005056c000010926000036cb-00003151

To: <sip:8888@10.106.111.182>

Call-ID: 005056c0-0001027b-00001cf2-00001201@192.168.0.105

Max-Forwards: 70

Date: Sat, 14 Apr 2018 13:40:19 GMT

CSeq: 2151 REGISTER

User-Agent: Cisco-SIPIPCommunicator/9.1.1

Contact: <sip:f5927b99-efa0-d1a0-8705-e11d9e2ebf0b@192.168.0.105:57378;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+u.sip!devicename.ccm.features.cisco.com="test_secure";+u.sip!model.ccm.cisco.com="30016"

Supported: replaces,join,sdp-anat,norefersub,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-5.1.0,X-cisco-xsi-8.5.1

Reason: SIP;cause=200;text="cisco-alarm:14 Name=SEP005056C00001 Load=CIPC-8-6-6-1 Last=cm-closed-tcp"

Expires: 3600

Content-Type: multipart/mixed; boundary=uniqueBoundary

Mime-Version: 1.0

Content-Length: 1073

 

--uniqueBoundary

Content-Type: application/x-cisco-remotecc-request+xml

Content-Disposition: session;handling=optional

 

<?xml version="1.0" encoding="UTF-8"?>

<x-cisco-remotecc-request>

<bulkregisterreq>

<contact all="true">

<register></register>

</contact>

</bulkregisterreq>

</x-cisco-remotecc-request>

 

--uniqueBoundary

Content-Type: application/x-cisco-remotecc-request+xml

Content-Disposition: session;handling=optional

 

<?xml version="1.0" encoding="UTF-8"?>

<x-cisco-remotecc-request>

 <optionsind>

  <combine max="6">

   <remotecc>

    <status></status>

   </remotecc>

   <service-control></service-control>

  </combine>

  <dialog usage="hook status">

   <unot></unot>

   <sub></sub>

  </dialog>

  <dialog usage="shared line">

   <unot></unot>

   <sub></sub>

  </dialog>

  <presence usage="blf speed dial">

   <unot></unot>

   <sub></sub>

  </presence>

  <joinreq></joinreq>

  <cfwdall-anyline>No</cfwdall-anyline>

  <coaching></coaching>

  <oosalarm></oosalarm>

 </optionsind>

</x-cisco-remotecc-request>

 

 

### 200 OK

 

02760584.001 |19:11:08.334 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.65.40.61 on port 57378 index 12386

[101341,NET]

SIP/2.0 200 OK

Via: SIP/2.0/TCP 192.168.0.105:57378;branch=z9hG4bK00007806;received=10.65.40.61

From: <sip:8888@10.106.111.182>;tag=005056c000010926000036cb-00003151

To: <sip:8888@10.106.111.182>;tag=1168208381

Date: Sat, 14 Apr 2018 13:41:08 GMT

Call-ID: 005056c0-0001027b-00001cf2-00001201@192.168.0.105

Server: Cisco-CUCM12.0

CSeq: 2151 REGISTER

Expires: 120

Contact: <sip:f5927b99-efa0-d1a0-8705-e11d9e2ebf0b@192.168.0.105:57378;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+u.sip!devicename.ccm.features.cisco.com="test_secure";+u.sip!model.ccm.cisco.com="30016";x-cisco-newreg

Supported: X-cisco-srtp-fallback,X-cisco-sis-9.0.0

Content-Type: application/x-cisco-remotecc-response+xml

Content-Length: 367

 

<x-cisco-remotecc-response>

<response>

<code>200</code>

<optionsind>

<combine max="6">

<remotecc><status/></remotecc>

<service-control/>

</combine>

<dialog usage="hook status"><unot/></dialog>

<dialog usage="shared line"><unot/></dialog>

<presence usage="blf speed dial"><unot/></presence>

<joinreq></joinreq>

</optionsind>

</response>

</x-cisco-remotecc-response>

 

 

### After logout the device again registers with its normal DN (7777)

 

02760738.004 |19:11:36.004 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.65.40.61 on port 57417 index 12389 with 2203 bytes:

[101342,NET]

REGISTER sip:10.106.111.182 SIP/2.0

Via: SIP/2.0/TCP 192.168.0.105:57417;branch=z9hG4bK00002532

From: <sip:7777@10.106.111.182>;tag=005056c00001092900001fb0-00000fc1

To: <sip:7777@10.106.111.182>

Call-ID: 005056c0-00010285-000046e9-00006cf9@192.168.0.105

Max-Forwards: 70

Date: Sat, 14 Apr 2018 13:40:47 GMT

CSeq: 2153 REGISTER

User-Agent: Cisco-SIPIPCommunicator/9.1.1

Contact: <sip:479c83c3-cb54-18e8-1ba1-06a9d6b9e33c@192.168.0.105:57417;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+u.sip!devicename.ccm.features.cisco.com="test_secure";+u.sip!model.ccm.cisco.com="30016"

Supported: replaces,join,sdp-anat,norefersub,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-5.1.0,X-cisco-xsi-8.5.1

Reason: SIP;cause=200;text="cisco-alarm:14 Name=SEP005056C00001 Load=CIPC-8-6-6-1 Last=cm-closed-tcp"

Expires: 3600

Content-Type: multipart/mixed; boundary=uniqueBoundary

Mime-Version: 1.0

Content-Length: 1073

 

--uniqueBoundary

Content-Type: application/x-cisco-remotecc-request+xml

Content-Disposition: session;handling=optional

 

<?xml version="1.0" encoding="UTF-8"?>

<x-cisco-remotecc-request>

<bulkregisterreq>

<contact all="true">

<register></register>

</contact>

</bulkregisterreq>

</x-cisco-remotecc-request>

 

--uniqueBoundary

Content-Type: application/x-cisco-remotecc-request+xml

Content-Disposition: session;handling=optional

 

<?xml version="1.0" encoding="UTF-8"?>

<x-cisco-remotecc-request>

 <optionsind>

  <combine max="6">

   <remotecc>

    <status></status>

   </remotecc>

   <service-control></service-control>

  </combine>

  <dialog usage="hook status">

   <unot></unot>

   <sub></sub>

  </dialog>

  <dialog usage="shared line">

   <unot></unot>

   <sub></sub>

  </dialog>

  <presence usage="blf speed dial">

   <unot></unot>

   <sub></sub>

  </presence>

  <joinreq></joinreq>

  <cfwdall-anyline>No</cfwdall-anyline>

  <coaching></coaching>

  <oosalarm></oosalarm>

 </optionsind>

</x-cisco-remotecc-request>

 

 

### 200 OK

 

02760759.001 |19:11:36.114 |AppInfo  |//SIP/SIPNormalization/trace_sip_message: Before outbound SIP Normalization msg is:

[101344,INT]

SIP/2.0 200 OK

Via: SIP/2.0/TCP 192.168.0.105:57417;branch=z9hG4bK00002532;received=10.65.40.61

From: <sip:7777@10.106.111.182>;tag=005056c00001092900001fb0-00000fc1

To: <sip:7777@10.106.111.182>;tag=983899518

Date: Sat, 14 Apr 2018 13:41:36 GMT

Call-ID: 005056c0-00010285-000046e9-00006cf9@192.168.0.105

Server: Cisco-CUCM12.0

CSeq: 2153 REGISTER

Expires: 120

Contact: <sip:479c83c3-cb54-18e8-1ba1-06a9d6b9e33c@192.168.0.105:57417;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+sip.instance="<urn:uuid:00000000-0000-0000-0000-005056c00001>";+u.sip!devicename.ccm.features.cisco.com="test_secure";+u.sip!model.ccm.cisco.com="30016";x-cisco-newreg

Supported: X-cisco-srtp-fallback,X-cisco-sis-9.0.0

Content-Type: application/x-cisco-remotecc-response+xml

Content-Length: 367

 

<x-cisco-remotecc-response>

<response>

<code>200</code>

<optionsind>

<combine max="6">

<remotecc><status/></remotecc>

<service-control/>

</combine>

<dialog usage="hook status"><unot/></dialog>

<dialog usage="shared line"><unot/></dialog>

<presence usage="blf speed dial"><unot/></presence>

<joinreq></joinreq>

</optionsind>

</response>

</x-cisco-remotecc-response>
```

## Common Defects for Extension Mobility

- CSCuv93330 : tvsGetNextThread() returned NULL

- CSCur57864 : 8841/8851 Secured Extension Mobility login intermittently fails

- CSCvb98664 : The timestamp will show in UTC even if other time zone is configured

- CSCuo94742 : CCM Device layer is always using English locales after EM login

- CSCuo13456 : Extension Mobility: Phones are limited to enter up to 32 characters on 78xx & 88xx

- CSCtz28748 : When logging into extension mobility gets Login unsuccessful Unknown 7

- CSCtx18810 : CIPC is not supporting secure EM (HTTPS login for EM)

- CSCue33973 : Tomcat high CPU / memory - AXL Throttling leak causing excessive queries

- CSCug88643 : CME: Extension Mobility: Support for SIP phones in different subnet

- CSCuo99592 : 7841 Intermittently will not login to Extension Mobility

- CSCug94607 : getDeviceProfile response gives error code -1

- CSCud97811 : Extensionmobilitydynamic entries not deleted on EM Logout

### Extension Mobility Error Codes

This document describes the error codes that are commonly experienced:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/8_6_1/trbl861/tbfeat.pdf

### Common Errors Experienced

This document describes common errors along with their fix:

https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/18772-extension-mobility.html

### Contributed by Cisco Engineers

Prerna Bagga

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)