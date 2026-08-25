---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214535-troubleshoot-fa73844b57
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214535-troubleshoot-extension-mobility-cross-cl.html
retrieved_at: 2026-08-25T07:53:57.182800+00:00
---

Troubleshoot Extension Mobility Cross Cluster (EMCC)

# Troubleshoot Extension Mobility Cross Cluster (EMCC)

### Download Options

Updated: April 19, 2021

Document ID: 214535

Contents

## Contents

## Introduction

This document describes the Extension Mobility Cross Cluster (EMCC) feature for Cisco Unified Communications Manager (CUCM). This document covers the purpose of the feature, configuration of the feature, important diagnostic data, example analysis of the data, and related resources for additional research.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Phone Registration

- Extension Mobility

- Multi Cluster Environments

### Components Used

This document is not restricted to specific software and hardware versions as currently supported software and hardware include this feature.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The purpose of this feature is to allow end users to travel from one cluster to another cluster while maintaining their Home Cluster dialing habits. The user doesn't need to bring their phone, but instead they simply log in to a phone at the remote site with their device profile.

### Network Diagram

## Configuration

EMCC configuration is covered in the document Enable UC servers for Extension Mobility Cross Cluster (EMCC)

## Troubleshoot

### Data to Collect

When you troubleshoot an EMCC issue you must collect this information from each CUCM cluster:

- show version active from the CUCM publisher’s CLI on both clusters.

- show network cluster from the CUCM publisher’s CLI on both clusters.

- Cisco CallManager logs from all nodes on both clusters.

- Cisco Extension Mobility logs from all nodes on both clusters.

- Cisco Extension Mobility Application logs from all nodes on both clusters.

- Cisco Tftp logs from all nodes on both clusters.

- Cisco Trust Verification Service logs from all nodes on both clusters.

- Event Viewer-Application Log from all nodes on both clusters.

- Event Viewer-System Log from all nodes on both clusters.

- It can be beneficial to get Packet Capture Logs from all nodes on both clusters; however, most scenarios don't require them.

- If there was a login/logout failure, details about the login attempt you must review:

User id:

Phone MAC address:

Phone IP address:

Time Stamp:

The EMCC Service URL:

- If there was a call failure, details about the problem you must review:

Calling Number:

Called Number:

Time Stamp:

What did the user experience (fast busy, other noises, phone went back to idle display, etc…)

You must also collect the following data from the phone:

- What did the user experience (Exact error on the screen, sequence of events on the phone screen, etc...)

- A PRT from the phone where the user was loged in.

- It can be beneficial to get a pcap from the phone; however, most scenarios don't require it.

### Example Analysis For Log in

#### Device information from Cisco lab

Phone:

Model: 7821 Firmware version: sip78xx.12-1-1-12 IP address: 192.168.7.104 eth.addr==c8:00:84:aa:87:43

Home Cluster:

Version: 11.5.1.15900-18 IP addresses: 192.168.7.200

Visiting Cluster:

Version: 11.5.1.15900-18 IP addresses: 192.168.7.100, 192.168.7.101, 192.168.7.102, 192.168.7.103

EMCC URL: http://192.168.7.100:8080/emapp/EMAppServlet?device=#DEVICENAME#&EMCC=#EMCC#

User information:

User ID: adgjm

Login Time: 11:15

#### Log review for Visiting Cluster CUCM

Note : The sequential order of logs shows messages between emapp and emservice. Be mindful of this while you read these log snippets.

```
emapp ##### 13:32:15,947 EMApp on the visiting cluster prints that it received a request pertaining to EMCC for Device Name SEPC80084AA8743
2019-03-09 13:32:15,947 INFO  [http-bio-80-exec-8  ] EMAppServlet              - EMApp Request# ----->2
2019-03-09 13:32:15,948 INFO  [http-bio-80-exec-8  ] EMAppServlet              - EMAppServlet: Request protocol is :http

 ##### 13:32:15,948 we can see the request isn't for logout, the device name, the ip address, and that EMCC is set to true
2019-03-09 13:32:15,948 INFO  [http-bio-80-exec-8  ] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=SEPC80084AA8743 User Id=null Device Profile=null Refresh=null Remote Host IP Address = 192.168.7.104 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,;q=0.8 Emcc = true emservice ##### 13:32:16,109 The device is being queried for a user
2019-03-09 13:32:16,109 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1:Querying device user for device SEPC80084AA8743
2019-03-09 13:32:16,110 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1:Getting device object - three params
2019-03-09 13:32:16,110 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1: DBRequestor.queryDeviceUser: Dev: 'SEPC80084AA8743' - Getting device object

 ##### 13:32:16,115 The result of the query is returned and we can see there isn't anyone logged in at the moment: currentuserid=,
2019-03-09 13:32:16,115 INFO  [http-bio-443-exec-6 ] CMDatabase                - getDeviceInfo:Result of the query: {tkproduct=508, loginduration=, lastuserid=adgjm, tkdeviceprotocol=11, pkid=b5a73ec1-a04d-5ad3-fa7f-e38c501800f7, tkmodel=621, logintime=, currentuserid=, allowhotelingflag=t, fkdevicepool=1b1b9eb6-7803-11d3-bdf0-00108302ead1, tkuserlocale=}
2019-03-09 13:32:16,115 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1: DBRequestor.queryDeviceUser: Dev: 'SEPC80084AA8743' - Device object returned
2019-03-09 13:32:16,115 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1: QueryDeviceUser: Device Logged out
2019-03-09 13:32:16,115 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1:Device query info contains userid= 
2019-03-09 13:32:16,116 INFO  [http-bio-443-exec-6 ] DBRequestor               - 1:Device query info contains last login userid= adgjm
2019-03-09 13:32:16,116 INFO  [http-bio-443-exec-6 ] EMServiceServlet          - 1:Query Processing Time: 68 emapp ##### 13:32:16,124 We can see the device doesn't have anyone logged in and that the profile is not already in use elsewhere
2019-03-09 13:32:16,124 INFO  [http-bio-80-exec-8  ] EMAppServlet              - The login status result for :SEPC80084AA8743:null:adgjm:null:no
2019-03-09 13:32:16,124 INFO  [http-bio-80-exec-8  ] CMDatabase                - CMDatabase:checkDeviceAllowsAlternateScript
2019-03-09 13:32:16,126 INFO  [http-bio-80-exec-8  ] CMDatabase                - SEPC80084AA8743 with model 621 and locale 1 does not support alternate script
2019-03-09 13:32:16,126 INFO  [http-bio-80-exec-8  ] EMAppServlet              - Sent login page for device SEPC80084AA8743
2019-03-09 13:32:16,126 INFO  [http-bio-80-exec-8  ] EMAppServlet              - Context:/emapp  ::URI:/jsp/form1.jsp
2019-03-09 13:32:16,127 INFO  [http-bio-80-exec-8  ] EMAppServlet              - findPreferredCharSet on utf-8,;q=0.8
2019-03-09 13:32:16,127 INFO  [http-bio-80-exec-8  ] EMAppServlet              - token1 = utf-8
2019-03-09 13:32:16,127 INFO  [http-bio-80-exec-8  ] EMAppServlet              -  token2 = utf-8
2019-03-09 13:32:16,127 INFO  [http-bio-80-exec-8  ] EMAppServlet              -  charset with q value is 1 utf-8
2019-03-09 13:32:16,127 INFO  [http-bio-80-exec-8  ] EMAppServlet              -  returning charset as q value is 1 utf-8
2019-03-09 13:32:16,127 INFO  [http-bio-80-exec-8  ] EMAppServlet              -  my charset =utf-8

 ##### 13:32:27,814 another request comes in via HTTP
2019-03-09 13:32:27,814 INFO  [http-bio-80-exec-7  ] EMAppServlet              - EMApp Request# ----->3
2019-03-09 13:32:27,815 INFO  [http-bio-80-exec-7  ] EMAppServlet              - EMAppServlet: Request protocol is :http

 ##### 13:32:27,815 we can see the same info from before, but this time there is a user id specified 
2019-03-09 13:32:27,815 INFO  [http-bio-80-exec-7  ] EMAppServlet              - EMApp Request parameters: Logout=null Device Name=SEPC80084AA8743 User Id=adgjm Device Profile=null Refresh=null Remote Host IP Address = 192.168.7.104 Via Header Set = false getClusterInfo = null Lang = en_US Charset=utf-8,;q=0.8 Emcc = true
2019-03-09 13:32:27,816 INFO  [http-bio-80-exec-7  ] EMServiceCommunicator     - Posting to EM Query Service:https://localhost:8443/emservice/EMServiceServlet
2019-03-09 13:32:27,835 INFO  [http-bio-80-exec-7  ] EMAppServlet              - EMCC Request for adgjm
2019-03-09 13:32:27,836 INFO  [http-bio-80-exec-7  ] EMAppServlet              - EMURI = http%3A%2F%2F192.168.7.100%3A8080%2Femapp%2FEMAppServlet%3Fdevice%3DSEPC80084AA8743%26doLogout%3Dtrue
2019-03-09 13:32:27,836 INFO  [http-bio-80-exec-7  ] EMServiceCommunicator     - postMsgToLoginService: Service URL :https://localhost:8443/emservice/EMServiceServlet emservice ##### 13:32:27,826 There is an authenticate request
2019-03-09 13:32:27,826 INFO  [http-bio-443-exec-10] EMServiceServlet          - 2: authenticate2: Authenticate request.
2019-03-09 13:32:27,827 INFO  [http-bio-443-exec-10] Authenticator             - 2:Authenticator.authenticateTransaction: AppID: CCMSysUser- Checking values in credential cache
2019-03-09 13:32:27,827 INFO  [http-bio-443-exec-10] Authenticator             - 2:Authenticator.authenticateTransaction: AppID: CCMSysUser- Approved through credential cache, 108234 ms remaining

 ##### 13:32:27,827 The authentication succeeds and there is a check for the user
2019-03-09 13:32:27,827 INFO  [http-bio-443-exec-10] EMServiceServlet          - 2:EMService Authentication succeeded
2019-03-09 13:32:27,827 INFO  [http-bio-443-exec-10] EMServiceServlet          - 2:EMService Check User Status
2019-03-09 13:32:27,827 INFO  [http-bio-443-exec-10] Authenticator             - 2:Authenticator.userExists: UserID: adgjm- Calling cmdb.isLocalUser(osUserID)...

 ##### 13:32:27,831 we see no user exists with id: adgjm
2019-03-09 13:32:27,831 ERROR [http-bio-443-exec-10] CMDatabase                - CMDatabase:isLocalUser: no user exists with id: adgjm
2019-03-09 13:32:27,831 ERROR [http-bio-443-exec-10] CMDatabase                - CMDatabase:isLocalUser: com.cisco.ccm.database.CMDBLException: Uknown user: adgjm
2019-03-09 13:32:27,832 ERROR [http-bio-443-exec-10] Authenticator             - Exception : Uknown user: adgjm
2019-03-09 13:32:27,832 WARN  [http-bio-443-exec-10] EMServiceServlet          - 2: executeQuery MyException.
2019-03-09 13:32:27,832 INFO  [http-bio-443-exec-10] EMServiceServlet          - 2:Query Processing Time: 11
2019-03-09 13:32:27,839 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - EMService Request# ----> : 3

 ##### 13:32:27,839 The request type is noted as EMCC
2019-03-09 13:32:27,839 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3:EMService: Request Type=EMCC
2019-03-09 13:32:27,843 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: processEmccRequest: Received EMCC Login Request for :adgjm
2019-03-09 13:32:27,843 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: Executing authenticate2...
2019-03-09 13:32:27,844 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: authenticate2: Authenticate request.
2019-03-09 13:32:27,844 INFO  [http-bio-443-exec-2 ] Authenticator             - 3:Authenticator.authenticateTransaction: AppID: CCMSysUser- Checking values in credential cache
2019-03-09 13:32:27,844 INFO  [http-bio-443-exec-2 ] Authenticator             - 3:Authenticator.authenticateTransaction: AppID: CCMSysUser- Approved through credential cache, 108216 ms remaining
2019-03-09 13:32:27,844 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3:EMService Authentication succeeded
2019-03-09 13:32:27,846 INFO  [http-bio-443-exec-2 ] PolicyValidator           - 3:PolicyValidator.checkDeviceAllowsLogin: Dev: SEPC80084AA8743- Calling dbr.getDeviceObject
2019-03-09 13:32:27,847 INFO  [http-bio-443-exec-2 ] DBRequestor               - 3:Getting device object - loginInfo, caller
2019-03-09 13:32:27,847 INFO  [http-bio-443-exec-2 ] DBRequestor               - 3: PolicyValidator.checkDeviceAllowsLogin: Dev: SEPC80084AA8743- Getting device object
2019-03-09 13:32:27,850 INFO  [http-bio-443-exec-2 ] CMDatabase                - getDeviceInfo:Result of the query: {tkproduct=508, loginduration=, lastuserid=adgjm, tkdeviceprotocol=11, pkid=b5a73ec1-a04d-5ad3-fa7f-e38c501800f7, tkmodel=621, logintime=, currentuserid=, allowhotelingflag=t, fkdevicepool=1b1b9eb6-7803-11d3-bdf0-00108302ead1, tkuserlocale=}
2019-03-09 13:32:27,851 INFO  [http-bio-443-exec-2 ] DBRequestor               - 3: PolicyValidator.checkDeviceAllowsLogin: Dev: SEPC80084AA8743- Device object returned
2019-03-09 13:32:27,851 INFO  [http-bio-443-exec-2 ] PolicyValidator           - 3:PolicyValidator.checkDeviceAllowsLogin: Dev: SEPC80084AA8743- dbr.getDeviceObject returned
2019-03-09 13:32:27,851 INFO  [http-bio-443-exec-2 ] EmccData                  - osQuery = SELECT COUNT(*) as value FROM ProductSupportsFeature p INNER JOIN Device d on (p.tkProduct =  d.tkProduct AND p.tkDeviceProtocol IN (99, d.tkDeviceProtocol )) INNER JOIN TypeSupportsFeature t ON p.tkSupportsFeature = t.Enum WHERE LOWER(d.name) = LOWER('SEPC80084AA8743') AND t.Moniker = 'SUPPORTS_FEATURE_EMCC'
2019-03-09 13:32:27,853 INFO  [http-bio-443-exec-2 ] PolicyValidator           - 3:PolicyValidator.checkCurrentLogin: getCurrentLoginTime return value- 0

 ##### 13:32:27,854 No user is logged into the phone and we are going to look for the user's home cluster (only 1 cluster is listed in cluster view for this lab setup)
2019-03-09 13:32:27,854 INFO  [http-bio-443-exec-2 ] PolicyValidator           - 3:PolicyValidator.checkCurrentLogin: no user currently logged in
2019-03-09 13:32:27,854 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3 findHomeCluster: Finding Home Cluster for User: adgjm

 ##### 13:32:27,928 The home cluster is determined to be 192.168.7.200 which is "ClusterTwo" with a pkid of b986ff55-4374-43d2-8d99-ad6db704e672
2019-03-09 13:32:27,928 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: EmccLoginRequest: Home Cluster URL for User:adgjm is : https://192.168.7.200:8443/emservice/EMServiceServlet
2019-03-09 13:32:27,929 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: EmccLoginRequest: Device Profile for this user is: test_emcc_udp
2019-03-09 13:32:27,969 INFO  [http-bio-443-exec-2 ] EmccData                  - 3: getRemoteClusterInfo: Pkid for cluster ClusterTwo is b986ff55-4374-43d2-8d99-ad6db704e672

 ##### 13:32:27,970 The login request is sent to the home cluster
2019-03-09 13:32:27,970 INFO  [http-bio-443-exec-2 ] EmccCommunicator          - 3: performDoLogin : Sending home login XML to :https://192.168.7.200:8443/emservice/EMServiceServlet and Parsing the response
2019-03-09 13:32:28,052 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: EmccLoginRequest: Performing Visiting Device Login for :adgjm
2019-03-09 13:32:28,052 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3:performVisitingDeviceLogin - SEPC80084AA8743
2019-03-09 13:32:28,072 INFO  [http-bio-443-exec-2 ] EMServiceServlet          - 3: EmccRequest Processing Time: 233 emapp ##### 13:32:28,075 The login is successful
2019-03-09 13:32:28,075 INFO  [http-bio-80-exec-7  ] EMAppServlet              - Successfully performed Login for user adgjm at SEPC80084AA8743
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              - Context:/emapp  ::URI:/jsp/phone_refresh.jsp
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              - findPreferredCharSet on utf-8,;q=0.8
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              - token1 = utf-8
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              -  token2 = utf-8
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              -  charset with q value is 1 utf-8
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              -  returning charset as q value is 1 utf-8
2019-03-09 13:32:28,076 INFO  [http-bio-80-exec-7  ] EMAppServlet              -  my charset =utf-8
```

#### Log review for Home Cluster CUCM

```
emservice logs: ##### 13:32:27,863 EMService on the home cluster receives an EMCC Check User Request
2019-03-09 13:32:27,863 INFO  [http-bio-443-exec-17] EMServiceServlet          - EMService Request# ----> : 1
2019-03-09 13:32:27,863 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1:EMService: Request Type=EMCC
2019-03-09 13:32:27,872 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1: Setting remoteIPAddr to connection IP=192.168.7.100
2019-03-09 13:32:27,873 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1 : 3 : ClusterOne: processEmccRequest: Received Check User Request for :adgjm

 ##### 13:32:27,873 The EMService on the home cluster checks if the user exists in the local database
2019-03-09 13:32:27,873 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1 : 3 : ClusterOne: EmccCheckUser : Checking if User adgjm exists in local database
2019-03-09 13:32:27,873 INFO  [http-bio-443-exec-17] Authenticator             - 1:Authenticator.userExists: UserID: adgjm- Calling cmdb.isLocalUser(osUserID)...

 ##### 13:32:27,889 EMService on the home cluster finds the user then looks up the information for the remote cluster and responds with the user id and associated device profiles
2019-03-09 13:32:27,889 INFO  [http-bio-443-exec-17] Authenticator             - 1:Authenticator.userExists: UserID: adgjm- cmdb.isLocalUser(osUserID) returned
2019-03-09 13:32:27,889 INFO  [http-bio-443-exec-17] DBRequestor               - 1: queryUDP2: User Exists
2019-03-09 13:32:27,892 INFO  [http-bio-443-exec-17] DBRequestor               - UserInfo:  UserID: adgjm Password:  Locale: 0 Authentication proxy rights: falseDevice Profiles:  test_emcc_udp
2019-03-09 13:32:27,892 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1: authenticate pin for adgjm
2019-03-09 13:32:27,923 INFO  [http-bio-443-exec-17] EmccData                  - 1: getRemoteClusterInfo: Pkid for cluster ClusterOne is f672bb12-5e1b-4795-81fa-d06d5ce07e84
2019-03-09 13:32:27,925 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1 : 3 : ClusterOne: EmccCheckUser
<emccResponse><checkUser><user id="adgjm"><numProfiles>1</numProfiles><exists/><deviceProfile1>test_emcc_udp</deviceProfile1></user></checkUser></emccResponse>
2019-03-09 13:32:27,925 INFO  [http-bio-443-exec-17] EMServiceServlet          - 1: EmccRequest Processing Time: 61

 ##### 13:32:27,975 EMService on the home cluster receives an EMCC Login Request
2019-03-09 13:32:27,975 INFO  [http-bio-443-exec-19] EMServiceServlet          - EMService Request# ----> : 2
2019-03-09 13:32:27,975 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2:EMService: Request Type=EMCC
2019-03-09 13:32:27,978 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2: Setting remoteIPAddr to connection IP=192.168.7.100
2019-03-09 13:32:27,978 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2 : 3 : ClusterOne: processEmccRequest: Received EMCC Home Cluster Login Request for :adgjm
2019-03-09 13:32:27,978 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2 : 3 : DeviceSecurityMode: 1 HomeCluster SecurityMode: 0
2019-03-09 13:32:27,978 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2: authenticate pin for adgjm
2019-03-09 13:32:27,980 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2 : 3 : ClusterOne: EmccHomeLogin : Performing Home Device Login for :adgjm
2019-03-09 13:32:27,981 INFO  [http-bio-443-exec-19] EmccData                  - 2: getRemoteClusterInfo: Pkid for cluster ClusterOne is f672bb12-5e1b-4795-81fa-d06d5ce07e84
2019-03-09 13:32:27,981 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2: computeLoginDuration: Device: SEPC80084AA8743 - Checking autologout settings...
2019-03-09 13:32:28,048 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2: scheduleLogout: Device: SEPC80084AA8743-Setting autologout request with logout scheduler for : 36000 secs
2019-03-09 13:32:28,049 INFO  [http-bio-443-exec-19] LogoutScheduler           - 2:LogoutScheduler.setLogout(): Dev: SEPC80084AA8743- Set logout for 36000 seconds
2019-03-09 13:32:28,049 INFO  [http-bio-443-exec-19] EMServiceServlet          - 2: EmccRequest Processing Time: 74

 ##### 13:32:28,154 EMService on the home cluster then updates the extensionmobilitydynamic database table
2019-03-09 13:32:28,154 INFO  [Thread-35           ] CMDatabase                - [CMDatabase] process(<msg><type>DBL</type><table>extensionmobilitydynamic</table><tableid>170</tableid><action>U</action><user>dbemweb</user><time>1552156348</time><old><cdrserver>2</cdrserver><cdrtime>1550846224</cdrtime><pkid>180363d9-ed4b-4d5c-b299-751aa3e06cfd</pkid><logintime>NULL</logintime><loginduration>NULL</loginduration><fkdevice_currentloginprofile>NULL</fkdevice_currentloginprofile><fkenduser_lastlogin>97f2a05c-f973-6fd4-fd5e-2048b7f70530</fkenduser_lastlogin><fkdevice>180363d9-ed4b-4d5c-b299-751aa3e06cfd</fkdevice><allowcticontrolflag>t</allowcticontrolflag><ctiidbase>3</ctiidbase><datetimestamp>1550846224</datetimestamp><fkcallingsearchspace_restrict>NULL</fkcallingsearchspace_restrict><fkenduser>NULL</fkenduser><fkmatrix_presence>NULL</fkmatrix_presence><fkmlppdomain>NULL</fkmlppdomain><fkphonetemplate>NULL</fkphonetemplate><fksoftkeytemplate>NULL</fksoftkeytemplate><ignorepi>f</ignorepi><lastnumplanindex>0</lastnumplanindex><mismatchedlogin>f</mismatchedlogin><tkpreemption>2</tkpreemption><tkstatus_mlppindicationstatus>2</tkstatus_mlppindicationstatus><tkuserlocale>1</tkuserlocale><userholdmohaudiosourceid>NULL</userholdmohaudiosourceid><versionstamp>1550846224-ca3abf91-97c3-4ce7-9a3d-4373eb132289</versionstamp><tkringsetting_dnd>NULL</tkringsetting_dnd><tkdndoption>2</tkdndoption><tkstatus_joinacrosslines>0</tkstatus_joinacrosslines><tkbarge>0</tkbarge><tkstatus_alwaysuseprimeline>2</tkstatus_alwaysuseprimeline><tkstatus_alwaysuseprimelineforvm>2</tkstatus_alwaysuseprimelineforvm><fkcallingsearchspace_emcc>NULL</fkcallingsearchspace_emcc><fkfeaturecontrolpolicy>NULL</fkfeaturecontrolpolicy><ifx_replcheck>6660833813205221397</ifx_replcheck></old><new><tkstatus_alwaysuseprimelineforvm>2</tkstatus_alwaysuseprimelineforvm><tkstatus_alwaysuseprimeline>2</tkstatus_alwaysuseprimeline><ignorepi>f</ignorepi><tkringsetting_dnd>NULL</tkringsetting_dnd><fkcallingsearchspace_restrict>NULL</fkcallingsearchspace_restrict><fkmlppdomain>NULL</fkmlppdomain><fkmatrix_presence>ad243d17-98b4-4118-8feb-5ff2e1b781ac</fkmatrix_presence><fkphonetemplate>16f15a8c-63f6-44ba-b240-82c24714ec12</fkphonetemplate><allowcticontrolflag>t</allowcticontrolflag><tkuserlocale>1</tkuserlocale><fksoftkeytemplate>NULL</fksoftkeytemplate><userholdmohaudiosourceid>NULL</userholdmohaudiosourceid><tkstatus_mlppindicationstatus>2</tkstatus_mlppindicationstatus><tkpreemption>2</tkpreemption><tkdndoption>2</tkdndoption><ctiidbase>1</ctiidbase><mismatchedlogin>f</mismatchedlogin><lastnumplanindex>0</lastnumplanindex><fkenduser>97f2a05c-f973-6fd4-fd5e-2048b7f70530</fkenduser><logintime>1552156348</logintime><loginduration>36000</loginduration><fkdevice_currentloginprofile>91ac8680-48d3-48c1-956e-f6e10d046ce4</fkdevice_currentloginprofile><datetimestamp>1552156347</datetimestamp><versionstamp>1552156347-145cec2d-3b45-430f-acaf-d79657a15c58</versionstamp></new></msg> ) started
2019-03-09 13:32:28,154 INFO  [Thread-35           ] CMDatabase                - [CMDatabase] process() - table=extensionmobilitydynamic
```

```
CCM logs: ##### 13:32:28.155 The database on the home cluster receives the update and processes it
00009522.001 |13:32:28.155 |AppInfo  |ProcessCnf N: extensionmobilitydynamic U 180363d9-ed4b-4d5c-b299-751aa3e06cfd, size(2864) fkmatrix_presence(NULL/ad243d17-98b4-4118-8feb-5ff2e1b781ac) fkphonetemplate(NULL/16f15a8c-63f6-44ba-b240-82c24714ec12) ctiidbase(3/1) fkenduser(NULL/97f2a05c-f973-6fd4-fd5e-2048b7f70530) logintime(NULL/1552156348) loginduration(NULL/36000) fkdevice_currentloginprofile(NULL/91ac8680-48d3-48c1-956e-f6e10d046ce4) datetimestamp(1550846224/1552156347) versionstamp(1550846224-ca3abf91-97c3-4ce7-9a3d-4373eb132289/1552156347-145cec2d-3b45-430f-acaf-d79657a15c58)
```

#### Service as seen in the phone config file

```
<phoneService type="0" category="0"> <name>EMCC_Service</name> <url>http://192.168.7.100:8080/emapp/EMAppServlet?device=#DEVICENAME#&amp;EMCC=#EMCC#</url> <vendor></vendor> <version></version> </phoneService>
```

#### Log review for the phone

Note : No debugs were enabled when these logs were collected.

```
##### 18:32:35.240378 || The EMCC mode is changed to true
4743 WRN Mar 09 18:32:35.240378 (618:910) JAVA-configmgr MQThread|DisplayTask:? -  EMCC mode changed to true
4744 WRN Mar 09 18:32:35.241080 (618:910) JAVA-configmgr MQThread|DisplayTask:? - resetCurrentPowerState(): Energywise is disabled
4745 WRN Mar 09 18:32:35.241873 (618:910) JAVA-configmgr MQThread|DisplayTask:? - resetCurrentPowerState(): Energywise null domain
4746 WRN Mar 09 18:32:35.242606 (618:910) JAVA-configmgr MQThread|DisplayTask:? - resetCurrentPowerState(): Energywise null secret
4747 WRN Mar 09 18:32:35.243643 (618:910) JAVA-configmgr MQThread|DisplayTask:? - resetCurrentPowerState(): Energywise disabled for EMCC mode
4748 ERR Mar 09 18:32:35.244254 (618:910) JAVA-IO_JNI| NIOLightLamp: led Data passed to cprLedSet(): 0x01000000
4749 ERR Mar 09 18:32:35.244712 (618:910) JAVA-[API]LED ID error
4750 ERR Mar 09 18:32:35.245170 (618:910) JAVA-IO_JNI| !!! cprLedSet() return failed!
4751 WRN Mar 09 18:32:35.245933 (618:910) JAVA-configmgr MQThread|DisplayTask:? -  resetCurrentPowerState(): energywise is not available now

 ##### 18:32:35.273065 || sipcc is notified that EMCC is enabled
4752 NOT Mar 09 18:32:35.273065 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - [commitEMCCProperties] to notify sipcc of EMCC:enabled
4753 NOT Mar 09 18:32:35.275751 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - [commitEMCCProperties] notify sipcc of [vEM-IP,vEM-Port]:[192.168.7.100,8080]

 ##### 18:32:35.313016 || We identify the TFTP servers for the home cluster
4754 NOT Mar 09 18:32:35.313016 (339:1813) downd-SETTFTP [339] emcc_mode =1, override =0, tempTftp1= 192.168.7.200, tempTftp2 = , tempTftp3 = , tempTftp4 = 

 ##### 18:32:36.726445 || The EMCC mini config files is received
4797 WRN Mar 09 18:32:36.726445 (618:910) JAVA-configmgr MQThread|cip.cfg.SipConfig:? - EMCC|Received Mini-config file.
4798 WRN Mar 09 18:32:36.727636 (618:910) JAVA-configmgr MQThread|cip.cfg.SipConfig:? - ====>no need set capf,EMCC=true and encrConfig=false
4799 INF Mar 09 18:32:36.728643 (618:910) JAVA-configmgr MQThread|cip.cfg.SipConfig:? - processConfigNoError: result=1
4800 NOT Mar 09 18:32:36.731786 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - Sending update notice to Metmand
4801 NOT Mar 09 18:32:36.732794 (624:624) metmand-config_parser_main parsing /usr/local/flash0/sip-SEPC80084AA8743.cnf.xml
4802 NOT Mar 09 18:32:36.741400 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - Sending update notice to Metmand - COMPLETE
4803 NOT Mar 09 18:32:36.748115 (618:910) JAVA-configmgr MQThread|cip.cfg.SipConfig:? - Config processConfigNoError() result code=CONFIG_FILE_CHANGED

 ##### 18:32:37.594689 || The phone requests the CTL file from the Home Cluster
4849 NOT Mar 09 18:32:37.594689 (339:1850) downd-GETXXTP [GT339][src=CTLSEPC80084AA8743.tlv][dest=/tmp/CTLFile.tlv][serv=][serv6=][sec=0]
4850 NOT Mar 09 18:32:37.597405 (339:1850) downd-In normal mode, call - > makeXXTPrequest (V6...)
4851 NOT Mar 09 18:32:37.643125 (618:755) JAVA-Thread-12|cip.setg.IpStacksStateProperty:? - IpStacksStateProperty changed from "IPv4-stack-state:1 (DHCP BOUND), IPv6-stack-state:199 (IPV6 STACK TURNED OFF)" to "IPv4-stack-state:1 (DHCP BOUND), IPv6-stack-state:199 (IPV6 STACK TURNED OFF)"
4852 NOT Mar 09 18:32:37.641843 (339:1850) downd-EMCC reading: 
4853 NOT Mar 09 18:32:37.643735 (339:1850) downd-	 EMCC Mode     - 1
4854 NOT Mar 09 18:32:37.643827 (339:1850) downd-	 EMCC Override - 0
4855 NOT Mar 09 18:32:37.643888 (339:1850) downd-	 Home Tftp 1   - [14] 192.168.7.200
4856 NOT Mar 09 18:32:37.643949 (339:1850) downd-	 Home Tftp 2   - [1] 
4857 NOT Mar 09 18:32:37.644010 (339:1850) downd-	 Home Tftp 3   - [1] 
4858 NOT Mar 09 18:32:37.644071 (339:1850) downd-	 Home Tftp 4   - [1] 
4859 NOT Mar 09 18:32:37.644132 (339:1850) downd-unable to convert the tempTftpSvr2: retVal=0  
4860 NOT Mar 09 18:32:37.644193 (339:1850) downd-unable to convert the tempTftpSvr4: retVal=0 

 ##### 18:32:37.644345 || look up server - 0 - 192.168.7.200
4861 NOT Mar 09 18:32:37.644345 (339:1850) downd-AUTH.SRVR [GT339] look up server - 0 - 192.168.7.200
4862 NOT Mar 09 18:32:37.646787 (618:755) JAVA-Calling handleNetSDEvent
4863 NOT Mar 09 18:32:37.699343 (339:1850) downd-AUTH.SRVR [GT339] look up server - 1 - 0.0.0.0
4864 NOT Mar 09 18:32:37.750465 (339:1850) downd-AUTH.SRVR [GT339] authentication retval = 9 
4865 NOT Mar 09 18:32:37.750648 (339:1850) downd-XXTP Non secure file requested  
4866 NOT Mar 09 18:32:37.750923 (339:1850) downd-XXTP start request, server 1 - 192.168.7.200 
4867 NOT Mar 09 18:32:37.751441 (339:1850) downd-XXTP actualserver [192.168.7.200]
4868 NOT Mar 09 18:32:37.763222 (339:1858) downd-XXX arg[0] /usr/sbin/gethtp
4869 NOT Mar 09 18:32:37.768655 (339:1858) downd-XXX arg[1] -t
4870 NOT Mar 09 18:32:37.769296 (339:1858) downd-XXX arg[2] 192.168.7.200
4871 NOT Mar 09 18:32:37.769784 (339:1858) downd-XXX arg[3] -i0
4872 NOT Mar 09 18:32:37.774088 (339:1858) downd-XXX arg[4] CTLSEPC80084AA8743.tlv
4873 NOT Mar 09 18:32:37.774606 (339:1858) downd-XXX arg[5] /tmp/CTLFile.tlv
4874 NOT Mar 09 18:32:37.775095 (339:1858) downd-XXX arg[6] (null)
4875 NOT Mar 09 18:32:37.818739 (1858:1858) GHTTP-LIMIT downdload will be limited to 2048 KB
4876 DEB Mar 09 18:32:37.974088 (618:755) JAVA-getassetid(): pid: 618 
4877 DEB Mar 09 18:32:37.974454 (618:755) JAVA-getassetid(): msgsnd() rc: 0, size: 44 bytes  
4878 DEB Mar 09 18:32:37.975980 (618:755) JAVA-getassetid(): msgrcv() 44 bytes  
4879 NOT Mar 09 18:32:37.978177 (322:366) NETSD-siginfoThrd(): tempvvlan: 4095  vvlan: 4095  linkState: 1  cdpState: 1 
4880 NOT Mar 09 18:32:37.979032 (322:366) NETSD-siginfoThrd(): activechange: 0 
4881 NOT Mar 09 18:32:37.979123 (322:366) NETSD-siginfoThrd(): force_dhcp: 0 

 ##### 18:32:37.985319 || The home cluster sends a 503 Service Unavailable
4882 ERR Mar 09 18:32:37.985319 (1858:1858) GHTTP-http get [HTTP/1.1 503 Service Unavailab]
4883 NOT Mar 09 18:32:38.001617 (339:1862) downd-XXX arg[0] /usr/sbin/tftpd
4884 NOT Mar 09 18:32:38.011475 (339:1862) downd-XXX arg[1] -t
4885 NOT Mar 09 18:32:38.011994 (339:1862) downd-XXX arg[2] 192.168.7.200
4886 NOT Mar 09 18:32:38.015595 (339:1862) downd-XXX arg[3] -i0
4887 NOT Mar 09 18:32:38.016023 (339:1862) downd-XXX arg[4] CTLSEPC80084AA8743.tlv
4888 NOT Mar 09 18:32:38.016541 (339:1862) downd-XXX arg[5] /tmp/CTLFile.tlv
4889 NOT Mar 09 18:32:38.016999 (339:1862) downd-XXX arg[6] (null)
4890 NOT Mar 09 18:32:38.082496 (618:755) JAVA-Thread-12|cip.setg.IpStacksStateProperty:? - IpStacksStateProperty changed from "IPv4-stack-state:1 (DHCP BOUND), IPv6-stack-state:199 (IPV6 STACK TURNED OFF)" to "IPv4-stack-state:1 (DHCP BOUND), IPv6-stack-state:199 (IPV6 STACK TURNED OFF)"
4891 NOT Mar 09 18:32:38.153608 (1862:1862) TFTPD-pid = 1862

 ##### 18:32:38.244254 || The phone requests the CTL file from the Home Cluster via port 69 instead of using http and port 6970
4892 NOT Mar 09 18:32:38.244254 (1862:1862) TFTPD-LIMIT downdload will be limited to 2048 KB
4893 ERR Mar 09 18:32:38.245933 (1862:1862) TFTPD-ai_family = 2, sockType = 2, protocol = 17
4894 NOT Mar 09 18:32:38.246634 (1862:1862) TFTPD-Requesting CTLSEPC80084AA8743.tlv from 192.168.7.200 
4895 WRN Mar 09 18:32:38.247306 (1862:1862) TFTPD-sendto() failed : Address family not supported by protocol 
4896 NOT Mar 09 18:32:38.752784 (1862:1862) TFTPD-Timeout: retransmit the last packet (1)

 ##### 18:32:38.754493 || The phone is told "File not found" since the cluster isn't in mixed mode
4897 WRN Mar 09 18:32:38.754493 (1862:1862) TFTPD-Error: (1+1)File not found 
4898 NOT Mar 09 18:32:38.756996 (339:1850) downd-XXTP complete - status = 2 

 ##### 18:32:38.767556 || The phone requests the ITL file from the Home Cluster
4899 NOT Mar 09 18:32:38.767556 (339:1882) downd-GETXXTP [GT339][src=ITLSEPC80084AA8743.tlv][dest=/tmp/ITLFile.tlv][serv=][serv6=][sec=0]
4900 NOT Mar 09 18:32:38.769540 (339:1882) downd-In normal mode, call - > makeXXTPrequest (V6...)
4901 NOT Mar 09 18:32:38.770944 (339:1882) downd-EMCC reading: 
4902 NOT Mar 09 18:32:38.772256 (339:1882) downd-	 EMCC Mode     - 1
4903 NOT Mar 09 18:32:38.774545 (339:1882) downd-	 EMCC Override - 0
4904 NOT Mar 09 18:32:38.775003 (339:1882) downd-	 Home Tftp 1   - [14] 192.168.7.200
4905 NOT Mar 09 18:32:38.775430 (339:1882) downd-	 Home Tftp 2   - [1] 
4906 NOT Mar 09 18:32:38.775888 (339:1882) downd-	 Home Tftp 3   - [1] 
4907 NOT Mar 09 18:32:38.776651 (339:1882) downd-	 Home Tftp 4   - [1] 
4908 NOT Mar 09 18:32:38.777170 (339:1882) downd-unable to convert the tempTftpSvr2: retVal=0  
4909 NOT Mar 09 18:32:38.777628 (339:1882) downd-unable to convert the tempTftpSvr4: retVal=0 
4910 NOT Mar 09 18:32:38.778177 (339:1882) downd-AUTH.SRVR [GT339] look up server - 0 - 192.168.7.200
4911 NOT Mar 09 18:32:38.805035 (339:1850) downd-DDGETTFTP.RESULT [_2_  File not found
	]
4912 NOT Mar 09 18:32:38.832565 (339:1882) downd-AUTH.SRVR [GT339] look up server - 1 - 0.0.0.0
4913 NOT Mar 09 18:32:38.883534 (339:1882) downd-AUTH.SRVR [GT339] authentication retval = 9 
4914 NOT Mar 09 18:32:38.883717 (339:1882) downd-XXTP Non secure file requested  
4915 NOT Mar 09 18:32:38.884724 (339:1882) downd-XXTP start request, server 1 - 192.168.7.200 
4916 NOT Mar 09 18:32:38.885334 (339:1882) downd-XXTP actualserver [192.168.7.200]
4917 NOT Mar 09 18:32:38.888997 (339:1886) downd-XXX arg[0] /usr/sbin/gethtp
4918 NOT Mar 09 18:32:38.889638 (339:1886) downd-XXX arg[1] -t
4919 NOT Mar 09 18:32:38.890126 (339:1886) downd-XXX arg[2] 192.168.7.200
4920 NOT Mar 09 18:32:38.890584 (339:1886) downd-XXX arg[3] -i0
4921 NOT Mar 09 18:32:38.891103 (339:1886) downd-XXX arg[4] ITLSEPC80084AA8743.tlv
4922 NOT Mar 09 18:32:38.891652 (339:1886) downd-XXX arg[5] /tmp/ITLFile.tlv
4923 NOT Mar 09 18:32:38.892171 (339:1886) downd-XXX arg[6] (null)
4924 NOT Mar 09 18:32:38.932397 (1886:1886) GHTTP-LIMIT downdload will be limited to 2048 KB

 ##### 18:32:38.937860 || The ITL file is received
4925 NOT Mar 09 18:32:38.937860 (1886:1886) GHTTP-hdr->HTTP/1.1 200 OK
4926 NOT Mar 09 18:32:38.938928 (1886:1886) GHTTP-hdr->Content-length: 7879
4927 NOT Mar 09 18:32:38.939355 (1886:1886) GHTTP-hdr->Cache-Control: no-store
4928 NOT Mar 09 18:32:38.939813 (1886:1886) GHTTP-hdr->Content-type: */*
4929 NOT Mar 09 18:32:38.943628 (339:1882) downd-XXTP complete - status = 100 
4930 NOT Mar 09 18:32:38.952052 (346:1887) SECUREAPP-AUTH: start of pad ('T' 0x0d) at TLV 15
4931 WRN Mar 09 18:32:38.957881 (346:1887) SECUREAPP-AUTH: hdr ver 1.2 (knows only upto 1.1)
4932 NOT Mar 09 18:32:38.958370 (346:1887) SECUREAPP-AUTH: skipping 1 trail bytes (pad and/or unknown TLVs)
4933 NOT Mar 09 18:32:38.987455 (339:1882) downd-DDGETTFTP.RESULT [_100_  HTTP NO ERROR
	]
4934 NOT Mar 09 18:32:39.928521 (413:426) CDP-cdpRcvPkt(): deviceId is HQSW

 ##### 18:32:40.161238 || The phone reaches out to the TVS server on the Visiting Cluster
4935 NOT Mar 09 18:32:40.161238 (346:1810) SECUREAPP-Sec SSL Connection - Handshake successful.
4936 NOT Mar 09 18:32:40.164291 (346:1810) SECUREAPP-TVS process request - Successfully sent the TVS request to TVS server, bytes written : 180
4937 NOT Mar 09 18:32:40.183701 (346:1810) SECUREAPP-Close and free connection handler at 0x2b2d2ac0
4938 NOT Mar 09 18:32:40.184220 (346:1810) SECUREAPP-Sec SSL Close Connection successful.

 ##### 18:32:40.672180 || The authentication is successful
4939 NOT Mar 09 18:32:40.672180 (346:1887) SECUREAPP-Hashes match... authentication successful.
4940 NOT Mar 09 18:32:40.676270 (346:1887) SECUREAPP-AUTH: start of pad ('T' 0x0d) at TLV 15
4941 WRN Mar 09 18:32:40.677002 (346:1887) SECUREAPP-AUTH: hdr ver 1.2 (knows only upto 1.1)
4942 NOT Mar 09 18:32:40.677491 (346:1887) SECUREAPP-AUTH: skipping 1 trail bytes (pad and/or unknown TLVs)

 ##### 18:32:40.678040 || The trust list is updated
4943 NOT Mar 09 18:32:40.678040 (346:1887) SECUREAPP-updateFromFile: TL parse to table: CTL_SUCCESS
4944 NOT Mar 09 18:32:40.678559 (346:1887) SECUREAPP-updateFromFile: Updating master TL table
4945 INF Mar 09 18:32:40.703372 (618:1845) JAVA-TL update Thread|cip.sec.ISecurityListener:---------updateCtl,result=8 - -------------invoke proxy
4946 INF Mar 09 18:32:40.704715 (618:910) JAVA-configmgr MQThread|cip.sec.ISecurityListener:---------updateCtl,result=8 - -------------invoke dispatcher
4947 NOT Mar 09 18:32:40.705142 (618:910) JAVA-configmgr MQThread|cip.cfg.ConfigManager$MySecurityListener:? - ConfigManager updateCTL() rc=8 retryCount=0, failReason:Success
4948 NOT Mar 09 18:32:40.721104 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - [SipConfig] endDownloadCTL-time:1552156360720
4949 NOT Mar 09 18:32:41.187578 (618:910) JAVA-CCAPIDevicesendAlarm: phone-app requesting alarm to be sent
4950 DEB Mar 09 18:32:41.188463 (618:910) JAVA-SIPCC-SIP_ALARM: storeAlarm:  stored alarm at index [1].
4951 DEB Mar 09 18:32:41.189012 (618:910) JAVA-[getDeployMode] deploy-mode:1 
4952 NOT Mar 09 18:32:41.195574 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - [SipConfig] beginDownloadConfig-time:1552156361195
4953 NOT Mar 09 18:32:41.196276 (618:910) JAVA-configmgr MQThread|cip.cfg.Config:  - [clearTftpTimeout] to reset tftp-timeout error

 ##### 18:32:41.198046 || The phone requests the CNF file from the Home Cluster
4954 NOT Mar 09 18:32:41.198046 (618:910) JAVA-configmgr MQThread|cip.cfg.SipConfig:? - Requesting CONFIG file: ram/SEPC80084AA8743.cnf.xml.59075 from TFTP Service(1), encrypt = false,isApplyingConfigFromFlash:false
4955 INF Mar 09 18:32:41.198748 (618:910) JAVA-[[MESSAGE_1.0]]: [CONFIG-MGR] --> tftpRequest(ram/SEPC80084AA8743.cnf.xml.59075) --> [TFTP] : 
4956 NOT Mar 09 18:32:41.202288 (339:1899) downd-GETXXTP [GT339][src=SEPC80084AA8743.cnf.xml][dest=/tmp/ram/SEPC80084AA8743.cnf.xml.59075][serv=][serv6=][sec=2]
4957 NOT Mar 09 18:32:41.203051 (339:1899) downd-In normal mode, call - > makeXXTPrequest (V6...)
4958 NOT Mar 09 18:32:41.204364 (339:1899) downd-EMCC reading: 
4959 NOT Mar 09 18:32:41.204852 (339:1899) downd-	 EMCC Mode     - 1
4960 NOT Mar 09 18:32:41.205310 (339:1899) downd-	 EMCC Override - 0
4961 NOT Mar 09 18:32:41.205768 (339:1899) downd-	 Home Tftp 1   - [14] 192.168.7.200
4962 NOT Mar 09 18:32:41.206531 (339:1899) downd-	 Home Tftp 2   - [1] 
4963 NOT Mar 09 18:32:41.206989 (339:1899) downd-	 Home Tftp 3   - [1] 
4964 NOT Mar 09 18:32:41.207416 (339:1899) downd-	 Home Tftp 4   - [1] 
4965 NOT Mar 09 18:32:41.208057 (339:1899) downd-unable to convert the tempTftpSvr2: retVal=0  
4966 NOT Mar 09 18:32:41.208515 (339:1899) downd-unable to convert the tempTftpSvr4: retVal=0 
4967 NOT Mar 09 18:32:41.209064 (339:1899) downd-AUTH.SRVR [GT339] look up server - 0 - 192.168.7.200
4968 NOT Mar 09 18:32:41.261010 (339:1899) downd-AUTH.SRVR [GT339] look up server - 1 - 0.0.0.0
4969 NOT Mar 09 18:32:41.312070 (339:1899) downd-AUTH.SRVR [GT339] authentication retval = 9 
4970 NOT Mar 09 18:32:41.312284 (339:1899) downd-XXTP Secure file requested 
4971 NOT Mar 09 18:32:41.312406 (339:1899) downd-XXTP authenticated file approved - add .sgn if necessary -- SEPC80084AA8743.cnf.xml.sgn  
4972 NOT Mar 09 18:32:41.312650 (339:1899) downd-XXTP start request, server 1 - 192.168.7.200 
4973 NOT Mar 09 18:32:41.313169 (339:1899) downd-XXTP actualserver [192.168.7.200]
4974 NOT Mar 09 18:32:41.317533 (339:1902) downd-XXX arg[0] /usr/sbin/gethtp
4975 NOT Mar 09 18:32:41.318266 (339:1902) downd-XXX arg[1] -t
4976 NOT Mar 09 18:32:41.318693 (339:1902) downd-XXX arg[2] 192.168.7.200
4977 NOT Mar 09 18:32:41.319151 (339:1902) downd-XXX arg[3] -i0
4978 NOT Mar 09 18:32:41.319578 (339:1902) downd-XXX arg[4] SEPC80084AA8743.cnf.xml.sgn
4979 NOT Mar 09 18:32:41.320097 (339:1902) downd-XXX arg[5] /tmp/ram/SEPC80084AA8743.cnf.xml.59075
4980 NOT Mar 09 18:32:41.320738 (339:1902) downd-XXX arg[6] (null)
4981 NOT Mar 09 18:32:41.360140 (1902:1902) GHTTP-LIMIT downdload will be limited to 2048 KB

 ##### 18:32:41.378666 || The CNF file is received
 4982 NOT Mar 09 18:32:41.378666 (1902:1902) GHTTP-hdr->HTTP/1.1 200 OK
4983 NOT Mar 09 18:32:41.378940 (1902:1902) GHTTP-hdr->Content-length: 12277
4984 NOT Mar 09 18:32:41.379062 (1902:1902) GHTTP-hdr->Cache-Control: no-store
4985 NOT Mar 09 18:32:41.379154 (1902:1902) GHTTP-hdr->Content-type: */*
4986 NOT Mar 09 18:32:41.384281 (339:1899) downd-XXTP complete - status = 100 

 ##### 18:32:43.821608 || The phone requests the SK file from the Home Cluster
5105 NOT Mar 09 18:32:43.821608 (339:1929) downd-GETXXTP [GT339][src=SKb0ec918f-b9ee-994b-57ae-345883c1fde8.xml][dest=/tmp/cache/SK-2103396823][serv=][serv6=][sec=2]
5106 NOT Mar 09 18:32:43.823500 (339:1929) downd-In normal mode, call - > makeXXTPrequest (V6...)
5107 NOT Mar 09 18:32:43.825850 (339:1929) downd-EMCC reading: 
5108 NOT Mar 09 18:32:43.826399 (339:1929) downd-	 EMCC Mode     - 1
5109 NOT Mar 09 18:32:43.828170 (339:1929) downd-	 EMCC Override - 0
5110 NOT Mar 09 18:32:43.828689 (339:1929) downd-	 Home Tftp 1   - [14] 192.168.7.200
5111 NOT Mar 09 18:32:43.830215 (339:1929) downd-	 Home Tftp 2   - [1] 
5112 NOT Mar 09 18:32:43.830642 (339:1929) downd-	 Home Tftp 3   - [1] 
5113 NOT Mar 09 18:32:43.831191 (339:1929) downd-	 Home Tftp 4   - [1] 
5114 NOT Mar 09 18:32:43.832381 (339:1929) downd-unable to convert the tempTftpSvr2: retVal=0  
5115 NOT Mar 09 18:32:43.832931 (339:1929) downd-unable to convert the tempTftpSvr4: retVal=0 
5116 NOT Mar 09 18:32:43.834396 (339:1929) downd-AUTH.SRVR [GT339] look up server - 0 - 192.168.7.200
5117 NOT Mar 09 18:32:43.888722 (339:1929) downd-AUTH.SRVR [GT339] look up server - 1 - 0.0.0.0
5118 NOT Mar 09 18:32:43.940485 (339:1929) downd-AUTH.SRVR [GT339] authentication retval = 9 
5119 NOT Mar 09 18:32:43.941065 (339:1929) downd-XXTP Secure file requested 
5120 NOT Mar 09 18:32:43.941248 (339:1929) downd-XXTP authenticated file approved - add .sgn if necessary -- SKb0ec918f-b9ee-994b-57ae-345883c1fde8.xml.sgn  
5121 NOT Mar 09 18:32:43.941522 (339:1929) downd-XXTP start request, server 1 - 192.168.7.200 
5122 NOT Mar 09 18:32:43.942926 (339:1929) downd-XXTP actualserver [192.168.7.200]
5123 NOT Mar 09 18:32:43.952510 (339:1932) downd-XXX arg[0] /usr/sbin/gethtp
5124 NOT Mar 09 18:32:43.953334 (339:1932) downd-XXX arg[1] -t
5125 NOT Mar 09 18:32:43.955318 (339:1932) downd-XXX arg[2] 192.168.7.200
5126 NOT Mar 09 18:32:43.956325 (339:1932) downd-XXX arg[3] -i0
5127 NOT Mar 09 18:32:43.956783 (339:1932) downd-XXX arg[4] SKb0ec918f-b9ee-994b-57ae-345883c1fde8.xml.sgn
5128 NOT Mar 09 18:32:43.957423 (339:1932) downd-XXX arg[5] /tmp/cache/SK-2103396823
5129 NOT Mar 09 18:32:43.958797 (339:1932) downd-XXX arg[6] (null)
5130 NOT Mar 09 18:32:44.063756 (1932:1932) GHTTP-LIMIT downdload will be limited to 2048 KB

 ##### 18:32:44.077399 || The SK template file is received
5131 NOT Mar 09 18:32:44.077399 (1932:1932) GHTTP-hdr->HTTP/1.1 200 OK
5132 NOT Mar 09 18:32:44.077948 (1932:1932) GHTTP-hdr->Content-length: 4137
5133 NOT Mar 09 18:32:44.078467 (1932:1932) GHTTP-hdr->Cache-Control: no-store
5134 NOT Mar 09 18:32:44.079078 (1932:1932) GHTTP-hdr->Content-type: */*
5135 NOT Mar 09 18:32:44.085456 (339:1929) downd-XXTP complete - status = 100 

 ##### 18:32:44.55309 || The list of CCM servers is printed (there is only 1 in the Home Cluster).
5319 DEB Mar 09 18:32:44.553090 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportCfgTableInit: For PRIMARY_CCM: IPv4 Addr: 192.168.7.200 Port: 5060 listen Port: 5060 IPv6 Addr:  Port: 5060 listen Port: 5060 transport: 4 Sec Level: 0 IP type: 1
5320 NOT Mar 09 18:32:44.554432 (618:927) JAVA-SIP : sip_transport_init_ti_addrs : Admin has not configured a valid cucm for cucm index=SECONDARY_CCM=2.
5321 DEB Mar 09 18:32:44.554646 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportCfgTableInit: For SECONDARY_CCM: IPv4 Addr:  Port: 0 listen Port: 0 IPv6 Addr:  Port: 0 listen Port: 0 transport: 4 Sec Level: 0 IP type: 0
5322 NOT Mar 09 18:32:44.555501 (618:927) JAVA-SIP : sip_transport_init_ti_addrs : Admin has not configured a valid cucm for cucm index=TERTIARY_CCM=3.
5323 DEB Mar 09 18:32:44.555653 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportCfgTableInit: For TERTIARY_CCM: IPv4 Addr:  Port: 0 listen Port: 0 IPv6 Addr:  Port: 0 listen Port: 0 transport: 4 Sec Level: 0 IP type: 0
5324 NOT Mar 09 18:32:44.556416 (618:927) JAVA-SIP : sip_transport_init_ti_addrs : Admin has not configured a valid cucm for cucm index=SRST_CCM=4.

 ##### 18:32:44.559102 || The phone opens a TCP connection with the CCM on the Home Cluster
5333 DEB Mar 09 18:32:44.559102 (618:927) JAVA-SIPCC-SIP_CC_CONN: sip_tcp_create_connection: socket connection in progress cpr_errno = 120 errno = 115 ipaddr: 192.168.7.200, port: 5060
5334 DEB Mar 09 18:32:44.559682 (618:927) JAVA-SIPCC-SIP_SOCK: sip_tcp_create_connection: socket:46, set tos/dscp: local address type:1,tos_dscp_val:96
5335 DEB Mar 09 18:32:44.559835 (618:927) JAVA-SIPCC-SIP_CC_CONN: sip_transport_setup_cc_conn: <PRIMARY_CCM>: CC TCP socket opened: to <192.168.7.200>:<5060>, local_port: 51778 handle=<46>
5336 DEB Mar 09 18:32:44.560323 (618:927) JAVA-SIPCC-SIP_ALARM: update_unregister_alarm_info: Info_type=CC_UNREG_ALARM_PORT_INFO  ccm_id=PRIMARY_CCM phone_tcp_port=51778 sip_info_msg=
5337 NOT Mar 09 18:32:44.560506 (618:927) JAVA-set_active_ccm: ccm=PRIMARY_CCM  port=51778
5338 NOT Mar 09 18:32:44.560872 (618:927) JAVA-SIP : sip_transport_init_ti_addrs : Admin has not configured a valid cucm for cucm index=SECONDARY_CCM=2.
5339 NOT Mar 09 18:32:44.561025 (618:927) JAVA-SIPCC-SIP_CC_CONN: sip_transport_setup_cc_conn: <SECONDARY_CCM>: CC address/port not configured2.
5340 NOT Mar 09 18:32:44.561544 (618:927) JAVA-SIP : sip_transport_init_ti_addrs : Admin has not configured a valid cucm for cucm index=TERTIARY_CCM=3.
5341 NOT Mar 09 18:32:44.561818 (618:927) JAVA-SIPCC-SIP_CC_CONN: sip_transport_setup_cc_conn: <TERTIARY_CCM>: CC address/port not configured2.
5342 NOT Mar 09 18:32:44.562703 (618:927) JAVA-SIP : sip_transport_init_ti_addrs : Admin has not configured a valid cucm for cucm index=SRST_CCM=4.
5343 NOT Mar 09 18:32:44.562887 (618:927) JAVA-SIPCC-SIP_CC_CONN: sip_transport_setup_cc_conn: <SRST_CCM>: CC address/port not configured2.
5344 NOT Mar 09 18:32:44.563711 (618:927) JAVA-SIPCC-SIP_CC_CONN: sip_regmgr_setup_cc_conns: NO VALID STANDBY CALL CONTROL AVAILABLE!

 ##### 18:32:45.402533 || ALL LINES UN-REGISTERED --- this is because the phone is unregistering from the visiting cluster
5818 NOT Mar 09 18:32:45.402533 (618:927) JAVA-SIPCC-UI_API: ui_update_registration_state_all_lines: ***********ALL LINES UN-REGISTERED****************
5819 DEB Mar 09 18:32:45.402838 (618:926) JAVA-SIPCC-SIP_REG_STATE: ccappFeatureUpdated: Updating the Reg State for all lines=1
5820 DEB Mar 09 18:32:45.403051 (618:926) JAVA-SNAPSHOT-CREATE: CCAPI_Line_getLineInfo:  reference pointer=b4af9478
5821 DEB Mar 09 18:32:45.403204 (618:926) JAVA-SIPCC-SIP_CC_PROV: ccsnap_gen_lineEvent: event type : REG_STATE
5822 DEB Mar 09 18:32:45.403296 (618:926) JAVA-[[MESSAGE_1.0]]: [SIPCC] --> REG_STATE() --> [PHONE-APP] : 
5823 DEB Mar 09 18:32:45.403601 (618:926) JAVA-SIPCC-SIP_CC_PROV: 1/0, CCAPI_lineInfo_getRegState: returned 0
5824 DEB Mar 09 18:32:45.403723 (618:926) JAVA-[[MESSAGE_1.0]]: [PHONE-APP] --> getRegState() --> [SIPCC] : sipcc resp: line 1 (|2222) is NOT REGISTERED
5825 NOT Mar 09 18:32:45.404120 (618:926) JAVA-Thread-4|cip.sipcc.SipCcAdapter$CcMgmtListener:  - lineNotify():mgmtState=MGMT_AWAITING_CFG_SYNC(8) line=1 registered=false inService=true regRequired = true
5826 DEB Mar 09 18:32:45.405096 (618:926) JAVA-SNAPSHOT-RELEASE: CCAPI_Line_releaseLineInfo:  reference pointer=b4af9478, ref released
5827 DEB Mar 09 18:32:45.405371 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_register_send_msg: cmd=85=SIP_REG_REQ ndx=97
5828 DEB Mar 09 18:32:45.405585 (618:927) JAVA-SIP : sip_platform_cc_mode_update : mode =0
5829 NOT Mar 09 18:32:45.405829 (618:927) JAVA-MED : updatePresentationCapTblValues : enter...
5830 NOT Mar 09 18:32:45.405951 (618:927) JAVA-MED : updatePresentationCapTblValues : orig gcap[1,0,0,0]
5831 NOT Mar 09 18:32:45.406103 (618:927) JAVA-MED : updatePresentationCapTblValues : new gcap[1,0,0,0]
5832 DEB Mar 09 18:32:45.406195 (618:927) JAVA-MED : escalateDeescalate : Ignoring video cap update
5833 NOT Mar 09 18:32:45.406287 (618:927) JAVA-MED : updateFeccCapTblValues : enter...
5834 NOT Mar 09 18:32:45.406378 (618:927) JAVA-MED : updateFeccCapTblValues : orig gcap[0]
5835 NOT Mar 09 18:32:45.406470 (618:927) JAVA-MED : updateFeccCapTblValues : new gcap[0]
5836 DEB Mar 09 18:32:45.406531 (618:927) JAVA-MED : escalateDeescalate : Ignoring video cap update
5837 NOT Mar 09 18:32:45.406622 (618:927) JAVA-SIPCC-SIP_CTRL: sip_restart: sip_taskInited is set to true 
5838 NOT Mar 09 18:32:45.408331 (618:927) JAVA-SIPCC-CC_API: 0/0, cc_int_fail_fallback: SIP -> GSM: FAILOVER_FALLBACK   
5839 DEB Mar 09 18:32:45.410315 (618:927) JAVA-SIPCC-MSG_SEND_REQ: SIPSPISendSubscribe: Sending SUBSCRIBE...
5840 DEB Mar 09 18:32:45.415137 (618:927) JAVA-edge_send_get: Length of data read from edge_gateway 64
5841 DEB Mar 09 18:32:45.415382 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipAddSessionIdHeader: tracking ID: 7821_cead41d7-0010-5000-a000-c80084aa8743
5842 DEB Mar 09 18:32:45.415534 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipAddSessionIdHeader: local_uuid: cead41d700105000a000c80084aa8743 remote_uuid: 
5843 DEB Mar 09 18:32:45.415870 (618:927) JAVA-SIPCC-SIP_SUB: sm_add_contact: adding device name [SEPC80084AA8743] to contact header 
5844 DEB Mar 09 18:32:45.416450 (618:927) JAVA-SIPCC-SIP_SUB: sipSPIAddRouteHeadersToSubNot: Route info not available; will not add Route header.
5845 DEB Mar 09 18:32:45.416602 (618:927) JAVA-SIPCC-SIP_SUB: xmlEncodeEventData: Encode event data: entered,
5846 DEB Mar 09 18:32:45.416725 (618:927) JAVA-SIPCC-SIP_SUB: xmlEncodeEventData: Framed raw buffer: length = 570,
5847 DEB Mar 09 18:32:45.417091 (618:927) JAVA-SIP : sipTransportCreateSendMessage : sippmh_write() with message size=[1503] 
5848 NOT Mar 09 18:32:45.417304 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_dump_send_msg_info: <192.168.7.200:5060>:REFER s: <sip:192.168.7.200> :1000 REFER::c80084aa-87430006-1a48a291-451dd0ff@192.168.7.104
5849 DEB Mar 09 18:32:45.417793 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportSendMessage: Sip msg sent handle=<46>,length=<1503>, message=

 ##### 18:32:45.419807 || A REFER to the Home Cluster for the "DeviceTLInfo" alarm with the ITL/TFTP from the Visiting Cluster
5850 DEB Mar 09 18:32:45.419807 (618:927) JAVA-sipio-sent---> REFER sip:192.168.7.200 SIP/2.0^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK20eb83bf^M
	From: "2222" <sip:2222@192.168.7.104>;tag=c80084aa874300122cd20b33-123852dd^M
	To: <sip:192.168.7.200>^M
	Call-ID: c80084aa-87430006-1a48a291-451dd0ff@192.168.7.104^M
	Session-ID: cead41d700105000a000c80084aa8743;remote=00000000000000000000000000000000^M
	Date: Sat, 09 Mar 2019 18:32:45 GMT^M
	CSeq: 1000 REFER^M
	User-Agent: Cisco-CP7821/12.1.1^M
	Expires: 10^M
	Max-Forwards: 70^M
	Contact: <sip:04984998-fe29-08c0-6d47-5593bf4ce606@192.168.7.104:51778;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEPC80084AA8743"^M
	Require: norefersub^M
	Referred-By: "2222" <sip:2222@192.168.7.104>^M
	Refer-To: cid:5098d8fa@192.168.7.104^M
	Content-Id: <5098d8fa@192.168.7.104>^M
	Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE^M
	Content-Length: 569^M
	Content-Type: application/x-cisco-alarm+xml^M
	Content-Disposition: session;handling=required^M
	^M
	<?xml version="1.0" encoding="UTF-8"?>
	<x-cisco-alarm>
	<Alarm Name="DeviceT
5851 DEB Mar 09 18:32:45.420021 (618:927) JAVA-LInfo">
	<ParameterList>
	<String name="DeviceName">SEPC80084AA8743</String>
	<String name="IPv4Address">192.168.7.104</String>
	<String name="IPv6Address"></String>
	<String name="CTL_Signature">Not Installed</String>
	<String name="CTL_TFTP_Server">N/A</String>
	<String name="ITL_Signature">1B A1 C9 07 E9 9E 4D 3C 53 9D C8 14 24 AF 6C 9F 7D CE 4D 6D </String>
	<String name="ITL_TFTP_Server">cucm-115.home.lab</String>
	<String name="StatusCode">3</String>
	</ParameterList>
	</Alarm>
	</x-cisco-alarm>
5852 DEB Mar 09 18:32:45.420173 (618:927) JAVA-::End-Of-Sip-Message::
5853 DEB Mar 09 18:32:45.420295 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportSendMessage: Starting reTx timer for 32000 secs
5854 DEB Mar 09 18:32:45.420784 (618:927) JAVA-[[MESSAGE_1.0]]: [SIPCC] --> REFER sip:192.168.7.200 SIP/2.0() --> [192.168.7.200] : 
5855 DEB Mar 09 18:32:45.421486 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_send_msg_for_alarm: local_uuid: , remote_uuid: , type:0, state:0
5856 DEB Mar 09 18:32:45.421638 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_send_msg_for_alarm: Sent:REFER sip:192.168.7.200 SIP/2.0  Cseq:1000 REFER CallId:c80084aa-87430006-1a48a291-451dd0ff@192.168.7.104    
5857 DEB Mar 09 18:32:45.422157 (618:927) JAVA-SIPCC-MSG_SEND_REQ: SIPSPISendSubscribe: Sending SUBSCRIBE...
5858 NOT Mar 09 18:32:45.423134 (624:624) metmand-update_sessionid: Received NULL or Invalid Type
5859 NOT Mar 09 18:32:45.423286 (624:624) metmand-update_sessionid: Local UUID: 
5860 NOT Mar 09 18:32:45.423408 (624:624) metmand-update_sessionid: Remote UUID: 
5861 DEB Mar 09 18:32:45.426064 (618:927) JAVA-edge_send_get: Length of data read from edge_gateway 64
5862 DEB Mar 09 18:32:45.426308 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipAddSessionIdHeader: tracking ID: 7821_cead41d7-0010-5000-a000-c80084aa8743
5863 DEB Mar 09 18:32:45.426430 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipAddSessionIdHeader: local_uuid: cead41d700105000a000c80084aa8743 remote_uuid: 
5864 DEB Mar 09 18:32:45.426766 (618:927) JAVA-SIPCC-SIP_SUB: sm_add_contact: adding device name [SEPC80084AA8743] to contact header 
5865 DEB Mar 09 18:32:45.427803 (618:927) JAVA-SIPCC-SIP_SUB: sipSPIAddRouteHeadersToSubNot: Route info not available; will not add Route header.
5866 DEB Mar 09 18:32:45.427956 (618:927) JAVA-SIPCC-SIP_SUB: xmlEncodeEventData: Encode event data: entered,
5867 DEB Mar 09 18:32:45.428109 (618:927) JAVA-SIPCC-SIP_SUB: xmlEncodeEventData: Framed raw buffer: length = 573,
5868 DEB Mar 09 18:32:45.428505 (618:927) JAVA-SIP : sipTransportCreateSendMessage : sippmh_write() with message size=[1506] 
5869 NOT Mar 09 18:32:45.428689 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_dump_send_msg_info: <192.168.7.200:5060>:REFER s: <sip:192.168.7.200> :1000 REFER::c80084aa-87430007-4ba0abc2-6f7623e8@192.168.7.104
5870 DEB Mar 09 18:32:45.429177 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportSendMessage: Sip msg sent handle=<46>,length=<1506>, message=

 ##### 18:32:45.430978 || A REFER to the Home Cluster for the "DeviceTLInfo" alarm with the ITL/TFTP from the Home Cluster
5871 DEB Mar 09 18:32:45.430978 (618:927) JAVA-sipio-sent---> REFER sip:192.168.7.200 SIP/2.0^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK63f5b3c9^M
	From: "2222" <sip:2222@192.168.7.104>;tag=c80084aa874300136f85470f-0b656e67^M
	To: <sip:192.168.7.200>^M
	Call-ID: c80084aa-87430007-4ba0abc2-6f7623e8@192.168.7.104^M
	Session-ID: cead41d700105000a000c80084aa8743;remote=00000000000000000000000000000000^M
	Date: Sat, 09 Mar 2019 18:32:45 GMT^M
	CSeq: 1000 REFER^M
	User-Agent: Cisco-CP7821/12.1.1^M
	Expires: 10^M
	Max-Forwards: 70^M
	Contact: <sip:04984998-fe29-08c0-6d47-5593bf4ce606@192.168.7.104:51778;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEPC80084AA8743"^M
	Require: norefersub^M
	Referred-By: "2222" <sip:2222@192.168.7.104>^M
	Refer-To: cid:3801f297@192.168.7.104^M
	Content-Id: <3801f297@192.168.7.104>^M
	Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE^M
	Content-Length: 572^M
	Content-Type: application/x-cisco-alarm+xml^M
	Content-Disposition: session;handling=required^M
	^M
	<?xml version="1.0" encoding="UTF-8"?>
	<x-cisco-alarm>
	<Alarm Name="DeviceT
5872 DEB Mar 09 18:32:45.431161 (618:927) JAVA-LInfo">
	<ParameterList>
	<String name="DeviceName">SEPC80084AA8743</String>
	<String name="IPv4Address">192.168.7.104</String>
	<String name="IPv6Address"></String>
	<String name="CTL_Signature">Not Installed</String>
	<String name="CTL_TFTP_Server">N/A</String>
	<String name="ITL_Signature">A3 6D CF 5D 1E 65 4D 76 CD E3 62 4B 22 BD 45 CF 85 75 44 A6 </String>
	<String name="ITL_TFTP_Server">clstr-2-pub.home.lab</String>
	<String name="StatusCode">3</String>
	</ParameterList>
	</Alarm>
	</x-cisco-alarm>
5873 DEB Mar 09 18:32:45.431283 (618:927) JAVA-::End-Of-Sip-Message::
5874 DEB Mar 09 18:32:45.431405 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportSendMessage: Starting reTx timer for 32000 secs
5875 DEB Mar 09 18:32:45.432168 (618:927) JAVA-[[MESSAGE_1.0]]: [SIPCC] --> REFER sip:192.168.7.200 SIP/2.0() --> [192.168.7.200] : 
5876 DEB Mar 09 18:32:45.432931 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_send_msg_for_alarm: local_uuid: , remote_uuid: , type:0, state:0
5877 DEB Mar 09 18:32:45.433083 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_send_msg_for_alarm: Sent:REFER sip:192.168.7.200 SIP/2.0  Cseq:1000 REFER CallId:c80084aa-87430007-4ba0abc2-6f7623e8@192.168.7.104    
5878 DEB Mar 09 18:32:45.433358 (618:927) JAVA-SIPCC-SIP_STATE: 97/1, sip_reg_sm_change_state: Registration state change: SIP_REG_STATE_IDLE ---> SIP_REG_STATE_IDLE
5879 DEB Mar 09 18:32:45.433816 (618:927) JAVA-SIPCC-SIP_STATE: 1/0, sip_stop_ack_timer:  ccb->index=97 ack_timer_index=0 
5880 DEB Mar 09 18:32:45.433969 (618:927) JAVA-SIPCC-SIP_STATE: 1/0, sip_start_ack_timer:  ccb->index=97 ack_timer_index=0 
5881 NOT Mar 09 18:32:45.434548 (624:624) metmand-update_sessionid: Received NULL or Invalid Type
5882 NOT Mar 09 18:32:45.434701 (624:624) metmand-update_sessionid: Local UUID: 
5883 NOT Mar 09 18:32:45.434762 (624:624) metmand-update_sessionid: Remote UUID: 
5884 DEB Mar 09 18:32:45.435098 (618:927) JAVA-[getDeployMode] deploy-mode:1 
5885 DEB Mar 09 18:32:45.435647 (618:927) JAVA-SIPCC-SIP_REG: ccsip_is_reg_refresh: Registration Refresh is FALSE
5886 DEB Mar 09 18:32:45.435800 (618:927) JAVA-SIPCC-SIP_REG_BULK: ccsip_handle_ev_reg_req: Bulk Reg Conditions met
5887 DEB Mar 09 18:32:45.436380 (618:927) JAVA-[getDeployMode] deploy-mode:1 
5888 DEB Mar 09 18:32:45.436624 (618:927) JAVA-SIPCC-MSG_SEND_REQ: sipSPIBuildRegisterHeaders: Sending REGISTER...
5889 DEB Mar 09 18:32:45.439493 (618:927) JAVA-edge_send_get: Length of data read from edge_gateway 64
5890 DEB Mar 09 18:32:45.439737 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipAddSessionIdHeader: tracking ID: 7821_cead41d7-0010-5000-a000-c80084aa8743
5891 DEB Mar 09 18:32:45.439889 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipAddSessionIdHeader: local_uuid: cead41d700105000a000c80084aa8743 remote_uuid: 
5892 NOT Mar 09 18:32:45.440134 (618:927) JAVA-ccsip_messaging: sipSPIAddContactHeader: CFGID_DEVICE_NAME = SEPC80084AA8743
5893 NOT Mar 09 18:32:45.440347 (618:927) JAVA-ccsip_messaging: sipSPIAddContactHeader: ccb->call_mode = 0, display_name = 2222
5894 DEB Mar 09 18:32:45.441080 (618:927) JAVA-VCM : vcmIsICESupported :  mediaTraversalMode(1)=Standard.
5895 DEB Mar 09 18:32:45.467144 (618:927) JAVA-[getDeployMode] deploy-mode:1 
5896 DEB Mar 09 18:32:45.467327 (618:927) JAVA-SIPCC-SIP_SUB: xmlEncodeEventData: Encode event data: entered,
5897 NOT Mar 09 18:32:45.467816 (618:927) JAVA-SIPCC-SIP_REG: addDefaultOptionInd: support bfcp 1 
5898 NOT Mar 09 18:32:45.467999 (618:927) JAVA-SIPCC-SIP_REG: addDefaultOptionInd: frame_rcc_options_ind_msg: check mobility refresh 0 
5899 NOT Mar 09 18:32:45.468090 (618:927) JAVA-SIPCC-SIP_REG: addDefaultOptionInd: support flex_dscp=0 
5900 NOT Mar 09 18:32:45.468914 (618:927) JAVA-SIPCC-SIP_REG: xmlEncodeEventData: returned content after encoding:
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
	    <cfwdall-anyline></cfwdall-anyline>
	    <coaching></coaching>
	    <oosalarm></oosalarm>
	    <rpid-orig-called></rpid-orig-called>
	    <x-cisco-number></x-cisco-number>
	    <bfcp></bfcp>
	    <ix></ix>
	    <gatewayrecording></gatewayrecording>
	    <conferenceDisplayInstance></conferenceDisplayInstance>
	  </optionsind>
	</x-cisco-remotecc-request>
5901 DEB Mar 09 18:32:45.469067 (618:927) JAVA-SIPCC-SIP: addOptionsIndBody: Framed buffer: length = 856,
5902 DEB Mar 09 18:32:45.469464 (618:927) JAVA-SIP : sipTransportCreateSendMessage : sippmh_write() with message size=[2516] 
5903 DEB Mar 09 18:32:45.470013 (618:927) JAVA-SIPCC-SIP_TRANS: sipTransportSendMessage: Sip msg sent handle=<46>,length=<2516>, message=

 ##### 18:32:45.473187 || A register message to the CCM server on the Home Cluster
5904 DEB Mar 09 18:32:45.473187 (618:927) JAVA-sipio-sent---> REGISTER sip:192.168.7.200 SIP/2.0^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK66da98ae^M
	From: <sip:2222@192.168.7.200>;tag=c80084aa8743001411d7279b-7ecf20ad^M
	To: <sip:2222@192.168.7.200>^M
	Call-ID: c80084aa-87430003-255b99f4-783a63d4@192.168.7.104^M
	Max-Forwards: 70^M
	Session-ID: cead41d700105000a000c80084aa8743;remote=00000000000000000000000000000000^M
	Date: Sat, 09 Mar 2019 18:32:45 GMT^M
	CSeq: 113 REGISTER^M
	User-Agent: Cisco-CP7821/12.1.1^M
	Contact: <sip:04984998-fe29-08c0-6d47-5593bf4ce606@192.168.7.104:51778;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-c80084aa8743>";+u.sip!devicename.ccm.cisco.com="SEPC80084AA8743";+u.sip!model.ccm.cisco.com="621"^M
	Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1^M
	Reason: SIP;cause=200;text="cisco-alarm:23 Name=SEPC80084AA8743 ActiveLoad=si
5905 DEB Mar 09 18:32:45.473370 (618:927) JAVA-p78xx.12-1-1-12.loads InactiveLoad=sip78xx.10-3-1-12.loads Last=reset-restart"^M
	Expires: 3600^M
	Content-Type: multipart/mixed; boundary=uniqueBoundary^M
	Mime-Version: 1.0^M
	Content-Length: 1313^M
	^M
	--uniqueBoundary^M
	Content-Type: application/x-cisco-remotecc-request+xml^M
	Content-Disposition: session;handling=optional^M
	^M
	<?xml version="1.0" encoding="UTF-8"?>
	<x-cisco-remotecc-request>
	<bulkregisterreq>
	<contact all="true">
	<register></register>
	</contact>
	</bulkregisterreq>
	</x-cisco-remotecc-request>
	^M
	--uniqueBoundary^M
	Content-Type: application/x-cisco-remotecc-request+xml^M
	Content-Disposition: session;handling=optional^M
	^M
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
	    
5906 DEB Mar 09 18:32:45.473462 (618:927) JAVA-<presence usage="blf speed dial">
	      <unot></unot>
	      <sub></sub>
	    </presence>
	    <joinreq></joinreq>
	    <cfwdall-anyline></cfwdall-anyline>
	    <coaching></coaching>
	    <oosalarm></oosalarm>
	    <rpid-orig-called></rpid-orig-called>
	    <x-cisco-number></x-cisco-number>
	    <bfcp></bfcp>
	    <ix></ix>
	    <gatewayrecording></gatewayrecording>
	    <conferenceDisplayInstance></conferenceDisplayInstance>
	  </optionsind>
	</x-cisco-remotecc-request>^M
	--uniqueBoundary--^M
5907 DEB Mar 09 18:32:45.473584 (618:927) JAVA-::End-Of-Sip-Message::
5908 DEB Mar 09 18:32:45.473737 (618:927) JAVA-SIPCC-ENTRY: LINE 97/1: sipTransportSendMessage            : Stopping reTx timer
5909 DEB Mar 09 18:32:45.473859 (618:927) JAVA-[[MESSAGE_1.0]]: [SIPCC] --> REGISTER sip:192.168.7.200 SIP/2.0() --> [192.168.7.200] : 
5910 DEB Mar 09 18:32:45.474500 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_send_msg_for_alarm: local_uuid: , remote_uuid: , type:1, state:16
5911 DEB Mar 09 18:32:45.474652 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_send_msg_for_alarm: Sent:REGISTER sip:192.168.7.200 SIP/2.0  Cseq:113 REGISTER CallId:c80084aa-87430003-255b99f4-783a63d4@192.168.7.104    
5912 DEB Mar 09 18:32:45.474896 (618:927) JAVA-SIPCC-SIP_REG_BULK: ccsip_set_bulk_reg_status: Transitioning bulk reg status from BULK_REG_NONE to BULK_REG_INITIATED
5913 DEB Mar 09 18:32:45.475018 (618:927) JAVA-SIPCC-SIP_STATE: 97/1, sip_reg_sm_change_state: Registration state change: SIP_REG_STATE_IDLE ---> SIP_REG_STATE_REGISTERING
5914 NOT Mar 09 18:32:45.475659 (624:624) metmand-update_sessionid: Received NULL or Invalid Type
5915 NOT Mar 09 18:32:45.475812 (624:624) metmand-update_sessionid: Local UUID: 
5916 NOT Mar 09 18:32:45.475965 (624:624) metmand-update_sessionid: Remote UUID: 
5917 DEB Mar 09 18:32:45.476880 (618:927) JAVA-SIPCC-HTTPISH: httpish_msg_process_network_msg: Content Length 0, Bytes Remaining 703.
5918 DEB Mar 09 18:32:45.477094 (618:927) JAVA-SIP : sip_tcp_newmsg_to_spi : Sip message rcv: message=

 ##### 18:32:45.477430 || The first REFER is accepted
5919 DEB Mar 09 18:32:45.477430 (618:927) JAVA-sipio-recv<--- SIP/2.0 202 Accepted^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK20eb83bf^M
	From: "2222" <sip:2222@192.168.7.104>;tag=c80084aa874300122cd20b33-123852dd^M
	To: <sip:192.168.7.200>;tag=417801073^M
	Date: Sat, 09 Mar 2019 18:32:46 GMT^M
	Call-ID: c80084aa-87430006-1a48a291-451dd0ff@192.168.7.104^M
	CSeq: 1000 REFER^M
	Contact: <sip:192.168.7.200:5060;transport=tcp>^M
	Content-Length: 0^M
	^M
5920 DEB Mar 09 18:32:45.477552 (618:927) JAVA-::End-Of-Sip-Message::
5921 DEB Mar 09 18:32:45.477643 (618:927) JAVA-[[MESSAGE_1.0]]: [192.168.7.200] --> SIP/2.0 202 Accepted() --> [SIPCC] : 
5922 NOT Mar 09 18:32:45.477796 (618:927) JAVA-SIPCC-SIP_MSG_RECV: ccsip_dump_recv_msg_info: <192.168.7.200:0   >:202 Acc: "2222" <sip:2222@192.168.7.104>;tag=c80084aa874300122cd20b33-123852dd :1000 REFER::c80084aa-87430006-1a48a291-451dd0ff@192.168.7.104
5923 DEB Mar 09 18:32:45.478376 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_rcvd_msg_for_alarm: local_uuid: , remote_uuid: , type:0, state:0
5924 DEB Mar 09 18:32:45.478528 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_rcvd_msg_for_alarm: Rcvd:SIP/2.0 202 Accepted  Cseq:1000 REFER CallId:c80084aa-87430006-1a48a291-451dd0ff@192.168.7.104    
5925 DEB Mar 09 18:32:45.479230 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipGetSessionId: Remote Session ID: (null)
5926 DEB Mar 09 18:32:45.479963 (618:927) JAVA-[getDeployMode] deploy-mode:1 
5927 DEB Mar 09 18:32:45.480176 (618:927) JAVA-SIPCC-SIP_ALARM: remove_stored_alarm: Alarm at index=0 of request_id=6 sent out successfully
5928 DEB Mar 09 18:32:45.482099 (618:927) JAVA-SIPCC-HTTPISH: httpish_msg_process_network_msg: Content Length 0, Bytes Remaining 319.
5929 DEB Mar 09 18:32:45.482313 (618:927) JAVA-SIP : sip_tcp_newmsg_to_spi : Sip message rcv: message=

 ##### 18:32:45.482679 || The second REFER is accepted
5930 DEB Mar 09 18:32:45.482679 (618:927) JAVA-sipio-recv<--- SIP/2.0 202 Accepted^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK63f5b3c9^M
	From: "2222" <sip:2222@192.168.7.104>;tag=c80084aa874300136f85470f-0b656e67^M
	To: <sip:192.168.7.200>;tag=231462831^M
	Date: Sat, 09 Mar 2019 18:32:46 GMT^M
	Call-ID: c80084aa-87430007-4ba0abc2-6f7623e8@192.168.7.104^M
	CSeq: 1000 REFER^M
	Contact: <sip:192.168.7.200:5060;transport=tcp>^M
	Content-Length: 0^M
	^M
5931 DEB Mar 09 18:32:45.482801 (618:927) JAVA-::End-Of-Sip-Message::
5932 DEB Mar 09 18:32:45.482893 (618:927) JAVA-[[MESSAGE_1.0]]: [192.168.7.200] --> SIP/2.0 202 Accepted() --> [SIPCC] : 
5933 NOT Mar 09 18:32:45.483045 (618:927) JAVA-SIPCC-SIP_MSG_RECV: ccsip_dump_recv_msg_info: <192.168.7.200:0   >:202 Acc: "2222" <sip:2222@192.168.7.104>;tag=c80084aa874300136f85470f-0b656e67 :1000 REFER::c80084aa-87430007-4ba0abc2-6f7623e8@192.168.7.104
5934 DEB Mar 09 18:32:45.483625 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_rcvd_msg_for_alarm: local_uuid: , remote_uuid: , type:0, state:0
5935 DEB Mar 09 18:32:45.483778 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_rcvd_msg_for_alarm: Rcvd:SIP/2.0 202 Accepted  Cseq:1000 REFER CallId:c80084aa-87430007-4ba0abc2-6f7623e8@192.168.7.104    
5936 DEB Mar 09 18:32:45.484480 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipGetSessionId: Remote Session ID: (null)
5937 DEB Mar 09 18:32:45.485243 (618:927) JAVA-[getDeployMode] deploy-mode:1 
5938 DEB Mar 09 18:32:45.485426 (618:927) JAVA-SIPCC-SIP_ALARM: remove_stored_alarm: Alarm at index=1 of request_id=7 sent out successfully
5939 DEB Mar 09 18:32:45.486067 (618:927) JAVA-SIP : sip_tcp_newmsg_to_spi : Sip message rcv: message=

 ##### 18:32:45.486403 || The Home Cluster is trying to do the register
5940 DEB Mar 09 18:32:45.486403 (618:927) JAVA-sipio-recv<--- SIP/2.0 100 Trying^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK66da98ae^M
	From: <sip:2222@192.168.7.200>;tag=c80084aa8743001411d7279b-7ecf20ad^M
	To: <sip:2222@192.168.7.200>^M
	Date: Sat, 09 Mar 2019 18:32:46 GMT^M
	Call-ID: c80084aa-87430003-255b99f4-783a63d4@192.168.7.104^M
	CSeq: 113 REGISTER^M
	Content-Length: 0^M
	^M
5941 DEB Mar 09 18:32:45.486525 (618:927) JAVA-::End-Of-Sip-Message::
5942 DEB Mar 09 18:32:45.486647 (618:927) JAVA-[[MESSAGE_1.0]]: [192.168.7.200] --> SIP/2.0 100 Trying() --> [SIPCC] : 
5943 DEB Mar 09 18:32:45.487562 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_rcvd_msg_for_alarm: local_uuid: , remote_uuid: , type:1, state:17
5944 DEB Mar 09 18:32:45.487715 (618:927) JAVA-SIPCC-SIP_MSG_SEND: ccsip_store_rcvd_msg_for_alarm: Rcvd:SIP/2.0 100 Trying  Cseq:113 REGISTER CallId:c80084aa-87430003-255b99f4-783a63d4@192.168.7.104    
5945 DEB Mar 09 18:32:45.488173 (618:927) JAVA-SIPCC-SIP_BRANCH: sip_sm_ccb_match_branch_cseq: Matched branch_id & CSeq
5946 DEB Mar 09 18:32:45.488325 (618:927) JAVA-SIPCC-SIP_SESSION_ID: sipGetSessionId: Remote Session ID: (null)
5947 DEB Mar 09 18:32:45.489149 (618:927) JAVA-SIPCC-SIP_RESP: sipSPICheckResponse: Response match: callid=c80084aa-87430003-255b99f4-783a63d4@192.168.7.104, cseq=113, cseq_method=REGISTER
5948 DEB Mar 09 18:32:45.489394 (618:927) JAVA-SIPCC-FUNC_ENTRY: LINE 97/1: ccsip_handle_ev_1xx                : SIP_REG_STATE_REGISTERING <- SIP(100)
5949 NOT Mar 09 18:32:45.490370 (624:624) metmand-update_sessionid: Received NULL or Invalid Type
5950 NOT Mar 09 18:32:45.490523 (624:624) metmand-update_sessionid: Local UUID: 
5951 NOT Mar 09 18:32:45.490614 (624:624) metmand-update_sessionid: Remote UUID: 
5952 NOT Mar 09 18:32:45.490828 (624:624) metmand-update_sessionid: Received NULL or Invalid Type
5953 NOT Mar 09 18:32:45.490920 (624:624) metmand-update_sessionid: Local UUID: 
5954 NOT Mar 09 18:32:45.491011 (624:624) metmand-update_sessionid: Remote UUID: 
5955 NOT Mar 09 18:32:45.491164 (624:624) metmand-update_sessionid: Received NULL or Invalid Type
5956 NOT Mar 09 18:32:45.491255 (624:624) metmand-update_sessionid: Local UUID: 
5957 NOT Mar 09 18:32:45.491316 (624:624) metmand-update_sessionid: Remote UUID: 
5958 INF Mar 09 18:32:45.508316 (618:891) JAVA-System P7-display MQThread|cip.callui.market.OverviewModel:? - OverviewModel---------------------propertychange regPromptProperty.getValue() = Registration in progress
5959 DEB Mar 09 18:32:45.508835 (618:891) JAVA-System P7-display MQThread|cip.callui.market.OverviewModel$MyCallAgentListener:OverviewModel notifyDisplay - ++++bug 1015782 debug++++  notifyText=Registering
5960 DEB Mar 09 18:32:45.509171 (618:891) JAVA-System P7-display MQThread|cip.callui.market.OverviewModel$MyCallAgentListener:OverviewModel notifyDisplay - ++++bug 1015782 debug++++  isRegistered=false
5961 ERR Mar 09 18:32:45.509567 (618:891) JAVA-System P7-display MQThread|cip.app.AppFrame:startNotification - Notification: Registeringcan't be display in status prompt
5962 INF Mar 09 18:32:45.510880 (618:891) JAVA-System P7-display MQThread|cip.callui.market.OverviewModel:? - OverviewModel---------------------hasServer headSubPromptVal: false
5963 DEB Mar 09 18:32:45.540942 (618:891) JAVA-SNAPSHOT-CREATE: CCAPI_Device_getDeviceInfo:  g_deviceInfo.ins_state=2
5964 DEB Mar 09 18:32:45.541156 (618:891) JAVA-SNAPSHOT-CREATE: CCAPI_Device_getDeviceInfo:  deviceInfo->sis_name=
5965 DEB Mar 09 18:32:45.541248 (618:891) JAVA-SNAPSHOT-CREATE: CCAPI_Device_getDeviceInfo:  reference pointer=b4af9478
5966 DEB Mar 09 18:32:45.541370 (618:891) JAVA-SNAPSHOT-CREATE: CCAPI_Device_getDeviceInfo:  deviceInfo->ins_state=2
5967 DEB Mar 09 18:32:45.541492 (618:891) JAVA-SIPCC-SIP_CC_PROV: 0xb4af9478, CCAPI_DeviceInfo_getCUCMMode: returned 00
5968 DEB Mar 09 18:32:45.541766 (618:891) JAVA-SNAPSHOT-RELEASE: CCAPI_Device_releaseDeviceInfo:  reference pointer=b4af9478
5969 DEB Mar 09 18:32:45.593560 (618:927) JAVA-SIPCC-HTTPISH: httpish_msg_process_network_msg: Content Length 381, Bytes Remaining 1615.
5970 DEB Mar 09 18:32:45.593956 (618:927) JAVA-SIP : sip_tcp_newmsg_to_spi : Sip message rcv: message=

 ##### 18:32:45.595055 || The Home Cluster successfully did the register
5971 DEB Mar 09 18:32:45.595055 (618:927) JAVA-sipio-recv<--- SIP/2.0 200 OK^M
	Via: SIP/2.0/TCP 192.168.7.104:51778;branch=z9hG4bK66da98ae^M
	From: <sip:2222@192.168.7.200>;tag=c80084aa8743001411d7279b-7ecf20ad^M
	To: <sip:2222@192.168.7.200>;tag=2121423204^M
	Date: Sat, 09 Mar 2019 18:32:46 GMT^M
	Call-ID: c80084aa-87430003-255b99f4-783a63d4@192.168.7.104^M
	Server: Cisco-CUCM11.5^M
	CSeq: 113 REGISTER^M
	Expires: 120^M
	Contact: <sip:04984998-fe29-08c0-6d47-5593bf4ce606@192.168.7.104:51778;transport=tcp>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-c80084aa8743>";+u.sip!devicename.ccm.cisco.com="SEPC80084AA8743";+u.sip!model.ccm.cisco.com="621";x-cisco-newreg^M
	Supported: X-cisco-srtp-fallback,X-cisco-sis-8.0.0^M
	Content-Type: application/x-cisco-remotecc-response+xml^M
	Content-Length: 381^M
	^M
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
	<presence usage="blf speed dial"><unot/></p
5972 DEB Mar 09 18:32:45.595238 (618:927) JAVA-resence>
	<joinreq></joinreq>
	<ix/>
	<bfcp/>
	</optionsind>
	</response>
	</x-cisco-remotecc-response>
	^M
5973 DEB Mar 09 18:32:45.595391 (618:927) JAVA-::End-Of-Sip-Message::
5974 DEB Mar 09 18:32:45.595513 (618:927) JAVA-[[MESSAGE_1.0]]: [192.168.7.200] --> SIP/2.0 200 OK() --> [SIPCC] :
```

#### PCAP review for the phone

This filter shows all the traffic between the phone and the two clusters:

ip.addr == 192.168.7.100 || ip.addr == 192.168.7.100

This filter narrows it down to show the important traffic:

((ip.addr== 192.168.7.100 || ip.addr == 192.168.7.200) && (sip || http || tcp.port == 2445 || udp.port == 69) && (frame.number <= 596))

## Related Information

### Contributed by Cisco Engineers

Patrick Kinane

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)