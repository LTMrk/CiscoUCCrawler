---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-12-5-1-cucm-b-release-notes-cucm-imp-1251-cucm-b-release-note-319c896873
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_5_1/cucm_b_release-notes-cucm-imp-1251/cucm_b_release-notes-cucm-imp-1251_chapter_0101.html
retrieved_at: 2026-08-21T01:31:10.758289+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

Updated: January 22, 2019

Chapter: Caveats

## Chapter: Caveats

- Caveats

- Bug Search                              	 Tool

- Open Caveats

# Caveats

## Bug Search
                        	 Tool

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs

You can
                           		search for open and resolved caveats of any severity for any release using the Cisco Bug Search tool, an online tool
                           		  available for customers to query defects according to their own needs.

Internet
                                    			 connection

Web browser

Cisco.com user ID
                                    			 and password

Follow these
                           		steps to use Cisco Bug Search tool:

Access the Cisco Bug Search tool: https://tools.cisco.com/bugsearch/ .

Log in with your
                                 			 Cisco.com user ID and password.

If you are looking for information about a specific problem, enter the bug ID number in the Search for: field and click Go .

Click Help on the Bug Search page for information about
                                       		  how to search for bugs, create saved searches, and create bug groups.

## Open Caveats

The following table compiles open caveats in this release. You can search for defects in the Bug Search Tool at https://bst.cloudapps.cisco.com/bugsearch/ .

Caveats

Description

Unified Communications Manager

CSCvn02095

CUCM sends ACK on ephemeral port in response to 491

CSCvn17505

CUCM changes the contact header port in response to mid-call INVITE

CSCvn30046

EMCC SIP trunk calls fail when connecting to CUCM 12.x Cluster

CSCvn32181

Under extended traffic load, Memory corruption caused ccm process core dump

CSCvn36226

CVP sends 491 Request Pending to CUCM, user hangs up before a 5 second timer

CSCvn41358

SRTP being reset in bogus answer in early consult transfer scenario

CSCvn43882

SIPInterface does not process blank invite as it is stuck in waitForAnswerorOfferorMXCap state

CSCvn57934

Memory Throttling Virtual Memory parameter still set to 2.9 GB for CUCM 10.x and onwards

CSCvn77411

After RecordingGatewayRegistrationTimeout, SIPvBIB does not receive the IN_SERVICE notification

CSCvn78081

FAX calls are not working if the transfer is initiated from SIP endpoint

CSCvn79777

Call queuing destinations HuntPilot fail due to multiple QueueControl PIDs

CSCvn80227

Customer cannot insert Directory URI and patterns which contain reserved characters

CSCvn75533

Phones not able to recognize SIP INVITE Call-Info huntpiloturi parameter

CSCvn78228

Call Pickup feature doesn't work when invoked from dual mode phones

CSCvn85800

CUCM loses dtmf parameters from SDP when ANAT is used

CSCvn85549

Cause value of 1 when received by CUCM (Called side) from SRST GW results into SIPStationCdfc leak

CSCvn85077

SNR to SNR call fails with no way audio due to two MTP insertion

CSCvm95380

DST/TZ update with 2018g

CSCvn26492

Change in "set password user security " CLI message

CSCvn55141

Time elapsed details while doing upgrades

CSCvn73875

Upgrade failure when smart licensing status is evaluation expired/Auth expired/OOC with grace expiry

CSCvn78796

Cluster Upgrade: If UCM Pub fails then UCM Sub and IM&P Pub should not proceed with upgrade

CSCvn80652

CUCM Publisher set network hostname with IP address change doesn't propagate to Subscribers

CSCvn81764

Simplified Upgrade - Confusing message while cluster status displayed on CLI

CSCvn91735

Install of cleanup gets stuck in some conditions

CSCvn82784

RTMT shows AMC service down in publisher

CSCvm78768

CallManager MultiSan Certificate toggles to old one while uploading a new one

CSCvm70018

TFTP Services prematurely self restarts while uploading a MultiSAN CallManager Certificate

CSCvm86354

MultiSAN Certificate Upload returns false negative status or timeout due to delay in pushCertificate

CSCvn48876

CUCM replies 200 OK for HTTP request even Oauth Token Expired

CSCvn65166

SAML SSO login might fail at times, even after SSO enablement was successful post upgrade

CSCvn90535

getAuthHeader function validation check to mitigate CTI core

CSCvk22709

Speed dials in BAT Exported file using Export Phones Specific Details option are out of order

CSCvm93248

Unable to import CCD Requesting Service

CSCvn01402

Unable to add bulk intercom directory numbers

CSCvn40041

Find buttons are not functioning at Phone Template Configuration page

CSCvn51683

RTMT tracelog collection: fails to add RSA key of SFTP server to UC apps in NAT setup

CSCvn57671

LDAP sync locks out LDAP accounts

CSCvn20235

Cloud Onboarding fails while trying to onboard for the very first time

CSCvn49234

Value of tag routePartitionName, under line tag is not adding during addPhone axl api request

CSCvn51603

Multiple Analyzer -DNA fails with HTTP 500 error

CSCvn57645

ALL-LANG: Self Care: Strings on status bar show up in English with locale

CSCvn57656

ALL-LANG: ccmadmin: Corrupted characters in EMCC Intercluster Service Profile

CSCvn64792

Not able to insert IPV6 SipTrunk on 12.5.1.10000-15 using Axl

CSCvn72342

Phones are showing unknown in PCA when the device description has Arabic language

CSCvn79005

Missing ACG (Access control group) & roles under Permissions Information section

CSCvn85656

CUCM imported pattern with brackets is not shown properly in UI

CSCvj07705

Wireless Access Point Controller's get stuck in the "Pending" state in CUCM

CSCvn15735

Certificate Operation "Complete By" Validation triggers before field complete

CSCvn40028

Unable to update Intercom DNs at Intercom Directory number configuration page

CSCvn46045

RTMT to not display the pop up alert when JRE time zone version of client and server mis-match

CSCvn47595

Selfcare: Missing icon for 8832

CSCvm76719

CMUI login requires clearing j_security_check error few times before successful login

CSCvn26756

Call Flow Diagram in RTMT not showing the first Invite CCM 12.0

CSCvn01600

Call Park BLF Button added using AXL request addPhoneButtonTemplate is not proper on CUCM DB

IM and Presence Service

CSCvn49679

IM&P Publisher Sync Agent not operational after hostname change

CSCvn65321

XCP Router cores when <presence> packets contain certain special character(s)

CSCvh72114

ICSA periodic sync failure "The cursor has been previously released and is unavailable"

CSCvm40610

PushEnabledSessionsApns counter displays wrong value

CSCvn12220

XCP SIP CM should not block outgoing requests if call-leg is terminated before response is received

CSCvn36404

ICSA should sync R2Rconfig during ICSA sync even if xcpsecret value does not change

CSCvn40022

Cisco XCP Connection Manager service crashes when disco#info request to domain timeouts

CSCvn46096

IM&P PE Core Dump just after PEIDSQueryError

CSCvn62075

XCP Routers should invalidate any Edge information that they receive from other nodes

CSCvn68387

XCP Auth cores when the proxydomain has a NULL value

CSCvh63600

Delayed Update of Presence After Failover Due to High Load

CSCvn73687

Upgrade and Migration guide has incorrect data in "version switching" section

CSCvk44869

CAXL updateContact or addContact make roster subscription as both

CSCvh72096

Change Notification delays when disabling or enabling presence via CUCM BAT

CSCvk09795

Memory leak in jabberd in idle state

CSCvm63696

Cisco XCP Router service crash caused by empty tag in presence throttling mechanism

CSCvn05142

Disabling AD sync feature and change group member presence to Offline

CSCvn31799

TC service memory leak due to external DB full

CSCvn35499

Last Synchronized Time is not updating correctly

CSCvn47142

Jabberd core on 12.5 tt5

CSCvn50468

APNS cluster onboarded but IMP xcpconfigmgr failing to fetch token due to missing certs

CSCvc98070

IM&P node is not aware of Group Chat Alias of another node

CSCve61037

TC cannot be started after enabling PChat, database MSSQL, CC mode enabled

CSCvk22395

Status codes in presence stanzas from rooms not being delivered for quiet/silent sessions

CSCvn75705

Jabberd process core dump just after L2 system upgrade

CSCvn78563

Cisco Presence Engine crashes when connecting to Microsoft Exchange server via EWS

CSCvn90001

Reserve Port 37239 for ICSA

CSCvo01877

jabberd deadlock on startup results in eventual core

| Tip | Click Help on the Bug Search page for information about
                                       		  how to search for bugs, create saved searches, and create bug groups. |
|---|---|

| Caveats | Description |
|---|---|
| Unified Communications Manager |
| CSCvn02095 | CUCM sends ACK on ephemeral port in response to 491 |
| CSCvn17505 | CUCM changes the contact header port in response to mid-call INVITE |
| CSCvn30046 | EMCC SIP trunk calls fail when connecting to CUCM 12.x Cluster |
| CSCvn32181 | Under extended traffic load, Memory corruption caused ccm process core dump |
| CSCvn36226 | CVP sends 491 Request Pending to CUCM, user hangs up before a 5 second timer |
| CSCvn41358 | SRTP being reset in bogus answer in early consult transfer scenario |
| CSCvn43882 | SIPInterface does not process blank invite as it is stuck in waitForAnswerorOfferorMXCap state |
| CSCvn57934 | Memory Throttling Virtual Memory parameter still set to 2.9 GB for CUCM 10.x and onwards |
| CSCvn77411 | After RecordingGatewayRegistrationTimeout, SIPvBIB does not receive the IN_SERVICE notification |
| CSCvn78081 | FAX calls are not working if the transfer is initiated from SIP endpoint |
| CSCvn79777 | Call queuing destinations HuntPilot fail due to multiple QueueControl PIDs |
| CSCvn80227 | Customer cannot insert Directory URI and patterns which contain reserved characters |
| CSCvn75533 | Phones not able to recognize SIP INVITE Call-Info huntpiloturi parameter |
| CSCvn78228 | Call Pickup feature doesn't work when invoked from dual mode phones |
| CSCvn85800 | CUCM loses dtmf parameters from SDP when ANAT is used |
| CSCvn85549 | Cause value of 1 when received by CUCM (Called side) from SRST GW results into SIPStationCdfc leak |
| CSCvn85077 | SNR to SNR call fails with no way audio due to two MTP insertion |
| CSCvm95380 | DST/TZ update with 2018g |
| CSCvn26492 | Change in "set password user security " CLI message |
| CSCvn55141 | Time elapsed details while doing upgrades |
| CSCvn73875 | Upgrade failure when smart licensing status is evaluation expired/Auth expired/OOC with grace expiry |
| CSCvn78796 | Cluster Upgrade: If UCM Pub fails then UCM Sub and IM&P Pub should not proceed with upgrade |
| CSCvn80652 | CUCM Publisher set network hostname with IP address change doesn't propagate to Subscribers |
| CSCvn81764 | Simplified Upgrade - Confusing message while cluster status displayed on CLI |
| CSCvn91735 | Install of cleanup gets stuck in some conditions |
| CSCvn82784 | RTMT shows AMC service down in publisher |
| CSCvm78768 | CallManager MultiSan Certificate toggles to old one while uploading a new one |
| CSCvm70018 | TFTP Services prematurely self restarts while uploading a MultiSAN CallManager Certificate |
| CSCvm86354 | MultiSAN Certificate Upload returns false negative status or timeout due to delay in pushCertificate |
| CSCvn48876 | CUCM replies 200 OK for HTTP request even Oauth Token Expired |
| CSCvn65166 | SAML SSO login might fail at times, even after SSO enablement was successful post upgrade |
| CSCvn90535 | getAuthHeader function validation check to mitigate CTI core |
| CSCvk22709 | Speed dials in BAT Exported file using Export Phones Specific Details option are out of order |
| CSCvm93248 | Unable to import CCD Requesting Service |
| CSCvn01402 | Unable to add bulk intercom directory numbers |
| CSCvn40041 | Find buttons are not functioning at Phone Template Configuration page |
| CSCvn51683 | RTMT tracelog collection: fails to add RSA key of SFTP server to UC apps in NAT setup |
| CSCvn57671 | LDAP sync locks out LDAP accounts |
| CSCvn20235 | Cloud Onboarding fails while trying to onboard for the very first time |
| CSCvn49234 | Value of tag routePartitionName, under line tag is not adding during addPhone axl api request |
| CSCvn51603 | Multiple Analyzer -DNA fails with HTTP 500 error |
| CSCvn57645 | ALL-LANG: Self Care: Strings on status bar show up in English with locale |
| CSCvn57656 | ALL-LANG: ccmadmin: Corrupted characters in EMCC Intercluster Service Profile |
| CSCvn64792 | Not able to insert IPV6 SipTrunk on 12.5.1.10000-15 using Axl |
| CSCvn72342 | Phones are showing unknown in PCA when the device description has Arabic language |
| CSCvn79005 | Missing ACG (Access control group) & roles under Permissions Information section |
| CSCvn85656 | CUCM imported pattern with brackets is not shown properly in UI |
| CSCvj07705 | Wireless Access Point Controller's get stuck in the "Pending" state in CUCM |
| CSCvn15735 | Certificate Operation "Complete By" Validation triggers before field complete |
| CSCvn40028 | Unable to update Intercom DNs at Intercom Directory number configuration page |
| CSCvn46045 | RTMT to not display the pop up alert when JRE time zone version of client and server mis-match |
| CSCvn47595 | Selfcare: Missing icon for 8832 |
| CSCvm76719 | CMUI login requires clearing j_security_check error few times before successful login |
| CSCvn26756 | Call Flow Diagram in RTMT not showing the first Invite CCM 12.0 |
| CSCvn01600 | Call Park BLF Button added using AXL request addPhoneButtonTemplate is not proper on CUCM DB |
| IM and Presence Service |
| CSCvn49679 | IM&P Publisher Sync Agent not operational after hostname change |
| CSCvn65321 | XCP Router cores when <presence> packets contain certain special character(s) |
| CSCvh72114 | ICSA periodic sync failure "The cursor has been previously released and is unavailable" |
| CSCvm40610 | PushEnabledSessionsApns counter displays wrong value |
| CSCvn12220 | XCP SIP CM should not block outgoing requests if call-leg is terminated before response is received |
| CSCvn36404 | ICSA should sync R2Rconfig during ICSA sync even if xcpsecret value does not change |
| CSCvn40022 | Cisco XCP Connection Manager service crashes when disco#info request to domain timeouts |
| CSCvn46096 | IM&P PE Core Dump just after PEIDSQueryError |
| CSCvn62075 | XCP Routers should invalidate any Edge information that they receive from other nodes |
| CSCvn68387 | XCP Auth cores when the proxydomain has a NULL value |
| CSCvh63600 | Delayed Update of Presence After Failover Due to High Load |
| CSCvn73687 | Upgrade and Migration guide has incorrect data in "version switching" section |
| CSCvk44869 | CAXL updateContact or addContact make roster subscription as both |
| CSCvh72096 | Change Notification delays when disabling or enabling presence via CUCM BAT |
| CSCvk09795 | Memory leak in jabberd in idle state |
| CSCvm63696 | Cisco XCP Router service crash caused by empty tag in presence throttling mechanism |
| CSCvn05142 | Disabling AD sync feature and change group member presence to Offline |
| CSCvn31799 | TC service memory leak due to external DB full |
| CSCvn35499 | Last Synchronized Time is not updating correctly |
| CSCvn47142 | Jabberd core on 12.5 tt5 |
| CSCvn50468 | APNS cluster onboarded but IMP xcpconfigmgr failing to fetch token due to missing certs |
| CSCvc98070 | IM&P node is not aware of Group Chat Alias of another node |
| CSCve61037 | TC cannot be started after enabling PChat, database MSSQL, CC mode enabled |
| CSCvk22395 | Status codes in presence stanzas from rooms not being delivered for quiet/silent sessions |
| CSCvn75705 | Jabberd process core dump just after L2 system upgrade |
| CSCvn78563 | Cisco Presence Engine crashes when connecting to Microsoft Exchange server via EWS |
| CSCvn90001 | Reserve Port 37239 for ICSA |
| CSCvo01877 | jabberd deadlock on startup results in eventual core |