---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-ff2d9f99b1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce-m-1501-webex-common-identity-user-sync-api.html
retrieved_at: 2026-08-21T16:49:10.720937+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Webex Common Identity User Sync API

## Chapter: Webex Common Identity User Sync API

# Webex Common Identity User Sync API

## Webex Common Identity User Sync API

Webex Common Identity Contact Center user sync API is accessible by PCCE Administrator roles only.

This API can be used to pull Webex Common Identity Contact Center users to CCE database.

### URL

https://<server>/unifiedconfig/config/wxci/sync

### Operations

POST: Manually trigger the Webex CI User Sync task.

### REST Responses

Following are the possible REST responses that can be received for Webex CI User Sync API calls:

Success (202 Accepted)

User sync task already running (403 Forbidden)

User sync task disabled (403 Forbidden)

Example of API 202 response headers:

Location: https://<server>/unifiedconfig/config/asyncrequeststatus/db/<asyncTaskID>

Example of API 202 response body:

```
{
    "progress": "IN_QUEUE"
}
```

## Webex Common Identity User Sync Status API

Webex Common Identity User Sync Status API is accessible by PCCE Administrator roles only.

This API returns the details about the last sync performed, whether it was an automatic or manual sync.

### URL

https://<AW host>/unifiedconfig/config/wxci/sync/status

### Operations

GET : Access existing user sync configurations.

AttributeName

API field

### Sample Response

Success - 200 ok

When the periodic sync task is not scheduled, the API returns status as below:

```
{
    "currentSyncStatus": "NOT_SCHEDULED"
}
```

When the periodic sync task has executed, completed and updated the status in DB, the API returns status as below:

```
{
    "currentSyncStatus": "SCHEDULED",
    "lastSyncStats": "{5} users(s) created, {3} users updated, {1} user(s) failed",
    "lastSyncStatus": "SUCCESS",
    "lastSyncTime": "02:06, May 21, 2024"
}
```

lastSyncTime is stored in UTC format in DB. API will convert this to AW timezone and return in the response.

### Error Responses

Unauthorized - 400

Server errors - 500

## Webex Common Identity User Sync Config API

Webex Common Identity User Sync Config API is accessible by PCCE Administrator roles only.

This API can be used to modify and access sync configuration of Webex CI Contact Center users. The sync configuration is based
                           on the parameters as given below.

### URL

https://<server>/unifiedconfig/config/wxci/sync/config

### Operations

GET : Access existing Contact Center user sync configurations.

PUT : Create and update Contact Center user sync configurations.

### Parameters

groups: A list of IDs for AD groups considered as source of users data.

enabled: A boolean flag for enabling or disabling the auto sync feature.

frequency: An integer value for specifying the frequency (in minutes) of auto sync feature.

### Example create and update requests

```
{
    "enabled": true,
    "frequency": 1241,
    "groups": [
        {
            "group": [
                "groupID1",
                "groupID2",
                "groupID3"
            ]
        }
    ]
}
```

### REST Responses

Following are the possible REST responses that can be received for Webex CI User Sync Config API calls:

Success (200 OK)

Examples of API errors:

Error Response - Structural Errors

```
{
    "apiError": [
        {
            "errorData": "enabled",
            "errorMessage": "Invalid boolean value; must be true or false.",
            "errorType": "invalidInput.format.boolean"
        },
        {
            "errorData": "frequency",
            "errorMessage": "Not a number: number",
            "errorType": "invalidInput.unexpectedXmlElement"
        }
    ]
}
```

Error Response - Validation Errors

```
{
    "apiError": [
        {
            "errorMessage": "Size of group IDs list must be within the range 1 to 3.",
            "errorType": "wxci.syncConfig.groupsMax"
        },
        {
            "errorMessage": "Invalid sync group ID.",
            "errorType": "wxci.syncConfig.groupsInvalid"
        },
        {
            "errorMessage": "Invalid sync group ID.",
            "errorType": "wxci.syncConfig.groupsInvalid"
        },
        {
            "errorMessage": "Empty sync group ID is not allowed.",
            "errorType": "wxci.syncConfig.groupsEmptyValue"
        },
        {
            "errorMessage": "Duplicated group IDs.",
            "errorType": "wxci.syncConfig.groupsDuplicated"
        },
        {
            "errorMessage": "Frequency must be an integer within the range 30 to 1440.",
            "errorType": "wxci.syncConfig.frequencyMin"
        }
    ]
}
```

## Webex Common Identity User Sync Failedusers API

Webex Common Identity User Sync Failedusers API is acessible by PCCE Administrator roles only.

This API can be used to retrieve the list of failed users.

URL

https://<server>/unifiedconfig/config/wxci/sync/failedusers

Operations

get : Returns the list of failed users with their details, or an error message.

Produces : application/json, application/xml

Sample Response

```
{
"username": [
"synergytest001@wbxlab.us",
"synergytest002@wbxlab.us",
"synergytest003@wbxlab.us",
"synergytest004@wbxlab.us",
"synergytest005@wbxlab.us",
"synergytest006@wbxlab.us",
"synergytest007@wbxlab.us",
"synergytest008@wbxlab.us",
"synergytest009@wbxlab.us",
"synergytest010@wbxlab.us",
"synergytest011@wbxlab.us",
"synergytest012@wbxlab.us",
"synergytest013@wbxlab.us",
"synergytest014@wbxlab.us",
"synergytest015@wbxlab.us",
"synergytest016@wbxlab.us",
"synergytest017@wbxlab.us",
"synergytest018@wbxlab.us",
"synergytest019@wbxlab.us",
"synergytest020@wbxlab.us",
"synergytest021@wbxlab.us",
"synergytest022@wbxlab.us",
"synergytest023@wbxlab.us",
"synergytest024@wbxlab.us",
"synergytest025@wbxlab.us",
"synergytest026@wbxlab.us"
]
}
```

Error codes:

400 - Unauthorized

500 - Internal server error

| AttributeName | API field |
|---|---|
| WXCI_SYNC_LAST_RUN_TIME | lastSyncTime |
| WXCI_SYNC_LAST_RUN_STATUS | lastSyncStatus |
| WXCI_SYNC_CURRENT_STATUS | currentSyncStatus |
| WXCI_SYNC_LAST_RUN_STATS | lastSyncStats |

| Note | lastSyncTime is stored in UTC format in DB. API will convert this to AW timezone and return in the response. |
|---|---|