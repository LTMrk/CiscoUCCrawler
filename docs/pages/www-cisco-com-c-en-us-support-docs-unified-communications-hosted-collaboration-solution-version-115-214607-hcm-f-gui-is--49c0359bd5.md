---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-version-115-214607-hcm-f-gui-is--49c0359bd5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-version-115/214607-hcm-f-gui-is-unavailable-post-upgrade.html
retrieved_at: 2026-09-01T14:58:47.576846+00:00
---

HCM-F services in STOPPED state after appliance upgrade

# HCM-F services in STOPPED state after appliance upgrade

### Download Options

Updated: July 5, 2019

Document ID: 214607

Contents

## Contents

## Introduction

This document describes a problem that transpired after upgrading Hosted Collaboration Mediation Fulfillment (HCM-F) along with the troubleshooting process.

The root cause of the issue is related to an expired Tomcat Certificate. Many customers who are planning to upgrade their HCM-F appliance (to benefit from the newly introduced features) will face this issue if their existing HCM-F Tomcat Certificate has expired, and was not regenerated.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Hosted Collaboration Solution (HCS)

- Cisco Hosted Collaboration Mediation Fulfillment (HCM-F)

### Components Used

The information in this document is based on these software and hardware versions:

- HCM-F 11.5.4

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

After Upgrading HCM-F (11.5.1 to 11.5.4) and switch version, the Graphical User Interface (GUI) page is no longer reachable and services are in stopped state.

## Troubleshooting Performed

- While checking services status, it is observed that Web User Interface (UI) and Tomcat related services are in STOPPED state:

```
admin: utils service list Requesting service status, please wait... System SSH [STARTED] Name Service Cache [STOPPED] Service Not Activated Entropy Monitoring Daemon [STARTED] Cisco SCSI Watchdog [STARTED]Service Manager [STARTED] Service Manager is running Getting list of all services >> Return code = 0 Cisco AMC Service[STARTED] Cisco Audit Event Service[STARTED] Cisco CDM Database[STARTED] Cisco CDP[STARTED] Cisco CDP Agent[STARTED] Cisco Certificate Expiry Monitor[STARTED] Cisco Configuration Manager[STARTED] Cisco DRF Local[STARTED] Cisco DRF Master[STARTED] Cisco HCS Admin UI[ STOPPED ] Component is not running Cisco HCS CSF UI Service[ STOPPED ]  Component is not running Cisco HCS CUCDMSync Service[STARTED] Cisco HCS ConfigMgr[STARTED] Cisco HCS DMA-SA Service[STARTED] Cisco HCS Data Access Manager Service[STARTED] Cisco HCS Fulfillment Service[STARTED] Cisco HCS IPA Service[STARTED] Cisco HCS Intelligent Loader Service[ STOPPED ]  Component is not running Cisco HCS License Manager Service[STARTED] Cisco HCS NBI REST FF Web Service[ STOPPED ] Component is not running Cisco HCS NBI REST SDR Web Service[ STOPPED ]  Component is not running Cisco HCS NBI REST UCMon Web Service[ STOPPED ]  Component is not running Cisco HCS North Bound Interface Web Service[ STOPPED ]  Component is not running Cisco HCS Provisioning Adapter Service[STARTED] Cisco HCS SDR Change Notification Service[STARTED] Cisco HCS SDR UI[ STOPPED ]  Component is not running Cisco HCS SI UI[ STOPPED ]  Component is not running Cisco HCS SSO SP Service[ STOPPED ]  Component is not running Cisco HCS Service Inventory[ STOPPED ]  Component is not running Cisco HCS UCPA Service[STARTED] Cisco HCS UCSMSync Service[STARTED] Cisco HCS VCenterSync Service[STARTED] Cisco JMS Broker[STARTED] Cisco Log Partition Monitoring Tool[STARTED] Cisco Platform Manager Service[ STOPPED ]  Component is not running Cisco RIS Data Collector[STARTED] Cisco RTMT Web Service[ STOPPED ]  Component is not running Cisco Syslog Agent[STARTED] Cisco Tomcat[STARTED] Cisco Tomcat Stats Servlet[ STOPPED ]  Component is not running Cisco Trace Collection Service[STARTED] Cisco Trace Collection Servlet[ STOPPED ]  Component is not running Host Resources Agent[STARTED] MIB2 Agent[STARTED] Platform Administrative Web Service[ STOPPED ]  Component is not running SNMP Master Agent[STARTED]System Application Agent[STARTED] Cisco HCS UC Monitor Service[STOPPED]  Service Not ActivatedPrimary Node =true
```

- In CiscoSyslog we see Hypertext Transfer Protocol (HTTP) 404 Error for different Web-related services:

```
admin:file view activelog /syslog/CiscoSyslog Jun 17 16:14:19 hcs862-hcm-f local7 2 : 6: hcs862-hcm-f.XXXXXXXX.net:
Jun 17 2019 14:14:19.781 UTC : %UC_SERVICEMANAGER-2-ServiceStartFailed: %[ServiceName=Cisco RTMT Web Service][ Reason=HTTP 404 Error ][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Failed to start service. Jun 17 16:14:19 hcs862-hcm-f local7 2 : 7: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:19.781 UTC : %UC_SERVICEMANAGER-2-ServiceFailed: %[ServiceName=Cisco RTMT Web Service][Reason=Service stopped abruptly][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service terminated. Jun 17 16:14:20 hcs862-hcm-f local7 2 : 8: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:20.791 UTC : %UC_SERVICEMANAGER-2-ServiceStartFailed : %[ServiceName=Cisco Trace Collection Servlet][Reason=HTTP 404 Error][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Failed to start service. Jun 17 16:14:20 hcs862-hcm-f local7 2 : 9: hcs862-hcm-f.XXXXXXXXtest.net: Jun 17 2019 14:14:20.791 UTC : %UC_SERVICEMANAGER-2-ServiceFailed : %[ServiceName=Cisco Trace Collection Servlet][Reason=Service stopped abruptly][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service terminated. Jun 17 16:14:21 hcs862-hcm-f local7 2 : 10: hcs862-hcm-f.XXXXXXXXtest.net: Jun 17 2019 14:14:21.796 UTC : %UC_SERVICEMANAGER-2-ServiceStartFailed : %[ServiceName=Cisco Tomcat Stats Servlet][Reason=HTTP 404 Error][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Failed to start service. Jun 17 16:14:21 hcs862-hcm-f local7 2 : 11: hcs862-hcm-f.XXXXXXXXtest.net: Jun 17 2019 14:14:21.796 UTC : %UC_SERVICEMANAGER-2-ServiceFailed : %[ServiceName=Cisco Tomcat Stats Servlet][Reason=Service stopped abruptly][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service terminated. Jun 17 16:14:22 hcs862-hcm-f local7 6 : 12: hcs862-hcm-f.XXXXXXXXtest.net: Jun 17 2019 14:14:22.800 UTC :  %UC_GENERIC-6-ServiceStarted: %[ServiceName=Cisco CDP][ProcessID=8426][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service started.
Jun 17 16:14:23 hcs862-hcm-f local7 2 : 13: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:23.804 UTC : %UC_SERVICEMANAGER-2-ServiceStartFailed : %[ServiceName=Cisco HCS Admin UI][ Reason=HTTP 404 Error ][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Failed to start service. Jun 17 16:14:23 hcs862-hcm-f local7 2 : 14: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:23.804 UTC : %UC_SERVICEMANAGER-2-ServiceFailed : %[ServiceName=Cisco HCS Admin UI][Reason=Service stopped abruptly][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service terminated. Jun 17 16:14:24 hcs862-hcm-f local7 2 : 15: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:24.808 UTC : %UC_SERVICEMANAGER-2-ServiceStartFailed : %[ServiceName=Cisco HCS SDR UI][ Reason=HTTP 404 Error ][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Failed to start service. Jun 17 16:14:24 hcs862-hcm-f local7 2 : 16: hcs862-hcm-f.XXXXXXXXtest.net: Jun 17 2019 14:14:24.808 UTC : %UC_SERVICEMANAGER-2-ServiceFailed : %[ServiceName=Cisco HCS SDR UI][Reason=Service stopped abruptly][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service terminated. Jun 17 16:14:25 hcs862-hcm-f local7 6 : 17: hcs862-hcm-f.XXXXXXXXtest.net: Jun 17 2019 14:14:25.812 UTC :  %UC_GENERIC-6-ServiceStarted: %[ServiceName=Cisco Certificate Expiry Monitor][ProcessID=8774][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service started.
Jun 17 16:14:25 hcs862-hcm-f local7 2 : 18: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:25.813 UTC : %UC_SERVICEMANAGER-2-ServiceStartFailed : %[ServiceName=Cisco HCS NBI REST SDR Web Service][Reason=HTTP 404 Error][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Failed to start service. Jun 17 16:14:25 hcs862-hcm-f local7 2 : 19: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 17 2019 14:14:25.813 UTC : %UC_SERVICEMANAGER-2-ServiceFailed : %[ServiceName=Cisco HCS NBI REST SDR Web Service][Reason=Service stopped abruptly][AppID=Cisco Service Manager][ClusterID=][NodeID=hcs862-hcm-f]: Service terminated.
```

- Tomcat in Catalina.out reports CCMTrustCerts context issue:

```
SEVERE: Context [/CCMTrustCerts] startup failed due to previous errors Jun 18, 2019 2:59:49 PM org.apache.catalina.startup.HostConfig deployDirectoryINFO: Deployment of web application directory /common/log/taos-log-a/tomcat/webapps/CCMTrustCerts has finished in 8,042 ms end of the file reachedoptions: q=quit, n=next, p=prev, b=begin, e=end (lines 1221 - 1223 of 1223) :INFO: Deploying web application directory /common/log/taos-log-a/tomcat/webapps/manager
Jun 18, 2019 2:59:33 PM org.apache.catalina.startup.SetContextPropertiesRule beginWARNING: [SetContextPropertiesRule]{Context} Setting property 'debug' to '0' did not find a matching property.
Jun 18, 2019 2:59:33 PM org.apache.tomcat.util.digester.SetPropertiesRule beginWARNING: [SetPropertiesRule]{Context/Realm} Setting property 'resourceName' to 'TomcatUsersDatabase' did not find a matching property.
Jun 18, 2019 2:59:41 PM org.apache.catalina.startup.TldConfig executeINFO: At least one JAR was scanned for TLDs yet contained no TLDs. Enable debug logging for this logger for a complete list of JARs that were scanned but no TLDs were found in them. Skipping unneeded JARs during scanning can improve startup time and JSP compilation time.
Jun 18, 2019 2:59:41 PM org.apache.catalina.core.StandardContext startInternalSEVERE: One or more Filters failed to start. Full details will be found in the appropriate container log file
Jun 18, 2019 2:59:41 PM org.apache.catalina.core.StandardContext startInternalSEVERE: Context [/manager] startup failed due to previous errors
Jun 18, 2019 2:59:41 PM org.apache.catalina.startup.HostConfig deployDirectoryINFO: Deployment of web application directory /common/log/taos-log-a/tomcat/webapps/manager has finished in 7,483 ms
Jun 18, 2019 2:59:41 PM org.apache.catalina.startup.HostConfig deployDirectoryINFO: Deploying web application directory /common/log/taos-log-a/tomcat/webapps/CCMTrustCerts
Jun 18, 2019 2:59:49 PM org.apache.catalina.startup.TldConfig executeINFO: At least one JAR was scanned for TLDs yet contained no TLDs. Enable debug logging for this logger for a complete list of JARs that were scanned but no TLDs were found in them. Skipping unneeded JARs during scanning can improve startup time and JSP compilation time.
Jun 18, 2019 2:59:49 PM org.apache.catalina.core.StandardContext startInternalSEVERE: One or more Filters failed to start. Full details will be found in the appropriate container log file Jun 18, 2019 2:59:49 PM org.apache.catalina.core.StandardContext startInternal options: SEVERE: Context [/CCMTrustCerts] startup failed due to previous errors Jun 18, 2019 2:59:49 PM org.apache.catalina.startup.HostConfig deployDirectoryINFO: Deployment of web application directory /common/log/taos-log-a/tomcat/webapps/CCMTrustCerts has finished in 8,042 ms
```

- Running “utils diagnose test” from Command-Line Interface (CLI) displays an error in tomcat_connectors module, indicating that internal connections to Tomcat are not working:

```
test - tomcat_connectors   : Failed - The HTTP and HTTPS ports are not responding to local requests. Please collect all of the Tomcat logs for root cause analysis: file get activelog tomcat/logs/*
```

- Tomcat certificate expired March 26th. Despite that, problems were not observed during (or prior to) upgrade of HCM-F:

```
Jun 19 12:00:00 hcs862-hcm-f local99 0 : 42: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 19 2019 10:00:00.19 UTC :  %UC_CERT-0-CertExpired: %[Message=Certificate expiration Notification. Certificate name:tomcat.der Unit:tomcat Type:own-cert Expiration:Sun Mar 26 12:30:59:000 CES][AppID=Cisco Certificate Monitor][ClusterID=][NodeID=hcs862-hcm-f]: Certificate has Expired and needs to be changed at the earliest Jun 19 12:00:00 hcs862-hcm-f local99 0 : 43: hcs862-hcm-f.XXXXXXXXtest.net:
Jun 19 2019 10:00:00.21 UTC :  %UC_CERT-0-CertExpired: %[Message=Certificate expiration Notification. Certificate name:ipsec.der Unit:ipsec Type:own-cert Expiration:Sun Mar 26 12:30:57:000 CEST ][AppID=Cisco Certificate Monitor][ClusterID=][NodeID=hcs862-hcm-f]: Certificate has Expired and needs to be changed at the earliest
```

## Solution

1. Regenerate Tomcat certificate :

```
admin: set cert regen tomcat WARNING: This operation will overwrite any CA signed certificate previously imported for  tomcat
Proceed with regeneration (yes|no)? yes Successfully Regenerated Certificate for tomcat.
You must restart services related to tomcat for the regenerated certificates to become active.
```

2.  Restart HCM-F server:

```
admin: utils system restart Do you really want to restart ?Enter (yes/no)? yes
```

## Verification

- Verify service status:

```
admin: utils service list Requesting service status, please wait... System SSH [STARTED] Name Service Cache [STOPPED] Service Not Activated Entropy Monitoring Daemon [STARTED] Cisco SCSI Watchdog [STARTED] Service Manager [STARTED]Service Manager is running Getting list of all services >> Return code = 0 Cisco AMC Service[STARTED] Cisco Audit Event Service[STARTED] Cisco CDM Database[STARTED] Cisco CDP[STARTED] Cisco CDP Agent[STARTED] Cisco Certificate Expiry Monitor[STARTED] Cisco Configuration Manager[STARTED] Cisco DRF Local[STARTED] Cisco DRF Master[STARTED] Cisco HCS Admin UI[STARTED] Cisco HCS CSF UI Service[STARTED] Cisco HCS CUCDMSync Service[STARTED] Cisco HCS ConfigMgr[STARTED] Cisco HCS DMA-SA Service[STARTED] Cisco HCS Data Access Manager Service[STARTED] Cisco HCS Fulfillment Service[STARTED] Cisco HCS IPA Service[STARTED] Cisco HCS Intelligent Loader Service[STARTED] Cisco HCS License Manager Service[STARTED] Cisco HCS NBI REST FF Web Service[STARTED] Cisco HCS NBI REST SDR Web Service[STARTED] Cisco HCS NBI REST UCMon Web Service[STARTED] Cisco HCS North Bound Interface Web Service[STARTED] Cisco HCS Provisioning Adapter Service[STARTED] Cisco HCS SDR Change Notification Service[STARTED] Cisco HCS SDR UI[STARTED] Cisco HCS SI UI[STARTED] Cisco HCS SSO SP Service[STARTED] Cisco HCS Service Inventory[STARTED] Cisco HCS UCPA Service[STARTED] Cisco HCS UCSMSync Service[STARTED] Cisco HCS VCenterSync Service[STARTED] Cisco JMS Broker[STARTED] Cisco Log Partition Monitoring Tool[STARTED] Cisco Platform Manager Service[STARTED] Cisco RIS Data Collector[STARTED] Cisco RTMT Web Service[STARTED] Cisco Syslog Agent[STARTED] Cisco Tomcat[STARTED] Cisco Tomcat Stats Servlet[STARTED] Cisco Trace Collection Service[STARTED] Cisco Trace Collection Servlet[STARTED] Host Resources Agent[STARTED]MIB2 Agent[STARTED] Platform Administrative Web Service[STARTED] SNMP Master Agent[STARTED] System Application Agent[STARTED] Cisco HCS UC Monitor Service[STOPPED] Service Not ActivatedPrimary Node =true
```

### Revision History

1.0

05-Jul-2019

Initial Release

### Contributed by Cisco Engineers

Kurt Van de Vel

Cisco CX

Andrea Cingolani

Cisco CX

Sebastian Danik

Cisco CX

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Jul-2019 | Initial Release |