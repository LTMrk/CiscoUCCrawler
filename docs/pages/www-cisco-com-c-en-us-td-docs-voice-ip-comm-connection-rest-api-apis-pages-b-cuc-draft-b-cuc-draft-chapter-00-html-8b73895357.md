---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-apis-pages-b-cuc-draft-b-cuc-draft-chapter-00-html-8b73895357
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_CUC_Draft/b_CUC_Draft_chapter_00.html
retrieved_at: 2026-08-21T08:07:59.995468+00:00
---

Cisco Unity Connection Draft

# Cisco Unity Connection Draft

Updated: January 2, 2019

Chapter: Cisco Unity
	 Connection API List

## Chapter: Cisco Unity
	 Connection API List

- Cisco Unity                              	 Connection API List

- Draft

# Cisco Unity
                     	 Connection API List

## Draft

```
https://<host>:<port>/vmrest/version
```

```
https://10.10.10.10:8443/vmrest/schema/VersionInformation
```

```
https://<host>:<port>/vmrest/distributionlists
```

```
https://10.10.10.10:8443/vmrest/schema/DistributionList
```

```
https://<host>:<port>/vmrest/distributionlists/{objectid}/distributionlistmembers
```

```
https://10.10.10.10:8443/vmrest/schema/DistributionListMember
```

| Description: | Use this API to retrieve the current version
                                          				  of the system. |
|---|---|
| API URI: | https://<host>:<port>/vmrest/version |
| Supported Response Formats: | XML |
| HTTP Method: | GET |
| Request Parameters: | None |
| Header Parameters: | None |
| Parameter Description: | None |
| Schema: | https://10.10.10.10:8443/vmrest/schema/VersionInformation |
| Failure Response Schema: | None |
| Related Error Codes: | See API Response Codes. |
| Events Triggered: | None |
| Release: | 8.5(1) |
| Notes or Examples: | Example |

| Description: | Use this API to work with distribution lists. |
|---|---|
| API URI: | https://<host>:<port>/vmrest/distributionlists |
| Supported Response Formats: | XML |
| HTTP Method: | GET,POST,PUT,DELETE |
| Request Parameters: | query, sort, pageNumber, rowsPerPage,
                                          				  properties |
| Header Parameters: | None |
| Parameter Description: | None |
| Schema: | https://10.10.10.10:8443/vmrest/schema/DistributionList |
| Failure Response Schema: | None |
| Related Error Codes: | See API Response Codes. |
| Events Triggered: | None |
| Release: | 8.5(1) |
| Notes or Examples: | Example |

| Description: | Use this API to work with distribution lists. |
|---|---|
| API URI: | https://<host>:<port>/vmrest/distributionlists/{objectid}/distributionlistmembers |
| Supported Response Formats: | XML |
| HTTP Method: | GET,POST,PUT,DELETE |
| Request Parameters: | query, sort, pageNumber, rowsPerPage,
                                          				  properties |
| Header Parameters: | None |
| Parameter Description: | None |
| Schema: | https://10.10.10.10:8443/vmrest/schema/DistributionListMember |
| Failure Response Schema: | None |
| Related Error Codes: | See API Response Codes |
| Events Triggered: | None |
| Release: | 8.5(1) |
| Notes or Examples: | Example |