---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-97656e6c07
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_011110.html
retrieved_at: 2026-08-21T17:51:30.914281+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Manager and Assistant Insertions

## Chapter: Manager and Assistant Insertions

- Manager and Assistant Insertions

- Insert Manager-Assistant Associations to Cisco Unified Communications Manager

- Topics Related to Manager and Assistant Insertion

# Manager and Assistant Insertions

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to manage the Cisco Unified Communications Manager Assistant feature in Cisco Unified Communications Manager . BAT allows you to add IP phones for managers and assistants with either proxy lines or shared lines.

The Cisco Unified CM Assistant feature works with several
                        		Cisco Unified IP Phone models and device profiles. Cisco Unified CM Assistant
                        		provides two modes for configuring managers and assistants lines for use with
                        		Cisco Unified CM Assistant features.

Proxy mode—The manager primary line associates with a proxy line
                              			 that has a different directory number on the assistant phone. See the Set Up Phones in Proxy Line Mode for Cisco Unified Communications Manager Assistant .

Shared line mode—The manager and assistant have a shared line on
                              			 their phones that uses the same directory number and partition. See the Set Up Phones in Shared Line Mode for Cisco Unified Communications Manager Assistant .

## Insert Manager-Assistant Associations to Cisco Unified Communications Manager

To insert new manager-assistant associations or update
                              		  existing associations, you need a CSV data file.

When BAT updates manager-assistant associations, it does not
                              		  change existing Cisco Unified CM Assistant line configurations for the intercom
                              		  directory number or associated devices.

The manager-assistant association fails when the assistant phone
                                          			 does not have enough lines to support the minimum Cisco Unified CM Assistant
                                          			 configuration.

### Before you begin

- Set Up Phones in Proxy Line Mode for Cisco Unified Communications Manager Assistant

- Set Up Phones in Shared Line Mode for Cisco Unified Communications Manager Assistant

- You must have a data file
                                 			 in comma separated value (CSV) format that contains the unique details for the
                                 			 new manager-assistant associations.

Choose Bulk
                                             				  Administration > Managers/Assistants > Insert
                                             				  Managers/Assistants .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

If the managers use extension mobility to log in, check the Configure managers as mobile managers check
                                       			 box.

When all the phones have shared lines, check the Uses shared lines check box.

In the Insert Options area, choose the type of CSV
                                       			 data file that you created:

- Associate one or
                                                   						more assistants to a manager

- Associate one or
                                                   						more managers to an assistant

- Custom—If you created
                                             				  a custom CSV data file for proxy mode.

In the Job Information area, enter the Job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert the
                                             				  manager-assistant associations immediately.

Click Run Later to insert the manager-assistant
                                             				  associations at a later time.

To create a job for inserting the manager-assistant records, click Submit .

If there were not enough available lines when BAT performs an
                                                      				  update to an assistant or manager configuration, the changes are only partially
                                                      				  completed and the whole transaction record fails.

### What to do next

For changes to take effect, you must restart Cisco Unified CM
                              		  Assistant service.

## Topics Related to Manager and Assistant Insertion

| Caution | The manager-assistant association fails when the assistant phone
                                          			 does not have enough lines to support the minimum Cisco Unified CM Assistant
                                          			 configuration. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Managers/Assistants > Insert
                                             				  Managers/Assistants . The Manager/Assistant Options window displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | If the managers use extension mobility to log in, check the Configure managers as mobile managers check
                                       			 box. |
| Step 4 | When all the phones have shared lines, check the Uses shared lines check box. |
| Step 5 | In the Insert Options area, choose the type of CSV
                                       			 data file that you created: Default—If you created
                                             				  a standard CSV data file, choose the type of associations for this transaction
                                             				  based on the data in the CSV file. Associate one or
                                                   						more assistants to a manager Associate one or
                                                   						more managers to an assistant Custom—If you created
                                             				  a custom CSV data file for proxy mode. |
| Step 6 | In the Job Information area, enter the Job description. |
| Step 7 | Choose an insert method. Do one of the following: Click Run Immediately to insert the
                                             				  manager-assistant associations immediately. Click Run Later to insert the manager-assistant
                                             				  associations at a later time. |
| Step 8 | To create a job for inserting the manager-assistant records, click Submit . To schedule and activate this job, use the Job Scheduler option
                                       			 in the Bulk Administration main menu. Attention If there were not enough available lines when BAT performs an
                                                      				  update to an assistant or manager configuration, the changes are only partially
                                                      				  completed and the whole transaction record fails. | Attention | If there were not enough available lines when BAT performs an
                                                      				  update to an assistant or manager configuration, the changes are only partially
                                                      				  completed and the whole transaction record fails. |
| Attention | If there were not enough available lines when BAT performs an
                                                      				  update to an assistant or manager configuration, the changes are only partially
                                                      				  completed and the whole transaction record fails. |

| Attention | If there were not enough available lines when BAT performs an
                                                      				  update to an assistant or manager configuration, the changes are only partially
                                                      				  completed and the whole transaction record fails. |
|---|---|