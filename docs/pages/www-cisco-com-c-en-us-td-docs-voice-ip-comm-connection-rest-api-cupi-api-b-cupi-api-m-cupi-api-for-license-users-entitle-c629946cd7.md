---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-for-license-users-entitle-c629946cd7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi_api-for-license-users-entitlement.html
retrieved_at: 2026-08-17T03:49:03.822617+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: License Users Entitlement

## Chapter: License Users Entitlement

# License Users Entitlement

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- License User
                        	 Entitlement

### License User
                           	 Entitlement APIs

Administrator can use this API to
                              		fetch users belonging to a tenant and their license information which includes
                              		messaging and Speech view.

#### Listing the Users
                              	 with Their Licensing Details Who Belongs to a Particular Tenant

Obtain the Object ID of the
                                    		  tenant that you want to list the user licenses for:

```
GET https://<connection-server>/vmrest/tenants
```

Perform a GET operation on the tenant Objec tID using the following
                                    		  URI to list all the user licenses:

```
GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-34b193cff5bb/userlicenses
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="1">
  <UserLicense>
     <Alias>raman@Texoma.com</Alias>
     <DtmfAccessId>1234</DtmfAccessId>
     <Messaging>Basic</Messaging>
     <SpeechView>Speech View Standard</SpeechView>
  </UserLicense></UserLicenses
```

```
Response Code: 200
```

JSON Example

To list all the user licenses, use the following:

```
Request URI:
GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-34b193cff5bb/userlicenses
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "@total": "1",
  "UserLicense":
  [
  {
     "Alias": "raman",
     "DtmfAccessId": "1234",
     "PartitionObjectId": "6a4ac446-8b88-4456-aad7-099f249958fa",
     "Messaging": "Basic",
     "SpeechView": "Speech View Standard"
  }
  ]
}
```

```
Response Code: 200
```

#### List Users by
                              	 Performing an Query

Users can be queried based on all the fields of the License User
                                    		  Entitlement API, namely, Alias, DtmfAccessId, Messaging, SpeechView.

Obtain the Object ID of the tenant that you want to list the user
                                    		  licenses for:

```
GET https://<connection-server>/vmrest/tenants
```

Perform a GET operation on the tenant Object ID using the following
                                    		  URI to list the user licenses:

```
GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-
34b193cff5bb/userlicenses?query=(DtmfAccessId%20is%201234)
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="1">
  <UserLicense>
     <Alias>raman@Texoma.com</Alias>
     <DtmfAccessId>1234</DtmfAccessId>
     <Messaging>Basic</Messaging>
     <SpeechView>Speech View Standard</SpeechView>
  </UserLicense>
</UserLicenses>
```

```
Response Code: 200
```

JSON Example

To list the user licenses, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-
34b193cff5bb/userlicenses?query=(DtmfAccessId%20is%201234)
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
     "@total": "1",
     "UserLicense": [{
     "Alias": "raman",
     "DtmfAccessId": "1234",
     "PartitionObjectId": "6a4ac446-8b88-4456-aad7-099f249958fa",
     "Messaging": "Basic",
     "SpeechView": "Speech View Standard"
     } ]
}
```

```
Response Code: 200
```

#### Explanation of
                              	 Data Fields

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Bulk User License

### Bulk User License
                           	 APIs

The administrator uses this API to fetch all the users along with the
                              		license detail of each user. This API works in both Multi Tenancy Mode and Non
                              		Multi Tenancy Mode of Cisco Unity Connection.

If the number of users is more than 20000, the Bulk User License API
                              		performs pagination and fetches the smaller number of users.

#### Listing the Users
                              	 with Their License Details

Perform a GET operation to list
                                    		  the users along with their license details:

```
Get https://<connection-server>/vmrest/userlicenses
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="2"> 
 <UserLicense> 
   <Alias>user1@Tenant1.com</Alias> 
   <Messaging>Basic</Messaging> 
   <SpeechView>Speech View Pro</SpeechView> 
   <TenantId>Tenant1</TenantId> 
 </UserLicense> 
 <UserLicense> 
   <Alias>user2@Tenant1.com</Alias> 
   <Messaging>Basic</Messaging> 
   <SpeechView>Speech View Pro</SpeechView> 
   <TenantId>Tenant1</TenantId> 
 </UserLicense> 
</UserLicenses>
```

```
Response Code: 200
```

JSON Example

To list all the users along with their license details, use the
                                    		  following:

```
Request URI:
GET  https://<connection-server>/vmrest/userlicenses
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{   
    "@total": "2",   
    "UserLicense":    
    [            
    {         
       "Alias": "user1@Tenant1.com",         
       "Messaging": "Basic",         
       "TenantId": "Tenant1"      
    },             
    {         
       "Alias": "user2@Tenant1.com",         
       "Messaging": "Basic",         
       "TenantId": "Tenant1"      
    }   
    ]
}
```

```
Response Code: 200
```

#### Listing Users with
                              	 License Details Using Pagination

To list the users along with their license details using pagination,
                                    		  pass the value in the properties "rowsPerPage" and "pageNumber". By default the
                                    		  value of "rowsPerPage" is 2001.

Perform a GET operation to list the users along with their license
                                    		  details using pagination:

```
Get https://<connection-server>/vmrest/userlicenses?rowsPerPage=1&pageNumber=1
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="1"> 
     <UserLicense>
         <Alias>user1@Tenant1.com</Alias>
         <Messaging>Basic</Messaging>
         <SpeechView>Speech View Standard</SpeechView>
         <TenantId>Tenant1</TenantId>
     </UserLicense>
</UserLicenses>
```

```
Response Code: 200
```

JSON Example

To list all the users along with their license details using
                                    		  pagination, use the following:

```
Request URI:
GET  https://<connection-server>/vmrest/userlicenses?rowsPerPage=1&pageNumber=1
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{   
     "@total": "1",   
     "UserLicense":    
     {      
            "Alias": "user1@Tenant1.com",      
            "Messaging": "Basic",      
            "SpeechView": "Speech View Standard",      
            "TenantId": "Tenant1"   
     }
}
```

```
Response Code: 200
```

#### List the Number of
                              	 Users Using Licenses

To List the number of users using licenses, pass the value 0 in the
                                    		  property "rowsPerPage" or "pageNumber".

Perform a GET operation to list the number of users using licenses:

```
Get https://<connection-server>/vmrest/userlicenses?pageNumber=0
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="2"/>
```

```
Response Code: 200
```

JSON Response

To list all the number of users using licenses, use the following:

```
Request URI:
GET  https://<connection-server>/vmrest/userlicenses?pageNumber=0
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{"@total": "2"}
```

```
Response Code: 200
```

#### Listing Users
                              	 Using Same Type of Licenses

To list the users that are using same type of licenses, pass the
                                    		  "query" parameter.

Perform a GET operation to list the number of users using licenses:

```
Get https://<connection-server>/vmrest/userlicenses?query=(Messaging is Basic)
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="2"> 
     <UserLicense>
        <Alias>user1@Tenant1.com</Alias>
        <Messaging>Basic</Messaging>
        <SpeechView>Speech View Standard</SpeechView>
        <TenantId>Tenant1</TenantId>
     </UserLicense>
     <UserLicense>
        <Alias>user2@Tenant1.com</Alias>
        <Messaging>Basic</Messaging>
        <SpeechView>Speech View Standard</SpeechView>
        <TenantId>Tenant1</TenantId>
     </UserLicense>
</UserLicenses> 
<pre>
<pre>
Response Code: 200
```

JSON Example

To list the number of users using same type of licenses, use the
                                    		  following:

```
Request URI:
GET  https://<connection-server>/vmrest/userlicenses?query=(Messaging is Basic)
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{   
      "@total": "2",   
      "UserLicense":    
      [            
      {         
          "Alias": "user1@Tenant1.com",         
          "Messaging": "Basic",         
          "SpeechView": "Speech View Standard",         
          "TenantId": "Tenant1"      
      },            
      {         
          "Alias": "user2@Tenant1.com",         
          "Messaging": "Basic",         
          "SpeechView": "Speech View Standard",         
          "TenantId": "Tenant1"      
      }   
      ]
}
```

```
Response Code: 200
```

#### Listing License
                              	 Details of a Particular User

To list the license of a particular user, pass the "query" parameter.

Perform a GET operation to list the number of users using licenses:

```
Get https://<connection-server>/vmrest/userlicenses?query=(Alias is user1)
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<UserLicenses total="1">
      <UserLicense> 
          <Alias>user1</Alias> 
          <Messaging>Basic</Messaging> 
          <SpeechView>Speech View Standard</SpeechView> 
          <TenantId>Tenant1</TenantId> 
      </UserLicense> 
</UserLicenses>
```

```
Response Code: 200
```

JSON Response

To list the license of a particular user, use the following:

```
Request URI:
GET  https://ucbu-aricent-vm259.cisco.com/vmrest/userlicenses?query=(Alias is user1)
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{   
      "@total": "1",   
      "UserLicense":    
      {      
           "Alias": "user1",      
           "Messaging": "Basic",      
           "SpeechView": "Speech View Standard",      
           "TenantId": "Tenant1"   
}
} 

Response Code: 200
```

#### Explanation of
                              	 Data Fields

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-34b193cff5bb/userlicenses |
|---|

| <UserLicenses total="1">
  <UserLicense>
     <Alias>raman@Texoma.com</Alias>
     <DtmfAccessId>1234</DtmfAccessId>
     <Messaging>Basic</Messaging>
     <SpeechView>Speech View Standard</SpeechView>
  </UserLicense></UserLicenses |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-34b193cff5bb/userlicenses
Accept: application /json
Connection: keep-alive |
|---|

| {
  "@total": "1",
  "UserLicense":
  [
  {
     "Alias": "raman",
     "DtmfAccessId": "1234",
     "PartitionObjectId": "6a4ac446-8b88-4456-aad7-099f249958fa",
     "Messaging": "Basic",
     "SpeechView": "Speech View Standard"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-
34b193cff5bb/userlicenses?query=(DtmfAccessId%20is%201234) |
|---|

| <UserLicenses total="1">
  <UserLicense>
     <Alias>raman@Texoma.com</Alias>
     <DtmfAccessId>1234</DtmfAccessId>
     <Messaging>Basic</Messaging>
     <SpeechView>Speech View Standard</SpeechView>
  </UserLicense>
</UserLicenses> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/tenants/c9d9c29d-4a81-47b5-9296-
34b193cff5bb/userlicenses?query=(DtmfAccessId%20is%201234)
Accept: application /json
Connection: keep-alive |
|---|

| {
     "@total": "1",
     "UserLicense": [{
     "Alias": "raman",
     "DtmfAccessId": "1234",
     "PartitionObjectId": "6a4ac446-8b88-4456-aad7-099f249958fa",
     "Messaging": "Basic",
     "SpeechView": "Speech View Standard"
     } ]
} |
|---|

| Response Code: 200 |
|---|

| Parameters | Operations | Data Type | Comments |
|---|---|---|---|
| Alias | Read Only | String(64) | The Alias of the user belonging to a
                                                					 Tenant. |
| dtmfAccessId | Read Only | String(40) | The DTMF access id (i.e., extension) of the
                                                					 subscriber. |
| Messaging | Read Only | String | Licensing Tag either Basic, Enhanced,
                                                					 Enhanced+ |
| SpeechView | Read Only | String | It is a licensing Tag that specifies the
                                                					 transcription service. Speech View Standard or Speech View Pro. This field is
                                                					 not displayed when users do not use the transcription service. |

| Note | In Cisco Unity Connection 10.0(1) and later, TenantId in API
                                          		  response is available in Tenant Partitioning. |
|---|---|

| Get https://<connection-server>/vmrest/userlicenses |
|---|

| <UserLicenses total="2"> 
 <UserLicense> 
   <Alias>user1@Tenant1.com</Alias> 
   <Messaging>Basic</Messaging> 
   <SpeechView>Speech View Pro</SpeechView> 
   <TenantId>Tenant1</TenantId> 
 </UserLicense> 
 <UserLicense> 
   <Alias>user2@Tenant1.com</Alias> 
   <Messaging>Basic</Messaging> 
   <SpeechView>Speech View Pro</SpeechView> 
   <TenantId>Tenant1</TenantId> 
 </UserLicense> 
</UserLicenses> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET  https://<connection-server>/vmrest/userlicenses
Accept: application /json
Connection: keep-alive |
|---|

| {   
    "@total": "2",   
    "UserLicense":    
    [            
    {         
       "Alias": "user1@Tenant1.com",         
       "Messaging": "Basic",         
       "TenantId": "Tenant1"      
    },             
    {         
       "Alias": "user2@Tenant1.com",         
       "Messaging": "Basic",         
       "TenantId": "Tenant1"      
    }   
    ]
} |
|---|

| Response Code: 200 |
|---|

| Get https://<connection-server>/vmrest/userlicenses?rowsPerPage=1&pageNumber=1 |
|---|

| <UserLicenses total="1"> 
     <UserLicense>
         <Alias>user1@Tenant1.com</Alias>
         <Messaging>Basic</Messaging>
         <SpeechView>Speech View Standard</SpeechView>
         <TenantId>Tenant1</TenantId>
     </UserLicense>
</UserLicenses> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET  https://<connection-server>/vmrest/userlicenses?rowsPerPage=1&pageNumber=1
Accept: application /json
Connection: keep-alive |
|---|

| {   
     "@total": "1",   
     "UserLicense":    
     {      
            "Alias": "user1@Tenant1.com",      
            "Messaging": "Basic",      
            "SpeechView": "Speech View Standard",      
            "TenantId": "Tenant1"   
     }
} |
|---|

| Response Code: 200 |
|---|

| Get https://<connection-server>/vmrest/userlicenses?pageNumber=0 |
|---|

| <UserLicenses total="2"/> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET  https://<connection-server>/vmrest/userlicenses?pageNumber=0
Accept: application /json
Connection: keep-alive |
|---|

| {"@total": "2"} |
|---|

| Response Code: 200 |
|---|

| Get https://<connection-server>/vmrest/userlicenses?query=(Messaging is Basic) |
|---|

| <UserLicenses total="2"> 
     <UserLicense>
        <Alias>user1@Tenant1.com</Alias>
        <Messaging>Basic</Messaging>
        <SpeechView>Speech View Standard</SpeechView>
        <TenantId>Tenant1</TenantId>
     </UserLicense>
     <UserLicense>
        <Alias>user2@Tenant1.com</Alias>
        <Messaging>Basic</Messaging>
        <SpeechView>Speech View Standard</SpeechView>
        <TenantId>Tenant1</TenantId>
     </UserLicense>
</UserLicenses> 
<pre>
<pre>
Response Code: 200 |
|---|

| Request URI:
GET  https://<connection-server>/vmrest/userlicenses?query=(Messaging is Basic)
Accept: application /json
Connection: keep-alive |
|---|

| {   
      "@total": "2",   
      "UserLicense":    
      [            
      {         
          "Alias": "user1@Tenant1.com",         
          "Messaging": "Basic",         
          "SpeechView": "Speech View Standard",         
          "TenantId": "Tenant1"      
      },            
      {         
          "Alias": "user2@Tenant1.com",         
          "Messaging": "Basic",         
          "SpeechView": "Speech View Standard",         
          "TenantId": "Tenant1"      
      }   
      ]
} |
|---|

| Response Code: 200 |
|---|

| Get https://<connection-server>/vmrest/userlicenses?query=(Alias is user1) |
|---|

| <UserLicenses total="1">
      <UserLicense> 
          <Alias>user1</Alias> 
          <Messaging>Basic</Messaging> 
          <SpeechView>Speech View Standard</SpeechView> 
          <TenantId>Tenant1</TenantId> 
      </UserLicense> 
</UserLicenses> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET  https://ucbu-aricent-vm259.cisco.com/vmrest/userlicenses?query=(Alias is user1)
Accept: application /json
Connection: keep-alive |
|---|

| {   
      "@total": "1",   
      "UserLicense":    
      {      
           "Alias": "user1",      
           "Messaging": "Basic",      
           "SpeechView": "Speech View Standard",      
           "TenantId": "Tenant1"   
}
} 

Response Code: 200 |
|---|

| Parameters | Operations | Data Type | Comments |
|---|---|---|---|
| Alias | Read Only | String(64) | The Alias of the user. |
| Messaging | Read Only | String | Licensing Tag either Basic, Enhanced,
                                                					 Enhanced+ |
| SpeechView | Read Only | String | It is a licensing Tag that specifies the
                                                					 transcription service Speech View Standard or Speech View Pro This field is not
                                                					 displayed when users do not use the transcription service. |
| TenantId | Read Only | String | This field contains the Name of the tenant
                                                					 to which the user belongs. This field will be populated only if the connection
                                                					 is working in the Multi Tenancy Mode and user belongs to a Tenant. |