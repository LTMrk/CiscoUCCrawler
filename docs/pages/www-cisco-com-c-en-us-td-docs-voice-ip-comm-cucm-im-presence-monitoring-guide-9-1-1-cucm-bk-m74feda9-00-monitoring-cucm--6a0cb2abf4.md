---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-monitoring-guide-9-1-1-cucm-bk-m74feda9-00-monitoring-cucm--6a0cb2abf4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/monitoring_guide/9_1_1/CUCM_BK_M74FEDA9_00_monitoring-cucm-presence-guide-91/CUCM_BK_M74FEDA9_00_monitoring-cucm-presence-guide-91_chapter_01.html
retrieved_at: 2026-08-21T01:27:19.882213+00:00
---

Monitoring Cisco Unified Communications Manager IM and Presence, Release 9.1(1)

# Monitoring Cisco Unified Communications Manager IM and Presence, Release 9.1(1)

Chapter: Alerts and alarms

## Chapter: Alerts and alarms

# Alerts and alarms

- Monitor alerts using Cisco Prime Unified Operations Manager

- Monitor alerts using Unified RTMT

- List of alerts

## Monitor alerts using Cisco Prime Unified Operations Manager

Cisco Prime Unified Operations Manager (Unified Operations Manager) 8.6 is capable of raising system alerts only for IM and Presence Service . Unified Operations Manager 8.7 and later include a custom syslog feature. This feature makes it possible to add syslog messages that are not in the Unified Operations Manager default list. These alerts will be raised based on their Cisco Unified Real-Time Monitoring Tool (Unified RTMT) default thresholds.

Complete the following procedure to monitor alerts using Unified Operations Manager.

- On the IM and Presence Administration GUI navigate to System > Enterprise Parameters .

- For Remote Syslog Server Name , add your Unified Operations Manager node name or IP address and click Save .

- On Unified Operations Manager, navigate to Administration > System Settings > Syslog Support and click Add .

Here you can specify which IM and Presence alerts you want Unified Operations Manager to monitor.

Any of the alerts in this document should be considered of critical severity.

## Monitor alerts using Unified RTMT

You can monitor both system and IM and Presence-specific alerts for an IM and Presence server using Cisco Unified Real-Time Monitoring Tool.

- Choose Tools > Alert Central .

- Right-click on each alert and choose Set alert > Properties to view alert descriptions, change default thresholds, and configure email notifications.

- Choose Tools > System summary .

## List of alerts

Alert messages are generated to notify administrators when a predefined condition is met, such as when an activated service goes from up to down. Cisco recommends that you monitor the following IM and Presence, Unified Operations Manager, and System alerts.

- IM and Presence Service alerts

- Cisco Prime Unified Operations Manager Alerts

- System Alerts

### IM and Presence Service alerts

The following is a list of common IM and Presence Service alerts.

#### CTIGWProviderDown

#### CTIGWProviderFailedToOpen

#### DbmonQueueWorkerExistWithError

This alert indicates that the Cisco Sync Agent service is no longer processing change notifications from the Cisco Unified Communications Manager cluster. This error can cause the data on the IM and Presence Service cluster to get out of sync with the data on the Cisco Unified Communications Manager cluster.

#### ESPSharedMemAllocFailed

#### ESPSharedMemCreateFailed

#### ESPSharedMemSetPermFailed

#### ESPStopped

#### ICSACertificateFingerPrintMisMatch

#### ICSACertificateValidationFailure

#### InterclusterSyncAgentAXLConnectionFailed

#### InterclusterSyncAgentFailedToCleanUpPeer

#### InterclusterSyncAgentFailedToSendCN

#### InterclusterSyncAgentPeerDuplicate

#### InterclusterSyncAgentPeerSyncFailed

#### NotInCucmAppServerListError

#### PEConfigNotificationFailure

#### PEDatabaseError

#### PEIDSQueryError

#### PEIDSSubscribeError

#### PEIDStoIMDBDatabaseSyncError

This alert indicates that synchronization between the IM and Presence database and the Cisco Presence Engine and a database service has failed (Cisco Login Datastore, Cisco Route Datastore, Cisco Presence Datastore, and Cisco SIP Registration Datastore).

Restart the Cisco Presence Engine service when convenient. See associated error message and log files and consult Cisco TAC if the problem persists.

#### PEOamInitialConfigFileError

#### PEOamInvalidInitialConfigFile

#### PEOamConfigFileError

#### PEPeerNodeFailure

#### PESipSgHostUnavailable

#### PESipSocketBindFailure

#### SRMFailed

#### SRMFailover

#### SyncAgentAXLConnectionFailed

#### SyncAgentCucmDbmonConnectionFailed

This alert indicates that the Cisco Sync Agent service lost the connection to the Cisco Database Layer Monitor service. This error can cause the data on the IM and Presence Service cluster to get out of sync with the data on the Cisco Unified Communications Manager cluster.

#### XCPConfigMgrConfigurationFailure

This alert indicates that the Cisco XCP Config Manager failed to successfully update XCP configuration.

See the Cisco XCP Config Manager logs for the root cause. Contact Cisco TAC for assistance.

#### XCPConfigMgrHostNameResolutionFailed

#### XCPConfigMgrJabberRestartRequired

This alert indicates that the Cisco XCP Config Manager has regenerated XCP XML files after system halt due to buffer size. The Cisco XCP Router must now be restarted to apply changes.

When it is convenient to do so, restart the Cisco XCP Router.

#### XCPConfigMgrQueueAtCriticalLevel

This alert indicates that the Cisco XCP Config Manager buffer has reached critical levels. The system will halt until configuration stabilizes, and then it will regenerate all files. The Cisco XCP Router will need to be restarted to apply these changes.

Restart the Cisco XCP Router after the alarm is sent that indicates that configuration has been regenerated successfully.

#### XCPConfigMgrR2RPasswordEncryptionFailed

This alert indicates that the Cisco XCP Config Manager was unable to encrypt the password that is associated with an Inter-cluster Router-to-Router configuration.

When it is convenient to do so, restart the Cisco XCP Config Manager and then restart the Cisco XCP Router.

#### XcpSIPGWStackResourceError

This alert indicates that the maximum supported concurrent SIP Federation subscriptions or SIP Federation IM sessions has been reached, and the Cisco XCP SIP Federation Connection Manager does not have the resources that are required to handle any addition subscriptions or IM sessions.

Increase the Pre-allocated SIP stack memory Service Parameter for the Cisco XCP SIP Federation Connection Manager. Note: If you are changing this setting, make sure that you have the memory available. If you do not have enough memory, you may have reached the limit of your hardware capability.

### Cisco Prime Unified Operations Manager Alerts

The following is a list of common Unified Operations Manager alerts.

Unified Operations Manager maintains its own set of alerts that are related to IM and Presence Service . Some of these mirror existing native alerts. For example, the native alert LowAvailableVirtualMemory and the Unified Operations Manager alert InsufficientFreeVirtualMemory both alert on the same item and are based on the same data, yet the default threshold is different on Unified Operations Manager (< 15%) and Unified RTMT (< 25%).

#### DevicePartiallyMonitored

- Check for any HTTP communication or network failures from the Operations Manager to the device.

- Check whether Cisco RIS Data Collector network service is running on the device. This service should be running in all the nodes of the cluster.

#### HighUtilization

#### HTTPInaccessible

- The Web Services for a server in the cluster is down.

- The credentials (HTTP username, password) for at least one of the running Web Services were not found or are incorrect.

#### InsufficientFreeVirtualMemory

#### ServerUnreachable

#### Unresponsive

- On a system: ICMP ping requests and SNMP queries to the device timeout receive no response.

- On an SNMP Agent: Device ICMP ping requests are successful, but SNMP requests time out with no response.

A system might also be reported as unresponsive if the only link (for example, an interface) to the system goes down. Unified Operations Manager performs root cause analysis for any unresponsive events.

If Unified Operations Manager receives a device unresponsive event, it will clear any interface unresponsive events from that device until the device is recognized as responsive.

### System Alerts

The following is a list of common System alerts.

#### CiscoDRFFailure

#### CpuPegging

The most common reason for this alert is that one or more processes are using excessive CPU space. The alert has information about which process is using the most CPU. After the process is identified, you may want to take action, which could include restarting the process. You can also verify the current CPU usage of the problem process using the Process tool.

It is helpful to check the trace setting for that process. Using the detailed/debug trace level is known to take up excessive CPU space. If so, you may want to take more drastic measures, such as stopping nonessential services or scheduling a restart of IM and Presence Server during off hours.

#### CriticalServiceDown

This alert is generated when one of the critical services (any of the services in the Critical Services tool in Unified RTMT) is not running. The problem could be due to someone manually stopping the service. If you intend to stop the service for a long period of time, you should deactivate it on the Serviceability GUI: Cisco Unified Serviceability > Tools > Service Activation .

Identify which services are not running. You can start the service manually from the Serviceability GUI: Cisco Unified Serviceability > Tools > Feature Services/Network Services .

Also, check to see whether there are any core files. Download the core files, if any, as well as service trace files.

#### HardwareFailure

#### LogPartitionHighWaterMarkExceeded

Note that after the log partition disk usage goes above the high water mark threshold, Cisco Log Partition Monitoring Tool (LPM) starts deleting files to put log partition disk usage under the low water mark threshold. Because LPM may delete the trace/log/core dump files you want to keep, it is very important to act when you receive a LogPartitionLowWaterMarkExceeded alert. You can use Trace and Log Central (TLC) In Unified RTMT to download files and delete them from the server.

#### LogPartitionLowWaterMarkExceeded

#### LowActivePartitionAvailableDiskSpace

- Administration GUI does not operate correctly.

- Cisco Unified Communications Manager Bulk Administration Tool (BAT) does not operate correctly.

- Unified RTMT does not operate correctly.

Because there are no user-manageable files in Active Partition, check the alert threshold. If the alert threshold is at the Cisco default, contact Cisco TAC for guidance.

#### LowAvailableVirtualMemory

#### LowSwapPartitionAvailableDiskSpace

#### ServerDown

#### SystemVersionMismatched

This alert occurs when there is a mismatch in the system version among all servers in the cluster. This alert is generated by monitoring the syslog messages that are received from the IM and Presence server.

#### TotalProcessesAndThreadsExceededThreshold

| Step 1 | First on IM and Presence. On the IM and Presence Administration GUI navigate to System > Enterprise Parameters . For Remote Syslog Server Name , add your Unified Operations Manager node name or IP address and click Save . |
|---|---|
| Step 2 | Then on Unified Operations Manager. On Unified Operations Manager, navigate to Administration > System Settings > Syslog Support and click Add . Specify the name of the alert you wish to monitor in Syslog Name . Here you can specify which IM and Presence alerts you want Unified Operations Manager to monitor. Note Any of the alerts in this document should be considered of critical severity. Figure 1. Syslog Support window | Note | Any of the alerts in this document should be considered of critical severity. |
| Note | Any of the alerts in this document should be considered of critical severity. |

| Note | Any of the alerts in this document should be considered of critical severity. |
|---|---|

| Step 1 | To monitor both System and IM and Presence Service -specific alerts on IM and Presence Service Server. Choose Tools > Alert Central . Right-click on each alert and choose Set alert > Properties to view alert descriptions, change default thresholds, and configure email notifications. |
|---|---|
| Step 2 | To view the recent alarm history on the IM and Presence Service Server. Choose Tools > System summary . Figure 2. Real Time Monitoring Tool window |

| Note | Unified Operations Manager maintains its own set of alerts that are related to IM and Presence Service . Some of these mirror existing native alerts. For example, the native alert LowAvailableVirtualMemory and the Unified Operations Manager alert InsufficientFreeVirtualMemory both alert on the same item and are based on the same data, yet the default threshold is different on Unified Operations Manager (< 15%) and Unified RTMT (< 25%). |
|---|---|