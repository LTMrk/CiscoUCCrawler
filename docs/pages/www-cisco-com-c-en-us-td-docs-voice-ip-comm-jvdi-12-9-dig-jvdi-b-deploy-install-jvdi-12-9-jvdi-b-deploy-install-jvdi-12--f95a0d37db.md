---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-9-dig-jvdi-b-deploy-install-jvdi-12-9-jvdi-b-deploy-install-jvdi-12--f95a0d37db
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_9/dig/jvdi_b_deploy-install-jvdi-12-9/jvdi_b_deploy-install-jvdi-12-9_chapter_01000.html
retrieved_at: 2026-08-22T00:32:21.968772+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.9

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.9

Updated: July 8, 2020

Chapter: Troubleshooting—Unicon eLux

## Chapter: Troubleshooting—Unicon eLux

# Troubleshooting—Unicon eLux

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

| Step 1 | On the Start menu, select Control Panel . |
|---|---|
| Step 2 | Select  the Setup tab. |
| Step 3 | Select the General tab and look for the OS line. |

| Step 1 | On the Start menu, select Control Panel . |
|---|---|
| Step 2 | Select the Setup tab. |
| Step 3 | Select the General tab. |
| Step 4 | Scroll down the list of packages and look for Cisco JVDI Client . The add-on versions appear in the same line. |

| Step 1 | Use Secure Shell (SSH) to connect to the thin client. |
|---|---|
| Step 2 | Search the running programs for vxc . ps -ef \| grep -r vxc You should see the following lines: admin@LWT44d3ca76ba19:~> ps -ef \|grep -r vxc

thinuser 6536 1 0 Mar14 ? 00:07:43 /bin/bash /usr/bin/pidrun.sh -c run_vxc.sh -a -m -o /var/log/cisco/vxcConsole.log -e /var/log/cisco/vxcError.log

thinuser 6538 6536 0 Mar14 ? 00:00:00 /bin/bash /usr/bin/run_vxc.sh -m

thinuser 6547 6538 8 Mar14 ? 13:02:16 vxc -m

admin 31576 31303 0 11:05 pts/0 00:00:00 grep -r vxc

admin@LWT44d3ca76ba19:~> |