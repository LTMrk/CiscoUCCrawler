---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-aws-rds-monitoring-extension-097d4b932c
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/aws-rds-monitoring-extension
retrieved_at: 2026-08-21T06:02:03.912364+00:00
---

# AWS RDS Monitoring Extension

## Use Case

Captures RDS statistics from Amazon CloudWatch and displays them in the AppDynamics Metric Browser.

## Prerequisite

- If you don't want to provide awsAccessKey and awsSecretKey, please run the extension on EC2 instance and configure Instance Profile by granting below permissions

```
"cloudwatch:GetMetricData",
"cloudwatch:GetMetricStatistics",
"cloudwatch:ListMetrics"
```

Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met.

Download and install Apache Maven which is configured with Java 8 to build the extension artifact from source. You can check the java version used in maven using command mvn -v or mvn --version . If your maven is using some other java version then please download java 8 for your platform and set JAVA_HOME parameter before starting maven.

The extension needs to be able to connect to AWS in order to collect and send metrics. To do this, you will have to either establish a remote connection in between the extension and the product, or have an agent on the same machine running the product in order for the extension to collect and send the metrics.

## Installation

- Clone the "aws-rds-monitoring-extension" repo using git clone <repoUrl> command.

- Run 'mvn clean install' from aws-rds-monitoring-extension

- Copy and unzip AWSRDSMonitor-<version>.zip from 'target' directory into <machine_agent_dir>/monitors/

- Edit config.yaml file in AWSRDSMonitor/conf and provide the required configuration (see Configuration section)

- Restart the Machine Agent.

Please place the extension in the "monitors" directory of your Machine Agent installation directory. Do not place the extension in the "extensions" directory of your Machine Agent installation directory.

## Configuration

Configure the "COMPONENT_ID" under which the metrics need to be reported. This can be done by changing the value of <COMPONENT_ID> in metricPrefix: "Server|Component:<COMPONENT_ID>|Custom Metrics|Amazon RDS|".

For example,

```
metricPrefix: "Server|Component:100|Custom Metrics|Amazon RDS|"
```

More details around metric prefix can be found here .

Configure "awsAccessKey", "awsSecretKey" and "regions"". If you are running this extension inside an EC2 instance which has IAM profile configured then you don't have to configure these values, extension will use IAM profile to authenticate.

For example

```
#Add you list of AWS accounts here
accounts:
  - awsAccessKey: "XXXXXXX1"
    awsSecretKey: "XXXXXXX1"
    displayAccountName: "Test1"
    regions: ["us-east-1","us-west-1","us-west-2"]

  - awsAccessKey: "XXXXXXX2"
    awsSecretKey: "XXXXXXX2"
    displayAccountName: "Test2"
    regions: ["eu-central-1","eu-west-1"]
```

If you want to encrypt the "awsAccessKey" and "awsSecretKey" then follow the "Credentials Encryption" section and provide the encrypted values in "awsAccessKey" and "awsSecretKey". Configure "enableDecryption" of "credentialsDecryptionConfig" to true and provide the encryption key in "encryptionKey"

For example,

```
#Encryption key for Encrypted password.
credentialsDecryptionConfig:
    enableDecryption: "true"
    encryptionKey: "XXXXXXXX"
```

If you want to filer metrics based on DB identifier, please configure as below. Configuring .* will fetch metrics for all DBs for configured account and region.

```
dimensions:
   - name: "DBInstanceIdentifier"
     displayName: "DBInstanceIdentifier"
     values: ["blog*", "demodb"]
```

Configure the numberOfThreads

```
concurrencyConfig:
   noOfAccountThreads: 3
   noOfRegionThreadsPerAccount: 3
   noOfMetricThreadsPerRegion: 3
```

Configure the monitoring level as shown below. Allowed values are Basic and Detailed. Refer this for more information Basic will fire CloudWatch API calls every 5 minutes. Detailed will fire CloudWatch API calls every 1 minutes

```
cloudWatchMonitoring: "Basic"
```

Configure the metrics section.

For configuring the metrics, the following properties can be used:

For example,

```
- name: "CPUUtilization"
         alias: "CPUUtilization"
         statType: "ave"
         aggregationType: "OBSERVATION"
         timeRollUpType: "CURRENT"
         clusterRollUpType: "COLLECTIVE"
         delta: false
         multiplier: 1
```

All these metric properties are optional, and the default value shown in the table is applied to the metric(if a property has not been specified) by default.

## Metrics

Metrics provided by this extension are defined in the link given below:

RDS Metrics

## Credentials Encryption

Please visit this page to get detailed instructions on password encryption. The steps in this document will guide you through the whole process.

## Extensions Workbench

Workbench is an inbuilt feature provided with each extension in order to assist you to fine tune the extension setup before you actually deploy it on the controller. Please review the following document on How to use the Extensions WorkBench

## Troubleshooting

- Please make sure correct accessKey and secretKey are provided in config.yml.

- Please verify the correct regions have been configured

- Ensure that the required permissions have been given to the account being used with the extension.

- Please follow the steps listed in this troubleshooting-document in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.

## Contributing

Always feel free to fork and contribute any changes directly here on GitHub .

## Version

Note : While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to AppDynamics’ maintenance and support policy . Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.

How do you like this sample code?

| Property | Default value | Possible values | Description |
|---|---|---|---|
| alias | metric name | Any string | The substitute name to be used in the metric browser instead of metric name. |
| statType | "ave" | "AVERAGE", "SUM", "MIN", "MAX" | AWS configured values as returned by API |
| aggregationType | "AVERAGE" | "AVERAGE", "SUM", "OBSERVATION" | Aggregation qualifier |
| timeRollUpType | "AVERAGE" | "AVERAGE", "SUM", "CURRENT" | Time roll-up qualifier |
| clusterRollUpType | "INDIVIDUAL" | "INDIVIDUAL", "COLLECTIVE" | Cluster roll-up qualifier |
| multiplier | 1 | Any number | Value with which the metric needs to be multiplied. |
| convert | null | Any key value map | Set of key value pairs that indicates the value to which the metrics need to be transformed. eg: UP:0, DOWN:1 |
| delta | false | true, false | If enabled, gives the delta values of metrics instead of actual values. |

| Name | Version |
|---|---|
| Extension Version | 2.0.7 |
| Last Update | 19/05/2021 |
| Changes list | ChangeLog |