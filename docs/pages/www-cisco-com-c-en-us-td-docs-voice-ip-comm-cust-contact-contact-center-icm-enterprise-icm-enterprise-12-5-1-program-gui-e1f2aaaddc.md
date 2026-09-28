---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-e1f2aaaddc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_0111.html
retrieved_at: 2026-08-16T20:27:51.073808+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Bulk Job API

## Chapter: Bulk Job API

- Bulk Job API

- Bulk Job API

# Bulk Job API

## Bulk Job API

Bulk jobs are a fast and efficient way to update existing agent and supervisor usernames to SSO usernames.

You can use the Bulk Job API to return a CSV template with records for agents and supervisors who are not enabled for SSO. You can also u se the Bulk Job API to list the bulk jobs currently defined in the database, define new bulk jobs, and view or delete records
                           of existing bulk jobs.

Avoid performing a bulk job transaction during a maintenance window.

Limit the bulk job import to 1000 records at any given instance.

### URL

### Operations

create : Creates one bulk job.

delete :
                                    				Permanently deletes one bulk job.

get :
                                    				Returns one bulk job using the URL https://<server>/unifiedconfig/config/bulkjob/<id> .

ssomigration

Returns the ssomigration CSV template as a file attachment. The template includes the first 12,000 agent and supervisor accounts
                                             that are not enabled for SSO. The form of the request is https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration .

If the database contains more than 12,000 non-SSO users, get the first 12,000 and update their credentials for SSO. Then get
                                             the next 12,000 users and update their credentials for SSO. Repeat until there are no more agents to migrate.

Non-SSO users can be filtered by peripheralId, agentTeamId, or both.

To filter by peripheralId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=peripheralId:<peripheralId> .

To filter by agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=agentTeamId:<agentTeamId> .

To filter by both peripheralId and agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ ssomigration?q=peripheralId:<peripheralId>agentTeamId:<agentTeamId> .

list :
                                    				Retrieves a list of bulk jobs.

### Parameters

refURL: The
                                    				refURL of the bulk job. See Shared Parameters .

description:
                                    				See Shared Parameters .

fileContent: The content of the bulk CSV file. The size of the file must not exceed 3MB. For information about the CSV file data, see Manage Bulk Jobs section in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

createDateTime: The time the bulk job was submitted. It
                                    				indicates the time in milliseconds elapsed from the zero epoch value of January
                                    				1, 1970, 00:00:00 GMT. Read-only.

jobHostName:
                                    				The Windows computer name of the AW that initiated the bulk job.
                                    				Read-only.

startDateTime:
                                    				The time the bulk job began executing. Read-only.

endDateTime:
                                    				The time the bulk job completed or failed. Read-only.

jobState: The
                                    				current state of the job. Read-only.

1: Queued

2:
                                          					 Processing

3:
                                          					 Succeeded

4: Failed

5:
                                          					 Cancelled

6:
                                          					 Partially succeeded

jobType: The job type. Optional. If this parameter is not provided, the value is determined automatically based on the header
                                    in the bulk job file. If the parameter is provided, the header must match the job type specified.

The only valid value is 5, for SSO Migration.

description:
                                    				See Shared Parameters .

logFile: A URL
                                    				to download the log file for the bulk job. Read-only.

csvFile: A URL
                                    				to download the CSV file that was originally uploaded in the fileContent
                                    				parameter. Read-only.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- description

- description

- jobType

- jobState

- jobHostName

- createDateTime

- startDateTime

- endDateTime

See Search and Sort .

### Example Get
                              		  Response

Example response
                              		  for a SSO migration create job that completed successfully:

```
<bulkJob>
  <changeStamp>2</changeStamp>
  <refURL>/unifiedconfig/config/bulkjob/(id)</refURL>
  <jobHostName>CCE_AW</jobHostName>
  <createDateTime>1461785074000</createDateTime>
  <startDateTime>1461785074000</startDateTime>
  <endDateTime>1461785074000</endDateTime>
  <jobState>3</jobState>
  <jobType>5</jobType>
  <description>sso migration bulk job</description>
  <logFile>
				<refURL>/unifiedconfig/config/bulkjob/(id)/log</refURL>
		</logFile>
  <csvFile>
				<refURL>/unifiedconfig/config/bulkjob/(id)/csv</refURL>
		</csvFile>
</bulkJob>
```

| Note | Avoid performing a bulk job transaction during a maintenance window. |
|---|---|

| Note | Limit the bulk job import to 1000 records at any given instance. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| description | description jobType jobState jobHostName createDateTime startDateTime endDateTime |