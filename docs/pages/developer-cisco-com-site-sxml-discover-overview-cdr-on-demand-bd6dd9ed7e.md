---
doc_id: developer-cisco-com-site-sxml-discover-overview-cdr-on-demand-bd6dd9ed7e
source_url: https://developer.cisco.com/site/sxml/discover/overview/cdr-on-demand/
retrieved_at: 2026-09-01T17:49:05.121185+00:00
---

# CDRonDemand Overview

Call Detail Records (CDR) are available through two interfaces to the Cisco Unified Communications Manager (Unified CM):

- CDR Service

- CDRonDemand API

The following image shows the architecture..

### CDR Data

Cisco Unified CM produces two types of records which store call history and diagnostic information:

- Call detail records (CDR) are data records containing information about each call  processed by CallManager.

- Call management records (CMR) are data records containing quality of service (QoS) or diagnostic information about the call. Also referred to as diagnostic records.

Both CDR and CMR are referred to as CDR data. CDR data provides a record of all calls that have been made or received by CallManager system users. CDR data is used primarily for generating billing records. However, CDR data can also be used for tracking call activity, diagnosing certain problem types, and capacity planning.

CDRs contain information about call origination, call destination, the date and time the call was started, the time the call connected, and the time the call ended. A call is considered started or originated when the caller goes off-hook. The call is considered ended when either the caller or the called party goes on-hook.

CMRs contain information about the amount of data sent and received, jitter, latency, and lost packets.

For details on the CDR service configuration, and CDR data file contents and definitions, refer to the Cisco Unified Communications Manager Administration Guides.

### When to use CDR Service or CDRonDemand API

For applications that need a continuous feed of all CDR records, use the CDR Service to configure the CDR Repository Manager to send CDR data files to your server via FTP or SSH-FTP.

To retrieve individual CDR files on demand, use the CDRonDemand API. However, this API is intended for ad-hoc inspection of a small number of individual files and is not suitable for bulk CDR retrieval. CDRonDemand requests are limited to 15 requests per minute by default.

For details on the CDR Service, go to CDR Overview (link).

### CDRonDemand API

The CDRonDemand API allows applications to request delivery of specified CDR flat files from the Cisco Unified CM CDR Repository (Publisher node)  to a remote FTP or SSH-FTP server.

### Use Cases

CDRonDemand allows applications to perform post-processing activities such as reviewing specific calls and performing targeted call analysis. CDRonDemand retrieves single files where each file covers a short period of time (by default one minute).

### How It Works

The CDRonDemand API enables applications to obtain CDR files in a two-step process.

- 1. The application uses a get_file_list query for available CDR files based on a specific time interval, limited to a one hour time span.

- 2. The application uses get_file to request a specific CDR file.

If an application needs to retrieve CDR files that span an interval over one hour, multiple get_file_list requests can be made to the service.

After the list of files is retrieved, the application requests a specific file (get_file). Upon receiving the request, the CDRonDemand API initiates a FTP or SSH-FTP session and sends the requested file to the application server. Only one file is processed per request.

### Additional Information

Applications only need to query the Cisco Unified CM Publisher node as the CDR Repository Manager consolidates the CDR files from all nodes in the cluster.

CDRonDemand requests are based on:

- UTC timestamp within an hour interval. The timestamp is a string of the format YYYYMMDDHHMM.

- FTP or SSH-FTP parameters including host name, username, password, and file delivery path

- CDR filename requested

To set throttling for CDRonDemand, from the Cisco Unified CM Administration Guide , select these parameters under System > Enterprise Parameters:

- Allowed CDRonDemand get_file queries per minute: minimum = 1, maximum = 20, default = 10

- Allowed CDRonDemand get_file_list queries per minute: minimum = 1, maximum = 40, default = 20