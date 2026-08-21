---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-cdrdef-cucm-b-cdr-admin-guide-1251-cucm-b-cdr-admin-guid-adc20219b5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/cdrdef/cucm_b_cdr-admin-guide-1251/cucm_b_cdr-admin-guide-1251_chapter_010.html
retrieved_at: 2026-08-21T01:38:06.157880+00:00
---

Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: CDR Processing

## Chapter: CDR Processing

- CDR Processing

- Record                              	 Processing

# CDR Processing

This chapter provides information about how CDRs are processed.

## Record
                        	 Processing

Unified Communications Manager generates two different types of call information records: CDRs and CMRs. The CDR records store information about a call.
                              The CMR records store information about the quality of the streamed audio of the call. The CDR records relate to the CMR records
                              by way of two GlobalCallID columns: Global CallID callManagerId and GlobalCallID Called. Depending upon the call scenario,
                              more than one CMR may exist for each CDR.

When Unified Communications Manager places or receives a call, the system generates a CDR record when the call terminates. The system writes the CDR to a flat
                              file (text file). Inside the Unified Communications Manager , the Call Control process generates CDR records. The system writes records when significant changes occur to a given call,
                              such as ending the call, transferring the call, redirecting the call, splitting the call, joining a call, and so forth.

When CDR
                              		  records are enabled, Call Control generates one or more CDR records for each
                              		  call. The system sends these records to EnvProcessCdr, where they are written
                              		  to the flat files. The number of records that are written varies by type of
                              		  call and the call scenario. When Diagnostics are enabled, the device generates
                              		  CMR records for each call. The system writes one CMR record for each IP phone
                              		  that is involved in the call or for each Media Gateway Control Protocol (MGCP)
                              		  gateway. The system also sends these records to EnvProcessCdr where they get
                              		  written to flat files.

The Unified Communications Manager generates CDR and CMR records but does not perform any post processing on the records. The system writes the records to comma-delimited
                              flat files and periodically passes them to the CDR Repository. The CDR and CMR files represent a specific filename format
                              within the flat file.

### Filename
                              		  Format

The
                              		  following example shows the full format of the filename: tag_clusterId_nodeId_datetime_seqNumber

tag —Identifies the type of file, either CDR or
                                    				CMR.

clusterId —Identifies the cluster or server where the Unified Communications Manager database resides.

nodeId —Identifies the node

datetime —UTC time in yyyymmddhhmm format

seqnumber —Sequence number

```
cdr_Cluster1_01_200404021658_1
cmr_Cluster1_02_200404061011_6125
```

### Flat File
                              		  Format

The CDR and
                              		  CMR flat files have the following format:

Line 1—List of
                                    				field names comma separated

Line 2—List of
                                    				field type comma separated

Line 3—Data
                                    				comma separated

Line 4—Data
                                    				comma separated

```
Line1- "cdrRecordType" , "globalCallID_callManagerId" , "globalCallID_callId" , "origLegCallIdentifier" ,...
Line2-INTEGER,INTEGER,INTEGER,INTEGER,...
Line3-1,1,388289,17586046,...
Line4-1,1,388293,17586054,...
```

If the value of the CDR Log Calls With Zero Duration Flag parameter is True, the system writes all calls to a flat file. See
                                          the "Configuring CDR Service Parameters" section in the CDR Analysis and Reporting Administration Guide for additional information about this parameter.

| Note | If the value of the CDR Log Calls With Zero Duration Flag parameter is True, the system writes all calls to a flat file. See
                                          the "Configuring CDR Service Parameters" section in the CDR Analysis and Reporting Administration Guide for additional information about this parameter. |
|---|---|