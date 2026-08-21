---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-877c6728d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_01001110.html
retrieved_at: 2026-08-21T08:59:06.211969+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Manage
	 Troubleshooting BAT and TAPS

## Chapter: Manage
	 Troubleshooting BAT and TAPS

# Manage
                     	 Troubleshooting BAT and TAPS

This chapter
                        		provides information about various problems and messages that you might
                        		encounter when you are using Cisco Unified Communications
                           		  Manager Bulk Administration (BAT) or Tool for Auto-Registered Phones
                        		Support.

## Enable Trace to View Configuration Files

You can enable the writing of trace files feature from the Service Control window in Cisco Unified Communications Manager Serviceability.

Trace files provide a means of tracking problems in the functioning of
                              		  a tool. The system writes trace files for BAT and TAPS to the server on which
                              		  BAT and TAPS are installed.

The BAT and TAPs trace files display as follows:

bps<index number>.log

taps<index number>.log

where <index number> ranges from 1- 250.

In Cisco Unified Communications Manager Serviceability, choose Trace > Trace
                                             				  Configuration .

Choose the Cisco Unified Communications Manager server, from the Server drop-down list box.

Choose one of the following services from the Configured Services drop-down list box.

- For BAT trace
                                          				file settings, choose CiscoBulk Provisioning Service

- For TAPS trace
                                          				file settings, choose TAPS Service

To activate the trace feature, click the Trace On check box.

In the Trace Filter Settings , choose the trace level
                                       			 that you want to set from the Debug Trace Level drop-down list box.

Click the desired debug trace level as described in the following
                                          				table.

Level

Description

Fatal

Traces very severe error events that may cause the
                                                      							 application to abort.

Error

Traces alarm conditions and events. Used for all traces
                                                      							 that are generated in abnormal path. Uses minimum number of CPU cycles.

Warn

Traces potentially harmful situations.

Info

Traces the majority of servlet problems and has a
                                                      							 minimal effect on system performance.

Debug

Traces all State Transition conditions plus media layer
                                                      							 events that occur during normal operation.

Trace level that turns on all logging.

Check the check boxes for CiscoBulk Provisioning Service Trace Fields and Device Name Based Trace Monitoring , as needed.

In the Trace Output Settings , enter values for the
                                       			 maximum number of files, maximum number of lines per file, and maximum number
                                       			 of minutes per file, and click Update .

- BAT trace files:
                                                				  /var/log/active/cm/trace/bps/log4j

- TAPS trace files:
                                                				  /var/log/active/cm/trace/taps/log4j

Click Update.

### What to do next

After you have configured the information that you want to include in
                              		  the trace files, you can collect and view trace files using the trace and log
                              		  central option in the Real-Time Monitoring Tool (RTMT). For more information, refer to CiscoUnified
                                 		  Communications Manager Serviceability System Guide .

## Disable Trace of Configuration Files

You can disable the writing of trace files from the Service Control
                              		  window in Cisco Unified Communications Manager Serviceability.

In Cisco Unified Communications Manager Serviceability, choose Trace > Trace
                                             				  Configuration .

Choose the Cisco Unified Communications Manager server from the Server drop-down list box.

Choose CiscoBulk Provisioning Service from the Configured Services drop-down list box.

To deactivate the trace feature, uncheck the Trace On check box.

Click Update .

This action disables the feature.

## BAT Log Files

BAT generates log files for each bulk transaction. The log
                              		  file shows the key value of a record, so the administrator may reexamine the
                              		  record. The MAC address of the phone serves as the key value when you are
                              		  adding, updating, or modifying phones. When users are added, the User ID serves
                              		  as the key value. To view the log files for each job that is created in BAT,
                              		  find the appropriate job and click on the link in the Log File Name column. A
                              		  pop-up window displays the log file details of that job.

The log file names designate the operation that was performed
                              		  and the time that the operation ended.

Log File Names—File name shows the Job ID, which is a unique
                                    				identifier that the system creates when a job is submitted.

TimeStamp—The timestamp format that is included in the log file
                                    				name specifies mmddyyyyhhmmss.

The log file name is of the format jobid#timestamp.txt

## Troubleshooting BAT

Problem The following list describes some scenarios that could occur and
                              		  provides possible resolutions.

### Bulk Administration Menu Does Not Display in Administration

Problem Bulk Administration menu does not display in Cisco Unified Communications Manager Administration.

Possible Cause Bulk Administration menu is accessible only from first node of Cisco Unified Communications Manager .

Solution Make sure that you are logged into first node of Cisco Unified Communications Manager .

### Cannot Access Complete Bulk Administration Functionality

Problem Cannot access complete Bulk Administration functionality.

Possible Cause After logging into Cisco Unified Communications Manager Administration, all the Bulk Administration
                                 		  windows are not accessible.

Solution This problem may arise due to restricted access to the application
                                 		  given to the User ID. Contact the System Administrator to be granted required
                                 		  permissions.

### Export to BAT Format Button Does Not Work in BAT.xlt File

Problem Export to BAT Format button does not work in BAT.xlt file.

Possible Cause Clicking the Export to BAT Format button in the BAT.xlt file does not
                                 		  seem to do anything.

Solution Click a blank cell. The button can seem to be disabled if the cursor
                                 		  is on the text in a cell or in the text box.

### BAT Excel Spreadsheet Gives a Compilation Error While Exporting Data to the CSV Format

Problem BAT Excel spreadsheet gives a compilation error while exporting data
                                 		  to the CSV format.

Possible Cause Check the version of Microsoft Excel that you are using. Customers
                                 		  have reported problems with BAT.xlt when they were using Excel97.

Solution Use Microsoft Excel 2000 version or higher.

### BAT Excel Spreadsheet Does Not Respond to Actions

Problem BAT Excel spreadsheet does not respond to actions.

Possible Cause .BAT Excel spreadsheet does not respond to actions like Add More Lines
                                 		  and so on.

Solution .Ensure that Enable Macros option is selected while opening BAT Excel
                                 		  spreadsheet.To enable macros in BAT.xlt use the following steps:

- Open BAT.xlt.

- Go to Menu > Tools > Macro > Security .

- Set the Security Level to
                                    			 Medium.

- Close BAT.xlt and open it
                                    			 again. When prompted, choose Enable Macros.

### Data Files (CSV) Format Do Not Match Phone Template/Sample File

Problem Data files (CSV) format do not match Phone Template/Sample File.

Possible Cause The number of lines in the data file should be less than or equal to
                                 		  the number of lines that are configured in the BAT phone template, but is not.
                                 		  For example, the phone template has three lines, and, of these, Lines 1, 2, and
                                 		  3 are configured. You should use a phone data file with up to three configured
                                 		  lines. 1111, 2222, 4444 results in Line1-1111, Line2-2222, Line3-none,
                                 		  Line4-4444.

Solution Check the BAT phone template that you intend to use. The number of
                                 		  lines that are specified on the CSV data file should not exceed the number of
                                 		  lines that are configured in the BAT phone template. Also, the number of speed
                                 		  dials that the CSV data file specifies should not exceed the maximum possible
                                 		  number of speed dials for the BAT phone template that you plan to use.

### Uploaded CSV File Does Not Display in the File Name Drop-down List Box

Problem Uploaded CSV file does not display in the File Name drop-down list
                                 		  box.

Possible Cause The CSV file that you uploaded to Cisco Unified Communications Manager Server using File Upload Configuration widow,
                                 		  does not display in the File Name drop-down list box field for various
                                 		  operations. For example, if you uploaded a CSV file for inserting phones using
                                 		  Uploading/Downloading menu option in Bulk Administration menu, but the file
                                 		  does not appear as one of the options in the Insert Phone Configuration window
                                 		  File Name drop-down list box.

Solution Check and make sure that the file is uploaded for the right function.
                                 		  In the preceding example, the you might have uploaded the file for Phones -
                                 		  Insert All details, where as the CSV file actually belongs to Phones -Insert
                                 		  Specific details.

Delete the file through Upload/Download Files menu option and upload
                                 		  it for the right function.

### Jobs Remain in Pending State Even After the Scheduled Time Expires

Problem Jobs remain in Pending state even after the scheduled time expires.

Possible Cause You schedule jobs with a specific scheduled time for execution. But,
                                 		  the jobs remain in Pending state, even after the scheduled time.

Solution Check for the following details:

- Check that Cisco Bulk
                                    			 Provisioning Service (BPS) is started.

- Check that there is no
                                    			 other job in Processing state. BPS can process only one job at a time.

- Check if Stop Processing
                                    			 is requested for BPS transactions. If so, go to Job Scheduler window and click
                                    			 Activate Job.

### Jobs Remain in Hold State

Problem Jobs remain in Hold state.

Possible Cause After you submit jobs with all the required data, the jobs show in
                                 		  Hold state on the job scheduler window. These jobs do not get executed.

Solution You need to activate jobs that are in Hold state, before they can be
                                 		  executed by BPS. Go to Job Scheduler window and follow the process to activate
                                 		  the job.

### Job Does Not Display in the Find and List Jobs Window

Problem Job does not display in the Find and List Jobs window.

Possible Cause After you submit a job with all the required data, choose Bulk
                                 		  Administration > Job Scheduler. Enter the appropriate search criteria for
                                 		  the job you scheduled and click Find. The job does not display in the search
                                 		  results. Check if Hide is chosen in the third drop-down list box in the Search
                                 		  Options area of the Find and List Jobs window. This option hides all the
                                 		  completed jobs. If the job you submitted is already complete then it will not
                                 		  be displayed in the Search Results area.

Solution In the Find and List jobs window, choose Show from the third drop-down
                                 		  window and click Find again. The search results now display completed jobs
                                 		  also.

### Port Number Not Configured in the Template

Problem Port number not configured in the template.

Possible Cause The CSV file specified the port number, but no corresponding ports are
                                 		  configured in the BAT template.

Solution In the BAT template, configure the ports that you have specified in
                                 		  the CSV file.

### MAC Address Values Are Not Allowed in the File If Dummy MAC Address Values Are Desired

Problem MAC address values are not allowed in the file if dummy MAC address
                                 		  values are desired.

Possible Cause The CSV file contains MAC addresses. You cannot provide dummy MAC
                                 		  addresses when MAC addresses are present in any row in the CSV file.

Solution If you want to use dummy MAC addresses, create a new CSV file that
                                 		  contains only those records for which you have not specified MAC addresses.
                                 		  Alternatively, you can specify MAC addresses in the CSV file and not check the
                                 		  Create Dummy MAC Address check box.

### The BAT.xlt Spreadsheet Does Not Work with Microsoft Excel XP (Office XP)

Problem The BAT.xlt spreadsheet does not work with Microsoft Excel XP (Office
                                 		  XP)

Possible Cause In Microsoft Excel packaged with Office XP, macro security is set to
                                 		  high by default. Due to this setting, macros in BAT.xlt cannot run which
                                 		  renders BAT.xlt unusable.

Solution To enable macros in BAT.xlt use the following steps:

- Open BAT.xlt.

- Go to Menu >Tools
                                    			 >Macro > Security.

- Set the Security Level to
                                    			 Medium.

- Close BAT.xlt and open it
                                    			 again. When prompted, choose Enable Macros.

### After the Request to
                           	 Migrate an SCCP Phone to SIP Through the Migrate Phones - SCCP TO SIP Window Is
                           	 Submitted, Model 7940 and 7960 Continue to Show Up as SCCP Phones

Problem After the request to
                                 		  migrate an SCCP phone to SIP through the Migrate Phones - SCCP TO SIP window is
                                 		  submitted, Cisco Unified IP
                                    			 Phone s model 7940 and 7960 continue to show up as SCCP phones.

Solution To solve this
                                 		  problem, power cycle (power off and on) individual phones after migration.

For Cisco Unified IP phones (models 7911, 7941, 7961 , 7970, and
                                                			 7971 ), the migration activity works correctly, and the phones register as SIP
                                             			 after migration.

### Record Does Not Match the File Format Selected

Problem Record does not match the file format selected.

Possible Cause When you create a CSV file using MS Excel with the last column blank,
                                 		  MS Excel fails to add a comma for the last column after row 15. This error
                                 		  occurs when such a CSV file is used for any of the BAT operations.

Solution If you want the last column of CSV file to be blank, use the following
                                 		  steps:

- Enter some dummy value for
                                    			 the last column while creating the CSV file.

- Save the CSV file and
                                    			 close it.

- Open the saved CSV file
                                    			 using Text Editor/Notepad.

- Replace the dummy values
                                    			 with a blank value and save it.

### BAT.xlt Is Working in Compatibility Mode with Microsoft Excel 2007

Problem BAT.xlt is working in compatibility mode with Microsoft Excel 2007.

Possible Cause The excel template bat.xlt is a Microsoft Excel 2003 file. When the
                                 		  file is opened in Microsoft Excel 2007, the file opens in compatibility mode.
                                 		  In compatibility mode, the excel template acts like a Microsoft Excel 2003
                                 		  file, and the features of Microsoft Excel 2007 are not available.

Solution Make sure that BAT.xlt is in normal mode. Open Bat.xltl; then choose
                                 		  File > Save As and click Excel Macro Enabled Workbook. Provide a name, and
                                 		  click Save. Close the bat.xlt and open the file that you saved (the Saved As
                                 		  file).

## Troubleshooting BAT Performance

Keep in mind that it is best to send bulk transactions during low-traffic periods. When you insert BAT files to the first
                              node database during the time when Unified Communications Manager is processing a high volume of calls, the BAT transactions
                              can be slow. In fact, you can adversely affect how Unified Communications Manager processes calls.

You can improve BAT performance by restricting the file size
                              		  of the file to less than 12000 records per file.

You can also improve BAT performance by stopping the TFTP service on the Unified Communications Manager first node server
                              before you insert the BAT files to the first node database. You must restart the TFTP service when the insert transaction
                              complete.

In Cisco Unified Serviceability window, choose Tools > Control Center - Feature Services .

Choose Cisco TFTP from the Unified CM Service list by clicking the corresponding radio button.

Click Stop and click OK .

You must restart the TFTP service when the insert transaction is
                                                      				  complete. Use the same procedure and click Start to restart the service.

## Troubleshooting BAT and TAPS

As a general rule, we recommend that you stop TAPS service when TAPS is not in use. You can prevent undesired TAPS usage by
                           stopping the service, and you can save some CPU time.

### Viewing Tool for Auto-Registered Phones Support Log Files

TAPS generates a row of information for each TAPS log file.

To view TAPS log file, choose Bulk
                                       				Administration > TAPS > View TAPS Log
                                       				File .

### Tool for Auto-Registered Phones Support Error Messages

You may receive the following messages while running TAPS on
                                 		  the CiscoUCCX server.

#### When Dialing the TAPS Route Point Number, the Caller Receives a Busy Tone

Problem When dialing the TAPS route point number, the caller receives a busy
                                    		  tone.

Possible Cause The busy tone indicates that the maximum number of simultaneous
                                    		  sessions for TAPS has been reached. The maximum number of sessions for TAPS
                                    		  equals the number of ports that are assigned to the TAPS application in UCCX
                                    		  configuration.

Solution You must increase the number of ports that are assigned to TAPS in
                                    		  CiscoUCCX to prevent this situation.

#### When the CiscoUCCX Server Starts, the JTAPI Subsystem Shows Partial Service or Out of Service

Problem When the CiscoUCCX server starts, the JTAPI subsystem shows partial
                                    		  service or out of service.

Possible Cause Message occurs because of configuration problems in the Cisco Unified Communications Manager or the CiscoUCCX server.

Solution Perform one or all of the following steps until the problem has been
                                    		  corrected:

Verify that Cisco Unified Communications Manager is started.

Make sure that JTAPI is available on the CiscoUCCX server.

Make sure that the JTAPI version on the UCCX server is the same as
                                          				the JTAPI version that is installed on Cisco Unified Communications Manager .

Make sure that the Route Points and CTI ports are properly
                                          				configured on the Cisco Unified Communications Manager .

Verify that the Allow control of device from CTI check box is
                                          				checked for the JTAPI user; you can verify that this in the user window in Cisco Unified Communications Manager Administration.

Verify that the CTI Manager service is started.

Verify that the ports and the route point are associated to the
                                          				user in the Cisco Unified Communications Manager user configuration.

For further troubleshooting, collect and review MIVR log files for
                                          				CiscoUCCX server.

## Topics Related to Troubleshooting BAT and TAPS

| Step 1 | In Cisco Unified Communications Manager Serviceability, choose Trace > Trace
                                             				  Configuration . The Trace Configuration window displays. |
|---|---|
| Step 2 | Choose the Cisco Unified Communications Manager server, from the Server drop-down list box. |
| Step 3 | Choose one of the following services from the Configured Services drop-down list box. For BAT trace
                                          				file settings, choose CiscoBulk Provisioning Service For TAPS trace
                                          				file settings, choose TAPS Service |
| Step 4 | To activate the trace feature, click the Trace On check box. |
| Step 5 | In the Trace Filter Settings , choose the trace level
                                       			 that you want to set from the Debug Trace Level drop-down list box. Click the desired debug trace level as described in the following
                                          				table. Table 1. Debug Trace Levels Level Description Fatal Traces very severe error events that may cause the
                                                      							 application to abort. Error Traces alarm conditions and events. Used for all traces
                                                      							 that are generated in abnormal path. Uses minimum number of CPU cycles. Warn Traces potentially harmful situations. Info Traces the majority of servlet problems and has a
                                                      							 minimal effect on system performance. Debug Traces all State Transition conditions plus media layer
                                                      							 events that occur during normal operation. Trace level that turns on all logging. | Level | Description | Fatal | Traces very severe error events that may cause the
                                                      							 application to abort. | Error | Traces alarm conditions and events. Used for all traces
                                                      							 that are generated in abnormal path. Uses minimum number of CPU cycles. | Warn | Traces potentially harmful situations. | Info | Traces the majority of servlet problems and has a
                                                      							 minimal effect on system performance. | Debug | Traces all State Transition conditions plus media layer
                                                      							 events that occur during normal operation. Trace level that turns on all logging. |
| Level | Description |
| Fatal | Traces very severe error events that may cause the
                                                      							 application to abort. |
| Error | Traces alarm conditions and events. Used for all traces
                                                      							 that are generated in abnormal path. Uses minimum number of CPU cycles. |
| Warn | Traces potentially harmful situations. |
| Info | Traces the majority of servlet problems and has a
                                                      							 minimal effect on system performance. |
| Debug | Traces all State Transition conditions plus media layer
                                                      							 events that occur during normal operation. Trace level that turns on all logging. |
| Step 6 | Check the check boxes for CiscoBulk Provisioning Service Trace Fields and Device Name Based Trace Monitoring , as needed. |
| Step 7 | In the Trace Output Settings , enter values for the
                                       			 maximum number of files, maximum number of lines per file, and maximum number
                                       			 of minutes per file, and click Update . The system enables the feature, and the trace files get written to
                                          				the following locations on the server: BAT trace files:
                                                				  /var/log/active/cm/trace/bps/log4j TAPS trace files:
                                                				  /var/log/active/cm/trace/taps/log4j |
| Step 8 | Click Update. |

| Level | Description |
|---|---|
| Fatal | Traces very severe error events that may cause the
                                                      							 application to abort. |
| Error | Traces alarm conditions and events. Used for all traces
                                                      							 that are generated in abnormal path. Uses minimum number of CPU cycles. |
| Warn | Traces potentially harmful situations. |
| Info | Traces the majority of servlet problems and has a
                                                      							 minimal effect on system performance. |
| Debug | Traces all State Transition conditions plus media layer
                                                      							 events that occur during normal operation. Trace level that turns on all logging. |

| Step 1 | In Cisco Unified Communications Manager Serviceability, choose Trace > Trace
                                             				  Configuration . The Trace Configuration window displays. |
|---|---|
| Step 2 | Choose the Cisco Unified Communications Manager server from the Server drop-down list box. |
| Step 3 | Choose CiscoBulk Provisioning Service from the Configured Services drop-down list box. |
| Step 4 | To deactivate the trace feature, uncheck the Trace On check box. |
| Step 5 | Click Update . This action disables the feature. |

| Note | For Cisco Unified IP phones (models 7911, 7941, 7961 , 7970, and
                                                			 7971 ), the migration activity works correctly, and the phones register as SIP
                                             			 after migration. |
|---|---|

| Step 1 | In Cisco Unified Serviceability window, choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | Choose Cisco TFTP from the Unified CM Service list by clicking the corresponding radio button. |
| Step 3 | Click Stop and click OK . Note You must restart the TFTP service when the insert transaction is
                                                      				  complete. Use the same procedure and click Start to restart the service. | Note | You must restart the TFTP service when the insert transaction is
                                                      				  complete. Use the same procedure and click Start to restart the service. |
| Note | You must restart the TFTP service when the insert transaction is
                                                      				  complete. Use the same procedure and click Start to restart the service. |

| Note | You must restart the TFTP service when the insert transaction is
                                                      				  complete. Use the same procedure and click Start to restart the service. |
|---|---|