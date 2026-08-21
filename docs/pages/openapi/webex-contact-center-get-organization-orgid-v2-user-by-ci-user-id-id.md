---
doc_id: webex-contact-center-get-organization-orgid-v2-user-by-ci-user-id-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/user/by-ci-user-id/{id}
operation_id: getUserByCiUserIdWithUserProfileGranularAccessUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.790665+00:00
---

# GET /organization/{orgid}/v2/user/by-ci-user-id/{id}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUserByCiUserIdWithUserProfileGranularAccessUser`

## Resumen
Get specific User by CI User ID

## Descripción
Retrieve an existing User using the CI ID  in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): CI ID of the User.
- `includeUserProfile` [query] (boolean): Specifiy whether to include user profile data
- `includeNames` [query] (boolean): Specifiy whether to include resource collection names
- `includeSkillDetails` [query] (boolean): If set to true, the response includes skill information for each dynamic skill assignment. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/user/by-ci-user-id/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK

### Ejemplo — respuesta 200
```json
{
  "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "id": "93912f11-6017-404b-bf14-5331890b1797",
  "version": 1,
  "firstName": "John",
  "lastName": "Wick",
  "email": "johnwick@company.com",
  "workPhone": "1234567890",
  "mobile": "1234567890",
  "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "timezone": "America/New_York",
  "xspVersion": "xsp-24.0",
  "subscriptionId": "04d0bdf6-6d6a-4aae-8a8a-71c9152e6478",
  "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "userProfileType": "PREMIUM_AGENT",
  "contactCenterEnabled": true,
  "siteId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "siteName": "bengaluru",
  "teamIds": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
  "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "deafultDialledNumber": "1234567890",
  "externalIdentifier": "121212",
  "active": true,
  "dbId": "1dq45f23-1234-6r18-9a83-2atuiy0d4bh1",
  "userProfileGranularAccessData": {
    "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "id": "93912f11-6017-404b-bf14-5331890b1797",
    "version": 1,
    "name": "Contact Center Admin Profile",
    "description": "This profile should be applied only to contact center admins.",
    "profileType": "PREMIUM_AGENT",
    "active": true,
    "permissionAccessLevel": "ALL",
    "resourceAccessLevel":
  ... (truncado)
```

### Ejemplo — respuesta 200
```json
{
  "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "id": "93912f11-6017-404b-bf14-5331890b1797",
  "version": 1,
  "firstName": "John",
  "lastName": "Wick",
  "email": "johnwick@company.com",
  "workPhone": "1234567890",
  "mobile": "1234567890",
  "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "timezone": "America/New_York",
  "xspVersion": "xsp-24.0",
  "subscriptionId": "04d0bdf6-6d6a-4aae-8a8a-71c9152e6478",
  "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "userProfileType": "PREMIUM_AGENT",
  "contactCenterEnabled": true,
  "siteId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "siteName": "bengaluru",
  "teamIds": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
  "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "deafultDialledNumber": "1234567890",
  "externalIdentifier": "121212",
  "active": true,
  "dbId": "1dq45f23-1234-6r18-9a83-2atuiy0d4bh1",
  "userProfileGranularAccessData": {
    "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "id": "93912f11-6017-404b-bf14-5331890b1797",
    "version": 1,
    "name": "Contact Center Admin Profile",
    "description": "This profile should be applied only to contact center admins.",
    "profileType": "PREMIUM_AGENT",
    "active": true,
    "permissionAccessLevel": "ALL",
    "resourceAccessLevel":
  ... (truncado)
```

## Respuestas de error
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs