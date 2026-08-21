---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-7c8c248f1b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0110101.html
retrieved_at: 2026-08-21T08:57:20.457071+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Client Matter Codes and Forced Authorization Codes

## Chapter: Client Matter Codes and Forced Authorization Codes

# Client Matter Codes and Forced Authorization Codes

This chapter provides information about using BAT to configure
                        		Forced Authorization Codes (FAC) and Client Matter Codes (CMC). You can create,
                        		update, delete, or add more CMC or FAC settings using either a CSV data file or
                        		a custom text-based CSV file.

## CMC and FAC Setup Using BAT

Forced Authorization Codes (FAC) and Client Matter Codes (CMC)
                              		  allow you to manage call access and accounting. CMC assists with call
                              		  accounting and billing for billable clients, while Forced Authorization Codes
                              		  regulate the types of calls that certain users can place.

Client Matter Codes force the user to enter a code to specify
                              		  that the call relates to a specific client matter. You can assign client matter
                              		  codes to customers, students, or other populations for call accounting and
                              		  billing purposes. The Forced Authorization Codes feature forces the user to
                              		  enter a valid authorization code before the call completes.

The CMC and FAC features require that you make changes to
                              		  route patterns and update your dial plan documents to reflect that you enabled
                              		  or disabled FAC and/or CMC for each route pattern.

Before you use BAT to configure CMC or FAC, review the
                              		  following information:

Create separate CSV files for CMC and FAC. Do not mix the two
                                    				features in a single CSV file.

When you add CMC or FAC settings for the first time, you can
                                    				create a CSV file through BAT.xlt or create a custom text-based CSV file.

To update, delete, or add more CMC or FAC settings (not first
                                    				time), you can edit an existing CSV file or create a custom text-based CSV
                                    				file.

In the file/spreadsheet, do not enter two or more codes (and
                                    				corresponding settings) on a single line. Designate a single line for each code
                                    				(and corresponding setting). For example, use the following format when you
                                    				enter codes for Forced Authorization Codes:

(Authorization Code, Authorization Code Name, Authorization Level)

1234,John Smith,20

1235,Lisa Mendez,10

5551,Debbie Dunn,30

Deleting information from a file and leaving the information blank does not remove the information from the database; in other words, a blank value does not overwrite an existing value in the database. Updating the values overwrites
                                    the existing value in the database.

Make sure that you upload the appropriate CSV files to the first node of the server.

Any time that you create or change a CSV file, you must insert the CSV file in BAT to update the database.

## Implement CMC and FAC Features

You can use Bulk Administration (BAT) to implement CMC and FAC features.

The CMC and FAC features require that you make changes to
                                          			 route patterns and update your dial plan documents to reflect that you enabled
                                          			 or disabled FAC and/or CMC for each route pattern.

Review important BAT information and general information about the
                                       			 CMC and FAC features.

CMC and FAC Setup Using BAT

Feature Configuration Guide for Cisco Unified Communications Manager

Create a CSV file for CMC or FAC and enter the CMC and FAC
                                       			 configuration information.

To update the database, insert the CSV file in BAT.

Enable FAC or CMC by adding or updating route patterns in Administration.

Update your dial plan documents or keep a printout of the BAT CSV
                                       			 file with your dial plan documents.

Refer to your dial plan documents.

Provide all necessary information, for example, codes, to users
                                       			 and explain how the features work.

## Create CMC and FAC CSV Data File Using BAT.xlt

You can create the CSV file for CMC or FAC using the BAT
                              		  spreadsheet BAT.xlt. You must create two separate CSV files, one for CMC and
                              		  one for FAC.

The BAT.xlt file exists on the first node of the server; however, you normally do not have Microsoft Excel installed on the server. In that case, copy the file from the first
                                          node and move it to a local machine that has Microsoft Excel installed.

### Before you begin

Review important considerations in CMC and FAC Setup Using BAT before you use BAT to configure CMC or FAC.

Choose Bulk Administration > Upload/Download Files .

Click Find and download the BAT.xlt file.

Copy BAT.xlt to a local machine where Microsoft Excel is
                                       			 installed.

To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file.

When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities.

Click one of the following tabs:

Insert CMC—If you are creating a CMC CSV file

Insert FAC—If you are creating a FAC CSV file

Enter CMC or FAC settings in the columns.

Repeat Step 7 until you enter all codes.

To transfer the Excel spreadsheet format to a CSV file, click Export to BAT Format .

The system automatically saves CSV files to C:\XlsDatafiles on the local machine.

Click Browse to choose a different location.

### What to do next

Upload the CSV files to the first node of the server.

You must add the CSV file to BAT and insert the file to update the database.

## CSV Data File Creation for Client Matter Codes and Forced Authorization Codes Using Text Editor

You can use a text editor to create the text-based CSV data
                              		  file for client matter codes and forced authorization codes. The comma
                              		  separated values (CSV) file provides textual information in tabular form and
                              		  contains lines of ASCII text with values separated by commas.

## Edit Existing CMC or FAC CSV Data File

You update existing codes by manually updating an existing
                              		  CSV file or creating a new CSV file using a text editor.

If you are updating a CMC CSV file, for example, you may enter
                              		  5555,Acme Toys, where 5555 equals the mandatory client matter code, and Acme
                              		  Toys equals the description.

If you are updating a FAC CSV file, for example, you may enter
                              		  1234,John Smith,20, where 1234 equals the forced authorization code, John Smith
                              		  equals the authorization code name, and 20 equals the authorization level.

You can change any part of an existing record, but you must include
                              		  the code; for example, the forced authorization code or client matter code.
                              		  Deleting information and leaving it blank does not remove the information from
                              		  the database; a blank value does not overwrite an existing value in the
                              		  database, but, updating the value, for example, to Acme Toys, Inc. or John L.
                              		  Smith from the preceding examples, overwrites the existing value in the
                              		  database.

To edit existing CSV data files, download the CSV files from the
                                       			 first node of the Cisco Unified Communications Manager server to your local workstation.

Open and edit the existing CSV file using a text editor.

Delete existing settings, add new codes, or update existing
                                          				settings. See Table 1 for descriptions of the CMC and FAC configuration settings.

If you add new codes at the same time that you update them, make
                                                      				  sure that you enter all required information.

A blank value does not overwrite an existing value in the
                                                      				  database, but updating the value overwrites the existing value in the database.

### What to do next

Upload the CSV files to the first node of the Cisco Unified Communications Manager server.

You must add the CSV file to BAT and insert the file to update the Cisco Unified Communications Manager database.

## CMC and FAC CSV Data File Settings

The following table provides descriptions of the
                              		  configuration settings in the CMC and FAC CSV data files.

Setting/Column

Description

For CMC CSV file

Client Matter Code

Enter a unique code of no more than 16 digits that the user
                                          					 will enter when placing a call. The client matter code displays in the CDRs for
                                          					 calls that use this code.

Description

This optional field helps you associate a client code with a
                                          					 client. The description can include up to 50 characters in any language, but it
                                          					 cannot include double-quotes ( " ), percentage sign
                                          					 ( % ), ampersand ( & ), back-slash
                                          					 ( \ ), or angle brackets (<>).

For FAC CSV File

Authorization Code

Enter a unique authorization code that is no more than 16
                                          					 digits. The user enters this code when the user places a call through a
                                          					 FAC-enabled route pattern.

Authorization Code Name

Enter a unique name that is no more than 50 characters. The
                                          					 authorization code name ties the authorization code to a specific user or group
                                          					 of users; this name displays in the CDRs for calls that use this code.

Authorization Level

Enter a three-digit authorization level that exists within the
                                          					 range of 0 to 255; the default equals 0. The level that you assign to the
                                          					 authorization code determines whether the user can route calls through
                                          					 FAC-enabled route patterns. To successfully route a call, the user
                                          					 authorization level must equal or be greater than the authorization level that
                                          					 is specified for the route pattern for the call.

## Update CMC or FAC in CUCM Database Using BAT

To update the Cisco Unified Communications Manager database, you must insert the CMC or FAC CSV
                              		  data file using BAT.

### Before you begin

Before you can update Cisco Unified Communications Manager , you must create or edit a CMC or FAC CSV
                              		  file.

In Cisco Unified Communications Manager Administration, choose one of the following
                                       			 options:

For CMC, choose Bulk
                                                   						Administration > Client Matter
                                                   						Codes > Insert Client Matter
                                                   						Codes .

For FAC, choose Bulk
                                                   						Administration > Forced Authorization
                                                   						Codes > Insert Forced Authorization
                                                   						Codes .

In the File Name drop-down list box, choose the CSV
                                       			 file that contains the updated codes.

To view the contents of the file that you want to insert, click View File .

If you are updating an existing list of codes, check the Override the existing configuration check box.

See BAT Settings to Update CMC and FAC in the Database for configuration details.

In the Job Information area, enter the Job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert FAC and CMC
                                             				  immediately.

Click Run Later to insert FAC and CMC at a later
                                             				  time.

To create a job for inserting FAC and CMC, click Submit .

## BAT Settings to Update CMC and FAC in the Database

Setting in BAT

Description

File Name

From the drop-down list box, choose the CMC or FAC file that
                                             					 you want to insert.

Override the existing configuration

This check box applies if you are updating code for existing
                                             					 settings.

Checking this check box overwrites the existing authorization
                                             					 code name (FAC), authorization level (FAC), or description (CMC) with the
                                             					 information that is contained in the file that you want to insert (existing
                                             					 authorization and client matter codes do not change). If you do not check the
                                             					 check box, an error, which writes to the log file, indicates that the
                                             					 authorization or client matter code already exists; therefore, no updates
                                             					 occur.

## Topics Related to CMC and FAC Configuration

| Note | The CMC and FAC features require that you make changes to
                                          			 route patterns and update your dial plan documents to reflect that you enabled
                                          			 or disabled FAC and/or CMC for each route pattern. |
|---|---|

| Step 1 | Review important BAT information and general information about the
                                       			 CMC and FAC features. CMC and FAC Setup Using BAT Feature Configuration Guide for Cisco Unified Communications Manager |
|---|---|
| Step 2 | Create a CSV file for CMC or FAC and enter the CMC and FAC
                                       			 configuration information. |
| Step 3 | To update the database, insert the CSV file in BAT. |
| Step 4 | Enable FAC or CMC by adding or updating route patterns in Administration. |
| Step 5 | Update your dial plan documents or keep a printout of the BAT CSV
                                       			 file with your dial plan documents. Refer to your dial plan documents. |
| Step 6 | Provide all necessary information, for example, codes, to users
                                       			 and explain how the features work. |

| Note | The BAT.xlt file exists on the first node of the server; however, you normally do not have Microsoft Excel installed on the server. In that case, copy the file from the first
                                          node and move it to a local machine that has Microsoft Excel installed. |
|---|---|

| Step 1 | Choose Bulk Administration > Upload/Download Files . The Find and List Files window opens. |
|---|---|
| Step 2 | Click Find and download the BAT.xlt file. |
| Step 3 | Copy BAT.xlt to a local machine where Microsoft Excel is
                                       			 installed. |
| Step 4 | To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file. |
| Step 5 | When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities. |
| Step 6 | Click one of the following tabs: Insert CMC—If you are creating a CMC CSV file Insert FAC—If you are creating a FAC CSV file |
| Step 7 | Enter CMC or FAC settings in the columns. See Table 1 for descriptions of configuration settings. Note Repeat Step 7 until you enter all codes. | Note | Repeat Step 7 until you enter all codes. |
| Note | Repeat Step 7 until you enter all codes. |
| Step 8 | To transfer the Excel spreadsheet format to a CSV file, click Export to BAT Format . The system automatically saves CSV files to C:\XlsDatafiles on the local machine. Tip Click Browse to choose a different location. | Tip | Click Browse to choose a different location. |
| Tip | Click Browse to choose a different location. |

| Note | Repeat Step 7 until you enter all codes. |
|---|---|

| Tip | Click Browse to choose a different location. |
|---|---|

| Step 1 | To edit existing CSV data files, download the CSV files from the
                                       			 first node of the Cisco Unified Communications Manager server to your local workstation. |
|---|---|
| Step 2 | Open and edit the existing CSV file using a text editor. Delete existing settings, add new codes, or update existing
                                          				settings. See Table 1 for descriptions of the CMC and FAC configuration settings. Caution If you add new codes at the same time that you update them, make
                                                      				  sure that you enter all required information. A blank value does not overwrite an existing value in the
                                                      				  database, but updating the value overwrites the existing value in the database. | Caution | If you add new codes at the same time that you update them, make
                                                      				  sure that you enter all required information. A blank value does not overwrite an existing value in the
                                                      				  database, but updating the value overwrites the existing value in the database. |
| Caution | If you add new codes at the same time that you update them, make
                                                      				  sure that you enter all required information. A blank value does not overwrite an existing value in the
                                                      				  database, but updating the value overwrites the existing value in the database. |

| Caution | If you add new codes at the same time that you update them, make
                                                      				  sure that you enter all required information. A blank value does not overwrite an existing value in the
                                                      				  database, but updating the value overwrites the existing value in the database. |
|---|---|

| Setting/Column | Description |
|---|---|
| For CMC CSV file |
| Client Matter Code | Enter a unique code of no more than 16 digits that the user
                                          					 will enter when placing a call. The client matter code displays in the CDRs for
                                          					 calls that use this code. |
| Description | This optional field helps you associate a client code with a
                                          					 client. The description can include up to 50 characters in any language, but it
                                          					 cannot include double-quotes ( " ), percentage sign
                                          					 ( % ), ampersand ( & ), back-slash
                                          					 ( \ ), or angle brackets (<>). |
| For FAC CSV File |
| Authorization Code | Enter a unique authorization code that is no more than 16
                                          					 digits. The user enters this code when the user places a call through a
                                          					 FAC-enabled route pattern. |
| Authorization Code Name | Enter a unique name that is no more than 50 characters. The
                                          					 authorization code name ties the authorization code to a specific user or group
                                          					 of users; this name displays in the CDRs for calls that use this code. Tip If you plan to assign an authorization code to
                                                   					 every user in the system, make sure that the code name includes an identifier
                                                   					 for the user, such as the user name or another unique, non-sensitive
                                                   					 identifier; for example, an email alias or employee/student number. Do not use
                                                   					 identifiers such as a social security number because the authorization code
                                                   					 name writes to CDRs, which are not secure. | Tip | If you plan to assign an authorization code to
                                                   					 every user in the system, make sure that the code name includes an identifier
                                                   					 for the user, such as the user name or another unique, non-sensitive
                                                   					 identifier; for example, an email alias or employee/student number. Do not use
                                                   					 identifiers such as a social security number because the authorization code
                                                   					 name writes to CDRs, which are not secure. |
| Tip | If you plan to assign an authorization code to
                                                   					 every user in the system, make sure that the code name includes an identifier
                                                   					 for the user, such as the user name or another unique, non-sensitive
                                                   					 identifier; for example, an email alias or employee/student number. Do not use
                                                   					 identifiers such as a social security number because the authorization code
                                                   					 name writes to CDRs, which are not secure. |
| Authorization Level | Enter a three-digit authorization level that exists within the
                                          					 range of 0 to 255; the default equals 0. The level that you assign to the
                                          					 authorization code determines whether the user can route calls through
                                          					 FAC-enabled route patterns. To successfully route a call, the user
                                          					 authorization level must equal or be greater than the authorization level that
                                          					 is specified for the route pattern for the call. |

| Tip | If you plan to assign an authorization code to
                                                   					 every user in the system, make sure that the code name includes an identifier
                                                   					 for the user, such as the user name or another unique, non-sensitive
                                                   					 identifier; for example, an email alias or employee/student number. Do not use
                                                   					 identifiers such as a social security number because the authorization code
                                                   					 name writes to CDRs, which are not secure. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, choose one of the following
                                       			 options: For CMC, choose Bulk
                                                   						Administration > Client Matter
                                                   						Codes > Insert Client Matter
                                                   						Codes . For FAC, choose Bulk
                                                   						Administration > Forced Authorization
                                                   						Codes > Insert Forced Authorization
                                                   						Codes . |
|---|---|
| Step 2 | In the File Name drop-down list box, choose the CSV
                                       			 file that contains the updated codes. Tip To view the contents of the file that you want to insert, click View File . | Tip | To view the contents of the file that you want to insert, click View File . |
| Tip | To view the contents of the file that you want to insert, click View File . |
| Step 3 | If you are updating an existing list of codes, check the Override the existing configuration check box. See BAT Settings to Update CMC and FAC in the Database for configuration details. |
| Step 4 | In the Job Information area, enter the Job description. |
| Step 5 | Choose an insert method. Do one of the following: Click Run Immediately to insert FAC and CMC
                                             				  immediately. Click Run Later to insert FAC and CMC at a later
                                             				  time. |
| Step 6 | To create a job for inserting FAC and CMC, click Submit . Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                       			 activate this job. |

| Tip | To view the contents of the file that you want to insert, click View File . |
|---|---|

| Setting in BAT | Description |
|---|---|
| File Name | From the drop-down list box, choose the CMC or FAC file that
                                             					 you want to insert. |
| Override the existing configuration | This check box applies if you are updating code for existing
                                             					 settings. Checking this check box overwrites the existing authorization
                                             					 code name (FAC), authorization level (FAC), or description (CMC) with the
                                             					 information that is contained in the file that you want to insert (existing
                                             					 authorization and client matter codes do not change). If you do not check the
                                             					 check box, an error, which writes to the log file, indicates that the
                                             					 authorization or client matter code already exists; therefore, no updates
                                             					 occur. |