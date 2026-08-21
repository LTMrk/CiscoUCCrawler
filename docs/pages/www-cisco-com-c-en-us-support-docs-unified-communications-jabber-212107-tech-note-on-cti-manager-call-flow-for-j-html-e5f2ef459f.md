---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212107-tech-note-on-cti-manager-call-flow-for-j-html-e5f2ef459f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212107-Tech-Note-on-CTI-Manager-Call-Flow-for-J.html
retrieved_at: 2026-08-21T07:06:10.365758+00:00
---

Tech Note on CTI Manager Call Flow for Jabber Deskphone Control Request

# Tech Note on CTI Manager Call Flow for Jabber Deskphone Control Request

### Download Options

Updated: September 18, 2017

Document ID: 212107

Contents

## Contents

## Introduction

This document describes the detailed Call flow for successful Computer Telephony Integration (CTI) Manager Authentication for Jabber Desktop Clients

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Lightweight Directory Access Protocol (LDAP)

- Computer Telephony Integration (CTI)

### Components Used

The information in this document is based on these software versions:

- Cisco Jabber for Windows 11.5

- Cisco Unified Communications Manager (CUCM) 10.5(2) and above

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## CTI Messaging for Jabber Deskphone Control

Ensure CTI Manager service logs are set to Debug level, reproduce the problem, then collect logs via command line or Real Time Monitoring Tool (RTMT). Follow the steps here to verify CTI Authentication

Step 1. Provider Open Request from the Jabber client is received by the CTI Manager service.

```
00895255.002 |08:59:16.944 |AppInfo |[CTI-APP] [CTIHandler::processIncomingMessage] CTI ProviderOpenRequest ( seq#=2 provider=UCProvider login=wwhite heartbeat=60 timer=10 priority=0 lightWeightProviderOpen=0 AuthType=0 RequestOldFetch=0 EncryptedSSODataSize=0)
00895256.000 |08:59:16.944 |SdlSig |CtiProviderOpenReq |init_complete_await_provopen |CTIHandler(1,200,22,7) |CTIHandler(1,200,22,7) |1,200,13,8.3^*^* |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Async Response=2 ProviderName=UCProvider ClientVersion=UCProvider LoginId=wwhite ApplName=Shibui ServerHeartbeat=60 CMAssignedAppId=1234 PluginName=Cisco JTAPI LightWeightProviderOpen=0 Auth Style=0 RequestOldFetch=0
00895256.001 |08:59:16.944 |AppInfo |SSOTOKEN =
00895256.002 |08:59:16.944 |AppInfo |CQBEBuilder::BuildQbeMessage(): objectID=2
00895256.003 |08:59:16.944 |AppInfo |CTIHandler::OutputQbeMessage: TcpHand=[1:200:13:8] QbePref={0x0xf74b346c,0x70} pQbeMsg=0x0xf74b3474 qbeMsgSize=0x70 tmpLen=0x78 msgSize_=0x78
```

Step 2. Provider Open Response is sent to Jabber client.

```
00895256.004 |08:59:16.944 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI ProviderOpenResponse (seq#=2) provider id=16777223 FIPSMode = 0
```

Step 3. The process of end user authentication is started.

```
00895260.000 |08:59:17.057 |SdlSig |CtiProceedWithAppLogin |init_complete_await_auth |CTIHandler(1,200,22,7) |CtiManager(1,200,21,1) |1,200,13,8.3^*^* |[R:L-H:0,N:0,L:0,V:0,Z:0,D:0]
00895261.000 |08:59:17.058 |SdlSig |CtiLoginCheckReq |ready |Directory(1,200,23,1) |CTIHandler(1,200,22,7) |1,200,13,8.3^*^* |[T:N-H:0,N:0,L:0,V:0,Z:0,D:0] Login=wwhite Seq#=2 Auth Style=0 3rd Party Certificate=0 mOcsp_url= mIssuerName= EncryptedSingleSignOnData Size=0
00895261.001 |08:59:17.058 |AppInfo |CtiLoginCheckReq:: authenticateByUserName
```

Step 4. Key decryption takes place and must be successful before the authentication attempt.

```
00895261.002 |08:59:17.058 |AppInfo |CCMAsymmetricEncryption::DecryptText Enter
00895261.003 |08:59:17.067 |AppInfo |CCMAsymmetricEncryption::DecryptText Exit
00895261.004 |08:59:17.067 |AppInfo | Decrypted Key Status success - [52] 00895261.005 |08:59:17.067 |AppInfo |Nonce =cc64fd13-d4e1-43bc-808f-f051f7c945d0
00895261.006 |08:59:17.067 |AppInfo |Nonce validation success
00895261.007 |08:59:17.067 |AppInfo |CCMSymmetricEncryption::DecryptText:enter
00895261.008 |08:59:17.067 |AppInfo | CCMEncryption::DecryptText (Exit) (Success)) 00895261.009 |08:59:17.067 |AppInfo | Decrypted Password Status success - [8]
```

Step 5. Username is retrieved and used for authentication along with the password.

```
00895261.010 |08:59:17.067 |AppInfo |AuthenticationImpl::login:enter
00895261.011 |08:59:17.067 |AppInfo |AuthenticationImpl::retrieveCredential:enter
00895261.012 |08:59:17.067 |AppInfo | userid is wwhite 00895261.013 |08:59:17.067 |AppInfo |AuthenticationImpl::login - no encryptedpassword Credential, look for password
00895261.014 |08:59:17.067 |AppInfo |AuthenticationImpl::login (Auth with password. Calling authenticateUserWithPassword)
00895261.015 |08:59:17.067 |AppInfo |authenticationDB:: authenticateUserWithPassword():enter 00895261.016 |08:59:17.067 |AppInfo | Credential Length is: 8
```

Step 6. CTI Manager checks the user's Credential Policy.

```
00895261.021 |08:59:17.113 |AppInfo |userType is: 1
00895261.022 |08:59:17.113 |AppInfo |timeOfLockout is: 0
00895261.023 |08:59:17.113 |AppInfo |timeHackedLockout is: 0
00895261.024 |08:59:17.113 |AppInfo |hackCount is: 0
00895261.025 |08:59:17.113 |AppInfo |daysToExpiry is: 0
00895261.026 |08:59:17.113 |AppInfo |doesNotExpire is: 0
00895261.027 |08:59:17.113 |AppInfo |useExpiryWarning is: 0
00895261.028 |08:59:17.113 |AppInfo |isInactive is: 0
00895261.029 |08:59:17.113 |AppInfo |userMustChange is: 0
00895261.030 |08:59:17.113 |AppInfo |endUserStatus is: 1
00895261.031 |08:59:17.113 |AppInfo |imsInfo is: 1
00895261.032 |08:59:17.113 |AppInfo |lastSuccessfulLoginTime is: 1455049675
00895261.033 |08:59:17.148 |AppInfo |XXXXXX Check 1
```

Step 7. CTI Authentication for the enduser continues.

```
00895261.034 |08:59:17.149 |AppInfo |authenticationDB::login ( Authenticating using LDAP )
00895261.035 |08:59:17.149 |AppInfo |authenticationLDAP.cpp::authenticateUserWithPassword():enter
00895261.036 |08:59:17.149 |AppInfo | LDAP userid is 'wwhite' 00895261.037 |08:59:17.149 |AppInfo |authenticationUtils::escapeLDAPSpecialCharsForFilter():enter
00895261.038 |08:59:17.149 |AppInfo |
After Escaping for LDAP special Characters for Filter = wwhite
```

Step 8. CTI Manager Service now attempt to connect to LDAP before authentication attempt.

```
00895261.040 |08:59:17.149 |AppInfo |LDAP not initialized...connecting...
00895261.041 |08:59:17.149 |AppInfo |authenticationLDAP::connect():enter
00895261.042 |08:59:17.149 |AppInfo |authenticationLDAP::Authenticate():enter
00895261.043 |08:59:17.149 |AppInfo |Authenticating with SSL not enabled ( ldap://10.10.10.10:3268 )
```

Step 9. Connection attempt is successful with the Service Account configured in the LDAP Authentication configuration.

```
00895261.044 |08:59:17.149 |AppInfo |LDAP initialize non-SSL Return Code (0)
```

Step 10. Admin authentication is successful.

```
00895261.051 |08:59:17.158 |AppInfo | LDAP authentication bind SUCCESS for Administrator@joshlab.net 00895261.052 |08:59:17.158 |AppInfo |Connection # (0): sucessful
00895261.053 |08:59:17.158 |AppInfo |Details ::
00895261.054 |08:59:17.158 |AppInfo |10.10.10.10 3268
00895261.055 |08:59:17.158 |AppInfo |------------------------------------------------------------------------
00895261.056 |08:59:17.158 |AppInfo |Available Servers (1)
00895261.057 |08:59:17.158 |AppInfo |authenticationLDAP::Authenticate():exit(0)
00895261.058 |08:59:17.158 |AppInfo | Authentication of LDAP administrator successful.
```

Step 11. CTI Manager service retrieve LDAP info and authenticate with the enduser account.

```
00895261.072 |08:59:17.164 |AppInfo |Retrieve the specified user entry: (&(&(objectclass=user)(!(objectclass=Computer))(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))( sAMAccountName=wwhite ))
00895261.073 |08:59:17.164 |AppInfo | LDAP Search for User base: 'OU=Breaking Bad,DC=joshlab,DC=net' 00895261.074 |08:59:17.165 |AppInfo |LDAP Search complete. Code: 0
00895261.075 |08:59:17.165 |AppInfo |Get DN of entry.
00895261.076 |08:59:17.165 |AppInfo |Got DN: CN=Walter White,OU=Breaking Bad,DC=joshlab,DC=net
00895261.077 |08:59:17.165 |AppInfo | Attempt to authenticate DN: CN=Walter White,OU=Breaking Bad,DC=joshlab,DC=net 00895261.078 |08:59:17.165 |AppInfo |authenticationLDAP::Authenticate():enter
00895261.079 |08:59:17.165 |AppInfo | Authenticating with SSL not enabled (ldap://10.10.10.10:3268)
```

Step 12. LDAP Authentication for the enduser is successful.

```
00895261.087 |08:59:17.171 |AppInfo | LDAP authentication bind SUCCESS for CN=Walter White,OU=Breaking Bad,DC=joshlab,DC=net 00895261.088 |08:59:17.171 |AppInfo |Connection # (0): sucessful
00895261.089 |08:59:17.171 |AppInfo |Details ::
00895261.090 |08:59:17.171 |AppInfo | 10.10.10.10 3268 00895261.091 |08:59:17.171 |AppInfo |------------------------------------------------------------------------
00895261.092 |08:59:17.171 |AppInfo |Available Servers (1)
00895261.093 |08:59:17.171 |AppInfo |authenticationLDAP::Authenticate():exit(0)
00895261.094 |08:59:17.171 |AppInfo |authenticationLDAP::authenticateUserWithPassword():Exit(0)
00895261.095 |08:59:17.171 |AppInfo | Successfully authenticated user: wwhite
```

Step 13. CTI Manager checks the database to ensure the enduser has the correct permissions to allow access to the phone.

```
00895262.000 |08:59:17.171 |SdlSig |CtiLoginCheckRes |authenticating |CTIHandler(1,200,22,7) |Directory(1,200,23,1) |1,200,13,8.3^*^* |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Seq#=2 result=Success LoginUserID= Expire days=4294967295
00895263.000 |08:59:17.172 |SdlSig |CtiUserSettingsReq |ready |CTIDbAccess(1,200,26,1) |CTIHandler(1,200,22,7) |1,200,13,8.3^*^* |[T:H-H:0,N:0,L:0,V:0,Z:0,D:0] mUserId=wwhite 00895263.001 |08:59:17.172 |AppInfo |DbAccess:: ReadCtiUserSettingsReq
```

Step 14. CTI User permissions are confirmed.

```
00895264.000 |08:59:17.172 |SdlSig | CtiUserSettingsRes |verifying |CTIHandler(1,200,22,7) |CTIDbAccess(1,200,26,1) |1,200,13,8.3^*^* |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] SuperProvider = Disabled CallParkRetrievalAllowed = Disabled ModifyCallingNumber = Disabled CTI Enabled = Enabled CallMonitor=Disabled CallRecord=Disabled Userid = wwhite result=0
00895264.001 |08:59:17.172 |AppInfo |[CTI-INFO] [CTIHandler::verifying_CtiUserSettingsRes] mCtiUserSettings.mbSecurityEnabled=0
00895264.002 |08:59:17.172 |AppInfo |[CTI-INFO] [CTIHandler::verifying_CtiUserSettingsRes] mListenPort=2748 00895264.003 |08:59:17.172 |AppInfo |[CTI-INFO] [CTIHandler::verifying_CtiUserSettingsRes] sent providerSubscriptionRegNotify for user wwhite
```

Step 15. CTI then sends a DeviceOpenRequest for the phone Jabber is going to control.

```
00895326.002 |08:59:17.335 |AppInfo |[CTI-APP] [CTIHandler::processIncomingMessage] CTI DeviceOpenRequest ( seq#=4 device name= SEP001794625DE5 softkeys AppID=1234)
00895327.000 |08:59:17.335 |SdlSig | CtiDeviceOpenDeviceReq |ready |CTIHandler(1,200,22,7) |CTIHandler(1,200,22,7) |1,200,13,8.5^14.48.68.203^SEP001794625DE5 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] AsyncResponse=4 DH=0|0 Name= SEP001794625DE5 Type=0 RisClass=0 TerminateMedia=5 RequestType=0 RtpDestination1|1 ApplnIpAddrMode=3 Filter Bitmap=000100000000000000000100000001001 AppLoginUserId=wwhite AppIPAddr= ipAddrType=0 ipv4=10.10.10.100 ApplicationIDListCount = 1 ApplicationIds are 1234, mSoftKeyApplicationID = 1234 ProviderIDListCount = 1 ProviderIds are 16777223, IsCTIConnectionTLS = F
```

Step 16. CTI Manager allows the connection and sends the DeviceOpenRequest Response.

```
00895329.000 |08:59:17.339 |SdlSig | CtiDeviceOpenDeviceRes |ready |CTIHandler(1,200,22,7) |CTIDeviceLineMgr(1,200,25,1) |1,200,13,8.5^ 10.10.10.100^SEP001794625DE5 |[R:N-H:0,N:3,L:0,V:0,Z:0,D:0] mAsyncResponse = 4 DH=1|38 Name= SEP001794625DE5 Type=7 StationPid=(0,0,0,0) mOpenResult=0x0 mEncodingType=3 mRequestType=0 mDSSDeviceState = 0
00895329.001 |08:59:17.339 |AppInfo |CQBEBuilder::BuildQbeMessage(): objectID=27
00895329.002 |08:59:17.340 |AppInfo |CTIHandler::OutputQbeMessage: TcpHand=[1:200:13:8] QbePref={0x0xf74b346c,0x98} pQbeMsg=0x0xf74b3474 qbeMsgSize=0x98 tmpLen=0xa0 msgSize_=0xa0
00895329.003 |08:59:17.340 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI DeviceOpenResponse ( seq#=4 result=0 DH=1|38 deviceName= SEP001794625DE5 deviceType=7 deviceId=38 registrationAllowed=0 deviceLocale=1 protocol=1 deviceRestricted=0 altScript= Rollover=0 BIB=0 DNDOption=0 IpAddrMode=0 supportsFeat=0 Visiting=0)
00895330.000 |08:59:17.340 |AppInfo |-->RisCTIManagerAccess::DeviceOpenActivityy(...)
00895331.000 |08:59:17.340 |AppInfo | DeviceOpenActivity (): activity: 1, connID: 7, deviceName: SEP001794625DE5 , appID: wwhite-10.10.10.100-58667, rtpaddr: , assocIpAddr: , mediaControl: 0, deviceType: 7, reason: 0
00895332.000 |08:59:17.340 |AppInfo |<--RisCTIManagerAccess::DeviceOpenActivityy(...)
```

Step 17. Finally there is the DeviceInService message which marks the sucessful completion of deskphone control request.

```
00895336.003 |08:59:17.343 |AppInfo |[CTI-APP] [CTIHandler::OutputCtiMessage ] CTI DeviceInServiceEvent ( DH=1|38 ) Encoding Type=3 Device locale=1 Alt Script= DNDStatus=0 DNDOption=0)
00895337.000 |08:59:17.344 |SdlSig |SdlDataInd |ready |CtiManager(1,200,21,1) |SdlTCPConnection(1,200,13,8) |1,200,13,8.6^*^* |*TraceFlagOverrode
00895337.001 |08:59:17.344 |AppInfo |CtiManager::ready_SdlDataInd(): ConnHandle=[1:200:13:8] TCP message length=0x108
00895338.000 |08:59:17.344 |SdlSig |CtiQbeGenericMessage |ready |CTIHandler(1,200,22,7) |CtiManager(1,200,21,1) |1,200,13,8.6^*^* |*TraceFlagOverrode
00895338.001 |08:59:17.344 |AppInfo |CQBEParser::ParseQbeMessage: PDU#=37
```

At this point the Jabber client is successfully able to control deskphone via CTI. Common issues can be seen at the LDAP authentication and the enduser permissions process of the CTI logs.

## Related Information

- Jabber Configuration Guide

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Josh Hammonds

Cisco TAC Engineer

Manoj Srinivas

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber