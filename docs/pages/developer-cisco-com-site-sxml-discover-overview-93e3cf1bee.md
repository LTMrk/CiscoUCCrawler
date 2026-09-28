---
doc_id: developer-cisco-com-site-sxml-discover-overview-93e3cf1bee
source_url: https://developer.cisco.com/site/sxml/discover/overview/
retrieved_at: 2026-08-25T21:10:34.167923+00:00
---

# What is Unified CM Serviceability?

## Real-time Information Port
                    (RiSPort)

The RisPort (Real-Time Information Port) service provides an API for querying the current connection status of phones, devices, and applications connected to Cisco Unified Communications Manager (Unified CM).

## Performance Monitoring
                    (PerfMon)

The Perfmon interface provides remote applications with performance information of Unified CM. Applications can retrieve the number of phones, gateways, or trunks currently registered, monitor services such as TFTP performance while phones download new firmware, and trigger alarms when performance thresholds are exceeded.

## Control Center
                    interfaces

The Control Center interfaces within the Service XML library provide remote applications with the ability to obtain status information for all of the services running on a Unified CM Publisher and Subscriber.  Applications can enable/disable, start/stop, and re-start services as needed.

## Call Detail Records

Unified CM call detail records are available for on-demand queries through the Call Detail Records on Demand (CDRonDemand) interface.

Call Detail Record files are also available via ftp for applications that require bulk or scheduled retrieval.

## Log Collection and
                    DIME

The Log Collection interfaces within the Service XML library provide remote applications with the ability to retrieve log files from Unified CM Publisher and Subscriber servers and virtual machines.

## SNMP

SNMP can be used to query for performance counters on demand and to subscribe to Unified CM serviceability events.