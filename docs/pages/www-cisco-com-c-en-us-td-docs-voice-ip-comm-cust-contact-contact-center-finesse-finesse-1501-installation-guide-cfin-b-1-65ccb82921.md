---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-installation-guide-cfin-b-1-65ccb82921
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/installation/guide/cfin_b_1501_cisco-installation-and-upgrade-guide-15_0/network_and_system_services_used_for_cisco_finesse.html
retrieved_at: 2026-08-21T15:53:13.252838+00:00
---

Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

# Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Network and System
	 Services Used for Cisco Finesse

## Chapter: Network and System
	 Services Used for Cisco Finesse

- Network and System                              	 Services Used for Cisco Finesse

# Network and System
                     	 Services Used for Cisco Finesse

To view the
                           		  platform TCP/IP services, UDP services, and Unix domain sockets that are used
                           		  by Cisco Finesse, access the CLI using the Administrator User credentials and
                           		  enter the following command:

show network all
                              			 detail

To view the system
                           		  services that are used by Cisco Finesse, access the CLI using the Administrator
                           		  User credentials and enter the following command:

utils service
                              			 list

The following services are enabled by default when Cisco Finesse starts. These services are essential for product operation
                           and must not be disabled.

A Cisco DB[STARTED]

A Cisco DB Replicator[STARTED]

Cisco AMC Service[STARTED]

Cisco Audit Event Service[STARTED]

Cisco CDP[STARTED]

Cisco CDP Agent[STARTED]

Cisco Certificate Change Notification[STARTED]

Cisco Certificate Expiry Monitor[STARTED]

Cisco DRF Local[STARTED]

Cisco DRF Primary[STARTED]

Cisco DRF Primary should be started only on the Finesse primary (A Side) server.

Status on the Finesse primary (A Side) server should be "STARTED" . Status on the Finesse secondary (B Side) server should be "STOPPED" Command Out of Service.

Cisco Database Layer Monitor[STARTED]

Cisco Finesse Notification Service[STARTED]

Cisco Finesse Tomcat[STARTED]

Cisco Log Partition Monitoring Tool[STARTED]

Cisco RIS Data Collector[STARTED]

Cisco RTMT Reporter Servlet[STARTED]

Cisco Syslog Agent[STARTED]

Cisco Tomcat[STARTED]

Cisco Tomcat Stats Servlet[STARTED]

Cisco Trace Collection Service[STARTED]

Cisco Trace Collection Servlet[STARTED]

Cisco Web Proxy Service[STARTED]

Host Resources Agent[STARTED]

MIB2 Agent[STARTED]

Platform Administrative Web Service[STARTED]

SNMP Primary Agent[STARTED]

SOAP -Log Collection APIs[STARTED]

SOAP -Performance Monitoring APIs[STARTED]

SOAP -Real-Time Service APIs[STARTED]

System Application Agent[STARTED]

| Note | Cisco DRF Primary should be started only on the Finesse primary (A Side) server. Status on the Finesse primary (A Side) server should be "STARTED" . Status on the Finesse secondary (B Side) server should be "STOPPED" Command Out of Service. |
|---|---|