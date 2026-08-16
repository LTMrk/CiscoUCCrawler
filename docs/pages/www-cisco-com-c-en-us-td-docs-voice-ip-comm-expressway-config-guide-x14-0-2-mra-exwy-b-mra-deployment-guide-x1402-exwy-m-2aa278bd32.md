---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-2-mra-exwy-b-mra-deployment-guide-x1402-exwy-m-2aa278bd32
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-2/mra/exwy_b_mra-deployment-guide-x1402/exwy_m_http-allow-list-formats.html
retrieved_at: 2026-08-16T15:21:50.692200+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.0.2)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.0.2)

Updated: July 23, 2021

Chapter: HTTP Allow List Formats

## Chapter: HTTP Allow List Formats

# HTTP Allow List Formats

This appendix contains information that can be used to generate and test HTTP Allow Lists.

## Allow List Rules File Reference

You can define rules using a CSV file. This topic provides a reference to acceptable data for each rule argument and demonstrates
                              the format of the CSV rules.

Argument index

Parameter name

Required/

Optional

Sample value

0

Url

Required

protocol://host[:port][/path]

Where:

protocol is http or https

host may be a DNS name or IP address

:port is optional, and may only be : followed by one number in the range 0-65535, for example: 8443

/path is optional and must conform to HTTP specification

1

Deployment

Optional

Name of the deployment that uses this rule. Required when you have more than one deployment, otherwise supply an empty argument.

2

Optional

Comma-delimited list of HTTP methods, optionally in double-quotes, for example: "GET,PUT"

3

Optional

exact or prefix . Default is prefix .

4

Optional

Text description of the rule. Enclose with double quotes if there are spaces.

### Example List Rules CSV File

```
Url,Deployment,HttpMethods,MatchType,Description
https://myServer1:8443/myPath1,myDomain1,GET,,"First Rule"
http://myServer2:8000/myPath2,myDomain200,"GET,PUT",exact,
https://myServer3:8080/myPath3,myDomain1,,prefix,"Third Rule"
https://myServer4/myPath4,myDomain1,,prefix,"Fourth Rule"
http://myServer5/myPath5,myDomain1,,prefix,"Fifth Rule"
```

List the parameter names (as shown) in the first line of the file

One rule per line, one line per rule

Separate arguments with commas

Correctly order the rule values as shown in the table above

Enclose values that have spaces in them with double quotes

## Allow List Tests File Reference

You can define tests using a CSV file. This topic provides a reference to acceptable data for each test argument and demonstrates
                              the format of the CSV tests.

Argument index

Parameter name

Required/

Optional

Sample value

0

Url

Required

protocol://host[:port][/path]

Where:

protocol is http or https

host may be a DNS name or IP address

:port is optional, and may only be : followed by one number in the range 0-65535

/path is optional and must conform to HTTP specification

1

ExpectedResult

Required

allow or block . Specifies whether the test expects that the rules should allow or block the specified URL.

2

Deployment

Optional

Name of the deployment to test with this URL. If you omit this argument, the test will use the default deployment.

3

Description

Optional

Text description of the rule. Enclose with double quotes if there are spaces.

4

HttpMethod

Optional

Specify one HTTP method to test for example, PUT . Defaults to GET if not supplied.

### Example List Tests CSV File

```
Url,ExpectedResult,Deployment,Description,HttpMethod
https://myServer1:8443/myPath1,block,"my deployment","a block test",GET
http://myServer2:8000/myPath2,allow,"my deployment","an allow test",PUT
https://myServer4/myPath4,allow,,,GET
http://myServer4/myPath4,block,,,POST
```

List the parameter names (as shown) in the first line

One test per line, one line per test

Separate arguments with commas

Correctly order the test values as shown in the table above

Enclose values that have spaces in them with double quotes

| Argument index | Parameter name | Required/ Optional | Sample value |
|---|---|---|---|
| 0 | Url | Required | protocol://host[:port][/path] Where: protocol is http or https host may be a DNS name or IP address :port is optional, and may only be : followed by one number in the range 0-65535, for example: 8443 /path is optional and must conform to HTTP specification |
| 1 | Deployment | Optional | Name of the deployment that uses this rule. Required when you have more than one deployment, otherwise supply an empty argument. |
| 2 |  | Optional | Comma-delimited list of HTTP methods, optionally in double-quotes, for example: "GET,PUT" |
| 3 |  | Optional | exact or prefix . Default is prefix . |
| 4 |  | Optional | Text description of the rule. Enclose with double quotes if there are spaces. |

| Argument index | Parameter name | Required/ Optional | Sample value |
|---|---|---|---|
| 0 | Url | Required | protocol://host[:port][/path] Where: protocol is http or https host may be a DNS name or IP address :port is optional, and may only be : followed by one number in the range 0-65535 /path is optional and must conform to HTTP specification |
| 1 | ExpectedResult | Required | allow or block . Specifies whether the test expects that the rules should allow or block the specified URL. |
| 2 | Deployment | Optional | Name of the deployment to test with this URL. If you omit this argument, the test will use the default deployment. |
| 3 | Description | Optional | Text description of the rule. Enclose with double quotes if there are spaces. |
| 4 | HttpMethod | Optional | Specify one HTTP method to test for example, PUT . Defaults to GET if not supplied. |