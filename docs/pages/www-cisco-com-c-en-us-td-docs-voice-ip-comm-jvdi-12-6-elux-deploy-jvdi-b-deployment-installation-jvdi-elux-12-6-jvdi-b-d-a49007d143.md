---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-elux-deploy-jvdi-b-deployment-installation-jvdi-elux-12-6-jvdi-b-d-a49007d143
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/elux/deploy/jvdi_b_deployment-installation-jvdi-elux-12-6/jvdi_b_deployment-installation-jvdi-elux-12-6_chapter_0101.html
retrieved_at: 2026-08-22T00:36:46.262583+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.6

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.6

Updated: April 9, 2019

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Verify Device Registration with Cisco Unified Communications Manager

After device registration, verify that the CSF device registered to the Cisco Unified Communications Manager from the thin
                              client IP address. For more information, see the documentation for your version of Cisco Unified Communications Manager.

## Verify the Platform Base Image Version

On the Start menu, select Control Panel .

Select  the Setup tab.

Select the General tab and look for the OS line.

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

## Verify That Cisco JVDI Client Is Installed

Use this procedure to verify that Cisco JVDI Client is installed, and to confirm the Cisco JVDI Client version.

On the Start menu, select Control Panel .

Select the Setup tab.

Select the General tab.

Scroll down the list of packages and look for Cisco JVDI Client .

The add-on versions appear in the same line.

## Verify That Cisco JVDI Agent Is Installed

You can use the Windows Control Panel to verify that Cisco JVDI Agent is installed. You can also verify the version.

From Control Panel, open Programs and Features (Windows 7) or Programs (Windows 8).

Scroll through the list of installed programs to locate Cisco JVDI Agent .

The Cisco JVDI Agent version appears in the Versions column.

## Verify That VXC Is Running on the Thin Client

Cisco Jabber Softphone for VDI requires that the vxc process be running.

Use Secure Shell (SSH) to connect to the thin client.

Search the running programs for vxc .

ps -ef | grep -r vxc

You should see the following lines:

```
admin@LWT44d3ca76ba19:~> ps -ef |grep -r vxc

thinuser 6536 1 0 Mar14 ? 00:07:43 /bin/bash /usr/bin/pidrun.sh -c run_vxc.sh -a -m -o /var/log/cisco/vxcConsole.log -e /var/log/cisco/vxcError.log

thinuser 6538 6536 0 Mar14 ? 00:00:00 /bin/bash /usr/bin/run_vxc.sh -m

thinuser 6547 6538 8 Mar14 ? 13:02:16 vxc -m

admin 31576 31303 0 11:05 pts/0 00:00:00 grep -r vxc

admin@LWT44d3ca76ba19:~>
```

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

The Problem Reporting Tool (PRT) is a small program that automatically runs if Cisco Jabber encounters an unrecoverable error, unhandled exception, or crash. The tool collects logs from the thin client and hosted
                              virtual desktop and then creates a problem report. The report is a zip file that you can send to the Cisco Technical Assistance
                              Center (TAC), to provide the necessary information to solve the problem. The tool saves the file to the user's desktop. Users
                              must accept the privacy agreement to run the PRT.

Advise users to include a memory dump with the problem report if Cisco Jabber crashes. We also recommend that users provide a description of the circumstances that lead up to the error.

If a user experiences an error that does not crash the software, the user can run the PRT from the Cisco Jabber menu: Help > Report a problem .

If Cisco Jabber is not running, users can generate a problem report from the Windows Start menu . To access the tool from outside the application, choose Start > All Programs > Cisco Jabber > Cisco Jabber Problem Report .

Problem reports include logs from the thin client, the hosted virtual desktop, and any detailed information that users enter.
                                          You can use this information to help troubleshoot the issue.

If there is a problem with the virtual channel, or if Cisco Jabber is not running, the problem report does not include logs from the thin client. For more information, see Virtual Channel Problem .

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

## Configuration Files

For each Cisco Unified Client Services Framework (CSF) device that you add to the system, Cisco Unified Communications Manager
                              creates a configuration (CNF.xml) file. The CNF file contains the device specifications for the associated user.

When users sign in to Cisco Jabber , Cisco Jabber Softphone for VDI starts the download of the associated CNF file to the thin client. To ensure the successful transfer of the file, open the
                              relevant ports in all firewall applications to allow the thin client to access the ports. For more information about how to
                              open ports, see the documentation for the firewall software.

Download of the CNF.xml file follows the system setting for HTTP proxy. Ensure that the proxy does not route the HTTP request
                                          from the thin client outside of the corporate network.

| Step 1 | On the Start menu, select Control Panel . |
|---|---|
| Step 2 | Select  the Setup tab. |
| Step 3 | Select the General tab and look for the OS line. |

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

| Step 1 | On the Start menu, select Control Panel . |
|---|---|
| Step 2 | Select the Setup tab. |
| Step 3 | Select the General tab. |
| Step 4 | Scroll down the list of packages and look for Cisco JVDI Client . The add-on versions appear in the same line. |

| Step 1 | From Control Panel, open Programs and Features (Windows 7) or Programs (Windows 8). |
|---|---|
| Step 2 | Scroll through the list of installed programs to locate Cisco JVDI Agent . The Cisco JVDI Agent version appears in the Versions column. |

| Step 1 | Use Secure Shell (SSH) to connect to the thin client. |
|---|---|
| Step 2 | Search the running programs for vxc . ps -ef \| grep -r vxc You should see the following lines: admin@LWT44d3ca76ba19:~> ps -ef \|grep -r vxc

thinuser 6536 1 0 Mar14 ? 00:07:43 /bin/bash /usr/bin/pidrun.sh -c run_vxc.sh -a -m -o /var/log/cisco/vxcConsole.log -e /var/log/cisco/vxcError.log

thinuser 6538 6536 0 Mar14 ? 00:00:00 /bin/bash /usr/bin/run_vxc.sh -m

thinuser 6547 6538 8 Mar14 ? 13:02:16 vxc -m

admin 31576 31303 0 11:05 pts/0 00:00:00 grep -r vxc

admin@LWT44d3ca76ba19:~> |

| Tip | Advise users to include a memory dump with the problem report if Cisco Jabber crashes. We also recommend that users provide a description of the circumstances that lead up to the error. |
|---|---|

| Important | Problem reports include logs from the thin client, the hosted virtual desktop, and any detailed information that users enter.
                                          You can use this information to help troubleshoot the issue. If there is a problem with the virtual channel, or if Cisco Jabber is not running, the problem report does not include logs from the thin client. For more information, see Virtual Channel Problem . |
|---|---|

| Important | Download of the CNF.xml file follows the system setting for HTTP proxy. Ensure that the proxy does not route the HTTP request
                                          from the thin client outside of the corporate network. |
|---|---|