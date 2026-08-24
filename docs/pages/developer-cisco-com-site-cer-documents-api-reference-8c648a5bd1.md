---
doc_id: developer-cisco-com-site-cer-documents-api-reference-8c648a5bd1
source_url: https://developer.cisco.com/site/cer/documents/api-reference/
retrieved_at: 2026-08-24T22:13:34.102912+00:00
---

This document provides all the information you need to integrate and build applications with Cisco Emergency Responder (CER).

The CER API supports XML formatted data. Use the Accept: text/xml header in all CER requests.

Explore the API resource documentation for details.

# Authentication

All API operations for CER require HTTPS, and are read-only using the HTTP GET method.  No HTTP body is expected for requests.

A combination of HTTP Basic Authentication and a HTTP cookie is required to authenticate API requests.

If API request credentials (username/password or cookie) are incorrect/expired, an HTTP 401 Not Authorized status code will be returned.

To successfully make an API request, both the HTTP Authorization: Basic and Cookie: JSESSIONID headers must be present.  For example:

Code Snippet

```
GET /cerappservices/export/authenticate/status HTTP/1.1
Authorization: Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ=
Accept: text/xml
Host: 10.10.20.3
Cookie: JSESSIONID=E1D64B05FA24B430F5FB5A0933539FB6
```

In order to obtain a session cookie that can be used in later authenticated requests, it is necessary to first make an initial API request ommitting the Authorization and Cookie headers.  The response will indicate a HTTP 401 Unauthorized status but will include a Set-Cookie header containing a newly generated JSESSIONID cookie:

Request

Code Snippet

```
GET /cerappservices/export/authenticate/status HTTP/1.1
Accept: text/xml
Host: 10.10.20.3
```

Response

Code Snippet

```
HTTP/1.1 401 Unauthorized
Set-Cookie: JSESSIONID=E1D64B05FA24B430F5FB5A0933539FB6; Path=/cerappservices; Secure; HttpOnly
WWW-Authenticate: Basic
...
```

This cookie can then be provided with subsequent authenticated requests, as above. JSESSIONID cookies have an expiration time of 20 minutes, which is renewed with each successfully authenticated request.  If the cookie expires, requests will fail with a 401 status, and a new session cookie will need to be obtained as above.

Note, if using a browser to access CER API resource URLs directly, the browser will prompt for the Basic Auth access credentials (username and password) each time - the JSESSIONID cookie should be handled transparently by the browser.

# API reference

## /authentication

http

```
GET http://{CER-IP}/cerappservices/export/authenticate/status
```

The /authentication resource provides a way to test API connectivity and validate API user credentials.  The response indicates whether your credentials are authenticated on both the CER Publisher and the Subscriber.

Response examples

Successful on both Publisher and Subscriber

xml

```
< authentication > < status > Authentication successful on publisher </ status > < subscriber > < status > Subscriber authentication Successful </ status > < ipaddress > 10.194.121.54 </ ipaddress > < hostname > cer54-8 </ hostname > </ subscriber > </ authentication >
```

Notes:

- Publisher details are added

- While testing connectivity, username and password are sent for authentication on Publisher

- Authentication is successful on both Publisher and Subscriber

Authentication is successful on Publisher but fails on Subscriber

xml

```
< authentication > < status > Authentication successful on publisher </ status > < subscriber > < status > Subscriber authentication failed </ status > </ subscriber > </ authentication >
```

- Publisher details are added

- While testing connectivity, username and password are sent for authentication on Publisher

- Authentication is successful on Publisher but fails on Subscriber

Authentication fails on standalone Publisher

xml

```
< authentication > < status > Authentication failed on publisher </ status > </ authentication >
```

- Publisher details are added

- While testing connectivity, username and password are sent for authentication on Publisher

- Authentication fails on standalone Publisher

Publisher is active

xml

```
< authentication > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ authentication >
```

- Publisher details are added

- While testing connectivity, username and password are sent for authentication on Publisher

- If Publisher is active, Subscriber login or viewing details of Subscriber is restricted.

- CER cannot connect to Subscriber if Publisher is active.

- Only details such as Switch Port and Unlocated Phones can be exported from Publisher.

Authentication fails on Publisher

xml

```
< authentication > < status > Authentication failed on publisher </ status > </ authentication >
```

- Publisher details are added

- While testing connectivity, username and password are sent for authentication on Publisher

- If authentication fails on Publisher, details cannot be exported from Publisher or Subscriber.

Authentication is successful on standalone Publisher

xml

```
< authentication > < status > Authentication successful on publisher </ status > < subscriber > < status > NO Subscriber </ status > </ subscriber > </ authentication >
```

- ublisher details are added

- While testing connectivity, username and password are sent for authentication on Publisher

- Authentication is successful on standalone Publisher

## /discoverystatus

Code Snippet

```
GET http://{CER-IP}/cerappservices/export/discoverystatus
```

The Discovery Status API retrieves the data discovery status from the box, indicating one of the following:

- Initial discovery is complete

- Tables are being modified

- Major discovery is in progress

- Discovery is complete.

If discovery is complete, data from CER can be retrieved.

Response examples

Initial discovery is not done

xml

```
< discoverystatus > < status > Intial discovery not done </ status > </ discoverystatus >
```

Initial discovery is not done, meaning that major discovery has never been executed on the box

Tables are being modified

xml

```
< discoverystatus > < status > Tables are being modified, please try later. </ status > </ discoverystatus >
```

Tables are being modified during data collection

Discovery in progess

xml

```
< discoverystatus > < status > Major discovery is in progress, please try later. </ status > </ discoverystatus >
```

Major discovery is in progess: try again later

Discovery is complete

xml

```
< discoverystatus > < status > Discovery is complete. </ status > </ discoverystatus >
```

Discovery is complete, and data from CER can now be retrieved

## /switchport/info

Code Snippet

```
GET http://{CER-IP}/cerappservices/export/switchport/info
```

The /switchport/info resource retrieves the switch port information available on CER. Call /discoverystatus to confirm that discovery is complete before invoking this API.

Response examples

Switch port information is available on CER

xml

```
< SwitchPort > < status > Exporting info </ status > < switchip > < SwitchHostName > switch-cer-3.cisco.com </ SwitchHostName > < SwitchIPAddress > 10.77.34.215 </ SwitchIPAddress > < portDetails > < ERLName /> < IfName > Fa0/1 </ IfName > < Location /> < PhoneMACAddress /> < PhoneExtension /> < PhoneIPAddress /> < PhoneType /> < PortDescription > 11111 </ PortDescription > < PortIdentifier > 0/3 </ PortIdentifier > < PortName > Fa0/1 </ PortName > </ portDetails > . . . </ switchip > . . . </ SwitchPort >
```

Switch port information is available on CER. The request is to the Publisher if it is the active server.

Information not available on Subscriber

xml

```
< SwitchPort > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ SwitchPort >
```

The Switch port information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from the Subscriber

Information not available on CER

xml

```
< SwitchPort > < status > No information to extract from CER. </ status > </ SwitchPort >
```

No Switch port information is available on CER

## /ipsubnet/info

http

```
GET http://{CER-IP}/cerappservices/export/ipsubnet/info
```

The IP subnet information API retrieves the IP subnet information detail available on CER, depending on the status returned by the /discoverystatus resource.

Response examples

Information not available on CER

xml

```
< IPSubnet > < status > No information to extract from CER </ status > </ IPSubnet >
```

No IP subnet information is available on CER

IP Subnet details request is on Subscriber

xml

```
< IPSubnet > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ IPSubnet >
```

The IP subnet information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from the Subscriber.

Information successfully retrieved

xml

```
< IPSubnet > < status > Exporting info </ status > < subnetdetails > < subnetID > 10.77.34.0 </ subnetID > < subnetMask > 255.255.255.0 </ subnetMask > < ERLName > Test </ ERLName > < Location /> < isIPv6Subnet > false </ isIPv6Subnet > < Isnontrackable > false </ Isnontrackable > < IPSubnetPhones > < Phone_MAC_Address > 00-1b-53-b9-3d-be </ Phone_MAC_Address > < Phone_IP_Address > 10.77.34.202 </ Phone_IP_Address > < Phone_Ext > 1004 </ Phone_Ext > < Phone_Type > Cisco 7961G-GE </ Phone_Type > </ IPSubnetPhones > </ subnetdetails > </ IPSubnet >
```

The IP subnet information is available on CER

## /unlocatedphones/info

http

```
GET http://{CER-IP}/cerappservices/export/unlocatedphones/info
```

Retrieves the unlocated phone information detail available on CER.

Response examples

Information not available on CER

xml

```
< UnlocatedDetails > < status > No information to extract from CER </ status > </ UnlocatedDetails >
```

No unlocated phone information is available on CER

Information not available on Subscriber

xml

```
< UnlocatedDetails > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ UnlocatedDetails >
```

The unlocated phone information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< UnlocatedDetails > < status > Exporting Info </ status > < PhoneDetails > < CerServerGroup > </ CerServerGroup > < PhoneIPAddr > 10.77.34.120 </ PhoneIPAddr > < PhoneMACAddr > 00059a3b7702 </ PhoneMACAddr > < PhoneExt > 1002 </ PhoneExt > < AssignedERL > </ AssignedERL > < EffectiveERL > Test4 </ EffectiveERL > < ERLUsedInfo > Manually Configured Phone Extension </ ERLUsedInfo > </ PhoneDetails > < PhoneDetails > < CerServerGroup > </ CerServerGroup > < PhoneIPAddr > 10.77.34.110 </ PhoneIPAddr > < PhoneMACAddr > 00059a3b7700 </ PhoneMACAddr > < PhoneExt > 1001 </ PhoneExt > < AssignedERL > </ AssignedERL > < EffectiveERL > Test4 </ EffectiveERL > < ERLUsedInfo > Manually Configured Phone Extension </ ERLUsedInfo > </ PhoneDetails > </ UnlocatedDetails >
```

The unlocated phone information is available on CER

## /manualconfphone/info

http

```
GET http://{CER-IP}/cerappservices/export/manualconfphone/info
```

The Manually Configured Phone Information API retrieves the manually configured phone information detail available on CER.

Response examples

Information not available on CER

xml

```
< manualconfphone > < status > No information to extract from CER </ status > </ manualconfphone >
```

No manually configured phone information is available on CER

Information not available on Subscriber

xml

```
< manualconfphone > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ manualconfphone >
```

The manually configured phone information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from the Subscriber

Information successfully retrieved

xml

```
< manualconfphone > < status > Exporting info </ status > < manualphonedetails > < Extension > 1001 </ Extension > < Type > Manual </ Type > < Version > 1.0 </ Version > < IPAddress > 10.77.34.110 </ IPAddress > < MACAddress > 00059a3b7700 </ MACAddress > < ERLName > Test4 </ ERLName > < Location > Bangalore </ Location > </ manualphonedetails > < manualphonedetails > < Extension > 1002 </ Extension > < Type > Manual </ Type > < Version > 1.0 </ Version > < IPAddress > 10.77.34.120 </ IPAddress > < MACAddress > 00059a3b7702 </ MACAddress > < ERLName > Test4 </ ERLName > < Location > Bangalore </ Location > </ manualphonedetails > </ manualconfphone >
```

The manually configured phone information is available on CER

## /syntheticphonelist/info

http

```
GET http://{CER-IP}/cerappservices/export/syntheticphonelist/info
```

Retrieves the synthetic phone information detail available on CER.

Response examples

Information not available on CER

xml

```
< syntheticphonelist > < status > No information to extract from CER </ status > </ syntheticphonelist >
```

No synthetic phone information is available on CER

Information not available on Subscriber

xml

```
< syntheticphonelist > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ syntheticphonelist >
```

The synthetic phone information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< syntheticphonelist > < status > Extracting Info </ status > < phonelist > < MACAddress > 00059a3b7700 </ MACAddress > < ERLName > test2 </ ERLName > </ phonelist > ... </ syntheticphonelist >
```

The synthetic configured phone information is available on CER

## /nontrackedphones/info

http

```
GET http://{CER-IP}/cerappservices/export/nontrackedphones/info
```

Retrieves the Non-tracked phone information detail available on CER.

Response examples

Information not available on CER

xml

```
< NonTrackedPhones > < status > No information to extract from CER </ status > </ NonTrackedPhones >
```

Non-tracked phones information are not available on CER

Information not available on Subscriber

xml

```
< NonTrackedPhones > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ NonTrackedPhones >
```

The Non-tracked phones information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< NonTrackedPhones > < status > Extracting the nontracked phone information </ status > < NonTrackedPhoneDetails > < IPaddress > 10.76.224.252 </ IPaddress > < Extension > 1002 </ Extension > < Type > Cisco IP Communication </ Type > < Devicename > SEP8C164523EA87 </ Devicename > < Macaddress > 74-e5-f9-e0-51-cd </ Macaddress > </ NonTrackedPhoneDetails > </ NonTrackedPhones >
```

The Non-tracked phones detail information is available on CER

## /trackedphones/info

http

```
GET http://{CER-IP}/cerappservices/export/trackedphones/info
```

Retrieves the Tracked phone information detail available on CER.

Response examples

Information not available on CER

xml

```
< TrackedPhones > < status > No information to extract from CER </ status > </ TrackedPhones >
```

Tracked phones information are not available on CER

Information not available on Subscriber

xml

```
< TrackedPhones > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ TrackedPhones >
```

The Tracked phones information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< TrackedPhones > < status > Extracting the tracked phone information </ status > < TrackedPhonesDetails > < IPaddress > 10.76.224.152 </ IPaddress > < Extension > 1003 </ Extension > < Type > Cisco IP Communication </ Type > < Devicename > SEP8C164523EA89 </ Devicename > < Macaddress > 74-e5-f9-75-51-cd </ Macaddress > </ TrackedPhonesDetails > </ TrackedPhones >
```

The Tracked phones detail information is available on CER

## /snmpv2switch/info

Code Snippet

```
GET http://{CER-IP}/cerappservices/export/snmpv2switch/info
```

Retrieves the SNMPv2 settings information detail configured on CER.

Response examples

Information not available on CER

xml

```
< SnmpV2Settings > < status > No information to extract from CER </ status > </ SnmpV2Settings >
```

SNMPv2 settings are not configured on CER.

Information not available on Subscriber

xml

```
< SnmpV2Settings > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ SnmpV2Settings >
```

The SNMPv2 settings information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from the Subscriber

Information successfully retrieved

xml

```
< SnmpV2Settings > < status > Exporting info </ status > < SNMPV2Switch > < IPAddress > 10.77.34.110 </ IPAddress > < Timeout > 20 </ Timeout > < MaximumRetryAttempts > 2 </ MaximumRetryAttempts > < ReadCommunity > public </ ReadCommunity > </ SNMPV2Switch > < SNMPV2Switch > < IPAddress > 10.77.34.120 </ IPAddress > < Timeout > 30 </ Timeout > < MaximumRetryAttempts > 3 </ MaximumRetryAttempts > < ReadCommunity > sandeep </ ReadCommunity > </ SNMPV2Switch > </ SnmpV2Settings >
```

The SNMPv2 settings information is available on CER

## /snmpv3list/info

Code Snippet

```
GET http://{CER-IP}/cerappservices/export/snmpv3list/info
```

Retrieves the SNMPv3 settings information detail configured on CER.

Response examples

Information not available on CER

xml

```
< snmpv3settings > < status > No information to extract from CER </ status > </ snmpv3settings >
```

SNMPv3 settings are not configured on CER

Information not available on Subscriber

xml

```
< snmpv3settings > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ snmpv3settings >
```

The SNMPv3 settings information request is to the Subscriber, but the Publisher is active and the information cannot be retrieved from the Subscriber

Information successfully retrieved

xml

```
< snmpv3settings > < status > Exporting Info </ status > < details > < IPAddress > 10.77.34.110 </ IPAddress > < UserName > test </ UserName > < AuthProtocol > MD5 </ AuthProtocol > < PrivProtocol > AES128 </ PrivProtocol > < Timeout > 20 </ Timeout > < RetryAttempts > 2 </ RetryAttempts > </ details > </ snmpv3settings >
```

The SNMPv3 settings information is available on CER

## /lanswitch/info

http

```
GET http://{CER-IP}/cerappservices/export/lanswitch/info
```

The LAN Switch Information API retrieves the LAN switch information detail available on CER.

Response examples

Information not available on CER

xml

```
< LanSwitches > < status > No information to extract from CER </ status > </ LanSwitches >
```

LAN switch details are not configured on CER

Information not available on Subscriber

xml

```
< LanSwitches > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ LanSwitches >
```

The LAN switch detail information request is to the Subscriber, but the Publisher is active and the information cannot be retrieved from the Subscriber

Information successfully retrieved

xml

```
< LanSwitches > < status > Exporting info </ status > < LanSwitchDetail > < IPORHostName > 10.77.34.215 </ IPORHostName > < Notes > </ Notes > < AllowCAM > false </ AllowCAM > < PortDescAsLocation > false </ PortDescAsLocation > < UseSnmpV3 > false </ UseSnmpV3 > </ LanSwitchDetail > < LanSwitchDetail > < IPORHostName > 10.77.34.245 </ IPORHostName > < Notes > </ Notes > < AllowCAM > false </ AllowCAM > < PortDescAsLocation > false </ PortDescAsLocation > < UseSnmpV3 > false </ UseSnmpV3 > </ LanSwitchDetail > </ LanSwitches >
```

The LAN switch detail information is available on CER.

## /schedule/info

http

```
GET http://{CER-IP}/cerappservices/export/schedule/info
```

Retrieves the phone tracking schedule information detail available on CER.

Response examples

Information not available on Subscriber

xml

```
< schedule > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ schedule >
```

The phone tracking schedule detail information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< schedule > < status > Extracting Info </ status > < IncrementalPTInterval > 30 </ IncrementalPTInterval > < Time hour = " 03 " min = " 20 " > Sunday </ Time > < Time hour = " 03 " min = " 20 " > Monday </ Time > < Time hour = " 03 " min = " 20 " > Tuesday </ Time > < Time hour = " 03 " min = " 20 " > Wednesday </ Time > < Time hour = " 03 " min = " 20 " > Thursday </ Time > < Time hour = " 03 " min = " 20 " > Friday </ Time > < Time hour = " 03 " min = " 20 " > Saturday </ Time > < Time hour = " 02 " min = " 25 " > Sunday </ Time > < Time hour = " 02 " min = " 25 " > Wednesday </ Time > </ schedule >
```

The phone tracking schedule detail information is available on CER

## /callhistory/info

http

```
GET http://{CER-IP}/cerappservices/export/callhistory/info
```

Retrieves the call history information detail available on CER.

Response examples

Information not available on CER

xml

```
< callhistory > < status > No information to extract from CER </ status > </ callhistory >
```

Call history details are not configured on CER

Information not available on Subscriber

xml

```
< callhistory > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ callhistory >
```

The call history detail information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< callhistory > < status > Exporting Info </ status > < details > < ERLName > testSplChar </ ERLName > < CallerExtension > 1007 </ CallerExtension > < CallTime > 4:23:01 PM IST </ CallTime > < RPELINMap > 10911.--6011230194 </ RPELINMap > < IsCallAcknowledged > false </ IsCallAcknowledged > < CallAcknowledgeTime /> < CallAcknowledgeDate /> </ details > </ callhistory >
```

The call history detail information is available on CER

## /cucmcluster/list

http

```
GET http://{CER-IP}/cerappservices/export/cucmcluster/list
```

Retrieves the Cisco Unified Communications Manager clusters detail available on CER.

Response examples

Information not available on Subscriber

xml

```
< CucmClusterList > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ CucmClusterList >
```

The Cisco Unified Communications Manager clusters information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< CucmClusterList > < status > Exporting info </ status > < CucmConfig > < CUCM > 10.77.34.222 </ CUCM > < CTIManger > 10.77.34.222 </ CTIManger > < CTIUser > certest </ CTIUser > < BackupCTIMngr1 > 10.77.34.220 </ BackupCTIMngr1 > < BackupCTIMngr2 > 10.77.34.221 </ BackupCTIMngr2 > < TelePortAddr > 7001 </ TelePortAddr > < NumbrOfTelePorts > 3 </ NumbrOfTelePorts > < SecureConnection > < EnableSecureConn > true </ EnableSecureConn > < TFTPIpAddr > 10.77.34.224 </ TFTPIpAddr > < TFTPPort > 69 </ TFTPPort > < BackupTFTPIp > 10.77.34.225 </ BackupTFTPIp > < CAPFIpAddr > 10.77.34.233 </ CAPFIpAddr > < CAPFPort > 3804 </ CAPFPort > < InstanceIdPub > 10.77.34.230 </ InstanceIdPub > < AuthStringPub > test </ AuthStringPub > < InstanceIdSub > </ InstanceIdSub > < AuthStringSub > </ AuthStringSub > </ SecureConnection > < AXLSettings > < AXLUser > test </ AXLUser > < AXLPort > 8443 </ AXLPort > </ AXLSettings > < UseSnmpV3 > true </ UseSnmpV3 > </ CucmConfig > </ CucmClusterList >
```

The Cisco Unified Communications Manager clusters information is available on CER

## /onsitealert/info

http

```
GET http://{CER-IP}/cerappservices/export/onsitealert/info
```

Retrieves the onsite alert information detail available on CER.

Response examples

Information not available on CER

xml

```
< onsitealert > < status > No information to extract from CER </ status > </ onsitealert >
```

Onsite alert details are not configured on CER.

Information not available on Subscriber

xml

```
< onsitealert > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ onsitealert >
```

The onsite alert detail information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< onsitealert > < status > Extracting Info </ status > < details > < OnsiteAlertID > AL1 </ OnsiteAlertID > < OnsiteAlertName > alert1 </ OnsiteAlertName > < OnsiteAlertNum > 1001 </ OnsiteAlertNum > < OnsiteAlertEmail > al1@test.com </ OnsiteAlertEmail > < OnsiteAlertPager > </ OnsiteAlertPager > < UserGroup > CER User </ UserGroup > </ details > < details > < OnsiteAlertID > AL2 </ OnsiteAlertID > < OnsiteAlertName > Alert2 </ OnsiteAlertName > < OnsiteAlertNum > 1000 </ OnsiteAlertNum > < OnsiteAlertEmail > alert@cisco.com </ OnsiteAlertEmail > < OnsiteAlertPager > </ OnsiteAlertPager > < UserGroup > CER User </ UserGroup > </ details > </ onsitealert >
```

The onsite alert detail information is available on CER

## /pageralert/info

http

```
GET http://{CER-IP}/cerappservices/export/pageralert/info
```

Retrieves the pager alert settings information detail available on CER.

Response examples

Code Snippet

```
Pager alert details are not configured on CER.
```

Information not available on Subscriber

xml

```
< PagerAlertSettings > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ PagerAlertSettings >
```

The Pager alert detail information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< PagerAlertSettings > < status > Extracting Info </ status > < Extension > Extension </ Extension > < Erl > Zone/ERL </ Erl > < Location > Location </ Location > < SystemTime > System Time of Call </ SystemTime > < Server > Server </ Server > < LocalTime > Local Call Time </ LocalTime > </ PagerAlertSettings >
```

The pager alert detail information is available on CER

## /conventionalerl/info

http

```
GET http://{CER-IP}/cerappservices/export/conventionalerl/info
```

Retrieves the conventional ERL information detail available on CER.

Response examples

Information not available on CER

xml

```
< ConventionalERL > < status > No information to extract from CER </ status > </ ConventionalERL >
```

Conventional ERL details are not configured on CER

Information not available on Subscriber

xml

```
< ConventionalERL > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ ConventionalERL >
```

The conventional ERL detail information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< ConventionalERL > < status > Exporting Info </ status > < ERLDetails > < ERLName > Default </ ERLName > < ERLNotes > </ ERLNotes > < TestERL > false </ TestERL > < ELINSettings > 111111--123456789 </ ELINSettings > < OnsiteSettings > </ OnsiteSettings > < ALIInfo > < HouseNumber > 4243 </ HouseNumber > < HouseNumberSuffix > </ HouseNumberSuffix > < StreetName > bangalore </ StreetName > < PrefixDirectional > </ PrefixDirectional > < StreetSuffix > </ StreetSuffix > < PostDirectional > </ PostDirectional > < CommunityName > bangalore </ CommunityName > < State > ka </ State > < MainNPA > </ MainNPA > < CustomerName > cisco </ CustomerName > < COS > 5 </ COS > < TOS > 4 </ TOS > < Exchange > </ Exchange > < MainTelNum > </ MainTelNum > < OrderNumber > </ OrderNumber > < CountyID > </ CountyID > < CompanyID > cisco </ CompanyID > < ZipCode > </ ZipCode > < ZipCodeExt > </ ZipCodeExt > < CustomerCode > 666 </ CustomerCode > < Comments > </ Comments > < Longitude > </ Longitude > < Latitude > </ Latitude > < Elevation > </ Elevation > < TARCode > </ TARCode > < Location > </ Location > < ProvReserved > </ ProvReserved > < ERLType > Conventional ERL </ ERLType > </ ALIInfo > </ ERLDetails > ... </ ConventionalERL >
```

The conventional ERL detail information is available on CER

## /telephonysetting/info

http

```
GET http://{CER-IP}/cerappservices/export/telephonysetting/info
```

Retrieves the telephony settings information detail available on CER.

Response examples

Information not available on CER

xml

```
< TelephonySettings > < status > No information to extract from CER </ status > </ TelephonySettings >
```

Telephony settings details are not configured on CER.

Information not available on Subscriber

xml

```
< TelephonySettings > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ TelephonySettings >
```

The telephony settings detail information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from the Subscriber

Information successfully retrieved

xml

```
< TelephonySettings > < status > Exporting Info </ status > < settings > < PrimaryRoutePoint > 911 </ PrimaryRoutePoint > < BackupRoutePoint > 912 </ BackupRoutePoint > < CallBackRoutePoint > 913XXXXXXXXXX </ CallBackRoutePoint > < ELINStringDigPattern > 913 </ ELINStringDigPattern > < UDPPort > 32000 </ UDPPort > < InterCiscoERGrpRP > 5684365643 </ InterCiscoERGrpRP > < IPTypeOfService > b8 </ IPTypeOfService > < OnsiteAlertPromptRptCnt > 2 </ OnsiteAlertPromptRptCnt > < IntradoRoutePattern > 64738465464 </ IntradoRoutePattern > < UseIPAddrCallSig > false </ UseIPAddrCallSig > </ settings > </ TelephonySettings >
```

The telephony settings detail information is available on CER.

## /cerclustergroup/list

http

```
GET http://{CER-IP}/cerappservices/export/cerclustergroup/list
```

Retrieves the CER cluster details available on CER.

Response examples

Information not available on Subscriber

xml

```
< CiscoERGroups > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ CiscoERGroups >
```

The CER cluster detail information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from the Subscriber

Information successfully retrieved

xml

```
< CiscoERGroups > < CiscoERGroupDetails > < InterServerGrouprp > </ InterServerGrouprp > < PrimaryCER > 10.77.34.195 </ PrimaryCER > < ServerGroupName > CERServerGroup </ ServerGroupName > < ServerGroupID > fc02b306-126b-47ae-b7af-3dab521f9ac5 </ ServerGroupID > < StandbyCER > </ StandbyCER > < Version > 14.0.0.98000(39) </ Version > </ CiscoERGroupDetails > </ CiscoERGroups >
```

The CER cluster detail information is available on CER

## /cergroupsettings/info

http

```
GET http://{CER-IP}/cerappservices/export/cergroupsettings/info
```

Retrieves the CER group settings detail available on CER.

Response examples

Information not available on Subscriber

xml

```
< CERGroupSettings > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ CERGroupSettings >
```

The CER group settings detail information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from Subscriber

Information successfully retrieved

xml

```
< CERGroupSettings > < status > Exporting info </ status > < CERServerGroup > CERServerGroup </ CERServerGroup > < PeerTCPPort > 17001 </ PeerTCPPort > < HeartbeatCount > 3 </ HeartbeatCount > < HeartbeatInterval > 30 </ HeartbeatInterval > < ActiveCallTimeout > 180 </ ActiveCallTimeout > < SMTPMailServer > </ SMTPMailServer > < SourceMailID > </ SourceMailID > < SysLog > No </ SysLog > < DynTrackSwitchIPAddress > False </ DynTrackSwitchIPAddress > < SecurityWebLanguage > English(US) </ SecurityWebLanguage > < LimitConcurrentSession > disable </ LimitConcurrentSession > < MaxNoConcurrentSessions > 0 </ MaxNoConcurrentSessions > </ CERGroupSettings >
```

The CER group settings detail information is available on CER

## /serversetting/info

http

```
GET http://{CER-IP}/cerappservices/export/serversetting/info
```

Retrieves the CER Server settings detail available on CER.

Response examples

- Information succesfully retrieved on Standalone Publisher

xml

Code Snippet - 1

```
< ServerSettings > < status > Exporting Info </ status > < settings > < DebugPackageList > < CERAGGREGATOR > true </ CERAGGREGATOR > < CERCALLENGINE > true </ CERCALLENGINE > < CERCLUSTER > true </ CERCLUSTER > < CERDATABASE > true </ CERDATABASE > < CERGROUP > true </ CERGROUP > < CERONSITEALERT > true </ CERONSITEALERT > < CER-PHONETRACKINGENGINE > true </ CERPHONETRACKINGENGINE > < CERPROVIDER > true </ CERPROVIDER > < CERREMOTEUPDATE > true </ CERREMOTEUPDATE > < CERSYSADMIN > true </ CERSYSADMIN > < CERTELEPHONY > true </ CERTELEPHONY > </ DebugPackageList > < TracePackageList > < CERAGGREGATOR > true </ CERAGGREGATOR > < CERCALLENGINE > true </ CERCALLENGINE > < CERCLUSTER > true </ CERCLUSTER > < CERDATABASE > true </ CERDATABASE > < CERGROUP > true </ CERGROUP > < CERONSITEALERT > true </ CERONSITEALERT > < CERPHONETRACKINGENGINE > true </ CERPHONETRACKINGENGINE > < CERPROVIDER > true </ CERPROVIDER > < CERREMOTEUPDATE > true </ CERREMOTEUPDATE > < CERSYSADMIN > true </ CERSYSADMIN > < CERTELEPHONY > true </ CERTELEPHONY > </ TracePackageList > < ServerHostName > cer171 </ ServerHostName > < ServerName > Publisher </ ServerName > </ settings > </ ServerSettings > - Information not available on Subscriber

    ```xml < ServerSettings > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ ServerSettings > ```

    The Server settings detail information request is to the Subscriber, however the Publisher is active and the information cannot be retrieved from Subscriber

- Information successfully retrieved

    ```xml < ServerSettings > < status > Exporting Info </ status > < settings > < DebugPackageList > < CERAGGREGATOR > true </ CERAGGREGATOR > < CERCALLENGINE > true </ CERCALLENGINE > < CERCLUSTER > true </ CERCLUSTER > < CERDATABASE > true </ CERDATABASE > < CERGROUP > true </ CERGROUP > < CERONSITEALERT > true </ CERONSITEALERT > < CER-PHONETRACKINGENGINE > true </ CERPHONETRACKINGENGINE > < CERPROVIDER > true </ CERPROVIDER > < CERREMOTEUPDATE > true </ CERREMOTEUPDATE > < CERSYSADMIN > true </ CERSYSADMIN > < CERTELEPHONY > true </ CERTELEPHONY > </ DebugPackageList > < TracePackageList > < CERAGGREGATOR > true </ CERAGGREGATOR > < CERCALLENGINE > true </ CERCALLENGINE > < CERCLUSTER > true </ CERCLUSTER > < CERDATABASE > true </ CERDATABASE > < CERGROUP > true </ CERGROUP > < CERONSITEALERT > true </ CERONSITEALERT > < CERPHONETRACKINGENGINE > true </ CERPHONETRACKINGENGINE > < CERPROVIDER > true </ CERPROVIDER > < CERREMOTEUPDATE > true </ CERREMOTEUPDATE > < CERSYSADMIN > true </ CERSYSADMIN > < CERTELEPHONY > true </ CERTELEPHONY > </ TracePackageList > < ServerHostName > cer171 </ ServerHostName > < ServerName > Publisher </ ServerName > </ settings > < settings > < DebugPackageList > < CERAGGREGATOR > true </ CERAGGREGATOR > < CERCALLENGINE > true </ CERCALLENGINE > < CERCLUSTER > true </ CERCLUSTER > < CERDATABASE > true </ CERDATABASE > < CERGROUP > true </ CERGROUP > < CERONSITEALERT > true </ CERONSITEALERT > < CERPHONETRACKINGENGINE > true </ CERPHONETRACKINGENGINE > < CERPROVIDER > true </ CERPROVIDER > < CERREMOTEUPDATE > true </ CERREMOTEUPDATE > < CERSYSADMIN > true </ CERSYSADMIN > < CERTELEPHONY > true </ CERTELEPHONY > </ DebugPackageList > < TracePackageList > < CERAGGREGATOR > true </ CERAGGREGATOR > < CERCALLENGINE > true </ CERCALLENGINE > < CERCLUSTER > true </ CERCLUSTER > < CERDATABASE > true </ CERDATABASE > < CERGROUP > true </ CERGROUP > < CERONSITEALERT > true </ CERONSITEALERT > < CERPHONETRACKINGENGINE > true </ CERPHONETRACKINGENGINE > < CERPROVIDER > true </ CERPROVIDER > < CERREMOTEUPDATE > true </ CERREMOTEUPDATE > < CERSYSADMIN > true </ CERSYSADMIN > < CERTELEPHONY > true </ CERTELEPHONY > </ TracePackageList > < ServerHostName > cer172 </ ServerHostName > < ServerName > Subscriber </ ServerName > </ settings > </ ServerSettings >
```

```
The Server settings detail information is available on CER
```

## /e911licensemanager/info

http

```
GET http://{CER-IP}/cerappservices/export/e911licensemanager/info
```

The License Manager API retrieves the license manager details available on CER.

Response examples

Information not available on Subscriber

xml

```
< E911LicenseManager > < status > Publisher is active. Cannot fetch information from subscriber. </ status > </ E911LicenseManager >
```

The license manager detail information request is on Subscriber, but the Publisher is active and the information cannot be retrieved from Subscriber.

Information successfully retrieved

xml

```
< E911LicenseManager > < Status > Exporting the info </ Status > < NoPhonesDiscovered > 0 </ NoPhonesDiscovered > < NoPhonesManuallyConfigured > 2 </ NoPhonesManuallyConfigured > < TotalUsersTracked > 2 </ TotalUsersTracked > < PrimeLicenseManager > < ServerHostname > cer539.cisco.com </ ServerHostname > < LastComplianceTime > 2014-09-01 13:10:05 </ LastComplianceTime > < ConnectivityStatus > Connected </ ConnectivityStatus > </ PrimeLicenseManager > </ E911LicenseManager >
```

The license manager detail information is available on CER