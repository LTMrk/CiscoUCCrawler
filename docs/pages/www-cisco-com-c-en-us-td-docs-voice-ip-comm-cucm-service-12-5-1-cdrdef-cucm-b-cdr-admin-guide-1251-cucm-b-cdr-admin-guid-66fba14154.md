---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-cdrdef-cucm-b-cdr-admin-guide-1251-cucm-b-cdr-admin-guid-66fba14154
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/cdrdef/cucm_b_cdr-admin-guide-1251/cucm_b_cdr-admin-guide-1251_chapter_01.html
retrieved_at: 2026-08-17T00:50:50.915835+00:00
---

Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Cisco Call Detail Records

## Chapter: Cisco Call Detail Records

# Cisco Call Detail Records

This chapter provides information about the format and logic of the call detail records (CDRs) that the Unified Communications Manager system generates. You can use this information for post-processing activities such as generating billing records and network
                        analysis.

When you install your system, the system enables CDRs by default. Call management records (CMRs) remain disabled by default.
                        You can enable or disable CDRs or CMRs at any time that the system is in operation. You do not need to restart Unified Communications Manager for the change to take effect. The system responds to all changes within a few seconds. The system enables CMR or diagnostic
                        data separately from CDR data.

## CDR Management

The CDR Management (CDRM) feature, a background application, supports the following capabilities:

Collects the CDR/CMR files from the Unified Communications Manager server or node to the CDR Repository server or node.

Collects and maintains the CDR/CMR files on the server where you configure CAR.

Maintains the CDR/CMR files on the CDR Repository node or CDR server.

Allows third-party applications to retrieve CDR/CMR files on demand through a SOAP interface.

Accepts on-demand requests for searching file names.

Pushes CDR/CMR files from individual nodes within a cluster to the CDR Repository server or node.

Sends CDR/CMR files to up to three customer billing servers via FTP/SFTP.

Monitors disk usage of CDR/CMR files on the server where you configure CAR or on the CDR Repository server or node.

Periodically deletes CDR/CMR files that were successfully delivered. You can configure the amount of storage that is used
                                    to store flat files. Predefined storage limits exist. If the storage limits are exceeded, the CDR Repository Manager deletes
                                    old files to reduce the disk usage to the preconfigured low water mark. The post-processing applications can later retrieve
                                    the buffered historical data to re-get any lost, corrupted, or missing data. The CDRM feature, which is not aware of the flat
                                    file format, does not manipulate the file contents.

CDRM comprises two default services, the CDR Agent and the CDR Repository Manager, and one activate service, CDR onDemand
                              Service.

### CDR Agent

As part of the CDRM feature, a resident component on the server or node within a Unified Communications Manager installation acts as the CDR Agent. On the server or node where both Unified Communications Manager and the CDR Agent are running, Unified Communications Manager writes the CDRs into CDR flat files in comma separated value (CSV) format. A special control character ( "_" ) that is prefixed to the filename by the call processing module that indicates that the file is not available for transfer.
                                 If this control character is not present, the system assumes that the file is available for transfer, and the CDR Agent then
                                 SFTPs those files to the designated CDR repository node. Upon successful transfer, the system deletes the local copy of the
                                 file.

Reliability gets the highest priority for the CDRM feature. CDRs comprise very important financial data, so the goal of this
                                 feature is to guarantee that no CDR is lost. The Unified Communications Manager continuously writes CDRs to flat files, closes existing flat files, and opens new ones. The number of records that are written
                                 varies by the type of call and the significant changes that occur during a call: such as, ending the call, transferring the
                                 call, redirecting the call, splitting the call, or joining the call.

On Linux platforms, the CDR Agent collects the CDR/CMR flat files that the Unified Communications Manager generates and sends these files to the publisher through SFTP. The Windows versions of do not support SFTP. On Windows platforms,
                                             the CDR Agent copies the files directly from the subscriber disk to the shared publisher disk.

### CDR Repository Manager

Within a Unified Communications Manager server or cluster, one instance of the CDR Repository Manager runs on the CDR Repository server or node. It manages CDR files
                                 that are received from the Unified Communications Manager nodes and periodically sends the files to the specified customer/third-party billing servers via FTP/SFTP.

When the file arrives on the CDR Repository server or node, the CDR Repository Manager detects it. The system archives the
                                 file in a directory that is dedicated to the date that is indicated by the UTC timestamp that was placed in the file name
                                 when the file was created.

If any external billing server is specified in the CDRM configuration, the system creates an empty file in each of the corresponding
                                 folders for CAR and the billing servers, if CAR or the corresponding billing server is activated. The CDR Agent monitors new
                                 CDR/CMR files that are generated on CallManager servers or nodes by the call processing component. It sends the files to the
                                 CDR Repository node and then deletes the local copy after the file is pushed out. The file sender component of the CDR Repository
                                 Manager detects these empty files and sends the file to the destination with the specified method. If the delivery is successful,
                                 the system removes the empty file in the destination directory.

Every Unified Communications Manager can generate one CDR file and one CMR file every minute for up to 1hour. You can configure the maximum disk space that is
                                 used for storage of CDR files in the CDR Repository through provisioning.

The File Manager component of the CDR Repository Manager runs hourly. When the File Manager runs, it deletes files with dates
                                 outside the configured preservation duration. It also checks whether disk usage has exceeded the high water mark. If so, the
                                 system deletes the processed CDR files until the low water mark is reached, starting with the oldest files. However, if any
                                 CDR file to be deleted was not successfully sent to the specified billing server, the system leaves it in the CDR Repository
                                 and raises a notification or alarm. The system creates a flag file during the configured maintenance window, which denies
                                 access to the CDR files for the CDR onDemand Service. The system removes the flag file after the maintenance window expires.

For detailed procedures on configuring the CDR Repository Manager and customer billing servers, see the "CDR Repository Manager Configuration" section in the Cisco Unified Serviceability Administration Guide .

### CDR onDemand
                           	 Service

The CDR
                                 		  onDemand Service, is a SOAP/HTTPS-based service, that runs on the CDR
                                 		  Repository server or node. It receives SOAP requests for CDR filename lists
                                 		  based on a user-specified time interval (up to a maximum of 1hour) and returns
                                 		  all lists that fit the duration that the request specifies.

The CDR
                                 		  onDemand Service can also handle requests for delivering a specific CDR file to
                                 		  a specified destination through an SFTP API. All SFTP connections require
                                 		  userid and password information for each session setup. A separate SFTP session
                                 		  gets set up for every file that is sent, and the session is closed after the
                                 		  file has been sent. The system can activate the CDR onDemand service on the CDR
                                 		  Repository node because it has to access the CDR files in the repository. The
                                 		  system prohibits service during the maintenance window. For detailed
                                 		  information on the CDR onDemand Service, see the Cisco Unified Communications Manager Developers
                                 		  Guide.

For Cisco Unified Communications Manager Release 10.x and later releases, CDR onDemand Service is not enabled by default.
                                 If you want to enable the CDR onDemand service, the service should be activated manually. Execute the following command at
                                 the root level to activate the CDR onDemand service: /usr/local/cm/bin/soapservicecontrol2.shCDRonDemandServiceCDRonDemanddeploy8443 .

## Cisco Unified Communications Manager Upgrades and CDR Data

When you upgrade from an earlier version of Unified Communications Manager to a later version of Unified Communications Manager , you may not be able to upgrade all your CDR data. For additional information about the limitations that affect the amount
                              of CDR data that may be available after upgrade, see the section titled "Upgrading the CAR Database" in the CDR Analysis and Reporting Administration Guide . You may also need to refer to the latest Data Migration Assistant User Guide and the latest upgrade documentation.

## CDR Database Backup
                        	 and Recovery

Be sure
                              		  that the CAR and CDR Disaster Recovery Service (DRS) is integrated into the Cisco Unified Communications
                                 			 Manager DRS.

See the Administration
                                 			 Guide for Cisco Unified Communications Manager .

## Documentation
                        	 Related to CDR

The following
                           		documents contain additional information related to CDRs:

Cisco Unified Serviceability Administration
                                       				  Guide .

See the "Configuring the
                                    				CDR Repository Manager" chapter in the Cisco Unified Serviceability Administration
                                       				  Guide .

CDR Analysis and Reporting Administration
                                       				  Guide .

See the "Activating
                                    				CAR" section in the Configuring CDR Analysis and Reporting Tool chapter
                                 			 found in the CDR Analysis
                                    				and Reporting Administration Guide .

Cisco Unified Communications Manager Developers
                                    				Guide

See the Administration Guide for Cisco Unified Communications
                                       				  Manager .

| Note | The CDRM feature handles CDR files and CMR files in the same manner. |
|---|---|

| Note | On Linux platforms, the CDR Agent collects the CDR/CMR flat files that the Unified Communications Manager generates and sends these files to the publisher through SFTP. The Windows versions of do not support SFTP. On Windows platforms,
                                             the CDR Agent copies the files directly from the subscriber disk to the shared publisher disk. |
|---|---|