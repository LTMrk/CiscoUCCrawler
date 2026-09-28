---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-637b0e9403
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_reason-code-api_1501.html
retrieved_at: 2026-08-21T16:47:55.792778+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Reason Code API

## Chapter: Reason Code API

- Reason Code API

- Reason Code API

# Reason Code API

## Reason Code API

The Reason Code feature in Packaged CCE is used to configure the Not Ready, Sign Out, and Wrap-Up reason codes.

Agents select the reason code on their agent desktops (Cisco Finesse) to provide the work status. Reason codes appear in the
                           Unified Intelligence Center reports and help identify agent behavior.

You can configure Reason Codes in Packaged CCE, and the configured reason codes appear in the agent desktop (Cisco Finesse)

Use the Reason Code API to define new reason codes, and edit and delete records of the existing reason codes.

### URL

### Operations

create : Creates one reason code.

delete : Marks one reason code for deletion.

get : Returns one reason code, using the URL https://<server>/unifiedconfig/config/reasoncode/<id> .

list : Retrieves a list of reason codes.

update : Updates one reason code.

### Parameters

refURL: The refURL of the reason code. See Shared Parameters .

changestamp: See Shared Parameters .

description: See Shared Parameters .

code: Required. The unique reason code. Integers between 1 and 65535. Value cannot be updated after the reason code has been
                                    created.

Do not specify code while configuring the Wrap-Up reasons.

text: Required. The text that describes the reason code. Maximum length of the text allowed is 39 characters.

reasonType: The type of reason. Allows the following values - NOT_READY, WRAPUP, and LOGOUT.

NOT_READY is the default reasonType. If reasonType is not specified in API, the system sets the reasonType as NOT_READY.

isGlobal: The reason code must be global (parameter set to true) or be assigned to a team to which the user belongs (parameter
                                    set to false). If isGlobal is not specified in API, the system sets isGlobal to true.

category: To identify the user-defined reason codes and system-defined (Not Ready and Sign Out) reason codes.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

text

description

text (default)

description

code

reasonType

category

See Search and Sort .

### Example Get Response

```
<reasonCode>
   <changeStamp>0</changeStamp>
   <refURL>/unifiedconfig/config/reasoncode/5001</refURL>
   <code>1</code> <isGlobal>false</isGlobal> <description>This is a reason code.</description>
   <text>Reason Code1</text> <reasonType>WRAPUP</reasonType> <category>User-defined</category> </reasonCode>
```

### Maximum limit for Reason Codes:

Reason Type

Global Reason Codes

Team Specific Reason Codes

Not-ready Reason Codes

Packaged CCE 2000 Agents Deployment - 100

Packaged CCE 4000 Agents Deployment - 1000

Packaged CCE 12000 Agents Deployment - 3000

Packaged CCE 2000 Agents Deployment - 100

Packaged CCE 4000 Agents Deployment - 100

Packaged CCE 12000 Agents Deployment - 100

Sign-out Reason Codes

Packaged CCE 2000 Agents Deployment - 100

Packaged CCE 4000 Agents Deployment - 1000

Packaged CCE 12000 Agents Deployment - 3000

Packaged CCE 2000 Agents Deployment - 100

Packaged CCE 4000 Agents Deployment - 100

Packaged CCE 12000 Agents Deployment - 100

Wrap-up Reason Labels

Packaged CCE 2000 Agents Deployment - 1500

Packaged CCE 4000 Agents Deployment - 1500

Packaged CCE 12000 Agents Deployment - 1500

Packaged CCE 2000 Agents Deployment - 100

Packaged CCE 4000 Agents Deployment - 100

Packaged CCE 12000 Agents Deployment - 100

Following are the REST responses received when the REST API runs to configure the Reason Codes:

Success - Configuration changes persist in AW DB and synchronized with Finesse DB.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with Finesse DB.

Code: 201

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with Finesse
                                    DB failed.)

Code: 503

Response: The server is currently busy. Please try again later. (This occurs when data synchronization to a device is in progress.)

```
<apiErrors>
<apiError>
<errorMessage>Configuration update failed for one or more devices.</errorMessage>
<errorType>PARTIAL_SUCCESS</errorType>
</apiError>
</apiErrors>
```

Failure - The configuration updates to AW DB is failed.

| Note | Do not specify code while configuring the Wrap-Up reasons. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| text description | text (default) description code reasonType category |

| Reason Type | Global Reason Codes | Team Specific Reason Codes |
|---|---|---|
| Not-ready Reason Codes | Packaged CCE 2000 Agents Deployment - 100 Packaged CCE 4000 Agents Deployment - 1000 Packaged CCE 12000 Agents Deployment - 3000 | Packaged CCE 2000 Agents Deployment - 100 Packaged CCE 4000 Agents Deployment - 100 Packaged CCE 12000 Agents Deployment - 100 |
| Sign-out Reason Codes | Packaged CCE 2000 Agents Deployment - 100 Packaged CCE 4000 Agents Deployment - 1000 Packaged CCE 12000 Agents Deployment - 3000 | Packaged CCE 2000 Agents Deployment - 100 Packaged CCE 4000 Agents Deployment - 100 Packaged CCE 12000 Agents Deployment - 100 |
| Wrap-up Reason Labels | Packaged CCE 2000 Agents Deployment - 1500 Packaged CCE 4000 Agents Deployment - 1500 Packaged CCE 12000 Agents Deployment - 1500 | Packaged CCE 2000 Agents Deployment - 100 Packaged CCE 4000 Agents Deployment - 100 Packaged CCE 12000 Agents Deployment - 100 |