---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15-cucm-b-pcd-admin-guide-15-cucm-b-pcd-admin-guide-1401-chapt-790d623de0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15/cucm_b_pcd-admin-guide-15/cucm_b_pcd-admin-guide-1401_chapter_0101.html
retrieved_at: 2026-08-17T00:33:11.585881+00:00
---

Prime Collaboration Deployment Administration Guide, Release 15 and SUs

# Prime Collaboration Deployment Administration Guide, Release 15 and SUs

Updated: February 5, 2026

Chapter: Cisco Prime Collaboration Deployment Configuration and Administration

## Chapter: Cisco Prime Collaboration Deployment Configuration and Administration

- Cisco Prime Collaboration Deployment Configuration and Administration

- Services

- Limitations and Restrictions

# Cisco Prime Collaboration Deployment Configuration and Administration

## Services

After the
                              		  installation of the Cisco Prime Collaboration Deployment platform, most
                              		  services start automatically. You can configure services by setting service
                              		  parameters for each service. If necessary, for example, for troubleshooting
                              		  purposes, you may need to stop, start, or restart a service. You can
                              		  perform these tasks by using the CLI on the Cisco
                              		  Prime Collaboration Deployment platform.

### Cisco Prime
                              		  Collaboration Deployment Service

This service
                              		  supports the Cisco Prime Collaboration Deployment application interface. This
                              		  service must be active for the Cisco Prime Collaboration Deployment application
                              		  to work correctly. It is active by default.

### Performance
                              		  and Monitoring Services

The Cisco Log
                                    		  Partition Monitoring Tool service supports the Log Partition Monitoring
                                    		  feature, which monitors the disk usage of the log partition on the Cisco Prime
                                    		  Collaboration Deployment platform by using configured thresholds and a polling
                                    		  interval.

The Real-Time
                                    		  Information Server (RIS) maintains real-time information, such as critical
                                    		  alarms generated.

The Alert Manager and Collector (AMC) service allows you to retrieve real-time
                                    		  information that exists on the server.

The Cisco Audit
                                    		  Event Service monitors and logs any configuration change to the Cisco Prime
                                    		  Collaboration Deployment platform by a user or as a result of the user action.

The Cisco
                                    		  SOAP-Log Collection APIs service allows you to collect log files and to
                                    		  schedule collection of log files on a remote SFTP server. Examples of log files
                                    		  that you can collect include syslog, core dump files, Cisco application trace
                                    		  files.

The Cisco SOAP-Performance Monitoring APIs service allows you to use performance monitoring
                                    		  counters for various applications through SOAP APIs; for example, you can
                                    		  monitor memory information per service and CPU usage.

### Backup and
                              		  Restore Services

The Cisco Disaster Recovery Framework (DRF) Master Agent service supports the DRF Master Agent, which works with the CLI
                                    to
                                    		  schedule backups, perform restorations, view dependencies, check status of
                                    		  jobs, and cancel jobs, if necessary. The Cisco DRF Master Agent also provides
                                    		  the storage medium for the backup and restoration process.

The Cisco DRF
                                    		  Local service supports the Cisco DRF Local Agent, which performs the work for the DRF Master Agent. Components register
                                    with the Cisco DRF Local Agent to
                                    		  use the disaster recovery framework. The Cisco DRF Local Agent runs
                                    		  commands that it receives from the Cisco DRF Master Agent. Cisco DRF Local
                                    		  Agent sends the status, logs, and command results to the Cisco DRF Master
                                    		  Agent.

Cisco Prime
                                    		  Collaboration Deployment runs a Secure File Transfer Protocol (SFTP) server locally.

### System
                              		  Services

Cisco Delivery Protocol (CDP) advertises the voice application to other network management applications, so
                                    		  the network management application can perform network management tasks for the
                                    		  voice application.

The Cisco Trace
                                    		  Collection Servlet, along with the Cisco Trace Collection Service, supports
                                    		  trace collection and allows users to view traces. If you stop this service, you
                                    		  cannot collect or view traces on the Cisco Prime Collaboration Deployment
                                    		  platform.

For SysLog Viewer
                                    		  and trace and log collection, the Cisco Trace Collection Servlet and the Cisco
                                    		  Trace Collection Service must run on the server.

The Cisco Trace
                                    		  Collection Service, along with the Cisco Trace Collection Servlet, supports
                                    		  trace collection and allows users to view traces. If you stop this service, you
                                    		  cannot collect or view traces on the Cisco Prime Collaboration Deployment
                                    		  platform.

For SysLog Viewer
                                    		  and trace and log collection, the Cisco Trace Collection Servlet and the Cisco
                                    		  Trace Collection Service must run on the server.

Tip

### Platform
                              		  Services

The Cisco Tomcat
                                    		  service supports the web server.

The Cisco Tomcat
                                    		  Stats servlet collects the Tomcat statistics.

The Platform Administrative Web service is a SOAP API that can be activated on Cisco Unified Communications Manager, Cisco
                                    Unified Presence, IM and Presence Service, Cisco Unified Contact Center Express, Cisco Unity Connection, or Cisco Emergency Responder systems, to allow the Cisco Prime Collaboration Deployment server to upgrade the system.

This service,
                                    		  which acts as the agent protocol engine, provides authentication,
                                    		  authorization, access control, and privacy functions that relate to Simple Network Management Protocol (SNMP) requests.

Tip

The Management Information Base (MIB2) Agent service
                                    		  provides SNMP access to variables, which are defined in RFC 1213, that read and
                                    		  write variables; for example, system and interfaces.

This service
                                    		  provides SNMP access to host information, such as storage resources, process
                                    		  tables, and installed software base. This service implements the
                                    		  HOST-RESOURCES-MIB.

This service
                                    		  provides SNMP access to the applications that are installed and running on
                                    		  the system. This service implements the SYSAPPL-MIB.

This service uses
                                    		  the Cisco Discovery Protocol to provide SNMP access to network connectivity
                                    		  information on the Cisco Prime Collaboration Deployment platform. This service
                                    		  implements the CISCO-CDP-MIB.

This service
                                    		  supports gathering of syslog messages that various components generate. This
                                    		  service implements the CISCO-SYSLOG-MIB.

This service
                                    		  periodically checks the expiration status of certificates that the system
                                    		  generates and sends notification when a certificate gets close to its
                                    		  expiration date.

### Working with
                              		  Services

To start, stop,
                              		  activate, or restart services or to configure service parameters for services
                              		  on the Cisco Prime Collaboration Deployment platform, you must use the CLI. You can start, stop, activate, or refresh
                              only one
                              		  service at a time.

When a service is stopping, you cannot start
                                          		  it until after the service is stopped. Also, when a service is starting,
                                          		  you cannot stop it until after the service is started.

The following
                              		  services are activated by default after you install the Cisco Prime
                              		  Collaboration Deployment platform.

Cisco AMC
                                    				Service

Cisco Audit
                                    				Event Service

Cisco CDP

Cisco CDP
                                    				Agent

Cisco
                                    				Certificate Expiry Monitor

Cisco DRF
                                    				Local

Cisco DRF
                                    				Master

Cisco Log
                                    				Partition Monitoring Tool

Cisco
                                    				Platform Manager Service

Cisco RIS
                                    				Data Collector

Cisco
                                    				Syslog Agent

Cisco
                                    				Tomcat

Cisco
                                    				Tomcat Stats Servlet

Cisco Trace
                                    				Collection Servlet

Host
                                    				Resources Agent

MIB2 Agent

SNMP Master
                                    				Agent

System
                                    				Application Agent

The following
                              		  services are stopped by default after you install the Cisco Prime Collaboration
                              		  Deployment platform.

Cisco Trace
                                    				Collection Service

SOAP-Log
                                    				Collection APIs

SOAP-Performance Monitoring APIs

Caution

Some changes to service parameters may cause system failure. We recommend that you do not make any changes to service parameters
                                          unless you fully understand the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) specifies
                                          the changes.

The following
                              		  table shows the commands that you need to work with services on the Cisco Prime
                              		  Collaboration Deployment platform.

Display
                                          					 a list of services and service status

Activate a service

Stop a
                                          					 service

Start a
                                          					 service

Restart
                                          					 a service

## Limitations and Restrictions

Cisco Prime Collaboration Deployment is not a diagnostic tool. An error message appears on the task list page if a task fails;
                                    however, you should use your usual set of tools and procedures to diagnose and correct the problem.

The SOAP services do not replace the existing OS Administration and CLI upgrade processes. You can still upgrade your servers
                                    by using the application GUIs or CLI commands. Cisco Prime Collaboration Deployment is another way to upgrade, restart, or
                                    switch versions on the application servers.

No localization is available for Cisco Prime Collaboration Deployment. The localization  is available in English only (including
                                    time and date formats).

| Tip | If necessary, to reduce the initialization time, we recommend that you restart the Cisco Trace Collection Service before
                                             restarting the Cisco Trace Collection Servlet. |
|---|---|

| Tip | After you complete SNMP configuration in the CLI, you must restart the SNMP Master Agent service. |
|---|---|

| Note | When a service is stopping, you cannot start
                                          		  it until after the service is stopped. Also, when a service is starting,
                                          		  you cannot stop it until after the service is started. |
|---|---|

| Caution | Some changes to service parameters may cause system failure. We recommend that you do not make any changes to service parameters
                                          unless you fully understand the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) specifies
                                          the changes. |
|---|---|

| Task | Command |
|---|---|
| Display
                                          					 a list of services and service status | utils
                                          					 service list |
| Activate a service | utils
                                          					 service activate |
| Stop a
                                          					 service | utils
                                          					 service stop servicename |
| Start a
                                          					 service | utils
                                          					 service start servicename |
| Restart
                                          					 a service | utils
                                          					 service restart servicename |