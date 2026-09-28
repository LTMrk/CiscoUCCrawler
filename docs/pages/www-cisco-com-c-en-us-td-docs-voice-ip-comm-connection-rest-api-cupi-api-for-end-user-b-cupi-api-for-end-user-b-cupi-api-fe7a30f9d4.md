---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-fe7a30f9d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010.html
retrieved_at: 2026-08-21T08:04:25.835234+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: December 21, 2018

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Unified Messaging Accounts

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Unified Messaging Accounts

- Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Unified Messaging Accounts

- About Unified Messaging Service Accounts

- Listing and Viewing

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Unified Messaging Accounts

Links to Other API pages: Cisco_Unity_Connection_APIs

This wiki page was written before we found out that there may not be any external service account that would require a user
                                    password. As of today (2010/05/06), this has not been confirmed, so I'm leaving this page as is. When it's time to officially
                                    publish this page, make sure to remove the sections on changing password if that information is indeed obsolete.

## About Unified Messaging Service Accounts

A user may have zero or more unified messaging service accounts (also known as external service accounts). Examples of these
                           services include Cisco Unified MeetingPlace 8.0, Exchange 2003, and Exchange 2007. Using CUPI for End Users, a user can:

Retrieve a list of its unified messaging service accounts,

Retrieve one of its unified messaging service accounts, and

Change the password for one of its unified messaging service accounts

## Listing and Viewing

To retrieve a list of unified messaging service accounts, use the GET method with URI _/vmrest/user/externalserviceaccounts_.
                              In the following example, the user has two unified messaging service accounts, Exchange2K3 and Exchange2K7:

```
ET http://<connection-server>/vmrest/user/externalserviceaccounts

200
OK
<?xml version="1.0" encoding="UTF-8"?>
<UserExternalServiceAccounts>
  <UserExternalServiceAccount>
    <URI>/vmrest/user/externalserviceaccounts/510eeaa6-6e85-40f3-88b3-863c2a4eec84</URI>
    <IsEnabled>true</IsEnabled>
    <UseServiceCredentials>true</UseServiceCredentials>
    <LoginType>0</LoginType>
    <ObjectId>510eeaa6-6e85-40f3-88b3-863c2a4eec84</ObjectId>
    <DisplayName>Exchange2K3</DisplayName>
  </UserExternalServiceAccount>
  <UserExternalServiceAccount>
    <URI>/vmrest/user/externalserviceaccounts/75436abf-8784-450f-ac61-23a08be2c364</URI>
    <IsEnabled>true</IsEnabled>
    <UseServiceCredentials>false</UseServiceCredentials>
    <LoginType>2</LoginType>
    <UserId>fung</UserId>
    <ObjectId>75436abf-8784-450f-ac61-23a08be2c364</ObjectId>
    <DisplayName>Exchange2K7</DisplayName>
  </UserExternalServiceAccount>
</UserExternalServiceAccounts>
```

For each unified messaging service account, CUPI returns the following information:

URI - The URI for retrieving the unified messaging service account

IsEnabled - A flag to indicate whether the unified messaging service account is enabled

UseServiceCredentials - A flag to indicate whether service credentials or user credentials are used to sign in the unified
                                    messaging service account

LoginType - A flag to indicate whether the user alias (0), a guest account (1), or a specified user ID (2) is used to sign
                                    in the account

UserId - The user ID to sign in to the unified messaging service account, if one is used

ObjectId - The unique ID of the unified messaging service account

Display Name - The display name of the unified messaging service account

To retrieve a specific unified messaging service account, use the GET method with the URI field from above as follows:

```
GET http://<connection-server>/vmrest/user/externalserviceaccounts/75436abf-8784-450f-ac61-23a08be2c364

200
OK
<?xml version="1.0" encoding="UTF-8"?>
<UserExternalServiceAccount>
  <IsEnabled>true</IsEnabled>
  <UseServiceCredentials>false</UseServiceCredentials>
  <LoginType>2</LoginType>
  <UserId>fung</UserId>
  <ObjectId>75436abf-8784-450f-ac61-23a08be2c364</ObjectId>
  <DisplayName>Exchange2K7</DisplayName>
</UserExternalServiceAccount>
```

Some unified messaging service accounts use service credentials to sign in; others employ user-supplied credentials. This
                              is indicated by the _UseServiceCredentials_ field. For unified messaging service accounts that require user credentials for
                              signing in (for example, those with _UseServiceCredentials_ set to false), the user may specify the password via a PUT method
                              by using the unified messaging service account URI and a query parameter, _password_, as follows:

```
PUT https://<connection-server>/vmrest/user/externalserviceaccounts/75436abf-8784-450f-ac61-23a08be2c364?password=abc123

204
No Content
null
```

Note that if you attempt to specify the password of a unified messaging service account that does not require a user password
                              (for example, one where _UseServiceCredentials_ is set to true), an error will be returned.

| Note | This wiki page was written before we found out that there may not be any external service account that would require a user
                                    password. As of today (2010/05/06), this has not been confirmed, so I'm leaving this page as is. When it's time to officially
                                    publish this page, make sure to remove the sections on changing password if that information is indeed obsolete. |
|---|---|

| ET http://<connection-server>/vmrest/user/externalserviceaccounts

200
OK
<?xml version="1.0" encoding="UTF-8"?>
<UserExternalServiceAccounts>
  <UserExternalServiceAccount>
    <URI>/vmrest/user/externalserviceaccounts/510eeaa6-6e85-40f3-88b3-863c2a4eec84</URI>
    <IsEnabled>true</IsEnabled>
    <UseServiceCredentials>true</UseServiceCredentials>
    <LoginType>0</LoginType>
    <ObjectId>510eeaa6-6e85-40f3-88b3-863c2a4eec84</ObjectId>
    <DisplayName>Exchange2K3</DisplayName>
  </UserExternalServiceAccount>
  <UserExternalServiceAccount>
    <URI>/vmrest/user/externalserviceaccounts/75436abf-8784-450f-ac61-23a08be2c364</URI>
    <IsEnabled>true</IsEnabled>
    <UseServiceCredentials>false</UseServiceCredentials>
    <LoginType>2</LoginType>
    <UserId>fung</UserId>
    <ObjectId>75436abf-8784-450f-ac61-23a08be2c364</ObjectId>
    <DisplayName>Exchange2K7</DisplayName>
  </UserExternalServiceAccount>
</UserExternalServiceAccounts> |
|---|

| GET http://<connection-server>/vmrest/user/externalserviceaccounts/75436abf-8784-450f-ac61-23a08be2c364

200
OK
<?xml version="1.0" encoding="UTF-8"?>
<UserExternalServiceAccount>
  <IsEnabled>true</IsEnabled>
  <UseServiceCredentials>false</UseServiceCredentials>
  <LoginType>2</LoginType>
  <UserId>fung</UserId>
  <ObjectId>75436abf-8784-450f-ac61-23a08be2c364</ObjectId>
  <DisplayName>Exchange2K7</DisplayName>
</UserExternalServiceAccount> |
|---|

| PUT https://<connection-server>/vmrest/user/externalserviceaccounts/75436abf-8784-450f-ac61-23a08be2c364?password=abc123

204
No Content
null |
|---|