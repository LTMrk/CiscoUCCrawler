---
doc_id: developer-cisco-com-site-sxml-discover-overview-log-collection-5d7dbd0bc1
source_url: https://developer.cisco.com/site/sxml/discover/overview/log-collection/
retrieved_at: 2026-09-01T17:49:09.413580+00:00
---

# Log Collection (LogCollection, DimeGetFile) Overview

The Log Collection service and the File Retrieval (DimeGetFile) service provide retrieval of trace files and logs.

The Log Collection service provides an API for querying, collecting, and transferring Cisco Unified Communications Manager (Unified CM) trace files and logs for troubleshooting and analysis.

The Log Collection API allows clients to:

- Query a list of Cisco Unified CM cluster nodes and their available service logs

- Query the location of log files for a service

- Retrieve FTP or SSH-FTP delivery of log files based on selection criteria

The DimeGetFile service provides an API to download a single log file via the Direct Internet Message Encapsulation (DIME) protocol. The API provides the ability to retrieve one file. Downloading of the file is provided directly across HTTP via the SOAP response without transferring the file to and from the SSH-FTP server

### Use Cases

Log Collection allows applications to retrieve trace files and logs. DimeGetFile allows applications to retrieve a single file via DIME. This information is useful in scenarios such as:

- Cisco Unified CM applications

- Log auto-archiving solutions

- Log analysis tools

- Performing post-processing activities such as reviewing a log for troubleshooting.

### How It Works

The Log Collection and DimeGetFile services are standards-based SOAP interfaces, with available WSDL schema definition.  The application sends a SOAP request with the application user's credentials to the Log Collection or DIME web service  on Cisco Unified CM. The web service processes the request and returns a SOAP response to the application.

### Additional Information

For DimeGetFile, the input parameter is the absolute file name of the file to retrieve from the server. The return value specifies the file name, but the file name will have an AXIS-specific name. After the file is downloaded, you may want to replace the file name with the actual file name received from the server.

The attachment to the SOAP response needs to be decoded with a DIME interpreter.