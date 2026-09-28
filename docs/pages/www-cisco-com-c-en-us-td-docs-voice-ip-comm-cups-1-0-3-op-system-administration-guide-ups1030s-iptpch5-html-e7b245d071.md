---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-3-op-system-administration-guide-ups1030s-iptpch5-html-e7b245d071
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_3/op_system/administration/guide/ups1030s/iptpch5.html
retrieved_at: 2026-08-21T02:48:23.496983+00:00
---

Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

# Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

Updated: February 21, 2007

Chapter: System Restart

## Chapter: System Restart

- Switch Versions and Restart

- Restart Current Version

- Shut Down the System

## System Restart

This section provides procedures for using the following restart options:

• Switch Versions and Restart

• Restart Current Version

• Shut Down the System

## Switch Versions and Restart

You can use this option both when you are upgrading to a newer software version or when you need to fall back to an earlier software version. To shut down the system that is running on the active disk partition and then automatically restart the system using the software version on the inactive partition, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Restart>Switch Versions .

The Switch Software Version window displays, which shows the software version on both the active and inactive partitions.

Step 2 To switch versions and restart, click Switch Version . To stop the operation, click Cancel .

If you click Switch Version , the system restarts, and the partition that is currently inactive becomes active.

## Restart Current Version

To restart the system on the current partition without switching versions, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Restart>Current Version .

The Restart Current Version window displays.

Step 2 To restart the system, click Restart , or to stop the operation, click Cancel .

If you click Restart , the system restarts on the current partition without switching versions.

## Shut Down the System

To shut down the system, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Restart>Shutdown System .

The Shutdown System window displays.

Step 2 To shut down the system, click Shutdown , or to stop the operation, click Cancel .

If you click Shutdown , the system halts all processes and shuts down.

Note The hardware does not power down automatically.