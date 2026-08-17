---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-14-cucm-b-reporting-billing-administration-gu-fd446c36ec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/14/cucm_b_reporting-billing-administration-guide-14/cucm_b_reporting-and-billing-administration-guide_chapter_0101.html
retrieved_at: 2026-08-17T00:26:33.517574+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 9, 2026

Chapter: Export CDRs and CMRs

## Chapter: Export CDRs and CMRs

# Export CDRs and CMRs

## CDR and CMR Records

This chapter describes how to export CDR/CMR records and how to view the exported records.

Use Export CDR/CMR in the CDR menu in Cisco Unified Communications Manager CDR Analysis and Reporting to export CDR/CMR dump
                           information to the location of your choice on your computer. The CDR/CMR dump exists in the CSV format. You can also view
                           the dump of the exported records.

### Export CDR and CMR Records

Follow this procedure to export CDR and CMR record results.

Step 1

From CDR Analysis and Reporting, choose CDR > Export CDR/CMR .

The Export CDR/CMR records window appears.

Step 2

In the From Date and To Date drop-down list boxes, choose a date range for the CDR/CMR dump.

Step 3

In Select records, check the CDR records and/or CMR records check box.

Step 4

Click Export to File .

The Export CDR/CMR records Result window appears. See the View CDR and CMR Records Results .

### View CDR and CMR Records Results

The following procedure describes how to view Export CDR/CMR record results.

#### Before you begin

Before you begin the following procedure, perform all the steps in the Export CDR and CMR Records .

Step 1

From the Export CDR/CMR Record Results window, right-click either the CDR Dump or CMR Dump link.

A popup window that comprises the following options displays:

Open - This option allows you to open the window that contains the CDR/CMR dump in the same window.

Open in a New Window - This option allows you to open the window that contains the CDR/CMR dump in a new window.

Save Target As... - This option allows you to save the CDR/CMR dump to a location on your computer.

Print Target - This option allows you to print the CDR/CMR dump information.

Copy Shortcut - This option allows you to copy the window shortcut to paste in another file.

Add to Favorites - This option allows you to add the CDR/CMR dump to your Favorites folder.

Properties - This option provides the properties of the CDR/CMR dump file.

Step 2

From the pop-up window, choose one of the options.

Step 3

If you chose to save the CDR/CMR dump to your computer, choose a location in which to save the dump and click Save . After the download is complete, you can locate the file wherever you download it to open it.

Step 4

To delete the CDR and/or CMR dump, check Delete File check box and click Back or Close .

The files get deleted.

If you do not check the Delete File check box(es) (for example, if the CDR or CMR dump files get left undeleted), the background
                                                         process deletes the files daily. Because the CDR and CMR dump files are large, Cisco recommends that you download the file
                                                         to a local disk and delete them from the server to avoid the disk usage on the server side.

### CDR Data

Call detail records (CDRs) detail the called number, the number that places the call, the date and time that the call starts,
                                 the time that the call connects, and the time that the call ends. Call management records (CMRs), or diagnostic records, detail
                                 the jitter, lost packets, the amount of data sent and received during the call, and latency. CDR data comprises CDRs and CMRs
                                 collectively. A single call can result in the generation of several CDRs and CMRs. Unified Communications Manager records information regarding each call in CDRs and CMRs. CDRs and CMRs, known collectively as CDR data, serve as the basic
                                 information source for CAR.

The Cisco CDR Agent service transfers CDR and CMR files that Unified Communications Manager generates from the local host to the CDR repository node, where the CDR Repository Manager service runs over a SFTP connection.
                                 If the SFTP connection fails, the Cisco CDR Agent services continue to make connection attempts to the CDR repository node
                                 until a connection is made. The CiscoCDR Agent service sends any accumulated CDR files when the connection to the CDR Repository
                                 node resumes. The CDR Repository Manager service maintains the CDR and CMR files, allocates the amount of disk space for use
                                 by CMRs and CDRs, sends the files to up to three configured destinations, and tracks the delivery result for each destination.
                                 CAR accesses the CDR/CMR files in the directory structure that the CDR Repository Manager service creates.

The high and low water mark settings that you configure specify percentages of the total disk space that are allocated for
                                 the CDR repository. Although the preserved folder under the CDR repository folder contributes to the high and low water mark
                                 percentages, Log Partition Monitoring never deletes the folder if the high water mark gets reached. If the high water mark
                                 gets reached, the CDR Repository Manager deletes processed CDR files until the low water mark is reached or all processed
                                 files are deleted, whichever comes first. If all processed CDR files are deleted but the low water mark has not been reached,
                                 the deletion stops. The CDRHighWaterMarkExceeded alarm gets generated until the system reaches the maximum disk allocation.
                                 If the maximum disk allocation gets reached, the system deletes undelivered files, and files within the preservation duration,
                                 starting with the oldest files, until disk utilization falls below the high water mark. If you receive the CDRMaximumDiskSpaceExceeded
                                 alarm repeatedly for this scenario, either increase the disk allocation or lower the number of preservation days.

When the disk allocation usage exceeds the configured high water mark threshold value, LMP also purges the CDR and CMR data
                                             that are exported at the following path automatically: /var/log/active/tomcat/logs/car/carreports/reports/ondemand/temp .

Customers or any third-party applications should ensure to retrieve the exported files immediately to avoid losing their buffered
                                             historical data.

Information on these alarms is found in the CDR Repository Alarm Catalog (CDRRepAlarmCatalog). The following table displays
                                 the alarms and alerts in this catalog.

To configure these alarms, go to Cisco Unified Serviceability > Alarm > Configuration > CDR Services .

Name

Severity

Description

CDRFileDeliveryFailed

ERROR_ALARM

SFTP delivery of CDR files to the outside billing server failed.

CDRAgentSendFileFailed

ERROR_ALARM

The CDR Agent cannot send CDR files from the Cisco Unified CM node to the CDR Repository node within the Unified Communications Manager cluster.

CDRHWMExceeded

WARNING_ALARM

The high water mark (HWM) for CDR files was reached; some successfully delivered CDR files have been deleted.

CDRMaximumDiskSpaceExceeded

CRITICAL_ALARM

The CDR files disk usage exceeded the maximum disk allocation. Some undelivered files may have been deleted to bring disk
                                             usage down.

CDRFileDeliveryFailureContinues

ERROR_ALARM

SFTP delivery of CDR files failed on retries.

CDRAgentSendFileFailureContinues

ERROR_ALARM

The CDR Agent cannot send CDR files from the Cisco Unified CM node to the CDR Repository node on retries.

For additional information on these alarms and recommended action, see the alarm definitions at Cisco Unified Serviceability > Alarm > Definitions > CDRRepAlarmCatalog .

For more information on CDR services and alarms, see the Cisco Unified Serviceability Administration Guide .

## CDR Search

In all CDR Search reports, the system only displays the oldest 100 records that fall into the time and date range that you
                              configure. The CDR Search reports generate only in HTML format.

You can configure CDR searches to verify the details of a call. The search forms groups of all the related legs of a call,
                              which can be useful if the call involves a conference or transfer. This method helps you track the progress and quality of
                              each part of an entire call.

This section describes the following features:

CDR Search by User/Phone Number/SIP URL - Available for CAR administrators. You can search CDRs by the user or directory number
                                    (calling, original called, final called, or bridge number) to analyze call details for the first 100 records that satisfy
                                    the search criteria. You can search for calls by using specific numbers for the period that you specify, which helps you trace
                                    calls that are placed from or to any specific numbers for diagnostic or informational purposes. All associated records, such
                                    as transfer and conference calls, appear together as a logical group. If you do not specify the phone number or SIP URL, the
                                    system returns the first 100 CDR records that match the date range that you specify.

CDR Search by Gateway - Available for CAR administrators. You can search CDRs by gateways to analyze the call details of calls
                                    that are using specific gateways. This method helps you trace issues on calls through specific gateways.

CDR Search by Cause for Call Termination - Available for CAR administrators. You can search CDRs by cause for call termination
                                    to get information about the cause for the termination of a call. You can choose from a list of causes for call termination
                                    and can generate the report for a particular date range. The generated report contains the report criteria, along with the
                                    total number of calls that were placed in the given time. In addition, a table displays with the fields Call Termination Cause
                                    Value and description, the total number of calls, and the percentage of calls for each Call Termination Cause, and an option
                                    to choose the CDRs.

CDR Search by Call Precedence Level - Available for CAR administrators. You can search CDRs by call precedence level. The
                                    report that generates allows you to view the CDRs on the basis of precedence. You can choose the precedence level and date
                                    range for which to generate a report. The report displays the number of calls and the percentage of these calls for each precedence
                                    level that you choose. Report criteria display the precedence levels and date range for which the report-generated information
                                    in the Call Precedence Details window. You can view the media information and the CDR-CMR dump from the CDR Search by Precedence
                                    Levels Result window. The media information and CDR-CMR dump information display in separate windows.

CDR Search for Malicious Calls - Available for CAR administrators. You can search for CDRs to get information about malicious
                                    calls. You can choose phone number or SIP URL and the date range for which to generate a report. The report displays the CDRs
                                    for all the malicious calls for a chosen phone number or SIP URL and date range. Report criteria display the phone number
                                    or SIP URL and the date range for which the report-generated information. You can view the media information and CDR-CMR dump
                                    from the CDR-CMR search results window. The media information and CDR-CMR dump information display in separate windows.

Export CDR/CMR - Available for CAR administrators. With this feature, you can export CDR/CMR dump information, for a given
                                    date range in the CSV format, to a location that you choose on your computer. You can also view the file size of the dump
                                    information and delete CDR/CMR files.

### Before You Begin

Make sure that you set the Unified Communications Manager service parameters CDR Enabled Flag and Call Diagnostics Enabled to True (enabled), so the system can generate CDR/CMR data. By default, the system disables these service parameters. For more information
                              about these service parameters, see the Configure CDR Service Parameters .

All CAR reports use CDR data. Be sure to have the most current CDR data from which to build your reports. By default, CDR
                              data loads continuously 24 hours a day, 7 days a week. However, you can set the loading time, interval, and duration as needed.
                              For more information, see Set Up CDR Load Schedule .

After you log in to the CAR main window, the following warning may display if Unified Communications Manager is also activated: "Warning: In some servers in this cluster the CDR Enabled Flag is false and so CDR entries may not be generated for all the
                                             calls that are made in this cluster." Some clusters have multiple nodes where some of the nodes do not run Unified Communications Manager services. This warning checks all nodes in the cluster regardless of Unified Communications Manager service activation status. Ignore the warning after manually checking the CDR Enabled Flag parameter settings for all the Unified Communications Manager service subscribers.

### Generate CDR Search by User

Only CAR administrators use the CDR Search by User/Phone Number/SIP URL feature.

This section describes how to show the details of CDR data based on a user or phone number or SIP URL feature. You can search
                                 CDR data by user or directory number (calling, original called, or final called) to analyze call details for the oldest 100
                                 records that satisfy the search criteria. If more than 100 records are returned, the system truncates the results. You can
                                 search for calls by using specific numbers for the period that you specify, which helps you trace calls that are placed from
                                 or to any specific numbers for diagnostic or informational purposes. All associated records, such as transfer, mobility, silent
                                 monitoring and recording, and conference calls, appear together as a logical group.

Step 1

Choose CDR > Search > By User/Phone Number/SIP URL .

The CDR Search window displays.

You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9.

Step 2

Perform one of the following tasks:

To search CDRs based on Internal Phone Number/SIP URLs, enter the value in the Phone Number/SIP URL field and click Add Phone Number/SIP URL .

To search CDRs based on user, click the Search Internal Phone Number/SIP URL based User link, enter the first few letters of the first and/or the last name in the First Name and/or the Last Name fields, and click Search . When the results display, click the Select link next to the result that you want to include. Click Close .

The phone number or SIP URL displays in the Phone Number/SIP URL(s) box.

To delete an item from the Report Criteria box, click Remove Phone Number/SIP URL(s) . You can delete all items from the Report Criteria box by clicking Remove All Phone Number/SIP URL(s) .

Step 3

Choose the date and time range of the period for which you want to see CDR data for the specified user or phone number or
                                          SIP URL. The current time displays in both Coordinated Universal Time (UTC) and local time and uses the following rules:

The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00.

The default FromDate and ToDate values display in UTC time.

The default ToDate specifies the current time of the server in UTC time.

The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, the
                                                FromDate default value = January 15, 2007 11:00:00 (all times in UTC).

Step 4

Choose whether to run the CDR Search report with grouping or without grouping. If you choose with grouping, check the check
                                          box beside With Grouping . The default value specifies Without Grouping.

With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call.

Step 5

Click OK .

The CDR-CMR Search Results window displays. The system only displays the oldest 100 records that fall into the date range
                                             that you configured in Step 3 .

Step 6

To view the CMR data, click Others . To view both the CDR and CMR data fields, click View .

Step 7

To mail the report to e-mail recipient(s), follow the steps in the Mail Reports .

### Generate CDR Search by Gateway

Only CAR administrators use the CDR Search by Gateway feature.

This section describes how to search CDR data based on a specific gateway type or on those gateways that use a chosen route
                                 pattern.

Step 1

Choose CDR > Search > By Gateway .

The CDR Search by Gateway window displays.

Step 2

Perform one of the following tasks:

To display all the gateways that are configured in the system, click Gateway Types in the Gateway Types and Route Patterns pane.

To expand the tree structure and display the type of gateway from which you can choose, click the icon next to Gateway types.

To choose a gateway that uses a particular route pattern/hunt pilot, rather than a gateway type, click Route Patterns/Hunt Pilots in the Gateway Types and Route Patterns pane. The gateways that are associated with the configured Route Patterns/Hunt Pilots
                                                display.

To expand the tree structure and display route pattern/hunt pilot for you to choose, click the icon next to Route Patterns/Hunt
                                                Pilots.

You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string.

Step 3

Choose a gateway type from the list.

The gateway name displays in the List of Gateways box.

The List of Gateways box displays up to 200 gateways that are configured for the chosen gateway type.

Step 4

In the List of Gateways box, choose the gateways that you want to include in the report.

You can generate a report for up to 15 gateways at a time. If you choose more than 15 gateways, you will receive a message
                                                         that states "Select 15 or fewer gateways to generate new report."

Step 5

To move the chosen gateway to the list of Selected Gateways box, click the down arrow.

The gateway that you chose displays in the Selected Gateways box.

Step 6

Choose the date and time range of the period during which you want to search for CDR data. The current time displays in both
                                          Coordinated Universal Time (UTC) and local time and uses the following rules:

The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00.

The default FromDate and ToDate values display in UTC time.

The default ToDate specifies the current time of the server in UTC time.

The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, the
                                                FromDate default value = January 15, 2007 11:00:00 (all times in UTC).

Step 7

Choose whether to run the CDR Search report with grouping or without grouping. If you chose with grouping, check the check
                                          box beside With Grouping . The default specifies Without Grouping.

With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call.

Step 8

Click OK .

The CDR-CMR Results window displays. The system only displays the oldest 100 records that fall into the date and time range
                                             that you configured in Step 6 . If more than 100 records are returned, the system truncates the results.

Step 9

To view the CMR data, click Others . To view both the CDR and CMR data fields, click View .

Step 10

To mail the report to e-mail recipient(s), follow the steps in the Mail Reports .

### Generate CDR Search by Cause for Call Termination

Only CAR administrators use the CDR Search by Cause for Call Termination feature. The following tables contain the call termination
                                 cause codes by which you may search.

Code

Description

0

No error

1

Unallocated (unassigned) number

2

No route to specified transit network (national use)

3

No route to destination

4

Send special information tone

5

Misdialed trunk prefix (national use)

6

Channel unacceptable

7

Call awarded and being delivered in an established channel

8

Preemption

9

Preemption - circuit reserved for reuse

16

Normal call clearing

17

User busy

18

No user responding

19

No answer from user (user alerted)

20

Subscriber absent

21

Call rejected

22

Number changed

26

Non-selected user clearing

27

Destination out of order

28

Invalid number format (address incomplete)

29

Facility rejected

30

Response to STATUS ENQUIRY

31

Normal, unspecified

34

No circuit/channel available

38

Network out of order

39

Permanent frame mode connection out of service

40

Permanent frame mode connection operational

41

Temporary failure

42

Switching equipment congestion

43

Access information discarded

44

Requested circuit/channel not available

46

Precedence call blocked

47

Resource unavailable, unspecified

49

Quality of Service not available

50

Requested facility not subscribed

53

Service operation violated

54

Incoming calls barred

55

Incoming calls barred within Closed User Group (CUG)

57

Bearer capability not authorized

58

Bearer capability not presently available

62

Inconsistency in designated outgoing access information and subscriber class

63

Service or option not available, unspecified

65

Bearer capability not implemented

66

Channel type not implemented

69

Requested facility not implemented

70

Only restricted digital information bearer capability is available (national use)

79

Service or option not implemented, unspecified

81

Invalid call reference value

82

Identified channel does not exist

83

A suspended call exists, but this call identity does not

84

Call identity in use

85

No call suspended

86

Call having the requested call identity has been cleared

87

User not member of CUG (Closed User Group)

88

Incompatible destination

90

Destination number missing and DC not subscribed

91

Invalid transit network selection (national use)

95

Invalid message, unspecified

96

Mandatory information element is missing

97

Message type nonexistent or not implemented

98

Message is not compatible with the call state, or the message type is nonexistent or not implemented

99

An information element or parameter does not exist or is not implemented

100

Invalid information element contents

101

The message is not compatible with the call state

102

Call terminated when timer expired; a recovery routine executed to recover from the error

103

Parameter nonexistent or not implemented - passed on (national use)

110

Message with unrecognized parameter discarded

111

Protocol error, unspecified

122

Precedence Level Exceeded

123

Device not Preemptable

125

Out of bandwidth (Cisco specific)

126

Call split (Cisco specific)

127

Interworking, unspecified

129

Precedence out of bandwidth

Decimal Value Code

Hex Value Code

Description

262144

0x40000

Conference Full (was 124)

393216

0x60000

Call split (was 126) This code applies when a call terminates during a transfer operation because it was split off and terminated
                                             (was not part of the final transferred call). This can help determine which calls terminated as part of a feature operation.

458752

0x70000

Conference drop any party/Conference drop last party (was 128)

16777257

0x1000029

CCM_SIP_400_BAD_REQUEST

33554453

0x2000015

CCM_SIP_401_UNAUTHORIZED

50331669

0x3000015

CCM_SIP_402_PAYMENT_REQUIRED

67108885

0x4000015

CCM_SIP_403_FORBIDDEN

83886081

0x5000001

CCM_SIP_404_NOT_FOUND

100663359

0x600003F

CCM_SIP_405_METHOD_NOT_ALLOWED

117440591

0x700004F

CCM_SIP_406_NOT_ACCEPTABLE

134217749

0x8000015

CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED

150995046

0x9000066

CCM_SIP_408_REQUEST_TIMEOUT

184549398

0xB000016

CCM_SIP__410_GONE

201326719

0xC00007F

CCM_SIP_411_LENGTH_REQUIRED

234881151

0xE00007F

CCM_SIP_413_REQUEST_ENTITY_TOO_LONG

251658367

0xF00007F

CCM_SIP_414_REQUEST_URI_TOO_LONG

268435535

0x1000004F

CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE

285212799

0x1100007F

CCM_SIP_416_UNSUPPORTED_URI_SCHEME

83886207

0x1500007F

CCM_SIP_420_BAD_EXTENSION

369098879

0x1600007F

CCM_SIP_421_EXTENSION_REQUIRED

402653311

0x1800007F

CCM_SIP_423_INTERVAL_TOO_BRIEF

419430421

0x19000015

CCM_SIP_424_BAD_LOCATION_INFO

1073741842

0x40000012

CCM_SIP_480_TEMPORARILY_UNAVAILABLE

1090519081

0x41000029

CCM_SIP_481_CALL_LEG_DOES_NOT_EXIST

1107296281

0x42000019

CCM_SIP_482_LOOP_DETECTED = 0x42000000 + EXCHANGE_ROUTING_ERROR

1124073497

0x43000019

CCM_SIP_483_TOO_MANY_HOOPS

1140850716

0x4400001C

CCM_SIP_484_ADDRESS_INCOMPLETE

1157627905

0x45000001

CCM_SIP_485_AMBIGUOUS

1174405137

0x46000011

CCM_SIP_486_BUSY_HERE

1191182367

0x4700001F

CCM_SIP_487_REQUEST_TERMINATED

1207959583

0x4800001F

CCM_SIP_488_NOT_ACCEPTABLE_HERE

1258291217

0x4B000011

CCM_SIP_491_REQUEST_PENDING

1291845649

0x4D000011

CCM_SIP_493_UNDECIPHERABLE

1409286185

0x54000029

CCM_SIP_500_SERVER_INTERNAL_ERROR

1442840614

0x56000026

CCM_SIP_502_BAD_GATEWAY

1459617833

0x57000029

CCM_SIP_503_SERVICE_UNAVAILABLE

-1493172161

0xA700003F

CCM_SIP_503_SERVICE_UNAVAILABLE_SER_OPTION_NOAVAIL

1476395110

0x58000066

CCM_SIP__504_SERVER_TIME_OUT

1493172351

0x5900007F

CCM_SIP_505_SIP_VERSION_NOT_SUPPORTED

1509949567

0x5A00007F

CCM_SIP_513_MESSAGE_TOO_LARGE

2701131793

0xA1000011

CCM_SIP_600_BUSY_EVERYWHERE

2717909013

0xA2000015

CCM_SIP_603_DECLINE

2734686209

0xA3000001

CCM_SIP_604_DOES_NOT_EXIST_ANYWHERE

2751463455

0xA400001F

CCM_SIP_606_NOT_ACCEPTABLE

This section describes how to search for information about the cause for termination of a call.

Step 1

Choose CDR > Search > By Cause for Call Termination .

The Cause for Call Termination window displays.

Step 2

To search for the cause(s) of the termination of a call, highlight the cause(s) in the list of call termination causes.

Tip

You can select more than one cause by clicking the causes that you want while holding down the Ctrl key on your keyboard.
                                                         You can also select all causes in the list by holding down the Shift key while clicking all causes.

Step 3

With the desired cause(s) highlighted, click the down arrow above the Selected Call Termination Causes box.

The cause(s) that you selected displays in the Selected Call Termination Causes list box.

To view a complete list of Call Termination Causes, see the "Call Termination Cause Codes" section in the Cisco Unified Communications Manager Call Detail Records Administration Guide .

Step 4

Choose the date and time range of the period during which you want to search CDR data. When you configure the time range,
                                          use UTC.

Step 5

Choose whether to run the CDR Search report with grouping or without grouping. If you chose with grouping, check the box beside With Grouping . The default specifies Without Grouping.

With Grouping choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call.

Step 6

Click OK .

The Call Termination Details window displays the report criteria for which the report was generated, along with the total
                                             number of calls that were placed during the given time range as well as how many call legs and the percentage of call legs
                                             for each cause code that is selected. The system displays only the oldest 100 records that fall into the date and time ranges
                                             that you configured in Step 4 . If more than 100 records are returned, the system truncates the results.

Step 7

To view CDRs, see the View Call Termination Details .

### View Call Termination Details

This section describes how to view the call termination details.

#### Before you begin

Follow the steps in the Generate CDR Search by Cause for Call Termination to display the Call Termination Details window.

Step 1

In the Select CDRs field, check the check box beside the individual CDRs that you want to view or if you want to view all
                                          CDRs in the list, check the Select CDRs check box.

Step 2

After you have chosen the CDRs that you want to view, click View CDRs .

The CDR-CMR Search Results window displays.

To view the media information and the CDR-CMR dump records, click Others and View links.

Step 3

To print information that displays on the window, click Edit in your browser. Right-click Select All to highlight the section of the report that you want to print. Click Print .

Step 4

To mail the report in an e-mail, click Send Report and follow the procedure that is described in the Mail Reports .

### Generate CDR Search by Call Precedence

Only CAR administrators use the CDR Search by Call Precedence Levels feature.

This section describes how to search for calls according to call precedence.

Step 1

Choose CDR > Search > By Call Precedence Level .

The CDR Search by Precedence Levels window displays.

Step 2

In Select Precedence Levels , check the check boxes for the call precedence levels on which you want to search as described in the following table.

Voice Quality

Description

Flash Override

Highest precedence setting for MLPP calls.

Flash

Second highest precedence setting for MLPP calls.

Immediate

Third highest precedence setting for MLPP calls.

Priority

Fourth highest precedence setting for MLPP calls.

Routine

Lowest precedence setting for MLPP calls.

The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report.

To check the check boxes of every precedence level, click Select All . To clear the check boxes, click Clear All .

Step 3

In the From Date field, choose the date and time from which you want CDRs searched. The current time displays in both Coordinated Universal
                                          Time (UTC) and local time and uses the following rules:

The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00.

The default FromDate and ToDate values display in UTC time.

The default ToDate specifies the current time of the server in UTC time.

The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, then
                                                the FromDate default value = January 15, 2007 11:00:00 (all times in UTC).

Step 4

In the To Date field, choose the date and time to which you want CDRs searched.

Step 5

Choose whether to run the CDR Search report With Grouping or Without Grouping. If you chose. With Grouping, check the check
                                          box beside With Grouping . The default value specifies Without Grouping.

With Grouping, choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call.

Step 6

Click OK .

The Call Precedence Details window displays and shows the call precedence levels and values, number of call legs, and percentage
                                             of call legs.

Step 7

In the Select CDRs column, check the check boxes of the CDRs at which you want to look.

Step 8

Click View CDRs .

The CDR-CMR Search by Precedence Levels - CDR-CMR Search Results window displays. The system displays only the oldest 100
                                             records that fall into the date and time ranges that you configured in Step 3 and Step 3 Step 4 . If more than 100 records are returned, the system truncates the results.

Step 9

To view the CMR data, click Others . To view both the CDR and CMR data fields, click View .

Step 10

To mail the report to e-mail recipient, click Send Report and follow the steps in the Mail Reports .

### Generate CDR Search for Malicious Calls

Only CAR administrators use the CDR Search for Malicious Calls feature.

This section describes how to search for malicious calls.

Step 1

Choose CDR > Search > Malicious Calls .

The CDR Search for Malicious Calls window displays.

Step 2

Perform one of the following tasks:

In the Select Phone Number/SIP URL(s) box, enter the phone number or SIP URL in the Phone Number/SIP URL field and click Add Phone Number/SIP URL .

The phone number or SIP URL of the user displays in the Selected Phone Number/SIP URL(s) box.

To search for a user phone number or SIP URL, click the Search Internal Phone Number/SIP URL based User link, enter the first few letters of the first and/or last name in the First Name and/or Last Name fields, and click the Search button. When the results display, click the Select link next to the result that you want to include. The phone number or SIP URL of the user displays in the Selected Phone
                                                Number/SIP URLs box. Click Close .

To remove the phone number or SIP URL, highlight the phone number or SIP URL that you want to remove and click Remove Phone Number/SIP URL(s) . To remove all phone numbers or SIP URL(s), click Remove All Phone Number/SIP URL(s) .

Step 3

Choose the date and time range of the period when you want to search for CDR data. The current time displays in both Coordinated
                                          Universal Time (UTC) and local time and uses the following rules:

The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00.

The default FromDate and ToDate values display in UTC time.

The default ToDate specifies the current time of the server in UTC time.

The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, then
                                                the FromDate default value = January 15, 2007 11:00:00 (all times in UTC).

Step 4

Choose whether to run the CDR Search report With Grouping or Without Grouping. If you chose with grouping, check the box beside With Grouping . The default value specifies Without Grouping

With Grouping means that the system returns CDR records that match the date and time range for the search and groups them
                                                         with their associated records. Without Grouping returns all the CDR records that match the date and time range without grouping
                                                         all the associated records for each call together.

Step 5

Click OK .

The CDR-CMR Search Results window displays. The system only displays the oldest 100 records that fall into the date and time
                                             ranges that you configured in Step 3 . If more than 100 records are returned, the system truncates the results.

Step 6

To view the CMR data, click Others . To view both the CDR and CMR data fields, click View .

Step 7

To mail the report to e-mail recipients, follow the steps in the Mail Reports .

### Generate CDR Search for Call Types

Only CAR administrators use the CDR Search for Different Call Types feature.

This section describes how to search for different call types.

Step 1

Choose CDR > Search > By Call Types .

The CDR Search for Different Call Types window displays.

You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9.

Step 2

Choose the call type from the Select Call Type drop down list.

The following is a list of the call types:

Successful IME Call : Calls that were successfully routed through IME trunks.

Failed IME Calls : Calls that tried to route through the IME trunk, but failed.

IME Calls with Fallback to Alternate Route : Calls which were initially routed through the IME trunk, but due to some reason (for example, poor QoS), the fallback mechanism
                                                   was initiated and these calls were re-routed mid-call to an alternate route. The alternate route is typically a PSTN route.

Successful Fallback Calls to Alternate Route : Calls which successfully fell back to the alternate route. The alternate route is typically a PSTN route.

Failed Fallback Calls to Alternate Route : Calls which failed to fall back to the alternate route.

Calls on Alternate Route due to IME Redirection : Calls that tried to route (at call setup) to IME, but for some reason were routed to an alternate route. The alternate route
                                                   is typically a PSTN route.

Step 3

Perform one of the following tasks:

To search CDRs based on phone numbers/SIP URLs, enter the phone number or SIP URL in the Phone Number/SIP URL field and click Add Phone Number/SIP URL .

To search CDRs based on user, click the Search Internal Phone Number/SIP URL based User link, enter the first few letters of the first and/or the last name in the First Name and/or Last Name fields, and click Search . When the results display, click the Select link next to the result that you want to include. Click Close .

The phone number or SIP URL displays in the Selected Phone Number/SIP URL(s) box.

To delete an item from the Report Criteria box, click the Remove Phone Number/SIP URL(s) button. You can delete all items from the Report Criteria box by clicking the Remove All Phone Number/SIP URL(s) .

Step 4

Current time displays in both Coordinated Universal Time (UTC) and local time. The UTC and local time comprise a numeric string
                                          of mmddyyyy hhmmss, as in January 15, 2007 12:00:00.

Step 5

From the Select TimeZone field, choose the time zone that you want to use to search the CDRs. Options include your local time zone and Greenwich Mean
                                          Time (GMT).

Step 6

In the From Date field and the To Date field, choose the date and time from and to which you want to search the CDRs, respectively. The times in the From and To
                                          fields use the following rules:

The default FromDate and ToDate values display in UTC time.

The default ToDate specifies the current time of the server in UTC time.

The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, then
                                                the FromDate default value = January 15, 2007 11:00:00 (all times in UTC).

Step 7

Click OK .

The CDR-CMR Search Results window displays. The system displays only the oldest 100 records that fall into the date and time
                                             ranges that you configured in Step 3 and Step 4. If more than 100 records are returned, the system truncates the results.

Step 8

To view the CMR data, click Others . To view both the CDR and CMR data fields, click View .

Step 9

To mail the report to e-mail recipient(s), click Send Report and follow the steps in the Mail Reports .

## CDR Search Results

The CDR search allows users to view the CDR/CMR fields as described in the table. The CDR search retrieves the CDR/CMR files
                              from the tbl_billing_data and tbl_billing_error tables of the CAR database.

See the following table.

Field

Description

Sl No

Specifies the serial or record number.

Call Type

Specifies the type of call: simple, transfer, forward, pickup, conference, refer, replaces, or redirection.

GCID_CMIdGCID_CallId

Specifies the call identifiers that are associated with all the records for the entire call.

Orig Node IdDest Node Id

Specifies the server where the call originator/destination was registered at the time of the call.

Orig Leg IdDest Leg Id

Specifies the unique identifiers to the originating/destination leg of a call.

Calling NoCalling No Partition

The calling number specifies the directory number where the call originated. The calling partition specifies the partition
                                          that is associated with the calling party.

Called NoCalled No Partition

The called number specifies the directory number from which the call was initially placed and is the same as the Dest No when
                                          the call is not transferred or forwarded. The called partition specifies the partition that is associated with the called
                                          party.

Dest NoDest No Partition

The destination number specifies the directory number where the call finally terminated and is the same as the called number
                                          when the call is not transferred or forwarded. The destination number partition specifies the partition that is associated
                                          with the destination number.

Last Rd NoLast Rd No Partition

The last redirected number specifies the directory number from which the call was finally redirected. The last redirected
                                          number partition specifies the partition that is associated with the last redirected number.

Media InfoOrig Pkts Rcd Dest Pkts Rcd Orig Pkts Lost Dest Pkts Lost

Specifies the packets that were received or lost for the origination or destination leg of a call and a link to the media
                                          information.

CDR - CMR Dump

Specifies a link to the CDR and CDR dump tables. This link allows the users to view the values in the CDR/CMR fields.

### Media Information

The media information table provides the following information. See the table.

Field

Description

Origination Leg

A unique identifier for the originating leg of a call.

Destination Leg

A unique identifier for the destination leg of a call.

Parameter

The media parameters MediaTransportAdd_Ip, PayLoadCapability, MediaCap_g723BitRate, Packets Sent, Octets Sent, Packets Received,
                                             Octets Received, Packets Lost, Jitter, Latency, QoS, VideoCap_Codec, VideoCap_Bandwidth, VideoCap_Resolution, VideoTransportAddress_IP,
                                             and VideoTransportAddress_Port

Origination

The value for all the preceding parameters for the origination leg of the call.

Destination

The value for all the preceding parameters for the destination leg of the call.

### CDR and CMR Dump Tables

The CDR and CMR dump tables provide the following information. See the following table.

You can view the content of the voice quality metrics field, varVQMetrics, in the Origination CMR and Destination CMR fields.

Field

Description

CDR

This field specifies the call detail record fields.

Origination CMR

Only a single set of fields for origination and destination exists. You can find the origination or destination CMR by using
                                             the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR, the following record represents Orig/Dest CMR.

Destination CMR

Only a single set of fields for origination and destination exists. You can find the origination or destination CMR by using
                                             the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR, the following record represents Orig/Dest CMR.

The following example displays output from a CDR dump file:

#### Sample CDR Dump File Output

cdrRecordType, globalCallID_callManagerId, globalCallID_callId, origLegCallIdentifier, dateTimeOrigination, origNodeId, origSpan,
                                 origIpAddr, callingPartyNumber, callingPartyUnicodeLoginUserID, origCause_location, origCause_value, origPrecedenceLevel,
                                 origMediaTransportAddress_IP, origMediaTransportAddress_Port, origMediaCap_payloadCapability, origMediaCap_maxFramesPerPacket,
                                 origMediaCap_g723BitRate, origVideoCap_Codec, origVideoCap_Bandwidth, origVideoCap_Resolution, origVideoTransportAddress_IP,
                                 origVideoTransportAddress_Port, origRSVPAudioStat, origRSVPVideoStat, destLegIdentifier, destNodeId, destSpan, destIpAddr,
                                 originalCalledPartyNumber, finalCalledPartyNumber, finalCalledPartyUnicodeLoginUserID, destCause_location, destCause_value,
                                 destPrecedenceLevel, destMediaTransportAddress_IP, destMediaTransportAddress_Port, destMediaCap_payloadCapability, destMediaCap_maxFramesPerPacket,
                                 destMediaCap_g723BitRate, destVideoCap_Codec, destVideoCap_Bandwidth, destVideoCap_Resolution, destVideoTransportAddress_IP,
                                 destVideoTransportAddress_Port, destRSVPAudioStat, destRSVPVideoStat, dateTimeConnect, dateTimeDisconnect, lastRedirectDn,
                                 pkid, originalCalledPartyNumberPartition, callingPartyNumberPartition, finalCalledPartyNumberPartition, lastRedirectDnPartition,
                                 duration, origDeviceName, destDeviceName, origCallTerminationOnBehalfOf, destCallTerminationOnBehalfOf, origCalledPartyRedirectOnBehalfOf,
                                 lastRedirectRedirectOnBehalfOf, origCalledPartyRedirectReason, lastRedirectRedirectReason, destConversationId, globalCallId_ClusterID,
                                 joinOnBehalfOf, comment, authCodeDescription, authorizationLevel, clientMatterCode, origDTMFMethod, destDTMFMethod, callSecuredStatus,
                                 origConversationId, origMediaCap_Bandwidth, destMediaCap_Bandwidth, authorizationCodeValue, outpulsedCallingPartyNumber, outpulsedCalledPartyNumber,
                                 origIpv4v6Addr, destIpv4v6Addr, origVideoCap_Codec_Channel2, origVideoCap_Bandwidth_Channel2, origVideoCap_Resolution_Channel2,
                                 origVideoTransportAddress_IP_Channel2, origVideoTransportAddress_Port_Channel2, origVideoChannel_Role_Channel2, destVideoCap_Codec_Channel2,
                                 destVideoCap_Bandwidth_Channel2, destVideoCap_Resolution_Channel2, destVideoTransportAddress_IP_Channel2, destVideoTransportAddress_Port_Channel2,
                                 destVideoChannel_Role_Channel2, IncomingProtocolID, IncomingProtocolCallRef, OutgoingProtocolID, OutgoingProtocolCallRef,
                                 currentRoutingReason, origRoutingReason, lastRedirectingRoutingReason, huntPilotPartition, huntPilotDN

INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, VARCHAR(50), VARCHAR(128), INTEGER, INTEGER, INTEGER,
                                 INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, VARCHAR(64), VARCHAR(64), INTEGER,
                                 INTEGER, INTEGER, INTEGER, VARCHAR(50), VARCHAR(50), VARCHAR(128), INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER,
                                 INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, VARCHAR(64), VARCHAR(64), INTEGER, INTEGER, VARCHAR(50), UNIQUEIDENTIFIER,
                                 VARCHAR(50), VARCHAR(50), VARCHAR(50), VARCHAR(50), INTEGER, VARCHAR(129), VARCHAR(129), INTEGER, INTEGER, INTEGER, INTEGER,
                                 INTEGER, INTEGER, INTEGER, VARCHAR(50), INTEGER, VARCHAR(2048), VARCHAR(50), INTEGER, VARCHAR(32), INTEGER, INTEGER, INTEGER,
                                 INTEGER, INTEGER, INTEGER, VARCHAR(32), VARCHAR(50), VARCHAR(50), VARCHAR(64), VARCHAR(64), INTEGER, INTEGER, INTEGER, INTEGER,
                                 INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, VARCHAR(32), INTEGER, VARCHAR(32), INTEGER,
                                 INTEGER, INTEGER, VARCHAR(50), VARCHAR(50)

1, 1, 37, 29654625, 1258090294, 1, 0, 136269066, 1001, caruser2, 0, 16, 4, 136269066, 16790, 4, 20, 0, 0, 0, 0, 0, 0, 0, 0,
                                 29654626, 1, 0, 85937418, 5555, 1002, caruser1, 0, 0, 4, 85937418, 30844, 4, 20, 0, 0, 0, 0, 0, 0, 0, 0, 1258090296, 1258090383,
                                 5555, dcf0b5c9-7d57-475b-b166-d207a6617f34, , , , , 87, SEP003094C3CCB0, SEP0002FD3BA528, 12, 0, 0, 0, 0, 0, 0, StandAloneCluster,
                                 0, , , 0, , 3, 3, 0, 0, 64, 64, , , , 10.77.31.8, 10.77.31.5, 101,0,5,0,0,1,100,0,3,0,0,1,3,0000000000000108012BB4AE00000002,3,0000000000000108012BB4B200000000,2,5,7,1000,
                                 5555

| Step 1 | From CDR Analysis and Reporting, choose CDR > Export CDR/CMR . The Export CDR/CMR records window appears. |
|---|---|
| Step 2 | In the From Date and To Date drop-down list boxes, choose a date range for the CDR/CMR dump. |
| Step 3 | In Select records, check the CDR records and/or CMR records check box. |
| Step 4 | Click Export to File . The Export CDR/CMR records Result window appears. See the View CDR and CMR Records Results . |

| Step 1 | From the Export CDR/CMR Record Results window, right-click either the CDR Dump or CMR Dump link. A popup window that comprises the following options displays: Open - This option allows you to open the window that contains the CDR/CMR dump in the same window. Open in a New Window - This option allows you to open the window that contains the CDR/CMR dump in a new window. Save Target As... - This option allows you to save the CDR/CMR dump to a location on your computer. Print Target - This option allows you to print the CDR/CMR dump information. Copy Shortcut - This option allows you to copy the window shortcut to paste in another file. Add to Favorites - This option allows you to add the CDR/CMR dump to your Favorites folder. Properties - This option provides the properties of the CDR/CMR dump file. |
|---|---|
| Step 2 | From the pop-up window, choose one of the options. |
| Step 3 | If you chose to save the CDR/CMR dump to your computer, choose a location in which to save the dump and click Save . After the download is complete, you can locate the file wherever you download it to open it. |
| Step 4 | To delete the CDR and/or CMR dump, check Delete File check box and click Back or Close . The files get deleted. Note If you do not check the Delete File check box(es) (for example, if the CDR or CMR dump files get left undeleted), the background
                                                         process deletes the files daily. Because the CDR and CMR dump files are large, Cisco recommends that you download the file
                                                         to a local disk and delete them from the server to avoid the disk usage on the server side. | Note | If you do not check the Delete File check box(es) (for example, if the CDR or CMR dump files get left undeleted), the background
                                                         process deletes the files daily. Because the CDR and CMR dump files are large, Cisco recommends that you download the file
                                                         to a local disk and delete them from the server to avoid the disk usage on the server side. |
| Note | If you do not check the Delete File check box(es) (for example, if the CDR or CMR dump files get left undeleted), the background
                                                         process deletes the files daily. Because the CDR and CMR dump files are large, Cisco recommends that you download the file
                                                         to a local disk and delete them from the server to avoid the disk usage on the server side. |

| Note | If you do not check the Delete File check box(es) (for example, if the CDR or CMR dump files get left undeleted), the background
                                                         process deletes the files daily. Because the CDR and CMR dump files are large, Cisco recommends that you download the file
                                                         to a local disk and delete them from the server to avoid the disk usage on the server side. |
|---|---|

| Note | When the disk allocation usage exceeds the configured high water mark threshold value, LMP also purges the CDR and CMR data
                                             that are exported at the following path automatically: /var/log/active/tomcat/logs/car/carreports/reports/ondemand/temp . Customers or any third-party applications should ensure to retrieve the exported files immediately to avoid losing their buffered
                                             historical data. |
|---|---|

| Name | Severity | Description |
|---|---|---|
| CDRFileDeliveryFailed | ERROR_ALARM | SFTP delivery of CDR files to the outside billing server failed. |
| CDRAgentSendFileFailed | ERROR_ALARM | The CDR Agent cannot send CDR files from the Cisco Unified CM node to the CDR Repository node within the Unified Communications Manager cluster. |
| CDRHWMExceeded | WARNING_ALARM | The high water mark (HWM) for CDR files was reached; some successfully delivered CDR files have been deleted. |
| CDRMaximumDiskSpaceExceeded | CRITICAL_ALARM | The CDR files disk usage exceeded the maximum disk allocation. Some undelivered files may have been deleted to bring disk
                                             usage down. |
| CDRFileDeliveryFailureContinues | ERROR_ALARM | SFTP delivery of CDR files failed on retries. |
| CDRAgentSendFileFailureContinues | ERROR_ALARM | The CDR Agent cannot send CDR files from the Cisco Unified CM node to the CDR Repository node on retries. |

| Note | CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. However, only
                                       CAR administrators can use CDR Search. |
|---|---|

| Note | After you log in to the CAR main window, the following warning may display if Unified Communications Manager is also activated: "Warning: In some servers in this cluster the CDR Enabled Flag is false and so CDR entries may not be generated for all the
                                             calls that are made in this cluster." Some clusters have multiple nodes where some of the nodes do not run Unified Communications Manager services. This warning checks all nodes in the cluster regardless of Unified Communications Manager service activation status. Ignore the warning after manually checking the CDR Enabled Flag parameter settings for all the Unified Communications Manager service subscribers. |
|---|---|

| Step 1 | Choose CDR > Search > By User/Phone Number/SIP URL . The CDR Search window displays. Note You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. | Note | You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. |
|---|---|---|---|
| Note | You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. |
| Step 2 | Perform one of the following tasks: To search CDRs based on Internal Phone Number/SIP URLs, enter the value in the Phone Number/SIP URL field and click Add Phone Number/SIP URL . To search CDRs based on user, click the Search Internal Phone Number/SIP URL based User link, enter the first few letters of the first and/or the last name in the First Name and/or the Last Name fields, and click Search . When the results display, click the Select link next to the result that you want to include. Click Close . The phone number or SIP URL displays in the Phone Number/SIP URL(s) box. Note To delete an item from the Report Criteria box, click Remove Phone Number/SIP URL(s) . You can delete all items from the Report Criteria box by clicking Remove All Phone Number/SIP URL(s) . | Note | To delete an item from the Report Criteria box, click Remove Phone Number/SIP URL(s) . You can delete all items from the Report Criteria box by clicking Remove All Phone Number/SIP URL(s) . |
| Note | To delete an item from the Report Criteria box, click Remove Phone Number/SIP URL(s) . You can delete all items from the Report Criteria box by clicking Remove All Phone Number/SIP URL(s) . |
| Step 3 | Choose the date and time range of the period for which you want to see CDR data for the specified user or phone number or
                                          SIP URL. The current time displays in both Coordinated Universal Time (UTC) and local time and uses the following rules: The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00. The default FromDate and ToDate values display in UTC time. The default ToDate specifies the current time of the server in UTC time. The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, the
                                                FromDate default value = January 15, 2007 11:00:00 (all times in UTC). |
| Step 4 | Choose whether to run the CDR Search report with grouping or without grouping. If you choose with grouping, check the check
                                          box beside With Grouping . The default value specifies Without Grouping. Note With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. | Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Step 5 | Click OK . The CDR-CMR Search Results window displays. The system only displays the oldest 100 records that fall into the date range
                                             that you configured in Step 3 . |
| Step 6 | To view the CMR data, click Others . To view both the CDR and CMR data fields, click View . |
| Step 7 | To mail the report to e-mail recipient(s), follow the steps in the Mail Reports . |

| Note | You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. |
|---|---|

| Note | To delete an item from the Report Criteria box, click Remove Phone Number/SIP URL(s) . You can delete all items from the Report Criteria box by clicking Remove All Phone Number/SIP URL(s) . |
|---|---|

| Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
|---|---|

| Step 1 | Choose CDR > Search > By Gateway . The CDR Search by Gateway window displays. |
|---|---|
| Step 2 | Perform one of the following tasks: To display all the gateways that are configured in the system, click Gateway Types in the Gateway Types and Route Patterns pane. To expand the tree structure and display the type of gateway from which you can choose, click the icon next to Gateway types. To choose a gateway that uses a particular route pattern/hunt pilot, rather than a gateway type, click Route Patterns/Hunt Pilots in the Gateway Types and Route Patterns pane. The gateways that are associated with the configured Route Patterns/Hunt Pilots
                                                display. To expand the tree structure and display route pattern/hunt pilot for you to choose, click the icon next to Route Patterns/Hunt
                                                Pilots. Note You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. | Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
| Step 3 | Choose a gateway type from the list. The gateway name displays in the List of Gateways box. Note The List of Gateways box displays up to 200 gateways that are configured for the chosen gateway type. | Note | The List of Gateways box displays up to 200 gateways that are configured for the chosen gateway type. |
| Note | The List of Gateways box displays up to 200 gateways that are configured for the chosen gateway type. |
| Step 4 | In the List of Gateways box, choose the gateways that you want to include in the report. Note You can generate a report for up to 15 gateways at a time. If you choose more than 15 gateways, you will receive a message
                                                         that states "Select 15 or fewer gateways to generate new report." | Note | You can generate a report for up to 15 gateways at a time. If you choose more than 15 gateways, you will receive a message
                                                         that states "Select 15 or fewer gateways to generate new report." |
| Note | You can generate a report for up to 15 gateways at a time. If you choose more than 15 gateways, you will receive a message
                                                         that states "Select 15 or fewer gateways to generate new report." |
| Step 5 | To move the chosen gateway to the list of Selected Gateways box, click the down arrow. The gateway that you chose displays in the Selected Gateways box. |
| Step 6 | Choose the date and time range of the period during which you want to search for CDR data. The current time displays in both
                                          Coordinated Universal Time (UTC) and local time and uses the following rules: The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00. The default FromDate and ToDate values display in UTC time. The default ToDate specifies the current time of the server in UTC time. The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, the
                                                FromDate default value = January 15, 2007 11:00:00 (all times in UTC). |
| Step 7 | Choose whether to run the CDR Search report with grouping or without grouping. If you chose with grouping, check the check
                                          box beside With Grouping . The default specifies Without Grouping. Note With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. | Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Step 8 | Click OK . The CDR-CMR Results window displays. The system only displays the oldest 100 records that fall into the date and time range
                                             that you configured in Step 6 . If more than 100 records are returned, the system truncates the results. |
| Step 9 | To view the CMR data, click Others . To view both the CDR and CMR data fields, click View . |
| Step 10 | To mail the report to e-mail recipient(s), follow the steps in the Mail Reports . |

| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
|---|---|

| Note | The List of Gateways box displays up to 200 gateways that are configured for the chosen gateway type. |
|---|---|

| Note | You can generate a report for up to 15 gateways at a time. If you choose more than 15 gateways, you will receive a message
                                                         that states "Select 15 or fewer gateways to generate new report." |
|---|---|

| Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search, and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
|---|---|

| Code | Description |
|---|---|
| 0 | No error |
| 1 | Unallocated (unassigned) number |
| 2 | No route to specified transit network (national use) |
| 3 | No route to destination |
| 4 | Send special information tone |
| 5 | Misdialed trunk prefix (national use) |
| 6 | Channel unacceptable |
| 7 | Call awarded and being delivered in an established channel |
| 8 | Preemption |
| 9 | Preemption - circuit reserved for reuse |
| 16 | Normal call clearing |
| 17 | User busy |
| 18 | No user responding |
| 19 | No answer from user (user alerted) |
| 20 | Subscriber absent |
| 21 | Call rejected |
| 22 | Number changed |
| 26 | Non-selected user clearing |
| 27 | Destination out of order |
| 28 | Invalid number format (address incomplete) |
| 29 | Facility rejected |
| 30 | Response to STATUS ENQUIRY |
| 31 | Normal, unspecified |
| 34 | No circuit/channel available |
| 38 | Network out of order |
| 39 | Permanent frame mode connection out of service |
| 40 | Permanent frame mode connection operational |
| 41 | Temporary failure |
| 42 | Switching equipment congestion |
| 43 | Access information discarded |
| 44 | Requested circuit/channel not available |
| 46 | Precedence call blocked |
| 47 | Resource unavailable, unspecified |
| 49 | Quality of Service not available |
| 50 | Requested facility not subscribed |
| 53 | Service operation violated |
| 54 | Incoming calls barred |
| 55 | Incoming calls barred within Closed User Group (CUG) |
| 57 | Bearer capability not authorized |
| 58 | Bearer capability not presently available |
| 62 | Inconsistency in designated outgoing access information and subscriber class |
| 63 | Service or option not available, unspecified |
| 65 | Bearer capability not implemented |
| 66 | Channel type not implemented |
| 69 | Requested facility not implemented |
| 70 | Only restricted digital information bearer capability is available (national use) |
| 79 | Service or option not implemented, unspecified |
| 81 | Invalid call reference value |
| 82 | Identified channel does not exist |
| 83 | A suspended call exists, but this call identity does not |
| 84 | Call identity in use |
| 85 | No call suspended |
| 86 | Call having the requested call identity has been cleared |
| 87 | User not member of CUG (Closed User Group) |
| 88 | Incompatible destination |
| 90 | Destination number missing and DC not subscribed |
| 91 | Invalid transit network selection (national use) |
| 95 | Invalid message, unspecified |
| 96 | Mandatory information element is missing |
| 97 | Message type nonexistent or not implemented |
| 98 | Message is not compatible with the call state, or the message type is nonexistent or not implemented |
| 99 | An information element or parameter does not exist or is not implemented |
| 100 | Invalid information element contents |
| 101 | The message is not compatible with the call state |
| 102 | Call terminated when timer expired; a recovery routine executed to recover from the error |
| 103 | Parameter nonexistent or not implemented - passed on (national use) |
| 110 | Message with unrecognized parameter discarded |
| 111 | Protocol error, unspecified |
| 122 | Precedence Level Exceeded |
| 123 | Device not Preemptable |
| 125 | Out of bandwidth (Cisco specific) |
| 126 | Call split (Cisco specific) |
| 127 | Interworking, unspecified |
| 129 | Precedence out of bandwidth |

| Decimal Value Code | Hex Value Code | Description |
|---|---|---|
| 262144 | 0x40000 | Conference Full (was 124) |
| 393216 | 0x60000 | Call split (was 126) This code applies when a call terminates during a transfer operation because it was split off and terminated
                                             (was not part of the final transferred call). This can help determine which calls terminated as part of a feature operation. |
| 458752 | 0x70000 | Conference drop any party/Conference drop last party (was 128) |
| 16777257 | 0x1000029 | CCM_SIP_400_BAD_REQUEST |
| 33554453 | 0x2000015 | CCM_SIP_401_UNAUTHORIZED |
| 50331669 | 0x3000015 | CCM_SIP_402_PAYMENT_REQUIRED |
| 67108885 | 0x4000015 | CCM_SIP_403_FORBIDDEN |
| 83886081 | 0x5000001 | CCM_SIP_404_NOT_FOUND |
| 100663359 | 0x600003F | CCM_SIP_405_METHOD_NOT_ALLOWED |
| 117440591 | 0x700004F | CCM_SIP_406_NOT_ACCEPTABLE |
| 134217749 | 0x8000015 | CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED |
| 150995046 | 0x9000066 | CCM_SIP_408_REQUEST_TIMEOUT |
| 184549398 | 0xB000016 | CCM_SIP__410_GONE |
| 201326719 | 0xC00007F | CCM_SIP_411_LENGTH_REQUIRED |
| 234881151 | 0xE00007F | CCM_SIP_413_REQUEST_ENTITY_TOO_LONG |
| 251658367 | 0xF00007F | CCM_SIP_414_REQUEST_URI_TOO_LONG |
| 268435535 | 0x1000004F | CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE |
| 285212799 | 0x1100007F | CCM_SIP_416_UNSUPPORTED_URI_SCHEME |
| 83886207 | 0x1500007F | CCM_SIP_420_BAD_EXTENSION |
| 369098879 | 0x1600007F | CCM_SIP_421_EXTENSION_REQUIRED |
| 402653311 | 0x1800007F | CCM_SIP_423_INTERVAL_TOO_BRIEF |
| 419430421 | 0x19000015 | CCM_SIP_424_BAD_LOCATION_INFO |
| 1073741842 | 0x40000012 | CCM_SIP_480_TEMPORARILY_UNAVAILABLE |
| 1090519081 | 0x41000029 | CCM_SIP_481_CALL_LEG_DOES_NOT_EXIST |
| 1107296281 | 0x42000019 | CCM_SIP_482_LOOP_DETECTED = 0x42000000 + EXCHANGE_ROUTING_ERROR |
| 1124073497 | 0x43000019 | CCM_SIP_483_TOO_MANY_HOOPS |
| 1140850716 | 0x4400001C | CCM_SIP_484_ADDRESS_INCOMPLETE |
| 1157627905 | 0x45000001 | CCM_SIP_485_AMBIGUOUS |
| 1174405137 | 0x46000011 | CCM_SIP_486_BUSY_HERE |
| 1191182367 | 0x4700001F | CCM_SIP_487_REQUEST_TERMINATED |
| 1207959583 | 0x4800001F | CCM_SIP_488_NOT_ACCEPTABLE_HERE |
| 1258291217 | 0x4B000011 | CCM_SIP_491_REQUEST_PENDING |
| 1291845649 | 0x4D000011 | CCM_SIP_493_UNDECIPHERABLE |
| 1409286185 | 0x54000029 | CCM_SIP_500_SERVER_INTERNAL_ERROR |
| 1442840614 | 0x56000026 | CCM_SIP_502_BAD_GATEWAY |
| 1459617833 | 0x57000029 | CCM_SIP_503_SERVICE_UNAVAILABLE |
| -1493172161 | 0xA700003F | CCM_SIP_503_SERVICE_UNAVAILABLE_SER_OPTION_NOAVAIL |
| 1476395110 | 0x58000066 | CCM_SIP__504_SERVER_TIME_OUT |
| 1493172351 | 0x5900007F | CCM_SIP_505_SIP_VERSION_NOT_SUPPORTED |
| 1509949567 | 0x5A00007F | CCM_SIP_513_MESSAGE_TOO_LARGE |
| 2701131793 | 0xA1000011 | CCM_SIP_600_BUSY_EVERYWHERE |
| 2717909013 | 0xA2000015 | CCM_SIP_603_DECLINE |
| 2734686209 | 0xA3000001 | CCM_SIP_604_DOES_NOT_EXIST_ANYWHERE |
| 2751463455 | 0xA400001F | CCM_SIP_606_NOT_ACCEPTABLE |

| Step 1 | Choose CDR > Search > By Cause for Call Termination . The Cause for Call Termination window displays. |
|---|---|
| Step 2 | To search for the cause(s) of the termination of a call, highlight the cause(s) in the list of call termination causes. Tip You can select more than one cause by clicking the causes that you want while holding down the Ctrl key on your keyboard.
                                                         You can also select all causes in the list by holding down the Shift key while clicking all causes. | Tip | You can select more than one cause by clicking the causes that you want while holding down the Ctrl key on your keyboard.
                                                         You can also select all causes in the list by holding down the Shift key while clicking all causes. |
| Tip | You can select more than one cause by clicking the causes that you want while holding down the Ctrl key on your keyboard.
                                                         You can also select all causes in the list by holding down the Shift key while clicking all causes. |
| Step 3 | With the desired cause(s) highlighted, click the down arrow above the Selected Call Termination Causes box. The cause(s) that you selected displays in the Selected Call Termination Causes list box. Note To view a complete list of Call Termination Causes, see the "Call Termination Cause Codes" section in the Cisco Unified Communications Manager Call Detail Records Administration Guide . | Note | To view a complete list of Call Termination Causes, see the "Call Termination Cause Codes" section in the Cisco Unified Communications Manager Call Detail Records Administration Guide . |
| Note | To view a complete list of Call Termination Causes, see the "Call Termination Cause Codes" section in the Cisco Unified Communications Manager Call Detail Records Administration Guide . |
| Step 4 | Choose the date and time range of the period during which you want to search CDR data. When you configure the time range,
                                          use UTC. |
| Step 5 | Choose whether to run the CDR Search report with grouping or without grouping. If you chose with grouping, check the box beside With Grouping . The default specifies Without Grouping. Note With Grouping choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. | Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Step 6 | Click OK . The Call Termination Details window displays the report criteria for which the report was generated, along with the total
                                             number of calls that were placed during the given time range as well as how many call legs and the percentage of call legs
                                             for each cause code that is selected. The system displays only the oldest 100 records that fall into the date and time ranges
                                             that you configured in Step 4 . If more than 100 records are returned, the system truncates the results. |
| Step 7 | To view CDRs, see the View Call Termination Details . |

| Tip | You can select more than one cause by clicking the causes that you want while holding down the Ctrl key on your keyboard.
                                                         You can also select all causes in the list by holding down the Shift key while clicking all causes. |
|---|---|

| Note | To view a complete list of Call Termination Causes, see the "Call Termination Cause Codes" section in the Cisco Unified Communications Manager Call Detail Records Administration Guide . |
|---|---|

| Note | With Grouping choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
|---|---|

| Step 1 | In the Select CDRs field, check the check box beside the individual CDRs that you want to view or if you want to view all
                                          CDRs in the list, check the Select CDRs check box. |
|---|---|
| Step 2 | After you have chosen the CDRs that you want to view, click View CDRs . The CDR-CMR Search Results window displays. To view the media information and the CDR-CMR dump records, click Others and View links. |
| Step 3 | To print information that displays on the window, click Edit in your browser. Right-click Select All to highlight the section of the report that you want to print. Click Print . |
| Step 4 | To mail the report in an e-mail, click Send Report and follow the procedure that is described in the Mail Reports . |

| Step 1 | Choose CDR > Search > By Call Precedence Level . The CDR Search by Precedence Levels window displays. |
|---|---|
| Step 2 | In Select Precedence Levels , check the check boxes for the call precedence levels on which you want to search as described in the following table. Table 4. Call Precedence Levels Voice Quality Description Flash Override Highest precedence setting for MLPP calls. Flash Second highest precedence setting for MLPP calls. Immediate Third highest precedence setting for MLPP calls. Priority Fourth highest precedence setting for MLPP calls. Routine Lowest precedence setting for MLPP calls. Note The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. Note To check the check boxes of every precedence level, click Select All . To clear the check boxes, click Clear All . | Voice Quality | Description | Flash Override | Highest precedence setting for MLPP calls. | Flash | Second highest precedence setting for MLPP calls. | Immediate | Third highest precedence setting for MLPP calls. | Priority | Fourth highest precedence setting for MLPP calls. | Routine | Lowest precedence setting for MLPP calls. | Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. | Note | To check the check boxes of every precedence level, click Select All . To clear the check boxes, click Clear All . |
| Voice Quality | Description |
| Flash Override | Highest precedence setting for MLPP calls. |
| Flash | Second highest precedence setting for MLPP calls. |
| Immediate | Third highest precedence setting for MLPP calls. |
| Priority | Fourth highest precedence setting for MLPP calls. |
| Routine | Lowest precedence setting for MLPP calls. |
| Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. |
| Note | To check the check boxes of every precedence level, click Select All . To clear the check boxes, click Clear All . |
| Step 3 | In the From Date field, choose the date and time from which you want CDRs searched. The current time displays in both Coordinated Universal
                                          Time (UTC) and local time and uses the following rules: The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00. The default FromDate and ToDate values display in UTC time. The default ToDate specifies the current time of the server in UTC time. The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, then
                                                the FromDate default value = January 15, 2007 11:00:00 (all times in UTC). |
| Step 4 | In the To Date field, choose the date and time to which you want CDRs searched. |
| Step 5 | Choose whether to run the CDR Search report With Grouping or Without Grouping. If you chose. With Grouping, check the check
                                          box beside With Grouping . The default value specifies Without Grouping. Note With Grouping, choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. | Note | With Grouping, choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Note | With Grouping, choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
| Step 6 | Click OK . The Call Precedence Details window displays and shows the call precedence levels and values, number of call legs, and percentage
                                             of call legs. |
| Step 7 | In the Select CDRs column, check the check boxes of the CDRs at which you want to look. |
| Step 8 | Click View CDRs . The CDR-CMR Search by Precedence Levels - CDR-CMR Search Results window displays. The system displays only the oldest 100
                                             records that fall into the date and time ranges that you configured in Step 3 and Step 3 Step 4 . If more than 100 records are returned, the system truncates the results. |
| Step 9 | To view the CMR data, click Others . To view both the CDR and CMR data fields, click View . |
| Step 10 | To mail the report to e-mail recipient, click Send Report and follow the steps in the Mail Reports . |

| Voice Quality | Description |
|---|---|
| Flash Override | Highest precedence setting for MLPP calls. |
| Flash | Second highest precedence setting for MLPP calls. |
| Immediate | Third highest precedence setting for MLPP calls. |
| Priority | Fourth highest precedence setting for MLPP calls. |
| Routine | Lowest precedence setting for MLPP calls. |

| Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. |
|---|---|

| Note | To check the check boxes of every precedence level, click Select All . To clear the check boxes, click Clear All . |
|---|---|

| Note | With Grouping, choice means that the system returns CDR records that match the date and time range for the search and groups
                                                         them with their associated records. Without Grouping returns all the CDR records that match the date and time range without
                                                         grouping all the associated records for each call. |
|---|---|

| Step 1 | Choose CDR > Search > Malicious Calls . The CDR Search for Malicious Calls window displays. |
|---|---|
| Step 2 | Perform one of the following tasks: In the Select Phone Number/SIP URL(s) box, enter the phone number or SIP URL in the Phone Number/SIP URL field and click Add Phone Number/SIP URL . The phone number or SIP URL of the user displays in the Selected Phone Number/SIP URL(s) box. To search for a user phone number or SIP URL, click the Search Internal Phone Number/SIP URL based User link, enter the first few letters of the first and/or last name in the First Name and/or Last Name fields, and click the Search button. When the results display, click the Select link next to the result that you want to include. The phone number or SIP URL of the user displays in the Selected Phone
                                                Number/SIP URLs box. Click Close . Note To remove the phone number or SIP URL, highlight the phone number or SIP URL that you want to remove and click Remove Phone Number/SIP URL(s) . To remove all phone numbers or SIP URL(s), click Remove All Phone Number/SIP URL(s) . | Note | To remove the phone number or SIP URL, highlight the phone number or SIP URL that you want to remove and click Remove Phone Number/SIP URL(s) . To remove all phone numbers or SIP URL(s), click Remove All Phone Number/SIP URL(s) . |
| Note | To remove the phone number or SIP URL, highlight the phone number or SIP URL that you want to remove and click Remove Phone Number/SIP URL(s) . To remove all phone numbers or SIP URL(s), click Remove All Phone Number/SIP URL(s) . |
| Step 3 | Choose the date and time range of the period when you want to search for CDR data. The current time displays in both Coordinated
                                          Universal Time (UTC) and local time and uses the following rules: The UTC and local time comprise a numeric string of mmddyyyy hhmmss, as in January 15, 2007 12:00:00. The default FromDate and ToDate values display in UTC time. The default ToDate specifies the current time of the server in UTC time. The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, then
                                                the FromDate default value = January 15, 2007 11:00:00 (all times in UTC). |
| Step 4 | Choose whether to run the CDR Search report With Grouping or Without Grouping. If you chose with grouping, check the box beside With Grouping . The default value specifies Without Grouping Note With Grouping means that the system returns CDR records that match the date and time range for the search and groups them
                                                         with their associated records. Without Grouping returns all the CDR records that match the date and time range without grouping
                                                         all the associated records for each call together. | Note | With Grouping means that the system returns CDR records that match the date and time range for the search and groups them
                                                         with their associated records. Without Grouping returns all the CDR records that match the date and time range without grouping
                                                         all the associated records for each call together. |
| Note | With Grouping means that the system returns CDR records that match the date and time range for the search and groups them
                                                         with their associated records. Without Grouping returns all the CDR records that match the date and time range without grouping
                                                         all the associated records for each call together. |
| Step 5 | Click OK . The CDR-CMR Search Results window displays. The system only displays the oldest 100 records that fall into the date and time
                                             ranges that you configured in Step 3 . If more than 100 records are returned, the system truncates the results. |
| Step 6 | To view the CMR data, click Others . To view both the CDR and CMR data fields, click View . |
| Step 7 | To mail the report to e-mail recipients, follow the steps in the Mail Reports . |

| Note | To remove the phone number or SIP URL, highlight the phone number or SIP URL that you want to remove and click Remove Phone Number/SIP URL(s) . To remove all phone numbers or SIP URL(s), click Remove All Phone Number/SIP URL(s) . |
|---|---|

| Note | With Grouping means that the system returns CDR records that match the date and time range for the search and groups them
                                                         with their associated records. Without Grouping returns all the CDR records that match the date and time range without grouping
                                                         all the associated records for each call together. |
|---|---|

| Step 1 | Choose CDR > Search > By Call Types . The CDR Search for Different Call Types window displays. Note You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. | Note | You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. |
|---|---|---|---|
| Note | You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. |
| Step 2 | Choose the call type from the Select Call Type drop down list. The following is a list of the call types: Successful IME Call : Calls that were successfully routed through IME trunks. Failed IME Calls : Calls that tried to route through the IME trunk, but failed. IME Calls with Fallback to Alternate Route : Calls which were initially routed through the IME trunk, but due to some reason (for example, poor QoS), the fallback mechanism
                                                   was initiated and these calls were re-routed mid-call to an alternate route. The alternate route is typically a PSTN route. Successful Fallback Calls to Alternate Route : Calls which successfully fell back to the alternate route. The alternate route is typically a PSTN route. Failed Fallback Calls to Alternate Route : Calls which failed to fall back to the alternate route. Calls on Alternate Route due to IME Redirection : Calls that tried to route (at call setup) to IME, but for some reason were routed to an alternate route. The alternate route
                                                   is typically a PSTN route. |
| Step 3 | Perform one of the following tasks: To search CDRs based on phone numbers/SIP URLs, enter the phone number or SIP URL in the Phone Number/SIP URL field and click Add Phone Number/SIP URL . To search CDRs based on user, click the Search Internal Phone Number/SIP URL based User link, enter the first few letters of the first and/or the last name in the First Name and/or Last Name fields, and click Search . When the results display, click the Select link next to the result that you want to include. Click Close . The phone number or SIP URL displays in the Selected Phone Number/SIP URL(s) box. Note To delete an item from the Report Criteria box, click the Remove Phone Number/SIP URL(s) button. You can delete all items from the Report Criteria box by clicking the Remove All Phone Number/SIP URL(s) . | Note | To delete an item from the Report Criteria box, click the Remove Phone Number/SIP URL(s) button. You can delete all items from the Report Criteria box by clicking the Remove All Phone Number/SIP URL(s) . |
| Note | To delete an item from the Report Criteria box, click the Remove Phone Number/SIP URL(s) button. You can delete all items from the Report Criteria box by clicking the Remove All Phone Number/SIP URL(s) . |
| Step 4 | Current time displays in both Coordinated Universal Time (UTC) and local time. The UTC and local time comprise a numeric string
                                          of mmddyyyy hhmmss, as in January 15, 2007 12:00:00. |
| Step 5 | From the Select TimeZone field, choose the time zone that you want to use to search the CDRs. Options include your local time zone and Greenwich Mean
                                          Time (GMT). |
| Step 6 | In the From Date field and the To Date field, choose the date and time from and to which you want to search the CDRs, respectively. The times in the From and To
                                          fields use the following rules: The default FromDate and ToDate values display in UTC time. The default ToDate specifies the current time of the server in UTC time. The default FromDate value specifies the ToDate value minus 1hour. For example, if ToDate = January 15, 2007 12:00:00, then
                                                the FromDate default value = January 15, 2007 11:00:00 (all times in UTC). |
| Step 7 | Click OK . The CDR-CMR Search Results window displays. The system displays only the oldest 100 records that fall into the date and time
                                             ranges that you configured in Step 3 and Step 4. If more than 100 records are returned, the system truncates the results. |
| Step 8 | To view the CMR data, click Others . To view both the CDR and CMR data fields, click View . |
| Step 9 | To mail the report to e-mail recipient(s), click Send Report and follow the steps in the Mail Reports . |

| Note | You can enter a wildcard pattern like "!" or "X" to search on phone number or SIP URL. The "!" represents any n digit that has 0-9 as each of its digits, and the "X" represents a single digit in the range 0-9. |
|---|---|

| Note | To delete an item from the Report Criteria box, click the Remove Phone Number/SIP URL(s) button. You can delete all items from the Report Criteria box by clicking the Remove All Phone Number/SIP URL(s) . |
|---|---|

| Field | Description |
|---|---|
| Sl No | Specifies the serial or record number. |
| Call Type | Specifies the type of call: simple, transfer, forward, pickup, conference, refer, replaces, or redirection. |
| GCID_CMIdGCID_CallId | Specifies the call identifiers that are associated with all the records for the entire call. |
| Orig Node IdDest Node Id | Specifies the server where the call originator/destination was registered at the time of the call. |
| Orig Leg IdDest Leg Id | Specifies the unique identifiers to the originating/destination leg of a call. |
| Calling NoCalling No Partition | The calling number specifies the directory number where the call originated. The calling partition specifies the partition
                                          that is associated with the calling party. |
| Called NoCalled No Partition | The called number specifies the directory number from which the call was initially placed and is the same as the Dest No when
                                          the call is not transferred or forwarded. The called partition specifies the partition that is associated with the called
                                          party. |
| Dest NoDest No Partition | The destination number specifies the directory number where the call finally terminated and is the same as the called number
                                          when the call is not transferred or forwarded. The destination number partition specifies the partition that is associated
                                          with the destination number. |
| Last Rd NoLast Rd No Partition | The last redirected number specifies the directory number from which the call was finally redirected. The last redirected
                                          number partition specifies the partition that is associated with the last redirected number. |
| Media InfoOrig Pkts Rcd Dest Pkts Rcd Orig Pkts Lost Dest Pkts Lost | Specifies the packets that were received or lost for the origination or destination leg of a call and a link to the media
                                          information. |
| CDR - CMR Dump | Specifies a link to the CDR and CDR dump tables. This link allows the users to view the values in the CDR/CMR fields. |

| Field | Description |
|---|---|
| Origination Leg | A unique identifier for the originating leg of a call. |
| Destination Leg | A unique identifier for the destination leg of a call. |
| Parameter | The media parameters MediaTransportAdd_Ip, PayLoadCapability, MediaCap_g723BitRate, Packets Sent, Octets Sent, Packets Received,
                                             Octets Received, Packets Lost, Jitter, Latency, QoS, VideoCap_Codec, VideoCap_Bandwidth, VideoCap_Resolution, VideoTransportAddress_IP,
                                             and VideoTransportAddress_Port |
| Origination | The value for all the preceding parameters for the origination leg of the call. |
| Destination | The value for all the preceding parameters for the destination leg of the call. |

| Note | You can view the content of the voice quality metrics field, varVQMetrics, in the Origination CMR and Destination CMR fields. |
|---|---|

| Field | Description |
|---|---|
| CDR | This field specifies the call detail record fields. |
| Origination CMR | Only a single set of fields for origination and destination exists. You can find the origination or destination CMR by using
                                             the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR, the following record represents Orig/Dest CMR. |
| Destination CMR | Only a single set of fields for origination and destination exists. You can find the origination or destination CMR by using
                                             the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR, the following record represents Orig/Dest CMR. |