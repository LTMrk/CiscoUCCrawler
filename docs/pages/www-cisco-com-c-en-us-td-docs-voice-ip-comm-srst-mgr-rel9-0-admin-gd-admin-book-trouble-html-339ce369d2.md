---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-trouble-html-339ce369d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/trouble.html
retrieved_at: 2026-08-21T23:40:08.847443+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Troubleshooting Using the CLI

## Chapter: Troubleshooting Using the CLI

## Troubleshooting Using the CLI

Cisco technical support personnel may request that you run one or more of these commands when troubleshooting a problem. Cisco technical support personnel will provide additional information about the commands at that time.

## Log and Trace Files

### About Logging

To check the log and trace files on the hard disk, use the show logs command in EXEC mode. This command displays the list of logs available, their size, and their dates of most recent modification.

When the log file reaches its maximum length, Cisco Unified SRST Manager renames the file and creates a new logging file.

For a detailed list of all the arguments associated with the trace command, see trace .

Note Logs for E-SRST are turned on by default.

### Example of Log Output

The following is an example of the show logs output:

### Log Commands in Configuration Mode

- log console errors —Displays error messages (severity=3)

- log console info —Displays information messages (severity=6)

- log console notice —Displays notices (severity=5)

- log console warning —Displays warning messages (severity=4)

- log server address a.b.c.d

log trace

- log trace local enable

- log trace server enable

- log trace server url ftp-url

### Log Commands in EXEC Mode

- log console monitor

- log trace boot

- log trace buffer save

### Saving and Viewing Log Files

Problem You must be able to save log files to a remote location.

Recommended Action Log files are saved to a disk by default. You can configure Cisco Unified SRST Manager to store the log files on a separate server by using the log server address command. Also, you can copy log files on the disk to a separate server if they need to be kept for history purposes, for example:

Problem You cannot display the contents of the log files.

Recommended Action Copy the log files from Cisco Unified SRST Manager to an external server and use a text editor, such as vi , to display the content.

## Using Trace Commands

To troubleshoot network configuration in Cisco Unified SRST Manager, use the trace command in EXEC mode. For a detailed list of all the arguments associated with the trace command, see trace .