---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-apigee-monitoring-extension-67a75c210f
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/apigee-monitoring-extension
retrieved_at: 2026-08-21T06:01:51.504034+00:00
---

# Apigee Monitoring Extension for AppDynamics

#### Tested with Apigee Edge

## Use Case

Apigee is an API management platform that enables developers and businesses to design, secure, deploy, monitor, and scale APIs. This extension makes it possible for AppDynamics customers to monitor the performance of Apigee API proxies.

The Apigee monitoring extension help AppDynamics customers to quickly isolate the root cause of performance issues - whether it is Apigee's overhead and/or the backend (target) service. The extension monitors API proxy performance metrics such as Total Error count, Traffic rate, Response Time and Error response codes. Also, it has an optional built-in feature to analyse and report on API proxy performance metrics using the AppDynamics BiQ platform - this gives customers the extra flexibility of slicing and dicing API proxy and target errors for reporting and continues enhancements purposes.

The extension now supports monitoring for multiple Apigee instances, environments and orgs - in any combination of your choice.

The following Apigee proxy metrics are monitored by this AppDynamics monitoring solution:

- Response Time: Total number of milliseconds it took to respond to a call. This time includes the Apigee API proxy overhead and your target server time.

- Target Response Time: Number of milliseconds it took your target server or service to respond to a call. This number tells you how your own services are behaving.

- Min and Max of Target Response Time: The Minimum and Maximum Target Response Time over in the given query period

- Overall Average Response Time: Overall Average Response Time for all proxies - it's calculated by summing the response times and dividing by the number of proxies available at the time.

- Request Processing Latency: Number of milliseconds from the time when a call reaches the selected API proxy to the time when Apigee sends the call to your target server.

- Min and Max of Processing Latency: The Minimum and Maximum Processing Latency values over the query period

- Traffic: The number of recorded API requests for each API proxy

- Error: The total number of times API proxies failed over the specified period. Proxy failure can occur when a policy fails or when there's a runtime

- Policy Error: The total number of times API proxy policy failed

- Error Count Sum: Summation of errors for all API proxies

- 401 Count: The total number of 401 HTTP Response Code for each API proxy

- 403 Count: The total number of 403 HTTP Response Code for each API proxy

- 4XX Count: The total number of all other 4XX HTTP Response Code for each API proxy but excluding the 401 and 403

- Total 4XX: Summation of 4XX HTTP Response Codes in all API proxies

- 502 Count: The total number of 502 HTTP Response Code for each API proxy

- 503 Count: The total number of 503 HTTP Response Code for each API proxy

- 504 Count: The total number of 504 HTTP Response Code for each API proxy

- 5XX Count: The total number of all other 5XX HTTP Response Code for each API proxy but excluding the 502, 503 and 404

- Total 5XX: Summation of 5XX HTTP Response Codes for all API proxies

## Prerequisite

- This extension works only with the standalone Java machine agent.

- Analytics module must be enabled in Apigee

- Create a service account in Apigee that has read access to ALL the API proxies you would like to monitor in AppDynamics

- jq must be installed on the server running the machine agent - https://stedolan.github.io/jq/download/

- AppDynamics BiQ license (optional)

### Installation

- Unzip the attached file into $MACHINE_AGENT_HOME/monitors

- Using your favourite text editor, open config.json and fill in the configuration properties:

- Version 2.0 and above of this extension support monitoring of multiple Apigee instances, environments or organisations. To do this, add an element to the connection details array as shown below. Note, use a unique server_friendly_name for each entry.

```
{
      "host_url": "https://localhost:8080",
      "org": "customer1",
      "env": "prod",
      "server_friendly_name": "Onpremise-Sever001-DC1",
      "username": "username",
      "use_proxy_filter": false,
      "is_password_encoded": false,
      "password": "password"
    }
```

- There are 2 types of APIGEE instances, SaaS and onprem. If ONPREM APIGEE instance then the Machine Agent needs to be runnning on a server in the same timezone as the APIGEE OnPrem Server. If it is onprem , then set the to value in the config.json to:-

"apigee_timezone": "onprem",

This means the API datetime query to the APIGEE API will be set in server's 'local-time'.

All APIGEE SaaS environments run as UTC time, so if you are monitoring a SaaS instance then set the value to:-

"apigee_timezone": "saas",

which will switche the API query datetime to UTC time.

Failure to set these correctly dpending on APIGEE environment will mean you are querying a time that is in the future or the worng date.

We've added the ability to encode the password for added security. This extension supports base64 password encoding. For example:

echo "password" | base64

will output base64 encode text, which can be used in the config.json instead of the plain text password

If you are using this feature then set the following param in the config.json as:-

"is_password_encoded": true,

or else leave set to false so password is clear text.

If use_proxy_filter is set to true, list the target proxies in the apipproxy.conf file - one item per line.

Note: user_proxy_filter, when set to true will ONLY send API performance metrics for the predefined proxies in the apiproxy.conf file. If set to false, performance data for ALL apigee proxies in the org and env will be collected.

- Test it: ./apigee_monitor.sh

- If everything is OK, you should see an output in stdout that is similar to this:

```
sending request to Apigee.... 
Using un-filtered request - collecting all proxy information
curl https://api.enterprise.apigee.com/v1/organizations/appd/environments/prod/stats/apiproxy,response_status_code,target_response_code?_optimized=js&realtime=true&limit=120&select=sum(message_count),avg(total_response_time),avg(target_response_time),avg(request_processing_latency),sum(is_error)&sort=DESC&sortby=sum(message_count),avg(total_response_time),sum(is_error)&timeRange=01/11/2020+18:13:43~01/11/2020+18:15:43&timeUnit=minute&tsAscending=true -u israelo@appd.com:******
==> 200
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Availability, value=1
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Total Message Count, value=16
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Total Error Count, value=2
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Total Policy Errors, value=0
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Total Target Errors, value=0
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Global Average Response Time, value=7222
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Average Total Response Time, value=5822
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Minimum Total Response Time, value=125
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Maximum Total Response Time, value=55145
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Global Request Processing Latency, value=1
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Average Request Processing Latency, value=1
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Minimum Request Processing Latency, value=0
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Maximum Request Processing Latency, value=2
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Global Average Target Response Time, value=7216
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Average Target Response Time, value=5815
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Minimum Target Response Time, value=120
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|Maximum Target Response Time, value=55142

Processing 4xx metrics for AppDynamics
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|4XX Count, value=2
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|Total 5XX, value=2

Processing 5xx metrics for AppDynamics
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|OAuth_v1|5XX Count, value=1
name=Server|Component:<tier-name>|Custom Metrics|Apigee|Onpremise-DC1|Proxies|prod|Total 5XX, value=1
```

Do not proceed until you get an output similar to the above.

- Restart the machine agent

Note: The Global* metric is synonymous with AppDynamics baseline metric. We recommend that you use the non-Global metrics for your health rule metrics.

### BiQ Output

If BiQ is enabled, you can now slice and dice Apigee metrics in many dimensions to suit your business needs, for example:

SELECT * FROM apigee_metrics WHERE total_response_time > 5 and four_xx > 0 and environment="prod" SINCE 2 hours

### Custom Dashboard

The custom dashboard below shows 2 API proxy performance metrics - with their respective SLAs

Metrics are located in Application Infrastructure Performance | Tier_NAME| Custom Metrics | Apigee |*

### Troubleshooting

Review $MACHINE_AGENT_HOME/logs/apigee-monitor.log

Check the analytics page in Apigee and ensure you can see performance data for the proxy APIs in the correct org and env

Send a manual curl request to your apigee instance to verify it's working

If you need to contact support, reload the Apigee analytics page, save HTTP HAR file and attach it to the support case.

### Contribution guidelines

- Fork and submit PR

How do you like this sample code?

| Config Property Name | Description |
|---|---|
| host_url | Apigee host url, including the port number if required. |
| query_interval_in_secs | Determines what interval in time is collected in the APIGEE API query |
| apigee_query_delay_secs | APIGEE states it may take upto 10-12+ minutes for their analytic metric data to be available. This determines how far back you will offset to collect so to guarantee the data is available in Apigee |
| apigee_timezone | To determine if the APIGEE datetime query is in localtime (APIGEE onprem) to the server where the machine agent is or in UTC (APIGEE saas) |
| metric_prefix | Define metrics prefix, for example:  `Server |
| org | Select the organization that contains the proxies you would like to monitor |
| env | Select the environment that contains the proxies you would like to monitor. prod, Dev, Prod, etc. |
| server_friendly_name | An free text indicator that best describes your Apigee environment, org, or environment. use - or _ to separate words, not spaces |
| username | Username of the read-only service account |
| is_password_encoded | If set to true, the monitoring extension will expect the password to be encoded as base64 |
| password | Password of the read-only service account |
| use_proxy_filter | If set to true, the monitoring extension will only collect metrics for proxies that are defined in the apipproxy.conf file |
| enable_BiQ | If set to true, the monitoring extension will send proxy and target response codes to BiQ platform. This requires BiQ license |
| analytics_endpoint | This is the analytics endpoint of your controller. This differs depending on the location of your controller. Please refer to this doc . |
| global_account_name | You can get the global account name to use from the License page |
| analytics_key | Create the analytics API Key by following the instruction in this doc .  Grant Manage, Query and Publish permissions to Custom |
| proxy_url | Define proxy host if in use, otherwise leave blank. |
| proxy_port | Define proxy port if proxy_url is not blank |
| schema_name | Define the custom analytics schema name. Schema names must be unique per controller |