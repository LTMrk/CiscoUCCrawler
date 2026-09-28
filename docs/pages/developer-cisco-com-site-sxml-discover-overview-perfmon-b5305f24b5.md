---
doc_id: developer-cisco-com-site-sxml-discover-overview-perfmon-b5305f24b5
source_url: https://developer.cisco.com/site/sxml/discover/overview/perfmon/
retrieved_at: 2026-09-01T17:48:56.825119+00:00
---

# PerfMon Overview

Performance Monitoring (PerfMon) provides platform, service, and application performance counters to
                monitor the health of Cisco Unified Communications Manager (Cisco Unified CM). Snapshot and
                session-based access is available via standard SOAP web services. This API returns a snapshot of the
                performance counters for all instances of an object on the specified host.

PerfMon allows clients to perform the following tasks:

- Collect and monitor PerfMon performance data either session-based or single-transaction

- Retrieve a list of all PerfMon objects and counter names installed on a particular host

- Retrieve a list of the current instances of a PerfMon object

- Retrieve textual description of a PerfMon counter

A session handle is needed by the client to collect session-based PerfMon counter data. The session
                handle is a unique identifier the application reuses for subsequent requests.

### Use Cases

Monitoring performance counters is useful in scenarios such as:

- A system use application to determine the peak hours of contacts to a call center to adequately
                    staff the center during that time frame.

- A system health and monitoring application to store and analyze the status and health of Cisco
                    Unified CM as an organization grows and call rates increase to accurately forecast and budget timely
                    software upgrades and hardware replacements.

### How It Works

PerfMon is a standards-based SOAP interface, with available WSDL schema definition. The application sends
                a SOAP request with the application user’s credentials to the PerfMon web service on Cisco
                Unified CM. The web service processes the request and returns a SOAP response to the application.

Use the PerfMon WSDL:

https://ServerName:8443/perfmonservice2/services/PerfmonService?wsdl

Replace ServerName with the Cisco Unified CM server name.

Performance monitoring provides two methods to collect data:

- Session-based

- Single-transaction based

#### Session-Based Performance Monitoring

Client programs use the perfmonOpenSession request to obtain a session handle. The client needs a session
                handle to do session-based PerfMon counter data collection. Use the perfmonOpenSession method to open a
                session and create a unique session identifier which will be used to manage subsequent PerfMon API
                requests.

In session-based PerfMon data collection, a common scenario uses the following related operations often
                executed in the following order:

- i. perfmonOpenSession

- ii. perfmonAddCounter

- iii. perfmonCollectSessionData

- iv. perfmonRemoveCounter

- v. perfmonCloseSession

After the client application gets a session handle, add a counter with perfmonAddCounter, and then follow
                with perfmonCollectSessionData. This collects the performance data requested.

Clients can dynamically add and remove counters to the session handle by using perfMonAddCounter and
                perfmonRemoveCounter while the session handle is still open.

When the client no longer needs the session handle, use perfmonCloseSession and the session handle is
                removed from the cache.

#### Single-Transaction Based Performance Monitoring

Single-transaction based performance monitoring involves percentage counters. Percentage counters require
                at least two samples to determine an average sample. Percentage value elements involve a single sample
                and do not require a session handle. However, a single sample may not provide the information needed.
                Session-based requests may be needed.