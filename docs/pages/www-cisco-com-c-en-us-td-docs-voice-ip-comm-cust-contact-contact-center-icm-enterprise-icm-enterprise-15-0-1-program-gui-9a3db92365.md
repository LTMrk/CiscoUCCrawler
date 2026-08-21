---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-9a3db92365
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_bulk-job-api_1501.html
retrieved_at: 2026-08-21T16:45:29.242888+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Bulk Job API

## Chapter: Bulk Job API

- Bulk Job API

- Bulk Job                              	 API

# Bulk Job API

## Bulk Job
                        	 API

Bulk jobs are a fast
                           		and efficient way to enter data at initial setup and to incorporate large-scale
                           		changes, such as changing agent skill groups between shifts and hiring multiple
                           		new agents.

You can use the Bulk
                           		Job API to list the bulk jobs currently defined in the database, define new
                           		bulk jobs, and view or delete records of existing bulk jobs.

Avoid performing a bulk job transaction during a maintainence window.

Limit the bulk job import to 1000 records at any given instance.

### URL

### Operations

create :
                                    				Creates one bulk job.

delete :
                                    				Permanently deletes one bulk job.

get : Returns one bulk job using the URL https://<server>/unifiedconfig/config/bulkjob/<id> .

dialednumber

agent

calltype

skillgroup

inventory (for lab mode inventory)

CVP file transfer

ssomigration

This template returns records for agent and supervisor accounts that are not enabled for single sign-on. You can use the template
                                          to migrate these user accounts to SSO.

Non-SSO users can be filtered by peripheralId, agentTeamId, or both.

To filter by peripheralId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=peripheralId:<peripheralId> .

To filter by agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ssomigration?q=agentTeamId:<agentTeamId> .

To filter by both peripheralId and agentTeamId, use the following URL:

https://<server>/unifiedconfig/config/bulkjob/templates/ ssomigration?q=peripheralId:<peripheralId>agentTeamId:<agentTeamId> .

Migration of Webex Common Identity users

Returns the Webex Common Identity Migration Content template as a CSV file attachment. The template includes the first 10,000
                                          agent and supervisor accounts that are not enabled for SSO Webex Common Identity.

If the database contains more than 10,000 non-Common Identity users, get the first 10,000 and update their credentials for
                                          SSO Webex Common Identity. Then get the next 10,000 users and update their credentials for SSO Webex Common Identity. Repeat
                                          until there are no more agents to migrate.

The Webex Common Identity Migration Content file must contain only two columns with headers loginName and ciUserLoginName.
                                          This file provides mapping of the current CCE users to the Webex Common Identity users.

LoginName represents the CCE users

ciUserLoginName represents the Webex Common Identity users to which we need to map the CCE users.

Consider the following criterias to validate and process the template file:

If loginName and ciUserLoginName are same

Updates firstName, lastName, loginName (with ciUserLoginName) and WebexCiUUID fetched from Common Identity API response.

If loginName and ciUserLoginName are different

If a Person record with ciUserLoginName doesn't exist in CCE, proceed with updating firstName, lastName, loginName (with ciUserLoginName)
                                                and WebexCiUUID fetched from Common Identity API response.

If a Person record with ciUserLoginName exist in CCE and WebexCiUUID is null, skip the record and add valid reason to bulkJob
                                                log stating duplicate record found with ciUserLoginName.

If a Person record with ciUserLoginName exists in CCE

If an agent is associated to the person record, skip the record and add valid reason to bulkJob log stating another agent
                                                      is associated with proposed ciUserLoginName.

If an agent is not associated to the person record, do permanent delete of that Person record and update the existing one
                                                      with firstName, lastName, loginName (with ciUserLoginName) and WebexCiUUID fetched from Common Identity API response.

aiFeature_association

The sample CSV template returns the list of agents and the associated feature types.

list :
                                    				Retrieves a list of bulk jobs.

### Parameters

refURL: The
                                    				refURL of the bulk job. See Shared Parameters .

description:
                                    				See Shared Parameters .

fileContent: The content of the bulk CSV file. The size of the file must not exceed 3MB. For information about the CSV file
                                    data, see the Manage Bulk Jobs section of the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

createDateTime: The time the bulk job was submitted. It
                                    				indicates the time in milliseconds elapsed from the zero epoch value of January
                                    				1, 1970, 00:00:00 GMT. Read-only.

jobHostName:
                                    				The Windows computer name of the AW that initiated the bulk job.
                                    				Read-only.

startDateTime: The time the bulk job began. Read-only.

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

jobType: The
                                    				job type. 
                                    			  Optional.  If this parameter is not provided, the value is determined automatically based on the header in the bulk job
                                    file. If the parameter is provided, the header must match the job type specified.

1: Dialed
                                          					 Number

2: Agent

3: Call
                                          					 Type

4: Skill
                                          					 Group

5: SSO Migration

5: SSO Migration

6: IVR Applications

9: Webex Common Identity Migration

102: Inventory

104: Contact Center AI feature association

You can create a bulk job and update the existing agent to enable or disable Contact Center AI features, using the aiFeature_association jobType. This jobType is available for administrators only when Cloud Connect is added in the inventory.

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

Example create request for enabling Transcript, VAVTranscript, VATransferSummaries, CallDropSummaries, WrapUpSummaries, and
                              RealTimeAssist features for the agents:

```
<bulkJob>
    <description>b1</description>
    <fileContent>
        agentId,userName,aiFeatures
        1111,Agent1,Transcript;VAVTranscript;VATransferSummaries;CallDropSummaries;WrapUpSummaries;RealTimeAssist
        2222,Agent2,Transcript;VAVTranscript;VATransferSummaries;CallDropSummaries;WrapUpSummaries;RealTimeAssist
    </fileContent>
</bulkJob>
```

### Example Get
                              		  Response

Example response
                              		  for a dialed number create job that completed successfully:

```
<bulkJob>
  <changeStamp>0</changeStamp>
  <refURL>/unifiedconfig/config/bulkjob/(id)</refURL>
  <jobHostName>CCE-AW-1</jobHostName>
  <createDateTime>1330441858360</createDateTime>
  <startDateTime>1330441858361</startDateTime>
  <endDateTime>1330441858368</endDateTime>
  <jobState>3</jobState>
  <jobType>1</jobType>
  <description>dn create bulk job</description>
  <logFile><refURL>/unifiedconfig/config/bulkjob/(id)/log</refURL></logFile>
  <csvFile><refURL>/unifiedconfig/config/bulkjob/(id)/csv</refURL></csvFile>
</bulkJob>
```

| Note | Avoid performing a bulk job transaction during a maintainence window. |
|---|---|

| Note | Limit the bulk job import to 1000 records at any given instance. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| description | description jobType jobState jobHostName createDateTime startDateTime endDateTime |