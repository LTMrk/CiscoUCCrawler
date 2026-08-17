---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-os-administration-guide-b-15cucosagx-b-15cucosagx-chapter-0100-90b6937200
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx/b_15cucosagx_chapter_0100.html
retrieved_at: 2026-08-17T03:43:18.928560+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15

Updated: October 1, 2024

Chapter: Version
	 Settings

## Chapter: Version
	 Settings

# Version
                     	 Settings

## Version
                        	 Settings

### Switch Versions
                           	 and Restart

You can use this option both when you are upgrading to a newer
                                 		  software version and when you need to fall back to an earlier software version.
                                 		  To shut down the system that is running on the active disk partition and then
                                 		  automatically restart the system with the software version on the inactive
                                 		  partition, follow this procedure:

Caution

This procedure causes the system to restart and become
                                             			 temporarily out of service.

Step 1

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > Version .

The Version Settings window, which shows the software version on
                                             				both the active and inactive partitions, displays.

Step 2

To switch versions and restart, click Switch Versions . To stop the operation, click Cancel .

If you click Switch Version , the system restarts, and the partition that
                                             				is currently inactive becomes active.

### Restart Current
                           	 Version

To restart the system on the current partition without switching
                                 		  versions, follow this procedure:

Caution

This procedure causes the system to restart and become
                                             			 temporarily out of service.

Step 1

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > Version .

The Version Settings window, which shows the software version on
                                             				both the active and inactive partitions, displays.

Step 2

To restart the system, click Restart or, to stop the operation, click Cancel .

If you click Restart , the system restarts on the current partition
                                             				without switching versions.

### Shut Down the
                           	 System

Caution

Do not press the power button on the server to shut down the
                                             			 server or to reboot the server. If you do, you may accidentally corrupt the
                                             			 file system, which may prevent you from being able to reboot your server.

To shut down the system, follow Procedure 1 or Procedure 2.

Caution

This procedure causes the system to shut down.

Step 1

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > Version .

The Version Settings window, which shows the software version on
                                             				both the active and inactive partitions, displays.

Step 2

To shut down the system, click Shutdown or, to stop the operation, click Cancel .

If you click Shutdown , the system halts all processes and shuts down.

The hardware may require several minutes to power down.

#### Alternate Procedure

Run the CLI command utils system shutdown or the command utils system restart. For information on how to run CLI commands,
                                             refer to the Command Line Interface Reference Guide for Cisco Unifed Communications Solutions.

| Caution | This procedure causes the system to restart and become
                                             			 temporarily out of service. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > Version . The Version Settings window, which shows the software version on
                                             				both the active and inactive partitions, displays. |
|---|---|
| Step 2 | To switch versions and restart, click Switch Versions . To stop the operation, click Cancel . If you click Switch Version , the system restarts, and the partition that
                                             				is currently inactive becomes active. |

| Caution | This procedure causes the system to restart and become
                                             			 temporarily out of service. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > Version . The Version Settings window, which shows the software version on
                                             				both the active and inactive partitions, displays. |
|---|---|
| Step 2 | To restart the system, click Restart or, to stop the operation, click Cancel . If you click Restart , the system restarts on the current partition
                                             				without switching versions. |

| Caution | Do not press the power button on the server to shut down the
                                             			 server or to reboot the server. If you do, you may accidentally corrupt the
                                             			 file system, which may prevent you from being able to reboot your server. |
|---|---|

| Caution | This procedure causes the system to shut down. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Settings > Version . The Version Settings window, which shows the software version on
                                             				both the active and inactive partitions, displays. |
|---|---|
| Step 2 | To shut down the system, click Shutdown or, to stop the operation, click Cancel . If you click Shutdown , the system halts all processes and shuts down. Note The hardware may require several minutes to power down. | Note | The hardware may require several minutes to power down. |
| Note | The hardware may require several minutes to power down. |

| Note | The hardware may require several minutes to power down. |
|---|---|

| Run the CLI command utils system shutdown or the command utils system restart. For information on how to run CLI commands,
                                             refer to the Command Line Interface Reference Guide for Cisco Unifed Communications Solutions. |
|---|