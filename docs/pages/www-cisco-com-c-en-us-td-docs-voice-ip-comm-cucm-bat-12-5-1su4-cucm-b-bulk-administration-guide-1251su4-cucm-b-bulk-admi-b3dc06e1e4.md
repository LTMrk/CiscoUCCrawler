---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-b3dc06e1e4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_01010000.html
retrieved_at: 2026-08-21T17:55:01.664332+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Manage Directory
	 URIs and Patterns

## Chapter: Manage Directory
	 URIs and Patterns

# Manage Directory
                     	 URIs and Patterns

This chapter
                        		describes how to import and export directory URIs, +E.164 patterns and PSTN
                        		failover rules to and from Cisco Unified Communications Manager.

## Export Local Directory URIs and +E.164 Patterns

This procedure describes how to export all locally configured directory URIs, +E.164 number patterns, and their associated
                              PSTN failover rules, to a CSV file that you can import into the other call control system.

Cisco Unified Communications Manager writes to the CSV file only those directory URIs and +E.164 number patterns that were configured in the local cluster. Cisco Unified Communications Manager includes directory URIs and +E.164 patterns that were imported from an LDAP directory into the local cluster, but does not
                                          include directory URIs or patterns that were learned via ILS or that were   imported from a third party URI catalog.

In Cisco Unified CM Administration, choose Bulk Administration > Directory URIs and Patterns > Export Local Directory URIs and Patterns .

Click one of the following radio buttons to define the domain name that you want to attach to the export file:

- Organizational Top Level Domain—Click this radio button to use the value of the Organizational Top Level Domain enterprise
                                          parameter for the export file domain name.

- Route String Domain—Click this radio button to use the value of the Route String field, as configured in ILS Configuration,
                                          for the export file domain name.

- User Defined Domain—Click this radio button to create a customized domain name to attach to the export file.

If you chose a User Defined Domain, enter the domain name in the Domain Name text box.

Click the Export Local Directory URIs and Patterns button.

Save the CSV file to a local drive.

## Import Directory
                        	 URIs and Patterns From a Non-ILS System

Follow this
                              		  procedure if you are running the Intercluster Lookup Service (ILS) on your
                              		  local cluster and you want to import a global dial plan catalog, including
                              		  directory URIs, +E.164 number patterns, or PSTN failover rules from a CSV file
                              		  for a call control system that is not running ILS, such as a Cisco TelePresence
                              		  Video Communication Server (VCS) or a third-party call control system.

To perform this
                              		  procedure, the Cisco Bulk Provisioning Service must be running on the local
                              		  cluster, which must be configured as a hub cluster in an ILS network. After you
                              		  import the catalog into Cisco
                                 			 Unified Communications Manager , ILS replicates the imported catalog
                              		  to the other clusters in the ILS network.

Make sure that
                                          			 the CSV file that you use for the import is compatible with your version of Cisco
                                             				Unified Communications Manager . For example, a CSV file that is
                                          			 compatible to import into Version 9.0(1) is not compatible with Version
                                          			 10.0(1). To view a sample CSV file for your release, in Cisco Unified CM
                                          			 Administration, choose Bulk
                                                				  Administration > Directory URIs and Patterns > Insert Directory URIs and
                                                				  Patterns and click View
                                             				Sample File .

Within Cisco
                                          			 Unified CM Administration, you can enter directory URIs with embedded double
                                          			 quotation marks or commas. However, when you use Bulk Administration to import
                                          			 a CSV file that contains directory URIs with embedded double quotation marks
                                          			 and commas, you must enclose the entire directory URI in double quotation marks
                                          			 and escape the embedded double quotation marks with a double quotation mark.
                                          			 For example, a directory URI of Jared, "Jerry" ,Smith@test.com must be input as "Jared" , " "Jerry" " , "Smith@test.com" in the CSV file.

In Cisco
                                       			 Unified CM Administration, choose Call
                                             				  Routing > Global Dial Plan Replication > Imported Global Dial Plan
                                             				  Catalogs .

In the Name field, enter a name for the catalog.

In the Description field, enter a description of the
                                       			 catalog.

In the Route String field, create a route string for
                                       			 the system from which you are importing the catalog.

Click Save .

In Cisco
                                       			 Unified CM Administration, choose Bulk
                                             				  Administration > Upload/Download Files .

Click Add
                                          				New .

Click Browse and select the CSV file for the catalog that
                                       			 you want to import.

In the Select the Target drop-down list box, choose Imported Directory URIs and Patterns .

In the Select Transaction Type drop-down list box,
                                       			 choose Insert
                                          				Imported Directory URIs and Patterns .

Click Save .

In Cisco
                                       			 Unified CM Administration, choose Bulk
                                             				  Administration > Directory URIs and Patterns > Insert Imported Directory
                                             				  URIs and Patterns .

In the File Name drop-down list box, choose the CSV
                                       			 file that contains the catalog that you want to import.

In the Imported Directory URI Catalog drop-down list
                                       			 box, choose the catalog that you named in the Imported Global Dial Plan Catalog
                                       			 window.

In the Job Description text box, enter a name for the
                                       			 job that you are about to run.

Select when
                                       			 you want to run the job.

- If you want to run the job
                                          				now, click the Run
                                             				  Immediately radio button, and click Submit.

- If you want to schedule the
                                          				job to run at a specified time, check the Run
                                             				  Later radio button and click Submit . If you choose this option, you must use the
                                          				Bulk Administration Job Scheduler to schedule when the job runs.

## Directory URI Format

Directory URIs are alphanumeric strings consisting of a user and a host address separated by the @ symbol. Cisco Unified Communications
                              Manager supports the following formats for directory URIs:

user@domain (for example, joe@cisco.com)

user@ip_address (for example, joe@10.10.10.1)

Cisco Unified Communications Manager supports the following formats in the user portion of a directory URI (the portion before
                              the @ symbol):

Accepted characters are a-z, A-Z, 0-9, !, $, %, &, *,  _, +, ~,  -, =,  \,  ?, \, ‘, ,, ., /.

The user portion has a maximum length of 47 characters.

The user portion accepts percent encoding from %2[0-9A-F] through %7[0-9A-F]. For some accepted characters, Unified CM automatically
                                    applies percent encoding. See below for more information on percent encoding.

The user portion is case-sensitive or case-insensitive depending on the value of the URI Lookup Policy enterprise parameter.
                                    The default value is case-sensitive.

Cisco Unified Communications Manager supports the following formats in the host portion of a directory URI (the portion after
                              the @ symbol):

Supports IPv4 addresses or fully qualified domain names.

Accepted characters are a-z, A-Z ,0-9, hyphens, and dots.

The host portion cannot start or end with a hyphen.

The host portion cannot have two dots in a row.

Minimum of two characters.

The host portion is not case sensitive.

Due to database restrictions, the Directory URI field has a maximum length of 254 characters.

You can also enter a directory number in the user portion of a directory URI. However, Cisco Unified Communications Manager
                                          may treat the directory URI as a directory number depending on which Dial String Interpretation option you choose for the
                                          SIP Profile.

For compatibility with third party call control systems, Cisco recommends setting the value of the URI Lookup Policy enterprise
                                          parameter to case insensitive.

### Percent Encoding of Directory URIs

In the user portion of a directory URI, Unified CM automatically applies percent encoding to the following characters when
                              the directory URI is saved in the database:

# % ^ ` { } | \ : ” < > [ ] \ ‘ and spaces

When percent encoding is applied, the digit length of the directory URI increases. For example, if you input joe smith#@cisco.com
                              (20 characters) as a directory URI, Cisco Unified Communications Manager stores the directory URI in the database as joe%20smith%23@cisco.com
                              (24 characters). Due to database restrictions, Cisco Unified Communications Manager rejects any attempt to save a directory
                              URI of greater than 254 characters.

### Directory URI Format Exception for Bulk Administration

Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                              you use Bulk Administration to import a CSV file that contains directory URIs with embedded double quotes and commas, you
                              must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                              example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file.

| Note | Cisco Unified Communications Manager writes to the CSV file only those directory URIs and +E.164 number patterns that were configured in the local cluster. Cisco Unified Communications Manager includes directory URIs and +E.164 patterns that were imported from an LDAP directory into the local cluster, but does not
                                          include directory URIs or patterns that were learned via ILS or that were   imported from a third party URI catalog. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Bulk Administration > Directory URIs and Patterns > Export Local Directory URIs and Patterns . |
|---|---|
| Step 2 | Click one of the following radio buttons to define the domain name that you want to attach to the export file: Organizational Top Level Domain—Click this radio button to use the value of the Organizational Top Level Domain enterprise
                                          parameter for the export file domain name. Route String Domain—Click this radio button to use the value of the Route String field, as configured in ILS Configuration,
                                          for the export file domain name. User Defined Domain—Click this radio button to create a customized domain name to attach to the export file. |
| Step 3 | If you chose a User Defined Domain, enter the domain name in the Domain Name text box. |
| Step 4 | Click the Export Local Directory URIs and Patterns button. |
| Step 5 | Save the CSV file to a local drive. |

| Note | Make sure that
                                          			 the CSV file that you use for the import is compatible with your version of Cisco
                                             				Unified Communications Manager . For example, a CSV file that is
                                          			 compatible to import into Version 9.0(1) is not compatible with Version
                                          			 10.0(1). To view a sample CSV file for your release, in Cisco Unified CM
                                          			 Administration, choose Bulk
                                                				  Administration > Directory URIs and Patterns > Insert Directory URIs and
                                                				  Patterns and click View
                                             				Sample File . |
|---|---|

| Note | Within Cisco
                                          			 Unified CM Administration, you can enter directory URIs with embedded double
                                          			 quotation marks or commas. However, when you use Bulk Administration to import
                                          			 a CSV file that contains directory URIs with embedded double quotation marks
                                          			 and commas, you must enclose the entire directory URI in double quotation marks
                                          			 and escape the embedded double quotation marks with a double quotation mark.
                                          			 For example, a directory URI of Jared, "Jerry" ,Smith@test.com must be input as "Jared" , " "Jerry" " , "Smith@test.com" in the CSV file. |
|---|---|

| Step 1 | In Cisco
                                       			 Unified CM Administration, choose Call
                                             				  Routing > Global Dial Plan Replication > Imported Global Dial Plan
                                             				  Catalogs . |
|---|---|
| Step 2 | In the Name field, enter a name for the catalog. |
| Step 3 | In the Description field, enter a description of the
                                       			 catalog. |
| Step 4 | In the Route String field, create a route string for
                                       			 the system from which you are importing the catalog. |
| Step 5 | Click Save . |
| Step 6 | In Cisco
                                       			 Unified CM Administration, choose Bulk
                                             				  Administration > Upload/Download Files . |
| Step 7 | Click Add
                                          				New . |
| Step 8 | Click Browse and select the CSV file for the catalog that
                                       			 you want to import. |
| Step 9 | In the Select the Target drop-down list box, choose Imported Directory URIs and Patterns . |
| Step 10 | In the Select Transaction Type drop-down list box,
                                       			 choose Insert
                                          				Imported Directory URIs and Patterns . |
| Step 11 | Click Save . |
| Step 12 | In Cisco
                                       			 Unified CM Administration, choose Bulk
                                             				  Administration > Directory URIs and Patterns > Insert Imported Directory
                                             				  URIs and Patterns . |
| Step 13 | In the File Name drop-down list box, choose the CSV
                                       			 file that contains the catalog that you want to import. |
| Step 14 | In the Imported Directory URI Catalog drop-down list
                                       			 box, choose the catalog that you named in the Imported Global Dial Plan Catalog
                                       			 window. |
| Step 15 | In the Job Description text box, enter a name for the
                                       			 job that you are about to run. |
| Step 16 | Select when
                                       			 you want to run the job. If you want to run the job
                                          				now, click the Run
                                             				  Immediately radio button, and click Submit. If you want to schedule the
                                          				job to run at a specified time, check the Run
                                             				  Later radio button and click Submit . If you choose this option, you must use the
                                          				Bulk Administration Job Scheduler to schedule when the job runs. Note Cisco
                                                   				Unified Communications Manager saves all imported +E.164 patterns to the Global
                                                   				Learned +E.164 Patterns partition. | Note | Cisco
                                                   				Unified Communications Manager saves all imported +E.164 patterns to the Global
                                                   				Learned +E.164 Patterns partition. |
| Note | Cisco
                                                   				Unified Communications Manager saves all imported +E.164 patterns to the Global
                                                   				Learned +E.164 Patterns partition. |

| Note | Cisco
                                                   				Unified Communications Manager saves all imported +E.164 patterns to the Global
                                                   				Learned +E.164 Patterns partition. |
|---|---|

| Note | You can also enter a directory number in the user portion of a directory URI. However, Cisco Unified Communications Manager
                                          may treat the directory URI as a directory number depending on which Dial String Interpretation option you choose for the
                                          SIP Profile. |
|---|---|

| Note | For compatibility with third party call control systems, Cisco recommends setting the value of the URI Lookup Policy enterprise
                                          parameter to case insensitive. |
|---|---|