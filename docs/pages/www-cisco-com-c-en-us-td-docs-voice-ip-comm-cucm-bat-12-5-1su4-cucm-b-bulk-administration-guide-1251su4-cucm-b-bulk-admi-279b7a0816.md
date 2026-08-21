---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-279b7a0816
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_01101.html
retrieved_at: 2026-08-21T17:50:20.259823+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Phone Migrations

## Chapter: Phone Migrations

- Phone Migrations

- Migrate Phone From SCCP to SIP

- Topics Related to Phone Migration

# Phone Migrations

Using Cisco Unified Communications Manager Bulk Administration (BAT), you can migrate a group of phones from Skinny Client Control Protocol (SCCP) to Session Initiation
                        Protocol (SIP).

## Migrate Phone From SCCP to SIP

You can migrate phones from SCCP to SIP. During the SCCP to
                              		  SIP migration, only SIP specific default values in the phone report get
                              		  migrated. Other values in the template are not migrated.

Migrating a phone that is running SCCP to SIP does not require a
                                          			 manual reset because the migration itself handles the reset of phones.

Choose Bulk
                                             				  Administration > Phones > Migrate
                                             				  Phones > SCCP to SIP .

From the first Find Phone where drop-down list box, choose
                                       			 one of the following criteria:

- Device Name

- Description

- Directory Number

- Calling Search Space

- Device Pool

- Device Type

- Call Pickup Group

- LSC Status

- Authentication String

- Location

- Phone Load Name

- Security Profile

From the second Find Phone where drop-down list box, choose
                                       			 one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Specify the appropriate search text, if applicable, then click Find .

To find all phones that are registered in the database, click Find without entering any search text.

- Device Name

- Description

- Device Pool

- Device Protocol

- Status

- IP Address

Click Next .

From the drop-down list box, choose the phone template.

SCCP to SIP migration will pick up only SIP specific default
                                                      				  values from this template during migration. It will not pick any other value
                                                      				  from the template.

In the Job Information area, enter the Job
                                       			 description.

Choose a migration method. Do one of the following:

Click Run Immediately to migrate phone records
                                             				  immediately.

Click Run Later to migrate phone records at a
                                             				  later time.

To create a job for migrating the phone records, click Submit .

### What to do next

After submitting a job for migrating phones from SCCP to SIP, make
                              		  sure that you reset these phones. Reset phones by using Bulk Administration > Phones > Reset/Restart
                                    				Phones > Query .

## Topics Related to Phone Migration

Migrate Phone From SCCP to SIP

Reset or Restart Phone Using Query

Manage Scheduled Jobs

| Note | Migrating a phone that is running SCCP to SIP does not require a
                                          			 manual reset because the migration itself handles the reset of phones. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Migrate
                                             				  Phones > SCCP to SIP . The Migrate Phones—SCCP to SIP window displays. |
|---|---|
| Step 2 | From the first Find Phone where drop-down list box, choose
                                       			 one of the following criteria: Device Name Description Directory Number Calling Search Space Device Pool Device Type Call Pickup Group LSC Status Authentication String Location Phone Load Name Security Profile |
| Step 3 | From the second Find Phone where drop-down list box, choose
                                       			 one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable, then click Find . To further define your query, check the check box corresponding
                                       			 to Search Within Results Using drop-down list
                                       			 box. You can choose AND or OR to add multiple filters. Repeat Step 2 through Step 4 . Tip To find all phones that are registered in the database, click Find without entering any search text. A list of discovered phones displays by: Device Name Description Device Pool Device Protocol Status IP Address | Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Step 5 | Click Next . |
| Step 6 | From the drop-down list box, choose the phone template. Note SCCP to SIP migration will pick up only SIP specific default
                                                      				  values from this template during migration. It will not pick any other value
                                                      				  from the template. | Note | SCCP to SIP migration will pick up only SIP specific default
                                                      				  values from this template during migration. It will not pick any other value
                                                      				  from the template. |
| Note | SCCP to SIP migration will pick up only SIP specific default
                                                      				  values from this template during migration. It will not pick any other value
                                                      				  from the template. |
| Step 7 | In the Job Information area, enter the Job
                                       			 description. |
| Step 8 | Choose a migration method. Do one of the following: Click Run Immediately to migrate phone records
                                             				  immediately. Click Run Later to migrate phone records at a
                                             				  later time. |
| Step 9 | To create a job for migrating the phone records, click Submit . To schedule and/or activate this job, use the Job Scheduler option in the Bulk Administration main menu. |

| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
|---|---|

| Note | SCCP to SIP migration will pick up only SIP specific default
                                                      				  values from this template during migration. It will not pick any other value
                                                      				  from the template. |
|---|---|