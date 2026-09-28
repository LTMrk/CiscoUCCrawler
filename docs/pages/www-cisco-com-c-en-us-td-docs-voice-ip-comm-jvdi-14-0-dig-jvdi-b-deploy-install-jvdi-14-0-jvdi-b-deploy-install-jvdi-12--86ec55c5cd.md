---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-0-dig-jvdi-b-deploy-install-jvdi-14-0-jvdi-b-deploy-install-jvdi-12--86ec55c5cd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_0/dig/jvdi_b_deploy-install-jvdi-14-0/jvdi_b_deploy-install-jvdi-12-9_chapter_0111.html
retrieved_at: 2026-08-22T00:31:36.248690+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 14.0

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 14.0

Updated: March 25, 2021

Chapter: Troubleshooting—HP Thin Pro and Ubuntu

## Chapter: Troubleshooting—HP Thin Pro and Ubuntu

# Troubleshooting—HP Thin Pro and Ubuntu

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

| Step 1 | Use Secure Shell (SSH) to connect to the thin client. |
|---|---|
| Step 2 | Search the running programs for vxc . ps -ef \| grep -r vxc You should see the following lines: admin@LWT44d3ca76ba19:~> ps -ef \|grep -r vxc

thinuser 6536 1 0 Mar14 ? 00:07:43 /bin/bash /usr/bin/pidrun.sh -c run_vxc.sh -a -m -o /var/log/cisco/vxcConsole.log -e /var/log/cisco/vxcError.log

thinuser 6538 6536 0 Mar14 ? 00:00:00 /bin/bash /usr/bin/run_vxc.sh -m

thinuser 6547 6538 8 Mar14 ? 13:02:16 vxc -m

admin 31576 31303 0 11:05 pts/0 00:00:00 grep -r vxc

admin@LWT44d3ca76ba19:~> |