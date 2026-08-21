---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--998f21e903
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010000.html
retrieved_at: 2026-08-21T01:34:28.648375+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CDR Error System Reports

## Chapter: CDR Error System Reports

# CDR Error System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## Generate CDR Error Reports

Only CAR administrators generate the CDR Error report. The
                              		  report provides statistics for the number of error records in the CAR Billing
                              		  Error (tbl_billing_error) table for a particular time period.

In order to determine why the error records failed the CDR
                              		  Load, you must review the information in the tbl_error_id_map table.

The following table lists the CDR error codes and the
                              		  definition of the error.

Error Code

Definition

CDRs

31101

CDR globalCallID_callManagerId <= 0

31102

CDR globalCallID_callId <= 0

31103

CDR origLegCallIdentifier <= 0

31105

CDR dateTimeOrigination <= 0

31108

CDR destLegIdentifier <= 0

31110

CDR dateTimeConnect <= 0

31111

CDR dateTimeDisconnect <= 0

31119

CDR originalCalledPartyNumber is empty

31120

CDR finalCalledPartyNumber is empty

31122

CDR duration < 0

31137

CDR LDAP error while retrieving UserID or ManagerID

31139

CDR callingPartyNumber is empty

31147

CDR origDeviceName is empty

31148

CDR destDeviceName is empty

31151

CDR origCallTerminationOnBehalfOf < 0

31152

CDR destCallTerminationOnBehalfOf < 0

31153

CDR lastRedirectRedirectOnBehalfOf < 0

31155

CDR destConversationId < 0

31156

CDR globalCallId_ClusterID is empty

Orig CMR

31123

Orig CMR globalCallID_callManagerId <= 0

31124

Orig CMR globalCallID_callId <= 0

31125

Orig CMR numberPacketsSent < 0

31126

Orig CMR numberPacketsReceived < 0

31127

Orig CMR jitter < 0

31129

Orig CMR callIdentifier <= 0

31149

Orig CMR deviceName is empty

31157

Orig CMR globalCallId_ClusterID is empty

Dest CMR

31140

Dest CMR globalCallID_callManagerId <= 0

31141

Dest CMR globalCallID_callId <= 0

31142

Dest CMR numberPacketsSent < 0

31143

Dest CMR numberPacketsReceived < 0

31144

Dest CMR jitter < 0

31145

Dest CMR callIdentifier <= 0

31150

Dest CMR deviceName is empty

31158

Dest CMR globalCallId_ClusterID is empty

This section describes how to generate, view, or mail
                              		  information about the CDR Error report.

Choose System Reports > CDR Error .

The CDR Error window displays.

Choose the date range of the period for which you want to generate
                                       			 the report.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter. |
|---|---|

| Error Code | Definition |
|---|---|
| CDRs |
| 31101 | CDR globalCallID_callManagerId <= 0 |
| 31102 | CDR globalCallID_callId <= 0 |
| 31103 | CDR origLegCallIdentifier <= 0 |
| 31105 | CDR dateTimeOrigination <= 0 |
| 31108 | CDR destLegIdentifier <= 0 |
| 31110 | CDR dateTimeConnect <= 0 |
| 31111 | CDR dateTimeDisconnect <= 0 |
| 31119 | CDR originalCalledPartyNumber is empty |
| 31120 | CDR finalCalledPartyNumber is empty |
| 31122 | CDR duration < 0 |
| 31137 | CDR LDAP error while retrieving UserID or ManagerID |
| 31139 | CDR callingPartyNumber is empty |
| 31147 | CDR origDeviceName is empty |
| 31148 | CDR destDeviceName is empty |
| 31151 | CDR origCallTerminationOnBehalfOf < 0 |
| 31152 | CDR destCallTerminationOnBehalfOf < 0 |
| 31153 | CDR lastRedirectRedirectOnBehalfOf < 0 |
| 31155 | CDR destConversationId < 0 |
| 31156 | CDR globalCallId_ClusterID is empty |
| Orig CMR |
| 31123 | Orig CMR globalCallID_callManagerId <= 0 |
| 31124 | Orig CMR globalCallID_callId <= 0 |
| 31125 | Orig CMR numberPacketsSent < 0 |
| 31126 | Orig CMR numberPacketsReceived < 0 |
| 31127 | Orig CMR jitter < 0 |
| 31129 | Orig CMR callIdentifier <= 0 |
| 31149 | Orig CMR deviceName is empty |
| 31157 | Orig CMR globalCallId_ClusterID is empty |
| Dest CMR |
| 31140 | Dest CMR globalCallID_callManagerId <= 0 |
| 31141 | Dest CMR globalCallID_callId <= 0 |
| 31142 | Dest CMR numberPacketsSent < 0 |
| 31143 | Dest CMR numberPacketsReceived < 0 |
| 31144 | Dest CMR jitter < 0 |
| 31145 | Dest CMR callIdentifier <= 0 |
| 31150 | Dest CMR deviceName is empty |
| 31158 | Dest CMR globalCallId_ClusterID is empty |

| Step 1 | Choose System Reports > CDR Error . The CDR Error window displays. |
|---|---|
| Step 2 | Choose the date range of the period for which you want to generate
                                       			 the report. |
| Step 3 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 4 | Click the View Report button. The report displays . |
| Step 5 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |