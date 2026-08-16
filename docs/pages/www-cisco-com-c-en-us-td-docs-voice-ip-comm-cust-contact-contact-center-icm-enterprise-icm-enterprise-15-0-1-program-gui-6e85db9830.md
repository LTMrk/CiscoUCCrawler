---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-6e85db9830
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_bulk-job-api_1501.html
retrieved_at: 2026-08-16T20:15:06.319637+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Bulk Job API

## Chapter: Bulk Job API

- Bulk Job API

- Bulk Job API

# Bulk Job API

## Bulk Job API

Use the Bulk Job API to list the bulk jobs currently defined in the database, define new bulk jobs, and view or delete records
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

get (template): Returns a sample CSV template for the given bulk job type. The response contains the CSV template as a file attachment. The
                                       form of the request is https://<server>/unifiedconfig/config/bulkjob/templates/<jobType> , where <jobType> can be one of the following:

dialednumber

agent

calltype

skillgroup

inventory (for lab mode inventory)

CVP file transfer

ssomigration:

Returns the Cisco IdS ssomigration CSV template as a file attachment. The template includes the first 12,000 agent and supervisor
                                          accounts that are not enabled for Cisco IdS SSO.

If the database contains more than 12,000 non-SSO users, get the first 12,000 and update their credentials for Cisco IdS SSO.
                                          Then get the next 12,000 users and update their credentials for Cisco IdS SSO. Repeat until there are no more agents to migrate.

Non-SSO users can be filtered by peripheralId, agentTeamId, or both.

To filter by peripheralId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=peripheralId:<peripheralId> .

To filter by agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=agentTeamId:<agentTeamId> .

To filter by both peripheralId and agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ ssomigration?q=peripheralId:<peripheralId>agentTeamId:<agentTeamId> .

aiFeatures_association

The sample CSV template returns the list of agents and the associated Contact Center AI feature types.

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

description

description

jobType

jobState

jobHostName

createDateTime

startDateTime

endDateTime

See Search and Sort .

### Example Create Request

For more information about the list of available AI features, see the Contact Center AI Features topic in this guide.

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