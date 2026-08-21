---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-761d5ec598
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_0110010.html
retrieved_at: 2026-08-21T09:11:20.778226+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Gateway Insertions

## Chapter: Gateway Insertions

# Gateway Insertions

This chapter provides information to insert Cisco-supported
                        		gateways into Cisco Unified Communications Manager database.

## CSV Data File Creation for Cisco VG200 Gateways

You can create a CSV data file to insert Cisco VG200 gateways and ports in the database. Use either the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG200 Gateways and T1 CAS, T1 PRI, E1 PRI, FXS or FXO Ports Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that
                                 		  contains the details, such as domain name, MGCP description, and port
                                 		  identifier, for individual T1 CAS, T1 PRI, E1 PRI, FXS or FXO ports.

For T1 CAS only, the ports that you specify in the BAT spreadsheet
                                 		  must be the same ports that you specified in the VG200 template. In the CSV
                                 		  data file, you can specify none, some, or all ports that were configured in the
                                 		  template. Do not configure any ports in the CSV data file that were not also
                                 		  configured in the template, or an error will result when you attempt to insert
                                 		  the BAT VG200 template and the CSV file.

For example, if you configured ports 1,2,3, and 4 in the template, you
                                 		  could configure none of the ports, or ports 1, 2, 3, and 4, or only ports 1 and
                                 		  2 in the CSV file, and the insertion would be accepted. But if you configured
                                 		  ports 5 and 6 in the CSV file when they are not configured in the template, you
                                 		  will receive an insertion error in BAT.

After you are finished editing the fields for the gateway ports in the
                                 		  BAT spreadsheet, export the file. The system saves the file to C:\XLSDataFiles or to your choice of another
                                 		  existing folder on your local workstation using the following default filename:

VG200Gateways#timestamp.txt

where " timestamp " represents the precise date and time that the file was created.

Attention

If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                             If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                             after a blank line does not get converted to the BAT format.

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

Click the VG200 T1-Pri T1-Cas E1-Pri FXSFXO tab.

Step 4

For T1 CAS endpoints only, scroll to the right until you see the Number of Port Identifiers field. Enter the
                                          			 number of port identifiers that you want to add for each Cisco VG200 gateway.
                                          			 If you want only one port identifier, skip this step.

Step 5

Provide the information for the following fields.

Field

Description

MGCP Domain Name

Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if it is configured
                                                         to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway.

The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                         on the gateway to resolve to vg200-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                         case, vg200-1). If the host name is configured on the gateway as vg200-1 and the IP domain name is configured on the gateway
                                                         as cisco.com, enter vg200-1.cisco.com in this field.

MGCP Description

Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the gateway.

Port Description

Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list of ports. This
                                                         applies to the description field for port 2 through port 4.

Port Directory Number

Enter the directory number, up to 24 numerals and special characters, for this port. This applies to the directory number
                                                         field for port 2 through port 4.

Attention

Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank.

Slot

Enter the slot number that you are trying to configure. For VG200, it is always 1.

Subunit

Enter an integer for the subunit value.

Port Number

Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format .

The system saves the file using the default filename VG200Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another
                                             				existing folder on your local workstation, where " timestamp " represents the precise date and
                                             				time that the file was created.

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Gateways window in BAT.

#### What to do next

You must upload the CSV data file to the first node of the server, so BAT can access the data input file.

## Create CSV Data File for Cisco Catalyst 6000 (FXS) Ports

You can create the CSV data file to insert Cisco Catalyst 6000 (FXS) ports, such as directory number and a description of
                              the port, in the database. Use either the BAT spreadsheet or a text editor to create the CSV data file.

Step 1

To open the BAT Spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities.

Step 3

Click the Catalyst 6000 (FXS) Ports tab.

Step 4

Enter information for each port record in a row.

Complete all mandatory fields and any relevant, optional fields.
                                          				Each column heading specifies the length of the field.

MAC Address—Enter the 12-character MAC address for the gateway.

Port Number—Enter the numeric port number (1 through 24) that you want to add to the gateway.

Directory Number—Enter a directory number, up to 24 numerals and special characters, for this port. You must enter a directory
                                                number if you have specified a partition.(Optional)

Partition—Enter the route partition, up to 50 characters, to which you want this port to belong. Do not specify a partition
                                                unless you also have specified a directory number. (Optional).

Caution

The system treats blank rows in the spreadsheet as End of File
                                                      				  and discards subsequent records.

Step 5

To transfer the data from the BAT Excel spreadsheet into a CSV
                                       			 file, click Export to BAT Format .

The system saves the file to C:\XLSDataFiles\ or to your choice of another
                                          				existing folder.

For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Gateways window in BAT.

### What to do next

You must upload the CSV data file to the first node of the server, so BAT can access the data input file. For more information, see Upload and Download Files .

## CSV Data Files Creation for Cisco VG224 Gateways and Ports

You can create a CSV data file to insert VG224 gateways and ports in the database. Use either the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG224 FXS Gateways and Ports Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that
                                 		  contains the details, such as domain name, MGCP description, and port
                                 		  identifier, for individual FXS ports.

After you are finished editing the fields for the gateway ports in the
                                 		  BAT spreadsheet, export the file. The system saves the file to C:\XLSDataFiles or to your choice of another
                                 		  existing folder on your local workstation using the following default filename:

VG224Gateways#timestamp.txt

where " timestamp " represents the precise date and time
                                 		  that the file was created.

Tip

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

Click the VG224 tab.

For MGCP protocol, click the MGCP radio button.

For SCCP protocol, click the SCCP radio button.

Step 4

Do one of the following:

If you choose MGCP, skip to Step 5 .

If you choose SCCP, a Create File Format button appears in the
                                                				  spreadsheet.

Click Create File Format , the Field Selection window displays.

From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG224 sheet.

Step 5

Provide the information for the following fields:

Domain Name—Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name
                                                   if it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway.

The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to vg224-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, vg224-1). If the host name is configured on the gateway as vg224-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter vg224-1.cisco.com in this field.

Description—Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Port Description—Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 to port 4.

Port Directory Number—Enter the directory number, up to 24 numerals and special characters, for this port. This applies to
                                                   the directory number field for port 2 to port 4.

Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank.

Slot 2—Enter the slot number that you are trying to configure. For VG224, the slot is always 2.

Subunit—Enter an integer for the subunit value. For VG224, the subunit is always 0.

Port Number—Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format .

The system saves the file using the default filename VG224Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another
                                             				existing folder on your local workstation.

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT.

#### What to do next

You must upload the CSV data file to the first node of the Cisco Unified Communications Manager server, so BAT can access the data input file.

## CSV Data File Creation for Cisco VG202 and VG204 Gateways

You can create a CSV data file to insert VG202 and VG204
                              		  gateways and ports in the Cisco Unified Communications Manager database. Use either the BAT spreadsheet or a
                              		  text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG202 and VG204 FXS Gateways and Ports Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that
                                 		  contains the details, such as domain name, MGCP description, and port
                                 		  identifier, for individual FXS ports.

After you are finished editing the fields for the gateway ports in the
                                 		  BAT spreadsheet, export the file. The system saves the file to C:\XLSDataFiles or to your choice of another
                                 		  existing folder on your local workstation using the following default filename:

VG202Gateways#timestamp.txt or VG204Gateways#timestamp.txt

where " timestamp " represents the precise date and time
                                 		  at which the file was created.

Tip

If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format. If you enter a
                                             			 blank row in the spreadsheet, the system treats the empty row as the end of the
                                             			 file. Data that is entered after a blank line does not get converted to the BAT
                                             			 format.

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

Click the VG202-VG204 tab.

For MGCP, click the MGCP radio button.

For SCCP, click the SCCP radio button.

Step 4

Do one of the following:

If you choose MGCP, proceed to Step 5 .

If you choose SCCP, a Create File Format button appears in the
                                                				  spreadsheet.

Click Create File Format; the Field Selection window displays.

From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device
                                                         Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG224 sheet.

Step 5

Provide the information for the following fields:

Domain Name/MAC Address—Enter a name from 1 to 64 characters, that identifies the gateway. Use the Domain Name System (DNS)
                                                   host name if it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. For
                                                   SCCP gateways, use the MAC address.

The host name must match exactly the host name that is configured on the Cisco IOS gateway. For example, if the host name
                                                   is configured on the gateway to resolve to vg204-1 and the IP domain name is not configured, enter the host name in this field
                                                   (in this case, vg204-1). If the host name is configured on the gateway as vg204-1 and the IP domain name is configured on
                                                   the gateway as cisco.com, enter vg204-1.cisco.com in this field.

Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Slot—Enter the slot number that you are trying to configure. For VG202 and VG204, the slot always equals 0.

Subunit—Enter an integer for the subunit value. For VG202 and VG204, the subunit always equals 0.

Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 to port 4.

Be aware that Port 1 Directory Number and Partition fields are required for FXS ports only.

Port Number—Enter an integer for the Port Number.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to identify the requried port in a
                                                   list of ports. This applies to the description field for port 2 to port 4.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format .

The system saves the file using the default filename VG202Gateways#timestamp.txt or VG204Gateways#timestamp.txt to C:\XLSDataFiles on your local workstation or to your choice of another existing folder.

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT.

#### What to do next

You must upload the CSV data file to the first node of the Cisco Unified Communications Manager server, so BAT can access the data input file.

## CSV Data Files Creation for Cisco VG310 Gateways and Ports

You can create a CSV data file to insert VG310 gateways and ports in the database. Use either the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG310 FXS Gateways and Ports Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that contains the details, such as domain name, MGCP description, and
                                 port identifier, for individual FXS ports.

After you are finished editing the fields for the gateway ports in the BAT spreadsheet, export the file. The system saves
                                 the file to C:\XLSDataFiles or to your choice of another existing folder on your local workstation using the following default filename:

VG310Gateways#timestamp.txt

where " timestamp " represents the precise date and time that the file was created.

Tip

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet capabilities.

Step 3

Click the VG310 tab.

For MGCP protocol, click the MGCP radio button.

For SSCP protocol, click the SCCP radio button.

Step 4

Do one of the following:

If you choose MGCP, skip to Step 5 .

If you choose SCCP, a Create File Format button appears in the spreadsheet.

Click Create File Format , the Field Selection window displays.

From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG310 sheet when you have selected the required fields

Step 5

Provide the information for the following fields:

Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway.

The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG310-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG310-1). If the host name is configured on the gateway as VG310-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG310-1.cisco.com in this field.

Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 to port 4.

Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 to port 4.

Slot 2—Enter the slot number that you are trying to configure. For VG310, the slot is always 2.

Subunit—Enter an integer for the subunit value. For VG310, the subunit is always 0.

Port Number—Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format .

The system saves the file using the default filename VG310Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation.

#### What to do next

You must upload the CSV data file to the first node of the Unified Communications Manager server, so BAT can access the data
                                 input file.

## CSV Data Files Creation for Cisco VG320 Gateways and Ports

You can create a CSV data file to insert VG320 gateways and ports in the database. Use either the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG320 FXS Gateways and Ports Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that contains the details, such as domain name, MGCP description, and
                                 port identifier, for individual FXS ports.

After you are finished editing the fields for the gateway ports in the BAT spreadsheet, export the file. The system saves
                                 the file to C:\XLSDataFiles or to your choice of another existing folder on your local workstation using the following default filename:

VG320Gateways#timestamp.txt

where " timestamp " represents the precise date and time that the file was created.

Tip

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet capabilities.

Step 3

Click the VG320 tab.

For MGCP protocol, click the MGCP radio button.

For SCCP protocol, click the SCCP radio button.

Step 4

Do one of the following:

If you choose MGCP, skip to Step 5 .

If you choose SCCP, a Create File Format button appears in the spreadsheet.

Click Create File Format , the Field Selection window displays.

From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG320 sheet when you have selected the required fields.

Step 5

Provide the information for the following fields:

Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway.

The host name must exactly the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG320-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG320-1). If the host name is configured on the gateway as VG320-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG320-1.cisco.com in this field.

Description—Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 to port 4.

Port Directory Number—Enter the directory number, up to 24 numerals and special characters, for this port. This applies to
                                                   the directory number field for port 2 to port 4.

Slot 2—Enter the slot number that you are trying to configure. For VG320, the slot is always 2.

Subunit—Enter an integer for the subunit value. For VG320, the subunit is always 0.

Port Number—Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format .

The system saves the file using the default filename VG320Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation.

#### What to do next

You must upload the CSV data file to the first node of the Unified Communications Manager server, so BAT can access the data
                                 input file.

## CSV Data Files Creation for Cisco VG350 Gateways and Ports

You can create a CSV data file to insert VG350 gateways and ports in the Unified Communications Manager database. Use either
                           the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG350 FXS  Gateways and Ports Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that contains the details, such as domain name, MGCP description, and
                                 port identifier, for individual FXS ports.

After you are finished editing the fields for the gateway ports in the BAT spreadsheet, export the file. The system saves
                                 the file to C:\XLSDataFiles or to your choice of another existing folder on your local workstation using the following default filename:

VG350Gateways#timestamp.txt

where " timestamp " represents the precise date and time that the file was created.

Tip

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet capabilities.

Step 3

Click the VG350 tab.

For MGCP protocol, click the MGCP radio button.

For SCCP protocol, click the SCCP radio button.

Step 4

Do one of the following:

If you choose MGCP, skip to Step 5 .

If you choose SCCP, a Create File Format button appears in the spreadsheet.

Click Create File Format , the Field Selection window displays.

From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG350 sheet when you have selected the required fields.

Step 5

Provide the information for the following fields:

Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway.

The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG350-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG350-1). If the host name is configured on the gateway as VG350-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG350-1.cisco.com in this field.

Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 through port 4.

Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 through port 4.

Slot 2—Enter the slot number that you are trying to configure. For VG350, the slot is always 2.

Subunit—Enter an integer for the subunit value. For VG350, the subunit is always 0.

Port Number—Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format .

The system saves the file using the default filename VG350Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation.

#### What to do next

You must upload the CSV data file to the first node of the Unified Communications Manager server, so BAT can access the data
                                 input file.

## CSV Data File Creation for Cisco VG420 Gateways

You can create a CSV data file to insert VG420 gateways and ports in the Unified Communications Manager database. Use either
                              the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG420 Gateways Using BAT Spreadsheet

After you are complete editing the fields for the gateway ports in the BAT spreadsheet, export the file. The system saves
                                 the file to C:\XLSDataFiles or to your choice of another existing folder on your local workstation using the following default filename:

VG420Gateways#timestamp.txt

where " timestamp " represents the precise date and time that the file was created.

Tip

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet capabilities.

Step 3

Click the VG420 tab.

For MGCP protocol, click the MGCP radio button.

For SCCP protocol, click the SCCP radio button.

For SIP protocol, click the SIP radio button.

Step 4

Do one of the following:

If you choose MGCP, skip to step 6

If you choose SCCP or SIP , a Create File Format button appears in the spreadsheet.

Click Create File Format , the Field Selection window displays.

From the Device Fields box, select the required device fields and click the >> button to move them to the Selected Device Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG420 sheet when you have selected the required fields.

Step 5

Provide the information in the following fields:

Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) hostname if
                                                   it is configured to resolve correctly; otherwise, use the hostname as defined on the Cisco MGCP gateway.

The hostname must match the hostname that is configured on the Cisco IOS gateway. For example, if the hostname is configured
                                                   on the gateway to resolve to VG420-1 and the IP domain name is not configured, enter the hostname in this field (in this case,
                                                   VG420-1). If the hostname is configured on the gateway as VG420-1 and the IP domain name is configured on the gateway as cisco.com,
                                                   enter VG420-1.cisco.com in this field.

Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports.

Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port.

Slot—Enter the slot number that you are trying to configure. For VG420, the slot can be 0 or 1.

Subunit—Enter an integer for the subunit value. For VG420, for slot 0, the subunit can be 1, 2, or 3. For slot 1, the subunit
                                                   is always 0.

Port Number—Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format .

The system saves the file using the default filename VG420Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation.

Tip

#### What to do next

You must upload the CSV data file to the first node of the Unified Communications Manager server, so BAT can access the data
                                 input file.

## CSV Data Files Creation for Cisco VG450 Gateways and Ports

You can create a CSV data file to insert VG450 gateways and ports in the Unified Communications Manager database. Use either
                           the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco VG450 FXS Gateways and Ports Using BAT Spreadsheet

After you are complete editing the fields for the gateway ports in the BAT spreadsheet, export the file. The system saves
                                 the file to C:\XLSDataFiles or to your choice of another existing folder on your local workstation using the following default filename:

VG450Gateways#timestamp.txt

where " timestamp " represents the precise date and time that the file was created.

Tip

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet capabilities.

Step 3

Click the VG450 tab.

For MGCP protocol, click the MGCP radio button.

For SCCP protocol, click the SCCP radio button.

For SIP protocol, click the SIP radio button.

Step 4

Do one of the following:

If you choose MGCP, skip to step 6

If you choose SCCP or SIP , a Create File Format button appears in the spreadsheet.

Click Create File Format , the Field Selection window displays.

From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the VG450 sheet when you have selected the required fields.

Step 5

Provide the information in the following fields:

Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway.

The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG450-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG450-1). If the host name is configured on the gateway as VG450-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG450-1.cisco.com in this field.

Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 through port 4.

Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 through port 4.

Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank.

Slot 2—Enter the slot number that you are trying to configure. For VG450, the slot is always 2.

Subunit—Enter an integer for the subunit value. For VG450, the subunit is always 0.

Port Number—Enter an integer for the Port Number.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format .

The system saves the file using the default filename VG450Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation.

Tip

For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT.

#### What to do next

You must upload the CSV data file to the first node of the Unified Communications Manager server, so BAT can access the data
                                 input file.

## CSV Data File Creation for Cisco ISR 4461 Gateways

You can create a CSV data file to insert ISR 4461 gateways in the Cisco Unified Communications Manager database. Use either
                           the BAT spreadsheet or a text editor to create the CSV data file.

### Create CSV Data Files for Cisco ISR 4461 Gateways Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file that contains the details, such as domain name, MGCP description, and
                                 other relevant information.

After you are finished editing the fields for the gateway ports in the BAT spreadsheet, export the file. The system saves
                                 the file to C:\XLSDataFiles or to your choice of another existing folder on your local workstation using the following default filename:

ISR4461Gateways-#timestamp.txt

where " timestamp " represents the precise date and time at which the file was created.

Tip

If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                             If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                             after a blank line does not get converted to the BAT format.

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet capabilities.

Step 3

Click the ISR 4461 tab.

For MGCP protocol, click the MGCP radio button.

For SCCP protocol, click the SCCP radio button.

For SIP protocol, click the SIP radio button.

Step 4

Do one of the following:

If you choose MGCP, proceed to Step 5 .

If you choose SCCP or SIP , a Create File Format button appears in the spreadsheet.

Click Create File Format ; the Field Selection window displays.

From the Device Fields box, select the required device fields and click the >> button to move them to the Selected Device
                                                         Fields box.

From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box.

Click the Up and Down buttons to rearrange the selected fields.

Click the << button to remove any of the selected fields from the selected fields list.

Click Create to add the selected fields to the ISR 4461 sheet when you have selected the required fields.

Step 5

In each row, provide the information for the following fields:

Domain Name/MAC Address—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS)
                                                   host name if it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. For
                                                   SCCP gateways and SIP gateways, use the MAC address.

The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to ISR 4461 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, ISR 4461). If the host name is configured on the gateway as ISR 4461 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter ISR 4461.cisco.com in this field.

Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway.

Slot—Enter the slot number that you are trying to configure. For ISR 4461, the slot can be 0, 1, 2, or 3.

Subunit—Enter an integer for the subunit value. In ISR 4461, for slot 0, the subunit can be 1, 2, or 3. For slot 1, 2, or
                                                   3, the subunit is always 0.

Port Directory Number—Enter the directory number, up to 24 numerals and special characters, for this port. This applies to
                                                   the directory number field for port 2 through port 4.

Port 1 Directory Number and Partition fields are required for FXS ports only.

Port Number—Enter an integer for the Port Number.

Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 through port 4.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format .

The system saves the file using the default filename ISR4461Gateways-#timestamp.txt to C:\XLSDataFiles on your local workstation or to your choice of another existing folder.

For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT.

#### What to do next

You must upload the CSV data file to the first node of the Unified Communications Manager server, so BAT can access the data
                                 input file.

## Insert Gateways and Ports to Cisco Unified Communications Manager

You can use the BAT spreadsheet to add Cisco gateways and
                              		  ports to Cisco Unified Communications Manager .

### Before you begin

If you want to insert a CiscoVG200 gateway, you must have a Cisco VG200 gateway template for the trunks or ports, and a CSV
                                    data file for the VG200 gateway ports. See Create Cisco VG200 Gateway Template and CSV Data File Creation for Cisco VG200 Gateways .

If you want to insert a CiscoCatalyst 6000 Port, you must have a CiscoCatalyst 6000 Ports template and a CSV data file that
                                    contains port details for this bulk transaction. See Create Cisco Catalyst 6000 (FXS) Gateway Template and Create CSV Data File for Cisco Catalyst 6000 (FXS) Ports .

If you want to insert a CiscoVG224 gateway, you must have a Cisco VG224 gateway template for the trunks or ports, and a CSV
                                    data file for the VG224 gateway ports. See Create Cisco VG200 Gateway Template and CSV Data File Creation for Cisco VG200 Gateways .

If you want to insert a CiscoVG202 or VG204 gateway, you must have a Cisco VG202 or VG204 gateway template for the trunks
                                    or ports and a CSV data file for the VG202 or VG204 gateway ports. See Create Cisco VG202 or VG204 Gateway Template and CSV Data File Creation for Cisco VG202 and VG204 Gateways .

Step 1

Choose Bulk
                                             				  Administration > Gateways > Insert
                                             				  Gateways .

The Insert Gateways Configuration window displays.

Step 2

From the Gateway Type drop-down list, choose the type of gateway you want to insert.

The Insert Gateway Configuration window displays.

Step 3

Choose the name of the CSV data file that contains the Cisco VG200 gateway information to be added from the File Name field drop-down list.

Step 4

Choose the name of the VG200 or the FXS gateway template that you created for this type of bulk transaction in the Gateway Template Name field.

Step 5

(Optional) Check the Override the existing configuration button to overwrite the existing gateway settings with the information that is contained in the file that you want to insert.

Step 6

Enter the job description in the Job Information area.

Step 7

Choose an insert method. Do one of the following:

Click Run Immediately to insert the gateway
                                             				  immediately.

Click Run Later to insert the gateway later.

Step 8

Click Submit to create a job for inserting the gateways.

| Attention | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                             If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                             after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | Click the VG200 T1-Pri T1-Cas E1-Pri FXSFXO tab. |
| Step 4 | For T1 CAS endpoints only, scroll to the right until you see the Number of Port Identifiers field. Enter the
                                          			 number of port identifiers that you want to add for each Cisco VG200 gateway.
                                          			 If you want only one port identifier, skip this step. |
| Step 5 | Provide the information for the following fields. Table 1. VG200 gateway T1 CAS, T1-PRI, E1-PRI, FXS and FXO ports field settings Field Description MGCP Domain Name Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if it is configured
                                                         to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                         on the gateway to resolve to vg200-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                         case, vg200-1). If the host name is configured on the gateway as vg200-1 and the IP domain name is configured on the gateway
                                                         as cisco.com, enter vg200-1.cisco.com in this field. MGCP Description Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the gateway. Port Description Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list of ports. This
                                                         applies to the description field for port 2 through port 4. Port Directory Number Enter the directory number, up to 24 numerals and special characters, for this port. This applies to the directory number
                                                         field for port 2 through port 4. Attention Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot Enter the slot number that you are trying to configure. For VG200, it is always 1. Subunit Enter an integer for the subunit value. Port Number Enter an integer for the Port Number. | Field | Description | MGCP Domain Name | Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if it is configured
                                                         to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                         on the gateway to resolve to vg200-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                         case, vg200-1). If the host name is configured on the gateway as vg200-1 and the IP domain name is configured on the gateway
                                                         as cisco.com, enter vg200-1.cisco.com in this field. | MGCP Description | Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the gateway. | Port Description | Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list of ports. This
                                                         applies to the description field for port 2 through port 4. | Port Directory Number | Enter the directory number, up to 24 numerals and special characters, for this port. This applies to the directory number
                                                         field for port 2 through port 4. Attention Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. | Attention | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. | Slot | Enter the slot number that you are trying to configure. For VG200, it is always 1. | Subunit | Enter an integer for the subunit value. | Port Number | Enter an integer for the Port Number. |
| Field | Description |
| MGCP Domain Name | Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if it is configured
                                                         to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                         on the gateway to resolve to vg200-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                         case, vg200-1). If the host name is configured on the gateway as vg200-1 and the IP domain name is configured on the gateway
                                                         as cisco.com, enter vg200-1.cisco.com in this field. |
| MGCP Description | Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the gateway. |
| Port Description | Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list of ports. This
                                                         applies to the description field for port 2 through port 4. |
| Port Directory Number | Enter the directory number, up to 24 numerals and special characters, for this port. This applies to the directory number
                                                         field for port 2 through port 4. Attention Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. | Attention | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Attention | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Slot | Enter the slot number that you are trying to configure. For VG200, it is always 1. |
| Subunit | Enter an integer for the subunit value. |
| Port Number | Enter an integer for the Port Number. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format . The system saves the file using the default filename VG200Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another
                                             				existing folder on your local workstation, where " timestamp " represents the precise date and
                                             				time that the file was created. Note For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Gateways window in BAT. |

| Field | Description |
|---|---|
| MGCP Domain Name | Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if it is configured
                                                         to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                         on the gateway to resolve to vg200-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                         case, vg200-1). If the host name is configured on the gateway as vg200-1 and the IP domain name is configured on the gateway
                                                         as cisco.com, enter vg200-1.cisco.com in this field. |
| MGCP Description | Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the gateway. |
| Port Description | Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list of ports. This
                                                         applies to the description field for port 2 through port 4. |
| Port Directory Number | Enter the directory number, up to 24 numerals and special characters, for this port. This applies to the directory number
                                                         field for port 2 through port 4. Attention Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. | Attention | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Attention | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Slot | Enter the slot number that you are trying to configure. For VG200, it is always 1. |
| Subunit | Enter an integer for the subunit value. |
| Port Number | Enter an integer for the Port Number. |

| Attention | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Gateways window in BAT. |
|---|---|

| Step 1 | To open the BAT Spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities. |
| Step 3 | Click the Catalyst 6000 (FXS) Ports tab. |
| Step 4 | Enter information for each port record in a row. Complete all mandatory fields and any relevant, optional fields.
                                          				Each column heading specifies the length of the field. MAC Address—Enter the 12-character MAC address for the gateway. Port Number—Enter the numeric port number (1 through 24) that you want to add to the gateway. Directory Number—Enter a directory number, up to 24 numerals and special characters, for this port. You must enter a directory
                                                number if you have specified a partition.(Optional) Partition—Enter the route partition, up to 50 characters, to which you want this port to belong. Do not specify a partition
                                                unless you also have specified a directory number. (Optional). Caution The system treats blank rows in the spreadsheet as End of File
                                                      				  and discards subsequent records. | Caution | The system treats blank rows in the spreadsheet as End of File
                                                      				  and discards subsequent records. |
| Caution | The system treats blank rows in the spreadsheet as End of File
                                                      				  and discards subsequent records. |
| Step 5 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                       			 file, click Export to BAT Format . The system saves the file to C:\XLSDataFiles\ or to your choice of another
                                          				existing folder. Note For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Gateways window in BAT. |

| Caution | The system treats blank rows in the spreadsheet as End of File
                                                      				  and discards subsequent records. |
|---|---|

| Note | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt
                                          		  encloses that field entry in double quotes when you export to BAT format. If
                                          		  you enter a blank row in the spreadsheet, the system treats the empty row as
                                          		  the end of the file. Data that is entered after a blank line does not get
                                          		  converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | Click the VG224 tab. For MGCP protocol, click the MGCP radio button. For SCCP protocol, click the SCCP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, skip to Step 5 . If you choose SCCP, a Create File Format button appears in the
                                                				  spreadsheet. Click Create File Format , the Field Selection window displays. From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG224 sheet. |
| Step 5 | Provide the information for the following fields: Domain Name—Enter a name, from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name
                                                   if it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to vg224-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, vg224-1). If the host name is configured on the gateway as vg224-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter vg224-1.cisco.com in this field. Description—Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Port Description—Enter a description for port 1, up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 to port 4. Port Directory Number—Enter the directory number, up to 24 numerals and special characters, for this port. This applies to
                                                   the directory number field for port 2 to port 4. Note Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot 2—Enter the slot number that you are trying to configure. For VG224, the slot is always 2. Subunit—Enter an integer for the subunit value. For VG224, the subunit is always 0. Port Number—Enter an integer for the Port Number. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format . The system saves the file using the default filename VG224Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another
                                             				existing folder on your local workstation. Note For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format. If you enter a
                                             			 blank row in the spreadsheet, the system treats the empty row as the end of the
                                             			 file. Data that is entered after a blank line does not get converted to the BAT
                                             			 format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | Click the VG202-VG204 tab. For MGCP, click the MGCP radio button. For SCCP, click the SCCP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, proceed to Step 5 . If you choose SCCP, a Create File Format button appears in the
                                                				  spreadsheet. Click Create File Format; the Field Selection window displays. From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device
                                                         Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG224 sheet. |
| Step 5 | Provide the information for the following fields: Domain Name/MAC Address—Enter a name from 1 to 64 characters, that identifies the gateway. Use the Domain Name System (DNS)
                                                   host name if it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. For
                                                   SCCP gateways, use the MAC address. The host name must match exactly the host name that is configured on the Cisco IOS gateway. For example, if the host name
                                                   is configured on the gateway to resolve to vg204-1 and the IP domain name is not configured, enter the host name in this field
                                                   (in this case, vg204-1). If the host name is configured on the gateway as vg204-1 and the IP domain name is configured on
                                                   the gateway as cisco.com, enter vg204-1.cisco.com in this field. Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Slot—Enter the slot number that you are trying to configure. For VG202 and VG204, the slot always equals 0. Subunit—Enter an integer for the subunit value. For VG202 and VG204, the subunit always equals 0. Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 to port 4. Note Be aware that Port 1 Directory Number and Partition fields are required for FXS ports only. Port Number—Enter an integer for the Port Number. Port Description—Enter a description for port 1 up to 50 characters. Use a description to identify the requried port in a
                                                   list of ports. This applies to the description field for port 2 to port 4. | Note | Be aware that Port 1 Directory Number and Partition fields are required for FXS ports only. |
| Note | Be aware that Port 1 Directory Number and Partition fields are required for FXS ports only. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format . The system saves the file using the default filename VG202Gateways#timestamp.txt or VG204Gateways#timestamp.txt to C:\XLSDataFiles on your local workstation or to your choice of another existing folder. Note For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Be aware that Port 1 Directory Number and Partition fields are required for FXS ports only. |
|---|---|

| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                          If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                          after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet capabilities. |
| Step 3 | Click the VG310 tab. For MGCP protocol, click the MGCP radio button. For SSCP protocol, click the SCCP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, skip to Step 5 . If you choose SCCP, a Create File Format button appears in the spreadsheet. Click Create File Format , the Field Selection window displays. From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG310 sheet when you have selected the required fields |
| Step 5 | Provide the information for the following fields: Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG310-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG310-1). If the host name is configured on the gateway as VG310-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG310-1.cisco.com in this field. Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 to port 4. Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 to port 4. Note Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot 2—Enter the slot number that you are trying to configure. For VG310, the slot is always 2. Subunit—Enter an integer for the subunit value. For VG310, the subunit is always 0. Port Number—Enter an integer for the Port Number. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format . The system saves the file using the default filename VG310Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation. Note For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                          If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                          after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet capabilities. |
| Step 3 | Click the VG320 tab. For MGCP protocol, click the MGCP radio button. For SCCP protocol, click the SCCP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, skip to Step 5 . If you choose SCCP, a Create File Format button appears in the spreadsheet. Click Create File Format , the Field Selection window displays. From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG320 sheet when you have selected the required fields. |
| Step 5 | Provide the information for the following fields: Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must exactly the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG320-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG320-1). If the host name is configured on the gateway as VG320-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG320-1.cisco.com in this field. Description—Enter a description, up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 to port 4. Port Directory Number—Enter the directory number, up to 24 numerals and special characters, for this port. This applies to
                                                   the directory number field for port 2 to port 4. Note Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot 2—Enter the slot number that you are trying to configure. For VG320, the slot is always 2. Subunit—Enter an integer for the subunit value. For VG320, the subunit is always 0. Port Number—Enter an integer for the Port Number. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format . The system saves the file using the default filename VG320Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation. Note For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                          If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                          after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet capabilities. |
| Step 3 | Click the VG350 tab. For MGCP protocol, click the MGCP radio button. For SCCP protocol, click the SCCP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, skip to Step 5 . If you choose SCCP, a Create File Format button appears in the spreadsheet. Click Create File Format , the Field Selection window displays. From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG350 sheet when you have selected the required fields. |
| Step 5 | Provide the information for the following fields: Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG350-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG350-1). If the host name is configured on the gateway as VG350-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG350-1.cisco.com in this field. Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 through port 4. Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 through port 4. Note Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot 2—Enter the slot number that you are trying to configure. For VG350, the slot is always 2. Subunit—Enter an integer for the subunit value. For VG350, the subunit is always 0. Port Number—Enter an integer for the Port Number. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format . The system saves the file using the default filename VG350Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation. Note For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                          If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                          after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet capabilities. |
| Step 3 | Click the VG420 tab. For MGCP protocol, click the MGCP radio button. For SCCP protocol, click the SCCP radio button. For SIP protocol, click the SIP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, skip to step 6 If you choose SCCP or SIP , a Create File Format button appears in the spreadsheet. Click Create File Format , the Field Selection window displays. From the Device Fields box, select the required device fields and click the >> button to move them to the Selected Device Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG420 sheet when you have selected the required fields. |
| Step 5 | Provide the information in the following fields: Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) hostname if
                                                   it is configured to resolve correctly; otherwise, use the hostname as defined on the Cisco MGCP gateway. The hostname must match the hostname that is configured on the Cisco IOS gateway. For example, if the hostname is configured
                                                   on the gateway to resolve to VG420-1 and the IP domain name is not configured, enter the hostname in this field (in this case,
                                                   VG420-1). If the hostname is configured on the gateway as VG420-1 and the IP domain name is configured on the gateway as cisco.com,
                                                   enter VG420-1.cisco.com in this field. Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. Note Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot—Enter the slot number that you are trying to configure. For VG420, the slot can be 0 or 1. Subunit—Enter an integer for the subunit value. For VG420, for slot 0, the subunit can be 1, 2, or 3. For slot 1, the subunit
                                                   is always 0. Port Number—Enter an integer for the Port Number. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format . The system saves the file using the default filename VG420Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation. Tip For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. | Tip | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
| Tip | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Tip | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                          If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                          after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet capabilities. |
| Step 3 | Click the VG450 tab. For MGCP protocol, click the MGCP radio button. For SCCP protocol, click the SCCP radio button. For SIP protocol, click the SIP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, skip to step 6 If you choose SCCP or SIP , a Create File Format button appears in the spreadsheet. Click Create File Format , the Field Selection window displays. From the Device Fields box, select the required device fields and click on the >> button to move them to the Selected Device Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the VG450 sheet when you have selected the required fields. |
| Step 5 | Provide the information in the following fields: Domain Name—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS) host name if
                                                   it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to VG450-1 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, VG450-1). If the host name is configured on the gateway as VG450-1 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter VG450-1.cisco.com in this field. Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 through port 4. Port Directory Number—Enter the directory number up to 24 numerals and special characters for this port. This applies to the
                                                   directory number field for port 2 through port 4. Note Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. Slot 2—Enter the slot number that you are trying to configure. For VG450, the slot is always 2. Subunit—Enter an integer for the subunit value. For VG450, the subunit is always 0. Port Number—Enter an integer for the Port Number. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format . The system saves the file using the default filename VG450Gateways#timestamp.txt to C:\XLSDataFiles or to your choice of another existing folder on your local workstation. Tip For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. | Tip | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
| Tip | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. For FXO ports, leave these fields blank. |
|---|---|

| Tip | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Tip | If you enter a comma in one of the fields, BAT.xlt encloses that field entry in double quotes when you export to BAT format.
                                             If you enter a blank row in the spreadsheet, the system treats the empty row as the end of the file. Data that is entered
                                             after a blank line does not get converted to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet capabilities. |
| Step 3 | Click the ISR 4461 tab. For MGCP protocol, click the MGCP radio button. For SCCP protocol, click the SCCP radio button. For SIP protocol, click the SIP radio button. |
| Step 4 | Do one of the following: If you choose MGCP, proceed to Step 5 . If you choose SCCP or SIP , a Create File Format button appears in the spreadsheet. Click Create File Format ; the Field Selection window displays. From the Device Fields box, select the required device fields and click the >> button to move them to the Selected Device
                                                         Fields box. From the Line Fields box, select the line fields and click the >> button to move them to the Selected Line Fields box. Click the Up and Down buttons to rearrange the selected fields. Click the << button to remove any of the selected fields from the selected fields list. Click Create to add the selected fields to the ISR 4461 sheet when you have selected the required fields. |
| Step 5 | In each row, provide the information for the following fields: Domain Name/MAC Address—Enter a name from 1 to 64 characters that identifies the gateway. Use the Domain Name System (DNS)
                                                   host name if it is configured to resolve correctly; otherwise, use the host name as defined on the Cisco MGCP gateway. For
                                                   SCCP gateways and SIP gateways, use the MAC address. The host name must match the host name that is configured on the Cisco IOS gateway. For example, if the host name is configured
                                                   on the gateway to resolve to ISR 4461 and the IP domain name is not configured, enter the host name in this field (in this
                                                   case, ISR 4461). If the host name is configured on the gateway as ISR 4461 and the IP domain name is configured on the gateway
                                                   as cisco.com, enter ISR 4461.cisco.com in this field. Description—Enter a description up to 100 characters for the gateway. Use a specific description that helps you locate the
                                                   gateway. Slot—Enter the slot number that you are trying to configure. For ISR 4461, the slot can be 0, 1, 2, or 3. Subunit—Enter an integer for the subunit value. In ISR 4461, for slot 0, the subunit can be 1, 2, or 3. For slot 1, 2, or
                                                   3, the subunit is always 0. Port Directory Number—Enter the directory number, up to 24 numerals and special characters, for this port. This applies to
                                                   the directory number field for port 2 through port 4. Note Port 1 Directory Number and Partition fields are required for FXS ports only. Port Number—Enter an integer for the Port Number. Port Description—Enter a description for port 1 up to 50 characters. Use a description to help identify the port in a list
                                                   of ports. This applies to the description field for port 2 through port 4. | Note | Port 1 Directory Number and Partition fields are required for FXS ports only. |
| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV file, click Export to BAT Format . The system saves the file using the default filename ISR4461Gateways-#timestamp.txt to C:\XLSDataFiles on your local workstation or to your choice of another existing folder. Note For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. | Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |

| Note | Port 1 Directory Number and Partition fields are required for FXS ports only. |
|---|---|

| Note | For information on how to read the exported CSV data file, click the link to View Sample File in the Insert Gateways window in BAT. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Gateways > Insert
                                             				  Gateways . The Insert Gateways Configuration window displays. |
|---|---|
| Step 2 | From the Gateway Type drop-down list, choose the type of gateway you want to insert. The Insert Gateway Configuration window displays. |
| Step 3 | Choose the name of the CSV data file that contains the Cisco VG200 gateway information to be added from the File Name field drop-down list. |
| Step 4 | Choose the name of the VG200 or the FXS gateway template that you created for this type of bulk transaction in the Gateway Template Name field. |
| Step 5 | (Optional) Check the Override the existing configuration button to overwrite the existing gateway settings with the information that is contained in the file that you want to insert. |
| Step 6 | Enter the job description in the Job Information area. |
| Step 7 | Choose an insert method. Do one of the following: Click Run Immediately to insert the gateway
                                             				  immediately. Click Run Later to insert the gateway later. |
| Step 8 | Click Submit to create a job for inserting the gateways. Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or activate this job. |