---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--411c7129c3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-cisco-virtualized-voice-browser-serviceability-administration-guide/ccvp_b_1251-cisco-virtualized-voice-browser-serviceability-administration-guide_chapter_010.html
retrieved_at: 2026-08-21T16:34:36.926810+00:00
---

Cisco Virtualized Voice Browser Serviceability Administration Guide, Release 12.5(1)

# Cisco Virtualized Voice Browser Serviceability Administration Guide, Release 12.5(1)

Updated: February 2, 2020

Chapter: Alarms

## Chapter: Alarms

# Alarms

Cisco VVB Serviceability alarms provide information on runtime status and
                           		  the state of the system so that you can monitor the status and troubleshoot
                           		  problems that are associated with the system. Alarm information includes the
                           		  catalog, name, severity, explanation, recommended action, routing list, and
                           		  parameters.

You can
                           		  view alarm information by using the SysLog Viewer in Cisco Unified Real-Time
                           		  Monitoring Tool (RTMT).

Use the Alarm
                                       			 Definitions web page in Cisco Unified Serviceability to find information about
                                       			 an alarm message.

For a complete list of alarm definitions, see https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_troubleshoot_and_alerts.html.

For information on how to view alarm definitions, see the Cisco Unified Contact
                                                				  Center Express Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html .

## Alarm
                        	 Configuration

Use the Alarm Configuration
                              		  web page in Cisco VVB Serviceability to view and configure alarm server
                              		  settings for different VVB components.

Alarm Server Configuration is
                                          			 applicable for the VVB components such as VVB Administration and Engine.

The alarm
                              		  configuration submenu allows you to:

Enable or
                                    				disable sending of alarms to local or remote syslog server.

Configure alarm
                                    				event level for local or remote syslog server

Select Alarm > Configuration from the Cisco VVB Serviceability menu bar to access the Alarm Configuration web
                              		  page.

## Configure Alarm
                        	 Settings

The Alarm
                              		  Configuration page is used to view and update Cisco VVB Alarm
                              		  Configuration for local and remote syslogs.

From the Cisco
                                          				VVB Serviceability menu bar, choose Alarm and click Configuration .

The Alarm
                                          				Configuration web page opens and the following fields are displayed on the
                                          				Alarm Configuration web page, if configured on your Cisco VVB server:

Field

Description

Local Syslogs

Enable
                                                      							 Alarm

Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 local syslog.

Alarm
                                                      							 Event Level

Lists
                                                      							 the alarm severity level.

Remote Syslogs

Enable
                                                      							 Alarm

Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 remote syslog.

Alarm
                                                      							 Event Level

Lists
                                                      							 the alarm severity level.

Server
                                                      							 Name

IP
                                                      							 address or host name of the Syslog server to which system should send the alarm
                                                      							 messages. If you are using CiscoWorks, enter the IP address or the host name of
                                                      							 the CiscoWorks server.

To update the
                                       			 Alarm Event Level for local or remote syslogs, check the check box before
                                       			 Enable Alarm field.

Modify Alarm
                                       			 Event Level for the local or remote syslogs by selecting from the Alarm Event
                                       			 Level drop-down list. Modify the syslog server name in case of remote syslog.

Click Update icon that displays in the tool bar in the
                                       			 upper, left corner of the window or the Update button that displays at the bottom of the
                                       			 window to save your configuration. Click Clear to reset data to the previous values.

You should
                                                      				  activate logging only for
                                                      				  the purpose of debugging and remember to deactivate logging once the debugging session is complete.

## Alarm Configuration
                        	 Settings

Use the Alarm Configuration page to modify alarm
                              		  settings.

In the case of a High Availability deployment, the alarm configuration
                              		  changes are automatically propagated to the second node. If the second node
                              		  cannot be contacted, an alert message indicating that the update has failed on
                              		  the remote node is displayed.

Following table defines the options available on this page:

Setting

Description

Enable Alarm
                                       					 for Local Syslogs

The SysLog
                                       					 viewer serves as the alarm destination. The program logs errors in the
                                       					 Application Logs within SysLog Viewer and provides a description of the alarm
                                       					 and a recommended action. You can access the SysLog Viewer from the Cisco
                                       					 Unified Real-Time Monitoring Tool.

Enable Alarm
                                       					 for Remote Syslogs

The Syslog
                                       					 file serves as the alarm destination. Check this check box to enable the Syslog
                                       					 messages to be stored on a Syslog server and to specify the Syslog server name.

Alarm Event
                                       					 Level

Alarm event
                                       					 level messages range from severity 0 (most severe) to severity 7 (least severe)
                                       					 description of which is mentioned below. When you choose a severity level, all
                                       					 messages of that severity level and higher are sent.

For example,
                                       					 if you choose ERROR_ALARM (Severity 3), all messages of severity 3, severity 2,
                                       					 severity 1, and severity 0 are sent. The default is "INFORMATIONAL_ALARM (Severity 6)" , which will send messages
                                       					 of all severity levels starting from 6 to severity level 0.

| Note | Use the Alarm
                                       			 Definitions web page in Cisco Unified Serviceability to find information about
                                       			 an alarm message. For a complete list of alarm definitions, see https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_troubleshoot_and_alerts.html. For information on how to view alarm definitions, see the Cisco Unified Contact
                                                				  Center Express Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html . |
|---|---|

| Note | Alarm Server Configuration is
                                          			 applicable for the VVB components such as VVB Administration and Engine. |
|---|---|

| Step 1 | From the Cisco
                                          				VVB Serviceability menu bar, choose Alarm and click Configuration . The Alarm
                                          				Configuration web page opens and the following fields are displayed on the
                                          				Alarm Configuration web page, if configured on your Cisco VVB server: Field Description Local Syslogs Enable
                                                      							 Alarm Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 local syslog. Alarm
                                                      							 Event Level Lists
                                                      							 the alarm severity level. Remote Syslogs Enable
                                                      							 Alarm Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 remote syslog. Alarm
                                                      							 Event Level Lists
                                                      							 the alarm severity level. Server
                                                      							 Name IP
                                                      							 address or host name of the Syslog server to which system should send the alarm
                                                      							 messages. If you are using CiscoWorks, enter the IP address or the host name of
                                                      							 the CiscoWorks server. | Field | Description | Local Syslogs | Enable
                                                      							 Alarm | Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 local syslog. | Alarm
                                                      							 Event Level | Lists
                                                      							 the alarm severity level. | Remote Syslogs | Enable
                                                      							 Alarm | Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 remote syslog. | Alarm
                                                      							 Event Level | Lists
                                                      							 the alarm severity level. | Server
                                                      							 Name | IP
                                                      							 address or host name of the Syslog server to which system should send the alarm
                                                      							 messages. If you are using CiscoWorks, enter the IP address or the host name of
                                                      							 the CiscoWorks server. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Local Syslogs |
| Enable
                                                      							 Alarm | Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 local syslog. |
| Alarm
                                                      							 Event Level | Lists
                                                      							 the alarm severity level. |
| Remote Syslogs |
| Enable
                                                      							 Alarm | Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 remote syslog. |
| Alarm
                                                      							 Event Level | Lists
                                                      							 the alarm severity level. |
| Server
                                                      							 Name | IP
                                                      							 address or host name of the Syslog server to which system should send the alarm
                                                      							 messages. If you are using CiscoWorks, enter the IP address or the host name of
                                                      							 the CiscoWorks server. |
| Step 2 | To update the
                                       			 Alarm Event Level for local or remote syslogs, check the check box before
                                       			 Enable Alarm field. |
| Step 3 | Modify Alarm
                                       			 Event Level for the local or remote syslogs by selecting from the Alarm Event
                                       			 Level drop-down list. Modify the syslog server name in case of remote syslog. |
| Step 4 | Click Update icon that displays in the tool bar in the
                                       			 upper, left corner of the window or the Update button that displays at the bottom of the
                                       			 window to save your configuration. Click Clear to reset data to the previous values. Caution You should
                                                      				  activate logging only for
                                                      				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. | Caution | You should
                                                      				  activate logging only for
                                                      				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. |
| Caution | You should
                                                      				  activate logging only for
                                                      				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. |

| Field | Description |
|---|---|
| Local Syslogs |
| Enable
                                                      							 Alarm | Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 local syslog. |
| Alarm
                                                      							 Event Level | Lists
                                                      							 the alarm severity level. |
| Remote Syslogs |
| Enable
                                                      							 Alarm | Use
                                                      							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                      							 remote syslog. |
| Alarm
                                                      							 Event Level | Lists
                                                      							 the alarm severity level. |
| Server
                                                      							 Name | IP
                                                      							 address or host name of the Syslog server to which system should send the alarm
                                                      							 messages. If you are using CiscoWorks, enter the IP address or the host name of
                                                      							 the CiscoWorks server. |

| Caution | You should
                                                      				  activate logging only for
                                                      				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. |
|---|---|

| Setting | Description |
|---|---|
| Enable Alarm
                                       					 for Local Syslogs | The SysLog
                                       					 viewer serves as the alarm destination. The program logs errors in the
                                       					 Application Logs within SysLog Viewer and provides a description of the alarm
                                       					 and a recommended action. You can access the SysLog Viewer from the Cisco
                                       					 Unified Real-Time Monitoring Tool. |
| Enable Alarm
                                       					 for Remote Syslogs | The Syslog
                                       					 file serves as the alarm destination. Check this check box to enable the Syslog
                                       					 messages to be stored on a Syslog server and to specify the Syslog server name. |
| Alarm Event
                                       					 Level | Alarm event
                                       					 level messages range from severity 0 (most severe) to severity 7 (least severe)
                                       					 description of which is mentioned below. When you choose a severity level, all
                                       					 messages of that severity level and higher are sent. For example,
                                       					 if you choose ERROR_ALARM (Severity 3), all messages of severity 3, severity 2,
                                       					 severity 1, and severity 0 are sent. The default is "INFORMATIONAL_ALARM (Severity 6)" , which will send messages
                                       					 of all severity levels starting from 6 to severity level 0. You can
                                       					 choose one of the following alarm event level options from the drop-down list
                                       					 box: Emergency This
                                             						  level designates system as unusable. Alert This
                                             						  level indicates that immediate action is needed. Critical The
                                             						  system detects a critical condition. Error This
                                             						  level signifies an error condition exists. Warning This
                                             						  level indicates that a warning condition is detected. Notice This
                                             						  level designates a normal but significant condition. Informational This
                                             						  level designates information messages only. Debug This
                                             						  level designates detailed event information that Cisco TAC engineers use for
                                             						  debugging. |