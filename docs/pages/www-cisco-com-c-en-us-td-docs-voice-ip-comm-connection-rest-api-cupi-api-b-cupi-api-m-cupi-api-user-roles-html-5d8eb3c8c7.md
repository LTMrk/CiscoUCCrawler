---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-roles-html-5d8eb3c8c7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-roles.html
retrieved_at: 2026-08-17T03:48:55.036317+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Roles

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Roles

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Roles

## User Roles
                        	 API

### Listing User
                           	 Roles

```
GET https://<connection-server>/vmrest/users/<user-objectid>/userroles
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<UserRole>
  <URI>/vmrest/users/d8054a3a-6c09-4a25-9880-6589d2f1dc85/userroles/973e143e-af15-4ef4-a7c1-5fafd9cc53d4</URI>
  <ObjectId>973e143e-af15-4ef4-a7c1-5fafd9cc53d4</ObjectId>
  <UserObjectId>d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserObjectId>
  <UserURI>/vmrest/users/d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserURI>
  <RoleObjectId>ba166947-41e8-4ec9-ad14-03658d91240e</RoleObjectId>
  <RoleURI>/vmrest/roles/ba166947-41e8-4ec9-ad14-03658d91240e</RoleURI>
  <RoleName>Audit Administrator</RoleName>
  <Alias>ABCD_user template</Alias>
</UserRole>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/useres/<usereobjectid>/userroles
Accept: application/json
Connection: keep-alive
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
{
  "@total":"1"
  "UserRole":
  {
   "URI":"/vmrest/users/a9272189-720b-44b3-86e0-df7ef519599c/userroles/167b7661-ee8b-4c83-8867-decb88ec0c1c"
   "ObjectId":"167b7661-ee8b-4c83-8867-decb88ec0c1c"
   "UserObjectId":"a9272189-720b-44b3-86e0-df7ef519599c"
   "UserURI":"/vmrest/users/a9272189-720b-44b3-86e0-df7ef519599c"
   "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
   "RoleURI":"/vmrest/roles/04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
   "RoleName":"Help Desk Administrator"
   "Alias":"tenant005_usertemplate_1"
  }
}
```

```
Response Code: 200
```

### Adding
                           	 Roles

```
POST https://<connection-server>/vmrest/users/<user-objectid>/userroles
```

```
https://<connection-server>/vmrest/roles
```

```
<UserRole>
  <RoleObjectId>4f077e4e-61c7-4ce8-a58a-2c4bc6089319</RoleObjectId>
</UserRole>
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/39871e30-849a-4dcf-b868-2faf360d503a/userroles/f4d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15
```

JSON Example

```
POST https://<connection-server>/vmrest/useres/<user-objectid>/userroles
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
  "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
}
```

The following is the response from the above *POST* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/39871e30-849a-4dcf-b868-2faf360d503a/userroles/f4d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15
```

### Delete Role of
                           	 User

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/userroles/<userrolesId>
```

The following is the response from the above *DELETE* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/userroles/<userroleid>
Accept: application/json
Connection: keep-alive
The following is the response from the above *DELETE* request and the actual response will depend upon the information given by you:
```

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

| GET https://<connection-server>/vmrest/users/<user-objectid>/userroles |
|---|

| <UserRole>
  <URI>/vmrest/users/d8054a3a-6c09-4a25-9880-6589d2f1dc85/userroles/973e143e-af15-4ef4-a7c1-5fafd9cc53d4</URI>
  <ObjectId>973e143e-af15-4ef4-a7c1-5fafd9cc53d4</ObjectId>
  <UserObjectId>d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserObjectId>
  <UserURI>/vmrest/users/d8054a3a-6c09-4a25-9880-6589d2f1dc85</UserURI>
  <RoleObjectId>ba166947-41e8-4ec9-ad14-03658d91240e</RoleObjectId>
  <RoleURI>/vmrest/roles/ba166947-41e8-4ec9-ad14-03658d91240e</RoleURI>
  <RoleName>Audit Administrator</RoleName>
  <Alias>ABCD_user template</Alias>
</UserRole> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/useres/<usereobjectid>/userroles
Accept: application/json
Connection: keep-alive
The following is the response from the above *GET* request and the actual response will depend upon the information given by you:
{
  "@total":"1"
  "UserRole":
  {
   "URI":"/vmrest/users/a9272189-720b-44b3-86e0-df7ef519599c/userroles/167b7661-ee8b-4c83-8867-decb88ec0c1c"
   "ObjectId":"167b7661-ee8b-4c83-8867-decb88ec0c1c"
   "UserObjectId":"a9272189-720b-44b3-86e0-df7ef519599c"
   "UserURI":"/vmrest/users/a9272189-720b-44b3-86e0-df7ef519599c"
   "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
   "RoleURI":"/vmrest/roles/04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
   "RoleName":"Help Desk Administrator"
   "Alias":"tenant005_usertemplate_1"
  }
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/users/<user-objectid>/userroles |
|---|

| Note | To get the roles object ID, use this URI: |
|---|---|

| https://<connection-server>/vmrest/roles |
|---|

| <UserRole>
  <RoleObjectId>4f077e4e-61c7-4ce8-a58a-2c4bc6089319</RoleObjectId>
</UserRole> |
|---|

| Response Code: 201
/vmrest/users/39871e30-849a-4dcf-b868-2faf360d503a/userroles/f4d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15 |
|---|

| POST https://<connection-server>/vmrest/useres/<user-objectid>/userroles
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
  "RoleObjectId":"04d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15"
} |
|---|

| Response Code: 201
/vmrest/users/39871e30-849a-4dcf-b868-2faf360d503a/userroles/f4d0f1ef-a8c6-454a-8cf0-0e8db7bb2b15 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/userroles/<userrolesId> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/users/<user-objectid>/userroles/<userroleid>
Accept: application/json
Connection: keep-alive
The following is the response from the above *DELETE* request and the actual response will depend upon the information given by you: |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| ObjectId | String(36) | Read Only | A globally unique, system-generated
                                             					 identifier for a particular role of user |
| UserId | String | Read Only | URI of the User object (subject) to which
                                             					 this role is assigned. |
| UserObjectId | String(36) | Read Only | The unique identifier of the User object
                                             					 (subject) to which this role is assigned. |
| RoleObjectId | String(36) | Read/Write | The unique identifier of the Role object
                                             					 that specifies the privileges to be granted to the subject, for the target. For
                                             					 example, the role could be a "Technician." |
| RoleName | String(64) | Read Only | The name of the role. |
| RoleURI | String | Read Only | URI of the particular role |
| Alias | String(64) | Read Only | The alias of the user |