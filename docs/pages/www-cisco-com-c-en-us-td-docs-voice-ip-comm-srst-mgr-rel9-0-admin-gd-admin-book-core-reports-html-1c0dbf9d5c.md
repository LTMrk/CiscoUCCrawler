---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-core-reports-html-1c0dbf9d5c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/core_reports.html
retrieved_at: 2026-08-21T23:39:38.356084+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Viewing Reports

## Chapter: Viewing Reports

## Viewing the Alert History Report

The Alert History Report displays a list of all system alert messages that have occurred on the system. The alerts include critical, error, warning, and informational messages. The messages are grouped by alert level, and appear in chronological order. You can filter the alerts according to alert level by selecting specific check boxes at the top of the report and clicking Go .

Step 1 Select Reports > Alert History .

The Alert History Report contains the following fields:

- Level—Alert level. Can be critical, error, warning, or informational.

- System—The system originating the alert message.

- Date and Time—Date and time when the system created the alert.

- Description—Description of the alert. See System Alerts for a list of all the alerts.

- Help—Additional information about the alert. To see the details, click details .

Step 2 To delete all of the alerts, click Delete Alert History .

Related Topics

## System Alerts

The following tables list all the alerts:

Table 11 System Alerts – Warnings

CcmFailoverToSecondary

The primary central call agent was unavailable for provisioning, but the secondary central call agent was successfully utilized.

CcmUnreachableForProvisioning

Cisco Unified SRST Manager was unable to pull provisioning information from the configured telephony service server because it could not be reached on the network. Typically telephony service is provided by a central call agent like Cisco Unified Communications Manager.

ProvisioningCycleSuspended

Cisco Unified SRST Manager has suspended the process of provisioning remote sites based on the central site configuration.

SiteProvisioningSkipped

Provisioning for a site was skipped due to incomplete configuration.

SrstCSSNameConflictFound

A name conflict was found for Cisco Unified Communications Manager Calling Search Space names when applied to the Cisco Unified Communications Manager Express class of restriction lists.

SrstDialPeerMatchingToCUCMRoutePatternNotFound

Unable to find a matching dial peer to a Cisco Unified Communications Manager route pattern.

SrstLongHuntGroupChainFound

Hunt group configuration: Unable to configure long hunt pilot.

SrstMultipleTimeZonesFound

Multiple time zones for a site were found on the central Cisco Unified Communications Manager.

SrstPartitionNameConflictFound

A name conflict was found for Cisco Unified Communications Manager partition names when applied to the Cisco Unified Communications Manager Express class of restriction names.

SrstTimeBasedPartitionsDayOfMonthLimitReached

After hours configuration: Cisco Unified SRST Manager was unable to add more day of month schedules because the Cisco Unified Communications Manager Express time-based-partitions day of month limit has been reached.

SrstWarning

Cisco Unified SRST Manager has indicated a warning. Refer to the log files for details about the warning.

TlsCredentialExpired

A TLS credential on Cisco Unified SRST Manager has expired.

UmgProvisioningWarnings

Provisioning of the secondary Cisco Unified SRST Manager has some anomalies.

Note The details link for this alert contains a list of all the provisioning errors seen for the Cisco Unified SRST Manager aggregated into a single alert.

UmgUnreachableForProvisioning

Cisco Unified SRST Manager was unable to provision a secondary Cisco Unified SRST Manager because it was unable to create a connection to the device.

Possible causes for the failure include Cisco Unified SRST Manager TLS configuration, router line VTY configuration, or a network problem.

Table 12 System Alerts – Errors

CcmGlobalDataRetrievalFailure

Cisco Unified SRST Manager was unable to update the global Cisco Unified SRST data from Cisco Unified Communications Manager. See the logs for more details.

CcmProvisiningFail

Cisco Unified SRST Manager could not provision because of a communications problem with the central call agent .

CcmProvisioningFailAuth

Cisco Unified SRST Manager could not provision because of bad central call agent AXL credentials. Update the AXL username and password for the central call agent and try again.

CcmProvisioningFailTls

Cisco Unified SRST Manager could not provision because of a bad central call agent public TLS certificate. Add the central call agent's TLS certificate to Cisco Unified SRST Manager and try again.

CcmSrstReferenceDataRetrievalFailure

Cisco Unified SRST Manager was unable to update site-specific Cisco Unified SRST data from Cisco Unified Communications Manager. See the logs for more details.

LocalhostDnsFailure

The Cisco Unified SRST Manager host cannot be resolved by the DNS server.

SrstAfterHourNoExemptFailure

Unable to get After Hours no Exempt for the specified site. See the logs for more details.

SrstAfterHoursBlockPatternFailed

The after-hours configuration was unable to configure some after hours block patterns. See the logs for more details.

SrstAfterHoursConfigurationFailed

The after-hours configuration failed. See the logs for failure details.

SrstAfterHoursCreationFailed

Cisco Unified SRST Manager was unable to create after hours. See the logs for more details.

SrstCallParkConfigurationFailed

One or more errors were seen while trying to configure call park entries. See the logs for more details.

SrstCcpDiscoveryFailure

Cisco Unified SRST Manager was unable to execute configuration discovery for the Cisco Unified SRST site. See the logs for more details.

SrstCMENotSupportedFailure

Cisco Unified Communications Manager Express voice is not supported on the router. Check the router version and image.

SrstCreateDnFailure

Cisco Unified SRST Manager was unable to create the DN in Cisco Unified SRST. See the logs for more details.

SrstCreateExternalCallRoutingFailure

Cisco Unified SRST Manager was unable to create the external call routing configuration in Cisco Unified SRST.

SrstCreatePhoneFailure

Cisco Unified SRST Manager was unable to create a phone in Cisco Unified SRST. See the logs for more details.

SrstCreateSoftkeyTemplateFailure

Cisco Unified SRST Manager was unable to create a softkey template in Cisco Unified SRST. See the logs for more details.

SrstCreateSpeedDialFailure

Cisco Unified SRST Manager was unable to create speed dial in Cisco Unified SRST. See the logs for more details.

SrstCreateTranslationRulesFailure

Cisco Unified SRST Manager was unable to create translation rules in Cisco Unified SRST.

SrstCritical

Cisco Unified SRST Manager has experienced a critical error. Refer to the log files for details about the error.

SrstDeleteDnFailure

Cisco Unified SRST Manager was unable to delete the DN in Cisco Unified SRST. See the logs for more details.

SrstDeleteExternalCallRoutingFailure

Cisco Unified SRST Manager was unable to delete the external call routing configuration in Cisco Unified SRST.

SrstDeletePhoneFailure

Cisco Unified SRST Manager was unable to delete a phone in Cisco Unified SRST. See the logs for more details.

SrstDeleteSokftKeyTemplateExceeded

The maximum number of configured softkey templates was exceeded.

SrstDeleteSokftKeyTemplateFailure

Cisco Unified SRST Manager was unable to delete the softkey template in Cisco Unified SRST. See the logs for more details.

SrstDeleteSpeedDialFailure

Cisco Unified SRST Manager was unable to delete speed dial in Cisco Unified SRST. See the logs for more details.

SrstDeleteTranslationRulesFailure

Cisco Unified SRST Manager was unable to delete translation rules in Cisco Unified SRST.

SrstError

Cisco Unified SRST Manager has experienced an error. Refer to the log files for details about the error.

SrstFetchingCcmSRSTConfigurationFailure

Cisco Unified SRST Manager was unable to fetch the Cisco Unified SRST configuration from Cisco Unified Communications Manager. See the logs for more details.

SrstFetchingHardwareConfigurationFailure

Cisco Unified SRST Manager was unable to provision the site because it was unable to get hardware information for the site. See the logs for more details.

SrstFetchingMappingConfigurationFailure

Cisco Unified SRST Manager was unable to fetch the Cisco Unified SRST mapping configuration from the database. See the logs for more details.

SrstFetchingPlatformInformationFailure

Cisco Unified SRST Manager was unable to provision the site because it was unable to get hardware platform information based on the hardware. Ensure that this hardware is supported.

SrstFetchingSRSTConfigurationFailure

Cisco Unified SRST Manager was unable to fetch the Cisco Unified SRST configuration from the router. See the logs for more details.

SrstFetchingTelephonyConfigurationFailure

Cisco Unified SRST Manager was unable to fetch the telephony configuration from the router. See the logs for more details.

SrstFetchTranslationRulesFailure

Cisco Unified SRST Manager was unable to fetch translation rules from Cisco Unified SRST.

SrstGettingCSSContainingPartitionFailed

Cisco Unified SRST Manager was unable to get CSS Containing Partition.

See the logs for more details.

SrstHuntGroupConfigurationFailed

The hunt groups configuration failed. See the logs for failure details.

SrstHuntGroupLongPilotFound

The hunt group configuration was unable to configure a long-chained hunt pilot.

SrstInvalidDateFormatFound

Cisco Unified SRST Manager was unable to provision the date format because an invalid or unsupported date format was found.

SrstInvalidTimeZoneFound

Cisco Unified SRST Manager was unable to provision the time zone because an invalid or unsupported time zone was found.

SrstMaxConfiguredCoRExceeded

The maximum configured class of restrictions was exceeded.

SrstMaxConfiguredPhoneExceeded

The number of maximum configured phones was exceeded.

SrstMaxConfiguredSpeedDialsExceeded

The maximum configured speed dials was exceeded in the phone.

SrstMaxConfiguredDnExceeded

The number of maximum configured DNs was exceeded.

SrstMOHProvisioningFailure

Unable to do MOH provisioning. See the logs for more details.

SrstMultipleExternalPhoneNumMaskFound

Multiple external phone number masks were found in Cisco Unified Communications Manager.

SrstMultipleTimeBasedPartitionsFound

The after-hours configuration was unable to configure a site because multiple time-based partitions were found on Cisco Unified Communications Manager.

SrstMultipleVMPilotsFound

Multiple voicemail pilots for a site were found on Cisco Unified Communications Manager.

SrstPhoneProvisioningFailed

Cisco Unified SRST Manager was unable to create or update the phone in Cisco Unified SRST. See the logs for more details.

SrstPickupGroupConfigurationFailed

One or more errors was seen while trying to configure pickup group entries. See the logs for more details.

SrstProvisioningFailed

Cisco Unified SRST Manager was unable to provision a Cisco Unified SRST site. See the logs for more details.

SrstRouterModeDetectionFailure

Cisco Unified SRST Manager was unable to detect the router properties. See the logs for more details.

SrstSNRProvisioningFailed

Unable to do SNR provisioning for the specified site. See the logs for more details.

SrstSNRUpdateFailed

Unable to update SNR for the specified site. See the logs for more details.

SrstSoftkeyTemplateProvisioningFailure

Cisco Unified SRST Manager was unable to provision Softkey Template in Cisco Unified SRST. See the logs for more details.

SrstSystemInSRSTModeFailure

Cisco Unified SRST Manager was unable to provision a site because the site is in Cisco Unified SRST mode. Remove the “call-manager-fallback” configuration and try again.

SrstUnsupportedCMEVersionFailure

Cisco Unified SRST Manager was unable to provision the site because the version of Cisco Unified Communications Manager Express found is unsupported. Check the router version and image.

SrstUpdateDnFailure

Cisco Unified SRST Manager was unable to update the DN in Cisco Unified SRST. See the logs for more details.

SrstUpdatePhoneFailure

Cisco Unified SRST Manager was unable to update a phone in Cisco Unified SRST. See the logs for more details.

SrstWritingMappingConfigurationFailure

Cisco Unified SRST Manager was unable to write the Cisco Unified SRST mapping configuration to the database. See the logs for more details.

TlsCredentialSigningFailed

There was a failed TLS credential signing request to an external SCEP certificate authority.

TlsCredentialSigningTimeout

There was a failed TLS credential signing request to an external SCEP certificate authority because the certificate authority never completed the transaction and returned the signed credentials.

UmgProvisioningFailed

Problems were encountered while provisioning the secondary Cisco Unified SRST Manager.

Note The details link for this alert contains a list of all the provisioning errors seen for the Cisco Unified SRST Manager aggregated into a single alert.

Table 13 System Alerts – Informational Messages

NewSrstReferenceDetected

A new Cisco Unified SRST reference has been detected on the central telephony server (Cisco Unified Communications Manager). This could be an indication of a new Cisco Unified SRST Manager site to prepare.

ProvisioningCycleComplete

Completed the process of provisioning remote sites based on the central site configuration.

ProvisioningCycleResuming

Restarted the process of learning of any configuration changes from the central site to complete the configuration that must be pushed down to SRSV-CUE devices on a remote site.

ProvisioningCycleStarted

Starting the process of learning of any configuration changes from the central site that must be pushed down to SRSV-CUE devices on a remote site.

SrstInfo

Cisco Unified SRST Manager has provided an informational message. Refer to the log files for message details.

TlsCredentialRenewed

A TLS credential on Cisco Unified SRST Manager has expired but has been automatically renewed through a SCEP certificate authority.

UmgProvisioningInfo

This message is an indication that provisioning of the secondary Cisco Unified SRST Manager has some additional information to convey.

Note The details link for this alert contains a list of all the provisioning errors seen for the Cisco Unified SRST Manager aggregated into a single alert.

Related Topics

## Viewing the Site Provisioning History Report

The Site Provisioning History Report shows the results of the most recent successful site provisioning cycle. These results cannot be cleared or deleted.

Step 1 Select Reports > Site Provisioning History .

The Site Provisioning History Report contains the following fields:

- Site—The site name. The report displays every site known to Cisco Unified SRST Manager.

- Last Attempt—Indicates the outcome of the most recent provisioning attempt made by Cisco Unified SRST Manager for that site. Results can include never, success, failed, or disabled.

– “Never” indicates that the site has never been provisioned. The site may be newly created and neither the manual nor scheduled provisioning has occurred yet.

– “Disabled” indicates that the site was administratively disabled for provisioning during the last provisioning cycle. You can enable a disabled site on the Site Profile page. See Changing the Information for a Single Cisco Unified SRST Site .

– If the last attempt field is set to “Failed,” the system displays the date and time of the failure, and generates an alert. The system also increments the failed provisioning status count on the dashboard. To see the alert details, click Reports > Alert History .

Note Site provisioning failures are severe. Correct the failure as soon as possible by reviewing the corresponding alert.

- Date and Time—The date and time of the last provisioning attempt. This field is blank if the Last Attempt field is Never or Disabled.

- Last Successful—Indicates the last time that Cisco Unified SRST Manager successfully provisioned the branch device. Can be either “Success” or “Never.”

- Date and Time—If the status of the Last Successful field is Success, the report shows the date and time (relative to the branch device) when the successful provisioning was completed.

- Ephones Controlled—Displays the number of ephones being controlled by the CUCME device. The number should be consistent with the number of ephones provided by Cisco Unified Communications Manager.

Note Ephone data is shown only if E-SRST is enabled on the site.

- Latest Configuration Changes—If there is any change in the configuration between the current and previous successful provisioning, then a file containing the CLI difference will be available to view. Click Details to view the CLI differences.

- Complete Configuration Changes—Click Details to view the complete list of CLI running on Cisco Unified SRST Manager.

Step 2 To filter by status, such as success, failed, or never, select the check box next to a status and click Go .

Step 3 To view the Site Dial Peer Details page for a site in the report, click the site name in the report. See Viewing Site Dial Peer Details .

Related Topics

## Viewing the Backup History Report

Step 1 Select Reports > Backup History .

If there is any backup history to report, the Backup History report contains the following fields:

- ID—ID of the backup.

- Server URL—The server where the backup history is stored.

- Backup Time and Date—Date and time when the system was last backed up.

- Version—The version of the Cisco Unified SRST Manager software that is installed.

- Description—A description of the backup.

- Result—Displays the status of the last backup procedure for system configuration information and for data. Values can be either Success or Fail.

Step 2 To sort backup reports, click any of the headers.

Related Topics

## Viewing the Restore History Report

The Restore History report shows the history of all the restore processes done on the current system since installation.

Step 1 Select Reports > Restore History .

If there is any restore history to report, the Restore History report contains the following fields:

- ID—ID of the restore.

- Server URL—The server where the restore history is stored.

- Restore Time and Date—Date and time when the system was last backed up.

- Version—The version of Cisco Unified SRST Manager software that is installed.

- Result—Status of the last restore procedure. Result shows Success or Fail for the components that were restored.

Step 2 To sort restore history reports, click any of the headers.

Related Topics

## Viewing the Network Time Protocol Report

Step 1 Choose Reports > Network Time Protocol .

The system displays the Network Time Protocol Report with the following fields:

- #—The prioritized number of the NTP server. The system attempts to synchronize its time starting with NTP server number one.

- NTP Server—IP address or hostname of the NTP server.

- Status—Indicates if the NTP server connected with Cisco Unified SRST Manager or if it was rejected.

- Time Difference (secs)—Time offset between the NTP server and the client.

- Time Jitter (secs)—Estimated time error of the system clock, measured as an exponential average of RMS time differences.

Related Topics

## Viewing Site Dial Peer Details

This Site Dial Peer Details page displays a list of dial peers for a specific site and details about each dial peer.

Step 1 Choose Reports > Site Provisioning History to display a report of the results of the most recent site provisioning cycle. The report includes each site known to Cisco Unified SRST Manager.

Step 2 Click the name of a site in the report.

The system displays the Site Dial Peer Details page for the site. The page contains the following information for each dial peer:

- Dial Peer tag—Digit that uniquely identifies a dial peer.

- Type—Category that identifies the type of dial peer.

- Destination Pattern—A pattern that the router uses to match the called number of incoming calls. If an incoming call conforms to the destination pattern for the dial peer, the router directs the call to that dial peer.

- Port—Voice port associated with the given dial peer.

- Preference—Preferred selection order of a dial peer within a hunt group.

- Created by SRST Manager—Indicates whether the dial peer was created by SRST Manager.

Related Topics

- Back to the Viewing Reports menu page

| Alert Name | Description |
|---|---|
| CcmFailoverToSecondary | The primary central call agent was unavailable for provisioning, but the secondary central call agent was successfully utilized. |
| CcmUnreachableForProvisioning | Cisco Unified SRST Manager was unable to pull provisioning information from the configured telephony service server because it could not be reached on the network. Typically telephony service is provided by a central call agent like Cisco Unified Communications Manager. |
| ProvisioningCycleSuspended | Cisco Unified SRST Manager has suspended the process of provisioning remote sites based on the central site configuration. |
| SiteProvisioningSkipped | Provisioning for a site was skipped due to incomplete configuration. |
| SrstCSSNameConflictFound | A name conflict was found for Cisco Unified Communications Manager Calling Search Space names when applied to the Cisco Unified Communications Manager Express class of restriction lists. |
| SrstDialPeerMatchingToCUCMRoutePatternNotFound | Unable to find a matching dial peer to a Cisco Unified Communications Manager route pattern. |
| SrstLongHuntGroupChainFound | Hunt group configuration: Unable to configure long hunt pilot. |
| SrstMultipleTimeZonesFound | Multiple time zones for a site were found on the central Cisco Unified Communications Manager. |
| SrstPartitionNameConflictFound | A name conflict was found for Cisco Unified Communications Manager partition names when applied to the Cisco Unified Communications Manager Express class of restriction names. |
| SrstTimeBasedPartitionsDayOfMonthLimitReached | After hours configuration: Cisco Unified SRST Manager was unable to add more day of month schedules because the Cisco Unified Communications Manager Express time-based-partitions day of month limit has been reached. |
| SrstWarning | Cisco Unified SRST Manager has indicated a warning. Refer to the log files for details about the warning. |
| TlsCredentialExpired | A TLS credential on Cisco Unified SRST Manager has expired. |
| UmgProvisioningWarnings | Provisioning of the secondary Cisco Unified SRST Manager has some anomalies. Note The details link for this alert contains a list of all the provisioning errors seen for the Cisco Unified SRST Manager aggregated into a single alert. |
| UmgUnreachableForProvisioning | Cisco Unified SRST Manager was unable to provision a secondary Cisco Unified SRST Manager because it was unable to create a connection to the device. Possible causes for the failure include Cisco Unified SRST Manager TLS configuration, router line VTY configuration, or a network problem. |

| Alert Name | Description |
|---|---|
| CcmGlobalDataRetrievalFailure | Cisco Unified SRST Manager was unable to update the global Cisco Unified SRST data from Cisco Unified Communications Manager. See the logs for more details. |
| CcmProvisiningFail | Cisco Unified SRST Manager could not provision because of a communications problem with the central call agent . |
| CcmProvisioningFailAuth | Cisco Unified SRST Manager could not provision because of bad central call agent AXL credentials. Update the AXL username and password for the central call agent and try again. |
| CcmProvisioningFailTls | Cisco Unified SRST Manager could not provision because of a bad central call agent public TLS certificate. Add the central call agent's TLS certificate to Cisco Unified SRST Manager and try again. |
| CcmSrstReferenceDataRetrievalFailure | Cisco Unified SRST Manager was unable to update site-specific Cisco Unified SRST data from Cisco Unified Communications Manager. See the logs for more details. |
| LocalhostDnsFailure | The Cisco Unified SRST Manager host cannot be resolved by the DNS server. |
| SrstAfterHourNoExemptFailure | Unable to get After Hours no Exempt for the specified site. See the logs for more details. |
| SrstAfterHoursBlockPatternFailed | The after-hours configuration was unable to configure some after hours block patterns. See the logs for more details. |
| SrstAfterHoursConfigurationFailed | The after-hours configuration failed. See the logs for failure details. |
| SrstAfterHoursCreationFailed | Cisco Unified SRST Manager was unable to create after hours. See the logs for more details. |
| SrstCallParkConfigurationFailed | One or more errors were seen while trying to configure call park entries. See the logs for more details. |
| SrstCcpDiscoveryFailure | Cisco Unified SRST Manager was unable to execute configuration discovery for the Cisco Unified SRST site. See the logs for more details. |
| SrstCMENotSupportedFailure | Cisco Unified Communications Manager Express voice is not supported on the router. Check the router version and image. |
| SrstCreateDnFailure | Cisco Unified SRST Manager was unable to create the DN in Cisco Unified SRST. See the logs for more details. |
| SrstCreateExternalCallRoutingFailure | Cisco Unified SRST Manager was unable to create the external call routing configuration in Cisco Unified SRST. |
| SrstCreatePhoneFailure | Cisco Unified SRST Manager was unable to create a phone in Cisco Unified SRST. See the logs for more details. |
| SrstCreateSoftkeyTemplateFailure | Cisco Unified SRST Manager was unable to create a softkey template in Cisco Unified SRST. See the logs for more details. |
| SrstCreateSpeedDialFailure | Cisco Unified SRST Manager was unable to create speed dial in Cisco Unified SRST. See the logs for more details. |
| SrstCreateTranslationRulesFailure | Cisco Unified SRST Manager was unable to create translation rules in Cisco Unified SRST. |
| SrstCritical | Cisco Unified SRST Manager has experienced a critical error. Refer to the log files for details about the error. |
| SrstDeleteDnFailure | Cisco Unified SRST Manager was unable to delete the DN in Cisco Unified SRST. See the logs for more details. |
| SrstDeleteExternalCallRoutingFailure | Cisco Unified SRST Manager was unable to delete the external call routing configuration in Cisco Unified SRST. |
| SrstDeletePhoneFailure | Cisco Unified SRST Manager was unable to delete a phone in Cisco Unified SRST. See the logs for more details. |
| SrstDeleteSokftKeyTemplateExceeded | The maximum number of configured softkey templates was exceeded. |
| SrstDeleteSokftKeyTemplateFailure | Cisco Unified SRST Manager was unable to delete the softkey template in Cisco Unified SRST. See the logs for more details. |
| SrstDeleteSpeedDialFailure | Cisco Unified SRST Manager was unable to delete speed dial in Cisco Unified SRST. See the logs for more details. |
| SrstDeleteTranslationRulesFailure | Cisco Unified SRST Manager was unable to delete translation rules in Cisco Unified SRST. |
| SrstError | Cisco Unified SRST Manager has experienced an error. Refer to the log files for details about the error. |
| SrstFetchingCcmSRSTConfigurationFailure | Cisco Unified SRST Manager was unable to fetch the Cisco Unified SRST configuration from Cisco Unified Communications Manager. See the logs for more details. |
| SrstFetchingHardwareConfigurationFailure | Cisco Unified SRST Manager was unable to provision the site because it was unable to get hardware information for the site. See the logs for more details. |
| SrstFetchingMappingConfigurationFailure | Cisco Unified SRST Manager was unable to fetch the Cisco Unified SRST mapping configuration from the database. See the logs for more details. |
| SrstFetchingPlatformInformationFailure | Cisco Unified SRST Manager was unable to provision the site because it was unable to get hardware platform information based on the hardware. Ensure that this hardware is supported. |
| SrstFetchingSRSTConfigurationFailure | Cisco Unified SRST Manager was unable to fetch the Cisco Unified SRST configuration from the router. See the logs for more details. |
| SrstFetchingTelephonyConfigurationFailure | Cisco Unified SRST Manager was unable to fetch the telephony configuration from the router. See the logs for more details. |
| SrstFetchTranslationRulesFailure | Cisco Unified SRST Manager was unable to fetch translation rules from Cisco Unified SRST. |
| SrstGettingCSSContainingPartitionFailed | Cisco Unified SRST Manager was unable to get CSS Containing Partition. See the logs for more details. |
| SrstHuntGroupConfigurationFailed | The hunt groups configuration failed. See the logs for failure details. |
| SrstHuntGroupLongPilotFound | The hunt group configuration was unable to configure a long-chained hunt pilot. |
| SrstInvalidDateFormatFound | Cisco Unified SRST Manager was unable to provision the date format because an invalid or unsupported date format was found. |
| SrstInvalidTimeZoneFound | Cisco Unified SRST Manager was unable to provision the time zone because an invalid or unsupported time zone was found. |
| SrstMaxConfiguredCoRExceeded | The maximum configured class of restrictions was exceeded. |
| SrstMaxConfiguredPhoneExceeded | The number of maximum configured phones was exceeded. |
| SrstMaxConfiguredSpeedDialsExceeded | The maximum configured speed dials was exceeded in the phone. |
| SrstMaxConfiguredDnExceeded | The number of maximum configured DNs was exceeded. |
| SrstMOHProvisioningFailure | Unable to do MOH provisioning. See the logs for more details. |
| SrstMultipleExternalPhoneNumMaskFound | Multiple external phone number masks were found in Cisco Unified Communications Manager. |
| SrstMultipleTimeBasedPartitionsFound | The after-hours configuration was unable to configure a site because multiple time-based partitions were found on Cisco Unified Communications Manager. |
| SrstMultipleVMPilotsFound | Multiple voicemail pilots for a site were found on Cisco Unified Communications Manager. |
| SrstPhoneProvisioningFailed | Cisco Unified SRST Manager was unable to create or update the phone in Cisco Unified SRST. See the logs for more details. |
| SrstPickupGroupConfigurationFailed | One or more errors was seen while trying to configure pickup group entries. See the logs for more details. |
| SrstProvisioningFailed | Cisco Unified SRST Manager was unable to provision a Cisco Unified SRST site. See the logs for more details. |
| SrstRouterModeDetectionFailure | Cisco Unified SRST Manager was unable to detect the router properties. See the logs for more details. |
| SrstSNRProvisioningFailed | Unable to do SNR provisioning for the specified site. See the logs for more details. |
| SrstSNRUpdateFailed | Unable to update SNR for the specified site. See the logs for more details. |
| SrstSoftkeyTemplateProvisioningFailure | Cisco Unified SRST Manager was unable to provision Softkey Template in Cisco Unified SRST. See the logs for more details. |
| SrstSystemInSRSTModeFailure | Cisco Unified SRST Manager was unable to provision a site because the site is in Cisco Unified SRST mode. Remove the “call-manager-fallback” configuration and try again. |
| SrstUnsupportedCMEVersionFailure | Cisco Unified SRST Manager was unable to provision the site because the version of Cisco Unified Communications Manager Express found is unsupported. Check the router version and image. |
| SrstUpdateDnFailure | Cisco Unified SRST Manager was unable to update the DN in Cisco Unified SRST. See the logs for more details. |
| SrstUpdatePhoneFailure | Cisco Unified SRST Manager was unable to update a phone in Cisco Unified SRST. See the logs for more details. |
| SrstWritingMappingConfigurationFailure | Cisco Unified SRST Manager was unable to write the Cisco Unified SRST mapping configuration to the database. See the logs for more details. |
| TlsCredentialSigningFailed | There was a failed TLS credential signing request to an external SCEP certificate authority. |
| TlsCredentialSigningTimeout | There was a failed TLS credential signing request to an external SCEP certificate authority because the certificate authority never completed the transaction and returned the signed credentials. |
| UmgProvisioningFailed | Problems were encountered while provisioning the secondary Cisco Unified SRST Manager. Note The details link for this alert contains a list of all the provisioning errors seen for the Cisco Unified SRST Manager aggregated into a single alert. |

| Alert Name | Description |
|---|---|
| NewSrstReferenceDetected | A new Cisco Unified SRST reference has been detected on the central telephony server (Cisco Unified Communications Manager). This could be an indication of a new Cisco Unified SRST Manager site to prepare. |
| ProvisioningCycleComplete | Completed the process of provisioning remote sites based on the central site configuration. |
| ProvisioningCycleResuming | Restarted the process of learning of any configuration changes from the central site to complete the configuration that must be pushed down to SRSV-CUE devices on a remote site. |
| ProvisioningCycleStarted | Starting the process of learning of any configuration changes from the central site that must be pushed down to SRSV-CUE devices on a remote site. |
| SrstInfo | Cisco Unified SRST Manager has provided an informational message. Refer to the log files for message details. |
| TlsCredentialRenewed | A TLS credential on Cisco Unified SRST Manager has expired but has been automatically renewed through a SCEP certificate authority. |
| UmgProvisioningInfo | This message is an indication that provisioning of the secondary Cisco Unified SRST Manager has some additional information to convey. Note The details link for this alert contains a list of all the provisioning errors seen for the Cisco Unified SRST Manager aggregated into a single alert. |