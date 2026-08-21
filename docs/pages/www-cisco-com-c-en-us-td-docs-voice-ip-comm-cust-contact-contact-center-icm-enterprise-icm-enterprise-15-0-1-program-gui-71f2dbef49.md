---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-71f2dbef49
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_operation-api_1501.html
retrieved_at: 2026-08-21T16:47:34.257118+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Operation API

## Chapter: Operation API

- Operation API

- Operation                              	 API

# Operation API

## Operation
                        	 API

Use the Operation API to save changes to several items of the same type in a single request.  The following changes are allowed
                           in an operation:

delete:
                                 			 Multiple items of the same type. Any item that supports the delete operation
                                 			 can be deleted using the Operation API.

Agent update: Update multiple agents.

### URL

### HTTP
                              		  Method

Use HTTP POST to
                              		  submit a request to the Operation API.

### Parameters

operationType:
                                    				Indicates if the items specified in the refURLs should be updated or deleted.
                                    				Values are update/delete.

refURLs: A
                                    				collection of refURL parameters indicating which items are included in the
                                    				request. See Shared Parameters .

changeset: Includes the parameters that are changed in
                                    an update operation. See Agent Call API.

skillGroupsAdded

skillGroupsRemoved

attributesAdded

attributesRemoved

description

agentTeam

agentDeskSettings

agentServicesToEnable: Indicates the Contact Center AI services to be enabled for a set of agents.

agentService: The type of Contact Center AI service. Supported values are AgentAnswers , VAVTranscript, and Transcript .

agentServicesToDisable: Indicates the Contact Center AI service to be disabled for a set of agents.

agentService: The type of Contact Center AI service. Supported values are AgentAnswers , VAVTranscript, and Transcript .

### Example Delete
                              		  Request

```
<operation>
  <operationType>delete</operationType>
  <refURLs>
    <refURL>/unifiedconfig/config/calltype/5000</refURL>
    <refURL>/unifiedconfig/config/calltype/5001</refURL>
  </refURLs>
</operation>
```

### Example Update Request

```
<operation>
  <operationType>update</operationType>
  <refURLs>
    <refURL>/unifiedconfig/config/agent/5000</refURL>
    <refURL>/unifiedconfig/config/agent/5001</refURL>
  </refURLs>
  <changeSet>
    <agent> <description>New description</description> <agentServicesToEnable>
            <agentService>AgentAnswers<agentService>
            ....
        </agentServicesToEnable>
        <agentServicesToDisable>
            <agentService>Transcript<agentService>
            ....
        </agentServicesToDisable> <agentServicesToDisable>
            <agentService>VAVTranscript<agentService>
            ....
        </agentServicesToDisable> <agentDeskSettings>
        <refURL>/unifiedconfig/config/agentdesksetting/5434</refURL>
      </agentDeskSettings>
      <agentTeam>
        <refURL>/unifiedconfig/config/agentteam/5000</refURL>
      </agentTeam> <skillGroupsAdded>
        <skillGroup>
          <refURL>/unifiedconfig/config/skillgroup/6000</refURL>
        </skillGroup>
      </skillGroupsAdded>
      <skillGroupsRemoved>
        <skillGroup>
          <refURL>/unifiedconfig/config/skillgroup/6001</refURL>
        </skillGroup>
      </skillGroupsAdded>
      </agent>
  </changeSet>
</operation>
```

### Response
                              		  Parameters

status:
                                    				Indicates the state of the operation.

success:
                                          					 The operation succeeded for all items.

partialSuccess: The operation succeeded for some items, but
                                          					 other items had errors.

failure:
                                          					 The operation failed for all items.

apiErrors:
                                    				Errors indicate which items had errors and the cause of the error.

### Example
                              		  Success Response

The following
                              		  example shows the response when the delete operation is successful:

```
<operationsResult>
  <status>success</status>
</operationsResult>
```

### Example
                              		  Partial Success Message

The following
                              		  example shows a partial success response for a request to delete several
                              		  agents:

```
<operationsResult>
    <apiErrors>
        <apiError>
            <errorDetail xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type=
             "resourceErrorDetail">
                <refURL>agent/1</refURL>
                <apiErrors>
                    <apiError>
                        <errorMessage>The specified ID does not exist
                         in the database.</errorMessage>
                        <errorType>notFound.dbData</errorType>
                    </apiError>
                </apiErrors>
            </errorDetail>
            <errorMessage>There were one or more errors processing the following 
             request: delete agent/1</errorMessage>
            <errorType>operation.resourceErrors</errorType>
        </apiError>
        <apiError>
            <errorDetail xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type=
             "resourceErrorDetail">
                <refURL>agent/2</refURL>
                <apiErrors>
                    <apiError>
                        <errorMessage>The specified ID does not exist 
                         in the database.</errorMessage>
                        <errorType>notFound.dbData</errorType>
                    </apiError>
                </apiErrors>
            </errorDetail>
            <errorMessage>There were one or more errors processing the following 
             request: delete agent/2</errorMessage>
            <errorType>operation.resourceErrors</errorType>
        </apiError>
    </apiErrors>
    <status>partialSuccess</status>
</operationsResult>
```

### Example
                              		  Failure Response

The following
                              		  example shows a failure response for a request to delete a call type that does
                              		  not exist:

```
<operationsResult>
  <status>failure</status>
  <apiErrors>
    <apiError>
      <errorDetail xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type=
       "resourceErrorDetail">
        <refURL>/unifiedconfig/config/calltype/9999</refURL>
        <apiErrors>
          <apiError>
            <errorMessage>The specified ID does not exist in the database.</errorMessage>
            <errorType>notFound.dbData</errorType>
          </apiError>
        </apiErrors>
      </errorDetail>
      <errorMessage>There were one or more errors processing the following request: 
       delete /unifiedconfig/config
      /calltype/9999</errorMessage>
      <errorType>operation.resourceErrors</errorType>
    </apiError>
  </apiErrors>
</operationsResult>
```

### Request Limit

Maximum 100 items are allowed in a request:

```
<operationsResult>
<apiErrors>
    <apiError>
      <errorMessage>The number of resources provided (101) exceeds the maximum number allowed (100).</errorMessage>  
      <errorType>operation.tooManyResources</errorType>
      </apiError>
      </apiErrors>
  <status>failure</status>
</operationsResult>
```