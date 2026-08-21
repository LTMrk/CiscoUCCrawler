---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-redis-monitoring-extension-fb6e146cb4
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/redis-monitoring-extension
retrieved_at: 2026-08-21T06:01:55.781286+00:00
---

# Redis Monitoring Extension for AppDynamics

## Use Case

Redis is an in memory key-value data store used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.

The Redis monitoring extension can monitor multiple Redis servers and display the statistics in AppDynamics Metric Browser.

## Prerequisites

- Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met.

- Download and install Apache Maven which is configured with Java 8 to build the extension artifact from source. You can check the java version used in maven using command mvn -v or mvn --version . If your maven is using some other java version then please download java 8 for your platform and set JAVA_HOME parameter before starting maven.

- This extension creates a java client to the Redis server that needs to be monitored. So the Redis server that has to be monitored, should be available for access from the machine that has the extension installed.

## Installation

- Clone the "redis-monitoring-extension" repo using git clone <repoUrl> command.

- Run 'mvn clean install' from "redis-monitoring-extension".

- Unzip the RedisMonitor-<version>.zip from target directory into the "<MachineAgent_Dir>/monitors" directory.

- Edit the file config.yml located at <MachineAgent_Dir>/monitors/RedisMonitor referring to configurations section below.

- Restart the Machine Agent.

## Recommendations

It is recommended that a single Redis monitoring extension be used to monitor multiple Redis servers belonging to a single cluster.

## Configuring the extension using config.yml

Configure the Redis monitoring extension by editing the config.yml file in <MACHINE_AGENT_HOME>/monitors/RedisMonitor/

Configure the "tier" under which the metrics need to be reported. This can be done by changing the value of <TIER NAME OR TIER ID> in metricPrefix: "Server|Component: <TIER NAME OR TIER ID> |Custom Metrics|Redis".

For example,

```
metricPrefix: "Server|Component:Extensions tier|Custom Metrics|Redis"
```

More details around metric prefix can be found here

Configure the Redis instances by specifying the name(required), host(required), port(required) of the Redis instance, password (only if authentication enabled), encryptedPassword(only if password encryption required).

For example,

```
#Add your list of Redis servers here.
 servers:
   - name: "Server1"
     host: "localhost"
     port: "6379"
     password: ""
     encryptedPassword: ""
   - name: "Server2"
     host: "localhost"
     port: "6380"
     password: ""
     encryptedPassword: ""
```

Configure the encyptionKey for encryptionPasswords(only if password encryption required).

For example,

```
#Encryption key for Encrypted password.
encryptionKey: "axcdde43535hdhdgfiniyy576"
```

Configure the numberOfThreads(only if the number of Redis servers need to be monitored is greater than 7).

For example,

If number Redis servers that need to be monitored is 10, then number of threads required is 10 * 3 = 30

```
numberOfThreads: 30
```

Configure the metrics section.

For configuring the metrics, the following properties can be used:

For example,

```
- total_connections_received:  #Total number of connections accepted by the server
    alias: "connectionsReceived"
    multiplier: 1
    aggregationType: "SUM"
    timeRollUpType: "CURRENT"
    clusterRollUpType: "INDIVIDUAL"
    delta: true
- role:  #Role of Redis server(master or slave)
    convert:
      master: 1
      slave: 0
```

All these metric properties are optional, and the default value shown in the table is applied to the metric(if a property has not been specified) by default.

## Metrics

This extension uses INFO command to fetch metrics from Redis server. Some of the metrics are listed below:

```
* Clients: connected_clients, blocked_clients
      * Memory: used_memory, used_memory_rss, used_memory_peak, used_memory_lua, mem_fragmentation_ratio
      * Stats: total_connections_received, total_commands_processed, keyspace_hits, keyspace_misses, keyspace_hit_ratio
      * Persistence: rdb_changes_since_last_save, aof_last_rewrite_time_sec
      * replication: role (MASTER:1, SLAVE:0), connected_slaves
      * CPU: used_cpu_sys, used_cpu_user, used_cpu_sys_children, used_cpu_user_children
```

This extension also uses SLOWLOG to fetch metrics from Redis server.

```
* no_of_new_slow_logs -> This metric represents the number of new logs that were recorded as slowlogs(log queries that exceeded a specified
                               execution time) since the extension has recorded in its previous run.
        To use this metric, the "slowlog-log-slower-than" config parameter has to be set for the Redis server.
```

In addition to the above metrics, there is a metric called "connectionStatus" with a value 0 when the connection to Redis server failed and 1 when the connection to the Redis server is successful.

## Credentials Encryption

Please visit this page to get detailed instructions on password encryption. The steps in this document will guide you through the whole process.

## Extensions Workbench

Workbench is an inbuilt feature provided with each extension in order to assist you to fine tune the extension setup before you actually deploy it on the controller. Please review the following document on How to use the Extensions WorkBench

## Troubleshooting

Please follow the steps listed in this troubleshooting-document in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.

## Contributing

Always feel free to fork and contribute any changes directly here on GitHub .

## Version

Note : While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to AppDynamics’ maintenance and support policy . Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.

How do you like this sample code?

| Property | Default value | Possible values | Description |
|---|---|---|---|
| alias | metric name | Any string | The substitute name to be used in the metric browser instead of metric name. |
| aggregationType | "AVERAGE" | "AVERAGE", "SUM", "OBSERVATION" | Aggregation qualifier |
| timeRollUpType | "AVERAGE" | "AVERAGE", "SUM", "CURRENT" | Time roll-up qualifier |
| clusterRollUpType | "INDIVIDUAL" | "INDIVIDUAL", "COLLECTIVE" | Cluster roll-up qualifier |
| multiplier | 1 | Any number | Value with which the metric needs to be multiplied. |
| convert | null | Any key value map | Set of key value pairs that indicates the value to which the metrics need to be transformed. eg: UP:0, DOWN:1 |
| delta | false | true, false | If enabled, gives the delta values of metrics instead of actual values. |

|  |  |
|---|---|
| Current version | 3.0.1 |
| Redis version tested on | 3.9, 4.0.8 |
| Last Update | 22/01/2021 |
| Changes list | ChangeLog |