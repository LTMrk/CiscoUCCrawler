---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-cbda40619b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_011000.html
retrieved_at: 2026-08-16T20:23:15.526989+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

Updated: August 21, 2023

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

Agent update: Update multiple agents (available for supervisors and administrators) .

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

agentServicesToEnable: Indicates the Contact Center AI services to be enabled for a set of agents.

agentService: The type of Contact Center AI service. Supported values are AgentAnswers and Transcript .

agentServicesToDisable: Indicates the Contact Center AI service to be disabled for a set of agents.

agentService: The type of Contact Center AI service. Supported values are AgentAnswers and Transcript .

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
    <agent> <agentServicesToEnable>
            <agentService>AgentAnswers<agentService>
            ....
        </agentServicesToEnable>
        <agentServicesToDisable>
            <agentService>Transcript<agentService>
            ....
        </agentServicesToDisable> <skillGroupsAdded>
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