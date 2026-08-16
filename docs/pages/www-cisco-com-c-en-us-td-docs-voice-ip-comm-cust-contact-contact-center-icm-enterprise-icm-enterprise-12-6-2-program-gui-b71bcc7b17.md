---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-b71bcc7b17
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_bulk_job_api-12_6_1.html
retrieved_at: 2026-08-16T20:19:44.866239+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Bulk Job API

## Chapter: Bulk Job API

- Bulk Job API

- Bulk Job API

# Bulk Job API

## Bulk Job API

U se the Bulk Job API to list the bulk jobs currently defined in the database, define new bulk jobs, and view or delete records
                           of existing bulk jobs.

Avoid performing a bulk job transaction during a maintenance window.

Limit the bulk job import to 1000 records at any given instance.

### URL

### Operations

create : Creates one bulk job.

You can update the existing agent and supervisor usernames to SSO usernames using the ssomigration jobType.

delete :
                                    				Permanently deletes one bulk job.

get :
                                    				Returns one bulk job using the URL https://<server>/unifiedconfig/config/bulkjob/<id> .

ssomigration

Returns the ssomigration CSV template as a file attachment. The template includes the first 12,000 agent and supervisor accounts
                                             that are not enabled for SSO.

If the database contains more than 12,000 non-SSO users, get the first 12,000 and update their credentials for SSO. Then get
                                             the next 12,000 users and update their credentials for SSO. Repeat until there are no more agents to migrate.

Non-SSO users can be filtered by peripheralId, agentTeamId, or both.

To filter by peripheralId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=peripheralId:<peripheralId> .

To filter by agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=agentTeamId:<agentTeamId> .

To filter by both peripheralId and agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ ssomigration?q=peripheralId:<peripheralId>agentTeamId:<agentTeamId> .

agentservice_association

The sample CSV template returns the list of agents and the associated Contact Center AI service types.

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

startDateTime: The time the bulk job began to run. Read-only.

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

The valid value is 5, for SSO Migration.

The valid value is 104, for Contact Center AI service association. You can create a bulk job and update the existing agent
                                    to enable or disable Contact Center AI services, using the agentservice_association jobType. This jobType is available for administrators only when Cloud Connect is added in the inventory.

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

### Example Create Request

Example create request for enabling Agent Answers service for the agents:

```
<bulkJob>
<jobType>104</jobType>
<fileContent>agentId,userName,agentServices
1111,Agent1,AgentAnswers
2222,Agent2,AgentAnswers
</fileContent>
</bulkJob>
```

Example create request for enabling Agent Answers and Transcript services for the agents:

```
<bulkJob>
<jobType>104</jobType>
<fileContent>agentId,userName,agentServices
1111,Agent1,AgentAnswers;Transcript
2222,Agent2,AgentAnswers;Transcript
</fileContent>
</bulkJob>
```

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