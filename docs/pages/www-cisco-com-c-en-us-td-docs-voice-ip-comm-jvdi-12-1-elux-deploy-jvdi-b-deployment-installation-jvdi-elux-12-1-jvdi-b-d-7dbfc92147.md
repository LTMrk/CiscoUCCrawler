---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-1-elux-deploy-jvdi-b-deployment-installation-jvdi-elux-12-1-jvdi-b-d-7dbfc92147
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_1/elux/deploy/jvdi_b_deployment-installation-jvdi-elux-12-1/jvdi_b_deployment-installation-jvdi-elux-12-1_chapter_0101.html
retrieved_at: 2026-08-22T00:37:45.176120+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.1

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.1

Updated: July 18, 2018

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Verify the Platform Base Image Version

On the Start menu, select Control Panel .

Select  the Setup tab.

Select the General tab and look for the OS line.

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

Users  see a prompt to reconnect to their hosted virtual desktops (HVDs). After the users reconnect, Cisco Jabber or Cisco UC Integration™ for Microsoft Lync call control features do not work.

This problem can occur if the thin client loses network connectivity.

To resolve this issue, have the users exit Cisco Jabber or Cisco UC Integration™ for Microsoft Lync and disconnect from their HVDs. Next they can log back in to their HVDs and sign back in to Cisco Jabber or Cisco UC Integration™ for Microsoft Lync to restore call control.

## Call Is Lost After HVD Disconnection

Users receive a prompt to log back in to their hosted virtual desktops (HVD) during an active call, and the call drops. The
                              other party to the call has  no indication that the call has ended, except the line is silent.

This issue can occur if the  connection between the thin client and the  HVD drops, causing a temporary loss of registration
                              and call control.

To work around this issue, users can call the other party back. If the other party is not available, users can send an instant
                              message (IM).

## Problem Reporting Tool

The Problem Reporting Tool (PRT) is a small program,
                              which automatically runs if Cisco Jabber or Cisco UC Integration™ for Microsoft Lync encounters an unrecoverable error,
                              or unhandled exception. The tool collects logs from the thin client and  hosted virtual desktop and then creates a problem
                              report. The report  is a zip file that you
                              can send to the Cisco Technical Assistance Center (TAC), to provide
                              the necessary information to solve the problem.

If a user experiences an error that does not crash the
                              software, the user can run the PRT from the client Help menu: Help > Report a problem .

Users can generate a problem report from the Windows Start menu if Cisco UC Integration™ for Microsoft Lync is not running. To access the tool from outside the application, choose Start > All Programs > Cisco Systems, Inc > Report a problem .

Advise users to include a memory dump with the problem report if their Cisco Unified Communications application crashes.

We recommend that users provide a description of the circumstances that lead up to the error. For more detailed information
                              about how to run the PRT, see the Troubleshooting section in the applicable user guide.

Users must accept the privacy agreement to run the PRT.

| Step 1 | On the Start menu, select Control Panel . |
|---|---|
| Step 2 | Select  the Setup tab. |
| Step 3 | Select the General tab and look for the OS line. |

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

| Tip | Advise users to include a memory dump with the problem report if their Cisco Unified Communications application crashes. |
|---|---|

| Note | Users must accept the privacy agreement to run the PRT. |
|---|---|