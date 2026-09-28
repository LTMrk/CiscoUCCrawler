---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-5-jvdi-b-deploy-install-cisco-jvdi-hp-ubuntu-12-5-jvdi-b-deploy-inst-a9ff5582cd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_5/jvdi_b_deploy-install-cisco-jvdi-hp-ubuntu-12-5/jvdi_b_deploy-install-cisco-jvdi-hp-ubuntu-12-5_chapter_0101.html
retrieved_at: 2026-08-22T00:35:09.545922+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.5

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.5

Updated: November 29, 2018

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Verify Device Registration with Cisco Unified Communications Manager

After device registration, verify that the CSF device registered to the Cisco Unified Communications Manager from the thin
                              client IP address. For more information, see the documentation for your version of Cisco Unified Communications Manager.

## Verify the Platform Version—HP Thin Pro

On the thin client, open the terminal console.

Enter the following command: lsb_release -a .

Look in the output for the HP Thin Pro version.

### Example:

```
HP Thin Pro 5.2
```

## Verify the Platform Version—Ubuntu

On the thin client, open System Settings .

Select Details .

The version appears under the Ubuntu logo.

### Example:

```
Ubuntu 14.04.x 32b LTS
```

## Verify That the Cisco JVDI Client Is Installed

Use this procedure to verify that Cisco JVDI Client is installed, and to confirm the version.

On the thin client, open the terminal console.

Enter the following command: dpkg -l | grep jvdi .

In the output, look for ii cisco-jvdi-client.

### Example:

```
ii cisco-jvdi-client <xx.x.x.xxx> i386 Cisco JVDI Client
```

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

| Step 1 | On the thin client, open the terminal console. |
|---|---|
| Step 2 | Enter the following command: lsb_release -a . |
| Step 3 | Look in the output for the HP Thin Pro version. Example: HP Thin Pro 5.2 |

| Step 1 | On the thin client, open System Settings . |
|---|---|
| Step 2 | Select Details . The version appears under the Ubuntu logo. Example: Ubuntu 14.04.x 32b LTS |

| Step 1 | On the thin client, open the terminal console. |
|---|---|
| Step 2 | Enter the following command: dpkg -l \| grep jvdi . |
| Step 3 | In the output, look for ii cisco-jvdi-client. Example: ii cisco-jvdi-client <xx.x.x.xxx> i386 Cisco JVDI Client |

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