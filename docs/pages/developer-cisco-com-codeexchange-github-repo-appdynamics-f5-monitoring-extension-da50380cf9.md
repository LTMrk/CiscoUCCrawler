---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-f5-monitoring-extension-da50380cf9
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/f5-monitoring-extension
retrieved_at: 2026-08-21T06:01:39.417913+00:00
---

# F5 Monitoring Extension

## Use Case

The F5 load balancer from F5 Networks, Inc. directs traffic away from servers that are overloaded or down to other servers that can handle the load. The F5 load balancer extension collects key performance metrics from an F5 load balancer and presents them in the AppDynamics Metric Browser.

## Prerequisites

- Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met.

- Download and install Apache Maven which is configured with Java 8 to build the extension artifact from source. You can check the java version used in maven using command mvn -v or mvn --version . If your maven is using some other java version then please download java 8 for your platform and set JAVA_HOME parameter before starting maven.

- The extension collects the data from the REST API. Please make sure that the API is available and accessible. To access F5 REST API, user account must have admin level access. Try this URL from the Browser https://f5-host:f5-port/mgmt/tm/ltm/pool/stats or via curl.

- The extension needs to be able to connect to the F5 in order to collect and send metrics. To do this, you will have to either establish a remote connection in between the extension and the product, or have an agent on the same machine running the product in order for the extension to collect and send the metrics.

## Installation

- Run 'mvn clean install' from "F5MonitorRepo"

- Unzip the F5Monitor-<version>.zip from target directory into the "<MachineAgent_Dir>/monitors" directory.

- Edit the file config.yml located at <MachineAgent_Dir>/monitors/F5Monitor The metricPrefix of the extension has to be configured as specified here . Please make sure that the right metricPrefix is chosen based on your machine agent deployment, otherwise this could lead to metrics not being visible in the controller.

- All metrics to be reported are configured in metrics.xml. Users can remove entries from metrics.xml to stop the metric from reporting, or add new entries as well.

- Restart the Machine Agent.

Please place the extension in the "monitors" directory of your Machine Agent installation directory. Do not place the extension in the "extensions" directory of your Machine Agent installation directory. In the AppDynamics Metric Browser, look for Application Infrastructure Performance|<Tier>|Custom Metrics|F5 Monitor and you should be able to see all the metrics.

## Configuration

### Config.yml

Configure the extension by editing the config.yml file in <MACHINE_AGENT_HOME>/monitors/F5Monitor/ .

Configure the "COMPONENT_ID" under which the metrics need to be reported. This can be done by changing the value of <COMPONENT_ID> in metricPrefix: Server|Component:<COMPONENT_ID>|Custom Metrics|F5 Monitor| . For example,

```
metricPrefix: "Server|Component:100|Custom Metrics|F5 Monitor|"
```

Server Details

```
servers:
                  - uri: "https://server1:8443"
                    name: "Server1"
                    username: "user"
                    password: "password"
                    encryptedPassword: "" # put the password as empty when using encryptedPassword
        
                  - uri: "https://server2:443"
                    name: "server2"
                    username: "user"
                    password: ""
                    encryptedPassword: "y444543gt3="
```

If encryptedPassword is used, make sure to update the encryptionKey in config.yml . Please read the documentation here to generate encrypted password.

```
filter:
          pools:
            includes: [".*"]
          poolMembers:
            includes: [".*"]
          rules:
            includes: [".*"]
          ...
          ...
```

Please refer to the config.yml for the complete configuration.

#### Token Based Authentication (BIG IP 12+)

Token-based authentication can be used in BIG IP v12+. Please refer to F5 documentation for more details. To enabled token based auth, please modify the config.yml as shown below.

```
servers:
      - uri: "https://server1:8443"
        name: "Server1"
        username: "user"
        password: "password"
        encryptedPassword: ""
        authType: "TOKEN"
        loginReference: ""
```

- If you are using an external authentication provider, get the loginReference from your system administrator. It looks something like https://localhost/mgmt/cm/system/authn/providers/ldap/-id-/login

- If you are using local authentication (that is, there is no external authentication provider), then leave the loginReference blank

#### Using a Non Admin account (BI IP 11.6+)

This is applicable only for BIG IP versions 11.6+. To use a non-admin, you have to explicitly grant access to the rest interface. Please follow the steps.

Create a user with guest role from the F5 Admin UI.

Run the following command and get the selfLink of the guest user(created in step #1 ) from the response JSON

```
curl -i -k -u <adminuser>:<pwd> https://f5-ip/mgmt/shared/authz/users
```

Replace the link in the --data argument json with the value of selfLink from the response of step #2

```
curl -i -k -u <adminuser>:<pwd> --request PATCH \
    --data '{"userReferences":[{"link":"https://localhost/mgmt/shared/authz/users/guestuser"}]}' \
    https://f5-ip/mgmt/shared/authz/roles/iControl_REST_API_User
```

This should give access to the user created in step #1 to invoke the rest api to invoke GET. If the guest role doesn't work, try "manager" role in step#1

### Metrics.xml

You can add/remove metrics of your choice by modifying the provided metrics.xml file. This file consists of all the metrics that will be monitored and sent to the controller. Please look how the metrics have been defined and follow the same convention, when adding new metrics. You do have the ability to chosoe your Rollup types as well as set an alias that you would like to be displayed on the metric browser.

```
<metric attr="nestedStats|entries|activeMemberCnt" alias="Active Members" aggregationType = "AVERAGE" timeRollUpType = "AVERAGE" clusterRollUpType = "COLLECTIVE"/>
```

For configuring the metrics, the following properties can be used:

All these metric properties are optional, and the default value shown in the table is applied to the metric (if a property has not been specified) by default.

#### Metrics

The metrics will be reported under the tree Application Infrastructure Performance|$TIER|Custom Metrics|F5 Monitor|

## Credentials Encryption

Please visit this page to get detailed instructions on password encryption. The steps in this document will guide you through the whole process.

## Extensions Workbench

Workbench is an inbuilt feature provided with each extension in order to assist you to fine tune the extension setup before you actually deploy it on the controller. Please review the following document on How to use the Extensions WorkBench .

## Troubleshooting

- Please follow the steps listed in this troubleshooting-document in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.

- config.yml: Validate the file here

- F5 REST API: Please make sure that the F5 REST API is available and accessible. Try this URL from the Browser or via curl https://f5-host:f5-port/mgmt/tm/ltm/pool/stats

- Metric Limit: Please start the machine agent with the argument -Dappdynamics.agent.maxMetrics=5000 if there is a metric limit reached error in the logs. If you dont see the expected metrics, this could be the cause.

- Check Logs: There could be some obvious errors in the machine agent logs. Please take a look.

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
| convert | null | Any key value map | Set of key value pairs that indicates the value to which the metrics need to be transformed. eg: UP:1, OPEN:1 |
| delta | false | true, false | If enabled, gives the delta values of metrics instead of actual values. |

| Name | Version |
|---|---|
| Extension Version | 2.5.2 |
| Product Tested On | 15.0.0 |
| Last Update | 04/02/2021 |
| Changes list | ChangeLog |