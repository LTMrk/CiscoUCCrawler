---
doc_id: developer-cisco-com-site-curri-learn-how-to-monitor-performance-5917697414
source_url: https://developer.cisco.com/site/curri/learn/how-to/monitor-performance/
retrieved_at: 2026-09-07T14:14:51.588479+00:00
---

# How to Monitor Performance

### Does CURRI affect Unified CM performance?

Unified CM experiences some degree of performance degradation if it queries route servers for a majority of incoming calls.

The performance degradation depends on the following factors:

- Response time from route servers

- Network latency for call routing requests and responses

Slow response or network latency adds delay to the post-dial silence for a call. Testing shows that when the response time from the route server is longer than 50ms (RTT), there is a 15% degradation in the maximum call rate when all calls are subject to a Route Request/Response

### How can I monitor Unified CM performance?

For external call control, performance monitoring counters display under the External Call Control object and the Cisco CallManager object in RTMT.

Call-related performance counters are in the Cisco CallManager object. These can be monitored to see how the External Call Control enabled calls are behaving.

- ExternalCallControlEnabledCallAttempted : Total number of External Call Control-enabled calls

- ExternalCallControlEnabledCallComplete : Total number of External Call Control-enabled calls that are answered

- ExternalCallControlEnabledFailureTreatmentApplied : Total number of External Call Control-enabled calls that failure treatments were applied

Here is an example of the Call-related counters being monitored RTMT

Server and connection related performance counters are found under the External Call Control object. These can be used to monitor performance of Route Servers and their connections.

- ConnectionsActiveToPDPServer : The number of active connections to Route Server (route decision point)

- ConnectionsLostToPDPServer: The total number of times that Unified CM has lost connections to the Route Server

- PDPServersInService: The total number of active Route Servers

- PDPServersOutOfService: The total number of times that Route Servers are out of service

- PDPServersTotal: The total number of Route Servers provisioned in Unified CM

Here is an example of the External Call Control counters being monitored RTMT

### Alarms

The following alarms may be raised:

Note: PDP - Route Decision Point

- ConnectionFailureToPDP [ERROR_ALARM] - Unified CM failed to connect to the Route Decision Point

- ConnectionToPDPInService [INFO_ALARM] - Connection to route server is restored

- AwaitingResponseFromPDPTimeout [ERROR_ALARM] - Unified CM has not received a response from the web service within a specified timer

- ErrorParsingDirectiveFromPDP [ERROR_ALARM] - Unified CM failed to parse a call routing directive and other mandatory parameters

- ErrorParsingResponseFromPDP [WARNING_ALARM] - Unified CM has errors when parsing the optional elements or attributes in the call routing response

- FailureResponseFromPDP [ERROR_ALARM] - Unified CM received a 4xx or a 5xx response

- CallAttemptBlockedByRoute [WARNING_ALARM] - Route Decision Point blocks a call and the reason is "Route Violation"