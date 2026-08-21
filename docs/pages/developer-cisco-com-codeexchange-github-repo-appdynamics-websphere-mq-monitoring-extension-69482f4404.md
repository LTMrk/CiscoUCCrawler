---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-websphere-mq-monitoring-extension-69482f4404
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/websphere-mq-monitoring-extension
retrieved_at: 2026-08-21T06:02:13.754269+00:00
---

# AppDynamics Monitoring Extension for use with IBM WebSphere MQ

## Use case

Websphere MQ, formerly known as MQ (message queue) series, is an IBM standard for program-to-program messaging across multiple platforms.

The WebSphere MQ monitoring extension can monitor multiple queues managers and their resources, namely queues, topics, channels and listeners The metrics are extracted out using the PCF command messages .

The metrics for queue manager, queue, topic, channel and listener can be configured.

The MQ Monitor currently supports IBM Websphere MQ version 7.x, 8.x and 9.x.

## Prerequisites

Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met.

Download and install Apache Maven which is configured with Java 8 to build the extension artifact from source. You can check the java version used in maven using command mvn -v or mvn --version . If your maven is using some other java version then please download java 8 for your platform and set JAVA_HOME parameter before starting maven.

If this extension is configured for CLIENT transport type

- Please make sure the MQ's host and port is accessible.

- Credentials of user with correct access rights would be needed in config.yml (Access Permissions section) .

- If the hosting OS for IBM MQ is Windows, Windows user credentials will be needed.

### Dependencies

The extension has a dependency on the following jar's depending on IBM MQ version:

- v8.0.0 and above

```
com.ibm.mq.allclient.jar
```

- For other versions

```
com.ibm.mq.commonservices.jar
com.ibm.mq.jar
com.ibm.mq.jmqi.jar
com.ibm.mq.headers.jar
com.ibm.mq.pcf.jar
dhbcore.jar
connector.jar
```

These jar files are typically found in /opt/mqm/java/lib on a UNIX server but may be found in an alternate location depending upon your environment.

In case of CLIENT transport type, IBM MQ Client must be installed to get the MQ jars. To download IBM MQ Client jars, see here

## Installation

- To build from source, clone this repository using git clone <repoUrl> command.

- Create a lib folder in "websphere-mq-monitoring-extension" and copy the following jars in the websphere-mq-monitoring-extension/lib folder. (These jars are shipped with your Websphere MQ product itself)

- For MQ v8.0.0 and above

```
com.ibm.mq.allclient.jar
```

- For other versions, please comment the "com.ibm.mq.allclient" dependency in pom.xml and uncomment the following dependencies. Then add these dependencies in websphere-mq-monitoring-extension/lib folder

```
com.ibm.mq.commonservices.jar
com.ibm.mq.jar
com.ibm.mq.jmqi.jar
com.ibm.mq.headers.jar
com.ibm.mq.pcf.jar
dhbcore.jar
connector.jar
```

- Run mvn clean install from websphere-mq-monitoring-extension directory. This will produce a WMQMonitor-<version>.zip in target directory.

- Unzip contents of WMQMonitor-<version>.zip file and copy to "<MachineAgentHome_Dir>/monitors" directory. Please place the extension in the Please place the extension in the "monitors" directory of your Machine Agent installation directory. Do not place the extension in the "extensions" directory of your Machine Agent installation directory.

- Binding : Requires WMQ Extension to be deployed in machine agent on the same machine where WMQ server is installed.

- Client : In this mode, the WMQ extension is installed on a different host than the IBM MQ server. Please install the IBM MQ Client for this mode to get the necessary jars as mentioned previously.

```
<classpath>websphere-mq-monitoring-extension.jar;/opt/mqm/java/lib/com.ibm.mq.allclient.jar</classpath>
```

```
<classpath>websphere-mq-monitoring-extension.jar;/opt/mqm/java/lib/com.ibm.mq.jar;/opt/mqm/java/lib/com.ibm.mq.jmqi.jar;/opt/mqm/java/lib/com.ibm.mq.commonservices.jar;/opt/mqm/java/lib/com.ibm.mq.headers.jar;/opt/mqm/java/lib/com.ibm.mq.pcf.jar;/opt/mqm/java/lib/connector.jar;/opt/mqm/java/lib/dhbcore.jar</classpath>
```

- If you plan to use Client transport type, create a channel of type server connection in each of the queue manager you wish to query.

- Edit the config.yml file.  An example config.yml file follows these installation instructions.

- Restart the Machine Agent.

## Configuration

Note : Please make sure to not use tab (\t) while editing yaml files. You may want to validate the yaml file using a yaml validator Configure the monitor by editing the config.yml file in /monitors/WMQMonitor/ .

```
metricPrefix: "Server|Component:100|Custom Metrics|WebsphereMQ|"
```

More details around metric prefix can be found here .

```
numberOfThreads: 20
```

```
queueManagers:
   - displayName: ""
     # displayName (optional). This will be your QM name that will show up in AppD metric path. If empty, name (below) will show up.
     host: "192.168.57.104"
     port: 1414
     #Actual name of the queue manager
     name: "TEST_QM_1"
     #Channel name of the queue manager
     channelName: "SYSTEM.ADMIN.SVRCONN"
     #The transport type for the queue manager connection, the default is "Bindings" for a binding type connection
     #For bindings type connection WMQ extension (i.e machine agent) need to be on the same machine on which WebbsphereMQ server is running
     #for client type connection change it to "Client".
     transportType: "Client"
     ##for user access level, please check "Access Permissions" section on the extensions page, no need to provide credentials in case of bindings transport type, it is only applicable for client type
     username: "hello"
     password: "hello"

     #This is the timeout on queue metrics threads.Default value is 20 seconds. No need to change the default
     #Unless you know what you are doing.
     #queueMetricsCollectionTimeoutInSeconds: 20
     #channelMetricsCollectionTimeoutInSeconds: 20
     #topicsMetricsCollectionTimeoutInSeconds: 20
     
     queueFilters:
         #An asterisk on its own matches all possible names.
         include: ["*"]
         #exclude all queues that starts with SYSTEM or AMQ.
         exclude:
            - type: "STARTSWITH"
              values: ["SYSTEM","AMQ"]

     channelFilters:
         #An asterisk on its own matches all possible names.
         include: ["*"]
         #exclude all queues that starts with SYSTEM.
         exclude:
            - type: "STARTSWITH"
              values: ["SYSTEM"]
     listenerFilters:
         #Can provide complete channel name or generic names. A generic name is a character string followed by an asterisk (*),
         #for example ABC*, and it selects all objects having names that start with the selected character string.
         #An asterisk on its own matches all possible names.
         include: ["*"]
         exclude:
            #type value: STARTSWITH, EQUALS, ENDSWITH, CONTAINS
            - type: "STARTSWITH"
            #The name of the queue or queue name pattern as per queue filter, comma separated values
              values: ["SYSTEM"]
 
     topicFilters:
         # For topics, IBM MQ uses the topic wildcard characters ('#' and '+') and does not treat a trailing asterisk as a wildcard
         # https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_7.5.0/com.ibm.mq.pla.doc/q005020_.htm
         include: ["#"]
         exclude:
              #type value: STARTSWITH, EQUALS, ENDSWITH, CONTAINS
            - type: "STARTSWITH"
              #The name of the queue or queue name pattern as per queue filter, comma separated values
              values: ["SYSTEM","$SYS"]

   - host: "102.138.37.105"
     port: 1414
     #Actual name of the queue manager
     name: "TEST_QM_2"
     #Channel name of the queue manager
     channelName: "SYSTEM.ADMIN.SVRCONN"
     #The transport type for the queue manager connection, the default is "Bindings" for a binding type connection
     #For bindings type connection WMQ extension (i.e machine agent) need to be on the same machine on which WebbsphereMQ server is running
     #for client type connection change it to "Client".
     transportType: "Client"
     ##for user access level, please check "Access Permissions" section on the extensions page, no need to provide credentials in case of bindings transport type, it is only applicable for client type
     username: "hello"
     password: "hello"
     #This is the timeout on queue metrics threads.Default value is 20 seconds. No need to change the default
     #Unless you know what you are doing.
     queueMetricsCollectionTimeoutInSeconds: 20

     queueFilters:
         #Matches all queues  that starts with TACA..
         include: ["TACA*"]
         #exclude all queues that starts with SYSTEM or AMQ.
         exclude:
            - type: "STARTSWITH"
              values: ["SYSTEM","AMQ"]

     channelFilters:
         #An asterisk on its own matches all possible names.
         include: ["*"]
         #exclude all queues that starts with SYSTEM.
         exclude:
            - type: "STARTSWITH"
              values: ["SYSTEM"]
```

```
mqMetrics:
  # This Object will extract queue manager metrics
  - metricsType: "queueMgrMetrics"
    metrics:
      include:
        - Status:
            alias: "Status"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACF_Q_MGR_STATUS"
        - ConnectionCount:
            alias: "ConnectionCount"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACF_CONNECTION_COUNT"
      
  # This Object will extract queue metrics
  - metricsType: "queueMetrics"
    metrics:
      include:
        - MaxQueueDepth:
            alias: "Max Queue Depth"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_MAX_Q_DEPTH"
            ibmCommand: "MQCMD_INQUIRE_Q"
          
        - CurrentQueueDepth:
            alias: "Current Queue Depth"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_CURRENT_Q_DEPTH"
            ibmCommand: "MQCMD_INQUIRE_Q"
          
        - OpenInputCount:
            alias: "Open Input Count"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_OPEN_INPUT_COUNT"
            ibmCommand: "MQCMD_INQUIRE_Q"
          
        - OpenOutputCount:
            alias: "Open Output Count"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_OPEN_OUTPUT_COUNT"
            ibmCommand: "MQCMD_INQUIRE_Q"

        - OldestMsgAge:
            alias: "OldestMsgAge"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACF_OLDEST_MSG_AGE"
            ibmCommand: "MQCMD_INQUIRE_Q_STATUS"
            aggregationType: "OBSERVATION"
            timeRollUpType: "CURRENT"
            clusterRollUpType: "INDIVIDUAL"

        - OnQTime:
            alias: "OnQTime"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACF_Q_TIME_INDICATOR"
            ibmCommand: "MQCMD_INQUIRE_Q_STATUS"
            aggregationType: "OBSERVATION"
            timeRollUpType: "CURRENT"
            clusterRollUpType: "INDIVIDUAL"

        - UncommittedMsgs:
            alias: "UncommittedMsgs"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACF_UNCOMMITTED_MSGS"
            ibmCommand: "MQCMD_INQUIRE_Q_STATUS"

        - HighQDepth:
            alias: "HighQDepth"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_HIGH_Q_DEPTH"
            ibmCommand: "MQCMD_RESET_Q_STATS"

        - MsgDeqCount:
            alias: "MsgDeqCount"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_MSG_DEQ_COUNT"
            ibmCommand: "MQCMD_RESET_Q_STATS"

        - MsgEnqCount:
            alias: "MsgEnqCount"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_MSG_ENQ_COUNT"
            ibmCommand: "MQCMD_RESET_Q_STATS"

      
  # This Object will extract channel metrics
  - metricsType: "channelMetrics"
    metrics:
      include:
        - Messages:
            alias: "Messages"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_MSGS"
          
        - Status:
            alias: "Status"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_CHANNEL_STATUS"  #http://www.ibm.com/support/knowledgecenter/SSFKSJ_7.5.0/com.ibm.mq.ref.dev.doc/q090880_.htm
          
        - ByteSent:
            alias: "Byte Sent"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_BYTES_SENT"
          
        - ByteReceived:
            alias: "Byte Received"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_BYTES_RECEIVED"
          
        - BuffersSent:
            alias: "Buffers Sent"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_BUFFERS_SENT"
          
        - BuffersReceived:
            alias: "Buffers Received"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_BUFFERS_RECEIVED"

  - metricsType: "listenerMetrics"
    metrics:
      include:
        - Status:
            alias: "Status"
            ibmConstant: "com.ibm.mq.constants.CMQCFC.MQIACH_LISTENER_STATUS"

  # This Object will extract topic metrics
  - metricsType: "topicMetrics"
    metrics:
      include:
        - PublishCount:
            alias: "Publish Count"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_PUB_COUNT"
            ibmCommand: "MQCMD_INQUIRE_TOPIC_STATUS"
        - SubscriptionCount:
            alias: "Subscription Count"
            ibmConstant: "com.ibm.mq.constants.CMQC.MQIA_SUB_COUNT"
            ibmCommand: "MQCMD_INQUIRE_TOPIC_STATUS"
```

- To run the extension at a frequency > 1 minute, please configure the taskSchedule section. Refer to the Task Schedule doc for details.

### Extension Working - Internals

This extension extracts metrics through PCF framework . A complete list of PCF commands are listed here Each queue manager has an administration queue with a standard queue name and the extension sends PCF command messages to that queue. On Windows and Unix platforms, the PCF commands are sent is always sent to the SYSTEM.ADMIN.COMMAND.QUEUE queue. More details about that is mentioned here

By default, the PCF responses are sent to the SYSTEM.DEFAULT.MODEL.QUEUE. Using this queue causes a temporary dynamic queue to be created. You can override the default here by using the modelQueueName and replyQueuePrefix fields in the config.yml. More details mentioned here

### Access Permissions

If you are in Bindings mode, please make sure to start the MA process under a user which has the following permissions on the broker. Similarly, for Client mode, please provide the user credentials in config.yml which have permissions listed below.

The user connecting to the queueManager should have the inquire, get, put (since PCF responses cause dynamic queues to be created) permissions. For metrics that execute MQCMD_RESET_Q_STATS command, chg permission is needed.

### SSL Support

Configure the IBM SSL Cipher Suite in the config.yml. Note that, to use some CipherSuites the unrestricted policy needs to be configured in JRE. Please visit this link for more details. For Oracle JRE, please update with JCE Unlimited Strength Jurisdiction Policy . The download includes a readme file with instructions on how to apply these files to JRE

Please add the following JVM arguments to the MA start up command or script.

-Dcom.ibm.mq.cfg.useIBMCipherMappings=false (If you are using IBM Cipher Suites, set the flag to true. Please visit this link for more details. )

To configure SSL, the MA's trust store and keystore needs to be setup with the JKS filepath. They can be passed either as Machine Agent JVM arguments or configured in config.yml (sslConnection)

a. Machine Agent JVM arguments as follows:

-Djavax.net.ssl.trustStore=<PATH_TO_JKS_FILE> -Djavax.net.ssl.trustStorePassword=<PASS> -Djavax.net.ssl.keyStore=<PATH_TO_JKS_FILE> -Djavax.net.ssl.keyStorePassword=<PASS>

b. sslConnection in config.yml, configure the trustStorePassword or trustStoreEncryptedPassword based on Credentials Encryption. Same holds for keyStore configuration as well.

```
sslConnection:
  trustStorePath: ""
  trustStorePassword: ""
  trustStoreEncryptedPassword: ""

  keyStorePath: ""
  keyStorePassword: ""
  keyStoreEncryptedPassword: ""
```

## Metrics

The metrics will be reported under the tree Application Infrastructure Performance|$TIER|Custom Metrics|WebsphereMQ

### QueueManagerMetrics

### QueueMetrics

#### QueueMetrics

This metrics below are only for the local queues, as these metrics are irrelevant for other queues .

#### QueueStatusMetrics

#### ResetQueueStatistics

The following metrics are extracted using the MQCMD_RESET_Q_STATS command which would reset the stats on the QM for that queue.

### ChannelMetrics

### ListenerMetrics

### TopicMetrics

## Credentials Encryption

Please visit this page to get detailed instructions on password encryption. The steps in this document will guide you through the whole process.

## Extensions Workbench

Workbench is an inbuilt feature provided with each extension in order to assist you to fine tune the extension setup before you actually deploy it on the controller. Please review the following document on How to use the Extensions WorkBench

## Troubleshooting

Please follow the steps listed in this troubleshooting-document in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.

Error Completion Code '2', Reason '2495' Normally this error occurs if the environment variables are not set up correctly for this extension to work MQ in Bindings Mode.

If you are seeing Failed to load the WebSphere MQ native JNI library: 'mqjbnd' , please add the following jvm argument when starting the MA.

-Djava.library.path=<path to libmqjbnd.so> For eg. on Unix it could -Djava.library.path=/opt/mqm/java/lib64 for 64-bit or -Djava.library.path=/opt/mqm/java/lib for 32-bit OS

Sometimes you also have run the setmqenv script before using the above jvm argument to start the machine agent.

. /opt/mqm/bin/setmqenv -s

For more details, please check this doc

This might occour due to various reasons ranging from incorrect installation to applying ibm fix packs but most of the time it happens when you are trying to connect in Bindings mode and machine agent is not on the same machine on which WMQ server is running. If you want to connect to WMQ server from a remote machine then connect using Client mode.

Another way to get around this issue is to avoid using the Bindings mode. Connect using CLIENT transport type from a remote box.

Error Completion Code '2', Reason '2035' This could happen for various reasons but for most of the cases, for Client mode the user specified in config.yml is not authorized to access the queue manager. Also sometimes even if userid and password are correct, channel auth (CHLAUTH) for that queue manager blocks traffics from other ips, you need to contact admin to provide you access to the queue manager. For Bindings mode, please make sure that the MA is owned by a mqm user. Please check this doc

MQJE001: Completion Code '2', Reason '2195' This could happen in Client mode. Please make sure that the IBM MQ dependency jars are correctly referenced in classpath of monitor.xml

MQJE001: Completion Code '2', Reason '2400' This could happen if unsupported cipherSuite is provided or JRE not having/enabled unlimited jurisdiction policy files. Please check SSL Support section.

If you are seeing "NoClassDefFoundError" or "ClassNotFound" error for any of the MQ dependency even after providing correct path in monitor.xml, then you can also try copying all the required jars in WMQMonitor (MAHome/monitors/WMQMonitor) folder and provide classpath in monitor.xml like below

```
<classpath>websphere-mq-monitoring-extension.jar;com.ibm.mq.allclient.jar</classpath>
```

OR

```
<classpath>websphere-mq-monitoring-extension.jar;com.ibm.mq.jar;com.ibm.mq.jmqi.jar;com.ibm.mq.commonservices.jar;com.ibm.mq.headers.jar;com.ibm.mq.pcf.jar;connector.jar;dhbcore.jar</classpath>
```

## Contributing

Always feel free to fork and contribute any changes directly via GitHub .

## Version

Note : While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to AppDynamics’ maintenance and support policy . Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.

How do you like this sample code?

| Metric Name | Description |
|---|---|
| Status | 1 - starting, 2 - running, 3 - quiescing |

| Metric Name | Description |
|---|---|
| MaxQueueDepth | Maximum queue depth |
| CurrentQueueDepth | Current queue depth |
| OpenInputCount | Number of MQOPEN calls that have the queue open for input |
| OpenOutputCount | Number of MQOPEN calls that have the queue open for output |

| Metric Name | Description |
|---|---|
| OldestMsgAge | Age of the oldest message |
| OnQTime | Indicator of the time that messages remain on the queue |
| UncommittedMsgs | The number of uncommitted changes (puts and gets) pending for the queue |

| Metric Name | Description |
|---|---|
| HighQDepth | Maximum number of messages on a queue |
| MsgDeqCount | Number of messages dequeued |
| MsgEnqCount | Number of messages enqueued |

| Metric Name | Description |
|---|---|
| Messages | Number of messages sent or received, or number of MQI calls handled |
| Status | 1 - binding, 2 - starting, 3 - running, 4 - stopping, 5 - retrying, 6 - stopped, 7 - requesting, 8 - paused, 13 - initializing, 14 - switching |
| ByteSent | Number of bytes sent |
| ByteReceived | Number of bytes received |
| BuffersSent | Number of buffers sent |
| BuffersReceived | Number of buffers received |

| Metric Name | Description |
|---|---|
| Status | 1 - starting, 2 - running, 3 - stopping |

| Metric Name | Description |
|---|---|
| PublishCount | The number of applications currently publishing to the topic. |
| SubscriptionCount | The number of subscribers for this topic string, including durable subscribers who are not currently connected. |

| Name | Version |
|---|---|
| Extension Version | 7.0.5 |
| IBM MQ Version tested On | 7.x, 8.x, 9.x and Windows, Unix, AIX |
| Last Update | 07/06/2021 |
| List of Changes | Change Log |