---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-f79d8830a7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_security-guide_12_6_1/ucce_b_security-guide_12_6_1_chapter_01011.html
retrieved_at: 2026-08-16T14:44:43.804070+00:00
---

Security Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Security Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Remote Administration

## Chapter: Remote Administration

# Remote Administration

## Windows Remote
                        	 Desktop

Remote Desktop permits users to remotely run applications on Windows Server from a range of devices over virtually any network
                              connection. You can run Remote Desktop in either Application Server or Remote Administration modes. Unified ICM / Unified CCE only supports Remote Administration mode.

Note

- Use of any remote
                                             				administration applications can cause adverse effects during load.

- Use of remote administration
                                             				tools that employ encryption can affect server performance. The performance
                                             				level impact is tied to the level of encryption used. More encryption results
                                             				in more impact to the server performance.

Remote Desktop can
                              		  be used for remote administration of ICM-CCE-CCH server. The mstsc command
                              		  connects to the local console session.

Using the Remote
                              		  Desktop Console session, you can:

Run
                                    				Configuration Tools

Run Script
                                    				Editor

Note

Remote Desktop
                                                				  is not supported for software installation or upgrade.

Note

Administration
                                          			 Clients and Administration Workstations can support remote desktop access. But,
                                          			 only one user can access a client or workstation at a time. Unified CCE does
                                          			 not support simultaneous access by several users on the same client or
                                          			 workstation.

### Remote Desktop
                           	 Protocol

Communication between the server and the client uses original Remote Desktop Protocol (RDP) encryption. By default, encryption
                                 based on the maximum key strength supported by the client protects all data.

RDP is the preferred
                                 		  remote control protocol due to its security and low impact on performance.

Windows Server Terminal Services enable you to shadow a console session. Terminal Services can replace the need for pcAnywhere
                                 or VNC. To launch from the Windows Command Prompt, enter:

Remote Desktop
                                 		  Connection: mstsc
                                    			 /v:<server[:port]>

### Per-User Terminal
                           	 Services Settings

Use the following
                                 		  procedure to set up per-user terminal services settings for each user.

#### Procedure

Step 1

Using Active
                                          			 Directory Users and Computers, right-click a user and then select Properties .

Step 2

On the Terminal
                                          			 Services Profile tab, set a user's right to sign in to terminal server by
                                          			 checking the Allow
                                             				logon to terminal server check box. Optionally, create a profile
                                          			 and set a path to a terminal services home directory.

Step 3

On the Sessions
                                          			 tab, set session active and idle time outs.

Step 4

On the Remote
                                          			 Control tab, set whether administrators can remotely view and control a remote
                                          			 session and whether a user's permission is required.

## VNC

SSH Server allows
                              		  the use of VNC through an encrypted tunnel to create secure remote control
                              		  sessions. However, Cisco does not support this configuration. The performance
                              		  impact of running an SSH server has not been determined.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | Use of any remote
                                             				administration applications can cause adverse effects during load. Use of remote administration
                                             				tools that employ encryption can affect server performance. The performance
                                             				level impact is tied to the level of encryption used. More encryption results
                                             				in more impact to the server performance. |
|---|---|

| Note | Remote Desktop
                                                				  is not supported for software installation or upgrade. |
|---|---|

| Note | Administration
                                          			 Clients and Administration Workstations can support remote desktop access. But,
                                          			 only one user can access a client or workstation at a time. Unified CCE does
                                          			 not support simultaneous access by several users on the same client or
                                          			 workstation. |
|---|---|

| Step 1 | Using Active
                                          			 Directory Users and Computers, right-click a user and then select Properties . |
|---|---|
| Step 2 | On the Terminal
                                          			 Services Profile tab, set a user's right to sign in to terminal server by
                                          			 checking the Allow
                                             				logon to terminal server check box. Optionally, create a profile
                                          			 and set a path to a terminal services home directory. |
| Step 3 | On the Sessions
                                          			 tab, set session active and idle time outs. |
| Step 4 | On the Remote
                                          			 Control tab, set whether administrators can remotely view and control a remote
                                          			 session and whether a user's permission is required. |