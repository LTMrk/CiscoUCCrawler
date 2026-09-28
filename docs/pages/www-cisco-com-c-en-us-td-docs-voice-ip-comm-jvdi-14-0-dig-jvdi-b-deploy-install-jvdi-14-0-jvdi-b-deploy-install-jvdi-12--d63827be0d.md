---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-0-dig-jvdi-b-deploy-install-jvdi-14-0-jvdi-b-deploy-install-jvdi-12--d63827be0d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_0/dig/jvdi_b_deploy-install-jvdi-14-0/jvdi_b_deploy-install-jvdi-12-9_chapter_01001.html
retrieved_at: 2026-08-22T00:31:44.687600+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 14.0

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 14.0

Updated: March 25, 2021

Chapter: Troubleshooting—Windows

## Chapter: Troubleshooting—Windows

# Troubleshooting—Windows

## Configuration Files

For each Cisco Unified Client Services Framework (CSF) device that you add to the system, Cisco Unified Communications Manager
                              creates a configuration (CNF.xml) file. The CNF file contains the device specifications for the associated user.

When users sign in to Cisco Jabber , Cisco Jabber Softphone for VDI starts the download of the associated CNF file to the thin client. To ensure the successful transfer of the file, open the
                              relevant ports in all firewall applications to allow the thin client to access the ports. For more information about how to
                              open ports, see the documentation for the firewall software.

Download of the CNF.xml file follows the system setting for HTTP proxy. Ensure that the proxy does not route the HTTP request
                                          from the thin client outside of the corporate network.

## Registry Keys

The Cisco JVDI Client installation program checks to ensure that either the Citrix Receiver or the VMware Horizon Client is
                              already installed on the reused PC. In one of the following registry locations, the InstallFolder string-type registry key must be present:

For Citrix, the installer searches in HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Citrix\Install\ICA Client for the path to the
                                    Citrix installation.

Example (from an x86 PC): [HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\Install\ICA Client] "InstallFolder"="C:\\Program Files\\Citrix\\ICA Client\\"

For VMware Horizon, the installer searches in HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\VMware, Inc.\VMware VDM for the path
                                    to the VMware installation.

Example (from an x64 PC): [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\VMware, Inc.\VMware VDM] "ClientInstallPath"="C:\\Program Files\\VMware\\VMware View\\Client\\"

## Verify That Cisco JVDI Client Is Running

Use Windows Task Manager to verify that Cisco JVDI Client is running.

In a Citrix environment, the Cisco Jabber Softphone for VDI processes start when the user signs in to their hosted virtual desktop (HVD). The processes stop when the session ends.

In a VMware environment, the Cisco Jabber Softphone for VDI processes start after the user signs in to their HVD and in to Cisco Jabber. The processes stop when the session ends.

On the thin client desktop, right-click the taskbar and then select Task Manager .

On the Processes tab, scroll down and look for the vxc.exe process.

## Confirm the Version of Cisco JVDI Client

Cisco JVDI Client appears in the list of installed programs and features.

On the thin client, open Control Panel > Programs and Features .

Scroll down the list and locate Cisco JVDI Client .

To confirm the version for Cisco JVDI Client , see the Version column.

## Call Control Is Lost After a Network Failure

Users  see a prompt to reconnect to their hosted virtual desktops (HVDs). After the users reconnect, Cisco Jabber call control features do not work.

This problem can occur if the thin client loses network connectivity.

To resolve this issue, have the users exit Cisco Jabber and disconnect from their HVDs. Next they can log back in to their HVDs and sign back in to Cisco Jabber to restore call control.

## Call Is Lost After HVD Disconnection

Users receive a prompt to log back in to their hosted virtual desktops (HVD) during an active call, and the call drops. The
                              other party to the call has  no indication that the call has ended, except the line is silent.

This issue can occur if the  connection between the thin client and the  HVD drops, causing a temporary loss of registration
                              and call control.

To work around this issue, users can call the other party back. If the other party is not available, users can send an instant
                              message (IM).

## Enable Log Collection

You can modify the Cisco configuration file (cisco.conf) to enable the collection of logs from the thin client.

The cisco.conf file is located in: C:\Program Files (x86)\Cisco Systems\Cisco VXME\cisco.conf

Open the cisco.conf file and add the following lines:

```
[logger]

log_level = Debug
```

You can set the log level to one of the following values: Fatal, Error, Warning, Info, Debug or Trace. The default level is
                                          Debug.

Save the file.

Restart the vxc process by logging out and back in to the HVD.

## Enable Memory Dump Collection

You can modify the Cisco configuration file (cisco.conf) to enable the Problem Reporting Tool (PRT) to collect a memory dump.

For Windows 32-bit, the cisco.conf file is located in C:\Program Files (x86)\Cisco Systems\Cisco VXME\cisco.conf .

For Windows 64-bit, the cisco.conf file is located in C:\Program Files\Cisco Systems\Cisco VXME\cisco.conf .

Open the cisco.conf file and add the following lines:

```
[logger]

dump_type = Minidump
dump_when_collect_log = True
```

You can set the dump_type to Fulldump or Minidump. The default is Minidump. If dump_when_collect_log is set to False, the
                                          PRT doesn't collect the memory dump.

Save the file.

Restart the vxc process by logging out and back in to the HVD.

## Display issues

Certain third-party application window can make preview, remote video, and remote share display as gray when the window is
                              close to a Jabber conversation window ( CSCvz75206 ).

In Jabber Softphone for VDI Release 14.0.3, we added support for a new Jabber parameter, EnableVDIFullScan , to correct these issues. You must run JVDI 14.0.3 with Jabber for Windows 14.0.4 to use this parameter.

| Important | Download of the CNF.xml file follows the system setting for HTTP proxy. Ensure that the proxy does not route the HTTP request
                                          from the thin client outside of the corporate network. |
|---|---|

| Step 1 | On the thin client desktop, right-click the taskbar and then select Task Manager . |
|---|---|
| Step 2 | On the Processes tab, scroll down and look for the vxc.exe process. |

| Step 1 |  |
|---|---|
| Step 2 | On the thin client, open Control Panel > Programs and Features . |
| Step 3 | Scroll down the list and locate Cisco JVDI Client . |
| Step 4 | To confirm the version for Cisco JVDI Client , see the Version column. |

| Step 1 | Open the cisco.conf file and add the following lines: [logger]

log_level = Debug You can set the log level to one of the following values: Fatal, Error, Warning, Info, Debug or Trace. The default level is
                                          Debug. |
|---|---|
| Step 2 | Save the file. |
| Step 3 | Restart the vxc process by logging out and back in to the HVD. |

| Step 1 | Open the cisco.conf file and add the following lines: [logger]

dump_type = Minidump
dump_when_collect_log = True You can set the dump_type to Fulldump or Minidump. The default is Minidump. If dump_when_collect_log is set to False, the
                                          PRT doesn't collect the memory dump. |
|---|---|
| Step 2 | Save the file. |
| Step 3 | Restart the vxc process by logging out and back in to the HVD. |