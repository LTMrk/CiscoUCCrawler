---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-applications-220225-troubleshoot-jabber-c1829d4876
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-applications/220225-troubleshoot-jabber-log-in-problems-n.html
retrieved_at: 2026-08-21T12:49:05.140514+00:00
---

Troubleshoot Jabber Log in Problems -  Non MRA

# Troubleshoot Jabber Log in Problems -  Non MRA

### Download Options

Updated: March 1, 2023

Document ID: 220225

Contents

## Contents

## Introduction

This document describes the required corrective action when the Jabber login fails at the IM and Presence Login stages.

Refer for

## STAGE 1 : Login (IM and Presence Login ) UI Error : Your username or password is not correct Error code : "LERR_CUP_AUTH"

Usually this error is caused due to user Authentication failure

Steps to Resolve ============= 1. Check if user is assigned to a Presence Node and there are no duplicates for the user ( check system troubleshooter) 2. Make sure the credentials are valid a. In case of LDAP user , verify if user is able to login to ccmenduser page b. If ccmenduser page login fails , check the LDAP Authentication settings in CUCM and also verify the same settings are replicated to IMP

run sql select * from ldapauthentication run sql select * from ldapauthenticationhost c. Check if the account is not locked in LDAP 3. Check if the server has a high TOMCAT CPU comsumption

show process load

utils diagnose test

4. Collect the logs for these services in DEBUG Mode Client Profile Agent Cisco Tomcat UI Error : Cannot communicate with the server Jabber Error code : "LERR_CUP_UNREACHABLE" , "LERR_CUP_TIMEOUT"

Usually this error is caused due to Issues with IMDB or TCP connectivity to IMP. Steps to Resolve ============= 1. Check if IMP FQDN/Hostnames are resolvable There is a known issue on the Android OS where the OS cannot resolve hostname only addresses.

IP Addresses and FQDNs can be accessed, but hostnames only cannot.

Also, this problem would only be present for the Android devices, MAC, iOS,  andWindows devices would not be effected by this problem. Check under CUCM administration > System > Presence Redundancy Groups > DefaultCUPSubcluster (This name could have been changed)  if Servers are defined with Hostname ,

if yes workaround for this would be to change the server names to either FQDN or IP Address in the Cluster Topology page. 2. Verify that firewall/VPN does not block the connectivity to IMP server ( Port 8443,5222) 3.  Check if user is assigned to a Presence Node and there are no duplicates for the user ( check system troubleshooter) 4.  If this error is also seen , check what is the Minimum version set in IMP and compare it with Jabber version . [CLoginCup::OnLoginFailed] - @LoginMgr: #0, CLoginCup::OnLoginFailed err-code: -1, err-string: The client does not meet the minimal version requirement. request-token:0 Configuration in IMP https://<IMP>/cupadmin/soapClientTypeEdit.do?key=a80b3d69-4541-454a-8d6e-62f3986a5bc2

3. Verify if these services run in IMP server

Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service 4. Check High Availability Replication  status

a.utils dbreplication runtimestate b.run pe sql ttlogin select count(*) from typesysreplication

or

utils imdb_replication status ( 10.5.2 SU2a and higher) 5. Collect the logs for these services if the problem is not resolved.

Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service Client Profile Agent TIP: If the problem persists for only one user , you can try to unassign and re-assign the user for presence in CUCM . If its a systemwide problem , collect the logs or check the services status UI Error : Cannot communicate with the server Jabber Error code : "LERR_CUP_INTERNAL_ERROR"

Usually this error is caused due to Issues with IMDB , Check "Presence Datastore Login" logs first. Steps to Resolve ================= 1. Verify if these services run in IMP server Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service Cisco Presence Login Datastore 4. Check High Availability Replication  status a.utils dbreplication runtimestate b.run pe sql ttlogin select count(*) from typesysreplication

or

utils imdb_replication status ( 10.5.2 SU2a and higher)

5. Collect the logs for these services if the problem is not resolved. Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service Client Profile Agent Cisco Presence Login Datastore TIP: If the problem persists for only one user , you can try to unassign and re-assign the user for presence in CUCM . If its a systemwide problem , collect the logs or check the services status

STAGE 2 : XMPP Login (IM and Presence Login ) UI Error : Cannot communicate with the server Jabber Error code : "LERR_JABBER_AUTH <17>: Authentication error with server, for example, resource bind, TLS, create session or SASL error" Steps to Resolve ================= 1. Check if user is assigned to a Presence Node and there are no duplicates for the user ( check system troubleshooter)

2. If High Availability is enabled ,Go to CUCM Administration->Server-> Presence Redundancy Group and check if they are in Normal state

3. Check High Availability Replication  status

a.utils dbreplication runtimestate b.run pe sql ttlogin select count(*) from typesysreplication

or

utils imdb_replication status (10.5.2 SU2a and higher)

4. Check if the cup-xmpp Certificates are valid.

5. Check if the Port 5222 is open.

6. Reboot the server.

7. Collect the logs for these services before step 6 if Root cause to be identified as Reboot of the server is the only fix known so far.

Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service Client Profile Agent UI Error : Cannot communicate with the server Jabber Error code : "LERR_JABBER_UNREACHABLE <16>" , "LERR_CUP_UNREACHABLE <9>" Steps to Resolve ================= 1. Check if IMP FQDN/Hostnames are resolvable There is a known issue on the Android OS where the OS cannot resolve hostname only addresses.  IP Addresses and FQDNs can be accessed, but hostnames only cannot.  Also, this problem would only be present for the Android devices, MAC, iOS,  andWindows devices would not be effected by this problem. Check under CUCM administration > System > Presence Redundancy Groups > DefaultCUPSubcluster (This name could have been changed) if Servers are defined with Hostname, if yes workaround for this would be to change the server names to either FQDN or IP Address in the Cluster Topology page.

2. Verify that firewall/VPN does not block the connectivity to IMP server ( Port 8443,5222)

3. Verify if these services run in IMP server

Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service

4. Check High Availability Replication  status

a.utils dbreplication runtimestate b.run pe sql ttlogin select count(*) from typesysreplication

or

utils imdb_replication status ( 10.5.2 SU2a and higher)

5. Collect the logs for these services if the problem is not resolved.

Cisco XCP Router Cisco XCP connection Manager Cisco XCP Authentication Service Client Profile Agent

6. In case of all users experience the same error, a server Reboot can be done for quick recovery.

Logs to Collect

How to Set logs to DEBUG

Collect Logs from RTMT

General Checks

utils diagnose test

utils service list

utils dbreplication runtimestate

utils status ha

### Revision History

1.0

10-Apr-2023

Initial Release

### Contributed by Cisco Engineers

AM Mahesh Babu

### Customers Also Viewed

- Configure Hybrid Calendar Service With Microsoft Exchange for WebEx

- Configure Webex Connect Email Asset with Open Authorization

### This Document Applies to These Products

- Webex Cloud-Connected UC

| RTMT | Admin CLI |
|---|---|
| Cisco Client Profile Agent | file get activelog tomcat/logs/epassoap/log4j/* |
| Cisco Login Datastore | file get activelog epas/trace/imdb/sdi/ttlogin/ |
| Cisco Tomcat Security Logs | file get activelog tomcat/logs/security/log4j/* |
| Cisco XCP Authentication Service | file get activelog epas/trace/xcp/log/auth* |
| Cisco XCP Connection Manager | file get activelog epas/trace/xcp/log/client-cm-1_*.log |
| Cisco XCP Router | file get activelog epas/trace/xcp/log/rtr-jsm-1 |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Apr-2023 | Initial Release |