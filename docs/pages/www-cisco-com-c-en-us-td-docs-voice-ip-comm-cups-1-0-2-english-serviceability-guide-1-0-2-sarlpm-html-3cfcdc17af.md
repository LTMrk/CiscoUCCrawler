---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-serviceability-guide-1-0-2-sarlpm-html-3cfcdc17af
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/serviceability/guide/1_0_2/sarlpm.html
retrieved_at: 2026-08-21T16:06:41.197105+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Log Partition Monitoring Configuration

## Chapter: Log Partition Monitoring Configuration

- Enabling Log Partition Monitoring

- Configuring Log Partition Monitoring

- Related Topics

## Log Partition Monitoring Configuration

Every 5 minutes, Log Partition Monitoring uses the following configured thresholds to monitor the disk usage of the log partition on a server (or all servers in the cluster):

• LogPartitionLowWaterMarkExceeded (% disk space)—When the disk usage is above the percentage that you specify, LPM sends out an alarm message to syslog and an alert to RTMT Alert central. To save the log files and regain disk space, you can use trace and log central option in RTMT.

• LogPartitionHighWaterMarkExceeded (% disk space)—When the disk usage is above the percentage that you specify, LPM sends a n alarm message to syslog and an alert to RTMT Alert central.

## Enabling Log Partition Monitoring

To enable Log Partition Monitoring, perform the following procedure:

Step 1 In Cisco Unified Presence Server Serviceability, choose Tools > Control Center > Network Services .

Step 2 From the Servers drop-down list box, choose the server where you want to monitor the disk usage.

Step 3 Under CCM Services, verify the status of the Cisco Log Partition Monitoring Tool (LPM).

Step 4 If the LPM is not running, click the radio button next to Cisco LPM and click the Start button

## Configuring Log Partition Monitoring

To configure Log Partitioning Monitoring, set the alert properties for the LogPartitionLowWaterMarkExceeded and LogPartitionHighWaterMarkExceeded alerts in Alert Central. See the "Setting Alert Properties" section .

Additional Information

See the Related Topics .

## Related Topics

• Log Partition Monitoring , Cisco Unified CallManager Serviceability System Guide

• Alert Configuration in RTMT , Cisco Unified CallManager Serviceability System Guide

• Trace Collection and Log Central in RTMT , Cisco Unified Presence Server Serviceability Administration Guide