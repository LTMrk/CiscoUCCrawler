---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-maintenance-guide-pcce-b-featur-92e888980e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/maintenance/guide/pcce_b_features-guide-1262/pcce_b_features-guide-1261_appendix_010011.html
retrieved_at: 2026-08-21T12:29:51.112917+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: November 15, 2024

Chapter: Do Not Call Table

## Chapter: Do Not Call Table

- Do Not Call Table

- Do_Not_Call Table

# Do Not Call Table

## Do_Not_Call Table

The Do_Not_Call
                              		  table includes all the phone numbers and extensions that, when matched exactly,
                              		  are not dialed during an Outbound Option campaign.

The following
                              		  table lists the Do_Not_Call table column names and provides their descriptions.

Column
                                          						Name

Type

Description

Phone

VARCHAR(20)

The Do
                                          						Not Call phone number.

PhoneExt

VARCHAR(8)

The extension for the Do Not Call phone number.

Although the phone number extension is imported into the table, it is currently not used for any dialing operations.

### Do Not Call
                              		  Considerations

Consider the following for the Do Not Call feature:

When you upgrade to or downgrade from Cisco Unified CCE, Release 11.6(1), the Do Not Call table is not available. Therefore,
                                    import the Do Not Call table again after upgrade or downgrade.

Do not configure multiple Do Not Call import rules.

A customer number is dialled even if the number is listed in the Do Not Call table. This occurs when:

the Campaign Manager restarts.

one of the routers is not available during the import of the Do Not Call records.

Do not perform manual operations on database including database replication.

| Column
                                          						Name | Type | Description |
|---|---|---|
| Phone | VARCHAR(20) | The Do
                                          						Not Call phone number. |
| PhoneExt | VARCHAR(8) | The extension for the Do Not Call phone number. Note Although the phone number extension is imported into the table, it is currently not used for any dialing operations. | Note | Although the phone number extension is imported into the table, it is currently not used for any dialing operations. |
| Note | Although the phone number extension is imported into the table, it is currently not used for any dialing operations. |

| Note | Although the phone number extension is imported into the table, it is currently not used for any dialing operations. |
|---|---|