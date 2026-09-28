---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-windows-deploy-jvdi-b-deployment-installation-jvdi-windows-12-6-jv-174b6ffef0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/windows/deploy/jvdi_b_deployment-installation-jvdi-windows-12-6/jvdi_b_deployment-installation-jvdi-windows-12-6_chapter_0101.html
retrieved_at: 2026-08-22T00:38:14.832508+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Windows Release 12.6

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Windows Release 12.6

Updated: April 9, 2019

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Configuration Files

For each Cisco Unified Client Services Framework (CSF) device that you add to the system, Cisco Unified Communications Manager
                              creates a configuration (CNF.xml) file. The CNF file contains the device specifications for the associated user.

When users sign in to Cisco Jabber , Cisco Jabber Softphone for VDI starts the download of the associated CNF file to the thin client. To ensure the successful transfer of the file, open the
                              relevant ports in all firewall applications to allow the thin client to access the ports. For more information about how to
                              open ports, see the documentation for the firewall software.

Download of the CNF.xml file follows the system setting for HTTP proxy. Ensure that the proxy does not route the HTTP request
                                          from the thin client outside of the corporate network.

## Verify Device Registration with Cisco Unified Communications Manager

After device registration, verify that the CSF device registered to the Cisco Unified Communications Manager from the thin
                              client IP address. For more information, see the documentation for your version of Cisco Unified Communications Manager.

## Registry Keys

The Cisco JVDI Client installation program checks to ensure that either the Citrix Receiver or the VMware Horizon Client is
                              already installed on the reused PC. In one of the following registry locations, the InstallFolder string-type registry key must be present:

For Citrix, the installer searches in HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Citrix\Install\ICA Client for the path to the
                                    Citrix installation.

Example (from an x86 PC): [HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\Install\ICA Client] "InstallFolder"="C:\\Program Files\\Citrix\\ICA Client\\"

For VMware Horizon, the installer searches in HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\VMware, Inc.\VMware VDM for the path
                                    to the VMware installation.

Example (from an x64 PC): [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\VMware, Inc.\VMware VDM] "ClientInstallPath"="C:\\Program Files\\VMware\\VMware View\\Client\\"

## Verify the Connection Status in Cisco Jabber

After you sign in to Cisco Jabber for Windows, you can check the connection status for Jabber and for Cisco Softphone for VDI. You can also confirm the versions
                              for the JVDI Agent and the JVDI Client.

Click to open the Settings Menu .

Go to Help > Show connection status

In the Connection Status window, click JVDI Details .

You can see the following information:

JVDI Client version

If the JVDI Client version is 12.5 or 12.1, the client version doesn't appear until after the softphone connects.

JVDI Agent version

Virtual Channel status indicates whether communication between the JVDI Client and Cisco Jabber is successful.

SIP status indicates whether SIP communication with Cisco Unified Communications Manager is successful.

Softphone CTI status indicates whether CTI communication is successful.

If the SIP status is Connected , but the Softphone CTI status is Not connected , check the CTI configuration in CUCM.

To see detailed diagnostic information for Cisco Jabber , press Ctrl +Shift +D .

## Verify That Cisco JVDI Client Is Running

Use Windows Task Manager to verify that Cisco JVDI Client is running.

In a Citrix environment, the Cisco Jabber Softphone for VDI processes start when the user signs in to their hosted virtual desktop (HVD). The processes stop when the session ends.

In a VMware environment, the Cisco Jabber Softphone for VDI processes start after the user signs in to their HVD and in to Cisco Jabber. The processes stop when the session ends.

On the thin client desktop, right-click the taskbar and then select Task Manager .

On the Processes tab, scroll down and look for the vxc.exe process.

## Verify That Cisco JVDI Agent Is Installed

You can use the Windows Control Panel to verify that Cisco JVDI Agent is installed. You can also verify the version.

From Control Panel, open Programs and Features (Windows 7) or Programs (Windows 8 and later).

Scroll through the list of installed programs to locate Cisco JVDI Agent .

The Cisco JVDI Agent version appears in the Versions column.

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

## Problem Reporting Tool

The Problem Reporting Tool (PRT) is a small program that automatically runs if Cisco Jabber encounters an unrecoverable error, unhandled exception, or crash. The tool saves a problem report to the user's desktop,
                              as a .zip file. Problem reports include logs from the thin client, the hosted virtual desktop, and any detailed information
                              that users enter. You can use this information to help troubleshoot the issue. You can send the problem report to the Cisco
                              Technical Assistance Center (TAC).

If a user experiences an error that does not crash the software, the user can run the PRT from the Help menu:

Cisco Jabber — Help > Report a problem

Users can generate a problem report from the Windows Start menu if Cisco Jabber is not running. You can access the tool from outside the application, from the Microsoft Windows Start menu.

Cisco Jabber — Start > All Programs > Cisco Jabber > Cisco Jabber Problem Report .

We recommend that users provide a description of the circumstances that lead up to the error.

Users must accept the privacy agreement to run the PRT.

### Virtual Channel Problem

If a problem exists with the virtual channel, the problem-reporting tool cannot collect the logs from the thin client. A problem
                                 with the virtual channel can cause the Device Selector to not start or to not populate with devices.

Cisco Technical Assistance Center (TAC) personnel may ask you to gather the logs manually by running one of the following
                                 executables:

Windows OS 32-bit: C:\Program Files (x86)\Cisco Systems\Cisco JVDI\CollectCiscoJVDIClientLogs.exe

Windows OS 64-bit: C:\Program Files\Cisco Systems\Cisco JVDI\CollectCiscoJVDIClientLogs.exe

Linux-based OS: /usr/bin/collect-files

The executable gathers the logs from the thin client and saves them to the desktop as a CiscoJVDIClient-logs[timestamp].7z
                                 file. You can still use the PRT to gather the logs from the hosted virtual desktop. Submit all logs gathered to TAC.

### Enable Log Collection

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

### Enable Memory Dump Collection

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

## d3dcompiler_47.dll Is Missing

Cisco JVDI Client requires d3dcompiler_47.dll, which is missing from some versions of Microsoft Windows. To resolve this problem, install KB4019990
                              for your version of Windows.

## MSVCP140.dll Is Missing

Cisco JVDI Client cannot start the vxc.exe process, which quits with the error: "MSVCP140.dll is missing" .

To resolve this issue, install Visual Studio C++ Redistributable 2012 Update 4 or later.

## VCRUNTIME140.dll Is Missing

CollectCiscoJVDIClientLogs.exe quits with the error message: "VCRUNTIME140.dll is missing" .

To resolve this issue, install Visual Studio C++ Redistributable 2012 Update 4 or later.

| Important | Download of the CNF.xml file follows the system setting for HTTP proxy. Ensure that the proxy does not route the HTTP request
                                          from the thin client outside of the corporate network. |
|---|---|

| Step 1 | Click to open the Settings Menu . |
|---|---|
| Step 2 | Go to Help > Show connection status |
| Step 3 | In the Connection Status window, click JVDI Details . You can see the following information: JVDI Client version Tip If the JVDI Client version is 12.5 or 12.1, the client version doesn't appear until after the softphone connects. JVDI Agent version Virtual Channel status indicates whether communication between the JVDI Client and Cisco Jabber is successful. SIP status indicates whether SIP communication with Cisco Unified Communications Manager is successful. Softphone CTI status indicates whether CTI communication is successful. Tip If the SIP status is Connected , but the Softphone CTI status is Not connected , check the CTI configuration in CUCM. | Tip | If the JVDI Client version is 12.5 or 12.1, the client version doesn't appear until after the softphone connects. | Tip | If the SIP status is Connected , but the Softphone CTI status is Not connected , check the CTI configuration in CUCM. |
| Tip | If the JVDI Client version is 12.5 or 12.1, the client version doesn't appear until after the softphone connects. |
| Tip | If the SIP status is Connected , but the Softphone CTI status is Not connected , check the CTI configuration in CUCM. |
| Step 4 | To see detailed diagnostic information for Cisco Jabber , press Ctrl +Shift +D . |

| Tip | If the JVDI Client version is 12.5 or 12.1, the client version doesn't appear until after the softphone connects. |
|---|---|

| Tip | If the SIP status is Connected , but the Softphone CTI status is Not connected , check the CTI configuration in CUCM. |
|---|---|

| Step 1 | On the thin client desktop, right-click the taskbar and then select Task Manager . |
|---|---|
| Step 2 | On the Processes tab, scroll down and look for the vxc.exe process. |

| Step 1 | From Control Panel, open Programs and Features (Windows 7) or Programs (Windows 8 and later). |
|---|---|
| Step 2 | Scroll through the list of installed programs to locate Cisco JVDI Agent . The Cisco JVDI Agent version appears in the Versions column. |

| Step 1 |  |
|---|---|
| Step 2 | On the thin client, open Control Panel > Programs and Features . |
| Step 3 | Scroll down the list and locate Cisco JVDI Client . |
| Step 4 | To confirm the version for Cisco JVDI Client , see the Version column. |

| Note | We recommend that users provide a description of the circumstances that lead up to the error. Users must accept the privacy agreement to run the PRT. |
|---|---|

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