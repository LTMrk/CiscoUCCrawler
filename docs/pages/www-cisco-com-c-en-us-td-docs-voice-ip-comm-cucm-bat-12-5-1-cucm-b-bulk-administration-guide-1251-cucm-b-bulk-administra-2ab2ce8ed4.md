---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-2ab2ce8ed4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_01100.html
retrieved_at: 2026-08-21T17:56:09.176940+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Phone Reports

## Chapter: Phone Reports

# Phone Reports

This chapter provides information about CSV file format BAT
                        		reports that you can generate. You can customize BAT reports for phones and
                        		user device profiles but reports for users, managers, assistants, and gateways
                        		have a fixed format and can not be customized.

## Phone Report Generation

Unified Communications Manager Bulk Administration (BAT) provides reports to help you manage records effectively. You can create and save reports that provide
                              information about phones, users, user device profiles, managers and assistants, and gateway records. You can save these reports
                              with a filename and store them in a folder on the first node server to review and print.

You can customize BAT reports for phones and for user device profiles to meet your particular needs by choosing items from
                              a list of device fields and line fields. You can also choose how to arrange the fields in the report. The system generates
                              the report in the CSV file format. Because reports for users, managers, assistants, and gateways have a fixed format, you
                              cannot customize them.

### Example

You need to have a list of all the directory numbers with their forwarding destinations by phone model. You can generate a
                              Phone Report for the Cisco Unified IP Phone 7960 and choose these query details: Device Name, Directory Number, Forward Busy
                              Destination, Forward No Answer Destination, and Label. You can arrange the report fields, so the Label field follows the Directory
                              Number field and precedes the two forward destination numbers.

## Generate Phone Reports

You can generate reports for phones and other IP telephony
                              		  devices.

Step 1

Choose Bulk
                                             				  Administration > Phones > Generate
                                             				  Phone Reports .

Step 2

In the first Find Phone where drop-down list box, choose
                                       			 the field to query such as Device Name or Directory Number .

Step 3

In the second drop-down list box, choose the search criteria such
                                       			 as begins with, contains, or is empty.

Step 4

In the search field/list box, either choose or enter the value
                                       			 that you want to locate, such as the model name from the list or directory
                                       			 number range.

Step 5

Specify the appropriate search text, if applicable, and click Find .

Tip

To generate a report for all phones that are registered in the
                                                      				  database, click Find without entering any search text.

To further define your query and to add multiple filters, check
                                          				the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Steps Step 2 through Step 5 .

Step 6

To choose details for your type of report, click Next .

Tip

If you want to change the type of query, click Back .

Step 7

In the Report File Name field, enter your name for
                                       			 this report (required).

Step 8

In the Available Device Fields drop-down list box,
                                       			 choose a device item and click the arrow to move the item into the Selected Fields for this Report list.

Tip

To rearrange the order of the items in the Selected Device Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list.

Step 9

In the Available Line Fields drop-down list box,
                                       			 choose a line item and click the arrow to move the item into the Selected Fields for this Report list.

Tip

To rearrange the order of the items in the Selected Line Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list.

Step 10

If you want to include IP phone services fields in your report,
                                       			 check the check boxes for Speed Dial Services and/or IP Phone Services .

Step 11

In the Job Information area, enter the Job description.

Step 12

Choose when to generate the report. Do one of the following:

Click Run Immediately to generate the report
                                             				  immediately.

Click Run Later to generate the report at a
                                             				  later time.

Step 13

To create a job for inserting the phone records, click Submit .

### What to do next

You can search and download the report file using the
                              		  Upload / Download Files option in the Bulk Administration menu.

### Phone and IP Telephony Device Reports

You can produce phone reports for all phones and IP telephony
                                 		  devices or limit the report to one of these options:

Device Name—Specify a filter or use exact name.

Description—Specify a filter or use exact description.

Phone Load Name—Specify a filter or use exact name.

Device Pool—Choose one from a list of device pools that are
                                       				configured in the cluster.

Calling Search Space—Choose one from a list of CSS that are
                                       				configured in the cluster.

Location—Choose one from a list of locations that are configured
                                       				in the cluster.

Directory Number—Specify a filter or use exact number.

After choosing the phone report type, you can choose the
                                 		  device and line details to include in the report.

You can choose from these Device fields:

AAR Calling Search Space

AAR Neighborhood

Authentication String

Built In Bridge

Calling Search Space

Calling Search Space Reroute

Certificate Operation

Certificate Status

Common Profile

Country

Description

Device Name

Device Pool

Device Profile

Device Protocol

Device_Default Profile

Dial Rules

Last Login user ID

Load Information

Location

Login Duration

Login Time

MLPP Domain

MLPP Indication

Media Resource List

Network Hold MOH Audio Source

Network Location

Packet Capture Duration

Packet Capture Mode

Phone Template

Preemption

Privacy

Product

Public Key

Qsig

SIP Profile

Secure Shell Password

Secure Shell User ID

Security Profile

Softkey Template

Upgrade Finish Time

User ID

Geo Location

Always Use Prime Line

Always Use Prime Line for Voice Message

You can choose from these Line fields:

Alerting Name

Auto Answer

CSS_Device Failure

CSS_MWI

Call Forward Duration

Calling Line Presentation Bit

Calling Name Presentation Bit

Calling Party Prefix Digits

Connected Line Presentation Bit

Connected Name Presentation Bit

Device Failure DN

Directory Number

Forward All CSS

Forward All Destination

Forward Busy External CSS

Forward Busy External Destination

Forward Busy Internal CSS

Forward Busy Internal 
                                       			 Destination

Forward No Answer External CSS

Forward No Answer External 
                                       			 Destination

Forward No Answer Internal CSS

Forward No Answer Internal 
                                       			 Destination

Forward No Answer Ring Duration

Forward No Coverage External CSS

Forward No Coverage External 
                                       			 Destination

Forward No Coverage Internal CSS

Forward No Coverage Internal 
                                       			 Destination

Forward Unregistered External CSS

Forward Unregistered External Destination

Forward Unregistered Internal CSS

Forward Unregistered Internal Destination

Forward on CTI Failure CSS

Forward on CTI Failure Destination

Line AAR Neighborhood

Line Alerting Name ASCII

Line Description

Line Network Hold MOH Audio Source

MLPP No Answer Ring Duration (Seconds)

Route Partition

Secondary Call Forward All CSS

Target CSS

Target Destination

User Hold MOH Audio Source

Party Entrance Tone

Log Missed Calls

Park Monitor Forward No Retrieve External Destination

Park Monitor Forward No Retrieve Internal Destination

Park Monitor Forward No Retrieve Internal Voice Mail

Park Monitor Forward No Retrieve External Voice Mail

Park Monitor Forward No Retrieve External CSS

Park Monitor Forward No Retrieve Internal CSS

Park Monitor Reversion Timer

URI Is Primary on Directory Number (1-5)

URI Route Partition on Directory Number (1-5)

URI on Directory Number (1--5)

### Generate List of Phones Having Dummy MAC Addresses

You can generate a list of phones that use dummy MAC addresses.

Step 1

Choose Bulk
                                                				  Administration > Phones > Generate
                                                				  Phone Reports .

Step 2

In the first Find Phone(s) where drop-down list box, choose Device Name .

Step 3

In the second drop-down list box, choose begins with .

Step 4

In the text field, enter BAT . All phones that are added with a dummy MAC address have device names that begin with BAT.

Step 5

Click Find . The text Device Name begins with 'BAT'
                                          			 and displays in the query text box.

Step 6

Click Next . The Generate Phone Report Configuration window
                                          			 displays.

#### What to do next

Complete the report generation procedure. Go to Generate Phone Reports .

Refer to Report Log Files .

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Generate
                                             				  Phone Reports . The Report Phone Query window appears. |
|---|---|
| Step 2 | In the first Find Phone where drop-down list box, choose
                                       			 the field to query such as Device Name or Directory Number . |
| Step 3 | In the second drop-down list box, choose the search criteria such
                                       			 as begins with, contains, or is empty. |
| Step 4 | In the search field/list box, either choose or enter the value
                                       			 that you want to locate, such as the model name from the list or directory
                                       			 number range. |
| Step 5 | Specify the appropriate search text, if applicable, and click Find . Tip To generate a report for all phones that are registered in the
                                                      				  database, click Find without entering any search text. To further define your query and to add multiple filters, check
                                          				the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Steps Step 2 through Step 5 . A list of discovered phones appears. | Tip | To generate a report for all phones that are registered in the
                                                      				  database, click Find without entering any search text. |
| Tip | To generate a report for all phones that are registered in the
                                                      				  database, click Find without entering any search text. |
| Step 6 | To choose details for your type of report, click Next . The Generate Phone Report Configuration window
                                       			 appears and shows the Query that you chose. Tip If you want to change the type of query, click Back . | Tip | If you want to change the type of query, click Back . |
| Tip | If you want to change the type of query, click Back . |
| Step 7 | In the Report File Name field, enter your name for
                                       			 this report (required). |
| Step 8 | In the Available Device Fields drop-down list box,
                                       			 choose a device item and click the arrow to move the item into the Selected Fields for this Report list. You must specify at least one device field to generate a report.
                                       			 You can choose multiple fields to include in your report. For a list of device
                                       			 and live fields, see the Phone and IP Telephony Device Reports . Tip To rearrange the order of the items in the Selected Device Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. | Tip | To rearrange the order of the items in the Selected Device Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. |
| Tip | To rearrange the order of the items in the Selected Device Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. |
| Step 9 | In the Available Line Fields drop-down list box,
                                       			 choose a line item and click the arrow to move the item into the Selected Fields for this Report list. You must specify at least one line field to generate a report.
                                       			 You can choose multiple fields to include in your report. Tip To rearrange the order of the items in the Selected Line Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. | Tip | To rearrange the order of the items in the Selected Line Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. |
| Tip | To rearrange the order of the items in the Selected Line Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. |
| Step 10 | If you want to include IP phone services fields in your report,
                                       			 check the check boxes for Speed Dial Services and/or IP Phone Services . |
| Step 11 | In the Job Information area, enter the Job description. |
| Step 12 | Choose when to generate the report. Do one of the following: Click Run Immediately to generate the report
                                             				  immediately. Click Run Later to generate the report at a
                                             				  later time. |
| Step 13 | To create a job for inserting the phone records, click Submit . Use the Job Configuration window to schedule this job, activate this job, or both. |

| Tip | To generate a report for all phones that are registered in the
                                                      				  database, click Find without entering any search text. |
|---|---|

| Tip | If you want to change the type of query, click Back . |
|---|---|

| Tip | To rearrange the order of the items in the Selected Device Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. |
|---|---|

| Tip | To rearrange the order of the items in the Selected Line Fields for this Report list, choose an item and click the
                                                      				  Up arrow or Down arrow to move the item to another position in the list. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Generate
                                                				  Phone Reports . The Report Phone Query window displays. |
|---|---|
| Step 2 | In the first Find Phone(s) where drop-down list box, choose Device Name . |
| Step 3 | In the second drop-down list box, choose begins with . |
| Step 4 | In the text field, enter BAT . All phones that are added with a dummy MAC address have device names that begin with BAT. |
| Step 5 | Click Find . The text Device Name begins with 'BAT'
                                          			 and displays in the query text box. |
| Step 6 | Click Next . The Generate Phone Report Configuration window
                                          			 displays. |