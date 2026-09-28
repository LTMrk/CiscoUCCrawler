---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-ad055c02c4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_1501_person_api.html
retrieved_at: 2026-08-16T20:18:37.727947+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Person API

## Chapter: Person API

- Person API

- Person API

# Person API

## Person API

Use the Person API to list the persons currently defined in the database, define new persons, view, edit, and delete existing
                           persons.

### URL

https://<server>/unifiedconfig/config/person/

### Operations

create : Creates a person using the url: https://<ip_address>/unifiedconfig/config/person

delete : Deletes a person using the url: https://<ip_address>/unifiedconfig/config/person/<personID>

get : Returns a single person using the url: https://<ip_address>/unifiedconfig/config/person/<personID>

update : Updates a person using the url: https://<ip_address>/unifiedconfig/config/person/<personID> .

list : Retrieves a list of persons.

Query parameters:

q : Query parameter for search

sort

startIndex : Default 0

resultsPerPage : Default 25

assignableForPeripheralId : Short number, considers all Person resources which can be assigned to an Agent under the specified Peripheral.

API access is provided to users who have Configuration access (but not Setup access) assigned on the User List page. Additionally, the Person List must be enabled in the Feature Control Set List page.

### Parameters

refURL: The refURL for the Person

digitalChannel: Whether the person is enabled for digital channel interaction. Email address is mandatory when digitalChannel
                                    is set to True. The valid values are True or False. The default is False.

changeStamp: shared parameter

description: shared parameter

emailAddress: The email address of the Person.

firstName: Persons's first name. Maximum of 32 characters.

lastName: Persons' first name. Maximum of 32 characters.

loginEnabled: Whether the Person can log in. True or False. The default is True.

userName: Persons's login name. Maximum of 255 characters. It cannot be empty.

password: Person's password. If Cisco IdS SSO is enabled, the password cannot be set.

### Search and Sort Values

Sorting fields can be set to ascending (asc) or descending (desc).

The following table shows the parameters that are searchable and the parameters that are sortable.

Search Parameter

Sort Parameter

firstName

firstName

lastName

lastName

loginName

loginName

See Search and Sort .

### Example Get Response

```
<person>
              <refURL>/unifiedconfig/config/person/5013</refURL>    
              <digitalChannel>false</digitalChannel>
              <emailAddress>person1@gmail.com</emailAddress>
              <firstName>person1</firstName>
              <lastName>person1</lastName>
              <loginEnabled>true</loginEnabled>
              <ssoEnabled>false</ssoEnabled>
              <changeStamp>0</changeStamp>
              <userName>person1@gmail.com</userName>
        </person>
```

| Note | API access is provided to users who have Configuration access (but not Setup access) assigned on the User List page. Additionally, the Person List must be enabled in the Feature Control Set List page. |
|---|---|

| Search Parameter | Sort Parameter |
|---|---|
| firstName | firstName |
| lastName | lastName |
| loginName | loginName |