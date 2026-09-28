---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-operation-guide-chcs-b-hcs-smart-licensing-operational-5bf5bbb5a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/Operation_Guide/chcs_b_hcs-smart-licensing-operational-guide/chcs_b_hcs-smart-licensing-operational-guide_chapter_0110.html
retrieved_at: 2026-09-01T20:56:17.947768+00:00
---

Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

# Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

Updated: April 23, 2020

Chapter: Smart Licensing Reports

## Chapter: Smart Licensing Reports

- Smart Licensing Reports

- HCM-F License Dashboard

# Smart Licensing Reports

## Smart Licensing Reports

HCM-F has Service Inventory and HLM (CSV and Excel) reports that have license-related details. Traditionally, these components
                           generate reports after consuming licenses from PLM. These components are enhanced to consume the license data from CSSM or Satellite and generate the reports. If PLMs are also provisioned in the system, then these components query the license details from
                           PLM , Satellite and CSSM, and generate the report in a unified format. Further, you can distinguish whether the licenses are consumed from
                           PLM or Smart Account - Virtual Account name.

The enhanced SI report for smart licensing contains license data from both CSSM , Satellite, and PLM. The report version remains same as no format has been changed. It is possible to have one cluster registered to PLM
                           and another cluster registered to a Virtual Account.

Sample SI Report with Smart Licensing:

PLM Hostname or IP Address: 200.0.X.XXX

Smart Account Domain name: smart-account.cisco.com

Virtual Account name: virtual-account1

Local Account name: local-account

```
|LICENSESUMMARYSTART|
|SUMMARY|PLMINFO|200.0.X.XXX|HCER|10|HCER_User|10010|0|10010|VALID|

|SUMMARY|PLMINFO|200.0.X.XXX|HUCM|10|HUCM_TelePresenceRoom|45000|0|45000|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HUCM|10|HUCM_Essential|56000|0|56000|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HUCM|10|HUCM_Basic|56010|0|56010|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HUCM|10|HUCM_Foundation|46000|2|45998|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HUCM|10|HUCM_Standard|46000|0|46000|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HCUC|10|HCUC_SpeechConnectPort|0|0|0|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HCUC|10|HCUC_BasicMessaging|13010|0|13010|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HCUC|10|HCUC_EnhancedMessaging|13000|0|13000|VALID|
|SUMMARY|PLMINFO|200.0.X.XXX|HCUC|10|HCUC_StandardMessaging|2000|0|2000|VALID|

|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HCER|10|HCER_User|10010|0|10010|In Compliance|

|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HUCM|10|HUCM_TelePresenceRoom|45000|0|45000|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HUCM|10|HUCM_Essential|56000|0|56000|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@local-account ,Satellite ,1000,2021-11-26,TERM|HUCM|10|HUCM_Basic|56010|0|56010|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HUCM|10|HUCM_Foundation|46000|2|45998|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@local-account ,Satellite ,1000,2021-11-26,TERM|HUCM|10|HUCM_Standard|46000|0|46000|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HCUC|10|HCUC_SpeechConnectPort|0|0|0|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HCUC|10|HCUC_BasicMessaging|13010|0|13010|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@local-account.cisco.com ,Satellite ,1000,2021-11-26,TERM|HCUC|10|HCUC_EnhancedMessaging|13000|0|13000|In Compliance|
|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com ,CSSM ,1000,2021-11-26,TERM|HCUC|10|HCUC_StandardMessaging|2000|0|2000|In Compliance|

|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C1|HUCM|200.2.1.11|HUCM_TelePresenceRoom|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C1|HUCM|200.2.1.11|HUCM_Essential|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C1|HUCM|200.2.1.11|HUCM_Foundation|1|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C1|HUCM|200.2.1.11|HUCM_Standard|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C1|HUCM|200.2.1.11|HUCM_Basic|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C2|HUCM|200.3.1.11|HUCM_TelePresenceRoom|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C2|HUCM|200.3.1.11|HUCM_Essential|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C2|HUCM|200.3.1.11|HUCM_Foundation|1|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C2|HUCM|200.3.1.11|HUCM_Standard|0|
|SUMMARY|CUSTLICENSEINFO|200.0.X.XXX|~|~|C2|HUCM|200.3.1.11|HUCM_Basic|0|

|SUMMARY|CUSTLICENSEINFO| virtual-account1@local-account ,Satellite |~|~|C3|HUCM|200.2.1.12|HUCM_TelePresenceRoom|0|
|SUMMARY|CUSTLICENSEINFO| virtual-account1@smart-account.cisco.com ,CSSM |~|~|C3|HUCM|200.2.1.12|HUCM_Essential|0|
|SUMMARY|CUSTLICENSEINFO| virtual-account1@smart-account.cisco.com ,CSSM |~|~|C3|HUCM|200.2.1.12|HUCM_Foundation|1|
|SUMMARY|CUSTLICENSEINFO| virtual-account1@local-account ,Satellite |~|~|C3|HUCM|200.2.1.12|HUCM_Standard|0|
|SUMMARY|CUSTLICENSEINFO| virtual-account1@smart-account.cisco.com ,CSSM |~|~|C3|HUCM|200.2.1.12|HUCM_Basic|0|

|SUMMARY|SITELICENSEINFO|~|~|C1|~|HCS Foundation|1|
|SUMMARY|SITELICENSEINFO|~|~|C2|~|HCS Foundation|2|
|LICENSESUMMARYEND|
```

```
The report format is as follows:

|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com,SubsID,Exp.Date,License Model|UC Application|product version|License Model|Installed License Count
|Required License Count|Available License Count|Status
```

```
The report format is as follows:

|SUMMARY|PLMINFO| virtual-account1@smart-account.cisco.com or virtual-account1@local-account,Transport Mode,SubsID,Exp.Date,License Model|UC Application|product version|License Model|Installed License Count
|Required License Count|Available License Count|Status
```

Similar to Service Inventory report format, the HLM reports maintained with name/hostname/IP address of the PLM are replaced
                                       with the Virtual Account and Smart Account names Virtual Account Name @ Smart Account Name . The LM Name column of the HLM report shows the virtual account along with the PLM.

### HCM-F License Dashboard

For more information on License Dashboard and how to view the license summary details, see HCM-F License Dashoard section at Cisco Hosted Collaboration Solution License Management Guide .

| Note | Similar to Service Inventory report format, the HLM reports maintained with name/hostname/IP address of the PLM are replaced
                                       with the Virtual Account and Smart Account names Virtual Account Name @ Smart Account Name . The LM Name column of the HLM report shows the virtual account along with the PLM. |
|---|---|