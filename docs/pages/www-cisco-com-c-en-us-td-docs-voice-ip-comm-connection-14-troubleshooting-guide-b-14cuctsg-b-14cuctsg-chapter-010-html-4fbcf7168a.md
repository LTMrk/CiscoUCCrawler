---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-010-html-4fbcf7168a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_010.html
retrieved_at: 2026-08-17T02:16:30.103584+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting Cisco Unity Connection Deployments

## Chapter: Troubleshooting Cisco Unity Connection Deployments

# Troubleshooting Cisco Unity Connection Deployments

## Troubleshooting
                        	 Installation Issues

If you receive an error during installation of Cisco Unity
                           		Connection, do the following:

Check if you are meeting the platform requirements mentioned in Cisco Unity Connection 14 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

Make sure that you have met the software requirements mentioned in System Requirements for Cisco Unity Connection Release
                                 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/requirements/b_14cucsysreqs.html .

Check if the problem is because of SELinux mode on publisher
                                 			 server during the installation of a subscriber server. See Troubleshooting
                                    				SELinux Issues section.

Review install logs to diagnose the problem. You can use CLI
                                 			 command or RTMT to collect installation logs. For more information on
                                 			 collecting logs from CLI command, see “file get” section of the “File Commands”
                                 			 chapter of the applicable Command Line Interface Reference Guide for Cisco
                                 			 Unified Communications Solutions. For information on collecting logs from RTMT,
                                 			 see the “Collect Installation Logs” section of the “Traces and Logs” chapter of
                                 			 the applicable Cisco Unified Real-Time Monitoring Tool Administration Guide.
                                 			 You can locate both the guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

If you receive any error while installing the subscriber server,
                                             				you can review the install logs of the subscriber server to troubleshoot the
                                             				problem.

Contact Cisco TAC if you are not able to resolve the issue.

## Troubleshooting
                        	 Upgrade Issues

Following are the issues that you might face while upgrading
                           		from one version of Unity Connection to another:

Switch Version Failures: To troubleshoot the switch version
                                 			 failures as a part of upgrade from Unity Connection 8.6 to a later version,
                                 			 verify whether the problem is caused by SELinux security policies. For more
                                 			 information, see the Troubleshooting
                                    				SELinux Issues section. You can also review install logs for upgrade
                                 			 failure. For more information on how to collect install logs, see applicable
                                 			 Command Line Interface Reference Guide for Cisco Unified Communications
                                 			 Solutions and Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Make sure to run pre upgrade CLI to verify if the system is good
                                             				to upgrade.

### Troubleshooting Locale Issues After Upgrade

If you face any problem related to locale after
                                 		  upgrade, do the following

Step 1

Check if the locale is installed or not
                                          			 using the show cuc locales CLI command.

Step 2

In Cisco Unity Connection Administration,
                                          			 navigate to Users > Users and select a user for whom locale is not
                                          			 displaying correctly.

Step 3

Verify that the correct language is selected
                                          			 from the language drop-down list.

Step 4

Click Save to apply the settings.

## Troubleshooting SELinux Issues

Step 1

To check the status of SELinux on Unity
                                       			 Connection server, run the Command Line Interface (CLI) command utils os secure status.

Step 2

If SELinux is in Enforcing mode, run the CLI
                                       			 command utils os secure permissive to put the Unity Connection server in
                                       			 Permissive mode.

Step 3

Try to reproduce the symptom with SELinux in
                                       			 permissive mode. If the symptom is reproducible, it is not caused by SELinux.

Step 4

If the symptom is not reproducible, do the
                                       			 following steps to gather logs before you contact Cisco TAC:

Create your test directory on sftp
                                             				  server to save the audit log diagnostic file at that location.

Put Unity Connection server in Enforcing
                                             				  mode by running the CLI command utils os secure enforce.

Try to create the symptom again.

Create the audit logs diagnostic file by
                                             				  running the CLI command utils create report security. This command creates a
                                             				  diagnostic file “security-diagnostics.tar.gz”. Copy the diagnostic file to sftp
                                             				  directory created in step 4(a) by running the CLI command file get activelog
                                             				  syslog/security-diagnostics.tar.gz.

Step 5

Contact Cisco TAC.

| Note | If you receive any error while installing the subscriber server,
                                             				you can review the install logs of the subscriber server to troubleshoot the
                                             				problem. |
|---|---|

| Note | Make sure to run pre upgrade CLI to verify if the system is good
                                             				to upgrade. |
|---|---|

| Step 1 | Check if the locale is installed or not
                                          			 using the show cuc locales CLI command. |
|---|---|
| Step 2 | In Cisco Unity Connection Administration,
                                          			 navigate to Users > Users and select a user for whom locale is not
                                          			 displaying correctly. |
| Step 3 | Verify that the correct language is selected
                                          			 from the language drop-down list. |
| Step 4 | Click Save to apply the settings. |

| Step 1 | To check the status of SELinux on Unity
                                       			 Connection server, run the Command Line Interface (CLI) command utils os secure status. |
|---|---|
| Step 2 | If SELinux is in Enforcing mode, run the CLI
                                       			 command utils os secure permissive to put the Unity Connection server in
                                       			 Permissive mode. |
| Step 3 | Try to reproduce the symptom with SELinux in
                                       			 permissive mode. If the symptom is reproducible, it is not caused by SELinux. |
| Step 4 | If the symptom is not reproducible, do the
                                       			 following steps to gather logs before you contact Cisco TAC: Create your test directory on sftp
                                             				  server to save the audit log diagnostic file at that location. Put Unity Connection server in Enforcing
                                             				  mode by running the CLI command utils os secure enforce. Try to create the symptom again. Create the audit logs diagnostic file by
                                             				  running the CLI command utils create report security. This command creates a
                                             				  diagnostic file “security-diagnostics.tar.gz”. Copy the diagnostic file to sftp
                                             				  directory created in step 4(a) by running the CLI command file get activelog
                                             				  syslog/security-diagnostics.tar.gz. |
| Step 5 | Contact Cisco TAC. |